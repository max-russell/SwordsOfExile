
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

using MonoGame.Extended.Graphics;

namespace SwordsOfExileGame
{

    static class StartupMap
    {

        static bool startupMapLoaded = false;

        static List<int> startupmapTerrains, startupmapTerrainsO;
        static ushort[,] startupMap;
        static int startupMapW, startupMapH;
        static Vector2 smScroll;
        static double Angle = 0d;

        public static void Load()
        {
            startupMapLoaded = false;

            startupmapTerrains = new List<int>();
            startupmapTerrainsO = new List<int>();
            startupMap = null;

            string mapdir = Path.Combine(Game.BaseDirectory, "Data", "StartupMap.dat");

            if (!File.Exists(mapdir)) return;// false;

            using (FileStream fs = new FileStream(mapdir, FileMode.Open, FileAccess.Read))
            using (BinaryReader file = new BinaryReader(fs))
            {
                int m = file.ReadInt16();
                for (int n = 0; n < m; n++)
                    startupmapTerrains.Add(file.ReadInt16());

                m = file.ReadInt16();
                for (int n = 0; n < m; n++)
                    startupmapTerrainsO.Add(file.ReadInt16());


                startupMapW = file.ReadInt32();
                startupMapH = file.ReadInt32();

                startupMap = new ushort[startupMapW, startupMapH];

                for (int y = 0; y < startupMapH; y++)
                    for (int x = 0; x < startupMapW; x++)
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

            int sx = (int)bx;
            int sy = (int)by;
            int tw = (int)(smScroll.X + VW / 2f + 1f);
            int th = (int)(smScroll.Y + VH / 2f + 1f);

            double dy = -offy;

            //Draw terrain
            sb.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);//.Opaque);

            for (int y = sy; y < th; y++)
            {
                double dx = -offx;

                int ty = y;
                if (y < 0) ty = startupMapH - (-y % startupMapH);//y - (0 - startupMapH);
                if (y >= startupMapH) ty = y % startupMapH;

                //if (y >= 0 && y < startupMapH)
                for (int x = sx; x < tw; x++)
                {
                    int tx = x;
                    if (x < 0) tx = startupMapW - (-x % startupMapW);//y - (0 - startupMapH);
                    if (x >= startupMapW) tx = x % startupMapW;


                    //if (x >= 0 && x < startupMapW)
                    //{
                    //OutsideSector s = Sectors[x / SECTOR_WIDTH, y / SECTOR_HEIGHT];
                    //int tx = x % SECTOR_WIDTH, ty = y % SECTOR_HEIGHT;

                    //if (s.Explored[tx, ty])
                    //{
                    XnaRect r_dst = new XnaRect((int)dx, (int)dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);

                    int terpic = startupmapTerrains[startupMap[tx, ty] & 0x00FF];

                    //TerrainRecord ter = TerrainRecord.UnderlayList[s[tx, ty] & 0x00FF];//TerrainRecord.List[s[tx, ty]];

                    //if (ter.Special == eTerSpec.TOWN_ENTRANCE) //Display alternate terrain for hidden town entrances
                    //{
                    //    TownMap town = s.TownEntranceHere(new Location(tx, ty), true);
                    //    if (town.Hidden) ter = TerrainRecord.UnderlayList[ter.flag1];
                    //}

                    //TerrainRecord to_n = ty > 0 ? TerrainRecord.List[s[tx, ty - 1]] : terrainAt(x, y - 1);
                    //TerrainRecord to_s = ty < SECTOR_WIDTH - 1 ? TerrainRecord.List[s[tx, ty + 1]] : terrainAt(x, y + 1);
                    //TerrainRecord to_e = tx < SECTOR_HEIGHT - 1 ? TerrainRecord.List[s[tx + 1, ty]] : terrainAt(x + 1, y);
                    //TerrainRecord to_w = tx > 0 ? TerrainRecord.List[s[tx - 1, ty]] : terrainAt(x - 1, y);


                    DrawTerrain(sb, terpic, r_dst);
                    //ter.Draw(sb, r_dst, true);//, to_n, to_s, to_w, to_e);//_Visible[x, y]);

                    int overlay = startupMap[tx, ty] & 0xFF00;
                    if (overlay != 0)
                    {
                        terpic = startupmapTerrainsO[(overlay >> 8) - 1];
                        DrawTerrain(sb, terpic, r_dst);
                    }

                    //}
                    //}
                    dx += Gfx.ZoomSizeW;
                }
                dy += Gfx.ZoomSizeH;
            }
            sb.End();

        }

        static void DrawTerrain(SpriteBatch sb, int p, XnaRect r_dst)
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

            //int sheet = p / 50;
            int col = p % 10;
            int row = p / 10;//(p % 50) / 10;
            XnaRect rs = new XnaRect(col * Gfx.SRCTILEWIDTH, row * Gfx.SRCTILEHEIGHT, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
            sb.Draw(Gfx.TerrainGfx[0], r_dst, rs, Color.White);
        }

        public static void End()
        {
            startupmapTerrains.Clear();
            startupMap = null;
        }

        public static void Update(GameTime t)
        {
            double dist = t.ElapsedGameTime.Milliseconds * 0.002d;

            smScroll = smScroll + new Vector2((float)(Math.Sin(Angle) * dist), (float)(Math.Cos(Angle) * dist));
            smScroll.X = (smScroll.X % startupMapW) + startupMapW;
            smScroll.Y = (smScroll.Y % startupMapH) + startupMapH;

            //Angle += 0.0005d;
        }
    }

}