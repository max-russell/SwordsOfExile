using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    /// <summary>
    /// Every NPC in the game is assigned a specific NPCRecord type. NPCRecord contains all the attributes common to NPCs of that type. For example, if two NPCs are both Goblin Fighters, their Record field will both be set to the 'Goblin Fighter' NPCRecord.
    /// </summary>
    public class NPCRecord : IListEntity//Formerly monster_record_type - bit of consistency, eh?
    {
        /// <summary>All NPCRecords in the current scenario</summary>
        public static ExileList<NPCRecord> List = new ExileList<NPCRecord>();

        /// <summary>String key used to identify a particular NPCRecord in NPCRecord.List</summary>
        public string ID { get { return id; } set { id = value; } }
        string id;

        /// <summary>Display name of the NPC</summary>
        public string Name;

        public int Num;
        
        /// <summary> Value reflecting the overall strength of the NPC. The higher level the harder the NPC will be to overcome in combat.</summary>
        public int Level;

        /// <summary>The amount of health points an NPC of this type will start with.</summary>
        public int Health;

        /// <summary>The amount of spell points an NPC of this type will start with.</summary>
        public int SP;

        /// <summary>Armour rating. NPCs with higher ratings take less damage.</summary>
        public int Armour;

        /// <summary>NPCs with higher skill hit more often.</summary>
        public int Skill;

        /// <summary>How many tiles an NPC will move each turn during combat.</summary>
        public int Speed;

        /// <summary>The level of NPC mage spells that an NPC can cast (0 - 7). If zero, an NPC will not cast mage spells.</summary>
        public int MageLevel;

        /// <summary>The level of NPC priest spells that an NPC can cast (0 - 7). If zero, an NPC will not cast priest spells.</summary>
        public int PriestLevel;

        /// <summary>The morale an NPC begins with. If morale falls too low, an NPC will flee. Morale is automatically calculated based on the creature's level, but some kinds of NPC (eg, Undead) are not affected by morale.</summary>
        public int Morale;

        /// <summary>Whether an NPC is immune or resistant to Fire, Cold, Magic or Poison. Use 'or' to combine more than one resistance or immunity. Eg: npc.Immunities = eImmunity.FIRE_RESISTANCE or eImmunity.COLD_IMMUNITY</summary>
        public eImmunity Immunities;

        /// <summary>Size of the NPC in tiles (Either 1 or 2)</summary>
        public int Width, Height;
        
        /// <summary>Summoning spells used this field to determine what creatures will be summoned. For instance, the spell 'Weak Summon' may summon an NPC if its Record's SummonType is set to 1.</summary>
        public int SummonType;
            
        /// <summary>Default picture portrait when the party talks to an NPC. Is overridden by an NPCPreset's FacialPic field.</summary>
        public int FacialPic;
        
        /// <summary>Graphic to use for the NPC</summary>
        public int Picture;

        /// <summary>Percentage chance of NPC radiating fields or summoning creatures according to their Radiate ability.</summary>
        public byte RadiateProbability;

        /// <summary>The NPC that will be summoned if the Radiate ability is set to 'Summon'</summary>
        public NPCRecord NPCtoSummon;

        /// <summary>Default starting attitude for this type of NPC.</summary>
        public eAttitude Attitude;

        /// <summary>Whether the creature will radiate fields as it moves, or automatically summon other NPCs</summary>
        public eRadiate Radiate;

        /// <summary> An NPC can have up to 3 attacks, each dealing a different amount of base damage.</summary>
        public short[] AttackAmount = new short[3];

        /// <summary>An NPC can have up to 3 attacks, each dealing a different amount of base damage.</summary>
        public short[] AttackMultiplier = new short[3];

        /// <summary>Description of the NPC's first attack.</summary>
        public eMonsterAttackTypes Attack1Type;

        /// <summary>Description of the NPC's second and third attacks.</summary>
        public eMonsterAttackTypes Attack23Type;


        public int Breath;
        public eBreathType BreathType;
        public int Treasure;
        public int Poison;
        public int DropItemChance;
        public eGenus Genus;/*(was m_type)*/
        public eCSS SpecialSkill;
        public Item DropItem = null;
        string DeathSoundA, DeathSoundB;

        public string DeathSound
        {
            get
            {
                if (DeathSoundA == "" && DeathSoundB == "") return "";
                if (DeathSoundA == "") return DeathSoundB;
                if (DeathSoundB == "") return DeathSoundA;
                else return Maths.Rand(1, 0, 1) == 0 ? DeathSoundA : DeathSoundB;
            }
        }

        public string FuncOnDeath;

        public bool ImmuneTo(eImmunity type)
        {
            return (Immunities & type) != eImmunity.NONE;
        }

        public void Load(BinaryReader In) { } //Needed for interface, not called.

        public static void LoadAll(BinaryReader In)
        {
            Dictionary<string, string> summonList = new Dictionary<string, string>();
            NPCRecord.List.Clear();

            while (true)
            {
                byte b = In.ReadByte();

                if (b == 0) break;

                if (b == 1)
                {
                    new NPCRecord(In, summonList);
                }
                else if (b == 2)
                    Scenario.LoadAndDisregardEditorFolder(In);
            }

            foreach (KeyValuePair<string, string> k in summonList)
            {
                NPCRecord summons;
                if (List.TryGetValue(k.Value, out summons))
                    List[k.Key].NPCtoSummon = summons;
            }
        }


        public NPCRecord() { }
        //Constructor just for making NPC pictures in message windows
        public NPCRecord(int picnum, int width, int height)
        {
            Picture = picnum;
            Width = width;
            Height = height;
        }

        public NPCRecord(BinaryReader In, Dictionary<string, string> summonList)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            Name = In.ReadString();
            Num = In.ReadInt16();
            Level = In.ReadInt16();
            Health = In.ReadInt16(); 
            Armour = In.ReadInt16();
            Skill = In.ReadInt16();
            AttackMultiplier[0] = In.ReadInt16();
            AttackAmount[0] = In.ReadInt16();
            AttackMultiplier[1] = In.ReadInt16();
            AttackAmount[1] = In.ReadInt16();
            AttackMultiplier[2] = In.ReadInt16();
            AttackAmount[2] = In.ReadInt16();
            Attack1Type = (eMonsterAttackTypes)In.ReadByte();
            Attack23Type = (eMonsterAttackTypes)In.ReadByte();
            Genus = (eGenus)In.ReadByte();
            DeathSoundA = In.ReadString();
            DeathSoundB = In.ReadString();

            Speed = In.ReadByte();
            MageLevel = In.ReadByte();
            PriestLevel = In.ReadByte();

            if (MageLevel > 0 || PriestLevel > 0) SP = 12 * Level;

            Breath = In.ReadByte();
            BreathType = (eBreathType)In.ReadByte();
            Treasure = In.ReadByte();
            SpecialSkill = (eCSS)In.ReadByte(); //TODO: NPC Special skill: Something about Petrifying Touch should be Disease touch?
            Poison = In.ReadByte();

            Morale = 0; 
            Morale = 10 * Level + (Level >= 20 ? 10 * (Level - 20) : 0);

            Item.List.TryGetValue(In.ReadString(), out DropItem);

            DropItemChance = In.ReadInt16();
            Immunities = (eImmunity)In.ReadByte();
            Width = In.ReadByte();
            Height = In.ReadByte();
            Radiate = (eRadiate)In.ReadByte();
            RadiateProbability = In.ReadByte();

            string s = In.ReadString();
            if (s != "")
                summonList.Add(ID, s);

            Attitude = (eAttitude)In.ReadByte();
            SummonType = In.ReadByte();
            FacialPic = In.ReadInt16();
            Picture = In.ReadInt32();

            FuncOnDeath = In.ReadString();

            List.Add(this);
        }

        public static NPCRecord GetSummonMonster(int summon_class)
        {
            List<NPCRecord> pool = new List<NPCRecord>();
            foreach (NPCRecord npc in List)
                if (npc.SummonType == summon_class) pool.Add(npc);

            if (pool.Count == 0) { return null; }
            return pool[Maths.Rand(1, 0, pool.Count - 1)];
        }

        public XnaRect GetGraphic(bool facing_right, bool attacking, out Texture2D stex)
        {
            int sheet = (Picture & 0x7C00) >> 10; 
            int no = (Picture & 0x03FF);

            if (Width == 1 && Height == 1)
            {
                if (Gfx.NPCGfx1x1[sheet] != null)
                {
                    stex = Gfx.NPCGfx1x1[sheet];
                    return new XnaRect((facing_right ? 0 : Gfx.CHARGFXWIDTH)
                        + (attacking ? Gfx.CHARGFXWIDTH * 2 : 0)
                        + (no % Gfx.NPCGfx1x1SlotsAcross[sheet]) * Gfx.CHARGFXWIDTH * 4,
                                                (no / Gfx.NPCGfx1x1SlotsAcross[sheet]) * Gfx.CHARGFXHEIGHT,
                                                 Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
                }
            }
            else if (Width == 2 && Height == 1)
            {
                if (Gfx.NPCGfx2x1[sheet] != null)
                {
                    XnaRect sr = new XnaRect((facing_right ? 0 : Gfx.CHARGFXWIDTH * 2)
                                                 + (attacking ? Gfx.CHARGFXWIDTH * 4 : 0)
                                                 + ((no % Gfx.NPCGfx2x1SlotsAcross[sheet]) * Gfx.CHARGFXWIDTH * 8),
                                                (no / Gfx.NPCGfx2x1SlotsAcross[sheet]) * Gfx.CHARGFXHEIGHT,
                                                 Gfx.CHARGFXWIDTH * 2, Gfx.CHARGFXHEIGHT);
                    stex = Gfx.NPCGfx2x1[sheet];
                    return sr;
                }
            }
            else if (Width == 1 && Height == 2)
            {
                if (Gfx.NPCGfx1x2[sheet] != null)
                {
                    XnaRect sr = new XnaRect((facing_right ? 0 : Gfx.CHARGFXWIDTH)
                                                + (attacking ? Gfx.CHARGFXWIDTH * 2 : 0)
                                                + ((no % Gfx.NPCGfx1x2SlotsAcross[sheet]) * Gfx.CHARGFXWIDTH * 4),
                                                (no / Gfx.NPCGfx1x2SlotsAcross[sheet]) * Gfx.CHARGFXHEIGHT * 2,
                                                 Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT * 2);
                    stex = Gfx.NPCGfx1x2[sheet];
                    return sr;
                }
            }
            else if (Width == 2 && Height == 2)
            {
                if (Gfx.NPCGfx2x2[sheet] != null)
                {
                    XnaRect sr = new XnaRect((facing_right ? 0 : Gfx.CHARGFXWIDTH * 2) +
                                                +(attacking ? Gfx.CHARGFXWIDTH * 4 : 0) +
                                                +((no % Gfx.NPCGfx2x2SlotsAcross[sheet]) * Gfx.CHARGFXWIDTH * 8),
                                                (no / Gfx.NPCGfx2x2SlotsAcross[sheet]) * Gfx.CHARGFXHEIGHT * 2,
                             Gfx.CHARGFXWIDTH * 2, Gfx.CHARGFXHEIGHT * 2);
                    if (attacking) sr.X += Gfx.CHARGFXWIDTH * 4;
                    stex = Gfx.NPCGfx2x2[sheet];
                    return sr;
                }
            }

            stex = Gfx.MixedGfx;
            return new XnaRect(312, 0, 28, 36);
        }

        public bool Humanish
        {
            get
            {
                switch (Genus)
                {
                    case eGenus.HUMAN:
                    case eGenus.IMPORTANT:
                    case eGenus.MAGE:
                    case eGenus.PRIEST:
                    case eGenus.HUMANOID:
                    case eGenus.GIANT:
                        return true;
                    default: return false;
                }
            }
        }


    }
}