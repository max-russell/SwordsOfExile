using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;


namespace SwordsOfExileGame
{
    public partial class TownMap : IListEntity, IMap
    {
        public static ExileList<TownMap> List = new ExileList<TownMap>();

        PartyType Party { get { return Game.CurrentParty; } }

        public int Width, Height;
        public string ID { get { return id; } set { id = value; } }
        string id;
        string name;
        public string Name { get { return name; } }

        protected ushort[,] _Terrain;
        protected bool[,] _Explored;
        byte[,] _Visible;

        public int Num { get { return List.IndexOf(this); } }
        public bool Hidden;
        bool HasStorageArea;
        Rectangle StorageArea;
        int town_chop_time; string town_chop_key;
        public int LightType; 
        public Rectangle Boundary;
        public int CreatureKillLimit; 
        string FuncOnEntry, FuncOnExit, FuncOnTurnHostile;
        public bool PreventMapping, PreventScrying; 
        public int Difficulty;
        public List<TriggerSpot> TriggerSpotList = new List<TriggerSpot>();
        public List<InfoRect> InfoRectList = new List<InfoRect>();
        public Location[] EnterPos = new Location[4]; 
        public List<Timer> TimerList = new List<Timer>();
        List<PresetItem> PresetItemList = new List<PresetItem>();
        List<PresetField> PresetFieldList = new List<PresetField>();
        List<NPCPreset> CreatureStartList = new List<NPCPreset>();
        List<TalkingNode> TalkingNodeList = new List<TalkingNode>();

        public bool Hostile = false;
        public bool Abandoned = false;
        public List<NPC> NPCList = new List<NPC>();
        public List<Item> ItemList = new List<Item>();
        public int KillCount; //How many monsters have been killed in this town

        List<NPC> NPCTurnQueue; //At the start of the NPC turn, this is populated with npcs in the order that they will act.
        protected uint[,] Misc;     //Only towns - now incorporates Sfx & Lighting in its bits

        public void MakeExplored(Location loc) { if (InBounds(loc)) _Explored[loc.X, loc.Y] = true; } //Used in True Sight spell
        
        public bool Visible(Location loc)
        {
            if (InBounds(loc) && _Visible[loc.X, loc.Y] != 0) return true; return false;
        }
        public bool InBounds(Location loc)
        {
            if (loc.X >= 0 && loc.X < Width && loc.Y >= 0 && loc.Y < Height) return true; return false;
        }
        public bool InActArea(Location loc)
        {
            return (loc.X >= Boundary.Left && loc.Y >= Boundary.Top && loc.X <= Boundary.Right && loc.Y <= Boundary.Bottom);
        }

        //Only to be called if the Party has gone outside the town's act area.
        public Direction GetDepartDirection(Location loc)
        {
            if (loc.X < Boundary.Left) return new Direction(eDir.W);
            if (loc.X > Boundary.Right) return new Direction(eDir.E);
            if (loc.Y < Boundary.Top) return new Direction(eDir.N);
            return new Direction(eDir.S);
        }

        public TerrainRecord TerrainAt(Location loc)
        {
            if (!InBounds(loc)) return null;

            int overlay = _Terrain[loc.X, loc.Y] & 0xFF00;
            if (overlay != 0)
                return TerrainRecord.OverlayList[overlay >> 8];
            else
                return TerrainRecord.UnderlayList[_Terrain[loc.X, loc.Y] & 0x00FF];
        }
        TerrainRecord terrainAt(int x, int y)
        {
            int overlay = _Terrain[x, y] & 0xFF00;
            if (overlay != 0)
                return TerrainRecord.OverlayList[overlay >> 8];
            else
                return TerrainRecord.UnderlayList[_Terrain[x, y] & 0x00FF];
        }

        public bool NPCIsHere(NPC npc) { return NPCList.Contains(npc); }

        public NPC NPCHasStarted(NPCPreset start)
        {
            return NPCList.Find(n => n.Start == start);
        }
        public int NPCStartIndex(NPCPreset start)
        {
            if (start == null) return -1;
            return CreatureStartList.IndexOf(start);
        }
        public NPCPreset GetNPCStartByIndex(int index)
        {
            if (index == -1) return null;
            return CreatureStartList[index];
        }

        public TownMap() { }

        public void Load(BinaryReader In) {
            //Loads just the town's header. The rest is loaded later.
            id = In.ReadString();
            In.ReadString(); //Folder: ignored
            name = In.ReadString();
            Hidden = In.ReadBoolean();
            Width = In.ReadInt16();
            Height = In.ReadInt16();
            HasStorageArea = In.ReadBoolean();
            if (HasStorageArea) StorageArea = Rectangle.Read(In);
            List.Add(this);
        }

        public void Draw(SpriteBatch sb) 
        {
            float VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
            float VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
            int offx = (int)(((Gfx.Scroll.X - VW / 2f) - (int)(Gfx.Scroll.X - VW / 2f)) * Gfx.ZoomSizeW);
            int offy = (int)(((Gfx.Scroll.Y - VH / 2f) - (int)(Gfx.Scroll.Y - VH / 2f)) * Gfx.ZoomSizeH);
            int sx = (int)(Gfx.Scroll.X - VW / 2f);
            int sy = (int)(Gfx.Scroll.Y - VH / 2f);
            int tw = (int)(Gfx.Scroll.X + VW / 2f + 1f);
            int th = (int)(Gfx.Scroll.Y + VH / 2f + 1f);

            int charzoomw = (int)((float)Gfx.ZoomSizeW * Gfx.CHARWIDTH);
            int charoffx = (int)((float)(Gfx.ZoomSizeW - charzoomw) / 2f);
            int bigitemzoomw = (int)((float)Gfx.ZoomSizeW * Gfx.CHARWIDTH);
            int bigitemoffx = (int)((float)(Gfx.ZoomSizeW - charzoomw) / 2f);

            int dy = -offy;

            int xmin = 0, xmax = Width, ymin = 0, ymax = Height;

            //Draw terrain
            sb.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);

            if (!PreventMapping)
                for (int y = sy; y < th; y++)
                {
                    int dx = -offx;
                    if (y >= ymin && y < ymax)
                        for (int x = sx; x < tw; x++)
                        {
                            if (x >= xmin && x < xmax)
                                if (_Explored[x, y])
                                {
                                    XnaRect r_dst = new XnaRect(dx, dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);

                                    TerrainRecord ter = TerrainRecord.UnderlayList[_Terrain[x, y] & 0x00FF];

                                    bool fullbright = _Visible[x, y] != 0;
                                    if (Game.PlayerTargeting && Action.TargetPC.Pos.DistanceTo(new Location(x, y)) > Action.TargetRange)
                                        fullbright = false;

                                    ter.Draw(sb, r_dst, fullbright);
                                    int overlay = _Terrain[x, y] & 0xFF00;
                                    if (overlay != 0)
                                    {
                                        ter = TerrainRecord.OverlayList[overlay >> 8];
                                        ter.Draw(sb, r_dst, fullbright);
                                    }
                                }
                            dx += Gfx.ZoomSizeW;
                        }
                    dy += Gfx.ZoomSizeH;
                }
            else //This town has PreventMapping property - explored but not visible squares are not displayed.
                for (int y = sy; y < th; y++)
                {
                    int dx = -offx;
                    if (y >= ymin && y < ymax)
                        for (int x = sx; x < tw; x++)
                        {
                            if (x >= xmin && x < xmax)
                                if (_Visible[x, y] != 0)
                                {
                                    XnaRect r_dst = new XnaRect(dx, dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                                    bool fullbright = true;
                                    TerrainRecord ter = TerrainRecord.UnderlayList[_Terrain[x, y] & 0x00FF];
                                    if (Game.PlayerTargeting && Action.TargetPC.Pos.DistanceTo(new Location(x, y)) > Action.TargetRange)
                                        fullbright = false;
                                    ter.Draw(sb, r_dst, fullbright);
                                    int overlay = _Terrain[x, y] & 0xFF00;
                                    if (overlay != 0)
                                    {
                                        ter = TerrainRecord.OverlayList[overlay >> 8];
                                        ter.Draw(sb, r_dst, fullbright);
                                    }
                                }
                            dx += Gfx.ZoomSizeW;
                        }
                    dy += Gfx.ZoomSizeH;
                }

            if (Gfx.ZoomSizeW > Gfx.ZOOMSIMPLETHRESHOLD && Gfx.ZoomSizeH > Gfx.ZOOMSIMPLETHRESHOLD)
            {
                //Draw Items
                foreach (Item i in ItemList)
                {
                    if (_Visible[i.Pos.X, i.Pos.Y] != 0 && i.Pos.Inside(sx, sy, tw, th))
                    {
                            XnaRect dr = new XnaRect((i.Pos.X - sx) * Gfx.ZoomSizeW - offx + bigitemoffx,
                                 (i.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                                 bigitemzoomw, Gfx.ZoomSizeH);
                            i.Draw(sb, dr);
                    }
                }
            }

            //Draw fields
            dy = -offy;
            for (int y = sy; y < th; y++)
            {
                int dx = -offx;
                if (y >= ymin && y < ymax)
                    for (int x = sx; x < tw; x++)
                    {

                        if (x >= xmin && x < xmax)
                            if (_Visible[x, y] != 0 && Misc[x, y] > 3) // > 3 because bits 1 & 2 are secret passages and special triggers, which aren't drawn
                            {
                                XnaRect r_dst = new XnaRect(dx, dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                                drawField(sb, x, y, r_dst);
                            }
                            else if (_Explored[x, y])
                            {
                                XnaRect r_dst = new XnaRect(dx, dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                                drawDimBarrierFields(sb, x, y, r_dst);
                            }
                        dx += Gfx.ZoomSizeW;
                    }
                dy += Gfx.ZoomSizeH;
            }

            //Draw animation underlays (moving crates / barrels)
            foreach (IAnimUnderlay underlay in Animation.EachUnderlayAnim())
            {
                Location p = new Location((int)underlay.Pos.X, (int)underlay.Pos.Y);

                if (p.Inside(sx, sy, tw, th) && Visible(p))
                {
                    Vector2 pos = new Vector2((underlay.Pos.X - sx) * Gfx.ZoomSizeW - offx,
                                         (underlay.Pos.Y - sy) * Gfx.ZoomSizeH - offy);
                    underlay.DrawUnderlay(sb, pos);
                }
            }

            Location mloc = Location.Zero;
            bool npc_at_mouse = false;

            //Draw dark square on target when targeting - behind NPCs
            if (Game.PlayerTargeting)
            {
                mloc = Gfx.GetTileAtMouse(Gui.Ms);
                npc_at_mouse = CharacterThere(mloc, false, true) != null;

                if (!Action.TargetNPCsOnly || npc_at_mouse)
                {
                    if (mloc != Action.TargetPC.Pos && Visible(mloc) && mloc.DistanceTo(Action.TargetPC.Pos) <= Action.TargetRange)
                    {
                        if (Action.TargetPattern == null)
                        {
                            XnaRect dr = new XnaRect((mloc.X - sx) * Gfx.ZoomSizeW - offx,
                                (mloc.Y - sy) * Gfx.ZoomSizeH - offy,
                                Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                            Gfx.DrawRect(dr.X, dr.Y, dr.Width, dr.Height, Color.FromNonPremultiplied(100, 100, 100, 100), true);
                        }
                        else
                        {
                            foreach (Location l in Action.TargetPattern.EachPatternSpot(mloc))
                            {
                                if (Visible(l))
                                {
                                    XnaRect dr = new XnaRect((l.X - sx) * Gfx.ZoomSizeW - offx,
                                        (l.Y - sy) * Gfx.ZoomSizeH - offy,
                                        Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                                    Gfx.DrawRect(dr.X, dr.Y, dr.Width, dr.Height, Color.FromNonPremultiplied(100, 100, 100, 100), true);
                                }
                            }
                        }
                    }
                }
            }

            sb.End();

            //Draw creatures
            foreach (NPC cr in NPCList)
            {
                bool vis = false;

                if (Party.DetectMonster > 0) 
                    vis = true;
                else
                    for (int y = 0; y < cr.Height; y++)
                        for (int x = 0; x < cr.Width; x++)
                        {
                            Location p = cr.Pos.Mod(x, y);
                            if (_Visible[p.X, p.Y] != 0 && p.Inside(sx, sy, tw, th)) { vis = true; break; }
                        }

                if (vis == false && cr.AnimAction is Animation_Move)
                {
                    for (int y = 0; y < cr.Height; y++)
                        for (int x = 0; x < cr.Width; x++)
                        {
                            Location p = cr.Pos.Mod(x, y) - ((Animation_Move)cr.AnimAction).PosMod;
                            if (_Visible[p.X, p.Y] != 0 && p.Inside(sx, sy, tw, th))
                            { vis = true; break; }
                        }
                }

                if (vis)
                {
                    XnaRect dr = new XnaRect((cr.Pos.X - sx) * Gfx.ZoomSizeW - offx + (charoffx * cr.Record.Width),
                             (cr.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                             charzoomw * cr.Record.Width, Gfx.ZoomSizeH * cr.Record.Height);
                    sb.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);
                    cr.Draw(sb, dr, Color.White);
                    sb.End();
                }
            }

            sb.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);

            //Draw Vehicles
            foreach (Vehicle v in Vehicle.List)
                if (v.Map == this && v.Pos.Inside(sx, sy, tw, th) && Visible(v.Pos))
                {
                    XnaRect dr = new XnaRect((v.Pos.X - sx) * Gfx.ZoomSizeW - offx + charoffx,
                     (v.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                     charzoomw, Gfx.ZoomSizeH);
                    v.Draw(sb, dr);
                }

            if (Gfx.ZoomSizeW > Gfx.ZOOMSIMPLETHRESHOLD && Gfx.ZoomSizeH > Gfx.ZOOMSIMPLETHRESHOLD)
            {
                //Draw dark edges to unexplored/out of sight areas
                float qw = (float)Gfx.ZoomSizeW / 3f, qh = (float)Gfx.ZoomSizeH / 3f;
                int qwf = Maths.Floor(qw), qhf = Maths.Floor(qh), qwc = Maths.Ceiling(qw), qhc = Maths.Ceiling(qh);


                dy = -offy;
                for (int y = sy; y < th; y++)
                {
                    int dx = -offx;
                    if (y >= ymin && y < ymax)
                        for (int x = sx; x < tw; x++)
                        {

                            if (x >= xmin && x < xmax)
                                if (_Explored[x, y])
                                {
                                    bool expl_w = x == 0 ? false : _Explored[x - 1, y];
                                    bool expl_e = x == (Width - 1) ? false : _Explored[x + 1, y];
                                    bool expl_n = y == 0 ? false : _Explored[x, y - 1];
                                    bool expl_s = y == (Height - 1) ? false : _Explored[x, y + 1];
                                    bool expl_nw = (x == 0 || y == 0) ? false : _Explored[x - 1, y - 1];
                                    bool expl_ne = (x == Width - 1 || y == 0) ? false : _Explored[x + 1, y - 1];
                                    bool expl_sw = (x == 0 || y == Height - 1) ? false : _Explored[x - 1, y + 1];
                                    bool expl_se = (x == Width - 1 || y == Height - 1) ? false : _Explored[x + 1, y + 1];

                                    if (!expl_w)
                                    {
                                        sb.Draw(Gfx.DarkEdges, new XnaRect(dx, dy + qhf, qwc, qhc), new XnaRect(16, 0, 16, 16), Color.White);

                                        if (!expl_n)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect(dx, dy, qwc, qhc), new XnaRect(64, 0, 16, 16), Color.White);
                                        else
                                            sb.Draw(Gfx.DarkEdges, new XnaRect(dx, dy, qwc, qhc), new XnaRect(16, 0, 16, 16), Color.White);

                                        if (!expl_s)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect(dx, (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(96, 0, 16, 16), Color.White);
                                        else
                                            sb.Draw(Gfx.DarkEdges, new XnaRect(dx, (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(16, 0, 16, 16), Color.White);
                                    }
                                    if (!expl_e)
                                    {
                                        sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), dy + qhf, qwc, qhc), new XnaRect(32, 0, 16, 16), Color.White);

                                        if (!expl_n)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), dy, qwc, qhc), new XnaRect(80, 0, 16, 16), Color.White);
                                        else
                                            sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), dy, qwc, qhc), new XnaRect(32, 0, 16, 16), Color.White);

                                        if (!expl_s)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(112, 0, 16, 16), Color.White);
                                        else
                                            sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(32, 0, 16, 16), Color.White);
                                    }
                                    if (!expl_n)
                                    {
                                        sb.Draw(Gfx.DarkEdges, new XnaRect(dx + qwf, dy, qwc, qhc), new XnaRect(0, 0, 16, 16), Color.White);
                                        if (expl_w)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect(dx, dy, qwc, qhc), new XnaRect(0, 0, 16, 16), Color.White);
                                        if (expl_e)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), dy, qwc, qhc), new XnaRect(0, 0, 16, 16), Color.White);
                                    }
                                    if (!expl_s)
                                    {
                                        sb.Draw(Gfx.DarkEdges, new XnaRect(dx + qwf, (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(48, 0, 16, 16), Color.White);
                                        if (expl_w)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect(dx, (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(48, 0, 16, 16), Color.White);
                                        if (expl_e)
                                            sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(48, 0, 16, 16), Color.White);
                                    }

                                    if (!expl_nw && expl_w && expl_s)
                                        sb.Draw(Gfx.DarkEdges, new XnaRect(dx, dy, qwc, qhc), new XnaRect(128, 0, 16, 16), Color.White);
                                    if (!expl_ne && expl_e && expl_n)
                                        sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), dy, qwc, qhc), new XnaRect(144, 0, 16, 16), Color.White);
                                    if (!expl_sw && expl_w && expl_s)
                                        sb.Draw(Gfx.DarkEdges, new XnaRect(dx, (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(160, 0, 16, 16), Color.White);
                                    if (!expl_se && expl_e && expl_s)
                                        sb.Draw(Gfx.DarkEdges, new XnaRect((dx + Maths.Floor(qw * 2)), (dy + Maths.Floor(qh * 2)), qwc, qhc), new XnaRect(176, 0, 16, 16), Color.White);
                                }
                            dx += Gfx.ZoomSizeW;
                        }
                    dy += Gfx.ZoomSizeH;
                }
            }

            //For fading to/from black we just draw a big black rectangle over the screen at various levels of opacity.
            if (Gfx.FadeMode != 0)
            {
                Gfx.DrawRect(0, 0, Gfx.WinW, Gfx.WinH, Gfx.FadeColor, true);
            }

            sb.End();

            //Draw PCs
            foreach(PCType pc in Party.GetPCDrawOrder())
            {

                if (Party.Vehicle == null || (pc == Party.LeaderPC && pc.AnimAction != null))
                {
                    sb.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);

                    XnaRect dr = new XnaRect((pc.Pos.X - sx) * Gfx.ZoomSizeW - offx + charoffx,
                                            (pc.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                                            charzoomw, Gfx.ZoomSizeH);
                    pc.Draw(sb, dr, Color.White);
                    sb.End();
                }

                //Draw town edge markers

                if (Game.Mode == eMode.TOWN || pc == Party.ActivePC)
                {
                    sb.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);
                    //If near to the town boundary, draw where the edge is.

                    for (int a = -1; a <= 1; a++)
                    {
                        Location p = pc.Pos.Mod(0, a);

                        if (InActArea(p))
                        {
                            if (p.X - Boundary.Left == 0 && drawBoundaryThere(p.Mod(-1, 0)))
                                Gfx.DrawRect((p.X - 1 - sx) * Gfx.ZoomSizeW - offx + (int)(Gfx.ZoomSizeW * 0.8f), (p.Y - sy) * Gfx.ZoomSizeH - offy, Gfx.ZoomSizeW / 5, Gfx.ZoomSizeH, Color.FromNonPremultiplied(255, 255, 255, 160), true);
                            else if (p.X - Boundary.Left == 1 && drawBoundaryThere(p.Mod(-2, 0)))
                                Gfx.DrawRect((p.X - 2 - sx) * Gfx.ZoomSizeW - offx + (int)(Gfx.ZoomSizeH * 0.8f), (p.Y - sy) * Gfx.ZoomSizeH - offy, Gfx.ZoomSizeW / 5, Gfx.ZoomSizeH, Color.FromNonPremultiplied(255, 255, 255, 90), true);

                            if (Boundary.Right - p.X == 0 && drawBoundaryThere(p.Mod(1, 0)))
                                Gfx.DrawRect((p.X + 1 - sx) * Gfx.ZoomSizeW - offx, (p.Y - sy) * Gfx.ZoomSizeH - offy, Gfx.ZoomSizeW / 5, Gfx.ZoomSizeH, Color.FromNonPremultiplied(255, 255, 255, 160), true);
                            else if (Boundary.Right - p.X == 1 && drawBoundaryThere(p.Mod(2, 0)))
                                Gfx.DrawRect((p.X + 2 - sx) * Gfx.ZoomSizeW - offx, (p.Y - sy) * Gfx.ZoomSizeH - offy, Gfx.ZoomSizeW / 5, Gfx.ZoomSizeH, Color.FromNonPremultiplied(255, 255, 255, 90), true);
                        }
                    }

                    for (int a = -1; a <= 1; a++)
                    {
                        Location p = pc.Pos.Mod(a, 0);

                        if (InActArea(p))
                        {
                            if (p.Y - Boundary.Top == 0 && drawBoundaryThere(p.Mod(0, -1)))
                                Gfx.DrawRect((p.X - sx) * Gfx.ZoomSizeW - offx, (p.Y - 1 - sy) * Gfx.ZoomSizeH - offy + (int)(Gfx.ZoomSizeH * 0.8f), Gfx.ZoomSizeW, Gfx.ZoomSizeH / 5, Color.FromNonPremultiplied(255, 255, 255, 160), true);
                            else if (p.Y - Boundary.Top == 1 && drawBoundaryThere(p.Mod(0, -2)))
                                Gfx.DrawRect((p.X - sx) * Gfx.ZoomSizeW - offx, (p.Y - 2 - sy) * Gfx.ZoomSizeH - offy + (int)(Gfx.ZoomSizeH * 0.8f), Gfx.ZoomSizeW, Gfx.ZoomSizeH / 5, Color.FromNonPremultiplied(255, 255, 255, 90), true);

                            if (Boundary.Bottom - p.Y == 0 && drawBoundaryThere(p.Mod(0, 1)))
                                Gfx.DrawRect((p.X - sx) * Gfx.ZoomSizeW - offx, (p.Y + 1 - sy) * Gfx.ZoomSizeH - offy, Gfx.ZoomSizeW, Gfx.ZoomSizeH / 5, Color.FromNonPremultiplied(255, 255, 255, 160), true);
                            else if (Boundary.Bottom - p.Y == 1 && drawBoundaryThere(p.Mod(0, 2)))
                                Gfx.DrawRect((p.X - sx) * Gfx.ZoomSizeW - offx, (p.Y + 2 - sy) * Gfx.ZoomSizeH - offy, Gfx.ZoomSizeW, Gfx.ZoomSizeH / 5, Color.FromNonPremultiplied(255, 255, 255, 90), true);
                        }
                    }
                    sb.End();
                }
            }

            sb.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);
           

            //Draw Animation Overlays (Damage markers, missiles etc)
            foreach (IAnimOverlay overlay in Animation.EachOverlayAnim())
            {
                Location p = new Location((int)overlay.Pos.X, (int)overlay.Pos.Y);

                if (p.Inside(sx, sy, tw, th) && (Visible(p) || overlay is Animation_Explosion))
                {
                    Vector2 pos = new Vector2((overlay.Pos.X - sx) * Gfx.ZoomSizeW - offx,
                                         (overlay.Pos.Y - sy) * Gfx.ZoomSizeH - offy);
                    overlay.DrawOverlay(sb, pos);
                }
            }

            //Targeting line
            if (Game.PlayerTargeting)
            {
                if (mloc != Action.TargetPC.Pos && Visible(mloc) && mloc.DistanceTo(Action.TargetPC.Pos) <= Action.TargetRange && (!Action.TargetNPCsOnly || npc_at_mouse))
                {

                    //Draw animated Line between targeter and target
                    if (Action.TargetDrawLine)
                    {
                        //Draw line between Targetting PC and tile at mouse
                        //Get angle to point from A to B
                        float rot = Action.TargetPC.Pos.GetAngle(mloc);

                        Vector2 startpos = Action.TargetPC.Pos.ToVector2() + new Vector2(0.5f, 0.5f);
                        Vector2 endpos = mloc.ToVector2() + new Vector2(0.5f, 0.5f);
                        float dist = Vector2.Distance(startpos, endpos);
                        Vector2 step = endpos - startpos; //Vector2.Lerp(startpos, endpos, (Game.AnimTicks+1f) / 5f);
                        step.Normalize();
                        float stepdist = Vector2.Distance(Vector2.Zero, step);

                        Vector2 pos = startpos + step * 0.5f;
                        float posdist = stepdist * 0.5f;

                        do
                        {
                            Vector2 drawpos = pos + step * ((float)Game.AnimTicks / 4f);
                            drawpos.X = (drawpos.X - sx) * Gfx.ZoomSizeW - offx;
                            drawpos.Y = (drawpos.Y - sy) * Gfx.ZoomSizeH - offy;
                            sb.Draw(Gfx.Bar, drawpos, null, Color.White, rot, new Vector2(8, 4), (float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH * 0.5f, SpriteEffects.None, 0);


                            pos += step;
                            posdist += stepdist;
                        } while (posdist < dist - stepdist * 0.5f);
                    }
                        
                    //Draw white rectangle around target
                    XnaRect dr = new XnaRect((mloc.X - sx) * Gfx.ZoomSizeW - offx,
                        (mloc.Y - sy) * Gfx.ZoomSizeH - offy,
                        Gfx.ZoomSizeW, Gfx.ZoomSizeH);

                    Gfx.DrawRect(dr.X, dr.Y, dr.Width, dr.Height, Color.White, false, (int)(Math.Ceiling(2f * (float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH)));
                }
                else
                {
                    //Draw NO! icon
                    XnaRect dr = new XnaRect((mloc.X - sx) * Gfx.ZoomSizeW - offx,
                                    (mloc.Y - sy) * Gfx.ZoomSizeH - offy,
                                    Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                    sb.Draw(Gfx.NewGui, dr, new XnaRect(219, 96, 32, 32), Color.White);
                }

                //Draw crosshairs over already selected targets.
                if (Action.TargetSelectCount > 0)
                {
                    foreach (Location l in Action.TargetSelectList)
                    {
                        if (l.Inside(sx, sy, tw, th))
                        {
                            XnaRect sr = new XnaRect(((l.X - sx) * Gfx.ZoomSizeW - offx),
                                                 ((l.Y - sy) * Gfx.ZoomSizeH - offy), Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                            sb.Draw(Gfx.NewGui, sr, new XnaRect(195, 128, 48, 48), new Color(0, 0, 0, 180));
                        }
                    }
                }


            }
            sb.End();
        }

        public void MakeBloodStain(Location loc) {Misc[loc.X, loc.Y] |= Field.LARGE_BLOOD.Bit;}
        public void MakeCrater(Location loc) { Misc[loc.X, loc.Y] |= Field.CRATER.Bit; }

        void drawField(SpriteBatch sb, int x, int y, XnaRect r_dst)
        {
            foreach (Field fr in Field.VisibleList)
            {
                if ((Misc[x, y] & fr.Bit) != 0)
                {
                    //Don't draw crates or barrels here if a crate move animation is running.
                    if ((fr.Bit == Field.BARREL.Bit || fr.Bit == Field.CRATE.Bit) && fieldsThere(new Location(x, y), Field.CRATE_MOVE.Bit)) continue;

                    if (fieldsThere(new Location(x, y), Field.FIELD_APPEAR.Bit))
                    {
                        bool skip = false;
                        foreach (IAnimUnderlay underlay in Animation.EachUnderlayAnim())
                        {
                            if (underlay is Animation_FieldAppear && underlay.Pos == new Vector2(x,y) && (underlay as Animation_FieldAppear).Type == fr)
                            { skip = true; break; }
                        }
                        if (skip) 
                            continue;
                    }
                    sb.Draw(Gfx.FieldsGfx, r_dst, fr.GetSrcRect(), Color.White);
                }
            }
        }

        void drawDimBarrierFields(SpriteBatch sb, int x, int y, XnaRect r_dst)
        {
            foreach (Field fr in Field.BarrierList)
            {
                if ((Misc[x, y] & fr.Bit) != 0)
                {
                    sb.Draw(Gfx.FieldsGfx, r_dst, fr.GetSrcRect(), Color.Gray);
                }
            }
        }

        public void LoadFull(BinaryReader In) { //IMap
            int x, y, num;

            In.ReadString(); //Default script file - only used in the editor
            town_chop_time = In.ReadInt16();
            town_chop_key = In.ReadString();
            LightType = In.ReadInt16();
            Boundary = Rectangle.Read(In);
            CreatureKillLimit = In.ReadInt16();
            FuncOnEntry = In.ReadString();
            FuncOnExit = In.ReadString();
            FuncOnTurnHostile = In.ReadString();
            PreventMapping = In.ReadBoolean();
            PreventScrying = In.ReadBoolean();
            Difficulty = In.ReadInt16();
            num = In.ReadInt16();
            for (x = 0; x < num; x++)
                TriggerSpotList.Add(new TriggerSpot(In));

            num = In.ReadInt16();
            for (x = 0; x < num; x++)
                InfoRectList.Add(new InfoRect(In));

            for (x = 0; x < 4; x++) {
                EnterPos[x] = In.ReadLocation();
            }

            num = In.ReadInt16();
            for (x = 0; x < num; x++) PresetItemList.Add(new PresetItem(In));

            num = In.ReadInt16();
            for (x = 0; x < num; x++) PresetFieldList.Add(new PresetField(In));

            num = In.ReadInt16();
            for (x = 0; x < num; x++) CreatureStartList.Add(new NPCPreset(In));

            _Terrain = new ushort[Width, Height];
            for (x = 0; x < Width; x++)
                for (y = 0; y < Height; y++)
                    _Terrain[x, y] = In.ReadUInt16();//In.ReadByte();

            _Explored = new bool[Width, Height]; //Stores which tiles have been discovered in bit 1, and force walls etc in the other bits
        }

        public bool SetUpExitFunc()
        {
            if (FuncOnExit == null || FuncOnExit == "") return false;
            Script.New_ExitTown(FuncOnExit, GetDepartDirection(Party.Pos));
            return true;
        }

        //This is called every time a town is entered. 
        public void Enter(bool firsttime)
        {

            if (firsttime)
            {
                /// Called when town is visited for the first time, or when revisited after visiting the number of other towns defined in Game.TOWN_VISIT_MEMORY (4 in BoE)
                /// This repopulates the town's creature instances from the CreatureStart list.

                //erase_specials();
                Misc = new uint[Width, Height]; //Stores special enc dots, crates, barrels, magic barriers & quickfire in its bits

                GenerateLightMap();

                //Set any special encounter dots
                foreach (TriggerSpot se in TriggerSpotList)
                    Misc[se.Pos.X, se.Pos.Y] |= Field.SPECIAL.Bit;// 2;

                //Set any fields
                foreach (PresetField pf in PresetFieldList)
                {
                    Misc[pf.Pos.X, pf.Pos.Y] |= pf.Type.Bit;
                }

                //Clear any existing instances
                NPCList.Clear();

                //Populate creature instances from Town's CreatureStartList
                foreach (NPCPreset cs in CreatureStartList)
                {
                    cs.InstanceWasKilled = false; //Reset this.

                    if (cs.SpecialGroup == 0 && cs.Appear != eNPCAppear.NEVER_HERE)
                    {
                        NPC ci = NPC.Instantiate(cs);
                        if (ci != null) NPCList.Add(ci);
                    }
                }

                //Get rid of all items except the ones in the designated storage area.
                if (HasStorageArea)
                    for (int n = ItemList.Count - 1; n >= 0; n--)
                    {
                        Item item = ItemList[n];
                        if (!StorageArea.LocIn(item.Pos)) ItemList.Remove(item);
                    }
                
                for (int i = PresetItemList.Count - 1; i >= 0; i--) //Pop items down on the map if they're not there yet.
                {
                    PresetItem pitem = PresetItemList[i];

                    if (pitem.Instance == null)
                    {
                        pitem.Instance = Item.CopyFromPreset(pitem, this);
                        ItemList.Add(pitem.Instance);
                    }
                }
            }
            else //Town has been visited before (is on the recently visited list)
            {
                foreach (NPCPreset cs in CreatureStartList)
                {
                    NPC npc = NPCHasStarted(cs);
                    if (npc != null)
                    {
                        npc.Pos = cs.Pos; //Put npcs back into their original positions.
                    }
                }

                for (int n = NPCList.Count-1; n >= 0; n--)
                {
                    NPC npc = NPCList[n];

                    //Remove summoned creatures.
                    if (npc.Summoned != 0)
                        NPCList.Remove(npc);
                    else
                    {
                        //Remove creatures whose LifeVariable has been set to 1
                        if (npc.Start != null && GlobalVariables.Get(npc.Start.LifeVariable) == 1)
                            NPCList.Remove(npc);
                        else
                        {
                            //Restore creatures health, spell points, morale, afflictions.
                            npc.Health = npc.MaxHealth;
                            npc.Morale = npc.Record.Morale;
                            npc.SP = npc.Record.SP;
                            npc.ClearStatus();
                        }
                    }
                }

                //Remove temporary fields (fire walls etc)
                for (int x = 0; x < Width; x++)
                    for (int y = 0; y < Height; y++)
                        removeField(new Location(x, y), Field.ANTIMAGIC.Bit | Field.BLADE_WALL.Bit | Field.FIRE_WALL.Bit | Field.ICE_WALL.Bit | Field.FORCE_WALL.Bit | Field.SLEEP_CLOUD.Bit | Field.STINK_CLOUD.Bit);        
            }

            //Now put in or remove temporary NPCs
            foreach(NPCPreset s in CreatureStartList)
            {
                if (s.SpecialGroup != 0) continue; //NPCs with SpecialGroup set are only instantiated from scripts and Appear settings are ignored.
                if (s.InstanceWasKilled) continue; //If npc has previously been killed it don't need removing and shouldn't be added.
                if (GlobalVariables.Get(s.LifeVariable) == 1) continue; //If npc's LifeVariable is 1, it's dead already.
                NPC npc = NPCHasStarted(s);

                switch (s.Appear)
                {
                    case eNPCAppear.APPEAR_WHEN: //Appear on given day, unless event has occurred
                    
                        if (npc == null && Party.DayReached(s.AppearDay, s.AppearVariable))
                        {
                            NPC ci = NPC.Instantiate(s);
                            if (ci != null) NPCList.Add(ci);
                            s.Appear = eNPCAppear.ALWAYS_HERE; 
                        }
                        else if (npc != null && !Party.DayReached(s.AppearDay, s.AppearVariable))
                        {
                            NPCList.Remove(npc);
                        }
                        break;
                    case eNPCAppear.DISAPPEAR_WHEN:

                        if (npc == null && !Party.DayReached(s.AppearDay, s.AppearVariable))
                        {
                            NPC ci = NPC.Instantiate(s);
                            if (ci != null) NPCList.Add(ci);
                        }
                        else if (npc != null && Party.DayReached(s.AppearDay, s.AppearVariable))
                        {
                            NPCList.Remove(npc);
                            s.Appear = eNPCAppear.NEVER_HERE;
                        }
                        break;
                    case eNPCAppear.APPEAR_EVENT: //Appear when event has occurred
                        if (npc == null && GlobalVariables.Get(s.AppearVariable) > 0)
                        {
                            NPC ci = NPC.Instantiate(s);
                            if (ci != null) NPCList.Add(ci);
                            s.Appear = eNPCAppear.ALWAYS_HERE; 
                        }
                        else if (npc != null && GlobalVariables.Get(s.AppearVariable) == 0)
                            NPCList.Remove(npc);
                        break;
                    case eNPCAppear.DISAPPEAR_EVENT:
                        if (npc == null && GlobalVariables.Get(s.AppearVariable) == 0)
                        {
                            NPC ci = NPC.Instantiate(s);
                            if (ci != null) NPCList.Add(ci);
                        }
                        else if (npc != null && GlobalVariables.Get(s.AppearVariable) > 0)
                        {
                            NPCList.Remove(npc);
                            s.Appear = eNPCAppear.NEVER_HERE;
                        }
                        break;
                    case eNPCAppear.SOMETIMES_A:
                    case eNPCAppear.SOMETIMES_B:
                    case eNPCAppear.SOMETIMES_C:
                        if (npc == null && (Party.Age / 1000) % 3 == (int)(s.Appear - eNPCAppear.SOMETIMES_A))
                        {
                            NPC ci = NPC.Instantiate(s);
                            if (ci != null) NPCList.Add(ci);
                        }
                        else if (npc != null && (Party.Age / 1000) % 3 != (int)(s.Appear - eNPCAppear.SOMETIMES_A))
                            NPCList.Remove(npc);
                        break;
                    case eNPCAppear.USE_SCRIPT:
                        if (npc == null && Script.RunNonLatentFuncBool(s.AppearVariable)) //This doubles as the function name for this option.
                        {
                            NPC ci = NPC.Instantiate(s);
                            if (ci != null) NPCList.Add(ci);   
                        }
                        else if (npc != null && !Script.RunNonLatentFuncBool(s.AppearVariable))
                            NPCList.Remove(npc);
                        break;
                }
            }

            //Work out if the town should be classed as abandoned.
            //If town is abandoned because the quota of npcs has been killed, all npcs are removed.
            //If town is abandoned because a day has been reached, only friendly npcs are removed.
            bool removefriendlies = false, removehostiles = false;

            if (!Abandoned)
            {
                if (KillCount >= CreatureKillLimit)
                {
                    Abandoned = true;
                    removefriendlies = true;
                    removehostiles = true;
                }

                if (town_chop_time > 0)
                {
                    if (Party.DayReached(town_chop_time, town_chop_key))
                    {
                        removefriendlies = true; //Day has been reached, remove FRIENDLY npcs - hostiles remain
                        Abandoned = true;
                    }
                }

                if (Abandoned)
                {
                    for (int n = NPCList.Count - 1; n >= 0; n--)
                    {
                        if ((removehostiles && NPCList[n].IsABaddie) || (removefriendlies && !NPCList[n].IsABaddie)) NPCList.RemoveAt(n);
                    }
                }
            }
            //Abandoned runs the same script (write the script so that it checks for Towns abandoned property)
            //If no script on entry, do autosave now, otherwise save is done after entry function has run.

            if (!Game.InMainMenu)
            {
                if (FuncOnEntry == null || FuncOnEntry == "")
                    Game.AutoSave();
                else
                {
                    Script.New_General(FuncOnEntry, eCallOrigin.ENTERING_TOWN);
                    Script.NeedAutoSave = true;
                }
            }

            //Reset local town timers that need it
            Timer.ResetLocalTimers(this);

            new NewsLine("Now entering:", false, 200);
            new NewsLine(Name, true, 200);
        }

        public void PlaceEncounterGroup(int n, bool with_summon_animation = false)
        {
            foreach (NPCPreset s in CreatureStartList)
            {
                if (s.SpecialGroup == n)
                {
                    NPC ci = NPC.Instantiate(s);
                    if (ci != null) NPCList.Add(ci);

                    if (!CharacterCanBeThere(ci.Pos, ci))
                        ci.Pos = FindClearSpot(ci.Pos, true, false);

                    if (with_summon_animation)
                        new Animation_Summon(ci);
                }
            }

        }

        public void UpdateLightLevel()
        {
            if (LightType == 2) Party.LightLevel = Maths.Max(0, Party.LightLevel - 9);
            if (LightType == 3)
            {
                if (Party.LightLevel > 0) Game.AddMessage("Your light is drained.");
                Party.LightLevel = 0;
            }
        }

        public void MakeTownHostile()
        {
            Script.New_General(FuncOnTurnHostile, eCallOrigin.TOWN_GETS_ANGRY);


            Game.AddMessage("The town turns against you!");

            foreach(NPC npc in NPCList)
                if (npc.Summoned == 0)
                {
                    npc.Attitude = eAttitude.HOSTILE_A;
                    npc.Mobile = true;
                    if (npc.Record.SpecialSkill == eCSS.GUARD)
                    {
                        npc.Active = eActive.COMBATIVE;
                        npc.Health *= 3;
                        npc.SetStatus(eAffliction.HASTE_SLOW, 8);
                        npc.SetStatus(eAffliction.BLESS_CURSE, 8);
                    }
                }

        }

        public void StartNPCTurn() {

            //NPCs TURN:
            //This happens differently in non-combat and combat mode.

            //COMBAT MODE: All npcs get their action points assigned and spend them one by one. This includes moving, attacking, casting spells.
            //Each NPC moves one after the other.
            //   Each NPC gets action moves assigned.
            //   Each NPC runs DoCombatMove and uses their action points to move and attack. Because DoCombatMove is latent, each NPC moves one-by-one

            //NON-COMBAT MODE: All mobile npcs get to move one square at the start of the turn - all moves take place at the same time.
            //Then all npcs get ap assigned and spend their action points one by one as in combat mode - EXCEPT they only get a third of their AP (but at least 1)
            //and they CANNOT move.
            //   Each NPC runs DoNonCombatMove and moves no more than 1 tile. Because DoNonCombatMove is non-latent, all NPCs move simultaneously because the game runs the script function for
            //       each of them before it allows the script to pause to carry out their animations.
            //   Each NPC then has its AP assigned - At least 1 point but only a third of the amount given in a combat turn.
            //   The Latent function DoCombatMove is then run for each NPC as in a combat move - the script however bars NPCs from any further movement, so NPCs will attack if adjacent to their opponent or they can use
            //       a ranged ability, but otherwise will not act.

            handledAfflictions = false;
            //So do the non-combat moves first.
            if (Game.Mode == eMode.TOWN) {
                
                //In non-combat mode, all npcs move simultaneosly one square per turn. 
                for (int n = NPCList.Count-1; n >= 0; n--)
                {
                    NPC npc = NPCList[n];
                    npc.DoNonCombatMove();
                }

            } 

            //Now all NPCs are assigned their individual Action Points for this turn.

            NPCTurnQueue = new List<NPC>();

            foreach (NPC cur_monst in NPCList) //(i = 0; i < num_monst; i++)
            {  // Give monsters ap's, check activity

                // See if hostile monster notices party, during combat
                if (cur_monst.Active != eActive.COMBATIVE && cur_monst.IsABaddie && Game.Mode == eMode.COMBAT)
                {
                    int r1 = Maths.Rand(1, 1, 100); // Check if see PCs first
                    r1 += (Party.Stealth > 0) ? 45 : 0;
                    r1 += CanSee(cur_monst.Pos, Party.ClosestPC(cur_monst.Pos).Pos) * 10;
                    if (r1 < 50)
                        cur_monst.Active = eActive.COMBATIVE;
                    else
                    {
                        //If the creature is within 5 tiles of another combative npc, it also becomes combative
                        foreach (NPC m2 in NPCList)// (j = 0; j < T_M; j++)
                        {
                            if (m2 != cur_monst && m2.Active == eActive.COMBATIVE && m2.Pos.VDistanceTo(cur_monst.Pos) <= 5)
                            {
                                cur_monst.Active = eActive.COMBATIVE;
                            }
                        }
                    }
                }
                if (cur_monst.Active != eActive.COMBATIVE && cur_monst.IsABaddie)
                {
                    // Now it looks for PC-friendly monsters
                    // dist check is for efficiency
                    foreach (NPC m2 in NPCList)
                        if (!m2.IsABaddie && cur_monst.Pos.DistanceTo(m2.Pos) <= 6 && CanSee(cur_monst.Pos, m2.Pos) < Constants.OBSCURITY_LIMIT)
                            cur_monst.Active = eActive.COMBATIVE;
                }

                // See if friendly, fighting monster see hostile monster. If so, make mobile
                // dist check is for efficiency
                if (cur_monst.Active != eActive.COMBATIVE && cur_monst.Attitude == eAttitude.FRIENDLY)
                {
                    foreach (NPC m2 in NPCList)
                        if (m2.IsABaddie && cur_monst.Pos.DistanceTo(m2.Pos) <= 6 && CanSee(cur_monst.Pos, m2.Pos) < Constants.OBSCURITY_LIMIT)
                        {
                            cur_monst.Active = eActive.COMBATIVE;
                            cur_monst.Mobile = true;
                        }
                }
                // End of seeing if monsters see others

                cur_monst.AssignAP();

                // Now take care of summoned monsters

                if ((cur_monst.Summoned % 100) == 1)
                {
                    cur_monst.Dying = true;
                    new Animation_Death(cur_monst);
                    cur_monst.AP = 0;
                    Game.AddMessage(String.Format("  {0} disappears.", cur_monst.Name));
                }
                Maths.MoveToZero(ref cur_monst.Summoned);

                //Add the NPC to the turn queue if it has any AP to spend.
                if (cur_monst.AP > 0) NPCTurnQueue.Add(cur_monst);

                //Sort the list on the basis of how close they are to the PCs
            }

            new Animation_Hold();
        }

        /// <summary>
        /// Runs the next instalment of the NPCs' turn, running one NPC's action each time it is called
        /// </summary>
        /// <returns>True if all NPCs have finished moving, and the player's turn can commence.</returns>
        public bool DoNPCTurn()
        {
            //Only proceed if all animations are over.
            while (Animation.NoAnimationsRunning())
            {
                if (NPCTurnQueue.Count > 0) 
                {
                    NPC npc = NPCTurnQueue[0];

                    //Move the next monster in the queue
                    if (npc.DoCombatMove())
                    {
                        NPCTurnQueue.RemoveAt(0);
                    }

                    if (Game.Mode == eMode.COMBAT && _Visible[npc.Pos.X, npc.Pos.Y] != 0) Gfx.ScrollTo(npc.Pos);
                }

                //If the turn queue is empty, all NPCs have moved, so end the turn.
                if (NPCTurnQueue.Count == 0)
                {
                    if (!handledAfflictions)
                    {
                        NPC.StartofNPCAfflictions();
                        foreach (NPC npc in NPCList)
                        {
                            npc.HandleAfflictions();
                        }
                        handledAfflictions = true;
                        return false;
                    }
                    else
                    {
                        handledAfflictions = false;
                        return true;
                    }
                }
            } 

            return false;
        }
        static bool handledAfflictions = false;


        public void GenerateLightMap()
        {
            if (Script.suspendMapUpdate) return;
            // Find bonfires, braziers, etc.

            //Turn off all light field bits.
            for (int i = 0; i < Width; i++)
                for (int j = 0; j < Height; j++)
                {
                    var l = new Location(i,j);
                    removeField(l, Field.LIGHT.Bit);
                }

            for (int i = 0; i < Width; i++)
                for (int j = 0; j < Height; j++) 
                {
                    Location l = new Location(i,j);
                    int rad = TerrainAt(l).light_radius;
                    if (rad > 0) {
                        Location where;
                        for (where.X = Maths.Max(0, i - rad); where.X < Maths.Min(Width, i + rad + 1); where.X++)
                            for (where.Y = Maths.Max(0, j - rad); where.Y < Maths.Min(Height, j + rad + 1); where.Y++)
                                if (!fieldsThere(where, Field.LIGHT.Bit) && where.DistanceTo(l) <= rad && CanSee(l, where, true) < Constants.OBSCURITY_LIMIT)
                                    addField(where, Field.LIGHT.Bit);
                    }
                }
        }


        bool squareInLight(Location to_where)
        {
            if (LightType == 0) return true;
            if (!InBounds(to_where)) return true;
            if (fieldsThere(to_where, Field.LIGHT.Bit)) return true;

            int rad = getLightRadius();
            foreach(PCType pc in Party.EachIndependentPC()) 
                if (pc.Pos.DistanceTo(to_where) <= rad) return true;
            return false;
        }

        int getLightRadius()
        {
            int store = 1;
            int[] extra_levels = { 10, 20, 50, 75, 110, 140 };
            if (LightType == 0) return 200;
            for (int i = 0; i < 6; i++)
                if (Party.LightLevel > extra_levels[i])
                    store++;
            return store;
        }

        public string GetInfoRectString(Location pos)
        {
            if (pos.X == -1) return "";

            foreach (InfoRect i in InfoRectList)
            {
                if (i.Rect.LocIn(pos))
                    return i.Text;
            }
            return null;
        }


        /// <summary>
        /// Find whether the PC moving here should trigger a script
        /// </summary>
        /// <param name="pos"></param>
        /// <param name="dir"></param>
        /// <param name="pc"></param>
        /// <returns>True if script should run. Move should not be completed until script has finished and permitted it.</returns>
        public bool TriggerStepOnSpecials(Location pos, Direction dir, PCType pc, bool boat_landing)
        {
            string foundfunc = null;
            TriggerSpot foundspot = null;

            TerrainRecord ter = TerrainAt(pos);

            if (ter.Special == eTerSpec.UNLOCKABLE_BASHABLE || ter.Special == eTerSpec.UNLOCKABLE_TERRAIN)
                return false;

            if (fieldsThere(pos, Field.SPECIAL.Bit))
                //First look for special encounter nodes here
                foreach (TriggerSpot se in TriggerSpotList)
                {
                    if (se.Pos == pos &&
                        se.TriggeredBy(eTriggerSpot.PCS_TRIGGER) && 
                        ((Game.Mode == eMode.TOWN && se.TriggeredBy(eTriggerSpot.STEP_ON)
                        || Game.Mode == eMode.COMBAT && se.TriggeredBy(eTriggerSpot.STEP_ON_CMBT))))
                    {
                        foundfunc = se.Func;
                        foundspot = se;
                        break;
                    }
                }

            //Look for terrain type here with a trigger

            if (foundfunc == null) //Terrain triggers ignored if map trigger is on the same space.
            {
                if (ter.Trigger != null &&
                    ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER) && 
                    ((Game.Mode == eMode.TOWN && ter.Trigger.TriggeredBy(eTriggerSpot.STEP_ON)
                    || Game.Mode == eMode.COMBAT && ter.Trigger.TriggeredBy(eTriggerSpot.STEP_ON_CMBT))))
                {
                    foundfunc = ter.Trigger.Func;
                    foundspot = ter.Trigger;
                }
            }

            //Quit if no script function triggers found.
            if (foundfunc == null) return false;

            if (!boat_landing)
                Script.New_MapTrigger(foundfunc, eCallOrigin.MOVING, foundspot, pc, pos, dir);
            else
                Script.New_MapTrigger(foundfunc, eCallOrigin.BOATLAND, foundspot, pc, pos, dir);
                return true;
        }

        public bool PCCanTryToWalkThere(Location loc, PCType pc) 
        {
            //Can't walk out town boundary in combat mode
            if (Game.Mode == eMode.COMBAT && !InActArea(loc) && !(this is CombatMap))
            {
                if (!TerrainAt(loc).BlocksPC) 
                    Game.AddMessage("Can't leave town during combat.");
                return false;
            }

            //Can't go on force barriers
            if (fieldsThere(loc, Field.FORCE_BARRIER.Bit)) return false;

            //Can't step on another PC if the fella doesn't have enough AP to switch places.
            foreach (PCType pc2 in Party.EachAlivePC())
            {
                if (loc == pc2.Pos && pc2.AP == 0)
                    return false;
            }

            TerrainRecord ter = TerrainAt(loc);

            if (ter.Special == eTerSpec.UNLOCKABLE_BASHABLE || ter.Special == eTerSpec.UNLOCKABLE_TERRAIN || ter.Special == eTerSpec.CHANGE_WHEN_STEP_ON)
                return true;

            //Blocking terrain
            if (ter.BlocksPC) 
            {
                if (fieldsThere(loc, Field.SECRET_PASSAGE.Bit)) return true;
                return false;
            }
            return true;
        }

        public bool CharacterCanBeThere(Location location, ICharacter m_num, bool allow_leave_map = false)
        {
            for(int y = 0; y < (m_num == null ? 1 : m_num.Height); y++)
                for (int x = 0; x < (m_num == null ? 1 : m_num.Width); x++)
                {
                    Location loc = new Location(location.X + x, location.Y + y);

                    //Blocking terrain
                    if (m_num is PCType)
                    {
                        //If there is a special encounter node type 4 (Secret passage) PCs can be here
                        if (TerrainAt(loc).BlocksPC && !fieldsThere(loc, Field.SECRET_PASSAGE.Bit)) return false;//not_really_blocked = true;
                    }
                    else
                    {
                        TerrainRecord ter = TerrainAt(loc);
                        if (ter.BlocksNPC) return false;
                        if (m_num != null)
                        {
                            if (ter.Special == eTerSpec.DOES_FIRE_DAMAGE && !((NPC)m_num).Record.ImmuneTo(eImmunity.FIRE)) return false;
                            if (ter.Special == eTerSpec.DOES_COLD_DAMAGE && !((NPC)m_num).Record.ImmuneTo(eImmunity.COLD)) return false;
                            if (ter.Special == eTerSpec.DOES_MAGIC_DAMAGE && !((NPC)m_num).Record.ImmuneTo(eImmunity.MAGIC)) return false;
                            if (ter.Special == eTerSpec.POISON_LAND && !((NPC)m_num).Record.ImmuneTo(eImmunity.POISON)) return false;
                        }
                    }

                    //Stepping out the town boundary
                    if (!allow_leave_map && !InActArea(loc)) return false;

                    //Stepping on another character
                    ICharacter ch = CharacterThere(loc);
                    if (ch != null && (m_num == null || ch != m_num)) return false;

                    //Can't go on force barriers
                    if (fieldsThere(loc, Field.FORCE_BARRIER.Bit)) return false;

                    //NPCs can't walk on vehicles
                    if ((m_num == null || m_num is NPC) && Vehicle.IsThere(this, location) != null) return false;
                }
            return true;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="p1"></param>
        /// <param name="p2"></param>
        /// <param name="mode">0: normal</param>
        /// <returns></returns>
        public int CanSee(Location p1, Location p2, bool ignore_light=false)
        {
            int dx, dy, count, storage = 0;

             // Light check
            if (!ignore_light && !squareInLight(p2)) return Constants.OBSCURITY_LIMIT+1;

            if (p1.Y == p2.Y)
            {
                if (p1.X > p2.X)
                    for (count = p2.X + 1; count < p1.X; count++)
                        storage += GetObscurity(new Location(count, p1.Y));
                else
                    for (count = p1.X + 1; count < p2.X; count++)
                        storage += GetObscurity(new Location(count, p1.Y));
                return storage;
            }
            if (p1.X == p2.X)
            {
                if (p1.Y > p2.Y)
                    for (count = p1.Y - 1; count > p2.Y; count--)
                        storage += GetObscurity(new Location(p1.X, count));
                else
                    for (count = p1.Y + 1; count < p2.Y; count++)
                        storage += GetObscurity(new Location(p1.X, count));
                return storage;
            }
            dx = p2.X - p1.X;
            dy = p2.Y - p1.Y;

            if (Math.Abs(dy) > Math.Abs(dx))
            {
                if (p2.Y > p1.Y)
                    for (count = 1; count < dy; count++)
                        storage += GetObscurity(new Location(p1.X + (count * dx) / dy, p1.Y + count));
                else
                    for (count = -1; count > dy; count--)
                        storage += GetObscurity(new Location(p1.X + (count * dx) / dy, p1.Y + count));
                return storage;
            }
            if (Math.Abs(dy) <= Math.Abs(dx))
            {
                if (p2.X > p1.X)
                    for (count = 1; count < dx; count++)
                        storage += GetObscurity(new Location(p1.X + count, p1.Y + (count * dy) / dx));
                else
                    for (count = -1; count > dx; count--)
                        storage += GetObscurity(new Location(p1.X + count, p1.Y + (count * dy) / dx));
                return storage;
            }
            return 0;
        }

        //This was Mode 1 of CanSee, moved it because that was stupid.
        public int PCPlacementScore(Location p1, Location p2)
        {
            int count, storage = 0,
                dx = p2.X - p1.X,
                dy = p2.Y - p1.Y;

            // Light check
            if (!squareInLight(p2)) return Constants.OBSCURITY_LIMIT + 1;

            if (p1.Y == p2.Y)
                if (p1.X > p2.X)
                    for (count = p2.X + 1; count < p1.X; count++)
                    {
                        TerrainRecord ter = terrainAt(count, p1.Y);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;//(ter.Blockage >= eBlock.CLEAR_BLOCKED || ter.is_lava) && mode == 1)
                    }
                else
                    for (count = p1.X + 1; count < p2.X; count++)
                    {
                        TerrainRecord ter = terrainAt(count, p1.Y);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
            else if (p1.X == p2.X)
                if (p1.Y > p2.Y)
                    for (count = p1.Y - 1; count > p2.Y; count--)
                    {
                        TerrainRecord ter = terrainAt(p1.X, count);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
                else
                    for (count = p1.Y + 1; count < p2.Y; count++)
                    {
                        TerrainRecord ter = terrainAt(p1.X, count);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
            else if (Math.Abs(dy) > Math.Abs(dx))
                if (p2.Y > p1.Y)
                    for (count = 1; count < dy; count++)
                    {
                        TerrainRecord ter = terrainAt(p1.X + (count * dx) / dy, p1.Y + count);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
                else
                    for (count = -1; count > dy; count--)
                    {
                        TerrainRecord ter = terrainAt(p1.X + (count * dx) / dy, p1.Y + count);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
            else if (Math.Abs(dy) <= Math.Abs(dx))
                if (p2.X > p1.X)
                    for (count = 1; count < dx; count++)
                    {
                        TerrainRecord ter = terrainAt(p1.X + count, p1.Y + (count * dy) / dx);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
                else
                    for (count = -1; count > dx; count--)
                    {
                        TerrainRecord ter = terrainAt(p1.X + count, p1.Y + (count * dy) / dx);
                        storage += ter.Obscurity;
                        if (ter.DoNotPlacePC) return Constants.OBSCURITY_LIMIT;
                    }
            if (storage > Constants.OBSCURITY_LIMIT) return Constants.OBSCURITY_LIMIT;
            else return storage;
        }

        public ICharacter CharacterThere(Location pos, bool include_pcs = true, bool include_npcs = true)
        {
            if (include_npcs)
                foreach (NPC npc in NPCList)
                {
                    for (int y = 0; y < npc.Height; y++) 
                        for(int x =0; x < npc.Width; x++)
                            if (npc.Pos.Mod(x,y) == pos) return npc;
                }

            if (include_pcs)
                foreach (PCType pc in Party.EachIndependentPC())
                {
                    if (pc.Pos == pos) return pc;
                }
            return null;
        }

        public IEnumerable<ICharacter> EachCharacter()
        {
            foreach (PCType pc in Party.EachAlivePC()) yield return pc;
            foreach (NPC npc in NPCList) yield return npc;
        }

        /// <summary>
        /// Enumerates all characters at specified position
        /// </summary>
        /// <param name="pos">The location</param>
        /// <param name="only_independent">If true, only the pc party leader will be yielded if the party is all together (not in combat mode)</param>
        /// <returns>Each of them characters.</returns>
        public IEnumerable<ICharacter> EachCharacterThere(Location pos, bool include_pcs = true, bool include_npcs = true)
        {
            if (include_pcs)
                foreach (PCType pc in Party.EachAlivePC())
                {
                    if (pc.Pos == pos) yield return pc;
                }

            if (include_npcs)
            {
                for(int n = NPCList.Count-1;n>=0;n--)
                {
                    NPC npc = NPCList[n];

                    for (int y = 0; y < npc.Height; y++)
                        for (int x = 0; x < npc.Width; x++)
                            if (npc.Pos.Mod(x, y) == pos) yield return npc;
                }
            }
        }

        public IEnumerable<ICharacter> EachCharacterInRange(Location pos, int range, bool include_pcs = true, bool include_npcs = true)
        {
            if (include_pcs)
                foreach (PCType pc in Party.EachAlivePC())
                {
                    if (pos.VDistanceTo(pc.Pos) <= range)
                        yield return pc;
                }
            if (include_npcs)
                for (int n = NPCList.Count - 1; n >= 0; n--)
                {
                    NPC npc = NPCList[n];

                    bool done_that_one = false; //Prevent enemies bigger than one square getting counted more than once.
                    for (int y = 0; y < npc.Height; y++)
                    {
                        for (int x = 0; x < npc.Width; x++)
                            if (pos.VDistanceTo(npc.Pos.Mod(x, y)) <= range)
                            {
                                yield return npc;
                                done_that_one = true;
                                break;
                            }
                        if (done_that_one) break;
                    }
                }
        }

        public IEnumerable<ICharacter> EachCharacterAdjacent(Location pos, bool include_pcs = true, bool include_npcs = true)
        {
            if (include_pcs)
                foreach (PCType pc in Party.EachAlivePC())
                {
                    if (pos.adjacent(pc.Pos))
                        yield return pc;
                }
            if (include_npcs)
                for (int n = NPCList.Count - 1; n >= 0; n--)
                {
                    NPC npc = NPCList[n];

                    bool done_that_one = false; //Prevent enemies bigger than one square getting counted more than once.

                    for (int y = 0; y < npc.Height; y++)
                    {
                        for (int x = 0; x < npc.Width; x++)

                            if (pos.adjacent(npc.Pos.Mod(x, y)))
                            {
                                yield return npc;
                                done_that_one = true;
                                break;
                            }
                        if (done_that_one) break;
                    }
                }
        }

        public bool NoHostileNPCsLeft()
        {
            foreach (NPC npc in NPCList)
                if (npc.IsABaddie) return false;
            return true;
        }

        public bool NPCsSeeCrime(PCType pc)
        {
            foreach(NPC npc in NPCList)
            {
                if (!npc.IsABaddie && CanSee(pc.Pos, npc.Pos) < Constants.OBSCURITY_LIMIT)
                {
                    return true;
                }
            }
            return false;
        }

        public IEnumerable<Item> EachItemThere(Location pos, bool include_contained = false)
        {
            for(int n = ItemList.Count-1;n>=0;n--)
            {
                Item i = ItemList[n];

                if (_Visible[pos.X, pos.Y] != 0 && pos == i.Pos && (include_contained || !i.Contained))
                    yield return i;
            }
        }
        public IEnumerable<Item> EachItemInRange(Location pos, int range)
        {
            for (int n = ItemList.Count - 1; n >= 0; n--)
            {
                Item i = ItemList[n];
                if (_Visible[i.Pos.X, i.Pos.Y] != 0 && pos.VDistanceTo(i.Pos) <= range)
                    yield return i;
            }
        }


        public void UnlockTerrain(Location loc)
        {
            TerrainRecord terrain = TerrainAt(loc);
            if (terrain.Special != eTerSpec.UNLOCKABLE_TERRAIN && terrain.Special != eTerSpec.UNLOCKABLE_BASHABLE)
                return; //Can't unlock that!
            TerrainRecord to = terrain.Flag1 as TerrainRecord;

            if (terrain.Layer == 0 && to == null) return;
            if (to != null && to.Layer != terrain.Layer) return;

            AlterTerrain(loc, terrain.Layer, to);
            UpdateVisible();
        }

        public void AlterTerrain(Location pos, int layer, TerrainRecord newter)
        {
            if (!InBounds(pos)) return;

            if (layer == 0) //Underlay
            {
                if (newter != null && newter.Layer == 0)
                {
                    _Terrain[pos.X, pos.Y] &= 0xFF00; //Wipe lower (underlay) byte
                    _Terrain[pos.X, pos.Y] += (byte)newter.Num;
                    adjustItemContainment(pos);
                }
            }
            else if (layer == 1) //Overlay
            {
                ushort b = 0;
                if (newter == null) b = 0; //If null terrainrecord passed, wipe the overlay
                else if (newter.Layer != 1) return;
                else b = (ushort)(newter.Num << 8);
                _Terrain[pos.X, pos.Y] &= 0x00FF; //Wipe upper (overlay) byte
                _Terrain[pos.X, pos.Y] += b;
                adjustItemContainment(pos);
            }
        }

        public void DeactivateTrigger(Location pos)
        {
            foreach (TriggerSpot ts in TriggerSpotList)
            {
                if (ts.Pos == pos) ts.Active = false;
            }
        }
        public void ActivateTrigger(Location pos)
        {
            foreach (TriggerSpot ts in TriggerSpotList)
            {
                if (ts.Pos == pos) ts.Active = true;
            }
        }
        public bool DoStoodOnTriggers()
        {
            bool script_run = false;

            foreach (TriggerSpot tr in TriggerSpotList)
            {
                if (tr.TriggeredBy(eTriggerSpot.STOOD_ON))
                {
                    if (tr.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                    {
                        if (Game.Mode == eMode.TOWN && Party.LeaderPC != null && Party.LeaderPC.Pos == tr.Pos)
                        {
                            Script.New_StoodOn(tr, Party.LeaderPC);
                            script_run = true;
                        }
                        else
                            foreach (ICharacter ch in EachCharacterThere(tr.Pos, true, false))
                            {
                                Script.New_StoodOn(tr, ch);
                                script_run = true;
                            }
                    }

                    if (tr.TriggeredBy(eTriggerSpot.NPCS_TRIGGER))
                        foreach (ICharacter ch in EachCharacterThere(tr.Pos, false, true))
                        {
                            Script.New_StoodOn(tr, ch);
                            script_run = true;
                        }
                }
            }

            foreach (PCType pc in Party.EachIndependentPC())
            {
                TerrainRecord ter = terrainAt(pc.Pos.X, pc.Pos.Y);

                if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.STOOD_ON) && ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                {
                    Script.New_StoodOn(ter.Trigger, pc);
                    script_run = true;
                }
            }

            foreach(NPC npc in NPCList)
            {
                if (npc.Active != eActive.INACTIVE)
                {
                    TerrainRecord ter = terrainAt(npc.Pos.X, npc.Pos.Y);
                    if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.STOOD_ON) && ter.Trigger.TriggeredBy(eTriggerSpot.NPCS_TRIGGER))
                    {
                        Script.New_StoodOn(ter.Trigger, npc);
                        script_run = true;
                    }
                }
            }

            return script_run;
        }

        public string GetToolTipMessage(Location loc)
        {
            if (Party.NoOfLivingPCs == 0) return null;
            if (!InBounds(loc) || !_Explored[loc.X,loc.Y]) return null;

            StringBuilder sb = new StringBuilder();

            if (_Visible[loc.X, loc.Y] == 0) return null;
            
            bool first = true;
            foreach (ICharacter ch in EachCharacterThere(loc))
            {
                if (!first) sb.Append("\n"); else first = false;

                sb.Append(ch.TooltipInfo(true));
            }

            int count = 0;
            foreach (Item i in ItemList)
            {
                if (i.Pos == loc && !i.Contained)
                {
                    if (count < Constants.POPUP_ITEMLIST_LIMIT)
                    {
                        count++;
                        if (!first) sb.Append("\n"); else first = false;
                        sb.Append(i.TooltipInfo(true));
                    }
                    else
                    {
                        sb.Append("... More Items.");
                        break;
                    }
                }
            }

            var v = Vehicle.IsThere(this, loc);
            if (v != null)
            {
                if (!first) sb.Append("\n"); else first = false;
                sb.Append(char.ToUpper(v.Name[0]) + v.Name.Substring(1));
                sb.Append(v.PartyOwns ? " (yours)" : " (not yours)");
            }
            
            if (sb.Length == 0) return null;
            return sb.ToString();
        }

        public List<PopUpMenuData> GetPopUpMenuOptions(Location loc, Location frompos)
        {
            if (!InBounds(loc) || _Visible[loc.X, loc.Y]==0) return null; //Tile must be visible and on the map

            var options = new List<PopUpMenuData>();
            int dist = loc.VDistanceTo(frompos);

            //Talking options
            if (Game.Mode != eMode.COMBAT && dist <= 2)
            {
                foreach (ICharacter ch in EachCharacterThere(loc))
                {
                    if (ch is NPC)
                    {
                        NPC npc = (NPC)ch;
                        if (npc.Active != eActive.COMBATIVE && !npc.IsABaddie) //Can only talk if friendly
                        {
                            options.Add(new PopUpMenuData(String.Format("Talk to {0}", npc.Record.Name), npc, null, PopUpMenuData.TALK_TO));
                        }
                    }
                }
            }

            //Search options
            if (dist <= 1)
            {

                if (fieldsThere(loc, Field.CRATE.Bit | Field.BARREL.Bit))
                    options.Add(new PopUpMenuData(String.Format("Inspect the {0}", fieldsThere(loc, Field.CRATE.Bit) ? "crate" : "barrel"), loc, null, PopUpMenuData.SEARCH));
                else
                {
                    TerrainRecord ter = TerrainAt(loc);
                    options.Add(new PopUpMenuData(String.Format("Inspect {0}", ter.Name), loc, null, PopUpMenuData.SEARCH));
                }
            }

            //Can pick up items within 1 tile range in combat, or 4 outside of combat
            int count = 0;
            if ((Game.Mode != eMode.COMBAT && dist <= 4) || dist <= 1)
            {
                foreach (Item item in EachItemThere(loc))
                {
                    if (count == Constants.POPUP_ITEMLIST_LIMIT) break; //No more than 10 listed here.
                    options.Add(new PopUpMenuData(String.Format("Take {0}", item.KnownName), item, null, PopUpMenuData.TAKE));
                    count++;
                }
            }

            if (count >= 2)
                options.Add(new PopUpMenuData("Take all", loc, null, PopUpMenuData.TAKE_ALL));

            if (options.Count > 0) return options;
            return null;
        }

        public void HandleMapPopUp(object o, object o2, int data)
        {
            switch (data)
            {
            case PopUpMenuData.TALK_TO:
                 new Action(eAction.Talk) { NPC = (NPC)o };
                break;
            case PopUpMenuData.TAKE:
                new Action(eAction.TakeItemMap) { PC = Game.Mode == eMode.COMBAT ? Party.ActivePC : Party.CurrentPC, Item = (Item)o };

                break;
            case PopUpMenuData.TAKE_ALL:
                new Action(eAction.TakeAllItemMap) { PC = Game.Mode == eMode.COMBAT ? Party.ActivePC : Party.CurrentPC, Loc = (Location)o };
                break;
            case PopUpMenuData.SEARCH:
                new Action(eAction.Search) { PC = Game.Mode == eMode.COMBAT ? Party.ActivePC : Party.CurrentPC, Loc = (Location)o };
                break;
            }
        }

        /// <summary>
        /// Put an item onto the map
        /// </summary>
        /// <param name="item">Item to place. Make sure it is removed from wherever it was first.</param>
        /// <param name="ch">Character to place item at</param>
        public bool PlaceItem(Item item, Location pos)
        {
            item.Pos = pos;
            if (!ItemList.Contains(item)) ItemList.Add(item);
            if (is_container(pos))
                item.Contained = true;
            return true;
            
        }

        public void Search(Location spot, PCType pc)
        {
            string foundfunc=null;
            TriggerSpot foundspot = null;
            string s;
            if (fieldsThere(spot, Field.CRATE.Bit)) s = "Crate";
            else if (fieldsThere(spot, Field.BARREL.Bit)) s = "barrel";
            else if (fieldsThere(spot, Field.FORCE_BARRIER.Bit))  s = "Force Barrier"; 
            else if (fieldsThere(spot, Field.FIRE_BARRIER.Bit))  s = "Fire Barrier"; 
            else s = TerrainAt(spot).Name;

            Game.AddMessage("You inspect the " + s + ".");

            if (!fieldsThere(spot, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit))
            {
                //First look for special encounter nodes here
                foreach (TriggerSpot se in TriggerSpotList)
                {
                    if (se.Pos == spot && se.TriggeredBy(eTriggerSpot.SEARCH) && se.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                    {
                        foundfunc = se.Func;
                        foundspot = se;
                        break;
                    }
                }
                //Look for terrain type here with a trigger
                if (foundfunc == null) //Terrain triggers ignored if map trigger is on the same space.
                {
                    TerrainRecord ter = TerrainAt(spot);
                    if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.SEARCH) && ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                    {
                        foundfunc = ter.Trigger.Func;
                        foundspot = ter.Trigger;
                    }
                }
            }

            if (foundfunc != null)
                Script.New_MapTrigger(foundfunc, eCallOrigin.SEARCHING, foundspot, pc, spot, pc.Dir);
            else
                CompleteSearch(spot, false);
        }

        public void CompleteSearch(Location spot, bool did_script)
        {
            if ((TerrainAt(spot).Special == eTerSpec.IS_A_CONTAINER || fieldsThere(spot, Field.BARREL.Bit | Field.CRATE.Bit)) && !fieldsThere(spot,Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit))
            {
                LootSpot loot = LootSpot.Generate(spot, this, false);
                new LootWindow(loot);
            }
            else if (!did_script)
                Game.AddMessage("  But find nothing.");
        }

        public void UseTile(Location spot)
        {
            string foundfunc = null;
            TriggerSpot foundspot = null;

            Game.AddMessage("Use...");

            if (fieldsThere(spot, Field.WEB.Bit))
            {
                Game.AddMessage("  You clear the webs.");
                removeField(spot, Field.WEB.Bit);
            }

            //Push any barrels or whatnot.
            PushLocation(Party.ActivePC, spot);

            //First look for special encounter nodes here
            foreach (TriggerSpot se in TriggerSpotList)
            {
                if (se.Pos == spot && se.TriggeredBy(eTriggerSpot.USE) && se.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                {
                    foundfunc = se.Func;
                    foundspot = se;
                    break;
                }
            }
            if (foundfunc != null)
                Script.New_MapTrigger(foundfunc, eCallOrigin.USING, foundspot, Party.ActivePC, spot, Party.ActivePC.Dir);

            else
            {
                TerrainRecord ter = TerrainAt(spot);

                if (ter.Special == eTerSpec.CHANGE_WHEN_USED)
                {
                    TerrainRecord to = ter.Flag1 as TerrainRecord;

                    if (to != null || ter.Layer == 1)
                    {
                        if (spot == Party.ActivePC.Pos)
                        {
                            Game.AddMessage("  Not while on space.");
                            return;
                        }
                        Game.AddMessage("  OK.");
                        AlterTerrain(spot, to == null ? 1 : to.Layer, to);
                        return;
                    }
                }
                else if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.USE) && ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER))// eTerSpec.CALL_SPECIAL_WHEN_USED)
                {
                    Script.New_MapTrigger(ter.Trigger.Func, eCallOrigin.USING, ter.Trigger, Party.ActivePC, spot, Party.ActivePC.Dir);
                }
            }

        }

        // This damages a character, after they've moved into a square
        public void InflictFields(ICharacter which_m) {

            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.QUICKFIRE.Bit))
            {
                which_m.QuickfireMe();
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.BLADE_WALL.Bit))
            {
                which_m.BladeWallMe(null);
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.FORCE_WALL.Bit))
            {
                which_m.ForceWallMe(null);
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.SLEEP_CLOUD.Bit))
            {
                which_m.SleepCloudMe();
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.ICE_WALL.Bit))
            {
                which_m.IceWallMe(null);
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.STINK_CLOUD.Bit))
            {
                which_m.StinkCloudMe();
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.WEB.Bit))//((is_web(where_check)) && (which_m.Record.Genus != eGenus.BUG))
            {
                which_m.WebSpaceMe();
                removeFieldArea(which_m.Pos, which_m.Width, which_m.Height, Field.WEB.Bit);
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.FIRE_WALL.Bit))
            {
                which_m.FireWallMe(null);
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.FIRE_BARRIER.Bit))
            {
                which_m.FireBarrierMe();
            }
            if (fieldsThereArea(which_m.Pos, which_m.Width, which_m.Height, Field.CRATE.Bit | Field.BARREL.Bit))
            {
                //NPCs destroy barrels and crates if they step on them.
                if (which_m is NPC)
                {
                    foreach (Item item in EachItemThere(which_m.Pos, true)) item.Contained = false;
                    removeFieldArea(which_m.Pos, which_m.Width, which_m.Height, Field.CRATE.Bit | Field.BARREL.Bit);
                }
            }
        }

        public Boolean NPCHateSpot(NPC ch, Location pos){
            NPCRecord record = ((NPC)ch).Record;

            for(int x = pos.X; x < pos.X + ch.Width; x++)
                for (int y = pos.Y; y < pos.Y + ch.Height; y++)
                {
                    if (((Misc[x, y] & (Field.BLADE_WALL.Bit | Field.FORCE_BARRIER.Bit | Field.FIRE_BARRIER.Bit | Field.QUICKFIRE.Bit)) != 0)

                    || ((Misc[x, y] & Field.ICE_WALL.Bit) != 0 && record.Radiate != eRadiate.ICE
                        && !record.ImmuneTo(eImmunity.COLD_IMMUNITY)) // hate ice wall?

                    || ((Misc[x, y] & Field.FIRE_WALL.Bit) != 0 && record.Radiate != eRadiate.FIRE
                        && !record.ImmuneTo(eImmunity.FIRE_IMMUNITY)) // hate fire wall?

                    || ((Misc[x, y] & Field.STINK_CLOUD.Bit) != 0 && record.Radiate != eRadiate.STINK
                        && !record.ImmuneTo(eImmunity.MAGIC)) // hate stink cloud?

                    || ((Misc[x, y] & Field.SLEEP_CLOUD.Bit) != 0 && record.Radiate != eRadiate.SLEEP
                        && !record.ImmuneTo(eImmunity.MAGIC)) // hate sleep cloud?

                    || ((Misc[x, y] & Field.FORCE_WALL.Bit) != 0 && record.Radiate != eRadiate.SHOCK
                        && !record.ImmuneTo(eImmunity.MAGIC_IMMUNITY)) // hate shock cloud?

                    || ((record.MageLevel > 0 || record.PriestLevel > 0)
                         && (Misc[x, y] & Field.ANTIMAGIC.Bit) != 0))
                        return true;// hate antimagic
                }
            return false;
        }

        eBlock2 blockageThere(Location loc)
        {
            return terrainAt(loc.X, loc.Y).Blockag;
        }

        bool drawBoundaryThere(Location loc)
        {
            var ter = terrainAt(loc.X, loc.Y);
            return (Visible(loc) && (ter.Blockag != eBlock2.BLOCKED || ter.BoatOver));
        }

        bool opaqueThere(Location loc)
        {
            return terrainAt(loc.X, loc.Y).Obscurity >= Constants.OBSCURITY_LIMIT;
        }



        // Looks at all spaces within 2, looking for a spot which is clear of nastiness and beings
        // returns {0,0} if none found
        // THIS MAKES NO ADJUSTMENTS FOR BIG MONSTERS!!!
        public Location FindClearSpot(Location from_where, bool prefer_adjacent, bool in_line_of_sight)
        {
            List<Location> spots = new List<Location>();

            for (int x = from_where.X - 2; x <= from_where.X + 2; x++)
                for (int y = from_where.Y - 2; y <= from_where.Y + 2; y++) {
                    Location loc = new Location(x, y);
                    if (loc == from_where) continue;

                    if (
                        (InActArea(loc) && CharacterCanBeThere(loc, null) && !fieldsThere(loc, Field.BARREL.Bit | Field.CRATE.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.ANTIMAGIC.Bit | Field.BLADE_WALL.Bit | Field.FIRE_WALL.Bit | Field.FORCE_WALL.Bit | Field.ICE_WALL.Bit | Field.SLEEP_CLOUD.Bit | Field.STINK_CLOUD.Bit))
                        && (!in_line_of_sight || CanSee(from_where, loc) < Constants.OBSCURITY_LIMIT))
                        spots.Add(loc);
                    
                }

            if (spots.Count == 0) return from_where;

            if (prefer_adjacent) //If prefer adjacent spaces
                if (spots.Count(n => n.adjacent(from_where)) > 0) //See if there are some adjacent spaces in the list
                    for (int i = spots.Count-1; i >= 0; i--) //If so, remove all non-adjacent spaces.
                        if (!spots[i].adjacent(from_where)) spots.RemoveAt(i);

            //Return a random entry in the list.
            return spots[Maths.Rand(1, 0, spots.Count - 1)];
        }

        public bool PushLocation(ICharacter pc, Location pos)
        {
            //Pushing crates and barrels about
            if (!fieldsThere(pos, Field.CRATE.Bit | Field.BARREL.Bit)) return false;
            
            bool is_crate = false;
            if (fieldsThere(pos, Field.CRATE.Bit))
            {
                is_crate = true;
            }

            //Work out a jolly good new place to put the barrel.
            Location loc_to_try = pos;
            loc_to_try.X = loc_to_try.X + (pos.X - pc.Pos.X); //New pos is one space away from pushing character
            loc_to_try.Y = loc_to_try.Y + (pos.Y - pc.Pos.Y);
            TerrainRecord ter = TerrainAt(loc_to_try);

            if (TerrainAt(loc_to_try).DestroysBarrels)
            {
                // Destroy crate
                foreach (Item item in EachItemThere(pos, true))
                { if (item.Contained) ItemList.Remove(item); }
                removeField(pos, Field.CRATE.Bit | Field.BARREL.Bit);
                new Animation_CrateMove(pos, loc_to_try, is_crate, true);
                return true;
            }

            else if (GetObscurity(loc_to_try) > 0 || blockageThere(loc_to_try) > 0 || !InActArea(loc_to_try) || CharacterThere(loc_to_try) != null)
            {
                if (GetObscurity(pc.Pos) > 0 || blockageThere(pc.Pos) > 0) return false; //Can't be pushed.
                loc_to_try = pc.Pos;
            }

            removeField(pos, is_crate ? Field.CRATE.Bit : Field.BARREL.Bit);
            addField(loc_to_try, (is_crate ? Field.CRATE.Bit : Field.BARREL.Bit) | Field.CRATE_MOVE.Bit);
            new Animation_CrateMove(pos, loc_to_try, is_crate, false);

            foreach (Item item in EachItemThere(pos, true))
            { if (item.Contained) item.Pos = loc_to_try; }
            return true;
        }

        public bool CheckSpecialTerrainPC(Location pos, PCType pc) {
            TerrainRecord ter = terrainAt(pos.X, pos.Y);
            bool can_enter = true;

            PushLocation(pc, pos);

            //Now consider the special effects of the terrain we have just stepped on.
            switch (ter.Special) {
                case eTerSpec.CHANGE_WHEN_STEP_ON:
                    
                    if (ter.Flag1 != null || ter.Layer > 0)
                    {
                        TerrainRecord to = ter.Flag1 as TerrainRecord;

                        AlterTerrain(pos, to == null ? 1 : to.Layer, to);
                        UpdateVisible();
                        Sound.Play((string)ter.Flag2);

                    }

                    if (ter.BlocksPC) can_enter = false;
                    break;

                //Locked doors
                case eTerSpec.UNLOCKABLE_TERRAIN:
                case eTerSpec.UNLOCKABLE_BASHABLE:
                    if (Game.Mode == eMode.COMBAT)
                       // No lockpicking in combat
                        Game.AddMessage("  Can't enter: It's locked.");
                    else
                        new LockpickWindow(pos);
                    return false;
            }
            return can_enter;
        }

        public void DoNastyTerrain(Location pos)
        {
            bool report = true;
            TerrainRecord ter = TerrainAt(pos);

            foreach (PCType pc in EachCharacterThere(pos))
            {
                ter.NastyTerrainEffect(pc, report);
                report = false;
            }
        }

        public bool CheckNPCDoors(Location pos, NPC npc)
        {
            switch(TerrainAt(pos).Special)
            {
                case eTerSpec.BLOCKED_TO_MONSTERS: return false;
                case eTerSpec.CHANGE_WHEN_STEP_ON:

                    if (npc.Active != eActive.COMBATIVE) return false; //Only fightin' npcs open doors.

                    var ter = TerrainAt(pos);

                    if (ter.Flag1 != null || ter.Layer > 0)
                    {
                        TerrainRecord to = ter.Flag1 as TerrainRecord;
                        AlterTerrain(pos, to == null ? 1 : to.Layer, to);
                        UpdateVisible();
                        Sound.Play((string)ter.Flag2);
                    }
                    if (ter.BlocksNPC) return false;
                    break;
            }
            return true;
        }

        public int GetObscurity(Location l) 
        {      
            TerrainRecord what_terrain = TerrainAt(l);
            int store = what_terrain.Obscurity;
            store += fieldObscurityThere(l);
            return store;
        }

        public void PlacePartyForCombat(eDir dir) {

            Location[] hor_vert_place = {new Location(0,0),new Location(-1,1),new Location(1,1),new Location(-2,2),new Location(0,2),
								         new Location(2,2),new Location(0,1),new Location(-1,2),new Location(1,2),new Location(-1,3),
								         new Location(1,3),new Location(0,3),new Location(0,4),new Location(0,5)};
            Location[] diag_place = {new Location(0,0),new Location(-1,0),new Location(0,1),new Location(-1,1),new Location(-2,0),
							         new Location(0,2),new Location(-2,1),new Location(-1,2),new Location(-2,2),new Location(-3,2),
							         new Location(-2,3),new Location(-3,3),new Location(-4,3),new Location(-3,4)};

            Boolean[] spot_ok = {true,true,true,true,true,true,true,
							        true,true,true,true,true,true,true};
            Location[] pos_locs = new Location[14]; //[14];
            Location check_loc;
            int x_adj, y_adj, how_many_ok = 1, where_in_a = 0, i;

            int direction = (int)dir;

            for (i = 0; i < 14; i++) {
                check_loc = Party.Pos;// c_town.p_loc;
                if (direction % 4 < 2)
                    x_adj = ((direction % 2 == 0) ? hor_vert_place[i].X : diag_place[i].X);
                else x_adj = ((direction % 2 == 0) ? hor_vert_place[i].Y : diag_place[i].Y);
                if (direction % 2 == 0)
                    x_adj = (direction < 4) ? x_adj : -1 * x_adj;
                else x_adj = ((direction == 1) || (direction == 7)) ? -1 * x_adj : x_adj;
                check_loc.X -= x_adj;
                if (direction % 4 < 2)
                    y_adj = ((direction % 2 == 0) ? hor_vert_place[i].Y : diag_place[i].Y);
                else y_adj = ((direction % 2 == 0) ? hor_vert_place[i].X : diag_place[i].X);
                if (direction % 2 == 0)
                    y_adj = ((direction > 1) && (direction < 6)) ? y_adj : -1 * y_adj;
                else y_adj = ((direction == 3) || (direction == 1)) ? -1 * y_adj : y_adj;

                check_loc.Y -= y_adj;
                pos_locs[i] = check_loc;
                if (InActArea(check_loc) 
                    && !TerrainAt(check_loc).BlocksPC && !fieldsThere(check_loc, Field.SPECIAL.Bit)  
                    && GetObscurity(check_loc) == 0 && PCPlacementScore(Party.Pos, check_loc) < 1 && CharacterThere(check_loc)==null) {
                     spot_ok[i] = true;
                     how_many_ok += (i > 1) ? 1 : 0;
                } 
                else 
                    spot_ok[i] = false;

                if (i == 0)
                    spot_ok[i] = true;
            }

            foreach (PCType pc in Party.EachAlivePC()) {
                if (how_many_ok == 1)
                    pc.Pos = pos_locs[where_in_a];
                else {
                    pc.Pos = pos_locs[where_in_a];
                    if (how_many_ok > 1)
                        where_in_a++;
                    how_many_ok--;
                    while (spot_ok[where_in_a] == false) where_in_a++;
                }

                if (pc.Pos != Party.Pos) new Animation_Move(pc, Party.Pos, pc.Pos, false);
            }

            //Reset all npcs target so they might choose a pc to pursue now they are all independent on the map
            foreach (NPC ci in NPCList)
                ci.Target = null;
        }

        public void DispelFieldPattern(Pattern pattern, Location center, int mode)
        {
            // First actually make barriers, then draw them, then inflict damaging effects.
            for (int i = Maths.MinMax(0, Width - 1, center.X - 4); i <= Maths.MinMax(0, Width - 1, center.X + 4); i++)
            {
                for (int j = Maths.MinMax(0, Height - 1, center.Y - 4); j <= Maths.MinMax(0, Height - 1, center.Y + 4); j++)
                {
                    Location spot = new Location(i,j);

                    if (center == spot || CanSee(center, spot) < Constants.OBSCURITY_LIMIT)
                    {
                        if (pattern[i - center.X + 4, j - center.Y + 4] > 0)
                            DispelFields(spot, mode);
                    }
                }
            }
        }

        public void PlaceFieldPattern(Pattern pattern, Location center, Field type, IExpRecipient who_hit)
        {
            int i, j;
            Location spot_hit;
            Location s_loc;

            Field[,] pat = new Field[9, 9];
            for (i = 0; i < 9; i++) 
                for (j = 0; j < 9; j++)
                {
                    if (type == null)
                        pat[j, i] = Field.List[pattern[j, i]]; //Use the fields already in the pattern object
                    else
                        if (pattern[j, i] > 0) pat[j, i] = type;
                }

            // eliminate barriers that can't be seen
            for (i = (int)Maths.MinMax(Boundary.Left, Boundary.Right, (long)center.X - 4);
             i <= Maths.MinMax(Boundary.Left, Boundary.Right, (long)center.X + 4); i++)
                for (j = (int)Maths.MinMax(Boundary.Top, Boundary.Bottom, (long)center.Y - 4);
                 j <= Maths.MinMax(Boundary.Top, Boundary.Bottom, (long)center.Y + 4); j++)
                {
                    s_loc.X = i; s_loc.Y = j;
                    if (CanSee(center, s_loc) >= Constants.OBSCURITY_LIMIT)
                        pat[i - center.X + 4, j - center.Y + 4] = null;// 0;
                }

            // First actually make barriers, then draw them, then inflict damaging effects.
            for (i = Maths.MinMax(0, Width - 1, center.X - 4); i <= Maths.MinMax(0, Width - 1, center.X + 4); i++)
            {
                for (j = Maths.MinMax(0, Height - 1, center.Y - 4); j <= Maths.MinMax(0, Height - 1, center.Y + 4); j++)
                {
                    if (GetObscurity(new Location(i, j)) < Constants.OBSCURITY_LIMIT)
                    {
                        Field effect = pat[i - center.X + 4, j - center.Y + 4];
                        if (effect != null)
                        {
                            spot_hit.X = i;
                            spot_hit.Y = j;
                            PlaceField(spot_hit, effect);
                        }
                    }
                }
            }
            new Animation_Hold();

            foreach (ICharacter ch in EachCharacterInRange(center, 5))
            {
                if (ch is PCType && ch != Party.LeaderPC && Game.Mode != eMode.COMBAT) continue;

                bool done_that_one = false;

                for (i = Maths.MinMax(0, Width - 1, center.X - 4); i <= Maths.MinMax(0, Width - 1, center.X + 4); i++)
                {
                    for (j = Maths.MinMax(0, Height - 1, center.Y - 4); j <= Maths.MinMax(0, Height - 1, center.Y + 4); j++)
                    {
                        spot_hit.X = i;
                        spot_hit.Y = j;
                        if (!done_that_one && GetObscurity(spot_hit) < Constants.OBSCURITY_LIMIT && ch.OnSpace(spot_hit))
                        {
                            Field effect = pat[i - center.X + 4, j - center.Y + 4];

                            if (effect != null) done_that_one = true;

                            if (effect == Field.WEB) ch.WebSpaceMe();//(3);
                            else if (effect == Field.FORCE_WALL) ch.ForceWallMe(who_hit);
                            else if (effect == Field.FIRE_WALL) ch.FireWallMe(who_hit);
                            else if (effect == Field.STINK_CLOUD) ch.StinkCloudMe();
                            else if (effect == Field.ICE_WALL) ch.IceWallMe(who_hit);
                            else if (effect == Field.BLADE_WALL) ch.BladeWallMe(who_hit);
                            else if (effect == Field.SLEEP_CLOUD) ch.SleepCloudMe();
                        }
                    }
                }
            }
        }

        public void ProcessFields()
        {
            //Spread quickfire
            int[,] qf = new int[Width,Height];

            for (int x = 0; x < Width; x++)
                for (int y = 0; y < Height; y++)
                    qf[x, y] = fieldsThere(new Location(x, y), Field.QUICKFIRE.Bit) ? 1 : 0;

            for (int k = 0; k < (Game.Mode == eMode.COMBAT ? 4 : 1); k++)
            {
                for (int x = 1; x < Width-1; x++)
                    for (int y = 1; y < Height-1; y++)
                        if (fieldsThere(new Location(x, y), Field.QUICKFIRE.Bit) && Maths.Rand(1, 1, 8) != 1)
                        {
                            if (qf[x - 1, y] == 0) qf[x - 1, y] = 1;
                            if (qf[x + 1, y] == 0) qf[x + 1, y] = 1;
                            if (qf[x, y - 1] == 0) qf[x, y - 1] = 1;
                            if (qf[x, y + 1] == 0) qf[x, y + 1] = 1;
                        }
                for (int x = 0; x < Width; x++)
                    for (int y = 0; y < Height; y++)
                        if (qf[x, y] == 1) { MakeQuickfire(new Location(x, y)); qf[x, y] = 2; };
            }

            //Fields decaying
            for (int x = 0; x < Width; x++)
                for (int y = 0; y < Height; y++)
                {
                    var l = new Location(x,y);

                    if (fieldsThere(l, Field.FORCE_WALL.Bit))
                    {
                        if (Maths.Rand(1, 1, 6) == 2) removeField(l, Field.FORCE_WALL.Bit);
                    }
                    if (fieldsThere(l, Field.ICE_WALL.Bit))
                    {
                        if (Maths.Rand(1, 1, 6) == 1) removeField(l, Field.ICE_WALL.Bit);
                    }
                    if (fieldsThere(l, Field.FIRE_WALL.Bit))
                    {
                        if (Maths.Rand(1, 1, 4) == 2) removeField(l, Field.FIRE_WALL.Bit);
                    }
                    if (fieldsThere(l, Field.BLADE_WALL.Bit))
                    {
                        if (Maths.Rand(1, 1, 5) == 1) removeField(l, Field.BLADE_WALL.Bit);
                    }
                    if (fieldsThere(l, Field.ANTIMAGIC.Bit))
                    {
                        if (Maths.Rand(1, 1, 8) == 2) removeField(l, Field.ANTIMAGIC.Bit);
                    }
                    if (fieldsThere(l, Field.STINK_CLOUD.Bit))
                    {
                        if (Maths.Rand(1, 1, 4) == 2) removeField(l, Field.STINK_CLOUD.Bit);
                    }
                    if (fieldsThere(l, Field.SLEEP_CLOUD.Bit))
                    {
                        if (Maths.Rand(1, 1, 4) == 2) removeField(l, Field.SLEEP_CLOUD.Bit);
                    }
                }

            //Damage from fields
            foreach (ICharacter ch in EachCharacter())
                InflictFields(ch);
        }

        // returns true if placement was successful
        public Boolean SummonMonster(ICharacter summoner, NPCRecord which, Location where, int duration)
        {
            if (which == null) return false;
            //For an NPC type, 'where' is the summoner's location, and the summoned monster is put in a nearby spot.
            //Or if the position is the summoner's position, it might be a PC using a summony item.
            if (summoner is NPC || summoner.Pos == where)
            {
                where = FindClearSpot(where, false, true);
                if (where == summoner.Pos) return false;
            }

            if (NPCList.Count >= Constants.AREA_NPC_LIMIT)
            {
                if (duration < 100)
                    Game.AddMessage("  Too many monsters.");
                return false;
            }

            NPC spot = NPC.Summon(which, where, summoner.MyAttitude(), duration);

            if (!CharacterCanBeThere(where, spot))
                return false;

            NPCList.Add(spot);
            new Animation_Summon(spot);
            Game.AddMessage(String.Format("  {0} summoned.", spot.Name));
            return true;
        }

        public NPC PlaceNewNPC(NPCRecord which, Location where, bool force)
        {
            NPC npc = NPC.Instantiate(which, where);
            if (!force && !CharacterCanBeThere(where, npc)) return null;
            if (!force && NPCList.Count >= Constants.AREA_NPC_LIMIT) return null;
            NPCList.Add(npc);
            return npc;
        }

        public void SplitOffMonster(NPC from_who)
        {
            if (NPCList.Count >= Constants.AREA_NPC_LIMIT) return;

            Location where_put = FindClearSpot(from_who.Pos, true, true);
            if (where_put == from_who.Pos) return;

            NPC newone = NPC.SplitOffCopy(from_who, where_put);
            NPCList.Add(newone);

            Game.AddMessage(String.Format("  {0} splits!.", from_who.Name));
        }

        public bool HitArea(Location centre_pos, int damage_multiplier, int damage_low, int damage_high, eDamageType dam_type, Pattern pattern, bool makes_crater, IExpRecipient hitter)
        {
            if (damage_high <= 0) damage_high = damage_low;
            bool has_hit_someone = false;
            var hashit = new List<ICharacter>(); //Keep a list of who was hit so they don't get hit twice (NPCs that take up more than one tile)

            foreach (Location pos in pattern.EachPatternSpot(centre_pos))
            {
                if (fieldsThere(pos, Field.ANTIMAGIC.Bit) && (dam_type == eDamageType.MAGIC || dam_type == eDamageType.FIRE || dam_type == eDamageType.COLD)) continue;

                int damage = Maths.Rand(damage_multiplier, damage_low, damage_high);

                if (damage > 0)
                    foreach (ICharacter ch in EachCharacterThere(pos))
                    {
                        if (!hashit.Contains(ch))
                        {
                            hashit.Add(ch);
                            has_hit_someone |= ch.Damage(hitter, damage, 0, dam_type);
                        }
                    }
            }

            if (makes_crater && GetObscurity(centre_pos) == 0 && !TerrainAt(centre_pos).BlocksPC) 
                addField(centre_pos, Field.CRATER.Bit);

            if (!has_hit_someone) Game.AddMessage("No damage.");

            return has_hit_someone;
        }

        /// <summary>
        /// When a terrain changes or barrel/crate gets placed or removed, make sure the Contained property for all the items
        /// in the square is updated.
        /// </summary>
        /// <param name="pos"></param>
        void adjustItemContainment(Location pos)
        {
            if (is_container(pos))
                foreach (Item i in EachItemThere(pos))
                    i.Contained = true;
            else
                foreach (Item i in EachItemThere(pos, true))
                    i.Contained = false;
        }     

        public bool fieldsThere(Location loc, uint bits)
        {
            return (Misc[loc.X, loc.Y] & bits) != 0;
        }
        bool fieldsThereArea(Location loc, int w, int h, uint bits)
        {
            for (int x = loc.X; x < loc.X + w; x++)
            {
                for (int y = loc.Y; y < loc.Y + h; y++)
                {
                    if ((Misc[x, y] & bits) != 0) return true;
                }
            }
            return false;
        }
        int fieldObscurityThere(Location loc)
        {
            int o = 0;

            if ((Misc[loc.X, loc.Y] & Field.ObscurityMask) == 0)
                return 0;

            foreach (Field f in Field.ObscuringList)
            {
                if (fieldsThere(loc, f.Bit)) o += f.Obscurity;
            }
            return o;
        }

        public bool FieldThere(Location loc, Field field)
        {
            return fieldsThere(loc, field.Bit);
        }

        public void RemoveField(Location loc, Field field)//eField field)
        {
            removeField(loc, field.Bit);
        }

        public void PlaceField(Location loc, Field field)
        {

            if (field == Field.ANTIMAGIC) make_antimagic(loc);
            else if (field == Field.BLADE_WALL) make_blade_wall(loc, null); 
            else if (field == Field.FIRE_BARRIER) MakeFireBarrier(loc); 
            else if (field == Field.FIRE_WALL) make_fire_wall(loc, null); 
            else if (field == Field.FORCE_BARRIER) MakeForceBarrier(loc); 
            else if (field == Field.FORCE_WALL) make_force_wall(loc, null); 
            else if (field == Field.ICE_WALL) make_ice_wall(loc, null); 
            else if (field == Field.QUICKFIRE) MakeQuickfire(loc); 
            else if (field == Field.SLEEP_CLOUD) make_sleep_cloud(loc); 
            else if (field == Field.STINK_CLOUD) make_scloud(loc); 
            else if (field == Field.WEB) make_web(loc);
            else
            {
                if (GetObscurity(loc) > 0) return;
                if (blockageThere(loc) != eBlock2.CLEAR) return;

                if (field == Field.BARREL)
                {
                    removeField(loc, Field.CRATE.Bit);
                    addField(loc, Field.BARREL.Bit);
                    adjustItemContainment(loc);
                }
                else if (field == Field.CRATE)
                {
                    removeField(loc, Field.BARREL.Bit);
                    addField(loc, Field.CRATE.Bit);
                    adjustItemContainment(loc);
                }

                else if (field == Field.SMALL_BLOOD || field == Field.MEDIUM_BLOOD || field == Field.LARGE_BLOOD)
                {
                    Field b = field;
                    if (fieldsThere(loc, Field.MEDIUM_BLOOD.Bit)) b = Field.LARGE_BLOOD;
                    else if (field == Field.SMALL_BLOOD && fieldsThere(loc, Field.SMALL_BLOOD.Bit)) b = Field.MEDIUM_BLOOD;
                    removeField(loc, Field.SMALL_BLOOD.Bit | Field.MEDIUM_BLOOD.Bit | Field.LARGE_BLOOD.Bit);
                    addField(loc, b.Bit);
                }
                else if (field == Field.SMALL_SLIME || field  == Field.LARGE_SLIME)
                {
                    Field b = field;
                    if (fieldsThere(loc, Field.SMALL_SLIME.Bit)) b = Field.LARGE_SLIME;
                    removeField(loc, Field.SMALL_SLIME.Bit | Field.LARGE_SLIME.Bit);
                    addField(loc, b.Bit);
                }
                else
                    addField(loc, field.Bit);
            }

        }

        void removeField(Location l, uint bits) { Misc[l.X, l.Y] &= bits ^ uint.MaxValue; }
        void removeFieldArea(Location l, int w, int h, uint bits)
        {
            for (int x = l.X; x < l.X + w; x++)
            {
                for (int y = l.Y; y < l.Y + h; y++)
                {
                    Misc[x, y] &= bits ^ uint.MaxValue;
                }
            }
        }


        void addField(Location l, uint bits) { Misc[l.X, l.Y] |= bits; } 

        void make_web(Location l)
        {
            if (fieldsThere(l, Field.WEB.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.FORCE_WALL.Bit 
                             | Field.FIRE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.ICE_WALL.Bit | Field.BLADE_WALL.Bit | Field.SLEEP_CLOUD.Bit)) return;
            addField(l, Field.WEB.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.WEB);
        }
        public void MakeFireBarrier(Location l)
        {
            if (fieldsThere(l, Field.FIRE_BARRIER.Bit)) return;
            if (fieldsThere(l, Field.ANTIMAGIC.Bit) && Maths.Rand(1, 0, 3) < 3) return;
            if (fieldsThere(l, Field.CRATE.Bit | Field.BARREL.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit)) return;
            removeField(l, Field.WEB.Bit | Field.FORCE_WALL.Bit | Field.FIRE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.STINK_CLOUD.Bit | Field.ICE_WALL.Bit 
                         | Field.BLADE_WALL.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.BLADE_WALL);
        }
        public void MakeForceBarrier(Location l)
        {
            if (fieldsThere(l, Field.FORCE_BARRIER.Bit)) return;
            if (fieldsThere(l, Field.ANTIMAGIC.Bit) && Maths.Rand(1, 0, 2) < 2) return;
            if (fieldsThere(l, Field.CRATE.Bit | Field.BARREL.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit)) return;
            removeField(l, Field.WEB.Bit | Field.FORCE_WALL.Bit | Field.FIRE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.STINK_CLOUD.Bit | Field.ICE_WALL.Bit
                         | Field.BLADE_WALL.Bit | Field.SLEEP_CLOUD.Bit);
            addField(l, Field.FORCE_BARRIER.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.FORCE_BARRIER);
        }
        void make_force_wall(Location l, IExpRecipient perp)
        {
            if (fieldsThere(l, Field.FORCE_WALL.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.CRATE.Bit | Field.BARREL.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.FORCE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.BLADE_WALL.Bit)) return;
            removeField(l, Field.WEB.Bit | Field.FIRE_WALL.Bit);
            addField(l, Field.FORCE_WALL.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.FORCE_WALL);
        }
        void make_fire_wall(Location l, IExpRecipient perp)
        {
            if (fieldsThere(l, Field.FIRE_WALL.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.CRATE.Bit | Field.BARREL.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit
                | Field.ANTIMAGIC.Bit | Field.STINK_CLOUD.Bit | Field.ICE_WALL.Bit | Field.BLADE_WALL.Bit | Field.SLEEP_CLOUD.Bit)) return;
            removeField(l, Field.WEB.Bit);
            addField(l, Field.FIRE_WALL.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.FIRE_WALL);
        }

        void make_antimagic(Location l)
        {
            if (fieldsThere(l, Field.ANTIMAGIC.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit)) return;
            removeField(l, Field.FORCE_WALL.Bit | Field.FIRE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.STINK_CLOUD.Bit | Field.ICE_WALL.Bit | Field.BLADE_WALL.Bit | Field.SLEEP_CLOUD.Bit);

            addField(l, Field.ANTIMAGIC.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.ANTIMAGIC);
        }

        void make_scloud(Location l)
        {
            if (fieldsThere(l, Field.STINK_CLOUD.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.FORCE_WALL.Bit | Field.FIRE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.ICE_WALL.Bit 
                         | Field.BLADE_WALL.Bit | Field.SLEEP_CLOUD.Bit)) return;
            addField(l, Field.STINK_CLOUD.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.STINK_CLOUD);
        }
        void make_ice_wall(Location l, IExpRecipient perp)
        {
            if (fieldsThere(l, Field.ICE_WALL.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.WEB.Bit | Field.CRATE.Bit | Field.BARREL.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.FORCE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.BLADE_WALL.Bit)) return;
            removeField(l, Field.FIRE_WALL.Bit | Field.STINK_CLOUD.Bit);
            addField(l, Field.ICE_WALL.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.ICE_WALL);
        }

        void make_blade_wall(Location l, IExpRecipient perp)
        {
            if (fieldsThere(l, Field.BLADE_WALL.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.ANTIMAGIC.Bit)) return;
            addField(l, Field.BLADE_WALL.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.BLADE_WALL);
        }
        void make_sleep_cloud(Location l)
        {
            if (fieldsThere(l, Field.SLEEP_CLOUD.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED) return;
            if (fieldsThere(l, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit | Field.ANTIMAGIC.Bit)) return;
            addField(l, Field.SLEEP_CLOUD.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.SLEEP_CLOUD);
        }

        public void MakeQuickfire(Location l)
        {
            if (fieldsThere(l, Field.QUICKFIRE.Bit)) return;
            if (fieldsThere(l, Field.ANTIMAGIC.Bit) && Maths.Rand(1, 0, 1) == 0) return;
            if (fieldsThere(l, Field.FORCE_BARRIER.Bit | Field.FIRE_BARRIER.Bit)) return;
            if (blockageThere(l) == eBlock2.BLOCKED || TerrainAt(l).Obscurity > 0) return;
            removeField(l, Field.FORCE_WALL.Bit | Field.FIRE_WALL.Bit | Field.ANTIMAGIC.Bit | Field.STINK_CLOUD.Bit | Field.ICE_WALL.Bit | Field.BLADE_WALL.Bit | Field.SLEEP_CLOUD.Bit
                          | Field.WEB.Bit | Field.CRATE.Bit | Field.BARREL.Bit | Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.QUICKFIRE.Bit);
            addField(l, Field.QUICKFIRE.Bit | Field.FIELD_APPEAR.Bit);
            new Animation_FieldAppear(l, Field.QUICKFIRE);
        }

        // mode 0 - dispel spell, 1 - always take  2 - always take and take fire and force too
        public void DispelFields(Location l, int mode)
        {
            if (mode == 2)removeField(l, Field.FIRE_BARRIER.Bit | Field.FORCE_BARRIER.Bit | Field.BARREL.Bit | Field.CRATE.Bit | Field.WEB.Bit);
            if (mode >= 1) mode = -10;
            removeField(l, Field.FIRE_WALL.Bit | Field.FORCE_WALL.Bit | Field.STINK_CLOUD.Bit);
            if (Maths.Rand(1, 1, 6) + mode <= 1) removeField(l, Field.WEB.Bit);
            if (Maths.Rand(1, 1, 6) + mode < 6) removeField(l, Field.ICE_WALL.Bit);
            if (Maths.Rand(1, 1, 6) + mode < 5) removeField(l, Field.SLEEP_CLOUD.Bit);
            if (Maths.Rand(1, 1, 8) + mode <= 1) removeField(l, Field.QUICKFIRE.Bit);;
            if (Maths.Rand(1, 1, 7) + mode < 5) removeField(l, Field.BLADE_WALL.Bit);;
        }

        Boolean is_container(Location loc)
        {
            if (fieldsThere(loc, Field.CRATE.Bit | Field.BARREL.Bit)) return true;
            return terrainAt(loc.X, loc.Y).Special == eTerSpec.IS_A_CONTAINER;
        }

        public void place_treasure(Location where, int level, int loot, int mode)
        {

            Item new_item;
            int amt, r1, j;
            int[,] treas_chart = {{0,-1,-1,-1,-1,-1},
								        {1,-1,-1,-1,-1,-1},
								        {2,1,1,-1,-1,-1},
								        {3,2,1,1,-1,-1},
								        {4,3,2,2,1,1}};
            int[,] treas_odds = {{10,0,0,0,0,0},
								        {50,0,0,0,0,0},
								        {60,50,40,0,0,0},
								        {100,90,80,70,0,0},
								        {100,80,80,75,75,75}};
            short[,] max_mult = {{0,0,0,0,0,0,0,0,0,1},
							        {0,0,1,1,1,1,2,3,5,20},
							        {0,0,1,1,2,2,4,6,10,25},
							        {5,10,10,10,15,20,40,80,100,100},
							        {25,25,50,50,50,100,100,100,100,100}};
            short[,] min_chart = {{0,0,0,0,0,0,0,0,0,1},
						        {0,0,0,0,0,0,0,0,5,20},
						        {0,0,0,0,1,1,5,10,15,40},
						        {10,10,15,20,20,30,40,50,75,100},
						        {50,100,100,100,100,200,200,200,200,200}};
            int max, min;

            if (loot == 1)
                amt = Maths.Rand(2, 1, 7) + 1;
            else 
                amt = loot * (Maths.Rand(1, 0, 10 + (loot * 6) + (level * 2)) + 5);

            if (Party.TotalLevel <= 12) amt += 1;
            if (Party.TotalLevel <= 60 && amt > 2) amt += 2;

            if (amt > 3) //Place some gold
            {
                new_item = Item.List["gold"].Copy();
                new_item.Charges = amt;
                r1 = Maths.Rand(1, 1, 9);
                if ((loot > 1 && r1 < 7) || (loot == 1 && r1 < 5) || mode == 1
                    || (r1 < 6 && Party.TotalLevel < 30) || loot > 2)
                    PlaceItem(new_item, where);
            }
            for (j = 0; j < 5; j++)
            {
                r1 = Maths.Rand(1, 0, 100);
                if ((treas_chart[loot, j] >= 0) && (r1 <= treas_odds[loot, j] + Party.GetSkillTotal(eSkill.LUCK)))
                {
                    r1 = Maths.Rand(1, 0, 9);
                    min = min_chart[treas_chart[loot, j], r1];
                    r1 = Maths.Rand(1, 0, 9);
                    max = (min + level + (2 * (loot - 1)) + (Party.GetSkillTotal(eSkill.LUCK) / 3)) * max_mult[treas_chart[loot, j], r1];
                    if (Maths.Rand(1, 0, 1000) == 500)
                    {
                        max = 10000;
                        min = 100;
                    }

                    // reality check
                    if ((loot == 1) && (max > 100) && (Maths.Rand(1, 0, 8) < 7))
                        max = 100;
                    if ((loot == 2) && (max > 200) && (Maths.Rand(1, 0, 8) < 6))
                        max = 200;


                    new_item = Item.GetTreasure(treas_chart[loot, j]);

                    if (new_item.BaseValue < min || new_item.BaseValue > max)
                    {
                        new_item = Item.GetTreasure(treas_chart[loot, j]);
                        if (new_item.BaseValue < min || new_item.BaseValue > max)
                        {
                            new_item = Item.GetTreasure(treas_chart[loot, j]);
                            if (new_item.BaseValue > max)
                                new_item.Variety = eVariety.None;
                        }
                    }

                    // not many magic items
                    if (mode == 0)
                    {
                        if (new_item.Magic && (level < 2) && (Maths.Rand(1, 0, 5) < 3))
                            new_item.Variety = eVariety.None;
                        if (new_item.Magic && (level == 2) && (Maths.Rand(1, 0, 5) < 2))
                            new_item.Variety = eVariety.None;
                        if (new_item.Cursed && (Maths.Rand(1, 0, 5) < 3))
                            new_item.Variety = eVariety.None;
                    }

                    // if forced, keep dipping until a treasure comes uo
                    if (mode == 1 && max >= 20)
                    {
                        do
                            new_item = Item.GetTreasure(treas_chart[loot, j]);
                        while (new_item.Variety == eVariety.None || new_item.BaseValue > max);
                    }

                    // Not many cursed items
                    if (new_item.Cursed && Maths.Rand(1, 0, 2) == 1)
                        new_item.Variety = 0;

                    if (new_item.Variety != eVariety.None)
                    {
                        if (Party.IdentifyItemRoll()) new_item.Identified = true;
                        PlaceItem(new_item, where);
                    }
                }
            }

        }

        public void WorkOutNPCTargetShortcuts(Location pos, int range)
        {
            List<ICharacter> targets = new List<ICharacter>();

            //Add all possible targets to the list.
            foreach(ICharacter ch in NPCList)
            {
                ch.TargetingNum = -1;
                if (ch.Pos == pos) continue;

                if (ch.Pos.DistanceTo(pos) <= range && _Visible[ch.Pos.X, ch.Pos.Y] != 0) targets.Add(ch);
            }

            if (targets.Count == 0) return;

            //Order the list by distance to pos
            IEnumerable<ICharacter> ordered = targets.OrderBy(n => n.Pos.DistanceTo(pos));

            int c = 0;
            foreach (ICharacter ch in ordered)
            {
                ch.TargetingNum = c++;
                if (c == 12) return;
            }
        }
        public NPC FindTargetLetterNPC(int num)
        {
            foreach (NPC npc in NPCList)
            {
                if (npc.TargetingNum == num) return npc;
            }
            return null;
        }

        public Location FindSpellTargetPosition(Location where, int radius, ref int m, ICharacter who)
        {
            Location check_loc;
            int cur_lev, level_max = 10;

            List<Location> possibles = new List<Location>();

            for (check_loc.X = 1; check_loc.X < Width - 1; check_loc.X++)
                for (check_loc.Y = 1; check_loc.Y < Height - 1; check_loc.Y++)
                    if (where.DistanceTo(check_loc) <= 8 && where.DistanceTo(check_loc) > radius && CanSee(where, check_loc, true) < Constants.OBSCURITY_LIMIT && GetObscurity(check_loc) < Constants.OBSCURITY_LIMIT)
                    {
                        cur_lev = CountLevels(check_loc, radius, who);
                        if (cur_lev > level_max) 
                        {
                            level_max = cur_lev;
                            possibles.Clear();
                            possibles.Add(check_loc);
                        }
                        else if (cur_lev == level_max)
                        {
                            possibles.Add(check_loc);
                        }
                    }

            m = level_max;
            if (possibles.Count == 0) return new Location(-1, -1);
            return possibles[Maths.Rand(1, 0, possibles.Count - 1)];
        }

        public int CountLevels(Location where, int radius, ICharacter who)
        {
            int store = 0;

            foreach (ICharacter ch in EachCharacterInRange(where, radius, Game.Mode == eMode.COMBAT))
                if (CanSee(where, ch.Pos) < Constants.OBSCURITY_LIMIT)
                    if (who.AlliedWith(ch))
                        store -= ch is PCType ? 10 : ch.Level;
                    else
                        store += ch is PCType ? 10 : ch.Level;

            if (Game.Mode != eMode.COMBAT)
                if (Party.Pos.VDistanceTo(where) <= radius && CanSee(where, Party.Pos) < Constants.OBSCURITY_LIMIT)
                    if (who.AlliedWith(Party.LeaderPC))
                        store -= 20;
                    else
                        store += 20;

            return store;
        }
    }
}
