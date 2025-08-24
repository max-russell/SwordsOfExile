//#define SUPER_DEFAULT_PCS //This makes the default prefabricated PCs high level, for testing purposes

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

public partial class PCType : IInventory, ICharacter, IExpRecipient, IAnimatable
{
    private PartyType Party => Game.CurrentParty;

    //MY STUFF
    public int Slot = 0; //Keep a record of what slot this PC is in.
    public int AP {get => actionPoints;
        set => actionPoints = Maths.Max(0, value);
    } //Keeps track of PC's action points (Vogel stores this outside in pc_moves[])

    private int actionPoints;
    public int Parry; //Vogel stores outside in pc_parry. I don't. Because I'm not stupid.
    public int MarkedDamage;
    public eAttitude MyAttitude() { return eAttitude.FRIENDLY; }
    public bool AlliedWith(ICharacter ch)
    {
        return ch.MyAttitude() == eAttitude.FRIENDLY || ch.MyAttitude() == eAttitude.NEUTRAL;
    }
    public bool NotDrawn { get; set; } = false; //Temporarily don't draw (used in teleporting animations)

    public int Provocation; //This is calculated at the end of every npcs turn based on what it did that turn. Attacking or casting a spell is a big provocation.
    //But if the pc does nothing attention-grabbing it decays back to 0 gradually.
    public ICharacter LastAttacked; //Did the pc attack another character last turn? Used when an enemy npc is deciding who to target.

    public int Width => 1;
    public int Height => 1;

    public int TargetingNum { get; set; } //Used when the player is targeting for firing an arrow / spell etc, so that the player can press a key to select this NPC

    public int Portrait;

    public void MakePCGraphics()
    {
        Gfx.MakePCGraphics(which_graphic, Portrait, out PCTexture, out PortraitTexture);
    }

    private eItemFilter _Filter;
    public eItemFilter Filter { get => _Filter;
        set 
        { 
            foreach (var pc in Party.EachAlivePC())
                pc._Filter = value;
        } 
    }

    public Texture2D PCTexture, PortraitTexture;

    //VOGEL'S STUFF
    public eLifeStatus LifeStatus, 
        BackupLifeStatus;//Used when the party splits, to store what member's status was before it was 'ABSENT'
    public string LifeStatusString
    {
        get
        {
            switch (LifeStatus)
            {
                case eLifeStatus.ALIVE:
                    return "ALIVE";
                case eLifeStatus.DEAD:
                    return "DEAD";
                case eLifeStatus.DUST:
                    return "DUST";
                case eLifeStatus.STONE:
                    return "STONE";
                default:
                    return "ABSENT";
            }
                
        }
    }


    public string Name { get; set; } = "";

    private int[] skills = new int[30];
    private int experience;
    public int Level { get; set; }

    private int cur_health, cur_sp;
    private int skill_pts;
    public int[] status = new int[15];

    public string DeathSound => "021_pcdying";

    public void SetSkill(eSkill what, int value) 
    {
        if (what < eSkill.NOT_REALLY_SKILLS) skills[(int)what] = value;
        else if (what == eSkill.HEALTH) { MaxHealth = value; cur_health = value; }
        else { MaxSP = value; cur_sp = value; }
    }
    public int GetSkill(eSkill what) 
    { 
        if (what < eSkill.NOT_REALLY_SKILLS) return skills[(int)what];
        if (what == eSkill.HEALTH) return MaxHealth; //This is only for the sake of the Stat Window Control
        return MaxSP;
    }

    private static int[] skillCosts = {3,3,3,2,2,2, 1,2,2,6, 5, 1,2,4,2,1, 4,2,5};
    private static int skillCostHealth = 1, skillCostSpellPts = 1;
    public int GetSkillCost(eSkill what)
    {
        if (what < eSkill.NOT_REALLY_SKILLS) return skillCosts[(int)what];
        if (what == eSkill.HEALTH) return skillCostHealth; //This is only for the sake of the Stat Window Control
        return skillCostSpellPts;
    }

    private static int[] skillPrices =  {50,50,50,40,40,40,30,50,40,250,250,25,100,200,30,20,100,80,0};
    private static int skillPriceHealth = 10, skillPriceSpellPts = 15;
    public int GetSkillPrice(eSkill what)
    {
        if (what < eSkill.NOT_REALLY_SKILLS) return skillPrices[(int)what];
        if (what == eSkill.HEALTH) return skillPriceHealth; //This is only for the sake of the Stat Window Control
        return skillPriceSpellPts;
    }


    public int Health { get => cur_health;
        set => cur_health = Maths.MinMax(0, MaxHealth, value);
    }
    public int MaxHealth { get; private set; }

    public int SP { get => cur_sp;
        set => cur_sp = Maths.MinMax(0, MaxSP, value);
    }
    public int MaxSP { get; private set; }

    public int SkillPoints { get => skill_pts;
        set { skill_pts = value; if (skill_pts < 0) skill_pts = 0; } }
    public bool Dying; //Set when a player's death animation runs, so the game keeps drawing the pc regardless of its main status

    public string[] AfflictionHlp = 
    {"Weapons are poisoned by using any poison held in a player's inventory. Poisoned weapons poison an enemy when it hits, but the poison wears off with each successive hit.",
        "A blessed character finds everything much easier - they will deal more damage to enemies and avoid damage in turn. Cursing is the opposite of blessing, and the two counteract each other.",
        "A character afflicted by poison will gradually lose health until the effect wears off or they are cured by a spell or potion.",
        "A character who has been hasted moves much faster in combat and has more action points to spend. Conversely, a character who has been Slowed loses action points, and may miss their turn completely.",
        "Invulnerable characters are much more resistant to damage of all kinds.",
        "Magic resistance reduces damage from magical sources.",
        "A webbed character finds it difficult to move and consequently loses action points in combat. If the character waits instead of performing an action they clean the webbing off.",
        "Disease regularly afflicts the character with other harmful ailments. It will wear off eventually but the right spell or potion can speed the process.",
        "Invisible characters won't be attacked by enemies for a while. But attacking someone will immediately make the character reappear.",
        "Dumbfounded characters find it much harder to cast spells. The effect won't wear off on its own - if you cast a spell to remove it, use a scroll or seek out a healer in town.",
        "Martyr's Shield magically reciprocates damage suffered in melee combat to the character's attacker.",
        "When a character is asleep they can't move or defend themselves (obviously). Being hit by something does tend to restore consciousness.",
        "Paralyzed characters find their movement severely restricted",
        "When a character is covered with acid they will suffer considerable damage every turn until it wears off."
    };

    public int Status(eAffliction type) { return status[(int)type]; } //ICharacter
    public void SetStatus(eAffliction type, int val, int min = int.MinValue, int max = int.MaxValue) { status[(int)type] = Maths.MinMax(min,max,val); }
    public void IncStatus(eAffliction type, int val, int max = int.MaxValue)
    {
        status[(int)type] += val;
        if (status[(int)type] > max) status[(int)type] = max;
    }
    public void DecStatus(eAffliction type, int val, int min = int.MinValue)
    {
        status[(int)type] -= val;
        if (status[(int)type] < min) status[(int)type] = min;
    }
    public void CounteractStatus(eAffliction type, int amount=1)
    {
        if (status[(int)type] > amount) status[(int)type]-=amount;
        else if (status[(int)type] < -amount) status[(int)type] += amount;
        else status[(int)type] = 0;
    }

    public static string StatusMsg(ICharacter ch, eAffliction type)
    {
        var degree= "";
        var n = ch.Status(type);
        if (n == 0) return degree;
        if (n is >= 6 or <= -6)  degree = "(Strong)";
        else if (n is >= 3 or <= -3) degree = "(Moderate)";
        else degree = "(Weak)";

        switch (type)
        {
            case eAffliction.POISONED_WEAPON: return "Poisoned Weapon " + degree;
            case eAffliction.BLESS_CURSE: 
                if (n < 0) return "Cursed " + degree;
                else return "Blessed " + degree;
            case eAffliction.POISON:
                return "Poisoned " + degree;
            case eAffliction.HASTE_SLOW:
                if (n < 0) return "Slowed " + degree;
                else return "Hastened " + degree;
            case eAffliction.INVULNERABLE:
                return "Invulnerable " + degree;
            case eAffliction.MAGIC_RESISTANCE:
                return "Magic Resistant " + degree;
            case eAffliction.WEBS:
                return "Webbed " + degree;
            case eAffliction.DISEASE:
                return "Diseased " + degree;
            case eAffliction.INVISIBLE:
                return "Invisible " + degree;
            case eAffliction.DUMB:
                return "Dumbfounded " + degree;
            case eAffliction.ASLEEP:
                return "Asleep " + degree;
            case eAffliction.MARTYRS_SHIELD:
                return "Martyr's Shield " + degree;
            case eAffliction.PARALYZED:
                return "Paralyzed";
            case eAffliction.ACID:
                return "Covered in Acid " + degree;
        }
        return "";
    }

    public string MainStatusMessage()
    {
        switch (LifeStatus)
        {
            case eLifeStatus.ABSENT: return "Missing";
            case eLifeStatus.DUST: return "Dust";
            case eLifeStatus.FLED: return "Fled";
            case eLifeStatus.STONE: return "Petrified";
            case eLifeStatus.SURFACE: return "On Surface";
            case eLifeStatus.WON: return "Won";
            case eLifeStatus.DEAD: return "Deceased";
            default: return "Alive";
        }
    }

    public bool IsVisible() { return true; }
    public List<Item> ItemList = new();
    public Item[] EquippedItemSlots = new Item[13];
    public Item PoisonedWeapon;
    public Dictionary<string, MagicSpell> KnownSpells = new();
 
    public void LearnSpell(string id)
    {
        MagicSpell m;

        if (MagicSpell.List.TryGetValue(id, out m))
        {
            if (!KnownSpells.ContainsKey(id))
                KnownSpells.Add(id, m);
        }
        else
        {
            Game.FlagError("Script Runtime Error", "Spell with ID '" + id + "' not found in PCType.LearnSpell", Script.FunctionRunning());
        }
    }

    public int which_graphic;
    public List<Trait> Traits = new();
    public bool HasTrait(Trait t) { return Traits.Contains(t); }

    public int exp_adj;
    private Direction direction;

    private static short[] hitChance = {20,30,40,45,50,55,60,65,69,73,
        77,81,84,87,90,92,94,96,97,98,99
        ,99,99,99,99,99,99,99,99,99,99
        ,99,99,99,99,99,99,99,99,99,99,
        99,99,99,99,99,99,99,99,99,99};

    public Direction Dir
    { get => direction;
        set => direction.Dir = value.Dir;
    }

    public void PositionPConPC(PCType pc)
    {
        pos = pc.pos;
        direction = pc.direction;
    }

    public bool OnSpace(Location loc) {return loc == Pos;}

    public bool TurnFinished => AP == 0;

    //Returns all items, whether equipped or in main inventory
    public IEnumerable<Item> EachItemHeld()
    {
        foreach (var i in ItemList) yield return i;
        foreach (var i in EquippedItemSlots) if (i != null) yield return i;
    }

    public Location Pos { get => pos;
        set => pos = value;
    } //PC's current position 

    private Location pos;
    public IAnimCharacter AnimAction { get; set; }

    public IAnimCharacter AnimFlash { get; set; }

    private TownMap curTown => Game.CurrentMap as TownMap;

    public string TooltipInfo(bool brief)
    {
        if (brief)
            return Name;

        var txt = string.Format("@b{0}@e@n  @9@iLevel: {1}@n  Exp: {2}\\{3}@n  Health: {4}\\{5}@n  Mana: {6}\\{7}",
            Name,
            Level,
            LevelExperience,
            ExperienceToNextLevel,
            Health,
            MaxHealth,
            SP,
            MaxSP);

        return txt;
    }

    public void GiveNewItem(string item_id, bool identified = false, int charges = -1)
    {
        Item item;

        if (Item.List.TryGetValue(item_id, out item))
        {
            item = item.Copy(identified, charges);

            if (!identified && Party.IdentifyItemRoll()) item.Identified = true;

            AddItem(item, true);
            Game.AddMessage(string.Format("  {0} gets {1}.", Name, item.KnownName));
        }
        else
        {
            Game.FlagError("Script Runtime Error", "Item with ID '" + item_id + "' not found.", Script.FunctionRunning());
        }
    }

    #region INVENTORY STUFF

    /// <summary>
    /// Returns all items in the inventory, and the slot number too
    /// </summary>
    /// <returns></returns>
    public IEnumerable<Tuple<Item, int>> EachItem()
    {
        foreach(var n in ItemList)
        {
            if (n.Filter(_Filter)) yield return new Tuple<Item, int>(n, _Filter == eItemFilter.ALL ? n.Pos.X : n.Pos.Y);
        }
    }

    /// <summary>
    /// IInventory function. Places an item in the inventory and returns the one it replaces at the slot (or null if not)
    /// </summary>
    /// <param name="item">Item to place</param>
    /// <param name="slotno">Slot to place in. 
    /// If an item is alread in the slot, it returns it with the function, but doesn't remove it from the inventory itself</param>
    /// If the item can combine with the item in the slot, it does so.
    /// <returns>The item that was previously in the slot, or null</returns>
    public Item PlaceItem(Item item, int slotno)
    {
        if (slotno == -1 || (_Filter != eItemFilter.ALL && item.GetFilterGroup() != _Filter)) 
        { 
            AddItem(item, true); 
            return null; 
        }

        var replaces = GetSlot(slotno);

        if (item != null) {

            if (item.CombinableWith(replaces))
            {
                item.Charges += replaces.Charges;
                if (item.Charges > Constants.ITEM_STACK_LIMIT)
                {
                    replaces.Charges = item.Charges - Constants.ITEM_STACK_LIMIT;
                    item.Charges = Constants.ITEM_STACK_LIMIT;
                }
                else
                {
                    RemoveItem(replaces);
                    replaces = null;
                }
            }


            if (item.NotYourProperty && curTown != null && curTown.NPCsSeeCrime(this))
            {
                Game.AddMessage("Your crime was seen!");
                curTown.MakeTownHostile();
            }

            if (_Filter == eItemFilter.ALL)
            {
                item.Pos.X = slotno;

                _Filter = item.GetFilterGroup();
                var n = 0;
                while (true)
                {
                    if (GetSlot(n) == null)
                    {
                        item.Pos.Y = n;
                        break;
                    }
                    n++;
                }
                _Filter = eItemFilter.ALL;
            }
            else
            {
                item.Pos.Y = slotno;
                var f = _Filter;
                _Filter = eItemFilter.ALL;
                var n = 0;
                while (true)
                {
                    if (GetSlot(n) == null)
                    {
                        item.Pos.X = n;
                        break;
                    }
                    n++;
                }
                _Filter = f;
            }

            item.NotYourProperty = false;
            item.Contained = false;

            if (!ItemList.Contains(item)) //Don't add it again if it's already in this inventory
                ItemList.Add(item);
        }
        return replaces;
    }

    /// <summary>
    /// Adds an item to the PCs inventory in the first free slot. .
    /// </summary>
    /// <param name="item"></param>
    /// <param name="stack">Whether to stack items that can combine with an item already there</param>
    /// <returns></returns>
    public bool AddItem(Item item, bool stack) 
    {
        if (item == null) return true;

        //Stack an item if it's combinable with one already held.
        if (stack)
            foreach (var i in ItemList)
                if (item != i && item.CombinableWith(i))
                {
                    i.Charges += item.Charges;
                    if (i.Charges > Constants.ITEM_STACK_LIMIT) { item.Charges = i.Charges - Constants.ITEM_STACK_LIMIT; i.Charges = Constants.ITEM_STACK_LIMIT; continue; } //Can only stack to 999
                    return true;
                }

        //Get Items slot in the ALL items filter (Stored in Pos.X)
        var n = 0;
        var slotfree = false;
        while (!slotfree) {
            slotfree = true;
            foreach (var i in ItemList)
                if (i.Pos.X == n) { n++; slotfree = false; break; }

        }
        item.Pos.X = n;

        //Get Item's slot in the specific filter for this item type (Stored in Pos.Y)
        n = 0;
        slotfree = false;
        var fg = item.GetFilterGroup();
        while (!slotfree)
        {
            slotfree = true;
            foreach (var i in ItemList)
                if (fg == i.GetFilterGroup() && i.Pos.Y == n) { n++; slotfree = false; break; }

        }
        item.Pos.Y = n;

        item.Contained = false;
        if (item.NotYourProperty && curTown != null && curTown.NPCsSeeCrime(this))
        {
            Game.AddMessage("Your crime was seen!");
            curTown.MakeTownHostile();
        }
        item.NotYourProperty = false;
        ItemList.Add(item);
        return true;
    }

    public void ArrangeItems()
    {
        var toremove = new List<Item>();

        //First combine any items that can be combined.
        //Items that should then be removed are put into the toremove list
        foreach (var i1 in EachItem())
        {
            if (toremove.Contains(i1.Item1)) continue;

            var reachedi1 = false;
            foreach (var i2 in EachItem())
            {
                if (reachedi1)
                {
                    if (!toremove.Contains(i2.Item1) && i1.Item1.CombinableWith(i2.Item1))
                    {
                        i1.Item1.Charges += i2.Item1.Charges;
                        if (i1.Item1.Charges > Constants.ITEM_STACK_LIMIT) 
                        { i2.Item1.Charges = i1.Item1.Charges - Constants.ITEM_STACK_LIMIT; i1.Item1.Charges = Constants.ITEM_STACK_LIMIT; }
                        else
                            toremove.Add(i2.Item1);
                    }
                }
                else if (i1 == i2)
                    reachedi1 = true;
            }
        }

        //Items in the toremove list are removed from the main list.
        ItemList = ItemList.Except(toremove).ToList();

        //Gaps are removed
        var newslot = 0;
        foreach (var i1 in EachItem())
        {
            if (_Filter == eItemFilter.ALL)
                i1.Item1.Pos.X = newslot++;
            else
                i1.Item1.Pos.Y = newslot++;
        }
    }

    /// <summary>
    /// Equips the item specified and returns whether it did it. Puts it in the correct slot for the item.
    /// </summary>
    /// <param name="item"></param>
    /// <returns></returns>
    public bool Equip(Item item, eEquipSlot slot, out Item replaced_item)//, eEquipSlot slot = eEquipSlot.Unknown)
    {
        replaced_item = null;

        if (slot == eEquipSlot.None && (slot = CanEquip(item,eEquipSlot.None)) == eEquipSlot.None)
            slot = item.SlotNeeded;

        if (!item.CompatibleSlot(slot))
        {
            Game.AddMessage("Can't equip item of that type there.");
            return false;
        }

        Item failed = null;

        //Budge off the item in the         slot we're trying to drop to
        var budged = GetEquipped(slot);

        if (budged != null && budged.CombinableWith(item))
        {
            item.Charges += budged.Charges;
            if (item.Charges > Constants.ITEM_STACK_LIMIT)
            {
                budged.Charges = item.Charges - 999;
                item.Charges = 999;
            }
            else
                budged = null;
        }

        var budged_poisoned = false;
        if (budged != null)
            if (!CanUnequip(slot))
                failed = budged;
            else
            {
                if (PoisonedWeapon == budged) budged_poisoned = true;
                Unequip(budged);
                AddItem(budged,false);
            }

        if (failed == null)
        {
            //Two handed weapons, knock off anything in the offhand to the PCs inventory;
            if (item.Variety == eVariety.TwoHanded && slot == eEquipSlot.MainHand)
            {
                var offhand = GetEquipped(eEquipSlot.OffHand);
                if (offhand != null)
                    if (CanUnequip(eEquipSlot.OffHand))
                    {
                        Unequip(offhand);
                        AddItem(offhand,false);
                    }
                    else
                    {
                        failed = offhand;
                    }
            }

            //Anything in the offhand knocks off Two handed weapons in main hand to PCs inventory;
            if (item.Variety is eVariety.Shield or eVariety.OneHanded && slot == eEquipSlot.OffHand)
            {
                var mainhand = GetEquipped(eEquipSlot.MainHand);
                if (mainhand != null && mainhand.Variety == eVariety.TwoHanded)
                    if (!CanUnequip(eEquipSlot.MainHand))
                    {
                        failed = mainhand;
                    }
                    else
                    {
                        Unequip(mainhand);
                        AddItem(mainhand,false); //Put knocked two-handed weapon to inventory
                    }
            }
        }

        if (failed != null)
        {
            failed.CursedMessage();
            if (failed != budged)
            {
                RemoveItem(budged); //Put item back.
                EquippedItemSlots[(int)slot] = budged;
                if (budged_poisoned) PoisonedWeapon = budged;
            }
            return false;
        }

        if (item.CombinableWith(budged))
        {
            EquippedItemSlots[(int)slot] = item; 
            item.Charges += budged.Charges;
            if (budged_poisoned) PoisonedWeapon = item;
        }
        else
        {
            EquippedItemSlots[(int)slot] = item;
            replaced_item = budged;
        }

        return true;               
    }

    /// <summary>
    /// See if the PC can equip the item.
    /// </summary>
    /// <param name="item">Item to try and equip</param>
    /// <param name="slot">Slot to try to equip in, or if none, any suitable slot.</param>
    /// <returns></returns>
    public eEquipSlot CanEquip(Item item, eEquipSlot slot)
    {
        if (item == null) return eEquipSlot.None;

        var slotneeded = item.SlotNeeded;
        if (slotneeded == eEquipSlot.None) return eEquipSlot.None;
        if (EquippedItemSlots.Contains(item)) return eEquipSlot.None;

        if (slot == eEquipSlot.None)
        {
            var use = GetEquipped(slotneeded) == null ? slotneeded : eEquipSlot.None;

            //Can't equip a two handed weapon if something is equipped in the off hand.
            if (item.Variety == eVariety.TwoHanded && GetEquipped(eEquipSlot.OffHand) != null) use = eEquipSlot.None;

            //Can put a one-handed weapon in the off hand
            if (use == eEquipSlot.None && item.Variety == eVariety.OneHanded && GetEquipped(eEquipSlot.OffHand) == null) use = eEquipSlot.OffHand; 

            //Can put a ring in the second ring slot if the first is occupied
            if (use == eEquipSlot.None && item.Variety == eVariety.Ring && GetEquipped(eEquipSlot.Ring2) == null) use = eEquipSlot.Ring2;

            //Can't equip a shield if a two-handed weapon is equipped in the main hand.
            if (item.Variety == eVariety.Shield
                && GetEquipped(eEquipSlot.MainHand) != null
                && GetEquipped(eEquipSlot.MainHand).Variety == eVariety.TwoHanded)
                use = eEquipSlot.None;

            //
            if (slotneeded == eEquipSlot.Ammo && item.CombinableWith(GetEquipped(slotneeded))) use = eEquipSlot.Ammo;
            return use;
        }
        else
        {
            if (GetEquipped(slot) != null) return eEquipSlot.None;
                
            //Can equip a ring there.
            if (slot == eEquipSlot.Ring2 && GetEquipped(eEquipSlot.Ring2) == null && item.Variety == eVariety.Ring) return slot;
            //Or a one-handed weapon in the off hand.
            if (slot == eEquipSlot.OffHand && GetEquipped(eEquipSlot.OffHand) == null && item.Variety == eVariety.OneHanded) return slot;

            if (slot == eEquipSlot.Ammo && item.CombinableWith(GetEquipped(eEquipSlot.Ammo))) return slot;

            if (slot == slotneeded)
            {
                if (item.Variety == eVariety.TwoHanded && GetEquipped(eEquipSlot.OffHand) != null) return eEquipSlot.None;
                if (item.Variety == eVariety.Shield && GetEquipped(eEquipSlot.MainHand) != null && GetEquipped(eEquipSlot.MainHand).Variety == eVariety.TwoHanded)
                    return eEquipSlot.None;
                return slot;
            }
        }
        return eEquipSlot.None;
    }

    public bool CanUnequip(eEquipSlot slot)
    {
        if (GetEquipped(slot) != null && GetEquipped(slot).Cursed) return false;
        return true;
    }
    public bool CanUnequip(Item item)
    {
        return CanUnequip(HasEquipped(item));
    }

    public void UnequipCursed()
    {
        foreach (var i in EachEquippedItem())
        {
            if (i.Cursed)
            {
                Unequip(i, true);
                AddItem(i, true);
            }
        }
    }

    /// <summary>
    /// Unequips the item specified and returns it. 
    /// - If item is null, any item in slot specified is removed.
    /// - If slot is Unknown, the item is removed from whatever slot it is in.
    /// </summary>
    /// <param name="item"></param>
    /// <param name="regardless_of_curse"></param>
    /// <param name="slot"></param>
    /// <returns>Item that has been unequipped. Null if couldn't.</returns>
    public Item Unequip(Item item, bool regardless_of_curse = false, eEquipSlot slot = eEquipSlot.None)
    {
        if (item != null)
        {
            if (!regardless_of_curse && item.Cursed) { Game.AddMessage("Can't unequip! Item is cursed!"); return null; }

            if (slot == eEquipSlot.None)
            {
                var s = getEquipSlot(item);
                if (s != eEquipSlot.None) { EquippedItemSlots[(int)s] = null; return item; }
            }
            else
            {
                if (EquippedItemSlots[(int)slot] == item) 
                {
                    if (PoisonedWeapon == item) PoisonedWeapon = null;
                    EquippedItemSlots[(int)slot] = null; 
                    return item; 
                }
            }
        }
        else
        {
            if (slot != eEquipSlot.None)
            {
                if (!regardless_of_curse && EquippedItemSlots[(int)slot] != null && EquippedItemSlots[(int)slot].Cursed == true)
                {
                    Game.AddMessage("Can't unequip! Item is cursed!"); return null;
                }
                item = EquippedItemSlots[(int)slot];
                if (item != null && PoisonedWeapon == item) PoisonedWeapon = null;
                EquippedItemSlots[(int)slot] = null; 
                return item; 
            }
        }
        return null;
    }

    private IEnumerable<Item> EachEquippedItem()
    {
        foreach(var i in EquippedItemSlots)
            if (i != null) yield return i;
    }

    public Item GetEquipped(eEquipSlot slot)
    {
        return EquippedItemSlots[(int)slot];
    }

    private eEquipSlot getEquipSlot(Item item)
    {
        for (var n = 0; n < EquippedItemSlots.Length; n++)
        {
            if (item == EquippedItemSlots[n]) return (eEquipSlot)n;
        }
        return eEquipSlot.None;
    }
    /// <summary>
    /// Return item from inventory at slot specified, null if slot is empty.
    /// </summary>
    /// <param name="slotno"></param>
    /// <returns></returns>
    public Item GetSlot(int slotno)
    {
        foreach (var i in EachItem()) 
            if (i.Item2 == slotno /*&& i != Gui.MoveItem*/) return i.Item1;
        return null;
    }

    /// <summary>
    /// Removes item from inventory (not from Equipped Items)
    /// </summary>
    /// <param name="i"></param>
    /// <returns></returns>
    public bool RemoveItem(Item i)
    {
        if (ItemList.Contains(i))
        {

            ItemList.Remove(i);
            return true;
        }

        return false;
            
    }

    private void handlePopUp(object o, object o2, int data)
    {
        var c = (Item)o;
        switch (data)
        {
            case PopUpMenuData.EQUIP:
                new Action(eAction.EquipItem) { PC = this, Item = c, InventoryFrom = this };
                break;
            case PopUpMenuData.UNEQUIP:
                new Action(eAction.UnequipItem) { PC = this, Item = c};
                break;
            case PopUpMenuData.DROP:
                new Action(LootWindow.IsOpen ? eAction.DropItemToLootSpot : eAction.TargetDropItem) { PC = this, Item = c};
                break;
            case PopUpMenuData.GIVE: 
                new Action(eAction.GiveItem) { PC = this, PC2 = o2 as PCType, Item = c };
                break;
            case PopUpMenuData.USE:
                new Action(eAction.UseItem) { PC = this, Item = c };
                break;
            case PopUpMenuData.SELL:
                var a = new Action(eAction.SellItem) { PC = this, Item = c, InventoryFrom = this, InventoryTo = (IInventory)o2 };
                a.PlaceDraggedItem(eAction.PlaceInInventory);
                new Action(eAction.NONE);
                break;
            case PopUpMenuData.IDENTIFY:
                c.Identify((o2 as IdentifyWindow.IdentifyBox).Price);
                break;
            case PopUpMenuData.ENCHANT:
                var e = o2 as EnchantingWindow.EnchantingBox;
                c.Enchant(e.Enchantment,e.EnchantCost(c));
                break;
        }
    }

    public void MakeItemToolTip(Item i, XnaRect r)
    {
        if (i != null)
        {
            var tt = new StringBuilder();
            tt.Append(i.TooltipInfo());

            if (i.Identified && HasEquipped(i) != eEquipSlot.None)
            {
                if (i.IsRangedWeapon())
                {
                    var hit_bonus = i.Bonus;
                    hit_bonus += GetSkillBonus(eSkill.DEXTERITY);
                    var s = HasItemEquippedWithAbility(eItemAbil.ACCURACY);
                    if (s != null)
                        hit_bonus += s.AbilityStrength / 2;

                    if (HasTrait(Trait.Nephilim)) hit_bonus += 2;

                    tt.Append(
                        $"@n@6   {(hit_bonus < 0 ? "Penalty to hit: %" : "Bonus to hit: %")}{Math.Abs(hit_bonus)}@e");
                }
                else if (i.IsAmmo())
                {
                    var dam_bonus = i.Bonus;
                    var s = HasItemEquippedWithAbility(eItemAbil.ACCURACY);
                    if (s != null)
                        dam_bonus += s.AbilityStrength / 2;
                    tt.Append(
                        $"@n@6   Damage: 1-{i.Level} {(dam_bonus == 0 ? "" : dam_bonus < 0 ? "(" + dam_bonus + ")" : "(+" + dam_bonus + ")")}");
                }
                else if (i.IsWeapon())
                {
                    var hit_adj = GetSkillBonus(eSkill.DEXTERITY) * 5 - TotalEncumbrance * 5
                                  + 5 * Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE));
                    if (!HasTrait(Trait.Ambidextrous) && HasEquipped(i) == eEquipSlot.OffHand)
                        hit_adj -= 25;

                    var dam_adj = GetSkillBonus(eSkill.STRENGTH) + Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE));

                    var s = HasItemEquippedWithAbility(eItemAbil.SKILL);
                    if (s != null)
                    {
                        hit_adj += 5 * (s.AbilityStrength / 2 + 1);
                        dam_adj += s.AbilityStrength / 2;
                    }

                    s = HasItemEquippedWithAbility(eItemAbil.GIANT_STRENGTH);
                    if (s != null)
                    {
                        hit_adj += s.AbilityStrength * 2;
                        dam_adj += s.AbilityStrength;
                    }

                    hit_adj += 5 * i.Bonus;
                    dam_adj += i.Bonus;

                    tt.Append($"@n@6   {(hit_adj < 0 ? "Penalty to hit: %" : "Bonus to hit: %")}{Math.Abs(hit_adj)}@e");
                    tt.Append(
                        $"@n@6   Damage: 1-{i.Level} {(dam_adj == 0 ? "" : dam_adj < 0 ? "(" + dam_adj + ")" : "(+" + dam_adj + ")")}");
                }
            }

            if (Gui.ShopIsOpen != null)
            {
                if (Gui.ShopIsOpen.WillBuy(i))
                {
                    tt.Append("@n@e@7Sell value: ");
                    tt.Append(i.Value);
                    tt.Append(" gold");
                }
                else tt.Append("@e@nCan't sell here");
            }
            if (Gui.ServiceBoxOpen is IdentifyWindow.IdentifyBox && !i.Identified)
            {
                tt.Append("@n@e@7Cost to identify: ");
                tt.Append(((IdentifyWindow.IdentifyBox)Gui.ServiceBoxOpen).Price);
                tt.Append(" gold");
            }
            if (Gui.ServiceBoxOpen is EnchantingWindow.EnchantingBox && i.IsEnchantable())
            {
                tt.Append("@n@e@7Cost to enchant: ");
                tt.Append(((EnchantingWindow.EnchantingBox)Gui.ServiceBoxOpen).EnchantCost(i));
                tt.Append(" gold");
            }

            new ToolTipV2(false, r, tt.ToString(), -1);
        }
    }

    public void MakeInventoryPopUpWindow(Item c)
    {
        if (Game.Mode == eMode.COMBAT && this != Party.ActivePC)
        {
            Game.AddMessage("Only the active character can access items in their inventory.");
            return;
        }

        var popupoptions = new List<PopUpMenuData>();

        if (c != null)
        {
            Gui.DragItem = null;

            if (Game.Mode != eMode.COMBAT)
            {
                if (Gui.ShopIsOpen != null && Gui.ShopIsOpen.WillBuy(c))
                    popupoptions.Add(new PopUpMenuData("Sell for " + c.Value + " gold", c, Gui.ShopIsOpen, PopUpMenuData.SELL));

                if (Gui.ServiceBoxOpen is IdentifyWindow.IdentifyBox && !c.Identified)
                    popupoptions.Add(new PopUpMenuData("Identify for " + ((IdentifyWindow.IdentifyBox)Gui.ServiceBoxOpen).Price + " gold", c, Gui.ServiceBoxOpen, PopUpMenuData.IDENTIFY));

                if (Gui.ServiceBoxOpen is EnchantingWindow.EnchantingBox && c.IsEnchantable())
                    popupoptions.Add(new PopUpMenuData("Enchant for " + ((EnchantingWindow.EnchantingBox)Gui.ServiceBoxOpen).EnchantCost(c) + " gold", c, Gui.ServiceBoxOpen, PopUpMenuData.ENCHANT));
            }

            if (c.IsEquippable)
                if (HasEquipped(c) != eEquipSlot.None) popupoptions.Add(new PopUpMenuData("Unequip", c, null, PopUpMenuData.UNEQUIP));
                else popupoptions.Add(new PopUpMenuData("Equip", c, null, PopUpMenuData.EQUIP));
            if (c.IsUseable())
                popupoptions.Add(new PopUpMenuData("Use", c, null, PopUpMenuData.USE));
            popupoptions.Add(new PopUpMenuData("Drop", c, null, PopUpMenuData.DROP));

            if (Game.Mode == eMode.COMBAT)
            {
                foreach (var pc in Party.EachAlivePC())
                {
                    if (pc != this)
                        popupoptions.Add(new PopUpMenuData("Give to " + pc.Name, c, pc, PopUpMenuData.GIVE));
                }
            }
            else
            {
                foreach(PCType pc in Game.Mode == eMode.OUTSIDE ? Party.EachAlivePC() : curTown.EachCharacterAdjacent(Pos, true, false))
                {
                    if (pc != this)
                        popupoptions.Add(new PopUpMenuData("Give to " + pc.Name, c, pc, PopUpMenuData.GIVE));
                }
            }

            new PopUpMenu(handlePopUp, popupoptions);
        }
    }

    #endregion


    private int pc_carry_weight()
    {
        var storage = 0;
        bool airy = false, heavy = false;

        foreach (var item in ItemList)
        {
            storage += item.Weight;
            if (item.Ability == eItemAbil.LIGHTER_OBJECT) airy = true;
            if (item.Ability == eItemAbil.HEAVIER_OBJECT) heavy = true;
        }
        if (airy) storage -= 30;
        if (heavy) storage += 30;
        if (storage < 0) storage = 0;
        return storage;
    }

    /// <summary>
    /// Uses up 1 charge on an item the PC holds. If the item is then out of charges it is removed.
    /// </summary>
    /// <param name="i"></param>
    public void UseItemCharge(Item i)
    {
        i.Charges--;
        if (i.Charges <= 0)
        {
            if (HasEquipped(i) != eEquipSlot.None)
            {
                Unequip(i, true);
            }
            else if (ItemList.Contains(i))
                RemoveItem(i);
        }
    }

    public int PickLockChance(Location loc)
    {
        var which_item = HasItemEquippedWithAbility(eItemAbil.LOCKPICKS);
        var terrain = curTown.TerrainAt(loc);

        if (which_item == null) return -1; //No lockpick, no chance.
        if (terrain.Special != eTerSpec.UNLOCKABLE_TERRAIN && terrain.Special != eTerSpec.UNLOCKABLE_BASHABLE) return -2;
        if (Convert.ToInt32(terrain.Flag2) >= 10) return -3;

        var chance = 100 - (Convert.ToInt32(terrain.Flag2) * 15 + 30);

        chance += 5 * GetSkillBonus(eSkill.DEXTERITY);
        chance -= curTown.Difficulty * 7;
        chance += 5 * GetSkill(eSkill.LOCKPICKING);
        chance += which_item.AbilityStrength * 7;
        chance += !HasTrait(Trait.Nimble) ? 8 : 0;
        chance += HasItemEquippedWithAbility(eItemAbil.THIEVING) != null ? 12 : 0;

        chance = Maths.MinMax(0, 100, chance);
        return chance;
    }

    public void PickLock(Location loc)
    {
        var chance = PickLockChance(loc);

        if (chance == -1)
        {
            Game.AddMessage("  Need lockpick equipped.        ");
            return;
        }
        if (chance == -2)
            return;
        if (chance == -3)
        {
            Game.AddMessage("The lock is too complicated to pick!");
            return;
        }

        if (Maths.Rand(1, 0, 100) < chance)
        {
            Game.AddMessage("  Door unlocked.                ");
            Sound.Play(9);
            curTown.UnlockTerrain(loc);

        }
        else
        {
            Game.AddMessage("  Didn't work.                ");

            var which_item = HasItemEquippedWithAbility(eItemAbil.LOCKPICKS);
            if (Maths.Rand(1, 0, 100) + which_item.AbilityStrength * 7 < 75)
            {
                Game.AddMessage("  Pick breaks.                ");
                UseItemCharge(which_item);
            }
            Sound.Play(41);
        }
    }

    public int BashDoorChance(Location loc)
    {
        var terrain = curTown.TerrainAt(loc);

        if (terrain.Special != eTerSpec.UNLOCKABLE_TERRAIN && terrain.Special != eTerSpec.UNLOCKABLE_BASHABLE) return -2;
        if (Convert.ToInt32(terrain.Flag2) >= 10) return -3;

        var chance = 100 - (Convert.ToInt32(terrain.Flag2) * 15 + 40);
        chance += 15 * GetSkillBonus(eSkill.STRENGTH);
        chance -= curTown.Difficulty * 4;
        chance = Maths.MinMax(0, 100, chance);
        return chance;
    }

    public void BashDoor(Location loc)
    {
        var chance = BashDoorChance(loc);

        if (chance == -2)
            return;
        if (chance == -3)
        {
            Game.AddMessage("The " + curTown.TerrainAt(loc).Name + " is too strong to break!");
            return;
        }

        new Animation_MoveFail(this, Pos, loc);
        new Animation_Hold();

        if (Maths.Rand(1, 0, 99) < chance)
        {
            Game.AddMessage("  Lock breaks.                ");
            Sound.Play(9);
            curTown.UnlockTerrain(loc);
            return;
        }
        else
        {
            Game.AddMessage("  Didn't work.                ");
            if (Damage(null, Maths.Rand(1, 1, 4), 0, eDamageType.UNBLOCKABLE)) new Animation_Hold();
            return;
        }
    }

    /// <summary>
    /// 1:Can cast  -1:Don't know spell  -2:Dumbfounded  -3:Paralyzed  -4:Asleep  
    /// -5:Level too high (Mage)  -6:Level too high (Priest)  -7:Not enough SP
    /// </summary>
    /// <param name="ms"></param>
    /// <returns></returns>
    public int CanCast(MagicSpell ms)
    {
        if (!KnownSpells.ContainsValue(ms)) return -1;
        if (Status(eAffliction.DUMB) >= 8 - ms.Level) return -2;
        if (Status(eAffliction.PARALYZED) > 0) return -3;
        if (Status(eAffliction.ASLEEP) > 0) return -4;
        if (ms.Mage && GetSkill(eSkill.MAGE_SPELLS) < ms.Level) return -5; 
        if (!ms.Mage && GetSkill(eSkill.PRIEST_SPELLS) < ms.Level) return -6;

        foreach (var i in EachEquippedItem())
            if (i.Awkward > 1) return -11;

        if (SP < ms.Cost) return -7;
        if (Game.Mode == eMode.COMBAT && ms.Where is eSpellWhere.TOWN or eSpellWhere.TOWN_AND_OUTDOOR or eSpellWhere.OUTDOOR) return -8;
        if (Game.Mode == eMode.OUTSIDE && ms.Where is eSpellWhere.COMBAT or eSpellWhere.TOWN or eSpellWhere.TOWN_AND_COMBAT) return -9;
        if (Game.Mode == eMode.TOWN && ms.Where is eSpellWhere.COMBAT or eSpellWhere.OUTDOOR) return -10;

        return 1;
    }

    public int CanConcoct(Recipe r)
    {
        if (GetSkill(eSkill.ALCHEMY) < r.Skill)
            return -2;

        if (Status(eAffliction.DUMB) > 0) return -3;
        if (Status(eAffliction.PARALYZED) > 0) return -4;
        if (Status(eAffliction.ASLEEP) > 0) return -5;

        foreach (var t in r.Ingredients)
        {
            var has = 0;
            foreach (var i in EachItemHeld())
                if (i.AlchemyID == t.Item1) has++;

            if (has < t.Item2) return -1;
        }
        return 1;
    }


    /// <summary>
    /// Moves PC
    /// </summary>
    /// <param name="mod"></param>
    /// <returns>Returns true if PC has now spent some action points</returns>
    public bool Move(Location mod)
    {
        var map = Game.CurrentMap;

        ///////////////////////////////////////////PAUSE/////////////////////////////////////////
        if (mod == Location.Zero) //PC isn't moving, just waiting.
        {
            AP = 0;
            if (Game.Mode == eMode.COMBAT)
            {
                Game.AddMessage(Party.ActivePC.Name + " stands ready.");
                if (Status(eAffliction.WEBS) > 0)
                {
                    Game.AddMessage(Party.ActivePC.Name + " cleans webs.");
                    CounteractStatus(eAffliction.WEBS, 2);
                }
                Parry = 100;
                if (map is TownMap) curTown.InflictFields(this);
            }
            else
            {
                if (Party.Vehicle != null && Party.Vehicle.Type == eVehicleType.HORSE)
                    Party.LeaveVehicle();
                else
                    Game.AddMessage("Pause.");

                foreach (var pc in Party.EachAlivePC())
                {
                    if (pc.Status(eAffliction.WEBS) > 0)
                    {
                        Game.AddMessage(string.Format("{0} cleans webs.", pc.Name));
                        pc.CounteractStatus(eAffliction.WEBS, 2);
                    }
                    if (map is TownMap) curTown.InflictFields(pc);
                }
            }
                

            return true;
        }
        ///////////////////////////////////////////PAUSE/////////////////////////////////////////

        var newpos = Pos + mod;
        var newdir = new Direction(mod);

        //Can try to attack character if one is there.
        var ch = (map as TownMap)?.CharacterThere(newpos);
        if (ch is NPC)
        {
            var npc = (NPC)ch;
            if (npc.IsABaddie)
                return (Attack(ch));
            else
            {
                if (Game.Mode != eMode.COMBAT) return false;
                var p = eDialogPic.CREATURE;
                if (npc.Record.Width == 2 && npc.Record.Height == 1) p = eDialogPic.CREATURE2x1;
                else if (npc.Record.Width == 1 && npc.Record.Height == 2) p = eDialogPic.CREATURE1x2;
                else if (npc.Record.Width == 2 && npc.Record.Height == 2) p = eDialogPic.CREATURE2x2;
                new MessageWindow(confirmFriendAttack, "The target is not hostile. Are you sure you want to attack?", p, npc.Record.Picture, "Yes", "No!");
                new Action(eAction.Attack) { PC = this, NPC = npc };
            }
        }

        ///////////////////////////////////////////////////IN A BOAT//////////////////////////////////////////////////
        else if (Party.Vehicle != null)
        {
            if (Party.Vehicle.Type == eVehicleType.BOAT)
            {
                    
                var canwalk = map.PCCanTryToWalkThere(newpos, this);

                if (Vehicle.IsThere(map, newpos) != null) return false; //Can't move onto another vehicle while in one.

                var ontoatown = Game.Mode == eMode.OUTSIDE && Game.WorldMap.TownEntranceHere(newpos) != null;

                if (canwalk && (!map.TerrainAt(newpos).BoatOver || (newpos.X != Pos.X && newpos.Y != Pos.Y)))
                {
                    if (!ontoatown)
                    {
                        //Leave boat
                        if (!map.TriggerStepOnSpecials(newpos, newdir, this, true))
                        {
                            Party.LeaveVehicle();
                            return CompleteMove(newpos, newdir);
                        }
                        return false;
                    }
                }
                if (newpos.X != Pos.X && newpos.Y != Pos.Y) return false; //Can't move diagonally in a boat

                // Crossing bridge: land or go through
                if (canwalk && !ontoatown && map.TerrainAt(newpos).BoatOver)
                {
                    new MessageWindow(confirmBoatLanding, "You have come to a dock/bridge. Pilot under it or land?", eDialogPic.NONE, 0, "Land", "Go under");
                    new Action(eAction.NONE) { PC = this, Loc = newpos, Dir = newdir };
                    return false;
                }

                if (ontoatown || (map.TerrainAt(newpos).BoatOver && !map.TriggerStepOnSpecials(newpos, newdir, this, false)))
                {
                    return CompleteMove(newpos, newdir);
                }
            }
            else if (Party.Vehicle.Type == eVehicleType.HORSE)
            {
                if (map.PCCanTryToWalkThere(newpos, this))
                {
                    if (map.TerrainAt(newpos).BlocksHorse)
                    {
                        Game.AddMessage("You can't take horses there!");
                        return false;
                    }
                    if (Vehicle.IsThere(map, newpos) != null) return false; //Can't move onto another vehicle while in one.

                    if (!map.TriggerStepOnSpecials(newpos, newdir, this, false))
                    {
                        return CompleteMove(newpos, newdir);
                    }
                }
            }
        }
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////
        else
        {
            foreach (var pc in Party.EachIndependentPC())
            {
                if (newpos == pc.Pos && pc.AP == 0)
                {
                    Game.AddMessage("Can't switch places.\n  " + pc.Name + " has no moves left");
                    return false;
                }
            }

            var boardvehicle = false;

            var v = Vehicle.IsThere(map, newpos);

            if (v != null)
            {
                if (Game.Mode == eMode.COMBAT) return false;
                if (!v.PartyOwns)
                {
                    Game.AddMessage("  Not your " + v.Name);
                    return false;
                }
                else
                    boardvehicle = true;
            }

            //Check there aren't any theoretical impediments to moving there.
            if (boardvehicle || map.PCCanTryToWalkThere(newpos, this))
            {
                //There are two types of special encounters we have to check for:
                //  Nodes in this space on the SpecialEncounterList
                //  & Nodes set in the Special field of the Terrain type for when walked on.
                // In both cases the result of the special node chain may ban us from moving here.
                // So we have to register the special node trigger and set a pending move to be completed later.
                if (!map.TriggerStepOnSpecials(newpos, newdir, this, false))
                {
                    return CompleteMove(newpos, newdir);
                }
            }
        }
        return false;
    }

    private void confirmFriendAttack(int button_index)
    {
        if (button_index != 0)
            new Action(eAction.NONE);
            
    }

    private void confirmBoatLanding(int button_index)
    {
        var a = Action.GetCurrent();

        if (button_index == 0)
        {
            if (!Game.CurrentMap.TriggerStepOnSpecials(a.Loc, a.Dir, this, true))
                new Action(eAction.BoatLanding) { PC = this, Loc = a.Loc, Dir = a.Dir };
        }
        else
            new Action(eAction.CompleteMove) { PC = this, Loc = a.Loc, Dir = a.Dir };
    }

    public bool DoParry()
    {
        Game.AddMessage(Name + " prepares to parry.");
        Parry = (AP / 4) * (2 + GetSkillBonus(eSkill.DEXTERITY) + GetSkill(eSkill.DEFENSE));
        AP = 0;
        return true;
    }

    public bool ForceMove(Location newpos, Direction newdir)
    {
        var map = Game.CurrentMap;
        if (Party.Vehicle != null) new Animation_VehicleMove(Party.Vehicle, pos, newpos, false);
        else new Animation_Move(this, pos, newpos, false, false);
        pos = newpos;
        direction.Dir = newdir.Dir;
        Gfx.CentreView(Pos, false);

        //In non-combat mode, all PCs move at the same time.
        if (Game.Mode != eMode.COMBAT)
        {
            foreach (var pc in Party.PCList)
                pc.PositionPConPC(this);
            map.UpdateVisible();
        }
        else
        {
            ((TownMap)map).UpdateVisiblePC(this, false);

        }

        if (Party.Vehicle != null)
        {
            Party.Vehicle.Pos = pos;
            Party.Vehicle.Dir.Dir = newdir.Dir;
        }
        return true;

    }

    public bool CompleteMove(Location newpos, Direction newdir)
    {
        var map = Game.CurrentMap;

        //BOAT MOVEMENT
        if (Party.Vehicle != null && Party.Vehicle.Type == eVehicleType.BOAT)
        {
            if (map.TerrainAt(newpos).BoatOver || (Game.Mode == eMode.OUTSIDE && Game.WorldMap.TownEntranceHere(newpos)!=null))
            {
                //Boat move here.
                new Animation_VehicleMove(Party.Vehicle, pos, newpos, true);
                pos = newpos;
                direction.Dir = newdir.Dir;
                AP -= 1;
                Party.Vehicle.Pos = newpos; //Move the boat too
                Party.Vehicle.Dir.Dir = newdir.Dir;
                foreach (var pc in Party.PCList)
                    pc.PositionPConPC(this);
                Gfx.CentreView(Pos, false);
                map.UpdateVisible();
                return true;
            }
        }

        var keep_going = map.CheckSpecialTerrainPC(newpos, this);
        PCType switchPC = null;

        if (keep_going)
        {
            if (Party.Vehicle == null || Party.Vehicle.Type == eVehicleType.HORSE)
            {
                if (!map.CharacterCanBeThere(newpos, this, true))//!map.TerrainBlocked(newpos) && map.CharacterThere(newpos) == null)
                {
                    keep_going = false;

                    foreach (var pc in Party.EachAlivePC())
                    {
                        if (newpos == pc.Pos && pc.AP > 0)
                        {
                            keep_going = true;
                            switchPC = pc;
                        }
                    }
                }
            }
            else if (Party.Vehicle != null && Party.Vehicle.Type == eVehicleType.BOAT) //If you're in a boat
                Party.LeaveVehicle();

            var boardsvehicle = false;

            var v = Vehicle.IsThere(map, newpos);
            if (v != null && Game.Mode != eMode.COMBAT)
            {
                Party.BoardVehicle(v);
                keep_going = true;
                boardsvehicle = true;
            }

            if (keep_going)
            {
                //In combat mode, each adjacent enemy gets a free attack if move is to a non-adjacent square - provided they aren't otherwise indisposed.
                if (map is TownMap && Game.Mode == eMode.COMBAT)
                {
                    foreach (NPC npc in curTown.EachCharacterAdjacent(pos, false, true))
                    {
                        if (!AlliedWith(npc) && npc.Active == eActive.COMBATIVE && !npc.AdjacentTo(newpos) && npc.Status(eAffliction.ASLEEP) == 0 && npc.Status(eAffliction.PARALYZED) == 0)
                        {
                            npc.Attack(this);
                            if (this.LifeStatus != eLifeStatus.ALIVE) return false; //The attack finished us off. Obviously don't move.
                        }
                    }
                }

                //On an outside combat if the move is out of the area, the character get a chance to flee. If flee fails the move is blocked.
                if (map is CombatMap && !((TownMap)map).InActArea(newpos))
                {
                    if (Maths.Rand(1, 0, 99) < Constants.FLEE_PROBABILITY)///3)
                    {
                        //PC has fled combat
                        AP = 0;
                        LifeStatus = eLifeStatus.FLED;
                        Game.AddMessage("Fled combat!");
                        new Animation_Move(this, pos, newpos, true); //Moves and fades away as it goes.
                        pos = newpos;
                        direction.Dir = newdir.Dir;
                    }
                    else
                    {
                        AP -= 1;
                        Game.AddMessage("Couldn't flee!");
                        new Animation_MoveFail(this, pos, newpos);
                    }
                    return true;
                }

                if (switchPC != null)
                {
                    new Animation_Move(switchPC, switchPC.Pos, pos, false );
                    switchPC.Pos = pos;
                    switchPC.AP -= 1;
                }

                if (!boardsvehicle && Party.Vehicle != null)
                    new Animation_VehicleMove(Party.Vehicle, pos, newpos, false);
                else
                    new Animation_Move(this, pos, newpos, true, boardsvehicle);

                pos = newpos;
                direction.Dir = newdir.Dir;
                AP -= 1;

                //In non-combat mode, all PCs move at the same time.
                if (Game.Mode != eMode.COMBAT)
                {
                    foreach (var pc in Party.PCList)
                        pc.PositionPConPC(this);
                    map.UpdateVisible();
                }
                else
                {
                    ((TownMap)map).UpdateVisiblePC(this, false);
                    if (switchPC != null) ((TownMap)map).UpdateVisiblePC(switchPC, false);
                }

                if (Party.Vehicle != null)
                {
                    Party.Vehicle.Pos = pos;
                    Party.Vehicle.Dir.Dir = newdir.Dir;
                }

                Gfx.CentreView(Pos, false);
                    
                if (map is TownMap && AP > 0)
                {
                    ((TownMap)map).InflictFields(this);
                    if (switchPC != null) ((TownMap)map).InflictFields(switchPC);
                }
                map.DoNastyTerrain(pos);
                if (switchPC != null) map.DoNastyTerrain(switchPC.pos);

                return true;
            }
        }
        return false;
    }

    public void UseItem(Item item)
    {
        bool take_charge = true,inept_ok = false;
        int item_use_code;
        var which_stat=eAffliction.BLESS_CURSE;

        ////NEW (same as for SPELLS) - Where= 0 - everywhere 1 - combat only 2 - town only 3 - town & outdoor only 4 - town & combat only  5 - outdoor only  6 - never
        // + 10 - mag. inept can use
        short[] abil_chart = {6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6, // 50
            6,6,6,6,6,6,6,6,6,6,
            14,0,0,0,4, 4,4,0,4,4,
            4,4,4,4,4, 0,0,0,0,4,
            14,4,4,5,0, 10,0,0,0,0,
            6,6,6,6,6,6,6,6,6,6, // 100
            1,1,1,1,1, 1,1,1,1,4,
            4,1,1,1,1, 1,1,1,1,4,
            1,2,2,1,1, 1,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6, // 150
            6,6,6,6,6,6,6,6,6,6, // 160
            6,6,6,6,6,6,6,0,6,6, // 170
            6,6,6,6,6,6,6,6,6,6,
            6,6,6,6,6,6,6,6,6,6};


        var abil = item.Ability;
        var level = item.Level;

        item_use_code = abil_chart[(short)abil];
        if (item_use_code >= 10) {
            item_use_code -= 10;
            inept_ok = true;
        }

        if (item_use_code == 6) {
            Game.AddMessage("Use: Can't use this item.");
            take_charge = false;
        }
        if (HasTrait(Trait.MagicallyInept) && !inept_ok){
            Game.AddMessage("Use: Can't - magically inept.");
            take_charge = false;
        }

        if (abil == eItemAbil.CAST_SPELL && MagicSpell.List.Contains(item.SpellID))
            item_use_code = (int)MagicSpell.List[item.SpellID].Where;


        if (take_charge == true) 
        {
            if (Game.Mode == eMode.OUTSIDE && item_use_code > 0 && item_use_code != 3 && item_use_code != 5)
            {
                Game.AddMessage("Use: Not while outdoors.");
                take_charge = false;
            }
            if (Game.Mode == eMode.TOWN && item_use_code is 1 or 5) {
                Game.AddMessage("Use: Not while in town. ");
                take_charge = false;
            }
            if (Game.Mode == eMode.COMBAT && item_use_code is 2 or 3 or 5) {
                Game.AddMessage("Use: Not in combat.");
                take_charge = false;
            }
            if (Game.Mode != eMode.OUTSIDE && item_use_code == 5){
                Game.AddMessage("Use: Only outdoors.");
                take_charge = false;
            }
        }
        if (take_charge == true) 
        {

            Game.AddMessage(string.Format("Use: {0}", item.KnownName));

            if (item.Variety == eVariety.Potion)
                Sound.Play(56);

            var str = item.AbilityStrength;

            var type = item.MagicUseType;

            switch (abil) {
                case eItemAbil.POISON_WEAPON: // poison weapon
                    take_charge = PoisonWeapon(str,false);
                    break;
                case eItemAbil.BLESS_CURSE: case eItemAbil.HASTE_SLOW:  case eItemAbil.AFFECT_INVULN: case eItemAbil.AFFECT_MAGIC_RES:
                case eItemAbil.AFFECT_WEB: case eItemAbil.AFFECT_SANCTUARY: case eItemAbil.AFFECT_MARTYRS_SHIELD:
                    var min=0;
                    switch (abil)
                    {
                        case eItemAbil.BLESS_CURSE:
                            Sound.Play(4);
                            which_stat = eAffliction.BLESS_CURSE;
                            if (type % 2 == 1)
                            {
                                Game.AddMessage("  You feel awkward."); str = str * -1;
                            }
                            else Game.AddMessage("  You feel blessed.");
                            min = -8;
                            break;
                        case eItemAbil.HASTE_SLOW:
                            Sound.Play(75);
                            which_stat = eAffliction.HASTE_SLOW;
                            if (type % 2 == 1)
                            {
                                Game.AddMessage("  You feel sluggish."); str = str * -1;
                            }
                            else Game.AddMessage("  You feel speedy.");
                            min = -8;
                            break;
                        case eItemAbil.AFFECT_INVULN:
                            Sound.Play(68);
                            which_stat = eAffliction.INVULNERABLE;
                            if (type % 2 == 1)
                            {
                                Game.AddMessage("  You feel odd."); str = str * -1;
                            }
                            else Game.AddMessage("  You feel protected.");
                            break;
                        case eItemAbil.AFFECT_MAGIC_RES:
                            Sound.Play(51);
                            which_stat = eAffliction.MAGIC_RESISTANCE;
                            if (type % 2 == 1)
                            {
                                Game.AddMessage("  You feel odd."); str = str * -1;
                            }
                            else Game.AddMessage("  You feel protected.");
                            break;
                        case eItemAbil.AFFECT_WEB:
                            which_stat = eAffliction.WEBS;
                            if (type % 2 == 1)
                                Game.AddMessage("  You feel sticky.");
                            else
                            {
                                Game.AddMessage("  Your skin tingles."); str = str * -1;
                            }
                            break;
                        case eItemAbil.AFFECT_SANCTUARY:
                            Sound.Play(43);
                            which_stat = eAffliction.INVISIBLE;
                            if (type % 2 == 1)
                            {
                                Game.AddMessage("  You feel exposed."); str = str * -1;
                            }
                            else Game.AddMessage("  You feel obscure.");
                            break;
                        case eItemAbil.AFFECT_MARTYRS_SHIELD:
                            Sound.Play(43);
                            which_stat = eAffliction.MARTYRS_SHIELD;
                            if (type % 2 == 1)
                            {
                                Game.AddMessage("  You feel dull."); str = str * -1;
                            }
                            else Game.AddMessage("  You start to glow slightly.");
                            break;
                    }

                    if (type > 1)
                        foreach (var pc in Party.EachAlivePC())
                            pc.SetStatus(which_stat, pc.Status(which_stat) + str, min, 8);
                    else
                        SetStatus(which_stat, Status(which_stat) + str, min, 8);
                    break;
                case eItemAbil.AFFECT_POISON:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel better."); Cure(str); break;
                        case 1: Game.AddMessage("  You feel ill."); Poison(str); break;
                        case 2: Game.AddMessage("  You all feel better."); foreach (var pc in Party.EachAlivePC()) pc.Cure(str); break;
                        case 3: Game.AddMessage("  You all feel ill."); foreach (var pc in Party.EachAlivePC()) pc.Poison(str); break;
                    }
                    break;
                case eItemAbil.AFFECT_DISEASE:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel healthy."); DecStatus(eAffliction.DISEASE, str, 0); break;
                        case 1: Game.AddMessage("  You feel sick."); Disease(str); break;
                        case 2: Game.AddMessage("  You all feel healthy."); foreach (var pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.DISEASE,str, 0); break;
                        case 3: Game.AddMessage("  You all feel sick."); foreach (var pc in Party.EachAlivePC()) pc.Disease(str); break;
                    }
                    break;
                case eItemAbil.AFFECT_DUMBFOUND:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel clear headed."); DecStatus(eAffliction.DUMB,str,0); break;
                        case 1: Game.AddMessage("  You feel confused."); Dumbfound(str); break;
                        case 2: Game.AddMessage("  You all feel clear headed."); foreach (var pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.DUMB,str,0); break;
                        case 3: Game.AddMessage("  You all feel confused."); foreach (var pc in Party.EachAlivePC()) pc.Dumbfound(str); break;
                    }
                    break;
                case eItemAbil.AFFECT_SLEEP:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel alert."); DecStatus(eAffliction.ASLEEP,str, -8); break;
                        case 1: Game.AddMessage("  You feel very tired."); Sleep(str+1, 200); break;
                        case 2: Game.AddMessage("  You all feel alert."); foreach (var pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.ASLEEP,str,-8); break;
                        case 3: Game.AddMessage("  You all feel very tired."); foreach (var pc in Party.EachAlivePC()) pc.Sleep(str + 1, 200); break;
                    }
                    break;
                case eItemAbil.AFFECT_PARALYSIS:
                    switch (type) {
                        case 0: Game.AddMessage("  You find it easier to move."); DecStatus(eAffliction.PARALYZED,str * 100,0); break;
                        case 1: Game.AddMessage("  You feel very stiff."); Paralyze(str * 20 + 10,200); break;
                        case 2: Game.AddMessage("  You all find it easier to move."); foreach (var pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.PARALYZED,str * 100,0); break;
                        case 3: Game.AddMessage("  You all feel very stiff."); foreach (var pc in Party.EachAlivePC()) pc.Paralyze(str * 20 + 10,200); break;
                    }
                    break;
                case eItemAbil.AFFECT_ACID:
                    switch (type) {
                        case 0: Game.AddMessage("  Your skin tingles pleasantly."); DecStatus(eAffliction.ACID,str,0); break;
                        case 1: Game.AddMessage("  Your skin burns!"); Acid(str); break;
                        case 2: Game.AddMessage("  You all tingle pleasantly."); foreach (var pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.ACID,str,0); break;
                        case 3: Game.AddMessage("  Everyone's skin burns!"); foreach (var pc in Party.EachAlivePC()) pc.Acid(str); break;
                    }
                    break;
                case eItemAbil.BLISS:
                    switch (type) {
                        case 0:
                        case 1:
                            Game.AddMessage("  You feel wonderful!");
                            Heal(str * 20);
                            IncStatus(eAffliction.BLESS_CURSE,str,8);
                            break;
                        case 2:
                        case 3:
                            Game.AddMessage("  Everyone feels wonderful!");
                            Party.HealAll(str * 20, false);
                            foreach (var pc in Party.EachAlivePC()) pc.IncStatus(eAffliction.BLESS_CURSE, str,8);
                            break;
                    }
                    break;
                case eItemAbil.AFFECT_EXPERIENCE:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel much smarter."); AwardXP(str * 5); break;
                        case 1: Game.AddMessage("  You feel forgetful."); AwardXP(str * -5); break;
                        case 2: Game.AddMessage("  You all feel much smarter."); Party.AwardXP(str * 5); break;
                        case 3: Game.AddMessage("  You all feel forgetful."); Party.AwardXP(str * -5); break;
                    }
                    break;
                case eItemAbil.AFFECT_SKILL_POINTS:
                    Sound.Play(68);
                    switch (type) {
                        case 0: Game.AddMessage("  You feel much smarter."); SkillPoints += str; break;
                        case 1: Game.AddMessage("  You feel forgetful."); SkillPoints = Maths.Max(0,SkillPoints - str); break;
                        case 2: Game.AddMessage("  You all feel much smarter."); foreach (var pc in Party.EachAlivePC()) pc.SkillPoints += str; break;
                        case 3: Game.AddMessage("  You all feel forgetful."); foreach (var pc in Party.EachAlivePC()) pc.SkillPoints = Maths.Max(0,pc.SkillPoints - str); break;
                    }
                    break;
                case eItemAbil.AFFECT_HEALTH:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel better."); Heal(str * 20); break;
                        case 1: Game.AddMessage("  You feel sick."); if (Damage(null, 20 * str,0, eDamageType.UNBLOCKABLE)) new Animation_Hold(); break;
                        case 2: Game.AddMessage("  You all feel better."); Party.HealAll(str * 20,false); break;
                        case 3: Game.AddMessage("  You all feel sick."); Party.Damage(20 * str,eDamageType.UNBLOCKABLE); break;
                    }
                    break;
                case eItemAbil.AFFECT_SPELL_POINTS:
                    switch (type) {
                        case 0: Game.AddMessage("  You feel energized."); SP += str * 5; break;
                        case 1: Game.AddMessage("  You feel drained."); SP -= str * 5; break;
                        case 2: Game.AddMessage("  You all feel energized."); foreach (var pc in Party.EachAlivePC()) pc.SP += str * 5; break;
                        case 3: Game.AddMessage("  You all feel drained."); foreach (var pc in Party.EachAlivePC()) pc.SP -= str * 5; break;
                    }
                    break;
                case eItemAbil.DOOM:
                    switch (type) {
                        case 0:
                        case 1: Game.AddMessage("  You feel terrible.");
                            AwardXP(str * -5);
                            Damage(null, 20 * str,0, eDamageType.UNBLOCKABLE);
                            Disease(2 * str);
                            Dumbfound(2 * str);
                            break;
                        case 2:
                        case 3: Game.AddMessage("  You all feel terrible."); 
                            foreach (var pc in Party.EachAlivePC())
                            {
                                pc.AwardXP(str * -5);
                                pc.Damage(null, 20 * str, 0, eDamageType.UNBLOCKABLE);
                                pc.Disease(2 * str);
                                pc.Dumbfound(2 * str);
                            }
                            break;
                    }
                    break;
                case eItemAbil.LIGHT:
                    Game.AddMessage("  You have more light."); Party.LightLevel += 50 * str;
                    break;
                case eItemAbil.STEALTH:
                    Game.AddMessage("  Your footsteps become quieter."); Party.Stealth += 5 * str;
                    break;
                case eItemAbil.FIREWALK:
                    Game.AddMessage("  You feel chilly."); Party.Firewalk += 2 * str;
                    break;
                case eItemAbil.FLYING:
                    if (Party.Flying > 0) {
                        Game.AddMessage("  Not while already flying.          ");
                        break;
                    }
                    if (Party.IsInABoat())
                        Game.AddMessage("  Leave boat first.             ");
                    else if (Party.IsOnAHorse())////
                        Game.AddMessage("  Leave horse first.             ");
                    else {
                        Game.AddMessage("  You rise into the air!"); Party.Flying += str;
                    }
                    break;
                case eItemAbil.MAJOR_HEALING:
                    switch (type) {
                        case 0:
                        case 1:
                            Game.AddMessage("  You feel wonderful.");
                            Heal(200);
                            Cure(8);
                            break;
                        case 2:
                        case 3:
                            Game.AddMessage("  You all feel wonderful.");
                            foreach (var pc in Party.EachAlivePC())
                            {
                                pc.Heal(200);
                                pc.Cure(8);
                            }
                            break;
                    }
                    break;
                case eItemAbil.CALL_SPECIAL:
                    break;

                case eItemAbil.CAST_SPELL:

                    if (MagicSpell.List.Contains(item.SpellID))
                    {
                        var ac = eAction.NONE;
                        PCType pc2 = null;
                        switch (MagicSpell.List[item.SpellID].Target)
                        {
                            case eSpellTarget.CASTER:
                                ac = eAction.CastSpell;
                                break;
                            case eSpellTarget.LIVING_PC: case eSpellTarget.DEAD_PC: //Use item spells can't target another specific PC
                                pc2 = this;
                                ac = eAction.CastSpell;
                                break;
                            case eSpellTarget.CHARACTER: case eSpellTarget.LOCATION:
                                ac = eAction.ItemSpellTargeting;
                                break;
                        }
                        new Action(ac) { Spell = MagicSpell.List[item.SpellID], Item = item, PC = this, PC2 = pc2 };
                    }
                    break;
            }
        }
        if (take_charge && item.Charges > 0) UseItemCharge(item);
    }

    /// <summary>
    /// Returns whether the PC is suitably equipped to fire a ranged weapon.
    /// </summary>
    /// <returns></returns>
    public bool CanFire()
    {
        var ranged = GetEquipped(eEquipSlot.Ranged);
        var ammo = GetEquipped(eEquipSlot.Ammo);

        if (ranged == null) return false;

        //Got the right ammo?
        switch (ranged.Variety)
        {
            case eVariety.Bow:
                return ammo != null && ammo.Variety == eVariety.Arrows;
            case eVariety.Crossbow:
                return ammo != null && ammo.Variety == eVariety.Bolts;
            case eVariety.Thrown:
            case eVariety.RangedNoAmmo:
                return true;
        }
        return false;
    }

    public bool HasRanged()
    {
        var i = GetEquipped(eEquipSlot.Ranged);
        if (i == null) return false;
        return i.Variety is eVariety.Bow or eVariety.Crossbow or eVariety.RangedNoAmmo;
    }

    public bool InventorysClose(IInventory other) {
        if (pos.adjacent(other.Pos) || other is Shop) return true;
        return false;
    }

    public eEquipSlot HasEquipped(Item item)
    { 
        if (item != null) 
            for (var n = 0; n < EquippedItemSlots.Length; n++)
                if (item == EquippedItemSlots[n]) return (eEquipSlot)n;
        return eEquipSlot.None;
    }

    public Item HasItemEquippedWithAbility(eItemAbil abil) { return EquippedItemSlots.ToList<Item>().Find(n => n != null && n.Ability == abil); }
    public Item HasItemWithAbility(eItemAbil abil) 
    {
        var i = ItemList.Find(n => n.Ability == abil);
        if (i != null) return i;
        return HasItemEquippedWithAbility(abil);
    }

    public bool IsAlive() {return LifeStatus == eLifeStatus.ALIVE;}
    public bool IsGone() { return LifeStatus is eLifeStatus.ABSENT or eLifeStatus.FLED or eLifeStatus.SURFACE or eLifeStatus.WON; }

    public XnaRect GetGraphicRect(bool forcerightwards = false)
    {

        return new XnaRect(direction.IsFacingRight || forcerightwards ? 0 : Gfx.CHARGFXWIDTH, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
    }

    public void Draw(SpriteBatch sb, XnaRect dr, Color col)
    {
        if (NotDrawn) return;

        float rot = 0;
        if (AnimAction != null) 
            AnimAction.AdjustCharRect(ref dr, ref rot, ref col);
        if (AnimFlash != null)
            AnimFlash.AdjustCharRect(ref dr, ref rot, ref col);

        if (this == Party.ActivePC && Game.Turn == eTurn.PLAYER && Game.Mode == eMode.COMBAT)//Animation.OnlyMovingAnimationsRunning() && (Game.Turn == Game.eTurn.PLAYER || Game.Mode != eMode.COMBAT))
        {
            var bigdr = dr;
            dr.Offset(dr.Width / 2, dr.Height / 2);
            bigdr.Inflate(Gfx.HIGHLIGHT_SIZE, Gfx.HIGHLIGHT_SIZE);
            bigdr.Offset(bigdr.Width / 2, bigdr.Height / 2);
            sb.Draw(AnimAction is Animation_Attack ? Gfx.PCCombatHighlightGfx : Gfx.PCHighlightGfx,
                bigdr, Gfx.PCHighlightGfx.Bounds, col, rot, new Vector2(Gfx.PCHighlightGfx.Width / 2, Gfx.PCHighlightGfx.Height / 2),
                direction.IsFacingRight ? SpriteEffects.None : SpriteEffects.FlipHorizontally, 0);
        }
        else
        {
            dr.Offset(dr.Width / 2, dr.Height / 2);
            var sr = GetGraphicRect();
            if (AnimAction is Animation_Attack) sr.X += Gfx.CHARGFXWIDTH * 2;
            sb.Draw(PCTexture, dr, sr, col, rot, new Vector2(Gfx.CHARGFXWIDTH / 2, Gfx.CHARGFXHEIGHT / 2), SpriteEffects.None, 0);
        }

        if (Game.Mode == eMode.COMBAT && Gfx.DrawHealthBars & !Dying)
        {
            var br = new XnaRect(134, 181, 20, 6);

            //Health
            var h = (float)Health / (float)MaxHealth;
            br.Y = ((int)(6 - h / (1f / 6f))) * 8 + 181;

            sb.Draw(Gfx.NewGui, new Vector2(dr.X - (dr.Width / 2f), dr.Y + (dr.Height / 2f) - 6), br, col);
        }
            
    }


    /// <summary>
    /// PC attacks specified character.
    /// </summary>
    /// <param name="target">Returns false if attacked was cancelled.</param>
    /// <returns></returns>
    public bool Attack(ICharacter target)
    {
        var weapons = new List<Item>();
        Item skill_item;
        int hit_adj, dam_adj;

        // slice out bad attacks
        if (!IsAlive()) return false;
        if (Status(eAffliction.ASLEEP) > 0 || Status(eAffliction.PARALYZED) > 0) return false;

        if (!(target is NPC)) return false; //PCs attacking other PCs not something in BoE or needs implementing yet.
        var which_m = (NPC)target;

        direction.FaceTowards(pos, target.Pos); //Face who you're attacking.

        LastAttacked = which_m;
        Provocation += Constants.AI_ATTACK_PROVOCATION_SCORE + 1; //Add provocation score (+1 because 1 automatically gets taken off at the end of every turn)

        var w1 = GetEquipped(eEquipSlot.MainHand);
        var w2 = GetEquipped(eEquipSlot.OffHand);
        if (w2 != null && !w2.IsMeleeWeapon()) w2 = null;
        if (w1 == null && w2 != null) weapons.Add(w2);
        else weapons.Add(w1);
        if (w1 != null && w2 != null) weapons.Add(w2); 

        hit_adj = -5 * Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE)) + 5 * Maths.MinMax(-8, 8, which_m.Status(eAffliction.BLESS_CURSE))
            - GetSkillBonus(eSkill.DEXTERITY) * 5 + EncumbranceRoll * 5;

        if (Game.PCsAlwaysHit) hit_adj -= 10000;

        dam_adj = Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE)) - Maths.MinMax(-8, 8, which_m.Status(eAffliction.BLESS_CURSE))
                  + GetSkillBonus(eSkill.STRENGTH);

        if (which_m.Status(eAffliction.ASLEEP) > 0 || which_m.Status(eAffliction.PARALYZED) > 0)
        {
            hit_adj -= 80;
            dam_adj += 10;
        }

        if ((skill_item = HasItemEquippedWithAbility(eItemAbil.SKILL)) != null)
        {
            hit_adj += 5 * (skill_item.Level / 2 + 1);
            dam_adj += skill_item.Level / 2;
        }
        if ((skill_item = HasItemEquippedWithAbility(eItemAbil.GIANT_STRENGTH)) != null)
        {
            dam_adj += skill_item.Level;
            hit_adj += skill_item.Level * 2;
        }

        if (Status(eAffliction.INVISIBLE) > 0)
        {
            Game.AddMessage("You become visible!");
            SetStatus(eAffliction.INVISIBLE, 0);
        }

        var store_hp = which_m.Health;
        var second_attack = false;

        foreach (var weapon in weapons)
        {
            if (!target.IsAlive()) break;

            var what_skill = weapon?.MeleeTypeToSkill() ?? eSkill.DEXTERITY;

            if (weapon == null)
            {
                Game.AddMessage(Name + " punches.  ");

                var r1 = Maths.Rand(1, 0, 100) + hit_adj - 20;
                r1 += 5 * (status[6] / 3);
                var r2 = Maths.Rand(1, 1, 4) + dam_adj;

                if (r1 <= hitChance[GetSkill(what_skill)])
                {
                    var aa = new Animation_Attack(this);
                    if (!which_m.Damage(this, r2, 0, eDamageType.WEAPON, eDamageType.WEAPON, "072_club"))
                        aa.SetSound("002_swordswish");
                }
                else
                {
                    new Animation_Attack(this, "002_swordswish");
                    Game.AddMessage(Name + " misses. ");
                }
            }
            else
            {
                Game.AddMessage(Name + " swings.");
                var r1 = Maths.Rand(1, 0, 100) - (second_attack ? 5 : 0) + hit_adj - 5 * weapon.Bonus;
                r1 += 5 * (Status(eAffliction.WEBS) / 3);

                if (weapons.Count > 1 && !HasTrait(Trait.Ambidextrous)) r1 += 25;

                // race adj.
                if (HasTrait(Trait.Slitherzakai) && weapon.MeleeType == eMeleeWeaponType.POLE) r1 -= 10;

                var r2 = Maths.Rand(1, 1, weapon.Level) + dam_adj + (second_attack ? -1 : 2) + weapon.Bonus;

                if (weapon.Ability == eItemAbil.WEAK_WEAPON) r2 = (r2 * (10 - weapon.AbilityStrength)) / 10;

                if (r1 <= hitChance[GetSkill(what_skill)])
                {
                    var aa = new Animation_Attack(this);
                    var does_damage = false;

                    eDamageType spec_dam_type;
                    var spec_dam = weapon.GetSpecialDamage(which_m.Record.Genus, out spec_dam_type);

                    // assassinate
                    if (!second_attack
                        && Level >= which_m.Record.Level - 1 
                        && GetSkill(eSkill.ASSASSINATION) >= which_m.Record.Level / 2
                        && which_m.Record.SpecialSkill != eCSS.SPLITS) // Can't assassinate splitters
                        if (Maths.Rand(1, 0, 100) < hitChance[Math.Max(GetSkill(eSkill.ASSASSINATION) - which_m.Record.Level, 0)])
                        {
                            Game.AddMessage("  You assassinate.           ");
                            spec_dam += r2;
                        }

                    switch (what_skill)
                    {
                        case eSkill.EDGED_WEAPONS:
                            if (weapon.Level < 8)
                                does_damage = which_m.Damage(this, r2, spec_dam, eDamageType.WEAPON, spec_dam_type, "069_sword1");
                            else 
                                does_damage = which_m.Damage(this, r2, spec_dam, eDamageType.WEAPON, spec_dam_type, "070_sword2");
                            break;
                        case eSkill.BASHING_WEAPONS:
                            does_damage = which_m.Damage(this, r2, spec_dam, eDamageType.WEAPON, spec_dam_type, "072_club");
                            break;
                        case eSkill.POLE_WEAPONS:
                            does_damage = which_m.Damage(this, r2, spec_dam, eDamageType.WEAPON, spec_dam_type, "071_sword3");
                            break;
                    }

                    if (!does_damage) aa.SetSound(what_skill == eSkill.POLE_WEAPONS ? "019_swordswish" : "002_swordswish");
                    new Animation_Hold();

                    if (!which_m.Dying) //Don't do extra attack effects if enemy has been killed.
                    {
                        // poison			
                        if (Status(eAffliction.POISONED_WEAPON) > 0 && PoisonedWeapon == weapon)
                        {
                            var poison_amt = status[0];
                            if (HasItemEquippedWithAbility(eItemAbil.POISON_AUGMENT) != null)
                                poison_amt += 2;
                            which_m.Poison(poison_amt);
                            Maths.MoveToZero(ref status[0]);
                        }
                        if (weapon.Ability == eItemAbil.POISONED_WEAPON && Maths.Rand(1, 0, 1) == 1)
                        {
                            Game.AddMessage("  Blade drips venom.             ");
                            which_m.Poison(weapon.AbilityStrength / 2);
                        }
                        if (weapon.Ability == eItemAbil.ACIDIC_WEAPON && Maths.Rand(1, 0, 1) == 1)
                        {
                            Game.AddMessage("  Blade drips acid.             ");
                            which_m.Acid(weapon.AbilityStrength / 2);
                        }
                        if (weapon.Ability == eItemAbil.SOULSUCKER && Maths.Rand(1, 0, 1) == 1)
                        {
                            Game.AddMessage("  Blade drains life.             ");
                            Health += weapon.AbilityStrength / 2;
                        }
                    }
                }
                else
                {
                    Game.AddMessage("  " + Name + " misses.              ");
                    new Animation_Attack(this, what_skill == eSkill.POLE_WEAPONS ? "019_swordswish" : "002_swordswish");
                }
            }
            second_attack = true;
        }

        CounteractStatus(eAffliction.POISONED_WEAPON);
        AP -= 4;// Math.Max(AP - 4, 0);

        if ((which_m.Status(eAffliction.MARTYRS_SHIELD) > 0 || which_m.Record.SpecialSkill == eCSS.PERMANENT_MARTYRS_SHIELD)
            && store_hp - which_m.Health > 0)
        {
            if (Damage(which_m, store_hp - which_m.Health, 0, eDamageType.MAGIC))
            {
                Game.AddMessage("  Shares damage!   ");
                new Animation_Hold();
            }
        }
        return true;
    }

    public bool FireMissile(Location target)
    {
        int spec_dam = 0, poison_amt = 0;
        ICharacter cur_monst;
        Item skill_item;

        var firing = HasRanged(); //If true, PC is firing (bow/crossbow/sling) - if false, PC is throwing (Javelins or whatnot)
        var ammo = GetEquipped(eEquipSlot.Ammo);
        var rangedwp = GetEquipped(eEquipSlot.Ranged);
        var no_ammo = rangedwp.Variety == eVariety.RangedNoAmmo; //Only applies to an ammo-less ranged weapon (like a sling)

        var skill = firing ? GetSkill(eSkill.ARCHERY) : GetSkill(eSkill.THROWN_MISSILES);
        var range = firing ? Constants.PC_FIRING_RANGE : Constants.PC_THROWING_RANGE;

        //The hitting item is the actual missile that does the damage, not the item that fires it except in the case of a ranged weapon that uses no ammo (eg, sling)
        var hitting_item = (firing && !no_ammo) ? ammo : rangedwp;

        int dam = 0, dam_bonus = 0, hit_bonus = 0;

        dam = hitting_item.Level;
        dam_bonus = hitting_item.Bonus + Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE));

        //Hit bonus starts with the thing firing the missile (in the case of a bow or crossbow that uses ammo)
        hit_bonus = (firing && !no_ammo) ? rangedwp.Bonus : 0;
                
        hit_bonus += GetSkillBonus(eSkill.DEXTERITY) - curTown.CanSee(pos, target) + Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE));
        if ((skill_item = HasItemEquippedWithAbility(eItemAbil.ACCURACY)) != null)
        {
            hit_bonus += skill_item.AbilityStrength / 2;
            dam_bonus += skill_item.AbilityStrength / 2;
        }

        // race adj.
        if (HasTrait(Trait.Nephilim)) hit_bonus += 2;
        var exploding = hitting_item.Ability == eItemAbil.MISSILE_EXPLODING;

        if (pos.DistanceTo(target) > range)
        {
            Game.AddMessage("  Out of range.");
            return false;
        }
        else if (curTown.CanSee(pos, target) >= Constants.OBSCURITY_LIMIT)
        {
            Game.AddMessage("  Can't see target.             ");
            return false;
        }
        else
        {
            // First, some missiles do special things

            if (Status(eAffliction.INVISIBLE) > 0)
            {
                Game.AddMessage("You become visible!");
                SetStatus(eAffliction.INVISIBLE, 0);
            }
            AP = firing ? AP - 3 : AP - 2;
            var r1 = Maths.Rand(1, 0, 100) - 5 * hit_bonus - 10;
            r1 += 5 * (Status(eAffliction.WEBS) / 3);

            if (Game.PCsAlwaysHit) r1 -= 1000;

            var r2 = Maths.Rand(1, 1, dam) + dam_bonus;
            Game.AddMessage(Name + " fires.");

            var m_type = 10;
            if (!firing)
                switch (rangedwp.Level) //Need to change this to allow proper missile graphic selection
                {
                    case 7: m_type = 10; break; //Flying knife
                    case 4: m_type = 1; break; //Dart
                    case 8: m_type = 5; break; //Javelin
                    case 9: m_type = 7; break; //Razordisc
                }

            else
            {
                if (no_ammo)
                    m_type = 9; //Sling shot bullet
                else
                    m_type = (hitting_item.Magic) ? 4 : 3; //Magic or not arrow
            }

            new Animation_Attack(this);
            new Animation_Missile(pos, target, m_type, false, "012_longbow");
            new Animation_Hold();

            if (exploding)
            {
                Game.AddMessage("  The " + hitting_item.ShortName + " explodes!");
                curTown.HitArea(target, hitting_item.AbilityStrength * 2, 1, 6, eDamageType.FIRE, Pattern.Radius2, true, this); new Animation_Hold();
            }
            else
            {

                cur_monst = curTown.CharacterThere(target);

                if (r1 > hitChance[skill])
                    Game.AddMessage("  Missed.");
                else if (cur_monst != null)
                {
                    var spec_dam_type = eDamageType.WEAPON;
                    spec_dam = cur_monst is NPC ? hitting_item.GetSpecialDamage(((NPC)cur_monst).Record.Genus, out spec_dam_type) : 0;
                    if (hitting_item.Ability == eItemAbil.MISSILE_HEAL_TARGET)
                    {
                        Game.AddMessage("  There is a flash of light.");
                        cur_monst.Health += r2;
                    }
                    else
                    if (cur_monst.Damage(this, r2, spec_dam, eDamageType.WEAPON, spec_dam_type, "098_missilehit")) new Animation_Hold();

                    // poison
                    if ((Status(eAffliction.POISONED_WEAPON) > 0) && (PoisonedWeapon == hitting_item))
                    {
                        poison_amt = Status(eAffliction.POISONED_WEAPON);
                        if (HasItemEquippedWithAbility(eItemAbil.POISON_AUGMENT) != null)
                            poison_amt++;
                        cur_monst.Poison(poison_amt);
                    }
                    if (hitting_item.Ability == eItemAbil.CAUSES_FEAR)
                        cur_monst.Scare(hitting_item.AbilityStrength * 10);
                    if (hitting_item.Ability == eItemAbil.MISSILE_ACID)
                        cur_monst.Acid(hitting_item.AbilityStrength);
                }
            }

            //Use up ammo

            if ((firing && no_ammo) || hitting_item.Ability == eItemAbil.MISSILE_RETURNING)
            {
                //No ammo to use up
            }
            else
            {
                hitting_item.Charges--;

                if (HasItemEquippedWithAbility(eItemAbil.DRAIN_MISSILES) != null)
                    hitting_item.Charges--;

                if (hitting_item.Charges <= 0)
                    Unequip(hitting_item, true);
            }
        }

        if (!exploding) CounteractStatus(eAffliction.POISONED_WEAPON);
        return true;
    }

    public bool Damage(IExpRecipient attacker, int how_much, int how_much_spec, eDamageType dam_type, eDamageType spec_dam_type = eDamageType.WEAPON, string sound_type = null)
    {
        int level;
        if (!IsAlive()) return false;

        var type_of_attacker = attacker is NPC ? ((NPC)attacker).Record.Genus : eGenus.HUMAN;

        if (sound_type == null)
        {
            switch (dam_type)
            {
                case eDamageType.FIRE:
                case eDamageType.UNBLOCKABLE: sound_type = "073_fireimpact"; break;
                case eDamageType.MAGIC: sound_type = "089_zap"; break;
                case eDamageType.COLD: sound_type = "075_cold"; break;
                case eDamageType.POISON: sound_type = "088_slime"; break;
                default: sound_type = "032_gethit1"; break;
            }
        }

        // armour
        if (dam_type is eDamageType.WEAPON or eDamageType.UNDEAD or eDamageType.DEMON)
        {
            how_much -= Maths.MinMax(-5, 5, Status(eAffliction.BLESS_CURSE));
            foreach (var item in EachEquippedItem())
            {
                if (item.IsArmour())
                {
                    how_much -= Maths.Rand(1, 1, item.Level);

                    // bonus for magical items
                    if (item.Bonus > 0)
                    {
                        how_much -= Maths.Rand(1, 1, item.Bonus);
                        how_much -= item.Bonus / 2;
                    }
                    if (item.Bonus < 0)
                        how_much = how_much - item.Bonus;
                    if (Maths.Rand(1, 0, 100) < hitChance[skills[8]] - 20)
                        how_much -= 1;
                }
                if (item.Protection > 0)
                    how_much -= Maths.Rand(1, 1, item.Protection);
                if (item.Protection < 0)
                    how_much += Maths.Rand(1, 1, -1 * item.Protection);
            }
        }

        // parry
        if ((dam_type == eDamageType.WEAPON) && (Parry < 100))
            how_much -= Parry / 4;

        if (HasTrait(Trait.Tough))
            how_much--;

        if (Maths.Rand(1, 0, 100) < 2 * (hitChance[skills[18]] - 20))
            how_much -= 1;

        if (dam_type == eDamageType.WEAPON && (level = get_prot_level(eItemAbil.PROTECTION)) > 0)
            how_much = how_much - level;
        if (dam_type == eDamageType.UNDEAD && (level = get_prot_level(eItemAbil.PROTECT_FROM_UNDEAD)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);
        if (dam_type == eDamageType.DEMON && (level = get_prot_level(eItemAbil.PROTECT_FROM_DEMONS)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);
        if (type_of_attacker == eGenus.HUMANOID && (level = get_prot_level(eItemAbil.PROTECT_FROM_HUMANOIDS)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);
        if (type_of_attacker == eGenus.REPTILE && (level = get_prot_level(eItemAbil.PROTECT_FROM_REPTILES)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);
        if (type_of_attacker == eGenus.GIANT && (level = get_prot_level(eItemAbil.PROTECT_FROM_GIANTS)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);

            
        // invuln
        if (Status(eAffliction.INVULNERABLE) > 0) how_much = 0;

        // magic resistance
        if (dam_type == eDamageType.MAGIC && (level = get_prot_level(eItemAbil.MAGIC_PROTECTION)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);

        // Mag. res helps w. fire and cold
        if (dam_type is eDamageType.FIRE or eDamageType.COLD &&
            Status(eAffliction.MAGIC_RESISTANCE) > 0)
            how_much = how_much / 2;

        // fire res.
        if (dam_type == eDamageType.FIRE && (level = get_prot_level(eItemAbil.FIRE_PROTECTION)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);

        // cold res.
        if (dam_type == eDamageType.COLD && (level = get_prot_level(eItemAbil.COLD_PROTECTION)) > 0)
            how_much = how_much / (level >= 7 ? 4 : 2);

        // major resistance
        if (dam_type is eDamageType.FIRE or eDamageType.POISON or eDamageType.MAGIC or eDamageType.COLD
            && (level = get_prot_level(eItemAbil.FULL_PROTECTION)) > 0)
            how_much = how_much / ((level >= 7) ? 4 : 2);

        if (Game.Invincible) how_much = 0;

        if (how_much <= 0)
        {
            Game.AddMessage("  No damage.");
            return false;
        }
        // if asleep, get bonus
        if (Status(eAffliction.ASLEEP) > 0)
            DecStatus(eAffliction.ASLEEP, 1, 0);

        Game.AddMessage(string.Format("  {0} takes {1}. ", Name, how_much));

        new Animation_Damage(Pos.ToVector2(), how_much, 0, dam_type, sound_type);
        Party.total_dam_taken += how_much;

        if (cur_health >= how_much)
        {
            cur_health = cur_health - how_much;  
        }
        else if (cur_health > 0)
        {
            cur_health = 0;
            new Animation_Hold();
            new Animation("003_cough");
        }
        else // Check if PC can die
        if (how_much > 25)
        {
            Game.AddMessage(string.Format("  {0} is obliterated.  ", Name));
            Kill(attacker, eLifeStatus.DUST);
        }
        else
        {
            Game.AddMessage(string.Format("  {0} is killed.  ", Name));
            Kill(attacker, eLifeStatus.DEAD);
        }
        return true;
    }

    public bool RunTrap(eTrapType trap_type, int trap_level, int diff)
    {
        short[] trap_odds = {5,30,35,42,48, 55,63,69,75,77,
            78,80,82,84,86, 88,90,92,94,96,98,99,99,99,99,99,99,99,99,99};

        var num_hits = 1 + trap_level;

        if (trap_type == eTrapType.RANDOM)
            trap_type = (eTrapType)Maths.Rand(1, 1, 4);
        if (trap_type == eTrapType.FALSE_ALARM)
            return true;

        var i = GetSkillBonus(eSkill.DEXTERITY);
        var i_level = get_prot_level(eItemAbil.THIEVING);
        if (i_level > 0) i = i + i_level / 2;
        var skill = Maths.MinMax(0, 20, GetSkill(eSkill.DISARM_TRAPS) +
            + GetSkill(eSkill.LUCK) / 2 + 1 - curTown.Difficulty + 2 * i);

        var r1 = Maths.Rand(1, 0, 100) + diff;
        // Nimble?
        if (!HasTrait(Trait.Nimble)) r1 -= 6;

        if (r1 < trap_odds[skill])
        {
            Game.AddMessage("  Trap disarmed.            ");
            return true;
        }
        else Game.AddMessage("  Disarm failed.          ");

        switch (trap_type)
        {
            case eTrapType.BLADE:
                Game.AddMessage(num_hits < 2 ? "  A knife flies out!" : "  " + num_hits + " knives fly out!");
                for (i = 0; i < num_hits; i++)
                {
                    r1 = Maths.Rand(2 + curTown.Difficulty / 14, 1, 10);
                    Damage(null, r1, 0, eDamageType.WEAPON);
                }
                new Animation_Hold();
                break;

            case eTrapType.DART:
                Game.AddMessage("  A dart flies out.              ");
                r1 = 3 + curTown.Difficulty / 14;
                r1 = r1 + trap_level * 2;
                Poison(r1);
                break;

            case eTrapType.GAS:
                Game.AddMessage("  Poison gas pours out.          ");
                r1 = 2 + curTown.Difficulty / 14;
                r1 = r1 + trap_level * 2;
                foreach (var pc in Party.EachAlivePC())
                    pc.Poison(r1);
                break;

            case eTrapType.EXPLOSION:
                for (i = 0; i < num_hits; i++)
                {
                    Game.AddMessage("  There is an explosion.        ");
                    r1 = Maths.Rand(3 + curTown.Difficulty / 13, 1, 8);
                    Party.Damage(r1, eDamageType.FIRE);
                }
                break;

            case eTrapType.SLEEP_RAY:
                Game.AddMessage("  A purple ray flies out.          ");
                r1 = 200 + curTown.Difficulty * 100;
                r1 = r1 + trap_level * 400;
                
                Sleep(r1, 50);
                break;
            case eTrapType.DRAIN_XP:
                Game.AddMessage("  You feel weak.            ");
                r1 = 40;
                r1 = r1 + trap_level * 30;
                AwardXP(-r1);
                break;

            case eTrapType.ALERT:
                Game.AddMessage("  An alarm goes off!!!            ");
                curTown.MakeTownHostile();
                break;

            case eTrapType.FLAMES:
                Game.AddMessage("  Flames shoot from the walls.        ");
                r1 = Maths.Rand(10 + trap_level * 5, 1, 8);
                Party.Damage(r1, eDamageType.FIRE);
                break;
            case eTrapType.DUMBFOUND:
                Game.AddMessage("  You feel disoriented.        ");
                foreach (var pc in Party.EachAlivePC())
                    pc.Dumbfound(2 + trap_level * 2);
                break;

            case eTrapType.DISEASE:
                Game.AddMessage("  You prick your finger. ");
                r1 = 3 + curTown.Difficulty / 14;
                r1 = r1 + trap_level * 2;
                Disease(r1);
                break;

            case eTrapType.DISEASE_ALL:
                Game.AddMessage("  A foul substance sprays out.");
                r1 = 2 + curTown.Difficulty / 14;
                r1 = r1 + trap_level * 2;
                foreach (var pc in Party.EachAlivePC())
                    pc.Disease(r1);
                break;
        }
        return true;
    }

    public void ForceWallMe(IExpRecipient perp) 
    { 
        Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.MAGIC); 
    }
    public void FireWallMe(IExpRecipient perp) 
    {

        Damage(perp, Maths.Rand(1, 1, 6) + 1, 0, eDamageType.FIRE);
    }
    public void IceWallMe(IExpRecipient perp) 
    {
        Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.COLD);    
    }
    public void BladeWallMe(IExpRecipient perp) 
    {
        Damage(perp, Maths.Rand(4, 1, 8), 0, eDamageType.WEAPON);  
    }
    public void StinkCloudMe() 
    {
        Curse(Maths.Rand(1, 1, 2));  
    }
    public void SleepCloudMe() 
    {
        Sleep(3, 0);
    }
    public void QuickfireMe()
    {
        Damage(null, Maths.Rand(2, 1, 8), 0, eDamageType.FIRE);
    }
    public void FireBarrierMe()
    {
        Damage(null, Maths.Rand(2, 1, 10), 0, eDamageType.MAGIC);
    }
    public void WebSpaceMe()
    {
        Web(Maths.Rand(1, 2, 3));
    }


    public bool Kill(IExpRecipient who_killed, eLifeStatus type, bool no_save = false)
    {
        Item i = null;

        if (type != eLifeStatus.STONE) i = HasItemEquippedWithAbility(eItemAbil.LIFE_SAVING);

        if (!no_save && type != eLifeStatus.ABSENT && (skills[18] > 0) &&
            Maths.Rand(1, 0, 100) < hitChance[skills[18]])
        {
            Game.AddMessage("  But you luck out!          ");
            cur_health = 0;
            return false;
        }
        else if (i == null || type == eLifeStatus.ABSENT)
        {
            if (Game.Mode != eMode.OUTSIDE)
            {
                var item_loc = Pos;//(BoE.overall_mode >= 10) ? Pos : Party.Pos;
                if (type == eLifeStatus.DEAD)
                    curTown.MakeBloodStain(item_loc);
                else if (type == eLifeStatus.DUST)
                    curTown.MakeCrater(item_loc);

            }
            if (type is eLifeStatus.DEAD or eLifeStatus.DUST)
            {
                new Animation_Hold();
                new Animation_Death(this);
                Dying = true;
            }
            for (var a = 0; a < status.Length; a++) status[a] = 0;
            LifeStatus = type;
            if (Party.ActivePC == this) Party.ActivePC = null;// Party.LeaderPC;
            AP = 0;
                
        }
        else
        {
            Game.AddMessage("  Life saved!              ");
            RemoveItem(i);
            Health += 200;
            return false;
        }
        if (!IsAlive() && Party.CurrentPC == this)
        {
            Party.CurrentPC = Party.LeaderPC;
            if (Party.CurrentPC == null)
            {
                Game.PartyDead = true;
                InventoryWindow.Close();
                StatsWindow.Close();
            }
        }
        if (Party.SingleActingPC == this) Party.SingleActingPC = null;
        return true;
    }

    public void FinishDying()
    {
        Dying = false;
    }


    public bool PoisonWeapon(int how_much, bool always_succeeds = true)
    {
        short[] p_chance = {40,72,81,85,88,89,90,
            91,92,93,94,94,95,95,96,97,98,100,100,100,100};

        foreach (var item in EquippedItemSlots)
            if (item != null && item.IsWeapon())
            {
                var p_level = how_much;
                Game.AddMessage(string.Format("  {0} poisons weapon.", Name));
                var r1 = Maths.Rand(1, 0, 100);
                // Nimble?
                if (HasTrait(Trait.Nimble)) r1 -= 6;
                if (r1 > p_chance[GetSkill(eSkill.POISON)] && !always_succeeds)
                {
                    Game.AddMessage("  Poison put on badly.         ");
                    p_level /= 2;
                    if (Maths.Rand(1, 0, 100) > p_chance[GetSkill(eSkill.POISON)] + 10)
                    {
                        Game.AddMessage(string.Format("  {0} accidentally poisoned!", Name));
                        IncStatus(eAffliction.POISON, p_level);
                    }
                }
                if (!always_succeeds)
                    Sound.Play(55);
                PoisonedWeapon = item;
                IncStatus(eAffliction.POISONED_WEAPON, p_level, 8);

                return true;
            }
        Game.AddMessage("  No weapon equipped.       ");
        return false;
    }

    public void Poison(int how_much, bool silent = false)
    {
        var _level = 0;

        if (IsAlive())
        {
            if ((_level = get_prot_level(eItemAbil.POISON_PROTECTION)) > 0)
                how_much -= Level / 2;
            if ((_level = get_prot_level(eItemAbil.FULL_PROTECTION)) > 0)
                how_much -= _level / 3;
            if (HasTrait(Trait.Frail) && how_much > 1)
                how_much++;
            if (HasTrait(Trait.Frail) && how_much == 1 && Maths.Rand(1, 0, 1) == 0)
                how_much++;

            if (how_much > 0)
            {
                status[2] = Math.Min(status[2] + how_much, 8);
                if (!silent) Game.AddMessage("  " + Name + " poisoned.");
                new Animation_CharFlash(this, Color.LimeGreen, "017_shortcough");
            }
        }
    }

    public void Heal(int amt, bool silent = false)
    {
        var realamt = Health;
        Health += amt;
        realamt = Health - realamt;
        if (!silent)
        {
            if (realamt > 0)
            {
                Game.AddMessage(string.Format("  {0} healed {1}", Name, realamt));
                new Animation_CharFlash(this, Color.FloralWhite, "052_magic2");
            }
            else if (realamt < 0)
            {
                Game.AddMessage(string.Format("  {0} harmed {1}", Name, -realamt));
                new Animation_CharFlash(this, Color.DarkRed, "052_magic2");
            }
        }
    }

    public void Cure(int amt)
    {
        if (IsAlive() == false) return;
        if (status[2] <= amt)
            status[2] = 0;
        else status[2] -= amt;
        new Animation_CharFlash(this, Color.LemonChiffon, "051_magic1");
    }

    public void Curse(int how_much, bool silent = false)
    {
        if (!IsAlive()) return;
        status[1] = Math.Max(status[1] - how_much, -8);
        if (!silent)
            Game.AddMessage("  " + Name + " cursed.");
        new Animation_CharFlash(this, Color.Black, "043_stoning");
    }
    public void Bless(int how_much, bool silent = false)
    {
        if (!IsAlive()) return;
        IncStatus(eAffliction.BLESS_CURSE, how_much, 8);

        if (!silent)
            Game.AddMessage("  " + Name + " blessed.");

        new Animation_CharFlash(this, Color.Gold, "004_bless");
    }

    public void Dumbfound(int how_much, bool silent = false)
    {
        int r1;

        if (!IsAlive()) return;
        r1 = Maths.Rand(1, 0, 90);
        if (HasItemEquippedWithAbility(eItemAbil.WILL) != null)
        {
            Game.AddMessage("  Ring of Will glows.");
            r1 -= 10;
        }
        if (r1 < Level)
            how_much -= 2;
        if (how_much <= 0)
        {
            Game.AddMessage("  " + Name + " saved.");
            return;
        }
        status[9] = Math.Min(status[9] + how_much, 8);
        if (!silent) Game.AddMessage("  " + Name + " dumbfounded.");
        new Animation_CharFlash(this, Color.DarkSlateBlue, "067_huh");
        Game.give_help(28, 0);
    }
    public void Disease(int how_much, bool silent = false)
    {
        int r1, _level;

        if (!IsAlive()) return;
        r1 = Maths.Rand(1, 0, 100);
        if (r1 < Level * 2)
            how_much -= 2;
        if (how_much <= 0)
        {
            Game.AddMessage("  " + Name + " saved.");
            return;
        }
        if ((_level = get_prot_level(eItemAbil.PROTECT_FROM_DISEASE)) > 0)////
            how_much -= _level / 2;
        if (HasTrait(Trait.Frail) && how_much > 1)
            how_much++;
        if (HasTrait(Trait.Frail) && how_much == 1 && Maths.Rand(1, 0, 1) == 0)
            how_much++;
        SetStatus(eAffliction.DISEASE, Math.Min(Status(eAffliction.DISEASE) + how_much, 8));
        if (!silent) Game.AddMessage("  " + Name + " diseased.");

        new Animation_CharFlash(this, Color.DarkOrange, "066_disease");

        Game.give_help(29, 0);
    }

    public void Sleep(int how_much, int adjust)
    {
        int r1, _level;
        if (!IsAlive()) return;
        if (how_much == 0) return;

        if ((_level = get_prot_level(eItemAbil.WILL)) > 0)
            how_much -= _level / 2;
        if ((_level = get_prot_level(eItemAbil.FREE_ACTION)) > 0)
            how_much -= _level;

        r1 = Maths.Rand(1, 0, 100) + adjust;

        if (r1 < 30 + Level * 2) how_much = -1;

        if (HasTrait(Trait.Alert) || Status(eAffliction.ASLEEP) > 0)
            how_much = -1;

        if (how_much <= 0)
        {
            Game.AddMessage("  " + Name + " resisted.");
            return;
        }

        IncStatus(eAffliction.ASLEEP, how_much, 8);
        Game.AddMessage("  " + Name + " falls asleep.");
        new Animation_CharFlash(this, Color.MidnightBlue, "096_sleep");
       
        AP = 0;
        Game.give_help(30, 0);
    }

    public void Paralyze(int how_much, int adjust)
    {
        int r1, _level;
        if (!IsAlive()) return;
        if (how_much == 0) return;

        if ((_level = get_prot_level(eItemAbil.WILL)) > 0)
            how_much -= _level / 2;
        if ((_level = get_prot_level(eItemAbil.FREE_ACTION)) > 0)
            how_much -= _level * 300;

        r1 = Maths.Rand(1, 0, 100) + adjust;
        if (r1 < 30 + Level * 2)
            how_much = -1;

        if (how_much <= 0)
        {
            Game.AddMessage("  " + Name + " resisted.");
            return;
        }
        IncStatus(eAffliction.PARALYZED, how_much, 5000);
        Game.AddMessage("  " + Name + " paralyzed.");
        new Animation_CharFlash(this, Color.Olive, "090_paralyze");

        AP = 0;

        Game.give_help(32, 0);
    }

    public void Slow(int how_much, bool silent = false)
    {
        if (!IsAlive()) return;

        status[3] = Maths.MinMax(-8, 8, status[3] - how_much);

        if (how_much < 0)
        {
            if (!silent) Game.AddMessage("  " + Name + " hasted.");
            new Animation_CharFlash(this, Color.Orange, "075_cold");
        }
        else
        {
            if (!silent) Game.AddMessage("  " + Name + " slowed.");
            new Animation_CharFlash(this, Color.PaleTurquoise, "075_cold");
        }
            
        if (how_much < 0)
            Game.give_help(35, 0);
    }

    public void Haste(int how_much, bool silent = false)
    {
        if (!IsAlive()) return;

        SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, Status(eAffliction.HASTE_SLOW) + how_much));
        if (how_much > 0)
        {
            if (!silent) Game.AddMessage("  " + Name + " hasted.");
            new Animation_CharFlash(this, Color.Orange, "075_cold");
        }

    }

    public void DrainXP(int how_much, bool silent = false)
    {
        experience = Maths.Max(experience - how_much, 0);
        if (!silent) Game.AddMessage("  " + Name + " drained.");
        new Animation_CharFlash(this, Color.SlateGray, "065_draining");
    }

    public void Web(int how_much, bool silent = false)
    {
        if (!IsAlive()) return;

        status[6] = Math.Min(status[6] + how_much, 8);
        if (!silent) Game.AddMessage("  " + Name + " webbed.");
        new Animation_CharFlash(this, Color.Gray, "017_shortcough");
        Game.give_help(31, 0);
    }

    public void Acid(int how_much, bool silent = false)
    {
        if (!IsAlive()) return;
        if (HasItemEquippedWithAbility(eItemAbil.ACID_PROTECTION) != null)
        {
            if (!silent) Game.AddMessage("  " + Name + " resists acid.");
            return;
        }
        SetStatus(eAffliction.ACID, Maths.Min(8,Status(eAffliction.ACID) + how_much));// += how_much;
        if (!silent) Game.AddMessage("  " + Name + " covered with acid!");
        new Animation_CharFlash(this, Color.GreenYellow, "042_dang");
    }

    public void Scare(int how_much, bool silent = false)
    {
        //PCs can't actually be scared in BoE. Put in for ICharacter
    }

    public void AwardXP(int amount)
    {
        if (amount < 0)
        {
            experience = Math.Max(experience + amount, 0);
            Game.AddMessage("  " + Name + " drained.");
            return;
        }

        int adjust, add_hp;
        int[] xp_percent = {150,120,100,90,80,70,60,50,50,50,
            45,40,40,40,40,35,30,25,23,20,
            15,15,15,15,15,15,15,15,15,15};
        if (Level > 49)
        {
            Level = 50;
            return;
        }
        if (amount > 200)
        { 
            return;
        }
        if (amount < 0)
        { 
            return;
        }
        if (!IsAlive()) return;

        if (Level >= 40)
            adjust = 15;
        else 
            adjust = xp_percent[Level / 2];

        if ((amount > 0) && (Level > 7))
        {
            if (Maths.Rand(1, 0, 100) < xp_percent[Level / 2])
                amount--;
        }
        if (amount <= 0)
            return;

        experience += (Math.Max(((amount * adjust) / 100), 0) * 100) / 100;
        Party.total_xp_gained += (Math.Max(((amount * adjust) / 100), 0) * 100) / 100;

        if (experience < 0)
        {
            experience = Level * GetExperienceModifier() - 1;
            return;
        }
        if (experience > Constants.EXPERIENCE_CAP)
        {
            experience = Constants.EXPERIENCE_CAP;
            return;
        }

        if (experience >= (Level * GetExperienceModifier())) Sound.Play("007_cool");
             
        while (experience >= (Level * GetExperienceModifier()))
        {   
            Level++;
            Game.AddMessage(string.Format("  {0} is level {1}!  ", Name, Level));
            skill_pts += (Level < 20) ? 5 : 4;
            add_hp = (Level < 26) ? Maths.Rand(1, 2, 6) + skill_bonus[skills[0]]
                : Math.Max((int)skill_bonus[skills[0]], 0);
            if (add_hp < 0)
                add_hp = 0;
            MaxHealth += add_hp;
            if (MaxHealth > 250)
                MaxHealth = 250;
            cur_health += add_hp;
            if (cur_health > 250)
                cur_health = 250;
        }

    }

    //Get experience To Next Level
    public int GetExperienceModifier()
    {
        int tnl = 100, store_per = 100;

        foreach (var t in Traits)
        {
            if (t.Race)
            {
                tnl = (tnl * (100 + t.Handicap)) / 100;
                break; //Only one race counts
            }
        }

        foreach (var t in Traits)
        {
            if (!t.Race)
                store_per += t.Handicap;
        }

        return (tnl * store_per) / 100;
    }

    public int LevelExperience
    {
        get
        {
            if (Level <= 1) return experience;
            else
                return experience - (Level - 1) * GetExperienceModifier();
        }
    }
    public int ExperienceToNextLevel
    {
        get
        {
            if (Level <= 1) return GetExperienceModifier();
            else
                return Level * GetExperienceModifier() - (Level - 1) * GetExperienceModifier();
        }
    }


    public PCType(bool dummy, int slot)
    {
        if (dummy)
        {
            LifeStatus = eLifeStatus.ABSENT;
            Name = "NOBODY";
        }
        else
        {
            LifeStatus = eLifeStatus.ALIVE;
            SkillPoints = 60;
            Health = 6;
            SetSkill(eSkill.STRENGTH, 1);
            SetSkill(eSkill.DEXTERITY, 1);
            SetSkill(eSkill.INTELLIGENCE, 1);
            Name = "Unnamed";
            Portrait = 8;
            which_graphic = 0;
            Traits.Add(Trait.Human);
            Slot = slot;
            string[] knownspells = {"m_light", "m_spark", "m_minor_haste","m_strength", "m_scare", "m_flame_cloud", 
                "m_identify", "m_scry_monster", "m_goo", "m_true_sight",
                "m_minor_poison", "m_flame", "m_slow", "m_dumbfound", "m_envenom", "m_stinking_cloud", "m_summon_beast",
                "m_conflagration", "m_dispel_fields", "m_sleep_cloud", "m_unlock_doors", "m_haste",
                "m_fireball", "m_long_light", "m_fear", "m_wall_of_force", "m_weak_summoning", "m_flame_arrows",
                "m_web", "m_resist_magic", "p_minor_bless", "p_minor_heal", "p_weaken_poison", "p_turn_undead",
                "p_location", "p_sanctuary", "p_symbiosis", "p_minor_manna", "p_sanctify", "p_stumble",
                "p_bless", "p_cure_poison", "p_curse", "p_light", "p_wound", "p_summon_spirit",
                "p_move_mountains", "p_charm_foe", "p_disease", "p_awaken", "p_heal", "p_light_heal_all",
                "p_holy_scourge", "p_detect_life", "p_cure_paralysis", "p_cure_disease", "p_manna", "p_forcefield", "p_restore_mind",
                "p_smite"};
            foreach (var ms in knownspells)
                KnownSpells.Add(ms, null);

            var race = slot == 1 ? 2 : (slot == 2 ? 1 : 0);
            var item = Item.GetStartItem((int)race * 2);
            Item d;
            Equip(item, eEquipSlot.None, out d);
            item = Item.GetStartItem((int)race * 2 + 1);
            Equip(item, eEquipSlot.None, out d);
        }
    }

    //Make a new default PC
    public PCType(int slotno) {

        LifeStatus = eLifeStatus.ALIVE;
        switch (slotno)
        {
            case 0: Name = "Jenneke"; Portrait = 17;
                break;
            case 1: Name = "Thissa"; Portrait = 52;
                break;
            case 2: Name = "Frrrrrr"; Portrait = 44;
                break;
            case 3: Name = "Adrianna"; Portrait = 14;
                break;
            case 4: Name = "Feodoric"; Portrait = 3;
                break;
            case 5: Name = "Michael"; Portrait = 6;
                break;
        }
        short[] pc_graphics = { 3, 32, 29, 16, 23, 14 };
        byte[,] pc_t = {{0,0,1,0,0,0,1,0,0,0, 0,1,0,0,0},		
            {1,0,0,0,0,1,0,0,0,0, 1,0,0,0,0},	
            {0,0,0,1,0,0,0,0,0,0, 0,0,1,0,0},	
            {0,1,0,0,0,0,0,0,0,0, 0,0,0,0,0},	
            {0,0,0,0,1,0,1,1,0,0, 0,0,0,0,1},	
            {0,1,0,0,0,0,0,0,0,0, 0,0,0,0,0}};
        Slot = slotno;
        which_graphic = 0;
        PoisonedWeapon = null;
        Traits.Clear();
        for (var i = 0; i < 30; i++)
            skills[i] = (i < 3) ? 1 : 0;
            
        for (var i = 0; i < 15; i++)
            status[i] = 0;
        direction = new Direction();
        exp_adj = 100;
        skill_pts = 0;

        if (slotno == 1) Traits.Add(Trait.Slitherzakai);
        else if (slotno == 2) Traits.Add(Trait.Nephilim);
        else Traits.Add(Trait.Human);

        which_graphic = pc_graphics[slotno];
            
#if SUPER_DEFAULT_PCS
            short[,] pc_stats = {{20,20,4, 20,0,0,0,0,0, 0,0,0,0,10, 0,0,20,0,0},
						        {20,20,4, 0,0,20,13,0,13, 0,0,0,0,0, 0,0,0,20,0},
						        {14,20,6, 12,12,0,0,20,0, 0,0,0,0,0, 20,20,0,20,15},
						        {5,6,20, 20,0,0,20,0,0, 7,0,20,0,10, 0,0,0,0,0},
						        {7,9,20, 20,0,0,20,0,0,  7,7,8,0,0, 0,0,0,0,15},
						        {6,5,20, 0,20,0,20,0,10, 0,7,20,20,0, 0,0,0,0,0}}; //6,19
            short[] pc_health = { 300, 300, 240, 200, 200, 200 };
            short[] pc_sp = { 0, 0, 0, 200, 180, 200 };
            experience = 30000;
            Level = 30;
#else
        short[,] pc_stats = {{8,6,2, 6,0,0,0,0,0, 0,0,0,0,1, 0,0,2,0,0},
            {8,7,2, 0,0,6,3,0,3, 0,0,0,0,0, 0,0,0,2,0},
            {8,6,2, 3,3,0,0,2,0, 0,0,0,0,0, 4,4,0,2,1},
            {3,2,6, 2,0,0,2,0,0, 3,0,3,0,1, 0,0,0,0,0},
            {2,2,6, 3,0,0,2,0,0,  2,1,4,0,0, 0,0,0,0,1},
            {2,2,6, 0,2,0,2,0,1, 0,3,3,2,0, 0,0,0,0,0}}; //6,19
        short[] pc_health = { 22, 24, 24, 16, 16, 18 };
        short[] pc_sp = { 0, 0, 0, 20, 20, 21 };
        Level = 1;
        experience = 0;
#endif

        string[] knownspells = {"m_light", "m_spark", "m_minor_haste","m_strength", "m_scare", "m_flame_cloud", 
            "m_identify", "m_scry_monster", "m_goo", "m_true_sight",
            "m_minor_poison", "m_flame", "m_slow", "m_dumbfound", "m_envenom", "m_stinking_cloud", "m_summon_beast",
            "m_conflagration", "m_dispel_fields", "m_sleep_cloud", "m_unlock_doors", "m_haste",
            "m_fireball", "m_long_light", "m_fear", "m_wall_of_force", "m_weak_summoning", "m_flame_arrows",
            "m_web", "m_resist_magic", "p_minor_bless", "p_minor_heal", "p_weaken_poison", "p_turn_undead",
            "p_location", "p_sanctuary", "p_symbiosis", "p_minor_manna", "p_sanctify", "p_stumble",
            "p_bless", "p_cure_poison", "p_curse", "p_light", "p_wound", "p_summon_spirit",
            "p_move_mountains", "p_charm_foe", "p_disease", "p_awaken", "p_heal", "p_light_heal_all",
            "p_holy_scourge", "p_detect_life", "p_cure_paralysis", "p_cure_disease", "p_manna", "p_forcefield", "p_restore_mind",
            "p_smite"
#if SUPER_DEFAULT_PCS
            ,
            "m_poison", "m_ice_bolt", "m_slow_group", "m_magic_map", "m_capture_soul", "m_simulacrum", "m_venom_arrows", "m_wall_of_ice",
            "m_stealth", "m_major_haste", "m_fire_storm", "m_dispel_barrier", "m_fire_barrier", "m_summoning", "m_shockstorm",
            "m_spray_fields", "m_major_poison", "m_group_fear", "m_kill", "m_paralyze", "m_daemon", "m_antimagic_cloud",
            "m_mindduel", "m_flight", "m_shockwave", "m_major_blessing", "m_mass_paralysis", "m_protection", "m_major_summon",
            "m_force_barrier", "m_quickfire", "m_death_arrows", "p_cure_all_poison", "p_curse_all", "p_dispel_undead",
            "p_remove_curse", "p_sticks_to_snakes", "p_martyrs_shield", "p_cleanse", "p_firewalk", "p_bless_party",
            "p_major_heal", "p_raise_dead", "p_flamestrike", "p_mass_sanctuary", "p_summon_host", "p_shatter",
            "p_dispel_fields", "p_heal_all", "p_revive", "p_hyperactivity", "p_destone", "p_summon_guardian",
            "p_mass_charm", "p_protective_circle", "p_pestilence", "p_revive_all", "p_ravage_spirit", "p_resurrect",
            "p_divine_thud", "p_avatar", "p_wall_of_blades", "p_word_of_recall", "p_major_cleansing"
#endif
        };

        foreach (var ms in knownspells)
        {
            KnownSpells.Add(ms, null);
        }

        for (var i = 0; i < 19; i++)
            skills[i] = pc_stats[slotno, i];
        cur_health = pc_health[slotno];
        MaxHealth = pc_health[slotno];

            
        for (var i = 0; i < 15; i++) status[i] = 0;
        cur_sp = pc_sp[slotno];
        MaxSP = pc_sp[slotno];

        for (var i = 0; i < 15; i++) {
            if (pc_t[slotno, i] == 1)
                Traits.Add(Trait.Index[i]);
        }

        var race = HasTrait(Trait.Human) ? 0 : (HasTrait(Trait.Nephilim) ? 1 : 2);

        var item = Item.GetStartItem((int)race * 2);
        Item dummy;
        Equip(item, eEquipSlot.None, out dummy);
        item = Item.GetStartItem((int)race * 2 + 1);
        Equip(item, eEquipSlot.None, out dummy);
    }

    /// <summary>
    /// Called when a party is put into a scenario
    /// </summary>
    public void SetupKnownSpells()
    {
        for (var n = 0; n < KnownSpells.Count; n++)
        {
            var s = KnownSpells.ElementAt(n).Key;
            if (MagicSpell.List.Contains(s)) KnownSpells[s] = MagicSpell.List[s];
        }
    }

    //////PC CONSTANTS
    public static short[] skill_cost = {3,3,3,2,2,2, 1,2,2,6,
        5, 1,2,4,2,1, 4,2,5,0};
    public static short[] skill_g_cost = {50,50,50,40,40,40,30,50,40,250,
        250,25,100,200,30,20,100,80,0,0};
    public static short[] skill_bonus = {-3,-3,-2,-1,0,0,1,1,1,2,
        2,2,3,3,3,3,4,4,4,5,5};
    public static short[] skill_max = {20,20,20,20,20,20,20,20,20,7,
        7,20,20,10,20,20,20,20,20};

    public void ResetCombatVars() {
        LastAttacked = null;
        Parry = 0;
        Provocation = Math.Max(Provocation - 1, 0); //Provocation score automatically decays every turn
    }

    public void set_pc_moves() //This is called for each pc at the start of each combat turn
    {
        int i_level;

        if (!IsAlive())
            AP = 0;
        else {
            AP = HasTrait(Trait.Sluggish) ? 3 : 4;
            AP = Maths.MinMax(1, 8, AP - (EncumbranceRoll / 3));

            if ((i_level = get_prot_level(eItemAbil.SPEED)) > 0) AP += i_level / 7 + 1;
            if ((i_level = get_prot_level(eItemAbil.SLOW_WEARER)) > 0) AP -= i_level / 5;

            if ((status[3] < 0) && (Party.Age % 2 == 1)) // slowed?
                AP = 0;
            else { // do webs
                AP = AP - status[6] / 2;
                if (AP == 0) {
                    Game.AddMessage(Name + " must clean webs.");
                    status[6] = Math.Max(0, status[6] - 3);
                }
            }
            if (status[3] > 7)
                AP *= 3;
            else if (status[3] > 0)
                AP *= 2;
            if ((status[11] > 0) || (status[12] > 0))
                AP = 0;
        }
    }

    private int get_prot_level(eItemAbil abil) {
        foreach (var item in EachEquippedItem()) {
            if (item.Ability == abil) return item.AbilityStrength;
        }
        return -1;
    }

    public int EncumbranceRoll
    {
        get
        {
            int store = 0, what_val;

            foreach (var item in EachEquippedItem())
            {
                what_val = item.Awkward;
                if ((what_val == 1) && (Maths.Rand(1, 0, 130) < hitChance[skills[8]]))
                    what_val--;
                if ((what_val > 1) && (Maths.Rand(1, 0, 70) < hitChance[skills[8]]))
                    what_val--;
                store += what_val;
            }
            return store;
        }
    }

    public int TotalEncumbrance
    {
        get
        {
            var store = 0;
            foreach (var item in EachEquippedItem())
                store += item.Awkward;
            return store;
        }
    }

    public int GetSkillBonus(eSkill which)
    {
        short tr;

        tr = skill_bonus[skills[(int)which]];
        if (which == eSkill.INTELLIGENCE)
        { //Skill is Intelligence
            if (HasTrait(Trait.MagicallyApt)) //Boost if Magically apt
                tr++;
        }
        if (which == eSkill.STRENGTH)
        { //Skill is strength
            if (HasTrait(Trait.Strong))  //Boost if Exceptional Strength
                tr++;
        }
        return tr;
    }

    public void CastUnlock(Location target)
    {
        int[] combat_percent = {150,120,100,90,80,80,80,70,70,70,70,70,67,62,57,52,47,42,40,40};

        var ter = curTown.TerrainAt(target);

        switch (ter.Special)
        { 
            case eTerSpec.UNLOCKABLE_TERRAIN:
            case eTerSpec.UNLOCKABLE_BASHABLE:
                var r1 = Maths.Rand(1, 0, 100) - 5 * GetSkillBonus(eSkill.INTELLIGENCE) + 5 * curTown.Difficulty;
                r1 += Convert.ToInt32(ter.Flag2) * 7; //unlock_adjust (door resistance)
                if (Convert.ToInt32(ter.Flag2) == 10) r1 = 10000;

                r1 = 0;

                if (r1 < (135 - combat_percent[Maths.Min(19, Level)]))
                {
                    Game.AddMessage("  Door unlocked.                 ");
                    Sound.Play(9);
                    curTown.AlterTerrain(target, ter.Layer, ter.GetUnlocked());
                }
                else
                {
                    Sound.Play(41);
                    Game.AddMessage("  Didn't work.                  ");
                }
                break;

            default:
                Game.AddMessage("  Wrong terrain type.               ");
                break;
        }
    }
}