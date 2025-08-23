using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using Microsoft.Xna.Framework.Input;


namespace SwordsOfExileGame;

public class OutsideSector: IListEntity
{
    public static ExileList<OutsideSector> List = new();
    public string ID { get => SectorPos.X + ", " + SectorPos.Y;
        set { } }

    private PartyType Party => Game.CurrentParty;

    public int Width, Height;
    public string Name { get; private set; }

    public byte Level; //When the party is in a sector on a certain level, only other sectors on the same level are visible on the world map.
    private ushort[,] _Terrain;
    public bool[,] Explored;
    public eMapOutExtraBit[,] MapExtra; //Stores rasterized info for secret passages and town entrances
    public ushort this[int x, int y] 
    { 
        get => _Terrain[x, y];
        set => _Terrain[x, y] = (ushort)value;
    }

    private bool inBounds(Location loc)
    {
        if (loc.X >= 0 && loc.X < Width && loc.Y > 0 && loc.Y <= Height) return true; return false;
    }
    public int CanSee(Location l1, Location l2, int mode)
    {
        return 0; 
    }

    public Location SectorPos;
    public OutsideSector[,] Neighbour = new OutsideSector[3, 3];
    public List<TriggerSpot> TriggerSpotList = new();
    public List<TownEntrance> TownEntranceList = new();
    public List<InfoRect> InfoRectList = new();
    public List<Location> SpawnPointList = new();

    public List<EncounterRecord> WanderingGroupList = new();

    public OutsideSector() { }
    public void Load(BinaryReader In)
    {
        //Just loads the sector header
        SectorPos = new Location(In.ReadInt16(), In.ReadInt16()); //Must be positive!
        In.ReadString(); //Folder: ignored
        Name = In.ReadString();
        List.Add(this);
    }

    public TownEntrance TownEntranceHere(Location pos, bool regardless_of_hidden = false)
    {
        foreach (var e in TownEntranceList)
        {
            if (e.DestTown == null) continue;
            if (e.Pos == pos && (!e.DestTown.Hidden || regardless_of_hidden)) return e;//.DestTown;
        }
        return null;
    }

    public void SetTrigger(Location pos, bool activate)
    {
        foreach (var ts in TriggerSpotList)
        {
            if (ts.Pos == pos) ts.Active = activate;
        }
    }

    public void LoadFull(BinaryReader In)
    {
        int x, y, num;
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

        num = In.ReadInt16();
        for (x = 0; x < num; x++)
            TriggerSpotList.Add(new TriggerSpot(In));

        num = In.ReadInt16();
        for (x = 0; x < num; x++)
        {
            var l = In.ReadLocation();
            MapExtra[l.X, l.Y] = eMapOutExtraBit.SECRET;
        }

        num = In.ReadInt16();
        for (x = 0; x < num; x++)
        {
            var te = new TownEntrance(In, this);
            MapExtra[te.Pos.X, te.Pos.Y] |= eMapOutExtraBit.ENTRANCE;
            TownEntranceList.Add(te);
        }

        num = In.ReadInt16();
        for (x = 0; x < num; x++)
            InfoRectList.Add(new InfoRect(In));

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
    }

    public string GetInfoRectString(Location pos)
    {
        foreach (var i in InfoRectList)
        {
            if (i.Rect.LocIn(pos))
                return i.Text;
        }
        return null;
    }

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
        var sb = new StringBuilder();
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
        return false;
    }
}