using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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
    //public class Action
    //{
    //    public static eAction Requested;
    //    public static PCType PC, PC2; //For when Action.Requested is an action concerning a PC
    //    public static NPCType NPC;
    //    public static Direction Dir;
    //    public static Item Item; //For when Action.Requested is an action concerning an item.
    //    public static Location Loc;
    //    public static IInventory InventoryTo, InventoryFrom;
    //    public static eEquipSlot EquipSlot;
    //    public static MagicSpell Spell;
    //    public static eItemFilter FilterTo;
    //    public static List<Location> TargetList;
    //}

    public static class Colour
    {
        public static Color FromRGB(byte r, byte g, byte b)
        {
            return new Color(r, g, b);
        }
    }

    public struct Location
    {
        public int X, Y;

        public Location(int lx, int ly) { X = lx; Y = ly; }

        public static Location Zero { get { return new Location(0, 0); } }

        //public static Location Read(BinaryReader In) {
        //    return new Location(In.ReadInt16(), In.ReadInt16());
        //}
        public override int GetHashCode() { return base.GetHashCode(); }

        public override bool Equals(object obj)
        {

            if ((obj is Location) && (((Location)obj) == this)) return true;
            return false;
        }

        public static bool operator ==(Location l1, Location l2)
        {
            return l1.X == l2.X && l1.Y == l2.Y;
        }
        public static bool operator !=(Location l1, Location l2)
        {
            return !(l1.X == l2.X && l1.Y == l2.Y);
        }

        public static Location operator +(Location l1, Location l2)
        {
            return new Location(l1.X + l2.X, l1.Y + l2.Y);
        }

        public static Location operator -(Location l1, Location l2)
        {
            return new Location(l1.X - l2.X, l1.Y - l2.Y);
        }

        public static Location operator *(Location l1, int m)
        {
            return new Location(l1.X * m, l1.Y * m);
        }

        public Microsoft.Xna.Framework.Vector2 ToVector2() { return new Microsoft.Xna.Framework.Vector2(X, Y); }

        public bool Inside(int left, int top, int right, int bottom)
        {
            if (X >= left && X < right && Y >= top && Y < bottom) return true; else return false;
        }

        public bool Inside(XnaRect r)
        {
            return X >= r.X && X < r.X + r.Width && Y >= r.Y && Y < r.Y + r.Height;
        }

        public Location Mod(int mx, int my)
        {
            return new Location(X + mx, Y + my);
        }

        public Location Mod(eDir dir, int amount = 1)
        {
            switch (dir)
            {
                case eDir.E: return new Location(X + amount, Y);
                case eDir.W: return new Location(X - amount, Y);
                case eDir.N: return new Location(X, Y - amount);
                case eDir.S: return new Location(X + amount, Y);
                case eDir.NE: return new Location(X + amount, Y - amount);
                case eDir.NW: return new Location(X - amount, Y - amount);
                case eDir.SW: return new Location(X - amount, Y + amount);
                case eDir.SE: return new Location(X + amount, Y + amount);
            }
            return this;
        }

        public int DistanceTo(Location l)
        {
            return (int)Math.Sqrt((double)((X - l.X) * (X - l.X) +
                        (Y - l.Y) * (Y - l.Y)));
        }

        public int VDistanceTo(Location p2)
        {
            int i, j;
            i = Math.Abs(X - p2.X);
            j = Math.Abs(Y - p2.Y);
            return Math.Max(i, j);
        }

        public eDir DirectionTo(Location l)
        { //was set_direction
            if (X == l.X)
                if (Y > l.Y)
                    return eDir.N;
                else if (Y < l.Y)
                    return eDir.S;
                else
                    return eDir.None;
            if (X > l.X)
            {
                if (Y > l.Y)
                    return eDir.NW;
                if (Y < l.Y)
                    return eDir.SW;
                return eDir.W;
            }
            if (Y > l.Y)
                return eDir.NE;
            if (Y < l.Y)
                return eDir.SE;
            return eDir.E;
        }

        //public RECT ToScreenRect(int width, int height) {
        //    Location where_put = new Location();
        //    where_put.x = 4 + x - GameScreen.center.x;
        //    where_put.y = 4 + y - GameScreen.center.y;

        //    return new RECT(18 + where_put.x * 28, 18 + where_put.y * 36,
        //        46 + where_put.x * 28 + 28 * (width - 1), 54 + where_put.y * 36 + 36 * (height - 1));
        //}

        //public Boolean OnScreen(Location center)
        //{
        //    return (Math.Abs(center.x - x) <= 4) && (Math.Abs(center.y - y) <= 4);
        //}

        public bool adjacent(Location l)
        {
            return Math.Abs(X - l.X) <= 1 && Math.Abs(Y - l.Y) <= 1;
        }

        /* functions */
        //public location toGlobal();		/* convert local coordinates to global*/
        //public Location toLocal() {
        //    Location l = new Location(x, y);
        //    if (BoE.Party.i_w_c.x == 1) l.x = l.x - 48;
        //    if (BoE.Party.i_w_c.y == 1) l.y = l.y - 48;
        //    return l;
        //}/* convert global coordinates to local*/
        public Location randomShift()
        {
            Location store;

            store.X = X + Maths.Rand(1, 0, 2) - 1;
            store.Y = Y + Maths.Rand(1, 0, 2) - 1;

            return store;
        }

        public float GetAngle(Location b)
        {
            return (float)Math.Atan2(b.Y - Y, b.X - X);
        }

    }

    public struct Rectangle
    {
        public int Left, Top, Right, Bottom;
        public Rectangle(int l, int t, int r, int b) { Left = l; Top = t; Right = r; Bottom = b; }

        public static Rectangle Read(BinaryReader In)
        {
            return new Rectangle(In.ReadInt16(), In.ReadInt16(), In.ReadInt16(), In.ReadInt16());
        }

        public int Width
        {
            get
            {
                return (Right - Left) + 1;
            }
            set
            {
                Right = (Left + value) - 1;
            }
        }
        public int Height
        {
            get
            {
                return (Bottom - Top) + 1;
            }
            set
            {
                Bottom = (Top + value) - 1;
            }
        }



        public Rectangle Offset(int dx, int dy)
        {
            Left += dx;
            Top += dy;
            Right += dx;
            Bottom += dy;
            return this;
        }
        public void Inflate(int dx, int dy)
        {
            Left -= dx;
            Top -= dy;
            Right += dx;
            Bottom += dy;
        }
        public void Intersect(Rectangle r1, Rectangle r2)
        {
            Left = r1.Left > r2.Left ? r1.Left : r2.Left;
            Top = r1.Top > r2.Top ? r1.Top : r2.Top;
            Right = r1.Right < r2.Right ? r1.Right : r2.Right;
            Bottom = r1.Bottom < r2.Bottom ? r1.Bottom : r2.Bottom;

            if (Right < Left || Bottom < Top) { Left = 0; Top = 0; Right = 0; Bottom = 0; }
        }

        public bool LocIn(Location l)
        {
            return l.X >= Left && l.X <= Right && l.Y >= Top && l.Y <= Bottom;
        }
    }

    public struct Direction
    {
        public static Direction None { get { return new Direction(); } }
        public static Direction Random() { return new Direction((eDir)Maths.Rnd.Next(0, 8)); }
        static eDir[,] dirs = { { eDir.NW, eDir.W, eDir.SW }, { eDir.N, eDir.None, eDir.S }, { eDir.NE, eDir.E, eDir.SE } };

        public Direction(eDir d, bool right = true)
        {
            dir = d;
            facingRight = right;
            setFacing();
        }
        public Direction(Location mod)
        {
            dir = dirs[mod.X + 1, mod.Y + 1];
            facingRight = true;
            setFacing();
        }
        public Direction(Location l1, Location l2)
        {

            Location mod = l2 - l1;
            mod.X = Math.Sign(mod.X);
            mod.Y = Math.Sign(mod.Y);
            dir = dirs[mod.X + 1, mod.Y + 1];
            facingRight = true;
            setFacing();
        }
        public int CardinalDir
        {
            get
            {
                switch (dir)
                {
                    case eDir.N:
                    case eDir.NW: return 0;
                    case eDir.W:
                    case eDir.SW: return 1;
                    case eDir.S:
                    case eDir.SE: return 2;
                    default: return 3;
                }
            }
        }
        public bool IsFacingRight
        {
            get { return facingRight; }
        }
        public bool IsNorth { get { return dir == eDir.N; } }
        public bool IsSouth { get { return dir == eDir.S; } }
        public bool IsEast { get { return dir == eDir.E; } }
        public bool IsWest { get { return dir == eDir.W; } }
        public bool IsNorthWest { get { return dir == eDir.NW; } }
        public bool IsNorthEast { get { return dir == eDir.NE; } }
        public bool IsSouthWest { get { return dir == eDir.SW; } }
        public bool IsSouthEast { get { return dir == eDir.SE; } }

        public override string ToString()
        {
            switch (dir)
            {
                case eDir.N: return "North";
                case eDir.S: return "South";
                case eDir.E: return "East";
                case eDir.W: return "West";
                case eDir.NW: return "North-West";
                case eDir.NE: return "North-East";
                case eDir.SW: return "South-West";
                case eDir.SE: return "South-East";
            }
            return "";
        }

        eDir dir;
        public eDir Dir
        {
            set
            {
                dir = value;
                setFacing();
            }
            get
            {
                return dir;
            }
        }

        void setFacing()
        {
            if (dir == eDir.NE || dir == eDir.E || dir == eDir.SE) facingRight = true;
            else if (dir == eDir.NW || dir == eDir.W || dir == eDir.SW) facingRight = false;
        }

        bool facingRight;

        public void FaceTowards(Location here, Location there)
        {
            Location mod = there - here;
            mod.X = Math.Sign(mod.X);
            mod.Y = Math.Sign(mod.Y);
            dir = dirs[mod.X + 1, mod.Y + 1];
            setFacing();
        }

        public eDir OppDir
        {
            get
            {
                switch (dir)
                {
                    case eDir.N: return eDir.S;
                    case eDir.S: return eDir.N;
                    case eDir.E: return eDir.W;
                    case eDir.W: return eDir.E;
                    case eDir.NW: return eDir.SE;
                    case eDir.NE: return eDir.SW;
                    case eDir.SW: return eDir.NE;
                    case eDir.SE: return eDir.NW;
                }
                return eDir.None;
            }
        }

        public int DirModX(int amount = 1)
        {
            switch (dir)
            {
                case eDir.N:
                case eDir.S: return 0 * amount;
                case eDir.E:
                case eDir.NE:
                case eDir.SE: return 1 * amount;
                case eDir.W:
                case eDir.NW:
                case eDir.SW: return -1 * amount;
            }
            return 0;
        }

        public int DirModY(int amount = 1)
        {
            switch (dir)
            {
                case eDir.E:
                case eDir.W: return 0 * amount;
                case eDir.N:
                case eDir.NE:
                case eDir.NW: return -1 * amount;
                case eDir.S:
                case eDir.SW:
                case eDir.SE: return 1 * amount;
            }
            return 0;
        }

        public eAction ToAction()
        {
            switch (dir)
            {
                case eDir.N: return eAction.Up;
                case eDir.S: return eAction.Down;
                case eDir.E: return eAction.Right;
                case eDir.NE: return eAction.UpRight;
                case eDir.SE: return eAction.DownRight;
                case eDir.W: return eAction.Left;
                case eDir.NW: return eAction.UpLeft;
                case eDir.SW: return eAction.DownLeft;
                case eDir.None: return eAction.StandReady;
            }
            return eAction.StandReady;
        }
        public eCursor ToCursor()
        {
            switch (dir)
            {
                case eDir.N: return eCursor.N;
                case eDir.S: return eCursor.S;
                case eDir.E: return eCursor.E;
                case eDir.NE: return eCursor.NE;
                case eDir.SE: return eCursor.SE;
                case eDir.W: return eCursor.W;
                case eDir.NW: return eCursor.NW;
                case eDir.SW: return eCursor.SW;
                case eDir.None: return eCursor.WAIT;
            }
            return eCursor.WAIT;
        }

        static public Location operator +(Location l, Direction d)
        {
            return new Location(l.X + d.DirModX(), l.Y + d.DirModY());
        }
    }

}