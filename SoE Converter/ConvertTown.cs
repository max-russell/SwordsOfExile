using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Runtime.InteropServices;
using System.Reflection;
using System.Xml.Linq;

namespace SoE_Converter
{
    partial class Program
    {
        static void SaveTown(int townnum, BinaryWriter Out)
        {
            short count;
            int x, y;

            Out.Write(String.Format("Town_{0:000}_{1}.py", townnum, GetFriendlyIDString(DataStore1.town_strs[0]))); //Default file to write script function to to in the editor

            if (Town.town_chop_time == -1)
                Out.Write((short)-1);
            else
                Out.Write((short)(Town.town_chop_time + (LEGACY_DAY_DELAY ? 20 : 0)));

            if (Town.town_chop_key > 0)
                Out.Write(String.Format("Event_{0}", Town.town_chop_key));
            else Out.Write("");

            Out.Write(Town.lighting); //Lighting level
            
            //Adjust in-town boundary so top left and bottom-right are just INSIDE the town area
            Town.in_town_rect.top++;
            Town.in_town_rect.left++;
            Town.in_town_rect.right--;
            Town.in_town_rect.bottom--;

            SaveRECT16(Town.in_town_rect, Out);

            Out.Write(Town.max_num_monst);
            Out.Write(GetNodeToFuncName(0, 1, townnum, 777)); //Town entry func
            Out.Write(GetNodeToFuncName(0, 1, townnum, 888)); //Town exit func

            if (!LEGACY_NO_TOWN_ANGRY_FUNC)
                Out.Write(GetNodeToFuncName(Town.res1, 1, townnum, 0)); //Func when town turns hostile (only for non-Vogel BoE)
            else
                Out.Write("");

            Out.Write(Town.specials1 % 10 == 1); //Defy mapping
            Out.Write(Town.specials2 % 10 == 1); //Defy scrying
            Out.Write(Town.difficulty);

            ///////////////////////////////////////////////////////////////////////////////
            //Write special encounter trigger spots
            ///////////////////////////////////////////////////////////////////////////////

            count = 0;
            for (x = 0; x < 50; x++)
                if (Town.special_locs[x].x != 100)
                {
                    //We ignore special spots of type 'Secret Passage' unless there are nodes after them in the chain
                    if (Town.specials[Town.spec_id[x]].type == 4 && Town.specials[Town.spec_id[x]].jumpto == -1) continue;

                    //We count twice special spots that begin with 'Ritual of Sanctification Block' nodes - so the game can call separate script funcs if they were triggered by casting a spell or otherwise
                    if (Town.specials[Town.spec_id[x]].type == 24)
                    {
                        if (Town.specials[Town.spec_id[x]].jumpto != -1) count++;
                        if (Town.specials[Town.spec_id[x]].ex1b != -1) count++;
                    }
                    else
                        count++;
                }

            List<location> waterfalls = new List<location>();
            if (!LEGACY_NO_WATERFALL_IN_TOWN)
            {
                //Find all waterfall terrains. Waterfalls are now handled by a script Function, so they need a special trigger on the tile above them.

                int sz = Scenario.town_size[townnum] == 0 ? 64 : (Scenario.town_size[townnum] == 1 ? 48 : 32);

                for (x = 0; x < sz; x++)
                    for (y = 1; y < sz; y++) //Not on the very top row as we can't put a trigger on the tile above it.
                    {
                        if (Scenario.ter_types[TownTerrain.terrain[x * sz + y]].special == 15) //Terrain here is a waterfall
                        {
                            var l = new location();
                            l.x = (sbyte)x; l.y = (sbyte)(y - 1);
                            waterfalls.Add(l);
                        }
                    }
                count += (short)waterfalls.Count;
            }

            //Count signs as triggers now too
            for (x = 0; x < 15; x++)
                if (Town.sign_locs[x].x != 100)
                    count++;

            Out.Write(count); //Write number of trigger spots
            for (x = 0; x < 50; x++)
                if (Town.special_locs[x].x != 100) //Must be on the map
                {
                    if (Town.specials[Town.spec_id[x]].type == 4 && Town.specials[Town.spec_id[x]].jumpto == -1) continue; //Ignore secret passage nodes - these are now saved separately.

                    if (Town.specials[Town.spec_id[x]].type == 24) //Ritual of sanctification.
                    {
                        if (Town.specials[Town.spec_id[x]].jumpto != -1)
                        {
                            SaveLocation(Town.special_locs[x], Out);
                            Out.Write(true); //Active
                            Out.Write((byte)(eTriggerSpot.CAST_SPELL | eTriggerSpot.PCS_TRIGGER)); //Triggered by - sanctify only
                            Out.Write(GetNodeToFuncName(Town.specials[Town.spec_id[x]].jumpto, 1, townnum, 0, true));
                            Out.Write((short)0); //Write number of extra variables
                        }
                        if (Town.specials[Town.spec_id[x]].ex1b != -1)
                        {
                            SaveLocation(Town.special_locs[x], Out);
                            Out.Write(true); //Active
                            Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.SEARCH | eTriggerSpot.PCS_TRIGGER)); //Triggered by step on or search
                            Out.Write(GetNodeToFuncName(Town.specials[Town.spec_id[x]].ex1b, 1, townnum, 0, false));
                            Out.Write((short)0); //Write number of extra variables
                        }
                    }
                    else
                    {
                        SaveLocation(Town.special_locs[x], Out);
                        Out.Write(true); //Active
                        if ((NewTownTerrain[townnum][Town.special_locs[x].x * GetTownSize(townnum) + Town.special_locs[x].y] & 0xFF00) == 0x0F00) //There's a special dot here - can't trigger in combat
                            Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.SEARCH | eTriggerSpot.PCS_TRIGGER)); //Write bits to signify triggered by step on (non-combat) or search
                        else
                            Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.STEP_ON_CMBT | eTriggerSpot.SEARCH | eTriggerSpot.PCS_TRIGGER)); //Write bits to signify triggered by step on (combat & non-combat) or search

                        Out.Write(GetNodeToFuncName(Town.spec_id[x], 1, townnum, 0)); //************************
                        Out.Write((short)0); //Write number of extra variables (none for BoE converted scenarios)
                    }
                }

            if (!LEGACY_NO_WATERFALL_IN_TOWN)
            {
                //Now write the waterfall triggers to the end.
                foreach (location l in waterfalls)
                {
                    SaveLocation(l, Out);
                    Out.Write(true); //Active
                    Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.PCS_TRIGGER)); //Triggered by stepping onto it.
                    Out.Write("Do_Waterfall"); //The same function for all waterfall triggers.
                    Out.Write((short)0); //No extra variables.
                }
            }

            //Now write signs
            for (x = 0; x < 15; x++)
                if (Town.sign_locs[x].x != 100)
                {
                    SaveLocation(Town.sign_locs[x], Out);
                    Out.Write(true); //Active
                    Out.Write((byte)(eTriggerSpot.SEARCH | eTriggerSpot.PCS_TRIGGER)); //Triggered by searching.
                    Out.Write("Do_Sign");
                    Out.Write((short)1); //Write 1 extra variable.
                    Out.Write("Msg");   //...With this ID
                    Out.Write((byte)1); //...and it's a string.
                    Out.Write(GetString(x + 100, 1, true));////DataStore1.town_strs[x + 120].Replace("|", "\n")); //And this is its value.
                }


            ///////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////////////////////////

            //Write info rectangles
            count = 0;
            for (x = 0; x < 16; x++)
                if (TownTerrain.room_rect[x].left != 0 || TownTerrain.room_rect[x].top != 0 || TownTerrain.room_rect[x].right != 0 || TownTerrain.room_rect[x].bottom != 0)
                    count++;
            Out.Write(count);
            for (x = 0; x < 16; x++)
                if (TownTerrain.room_rect[x].left != 0 || TownTerrain.room_rect[x].top != 0 || TownTerrain.room_rect[x].right != 0 || TownTerrain.room_rect[x].bottom != 0)
                {
                    SaveRECT16(TownTerrain.room_rect[x], Out);
                    Out.Write(FixYeah(DataStore1.town_strs[x + 1], false)); //The actual rectangle message
                }

            //Write entry/exit direction stuff
            for (x = 0; x < 4; x++)
            {
                SaveLocation(Town.start_locs[x], Out); //Town entry start points
            }

            //Write preset items
            count = 0;
            for (x = 0; x < 64; x++)
                if (Town.preset_items[x].item_code > -1) count++;
            Out.Write(count);
            for (x = 0; x < 64; x++)
            {
                if (Town.preset_items[x].item_code > -1)
                {
                    Out.Write(GetItemID(Town.preset_items[x].item_code));
                    SaveLocation(Town.preset_items[x].item_loc, Out);
                    Out.Write(Town.preset_items[x].ability);

                    Out.Write(Town.preset_items[x].always_there != 0 ? true : false);
                    Out.Write(Town.preset_items[x].property != 0 ? true : false);
                    Out.Write(Town.preset_items[x].contained != 0 ? true : false);
                }
            }

            List<location> secretpassagelist = new List<location>();
            //FIND SECRET PASSAGES:
            //These were stored as special encounters that trigger special node type 4 - but now they are stored as a preset field type
            //So search all the special encounter spots on the map that directly trigger a node type 4
            for (x = 0; x < 50; x++)
                if (Town.special_locs[x].x != 100)
                    if (Town.specials[Town.spec_id[x]].type == 4)
                        secretpassagelist.Add(new location { x = Town.special_locs[x].x, y = Town.special_locs[x].y });

            //Write preset fields
            count = 0;
            for (x = 0; x < 50; x++)
                if (Town.preset_fields[x].field_type != 0) count++;
            count += (short)secretpassagelist.Count;

            Out.Write(count);

            //For the field type we convert to the value for the eField in the main game
            for (x = 0; x < 50; x++)
            {
                if (Town.preset_fields[x].field_type != 0)
                {

                    short[] f = {0,0,0, /*misc_i fields --> */ 1, 3, 2, 4, 5, 12,
                                 0,0,0,0,0,
                                 14, 15, 16, 17,18, 19,20,21}; //sfx fields

                    Out.Write(f[Town.preset_fields[x].field_type]); //misc_i fields are 3=web to 8==quickfire, sfx fields are 14=sm blood etc,.
                    SaveLocation(Town.preset_fields[x].field_loc, Out);
                }
            }
            foreach (location l in secretpassagelist)
            {
                Out.Write((short)22);
                SaveLocation(l, Out);
            }

            //Write creature starts
            count = 0;
            for (x = 0; x < TownTerrain.creatures.Length; x++)
                if (TownTerrain.creatures[x].number > 0) count++;
            Out.Write(count);
            for (x = 0; x < TownTerrain.creatures.Length; x++)
            {
                if (TownTerrain.creatures[x].number > 0)
                {
                    Out.Write((short)TownTerrain.creatures[x].number);
                    Out.Write(TownTerrain.creatures[x].start_attitude);
                    SaveLocation(TownTerrain.creatures[x].start_loc, Out);
                    Out.Write(TownTerrain.creatures[x].mobile != 0);
                    Out.Write(TownTerrain.creatures[x].time_flag);
                    if (ValidStuffDone(TownTerrain.creatures[x].spec1, TownTerrain.creatures[x].spec2))
                        Out.Write(String.Format("{0}_{1}", TownTerrain.creatures[x].spec1, TownTerrain.creatures[x].spec2));
                    else
                        Out.Write("");
                    Out.Write(TownTerrain.creatures[x].spec_enc_code);
                    if (TownTerrain.creatures[x].time_code > 0) Out.Write(String.Format("Event_{0}", TownTerrain.creatures[x].time_code)); else Out.Write("");
                    Out.Write((short)(TownTerrain.creatures[x].monster_time + (LEGACY_DAY_DELAY ? 20 : 0)));

                    if (TownTerrain.creatures[x].personality == -1)
                        Out.Write((short)-1);
                    else
                    {
                        bool found = false;
                        for (int z = 0; z < Personality_IDs.Count; z++)
                        {

                            if (Personality_IDs[z] == TownTerrain.creatures[x].personality)
                            {
                                Out.Write((short)z);
                                found = true;
                                break;
                            }
                        }
                        if (!found) Out.Write((short)-1);
                    }
                    Out.Write(GetNodeToFuncName(TownTerrain.creatures[x].special_on_kill, 1, townnum, 0)); //************************

                    if (TownTerrain.creatures[x].facial_pic < 1000)
                        Out.Write((short)(TownTerrain.creatures[x].facial_pic - 1));
                    else
                    {
                        Out.Write((short)(UpdateCustomList(CustomFacePicList, TownTerrain.creatures[x].facial_pic - 1000)));//(TownTerrain.creatures[x].facial_pic));
                    }
                }
            }

            //Now terrain and lighting
            for (x = 0; x < NewTownTerrain[townnum].Length; x++)
            {
                Out.Write(NewTownTerrain[townnum][x]);
            }
        }

    }
}