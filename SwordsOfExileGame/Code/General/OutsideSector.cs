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


namespace SwordsOfExileGame
{

    public class OutsideSector: IListEntity
    {
        public static ExileList<OutsideSector> List = new ExileList<OutsideSector>();
        public string ID { get { return SectorPos.X + ", " + SectorPos.Y; } set { } }

        PartyType Party { get { return Game.CurrentParty; } }

        public int Width, Height;
        string name;
        public string Name { get { return name; } }//IMap
        public byte Level; //When the party is in a sector on a certain level, only other sectors on the same level are visible on the world map.
        //long DataPos;
        ushort[,] _Terrain;
        public bool[,] Explored;
        //bool[,] _Visible;
        public eMapOutExtraBit[,] MapExtra; //Stores rasterized info for secret passages and town entrances
        public ushort this[int x, int y] { get { /*if (x >= 0 && x < Width && y >= 0 && y < Height)*/ return _Terrain[x, y];
        //else return 0;
        }
            set { _Terrain[x, y] = (ushort)value; }
        } //IMap
        //public bool Visible(Location loc)
        //{
        //    if (inBounds(loc) && _Visible[loc.x, loc.y]) return true; return false;
        //}
        bool inBounds(Location loc)
        {
            if (loc.X >= 0 && loc.X < Width && loc.Y > 0 && loc.Y <= Height) return true; return false;
        }
        public int CanSee(Location l1, Location l2, int mode)
        {
            return 0; //TerrainRecord.CanSeeTerrain(_Terrain, l1, l2, mode);
        }

        //public List<SpecialNode> SpecialNodeList { get { return specialNodeList; } }
        //List<SpecialNode> specialNodeList = new List<SpecialNode>();
        //public List<Sign> SignList = new List<Sign>();
        public Location SectorPos;
        public OutsideSector[,] Neighbour = new OutsideSector[3, 3];
        public List<TriggerSpot> TriggerSpotList = new List<TriggerSpot>();
        public List<TownEntrance> TownEntranceList = new List<TownEntrance>();
        public List<InfoRect> InfoRectList = new List<InfoRect>();
        //public List<NPCGroupRecord> WanderingGroupList = new List<NPCGroupRecord>();
        public List<Location> SpawnPointList = new List<Location>();
        //public List<NPCGroupRecord> SpecialGroupList = new List<NPCGroupRecord>();

        public List<EncounterRecord> WanderingGroupList = new List<EncounterRecord>();

        public OutsideSector() { }
        public void Load(BinaryReader In)
        {
            //Just loads the sector header
            //DataPos = In.ReadInt64();
            SectorPos = new Location(In.ReadInt16(), In.ReadInt16()); //Must be positive!
            In.ReadString(); //Folder: ignored
            name = In.ReadString();
            List.Add(this);
        }

        public TownEntrance TownEntranceHere(Location pos, bool regardless_of_hidden = false)
        {
            foreach (TownEntrance e in TownEntranceList)
            {
                if (e.DestTown == null) continue;
                if (e.Pos == pos && (!e.DestTown.Hidden || regardless_of_hidden)) return e;//.DestTown;
            }
            return null;
        }

        public void SetTrigger(Location pos, bool activate)
        {
            foreach (TriggerSpot ts in TriggerSpotList)
            {
                if (ts.Pos == pos) ts.Active = activate;
            }
        }

        public void LoadFull(BinaryReader In)
        {
            int x, y, num;

            //In.BaseStream.Seek(DataPos, SeekOrigin.Begin);

            Width = Constants.SECTOR_WIDTH;
            Height = Constants.SECTOR_HEIGHT;

            In.ReadString(); //Default script file - only used in the editor
            Level = In.ReadByte();

            _Terrain = new ushort[Width, Height];
            for (x = 0; x < Width; x++)
                for (y = 0; y < Height; y++)
                    _Terrain[x, y] = In.ReadUInt16();//In.ReadByte();
            Explored = new bool[Width, Height];
            MapExtra = new eMapOutExtraBit[Width, Height];

            //num = In.ReadInt16();
            //for (x = 0; x < num; x++) SpecialNodeList.Add(new SpecialNode());
            //for (x = 0; x < num; x++) SpecialNodeList[x].Load(SpecialNodeList, In);

            num = In.ReadInt16();
            for (x = 0; x < num; x++)
                TriggerSpotList.Add(new TriggerSpot(In));

            num = In.ReadInt16();
            for (x = 0; x < num; x++)
            {
                Location l = In.ReadLocation();
                MapExtra[l.X, l.Y] = eMapOutExtraBit.SECRET;
            }

            num = In.ReadInt16();
            for (x = 0; x < num; x++)
            {
                var te = new TownEntrance(In, this);
                MapExtra[te.Pos.X, te.Pos.Y] |= eMapOutExtraBit.ENTRANCE;
                TownEntranceList.Add(te);
            }

            //num = In.ReadInt16();
            //for (x = 0; x < num; x++)
            //    SignList.Add(new Sign(In));

            num = In.ReadInt16();
            for (x = 0; x < num; x++)
                InfoRectList.Add(new InfoRect(In));

            //num = In.ReadInt16();
            //for (x = 0; x < num; x++)
            //    WanderingGroupList.Add(new NPCGroupRecord(In));

            //Load the list of wandering groups that can spawn in this sector
            string s;
            while ((s = In.ReadString()) != "")
            {
                var ng = EncounterRecord.List[s];
                if (ng != null)
                    WanderingGroupList.Add(ng);
            }

            num = In.ReadInt16();
            for (x = 0; x < num; x++)
                SpawnPointList.Add(In.ReadLocation());

            //num = In.ReadInt16();
            //for (x = 0; x < num; x++)
            //    SpecialGroupList.Add(new NPCGroupRecord(In));

            //Set all the neighbouring sector shortcuts.
            //for (x = -1; x <= 1; x++)
            //    for (y = -1; y <= 1; y++)
            //        Neighbour[x + 1, y + 1] = SectorAt(SectorPos.x + x, SectorPos.y + y);

            //Loaded = true;
        }


        //public static OutsideSector SectorAt(int x, int y) {
        //    foreach (OutsideSector o in Scenario.OutsideSectors)
        //        if (o.SectorPos.x == x && o.SectorPos.y == y) return o;
        //    return null;
       // }

        public string GetInfoRectString(Location pos)
        {
            foreach (InfoRect i in InfoRectList)
            {
                if (i.Rect.LocIn(pos))
                    return i.Text;
            }
            return null;
        }

        //public bool TerrainBlocked(Location pos)
        //{
        //    ushort ter = _Terrain[pos.x, pos.y];//(is_town()) ? t_d.terrain[to_check.x][to_check.y] : combat_terrain[to_check.x][to_check.y];                
        //    int gr = TerrainRecord.List[ter].picture;

        //    if (TerrainRecord.List[ter].Blockage > eBlock.CLEAR_WALK_PC) return true;
        //    return false;
        //}

        public ICharacter CharacterThere(Location pos)
        {
            if (Party.OutsidePos == pos) return Party.LeaderPC;
            return null;
        }

        public Boolean CharacterCanBeThere(Location loc, ICharacter m_num, bool allow_leave_map = false)
        {
            return true;
        }

        public Location GetTileAtMouse(MouseState ms)
        {
            return Location.Zero;
        }

        public string GetToolTipMessage(Location loc)
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine("You see:");
            sb.AppendLine("");
            //First the terrain.
            sb.AppendLine(TerrainRecord.UnderlayList[_Terrain[loc.X, loc.Y]].Name);
            return sb.ToString();
        }

        /// <summary>
        /// Dropping an item outside means it goes away forever.
        /// </summary>
        /// <param name="item">Item to place. Make sure it is removed from wherever it was first.</param>
        /// <param name="ch">Only PCs can drop outside</param>
        public bool DropItem(Item item, Location pos)
        {
            //if (ch is PCType)
            //{
            //    //TODO: When dropping item outside, ask player if they really want the item gone forever.
            //    return true;
            //}
            return false;
        }

        //public Sign SignAtLoc(Location loc)
        //{
        //    return SignList.Find(n => n.Pos == loc);
        //}

        //public void RemoveSpecialNodeDots()
        //{
        //}

        //public bool TriggerStepOnSpecials(Location pos, Direction dir, PCType pc)
        //{
        //    return false;
        //}

        //public bool PCCanTryToWalkThere(Location pos, PCType pc)
        //{
        //    return true;
        //}

    }

}
