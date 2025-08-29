using System;
using System.IO;
using System.Collections.Generic;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

public partial class WorldMapType : IMap
{
    private PartyType Party => Game.CurrentParty;

    public int Width, Height; //Size in tiles of the whole world
    public List<Encounter> NPCGroupList = new();

    public Encounter PCAttacker = null; //Used to store which NPC group has just tried to attack the party

    public void LoadFull(BinaryReader In)
    {
        foreach (var o in OutsideSector.List)//Sectors)
            o.LoadFull(In);
    }

    private bool Explored(int x, int y)
    {
        var pos = new Location(x / Constants.SECTOR_WIDTH, y / Constants.SECTOR_HEIGHT);
        foreach (var s in OutsideSector.List)
        {
            if (s.SectorPos == pos)
            {
                int tx = x % Constants.SECTOR_WIDTH, ty = y % Constants.SECTOR_HEIGHT;
                return s.Explored[tx, ty];
            }
        }
        return false;
    }

    private void SetExplored(int x, int y, bool value)
    {
        var pos = new Location(x / Constants.SECTOR_WIDTH, y / Constants.SECTOR_HEIGHT);
        foreach (var s in OutsideSector.List)
        {
            if (s.SectorPos == pos)
            {
                int tx = x % Constants.SECTOR_WIDTH, ty = y % Constants.SECTOR_HEIGHT;
                s.Explored[tx, ty] = value;//Sectors[sx, sy].;
                return;
            }
        }
    }

    public OutsideSector SectorAt(Location pos)
    {
        pos = new Location(pos.X / Constants.SECTOR_WIDTH, pos.Y / Constants.SECTOR_HEIGHT);
        foreach (var s in OutsideSector.List)
        {
            if (s.SectorPos == pos) return s;
        }
        return null;
    }

    private Location toLocal(Location pos)
    {
        return new Location(pos.X % Constants.SECTOR_WIDTH, pos.Y % Constants.SECTOR_HEIGHT);
    }

    public Location ToGlobal(Location pos, OutsideSector o)
    {
        return (o.SectorPos * 48) + pos;
    }

    public void DeactivateTrigger(Location pos)
    {
        var o = SectorAt(pos);
        if (o != null)
            o.SetTrigger(toLocal(pos), false);
    }
    public void ActivateTrigger(Location pos)
    {
        var o = SectorAt(pos);
        if (o != null)
            o.SetTrigger(toLocal(pos), true);
    }

    public bool Visible(Location loc) { return true; }
    public string Name => SectorAt(Party.Pos).Name;

    public void Draw(SpriteBatch sb)
    {
        var VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
        var VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
        var offx = (int)(((Gfx.Scroll.X - VW / 2f) - (int)(Gfx.Scroll.X - VW / 2f)) * Gfx.ZoomSizeW);
        var offy = (int)(((Gfx.Scroll.Y - VH / 2f) - (int)(Gfx.Scroll.Y - VH / 2f)) * Gfx.ZoomSizeH);
        var sx = (int)(Gfx.Scroll.X - VW / 2f);
        var sy = (int)(Gfx.Scroll.Y - VH / 2f);
        var tw = (int)(Gfx.Scroll.X + VW / 2f + 1f);
        var th = (int)(Gfx.Scroll.Y + VH / 2f + 1f);

        var charzoomw = (int)((float)Gfx.ZoomSizeW * Gfx.CHARWIDTH);
        var charoffx = (int)((float)(Gfx.ZoomSizeW - charzoomw) / 2f);

        //Draw terrain
        sb.Begin(SpriteSortMode.Deferred, BlendState.AlphaBlend);

        for (var sector_y = Maths.Floor((float)sy / (float)Constants.SECTOR_HEIGHT); sector_y <= (th - 1) / Constants.SECTOR_HEIGHT; sector_y++)
        {
            for (var sector_x = Maths.Floor((float)sx / (float)Constants.SECTOR_WIDTH); sector_x <= (tw - 1) / Constants.SECTOR_WIDTH; sector_x++)
            {
                var s = SectorAtGlobal(sector_x, sector_y);
                if (s == null) continue;

                var y_from = Maths.Max(sy, sector_y * Constants.SECTOR_HEIGHT);
                var y_to = Maths.Min(th, ((sector_y + 1) * Constants.SECTOR_HEIGHT) - 1);
                var x_from = Maths.Max(sx, sector_x * Constants.SECTOR_WIDTH);
                var x_to = Maths.Min(tw, ((sector_x + 1) * Constants.SECTOR_WIDTH) - 1);

                var kx = -offx - Maths.Min(sx, sector_x * Constants.SECTOR_WIDTH) * Gfx.ZoomSizeW + (Gfx.ZoomSizeW * sector_x * Constants.SECTOR_WIDTH);
                var ky = -offy - Maths.Min(sy, sector_y * Constants.SECTOR_HEIGHT) * Gfx.ZoomSizeH + (Gfx.ZoomSizeH * sector_y * Constants.SECTOR_HEIGHT);

                var dy = ky;

                for (var y = y_from; y <= y_to; y++)
                {
                    var dx = kx;

                    for (var x = x_from; x <= x_to; x++)
                    {
                        int tx = x % Constants.SECTOR_WIDTH, ty = y % Constants.SECTOR_HEIGHT;
                        if (s.Explored[tx, ty])
                        {
                            var r_dst = new XnaRect(dx, dy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);

                            var underlay = TerrainRecord.UnderlayList[s[tx, ty] & 0x00FF];
                            var overlay = TerrainRecord.OverlayList[(s[tx, ty] & 0xFF00) >> 8];

                            if ((s.MapExtra[tx, ty] & eMapOutExtraBit.ENTRANCE) != 0) //Display alternate terrain for hidden town entrances
                            {
                                var towne = s.TownEntranceHere(new Location(tx, ty), true);
                                if (towne != null && towne.DestTown != null && towne.DestTown.Hidden && towne.TerrainIfHidden != null)
                                {
                                    if (towne.TerrainIfHidden.Layer == 0)
                                        underlay = towne.TerrainIfHidden;
                                    else
                                        overlay = towne.TerrainIfHidden;
                                }
                            }
                            if (underlay != null) underlay.Draw(sb, r_dst, true);
                            if (overlay != null) overlay.Draw(sb, r_dst, true);
                        }
                        dx += Gfx.ZoomSizeW;
                    }

                    dy += Gfx.ZoomSizeH;
                }
            }
        }

        foreach (var gr in NPCGroupList)
        {
            var vis = false;
            if (Explored(gr.Pos.X, gr.Pos.Y) && gr.Pos.VDistanceTo(Party.Pos) < Constants.NPC_GROUP_VISIBLE_DISTANCE
                                             && gr.Pos.Inside(sx, sy, tw, th))
                vis = true;

            if (!vis && gr.AnimAction is Animation_Move)
            {
                var p = gr.Pos - ((Animation_Move)gr.AnimAction).PosMod;
                if (Explored(p.X, p.Y) && p.VDistanceTo(Party.Pos) < Constants.NPC_GROUP_VISIBLE_DISTANCE
                                       && p.Inside(sx, sy, tw, th))
                    vis = true;
            }

            if (vis)
            {
                var dr = new XnaRect((gr.Pos.X - sx) * Gfx.ZoomSizeW - offx + charoffx,
                    (gr.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                    charzoomw, Gfx.ZoomSizeH);
                gr.Draw(sb, dr, Color.White);
            }
        }

        //Draw Vehicles
        foreach (var v in Vehicle.List)
            if (v.Map == this && v.Pos.Inside(sx, sy, tw, th) && Visible(v.Pos))
            {
                var dr = new XnaRect((v.Pos.X - sx) * Gfx.ZoomSizeW - offx + charoffx,
                    (v.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                    charzoomw, Gfx.ZoomSizeH);
                v.Draw(sb, dr);
            }

        if (Gfx.ZoomSizeW > Gfx.ZOOMSIMPLETHRESHOLD && Gfx.ZoomSizeH > Gfx.ZOOMSIMPLETHRESHOLD)
        {
            //Draw dark edges to unexplored/out of sight areas
            float qw = (float)Gfx.ZoomSizeW / 3f, qh = (float)Gfx.ZoomSizeH / 3f;
            int qwf = Maths.Floor(qw), qhf = Maths.Floor(qh), qwc = Maths.Ceiling(qw), qhc = Maths.Ceiling(qh);

            for (var sector_y = Maths.Floor((float)sy / (float)Constants.SECTOR_HEIGHT); sector_y <= (th - 1) / Constants.SECTOR_HEIGHT; sector_y++)
            {
                for (var sector_x = Maths.Floor((float)sx / (float)Constants.SECTOR_WIDTH); sector_x <= (tw - 1) / Constants.SECTOR_WIDTH; sector_x++)
                {
                    var s = SectorAtGlobal(sector_x, sector_y);
                    if (s == null) continue;

                    var y_from = Maths.Max(sy, sector_y * Constants.SECTOR_HEIGHT);
                    var y_to = Maths.Min(th, ((sector_y + 1) * Constants.SECTOR_HEIGHT) - 1);
                    var x_from = Maths.Max(sx, sector_x * Constants.SECTOR_WIDTH);
                    var x_to = Maths.Min(tw, ((sector_x + 1) * Constants.SECTOR_WIDTH) - 1);

                    var kx = -offx - Maths.Min(sx, sector_x * Constants.SECTOR_WIDTH) * Gfx.ZoomSizeW + (Gfx.ZoomSizeW * sector_x * Constants.SECTOR_WIDTH);
                    var ky = -offy - Maths.Min(sy, sector_y * Constants.SECTOR_HEIGHT) * Gfx.ZoomSizeH + (Gfx.ZoomSizeH * sector_y * Constants.SECTOR_HEIGHT);

                    var dy = ky;

                    for (var y = y_from; y <= y_to; y++)
                    {
                        var dx = kx;

                        for (var x = x_from; x <= x_to; x++)
                        {
                            int tx = x % Constants.SECTOR_WIDTH, ty = y % Constants.SECTOR_HEIGHT;

                            if (s.Explored[tx, ty])
                            {
                                var expl_w = tx == 0 ? Explored(x - 1, y) : s.Explored[tx - 1, ty];
                                var expl_e = tx == (Constants.SECTOR_WIDTH - 1) ? Explored(x + 1, y) : s.Explored[tx + 1, ty];
                                var expl_n = ty == 0 ? Explored(x, y - 1) : s.Explored[tx, ty - 1];
                                var expl_s = ty == (Constants.SECTOR_HEIGHT - 1) ? Explored(x, y + 1) : s.Explored[tx, ty + 1];
                                var expl_nw = (tx == 0 || ty == 0) ? Explored(x - 1, y - 1) : s.Explored[tx - 1, ty - 1];
                                var expl_ne = (tx == Constants.SECTOR_WIDTH - 1 || ty == 0) ? Explored(x + 1, y - 1) : s.Explored[tx + 1, ty - 1];
                                var expl_sw = (tx == 0 || ty == Constants.SECTOR_HEIGHT - 1) ? Explored(x - 1, y + 1) : s.Explored[tx - 1, ty + 1];
                                var expl_se = (tx == Constants.SECTOR_WIDTH - 1 || ty == Constants.SECTOR_HEIGHT - 1) ? Explored(x + 1, y + 1) : s.Explored[tx + 1, ty + 1];

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


                        }
                        dx += Gfx.ZoomSizeW;
                    }
                    dy += Gfx.ZoomSizeH;
                }
            }
        }

        if (Gfx.FadeMode != 0)
        {
            Gfx.DrawRect(0, 0, Gfx.WinW, Gfx.WinH, Gfx.FadeColor, true);
        }

        //Draw Party
        if (Party.Vehicle == null || Party.LeaderPC.AnimAction != null)
        {
            var drawnpc = false;

            foreach (var pc in Party.PCList)
                if (!(pc.AnimAction == null))
                {
                    var pdr = new XnaRect((pc.Pos.X - sx) * Gfx.ZoomSizeW - offx + charoffx,
                        (pc.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                        charzoomw, Gfx.ZoomSizeH);

                    pc.Draw(sb, pdr, Color.White);
                    drawnpc = true;
                    break;
                }

            if (drawnpc == false && Party.LeaderPC != null && !Game.PartyDead)
            {
                var pdr = new XnaRect((Party.Pos.X - sx) * Gfx.ZoomSizeW - offx + charoffx,
                    (Party.Pos.Y - sy) * Gfx.ZoomSizeH - offy,
                    charzoomw, Gfx.ZoomSizeH);
                Party.LeaderPC.Draw(sb, pdr, Color.White);
            }
        }


        //Draw Animation Overlays (Damage markers, missiles etc)
        foreach (var overlay in Animation.EachOverlayAnim())
        {
            var p = new Location((int)overlay.Pos.X, (int)overlay.Pos.Y);

            if (p.Inside(sx, sy, tw, th) && Visible(p))
            {
                var pos = new Vector2((overlay.Pos.X - sx) * Gfx.ZoomSizeW - offx,
                    (overlay.Pos.Y - sy) * Gfx.ZoomSizeH - offy);
                overlay.DrawOverlay(sb, pos);
            }
        }

        //Draw targeting (Just for searching for the outside map)
        if (Game.PlayerTargeting)
        {
            var mloc = Gfx.GetTileAtMouse(Gui.Ms);
            if (mloc != Action.TargetPC.Pos && Visible(mloc) && mloc.DistanceTo(Action.TargetPC.Pos) <= Action.TargetRange)
            {
                //Draw white rectangle around target
                var dr = new XnaRect((mloc.X - sx) * Gfx.ZoomSizeW - offx,
                    (mloc.Y - sy) * Gfx.ZoomSizeH - offy,
                    Gfx.ZoomSizeW, Gfx.ZoomSizeH);

                Gfx.DrawRect(dr.X, dr.Y, dr.Width, dr.Height, Color.White, false, (int)(Math.Ceiling(2f * (float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH)));
            }
            else
            {
                //Draw NO! icon
                var dr = new XnaRect((mloc.X - sx) * Gfx.ZoomSizeW - offx,
                    (mloc.Y - sy) * Gfx.ZoomSizeH - offy,
                    Gfx.ZoomSizeW, Gfx.ZoomSizeH);
                sb.Draw(Gfx.NewGui, dr, new XnaRect(219, 96, 32, 32), Color.White);
            }
        }


        sb.End();
    }

    public bool PlaceItem(Item item, Location loc) { return true; }
    public void Enter(bool firsttime) 
    {
        Timer.ResetLocalTimers(this);
        Game.AutoSave(); 
    }

    public void UpdateVisible()
    {
        //Outside we can only see as far as 4 spaces around the Party
        if (Script.suspendMapUpdate) return;

        var l = Party.Pos;

        int ymin = Party.Pos.Y - 4,
            ymax = Party.Pos.Y + 4;
        int xmin = Party.Pos.X - 4,
            xmax = Party.Pos.X + 4;

        for (var y = ymin; y <= ymax; y++)
        for (var x = xmin; x <= xmax; x++)
            if (!Explored(x, y))
            {
                if (CanSee(Party.Pos, new Location(x, y), 0) < 5) 
                    SetExplored(x, y, true);
            }

    }

    public string GetInfoRectString(Location pos)
    {
        foreach (var i in SectorAt(pos).InfoRectList)
        {
            if (i.Rect.LocIn(toLocal(pos)))
                return i.Text;
        }
        return null;
    }

    public bool NPCGroupInRange(int range)
    {
        foreach (var npc in NPCGroupList)
        {
            if (npc.Pos.DistanceTo(Party.Pos) <= range) return true;
        }
        return false;
    }

    public bool CheckSpecialTerrainPC(Location pos, PCType ch)
    {
        var ter = terrainAt(pos.X, pos.Y);

        if (ter.Special == eTerSpec.CHANGE_WHEN_STEP_ON) //Change when step on (eg, Non-locked doors)
        {
            var to = ter.Flag1 as TerrainRecord;
            if (to != null)
            {
                AlterTerrain(pos, ter.Layer, to);
                UpdateVisible();
                if (ter.Flag2 is string && (string)ter.Flag1 != "")
                {
                    Sound.Play((string)ter.Flag2);
                }
            }
            if (ter.BlocksPC) return false;
        }
        return true;
    }

    public void AlterTerrain(Location pos, int layer, TerrainRecord newter)
    {
        var s = SectorAt(pos);
        pos = toLocal(pos);

        if (layer == 0) //Underlay
        {
            if (newter != null && newter.Layer == 0)
            {
                s[pos.X, pos.Y] &= 0xFF00; //Wipe lower (underlay) byte
                s[pos.X, pos.Y] += (byte)newter.Num;
                if (this == Game.CurrentMap) UpdateVisible();
            }
        }
        else if (layer == 1) //Overlay
        {
            ushort b = 0;
            if (newter == null) b = 0; //If null terrainrecord passed, wipe the overlay
            else if (newter.Layer != 1) return;
            else b = (ushort)(newter.Num << 8);
            s[pos.X, pos.Y] &= 0x00FF; //Wipe upper (overlay) byte
            s[pos.X, pos.Y] += b;
            if (this == Game.CurrentMap) UpdateVisible();
        }
    }

    public void DoNastyTerrain(Location pos)
    {
        var report = true;
        var ter = terrainAt(pos.X, pos.Y);

        foreach (var pc in Party.EachAlivePC())
        {
            ter.NastyTerrainEffect(pc, report);
            report = false;
        }
    }

    public bool DoStoodOnTriggers()
    {
        return false;
        //TO DO
    }

    public TownEntrance TownEntranceHere(Location pos, bool regardless_of_hidden = false)
    {
        var o = SectorAt(pos);
        var t = toLocal(pos);

        foreach (var e in o.TownEntranceList)
        {
            if (e.DestTown == null) continue;
            if (e.Pos == t && (!e.DestTown.Hidden || regardless_of_hidden)) return e;//.DestTown;
        }
        return null;
    }

    public bool SomeoneThere(Location pos)
    {
        if (Party.Pos == pos) return true;
        foreach (var g in NPCGroupList)
        {
            if (g.Pos == pos) return true;
        }
        return false;
    }

    public bool CharacterCanBeThere(Location loc, ICharacter m_num, bool allow_leave_map = false)
    {
        if (m_num is PCType)
        {
            //This is solely used when checking if the party lands safely after flying.
            if (SecretPassageThere(loc)) return true;
            if (Party.Flying == 0 && TerrainAt(loc).BlocksPC) return false;
        }

        return true;
    }

    public string GetToolTipMessage(Location loc)
    {
        var sec = SectorAt(loc);
        if (sec == null) return null;

        var sb = new StringBuilder();

        foreach (var npc in NPCGroupList)
        {
            if (npc.Pos == loc)
            {
                sb.AppendLine("Wandering encounter");
            }
        }

        var towne = TownEntranceHere(loc);
        if (towne != null)
            sb.AppendLine(towne.DestTown.Name);

        if (Party.Pos == loc)
            sb.AppendLine("Your party");

        var v = Vehicle.IsThere(this, loc);
        if (v != null)
        {
            sb.AppendLine(char.ToUpper(v.Name[0]) + v.Name.Substring(1));
            sb.AppendLine(v.PartyOwns ? " (yours)" : " (not yours)");
        }

        if (sb.Length == 0) return null;
        sb.Remove(sb.Length - 1, 1);
        return sb.ToString();

    }
    public List<PopUpMenuData> GetPopUpMenuOptions(Location loc, Location frompos)
    {
        if (SectorAt(loc) == null || !Visible(loc)) return null; //Tile must be visible and on the map

        var options = new List<PopUpMenuData>();
        var dist = loc.VDistanceTo(frompos);

        //Search options
        if (dist <= 1)
        {
            var ter = TerrainAt(loc);
            options.Add(new PopUpMenuData(string.Format("Inspect {0}", ter.Name), loc, null, PopUpMenuData.SEARCH));
        }

        if (options.Count > 0) return options;
        return null;
    }

    public void HandleMapPopUp(object o, object o2, int data)
    {
        switch (data)
        {
            case PopUpMenuData.SEARCH:
                new Action(eAction.Search) { PC = (Game.Mode == eMode.COMBAT) ? Party.ActivePC : Party.CurrentPC, Loc = (Location)o };
                break;
        }
    }

    public bool DoNPCTurn()
    {
        //For the outside area, all NPC Groups moved in StartNPCTurn, so just possibly spawn new groups here
        if (Maths.Rand(1, 1, Constants.OUTSIDE_WANDERING_SPAWN_CHANCE)  == 1)
        {
            SpawnWanderingGroup();
        }
        return true;
    }

    public void SpawnWanderingGroup()
    {
        if (NPCGroupList.Count >= Constants.NPC_GROUP_LIMIT)
        {
            //No more wandering monsters can exist!
            //Try to cull groups that are too far from the party
            var culled = false;
            foreach (var g in NPCGroupList)
            {
                if (g.Pos.VDistanceTo(Party.Pos) >= Constants.NPC_GROUP_CULL_DISTANCE) { NPCGroupList.Remove(g); culled = true; break; }
            }
            if (!culled) return; //Nope, couldn't get rid of any groups, so just quit.
        }

        var o = SectorAt(Party.Pos);
        var possspawnspots = new List<Location>();
        foreach (var loc in o.SpawnPointList)
        {
            var gloc = ToGlobal(loc, o);
            if (gloc.VDistanceTo(Party.Pos) >= Constants.SPAWN_MIN_DISTANCE && !TerrainAt(gloc).BlocksNPC && !Game.WorldMap.SomeoneThere(gloc))
                possspawnspots.Add(gloc);
        }

        if (possspawnspots.Count == 0) return;

        var spawnat = possspawnspots[Maths.Rnd.Next(0, possspawnspots.Count - 1)];
        if (o.WanderingGroupList.Count == 0) return; //No preset wandering groups in this area to spawn.

        var wg = o.WanderingGroupList[Maths.Rnd.Next(0, o.WanderingGroupList.Count - 1)];

        if (GlobalVariables.Get(wg.EndVar) > 0) return;

        NPCGroupList.Add(new Encounter(wg, spawnat));

    }

    public void SpawnEncounter(string group_id, Location pos)
    {
        EncounterRecord npcg;
        if (!EncounterRecord.List.TryGetValue(group_id, out npcg)) return;

        if (GlobalVariables.Get(npcg.EndVar) > 0) return;

        var spots = new List<Location>();

        var dist = 1;

        //Find somewhere for the NPCGroup to go. Start at a distance of 1 from the Centre and 
        while (spots.Count == 0)
        {
            for (var x = pos.X - dist; x <= pos.X + dist; x++)
            for (var y = pos.Y - dist; y <= pos.Y + dist; y++)
            {
                var loc = new Location(x, y);
                if (spots.Contains(loc)) continue; //Not one already on the list
                if (loc == pos) continue; //Not the centre spot itself (that's where the party will be)
                if (SectorAt(loc) == null) continue; //Not one that's off the world map
                if (TerrainAt(loc).BlocksNPC) continue; //Not one with blocking terrain on it.
                foreach (var npc in NPCGroupList) if (npc.Pos == loc) continue; //Not one with another group on it.
                spots.Add(loc);
            }
            dist++;
        }

        //Return a random entry in the list.
        pos = spots[Maths.Rand(1, 0, spots.Count - 1)];

        NPCGroupList.Add(new Encounter(npcg, pos));
    }

    public void StartNPCTurn()
    {
        PCAttacker = null;

        //Groups with 'Forced' property attack immediately regardless of where they are
        foreach (var grp in NPCGroupList)
        {
            if (grp.Record.Forced)
            {
                PCAttacker = grp;
                break;
            }
        }

        //Otherwise, groups move and will attack if next to the Party
        if (PCAttacker == null)
        {
            foreach (var grp in NPCGroupList)
            {
                if (grp.Move() && PCAttacker == null)
                    PCAttacker = grp;
            }
        }

        if (PCAttacker != null)
        {
            // Is combat too easy?
            if (!PCAttacker.Record.CantFlee && ((Party.TotalLevel > (PCAttacker.Record.out_enc_lev_tot * 5) / 3 && PCAttacker.Record.out_enc_lev_tot < 200) || Game.NPCGroupsFlee))
            {
                Game.AddMessage("Combat: Enemies fled!");
                Animation.Create(new Animation_Hold());
                Animation.Create(new Animation_Death(PCAttacker));
                return;
            }

            Animation.Create(new Animation_Hold());
            Animation.Create(new Animation_Attack(PCAttacker, "023_startoutdoorcombat"));
        }
    }

    public void MoveNPCsDuringRest()
    {
        //No need to check attacking, as resting is stopped if a group gets to within 3 squares of the party.

        foreach (var grp in NPCGroupList)
        {
            grp.Move(true);
        }
    }

    public int CanSee(Location p1, Location p2, int dummy)
    {
        int dx, dy, count, storage = 0;

        if (p1.Y == p2.Y)
        {
            if (p1.X > p2.X)
            {
                for (count = p2.X + 1; count < p1.X; count++)
                {
                    var ter = terrainAt(count, p1.Y);
                    storage += ter.Obscurity;
                }
            }
            else
            {
                for (count = p1.X + 1; count < p2.X; count++)
                {
                    var ter = terrainAt(count, p1.Y);
                    storage += ter.Obscurity;
                }
            }
            return storage;
        }
        if (p1.X == p2.X)
        {
            if (p1.Y > p2.Y)
            {
                for (count = p1.Y - 1; count > p2.Y; count--)
                {
                    var ter = terrainAt(p1.X, count);
                    storage += ter.Obscurity;
                }
            }
            else
            {
                for (count = p1.Y + 1; count < p2.Y; count++)
                {
                    var ter = terrainAt(p1.X, count);
                    storage += ter.Obscurity;
                }
            }
            return storage;
        }
        dx = p2.X - p1.X;
        dy = p2.Y - p1.Y;

        if (Math.Abs(dy) > Math.Abs(dx))
        {
            if (p2.Y > p1.Y)
            {
                for (count = 1; count < dy; count++)
                {
                    var ter = terrainAt(p1.X + (count * dx) / dy, p1.Y + count);
                    storage += ter.Obscurity;
                }
            }
            else
            {
                for (count = -1; count > dy; count--)
                {
                    var ter = terrainAt(p1.X + (count * dx) / dy, p1.Y + count);
                    storage += ter.Obscurity;
                }
            }
            return storage;
        }
        if (Math.Abs(dy) <= Math.Abs(dx))
        {
            if (p2.X > p1.X)
            {
                for (count = 1; count < dx; count++)
                {
                    var ter = terrainAt(p1.X + count, p1.Y + (count * dy) / dx);
                    storage += ter.Obscurity;
                }
            }
            else
            {
                for (count = -1; count > dx; count--)
                {
                    var ter = terrainAt(p1.X + count, p1.Y + (count * dy) / dx);
                    storage += ter.Obscurity;
                }
            }
            return storage;
        }
        if (storage > Constants.OBSCURITY_LIMIT) return Constants.OBSCURITY_LIMIT;
        else return storage;
    }

    public OutsideSector SectorAtGlobal(int x, int y)
    {
        foreach (var s in OutsideSector.List)
        {
            if (s.SectorPos == new Location(x, y)) return s;
        }
        return null;
    }

    private TerrainRecord terrainAt(int x, int y)
    {
        var s = SectorAt(new Location(x, y));
        if (s == null) return null;
        int tx = x % Constants.SECTOR_WIDTH, ty = y % Constants.SECTOR_HEIGHT;

        TerrainRecord ter;
        var overlay = s[tx, ty] & 0xFF00;
        if (overlay != 0)
            ter = TerrainRecord.OverlayList[overlay >> 8];
        else
            ter = TerrainRecord.UnderlayList[s[tx, ty] & 0x00FF];

        if ((s.MapExtra[tx,ty] & eMapOutExtraBit.ENTRANCE) != 0)
        {
            var towne = TownEntranceHere(new Location(x,y), true);
            if (towne != null && towne.DestTown.Hidden)
            {
                ter = towne.TerrainIfHidden;
            }
        }

        return ter;

    }

    public TerrainRecord TerrainAt(Location pos)
    {
        var s = SectorAt(pos);
        if (s == null) return null;
        int tx = pos.X % Constants.SECTOR_WIDTH, ty = pos.Y % Constants.SECTOR_HEIGHT;

        TerrainRecord ter;
        var overlay = s[tx, ty] & 0xFF00;
        if (overlay != 0)
            ter = TerrainRecord.OverlayList[overlay >> 8];
        else
            ter = TerrainRecord.UnderlayList[s[tx, ty] & 0x00FF];

        if ((s.MapExtra[tx, ty] & eMapOutExtraBit.ENTRANCE) != 0)
        {
            var towne = TownEntranceHere(pos, true);
            if (towne != null && towne.DestTown.Hidden)
            {
                ter = towne.TerrainIfHidden;
            }
        }

        return ter;

    }

    public void TerrainAtX(Location pos, ref TerrainRecord under, ref TerrainRecord over)
    {
        var s = SectorAt(pos);
        if (s == null)
        {
            under = TerrainRecord.UnderlayList[0];
            over = null;
            return;
        }
        int tx = pos.X % Constants.SECTOR_WIDTH, ty = pos.Y % Constants.SECTOR_HEIGHT;

        var overlay = (s[tx, ty] & 0xFF00) >> 8;
        if (overlay == 0)
            over = null;
        else
            over = TerrainRecord.OverlayList[overlay];
        under = TerrainRecord.UnderlayList[s[tx, ty] & 0x00FF];
    }

    public bool PCCanTryToWalkThere(Location pos, PCType pc)
    {
        var ter = terrainAt(pos.X, pos.Y);

        //Blocking terrain
        if (ter.BlocksPC && Party.Flying == 0)
        {
            //If there is a special encounter node type 4 (Secret passage) PCs can be here

            var o = SectorAtGlobal(pos.X, pos.Y);
            if (o == null) return false;

            var sx = pos.X / Constants.SECTOR_WIDTH;
            var sy = pos.Y / Constants.SECTOR_WIDTH;
            var basecoord = new Location(sx * Constants.SECTOR_WIDTH, sy * Constants.SECTOR_HEIGHT);
            if ((o.MapExtra[pos.X - basecoord.X, pos.Y - basecoord.Y] & eMapOutExtraBit.SECRET) != 0) return true;
            if (Vehicle.IsThere(this, pos) != null) return true;
            return false;
        }

        if (Party.Flying > 0 && !ter.FlyOver && ter.BlocksPC) return false;

        return true;
    }

    public bool SecretPassageThere(Location pos)
    {
        var o = SectorAtGlobal(pos.X, pos.Y);
        if (o == null) return false;
        var sx = pos.X / Constants.SECTOR_WIDTH;
        var sy = pos.Y / Constants.SECTOR_WIDTH;
        var basecoord = new Location(sx * Constants.SECTOR_WIDTH, sy * Constants.SECTOR_HEIGHT);
        return (o.MapExtra[pos.X - basecoord.X, pos.Y - basecoord.Y] & eMapOutExtraBit.SECRET) != 0;
    }


    public bool TriggerStepOnSpecials(Location gpos, Direction dir, PCType pc, bool boat_landing)
    {
        string foundfunc = null;
        TriggerSpot foundspot = null;

        var o = SectorAt(gpos);
        var pos = new Location(gpos.X % Constants.SECTOR_WIDTH, gpos.Y % Constants.SECTOR_HEIGHT);

        //First look for special encounter nodes here
        foreach (var se in o.TriggerSpotList)
        {
            if (se.Pos == pos && se.TriggeredBy(eTriggerSpot.STEP_ON) && se.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
            {
                foundspot = se;
                foundfunc = se.Func;
                break;
            }
        }

        //Look for terrain type here with a trigger
        var ter = terrainAt(gpos.X, gpos.Y);

        if (foundfunc == null) //Terrain triggers ignored if map trigger is on the same space.
        {
            if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.STEP_ON) && ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
            {
                foundfunc = ter.Trigger.Func;
                foundspot = ter.Trigger;
            }
        }

        //Quit if no special node triggers found.
        if (foundfunc == null) return false;

        //Set up the special
        Script.New_MapTrigger(foundfunc, eCallOrigin.MOVING, foundspot, pc, gpos, dir);

        return true;
    }

    public void Search(Location spot, PCType pc)
    {
        string foundfunc = null;
        TriggerSpot foundspot = null;

        var s = SectorAt(spot);
        var local_spot = toLocal(spot);
        var ter = TerrainAt(spot);

        Game.AddMessage("You inspect the " + ter.Name + ".");

        //First look for special encounter nodes here
        foreach (var se in s.TriggerSpotList)
        {
            if (se.Pos == local_spot && se.TriggeredBy(eTriggerSpot.SEARCH) && se.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
            {
                foundfunc = se.Func;
                foundspot = se;
                break;
            }
        }
        //Look for terrain type here with a trigger
        if (foundfunc == null) //Terrain triggers ignored if map trigger is on the same space.
        {
            if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.SEARCH) && ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
            {
                foundfunc = ter.Trigger.Func;
                foundspot = ter.Trigger;
            }
        }

        if (foundfunc != null)
            Script.New_MapTrigger(foundfunc, eCallOrigin.SEARCHING, foundspot, pc, spot, pc.Dir);
        else
        {
            Game.AddMessage("  But find nothing.");
        }
                
    }
}