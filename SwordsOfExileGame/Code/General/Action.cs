using System;
using System.Collections.Generic;

namespace SwordsOfExileGame;

public class Action
{
    private static Action current;

    public static bool Exists() { return current != null && current.Requested != eAction.NONE; }
    public static Action GetCurrent()
    {
        return current;
    }
    public static eState Handle()
    {
        return current._Handle();
    }
    public static bool HandleTargeting()
    {
        return current._HandleTargeting();
    }
    public static void Clear()
    {
        current.Requested = eAction.NONE;
    }
    public Action(eAction what)
    {
        if (current is { Requested: > eAction.BLOCKABLE_ACTIONS })
            return;

        Requested = what;
        current = this;
    }
 
    public eAction Requested;
    public PCType PC, PC2; //For when Action.Requested is an action concerning a PC
    public NPC NPC;
    public Direction Dir;
    public Item Item; //For when Action.Requested is an action concerning an item.
    public Location Loc;
    public IInventory InventoryTo, InventoryFrom;
    public eEquipSlot EquipSlot;
    public MagicSpell Spell;
    public eItemFilter FilterTo;
    public List<Location> TargetList;

    public static bool /*PlayerTargeting = false,*/ TargetDrawLine = false, TargetNumbersOn = false;
    public static eAction TargetWhat;
    public static int TargetRange;
    private static Item TargetItem;
    public static PCType TargetPC;
    public static MagicSpell TargetSpell;
    public static int TargetTotalTargets; //How many targets player needs to select
    public static int TargetSelectCount;  //Keep track of how many targets we've picked so far.
    public static List<Location> TargetSelectList; //All targets will be stored here.
    public static bool TargetNPCsOnly;    //Only allow targeting tiles occupied by NPCs
    public static Pattern TargetPattern;

    public static eAction LockActions = eAction.NONE; //Set this to prevent certain actions being called. All actions BEFORE this one in the enum will be blocked. 

    //Shortcuts
    private PartyType CurrentParty = Game.CurrentParty;
    private IMap CurrentMap = Game.CurrentMap;
    private TownMap CurrentTown = Game.CurrentTown;
    private WorldMapType WorldMap = Game.WorldMap;
    private eMode Mode = Game.Mode;
    private void AddMessage(string m) { Game.AddMessage(m); }

    public eState _Handle()
    {
        var action = Requested;
        Requested = eAction.NONE;

        if (action == eAction.NONE) return eState.PC_TURN_PROCESS_ACTION; //gameState;

        if (Gui.DragItem != null && action < eAction.DRAG_ITEM_LOCKED_ACTIONS)
            Gui.DragItem = null; //Cancel the drag.

        //Ignore everything except specific inventory actions if a loot/shop window is open or the player is dragging an item on the mouse pointer.
        //BUT Actions disallowed while a loot window is open just causes the loot window to close.
        if (action < LockActions)
        {
            var w = Gui.GetWindowOfType(typeof(LootWindow));
            if (LockActions == eAction.INVENTORY_LOCKED_ACTIONS && w != null)
                w.Close();
            else
                return eState.PC_TURN_PROCESS_ACTION;
        }

        var advance = false;
        var start_target = false;

        switch (action)
        {
            case eAction.Up: advance = CurrentParty.Move(new Location(0, -1)); break;
            case eAction.Down: advance = CurrentParty.Move(new Location(0, 1)); break;
            case eAction.Right: advance = CurrentParty.Move(new Location(1, 0)); break;
            case eAction.Left: advance = CurrentParty.Move(new Location(-1, 0)); break;
            case eAction.UpLeft: advance = CurrentParty.Move(new Location(-1, -1)); break;
            case eAction.UpRight: advance = CurrentParty.Move(new Location(1, -1)); break;
            case eAction.DownLeft: advance = CurrentParty.Move(new Location(-1, 1)); break;
            case eAction.DownRight: advance = CurrentParty.Move(new Location(1, 1)); break;
            case eAction.StandReady: advance = CurrentParty.Move(new Location(0, 0)); break;
            case eAction.Parry: advance = CurrentParty.ActivePC.DoParry(); break;
            case eAction.Wait: advance = CurrentParty.DoWait(); break;
            case eAction.Act: CurrentParty.DoAct(); break;
            case eAction.StartCombat: Game.StartCombat(); return eState.BEGIN_PC_TURN;
            case eAction.EndCombat: if (Game.EndCombat()) return eState.COMBAT_END; break;

            case eAction.GatherLoot:
                var loot = LootSpot.Generate(CurrentParty.Pos, (TownMap)CurrentMap, true);
                if (loot != null) new LootWindow(loot); else Game.AddMessage(string.Format("Nothing nearby to gather"));
                break;

            case eAction.EscapeMenu:
                new EscapeMenuWindow();
                Gui.ActiveToolTip = null;
                break;

            case eAction.RunConsoleWindow:
                new InputTextWindow(Script.RunConsoleScript, "Enter Python statement to execute", "", false, Gfx.WinW - 20);
                Gui.ActiveToolTip = null;
                break;

            case eAction.Search:
                CurrentMap.Search(Loc, PC);
                break;
            case eAction.Use:
                CurrentTown.UseTile(Loc);
                break;
            case eAction.FireRanged:
                advance = PC.FireMissile(Loc);
                break;

            case eAction.TakeItem:
                //Take item from a Loot window (not directly from the map)

                if (Mode == eMode.COMBAT && CurrentParty.ActivePC.AP <= 0 && (!(CurrentTown is CombatMap) || CurrentTown.NPCList.Count == 0))
                {
                    Game.AddMessage("Not enough AP to take item during combat");
                    break;
                }
                //Don't need to check for proximity - loot windows only show items in range

                LootSpot.GetActiveLootSpot().RemoveItem(Item);
                if (Item.Variety == eVariety.Gold)
                {
                    CurrentParty.Gold += Item.Charges;
                    Sound.Play("039_coinsjingle");
                }
                else if (Item.Variety == eVariety.Food)
                {
                    CurrentParty.Food += Item.Charges;
                    Sound.Play("062_mmm");
                }
                else
                {
                    PC.AddItem(Item, true);
                    Sound.ItemSound();
                }

                InventoryFrom.ArrangeItems();

                if (Mode == eMode.COMBAT) PC.AP -= 2;
                break;

            case eAction.TakeAllItems:
                loot = LootSpot.GetActiveLootSpot();
                if (!loot.InventorysClose(PC))
                {
                    Game.AddMessage("Items are out of range.");
                    break;
                }

                var to_remove = new List<Item>();

                bool hasitem = false, hasfood = false, hasgold = false;

                foreach (var i in loot.RemoveEach())
                {
                    if (i.Variety == eVariety.Gold)
                    {
                        hasgold = true;
                        CurrentParty.Gold += i.Charges;
                    }
                    else if (i.Variety == eVariety.Food)
                    {
                        hasfood = true;
                        CurrentParty.Food += i.Charges;
                    }
                    else
                    {
                        hasitem = true;
                        PC.AddItem(i, true);
                    }
                }
                if (hasitem) Sound.ItemSound();
                if (hasgold) Sound.Play("039_coinsjingle");
                if (hasfood) Sound.Play("062_mmm");

                if (Mode == eMode.COMBAT) PC.AP = 0;
                break;

            case eAction.TakeItemMap:
                //Item must be in proximity or menu option wouldn't have appeared.

                CurrentTown.ItemList.Remove(Item);
                if (Item.Variety == eVariety.Gold)
                {
                    CurrentParty.Gold += Item.Charges;
                    Sound.Play("039_coinsjingle");
                }
                else if (Item.Variety == eVariety.Food)
                {
                    CurrentParty.Food += Item.Charges;
                    Sound.Play("062_mmm");
                }
                else
                {
                    PC.AddItem(Item, true);
                    Sound.ItemSound();
                }
                if (Mode == eMode.COMBAT) PC.AP -= 2;
                break;

            case eAction.TakeAllItemMap:
                var removelist = new List<Item>();

                foreach (var item in CurrentTown.EachItemThere(Loc))
                    removelist.Add(item);

                hasfood = false; hasgold = false; hasitem = false;
                foreach (var item in removelist)
                {
                    CurrentTown.ItemList.Remove(item);
                    if (item.Variety == eVariety.Gold)
                    {
                        CurrentParty.Gold += item.Charges;
                        hasgold = true;
                    }
                    else if (item.Variety == eVariety.Food)
                    {
                        CurrentParty.Food += item.Charges;
                        hasfood = true;
                    }
                    else
                    {
                        PC.AddItem(item, true);
                        hasitem = true;
                    }
                }
                if (hasitem) Sound.ItemSound();
                if (hasgold) Sound.Play("039_coinsjingle");
                if (hasfood) Sound.Play("062_mmm");
                if (Mode == eMode.COMBAT) PC.AP = 0;
                break;

            case eAction.DropItem:
                if (PC.HasEquipped(Item) != eEquipSlot.None)
                    PC.Unequip(Item);
                else
                    PC.RemoveItem(Item);

                CurrentMap.PlaceItem(Item, Loc);
                Game.AddMessage(string.Format("{0} drops the {1}", PC.Name, Item.KnownName));
                Sound.ItemSound();
                if (Mode == eMode.COMBAT) PC.AP -= 2;
                break;

            case eAction.UseItem:
                PC.UseItem(Item);
                break;

            case eAction.GiveItem:
                //Take item from one PCs inventory (PC1) and put it in another's (PC2)

                if (PC.IsGone() || PC2.IsGone())
                {
                    Game.AddMessage("Give: Character is not in party.");
                    break;
                }

                //Check for proximity of PCs
                if (!PC.Pos.adjacent(PC2.Pos))
                {
                    Game.AddMessage("Give: must be adjacent.");
                    break;
                }

                if (Mode == eMode.COMBAT && CurrentParty.ActivePC.AP <= 0 && (!(CurrentMap is CombatMap) || CurrentTown.NPCList.Count == 0))
                {
                    Game.AddMessage("Not enough AP to give item during combat");
                    break;
                }

                if (PC.HasEquipped(Item) != eEquipSlot.None)
                {
                    if (PC.Unequip(Item) != null)
                    {
                        PC2.AddItem(Item, true);
                        if (Mode == eMode.COMBAT) PC.AP -= 2;
                    }
                }
                else
                {
                    PC.RemoveItem(Item);//, false))
                    PC2.AddItem(Item, true);
                    Sound.ItemSound();
                    if (Mode == eMode.COMBAT) PC.AP -= 2;
                }

                break;

            case eAction.DropItemToLootSpot:
                loot = LootSpot.GetActiveLootSpot();
                if (!loot.InventorysClose(PC))
                {
                    Game.AddMessage("Item is out of range.");
                    break;
                }

                if (PC.HasEquipped(Item) != eEquipSlot.None)
                {
                    if (PC.Unequip(Item) == null)
                        break;
                }
                else
                    PC.RemoveItem(Item);
                loot.AddItem(Item, true);
                Sound.ItemSound();
                break;

            case eAction.EquipItem:
                if (Mode == eMode.COMBAT && PC != CurrentParty.ActivePC)
                {
                    Game.AddMessage("Only the active character can equip items during combat.");
                    break;
                }
                //Check for proximity of PC
                if (!InventoryFrom.InventorysClose(PC))
                {
                    Game.AddMessage("Item is out of range.");
                    break;
                }

                //If item has to move between different inventories, need enough AP to do it during combat.
                if (Mode == eMode.COMBAT && CurrentParty.ActivePC.AP <= 0 && PC != InventoryFrom && (!(CurrentMap is CombatMap) || CurrentTown.NPCList.Count == 0))
                {
                    Game.AddMessage("Not enough AP to take item during combat");
                    break;
                }
                Item replaced_item;
                if (PC.Equip(Item, eEquipSlot.None, out replaced_item))
                {
                    InventoryFrom.RemoveItem(Item);
                    Sound.ItemSound();
                }

                break;
            case eAction.UnequipItem:
                if (PC.Unequip(Item) != null)
                {
                    PC.AddItem(Item, true);
                    Sound.ItemSound();
                }
                break;
            case eAction.PlaceInInventory:
            case eAction.PlaceInEquipSlot:
                PlaceDraggedItem(action);
                break;

            case eAction.BuyItem:
                if (((Shop)InventoryFrom).BuyCost(Item.Value) <= CurrentParty.Gold)
                {
                    AddMessage("You buy it.");
                    CurrentParty.Gold -= ((Shop)InventoryFrom).BuyCost(Item.Value);
                    InventoryTo.AddItem(Item.Copy(), true);
                    Sound.Play("015_cash");
                }
                else
                    AddMessage("You can't afford it.");
                break;

            case eAction.SellItem:
                PlaceDraggedItem(eAction.PlaceInInventory);
                break;

            case eAction.StartRest:
                if (CurrentParty.CanRest())
                {
                    Animation.Create(new Animation_FadeDown(300));
                    return eState.DO_CAMPING;
                }
                break;

            case eAction.QuickSave:
                Game.SaveGame("Quicksave", false);//, "Quicksave");
                break;

            case eAction.QuickLoad:
                Game.LastSaveFile = "Quicksave";
                Game.BeginLoadingThread(false);
                break;

            case eAction.LoadSaveMenu:
                new LoadGameWindow(true, Game.Mode != eMode.COMBAT, false, Game.DoLoadSave);
                break;

            case eAction.ChangeCurrentPC:

                if (PC == null) break;
                if ((Game.Mode != eMode.COMBAT && MagicWindow.Instance != null) || MagicWindow.Instance == null)
                    CurrentParty.CurrentPC = PC;
                break;

            case eAction.ShowInventoryWin:
                InventoryWindow.Reveal(PC, true);
                CurrentParty.CurrentPC = PC;
                break;

            case eAction.ShowCharacterWin:
                StatsWindow.Reveal(PC);
                CurrentParty.CurrentPC = PC;
                break;

            //START TARGETING ACTIONS
            case eAction.SpellTargeting:
            case eAction.ItemSpellTargeting:

                TargetTotalTargets = Spell.GetTargetCount(PC, Requested == eAction.ItemSpellTargeting ? Item : null);
                if (TargetTotalTargets < 1) break;

                start_target = true;
                TargetWhat = action;
                TargetSpell = Spell;
                TargetNumbersOn = true;
                TargetDrawLine = true;
                TargetRange = Spell.Range;
                TargetPC = PC;
                TargetSelectCount = 0;
                TargetNPCsOnly = Spell.Target == eSpellTarget.CHARACTER;
                TargetSelectList = new List<Location>();
                TargetPattern = Spell.TargetPattern;
                TargetSpell.MakeNewsLine(TargetTotalTargets);
                CurrentTown.WorkOutNPCTargetShortcuts(TargetPC.Pos, TargetRange);
                CurrentTown.UpdateVisiblePC(TargetPC, true);
                break;

            case eAction.TargetDropItem:
                if (PC.HasEquipped(Item) != eEquipSlot.None && !PC.CanUnequip(Item))
                {
                    Item.CursedMessage();
                    break;
                }
                start_target = true;
                TargetDrawLine = false;
                TargetNumbersOn = false;
                TargetRange = 1;
                TargetWhat = eAction.TargetDropItem;
                TargetItem = Item;
                TargetPC = PC;
                TargetTotalTargets = 1;
                TargetSelectCount = 0;
                TargetSelectList = new List<Location>();
                TargetNPCsOnly = false;
                TargetPattern = null;
                Game.AddMessage(string.Format("Select an adjacent space to drop the {0} ('m' to Cancel)", Item.KnownName));
                new NewsLine(string.Format("Select an adjacent space to drop the {0}", Item.KnownName), true);
                new NewsLine("('m' to Cancel)", false);
                break;

            case eAction.TargetFireRanged:
                if (!CurrentParty.ActivePC.CanFire())
                {
                    AddMessage(CurrentParty.ActivePC.Name + " is not equipped for ranged combat.");
                    break;
                }
                TargetRange = CurrentParty.ActivePC.HasRanged() ? Constants.PC_FIRING_RANGE : Constants.PC_THROWING_RANGE;
                start_target = true;//PlayerTargeting = true;
                TargetDrawLine = true;
                TargetNumbersOn = true;
                TargetPC = CurrentParty.ActivePC;
                CurrentTown.UpdateVisiblePC(TargetPC, true);
                TargetWhat = eAction.TargetFireRanged;
                TargetNPCsOnly = true;
                TargetTotalTargets = 1;
                TargetSelectCount = 0;
                TargetPattern = null;
                TargetSelectList = new List<Location>();
                CurrentTown.WorkOutNPCTargetShortcuts(TargetPC.Pos, TargetRange);
                new NewsLine(string.Format("Select where to fire"), true);
                new NewsLine("('m' to Cancel)", false);
                break;

            case eAction.TargetSearch:
                start_target = true;//PlayerTargeting = true;
                TargetDrawLine = false;
                TargetNumbersOn = false;
                TargetRange = 1;
                TargetWhat = eAction.TargetSearch;
                TargetPC = CurrentParty.ActivePC;
                TargetNPCsOnly = false;
                TargetTotalTargets = 1;
                TargetSelectCount = 0;
                TargetSelectList = new List<Location>();
                Game.AddMessage("Select what to inspect ('m' to Cancel)");
                new NewsLine("Select what to inspect", true);
                new NewsLine("('m' to Cancel)", false);
                break;

            case eAction.TargetUse:
                start_target = true;//PlayerTargeting = true;
                TargetDrawLine = false;
                TargetNumbersOn = false;
                TargetRange = 1;
                TargetWhat = eAction.TargetUse;
                TargetPC = CurrentParty.ActivePC;
                TargetNPCsOnly = false;
                TargetTotalTargets = 1;
                TargetSelectCount = 0;
                TargetSelectList = new List<Location>();
                Game.AddMessage("Select adjacent tile to use ('m' to Cancel)");
                new NewsLine("Select adjacent tile to use", true);
                new NewsLine("('m' to Cancel)", false);
                break;

            case eAction.TargetTalk:
                //Check there actually are NPCs within range of the player
                var foundtalk = false;
                foreach (NPC npc in CurrentTown.EachCharacterInRange(PC.Pos, 2, false, true))
                {
                    if (CurrentTown.Visible(npc.Pos) && !npc.IsABaddie && npc.Active != eActive.COMBATIVE && npc.Personality != null)
                    {
                        foundtalk = true;
                        break;
                    }
                }
                if (!foundtalk)
                {
                    AddMessage("Nobody who will talk to you is in range.");
                    Requested = eAction.NONE;
                    advance = false;
                    break;
                }

                start_target = true;//PlayerTargeting = true;
                TargetDrawLine = false;
                TargetNumbersOn = true;
                TargetRange = 2;
                TargetWhat = eAction.TargetTalk;
                TargetPC = PC;
                TargetNPCsOnly = true;
                TargetTotalTargets = 1;
                TargetSelectCount = 0;
                TargetSelectList = new List<Location>();
                CurrentTown.WorkOutNPCTargetShortcuts(TargetPC.Pos, TargetRange);
                Game.AddMessage("Select who to talk to ('m' to Cancel)");
                new NewsLine("Select who to talk to", true);
                new NewsLine("('m' to Cancel)", false);
                break;

            case eAction.Talk:
                //Check NPC is in range.
                if (CurrentParty.Pos.VDistanceTo(NPC.Pos) > 2)
                    Game.AddMessage("Too far away to talk to!");
                else if (NPC.IsABaddie || NPC.Active == eActive.COMBATIVE)
                    Game.AddMessage(NPC.Name + " is too busy to talk.");
                else if (NPC.Personality == null)
                    Game.AddMessage(NPC.Name + " has nothing to say.");
                else
                    new ConversationWindow(NPC);
                break;
            case eAction.Attack:
                advance = PC.Attack(NPC);
                break;

            case eAction.ChooseMagicM:
                new MagicWindow(true);
                break;
            case eAction.ChooseMagicP:
                new MagicWindow(false);
                break;

            case eAction.DoAlchemy:
                new AlchemyWindow();
                break;

            case eAction.CastSpell:
                switch (Spell.Target)
                {
                    case eSpellTarget.CASTER: Spell.Cast(PC, null, Item); break;
                    case eSpellTarget.LIVING_PC:
                    case eSpellTarget.DEAD_PC: Spell.Cast(PC, PC2, Item); break;
                    case eSpellTarget.CHARACTER:
                    case eSpellTarget.LOCATION:
                        if (!Spell.MultiTarget)
                            Spell.Cast(PC, Loc, Item);
                        else
                            Spell.Cast(PC, TargetList, Item);
                        break;
                }
                break;

            case eAction.CompleteMove:
                advance = PC.CompleteMove(Loc, Dir);
                break;

            case eAction.BoatLanding:
                CurrentParty.LeaveVehicle();
                advance = PC.CompleteMove(Loc, Dir);
                break;

            case eAction.CompleteCastSpell:
                //Complete spell from a cast
                PC.SP -= Spell.Cost;
                PC.AP -= 4;
                advance = true;
                break;

            case eAction.CompleteCastItemSpell:
                //Complete spell from an item use
                PC.AP -= 2;
                PC.UseItemCharge(Item);
                advance = true;
                break;

            case eAction.Ok:
                break;


        }

        if (advance)
            if (Game.Mode == eMode.COMBAT)
                return eState.PICK_NEXT_PC;
            else
                return eState.BEGIN_NPC_TURN;
        if (start_target) return eState.TARGET_MODE;
        return eState.PC_TURN_PROCESS_ACTION;
    }

    private bool _HandleTargeting()
    {
        var finishspell = false; //For when player presses 'space' to finish a multi-target spell without using all targets.
        var target = new Location(-1, -1);
        switch (Requested)
        {
            case eAction.MapClick:
                target = Loc; break;
            case eAction.Left: if (TargetPC != null) target = TargetPC.Pos.Mod(-1, 0); break;
            case eAction.Right: if (TargetPC != null) target = TargetPC.Pos.Mod(1, 0); break;
            case eAction.Down: if (TargetPC != null) target = TargetPC.Pos.Mod(0, 1); break;
            case eAction.Up: if (TargetPC != null) target = TargetPC.Pos.Mod(0, -1); break;
            case eAction.UpLeft: if (TargetPC != null) target = TargetPC.Pos.Mod(-1, -1); break;
            case eAction.UpRight: if (TargetPC != null) target = TargetPC.Pos.Mod(1, -1); break;
            case eAction.DownLeft: if (TargetPC != null) target = TargetPC.Pos.Mod(-1, 1); break;
            case eAction.DownRight: if (TargetPC != null) target = TargetPC.Pos.Mod(1, 1); break;
            case eAction.Space:

                if (TargetSpell != null)
                {
                    if (TargetSpell.MultiTarget)
                        finishspell = true;
                    else

                        for (var n = 0; n < Pattern.Field.Length; n++)
                            if (Pattern.Field[n] == TargetPattern)
                            {
                                TargetPattern = Pattern.Field[(n + 1) % Pattern.Field.Length];
                                break;
                            }
                }
                break;

            case eAction.Cancel: case eAction.EscapeMenu: case eAction.RunConsoleWindow: case eAction.QuickSave: case eAction.QuickLoad:

                NewsLine.Clear();
                AddMessage("  Action cancelled.");
                if (Game.Mode != eMode.OUTSIDE) CurrentTown.UpdateVisible();

                //If EscapeMenu or ConsoleMenu is run, allow action to remain to be handled by the main HandleAction routine
                if (Requested == eAction.Cancel)
                    Requested = eAction.NONE;
                return true;
        }

        if (Requested >= eAction.TargetLetterSelectA && Requested <= eAction.TargetLetterSelectL && TargetNumbersOn)
        {
            var num = Requested - eAction.TargetLetterSelectA;
            var npc = CurrentTown.FindTargetLetterNPC(num);
            target = npc.Pos;
        }

        Requested = eAction.NONE;

        if (target == new Location(-1, -1) && !finishspell) return false;

        if (!finishspell)
        {
            if (Game.Mode != eMode.OUTSIDE)
            {
                //First check if this target is valid.
                if (!CurrentTown.InBounds(target)) return false; //Outside map limit

                if (!CurrentTown.Visible(target))
                {
                    Game.AddMessage("Target must be visible.");
                    return false;
                }

                if (TargetWhat is eAction.ItemSpellTargeting or eAction.SpellTargeting
                    && CurrentTown.FieldThere(target, Field.ANTIMAGIC))
                {
                    Game.AddMessage("Target must not be in an antimagic field.");
                    return false;
                }
            }
            else
            {
                if (WorldMap.TerrainAt(target) == TerrainRecord.NoOverlay) { return false; }
                if (WorldMap.CanSee(target, CurrentParty.Pos, 0) == 5) { Game.AddMessage("Target must be visible."); return false; }
            }

            if (target.DistanceTo(TargetPC.Pos) > TargetRange)
            {
                Game.AddMessage("Must be adjacent.");
                return false;
            }

            if (TargetNPCsOnly)
            {
                var npc = CurrentTown.CharacterThere(target) as NPC;
                if (npc == null || npc.Record.SpecialSkill == eCSS.INVISIBLE)
                {
                    Game.AddMessage("Must select a visible enemy");
                    return false;
                }
            }

            //If you click on a square that's already on the target list, it is removed from the list
            int l;
            if ((l = TargetSelectList.FindIndex(n => n == target)) != -1)
            {
                TargetSelectList.RemoveAt(l);
                TargetSelectCount--;
                NewsLine.Clear();
                TargetSpell.MakeNewsLine(TargetTotalTargets - TargetSelectCount);
                Sound.Play("000_highbeep");
                return false;
            }

            TargetSelectList.Add(target);
            if (++TargetSelectCount < TargetTotalTargets)
            {
                TargetSpell.MakeNewsLine(TargetTotalTargets - TargetSelectCount);
                Sound.Play("000_highbeep");
                return false; //still more targets to select.
            }
        }

        Requested = eAction.NONE;
        //Target acquired. Complete action that needed the targeting.
        switch (TargetWhat)
        {
            case eAction.TargetSearch:
                if (!target.adjacent(TargetPC.Pos))
                {
                    Game.AddMessage("Must be adjacent.");
                    break;
                }
                Requested = eAction.Search;
                Loc = target;
                PC = TargetPC;
                break;

            case eAction.TargetUse:
                if (!target.adjacent(TargetPC.Pos))
                {
                    Game.AddMessage("Must be adjacent.");
                    break;
                }
                Requested = eAction.Use;
                Loc = target;
                break;

            case eAction.TargetDropItem:
                if (!target.adjacent(TargetPC.Pos))
                {
                    Game.AddMessage("Must be adjacent.");
                    break;
                }

                Requested = eAction.DropItem;
                PC = TargetPC;
                Item = TargetItem;
                Loc = target;
                break;

            case eAction.TargetTalk:

                var npc = CurrentTown.CharacterThere(target) as NPC;

                if (npc == null)
                    Game.AddMessage("Nobody there.");
                else
                {
                    Requested = eAction.Talk;
                    NPC = npc;
                }
                break;

            case eAction.TargetFireRanged:
                Requested = eAction.FireRanged;
                Loc = target;
                PC = TargetPC;
                break;

            case eAction.SpellTargeting:
            case eAction.ItemSpellTargeting:
                Requested = eAction.CastSpell;
                Spell = TargetSpell;
                PC = TargetPC;
                Loc = target;
                TargetList = TargetSelectList;
                Item = TargetWhat == eAction.ItemSpellTargeting ? Item : null;

                if (!TargetSpell.MultiTarget)
                {
                    Loc = target;
                    TargetList = null;
                }
                else
                {
                    Loc = Location.Zero;
                    TargetList = TargetSelectList;
                }
                break;
        }
        NewsLine.Clear();
        if (Game.Mode != eMode.OUTSIDE) CurrentTown.UpdateVisible();
        return true;
    }

    public void PlaceDraggedItem(eAction action)
    {
        bool notenoughap = false, has_equipped = false;
        PCType pcfrom = null, pcto = InventoryTo as PCType;
        var fromequipslot = eEquipSlot.None;

        //If dragging from a shop we must be able to afford to buy it.
        if (InventoryFrom is Shop && InventoryTo is PCType)
        {
            var shop = (Shop)InventoryFrom;
            if (shop.BuyCost(Item.Value) > CurrentParty.Gold)
            {
                AddMessage("You can't afford it.");
                Gui.DragItem = null;
                return;
            }
        }

        //Check where we're moving between is in range of each other.
        if (!InventoryFrom.InventorysClose(InventoryTo))
        {
            AddMessage("Too far away to move item there.");
            return;
        }

        //Check we've got enough AP to complete the move - but don't give up yet as there may be more important reasons why the equip can't be done
        //AP check only an issue in combat and between different inventories
        if (Game.Mode == eMode.COMBAT && InventoryFrom != InventoryTo && CurrentParty.ActivePC.AP < 1)
        {
            notenoughap = true;
        }

        if (Game.Mode == eMode.COMBAT && action == eAction.PlaceInEquipSlot && PC != CurrentParty.ActivePC)
        {
            AddMessage("Only the active character can equip items in combat!");
            return;
        }


        //If DragItem is equipped, go no further if item can't be unequipped
        if (InventoryFrom is PCType)
        {
            pcfrom = (PCType)InventoryFrom;
            if ((fromequipslot = pcfrom.HasEquipped(Item)) != eEquipSlot.None)
            {
                if (!pcfrom.CanUnequip(fromequipslot))
                {
                    AddMessage("Can't unequip");
                    Gui.DragItem = null;
                    return;
                }

                has_equipped = true;
            }
        }

        if (notenoughap)
        {
            AddMessage("Not enough action points!");
            Gui.DragItem = null;
            return;
        }

        if (action == eAction.PlaceInInventory)
        {
            Item replaced = null;

            if (has_equipped)
            {
                if (InventoryTo is Shop)
                {
                    //Drag from Equipment slot to Item Shop
                    if (((Shop)InventoryTo).SellTo(Item))
                    {
                        pcfrom.Unequip(Item);
                    }
                }
                else
                {
                    //Drag from Equipment slot to Inventory
                    pcfrom.Unequip(Item);
                    replaced = InventoryTo.PlaceItem(Item, Loc.X);
                }
            }
            else
            {
                if (InventoryFrom is Shop)
                {
                    if (InventoryTo is Shop)
                    {
                        Gui.DragItem = null;
                        return;
                    }

                    //Drag from Item shop to inventory
                    AddMessage("You buy it.");
                    Sound.Play("015_cash");
                    CurrentParty.Gold -= ((Shop)InventoryFrom).BuyCost(Item.Value);
                    replaced = InventoryTo.PlaceItem(Item.Copy(), Loc.X);
                }
                else
                {
                    if (InventoryTo is Shop)
                    {
                        //Drag from inventory to ItemShop
                        if (((Shop)InventoryTo).SellTo(Item))
                        {
                            InventoryFrom.RemoveItem(Item);
                        }
                    }
                    else
                    {
                        //Drag from inventory to inventory
                        if (InventoryTo.GetSlot(Loc.X) == Item)
                        {
                            //Don't bother if dragging item to itself.
                            Gui.DragItem = null;
                            return;
                        }

                        InventoryFrom.RemoveItem(Item); //Remove dragged item from its old inventory
                        replaced = InventoryTo.PlaceItem(Item, Loc.X);
                    }

                }

            }

            if (replaced != null)
            {
                InventoryTo.RemoveItem(replaced);
                InventoryTo.AddItem(replaced, false);
                Game.StartItemDrag(replaced, InventoryTo, false);
            }
            else
                Gui.DragItem = null;
        }
        else if (action == eAction.PlaceInEquipSlot)
        {
            if (has_equipped)
            {
                //Drag from equipment slot to equipment slot
                if (pcfrom == pcto && EquipSlot == fromequipslot)
                {
                    //Don't bother if dragging item to itself.
                    Gui.DragItem = null;
                    return;
                }


                if (Item.CompatibleSlot(EquipSlot))
                {

                    Item already_equipped;
                    pcto.Equip(Item, EquipSlot, out already_equipped);

                    pcfrom.Unequip(Item);
                    if (already_equipped != null)
                    {
                        Game.StartItemDrag(already_equipped, pcto, false);
                    }
                    else
                        Gui.DragItem = null;
                }
                else
                {
                    Game.AddMessage("Can't equip that there.");
                    return;
                }
            }
            else
            {
                if (InventoryFrom is Shop)
                {
                    //Drag from Shop to Equipment slot
                    if (Item.CompatibleSlot(EquipSlot))//(pcto.CanEquip(Action.Item, Action.EquipSlot) != eEquipSlot.None)
                    {

                        Item already_equipped;
                        pcto.Equip(Item.Copy(), EquipSlot, out already_equipped);

                        AddMessage("You buy it.");
                        Sound.Play("015_cash");
                        CurrentParty.Gold -= ((Shop)InventoryFrom).BuyCost(Item.Value);
                        if (already_equipped != null)
                        {
                            Game.StartItemDrag(already_equipped, pcto, false);
                        }
                        else
                            Gui.DragItem = null;
                    }
                    else
                    {
                        Game.AddMessage("Can't equip that there.");
                        return;
                    }
                }
                else
                {
                    //Drag from inventory to equipment slot

                    if (Item.CompatibleSlot(EquipSlot))
                    {
                        InventoryFrom.RemoveItem(Item);

                        Item already_equipped;
                        pcto.Equip(Item, EquipSlot, out already_equipped);

                        if (already_equipped != null)
                        {
                            Game.StartItemDrag(already_equipped, pcto, false);
                        }
                        else
                            Gui.DragItem = null;
                    }
                    else
                    {
                        Game.AddMessage("Can't equip that there.");
                        return;
                    }
                }
            }
        }

        Sound.ItemSound();
    }
}