using System;
using System.Text;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    public partial class Item : IListEntity
    {
        //A list of all the items in the game
        public static ExileList<Item> List = new ExileList<Item>();

        public string ID { get { return id; } set { id = value; } }
        string id;

        static int[] loot_min = { 0, 0, 5, 50, 400 }, loot_max = { 3, 8, 40, 800, 4000 };

        public eVariety Variety;
        public int Level;
        public int Awkward, Bonus, Protection, Charges, MagicUseType;
        public eMeleeWeaponType MeleeType;
        public int Picture, AbilityStrength, TypeFlag, IsSpecial, a;
        public eItemAbil Ability;
        public int BaseValue;

        public int Weight, SpecialClass;
        public Location Pos;
        public string Name, ShortName;
        public string KnownName { get { return Identified ? Name : ShortName; } }

        public int TreasureClass, //0 - Junk
            //1 - Lousy 1-20gp
            //2 - So-so 20-200gp
            //3 - Good  200+ gp
            //4 - Great 2500+ gp
            Properties;//, reserved1, reserved2;

        public string SpellID, //The ID of the magic spell this item will cast when it is used. Only used if Ability property is CAST_SPELL
                      AlchemyID; //To allow alchemical recipes to make use of this item as an ingredient

        public void DrawBigViewInfo(SpriteBatch sb, Vector2 d)
        {
            string s;
            if (NotYourProperty) 
            { 
                s = "Not Yours";
                sb.DrawString(Gfx.ItalicFont, s, d, Color.Magenta);
                d.X += Gfx.ItalicFont.MeasureString(s).Width + 8f;
            }
            if (!Identified)
            {
                s = "Unidentified";
                sb.DrawString(Gfx.ItalicFont, s, d, Color.Cyan);
            }
            else
            {
                if (Cursed)
                {
                    s = "Cursed";
                    sb.DrawString(Gfx.ItalicFont, s, d, Color.Red);
                    d.X += Gfx.ItalicFont.MeasureString(s).Width + 8f;
                }
                sb.DrawString(Gfx.ItalicFont, "Value: " + Value, d, Color.LightGray);
            }
        }

        public string TooltipInfo(bool brief = false) 
        {
            var s = new StringBuilder();

            if (brief)
            {
                s.Append(KnownName);
                if (Charges > 0) s.Append(" @4(" + Charges + ")");
                if (NotYourProperty) s.Append(" @i@3Not Yours@e");
                if (!Identified) s.Append(" @i@5Unidentified@e");
                if (Identified && Cursed) s.Append(" @i@2Cursed@e");
                s.Append("@7");
            }
            else
            {
                s.AppendFormat("@b{0}@e", KnownName);
                if (Charges > 0) s.Append(" @4(" + Charges + ")@7");
                if (NotYourProperty) s.Append(" @i@3Not Yours@7@e");
                if (!Identified) s.Append(" @i@5Unidentified@e");

                if (Identified && Cursed) s.Append(" @i@2 Cursed@e");

                switch (Variety)
                {
                    case eVariety.Armour: s.Append("@n   @9@iArmour");
                        break;
                    case eVariety.Arrows: s.Append("@n   @9@iAmmo for Bow");
                        break;
                    case eVariety.Bolts: s.Append("@n   @9@iAmmo for Crossbow");
                        break;
                    case eVariety.Boots: s.Append("@n   @9@iFootwear");
                        break;
                    case eVariety.Bow: s.Append("@n   @9@iRanged Weapon");
                        break;
                    case eVariety.Crossbow: s.Append("@n   @9@iRanged Weapon");
                        break;
                    case eVariety.Gloves: s.Append("@n   @9@iHandwear");
                        break;
                    case eVariety.Helm: s.Append("@n   @9@iHelm");
                        break;
                    case eVariety.Necklace: s.Append("@n   @9@iNecklace");
                        break;
                    case eVariety.OneHanded:
                    case eVariety.TwoHanded:
                        switch (MeleeType)
                        {
                            case eMeleeWeaponType.EDGED: s.AppendFormat("@n   @9@i{0}-Handed Edged Weapon", Variety == eVariety.OneHanded ? 1 : 2); break;
                            case eMeleeWeaponType.BLUNT: s.AppendFormat("@n   @9@i{0}-Handed Blunt Weapon", Variety == eVariety.OneHanded ? 1 : 2); break;
                            case eMeleeWeaponType.POLE: s.AppendFormat("@n   @9@i{0}-Handed Pole Weapon", Variety == eVariety.OneHanded ? 1 : 2); break;
                        }
                        break;
                    case eVariety.Poison: s.Append("@n   @9@iPoison");
                        break;
                    case eVariety.Potion: s.Append("@n   @9@iPotion");
                        break;
                    case eVariety.RangedNoAmmo: s.Append("@n   @9@iRanged Weapon");
                        break;
                    case eVariety.Ring: s.Append("@n   @9@iRing");
                        break;
                    case eVariety.Scroll: s.Append("@n   @9@iScroll");
                        break;
                    case eVariety.Shield: s.Append("@n   @9@iShield");
                        break;
                    case eVariety.Thrown: s.Append("@n   @9@iThrown Weapon");
                        break;
                    case eVariety.Tool: s.Append("@n   @9@iTool");
                        break;
                    case eVariety.Trousers: s.Append("@n   @9@iPants");
                        break;
                    case eVariety.Wand: s.Append("@n   @9@iWand");
                        break;
                    case eVariety.Food:
                    case eVariety.Gold:
                        return s.ToString();
                }


                if (IsRangedWeapon())
                {
                    s.AppendFormat("@n   Base Hit Bonus: {0}", Identified ? Bonus.ToString() : "@5??@9");
                }
                else if (IsWeapon())
                {
                    s.AppendFormat("@n   Base Damage: {0}", Identified ? "1-" + Level.ToString() : "@5??@9");
                    if (Identified && Bonus > 0) s.AppendFormat(" (+{0})", Bonus);
                }
                if (IsArmour())
                {
                    s.AppendFormat("@n   Defence: {0}", Identified ? Level.ToString() : "@5??@9");
                    if (Identified && Bonus > 0) s.AppendFormat(" (+{0})", Bonus);
                }

                if (Identified)
                {
                    if (Protection != 0)
                    {
                        if (Protection == 1)
                            s.AppendFormat("@n   Defence Bonus: 1");
                        else if (Protection == -1)
                            s.AppendFormat("@n   Defence Penalty: @21@9");
                        else if (Protection > 1)
                            s.AppendFormat("@n   Defence Bonus: 1 to {0}", Protection);
                        else
                            s.AppendFormat("@n   Defence Penalty: @21 to {0}@9", -1 * Protection);
                    }

                    string[] abils_grp1 = {
                    "", "Flaming Weapon",
                    "Demon Slayer",
                    "Undead Slayer",
                    "Lizard Slayer",
                    "Giant Slayer",
                    "Mage Slayer",
                    "Priest Slayer",
                    "Bug Slayer",
                    "Acidic Weapon",
                    "Soulsucker",//10
                    "Drain Missiles",
                    "Weak Weapon",
                    "Causes Fear",
                    "Poisoned Weapon"};

                    string[] abils_grp2 = {
                    "Protection", //30
                    "Full Protection",
                    "Fire Protection",
                    "Cold Protection",
                    "Poison Protection",
                    "Magic Protection",
                    "Acid Protection",
                    "Skill",
                    "Strength",
                    "Dexterity",
                    "Intelligence",//40
                    "Accuracy",
                    "Thieving",
                    "Giant Strength",
                    "Lighter Object",
                    "Heavier Object",
                    "Occasional Bless",
                    "Occasional Haste",
                    "Life Saving",
                    "Prot. From Petrify",
                    "Regenerate",//50
                    "Poison Augment",
                    "Disease Party",
                    "Will",
                    "Free Action",
                    "Speed",
                    "Slow Wearer",
                    "Protection from Undead",
                    "Protection from Demons",
                    "Prot. from Humanoids",
                    "Prot. from Reptiles",//60
                    "Prot. from Giants",
                    "Prot. from Disease"};

                    string[] abils_grp3 = {
                    "Poisons Weapon",//70
                    "Curse/Bless User",
                    "Cure/Cause Poison",
                    "Speed/Slow User",
                    "Add/Lose Invulnerability",
                    "Add/Lose Magic Res.",
                    "Add/Lose Web",
                    "Cause/Cure Disease",
                    "Add/Lose Sanctuary",
                    "Cure/Cause Dumbfound",
                    "Add/Lose Martyr's Shield",//80
                    "Cure/Cause Sleep",
                    "Cure/Cause Paralysis",
                    "Cure/Cause Acid",
                    "Bliss",
                    "Add/Lose Experience",
                    "Add/Lose Skill Pts.",
                    "Add/Lose Health",
                    "Add/Lose Spell Points",
                    "Doom",
                    "Light",//90
                    "Stealth",
                    "Firewalk",
                    "Flying",
                    "Major Healing"};//94

                    string[] abils_grp4 = {
                    "Returning", //170
                    "Lightning",
                    "Exploding",
                    "Acid",
                    "Slay Undead",
                    "Slay Demon",
                    "Heal Target"}; //176

                    int abil = (int)Ability;
                    if (Ability >= eItemAbil.FLAMING_WEAPON && Ability <= eItemAbil.POISONED_WEAPON)
                        s.AppendFormat("@n   Ability: {0}", abils_grp1[abil]);
                    else if (Ability >= eItemAbil.PROTECTION && Ability <= eItemAbil.PROTECT_FROM_DISEASE)
                        s.AppendFormat("@n   Ability: {0}", abils_grp2[abil - 30]);
                    else if (Ability >= eItemAbil.POISON_WEAPON && Ability <= eItemAbil.MAJOR_HEALING)
                        s.AppendFormat("@n   Ability: {0}", abils_grp3[abil - 70]);
                    else if (Ability >= eItemAbil.MISSILE_RETURNING && Ability <= eItemAbil.MISSILE_HEAL_TARGET)
                        s.AppendFormat("@n   Ability: {0}", abils_grp4[abil - 170]);
                    else if (Ability >= eItemAbil.HOLLY && Ability <= eItemAbil.MANDRAKE)
                        s.Append("@n   Ability: Alchemical ingredient");
                    else if (Ability == eItemAbil.CAST_SPELL)
                        s.AppendFormat("@n   Ability: {0}", MagicSpell.List[SpellID].Name);
                }
                else
                {
                    s.Append("@n   Ability: @5??@9");
                }

                if (IsArmour())
                {
                    s.AppendFormat("@n   Encumbrance: @2{0}@9", Awkward);
                }

                s.AppendFormat("@n   Weight: {0}", Weight);
                s.AppendFormat("@n   Value: {0} gold", Identified ? Value.ToString() : "@5??@9");
            }

            return s.ToString();
        }

        public int Value {
        get {
            if (Variety == eVariety.Gold) return Charges;
            if (Charges < 2) return BaseValue;
            else return Charges * BaseValue;
        }}

        public Color GetEquipBoxColour()
        {
            return Color.Green;
        }

        public Item()
        {
            Variety = eVariety.None;
        }

        public void Load(BinaryReader In)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            Name = In.ReadString();
            ShortName = In.ReadString();
            Variety = (eVariety)In.ReadInt16();
            Level = In.ReadInt16();
            Awkward = In.ReadSByte();
            Bonus = In.ReadSByte();
            Protection = In.ReadSByte();
            Charges = In.ReadInt16();
            MeleeType = (eMeleeWeaponType)In.ReadSByte();
            MagicUseType = In.ReadSByte();
            Picture = In.ReadInt16();
            Ability = (eItemAbil)In.ReadByte();
            AbilityStrength = In.ReadByte();
            TypeFlag = In.ReadByte();
            IsSpecial = In.ReadByte();
            a = In.ReadByte();
            BaseValue = In.ReadInt16();
            Weight = In.ReadByte();
            SpecialClass = In.ReadByte();
            Pos = In.ReadLocation();
            TreasureClass = In.ReadByte();
            Properties = In.ReadByte();
            SpellID = In.ReadString();
            AlchemyID = In.ReadString();
            if (BaseValue < Constants.ITEM_VALUE_IDENTIFY_LIMIT) Identified = true;
            if (Variety == eVariety.Food || Variety == eVariety.Gold) Identified = true; //Food and gold are never unidentified.
            List.Add(this);
        }

        public void LoadInstance(BinaryReader In)
        {
            id = In.ReadString();
            Name = In.ReadString();
            ShortName = In.ReadString();
            Variety = (eVariety)In.ReadInt16();
            Level = In.ReadInt16();
            Awkward = In.ReadSByte();
            Bonus = In.ReadSByte();
            Protection = In.ReadSByte();
            Charges = In.ReadInt16();
            MeleeType = (eMeleeWeaponType)In.ReadSByte();
            MagicUseType = In.ReadSByte();
            Picture = In.ReadInt16();
            Ability = (eItemAbil)In.ReadByte();
            AbilityStrength = In.ReadByte();
            TypeFlag = In.ReadByte();
            IsSpecial = In.ReadByte();
            a = In.ReadByte();
            BaseValue = In.ReadInt16();
            Weight = In.ReadByte();
            SpecialClass = In.ReadByte();
            Pos = In.ReadLocation();
            TreasureClass = In.ReadByte();
            Properties = In.ReadByte();
            SpellID = In.ReadString();
            AlchemyID = In.ReadString();
            if (BaseValue < Constants.ITEM_VALUE_IDENTIFY_LIMIT) Identified = true;
            if (Variety == eVariety.Food || Variety == eVariety.Gold) Identified = true; //Food and gold are never unidentified.
        }

        const int PROP_IDENTIFIED = 1;
        const int PROP_PROPERTY = 2;
        const int PROP_MAGIC = 4;
        const int PROP_CONTAINED = 8;
        const int PROP_CURSED = 16;

        public bool Identified {
            get{return (Properties & PROP_IDENTIFIED) != 0;}
            set { Properties = value ? Properties | PROP_IDENTIFIED : (PROP_IDENTIFIED ^ int.MaxValue) & Properties; }
        }
        public bool Magic
        {
            get { return (Properties & PROP_MAGIC) != 0; }
            set { Properties = value ? Properties | PROP_MAGIC : (PROP_MAGIC ^ int.MaxValue) & Properties; }
        }
        public bool NotYourProperty
        {
            get { return (Properties & PROP_PROPERTY) != 0; }
            set { Properties = value ? Properties | PROP_PROPERTY : (PROP_PROPERTY ^ int.MaxValue) & Properties; }
        }
        public bool Cursed
        {
            get { return (Properties & PROP_CURSED) != 0; }
            set { Properties = value ? Properties | PROP_CURSED : (PROP_CURSED ^ int.MaxValue) & Properties; }
        }
        public bool Contained
        {
            get { return (Properties & PROP_CONTAINED) != 0; }
            set { Properties = value ? Properties | PROP_CONTAINED : (PROP_CONTAINED ^ int.MaxValue) & Properties; }
        }

        public bool IsGoldOrFood()
        {
            return Variety == eVariety.Gold || Variety == eVariety.Food;
        }

        public bool IsArmour()
        {
            switch (Variety)
            {
            case eVariety.Armour:
            case eVariety.Boots:
            case eVariety.Gloves:
            case eVariety.Helm:
            case eVariety.Shield:
            case eVariety.Trousers:
                return true;
            } return false;
        }

        public bool IsWeapon()
        {
            return Variety == eVariety.OneHanded || Variety == eVariety.TwoHanded || Variety == eVariety.Thrown ||
                Variety == eVariety.Crossbow || Variety == eVariety.Bow || Variety == eVariety.Arrows ||
                Variety == eVariety.Bolts || Variety == eVariety.RangedNoAmmo;
        }

        public bool IsMeleeWeapon() { return Variety == eVariety.OneHanded || Variety == eVariety.TwoHanded; }
        public bool IsAmmo() { return Variety == eVariety.Bolts || Variety == eVariety.Arrows || Variety == eVariety.Thrown; }
        public bool IsRangedWeapon() { return Variety == eVariety.Bow || Variety == eVariety.Crossbow || Variety == eVariety.RangedNoAmmo; }

        public bool IsUseable()
        {
            return (Ability >= eItemAbil.POISON_AUGMENT && Ability <= eItemAbil.CALL_SPECIAL) || Ability == eItemAbil.CAST_SPELL;
        }

        public bool IsEquippable {get
        {
            switch (Variety)
            {
            case eVariety.None:
            case eVariety.Gold:
            case eVariety.Potion:
            case eVariety.Scroll:
            case eVariety.Wand:
            case eVariety.Food:
            case eVariety.Poison:
            case eVariety.NonUse: return false;
            } return true;
        }}

        public int GetSpecialDamage(eGenus npctype, out eDamageType dam_type) ////
        {
            int store = 0;
            dam_type = eDamageType.MAGIC;

            switch (Ability)
            {
                case eItemAbil.FLAMING_WEAPON:
                    store += Maths.Rand(1,1,AbilityStrength);//(AbilityStrength, 1, 6);
                    dam_type = eDamageType.FIRE;
                    break;
                case eItemAbil.MISSILE_LIGHTNING:
                    store += Maths.Rand(AbilityStrength, 1, 6);
                    break;
                case eItemAbil.DEMON_SLAYER:

                    if (npctype == eGenus.DEMON)
                        store += 8 * AbilityStrength;
                    break;
                case eItemAbil.UNDEAD_SLAYER:
                    if (npctype == eGenus.UNDEAD)
                        store += 6 * AbilityStrength;
                    break;
                case eItemAbil.LIZARD_SLAYER:
                    if (npctype == eGenus.REPTILE)
                        store += 5 * AbilityStrength;
                    break;
                case eItemAbil.GIANT_SLAYER:
                    if (npctype == eGenus.GIANT)
                        store += 8 * AbilityStrength;
                    break;
                case eItemAbil.MAGE_SLAYER:
                    if (npctype == eGenus.MAGE)
                        store += 4 * AbilityStrength;
                    break;
                case eItemAbil.PRIEST_SLAYER:
                    if (npctype == eGenus.PRIEST)
                        store += 4 * AbilityStrength;
                    break;
                case eItemAbil.BUG_SLAYER:
                    if (npctype == eGenus.BUG)
                        store += 7 * AbilityStrength;
                    break;
                case eItemAbil.MISSILE_SLAY_UNDEAD:
                    if (npctype == eGenus.UNDEAD)
                        store += 20 + 6 * AbilityStrength;
                    break;
                case eItemAbil.MISSILE_SLAY_DEMON:
                    if (npctype == eGenus.DEMON)
                        store += 25 + 8 * AbilityStrength;
                    break;
            }

            if (store == 0) dam_type = eDamageType.WEAPON;
            return store;
        }

        public void CursedMessage()
        {
            Game.AddMessage("Can't unequip " + ShortName + ". It's cursed!");
        }

        /// Returns the slot this item will need to be equipped in.
        /// DOES NOT TAKE INTO ACCOUNT - rings, which have a second ring slot.
        ///   & One-Handed weapons, which can be equipped in the off-hand slot.
        public eEquipSlot SlotNeeded
        {
            get
            {

                switch (Variety)
                {
                case eVariety.Armour: return eEquipSlot.Torso;
                case eVariety.Arrows: case eVariety.Bolts: return eEquipSlot.Ammo;
                case eVariety.Boots: return eEquipSlot.Feet;
                case eVariety.Bow: case eVariety.Crossbow: case eVariety.RangedNoAmmo: case eVariety.Thrown: return eEquipSlot.Ranged;
                case eVariety.Gloves: return eEquipSlot.Hands;
                case eVariety.Helm: return eEquipSlot.Head;
                case eVariety.Necklace: return eEquipSlot.Necklace;
                case eVariety.OneHanded: case eVariety.TwoHanded: return eEquipSlot.MainHand;
                case eVariety.Ring: return eEquipSlot.Ring1;
                case eVariety.Shield: return eEquipSlot.OffHand;
                case eVariety.Trousers: return eEquipSlot.Legs;
                case eVariety.Tool: return eEquipSlot.Tool;
                default:
                        return eEquipSlot.None;
                }
            }
        }

        public bool CompatibleSlot(eEquipSlot slot)
        {
            switch (Variety)
            {
            case eVariety.Armour: return slot == eEquipSlot.Torso;
            case eVariety.Arrows:
            case eVariety.Bolts: return slot == eEquipSlot.Ammo;
            case eVariety.Boots: return slot == eEquipSlot.Feet;
            case eVariety.Bow:
            case eVariety.Crossbow:
            case eVariety.RangedNoAmmo:
            case eVariety.Thrown: return slot == eEquipSlot.Ranged;
            case eVariety.Gloves: return slot == eEquipSlot.Hands;
            case eVariety.Helm: return slot == eEquipSlot.Head;
            case eVariety.Necklace: return slot == eEquipSlot.Necklace;
            case eVariety.OneHanded: return slot == eEquipSlot.MainHand || slot == eEquipSlot.OffHand;
            case eVariety.TwoHanded: return slot == eEquipSlot.MainHand;
            case eVariety.Ring: return slot == eEquipSlot.Ring1 || slot == eEquipSlot.Ring2;
            case eVariety.Shield: return slot == eEquipSlot.OffHand;
            case eVariety.Trousers: return slot == eEquipSlot.Legs;
            case eVariety.Tool: return slot == eEquipSlot.Tool;
            default:
                return false;
            }
        }

        public static Item CopyFromPreset(PresetItem p, TownMap town)
        {
            Item item = (Item)p.Record.MemberwiseClone();
            item.Pos = p.Pos;
            if (p.Charges != -1) item.Charges = p.Charges;
            if (item.IsGoldOrFood()) item.Level = p.Charges;

            if (p.Property) item.Properties |= 2;
            if (town.Abandoned)
                item.Properties &= 253;//NOT property because the town is abandoned.
            if (p.Contained) item.Properties |= 8;
            return item;
        }

        public Item Copy(bool make_identified = false, int specify_charges=-1) 
        {
            Item i = (Item)this.MemberwiseClone();
            if (make_identified) i.Identified = true;
            if (specify_charges != -1) i.Charges = specify_charges;
            return i;
        }

        /// <summary>
        /// See if this item can be stacked with the other one
        /// </summary>
        /// <param name="other"></param>
        /// <returns></returns>
        public bool CombinableWith(Item other)
        {
            if (other == null) return false;
            if (other.Charges < 1 || Charges < 1 || Charges >= Constants.ITEM_STACK_LIMIT || other.Charges >= Constants.ITEM_STACK_LIMIT) return false;

            //Apart from Position, Charges and Containable property, everything should be the same.
            return
                Variety == other.Variety &&
                Level == other.Level &&
                Awkward == other.Awkward &&
                Bonus == other.Bonus &&
                Protection == other.Protection &&
                MeleeType == other.MeleeType &&
                MagicUseType == other.MagicUseType &&
                Picture == other.Picture &&
                AbilityStrength == other.AbilityStrength &&
                TypeFlag == other.TypeFlag &&
                IsSpecial == other.IsSpecial &&
                Ability == other.Ability &&
                BaseValue == other.BaseValue &&
                Weight == other.Weight &&
                SpecialClass == other.SpecialClass &&
                Name == other.Name &&
                ShortName == other.ShortName &&
                TreasureClass == other.TreasureClass &&
                (Properties | PROP_CONTAINED) == (other.Properties | PROP_CONTAINED); 
        }

        public void DrawOffMapSimple(SpriteBatch sb, Vector2 pos, Color col)
        {
            pos = pos - new Vector2(Gfx.ITEMGFXWIDTH / 2, Gfx.ITEMGFXHEIGHT / 2);

            int sheet = (Picture & 0x7C00) >> 10;
            int no = (Picture & 0x03FF);

            if (Gfx.ItemGfx[sheet] == null) { sb.Draw(Gfx.NewGui, pos, new XnaRect(266, 193, 28, 36), Color.White); return; }
            XnaRect sr = new XnaRect((no % Gfx.ItemGfxSlotsAcross[sheet]) * Gfx.ITEMGFXWIDTH, (no / Gfx.ItemGfxSlotsAcross[sheet]) * Gfx.ITEMGFXHEIGHT, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT);
            sb.Draw(Gfx.ItemGfx[sheet], pos, sr, col);
        }

        public void DrawOffMap(SpriteBatch sb, Vector2 pos, Color col)
        {
            int sheet = (Picture & 0x7C00) >> 10;
            int no = (Picture & 0x03FF);

            if (Gfx.ItemGfx[sheet] == null)
            {
                sb.Draw(Gfx.NewGui, pos, new XnaRect(266, 193, 28, 36), Color.White); return;
            }
            else
            {
                XnaRect sr = new XnaRect((no % Gfx.ItemGfxSlotsAcross[sheet]) * Gfx.ITEMGFXWIDTH, (no / Gfx.ItemGfxSlotsAcross[sheet]) * Gfx.ITEMGFXHEIGHT, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT);
                sb.Draw(Gfx.ItemGfx[sheet], pos, sr, col);
            }

            //Draw box around it if this item is being dragged.
            if (Gui.DragItem == this)
            {
                Gfx.DrawRect((int)pos.X, (int)pos.Y, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT, Color.Tomato, false, 2);
            }

            //Draw charges in bottom right corner
            if (Charges > 0)
            {
                String ch = Charges.ToString();
                Vector2 chpos = pos + new Vector2(Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT) - new Vector2(Gfx.TinyFont.MeasureString(ch).Width, Gfx.TinyFont.MeasureString(ch).Height);
                sb.DrawString(Gfx.TinyFont, ch, chpos, Color.LightBlue); 
            }

            //Draw red 'NY' for 'Not Yours' in top-right corner
            if (NotYourProperty)
            {
                string ny = "NY";
                pos.X += Gfx.ITEMGFXWIDTH - Gfx.TinyFont.MeasureString(ny).Width;
                sb.DrawString(Gfx.TinyFont, ny, pos, Color.Red);
            }

        }

        public bool Filter(eItemFilter filter)
        {
            switch (filter)
            {
                case eItemFilter.ALL: return true;
                case eItemFilter.WEAPONS: return IsWeapon() || IsAmmo();
                case eItemFilter.ARMOUR: return IsArmour() || Variety == eVariety.Ring || Variety == eVariety.Necklace;
                case eItemFilter.OTHER: return Variety == eVariety.NonUse || Variety == eVariety.Food || Variety == eVariety.Gold || Variety == eVariety.Tool;
                case eItemFilter.POTIONS: return Variety == eVariety.Potion || Variety == eVariety.Poison;
                case eItemFilter.USEABLES: return Variety == eVariety.Wand || Variety == eVariety.Scroll;
            }
            return false;
        }
        public eItemFilter GetFilterGroup()
        {
            for (eItemFilter e = eItemFilter.WEAPONS; e <= eItemFilter.OTHER; e++)
                if (Filter(e)) return e;
            return eItemFilter.ALL;
        }


        public void Draw(SpriteBatch sb, XnaRect dr)
        {
            if (Contained) return;

            int sheet = (Picture & 0x7C00) >> 10;
            int no = (Picture & 0x03FF);

            if (Gfx.ItemGfx[sheet] == null)
            {
                sb.Draw(Gfx.NewGui, dr, new XnaRect(266, 193, 28, 36), Color.White); return;
            }
            else
            {
                XnaRect sr = new XnaRect((no % Gfx.ItemGfxSlotsAcross[sheet]) * Gfx.ITEMGFXWIDTH, (no / Gfx.ItemGfxSlotsAcross[sheet]) * Gfx.ITEMGFXHEIGHT, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT);
                sb.Draw(Gfx.ItemGfx[sheet], dr, sr, Color.White);
            }
        }

        public bool Identify(int cost)
        {
            if (Identified) { Game.AddMessage("Item is already identified"); return false; }
            if (Game.CurrentParty.Gold < cost) { Game.AddMessage("You need " + cost + " gold\nto identify that"); return false; }
            Identified = true;
            Game.CurrentParty.Gold -= cost;
            Game.AddMessage(ShortName + " identified as '" + Name + "'");
            Sound.Play("068_identify");
            return true;
        }

        public bool IsEnchantable()
        {
            return Identified && IsWeapon() && Ability == eItemAbil.NO_ABILITY && !Magic;
        }

        public bool Enchant(eEnchantShop type, int cost)
        {
            if (!Identified) { Game.AddMessage("Item must be identified"); return false; }
            if (!IsWeapon()) { Game.AddMessage("Can only enchant weapons"); return false; }
            if (Ability != eItemAbil.NO_ABILITY) { Game.AddMessage("Item must not already have an ability"); return false; }
            if (Magic) { Game.AddMessage("Can only enchant non-magic items"); return false; }
            if (Game.CurrentParty.Gold < cost) { Game.AddMessage("You need " + cost + " gold\nto enchant that"); return false; }            
            Game.CurrentParty.Gold -= cost;

            Magic = true;
            switch (type)
            {
            case eEnchantShop.PLUS_1:
                Name = Name + "(+1)";
                Bonus++;
                BaseValue = cost;
                break;
            case eEnchantShop.PLUS_2:
                Name = Name + "(+2)";
                Bonus += 2;
                BaseValue = cost;
                break;
            case eEnchantShop.PLUS_3:
                Name = Name + "(+3)";
                Bonus += 3;
                BaseValue = cost;
                break;
            case eEnchantShop.SHOOT_FLAMES:
                Name = Name + "(F)";
                Ability = eItemAbil.CAST_SPELL;
                AbilityStrength = 5;
                Charges = 8;
                SpellID = "m_flame";
                break;
            case eEnchantShop.FLAMING:
                Name = Name + "(F!)";
                BaseValue = cost;
                Ability = eItemAbil.FLAMING_WEAPON; 
                AbilityStrength = 5;
                break;
            case eEnchantShop.PLUS_5:
                Name = Name + "(+5)";
                BaseValue = cost;
                Bonus += 5;
                break;
            case eEnchantShop.BLESSED:
                Name = Name + "(B)";
                Bonus++;
                Ability = eItemAbil.BLESS_CURSE;
                AbilityStrength = 5;
                MagicUseType = 0;
                Charges = 8;
                break;
            }
            if (BaseValue > 15000)
                BaseValue = 15000;
            if (BaseValue < 0)
                BaseValue = 15000;

            Game.AddMessage(ShortName + " is now '" + Name + "'");

            return true;
        }

        //Some static functions for generating treasure or pc starting items
        #region LOOT_GENERATORS

        public static Item GetStartItem(int n)
        {
            Item i = new Item();
            switch (n)
            {
                case 0:
                    i.Variety = eVariety.OneHanded;
                    i.Level = 4;
                    i.Bonus = 1;
                    i.MeleeType = eMeleeWeaponType.EDGED;
                    i.Picture = 45;
                    i.BaseValue = 2;
                    i.Weight = 7;
                    i.Name = "Bronze Knife";
                    i.ShortName = "Knife";
                    i.Properties = 1;
                    break;
                case 1:
                    i.Variety = eVariety.Shield;
                    i.Level = 1;
                    i.Awkward = 1;
                    i.Picture = 65;
                    i.BaseValue = 2;
                    i.Weight = 20;
                    i.Name = "Crude Buckler";
                    i.ShortName = "Buckler";
                    i.Properties = 1;
                    break;
                case 2:
                    i.Variety = eVariety.Bow;
                    i.Picture = 10;
                    i.BaseValue = 15;
                    i.Weight = 20;
                    i.Name = "Cavewood Bow";
                    i.ShortName = "Bow";
                    i.Properties = 1;
                    break;
                case 3:
                    i.Variety = eVariety.Arrows;
                    i.Level = 12;
                    i.Charges = 12;
                    i.Picture = 47;
                    i.BaseValue = 1;
                    i.Weight = 1;
                    i.Name = "Arrows";
                    i.ShortName = "Arrows";
                    i.Properties = 1;
                    i.ID = "Arrows_103";
                    i.TreasureClass = 1;
                    i.TypeFlag = 6;
                    i.MeleeType = eMeleeWeaponType.EDGED;
                    
                    break;
                case 4:
                    i.Variety = eVariety.TwoHanded;
                    i.Level = 9;
                    i.MeleeType = eMeleeWeaponType.POLE;
                    i.Picture = 4;
                    i.BaseValue = 10;
                    i.Weight = 30;
                    i.Name = "Stone Spear";
                    i.ShortName = "Spear";
                    i.Properties = 1;
                    break;
                case 5:
                    i.Variety = eVariety.Helm;
                    i.Level = 1;
                    i.Picture = 66;
                    i.BaseValue = 6;
                    i.Weight = 15;
                    i.Name = "Leather Helm";
                    i.ShortName = "Helm";
                    i.Properties = 1;
                    break;
            }
            return i;
        }

        public eSkill MeleeTypeToSkill()
        {
            switch (MeleeType)
            {
                case eMeleeWeaponType.EDGED: return eSkill.EDGED_WEAPONS;
                case eMeleeWeaponType.BLUNT: return eSkill.BASHING_WEAPONS;
                case eMeleeWeaponType.POLE: return eSkill.POLE_WEAPONS;
                default: return eSkill.EDGED_WEAPONS;
            }
        }

        public static Item GetTreasure(int loot)
        {
            Item treas = null;// = new Item_Record_Type();

            short[] which_treas_chart = {1,1,1,1,1,2,2,2,2,2,
								        3,3,3,3,3,2,2,2,4,4,
								        4,4,5,5,5,6,6,6,7,7,
								        7,8,8,9,9,10,11,12,12,13,
								        13,14, 9,10,11,9,10,11}; //48
            int r1;

            //treas.variety = 0;
            r1 = Maths.Rand(1, 0, 41);
            if (loot >= 3) r1 += 3;
            switch (which_treas_chart[r1])
            {
                case 1: treas = get_food(); break;
                case 2: treas = get_weapon(loot); break;
                case 3: treas = get_armor(loot); break;
                case 4: treas = get_shield(loot); break;
                case 5: treas = get_helm(loot); break;
                case 6: treas = get_missile(loot); break;
                case 7: treas = get_potion(loot); break;
                case 8: treas = get_scroll(loot); break;
                case 9: treas = get_wand(loot); break;
                case 10: treas = get_ring(loot); break;
                case 11: treas = get_necklace(loot); break;
                case 12: treas = get_poison(loot); break;
                case 13: treas = get_gloves(loot); break;
                case 14: treas = get_boots(loot); break;
            }	
            if (treas != null) return treas;
            else return new Item();
            //TODO: For now we don't return null if we can't find a treasure, just a dummy item with a Variety of None.
        }

        static Item pull_item_of_type(int loot_max, int min_val, int max_val, eVariety t1, eVariety t2 = eVariety.None, eVariety t3 = eVariety.None)
        {
            int i, val;
            Item temp_i;

            // occasionally get nice item
            if (Maths.Rand(1, 0, 160) == 80)
            {
                loot_max += 2;
                max_val += 2000;
            }
            for (i = 0; i < 80; i++)
            {
                temp_i = Item.GetRandom().Copy();
                if (temp_i.Variety == t1 || (t2 != eVariety.None && temp_i.Variety == t2) || (t3 != eVariety.None && temp_i.Variety == t3))
                {
                    val = temp_i.Value;
                    if ((val >= min_val) && (val <= max_val) && (temp_i.TreasureClass != 0) &&
                        (temp_i.TreasureClass <= loot_max))
                        return temp_i;
                }
            }
            return null;
        }

        public static Item GetRandom()
        {
            if (List.Count == 0) return null;
            else return List[Maths.Rand(1, 0, List.Count-1)];
        }

        static Item get_food()
        {
            if (Maths.Rand(1, 0, 2) != 1) return null;

            Item food = new Item();
            food.Variety = eVariety.Food; // 11;
            food.Picture = 62;
            food.Name = "Food";
            food.ShortName = "Food";
            food.Identified = true;
            food.Picture += (byte)Maths.Rand(1, 0, 2);
            food.Level = (short)Maths.Rand(1, 5, 10);
            if (Maths.Rand(1, 0, 9) == 5)
                food.Picture = 113;
            if (Maths.Rand(1, 0, 9) == 5)
                food.Picture = 114;

            return food;
        }

        static Item get_weapon(int loot)
        {
            if (loot == 0) return null;
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.OneHanded, eVariety.TwoHanded);
        }

        static Item get_armor(int loot)
        {
            int r1;
            if (loot == 0) return null;
            r1 = Maths.Rand(1, (loot - 1) * 5 + 124, 142);
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Armour);//13);
        }

        static Item get_helm(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Helm);// 14);
        }

        static Item get_gloves(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Gloves);//15);
        }

        static Item get_boots(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Boots);
        }

        static Item get_shield(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Shield);
        }

        static Item get_potion(int loot)
        {
            if (Maths.Rand(1, 0, 80) < 20 * (4 - loot))
                return pull_item_of_type(loot, loot_min[loot], loot_max[loot] / 2, eVariety.Potion);
            else return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Potion);
        }

        static Item get_scroll(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Scroll);
        }

        static Item get_missile(int loot)
        {
            if (Maths.Rand(1, 0, 2) < 2)
                return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Arrows, eVariety.Thrown, eVariety.Bow);
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Crossbow, eVariety.Bolts, eVariety.RangedNoAmmo);
        }

        static Item get_poison(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Poison);
        }

        static Item get_wand(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Wand);
        }

        static Item get_ring(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Ring);
        }

        static Item get_necklace(int loot)
        {
            return pull_item_of_type(loot, loot_min[loot], loot_max[loot], eVariety.Necklace);
        } 

        #endregion
    }
}
