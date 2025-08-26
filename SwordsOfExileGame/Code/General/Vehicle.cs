using System;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

public class Vehicle : IListEntity, IAnimatable
{
    public static ExileList<Vehicle> List = new();

    public string ID { get; set; }

    public eVehicleType Type;
    public Location Pos { get; set; }

    public IMap Map;
    public bool PartyOwns;
    public Direction Dir;

    public bool NotDrawn { get; set; } = false; //Temporarily don't draw (used in teleporting animations)

    public string Name { get { if (Type == eVehicleType.HORSE) return "horses"; else if (Type == eVehicleType.BOAT) return "boat"; else return "vehicle"; } }
    public string BoardMessage() { if (Type == eVehicleType.HORSE) return "You mount the horses."; else return "You board the boat."; }
    public string LeaveMessage() { if (Type == eVehicleType.HORSE) return "You dismount."; else return "You disembark."; }

    public void LoadGame(BinaryReader file)
    {
        Pos = file.ReadLocation();
        var d = file.ReadInt32();
        if (d == -1)
            Map = Game.WorldMap;
        else
            Map = TownMap.List[d];
        PartyOwns = file.ReadBoolean();
        Dir = file.ReadDirection();
    }

    public void SaveGame(BinaryWriter file)
    {
        file.Write(Pos);
        if (Map is WorldMapType)
            file.Write(-1);
        else
            file.Write(((TownMap)Map).Num);//   ((TownMap)Map).ID);
        file.Write(PartyOwns);
        file.Write(Dir);
    }

    public Vehicle() { }
    public void Load (BinaryReader In)
    {
        ID = In.ReadString();
        In.ReadString(); //Editor Folder (disregard)
        Type = (eVehicleType)In.ReadByte();

        var m = In.ReadString();

        if (m == "")
            Map = Game.WorldMap;
        else
        {
            TownMap town;
            if (!TownMap.List.TryGetValue(m, out town))
                Map = (TownMap)TownMap.List[0];
            else
                Map = town;
        }
        Pos = In.ReadLocation();
        PartyOwns = !In.ReadBoolean();

        Dir = new Direction(eDir.E);
        List.Add(this);
    }

    public void Draw(SpriteBatch sb, XnaRect dr)
    {
        var tex = Gfx.MixedGfx;
        XnaRect sr;
        float rot = 0;
        var col = Color.White;

        if (AnimAction != null)
            AnimAction.AdjustCharRect(ref dr, ref rot, ref col);
        if (AnimFlash != null)
            AnimFlash.AdjustCharRect(ref dr, ref rot, ref col);

        if (Type == eVehicleType.BOAT)
        {
            sr = Dir.IsFacingRight ? new XnaRect(117, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT)
                : new XnaRect(89, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
        }
        else //Horse
        {
            sr = Dir.IsFacingRight ? new XnaRect(117, 110, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT)
                : new XnaRect(145, 110, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
            if (Game.CurrentParty.Vehicle == this)
            {
                sr.X -= Gfx.CHARGFXWIDTH * 2;
                sr.Y -= Gfx.CHARGFXHEIGHT;
            }
        }
        sb.Draw(tex, dr, sr, Color.White);
    }

    public IAnimCharacter AnimAction { get; set; }

    public IAnimCharacter AnimFlash { get; set; }

    public void FinishDying()
    {
        List.Remove(this);
    }

    public bool IsVisible()
    {
        return Map == Game.CurrentMap && Map.Visible(Pos);
    }

    public static Vehicle IsThere(IMap where, Location l, eVehicleType specific_type = eVehicleType.NONE)
    {
        foreach (var hb in List)
            if (hb.Map == where && hb.Pos == l && (specific_type == eVehicleType.NONE || specific_type == hb.Type))
                return hb;
        return null;
    }

}