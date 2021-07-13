using System;
using System.IO;
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
    public class Vehicle : IListEntity, IAnimatable
    {
        public static ExileList<Vehicle> List = new ExileList<Vehicle>();

        public string ID { get { return id; } set { id = value; } }
        string id;
        public eVehicleType Type;
        Location pos;
        public Location Pos { get { return pos; } set { pos = value; } }
        public IMap Map;
        public Boolean PartyOwns;
        public Direction Dir;

        public bool NotDrawn { get { return notDrawn; } set { notDrawn = value; } } //Temporarily don't draw (used in teleporting animations)
        bool notDrawn = false;

        public string Name { get { if (Type == eVehicleType.HORSE) return "horses"; else if (Type == eVehicleType.BOAT) return "boat"; else return "vehicle"; } }
        public string BoardMessage() { if (Type == eVehicleType.HORSE) return "You mount the horses."; else return "You board the boat."; }
        public string LeaveMessage() { if (Type == eVehicleType.HORSE) return "You dismount."; else return "You disembark."; }

        //public static RECT[] boat_rects = { new RECT(0, 0, 28, 36), new RECT(28, 0, 56, 36), new RECT(56, 0, 84, 36), new RECT(84, 0, 112, 36) };

        //public static void Load(BinaryReader In)
        //{
        //    List.Clear();

        //    while (true)
        //    {
        //        byte b = In.ReadByte();

        //        if (b == 0) break;

        //        if (b == 1)
        //            new Vehicle(In);
        //        else if (b == 2)
        //            Scenario.LoadAndDisregardEditorFolder(In);
        //    }
        //}

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
            id = In.ReadString();
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
            pos = In.ReadLocation();
            PartyOwns = !In.ReadBoolean();

            Dir = new Direction(eDir.E);
            List.Add(this);
        }

        public void Draw(SpriteBatch sb, XnaRect dr)
        {
            Texture2D tex = Gfx.MixedGfx;
            XnaRect sr;
            float rot = 0;
            Color col = Color.White;

            if (animAction != null)
                animAction.AdjustCharRect(ref dr, ref rot, ref col);
            if (animFlash != null)
                animFlash.AdjustCharRect(ref dr, ref rot, ref col);

            if (Type == eVehicleType.BOAT)
            {
                sr = Dir.IsFacingRight ? new XnaRect(117, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT)
                                       : new XnaRect(89, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
                //sb.Draw(tex, dr, sr, Color.White);
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

        IAnimCharacter animAction;
        public IAnimCharacter AnimAction { get { return animAction; } set { animAction = value; } }
        IAnimCharacter animFlash;
        public IAnimCharacter AnimFlash { get { return animFlash; } set { animFlash = value; } }

        public void FinishDying()
        {
            List.Remove(this);
        }

        public bool IsVisible()
        {
            return Map == Game.CurrentMap && Map.Visible(pos);
        }

        //public static HorseBoat LoadNew(System.IO.BinaryReader In)
        //{
        //    HorseBoat h = new HorseBoat();
        //    h.Pos.x = In.ReadSByte();
        //    h.Pos.y = In.ReadSByte();
        //    h.loc_in_sec.x = In.ReadSByte();
        //    h.loc_in_sec.y = In.ReadSByte();
        //    h.sector.x = In.ReadSByte();
        //    h.sector.y = In.ReadSByte();
        //    h.which_town = BoE.ReadShort(In);
        //    h.Exists = In.ReadBoolean();
        //    h.Property = In.ReadBoolean();
        //    if (h.which_town == -1) return null;
        //    return h;
        //}

        public static Vehicle IsThere(IMap where, Location l, eVehicleType specific_type = eVehicleType.NONE)
        {

            foreach (Vehicle hb in List)
                if (hb.Map == where && hb.Pos == l && (specific_type == eVehicleType.NONE || specific_type == hb.Type))
                    return hb;
            //
            //                    if (place is OutsideSector && place == hb.sector && hb.loc_in_sec == l) return hb;
            //                    else if (place is TownMap && place == hb.Town && hb.Pos == l) return hb;
            //            }
            return null;

        }

    }
}