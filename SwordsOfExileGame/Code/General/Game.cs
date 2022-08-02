using System;
using System.Collections.Generic;
using System.IO;
using System.Xml;
using System.Xml.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Input;


using System.Threading;

namespace SwordsOfExileGame
{
    /// <summary>
    /// This is the main type for your game
    /// </summary>
    public partial class Game : Microsoft.Xna.Framework.Game
    {
        public static Game Instance;
        public static void FlagError(string type, string msg, string location=null)
        {
            if (!ErrorFlagged)
            {
                ErrorFlagged = true;
                errorType = type;
                errorMessage = msg + (location == null ? "" : ("\n@bLocation:@e " + location));
            }
        }
        public static bool ErrorFlagged = false;
        static string errorType, errorMessage;
        public static bool Quit = false;

        //Loading status flags.
        static bool loadingComplete = false, loadingStartNew = false;
        public static bool Loading = false;

        public static string RootDirectory; //The root directory for the game
        public static string BaseDirectory, ScenarioDirectory, SavesDirectory; //The directory for the 'Base' data.

        public static bool InMainMenu = true;
        
        //Should be set to the designated placeholder entries in the enum. Eg, Set to INVENTORY_LOCKED_ACTIONS, when a Loot Window or Shop window is open, to stop any actions except inventory ones
        public static bool PartyDead = false, GameOver = false;

        public static PartyType CurrentParty;
        public static IMap CurrentMap;
        public static TownMap CurrentTown { get { return CurrentMap as TownMap; } }
        public static WorldMapType WorldMap;
        public static List<TownMap> RecentTownList;
        public static eMode Mode { get { return mode;}
            set
            {
                mode = value;
                if (menuBarWindow != null) menuBarWindow.Update();
            }
        }
        static eMode mode = eMode.TOWN;

        //Cheats / Testing
        public static bool DebugLoad = false; //Sets to true when press '`' at the same time as load button. Resets original scenario terrain on load.
        public static bool Invincible = false, //PCs can't be harmed
                           OneHitKill = false, //One hit kills enemies
                           PassiveNPCs = false, //Enemies don't attack anyone or use any abilities
                           NPCsIgnorePCs = false,
                           PCsAlwaysHit = false,
                           NPCGroupsFlee = false;

        public static bool DebugMode 
        { 
            get { return Invincible && OneHitKill && PCsAlwaysHit && NPCGroupsFlee; } 
            set 
            { 
                Invincible = OneHitKill = PCsAlwaysHit = NPCGroupsFlee = value;
                if (!value)
                    AddMessage("Debug Mode Deactivated.");
                else
                    AddMessage("Debug Mode Activated:\n  Invincible PCs\n  PCs always hit\n  PCs kill on one hit\n  Outside NPC Groups flee");
            } 
        }

        public static int AnimTicks = 0;
        static int tickSpeed = 250, nextTick = 0;
        public static eTurn Turn { get { if (gameState == eState.BEGIN_PC_TURN || gameState == eState.PICK_NEXT_PC || gameState == eState.PC_TURN_PROCESS_ACTION || gameState == eState.TARGET_MODE) return eTurn.PLAYER; else return eTurn.NPCS; } }//= eTurn.PLAYER;
        static bool turnBegin;

        public static bool PlayerTargeting { get { return gameState == eState.TARGET_MODE; } }

        static List<PortraitWindow> portraitWindows;
        static InventoryWindow inventoryWindow;
        static StatsWindow statsWindow;
        static InfoListWindow messageWindow;
        static MenuBarWindow menuBarWindow;

        static eState gameState = eState.BEGIN_PC_TURN;

        public Game()
        {
            Instance = this;
#if DEBUG
            Directory.SetCurrentDirectory(@"..\..\..\..");
#else
            Directory.SetCurrentDirectory(Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location));
#endif
            RootDirectory = Directory.GetCurrentDirectory();
            BaseDirectory = Path.Combine(RootDirectory, "Base");
            SavesDirectory = Path.Combine(RootDirectory, "Saves");
            Gfx.Initialise(this);
        }

        protected override void Initialize()
        {
            for (int n = 0; n < 30; n++)
                KeyHandler.KeyMap[n] = KeyHandler.Default1KeyMap[n];
            LoadSettings();
            base.Initialize();
        }

        protected override void LoadContent()
        {
            //Load graphics and sounds from the 'Data' directory, which may be added to or overridden when a scenario is loaded
            Gfx.Load(GraphicsDevice, true);
            Sound.Load(true);
            StartMenuWindow.Begin();
        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// all content.
        /// </summary>
        protected override void UnloadContent()
        {
            Script.CleanUp();
        }

        protected override void Update(GameTime gameTime)
        {
            // Allows the game to exit
            if (Quit) this.Exit();

            nextTick += gameTime.ElapsedGameTime.Milliseconds;
            if (nextTick >= tickSpeed)
            {
                nextTick = 0;
                AnimTicks = ++AnimTicks % 4;
            }
            Sound.Refresh();

            KeyHandler.GetKeysHit(gameTime.ElapsedGameTime.Milliseconds);
            
            Gui.Handle();
            Gui.HandleToolTip();

            if (ErrorFlagged) { 
                Gui.ErrorReport(errorType, errorMessage);
                return;
            }

            //If the game is loading (in a separately running thread) don't do anything else until it finishes.
            if (Loading)
            {
                if (loadingComplete/* && !DrawCalled*/) BeginGame();
                else if (InMainMenu) StartupMap.Update(gameTime);
                return;
            }

            if (InMainMenu)
            {
                StartupMap.Update(gameTime);
                return;
            }

            if (!Gui.WorldModalPaused)
            {
                Gfx.DoMapScroll(gameTime.ElapsedGameTime.Milliseconds);
                Gfx.DoMapZoom(gameTime.ElapsedGameTime.Milliseconds);
                KeyHandler.GetActionKeys();

                //1st priority: If there are any animations in the queue, update them now.
                if (!Animation.NoAnimationsRunning())
                {
                    Animation.AdvanceAll(gameTime.ElapsedGameTime.Milliseconds);

                    //if (!Animation.OnlyMovingAnimationsRunning()) Action.Requested = eAction.NONE;
                }
                //2nd priority: If there are any scripts in the queue, run them now.
                else if (Script.IsRunning && gameState != eState.GAME_OVER)
                {
                    Script.RunNext();
                }
                else
                {
                //Now the main state machine
                    bool immediate_state_switch;

                    do
                    {
                        //This is set to true in each state to allow switching to the next state without updating animations/scripts/user input
                        immediate_state_switch = false;

                        //Now handle the main game state
                        switch (gameState)
                        {
                            //Set the PCs action points for the turn
                            case eState.BEGIN_PC_TURN:
                                CurrentParty.StartNewTurn();
                                gameState = eState.PICK_NEXT_PC;
                                immediate_state_switch = true;
                                break;

                            //Choose the PC to control based on who has action points left.
                            case eState.PICK_NEXT_PC:
                                if (CurrentParty.PickNextPC())
                                {
                                    //No PC has action points left, so make it the NPCs go. (This is only reached in combat mode - in town mode the state switches to NPCs after every player action)
                                    gameState = eState.BEGIN_NPC_TURN;
                                }
                                else
                                {
                                    Gfx.CentreView(CurrentParty.ActivePC.Pos, false); 
                                    gameState = eState.PC_TURN_PROCESS_ACTION;
                                    if (!Script.IsRunning && Animation.NoAnimationsRunning()) immediate_state_switch = true; 
                                }
                                break;

                            //The main state for handling the player's actions
                            case eState.PC_TURN_PROCESS_ACTION:

                                if (GameOver) { gameState = eState.END_TURN; immediate_state_switch = true; break; }

                                gameState = Action.Handle();//eState.BEGIN_NPC_TURN;

                                if (PartyDead) { gameState = eState.PARTY_DEAD; immediate_state_switch = true; break; }

                                if ((gameState == eState.BEGIN_NPC_TURN || gameState == eState.PICK_NEXT_PC) &&
                                    !Script.IsRunning && (
                                    (Game.Mode != eMode.COMBAT && Animation.OnlyMovingAnimationsRunning()) ||
                                    Game.Mode == eMode.COMBAT && Animation.NoAnimationsRunning()))
                                    immediate_state_switch = true;

                                break;

                            //Handle player's actions in Target Mode (when needing to choose a target npc/tile on the map)
                            case eState.TARGET_MODE:

                                if (Action.HandleTargeting())
                                {
                                    gameState = eState.PC_TURN_PROCESS_ACTION;
                                    immediate_state_switch = true;
                                }
                                break;

                            //Assign action points to NPCs for the turn, activate new NPCs
                            case eState.BEGIN_NPC_TURN:

                                CurrentMap.StartNPCTurn();
                                gameState = eState.NPC_TURN;
                                if (!Script.IsRunning && Animation.NoAnimationsRunning()) immediate_state_switch = true; 
                                break;

                            //Move each NPC.
                            case eState.NPC_TURN:
                                if (CurrentMap.DoNPCTurn()) //Returns true when the last NPC has acted.
                                {
                                    gameState = eState.END_TURN;
                                    if (!Script.IsRunning && Animation.NoAnimationsRunning()) immediate_state_switch = true; 
                                }
                                break;

                            //Handle various checks and stuff at the end of each turn.
                            case eState.END_TURN:

                                //The PCs are dead. End the game
                                if (PartyDead)
                                {
                                    immediate_state_switch = true; 
                                    gameState = eState.PARTY_DEAD;
                                }
                                else if (GameOver)
                                {
                                    new Animation_FadeDown(1000);
                                    gameState = eState.GAME_OVER;                                    
                                }
                                //Check: PCs leave town.
                                else if (Mode == eMode.TOWN && !CurrentTown.InActArea(CurrentParty.Pos))
                                {
                                    //Set up any scripts to run on leaving the town
                                    CurrentTown.SetUpExitFunc();
                                    gameState = eState.BEGIN_LEAVE_MAP;
                                }
                                //Check: PCs step on town in world map.
                                else if (Mode == eMode.OUTSIDE && WorldMap.TownEntranceHere(CurrentParty.Pos) != null)
                                {
                                    TownMap t = WorldMap.TownEntranceHere(CurrentParty.Pos).DestTown;
                                    if (t.LightType > 0) Sound.Play("095_enterdungeon");
                                    else Sound.Play("016_townentry");
                                    new Animation_FadeDown(300);
                                    gameState = eState.BEGIN_ENTER_TOWN;
                                }
                                //Check: Outside NPCs want to attack
                                else if (Mode == eMode.OUTSIDE && WorldMap.PCAttacker != null) //A wandering NPC group is next to the party and wants to attack!
                                {
                                    gameState = eState.BEGIN_NPC_GROUP_ATTACK;
                                }
                                //Check: All PCs flee combat map
                                else if (Mode == eMode.COMBAT && CurrentTown is CombatMap && CurrentParty.PartyFled())
                                {
                                    //The entire party has run away from combat. Put back on world map.
                                    new Animation_FadeDown(300);
                                    Script.New_NPCGroup(((CombatMap)CurrentMap).NPCGroup.FuncOnFlee, eCallOrigin.FLEE_ENCOUNTER, ((CombatMap)CurrentMap).NPCGroup);
                                    gameState = eState.BEGIN_PARTY_FLEE;
                                }
                                else
                                {
                                    //Handle status effects, Timer events, light levels, fields.
                                    CurrentParty.IncreaseAge();
                                    if (PartyDead) { gameState = eState.PARTY_DEAD; immediate_state_switch = true; break; }

                                    //Handle map squares with 'stood on' triggers
                                    CurrentMap.DoStoodOnTriggers();
                                    if (PartyDead) { gameState = eState.PARTY_DEAD; immediate_state_switch = true; break; }

                                    gameState = eState.BEGIN_PC_TURN;
                                    if (!Script.IsRunning && Animation.NoAnimationsRunning()) immediate_state_switch = true;
                                }
                                break;

                            case eState.BEGIN_LEAVE_MAP:
                                new Animation_FadeDown(300);
                                gameState = eState.LEAVE_MAP;
                                break;

                            case eState.LEAVE_MAP:
                                CurrentParty.OutsidePos += CurrentTown.GetDepartDirection(CurrentParty.Pos);
                                CurrentParty.Pos = CurrentParty.OutsidePos;
                                CurrentParty.MoveToMap(WorldMap);
                                gameState = eState.BEGIN_PC_TURN;
                                break;

                            case eState.BEGIN_ENTER_TOWN:

                                TownMap town = WorldMap.TownEntranceHere(CurrentParty.Pos).DestTown;
                                CurrentParty.OutsidePos = CurrentParty.Pos;
                                Mode = eMode.TOWN;
                                switch (CurrentParty.Direction.Dir)
                                {
                                    case eDir.S: CurrentParty.Pos = town.EnterPos[0]; break;
                                    case eDir.SE:
                                    case eDir.E:
                                    case eDir.NE: CurrentParty.Pos = town.EnterPos[3]; break;
                                    case eDir.N: CurrentParty.Pos = town.EnterPos[2]; break;
                                    case eDir.NW:
                                    case eDir.W:
                                    case eDir.SW: CurrentParty.Pos = town.EnterPos[1]; break;
                                }
                                CurrentParty.MoveToMap(town);
                                gameState = eState.BEGIN_PC_TURN;
                                break;

                            case eState.BEGIN_PARTY_FLEE:

                                foreach (PCType pc in CurrentParty.PCList)
                                {
                                    if (pc.LifeStatus == eLifeStatus.FLED) pc.LifeStatus = eLifeStatus.ALIVE;
                                }
                                CurrentParty.Pos = CurrentParty.OutsidePos;
                                CurrentParty.MoveToMap(WorldMap);
                                //Reset things
                                Mode = eMode.OUTSIDE;
                                turnBegin = true;
                                Gfx.CentreView(CurrentParty.Pos, true);
                                gameState = eState.BEGIN_PC_TURN;
                                break;

                            case eState.BEGIN_NPC_GROUP_ATTACK:
                                if (!WorldMap.NPCGroupList.Contains(WorldMap.PCAttacker))
                                {
                                    WorldMap.PCAttacker = null; //Attacker chose to flee!
                                    gameState = eState.END_TURN;
                                }
                                else
                                {
                                    bool cancelled;
                                    if (!WorldMap.PCAttacker.DoMeetingScript(out cancelled))
                                    {
                                        new Animation_FadeDown(300);
                                        gameState = eState.NPC_GROUP_ATTACK;
                                        break;
                                    }
                                    if (cancelled)
                                    {
                                        WorldMap.NPCGroupList.Remove(WorldMap.PCAttacker);
                                        WorldMap.PCAttacker = null;
                                        gameState = eState.END_TURN;
                                    }
                                }
                                break;

                            case eState.NPC_GROUP_ATTACK:

                                //Change to combat map!
                                initiateOutdoorCombat(WorldMap.PCAttacker.Record);
                                new Animation_FadeUp(300);

                                //Also, delete this outdoor wandering group now.
                                WorldMap.NPCGroupList.Remove(WorldMap.PCAttacker);
                                gameState = eState.BEGIN_PC_TURN;

                                break;

                            case eState.COMBAT_END:
                                if (CurrentTown is CombatMap) //We've finished fighting on a combat map, back to world map.
                                {
                                    foreach (PCType pc in CurrentParty.PCList)
                                        if (pc.LifeStatus == eLifeStatus.FLED) pc.LifeStatus = eLifeStatus.ALIVE;
                                    gameState = eState.BEGIN_PC_TURN;
                                    CurrentParty.Pos = CurrentParty.OutsidePos;
                                    CurrentParty.MoveToMap(WorldMap);
                                    Mode = eMode.OUTSIDE;

                                }
                                else
                                {
                                    gameState = eState.BEGIN_NPC_TURN;
                                    Mode = eMode.TOWN;
                                }
                                break;

                            case eState.DO_CAMPING:
                                CurrentParty.DoRest();
                                new Animation_FadeUp(300);
                                gameState = eState.BEGIN_PC_TURN;
                                break;

                            case eState.PARTY_DEAD:
                                if (CurrentParty.IsSplit) //Unless just the solo PC in split mode is.
                                {
                                    //If the solo PC in a split party dies, the game is not over, the rest of the PCs take over.
                                    PartyDead = false;
                                    CurrentParty.Reunite();
                                    if (Game.Mode == eMode.COMBAT) { Game.EndCombat(true); gameState = eState.COMBAT_END; }
                                    else
                                    {
                                        CurrentParty.IncreaseAge();
                                        gameState = eState.BEGIN_PC_TURN;
                                    }
                                }
                                else
                                {
                                    Sound.Play("013_partydeath");
                                    new Animation_FadeDown(1000);
                                    gameState = eState.GAME_OVER;
                                }
                                break;

                            case eState.GAME_OVER:
                                if (PartyDead)
                                {
                                    Gui.GuiWindows.Clear();
                                    new GameOverWindow();
                                }
                                else
                                {
                                    GameOver = false;
                                    foreach (PCType pc2 in CurrentParty.PCList)
                                    {
                                        if (pc2.LifeStatus == eLifeStatus.ABSENT) pc2.LifeStatus = eLifeStatus.ALIVE;
                                    }
                                    CurrentParty.IsSplit = false;
                                    CurrentParty.Restore();
                                    CurrentParty.StripItems(); //Remove items that can't be taken from the scenario.
                                    new LoadGameWindow(false, true, true, doAfterWin);
                                }
                                break;
                        }

                    //If we don't want to give a chance to animations or scripts to run before changing state, this should be set.
                    } while (immediate_state_switch);
                }
            }
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            Gfx.Draw();
        }

        public static void doLoadSave(int option, string filename)
        {
            if (option == LoadGameWindow.LOAD)
            {
                SaveInfo i = Game.LoadSaveInfo(filename, false);
                if (i != null)
                {
                    Scenario.Filename = Path.GetFileNameWithoutExtension(i.ScenFile);
                    Game.ScenarioDirectory = Path.Combine(Game.RootDirectory, "Scenarios", Scenario.Filename);
                    Game.LastSaveFile = filename;
                    Game.BeginLoadingThread(false);
                }
            }
            else if (option == LoadGameWindow.SAVE)
            {
                SaveGame(filename, false);
            }
        }

        public static void DoNPCsTurn()
        {
            if ((Game.Mode != eMode.COMBAT && Animation.OnlyMovingAnimationsRunning()) ||
                 Game.Mode == eMode.COMBAT && Animation.NoAnimationsRunning())
            {
                if (turnBegin == true)
                {
                    //This sets up the NPCs, but also does the 1 tile move of all NPCs simultaneously in Non-Combat mode.
                    CurrentMap.StartNPCTurn();
                    turnBegin = false;
                }
                else if (Game.Mode == eMode.OUTSIDE && WorldMap.PCAttacker != null) //A wandering NPC group is next to the party and wants to attack!
                {
                    if (Animation.NoAnimationsRunning()) //Wait for attacking animation to finish.
                    {
                        if (!WorldMap.NPCGroupList.Contains(WorldMap.PCAttacker))
                            WorldMap.PCAttacker = null; //Attacker chose to flee!
                        else
                        {
                            bool cancelled;
                            if (!WorldMap.PCAttacker.DoMeetingScript(out cancelled))
                            {
                                if (Gfx.FadeMode == 0)
                                    //Gfx.StartFade(300, false);
                                    new Animation_FadeDown(300);
                                else
                                {
                                    //Change to combat map!
                                    initiateOutdoorCombat(WorldMap.PCAttacker.Record);
                                    new Animation_FadeUp(300);

                                    //Also, delete this outdoor wandering group now.
                                    WorldMap.NPCGroupList.Remove(WorldMap.PCAttacker);
                                }
                            }
                            if (cancelled)
                            {
                                WorldMap.NPCGroupList.Remove(WorldMap.PCAttacker);
                                WorldMap.PCAttacker = null;
                                return;
                            }
                        }
                    }
                }
                else if (CurrentMap.DoNPCTurn())
                {
                    turnBegin = true;
                }
            }
        }

        static void LoadingThread()
        {
            if (loadingStartNew)
            {
                if (!Scenario.Load()) return ;
                if (!Script.Initialise()) return;
            }
            else
            {
                if (!LoadGame()) return;
            }

            DebugLoad = false; //This can be turned off now, if it was ever on.

            foreach (PCType pc in CurrentParty.PCList)
                pc.SetupKnownSpells();

            CurrentParty.SetUpKnownRecipes();

            Thread.Sleep(1000);
            LoadingWindow.Terminate();  
            loadingComplete = true;
        }

        //Gets ready to load the game, or start a new scenario.
        //If start_new is true, the filename saved in Scenario will be the scenario loaded.
        //and the current Party is presumed already loaded/created.
        //For loading a game, the save file to load should be in in Game.LastSaveFile
        public static void BeginLoadingThread(bool start_new)
        {
            Gui.GuiWindows.Clear();

            new LoadingWindow();

            loadingStartNew = start_new;
            Loading = true;
            loadingComplete = false;

            Gfx.FadeMode = 3;
            Gfx.FadeColor = Color.Black;
            Thread t = new Thread(LoadingThread);
            t.Start();
        }

        public static void BeginGame()
        {
            PartyDead = false;

            Gfx.Load(null, false); //We don't do this during the loading thread because it wigs out with the Texture Loader

            if (loadingStartNew)
            {
                CurrentMap = Scenario.StartTown;
                CurrentParty.Pos = Scenario.TownStartPos;
                CurrentParty.Age = 0;

                Location op = new Location(Scenario.StartOutside.SectorPos.X * Constants.SECTOR_WIDTH, Scenario.StartOutside.SectorPos.Y * Constants.SECTOR_HEIGHT);
                CurrentParty.OutsidePos = op + Scenario.OutsideStartPos;

                if (Scenario.InitialiseFunc != null && Scenario.InitialiseFunc != "") Script.RunNonLatentFuncBool(Scenario.InitialiseFunc);

                CurrentParty.MoveToMap(CurrentMap);
                Shop.RestockAll(-1);
                SetUpGameWindows();
                Script.New_General(Scenario.IntroFunc, eCallOrigin.START_SCENARIO);
                Game.AddMessage("Welcome to '" + Scenario.Name + "'");
            }
            else
            {
                Gfx.MakeCharacterHighlight(CurrentParty.ActivePC);
                Gfx.CentreView(CurrentParty.Pos, true);
                Game.CurrentMap.UpdateVisible();
                SetUpGameWindows();;
                Game.AddMessage("Saved game loaded.");
            }

            Gui.WorldModalPaused = false;
            Action.LockActions = eAction.BLOCKABLE_ACTIONS;
            Loading = false;
            StartupMap.End();
            InMainMenu = false;
            turnBegin = true;
            gameState = eState.BEGIN_PC_TURN;
            Animation.CancelAll();
            new Animation_FadeUp(1000);
        }

        static void SetUpGameWindows()
        {
            Gui.GuiWindows.Clear();
            portraitWindows = new List<PortraitWindow>();
            foreach (PCType pc in CurrentParty.PCList)
            {
                portraitWindows.Add(new PortraitWindow(pc, portraitWindows.Count));
            }
            SetPortraitWindowKeys();

            inventoryWindow = new InventoryWindow();
            statsWindow = new StatsWindow();
            messageWindow = new InfoListWindow();
            menuBarWindow = new MenuBarWindow();
        }

        static void initiateOutdoorCombat(EncounterRecord group)
        {
            Mode = eMode.COMBAT;
            CurrentParty.ActivePC = CurrentParty.LeaderPC;
            turnBegin = true;
            CurrentParty.OutsidePos = CurrentParty.Pos; //Store this re
            CurrentParty.outsideDir = CurrentParty.Direction;

            TerrainRecord[,] unders = new TerrainRecord[3, 3];
            TerrainRecord[,] overs = new TerrainRecord[3, 3];

            for(int y = -1; y <=1; y++)
                for (int x = -1; x <= 1; x++)    
                    WorldMap.TerrainAtX(CurrentParty.Pos.Mod(x, y), ref unders[x + 1, y + 1], ref overs[x + 1, y + 1]);

            CurrentMap = new CombatMap(group, unders, overs);

            //TODO: Like in BoE - dump freshly dead PCs belongings on the combat map - in case he's been
            //killed in a special just prior to combat???
        }

        public static void StartCombat() 
        {
            CurrentParty.SingleActingPC = null;
            ((TownMap)CurrentMap).PlacePartyForCombat(CurrentParty.Direction.Dir);
            Sound.Play("093_sheathe");
            Mode = eMode.COMBAT;
            CurrentTown.UpdateVisible();
            turnBegin = true;
        }

        public static bool EndCombat(bool death_during_split = false)
        {
            if (!death_during_split)
            {
                if (CurrentTown is CombatMap)
                {
                    if (!CurrentTown.NoHostileNPCsLeft())
                    {
                        AddMessage("Can't end combat while enemies are still around!");
                        return false;
                    }

                    Script.New_NPCGroup(((CombatMap)CurrentTown).NPCGroup.FuncOnWin, eCallOrigin.WIN_ENCOUNTER, ((CombatMap)CurrentTown).NPCGroup);
                    new Animation_FadeDown(300);
                }
                CurrentParty.EndCombat();
            }
            //Don't just change the mode here, we need to delay until after the end combat animation has finished, or all the
            //PCs won't draw individually when they whizz back together.
            //combatIsEnding = true;
            return true;
        }

        /// <summary>
        /// Sets the Drag item to the one selected
        /// </summary>
        /// <param name="item"></param>
        /// <param name="from"></param>
        /// <param name="split">If true brings up a window allowing you to split the item. Make sure this isn't allowed if another item is going
        /// to swap into its place.</param>
        public static void StartItemDrag(Item item, IInventory from, bool split)
        {
            if (item == null) { Gui.DragItem = null; return; }

            //Gold or food is never dragged - it just immediately goes to the party's gold/food count
            if (item.Variety == eVariety.Gold)
            {
                from.RemoveItem(item);
                CurrentParty.Gold += item.Charges;
                Sound.Play("039_coinsjingle");
            }
            else if (item.Variety == eVariety.Food)
            {
                from.RemoveItem(item);
                CurrentParty.Food += item.Charges;
                Sound.Play("062_mmm");
            }
            else
            {
                if (split && item.Charges > 1)
                {
                    Gui.SplitDragItem = item;
                    Gui.SplitDragFrom = from;
                    new InputTextWindow(splitDragItem, "Take how many?", item.Charges.ToString(), true);
                }
                else
                {
                    Gui.DragItem = item; //Make whatever's in the slot we've dragged to the new drag item
                    Gui.DragItemFrom = from;
                }
            }
        }

        static void splitDragItem(string txt)
        {
            if (txt == null) return;
            int num = Convert.ToInt32(txt);

            if (num > 0 && num < Gui.SplitDragItem.Charges) //Take some
            {
                Item newitem = Gui.SplitDragItem.Copy();
                newitem.Charges = num;

                if (!(Gui.SplitDragFrom is Shop))
                {
                    Gui.SplitDragItem.Charges -= num;
                    Gui.SplitDragFrom.AddItem(newitem, false);
                }
                Gui.DragItem = newitem;
                Gui.DragItemFrom = Gui.SplitDragFrom;
            }
            else if (num == Gui.SplitDragItem.Charges) //Just take the lot
            {
                Gui.DragItem = Gui.SplitDragItem; //Make whatever's in the slot we've dragged to the new drag item
                Gui.DragItemFrom = Gui.SplitDragFrom;
            }
        }

        public void BackToMainMenu()
        {
            GameOver = false;
            Gfx.FadeMode = 0;
            Action.LockActions = eAction.NONE;
            Action.Clear();
            gameState = eState.BEGIN_PC_TURN;
            InMainMenu = true;
            CurrentParty = null;
            Scenario.Filename = "";
            CurrentMap = null;
            TownMap.List.Clear();
            WorldMap = null;
            RecentTownList = null;
            portraitWindows.Clear();
            InventoryWindow.Close();
            inventoryWindow = null;
            StatsWindow.Close();
            statsWindow = null;
            messageWindow = null;
            menuBarWindow = null;
            Gui.GuiWindows.Clear();
            Script.CleanUp();
            Gfx.Load(GraphicsDevice, true);
            Sound.Load(true);
            StartMenuWindow.Begin();
        }

        public static void AddMessage(string s)
        {
            messageWindow.AddMessage(s);
        }

        public static void give_help(int a, int b)
        {
        }

        public static void give_error(string e, string m, int n)
        {
        }

        static void LoadSettings()
        {
            //Here's where the game's settings are loaded from the XML file in the game root directory

            XElement xml = null;
            string fn = Path.Combine(Game.RootDirectory, "Settings.xml");

            if (File.Exists(fn))
            {
                xml = XElement.Load(Path.Combine(Game.RootDirectory, "Settings.xml"));
                if (xml.Name != "Settings") throw new Exception("Corrupt settings file.");

                foreach(XElement e in xml.Elements())
                {
                    switch (e.Name.ToString())
                    {
                        case "LastSave":
                            Game.LastSaveFile = e.Value;
                            break;
                        case "DisplayWidth":
                            Gfx.WinW = Convert.ToInt32(e.Value);
                            break;
                        case "DisplayHeight":
                            Gfx.WinH = Convert.ToInt32(e.Value);
                            break;
                        case "FullScreen":
                            Gfx.FullScreen = Convert.ToBoolean(e.Value);
                            break;
                        case "Volume":
                            Sound.Volume = Maths.MinMax(0,10,Convert.ToInt32(e.Value));
                            break;

                        case "KeyMap":
                            foreach (XAttribute k in e.Attributes())
                            {
                                for (int n = 0; n < 30; n++)
                                {
                                    var s = KeyHandler.KeyMapNames[n].Replace("/", "");
                                    s = s.Replace("\n", "");
                                    s = s.Replace(" ", "");

                                    if (s == k.Name.ToString())
                                    {
                                        KeyHandler.KeyMap[n] = (Keys)Convert.ToInt32(k.Value);
                                        break;
                                    }
                                }
                            }
                            break;
                    }

                }
            }
            else
            {
                SaveSettings();
            }
        }
        public static void SaveSettings(int w = -1, int h = -1, int fullscreen = -1)
        {
            if (w == -1) w = Gfx.WinW;
            if (h == -1) h = Gfx.WinH;
            bool fs = fullscreen == -1 ? Gfx.FullScreen : Convert.ToBoolean(fullscreen);


            string fn = Path.Combine(Game.RootDirectory, "Settings.xml");

            XmlWriterSettings settings = new XmlWriterSettings();
            settings.Indent = true;
            settings.OmitXmlDeclaration = true;
            settings.ConformanceLevel = ConformanceLevel.Fragment;

            using (XmlWriter writer = XmlWriter.Create(fn, settings))
            {
                writer.WriteStartElement("Settings");
                writer.WriteElementString("LastSave", LastSaveFile);
                writer.WriteElementString("Volume", Convert.ToString(Sound.Volume));
                writer.WriteElementString("DisplayWidth", Convert.ToString(w));
                writer.WriteElementString("DisplayHeight", Convert.ToString(h));
                writer.WriteElementString("FullScreen", Convert.ToString(fs));
                //We'll have to set the graphics settings when the graphics have been loaded.

                writer.WriteStartElement("KeyMap");
                for (int n = 0; n < 30; n++)
                {
                    var s = KeyHandler.KeyMapNames[n].Replace("/", "");
                    s = s.Replace("\n", "");
                    s = s.Replace(" ", "");
                    writer.WriteAttributeString(s, Convert.ToString((int)KeyHandler.KeyMap[n]));
                }
                writer.WriteEndElement();
                writer.WriteEndElement();

            }
        }

        public static void ReOrderPortraits()
        {
            var newlist = new List<PortraitWindow>();

            for (int i = 0; i < Constants.PC_LIMIT; i++)
            {
                var p = portraitWindows.Find(n => n.PC == CurrentParty.PCList[i]);
                newlist.Add(p);
                p.Position(10, i * PortraitWindow.HEIGHT + 10);
            }
            portraitWindows = newlist;
        }

        public static void SetPortraitWindowKeys()
        {
            if (portraitWindows != null && portraitWindows.Count > 0 && CurrentParty.CurrentPC != null)
                for (int n = 0; n < portraitWindows.Count; n++)
                    portraitWindows[n].SetShortcuts(CurrentParty.CurrentPC.Slot == n);
        }

        void doAfterWin(int option, string filename)
        {
            if (option == LoadGameWindow.SAVE)
            {
                SaveGame(filename, true);
            }

            BackToMainMenu();
        }
    }

}
