using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace SoE_Converter
{
    internal partial class Program
    {
        private static void SaveOutdoors(BinaryWriter Out, int ox, int oy)
        {
            int x, y;
            short count = 0;

            //Save the currently loaded outdoor section

            Out.Write(String.Format("Out_{0:000}_{1:000}_{2}.py", ox, oy, GetFriendlyIDString(DataStore4.outdoor_text[0]))); //Default file to write script function to to in the editor
            Out.Write((byte)0); //Level

            //Write terrain
            for (x = 0; x < NewOutsideTerrain[ox, oy].Length; x++)
            {
                Out.Write(NewOutsideTerrain[ox, oy][x]);
            }

            //Find all waterfall terrains. Waterfalls are now handled by a script Function, so they need a special trigger on the tile above them.
            var waterfalls = new List<location>();
            for (x = 0; x < 48; x++)
                for (y = 1; y < 48; y++) //Not on the very top row as we can't put a trigger on the tile above it.
                {
                    if (Scenario.ter_types[Outdoors.terrain[x * 48 + y]].special == 15) //Terrain here is a waterfall
                    {
                        var l = new location();
                        l.x = (sbyte)x; l.y = (sbyte)(y - 1);
                        waterfalls.Add(l);
                    }
                }

            //Write special encounter spots
            for (x = 0; x < 18; x++)
                if (Outdoors.special_locs[x].x != 100)//;0xFF)
                    if (!(Outdoors.specials[Outdoors.special_id[x]].type == 4 && Outdoors.specials[Outdoors.special_id[x]].jumpto == -1)) //Discount special encounter spots that are just secret passages
                        count++;
            count += (short)waterfalls.Count(); //Add the number of waterfall triggers on this map too.

            for (x = 0; x < 8; x++)
                if (Outdoors.sign_locs[x].x != 100)
                    count++;

            Out.Write(count);
            for (x = 0; x < 18; x++)
                if (Outdoors.special_locs[x].x != 100 && !(Outdoors.specials[Outdoors.special_id[x]].type == 4 && Outdoors.specials[Outdoors.special_id[x]].jumpto == -1))
                {//0xFF) {
                    SaveLocation(Outdoors.special_locs[x], Out);
                    Out.Write(true); //Active
                    Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.PCS_TRIGGER)); //Write bits to signify triggered by stepping on
                    Out.Write(GetNodeToFuncName(Outdoors.special_id[x], 2, ox, oy));   //************************
                    Out.Write((short)0); //No extra variables.
                }
            //Now write the waterfall triggers to the end.
            foreach (var l in waterfalls)
            {
                SaveLocation(l, Out);
                Out.Write(true); //Active
                Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.PCS_TRIGGER));
                Out.Write("Do_Waterfall"); //The same function for all waterfall triggers.
                Out.Write((short)0); //No extra variables.
            }
            //Now write signs as triggers with a custom variable holding the message
            for (x = 0; x < 8; x++)
                if (Outdoors.sign_locs[x].x != 100)
                {
                    SaveLocation(Outdoors.sign_locs[x], Out);
                    Out.Write(true); //Active
                    Out.Write((byte)(eTriggerSpot.SEARCH | eTriggerSpot.PCS_TRIGGER)); //Triggered by searching only;
                    Out.Write("Do_Sign");
                    Out.Write((short)1);
                    Out.Write("Msg");
                    Out.Write((byte)1);
                    Out.Write(GetString(x + 90, 2, true));//  DataStore4.outdoor_text[x + 100].Replace("|", "\n")); //The actual sign message
                }


            var secretpassagelist = new List<location>();
            //FIND SECRET PASSAGES:
            //These were stored as special encounters that trigger special node type 4 - but now they are stored as a preset field type
            //So search all the special encounter spots on the map that directly trigger a node type 4
            for (x = 0; x < 18; x++)
                if (Outdoors.special_locs[x].x != 100)
                    if (Outdoors.specials[Outdoors.special_id[x]].type == 4)
                        secretpassagelist.Add(new location { x = Outdoors.special_locs[x].x, y = Outdoors.special_locs[x].y });
            Out.Write((short)secretpassagelist.Count);
            foreach (var l in secretpassagelist)
            {
                SaveLocation(l, Out);
            }

            //Write town entrances
            count = 0;
            for (x = 0; x < 8; x++)
                if (Outdoors.exit_dests[x] >= 0 && Outdoors.exit_locs[x].x != 100)
                    count++;
            Out.Write(count);
            for (x = 0; x < 8; x++)
                if (Outdoors.exit_dests[x] >= 0 && Outdoors.exit_locs[x].x != 100)
                {
                    //Out.Write((short)Outdoors.exit_dests[x]);
                    Out.Write(Town_IDs[Outdoors.exit_dests[x]]);
                    SaveLocation(Outdoors.exit_locs[x], Out);

                    //Write Terrain if hidden.
                    if (Scenario.ter_types[Outdoors.terrain[Outdoors.exit_locs[x].x * 48 + Outdoors.exit_locs[x].y]].special == 21)
                        Out.Write(GetTerrainID(Scenario.ter_types[Outdoors.terrain[Outdoors.exit_locs[x].x * 48 + Outdoors.exit_locs[x].y]].flag1));
                    else
                        Out.Write("");
                }

            //Write info rectangles
            count = 0;
            for (x = 0; x < 8; x++)
                if (Outdoors.info_rect[x].left != 0 || Outdoors.info_rect[x].top != 0 || Outdoors.info_rect[x].right != 0 || Outdoors.info_rect[x].bottom != 0)
                    count++;
            Out.Write(count);
            for (x = 0; x < 8; x++)
                if (Outdoors.info_rect[x].left != 0 || Outdoors.info_rect[x].top != 0 || Outdoors.info_rect[x].right != 0 || Outdoors.info_rect[x].bottom != 0)
                {
                    SaveRECT16(Outdoors.info_rect[x], Out);
                    Out.Write(FixYeah(DataStore4.outdoor_text[x + 1], false)); //The actual rectangle message
                }

            //We don't save wandering/special monster groups here anymore - but we do save a list of all the groups that could spawn in this sector
            for (x = 0; x < 4; x++)
            {
                var emptygroup = true;
                for (y = 0; y < 7; y++)
                    if (Outdoors.wandering[x].monst[y] != 0) { emptygroup = false; break; }
                if (emptygroup) continue;
                Out.Write(String.Format("Group_{0}_{1}_{2}", ox, oy, x));
            }
            Out.Write(""); //Indicate end of list.

            //Write wandering monster spawn points
            Out.Write((short)4);
            for (x = 0; x < 4; x++)
                SaveLocation(Outdoors.wandering_locs[x], Out);
        }
    }
}