using System;
using System.IO;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;


namespace SwordsOfExileGame
{
    public class TerrainRecord : IListEntity 
    {
        PartyType Party { get { return Game.CurrentParty; } }
        public static TerrainRecord NoOverlay = new TerrainRecord();
        public static TerrainRecord[] UnderlayList = new TerrainRecord[256];
        public static TerrainRecord[] OverlayList = new TerrainRecord[256];
        public static ExileList<TerrainRecord> List = new ExileList<TerrainRecord>(); 

        const int CAVE_WALKWAY = 82;
        const int GRASS_WALKWAY = 83;
        const int CAVE_ROAD = 79,
            GRASS_ROAD = 80,
            HILLS_ROAD = 81,
            GRASS_S_HILLS_N = 38,
            GRASS_E_HILLS_W = 40,
            GRASS_N_HILLS_S = 42,
            GRASS_W_HILLS_E = 44;

        public string ID { get { return id; } set { id = value; } }
        string id;

        public int Num;
        public int Picture;
        public eBlock2 Blockag;
        public int Obscurity;
        public int Layer;

        public object Flag1, Flag2;
        public TerrainRecord TransformTo;
        public eTerSpec Special;
        public bool FlyOver, BoatOver, BlocksHorse, DestroysBarrels;
        public int light_radius, step_sound;

        public TriggerSpot Trigger;

        public string Name; //Not in Vogel's original

        public string TooltipInfo(Location pos, Location from)
        {
            return Name;
        }

        public void Load(BinaryReader In) { }
        public static void LoadAll(BinaryReader In)
        {
            TerrainRecord.List.Clear();
            TerrainRecord.UnderlayList = new TerrainRecord[256];
            TerrainRecord.OverlayList = new TerrainRecord[256];
            TerrainRecord.OverlayList[0] = TerrainRecord.NoOverlay;
            List<string> trans_to_ids = new List<string>();

            while (true)
            {
                byte b = In.ReadByte();

                if (b == 0) break;

                if (b == 1)
                {
                    new TerrainRecord(In, trans_to_ids);
                }
                else if (b == 2)
                    Scenario.LoadAndDisregardEditorFolder(In);
            }

            int x = 0;
            foreach (TerrainRecord ter in TerrainRecord.List)
            {
                if (trans_to_ids[x] != "" && TerrainRecord.List.Contains(trans_to_ids[x]))
                    ter.TransformTo = TerrainRecord.List[trans_to_ids[x]];
                x++;

                if (ter.Special == eTerSpec.CHANGE_WHEN_STEP_ON || ter.Special == eTerSpec.CRUMBLING_TERRAIN || ter.Special == eTerSpec.LOCKABLE_TERRAIN
                    || ter.Special == eTerSpec.UNLOCKABLE_TERRAIN || ter.Special == eTerSpec.UNLOCKABLE_BASHABLE || ter.Special == eTerSpec.CHANGE_WHEN_USED)
                {
                    string s = (string)ter.Flag1;
                    if (s != "" && TerrainRecord.List.Contains(s))
                        ter.Flag1 = TerrainRecord.List[s];
                }
            }
        }

        public TerrainRecord() { Num = -1; Picture = -1; }

        public TerrainRecord(BinaryReader In, List<string> trans_to_id)
        {
            ID = In.ReadString();
            In.ReadString(); //Folder: disregard
            Num = In.ReadInt16();
            Layer = In.ReadByte();

            Name = In.ReadString();
            Picture = In.ReadInt32();
            Blockag = (eBlock2)In.ReadByte();
            Obscurity = In.ReadByte();

            byte b = In.ReadByte();
            BlocksHorse = (b & 1) != 0;
            BoatOver = (b & 2) != 0;
            FlyOver = (b & 4) != 0;
            DestroysBarrels = In.ReadBoolean();
            step_sound = In.ReadByte();
            light_radius = In.ReadByte();
            In.ReadByte(); //Editor Icon - not used in game
            Special = (eTerSpec)In.ReadByte();

            trans_to_id.Add(In.ReadString());

            if (Special == eTerSpec.CHANGE_WHEN_STEP_ON || Special == eTerSpec.CRUMBLING_TERRAIN || Special == eTerSpec.LOCKABLE_TERRAIN
                || Special == eTerSpec.UNLOCKABLE_TERRAIN || Special == eTerSpec.UNLOCKABLE_BASHABLE || Special == eTerSpec.CHANGE_WHEN_USED)
                Flag1 = In.ReadString(); //For now, but after all terrains have loaded, convert to a TerrainRecord
            else
                Flag1 = (Int32)In.ReadInt16(); //It's a number

            if (Special == eTerSpec.CHANGE_WHEN_STEP_ON)
                Flag2 = In.ReadString(); //Sound Effect ID, leave as string
            else
                Flag2 = (Int32)In.ReadInt16();

            if (In.ReadBoolean()) //Does this terrain have a script trigger?
            {
                Trigger = new TriggerSpot(In, true); //Read the trigger, but it has no map location
            }

            In.ReadString(); //EditorScript - not used in game.

            if (Layer == 1 && Num >= 1 && Num <= 255) OverlayList[Num] = this;
            else if (Layer == 0 && Num >= 0 && Num <= 255) UnderlayList[Num] = this;
            List.Add(this);
        }

        public void Draw(SpriteBatch sb, XnaRect r_dst, bool fullbright)//, TerrainRecord to_n = null, TerrainRecord to_s = null, TerrainRecord to_w = null, TerrainRecord to_e = null)
        {
            int sheet = (Picture & 0x7C00) >> 10;            
            int no = (Picture & 0x03FF); 

            if ((Picture & 0x10000) != 0)
            {
                if (Gfx.AnimTerrainGfx[sheet] == null) return;
                //Animated terrain
                var r_src = new XnaRect(no % Gfx.AnimTerrainGfxSlotsAcross[sheet] * 4 * Gfx.SRCTILEWIDTH + Game.AnimTicks * Gfx.SRCTILEWIDTH,
                                          (no / Gfx.AnimTerrainGfxSlotsAcross[sheet]) * Gfx.SRCTILEHEIGHT,
                                          Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
                sb.Draw(Gfx.AnimTerrainGfx[sheet], r_dst, r_src, fullbright ? Color.White : Color.Gray);
            }
            else
            {
                if (Gfx.TerrainGfx[sheet] == null) return;
                //Static terrain

                int col = no % Gfx.TerrainGfxSlotsAcross[sheet];
                int row = no / Gfx.TerrainGfxSlotsAcross[sheet];
                XnaRect rs = new XnaRect(col * Gfx.SRCTILEWIDTH, row * Gfx.SRCTILEHEIGHT, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
                sb.Draw(Gfx.TerrainGfx[sheet], r_dst, rs, fullbright ? Color.White : Color.Gray);
            }
            return;
        }

        public TerrainRecord GetLocked()
        {
            if (Special == eTerSpec.LOCKABLE_TERRAIN && !(Flag1 == null) && Flag1 is TerrainRecord)
                return (TerrainRecord)Flag1;
            else
                return this;
        }
        public TerrainRecord GetUnlocked()
        {
            if ((Special == eTerSpec.UNLOCKABLE_TERRAIN || Special == eTerSpec.UNLOCKABLE_BASHABLE)
                && !(Flag1 == null) && Flag1 is TerrainRecord)
                return (TerrainRecord)Flag1;
            else
                return this;
        }
        public TerrainRecord GetCrumbleTo()
        {
            if (Special == eTerSpec.CRUMBLING_TERRAIN && !(Flag1 == null) && Flag1 is TerrainRecord)
                return (TerrainRecord)Flag1;
            else
                return this;
        }

        public bool DoNotPlacePC { get{return Blockag >= eBlock2.CLEAR_NO_PLACE;}}
        public bool DoNotPlaceNPC { get { return Blockag >= eBlock2.CLEAR_PC; } }

        public bool BlocksPC { get { return Blockag == eBlock2.BLOCKED; } }////Blockage > eBlock.CLEAR_WALK_PC; } }
        public bool BlocksNPC { get { return Blockag == eBlock2.BLOCKED || Blockag == eBlock2.CLEAR_PC; } }//Blockage >= eBlock.CLEAR_WALK_PC; } }
 

        /// <summary>
        /// Called when a PC steps onto the terrain which has a damaging effect (lave, swamp etc)
        /// </summary>
        /// <param name="pc"></param>
        /// <param name="report">Whether to display a message reporting stepping here.</param>
        public void NastyTerrainEffect(PCType pc, bool report = true)
        {
            switch (Special)
            {
                case eTerSpec.DOES_FIRE_DAMAGE:
                case eTerSpec.DOES_COLD_DAMAGE:
                case eTerSpec.DOES_MAGIC_DAMAGE:
                    if (Party.Flying > 0) break;
                    eDamageType dam_type = eDamageType.WEAPON; int pic_type = 0;
                    if (Special == eTerSpec.DOES_FIRE_DAMAGE)
                    {
                        if (report) Game.AddMessage("  It's hot!");
                        dam_type = eDamageType.FIRE; pic_type = 0;
                        if (Party.Firewalk > 0)
                        {
                            if (report) Game.AddMessage("  It doesn't affect you.");
                            break;
                        }
                    }
                    if (Special == eTerSpec.DOES_COLD_DAMAGE)
                    {
                        if (report) Game.AddMessage("  You feel cold!");
                        dam_type = eDamageType.COLD; pic_type = 4;
                    }
                    if (Special == eTerSpec.DOES_MAGIC_DAMAGE)
                    {
                        if (report) Game.AddMessage("  Something shocks you!");
                        dam_type = eDamageType.MAGIC; pic_type = 1;
                    }
                    int r1 = Maths.Rand(Convert.ToInt32(Flag2), 1/*(int)dam_type*/, Convert.ToInt32(Flag1));
                    pc.Damage(null, r1, 0, dam_type);
                    break;
                case eTerSpec.POISON_LAND:
                case eTerSpec.DISEASED_LAND:
                    if (Party.Flying > 0) break;
                    if (Party.IsInABoat()) break; ;

                    if (Maths.Rand(1, 1, 100) <= Convert.ToInt32(Flag2))
                    {
                        if (Special == eTerSpec.POISON_LAND)
                            pc.Poison(Convert.ToInt32(Flag1));
                        else pc.Disease(Convert.ToInt32(Flag1));
                    }
                    break;
            }
        }

    }

}