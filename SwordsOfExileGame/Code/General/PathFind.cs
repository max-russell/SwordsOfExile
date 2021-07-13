using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading;

namespace SwordsOfExileGame
{
    public partial class MapPath
    {
        Stack<eDir> PathToTarget = new Stack<eDir>();
        Location PathPosition, PathDestination;
        bool Calculated = false;
        IMap pathMap;
        ICharacter pathChar;

        class PathNode : IEquatable<PathNode>
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
            Thread t = new Thread(p.Calculate);
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

        MapPath(IMap map, ICharacter ch, Location dest)
        {
            Calculated = false;
            PathPosition = ch.Pos;
            PathDestination = dest;
            pathMap = map;
            pathChar = ch;
        }

        void Calculate()
        {
            //Use A* pathfinding
            List<PathNode> OpenNodes = new List<PathNode>();
            List<PathNode> ClosedNodes = new List<PathNode>();

            OpenNodes.Add(new PathNode { Pos = pathChar.Pos, Parent = null, Score = 0, Level = 0 });
            bool found = false;

            //Work out nasty field aversion based on health remaining
            //If > 100, only minimal aversion
            //Then down to maximum aversion for < 25 health
            int f_aversion = Maths.MinMax(Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_LOW, Constants.PATH_NASTY_FIELD_AVERSION_MAX, pathChar.Health);// 
            f_aversion -= Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_LOW;
            float aver = (float)f_aversion / (float)(Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_HIGH - Constants.PATH_NASTY_FIELD_AVERSION_HEALTH_LOW);
            f_aversion = (int)(aver * (float)(Constants.PATH_NASTY_FIELD_AVERSION_MAX - Constants.PATH_NASTY_FIELD_AVERSION_MIN)) + Constants.PATH_NASTY_FIELD_AVERSION_MIN;

            while (!found && OpenNodes.Count > 0)
            {
                if (OpenNodes[0].Pos.adjacent(PathDestination) || OpenNodes[0].Level >= Constants.PATHFINDLIMIT) { found = true; break; }

                PathNode curnode = OpenNodes[0];
                OpenNodes.RemoveAt(0);
                ClosedNodes.Add(curnode);

                for (int x = curnode.Pos.X - 1; x <= curnode.Pos.X + 1; x++)
                {
                    for (int y = curnode.Pos.Y - 1; y <= curnode.Pos.Y + 1; y++)
                    {
                        Location l = new Location(x, y);

                        if (pathMap.CharacterCanBeThere(l, pathChar) && !ClosedNodes.Contains(new PathNode { Pos = l }))
                        {
                            int sc = curnode.Score + 1 + l.VDistanceTo(PathDestination);

                            if (pathChar is NPC && ((TownMap)pathMap).NPCHateSpot((NPC)pathChar, l)) sc += f_aversion;//Constants.PATH_NASTY_FIELD_AVERSION; //Dislike squares with nasty fields in them

                            var newnode = new PathNode { Pos = l, Score = sc, Parent = curnode, Level = curnode.Level + 1 };

                            var alreadyon = OpenNodes.Find(nd => nd.Pos == l);

                            if (alreadyon != null)
                                if (newnode.Score < alreadyon.Score)
                                    OpenNodes.Remove(alreadyon);
                                else
                                    continue;

                            int n = 0;
                            foreach (PathNode p in OpenNodes)
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
                PathNode node = OpenNodes[0];
                while (node.Parent != null)
                {
                    Add(node.Parent.Pos.DirectionTo(node.Pos));
                    node = node.Parent;
                }
                Calculated = true;
            }
        }

        void Add(eDir d)
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
}