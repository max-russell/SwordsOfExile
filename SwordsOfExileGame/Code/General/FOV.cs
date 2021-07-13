//#define INCLUDE_SHADOWCASTING

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
    public partial class TownMap : IMap
    {
        #if INCLUDE_SHADOWCASTING
        Location FOV_origin;
        byte FOV_bitno;
        byte FOV_bitinverse;
        bool FOV_consider_light;
        #endif
        int FOV_light_radius;

        public void UpdateVisible()
        {
            if (Script.suspendMapUpdate) return;

            _Visible = new byte[Width, Height];

            if (Game.Mode == eMode.COMBAT)
            {
                foreach (PCType pc in Party.EachAlivePC())
                {
                    UpdateVisiblePC(pc, false);
                }
            }
            else
                UpdateVisiblePC(null, false);
        }

        /// <summary>
        /// Update visible map. The lower 6 bits of each byte in the array contains the separate visibility data for all characters in the
        /// party. 
        /// </summary>
        /// <param name="pc">The character to update visibility for. If null, update entire party.</param>
        /// <param name="clear_existing">Whether to ditch all existing visibility data first. Irrelevant if updating entire party.</param>
        public void UpdateVisiblePC(PCType pc, bool clear_existing = false)//params Location[] locs)
        {
            if (clear_existing)
                _Visible = new byte[Width, Height];

#if !INCLUDE_SHADOWCASTING
            Location FOV_origin;
            byte FOV_bitno, FOV_bitinverse;
            //bool FOV_consider_light;
#endif
            FOV_origin = pc == null ? Party.LeaderPC.Pos : pc.Pos;
            FOV_bitno = pc == null ? (byte)255 : (byte)Math.Pow(2, Party.PCList.IndexOf(pc));
            FOV_bitinverse = (byte)(FOV_bitno ^ 255);
            FOV_light_radius = getLightRadius();

//            if (!Constants.FOV_SHADOW_CASTING)
//            {

            //Clear visibility
            if (!clear_existing)
            {
                for (int x = 0; x < Width; x++)
                    for (int y = 0; y < Height; y++)
                        _Visible[x, y] &= FOV_bitinverse;
            }
            _Visible[FOV_origin.X, FOV_origin.Y] |= FOV_bitno;
            _Explored[FOV_origin.X, FOV_origin.Y] = true;

#if INCLUDE_SHADOWCASTING

            //New Shadow Casting Field of view generation
            //FOV using recursive shadowcasting - Björn Bergström [bjorn.bergstrom@roguelikedevelopment.org]
            //Code and improvement for recursive shadowcasting - Henri Hakl 

            if (!clear_existing)
                for(int x = 0; x < Width; x++)
                    for(int y = 0; y < Height; y++)
                        _Visible[x, y] &= FOV_bitinverse;

            _Visible[FOV_origin.x, FOV_origin.y] |= FOV_bitno;

            for (int o = 1; o <= 8; o++)
                FOVScanOctant(1, o, 1.0, 0.0);

#else
            //This is the traditional Blades of Exile Field of View generation

            int lx = Maths.Max(0, FOV_origin.X - Constants.SIGHT_RANGE),
                rx = Maths.Min(Width, FOV_origin.X + Constants.SIGHT_RANGE + 1),
                ty = Maths.Max(0, FOV_origin.Y - Constants.SIGHT_RANGE),
                by = Maths.Min(Height, FOV_origin.Y + Constants.SIGHT_RANGE + 1);
                
            bool ignore_light = LightType == 0;



            //if (LightType == 0)
            //{
            for (int y = ty; y < by; y++)
                for (int x = lx; x < rx; x++)
                {
                    //Don't do this square if it's been marked visible previously.
                    if ((_Visible[x,y] & FOV_bitno) > 0) continue;

                    //_Visible[x, y] &= FOV_bitinverse;

                    Location p1 = FOV_origin, p2 = new Location(x,y);

                    int storage = 0;
                        // Light check
                    //if (!ignore_light && !squareInLight(p2)) continue;//return Constants.OBSCURITY_LIMIT+1;

                     
                    if (p1.Y == p2.Y)
                    {
                        //if (p1.x == 1 && p2.x == 0)
                        //{
                        //}

                        if (p1.X > p2.X)
                        {
                            for (int count = p1.X - 1; count >= p2.X; count--)
                            {
                                _Visible[count, p1.Y] |= FOV_bitno;
                                _Explored[count, p1.Y] = true;
                                storage += FOV_GetObscurity(new Location(count, p1.Y));
                                if (storage >= Constants.OBSCURITY_LIMIT) break;
                            }
                        }
                        else
                        {
                            for (int count = p1.X + 1; count <= p2.X; count++)
                            {
                                _Visible[count, p1.Y] |= FOV_bitno;
                                _Explored[count, p1.Y] = true;
                                storage += FOV_GetObscurity(new Location(count, p1.Y));
                                if (storage >= Constants.OBSCURITY_LIMIT) break;
                            }
                        }
                    }
                    else if (p1.X == p2.X)
                    {
                        if (p1.Y > p2.Y)
                            for (int count = p1.Y - 1; count >= p2.Y; count--)
                            {
                                _Visible[p1.X, count] |= FOV_bitno;
                                _Explored[p1.X, count] = true;
                                storage += FOV_GetObscurity(new Location(p1.X, count));
                                if (storage >= Constants.OBSCURITY_LIMIT) break;
                            }
                        else
                            for (int count = p1.Y + 1; count <= p2.Y; count++)
                            {
                                _Visible[p1.X, count] |= FOV_bitno;
                                _Explored[p1.X, count] = true;
                                storage += FOV_GetObscurity(new Location(p1.X, count));
                                if (storage >= Constants.OBSCURITY_LIMIT) break;
                            }
                    }
                    else
                    {
                        int dx = p2.X - p1.X;
                        int dy = p2.Y - p1.Y;

                        if (Math.Abs(dy) > Math.Abs(dx))
                        {
                            if (p2.Y > p1.Y)
                                for (int count = 1; count <= dy; count++)
                                {
                                    _Visible[p1.X + (count * dx) / dy, p1.Y + count] |= FOV_bitno;
                                    _Explored[p1.X + (count * dx) / dy, p1.Y + count] = true;
                                    storage += FOV_GetObscurity(new Location(p1.X + (count * dx) / dy, p1.Y + count));
                                    if (storage >= Constants.OBSCURITY_LIMIT) break;
                                }
                            else
                                for (int count = -1; count >= dy; count--)
                                {
                                    _Visible[p1.X + (count * dx) / dy, p1.Y + count] |= FOV_bitno;
                                    _Explored[p1.X + (count * dx) / dy, p1.Y + count] = true;
                                    storage += FOV_GetObscurity(new Location(p1.X + (count * dx) / dy, p1.Y + count));
                                    if (storage >= Constants.OBSCURITY_LIMIT) break;
                                }
                        }
                        else if (Math.Abs(dy) <= Math.Abs(dx))
                        {
                            if (p2.X > p1.X)
                                for (int count = 1; count <= dx; count++)
                                {
                                    _Visible[p1.X + count, p1.Y + (count * dy) / dx] |= FOV_bitno;
                                    _Explored[p1.X + count, p1.Y + (count * dy) / dx] = true;
                                    storage += FOV_GetObscurity(new Location(p1.X + count, p1.Y + (count * dy) / dx));
                                    if (storage >= Constants.OBSCURITY_LIMIT) break;
                                }
                            else
                                for (int count = -1; count >= dx; count--)
                                {
                                    _Visible[p1.X + count, p1.Y + (count * dy) / dx] |= FOV_bitno;
                                    _Explored[p1.X + count, p1.Y + (count * dy) / dx] = true;
                                    storage += FOV_GetObscurity(new Location(p1.X + count, p1.Y + (count * dy) / dx));
                                    if (storage >= Constants.OBSCURITY_LIMIT) break;
                                }
                        }
                    }
                    //if (CanSee(FOV_origin, new Location(x, y), no_light_check) < Constants.OBSCURITY_LIMIT)
                    //{
                    //    _Visible[x, y] |= FOV_bitno;
                    //    _Explored[x, y] = true;
                    //}
                }
        //}
        //else
        //{
        //    for (int y = ty; y < by; y++)
        //        for (int x = lx; x < rx; x++)
        //        {
        //            _Visible[x, y] &= FOV_bitinverse;

        //            if (CanSee(FOV_origin, new Location(x, y), true) < Constants.OBSCURITY_LIMIT && squareInLight(new Location(x, y)))
        //            {
        //                _Visible[x, y] |= FOV_bitno;
        //                _Explored[x, y] = true;
        //            }

        //        }
        //}
    }

#endif
        


#if INCLUDE_SHADOWCASTING
        void FOVScanOctant(int pDepth, int pOctant, double pStartSlope, double pEndSlope)
        {
            int visrange2 = Constants.SIGHT_RANGE * Constants.SIGHT_RANGE;
            int x = 0;
            int y = 0;

            switch (pOctant)
            {

                case 1: //nnw
                    y = FOV_origin.y - pDepth;
                    if (y < 0) return;

                    x = FOV_origin.x - Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (x < 0) x = 0;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, false) >= pEndSlope)
                    {
                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;


                            if (FOV_Opaque(x,y)) //current cell blocked
                            {
                                if (x - 1 >= 0 && !FOV_Opaque(x-1,y)) //prior cell within range AND open...
                                    //...incremenet the depth, adjust the endslope and recurse
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x - 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, false));
                            }
                            else
                            {
                                if (x - 1 >= 0 && FOV_Opaque(x - 1, y)) //prior cell within range AND open...
                                    //..adjust the startslope
                                    pStartSlope = getSlope(x - 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, false);
                            }
                        }
                        x++;
                    }
                    x--;
                    break;

                case 2: //nne

                    y = FOV_origin.y - pDepth;
                    if (y < 0) return;

                    x = FOV_origin.x + Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (x >= Width) x = Width - 1;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, false) <= pEndSlope)
                    {
                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (x + 1 < Width && !FOV_Opaque(x + 1, y))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x + 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, false));
                            }
                            else
                            {
                                if (x + 1 < Width && FOV_Opaque(x + 1, y))
                                    pStartSlope = -getSlope(x + 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, false);
                            }
                        }
                        x--;
                    }
                    x++;
                    break;

                case 3:

                    x = FOV_origin.x + pDepth;
                    if (x >= Width) return;

                    y = FOV_origin.y - Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (y < 0) y = 0;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, true) <= pEndSlope)
                    {

                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (y - 1 >= 0 && !FOV_Opaque(x, y-1))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x - 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, true));
                            }
                            else
                            {
                                if (y - 1 >= 0 && FOV_Opaque(x, y-1))
                                    pStartSlope = -getSlope(x + 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, true);
                            }
                        }
                        y++;
                    }
                    y--;
                    break;

                case 4:

                    x = FOV_origin.x + pDepth;
                    if (x >= Width) return;

                    y = FOV_origin.y + Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (y >= Height) y = Height - 1;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, false) >= pEndSlope)
                    {

                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (y + 1 < Height && !FOV_Opaque(x, y+1))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x - 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, true));
                            }
                            else
                            {
                                if (y + 1 < Height && FOV_Opaque(x, y+1))
                                    pStartSlope = getSlope(x + 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, true);
                            }
                        }
                        y--;
                    }
                    y++;
                    break;

                case 5:

                    y = FOV_origin.y + pDepth;
                    if (y >= Height) return;

                    x = FOV_origin.x + Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (x >= Width) x = Width - 1;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, false) >= pEndSlope)
                    {
                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (x + 1 < Height && !FOV_Opaque(x + 1, y))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x + 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, false));
                            }
                            else
                            {
                                if (x + 1 < Height
                                        && FOV_Opaque(x + 1, y))
                                    pStartSlope = getSlope(x + 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, false);
                            }
                        }
                        x--;
                    }
                    x++;
                    break;

                case 6:

                    y = FOV_origin.y + pDepth;
                    if (y >= Height) return;

                    x = FOV_origin.x - Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (x < 0) x = 0;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, false) <= pEndSlope)
                    {
                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (x - 1 >= 0 && !FOV_Opaque(x - 1, y))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x - 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, false));
                            }
                            else
                            {
                                if (x - 1 >= 0
                                        && FOV_Opaque(x - 1, y))
                                    pStartSlope = -getSlope(x - 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, false);
                            }
                        }
                        x++;
                    }
                    x--;
                    break;

                case 7:

                    x = FOV_origin.x - pDepth;
                    if (x < 0) return;

                    y = FOV_origin.y + Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (y >= Height) y = Height - 1;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, true) <= pEndSlope)
                    {

                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (y + 1 < Height && !FOV_Opaque(x, y+1))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x + 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, true));
                            }
                            else
                            {
                                if (y + 1 < Height && FOV_Opaque(x, y+1))
                                    pStartSlope = -getSlope(x - 0.5, y + 0.5, FOV_origin.x, FOV_origin.y, true);
                            }
                        }
                        y--;
                    }
                    y++;
                    break;

                case 8: //wnw

                    x = FOV_origin.x - pDepth;
                    if (x < 0) return;

                    y = FOV_origin.y - Convert.ToInt32((pStartSlope * Convert.ToDouble(pDepth)));
                    if (y < 0) y = 0;

                    while (getSlope(x, y, FOV_origin.x, FOV_origin.y, true) >= pEndSlope)
                    {

                        if (getVisDistance(x, y, FOV_origin.x, FOV_origin.y) <= visrange2)
                        {
                            _Visible[x, y] |= FOV_bitno;

                            if (FOV_Opaque(x, y))
                            {
                                if (y - 1 >= 0 && !FOV_Opaque(x, y-1))
                                    FOVScanOctant(pDepth + 1, pOctant, pStartSlope, getSlope(x + 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, true));

                            }
                            else
                            {
                                if (y - 1 >= 0 && FOV_Opaque(x, y-1))
                                    pStartSlope = getSlope(x - 0.5, y - 0.5, FOV_origin.x, FOV_origin.y, true);
                            }
                        }
                        y++;
                    }
                    y--;
                    break;
            }


            if (x < 0)
                x = 0;
            else if (x >= Width)
                x = Width - 1;

            if (y < 0)
                y = 0;
            else if (y >= Height)
                y = Height - 1;

            if (pDepth < Constants.SIGHT_RANGE & !FOV_Opaque(x,y))
                FOVScanOctant(pDepth + 1, pOctant, pStartSlope, pEndSlope);

        }

        bool FOV_Opaque(int x, int y)
        {

            if (LightType != 0 && squareInLight(new Location(x, y)))
                return false;

            TerrainRecord what_terrain = terrainAt(x, y);// _Terrain[x, y];// TerrainAt(l);// _Terrain[l.x, l.y];//coord_to_ter(x,y);
            int store = what_terrain.Obscurity;
            store += fieldObscurityThere(new Location(x,y));
            return store >= Constants.OBSCURITY_LIMIT;
        }

        /// <summary>
        /// Get the gradient of the slope formed by the two points
        /// </summary>
        /// <param name="pX1"></param>
        /// <param name="pY1"></param>
        /// <param name="pX2"></param>
        /// <param name="pY2"></param>
        /// <param name="pInvert">Invert slope</param>
        /// <returns></returns>
        double getSlope(double pX1, double pY1, double pX2, double pY2, bool pInvert)
        {
            if (pInvert)
                return (pY1 - pY2) / (pX1 - pX2);
            else
                return (pX1 - pX2) / (pY1 - pY2);
        }

        /// <summary>
        /// Calculate the distance between the two points
        /// </summary>
        /// <param name="pX1"></param>
        /// <param name="pY1"></param>
        /// <param name="pX2"></param>
        /// <param name="pY2"></param>
        /// <returns>Distance</returns>
        int getVisDistance(int pX1, int pY1, int pX2, int pY2)
        {
            return ((pX1 - pX2) * (pX1 - pX2)) + ((pY1 - pY2) * (pY1 - pY2));
        }
#endif
        public int FOV_GetObscurity(Location l)
        {

            if (LightType > 0 && 
               !fieldsThere(l, Field.LIGHT.Bit))
            {
                bool near_pc = false;
                foreach (PCType pc in Party.EachIndependentPC())
                    if (pc.Pos.DistanceTo(l) <= FOV_light_radius) { near_pc = true; break; }
                if (!near_pc)
                    return Constants.OBSCURITY_LIMIT + 1;
            }

            TerrainRecord what_terrain = TerrainAt(l);
            int store = what_terrain.Obscurity;
            store += fieldObscurityThere(l);
            return store;
        }
    


    }
}