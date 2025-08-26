using System;
using System.Collections.Generic;
using System.Threading;

namespace SwordsOfExileGame;

public partial class MapPath
{
    private Stack<eDir> PathToTarget = new();
    private Location PathPosition, PathDestination;
    private bool Calculated = false;
    private IMap pathMap;
    private ICharacter pathChar;

    private class PathNode : IEquatable<PathNode>
    {
        public Location Pos;
        public PathNode Parent;
        public int Score;
        public int Level;

        public bool Equals(PathNode other)
        {
            return Pos == other.Pos;
        }
    }

    public static MapPath CalculateParallel(IMap map, ICharacter ch, Location dest)
    {
        var p = new MapPath(map, ch, dest);
        var t = new Thread(p.Calculate);
        t.Start();
        return p;
    }

    public static MapPath CalculateNew(IMap map, ICharacter ch, Location dest)
    {
        var p = new MapPath(map, ch, dest);
        p.Calculate();
        if (p.Calculated) return p;
        return null;
    }

    public MapPath()
    {
        Calculated = false;
    }

    private MapPath(IMap map, ICharacter ch, Location dest)
    {
        Calculated = false;
        PathPosition = ch.Pos;
        PathDestination = dest;
        pathMap = map;
        pathChar = ch;
    }

    private void Calculate()
    {
        //Use A* pathfinding
        var OpenNodes = new List<PathNode>();
        var ClosedNodes = new List<PathNode>();

        OpenNodes.Add(new PathNode { Pos = pathChar.Pos, Parent = null, Score = 0, Level = 0 });
        var found = false;

        //Work out nasty field aversion based on health remaining
        //If > 100, only minimal aversion
        //Then down to maximum aversion for < 25 health
        var f_aversion = Maths.MinMax(Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_LOW, Constants.PATH_NASTY_FIELD_AVERSION_MAX, pathChar.Health);// 
        f_aversion -= Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_LOW;
        var aver = (float)f_aversion / (float)(Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_HIGH - Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_LOW);
        f_aversion = (int)(aver * (float)(Constants.PATH_NASTY_FIELD_AVERSION_MAX - Constants.PATH_NASTY_FIELD_AVERSION_MIN)) + Constants.PATH_NASTY_FIELD_AVERSION_MIN;

        while (!found && OpenNodes.Count > 0)
        {
            if (OpenNodes[0].Pos.adjacent(PathDestination) || OpenNodes[0].Level >= Constants.PATHFINDLIMIT) { found = true; break; }

            var curnode = OpenNodes[0];
            OpenNodes.RemoveAt(0);
            ClosedNodes.Add(curnode);

            for (var x = curnode.Pos.X - 1; x <= curnode.Pos.X + 1; x++)
            {
                for (var y = curnode.Pos.Y - 1; y <= curnode.Pos.Y + 1; y++)
                {
                    var l = new Location(x, y);

                    if (pathMap.CharacterCanBeThere(l, pathChar) && !ClosedNodes.Contains(new PathNode { Pos = l }))
                    {
                        var sc = curnode.Score + 1 + l.VDistanceTo(PathDestination);

                        if (pathChar is NPC && ((TownMap)pathMap).NPCHateSpot((NPC)pathChar, l)) sc += f_aversion;//Constants.PATH_NASTY_FIELD_AVERSION; //Dislike squares with nasty fields in them

                        var newnode = new PathNode { Pos = l, Score = sc, Parent = curnode, Level = curnode.Level + 1 };

                        var alreadyon = OpenNodes.Find(nd => nd.Pos == l);

                        if (alreadyon != null)
                            if (newnode.Score < alreadyon.Score)
                                OpenNodes.Remove(alreadyon);
                            else
                                continue;

                        var n = 0;
                        foreach (var p in OpenNodes)
                        {
                            if (sc < p.Score) break;
                            n++;
                        }

                        if (n == OpenNodes.Count)
                            OpenNodes.Add(new PathNode { Pos = l, Parent = curnode, Score = sc });
                        else
                            OpenNodes.Insert(n, new PathNode { Pos = l, Parent = curnode, Score = sc, Level = curnode.Level + 1 });

                    }
                }
            }
        }

        if (found)
        {
            var node = OpenNodes[0];
            while (node.Parent != null)
            {
                Add(node.Parent.Pos.DirectionTo(node.Pos));
                node = node.Parent;
            }
            Calculated = true;
        }
    }

    private void Add(eDir d)
    {
        PathToTarget.Push(d);
    }

    public bool StillValid(Location start, Location end)
    {
        return Calculated && PathToTarget.Count > 0 && start == PathPosition;// && start.VDistanceTo(end) >= start.VDistanceTo(PathDestination);
    }

    public Location GetStart()
    {
        return PathPosition;
    }

    public Location GetDestination()
    {
        return PathDestination;
    }

    public eDir GetNext()
    {
        var d = PathToTarget.Pop();
        PathPosition = PathPosition.Mod(d);
        return d;
    }
}