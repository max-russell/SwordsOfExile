using System.Collections.Generic;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

public class Field
{
    public static uint ObscurityMask;

    public string Name;
    public int Index;
    public uint Bit;
    private XnaRect rect;
    public bool Animated;
    public int Obscurity;

    //Constructor for visible fields (representing real things in the game world)
    public Field(int num, string name, uint bit, int sx, int sy, int obscurity = 0, bool animated = false)
    {
        if (num is 4 or 5) BarrierList.Add(this);

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

    public static Field[] List = new Field[27];//{
    public static List<Field> VisibleList = new();
    public static List<Field> ObscuringList = new();
    public static List<Field> BarrierList = new();

    public static Field

        //These are the non-visible fields
        LIGHT = new(25, 0x100),
        SPECIAL = new(26, 0x2),
        SECRET_PASSAGE = new(22, 0x1),
        CRATE_MOVE = new(23, 0x1000000),
        FIELD_APPEAR = new(24, 0x2000000),

        //These should be in the order they are drawn to screen - later ones are drawn on top
        //(this is because they are added to the VisibleList in this order)
        CRATER = new(19, "Crater", 2097152, 5, 3),
        SMALL_BLOOD = new(14, "Bloodstain", 65536, 0, 3),//15
        MEDIUM_BLOOD = new(15, "Bloodstain", 131072, 1, 3),
        LARGE_BLOOD = new(16, "Bloodstain", 262144, 2, 3),
        SMALL_SLIME = new(17, "Slime", 524288, 3, 3),
        LARGE_SLIME = new(18, "Slime", 1048576, 4, 3),
        BONES = new(20, "Bones", 4194304, 6, 3),
        ROCKS = new(21, "Rocks", 8388608, 7, 3),
        BARREL = new(2, "Barrel", 16, 7, 0, 1),
        CRATE = new(3, "Crate", 8, 6, 0, 1),
        WEB = new(1, "Web", 4, 5, 0, 2),
        FORCE_WALL = new(6, "Force wall", 512, 0, 1),
        FIRE_WALL = new(7, "Fire wall", 1024, 1, 1),
        SLEEP_CLOUD = new(13, "Sleep cloud", 32768, 6, 1),
        STINK_CLOUD = new(9, "Stink cloud", 4096, 3, 1),
        ICE_WALL = new(10, "Ice wall", 8192, 4, 1),
        BLADE_WALL = new(11, "Blade wall", 16384, 5, 1),
        ANTIMAGIC = new(8, "Antimagic cloud", 2048, 2, 1),
        QUICKFIRE = new(12, "Quickfire", 128, 7, 1),
        FIRE_BARRIER = new(4, "Fire barrier", 32, 0, 2, 255, true),
        FORCE_BARRIER = new(5, "Force barrier", 64, 0, 2, 255, true);
}