using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml;
using System.Xml.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Input;
using System.Threading;

namespace SwordsOfExileGame;

public partial class Game 
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
    private static string errorType, errorMessage;
    public static bool Quit = false;

    //Loading status flags.
    private static bool loadingComplete = false, loadingStartNew = false;
    public static bool Loading = false;

    public static string RootDirectory; //The root directory for the game
    public static string BaseDirectory, ScenarioDirectory, SavesDirectory; //The directory for the 'Base' data.

    public static bool InMainMenu = true;
        
    //Should be set to the designated placeholder entries in the enum. Eg, Set to INVENTORY_LOCKED_ACTIONS, when a Loot Window or Shop window is open, to stop any actions except inventory ones
    public static bool PartyDead = false, GameOver = false;

    public static PartyType CurrentParty;
    public static IMap CurrentMap;
    public static TownMap CurrentTown => CurrentMap as TownMap;
    public static WorldMapType WorldMap;
    public static List<TownMap> RecentTownList;
    public static eMode Mode { get => mode;
        set
        {
            mode = value;
            _menuBarWindow?.Update();
        }
    }

    private static eMode mode = eMode.TOWN;

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
        get => Invincible && OneHitKill && PCsAlwaysHit && NPCGroupsFlee;
        set
        {
            Invincible = OneHitKill = PCsAlwaysHit = NPCGroupsFlee = value;
            AddMessage(!value
                ? "Debug Mode Deactivated."
                : "Debug Mode Activated:\n  Invincible PCs\n  PCs always hit\n  PCs kill on one hit\n  Outside NPC Groups flee");
        } 
    }

    public static int AnimTicks = 0;
    private const int TICK_SPEED = 250;
    private static int _nextTick = 0;
    public static eTurn Turn { get { if (_gameState is eState.BEGIN_PC_TURN or eState.PICK_NEXT_PC or eState.PC_TURN_PROCESS_ACTION or eState.TARGET_MODE) return eTurn.PLAYER; else return eTurn.NPCS; } }//= eTurn.PLAYER;
    private static bool _turnBegin;

    public static bool PlayerTargeting => _gameState == eState.TARGET_MODE;

    private static List<PortraitWindow> _portraitWindows;
    private static InventoryWindow _inventoryWindow;
    private static StatsWindow _statsWindow;
    private static InfoListWindow _messageWindow;
    private static MenuBarWindow _menuBarWindow;

    private static eState _gameState = eState.BEGIN_PC_TURN;

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
        for (var n = 0; n < 30; n++)
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
        if (Quit) Exit();

        _nextTick += gameTime.ElapsedGameTime.Milliseconds;
        if (_nextTick >= TICK_SPEED)
        {
            _nextTick = 0;
            AnimTicks = ++AnimTicks % 4;
        }

        Sound.Refresh();

        KeyHandler.GetKeysHit(gameTime.ElapsedGameTime.Milliseconds);

        Gui.Handle();
        Gui.HandleToolTip();

        if (ErrorFlagged)
        {
            Gui.ErrorReport(errorType, errorMessage);
            return;
        }

        //If the game is loading (in a separately running thread) don't do anything else until it finishes.
        if (Loading)
        {
            if (loadingComplete /* && !DrawCalled*/) BeginGame();
            else if (InMainMenu) StartupMap.Update(gameTime);
            return;
        }

        if (InMainMenu)
        {
            StartupMap.Update(gameTime);
            return;
        }

        if (Gui.WorldModalPaused)
        {
            return;
        }

        Gfx.DoMapScroll(gameTime.ElapsedGameTime.Milliseconds);
        Gfx.DoMapZoom(gameTime.ElapsedGameTime.Milliseconds);
        KeyHandler.GetActionKeys();

        //1st priority: If there are any animations in the queue, update them now.
        if (!Animation.NoAnimationsRunning())
        {
            Animation.AdvanceAll(gameTime.ElapsedGameTime.Milliseconds);
            return;
        }
        
        //2nd priority: If there are any scripts in the queue, run them now.
        if (Script.IsRunning && _gameState != eState.GAME_OVER)
        {
            Script.RunNext();
            return;
        }

        //Now the main state machine
        bool immediateStateSwitch;

        do
        {
            //This is set to true in each state to allow switching to the next state without updating animations/scripts/user input
            immediateStateSwitch = ProcessGameState();
            
            //If we don't want to give a chance to animations or scripts to run before changing state, this should be set.
        } while (immediateStateSwitch);
    }
    
    protected override void Draw(GameTime gameTime)
    {
        Gfx.Draw();
    }

    private bool ProcessGameState()
    { 
        //Now handle the main game state
        switch (_gameState)
        {
            //Set the PCs action points for the turn
            case eState.BEGIN_PC_TURN:
                CurrentParty.StartNewTurn();
                _gameState = eState.PICK_NEXT_PC;
                return true;
                break;

            //Choose the PC to control based on who has action points left.
            case eState.PICK_NEXT_PC:
                if (CurrentParty.PickNextPC())
                {
                    //No PC has action points left, so make it the NPCs go. (This is only reached in combat mode - in town mode the state switches to NPCs after every player action)
                    _gameState = eState.BEGIN_NPC_TURN;
                }
                else
                {
                    Gfx.CentreView(CurrentParty.ActivePC.Pos, false);
                    _gameState = eState.PC_TURN_PROCESS_ACTION;
                    if (!Script.IsRunning && Animation.NoAnimationsRunning()) return true;
                }

                break;

            //The main state for handling the player's actions
            case eState.PC_TURN_PROCESS_ACTION:

                if (GameOver)
                {
                    _gameState = eState.END_TURN;
                    return true;
                }

                _gameState = Action.Handle(); //eState.BEGIN_NPC_TURN;

                if (PartyDead)
                {
                    _gameState = eState.PARTY_DEAD;
                    return true;
                }

                if (_gameState is eState.BEGIN_NPC_TURN or eState.PICK_NEXT_PC &&
                    !Script.IsRunning && (
                        (Game.Mode != eMode.COMBAT && Animation.OnlyMovingAnimationsRunning()) ||
                        Game.Mode == eMode.COMBAT && Animation.NoAnimationsRunning()))
                    return true;

                break;

            //Handle player's actions in Target Mode (when needing to choose a target npc/tile on the map)
            case eState.TARGET_MODE:

                if (Action.HandleTargeting())
                {
                    _gameState = eState.PC_TURN_PROCESS_ACTION;
                    return true;
                }

                break;

            //Assign action points to NPCs for the turn, activate new NPCs
            case eState.BEGIN_NPC_TURN:

                CurrentMap.StartNPCTurn();
                _gameState = eState.NPC_TURN;
                if (!Script.IsRunning && Animation.NoAnimationsRunning()) return true;
                break;

            //Move each NPC.
            case eState.NPC_TURN:
                if (CurrentMap.DoNPCTurn()) //Returns true when the last NPC has acted.
                {
                    _gameState = eState.END_TURN;
                    if (!Script.IsRunning && Animation.NoAnimationsRunning()) return true;
                }

                break;

            //Handle various checks and stuff at the end of each turn.
            case eState.END_TURN:

                //The PCs are dead. End the game
                if (PartyDead)
                {
                    _gameState = eState.PARTY_DEAD;
                    return true;
                }
                else if (GameOver)
                {
                    new Animation_FadeDown(1000);
                    _gameState = eState.GAME_OVER;
                }
                //Check: PCs leave town.
                else if (Mode == eMode.TOWN && !CurrentTown.InActArea(CurrentParty.Pos))
                {
                    //Set up any scripts to run on leaving the town
                    CurrentTown.SetUpExitFunc();
                    _gameState = eState.BEGIN_LEAVE_MAP;
                }
                //Check: PCs step on town in world map.
                else if (Mode == eMode.OUTSIDE && WorldMap.TownEntranceHere(CurrentParty.Pos) != null)
                {
                    var t = WorldMap.TownEntranceHere(CurrentParty.Pos).DestTown;
                    Sound.Play(t.LightType > 0 ? "095_enterdungeon" : "016_townentry");
                    new Animation_FadeDown(300);
                    _gameState = eState.BEGIN_ENTER_TOWN;
                }
                //Check: Outside NPCs want to attack
                else if (Mode == eMode.OUTSIDE &&
                         WorldMap.PCAttacker !=
                         null) //A wandering NPC group is next to the party and wants to attack!
                {
                    _gameState = eState.BEGIN_NPC_GROUP_ATTACK;
                }
                //Check: All PCs flee combat map
                else if (Mode == eMode.COMBAT && CurrentTown is CombatMap && CurrentParty.PartyFled())
                {
                    //The entire party has run away from combat. Put back on world map.
                    new Animation_FadeDown(300);
                    Script.New_NPCGroup(((CombatMap)CurrentMap).NPCGroup.FuncOnFlee,
                        eCallOrigin.FLEE_ENCOUNTER,
                        ((CombatMap)CurrentMap).NPCGroup);
                    _gameState = eState.BEGIN_PARTY_FLEE;
                }
                else
                {
                    //Handle status effects, Timer events, light levels, fields.
                    CurrentParty.IncreaseAge();
                    if (PartyDead)
                    {
                        _gameState = eState.PARTY_DEAD;
                        return true;
                    }

                    //Handle map squares with 'stood on' triggers
                    CurrentMap.DoStoodOnTriggers();
                    if (PartyDead)
                    {
                        _gameState = eState.PARTY_DEAD;
                        return true;
                    }

                    _gameState = eState.BEGIN_PC_TURN;
                    if (!Script.IsRunning && Animation.NoAnimationsRunning()) return true;
                }

                break;

            case eState.BEGIN_LEAVE_MAP:
                new Animation_FadeDown(300);
                _gameState = eState.LEAVE_MAP;
                break;

            case eState.LEAVE_MAP:
                CurrentParty.OutsidePos += CurrentTown.GetDepartDirection(CurrentParty.Pos);
                CurrentParty.Pos = CurrentParty.OutsidePos;
                CurrentParty.MoveToMap(WorldMap);
                _gameState = eState.BEGIN_PC_TURN;
                break;

            case eState.BEGIN_ENTER_TOWN:

                var town = WorldMap.TownEntranceHere(CurrentParty.Pos).DestTown;
                CurrentParty.OutsidePos = CurrentParty.Pos;
                Mode = eMode.TOWN;
                switch (CurrentParty.Direction.Dir)
                {
                    case eDir.S:
                        CurrentParty.Pos = town.EnterPos[0];
                        break;
                    case eDir.SE:
                    case eDir.E:
                    case eDir.NE:
                        CurrentParty.Pos = town.EnterPos[3];
                        break;
                    case eDir.N:
                        CurrentParty.Pos = town.EnterPos[2];
                        break;
                    case eDir.NW:
                    case eDir.W:
                    case eDir.SW:
                        CurrentParty.Pos = town.EnterPos[1];
                        break;
                }

                CurrentParty.MoveToMap(town);
                _gameState = eState.BEGIN_PC_TURN;
                break;

            case eState.BEGIN_PARTY_FLEE:

                foreach (var pc in CurrentParty.PCList.Where(pc => pc.LifeStatus == eLifeStatus.FLED))
                {
                    pc.LifeStatus = eLifeStatus.ALIVE;
                }

                CurrentParty.Pos = CurrentParty.OutsidePos;
                CurrentParty.MoveToMap(WorldMap);
                //Reset things
                Mode = eMode.OUTSIDE;
                _turnBegin = true;
                Gfx.CentreView(CurrentParty.Pos, true);
                _gameState = eState.BEGIN_PC_TURN;
                break;

            case eState.BEGIN_NPC_GROUP_ATTACK:
                if (!WorldMap.NPCGroupList.Contains(WorldMap.PCAttacker))
                {
                    WorldMap.PCAttacker = null; //Attacker chose to flee!
                    _gameState = eState.END_TURN;
                }
                else
                {
                    bool cancelled;
                    if (!WorldMap.PCAttacker.DoMeetingScript(out cancelled))
                    {
                        new Animation_FadeDown(300);
                        _gameState = eState.NPC_GROUP_ATTACK;
                        break;
                    }

                    if (cancelled)
                    {
                        WorldMap.NPCGroupList.Remove(WorldMap.PCAttacker);
                        WorldMap.PCAttacker = null;
                        _gameState = eState.END_TURN;
                    }
                }

                break;

            case eState.NPC_GROUP_ATTACK:

                //Change to combat map!
                InitiateOutdoorCombat(WorldMap.PCAttacker.Record);
                new Animation_FadeUp(300);

                //Also, delete this outdoor wandering group now.
                WorldMap.NPCGroupList.Remove(WorldMap.PCAttacker);
                _gameState = eState.BEGIN_PC_TURN;

                break;

            case eState.COMBAT_END:
                if (CurrentTown is CombatMap) //We've finished fighting on a combat map, back to world map.
                {
                    foreach (var pc in CurrentParty.PCList.Where(pc => pc.LifeStatus == eLifeStatus.FLED))
                    {
                        pc.LifeStatus = eLifeStatus.ALIVE;
                    }

                    _gameState = eState.BEGIN_PC_TURN;
                    CurrentParty.Pos = CurrentParty.OutsidePos;
                    CurrentParty.MoveToMap(WorldMap);
                    Mode = eMode.OUTSIDE;

                }
                else
                {
                    _gameState = eState.BEGIN_NPC_TURN;
                    Mode = eMode.TOWN;
                }

                break;

            case eState.DO_CAMPING:
                CurrentParty.DoRest();
                new Animation_FadeUp(300);
                _gameState = eState.BEGIN_PC_TURN;
                break;

            case eState.PARTY_DEAD:
                if (CurrentParty.IsSplit) //Unless just the solo PC in split mode is.
                {
                    //If the solo PC in a split party dies, the game is not over, the rest of the PCs take over.
                    PartyDead = false;
                    CurrentParty.Reunite();
                    if (Game.Mode == eMode.COMBAT)
                    {
                        Game.EndCombat(true);
                        _gameState = eState.COMBAT_END;
                    }
                    else
                    {
                        CurrentParty.IncreaseAge();
                        _gameState = eState.BEGIN_PC_TURN;
                    }
                }
                else
                {
                    Sound.Play("013_partydeath");
                    new Animation_FadeDown(1000);
                    _gameState = eState.GAME_OVER;
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
                    foreach (var pc2 in CurrentParty.PCList.Where(pc2 => pc2.LifeStatus == eLifeStatus.ABSENT))
                    {
                        pc2.LifeStatus = eLifeStatus.ALIVE;
                    }

                    CurrentParty.IsSplit = false;
                    CurrentParty.Restore();
                    CurrentParty.StripItems(); //Remove items that can't be taken from the scenario.
                    new LoadGameWindow(false, true, true, DoAfterWin);
                }

                break;
            case eState.BEGIN_COMBAT_END:
            case eState.ENTER_TOWN:
            case eState.BEGIN_PARTY_DEATH:
            case eState.PARTY_FLEE:
            default:
                throw new ArgumentOutOfRangeException();
        }

        return false;
    }

    public static void DoLoadSave(int option, string filename)
    {
        if (option == LoadGameWindow.LOAD)
        {
            var i = LoadSaveInfo(filename, false);
            if (i == null)
            {
                return;
            }
            
            Scenario.Filename = Path.GetFileNameWithoutExtension(i.ScenFile);
            ScenarioDirectory = Path.Combine(Game.RootDirectory, "Scenarios", Scenario.Filename);
            LastSaveFile = filename;
            BeginLoadingThread(false);
        }
        else if (option == LoadGameWindow.SAVE)
        {
            SaveGame(filename, false);
        }
    }
    
    private static void LoadingThread()
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

        foreach (var pc in CurrentParty.PCList)
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
    public static void BeginLoadingThread(bool startNew)
    {
        Gui.GuiWindows.Clear();

        new LoadingWindow();

        loadingStartNew = startNew;
        Loading = true;
        loadingComplete = false;

        Gfx.FadeMode = 3;
        Gfx.FadeColor = Color.Black;
        var t = new Thread(LoadingThread);
        t.Start();
    }

    private static void BeginGame()
    {
        PartyDead = false;

        Gfx.Load(null, false); //We don't do this during the loading thread because it wigs out with the Texture Loader

        if (loadingStartNew)
        {
            CurrentMap = Scenario.StartTown;
            CurrentParty.Pos = Scenario.TownStartPos;
            CurrentParty.Age = 0;

            var op = new Location(Scenario.StartOutside.SectorPos.X * Constants.SECTOR_WIDTH, Scenario.StartOutside.SectorPos.Y * Constants.SECTOR_HEIGHT);
            CurrentParty.OutsidePos = op + Scenario.OutsideStartPos;

            if (!string.IsNullOrEmpty(Scenario.InitialiseFunc)) Script.RunNonLatentFuncBool(Scenario.InitialiseFunc);

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
        _turnBegin = true;
        _gameState = eState.BEGIN_PC_TURN;
        Animation.CancelAll();
        new Animation_FadeUp(1000);
    }

    private static void SetUpGameWindows()
    {
        Gui.GuiWindows.Clear();
        _portraitWindows = new List<PortraitWindow>();
        foreach (var pc in CurrentParty.PCList)
        {
            _portraitWindows.Add(new PortraitWindow(pc, _portraitWindows.Count));
        }
        SetPortraitWindowKeys();

        _inventoryWindow = new InventoryWindow();
        _statsWindow = new StatsWindow();
        _messageWindow = new InfoListWindow();
        _menuBarWindow = new MenuBarWindow();
    }

    private static void InitiateOutdoorCombat(EncounterRecord group)
    {
        Mode = eMode.COMBAT;
        CurrentParty.ActivePC = CurrentParty.LeaderPC;
        _turnBegin = true;
        CurrentParty.OutsidePos = CurrentParty.Pos; //Store this re
        CurrentParty.outsideDir = CurrentParty.Direction;

        var unders = new TerrainRecord[3, 3];
        var overs = new TerrainRecord[3, 3];

        for(var y = -1; y <=1; y++)
        for (var x = -1; x <= 1; x++)    
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
        _turnBegin = true;
    }

    public static bool EndCombat(bool deathDuringSplit = false)
    {
        if (deathDuringSplit)
        {
            return true;
        }
        
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
                new InputTextWindow(SplitDragItem, "Take how many?", item.Charges.ToString(), true);
            }
            else
            {
                Gui.DragItem = item; //Make whatever's in the slot we've dragged to the new drag item
                Gui.DragItemFrom = from;
            }
        }
    }

    private static void SplitDragItem(string txt)
    {
        if (txt == null) return;
        var num = Convert.ToInt32(txt);

        if (num > 0 && num < Gui.SplitDragItem.Charges) //Take some
        {
            var newItem = Gui.SplitDragItem.Copy();
            newItem.Charges = num;

            if (Gui.SplitDragFrom is not Shop)
            {
                Gui.SplitDragItem.Charges -= num;
                Gui.SplitDragFrom.AddItem(newItem, false);
            }
            Gui.DragItem = newItem;
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
        _gameState = eState.BEGIN_PC_TURN;
        InMainMenu = true;
        CurrentParty = null;
        Scenario.Filename = "";
        CurrentMap = null;
        TownMap.List.Clear();
        WorldMap = null;
        RecentTownList = null;
        _portraitWindows.Clear();
        InventoryWindow.Close();
        _inventoryWindow = null;
        StatsWindow.Close();
        _statsWindow = null;
        _messageWindow = null;
        _menuBarWindow = null;
        Gui.GuiWindows.Clear();
        Script.CleanUp();
        Gfx.Load(GraphicsDevice, true);
        Sound.Load(true);
        StartMenuWindow.Begin();
    }

    public static void AddMessage(string s)
    {
        _messageWindow.AddMessage(s);
    }

    public static void give_help(int a, int b)
    {
    }

    private static void LoadSettings()
    {
        //Here's where the game's settings are loaded from the XML file in the game root directory

        var fn = Path.Combine(Game.RootDirectory, "Settings.xml");

        if (!File.Exists(fn))
        {
            SaveSettings();
            return;
        }

        var xml = XElement.Load(Path.Combine(Game.RootDirectory, "Settings.xml"));
            if (xml.Name != "Settings") throw new Exception("Corrupt settings file.");

        foreach (var e in xml.Elements())
        {
            switch (e.Name.ToString())
            {
                case "LastSave":
                    LastSaveFile = e.Value;
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
                    Sound.Volume = Maths.MinMax(0, 10, Convert.ToInt32(e.Value));
                    break;

                case "KeyMap":
                    foreach (var k in e.Attributes())
                    {
                        for (var n = 0; n < 30; n++)
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
    public static void SaveSettings(int w = -1, int h = -1, int fullscreen = -1)
    {
        if (w == -1) w = Gfx.WinW;
        if (h == -1) h = Gfx.WinH;
        var fs = fullscreen == -1 ? Gfx.FullScreen : Convert.ToBoolean(fullscreen);


        var fn = Path.Combine(Game.RootDirectory, "Settings.xml");

        var settings = new XmlWriterSettings();
        settings.Indent = true;
        settings.OmitXmlDeclaration = true;
        settings.ConformanceLevel = ConformanceLevel.Fragment;

        using var writer = XmlWriter.Create(fn, settings);
        
        writer.WriteStartElement("Settings");
        writer.WriteElementString("LastSave", LastSaveFile);
        writer.WriteElementString("Volume", Convert.ToString(Sound.Volume));
        writer.WriteElementString("DisplayWidth", Convert.ToString(w));
        writer.WriteElementString("DisplayHeight", Convert.ToString(h));
        writer.WriteElementString("FullScreen", Convert.ToString(fs));
        //We'll have to set the graphics settings when the graphics have been loaded.

        writer.WriteStartElement("KeyMap");
        for (var n = 0; n < 30; n++)
        {
            var s = KeyHandler.KeyMapNames[n].Replace("/", "");
            s = s.Replace("\n", "");
            s = s.Replace(" ", "");
            writer.WriteAttributeString(s, Convert.ToString((int)KeyHandler.KeyMap[n]));
        }
        writer.WriteEndElement();
        writer.WriteEndElement();
    }

    public static void ReOrderPortraits()
    {
        var newList = new List<PortraitWindow>();

        for (var i = 0; i < Constants.PC_LIMIT; i++)
        {
            var p = _portraitWindows.Find(n => n.PC == CurrentParty.PCList[i]);
            newList.Add(p);
            p.Position(10, i * PortraitWindow.HEIGHT + 10);
        }
        _portraitWindows = newList;
    }

    public static void SetPortraitWindowKeys()
    {
        if (_portraitWindows is not { Count: > 0 } || CurrentParty.CurrentPC == null)
        {
            return;
        }

        for (var n = 0; n < _portraitWindows.Count; n++)
        {
            _portraitWindows[n].SetShortcuts(CurrentParty.CurrentPC.Slot == n);
        }
    }

    private void DoAfterWin(int option, string filename)
    {
        if (option == LoadGameWindow.SAVE)
        {
            SaveGame(filename, true);
        }

        BackToMainMenu();
    }
}