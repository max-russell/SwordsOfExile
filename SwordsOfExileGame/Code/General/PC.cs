//#define SUPER_DEFAULT_PCS //This makes the default prefabricated PCs high level, for testing purposes

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    public partial class PCType : IInventory, ICharacter, IExpRecipient, IAnimatable
    {
        PartyType Party { get { return Game.CurrentParty; } }

        //MY STUFF
        public int Slot = 0; //Keep a record of what slot this PC is in.
        public int AP {get{return actionPoints;} set{ actionPoints = Maths.Max(0, value);}} //Keeps track of PC's action points (Vogel stores this outside in pc_moves[])
        int actionPoints;
        public int Parry; //Vogel stores outside in pc_parry. I don't. Because I'm not stupid.
        public int MarkedDamage;
        public eAttitude MyAttitude() { return eAttitude.FRIENDLY; }
        public bool AlliedWith(ICharacter ch)
        {
            return ch.MyAttitude() == eAttitude.FRIENDLY || ch.MyAttitude() == eAttitude.NEUTRAL;
        }
        public bool NotDrawn { get { return notDrawn; } set { notDrawn = value; } } //Temporarily don't draw (used in teleporting animations)
        bool notDrawn = false;

        public int Provocation; //This is calculated at the end of every npcs turn based on what it did that turn. Attacking or casting a spell is a big provocation.
                                //But if the pc does nothing attention-grabbing it decays back to 0 gradually.
        public ICharacter LastAttacked; //Did the pc attack another character last turn? Used when an enemy npc is deciding who to target.

        public int Width { get { return 1; } }
        public int Height { get { return 1; } }

        int targetingNum;
        public int TargetingNum {get {return targetingNum;} set {targetingNum = value;}} //Used when the player is targeting for firing an arrow / spell etc, so that the player can press a key to select this NPC

        public int Portrait;

        public void MakePCGraphics()
        {
            Gfx.MakePCGraphics(which_graphic, Portrait, out PCTexture, out PortraitTexture);
        }

        eItemFilter _Filter;
        public eItemFilter Filter { get { return _Filter; } 
            set 
            { 
                foreach (PCType pc in Party.EachAlivePC())
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


        string name = ""; //char[] name = new char[20];
        public string Name { get { return name; } set { name = value; } }
        int[] skills = new int[30];
        int max_health, max_sp, experience;
        int level;
        public int Level {get {return level;} set {level = value;}}
        int cur_health, cur_sp;
        int skill_pts;
        public int[] status = new int[15];

        public string DeathSound { get { return "021_pcdying"; } }

        public void SetSkill(eSkill what, int value) 
        {
            if (what < eSkill.NOT_REALLY_SKILLS) skills[(int)what] = value;
            else if (what == eSkill.HEALTH) { max_health = value; cur_health = value; }
            else { max_sp = value; cur_sp = value; }
        }
        public int GetSkill(eSkill what) 
        { 
            if (what < eSkill.NOT_REALLY_SKILLS) return skills[(int)what];
            if (what == eSkill.HEALTH) return MaxHealth; //This is only for the sake of the Stat Window Control
            return MaxSP;
        }

        static int[] skillCosts = {3,3,3,2,2,2, 1,2,2,6, 5, 1,2,4,2,1, 4,2,5};
        static int skillCostHealth = 1, skillCostSpellPts = 1;
        public int GetSkillCost(eSkill what)
        {
            if (what < eSkill.NOT_REALLY_SKILLS) return skillCosts[(int)what];
            if (what == eSkill.HEALTH) return skillCostHealth; //This is only for the sake of the Stat Window Control
            return skillCostSpellPts;
        }

        static int[] skillPrices =  {50,50,50,40,40,40,30,50,40,250,250,25,100,200,30,20,100,80,0};
        static int skillPriceHealth = 10, skillPriceSpellPts = 15;
        public int GetSkillPrice(eSkill what)
        {
            if (what < eSkill.NOT_REALLY_SKILLS) return skillPrices[(int)what];
            if (what == eSkill.HEALTH) return skillPriceHealth; //This is only for the sake of the Stat Window Control
            return skillPriceSpellPts;
        }


        public int Health { get { return cur_health; } set { cur_health = Maths.MinMax(0, MaxHealth, value); } }
        public int MaxHealth {get {return max_health;}}
        public int SP { get { return cur_sp; } set { cur_sp = Maths.MinMax(0, max_sp, value); } }
        public int MaxSP { get { return max_sp; } }
        public int SkillPoints { get { return skill_pts; } set { skill_pts = value; if (skill_pts < 0) skill_pts = 0; } }
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
        public void SetStatus(eAffliction type, int val, int min = Int32.MinValue, int max = Int32.MaxValue) { status[(int)type] = Maths.MinMax(min,max,val); }
        public void IncStatus(eAffliction type, int val, int max = Int32.MaxValue)
        {
            status[(int)type] += val;
            if (status[(int)type] > max) status[(int)type] = max;
        }
        public void DecStatus(eAffliction type, int val, int min = Int32.MinValue)
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
            string degree= "";
            int n = ch.Status(type);
            if (n == 0) return degree;
            if (n >=6 || n <= -6)  degree = "(Strong)";
            else if (n >= 3 || n <= -3) degree = "(Moderate)";
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

        //item_record_type[] items = new item_record_type[24];

        public List<Item> ItemList = new List<Item>();
        //public List<Item> equip = new List<Item>(); //Which items in items are equipped.
        public Item[] EquippedItemSlots = new Item[13];
        public Item PoisonedWeapon;

        //public Boolean[] priest_spells = new Boolean[62], mage_spells = new Boolean[62];
        public Dictionary<string, MagicSpell> KnownSpells = new Dictionary<string, MagicSpell>();
        //public Dictionary<string, MagicSpell> FavouriteSpells = new Dictionary<string, MagicSpell>(); //The spells from above list player has marked as favourite for easy access

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

        //List<string> knownSpellIDList = new List<string>(); //IDs of all known spells - includes spell ids from other scenarios that aren't in the currently loaded one - stored here so the
        //spells the characters know are preserved.

        public int which_graphic;
        


        //static string[] traitNames = {
        //                                 "Toughness",
        //                                 "Magically Apt",
        //                                 "Ambidextrous",
        //                                 "Nimble Fingers",
        //                                 "Cave Lore",
        //                                 "Woodsman",
        //                                 "Good Constitution",
        //                                 "Highly Alert",
        ////                                 "Exceptional Strength",
        //                                 "Recuperation",
        //                                 "Sluggish",
        //                                 "Magically Inept",
        //                                 "Frail",
        //                                 "Chronic Disease",
        //                                 "Bad Back",
        //                                 "Pacifist",
        //                                 "Human",
        //                                 "Slitherzakai",
        //                                 "Nephilim"
        //                             }
        //List<eTrait> Traits = new List<eTrait>();//new Boolean[15];
        //public bool HasTrait(eTrait t) { return Traits.Contains(t);}

        public List<Trait> Traits = new List<Trait>();//new Boolean[15];
        public bool HasTrait(Trait t) { return Traits.Contains(t); }

        public int exp_adj;
        //public ePCRace race; //Race is now a trait
        Direction direction;

        static short[] hitChance = {20,30,40,45,50,55,60,65,69,73,
							77,81,84,87,90,92,94,96,97,98,99
							,99,99,99,99,99,99,99,99,99,99
							,99,99,99,99,99,99,99,99,99,99,
							99,99,99,99,99,99,99,99,99,99};

        //public bool IsNotHere() { return false; }

        public Direction Dir
        { get { return direction; } set 
        { direction.Dir = value.Dir; } }

        public void PositionPConPC(PCType pc)
        {
            pos = pc.pos;
            direction = pc.direction;
        }

        public bool OnSpace(Location loc) {return loc == Pos;}

        public bool TurnFinished
        {
            get
            {
                return AP == 0;
            }
        }

        //Returns all items, whether equipped or in main inventory
        public IEnumerable<Item> EachItemHeld()
        {
            foreach (Item i in ItemList) yield return i;
            foreach (Item i in EquippedItemSlots) if (i != null) yield return i;
        }

        //ICharacter stuff
        public Location Pos { get { return pos; } set { pos = value; } } //PC's current position 
        Location pos;
        //public void StartMovingAnim(Direction dir) { moveChar = new MovingCharacter(this, dir); }
        //public void AdvanceMovingAnim() { if (moveChar != null && moveChar.AdvanceMove()) moveChar = null; }
        //public Vector2 MovingAnimAdjustment {get { if (moveChar != null) return moveChar.GetMovePosAdjustment(); else return Vector2.Zero; }}
        //public bool MoveAnimInProgress() { return moveChar != null; }
        //MovingCharacter moveChar;
        IAnimCharacter animAction;
        public IAnimCharacter AnimAction { get { return animAction; } set { animAction = value; } }
        IAnimCharacter animFlash;
        public IAnimCharacter AnimFlash { get { return animFlash; } set { animFlash = value; } }


        //public bool DoingMovingAnim { get { return MoveChar != null; } }
        //public void SetMovingAnim(MovingCharacter mc) { moveChar = mc; }
        TownMap curTown { get { return Game.CurrentMap as TownMap; } }

        public string TooltipInfo(bool brief)
        {
            if (brief)
                return name;

            string txt = string.Format("@b{0}@e@n  @9@iLevel: {1}@n  Exp: {2}\\{3}@n  Health: {4}\\{5}@n  Mana: {6}\\{7}",
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

        //public bool GiveItem(Item item, bool ignore_weight, bool print)
        //{
        //    if (item.Variety == eVariety.Gold)
        //    {
        //        Party.gold += item.Level;
        //        Game.AddMessage("You get some gold.");
        //        return true;
        //    }
        //    if (item.Variety == eVariety.Food)
        //    {
        //        Party.food += item.Level;
        //        Game.AddMessage("You get some food.");
        //        return true;
        //    }
        //    //if (ItemList.Count >= INVENTORY_MAXIMUM || !IsAlive())
        //    //    return false;
        //    //if (!ignore_weight && item.Weight > carryLimit - pc_carry_weight())
        //    //{
        //    //    if (print)
        //    //    {
        //    //        Sound.SysBeep(20);
        //    //        Game.AddMessage("Item too heavy to carry.");
        //    //    }
        //    //    return false;
        //    //}
        //    AddItem(item, true);
        //    if (print)
        //    {
        //        Game.AddMessage(String.Format("  {0} gets {1}.", name, item.KnownName));
        //        Party.CurrentPC = this;
        //    }
        //    return true;
        //}

        public void GiveNewItem(string item_id, bool identified = false, int charges = -1)
        {
            Item item;

            if (Item.List.TryGetValue(item_id, out item))
            {
                item = item.Copy(identified, charges);

                if (!identified && Party.IdentifyItemRoll()) item.Identified = true;

                AddItem(item, true);
                Game.AddMessage(String.Format("  {0} gets {1}.", name, item.KnownName));
            }
            else
            {
                Game.FlagError("Script Runtime Error", "Item with ID '" + item_id + "' not found.", Script.FunctionRunning());
            }
        }

        ///// <summary>
        ///// Removes all items that the specified SpecialClass. This is called by certain Special Nodes.
        ///// </summary>
        ///// <param name="_class">SpecialClass</param>
        ///// <param name="equipped">Only if the item is equipped.</param>
        ///// <returns>Number of items that were taken (including stacked items)</returns>
        //public int TakeAllItemsOfClass(int _class, bool equipped = false)
        //{
        //    int tally = 0;
        //    //List<Item> list = equipped ? equip : items;
        //    if (!equipped)
        //    {
        //        for (int i = ItemList.Count - 1; i >= 0; i--)
        //        {
        //            if (ItemList[i].SpecialClass == _class)
        //            {
        //                if (ItemList[i].Charges > 1)
        //                    tally += ItemList[i].Charges;
        //                else
        //                    tally++;
        //                RemoveItem(ItemList[i]);
        //            }
        //        }
        //    }

        //    int slot = 0;
        //    foreach (Item t in EquippedItemSlots)
        //    {
        //        if (t == null) continue;
        //        if (t.SpecialClass == _class)
        //        {
        //            if (t.Charges > 1) tally += t.Charges;
        //            else tally++;
        //            EquippedItemSlots[slot] = null;
        //        }

        //        slot++;
        //    }
        //    return tally;
        //}

        #region INVENTORY STUFF

        //IInventory Stuff
        //public IEnumerable<Item> MyInventory()
        //{
        //    foreach (Item i in items) /*if (!equip.Contains(i))*/ yield return i;
        //}
            //List<Item> MyInventory { get { return items; } /*set { items = value; }*/ }
        


        /// <summary>
        /// Returns all items in the inventory, and the slot number too
        /// </summary>
        /// <returns></returns>
        public IEnumerable<Tuple<Item, int>> EachItem()
        {
            foreach(Item n in ItemList)
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

            Item replaces = GetSlot(slotno);

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
                    int n = 0;
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
                    eItemFilter f = _Filter;
                    _Filter = eItemFilter.ALL;
                    int n = 0;
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
                //lastSlot = -1;
                //foreach (Item i in ItemList) lastSlot = i.Pos.x > lastSlot ? i.Pos.x : lastSlot;



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
                foreach (Item i in ItemList)
                    if (item != i && item.CombinableWith(i))
                    {
                        i.Charges += item.Charges;
                        if (i.Charges > Constants.ITEM_STACK_LIMIT) { item.Charges = i.Charges - Constants.ITEM_STACK_LIMIT; i.Charges = Constants.ITEM_STACK_LIMIT; continue; } //Can only stack to 999
                        return true;
                    }

            //Get Items slot in the ALL items filter (Stored in Pos.X)
            int n = 0;
            bool slotfree = false;
            while (!slotfree) {
                slotfree = true;
                foreach (Item i in ItemList)
                    if (i.Pos.X == n) { n++; slotfree = false; break; }

            }
            item.Pos.X = n;

            //Get Item's slot in the specific filter for this item type (Stored in Pos.Y)
            n = 0;
            slotfree = false;
            eItemFilter fg = item.GetFilterGroup();
            while (!slotfree)
            {
                slotfree = true;
                foreach (Item i in ItemList)
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
            //lastSlot = -1;
            //foreach (Item i in ItemList) lastSlot = i.Pos.x > lastSlot ? i.Pos.x : lastSlot;
            return true;
        }

        public void ArrangeItems()
        {
            var toremove = new List<Item>();

            //First combine any items that can be combined.
            //Items that should then be removed are put into the toremove list
            foreach (Tuple<Item, int>i1 in EachItem())
            {
                if (toremove.Contains(i1.Item1)) continue;

                bool reachedi1 = false;
                foreach (Tuple<Item, int> i2 in EachItem())
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
            int newslot = 0;
            foreach (Tuple<Item, int> i1 in EachItem())
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
            Item budged = GetEquipped(slot);

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

            bool budged_poisoned = false;
            if (budged != null)
                if (!CanUnequip(slot))
                    failed = budged;
                else
                {
                    if (PoisonedWeapon == budged) budged_poisoned = true;
                    Unequip(budged);
                    AddItem(budged,false);
                    //StartItemDrag(budged, Action.PC);
                }

            if (failed == null)
            {
                //Two handed weapons, knock off anything in the offhand to the PCs inventory;
                if (item.Variety == eVariety.TwoHanded && slot == eEquipSlot.MainHand)
                {
                    Item offhand = GetEquipped(eEquipSlot.OffHand);
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
                if ((item.Variety == eVariety.Shield || item.Variety == eVariety.OneHanded) && slot == eEquipSlot.OffHand)
                {
                    Item mainhand = GetEquipped(eEquipSlot.MainHand);
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

            eEquipSlot slotneeded = item.SlotNeeded;
            if (slotneeded == eEquipSlot.None) return eEquipSlot.None;
            if (EquippedItemSlots.Contains(item)) return eEquipSlot.None;

            if (slot == eEquipSlot.None)
            {
                eEquipSlot use = GetEquipped(slotneeded) == null ? slotneeded : eEquipSlot.None;

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

        //public bool EquipAt(Item item, eEquipSlot slot, out Item replaced_item, bool regardless_of_curse = false)
        //{
        //    
        //}

        public void UnequipCursed()
        {
            foreach (Item i in EachEquippedItem())
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
                    eEquipSlot s = getEquipSlot(item);
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

        IEnumerable<Item> EachEquippedItem()
        {
            foreach(Item i in EquippedItemSlots)
                if (i != null) yield return i;
        }

        public Item GetEquipped(eEquipSlot slot)
        {
            return EquippedItemSlots[(int)slot];
        }

        eEquipSlot getEquipSlot(Item item)
        {
            for (int n = 0; n < EquippedItemSlots.Length; n++)
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
            foreach (Tuple<Item, int> i in EachItem()) 
                if (i.Item2 == slotno /*&& i != Gui.MoveItem*/) return i.Item1;
            return null;
        }

        //public int LastSlot { get { return lastSlot; } }

        /// <summary>
        /// Removes item from inventory (not from Equipped Items)
        /// </summary>
        /// <param name="i"></param>
        /// <returns></returns>
        public bool RemoveItem(Item i)//, bool regardless_of_curse=false)
        {
            if (ItemList.Contains(i))
            {

                ItemList.Remove(i);
                //lastSlot = -1;
                //foreach (Item item in ItemList) lastSlot = item.Pos.x > lastSlot ? item.Pos.x : lastSlot;
                return true;
            }

            return false;
            
        }

        void handlePopUp(object o, object o2, int data)
        {//string option) {
            Item c = (Item)o;//owner.GetSlot(popupSlot);//carryables.Find(cFind => cFind.Pos.X == popupSlot);

            //PCType pc = Party.CurrentPC;//owner as PCType;
            switch (data)
            {
            case PopUpMenuData.EQUIP:
                    new Action(eAction.EquipItem) { PC = this, Item = c, InventoryFrom = this };
                //Action.Requested = eAction.EquipItem; 
                //Action.PC = this;  
                //Action.Item = c;
                //Action.InventoryFrom = this;
                break;
            case PopUpMenuData.UNEQUIP:
                new Action(eAction.UnequipItem) { PC = this, Item = c};
                //Action.Requested = eAction.UnequipItem; 
                //Action.PC = this; 
                //Action.Item = c; 
                break;
            case PopUpMenuData.DROP:
                //if (LootWindow.IsOpen)//Gui.GetWindowOfType(typeof(LootWindow)) != null)
                //    Action.Requested = eAction.DropItemToLootSpot;
                //else
                //    Action.Requested = eAction.TargetDropItem;
                //Action.PC = this;
                //Action.Item = c;
                new Action(LootWindow.IsOpen ? eAction.DropItemToLootSpot : eAction.TargetDropItem) { PC = this, Item = c};
                break;
            case PopUpMenuData.GIVE: 
                //Action.Requested = eAction.GiveItem; 
                //Action.PC = this; 
                //Action.PC2 = o2 as PCType; 
                //Action.Item = c;
                new Action(eAction.GiveItem) { PC = this, PC2 = o2 as PCType, Item = c };
                break;
            case PopUpMenuData.USE:
                //Action.Requested = eAction.UseItem;
                //Action.PC = this;
                //Action.Item = c;
                new Action(eAction.UseItem) { PC = this, Item = c };
                break;
            case PopUpMenuData.SELL:
                //Action.Requested = eAction.SellItem;
                //Action.PC = this;
                //Action.Item = c;
                //Action.InventoryFrom = this;
                //Action.InventoryTo = (IInventory)o2;
                var a = new Action(eAction.SellItem) { PC = this, Item = c, InventoryFrom = this, InventoryTo = (IInventory)o2 };
                a.PlaceDraggedItem(eAction.PlaceInInventory);
                new Action(eAction.NONE);
                //Action.Requested = eAction.NONE;
                break;
            case PopUpMenuData.IDENTIFY:
                c.Identify((o2 as IdentifyWindow.IdentifyBox).Price);
                break;
            case PopUpMenuData.ENCHANT:
                EnchantingWindow.EnchantingBox e = o2 as EnchantingWindow.EnchantingBox;
                c.Enchant(e.Enchantment,e.EnchantCost(c));
                break;

            }
        }

        public void MakeItemToolTip(Item i, XnaRect r)//int slotno)
        {
            //Item i = GetSlot(slotno);

            if (i != null)
            {
                var tt = new StringBuilder();
                tt.Append(i.TooltipInfo());

                if (i.Identified && HasEquipped(i) != eEquipSlot.None)
                {
                    if (i.IsRangedWeapon())
                    {
                        int hit_bonus = i.Bonus;
                        hit_bonus += GetSkillBonus(eSkill.DEXTERITY);
                        Item s = HasItemEquippedWithAbility(eItemAbil.ACCURACY);
                        if (s != null)
                            hit_bonus += s.AbilityStrength / 2;

                        if (HasTrait(Trait.Nephilim)) hit_bonus += 2;

                        tt.AppendFormat("@n@6   {0}{1}@e", hit_bonus < 0 ? "Penalty to hit: %" : "Bonus to hit: %", Math.Abs(hit_bonus));
                    }
                    else if (i.IsAmmo())
                    {
                        int dam_bonus = i.Bonus;
                        Item s = HasItemEquippedWithAbility(eItemAbil.ACCURACY);
                        if (s != null)
                            dam_bonus += s.AbilityStrength / 2;
                        tt.AppendFormat("@n@6   Damage: 1-{0} {1}", i.Level, dam_bonus == 0 ? "" : dam_bonus < 0 ? "(" + dam_bonus + ")" : "(+" + dam_bonus + ")");
                    }
                    else if (i.IsWeapon())
                    {
                        int hit_adj = GetSkillBonus(eSkill.DEXTERITY) * 5 - TotalEncumbrance * 5
                            + 5 * Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE));
                        if (!HasTrait(Trait.Ambidextrous) && HasEquipped(i) == eEquipSlot.OffHand)
                            hit_adj -= 25;

                        int dam_adj = GetSkillBonus(eSkill.STRENGTH) + Maths.MinMax(-8, 8, Status(eAffliction.BLESS_CURSE));

                        Item s = HasItemEquippedWithAbility(eItemAbil.SKILL);
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

                        tt.AppendFormat("@n@6   {0}{1}@e", hit_adj < 0 ? "Penalty to hit: %" : "Bonus to hit: %", Math.Abs(hit_adj));
                        tt.AppendFormat("@n@6   Damage: 1-{0} {1}", i.Level, dam_adj == 0 ? "" : dam_adj < 0 ? "(" + dam_adj + ")" : "(+" + dam_adj + ")");
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

                new ToolTipV2(false, r, tt.ToString(), -1);//ToolTip(tt.ToString(), -1, false);
            }
        }

        public void MakeInventoryPopUpWindow(Item c)//int slot)
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

                if (c.IsEquippable)//CanEquip(c))
                    if (HasEquipped(c) != eEquipSlot.None) popupoptions.Add(new PopUpMenuData("Unequip", c, null, PopUpMenuData.UNEQUIP));
                    else popupoptions.Add(new PopUpMenuData("Equip", c, null, PopUpMenuData.EQUIP));
                if (c.IsUseable())
                    popupoptions.Add(new PopUpMenuData("Use", c, null, PopUpMenuData.USE));
                popupoptions.Add(new PopUpMenuData("Drop", c, null, PopUpMenuData.DROP));

                if (Game.Mode == eMode.COMBAT)
                {
                    foreach (PCType pc in Party.EachAlivePC())
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


        int pc_carry_weight()
        {
            int storage = 0;
            Boolean airy = false, heavy = false;

            foreach (Item item in ItemList)
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
            Item which_item = HasItemEquippedWithAbility(eItemAbil.LOCKPICKS);
            TerrainRecord terrain = curTown.TerrainAt(loc);

            if (which_item == null) return -1; //No lockpick, no chance.
            if (terrain.Special != eTerSpec.UNLOCKABLE_TERRAIN && terrain.Special != eTerSpec.UNLOCKABLE_BASHABLE) return -2;
            if (Convert.ToInt32(terrain.Flag2) >= 10) return -3;

            int chance = 100 - (Convert.ToInt32(terrain.Flag2) * 15 + 30);

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
            int chance = PickLockChance(loc);

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

                Item which_item = HasItemEquippedWithAbility(eItemAbil.LOCKPICKS);
                if (Maths.Rand(1, 0, 100) + which_item.AbilityStrength * 7 < 75)
                {
                    Game.AddMessage("  Pick breaks.                ");
                    UseItemCharge(which_item);
                    //which_item.remove_charge();//(pc_num,which_item);
                }
                Sound.Play(41);
            }

            //int r1 = Maths.Rand(1, 0, 100) + which_item.AbilityStrength * 7;

            //if (r1 < 75) will_break = true;

            //r1 = Maths.Rand(1, 0, 100) - 5 * stat_adj(eSkill.DEXTERITY) + curTown.Difficulty * 7
            // - 5 * GetSkill(eSkill.LOCKPICKING) - which_item.AbilityStrength * 7;

            //// Nimble?
            //if (!HasTrait(eTrait.NIMBLE)) r1 -= 8;

            //if (pc_has_abil_equip(eItemAbil.THIEVING) != null) r1 = r1 - 12;

            //switch (curTown.PickorBashDoor(r1, 30, loc))
            //{
            //case 0:
            //    Game.AddMessage("  Wrong terrain type.           ");
            //    break;
            //case 1:
            //    Game.AddMessage("  Didn't work.                ");
            //    if (will_break)
            //    {
            //        Game.AddMessage("  Pick breaks.                ");
            //        which_item.Charges--;
            //        if (which_item.Charges < 1)
            //        {
            //            //items.Remove(which_item);
            //            //equip.Remove(which_item);
            //            Unequip(which_item, false);
            //        }
            //        //which_item.remove_charge();//(pc_num,which_item);
            //    }
            //    Snd.play_sound(41);
            //    break;
            //case 2:
            //    Game.AddMessage("  Door unlocked.                ");
            //    Snd.play_sound(9);
            //    break;
            //}
        }

        public int BashDoorChance(Location loc)
        {
            TerrainRecord terrain = curTown.TerrainAt(loc);

            if (terrain.Special != eTerSpec.UNLOCKABLE_TERRAIN && terrain.Special != eTerSpec.UNLOCKABLE_BASHABLE) return -2;
            if (Convert.ToInt32(terrain.Flag2) >= 10) return -3;

            int chance = 100 - (Convert.ToInt32(terrain.Flag2) * 15 + 40);
            chance += 15 * GetSkillBonus(eSkill.STRENGTH);
            chance -= curTown.Difficulty * 4;
            chance = Maths.MinMax(0, 100, chance);
            return chance;
        }

        public void BashDoor(Location loc)
        {
            //int r1 = Maths.Rand(1, 0, 100) - 15 * stat_adj(eSkill.STRENGTH) + curTown.Difficulty * 4;

            int chance = BashDoorChance(loc);

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

            foreach (Item i in EachEquippedItem())
                if (i.Awkward > 1) return -11;

            if (SP < ms.Cost) return -7;
            if (Game.Mode == eMode.COMBAT && (ms.Where == eSpellWhere.TOWN || ms.Where == eSpellWhere.TOWN_AND_OUTDOOR || ms.Where == eSpellWhere.OUTDOOR)) return -8;
            if (Game.Mode == eMode.OUTSIDE && (ms.Where == eSpellWhere.COMBAT || ms.Where == eSpellWhere.TOWN || ms.Where == eSpellWhere.TOWN_AND_COMBAT)) return -9;
            if (Game.Mode == eMode.TOWN && (ms.Where == eSpellWhere.COMBAT || ms.Where == eSpellWhere.OUTDOOR)) return -10;

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
                int has = 0;
                foreach (Item i in EachItemHeld())
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
            IMap map = Game.CurrentMap;

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
                    //AP = 0;
                    if (map is TownMap) curTown.InflictFields(this);
                }
                else
                {
                    if (Party.Vehicle != null && Party.Vehicle.Type == eVehicleType.HORSE)
                        Party.LeaveVehicle();
                    else
                        Game.AddMessage("Pause.");

                    foreach (PCType pc in Party.EachAlivePC())
                    {
                        if (pc.Status(eAffliction.WEBS) > 0)
                        {
                            Game.AddMessage(String.Format("{0} cleans webs.", pc.Name));
                            pc.CounteractStatus(eAffliction.WEBS, 2);
                        }
                        if (map is TownMap) curTown.InflictFields(pc);
                    }
                }
                

                return true;
            }
            ///////////////////////////////////////////PAUSE/////////////////////////////////////////

            Location newpos = Pos + mod;
            Direction newdir = new Direction(mod);

            //Can try to attack character if one is there.
            ICharacter ch = map is TownMap ? ((TownMap)map).CharacterThere(newpos) : null;
            if (ch is NPC)
            {
                NPC npc = (NPC)ch;
                if (npc.IsABaddie)
                    return (Attack(ch));
                else
                {
                    if (Game.Mode != eMode.COMBAT) return false;
                    eDialogPic p = eDialogPic.CREATURE;
                    if (npc.Record.Width == 2 && npc.Record.Height == 1) p = eDialogPic.CREATURE2x1;
                    else if (npc.Record.Width == 1 && npc.Record.Height == 2) p = eDialogPic.CREATURE1x2;
                    else if (npc.Record.Width == 2 && npc.Record.Height == 2) p = eDialogPic.CREATURE2x2;
                    new MessageWindow(confirmFriendAttack, "The target is not hostile. Are you sure you want to attack?", p, npc.Record.Picture, "Yes", "No!");

                    //Action.PC = this;
                    //Action.NPC = npc;
                    new Action(eAction.Attack) { PC = this, NPC = npc };
                }
            }

      ///////////////////////////////////////////////////IN A BOAT//////////////////////////////////////////////////
            else if (Party.Vehicle != null)
            {
                if (Party.Vehicle.Type == eVehicleType.BOAT)
                {
                    
                    bool canwalk = map.PCCanTryToWalkThere(newpos, this);

                    if (Vehicle.IsThere(map, newpos) != null) return false; //Can't move onto another vehicle while in one.

                    bool ontoatown = Game.Mode == eMode.OUTSIDE && Game.WorldMap.TownEntranceHere(newpos) != null;

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

                        //Action.PC = this;
                        //Action.Loc = newpos;
                        //Action.Dir = newdir;
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
                foreach (PCType pc in Party.EachIndependentPC())
                {
                    if (newpos == pc.Pos && pc.AP == 0)
                    {
                        Game.AddMessage("Can't switch places.\n  " + pc.Name + " has no moves left");
                        return false;
                    }
                }

                bool boardvehicle = false;

                Vehicle v = Vehicle.IsThere(map, newpos);

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

        void confirmFriendAttack(int button_index)
        {
            //if (button_index == 0)
            //    Action.Requested = eAction.Attack;
            if (button_index != 0)
                new Action(eAction.NONE);
            
        }
        void confirmBoatLanding(int button_index)
        {
            var a = Action.GetCurrent();
            //new Action(eAction.NONE);

            if (button_index == 0)
            {
                if (!Game.CurrentMap.TriggerStepOnSpecials(a.Loc, a.Dir, this, true))
                    //Action.Requested = eAction.BoatLanding;
                    new Action(eAction.BoatLanding) { PC = this, Loc = a.Loc, Dir = a.Dir };
            }
            else
                new Action(eAction.CompleteMove) { PC = this, Loc = a.Loc, Dir = a.Dir };
            //    Action.Requested = eAction.CompleteMove;


           /*     if (!map.TriggerStepOnSpecials(Action.Loc, Action.Dir, this))
                {
                    Party.Vehicle = null;
                    return CompleteMove(Action.Loc, Action.Dir);
                }
            }
            else
                return CompleteMove(Action.Loc, Action.Dir);            
            */
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
            //new Action(eAction.CompleteMove) { Dir = newdir, Loc = newpos, PC = this };
            //return true;
            IMap map = Game.CurrentMap;
            if (Party.Vehicle != null) new Animation_VehicleMove(Party.Vehicle, pos, newpos, false);
            else new Animation_Move(this, pos, newpos, false, false);
            pos = newpos;
            direction.Dir = newdir.Dir;
            Gfx.CentreView(Pos, false);

            //In non-combat mode, all PCs move at the same time.
            if (Game.Mode != eMode.COMBAT)
            {
                foreach (PCType pc in Party.PCList)
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
            IMap map = Game.CurrentMap;

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
                    foreach (PCType pc in Party.PCList)
                        pc.PositionPConPC(this);
                    Gfx.CentreView(Pos, false);
                    map.UpdateVisible();
                    return true;
                }
            }

            bool keep_going = map.CheckSpecialTerrainPC(newpos, this);
            PCType switchPC = null;

            if (keep_going)
            {
                if (Party.Vehicle == null || Party.Vehicle.Type == eVehicleType.HORSE)
                {
                    if (!map.CharacterCanBeThere(newpos, this, true))//!map.TerrainBlocked(newpos) && map.CharacterThere(newpos) == null)
                    {
                        keep_going = false;

                        foreach (PCType pc in Party.EachAlivePC())
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

                bool boardsvehicle = false;

                Vehicle v = Vehicle.IsThere(map, newpos);
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
                    if (map is CombatMap && !((TownMap)map).InActArea(newpos))//map.TerrainAt(newpos).IsPit)
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
                        foreach (PCType pc in Party.PCList)
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
                else //if (map is TownMap)
                {
                    //TownMap town = (TownMap)map;
                    //if (town.IsDoor(newpos))
                    //    Game.AddMessage("Door locked: " + newdir.ToString() + "               ");
                    //els

                        //Game.AddMessage("Blocked: " + newdir.ToString() + "               ");
                }
                //}
            }
            return false;
        }

        public void UseItem(Item item)
        {
	        Boolean take_charge = true,inept_ok = false;
	        int item_use_code;
            eAffliction which_stat=eAffliction.BLESS_CURSE;
	        //char to_draw[60];
	        //location user_loc;
        //creature_data_type *which_m;
        //effect_pat_type s = {{{0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,1,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0},
        //                        {0,0,0,0,0,0,0,0,0}}};

            //OLD -                               0 - everywhere 1 - combat only 2 - town only                         3 - town & combat only  5 - outdoor      4 - can't use 

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


	        eItemAbil abil = item.Ability;
            int level = item.Level;

	        item_use_code = abil_chart[(short)abil];
	        if (item_use_code >= 10) {
		        item_use_code -= 10;
		        inept_ok = true;
		    }

	        //if (is_out()) user_loc = party.p_loc;
	        //if (is_town()) user_loc = c_town.p_loc;
	        //if (is_combat()) user_loc = pc_pos[current_pc];

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
			    if (Game.Mode == eMode.TOWN && (item_use_code == 1 || item_use_code == 5)) {
				    Game.AddMessage("Use: Not while in town. ");
				    take_charge = false;
				}
			    if (Game.Mode == eMode.COMBAT && (item_use_code == 2 || item_use_code == 3 || item_use_code == 5)) {
				    Game.AddMessage("Use: Not in combat.");
				    take_charge = false;
				}
			    if (Game.Mode != eMode.OUTSIDE && item_use_code == 5){
				    Game.AddMessage("Use: Only outdoors.");
				    take_charge = false;
				}
		    }
	        if (take_charge == true) {

                 Game.AddMessage(String.Format("Use: {0}", item.KnownName));

		        if (item.Variety == eVariety.Potion)
		      	        Sound.Play(56);

		        int str = item.AbilityStrength;
		        //store_item_spell_level = str * 2 + 1;

		        int type = item.MagicUseType;

		        switch (abil) {
			        case eItemAbil.POISON_WEAPON: // poison weapon
				        take_charge = PoisonWeapon(str,false);
				        break;
			        case eItemAbil.BLESS_CURSE: case eItemAbil.HASTE_SLOW:  case eItemAbil.AFFECT_INVULN: case eItemAbil.AFFECT_MAGIC_RES:
			        case eItemAbil.AFFECT_WEB: case eItemAbil.AFFECT_SANCTUARY: case eItemAbil.AFFECT_MARTYRS_SHIELD:
                        int min=0;
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
                            foreach (PCType pc in Party.EachAlivePC())
                                pc.SetStatus(which_stat, pc.Status(which_stat) + str, min, 8);
                        else
                            SetStatus(which_stat, Status(which_stat) + str, min, 8);
				        break;
			        case eItemAbil.AFFECT_POISON:
				        switch (type) {
					        case 0: Game.AddMessage("  You feel better."); Cure(str); break;
					        case 1: Game.AddMessage("  You feel ill."); Poison(str); break;
                            case 2: Game.AddMessage("  You all feel better."); foreach (PCType pc in Party.EachAlivePC()) pc.Cure(str); break;
                            case 3: Game.AddMessage("  You all feel ill."); foreach (PCType pc in Party.EachAlivePC()) pc.Poison(str); break;
					        }
				        break;
			        case eItemAbil.AFFECT_DISEASE:
				        switch (type) {
                            case 0: Game.AddMessage("  You feel healthy."); DecStatus(eAffliction.DISEASE, str, 0); break;
                            case 1: Game.AddMessage("  You feel sick."); Disease(str); break;
					        case 2: Game.AddMessage("  You all feel healthy."); foreach (PCType pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.DISEASE,str, 0); break;
                            case 3: Game.AddMessage("  You all feel sick."); foreach (PCType pc in Party.EachAlivePC()) pc.Disease(str); break;
					        }
				        break;
			        case eItemAbil.AFFECT_DUMBFOUND:
				        switch (type) {
					        case 0: Game.AddMessage("  You feel clear headed."); DecStatus(eAffliction.DUMB,str,0); break;
                            case 1: Game.AddMessage("  You feel confused."); Dumbfound(str); break;
					        case 2: Game.AddMessage("  You all feel clear headed."); foreach (PCType pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.DUMB,str,0); break;
                            case 3: Game.AddMessage("  You all feel confused."); foreach (PCType pc in Party.EachAlivePC()) pc.Dumbfound(str); break;
					        }
				        break;
			        case eItemAbil.AFFECT_SLEEP:
				        switch (type) {
					        case 0: Game.AddMessage("  You feel alert."); DecStatus(eAffliction.ASLEEP,str, -8); break;
                            case 1: Game.AddMessage("  You feel very tired."); Sleep(str+1, 200); break;
					        case 2: Game.AddMessage("  You all feel alert."); foreach (PCType pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.ASLEEP,str,-8); break;
                            case 3: Game.AddMessage("  You all feel very tired."); foreach (PCType pc in Party.EachAlivePC()) pc.Sleep(str + 1, 200); break;
					        }
				        break;
			        case eItemAbil.AFFECT_PARALYSIS:
				        switch (type) {
					        case 0: Game.AddMessage("  You find it easier to move."); DecStatus(eAffliction.PARALYZED,str * 100,0); break;
					        case 1: Game.AddMessage("  You feel very stiff."); Paralyze(str * 20 + 10,200); break;
					        case 2: Game.AddMessage("  You all find it easier to move."); foreach (PCType pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.PARALYZED,str * 100,0); break;
					        case 3: Game.AddMessage("  You all feel very stiff."); foreach (PCType pc in Party.EachAlivePC()) pc.Paralyze(str * 20 + 10,200); break;
					        }
				        break;
			        case eItemAbil.AFFECT_ACID:
				        switch (type) {
					        case 0: Game.AddMessage("  Your skin tingles pleasantly."); DecStatus(eAffliction.ACID,str,0); break;
					        case 1: Game.AddMessage("  Your skin burns!"); Acid(str); break;
					        case 2: Game.AddMessage("  You all tingle pleasantly."); foreach (PCType pc in Party.EachAlivePC()) pc.DecStatus(eAffliction.ACID,str,0); break;
                            case 3: Game.AddMessage("  Everyone's skin burns!"); foreach (PCType pc in Party.EachAlivePC()) pc.Acid(str); break;
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
						        foreach (PCType pc in Party.EachAlivePC()) pc.IncStatus(eAffliction.BLESS_CURSE, str,8);
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
					        case 2: Game.AddMessage("  You all feel much smarter."); foreach (PCType pc in Party.EachAlivePC()) pc.SkillPoints += str; break;
                            case 3: Game.AddMessage("  You all feel forgetful."); foreach (PCType pc in Party.EachAlivePC()) pc.SkillPoints = Maths.Max(0,pc.SkillPoints - str); break;
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
					        case 2: Game.AddMessage("  You all feel energized."); foreach (PCType pc in Party.EachAlivePC()) pc.SP += str * 5; break;
                            case 3: Game.AddMessage("  You all feel drained."); foreach (PCType pc in Party.EachAlivePC()) pc.SP -= str * 5; break;
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
                                foreach (PCType pc in Party.EachAlivePC())
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
                                foreach (PCType pc in Party.EachAlivePC())
                                {
                                    pc.Heal(200);
                                    pc.Cure(8);
                                }
						        break;
					        }
				        break;
			        case eItemAbil.CALL_SPECIAL:

                        //switch(type){
                        //    case 0:
                        //        if((is_town()) || ((is_combat()) && (which_combat_type == 1)))
                        //            run_special(SPEC_USE_SPEC_ITEM,2,str,location(),&i,&j,&r1);// Call town special
                        //        else
                        //            run_special(SPEC_USE_SPEC_ITEM,1,str,location(),&i,&j,&r1);// Call outdoor special
                        //    break;
                        //    case 1:
                        //        if((is_town()) || ((is_combat()) && (which_combat_type == 1)))
                        //            run_special(SPEC_USE_SPEC_ITEM,2,str,location(),&i,&j,&r1);// Call town special
                        //        else
                        //            run_special(SPEC_USE_SPEC_ITEM,0,str,location(),&i,&j,&r1);// Call scenario special
                        //    break;
                        //    case 2:
                        //        if((is_town()) || ((is_combat()) && (which_combat_type == 1)))
                        //            run_special(SPEC_USE_SPEC_ITEM,0,str,location(),&i,&j,&r1);// Call scenario special
                        //        else
                        //            run_special(SPEC_USE_SPEC_ITEM,1,str,location(),&i,&j,&r1);// Call outdoor special
                        //    break;
                        //    case 3:
                        //        run_special(SPEC_USE_SPEC_ITEM,0,str,location(),&i,&j,&r1);// Call scenario special
                        //    break;
                        //}
                        break;

                    case eItemAbil.CAST_SPELL:

                        if (MagicSpell.List.Contains(item.SpellID))
                        {
                            //Action.Spell = MagicSpell.List[item.SpellID];
                            //Action.Item = item;

                            eAction ac = eAction.NONE;
                            PCType pc2 = null;
                            switch (MagicSpell.List[item.SpellID].Target)
                            {
                            case eSpellTarget.CASTER:
                                ac = eAction.CastSpell;
                                break;
                            case eSpellTarget.LIVING_PC: case eSpellTarget.DEAD_PC: //Use item spells can't target another specific PC
                                //Action.PC2 = this;
                                pc2 = this;
                                ac = eAction.CastSpell;
                                break;
                            case eSpellTarget.CHARACTER: case eSpellTarget.LOCATION:
                                ac = eAction.ItemSpellTargeting;
                                break;
                            }
                            //Action.PC = this;

                            new Action(ac) { Spell = MagicSpell.List[item.SpellID], Item = item, PC = this, PC2 = pc2 };
                        }
                        break;

                    //// spell effects
                    //case eItemAbil.SPELL_FLAME:
                    //    Game.AddMessage("  It fires a bolt of flame.");
                    //    start_spell_targeting(1011);
                    //    break;
                    //case eItemAbil.SPELL_FIREBALL:
                    //    Game.AddMessage("  It shoots a fireball.         ");
                    //    start_spell_targeting(1022);
                    //    break;
                    //case eItemAbil.SPELL_FIRESTORM:
                    //    Game.AddMessage("  It shoots a huge fireball. ");
                    //    start_spell_targeting(1040);
                    //    break;
                    //case eItemAbil.SPELL_KILL:
                    //    Game.AddMessage("  It shoots a black ray.  ");
                    //    start_spell_targeting(1048);
                    //    break;
                    //case eItemAbil.SPELL_ICE_BOLT:
                    //    Game.AddMessage("  It fires a ball of ice.   ");
                    //    start_spell_targeting(1031);
                    //    break;
                    //case eItemAbil.SPELL_SLOW:
                    //    Game.AddMessage("  It fires a purple ray.   ");
                    //    start_spell_targeting(1012);
                    //    break;
                    //case eItemAbil.SPELL_SHOCKWAVE:
                    //    Game.AddMessage("  The ground shakes!        ");
                    //    do_shockwave(pc_pos[current_pc]);
                    //    break;
                    //case eItemAbil.SPELL_DISPEL_UNDEAD:
                    //    Game.AddMessage("  It shoots a white ray.   ");
                    //    start_spell_targeting(1132);
                    //    break;
                    //case eItemAbil.SPELL_RAVAGE_SPIRIT:
                    //    Game.AddMessage("  It shoots a golden ray.   ");
                    //    start_spell_targeting(1155);
                    //    break;
                    //case eItemAbil.SPELL_SUMMONING:
                    //    if (summon_monster(str,user_loc,50,2) == false)
                    //        Game.AddMessage("  Summon failed.");
                    //    break;
                    //case eItemAbil.SPELL_MASS_SUMMONING:
                    //    r1 = get_ran(6,1,4);
                    //    j = get_ran(1,3,5);
                    //    for (i = 0; i < j; i++)
                    //        if (summon_monster(str,user_loc,r1,2) == false)
                    //            Game.AddMessage("  Summon failed.");
                    //    break;
                    //case eItemAbil.SPELL_ACID_SPRAY:
                    //    Game.AddMessage("  Acid sprays from the tip!   ");
                    //    start_spell_targeting(1068);
                    //    break;
                    //case eItemAbil.SPELL_STINKING_CLOUD:
                    //    Game.AddMessage("  It creates a cloud of gas.   ");
                    //    start_spell_targeting(1066);
                    //    break;
                    //case eItemAbil.SPELL_SLEEP_FIELD:
                    //    Game.AddMessage("  It creates a shimmering cloud.   ");
                    //    start_spell_targeting(1019);
                    //    break;
                    //case eItemAbil.SPELL_VENOM:
                    //    Game.AddMessage("  A green ray emerges.        ");
                    //    start_spell_targeting(1030);
                    //    break;
                    //case eItemAbil.SPELL_SHOCKSTORM:
                    //    Game.AddMessage("  Sparks fly.");
                    //    start_spell_targeting(1044);
                    //    break;
                    //case eItemAbil.SPELL_PARALYSIS:
                    //    Game.AddMessage("  It shoots a silvery beam.   ");
                    //    start_spell_targeting(1069);
                    //    break;
                    //case eItemAbil.SPELL_WEB_SPELL:
                    //    Game.AddMessage("  It explodes!");
                    //    start_spell_targeting(1065);
                    //    break;
                    //case eItemAbil.SPELL_STRENGTHEN_TARGET:
                    //    Game.AddMessage("  It shoots a fiery red ray.   ");
                    //    start_spell_targeting(1062);
                    //    break;
                    //case eItemAbil.SPELL_QUICKFIRE:
                    //    Game.AddMessage("Fire pours out!");
                    //    make_quickfire(user_loc.x,user_loc.y);
                    //    break;
                    //case eItemAbil.SPELL_MASS_CHARM:
                    //    Game.AddMessage("It throbs, and emits odd rays.");
                    //    for (i = 0; i < T_M; i++) {
                    //            if ((c_town.monst.dudes[i].active != 0) && (c_town.monst.dudes[i].attitude % 2 == 1)
                    //             && (dist(pc_pos[current_pc],c_town.monst.dudes[i].m_loc) <= 8)
                    //             && (can_see(pc_pos[current_pc],c_town.monst.dudes[i].m_loc,0) < 5))
                    //                {
                    //                    c_town.monst.dudes[i].charm(0,0,8);
                    //                }
                    //            }
                    //    break;
                    //case eItemAbil.SPELL_MAGIC_MAP:
                    //    if ((c_town.town.defy_scrying == 1) && (c_town.town.defy_mapping == 1)) {
                    //        Game.AddMessage("  It doesn't work.");
                    //        break;
                    //        }
                    //    Game.AddMessage("  You have a vision.            ");
                    //    for (i = 0; i < town_size[town_type]; i++)
                    //        for (j = 0; j < town_size[town_type]; j++)
                    //            make_explored(i,j);
                    //    clear_map();
                    //    break;
                    //case eItemAbil.SPELL_DISPEL_BARRIER:
                    //    Game.AddMessage("  It fires a blinding ray.");
                    //    Game.AddMessage("  Target spell.    ");
                    //    overall_mode = MODE_TOWN_TARGET;
                    //    current_pat = s;
                    //    set_town_spell(1041,current_pc);
                    //break;
                    //case eItemAbil.SPELL_MAKE_ICE_WALL:
                    //    Game.AddMessage("  It shoots a blue sphere.   ");
                    //    start_spell_targeting(1064);
                    //    break;
                    //case eItemAbil.SPELL_CHARM_SPELL:
                    //    Game.AddMessage("  It fires a lovely, sparkling beam.");
                    //    start_spell_targeting(1117);
                    //    break;
                    //case eItemAbil.SPELL_ANTIMAGIC_CLOUD:
                    //    Game.AddMessage("  Your hair stands on end.   ");
                    //    start_spell_targeting(1051);
                    //    break;
			        }
        // Special spells:
        //   62 - Carrunos
        //	 63 - Summon Rat <= doesn't exist anymore
        //	 64 - Ice Wall Balls
        //	 65 - Goo Bomb
        //   66 - Foul Vapors
        //   67 - Sleep cloud <= doesn't exist anymore
        //	 68 - Spray Acid
        //	 69 - Paralyze
        //   70 - mass sleep <= doesn't exist anymore
		        }

	        //put_pc_screen();
            if (take_charge && item.Charges > 0) UseItemCharge(item);
        }


        //public void Equip(Item i) {
        //    equip.Add(i);
        //}

        //public void Unequip(Item i) {
        //    equip.Remove(i);
        //}

        /// <summary>
        /// Returns whether the PC is suitably equipped to fire a ranged weapon.
        /// </summary>
        /// <returns></returns>
        public bool CanFire()
        {
            Item ranged = GetEquipped(eEquipSlot.Ranged);
            Item ammo = GetEquipped(eEquipSlot.Ammo);

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
            Item i = GetEquipped(eEquipSlot.Ranged);
            if (i == null) return false;
            return i.Variety == eVariety.Bow || i.Variety == eVariety.Crossbow || i.Variety == eVariety.RangedNoAmmo;
        }

        public bool InventorysClose(IInventory other) {
            if (pos.adjacent(other.Pos) || other is Shop) return true;
            return false;
        }

        public eEquipSlot HasEquipped(Item item)
        { //return item != null && EquippedItems.Contains(item); }
            if (item != null) 
                for (int n = 0; n < EquippedItemSlots.Length; n++)
                    if (item == EquippedItemSlots[n]) return (eEquipSlot)n;
            return eEquipSlot.None;
        }

        public Item HasItemEquippedWithAbility(eItemAbil abil) { return EquippedItemSlots.ToList<Item>().Find(n => n != null && n.Ability == abil); }
        public Item HasItemWithAbility(eItemAbil abil) 
        {
            Item i = ItemList.Find(n => n.Ability == abil);
            if (i != null) return i;
            return HasItemEquippedWithAbility(abil);
        }

        public bool IsAlive() {return LifeStatus == eLifeStatus.ALIVE;}
        public bool IsGone() { return LifeStatus == eLifeStatus.ABSENT || LifeStatus == eLifeStatus.FLED || LifeStatus == eLifeStatus.SURFACE || LifeStatus == eLifeStatus.WON; }

        public XnaRect GetGraphicRect(bool forcerightwards = false)
        {

            return new XnaRect(direction.IsFacingRight || forcerightwards ? 0 : Gfx.CHARGFXWIDTH, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
        }

        public void Draw(SpriteBatch sb, XnaRect dr, Color col)
        {
            if (NotDrawn) return;

            float rot = 0;
            if (animAction != null) 
                animAction.AdjustCharRect(ref dr, ref rot, ref col);
            if (animFlash != null)
                animFlash.AdjustCharRect(ref dr, ref rot, ref col);

            if (this == Party.ActivePC && Game.Turn == eTurn.PLAYER && Game.Mode == eMode.COMBAT)//Animation.OnlyMovingAnimationsRunning() && (Game.Turn == Game.eTurn.PLAYER || Game.Mode != eMode.COMBAT))
            {
                XnaRect bigdr = dr;
                dr.Offset(dr.Width / 2, dr.Height / 2);
                bigdr.Inflate(Gfx.HIGHLIGHT_SIZE, Gfx.HIGHLIGHT_SIZE);
                bigdr.Offset(bigdr.Width / 2, bigdr.Height / 2);
                sb.Draw(animAction is Animation_Attack ? Gfx.PCCombatHighlightGfx : Gfx.PCHighlightGfx,
                    bigdr, Gfx.PCHighlightGfx.Bounds, col, rot, new Vector2(Gfx.PCHighlightGfx.Width / 2, Gfx.PCHighlightGfx.Height / 2),
                    direction.IsFacingRight ? SpriteEffects.None : SpriteEffects.FlipHorizontally, 0);
            }
            else
            {
                dr.Offset(dr.Width / 2, dr.Height / 2);
                XnaRect sr = GetGraphicRect();
                if (animAction is Animation_Attack) sr.X += Gfx.CHARGFXWIDTH * 2;
                sb.Draw(PCTexture, dr, sr, col, rot, new Vector2(Gfx.CHARGFXWIDTH / 2, Gfx.CHARGFXHEIGHT / 2), SpriteEffects.None, 0);
            }

            if (Game.Mode == eMode.COMBAT && Gfx.DrawHealthBars & !Dying)
            {
                XnaRect br = new XnaRect(134, 181, 20, 6);

                //Health
                float h = (float)Health / (float)MaxHealth;
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
            List<Item> weapons = new List<Item>();
            Item skill_item;
            int hit_adj, dam_adj;

            // slice out bad attacks
            if (!IsAlive()) return false;
            if (Status(eAffliction.ASLEEP) > 0 || Status(eAffliction.PARALYZED) > 0) return false;

            if (!(target is NPC)) return false; //PCs attacking other PCs not something in BoE or needs implementing yet.
            NPC which_m = (NPC)target;

            direction.FaceTowards(pos, target.Pos); //Face who you're attacking.

            LastAttacked = which_m;
            Provocation += Constants.AI_ATTACK_PROVOCATION_SCORE + 1; //Add provocation score (+1 because 1 automatically gets taken off at the end of every turn)

            Item w1 = GetEquipped(eEquipSlot.MainHand);
            Item w2 = GetEquipped(eEquipSlot.OffHand);
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

            int store_hp = which_m.Health;
            bool second_attack = false;

            foreach (Item weapon in weapons)
            {
                if (!target.IsAlive()) break;

                eSkill what_skill = weapon == null ? eSkill.DEXTERITY : weapon.MeleeTypeToSkill();

                if (weapon == null)
                {
                    Game.AddMessage(name + " punches.  ");

                    int r1 = Maths.Rand(1, 0, 100) + hit_adj - 20;
                    r1 += 5 * (status[6] / 3);
                    int r2 = Maths.Rand(1, 1, 4) + dam_adj;

                    if (r1 <= hitChance[GetSkill(what_skill)])
                    {
                        var aa = new Animation_Attack(this);
                        if (!which_m.Damage(this, r2, 0, eDamageType.WEAPON, eDamageType.WEAPON, "072_club"))
                            aa.SetSound("002_swordswish");
                    }
                    else
                    {
                        new Animation_Attack(this, "002_swordswish");
                        //GameScreen.draw_terrain(2);
                        Game.AddMessage(name + " misses. ");
                    }
                }
                else
                {
                    Game.AddMessage(name + " swings.");
                    int r1 = Maths.Rand(1, 0, 100) - (second_attack ? 5 : 0) + hit_adj - 5 * weapon.Bonus;
                    r1 += 5 * (Status(eAffliction.WEBS) / 3);

                    if (weapons.Count > 1 && !HasTrait(Trait.Ambidextrous)) r1 += 25;

                    // race adj.
                    if (HasTrait(Trait.Slitherzakai) && weapon.MeleeType == eMeleeWeaponType.POLE) r1 -= 10;

                    int r2 = Maths.Rand(1, 1, weapon.Level) + dam_adj + (second_attack ? -1 : 2) + weapon.Bonus;

                    if (weapon.Ability == eItemAbil.WEAK_WEAPON) r2 = (r2 * (10 - weapon.AbilityStrength)) / 10;

                    if (r1 <= hitChance[GetSkill(what_skill)])
                    {
                        var aa = new Animation_Attack(this);
                        bool does_damage = false;

                        eDamageType spec_dam_type;
                        int spec_dam = weapon.GetSpecialDamage(which_m.Record.Genus, out spec_dam_type);

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
                                int poison_amt = status[0];
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
                        Game.AddMessage("  " + name + " misses.              ");
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

            bool firing = HasRanged(); //If true, PC is firing (bow/crossbow/sling) - if false, PC is throwing (Javelins or whatnot)
            Item ammo = GetEquipped(eEquipSlot.Ammo);
            Item rangedwp = GetEquipped(eEquipSlot.Ranged);
            bool no_ammo = rangedwp.Variety == eVariety.RangedNoAmmo; //Only applies to an ammo-less ranged weapon (like a sling)

            int skill = firing ? GetSkill(eSkill.ARCHERY) : GetSkill(eSkill.THROWN_MISSILES);
            int range = firing ? Constants.PC_FIRING_RANGE : Constants.PC_THROWING_RANGE;

            //The hitting item is the actual missile that does the damage, not the item that fires it except in the case of a ranged weapon that uses no ammo (eg, sling)
            Item hitting_item = (firing && !no_ammo) ? ammo : rangedwp;

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
            bool exploding = hitting_item.Ability == eItemAbil.MISSILE_EXPLODING;

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
                int r1 = Maths.Rand(1, 0, 100) - 5 * hit_bonus - 10;
                r1 += 5 * (Status(eAffliction.WEBS) / 3);

                if (Game.PCsAlwaysHit) r1 -= 1000;

                int r2 = Maths.Rand(1, 1, dam) + dam_bonus;
                Game.AddMessage(Name + " fires.");

                int m_type = 10;
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
                        eDamageType spec_dam_type = eDamageType.WEAPON;
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

                //if (ammo != null && (rangedwp == null || (rangedwp != null && rangedwp.Variety != eVariety.RangedNoAmmo)))
                //{
                //    if (ammo.Ability != eItemAbil.MISSILE_RETURNING)
                //        ammo.Charges--;
                //    else
                //        ammo.Charges = 1;

                //    if (HasItemEquippedWithAbility(eItemAbil.DRAIN_MISSILES) != null && ammo.Ability != eItemAbil.MISSILE_RETURNING)
                //        ammo.Charges--;

                //    if (ammo.Charges <= 0)
                //        Unequip(ammo, true);
                //}
            }

            if (!exploding) CounteractStatus(eAffliction.POISONED_WEAPON);
            return true;
        }

        public bool Damage(IExpRecipient attacker, int how_much, int how_much_spec, eDamageType dam_type, eDamageType spec_dam_type = eDamageType.WEAPON, string sound_type = null)
        {
            int level;
            if (!IsAlive()) return false;

            eGenus type_of_attacker = attacker is NPC ? ((NPC)attacker).Record.Genus : eGenus.HUMAN;

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
            if (dam_type == eDamageType.WEAPON || dam_type == eDamageType.UNDEAD || dam_type == eDamageType.DEMON)
            {
                how_much -= Maths.MinMax(-5, 5, Status(eAffliction.BLESS_CURSE));
                foreach (Item item in EachEquippedItem())// (i = 0; i < 24; i++)
                //if ((items[i].Variety != 0) && (equip[i] == true))
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

            //if (Party.vogelsExtraShit[6, 7] > 0) //EASY MODE
            //    how_much -= 3;
            // toughness
            if (HasTrait(Trait.Tough))
                how_much--;
            // luck
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
            if ((dam_type == eDamageType.FIRE || dam_type == eDamageType.COLD) &&
                Status(eAffliction.MAGIC_RESISTANCE) > 0)
                how_much = how_much / 2;

            // fire res.
            if (dam_type == eDamageType.FIRE && (level = get_prot_level(eItemAbil.FIRE_PROTECTION)) > 0)
                how_much = how_much / (level >= 7 ? 4 : 2);

            // cold res.
            if (dam_type == eDamageType.COLD && (level = get_prot_level(eItemAbil.COLD_PROTECTION)) > 0)
                how_much = how_much / (level >= 7 ? 4 : 2);

            // major resistance
            if ((dam_type == eDamageType.FIRE || dam_type == eDamageType.POISON || dam_type == eDamageType.MAGIC || dam_type == eDamageType.COLD)
             && (level = get_prot_level(eItemAbil.FULL_PROTECTION)) > 0)
                how_much = how_much / ((level >= 7) ? 4 : 2);

            //if (BoE.boom_anim_active == true)
            //{
            //    if (how_much < 0)
            //        how_much = 0;
            //    MarkedDamage += how_much;
            //    if (BoE.is_town())
            //        new store_boom_type(BoE.Party.Pos, how_much, 0, (damage_type > eDamageType.POISON) ? 2 : 0, 0, 0);
            //    else
            //        new store_boom_type(Pos, how_much, 0, (damage_type > eDamageType.POISON) ? 2 : 0, 0, 0);
            //    if (how_much == 0)
            //        return false;
            //    else return true;
            //}

            if (Game.Invincible) how_much = 0;

            if (how_much <= 0)
            {
                //if (dam_type == eDamageType.WEAPON || dam_type == eDamageType.UNDEAD || dam_type == eDamageType.DEMON)  
                //    Sound.Play(2);
                Game.AddMessage("  No damage.");
                return false;
            }
            //else
            //{
                // if asleep, get bonus
            if (Status(eAffliction.ASLEEP) > 0)
                DecStatus(eAffliction.ASLEEP, 1, 0);// status[11]--;

            //sprintf((char*)c_line, "  %s takes %d. ", (char*)name, how_much);
            //if (do_print)
            Game.AddMessage(String.Format("  {0} takes {1}. ", name, how_much));
            //if (dam_type != eDamageType.WEAPON_MARKED)
            //{
            //    if (BoE.is_combat())
            //        Gfx.boom_space(Pos, Gfx.boom_gr[(int)damage_type], how_much, sound_type);
            //    else if (BoE.is_town())
            //        Gfx.boom_space(Party.Pos, Gfx.boom_gr[(int)damage_type], how_much, sound_type);
            //    else Gfx.boom_space(Party.Pos, Gfx.boom_gr[(int)damage_type], how_much, sound_type);
            //}
            //if (BoE.overall_mode != 0) 
            //FlushEvents(1);
            //FlushEvents(0);

            
            //}
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
                    //sprintf((char*)c_line, "  %s is obliterated.  ", (char*)name);
                    Game.AddMessage(String.Format("  {0} is obliterated.  ", name));
                    Kill(attacker, eLifeStatus.DUST);
                }
                else
                {
                    Game.AddMessage(String.Format("  {0} is killed.  ", name));
                    //add_string_to_buf((char*)c_line);
                    Kill(attacker, eLifeStatus.DEAD);
                }
            //if (cur_health == 0 && IsAlive())
            //    Sound.Play(3);

            return true;
        }

        public Boolean RunTrap(eTrapType trap_type, int trap_level, int diff)
        //short pc_num; // 6 - BOOM!  7 - pick here
        //short trap_type; // 0 - random  1 - blade  2 - dart  3 - gas  4 - boom  5,6  - no   
        // 7 - level drain  8 - alert  9 - big flames 10 - dumbfound 11 - town hostile
        //	20 + *  - trap *, but nasty 
        {
            //int r1, skill, i, i_level;
            short[] trap_odds = {5,30,35,42,48, 55,63,69,75,77,
							        78,80,82,84,86, 88,90,92,94,96,98,99,99,99,99,99,99,99,99,99};

            //if (pc_num == 7) {
            //    pc_num = select_pc(1,0);
            //    if (pc_num == 6)
            //        return FALSE;
            //    }

            int num_hits = 1 + trap_level;

            if (trap_type == eTrapType.RANDOM)
                trap_type = (eTrapType)Maths.Rand(1, 1, 4);
            if (trap_type == eTrapType.FALSE_ALARM)
                return true;

            //if (pc_num < 6) {
            int i = GetSkillBonus(eSkill.DEXTERITY);
            int i_level = get_prot_level(eItemAbil.THIEVING);
            if (i_level > 0) i = i + i_level / 2;
            int skill = Maths.MinMax(0, 20, GetSkill(eSkill.DISARM_TRAPS) +
                + GetSkill(eSkill.LUCK) / 2 + 1 - curTown.Difficulty + 2 * i);

            int r1 = Maths.Rand(1, 0, 100) + diff;
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
                foreach (PCType pc in Party.EachAlivePC())
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
                foreach (PCType pc in Party.EachAlivePC())
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
                foreach (PCType pc in Party.EachAlivePC())
                    pc.Disease(r1);
                break;
            }
            return true;
        }

        public void ForceWallMe(IExpRecipient perp) 
        { 
            //if (Game.Mode == eMode.COMBAT)
                Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.MAGIC); 
            //else
            //    foreach (PCType pc in Party.EachAlivePC()) 
            //        pc.Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.MAGIC);
        }
        public void FireWallMe(IExpRecipient perp) 
        {
            //if (Game.Mode == eMode.COMBAT)
                Damage(perp, Maths.Rand(1, 1, 6) + 1, 0, eDamageType.FIRE);
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Damage(perp, Maths.Rand(1, 1, 6) + 1, 0, eDamageType.FIRE);
 
        }
        public void IceWallMe(IExpRecipient perp) 
        {
            //if (Game.Mode == eMode.COMBAT)
                Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.COLD); 
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.COLD);    
        }
        public void BladeWallMe(IExpRecipient perp) 
        {
            //if (Game.Mode == eMode.COMBAT)
                Damage(perp, Maths.Rand(4, 1, 8), 0, eDamageType.WEAPON); 
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Damage(perp, Maths.Rand(4, 1, 8), 0, eDamageType.WEAPON); 
        }
        public void StinkCloudMe() 
        {
            //if (Game.Mode == eMode.COMBAT)
                Curse(Maths.Rand(1, 1, 2)); 
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Curse(Maths.Rand(1, 1, 2)); 
        }
        public void SleepCloudMe() 
        {
            //if (Game.Mode == eMode.COMBAT)
                Sleep(3, 0);
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Sleep(3, 0);
        }
        public void QuickfireMe()
        {
            //if (Game.Mode == eMode.COMBAT)
                Damage(null, Maths.Rand(2, 1, 8), 0, eDamageType.FIRE);
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Damage(null, Maths.Rand(2, 1, 8), 0, eDamageType.FIRE);
        }
        public void FireBarrierMe()
        {
            //if (Game.Mode == eMode.COMBAT)
                Damage(null, Maths.Rand(2, 1, 10), 0, eDamageType.MAGIC);
            //else
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Damage(null, Maths.Rand(2, 1, 10), 0, eDamageType.MAGIC, false);
        }
        public void WebSpaceMe()
        {
            //if (Game.Mode == eMode.COMBAT)
                Web(Maths.Rand(1, 2, 3));
            //else foreach (PCType pc in Party.EachAlivePC())
            //{
            //    pc.Web(Maths.Rand(1, 2, 3));
            //}
        }


        public bool Kill(IExpRecipient who_killed, eLifeStatus type, bool no_save = false)
        {
            Item i = null;

            //if (type >= 10)
            //{
            //    type -= 10;
            //    no_save = true;
            //}

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
                //We failed to save the PC from death.
                //if (BoE.combat_active_pc == this)
                //    BoE.combat_active_pc = null;

                //for (i = 0; i < 24; i++)
                //    adven[which_pc].equip[i] = FALSE;

                //foreach (Item item in EachEquippedItem())
                //{
                //    Unequip(item);
                //    AddItem(item, true);
                //}
                //equip.Clear();

                if (Game.Mode != eMode.OUTSIDE)
                {
                    Location item_loc = Pos;//(BoE.overall_mode >= 10) ? Pos : Party.Pos;
                    if (type == eLifeStatus.DEAD)
                        curTown.MakeBloodStain(item_loc);
                    else if (type == eLifeStatus.DUST)
                        curTown.MakeCrater(item_loc);

                    //for (int x = ItemList.Count - 1; x >= 0; x--)// (i = 0; i < 24; i++)
                    //{
                    //    curTown.PlaceItem(ItemList[x], item_loc);//, true);
                    //    ItemList.RemoveAt(x);
                    //}
                }
                if (type == eLifeStatus.DEAD || type == eLifeStatus.DUST)
                {
                    new Animation_Hold();
                    new Animation_Death(this);
                    Dying = true;
                    //if (Party.IsSplit)
                    //{
                    //    Party.Reunite();
                    //    if (Game.Mode == eMode.COMBAT) Game.EndCombat(true);
                    //}
                }
                for (int a = 0; a < status.Length; a++) status[a] = 0;
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

        //public void take_ap(int amount) {
        //    AP -= amount;
        //    if (AP < 0) AP = 0;
        //}

        //public Boolean take_sp(int amt)
        //{
        //    if (cur_sp < amt)
        //        return false;
        //    cur_sp -= amt;
        //    return true;
        //}

        //public void restore_sp_pc(int amt)
        //{
        //    if (cur_sp > max_sp)
        //        return;
        //    cur_sp += amt;
        //    if (cur_sp > max_sp)
        //        cur_sp = max_sp;
        //}

        //public void heal_pc(int amt) //Deprecated - use Health property
        //{
        //    if (cur_health > max_health || IsAlive() == false) return;
        //    cur_health += amt;
        //    if (cur_health > max_health) cur_health = max_health;
        //}

        //public void drain_pc(int how_much)
        //{
        //    if (!IsAlive()) return;           
        //    experience = Math.Max(experience - how_much, 0);
        //    Game.AddMessage("  " + name + " drained.");
        //}

        public bool PoisonWeapon(int how_much, bool always_succeeds = true)
        //short safe; // 1 - always succeeds
        {
            short[] p_chance = {40,72,81,85,88,89,90,
							    91,92,93,94,94,95,95,96,97,98,100,100,100,100};

            foreach (Item item in EquippedItemSlots)
                if (item != null && item.IsWeapon())
                {
                    int p_level = how_much;
                    Game.AddMessage(String.Format("  {0} poisons weapon.", Name));
                    int r1 = Maths.Rand(1, 0, 100);
                    // Nimble?
                    if (HasTrait(Trait.Nimble)) r1 -= 6;
                    if (r1 > p_chance[GetSkill(eSkill.POISON)] && !always_succeeds)
                    {
                        Game.AddMessage("  Poison put on badly.         ");
                        p_level /= 2;
                        if (Maths.Rand(1, 0, 100) > p_chance[GetSkill(eSkill.POISON)] + 10)
                        {
                            Game.AddMessage(String.Format("  {0} accidentally poisoned!", Name));
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
            int _level = 0;

            if (IsAlive())
            {
                if ((_level = get_prot_level(eItemAbil.POISON_PROTECTION)) > 0)////
                    how_much -= Level / 2;
                if ((_level = get_prot_level(eItemAbil.FULL_PROTECTION)) > 0)////
                    how_much -= _level / 3;
                if (HasTrait(Trait.Frail) && how_much > 1)
                    how_much++;
                if (HasTrait(Trait.Frail) && how_much == 1 && Maths.Rand(1, 0, 1) == 0)
                    how_much++;

                if (how_much > 0)
                {
                    status[2] = Math.Min(status[2] + how_much, 8);
                    if (!silent) Game.AddMessage("  " + name + " poisoned.");
                    //if (!silent) Sound.one_sound(17);

                    new Animation_CharFlash(this, Color.LimeGreen, "017_shortcough");

                    //Game.give_help(33, 0);
                }
            }
        }

        public void Heal(int amt, bool silent = false)
        {
            int realamt = Health;
            Health += amt;
            realamt = Health - realamt;
            if (!silent)
            {
                if (realamt > 0)
                {
                    Game.AddMessage(String.Format("  {0} healed {1}", Name, realamt));
                    new Animation_CharFlash(this, Color.FloralWhite, "052_magic2");
                }
                else if (realamt < 0)
                {
                    Game.AddMessage(String.Format("  {0} harmed {1}", Name, -realamt));
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
            //Sound.one_sound(51);
            new Animation_CharFlash(this, Color.LemonChiffon, "051_magic1");
        }

        public void Curse(int how_much, bool silent = false)
        {
            if (!IsAlive()) return;
            status[1] = Math.Max(status[1] - how_much, -8);
            if (!silent)
                Game.AddMessage("  " + name + " cursed.");
            new Animation_CharFlash(this, Color.Black, "043_stoning");

            //Game.give_help(59, 0);
        }
        public void Bless(int how_much, bool silent = false)
        {
            if (!IsAlive()) return;
            IncStatus(eAffliction.BLESS_CURSE, how_much, 8);

            if (!silent)
                Game.AddMessage("  " + name + " blessed.");

            new Animation_CharFlash(this, Color.Gold, "004_bless");
            //Game.give_help(59, 0);
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
                Game.AddMessage("  " + name + " saved.");
                return;
            }
            status[9] = Math.Min(status[9] + how_much, 8);
            if (!silent) Game.AddMessage("  " + name + " dumbfounded.");
            //if (!silent) Sound.one_sound(67);
            new Animation_CharFlash(this, Color.DarkSlateBlue, "067_huh");
            //adjust_spell_menus(); TODO
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
                Game.AddMessage("  " + name + " saved.");
                return;
            }
            if ((_level = get_prot_level(eItemAbil.PROTECT_FROM_DISEASE)) > 0)////
                how_much -= _level / 2;
            if (HasTrait(Trait.Frail) && how_much > 1)
                how_much++;
            if (HasTrait(Trait.Frail) && how_much == 1 && Maths.Rand(1, 0, 1) == 0)
                how_much++;
            SetStatus(eAffliction.DISEASE, Math.Min(Status(eAffliction.DISEASE) + how_much, 8));
            if (!silent) Game.AddMessage("  " + name + " diseased.");

            //if (!silent) Sound.one_sound(66);
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
                Game.AddMessage("  " + name + " resisted.");
                return;
            }

            IncStatus(eAffliction.ASLEEP, how_much, 8);
            Game.AddMessage("  " + name + " falls asleep.");
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
                Game.AddMessage("  " + name + " resisted.");
                return;
            }
            IncStatus(eAffliction.PARALYZED, how_much, 5000);
            Game.AddMessage("  " + name + " paralyzed.");
            new Animation_CharFlash(this, Color.Olive, "090_paralyze");

            AP = 0;

            Game.give_help(32, 0);
        }

        //public void Charm(int how_much, eAffliction what_type, int adjust) //Used to be Sleep but changed to tie in with NPCs
        //// higher adjust, less chance of saving
        //{
        //    int r1, _level;
        //    if (!IsAlive()) return;
        //    if (how_much == 0)
        //        return;
        //    if (what_type != eAffliction.ASLEEP && what_type != eAffliction.PARALYZED) return;

        //    if ((_level = get_prot_level(eItemAbil.WILL)) > 0)
        //        how_much -= _level / 2;
        //    if ((_level = get_prot_level(eItemAbil.FREE_ACTION)) > 0)
        //        how_much -= (what_type == eAffliction.ASLEEP) ? _level : _level * 300;

        //    r1 = Maths.Rand(1, 0, 100) + adjust;
        //    if (r1 < 30 + Level * 2)
        //        how_much = -1;
        //    if (what_type == eAffliction.ASLEEP && (HasTrait(Trait.Alert) || Status(eAffliction.ASLEEP) < 0))
        //        how_much = -1;
        //    if (how_much <= 0)
        //    {
        //        Game.AddMessage("  " + name + " resisted.");
        //        return;
        //    }

        //    SetStatus(what_type, how_much);

        //    if (what_type == eAffliction.ASLEEP)
        //    {
        //        Game.AddMessage("  " + name + " falls asleep.");
        //        new Animation_CharFlash(this, Color.MidnightBlue, "096_sleep");
        //    }
        //    else
        //    {
        //        Game.AddMessage("  " + name + " paralyzed.");
        //        new Animation_CharFlash(this, Color.Olive, "090_paralyze");
        //    }

        //    AP = 0;

        //    if (what_type == eAffliction.ASLEEP)
        //        Game.give_help(30, 0);
        //    else
        //        Game.give_help(32, 0);
        //}

        public void Slow(int how_much, bool silent = false)
        {
            if (!IsAlive()) return;

            status[3] = Maths.MinMax(-8, 8, status[3] - how_much);

            if (how_much < 0)
            {
                if (!silent) Game.AddMessage("  " + name + " hasted.");
                new Animation_CharFlash(this, Color.Orange, "075_cold");
            }
            else
            {
                if (!silent) Game.AddMessage("  " + name + " slowed.");
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
                if (!silent) Game.AddMessage("  " + name + " hasted.");
                new Animation_CharFlash(this, Color.Orange, "075_cold");
            }

        }

        public void DrainXP(int how_much, bool silent = false)
        {
            experience = Maths.Max(experience - how_much, 0);
            if (!silent) Game.AddMessage("  " + name + " drained.");
            new Animation_CharFlash(this, Color.SlateGray, "065_draining");
        }

        public void Web(int how_much, bool silent = false)
        {
            if (!IsAlive()) return;

            status[6] = Math.Min(status[6] + how_much, 8);
            if (!silent) Game.AddMessage("  " + name + " webbed.");
            //if (!silent) Sound.one_sound(17);
            new Animation_CharFlash(this, Color.Gray, "017_shortcough");
            Game.give_help(31, 0);
        }

        public void Acid(int how_much, bool silent = false)
        {
            if (!IsAlive()) return;
            if (HasItemEquippedWithAbility(eItemAbil.ACID_PROTECTION) != null)
            {
                if (!silent) Game.AddMessage("  " + name + " resists acid.");
                return;
            }
            SetStatus(eAffliction.ACID, Maths.Min(8,Status(eAffliction.ACID) + how_much));// += how_much;
            if (!silent) Game.AddMessage("  " + name + " covered with acid!");
            //if (!silent) Sound.one_sound(42);
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
                Game.AddMessage("  " + name + " drained.");
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
            { // debug
                //Snd.SysBeep(50); Snd.SysBeep(50);
                //MessageFeed.add_string_to_buf("Oops! Too much xp!");
                //MessageFeed.add_string_to_buf("Report this!");
                return;
            }
            if (amount < 0)
            { // debug
                //Snd.SysBeep(50); Snd.SysBeep(50);
                //MessageFeed.add_string_to_buf("Oops! Negative xp!");
                //MessageFeed.add_string_to_buf("Report this!");
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
                //Snd.SysBeep(50); Snd.SysBeep(50);
                //MessageFeed.add_string_to_buf("Oops! Xp became negative somehow!");
                //MessageFeed.add_string_to_buf("Report this!");
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
                Game.AddMessage(String.Format("  {0} is level {1}!  ", name, Level));
                skill_pts += (Level < 20) ? 5 : 4;
                add_hp = (Level < 26) ? Maths.Rand(1, 2, 6) + skill_bonus[skills[0]]
                   : Math.Max((int)skill_bonus[skills[0]], 0);
                if (add_hp < 0)
                    add_hp = 0;
                max_health += add_hp;
                if (MaxHealth > 250)
                    max_health = 250;
                cur_health += add_hp;
                if (cur_health > 250)
                    cur_health = 250;
            }

        }

        //Get experience To Next Level
        public int GetExperienceModifier()
        {
            int tnl = 100, store_per = 100;

            foreach (Trait t in Traits)
            {
                if (t.Race)
                {
                    tnl = (tnl * (100 + t.Handicap)) / 100;
                    break; //Only one race counts
                }
            }

            foreach (Trait t in Traits)
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
                name = "NOBODY";
            }
            else
            {
                LifeStatus = eLifeStatus.ALIVE;
                SkillPoints = 60;
                Health = 6;
                SetSkill(eSkill.STRENGTH, 1);
                SetSkill(eSkill.DEXTERITY, 1);
                SetSkill(eSkill.INTELLIGENCE, 1);
                name = "Unnamed";
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
                foreach (string ms in knownspells)
                    KnownSpells.Add(ms, null);

                int race = slot == 1 ? 2 : (slot == 2 ? 1 : 0);
                Item item = Item.GetStartItem((int)race * 2);
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
            case 0: name = "Jenneke"; Portrait = 17;
                break;
            case 1: name = "Thissa"; Portrait = 52;
                break;
            case 2: name = "Frrrrrr"; Portrait = 44;
                break;
            case 3: name = "Adrianna"; Portrait = 14;
                break;
            case 4: name = "Feodoric"; Portrait = 3;
                break;
            case 5: name = "Michael"; Portrait = 6;
                break;
            }
            short[] pc_graphics = { 3, 32, 29, 16, 23, 14 };
            //[] pc_race = { 0, 2, 1, 0, 0, 0 };
            byte[,] pc_t = {{0,0,1,0,0,0,1,0,0,0, 0,1,0,0,0},		
						        {1,0,0,0,0,1,0,0,0,0, 1,0,0,0,0},	
						        {0,0,0,1,0,0,0,0,0,0, 0,0,1,0,0},	
						        {0,1,0,0,0,0,0,0,0,0, 0,0,0,0,0},	
						        {0,0,0,0,1,0,1,1,0,0, 0,0,0,0,1},	
						        {0,1,0,0,0,0,0,0,0,0, 0,0,0,0,0}};
            Slot = slotno;
            which_graphic = 0;
            PoisonedWeapon = null;// 24;
            Traits.Clear();
            for (int i = 0; i < 30; i++)
                skills[i] = (i < 3) ? 1 : 0;
            
            for (int i = 0; i < 15; i++)
                status[i] = 0;
            direction = new Direction();
            exp_adj = 100;
            skill_pts = 0;

            if (slotno == 1) Traits.Add(Trait.Slitherzakai);
            else if (slotno == 2) Traits.Add(Trait.Nephilim);
            else Traits.Add(Trait.Human);

            //race = (ePCRace)pc_race[slotno];
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

            foreach (string ms in knownspells)
            {
                KnownSpells.Add(ms, null);
            }

            for (int i = 0; i < 19; i++)
                skills[i] = pc_stats[slotno, i];
            cur_health = pc_health[slotno];
            max_health = pc_health[slotno];

            
            for (int i = 0; i < 15; i++) status[i] = 0;
            cur_sp = pc_sp[slotno];
            max_sp = pc_sp[slotno];

            for (int i = 0; i < 15; i++) {
                if (pc_t[slotno, i] == 1)
                    Traits.Add(Trait.Index[i]);
            }

            int race = HasTrait(Trait.Human) ? 0 : (HasTrait(Trait.Nephilim) ? 1 : 2);

            Item item = Item.GetStartItem((int)race * 2);
            Item dummy;
            Equip(item, eEquipSlot.None, out dummy);
            item = Item.GetStartItem((int)race * 2 + 1);
            Equip(item, eEquipSlot.None, out dummy);

            //SkillPoints = 10;

        }

        /// <summary>
        /// Called when a party is put into a scenario
        /// </summary>
        public void SetupKnownSpells()
        {

            for (int n = 0; n < KnownSpells.Count; n++)
            {
                //foreach (string s in KnownSpells.Keys)
                //{
                string s = KnownSpells.ElementAt(n).Key;
                //MagicSpell spell;
                //if ((spell = MagicSpell.Spells.Find(n => n.ID == s)) != null)
                //    KnownSpellList.Add(spell);

                if (MagicSpell.List.Contains(s)) KnownSpells[s] = MagicSpell.List[s];//.Add(MagicSpell.Spells[s]);

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
        //public static short[] spell_level = {1,1,1,1,1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2,2, 3,3,3,3,3,3,3,3,3,3,
        //                        4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5,5, 6,6,6,6,6,6,6,6, 7,7,7,7,7,7,7,7};
        //public static short[,] spell_cost = {{1,1,1,1,1,2,50,2,1,3, 2,3,2,2,2,2,4,4,2,6, 3,3,5,3,3,5,6,4,6,4,
        //                            4,5,4,8,30,-1,8,6, 5,8,8,6,9,10,6,6, 7,6,8,7,12,10,12,20, 12,8,20,10,14,10,50,10},
        //                            {1,1,1,2,1,1,3,5,50,1, 2,2,2,2,3,5,8,6,4,2, 3,4,3,3,3,10,5,3,4,6,
        //                             5,5,5,15,6,5,5,8, 6,7,25,8,10,12,12,6, 8,7,8,8,14,17,8,7, 10,10,35,10,12,12,30,10}};

        public void ResetCombatVars() {
            LastAttacked = null;//T_M + 10;
            Parry = 0;// pc_parry[i] = 0;
            //direction = Party.Direction;////pc_dir[i] = direction;

            Provocation = Math.Max(Provocation - 1, 0); //Provocation score automatically decays every turn

            //adven[current_pc].direction = direction;
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
                        Game.AddMessage(name + " must clean webs.");
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

        int get_prot_level(eItemAbil abil) {
            foreach (Item item in EachEquippedItem()) {
                if (item.Ability == abil) return item.AbilityStrength;
            }
            return -1;
        }

        public int EncumbranceRoll
        {
            get
            {
                int store = 0, what_val;

                foreach (Item item in EachEquippedItem())// (i = 0; i < 16; i++)
                //if (adven[pc_num].equip[i] == true)
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
                int store = 0;
                foreach (Item item in EachEquippedItem())
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
                //if (pc_has_abil_equip(99) < 16) //DUNNO WHAt THIS IS ABOUT
                //    tr++;
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

            TerrainRecord ter = curTown.TerrainAt(target);

            switch (ter.Special)
            { ////
            case eTerSpec.UNLOCKABLE_TERRAIN:
            case eTerSpec.UNLOCKABLE_BASHABLE:
                int r1 = Maths.Rand(1, 0, 100) - 5 * GetSkillBonus(eSkill.INTELLIGENCE) + 5 * curTown.Difficulty;
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

}
