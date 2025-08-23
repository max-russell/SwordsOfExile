using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework.Input;

namespace SwordsOfExileGame;

public partial class PartyType : IExpRecipient
{
    public string Name;//, SaveFileName;
    public DateTime LastSavedDate, CreationDate;
    public int Age = 0; //TODO: If age is increased by resting, or a script - make allowances for Timers triggering and interrupting the rest!
    public int Day => Age / Constants.DAY_LENGTH + 1;
    private int gold = Constants.STARTING_GOLD, food = Constants.STARTING_FOOD;
    public int Gold { get => gold;
        set => gold = Maths.MinMax(0, Constants.GOLD_LIMIT, value);
    }
    public int Food { get => food;
        set => food = Maths.MinMax(0, Constants.FOOD_LIMIT, value);
    }

    public int LightLevel = 0;
    public Location OutsidePos; //Temporarily stores Party's outside position when in town mode.
    public Direction outsideDir;
    public int Stealth;
    public int Firewalk;
    public int DetectMonster;

    public bool IsSplit = false;
    public Location SplitPos = Location.Zero;

    public Dictionary<string, Keys> SpellKeyShortcuts = new();

    public Dictionary<string, Recipe> KnownRecipes = new();

    public void SetUpKnownRecipes()
    {
        for (var n = 0; n < KnownRecipes.Count; n++)
        {
            var s = KnownRecipes.ElementAt(n).Key;
            if (Recipe.List.Contains(s)) KnownRecipes[s] = Recipe.List[s];//.Add(MagicSpell.Spells[s]);
        }
    }
    public void LearnRecipe(string id)
    {
        Recipe r;

        if (Recipe.List.TryGetValue(id, out r))
        {
            if (!KnownRecipes.ContainsKey(id))
                KnownRecipes.Add(id, r);
        }
        else
        {
            Game.FlagError("Script Runtime Error", "Recipe with ID '" + id + "' not found in Party.LearnRecipe", Script.FunctionRunning());
        }
    }

    //Interesting stat records
    public long total_dam_done = 0;
    public int total_m_killed = 0;
    public long total_xp_gained = 0;
    public long total_dam_taken = 0;

    private IMap currentMap { get => Game.CurrentMap;
        set => Game.CurrentMap = value;
    }

    public Location Pos {
        get
        {
            try
            {
                switch (Game.Mode)
                {
                    case eMode.COMBAT: return ActivePC.Pos; //Shouldn't really be used for this.
                    case eMode.TOWN: return LeaderPC.Pos;
                    case eMode.OUTSIDE: return LeaderPC.Pos;
                }
            }
            catch (NullReferenceException)
            { }
            return new Location(-1, -1);
        }
        set
        {
            //switch (Game.Mode)
            //{
            //    case eMode.COMBAT:
            //    case eMode.TOWN:
            foreach (var pc in PCList) pc.Pos = value;
            //break;
            //    case eMode.OUTSIDE:
            //        OutsidePos = value;
            //        break;
            //}
        }
    }

    public Direction Direction
    {
        get
        {
            switch (Game.Mode)
            {
                case eMode.COMBAT: return ActivePC.Dir; //Shouldn't really be used for this.
                case eMode.TOWN: return PCList[0].Dir;
                case eMode.OUTSIDE: return ActivePC.Dir;//outsideDir;
            }
            return Direction.None;
        }
        set
        {
            //switch (Game.Mode)
            //{
            //    case eMode.COMBAT:
            //    case eMode.TOWN:
            foreach (var pc in PCList) pc.Dir = value;
            //        break;
            //    case eMode.OUTSIDE:
            //        outsideDir = value;
            //        break;
            //}
        }
    }

    public List<PCType> PCList;

    public PCType CurrentPC //PC currently selected in the stats/inventory window
    {
        get => currentPC;
        set { 
            currentPC = value;

            if (value != null)
            {
                if (Gui.MagicShopIsOpen != null) Gui.MagicShopIsOpen.UpdateSpellList();
                if (MagicWindow.Instance != null) MagicWindow.Instance.UpdateCaster(CurrentPC);
                AlchemyWindow.Update(CurrentPC);
                Game.SetPortraitWindowKeys();
                InventoryWindow.Update();
                StatsWindow.Update();
            }
        }
    }

    private PCType currentPC;

    public PCType ActivePC //PC currently active (only in combat, leader pc otherwise)
    {
        get
        {
            //return activePC;
            if (Game.Mode == eMode.COMBAT) return activePC;
            else return LeaderPC;
        }
        set
        {
            //if ()
            //{
            if (!Game.InMainMenu && value != null && (activePC != value || Gfx.PCHighlightGfx == null)) Gfx.MakeCharacterHighlight(value);
            activePC = value;
            //}
        }
    }

    private PCType activePC;
    public PCType LeaderPC  //The first PC who isn't dead or missing
    {
        get
        {
            foreach (var pc in PCList)
                if (pc != null && pc.IsAlive()) return pc;
            return null;
        }
    }

    public PCType SingleActingPC = null; //When this is set to a PC, only this PC will have her turn during combat, others will skip automatically.
    //Turned on and off with the 'Act' button in combat.


    //Called by scripts
    public bool Split(PCType pc, Location pos) 
    {
        if (IsSplit || pc == null || !PCList.Contains(pc) || pc.LifeStatus != eLifeStatus.ALIVE) return false;

        SplitPos = pc.Pos;
        CurrentPC = pc;
        ActivePC = pc;
        foreach (var pc2 in PCList)
        {
            if (pc2 != pc)
            {
                pc2.BackupLifeStatus = pc2.LifeStatus;
                pc2.LifeStatus = eLifeStatus.ABSENT;
            }
        }
        Pos = pos;
        currentMap.UpdateVisible();
        Gfx.CentreView(pos, false);
        IsSplit = true;
        Script.PreventAction();
        return true;
    }

    public bool Reunite() //Called by scripts
    {
        if (!IsSplit) return false;
        foreach (var pc2 in PCList)
        {
            if (pc2.LifeStatus == eLifeStatus.ABSENT)
            {
                pc2.LifeStatus = pc2.BackupLifeStatus;
            }
        }
        IsSplit = false;
        Pos = SplitPos;
        currentMap.UpdateVisible();
        Gfx.CentreView(Pos, false);
        Script.PreventAction();
        return true;
    }

    public void ReorderPC(PCType pc, int direction)
    {
        if (Game.Mode == eMode.COMBAT) return;
        if (pc.Slot <= 0 && direction == PopUpMenuData.MOVEUPORDER) return;
        if (pc.Slot >= Constants.PC_LIMIT - 1 && direction == PopUpMenuData.MOVEDOWNORDER) return;

        PCList.Remove(pc);
        if (direction == PopUpMenuData.MOVEUPORDER)
            PCList.Insert(pc.Slot - 1, pc);
        else if (direction == PopUpMenuData.MOVEDOWNORDER)
            PCList.Insert(pc.Slot + 1, pc);

        for (var n = 0; n < Constants.PC_LIMIT; n++)
            PCList[n].Slot = n;

        Game.ReOrderPortraits();
    }

    public int TotalLevel
    {
        get
        {
            var j = 0;
            foreach (var pc in EachAlivePC())
                j += pc.Level;
            return j;
        }
    }

    public bool HasTrait(Trait trait)
    {
        foreach (var pc in EachAlivePC())
            if (pc.HasTrait(trait)) return true;
        return false;
    }

    public int GetSkillTotal(eSkill skill)
    {
        var total = 0;
        foreach (var pc in EachAlivePC())
            total += pc.GetSkill(skill);
        return total;
    }


    public void HealAll(int amount, bool silent=false)
    {
        foreach (var pc in EachAlivePC())
            if (!silent) pc.Heal(amount);
            else pc.Health += amount;
        if (!silent) new Animation_Hold();
    }
    public void RestoreSP(int amount)
    {
        foreach (var pc in EachAlivePC())
            pc.SP += amount;
    }

    public void Restore()
    {
        //Completely rejuvenates party and removes all effects.
        foreach (var pc in PCList)
        {
            if (pc.LifeStatus != eLifeStatus.ABSENT)
            {
                pc.LifeStatus = eLifeStatus.ALIVE;
                pc.Health = pc.MaxHealth;
                pc.SP = pc.MaxSP;
                for (var a = 0; a < pc.status.Length; a++)
                    pc.status[a] = 0;
            }
        }
    }
    public void StripItems()
    {
        //Removes items from the party that can't be taken into another scenario.
        //Like items that call a script or cast a spell, or use a custom picture.

        foreach (var pc in PCList)
        {
            for (var a = pc.ItemList.Count - 1; a >= 0; a--)
            {
                var item = pc.ItemList[a];
                item.SpecialClass = 0;

                if (item != null &&
                    ((item.Ability == eItemAbil.CALL_SPECIAL || item.Ability == eItemAbil.CAST_SPELL)
                     || item.Picture >= Constants.ITEM_CUSTOM_PIC_START))
                    pc.ItemList.RemoveAt(a);
            }
            

        }
    }

    /// <summary>
    /// An enumerator that goes through all the pcs currently independent on the map. If the party isn't in combat
    /// this will only be the leader PC, as all the party are on the same spot.
    /// </summary>
    /// <returns></returns>
    public IEnumerable<PCType> EachIndependentPC(bool include_dying = false)
    {
        if (Game.Mode == eMode.COMBAT)
        {
            foreach (var pc in PCList)
                if (pc.IsAlive() || (include_dying && pc.Dying)) yield return pc;
        }
        else
        {
            if (LeaderPC != null) yield return LeaderPC;
        }
    }

    public IEnumerable<PCType> EachAlivePC() {
        foreach (var pc in PCList) if (pc.IsAlive()) yield return pc;
    }

    /// <summary>
    /// Choose a PC who is still alive at random.
    /// </summary>
    /// <returns>Random PC, or null if they're all dead.</returns>
    public PCType RandomPC()
    {
        var live_pcs = PCList.FindAll(n => n.LifeStatus == eLifeStatus.ALIVE);
        if (live_pcs.Count == 0) return null;
        return live_pcs[Maths.Rnd.Next(live_pcs.Count)];
    }

    //public bool PartyToast()
    //{
    //    foreach(PCType pc in EachAlivePC()) {return false;}
    //    return true;
    //}

    public int NoOfLivingPCs
    {
        get
        {
            var amt = 0;
            foreach (var pc in EachAlivePC()) amt++;
            return amt;
        }
    }


    public PCType ClosestPC(Location where) {

        PCType pcclose = null;//_where = new Location(120, 120);

        foreach (var pc in EachIndependentPC()) //(i = 0; i < 6; i++)
            if (pcclose == null || where.DistanceTo(pc.Pos) < where.DistanceTo(pcclose.Pos))
                pcclose = pc;
        return pcclose;//  pc_where;
    }

    public int Flying;// { get {return vogelsExtraShit[5, 1];} set {vogelsExtraShit[5,1] = (byte)value;} }
    public bool IsInABoat() { return Vehicle != null && Vehicle.Type == eVehicleType.BOAT; }
    public bool IsOnAHorse() { return Vehicle != null && Vehicle.Type == eVehicleType.HORSE; }
    public Vehicle Vehicle = null;
    public void BoardVehicle(Vehicle v) { Vehicle = v; MenuBarWindow.CombatEnabled = false; Game.AddMessage(v.BoardMessage()); }
    public void LeaveVehicle() { if (Vehicle != null) Game.AddMessage(Vehicle.LeaveMessage()); Vehicle = null; MenuBarWindow.CombatEnabled = true; }

    public PartyType() {

        //Initialise to default settings
        CreationDate = DateTime.Now;
        Name = "The Merry Marauders";
        Age = 0;
        gold = Constants.STARTING_GOLD;
        food = Constants.STARTING_FOOD;
        LightLevel = 0;

        //Create default pcs.
        PCList = new List<PCType>();
        for (var i = 0; i < Constants.PC_LIMIT; i++)
            PCList.Add(new PCType(i));
        CurrentPC = LeaderPC;
        ActivePC = LeaderPC;
    }

    public IEnumerable<PCType> GetPCDrawOrder()
    {
        if (Game.Mode != eMode.COMBAT)
        {
            foreach (var pc in PCList)
                if (!(pc.AnimAction == null))
                {
                    yield return pc;
                    yield break;
                }

            if (LeaderPC != null && (LeaderPC.IsAlive())) 
                yield return LeaderPC;
        }
        else
        {
            //We'll make a temporary list of the pcs to draw in the order to draw them (so PCs drawn last will be on top)
            var list = new List<PCType>();

            //First add PCs that are doing some animation.
            foreach (var pc in PCList)
            {
                if (pc.AnimAction != null || pc.AnimFlash != null)
                    list.Add(pc);
            }

            //Under them should be the active PC
            if (activePC != null && !list.Contains(activePC))
                list.Insert(0,activePC);

            //And before that the rest of the PCs
            foreach (var pc in PCList)
            {
                if ((pc.IsAlive() || pc.Dying) && !list.Contains(pc))
                    list.Insert(0,pc);
            }

            foreach (var pc in list)
            {
                yield return pc;
            }
        }
    }

    public void GiveNewItem(string item_id, bool identified = false, int charges = -1)
    {
        if (currentPC == null)
            LeaderPC.GiveNewItem(item_id, identified, charges);
        else
            CurrentPC.GiveNewItem(item_id, identified, charges);
    }

    /// <summary>
    /// Returns the number of items of a certain held by everyone in the party.
    /// </summary>
    /// <param name="cls"></param>
    /// <param name="and_remove"></param>
    /// <returns></returns>
    public int CountItemClass(int cls, bool and_remove)
    {
        var count = 0;
        foreach (var pc in EachAlivePC())
        {
            for (var n = pc.ItemList.Count - 1; n >= 0; n--)
                if (pc.ItemList[n].SpecialClass == cls)
                {
                    count++;
                    if (and_remove) pc.ItemList.RemoveAt(n);
                }

            for (var n = 0; n < pc.EquippedItemSlots.Length; n++)
                if (pc.EquippedItemSlots[n] != null && pc.EquippedItemSlots[n].SpecialClass == cls)
                {
                    count++;
                    if (and_remove) pc.Unequip(pc.EquippedItemSlots[n],true);// = null;
                }
        }
        return count;
    }

    /// <summary>
    /// Returns the number of items of a certain equipped by everyone in the party.
    /// </summary>
    /// <param name="cls"></param>
    /// <param name="and_remove"></param>
    /// <returns></returns>
    public int CountItemClassEquipped(int cls, bool and_remove)
    {
        var count = 0;
        foreach (var pc in EachAlivePC())
        {
            for (var n = 0; n < pc.EquippedItemSlots.Length; n++)
                if (pc.EquippedItemSlots[n].SpecialClass == cls)
                {
                    count++;
                    if (and_remove) pc.Unequip(pc.EquippedItemSlots[n], true);
                }
        }
        return count;
    }

    public bool IdentifyItemRoll()
    {
        int[] id_odds = {0,10,15,20,25,30,35,39,43,47,
            51,55,59,63,67,71,73,75,77,79,81};

        foreach (var pc in EachAlivePC())
            if (Maths.Rand(1, 0, 100) < id_odds[pc.GetSkill(eSkill.ITEM_LORE)])
                return true;
        return false;
    }


    public void EndCombat()
    {
        SingleActingPC = null;

        var pc = RandomPC();
        foreach (var pc2 in EachAlivePC())
        {
            if (pc2 != pc)
            {
                new Animation_Move(pc2, pc2.Pos, pc.Pos, false);//, 0.1f);
                pc2.PositionPConPC(pc);
            }
            pc2.Parry = 0;
        }
        Sound.Play(93);
        ActivePC = LeaderPC;
        Gfx.CentreView(ActivePC.Pos, false);
        Game.CurrentTown.UpdateVisible();
    }

    public void MoveToMap(IMap map)
    {
        Game.CurrentMap = map;
        currentMap = map;
        if (map is TownMap)
        {
            Game.Mode = eMode.TOWN;
            map = Script.RunTownPreEntry(Scenario.TownPreEntryFunc, (TownMap)map);
            Game.CurrentMap = map;
            currentMap = map;
            var town = (TownMap)map;
            if (Vehicle != null)
            {
                Vehicle.Map = map;
                Vehicle.Pos = Pos;
            }

            if (!Game.RecentTownList.Contains(town))
            {
                Game.RecentTownList.Add(town);
                if (Game.RecentTownList.Count > Constants.TOWN_VISIT_MEMORY)
                    Game.RecentTownList.RemoveAt(0);
                town.Enter(true);
            }
            else
                town.Enter(false);
        }
        else
        {
            if (Vehicle != null)
            {
                Vehicle.Map = map;
                Vehicle.Pos = Pos;
            }
            Game.Mode = eMode.OUTSIDE;
            map.Enter(false);
        }

        Script.PreventAction();
        Gfx.CentreView(Pos, true);
        currentMap.UpdateVisible();
        Animation.CancelAll();
        new Animation_FadeUp(300);
    }

    public bool Move(Location mod)
    {
        var movepc = ActivePC;

        if (Game.Mode != eMode.COMBAT)
        {
            //In case the leader has changed, make sure all PCs are on the same spot as the one that just moved.
            foreach (var pc in PCList)
            {
                pc.PositionPConPC(movepc);
            }
        }

        return movepc.Move(mod);
    }

    public void Reposition(Location pos)
    {
        if (Game.Mode == eMode.COMBAT) return;
        Pos = pos;
        currentMap.UpdateVisible();
        Gfx.CentreView(Pos, false);
    }

    /// <summary>
    /// Damages either all the PCs in the party, or just the active one if in combat mode. To be used for things like stepping on damaging tiles that
    /// hurt the PC(s) moving onto it. Not for when, for instance, an npc picks a specific PC to attack.
    /// </summary>
    /// <param name="how_much"></param>
    /// <param name="dam_type"></param>
    /// <param name="force_everyone"></param>
    public void DamageActive(int how_much, eDamageType dam_type)
    {
        var someone = false;
        if (Game.Mode == eMode.COMBAT)
            someone = activePC.Damage(null, how_much, 0, dam_type);
        else foreach (var pc in EachAlivePC())
            someone |= pc.Damage(null, how_much, 0, dam_type);
        if (someone) new Animation_Hold();
    }

    /// <summary>
    /// Damages all living PCs in the party.
    /// </summary>
    /// <param name="how_much"></param>
    /// <param name="dam_type"></param>
    public bool Damage(int how_much, eDamageType dam_type)
    {   var someone = false;
        foreach (var pc in EachAlivePC())
            someone |= pc.Damage(null, how_much, 0, dam_type);
        if (someone) new Animation_Hold();
        return false;
    }

    /// <summary>
    /// Returns true if there are no PCs left to move
    /// </summary>
    /// <returns></returns>
    public void StartNewTurn() {

        if (Game.Mode != eMode.COMBAT)
        {
            ActivePC.AP = 1;
            return;
        }

        foreach (var pc in EachAlivePC()) {
            pc.ResetCombatVars();
            pc.set_pc_moves();
        }

        return;

    }

    public bool DoWait()
    {
        if (SingleActingPC == ActivePC) return false;

        foreach (var pc in EachAlivePC())
        {
            if (pc.Slot > ActivePC.Slot && pc.AP > 0)
            {
                Gfx.CentreView(pc.Pos, false);
                Game.AddMessage("Wait: " + ActivePC.Name + " delays acting.");
                ActivePC = pc; return true;
            }
        }
        foreach (var pc in EachAlivePC())
        {
            if (pc.Slot < ActivePC.Slot && pc.AP > 0)
            {
                Gfx.CentreView(pc.Pos, false);
                Game.AddMessage("Wait: " + ActivePC.Name + " delays acting.");
                ActivePC = pc; return true;
            }
        }
        Game.AddMessage("Wait: " + ActivePC.Name + " is the last to move.");
        return false;
    }

    public void DoAct()
    {
        if (SingleActingPC == null)
        {
            Game.AddMessage("Only " + ActivePC.Name + " now active.");
            SingleActingPC = ActivePC;
        }
        else
        {
            Game.AddMessage("All characters now active.");
            SingleActingPC = null;
        }
    }

    /// <summary>
    /// Finds out if the party has fled combat. For this to be the case, no PCs must be ALIVE, and at least 1 must be FLED
    /// </summary>
    /// <returns></returns>
    public bool PartyFled()
    {
        var somefled = false;
        foreach (var pc in PCList)
        {
            if (pc.LifeStatus == eLifeStatus.ALIVE) return false;
            if (pc.LifeStatus == eLifeStatus.FLED) somefled = true;
        }
        return somefled;
    }

    // Find next active PC in combat mode, return TRUE if monsters need running, and run monsters is slow spells
    // active
    public Boolean PickNextPC() {

        if (activePC == null)
            activePC = LeaderPC;

        if (Game.Mode != eMode.COMBAT) return false;

        var s = activePC.Slot;

        // Find next PC with moves
        activePC = null;

        //Find next PC with AP remaining AFTER this one in the party order.
        foreach (var pc in EachAlivePC()) {
            if (pc.Slot >= s && pc.AP > 0) {
                if (SingleActingPC != null && SingleActingPC != pc) continue;
                ActivePC = pc; break;
            }
        }

        if (activePC == null) {

            //If none found, look for one BEFORE this one in the party order.
            foreach (var pc in EachAlivePC())
            {
                if (pc.Slot < s && pc.AP > 0)
                {
                    if (SingleActingPC != null && SingleActingPC != pc) continue;
                    ActivePC = pc; break;
                }
            }

            //If no character found with action points, turn must be over.
            if (activePC == null)
            {
                ActivePC = LeaderPC;
                return true; //NPCs' turn;
            }
        }

        CurrentPC = ActivePC;
        return false;
    }

    public void AwardXP(int amount)
    {
        foreach (var pc in EachAlivePC())
            pc.AwardXP(amount);
    }

    public bool IncreaseAge() //Return true if a timer has triggered a script.
    {
        var old_age = Age;
        // Increase age, adjust light level & stealth
        var store_day = Day;
        if (Game.Mode == eMode.OUTSIDE) {
            //Outside, if not on a horse, Age is rounded down to the nearest multiple of 10, and then goes up by 10 each turn.
            //One a horse, age is rounded down to the nearest multiple of 5, and then goes up by 5 each turn.

            if (!IsOnAHorse())
            {
                Age -= Age % 10;
                Age += 10;
            }
            else
            {
                Age -= Age % 5;
                Age += 5;
            }
        }
        else 
            Age++;

        Maths.MoveToZero(ref LightLevel);

        // Party spell effects
        if (Stealth == 1) Game.AddMessage("Your footsteps grow louder.");
        Maths.MoveToZero(ref Stealth);

        if (DetectMonster == 1) Game.AddMessage("You stop detecting monsters.");
        Maths.MoveToZero(ref DetectMonster);

        if (Firewalk == 1) Game.AddMessage("Your feet stop glowing");
        Maths.MoveToZero(ref Firewalk);

        if (Flying == 2)
        {
            Game.AddMessage("You are starting to descend.");
            Maths.MoveToZero(ref Flying);
        }
        else if (Flying == 1)
        {
            Maths.MoveToZero(ref Flying);
            if (!currentMap.CharacterCanBeThere(Pos, LeaderPC))
            {
                Game.AddMessage("You plummet to your deaths.");
                new Animation_Death(LeaderPC);
                LeaderPC.Dying = true;
                foreach (var pc in PCList)
                {
                    pc.LifeStatus = eLifeStatus.DEAD;
                }
                Game.PartyDead = true;
                InventoryWindow.Close();
                StatsWindow.Close();
                return true;
            }
            else
                Game.AddMessage("You land safely.");
        }
        else
            Maths.MoveToZero(ref Flying);

        if (currentMap is TownMap) ((TownMap)currentMap).UpdateLightLevel();

        // Got a radioactive bar or whatnot.
        if (Age % 500 == 0 && Maths.Rand(1,0,5) == 3 && HasItemWithAbility(eItemAbil.DISEASE_PARTY)) {
            foreach(var pc in EachAlivePC())
                pc.Disease(2, true);
        }

        // Plants and magic shops
        Shop.RestockAll(Age);

        // Protection, etc.
        foreach(var pc in EachAlivePC()) { // Process some status things, and check if stats updated
                
            pc.CounteractStatus(eAffliction.INVULNERABLE);
            pc.CounteractStatus(eAffliction.MAGIC_RESISTANCE);
            pc.CounteractStatus(eAffliction.INVISIBLE);
            pc.CounteractStatus(eAffliction.MARTYRS_SHIELD);
            pc.CounteractStatus(eAffliction.ASLEEP);
            pc.CounteractStatus(eAffliction.PARALYZED);
            if (Age % 40 == 0 && pc.Status(eAffliction.POISONED_WEAPON) > 0) {
                pc.CounteractStatus(eAffliction.POISONED_WEAPON);
            }
        }

        // Food
        if (Age % 1000 == 0 && Game.Mode != eMode.COMBAT) {
            food -= NoOfLivingPCs;
            if (food < 0)
            {
                food = 0;
                Game.AddMessage("Starving!");
                Damage(Maths.Rand(3,1,6),eDamageType.UNBLOCKABLE);
            }
            else
            {
                Sound.Play(6);
                Game.AddMessage("You eat.");
            }
        }

        // Poison, acid, disease damage
        if (AnyoneHas(eAffliction.POISON))
            if ((Game.Mode == eMode.OUTSIDE && (Age % 50) == 0) || (Game.Mode != eMode.OUTSIDE && (Age % 20) == 0))
                HandlePoison();

        if (AnyoneHas(eAffliction.DISEASE))
            if ((Game.Mode == eMode.OUTSIDE && (Age % 100) == 0) || (Game.Mode != eMode.OUTSIDE && (Age % 25) == 0))
                HandleDisease();

        if (AnyoneHas(eAffliction.ACID))
            HandleAcid();

        // Healing and restoration of spell pts.
        if (Game.Mode == eMode.OUTSIDE) 
        {
            if (Age % 100 == 0) HealAll(2,true);
        }
        else 
        {
            if (Age % 50 == 0) HealAll(1,true);
        }
        if (Game.Mode == eMode.OUTSIDE) 
        {
            if (Age % 80 == 0) RestoreSP(2);
        }
        else 
        {
            if (Age % 40 == 0) RestoreSP(1);
        }

        // Recuperation and chronic disease disads
        foreach (var pc in EachAlivePC())
        {
            if (pc.HasTrait(Trait.Recuperation) && Maths.Rand(1,0,10) == 1 && pc.Health < pc.MaxHealth)
                pc.Heal(2);
            if (pc.HasTrait(Trait.ChronicDisease) && Maths.Rand(1, 0, 110) == 1)
                pc.Disease(4);
        }

        // Blessing, slowed,etc.
        if (Age % 4 == 0)
            foreach(var pc in EachAlivePC())
            {
                pc.CounteractStatus(eAffliction.BLESS_CURSE);
                pc.CounteractStatus(eAffliction.HASTE_SLOW);
                Item item;

                if ((item = pc.HasItemEquippedWithAbility(eItemAbil.REGENERATE)) != null
                    && pc.Health < pc.MaxHealth
                    && (Game.Mode != eMode.OUTSIDE || Maths.Rand(1,0,10) == 5)) 
                {
                    var j = Maths.Rand(1,0,item.AbilityStrength / 3);
                    if (item.AbilityStrength / 3 == 0)
                        j = Maths.Rand(1,0,1);
                    if (Game.Mode == eMode.OUTSIDE) j *= 4;
                    pc.Heal(j);
                }
            }

        if (currentMap is TownMap) ((TownMap)currentMap).ProcessFields();

        return Timer.Update(Age - old_age);
    }

    public Boolean DayReached(int which_day, string which_event)
        // which_day is day event should happen
        // which_event is the party.key_times value to cross reference with. 
        // if the key_time is reached before which_day, event won't happen
        // if it's 8, event always happens
        // which_day gets an extra 20 days to give party bonus time (NO IT DOESN'T - THIS IS AUTOMATICALLY ADDED ON WHEN OLD SCENARIOS ARE CONVERTED)
    {
        if (which_day == -1) return false;

        var v = GlobalVariables.Get(which_event);

        if (Day < which_day || (v > 0 && v < which_day)) return false;
        return true;
    }

    private void HandlePoison()
    {
        Game.AddMessage("Poison:");
        foreach (var pc in EachAlivePC())
        {   
            var p = pc.Status(eAffliction.POISON);
            if (p > 0)
            {
                if (pc.Damage(null, Maths.Rand(p,1,6), 0, eDamageType.POISON)) new Animation_Hold();
                if (Maths.Rand(1, 0, 8) < 6) pc.DecStatus(eAffliction.POISON, 1, 0);
                if (Maths.Rand(1, 0, 8) < 6 && pc.HasTrait(Trait.Constitution)) pc.DecStatus(eAffliction.POISON, 1, 0);
            }
        }
    }

    private void HandleDisease()
    {
        Game.AddMessage("Disease:");
        foreach (var pc in EachAlivePC())
        {
            if (pc.Status(eAffliction.DISEASE) <= 0) continue;

            switch (Maths.Rand(1, 1, 10))
            {
                case 1:
                case 2:
                    pc.Poison(2);
                    break;
                case 3:
                case 4:
                    pc.Slow(2);
                    break;
                case 5:
                    pc.DrainXP(5);
                    break;
                case 6:
                case 7:
                    pc.Curse(3);
                    break;
                case 8:
                    pc.Dumbfound(3);
                    break;
                case 9:
                case 10:
                    Game.AddMessage("  " + pc.Name + " unaffected. ");
                    break;
            }

            var r1 = Maths.Rand(1, 0, 7);
            if (pc.HasTrait(Trait.Constitution)) r1 -= 2;
            if (r1 <= 0 || pc.HasItemEquippedWithAbility(eItemAbil.PROTECT_FROM_DISEASE) != null)
                pc.DecStatus(eAffliction.DISEASE, 1, 0);
        }
    }

    private void HandleAcid()
    {
        Game.AddMessage("Acid:");
        foreach (var pc in EachAlivePC())
        {
            var p = pc.Status(eAffliction.ACID);
            if (p > 0)
            {
                if (pc.Damage(null, Maths.Rand(p,1,6), 0, eDamageType.MAGIC)) new Animation_Hold();
                pc.DecStatus(eAffliction.ACID, 1, 0);
            }
        }
    }

    public bool HasItemWithAbility(eItemAbil abil)
    {
        foreach(var pc in EachAlivePC())
            if (pc.HasItemWithAbility(abil) != null) return true;
        return false;
    }

    public bool AnyoneHas(eAffliction stat, bool inc_pos = true, bool inc_neg = false)
    {
        foreach (var pc in EachAlivePC())
        {
            var i = pc.Status(stat);
            if (inc_pos && i > 0) return true;
            if (inc_neg && i < 0) return true;
        }
        return false;
    }

    public bool CanRest()
    {
        if (Game.Mode != eMode.OUTSIDE) return false; //Just in case.

        var ter = Game.WorldMap.TerrainAt(Pos);
        if (IsInABoat())
        {
            Game.AddMessage("Rest:  Not in boat.");
            return false;
        }
        else if (AnyoneHas(eAffliction.POISON))
        {
            Game.AddMessage("Rest: Someone poisoned.           ");
            return false;
        }
        else if (Food <= 12)
        {
            Game.AddMessage("Rest: Not enough food.            ");
            return false;
        }
        else if (Game.WorldMap.NPCGroupInRange(3))
        {
            Game.AddMessage("Rest: Monster too close.            ");
            return false;
        }
        else if (ter.Special >= eTerSpec.DOES_FIRE_DAMAGE && ter.Special <= eTerSpec.DISEASED_LAND)
        {
            Game.AddMessage("Rest: It's dangerous here.");////
            return false;
        }
        else if (Flying > 0)
        {
            Game.AddMessage("Rest: Not while flying.           ");
            return false;
        }
        return true;
    }

    public void DoRest()
    {
        var i = 0;

        Game.AddMessage("Resting...                    ");
        Sound.Play(20);
        Food -= 6;

        while (i < 50)
        {
            var timed_special_happened = IncreaseAge();// increase_age();

            if (Maths.Rand(1, 1, 2) == 2)
                Game.WorldMap.MoveNPCsDuringRest();

            if (Maths.Rand(1, 1, 70) == 10)
                Game.WorldMap.SpawnWanderingGroup();

            if (Game.WorldMap.NPCGroupInRange(3))
            {
                i = 200;
                Game.AddMessage("  Monsters nearby.");
            }
            if (timed_special_happened && Constants.COMPATIBILITY_SPECIALS_INTERRUPT_REST)
            {
                i = 200;
                Game.AddMessage("  Rest interrupted.");
            }
            else i++;
        }
        if (i == 50)
        {
            if (Constants.COMPATIBILITY_CHECK_TIMERS_WHILE_RESTING)
            {
                for (i = 0; i < 115; i++)
                {
                    Age += 10;
                    // Specials countdowns
                    if (Age % 500 == 0 && Maths.Rand(1, 0, 5) == 3 && this.HasItemWithAbility(eItemAbil.DISEASE_PARTY))
                    {
                        i = 200;
                        foreach (var pc in EachAlivePC()) pc.Disease(2);
                    }
                    // Plants and magic shops
                    Shop.RestockAll(Age);

                    var timed_special_happened = Timer.Update(10);//don't delay the trigger of the special, if there's a special

                    if (timed_special_happened && Constants.COMPATIBILITY_SPECIALS_INTERRUPT_REST)
                    {
                        i = 200;
                        Game.AddMessage("  Rest interrupted.");
                    }
                }
                if (i == 115)
                {
                    Game.AddMessage("  Rest successful.                ");
                    HealAll(Maths.Rand(5, 1, 10), true);
                    RestoreSP(50);
                }
            }
            else
            {
                Age += 1200;
                Game.AddMessage("  Rest successful.                ");
                HealAll(Maths.Rand(5, 1, 10), true);
                RestoreSP(50);
            }
        }

    }



}