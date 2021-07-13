using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using IronPython.Hosting;
using Microsoft.Scripting;
using Microsoft.Scripting.Hosting;
using System.Reflection;
using System.Threading;
using PyList = IronPython.Runtime.List;

namespace SwordsOfExileGame
{
    /*
     * References to pass TO script:
     *     PartyType Party : The current Party
     *     TownMap Town : The current Town
     *     OutsideSector OutsideArea : The current outside sector
     *     WorldMapType WorldMap : The world map
     * 
     *     eScriptCallOrigin ScriptCallOrigin : In what circumstance this script was triggered
     *     Location SpecialPos : The location of the special encounter spot that triggered this script
     *     PCType ScriptSelectPC : The PC that has just been selected in a ScriptSelect Window
     *     object DialogResult : What the user just selected in a message window
     *     PCType Caster : Who just cast a spell
     *     object Target : What the spell was cast on
     *     
     * Reference FROM the script that we'll need to read
     * 
     *     string TalkingText : When a talking node runs a script, this is set so the Conversation window can display it
     *     bool CancelMove : The script has decided to stop a planned PC from moving (for when ScriptCallOrigin == MOVING)
     *     bool CancelOutdoorEncounter : For when the party encounters a wandering group outside (old spec_on_meet)
     * 
     * */

    //One of these is passed to every latent script function
    public class ScriptParameters
    {
        //The scripts can READ these to know about the context the script was called.
        public eCallOrigin Origin;
        public PCType PC = null;
        public Location Target = Location.Zero;
        public Direction Dir = Direction.None;
        public List<Location> TargetList = null;
        public NPC NPCTarget = null;
        public List<NPC> NPCTargetList = null;
        public PCType PCTarget = null;
        public Pattern TargetPattern = null;
        public MagicSpell Spell = null;
        public Item UsedItem = null;
        public EncounterRecord NPCGroup = null;
        public SpecialItem SItem = null;
        public Dictionary<string, object> Vars = new Dictionary<string, object>();

        //The script sets these to control what happens when the script has finished
        public bool CancelAction = false;
        public string TalkingText = null;

        public ScriptParameters(eCallOrigin origin)
        {
            Origin = origin;
        }
    }

    class Script
    {
        static List<Script> ScriptQueue;
        public static GlobalVariables StuffDone;

        static public bool CancelOutdoorEncounter;
        static public string TalkingText;
        static public bool NeedAutoSave = false;

        Func<ScriptParameters, object> Func;
        ScriptParameters Params; 
        string funcName;

        //Script thread flags
        static bool scriptsbegun = false;
        static bool scriptsstopped = false;
        static bool scriptsfinished = false;
        static SemaphoreSlim _sem = new SemaphoreSlim(1);
        static bool latentScriptRunning = false; //Flag to prevent Wait() being called from script that isn't latent.

        //Python stuff
        static ScriptEngine scrEngine;
        static ScriptScope scrScope;
        static ScriptScope builtinScope;

        #region Latent Script Function Creators
        Script(eCallOrigin origin, string func) 
        {
            Params = new ScriptParameters(origin);
            try
            {
                Func = scrScope.GetVariable<Func<ScriptParameters, object>>(func);
            }
            catch (MissingMemberException e)
            {
                Game.FlagError("Script Error", "Function '" + func + "' not found.");
                return;
            }

            ScriptQueue.Add(this);
            funcName = func;
        }
        public Script(ScriptParameters p, string func)
        {
            funcName = func;
            Params = p;
            try
            {
                Func = scrScope.GetVariable<Func<ScriptParameters, object>>(func);
            }
            catch (MissingMemberException e)
            {
                Game.FlagError("Script Error", "Function '" + func + "' not found.");
                return;
            }
            ScriptQueue.Add(this);
        }

        /// <summary>
        /// This is for general latent scripts whose functions have no parameters besides Call Origin (eg, Talking)
        /// </summary>
        /// <param name="func">Function name in the script</param>
        /// <param name="origin">The origin type</param>
        public static void New_General(string func, eCallOrigin origin)
        {
            if (func == null || func == "") return;
            Script s = new Script(origin, func);
        }
        public static void New_Talking(string func, NPC npc)
        {
            if (func == null || func == "") return;
            Script s = new Script(eCallOrigin.TALKING, func);
            s.Params.NPCTarget = npc;
        }

        public static void New_ExitTown(string func, Direction dir)
        {
            Script s = new Script(eCallOrigin.LEAVING_TOWN, func);
            s.Params.Dir = dir;
        }

        public static void New_MapTrigger(string func, eCallOrigin origin, TriggerSpot spot, PCType pc, Location pos, Direction dir)
        {
            if (func == null || func == "") return;
            Script s = new Script(origin, func);
            s.Params.Target = pos;
            s.Params.Dir = dir;
            s.Params.PC = pc;
            if (spot != null) s.Params.Vars = spot.Vars;
        }

        public static void New_StoodOn(TriggerSpot tr, ICharacter ch)
        {
            if (tr.Func == null || tr.Func == "") return;
            if (ch is PCType)
            {
                Script s = new Script(eCallOrigin.PC_STOOD_ON, tr.Func);
                s.Params.PC = (PCType)ch;
                s.Params.Vars = tr.Vars;
            }
            else if (ch is NPC)
            {
                Script s = new Script(eCallOrigin.NPC_STOOD_ON, tr.Func);
                s.Params.NPCTarget = (NPC)ch;
                s.Params.Vars = tr.Vars;
            }
        }

        public static void New_KillNPC(string func, NPC npc, PCType pc) 
        {
            if (func == null || func == "") return;
            Script s = new Script(eCallOrigin.KILLED_NPC, func);
            s.Params.NPCTarget = npc;
            s.Params.PC = pc;
        }
        public static void New_NPCGroup(string func, eCallOrigin origin, EncounterRecord npcg)
        {
            if (func == null || func == "") return;
            Script s = new Script(origin, func);
            s.Params.NPCGroup = npcg;
        }

        public static void New_UseSpecialItem(string func, SpecialItem si)
        {
            if (func == null || func == "") return;
            Script s = new Script(eCallOrigin.USING_SPECIAL_ITEM, func);
            s.Params.SItem = si;
        }

        public static void New_CastSpell(string func, PCType caster_pc, Location target, List<Location> targetlist,
                        NPC npctarget, List<NPC> npctargetlist, PCType pctarget, Pattern targetpattern, MagicSpell spell, Item item)
        {
            if (func == null || func == "") return;
            Script s = new Script(item == null ? eCallOrigin.CAST_SPELL : eCallOrigin.CAST_ITEM_SPELL, func);

            s.Params.PC = caster_pc;
            s.Params.Target = target;
            s.Params.TargetList = targetlist;
            s.Params.NPCTarget = npctarget;
            s.Params.NPCTargetList = npctargetlist;
            s.Params.PCTarget = pctarget;
            s.Params.TargetPattern = targetpattern;
            s.Params.Spell = spell;
            s.Params.UsedItem = item;
        }

        /// <summary>
        /// This is caused when a map trigger is set to fire if a spell is cast on its location. It's script is run AFTER the general magic script for the spell
        /// </summary>
        /// <param name="caster"></param>
        /// <param name="trigger"></param>
        /// <param name="loc"></param>
        /// <param name="spell"></param>
        /// <param name="item"></param>
        public static void New_MapSpellTrigger(PCType caster, TriggerSpot trigger, Location loc, MagicSpell spell, Item item)
        {
            if (trigger.Func == null || trigger.Func == "") return;
            Script s = new Script(item == null ? eCallOrigin.CAST_SPELL : eCallOrigin.CAST_ITEM_SPELL, trigger.Func);
            s.Params.PC = caster;
            s.Params.Target = loc;
            s.Params.Spell = spell;
            s.Params.UsedItem = item;
        }
        #endregion

        void scriptThreadRoutine()
        {
            ResetInterfaceValues();
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);
            latentScriptRunning = true;

            _sem.Wait();
            scriptsbegun = true;

            try { Func(Params);}
            catch (Exception e)
            { FlagScriptError(e); }

            //Raise flag to tell the main thread we're ending.
            scriptsfinished = true;
            latentScriptRunning = false;
            _sem.Release();

        }

        public bool Run()
        {
            if (!scriptsstopped)
            {
                //Initiate the script thread and start it running.
                Thread h = new Thread(scriptThreadRoutine);
                h.Start();
                //Wait until the Script thread has locked the action.
                while (!scriptsbegun){}
                scriptsbegun = false; //This flag is no longer used and can now be reset ready for next time.
            }
            else
            {
                //Release the lock, the script thread can then take over.
                _sem.Release();

                //Wait until the script thread drops the flag the ensure the main thread doesn't put in a lock request before the script thread has a chance to.
                while (scriptsstopped) { }

            }

            //Wait until the script thread has signalled it has released the lock, then lock it ourselves
            _sem.Wait();

            //This might be because the script has finised, so exit.
            if (scriptsfinished)
            {
                _sem.Release();
                scriptsfinished = false; //This flag is no longer used and can now be reset ready for next time.
                Finish();
                return true;
            }
            //Otherwise the script thread has yielded, raise the flag to allow the script thread to put in a lock request.
            scriptsstopped = true;
            return false;
        }

        void Finish()
        {
            SpecialItemsWindow.Refresh();

            if (Game.PartyDead) return;

            //Don't do any end script actions until the last script in the queue that has this call origin has completed. This allows a script to call another script
            //and have that script decide whether to cancel the respective action (This is basically for looping node scripts)
            if (ScriptQueue.Count(n => n.Params.Origin == Params.Origin) > 1)
                return;

            //Script finished, complete any actions that the engine was waiting for the script's permission to do.
            if (Params.Origin == eCallOrigin.MOVING && !Params.CancelAction)
            {
                new Action(eAction.CompleteMove) { Dir = Params.Dir, Loc = Params.Target, PC = Params.PC };
            }
            else if (Params.Origin == eCallOrigin.BOATLAND && !Params.CancelAction)
            {
                new Action(eAction.BoatLanding) { Dir = Params.Dir, Loc = Params.Target, PC = Params.PC };
            }
            else if (Params.Origin == eCallOrigin.SEARCHING && !Params.CancelAction && Game.Mode != eMode.OUTSIDE)
            {
                Game.CurrentTown.CompleteSearch(Params.Target, true);
            }
            else if (Params.Origin == eCallOrigin.CAST_SPELL || Params.Origin == eCallOrigin.CAST_ITEM_SPELL)
            {
                if (!Params.CancelAction)
                {
                    new Action(Params.Origin == eCallOrigin.CAST_SPELL ? eAction.CompleteCastSpell : eAction.CompleteCastItemSpell)
                    {
                        Spell = Params.Spell,
                        PC = Params.PC,
                        Item = Params.Origin == eCallOrigin.CAST_SPELL ? null : Params.UsedItem
                    };
                }
            }
            else if (Params.Origin == eCallOrigin.OUTDOOR_ENCOUNTER)
                CancelOutdoorEncounter = Params.CancelAction;
            else if (Params.Origin == eCallOrigin.TALKING)
            {
                //If the script hasn't set the TalkingText, leave it as the default set in the Talking node
                if (Params.TalkingText != null) 
                    TalkingText = Params.TalkingText;
            }
            else if (Params.Origin == eCallOrigin.LEAVING_TOWN)
                new Animation_FadeDown(300);
            else if (Params.Origin == eCallOrigin.ENTERING_TOWN && ScriptQueue.Count <= 1)
                Game.AutoSave();
        }

        /// <summary>
        /// Loads and compiles the Python scripts for the scenario
        /// </summary>
        public static bool Initialise()
        {
            scrEngine = Python.CreateEngine();

            //Add all of the main engine's stuff to the script assembly so it can access it
            scrEngine.Runtime.LoadAssembly(Assembly.GetAssembly(typeof(SwordsOfExileGame.Location)));
            scrScope = scrEngine.CreateScope();

            //Execute just this little line of script that will let all the script files access the game's objects an ting.
            ScriptSource source = scrEngine.CreateScriptSourceFromString("from SwordsOfExileGame import *", SourceCodeKind.SingleStatement);
            CompiledCode comp = source.Compile();
            comp.Execute(scrScope);

            builtinScope = scrEngine.Runtime.GetBuiltinModule();

            //Remove Built In Python stuff to (hopefully) stop any malicious scripts.
            builtinScope.RemoveVariable("__import__");
            builtinScope.RemoveVariable("compile");
            builtinScope.RemoveVariable("dir");
            builtinScope.RemoveVariable("execfile");
            builtinScope.RemoveVariable("file");
            builtinScope.RemoveVariable("open");
            builtinScope.RemoveVariable("reload");

            //Make lists of every python script file in 'Base/Scripts' and '<scenario>/Scripts'
            var basescriptfiles = Directory.EnumerateFiles(Path.Combine(Game.BaseDirectory, "Scripts"), "*.py", SearchOption.TopDirectoryOnly).ToList();
            var scenscriptfiles = Directory.Exists(Path.Combine(Game.ScenarioDirectory, "Scripts")) 
                                    ? Directory.EnumerateFiles(Path.Combine(Game.ScenarioDirectory, "Scripts"), "*.py", SearchOption.TopDirectoryOnly).ToList()
                                    : new List<String>();

            //Make all filenames uppercase
            for (int n = 0; n < basescriptfiles.Count; n++)
                basescriptfiles[n] = basescriptfiles[n].ToUpper();
            for (int n = 0; n < scenscriptfiles.Count; n++)
                scenscriptfiles[n] = scenscriptfiles[n].ToUpper();

            //Exclude Base script files if there is a file of the same name in the scenario scripts
            basescriptfiles = basescriptfiles.Except(scenscriptfiles).ToList(); 

            foreach (string s in basescriptfiles)
            {
                source = scrEngine.CreateScriptSourceFromFile(Path.Combine(Game.BaseDirectory, "Scripts", s));//.CreateScriptSourceFromString(code, SourceCodeKind.Statements);
                try
                {
                    comp = source.Compile();
                }
                catch (SyntaxErrorException e)
                {
                    Game.FlagError("Script Syntax Error", e.Message, "File: " + Path.GetFileName(e.SourcePath) + " Line: " + e.Line + " Column: " + e.Column);
                    return false;
                }
                comp.Execute(scrScope);
            }

            foreach (string s in scenscriptfiles)
            {
                source = scrEngine.CreateScriptSourceFromFile(Path.Combine(Game.ScenarioDirectory, "Scripts", s));//.CreateScriptSourceFromString(code, SourceCodeKind.Statements);
                try
                {
                    comp = source.Compile();
                }
                catch (SyntaxErrorException e)
                {
                    Game.FlagError("Script Syntax Error", e.Message, "File: " + Path.GetFileName(e.SourcePath) + " Line: " + e.Line + " Column: " + e.Column);
                    return false;
                }
                comp.Execute(scrScope);
            }
            
            StuffDone = new GlobalVariables();
            scrScope.SetVariable("StuffDone", StuffDone);
            builtinScope.SetVariable("Wait", new System.Action(script_Wait));
            builtinScope.SetVariable("Message", new System.Action<string>(script_SmallMessage));
            builtinScope.SetVariable("MessageBox", new System.Action<string>(script_Message));
            builtinScope.SetVariable("ChoiceBox", new System.Func<string, eDialogPic, int, PyList, int>(script_Choice));
            builtinScope.SetVariable("SelectPCBox", new System.Func<string, bool, PCType>(script_SelectPC));
            builtinScope.SetVariable("InputTextBox", new System.Func<string, string, string>(script_InputText));
            builtinScope.SetVariable("InputNumberBox", new System.Func<string, int, int>(script_InputNumber));
            builtinScope.SetVariable("RunScript", new System.Func<string, ScriptParameters, bool>(script_RunScript));
            builtinScope.SetVariable("OpenShop", new System.Action<string>(script_OpenShop));
            builtinScope.SetVariable("OpenHealingShop", new System.Action<int>(script_OpenHealingShop));
            builtinScope.SetVariable("OpenTrainingShop", new System.Action(script_OpenTrainingShop));
            builtinScope.SetVariable("OpenIdentifyShop", new System.Action<string, int>(script_OpenIdentifyShop));
            builtinScope.SetVariable("OpenEnchantShop", new System.Action<string, eEnchantShop>(script_OpenEnchantShop));
            builtinScope.SetVariable("CentreView", new System.Action<Location, bool>(script_CentreView));
            builtinScope.SetVariable("SuspendMapUpdate", new System.Action(script_SuspendMapUpdate));
            builtinScope.SetVariable("ResumeMapUpdate", new System.Action(script_ResumeMapUpdate));

            ScriptQueue = new List<Script>();
            return true;
        }

        public static void PreventAction()
        {
            if (ScriptQueue.Count > 0)
                ScriptQueue[0].Params.CancelAction = true;   
        }

        public static void CleanUp()
        {
            if (scrEngine != null)
            {
                if (ScriptQueue != null) ScriptQueue.Clear();
                scrEngine.Runtime.Shutdown();
                scrEngine = null;
                scrScope = null;
                builtinScope = null;
            }
        }

        public static Func<IEnumerable<object>> GetFunc(string f)
        {
            if (f == null || f == "") return null;
            return scrScope.GetVariable<Func<IEnumerable<object>>>(f);
        }

        /// <summary>
        /// Whether there are scripts running or waiting to run.
        /// </summary>
        public static bool IsRunning
        {
            get { return (ScriptQueue.Count > 0); }
        }

        public static string FunctionRunning()
        {
            if (ScriptQueue.Count > 0)
                return ScriptQueue[0].funcName;
            return "";
        }

        /// <summary>
        /// Executes any script threads waiting in the queue.
        /// </summary>
        /// <returns>True if the script thread queue is now empty after this and all scripts have finished executing. False if still needs running</returns>
        public static bool RunNext()
        {
            if (ScriptQueue.Count == 0) return true;
            Script thread = ScriptQueue[0];

            if (thread.Run())
            {
                ScriptQueue.Remove(thread);
                if (ScriptQueue.Count == 0) return true;
            }

            return false;
        }

        #region Non-Latent Script Functions

        public static void RunConsoleScript(string s)
        {
            if (s == null || s == "") return;

            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);

            try
            {
                scrEngine.Execute(s, scrScope);
            }
            catch (Exception e)
            {
                Game.AddMessage(e.Message);
                return;
            }
            Game.AddMessage("Command executed successfully.");
        }

        public static int RunTargetCount(string func, PCType pc, MagicSpell spell, Item item)
        {
            var f = scrScope.GetVariable<Func<PCType, MagicSpell, Item, int>>(func);
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);
            try { return f(pc,spell,item); }
            catch (Exception e) { FlagScriptError(e); return 1; }

        }
        public static bool RunNonLatentFuncBool(string func)
        {
            Func<bool> f;

            try
            {
                f = scrScope.GetVariable<Func<bool>>(func);
            }
            catch(Exception e)
            {
                Game.FlagError("Finding Script Function", e.Message, func);
                return false;
            }
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);

            try { return f(); }
            catch(Exception e)
            {
                FlagScriptError(e); 
                return false;
            }
        }

        public static bool RunNPCMove(string func, NPC npc)
        {
            Func<NPC, bool> f = scrScope.GetVariable<Func<NPC, bool>>(func);
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);
            try { return f(npc); }
            catch (Exception e) { FlagScriptError(e); return false; }
        }
        public static TownMap RunTownPreEntry(string func, TownMap town)
        {
            if (func == null || func == "") return town;
            Func<TownMap, TownMap> f = scrScope.GetVariable<Func<TownMap, TownMap>>(func);
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);
            try { return f(town); }
            catch (Exception e) { FlagScriptError(e); return town; }
        }

        public static bool RunShopRestock(string func, Shop shop)
        {
            if (func == null || func == "") return false;
            Func<Shop, bool> f = scrScope.GetVariable<Func<Shop, bool>>(func);
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);
            try { return f(shop); }
            catch (Exception e) { FlagScriptError(e); return false; }
        }

        public static bool RunGenerateMap(string func, TownMap town, EncounterRecord encounter, TerrainRecord[,] underterrain, TerrainRecord[,] overterrain)
        {
            if (func == null || func == "") return false;

            var f = scrScope.GetVariable<Func<TownMap, EncounterRecord, TerrainRecord[,], TerrainRecord[,], bool>>(func);
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);

            try { return f(town, encounter, underterrain, overterrain); }
            catch (Exception e) {FlagScriptError(e);return false;}

        }

        public static bool RunAlchemy(PCType pc, Recipe recipe)
        {
            var f = scrScope.GetVariable<Func<PCType, Recipe, bool>>("DoAlchemy");
            builtinScope.SetVariable("Party", Game.CurrentParty);
            builtinScope.SetVariable("Town", Game.CurrentTown);
            builtinScope.SetVariable("WorldMap", Game.WorldMap);

            try { return f(pc, recipe); }
            catch (Exception e) { FlagScriptError(e); return false; }
        }

        #endregion

        static void FlagScriptError(Exception e)
        {
            ExceptionOperations eo = scrEngine.GetService<ExceptionOperations>();
            string error = eo.FormatException(e);
            Game.FlagError("Script Runtime Error", error);
        }


#region Script accessible routines
        static void script_Wait()
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.

            //Release our lock so the main thread's request can take over.
            _sem.Release();

            //Wait until the main thread raises the flag, to ensure the script thread doesn't put in a lock request before the main thread has taken over.
            while (!scriptsstopped) { }
            _sem.Wait();

            //Drop flag to allow the main thread to put in a lock request now.
            scriptsstopped = false;
        }
        static void script_SmallMessage(string s)
        {
            Game.AddMessage(s);
        }

        static void script_Message(string s)
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.
            new MessageWindow(defaultHandler, s, eDialogPic.NONE, 0, "OK");
            script_Wait();
        }

        static int script_Choice(string s, eDialogPic pictype, int picnum, PyList buttons)
        {
            if (!latentScriptRunning) return -1; //Nothing happens if script is non-latent.
            Result = -1;

            string[] b_array = new string[buttons.Count];

            int n = 0;
            foreach (string b in buttons)
            {
                b_array[n++] = b;
            }
            new MessageWindow(defaultHandler, s, pictype, picnum, b_array);
            script_Wait();
            return Result;
        }

        static PCType script_SelectPC(string s, bool only_living = true)
        {
            if (!latentScriptRunning) return null; //Nothing happens if script is non-latent.
            SelectedPC = null;
            new SelectPCWindow(defaultPCHandler, s, only_living);
            script_Wait();
            return SelectedPC;
        }

        static string script_InputText(string msg, string def)
        {
            if (!latentScriptRunning) return ""; //Nothing happens if script is non-latent.
            TextResult = "";
            new InputTextWindow(defaultTextHandler, msg, def, false);
            script_Wait();
            return TextResult;
        }
        static int script_InputNumber(string msg, int def)
        {
            if (!latentScriptRunning) return -1; //Nothing happens if script is non-latent.
            Result = -1;
            new InputTextWindow(defaultNumberHandler, msg, Convert.ToString(def), true);
            script_Wait();
            return Result;
        }

        static bool script_RunScript(string func, ScriptParameters s)//, Location pos)
        {
            if (!latentScriptRunning) return false; //Nothing happens if script is non-latent.
            if (func == null || func == "") return false;
            if (s == null) return false;
            new Script(s, func);
            return true;
        }

        static void script_OpenShop(string id)
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.
            if (Shop.List.Contains(id))
            {
                Shop.List[id].Run();
                script_Wait();
            }
        }

        static void script_OpenHealingShop(int pricelevel)
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.
            new HealerShopWindow(null, pricelevel);
            script_Wait();
        }
        static void script_OpenTrainingShop()
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.
            new TrainerWindow(null);
            script_Wait();
        }
        static void script_OpenIdentifyShop(string shopname, int price)
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.
            new IdentifyWindow(null, shopname, price);
            script_Wait();
        }
        static void script_OpenEnchantShop(string shopname, eEnchantShop enchant_type)
        {
            if (!latentScriptRunning) return; //Nothing happens if script is non-latent.
            new EnchantingWindow(null, shopname, enchant_type);
            script_Wait();
        }
        static void script_CentreView(Location l, bool instant)
        {
            Gfx.CentreView(l, instant);
        }
        static void script_SuspendMapUpdate()
        {
            suspendMapUpdate = true;
        }
        static void script_ResumeMapUpdate()
        {
            suspendMapUpdate = false;
            if (Game.CurrentMap is TownMap) Game.CurrentTown.GenerateLightMap();
            Game.CurrentMap.UpdateVisible();
        }

        static void defaultTextHandler(string s)
        {
            TextResult = s;
        }
        static void defaultNumberHandler(string s)
        {
            Result = Convert.ToInt32(s);
        }
        static void defaultHandler(int button_index)
        {
            Result = button_index;
        }
        static void defaultPCHandler(PCType pc)
        {
            SelectedPC = pc;
        }
#endregion

        //SCRIPT READABLE VALUES
        static int Result;
        static string TextResult;
        static PCType SelectedPC = null;

        //A script may set this when making a lot of changes to the map, to halt updating visibility updates until finished.
        //It is up to the script to switch this off again!
        public static bool suspendMapUpdate = false;

        //SCRIPT WRITEABLE VALUES

        //This one is public but it's not to be called by the script itself! It's called the first time a script function executes
        static void ResetInterfaceValues()
        {
            Result = -1;
            SelectedPC = null;
        }
    }
}
