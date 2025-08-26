using System;

namespace SwordsOfExileGame;

public partial class TownMap : IMap
{
    private int FOV_light_radius;

    public void UpdateVisible()
    {
        if (Script.suspendMapUpdate) return;

        _Visible = new byte[Width, Height];

        if (Game.Mode == eMode.COMBAT)
        {
            foreach (var pc in Party.EachAlivePC())
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

        Location FOV_origin;
        FOV_origin = pc?.Pos ?? Party.LeaderPC.Pos;
        var FOV_bitno = pc == null ? (byte)255 : (byte)Math.Pow(2, Party.PCList.IndexOf(pc));
        var FOV_bitinverse = (byte)(FOV_bitno ^ 255);
        FOV_light_radius = getLightRadius();

        //Clear visibility
        if (!clear_existing)
        {
            for (var x = 0; x < Width; x++)
            for (var y = 0; y < Height; y++)
                _Visible[x, y] &= FOV_bitinverse;
        }
        _Visible[FOV_origin.X, FOV_origin.Y] |= FOV_bitno;
        _Explored[FOV_origin.X, FOV_origin.Y] = true;

        //This is the traditional Blades of Exile Field of View generation

        int lx = Maths.Max(0, FOV_origin.X - Constants.SIGHT_RANGE),
            rx = Maths.Min(Width, FOV_origin.X + Constants.SIGHT_RANGE + 1),
            ty = Maths.Max(0, FOV_origin.Y - Constants.SIGHT_RANGE),
            by = Maths.Min(Height, FOV_origin.Y + Constants.SIGHT_RANGE + 1);

        for (var y = ty; y < by; y++)
        for (var x = lx; x < rx; x++)
        {
            //Don't do this square if it's been marked visible previously.
            if ((_Visible[x,y] & FOV_bitno) > 0) continue;

            //_Visible[x, y] &= FOV_bitinverse;

            Location p1 = FOV_origin, p2 = new(x,y);

            var storage = 0;
                     
            if (p1.Y == p2.Y)
            {
                if (p1.X > p2.X)
                {
                    for (var count = p1.X - 1; count >= p2.X; count--)
                    {
                        _Visible[count, p1.Y] |= FOV_bitno;
                        _Explored[count, p1.Y] = true;
                        storage += FOV_GetObscurity(new Location(count, p1.Y));
                        if (storage >= Constants.OBSCURITY_LIMIT) break;
                    }
                }
                else
                {
                    for (var count = p1.X + 1; count <= p2.X; count++)
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
                    for (var count = p1.Y - 1; count >= p2.Y; count--)
                    {
                        _Visible[p1.X, count] |= FOV_bitno;
                        _Explored[p1.X, count] = true;
                        storage += FOV_GetObscurity(new Location(p1.X, count));
                        if (storage >= Constants.OBSCURITY_LIMIT) break;
                    }
                else
                    for (var count = p1.Y + 1; count <= p2.Y; count++)
                    {
                        _Visible[p1.X, count] |= FOV_bitno;
                        _Explored[p1.X, count] = true;
                        storage += FOV_GetObscurity(new Location(p1.X, count));
                        if (storage >= Constants.OBSCURITY_LIMIT) break;
                    }
            }
            else
            {
                var dx = p2.X - p1.X;
                var dy = p2.Y - p1.Y;

                if (Math.Abs(dy) > Math.Abs(dx))
                {
                    if (p2.Y > p1.Y)
                        for (var count = 1; count <= dy; count++)
                        {
                            _Visible[p1.X + (count * dx) / dy, p1.Y + count] |= FOV_bitno;
                            _Explored[p1.X + (count * dx) / dy, p1.Y + count] = true;
                            storage += FOV_GetObscurity(new Location(p1.X + (count * dx) / dy, p1.Y + count));
                            if (storage >= Constants.OBSCURITY_LIMIT) break;
                        }
                    else
                        for (var count = -1; count >= dy; count--)
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
                        for (var count = 1; count <= dx; count++)
                        {
                            _Visible[p1.X + count, p1.Y + (count * dy) / dx] |= FOV_bitno;
                            _Explored[p1.X + count, p1.Y + (count * dy) / dx] = true;
                            storage += FOV_GetObscurity(new Location(p1.X + count, p1.Y + (count * dy) / dx));
                            if (storage >= Constants.OBSCURITY_LIMIT) break;
                        }
                    else
                        for (var count = -1; count >= dx; count--)
                        {
                            _Visible[p1.X + count, p1.Y + (count * dy) / dx] |= FOV_bitno;
                            _Explored[p1.X + count, p1.Y + (count * dy) / dx] = true;
                            storage += FOV_GetObscurity(new Location(p1.X + count, p1.Y + (count * dy) / dx));
                            if (storage >= Constants.OBSCURITY_LIMIT) break;
                        }
                }
            }
        }
    }

    public int FOV_GetObscurity(Location l)
    {

        if (LightType > 0 && 
            !fieldsThere(l, Field.LIGHT.Bit))
        {
            var near_pc = false;
            foreach (var pc in Party.EachIndependentPC())
                if (pc.Pos.DistanceTo(l) <= FOV_light_radius) { near_pc = true; break; }
            if (!near_pc)
                return Constants.OBSCURITY_LIMIT + 1;
        }

        var what_terrain = TerrainAt(l);
        var store = what_terrain.Obscurity;
        store += fieldObscurityThere(l);
        return store;
    }
}