using System;
using System.Collections.Generic;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal static class StartupMap
{
    private static bool startupMapLoaded = false;

    private static List<int> startupmapTerrains, startupmapTerrainsO;
    private static ushort[,] startupMap;
    private static int startupMapW, startupMapH;
    private static Vector2 smScroll;
    private static double Angle = 0d;

    public static void Load()
    {
        startupMapLoaded = false;

        startupmapTerrains = new List<int>();
        startupmapTerrainsO = new List<int>();
        startupMap = null;

        var mapdir = Path.Combine(Game.BaseDirectory, "Data", "StartupMap.dat");

        if (!File.Exists(mapdir)) return;// false;

        using (var fs = new FileStream(mapdir, FileMode.Open, FileAccess.Read))
        using (var file = new BinaryReader(fs))
        {
            int m = file.ReadInt16();
            for (var n = 0; n < m; n++)
                startupmapTerrains.Add(file.ReadInt16());

            m = file.ReadInt16();
            for (var n = 0; n < m; n++)
                startupmapTerrainsO.Add(file.ReadInt16());


            startupMapW = file.ReadInt32();
            startupMapH = file.ReadInt32();

            startupMap = new ushort[startupMapW, startupMapH];

            for (var y = 0; y < startupMapH; y++)
            for (var x = 0; x < startupMapW; x++)
                startupMap[x, y] = file.ReadUInt16();
        }
        startupMapLoaded = true;
        smScroll = new Vector2(Maths.Rand(1,0,startupMapW-1)+startupMapW, Maths.Rand(1,0,startupMapH-1)+startupMapH);// new Vector2(startupMapW, startupMapH);//Vector2.Zero;
        Angle = new Random().NextDouble() * Math.PI * 2;
    }

    public static void Draw(SpriteBatch sb)
    {
        if (!startupMapLoaded) return;

        //VW, VH: Screen Width and Height in tiles at current zoom size
        double VW = (float)Gfx.WinW / Gfx.DEFAULTZOOM; 
        double VH = (float)Gfx.WinH / Gfx.DEFAULTZOOM;

        //Position in tiles at top left of screen for current scroll position
        double bx = smScroll.X - VW / 2d,
            by =  smScroll.Y - VH / 2d;

        double offx = (int)(  (bx * Gfx.DEFAULTZOOM) - (int)bx * Gfx.DEFAULTZOOM);
        double offy = (int)(  (by * Gfx.DEFAULTZOOM) - (int)by * Gfx.DEFAULTZOOM);

        var sx = (int)bx;
        var sy = (int)by;
        var tw = (int)(smScroll.X + VW / 2f + 1f);
        var th = (int)(smScroll.Y + VH / 2f + 1f);

        var dy = -offy;

        //Draw terrain
        sb.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);

        for (var y = sy; y < th; y++)
        {
            var dx = -offx;

            var ty = y;
            if (y < 0) ty = startupMapH - (-y % startupMapH);
            if (y >= startupMapH) ty = y % startupMapH;

            for (var x = sx; x < tw; x++)
            {
                var tx = x;
                if (x < 0) tx = startupMapW - (-x % startupMapW);
                if (x >= startupMapW) tx = x % startupMapW;

                var r_dst = new XnaRect((int)dx, (int)dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);

                var terpic = startupmapTerrains[startupMap[tx, ty] & 0x00FF];

                DrawTerrain(sb, terpic, r_dst);

                var overlay = startupMap[tx, ty] & 0xFF00;
                if (overlay != 0)
                {
                    terpic = startupmapTerrainsO[(overlay >> 8) - 1];
                    DrawTerrain(sb, terpic, r_dst);
                }
                dx += Gfx.ZoomSizeW;
            }
            dy += Gfx.ZoomSizeH;
        }
        sb.End();

    }

    private static void DrawTerrain(SpriteBatch sb, int p, XnaRect r_dst)
    {
        if (p >= 400)
        {
            //Animated
            var r_src = new XnaRect((p - 400) / 5 * 4 * Gfx.SRCTILEWIDTH + Game.AnimTicks * Gfx.SRCTILEWIDTH,
                (p - 400) % 5 * Gfx.SRCTILEHEIGHT,
                Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
            sb.Draw(Gfx.AnimTerrainGfx[0], r_dst, r_src, Color.White);
            return;
        }

        var col = p % 10;
        var row = p / 10;
        var rs = new XnaRect(col * Gfx.SRCTILEWIDTH, row * Gfx.SRCTILEHEIGHT, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
        sb.Draw(Gfx.TerrainGfx[0], r_dst, rs, Color.White);
    }

    public static void End()
    {
        startupmapTerrains.Clear();
        startupMap = null;
    }

    public static void Update(GameTime t)
    {
        var dist = t.ElapsedGameTime.Milliseconds * 0.002d;

        smScroll = smScroll + new Vector2((float)(Math.Sin(Angle) * dist), (float)(Math.Cos(Angle) * dist));
        smScroll.X = (smScroll.X % startupMapW) + startupMapW;
        smScroll.Y = (smScroll.Y % startupMapH) + startupMapH;
    }
}