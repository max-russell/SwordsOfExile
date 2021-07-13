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

    public class Field
    {
        public static uint ObscurityMask;

        public string Name;
        public int Index;
        public uint Bit;
        XnaRect rect;
        public bool Animated;
        public int Obscurity;

        //Constructor for visible fields (representing real things in the game world)
        public Field(int num, string name, uint bit, int sx, int sy, int obscurity = 0, bool animated = false)
        {
            if (num == 4 || num == 5) BarrierList.Add(this);

            VisibleList.Add(this);
            Index = num;
            List[num] = this;
            Name = name; Bit = bit; Animated = animated; //F = f;
            rect = new XnaRect(sx * Gfx.SRCTILEWIDTH, sy * Gfx.SRCTILEHEIGHT, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
            Obscurity = obscurity;

            if (Obscurity != 0)
            {
                ObscurityMask |= Bit;
                ObscuringList.Add(this);
            }
        }

        public XnaRect GetSrcRect()
        {
            if (Animated)
                return new XnaRect(rect.X + Game.AnimTicks * Gfx.SRCTILEWIDTH, rect.Y, rect.Width, rect.Height);
            else
                return rect;
        }

        //Constructor for invisible fields (for game mechanics)
        public Field(int num, uint bit)
        {
            Obscurity = 0;
            Index = num;
            List[num] = this;
            Bit = bit;
        }

        //public static FieldRecord GetRecord(eField f)
        //{
        //    foreach (FieldRecord r in List)
        //        if (r.F == f) return r;
        //    return null;
        //}

        public static Field[] List = new Field[27];//{
        public static List<Field> VisibleList = new List<Field>();
        public static List<Field> ObscuringList = new List<Field>();
        public static List<Field> BarrierList = new List<Field>();

        public static Field

            //These are the non-visible fields
            LIGHT = new Field(25, 0x100),
            SPECIAL = new Field(26, 0x2),
            SECRET_PASSAGE = new Field(22, 0x1),
            CRATE_MOVE = new Field(23, 0x1000000),
            FIELD_APPEAR = new Field(24, 0x2000000),

            //These should be in the order they are drawn to screen - later ones are drawn on top
            //(this is because they are added to the VisibleList in this order)
            CRATER = new Field(19, "Crater", 2097152, 5, 3),
            SMALL_BLOOD = new Field(14, "Bloodstain", 65536, 0, 3),//15
            MEDIUM_BLOOD = new Field(15, "Bloodstain", 131072, 1, 3),
            LARGE_BLOOD = new Field(16, "Bloodstain", 262144, 2, 3),
            SMALL_SLIME = new Field(17, "Slime", 524288, 3, 3),
            LARGE_SLIME = new Field(18, "Slime", 1048576, 4, 3),
            BONES = new Field(20, "Bones", 4194304, 6, 3),
            ROCKS = new Field(21, "Rocks", 8388608, 7, 3),
            BARREL = new Field(2, "Barrel", 16, 7, 0, 1),
            CRATE = new Field(3, "Crate", 8, 6, 0, 1),
            WEB = new Field(1, "Web", 4, 5, 0, 2),
            FORCE_WALL = new Field(6, "Force wall", 512, 0, 1),
            FIRE_WALL = new Field(7, "Fire wall", 1024, 1, 1),
            SLEEP_CLOUD = new Field(13, "Sleep cloud", 32768, 6, 1),
            STINK_CLOUD = new Field(9, "Stink cloud", 4096, 3, 1),
            ICE_WALL = new Field(10, "Ice wall", 8192, 4, 1),
            BLADE_WALL = new Field(11, "Blade wall", 16384, 5, 1),
            ANTIMAGIC = new Field(8, "Antimagic cloud", 2048, 2, 1),
            QUICKFIRE = new Field(12, "Quickfire", 128, 7, 1),
            FIRE_BARRIER = new Field(4, "Fire barrier", 32, 0, 2, 255, true),
            FORCE_BARRIER = new Field(5, "Force barrier", 64, 0, 2, 255, true);
    }

}