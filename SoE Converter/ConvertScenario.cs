using System;
using System.Text;
using System.IO;

namespace SoE_Converter;

internal partial class Program
{
    private static void SaveScenario()
    {
        Console.WriteLine("Writing scenario: \"" + DataStore5.scen_strs[0] + "\"");
        Console.WriteLine("Writing converted scenario to \"" + NewFilename + "\"");

        short count; int x, y;

        using var fs = new FileStream(NewFilename, FileMode.Create, FileAccess.Write);
        using var Out = new BinaryWriter(fs);
        
        Console.WriteLine("Writing scenario header...");

        //First, write our new scenario tag (as an array of chars so it's not length prefixed.
        Out.Write(SCENARIO_FILE_KEY);
        //Then file version number.
        Out.Write(SCENARIO_FILE_VERSION);

        //Now write scenario data.
        Out.Write(DataStore5.scen_strs[0]); //Scenario name
        Out.Write(Scenario.ver);   //Version numbers

        var f = Path.GetFileNameWithoutExtension(NewFilename).ToUpper();

        //If one of Jeff's 3 original scenarios, use the longer description from the BoE program.
        if (f == "VALLEYDY")
            Out.Write("The crops have withered, the children are dying, and even the water burns. Can you find the source of the sickness before the entire valley dies?");
        else if (f == "STEALTH")
            Out.Write("The enemy - a secret band of deadly rebels. The job - infiltrate them, win their trust, and find their leader. The question - are you fighting on the right side?");
        else if (f == "ZAKHAZI")
            Out.Write("A fortress is under siege, and only you can get them the weapons they need to survive. You have 20 days to find your way through the nastiest caves in Exile, or all will be lost.");
        else
            Out.Write(FixYeah(DataStore5.scen_strs[1], false)); //Description

        Out.Write(FixYeah(DataStore5.scen_strs[2], false)); //Credits 1
        Out.Write(FixYeah(DataStore5.scen_strs[3], false)); //Credits 2
        Out.Write(FixYeah(DataStore5.scen_strs[4], false)); //Contact info
        Out.Write(Scenario.rating);
        Out.Write(Scenario.difficulty);
        Out.Write(Scenario.intro_pic);

        // ^^^^ Loaded up to here when scenario info is loaded for Scenario Select window in game.

        Out.Write(Scenario.default_ground);
        Out.Write(Scenario.intro_mess_pic);

        //Write Death message
        Out.Write("Being an adventurer is unpredictable work. Sometimes, you becomes heroes, wealthy as Croesus and famous beyond words. " +
                  "And, sometimes your gnawed bones are left to dry out in some shadowy, forgotten hole.@n@n" +
                  "Unfortunately, the latter fate is the one that just befell you. Easy come, easy go. Care to make another attempt?");

        Out.Write("Initialise_Scenario"); //Write Initialise scenario function name (non-latent function) - Not used in converted BoE scenarios
        Out.Write("Intro_Message"); //Write start scenario function name (latent function)

        //Only make the town pre-entry func if there are any set
        if (HasTownPreEntryFunc)
            Out.Write("Town_Pre_Entry");
        else
            Out.Write("");

        Out.Write((ushort)28); //Size of combat area: Width
        Out.Write((ushort)28); //  "           "    : Height
        Out.Write("Generate_Combat_Map"); //Script function for generating the combat map

        //Write outdoors headers - which is basically just the name of the area.
        Console.WriteLine("Writing outdoor headers");

        for (x = 0; x < Scenario.out_width; x++)
        for (y = 0; y < Scenario.out_height; y++)
        {
            LoadOutdoors(x, y);
            Out.Write((byte)1);//Outdoor sector follows
            Out.Write((short)x); //Sector coordinates.
            Out.Write((short)y);
            Out.Write(""); //Folder
            Out.Write(DataStore4.outdoor_text[0]); //Name
        }
        Out.Write((byte)0); //End of outside headers

        //Now write town headers
        Console.WriteLine("Writing town headers");

        for (x = 0; x < Scenario.num_towns; x++)
        {
            LoadTown(x);  //Load town purely to get the name of the town. Super efficient, I know.
            Out.Write((byte)1); //Town follows
            Out.Write(Town_IDs[x]); //ID
            Out.Write(""); //Folder

            Out.Write(DataStore1.town_strs[0]); //Town name

            Out.Write(Scenario.town_hidden[x] != 0);

            var sz = (short)GetTownSize(x);
            Out.Write(sz); Out.Write(sz);

            //Write item storage rectangles, if there is one here. There can only be one per town, so if there isn't one here, write FALSE
            for (y = 0; y < 3; y++)
            {
                if (Scenario.store_item_towns[y] == x)
                {
                    Out.Write(true);
                    SaveRECT16(Scenario.store_item_rects[y], Out);
                    y = 10; break;
                }
            }
            if (y != 10) Out.Write(false);
        }
        Out.Write((byte)0); //End of town headers

        Out.Write(Town_IDs[Scenario.which_town_start]);
        SaveLocation(Scenario.where_start, Out); //Town tile coordinates to start in
        SaveLocation(Scenario.out_sec_start, Out); //Outside sector coordinates
        SaveLocation(Scenario.out_start, Out);     //Tile coordinates within sector

        #region VEHICLES
        //Save boats and horses. We're collating both into one list, 'Vehicles'. But we have to change special nodes type 15&16 that reference a horse or
        //boat, so that they refer to the right one.
        for (x = 0; x < 30; x++)
        {
            if (Scenario.scen_horses[x].which_town != -1)
            {
                Out.Write((byte)1); //Vehicle follows
                Out.Write("Horse_" + x); //Write ID
                Out.Write(""); //Folder ID
                Out.Write((byte)0); //0 for a horse
                Out.Write(Town_IDs[Scenario.scen_horses[x].which_town]);
                SaveLocation(Scenario.scen_horses[x].boat_loc, Out);
                Out.Write(Scenario.scen_horses[x].property != 0);
            }
        }
        for (x = 0; x < 30; x++)
        {
            if (Scenario.scen_boats[x].which_town != -1)
            {
                Out.Write((byte)1); //Vehicle follows
                Out.Write("Boat_" + x); //Write ID
                Out.Write(""); // Folder ID
                Out.Write((byte)1); //1 for a boat
                Out.Write(Town_IDs[Scenario.scen_boats[x].which_town]);
                SaveLocation(Scenario.scen_boats[x].boat_loc, Out);
                Out.Write(Scenario.scen_boats[x].property != 0);
            }
        }
        Out.Write((byte)0); //No more vehicles
        FixBoatSpecialNodes(ref Scenario.scen_specials); //Fix special nodes for the scenario (we'll also have to change town and outdoor specials later)

        #endregion

        #region SPECIAL ITEMS

        ////Save special items - Count how many there are, by discarding the ones with the default name, but only if there aren't proper ones after it.
        ////This is just in case someone has left a gap between existing special items, so that their indices remain the same.
        //count = 50;
        //for (x = 49; x >= 0; x--)
        //    if (DataStore5.scen_strs[x * 2 + 60] == "Unused Special Item") count--; else break;
        //Out.Write(count); //Number of special items
        for (x = 0; x < 50; x++)
        {
            if (DataStore5.scen_strs[x * 2 + 60] != "Unused Special Item")
            {
                Out.Write((byte)1);
                Out.Write(SpecialItemList[x]);//GetSpecialItemName(x)); //ID
                Out.Write(""); //Folder ID
                Out.Write(DataStore5.scen_strs[x * 2 + 60]); //Name
                Out.Write(DataStore5.scen_strs[x * 2 + 61]); //Description
                Out.Write(Scenario.special_items[x] >= 10 ? true : false); //Starts with item?
                Out.Write(Scenario.special_items[x] % 10 == 1 ? true : false); //Can be used
                Out.Write(GetNodeToFuncName(Scenario.special_item_special[x], 0, 0, 0)); //Special node to call when used; //************************
            }
        }
        Out.Write((byte)0); //No more special items

        #endregion

        #region TIMERS

        //Special event timers: These are NOT afftected by special nodes 'Set General Timer', as those switch on separate 'party' timers
        //count = 0;
        //long timercountpos = fs.Position;
        //Out.Write(count); //Leave space

        for (x = 0; x < 20; x++)
            if (Scenario.scenario_timer_times[x] > 0)
            {
                //count++;
                Out.Write((byte)1);
                Out.Write("GlobalTimer_" + x); //ID
                Out.Write(""); //Folder ID
                Out.Write(true); //Enabled
                Out.Write(Scenario.scenario_timer_times[x]); 
                Out.Write(GetNodeToFuncName(Scenario.scenario_timer_specs[x], 0, 0, 0)); //************************
                Out.Write(""); //Domain - global
                Out.Write(true); //Recurring
                //Cos global no timer behaviour needed
            }

        for (var townnum = 0; townnum < Scenario.num_towns; townnum++)
        {
            LoadTown(townnum);

            for (x = 0; x < 8; x++) //Write normal town timers
            {
                if (Town.timer_spec_times[x] != 0)
                {
                    Out.Write((byte)1);
                    Out.Write("TimerT_" + townnum + "_" + x); //ID
                    Out.Write(""); //Folder ID
                    Out.Write(true); //Enabled;
                    Out.Write(Town.timer_spec_times[x]);
                    Out.Write(GetNodeToFuncName(Town.timer_specs[x], 1, townnum, 0)); //************************
                    Out.Write(Town_IDs[townnum]); //Domain
                    Out.Write((byte)2); //CONTINUE timer type (continues ticking even when out of town, but doesn't trigger)
                    Out.Write(true); //Recurring
                }
            }

            for (x = 0; x < 4; x++) //Write wandering monster town timers
                if (!(Town.wandering[x].monst[0] == 0 && Town.wandering[x].monst[1] == 0 && Town.wandering[x].monst[2] == 0 && Town.wandering[x].monst[3] == 0))
                {
                    Out.Write((byte)1);
                    Out.Write("TimerW_" + townnum + "_" + x); //ID
                    Out.Write(""); //Folder ID
                    Out.Write(true); //Enabled
                    Out.Write((short)10);
                    Out.Write("Generate_Wandering_" + townnum + "_" + GetFriendlyIDString(DataStore1.town_strs[0]));
                    Out.Write(Town_IDs[townnum]); //Domain
                    Out.Write((byte)2); //CONTINUE timer type (continues ticking even when out of town, but doesn't trigger)
                    Out.Write(true); //Recurring
                    break;
                }
        }
        Out.Write((byte)0); //End of timers

        #endregion

        #region TERRAIN UNDERLAYS

        SaveFolder(0, "Underlays", Out);

        //Save Terrain records (underlays)
        for (x = 0; x < 256; x++)
        {
            Out.Write((byte)1);
            Out.Write(GetTerrainID(x)); //ID
            Out.Write("\t0"); //Folder it's in.

            Out.Write((short)x); //Terrain number
            Out.Write((byte)0);  //Underlay layer.

            var m = Encoding.ASCII.GetString(ScenItems.ter_names, x * 30, 30);
            m = m.Remove(m.IndexOf((char)0));

            Out.Write(m); //Name

            switch (Scenario.ter_types[x].picture)
            {
                //Custom animated terrain
                case >= 2000:
                    Out.Write((UpdateCustomList(CustomAnimTerrainList, Scenario.ter_types[x].picture - 2000)));
                    break;
                //Custom static
                case >= 1000:
                    Out.Write(UpdateCustomList(CustomTerrainList, Scenario.ter_types[x].picture - 1000));
                    break;
                case >= 400:
                    Out.Write((int)(Scenario.ter_types[x].picture - 400) + 65536);
                    break;
                default:
                    Out.Write((int)Scenario.ter_types[x].picture);
                    break;
            }

            //Translate blockage to new system with separate values for Blocking and Obscurity
            if (Scenario.ter_types[x].picture == 404) //Lava
            {
                Out.Write((byte)2); Out.Write((byte)0);
            }
            else
            {
                switch (Scenario.ter_types[x].blockage)
                {                     //    v Blockage          v Obscurity
                    case 0: Out.Write((byte)0); Out.Write((byte)0); break;
                    case 1: Out.Write((byte)0); Out.Write((byte)255); break;
                    case 2: Out.Write((byte)1); Out.Write((byte)0); break;
                    case 3: Out.Write((byte)3); Out.Write((byte)0); break;
                    case 4: Out.Write((byte)3); Out.Write((byte)1); break;
                    case 5: Out.Write((byte)3); Out.Write((byte)255); break;
                }
            }

            Out.Write((byte)((Scenario.ter_types[x].fly_over << 2) | (Scenario.ter_types[x].boat_over << 1) | (Scenario.ter_types[x].block_horse)));
            Out.Write(x == 90 || (x >= 50 && x <= 64) || x == 71 || (x >= 74 && x <= 78)); //Write if destroys barrel that are pushed onto it.
            Out.Write(Scenario.ter_types[x].step_sound);
            Out.Write(Scenario.ter_types[x].light_radius);

            //Write editor icon. The little icon that can get displayed in the corner of the tile in the map view.
            if (Scenario.ter_types[x].blockage == 1  //Walkthrough/opaque
                || Scenario.ter_types[x].special == 1) //Change when step on.
                Out.Write((byte)23); //Little blue 's'
            else switch (Scenario.ter_types[x].special)
            {
                //Does fire damage
                case 2:
                    Out.Write((byte)37); //Red circle
                    break;
                //Does cold damage
                case 3:
                    Out.Write((byte)38); //Blue circle
                    break;
                //Does magical damage
                case 4:
                    Out.Write((byte)39); //Lilac circle
                    break;
                //Poison land
                case 5:
                    Out.Write((byte)35); //Green P
                    break;
                //Diseased land
                case 6:
                    Out.Write((byte)33); //Lilac circle
                    break;
                //Crumbling terrain
                case 7:
                    Out.Write((byte)34); //Blue A
                    break;
                case 9:
                //Unlockable terrain
                case 10:
                {
                    if (Scenario.ter_types[x].flag2 <= 4)
                        Out.Write((byte)30); //Green L
                    else if (Scenario.ter_types[x].flag2 <= 9)
                        Out.Write((byte)31); //Green M
                    else
                        Out.Write((byte)32); //Black I
                    break;
                }
                //Sign
                case 11:
                    Out.Write((byte)26); //Sign
                    break;
                //Container
                case 14:
                    Out.Write((byte)36);
                    break;
                //Conveyor N
                case 16:
                    Out.Write((byte)27); //N arrow
                    break;
                //Conveyor E
                case 17:
                    Out.Write((byte)28); //E arrow
                    break;
                //Conveyor S
                case 18:
                    Out.Write((byte)29); //S arrow
                    break;
                //Conveyor W
                case 19:
                    Out.Write((byte)20); //W arrow
                    break;
                //Blocked to monsters
                case 20:
                    Out.Write((byte)21); //Black B
                    break;
                default:
                    Out.Write((byte)255);
                    break;
            }

            if ((Scenario.ter_types[x].special >= 15 && Scenario.ter_types[x].special <= 19) //Disregard waterfalls (they are now automatically converted to map triggers), and conveyor belts (terrain trigger)
                || Scenario.ter_types[x].special == 11 //Ditto signs (map trigger)
                || Scenario.ter_types[x].special == 12 //Ditto call LOCAL node
                || Scenario.ter_types[x].special == 13 //Ditto call SCENARIO node
                || Scenario.ter_types[x].special == 23) //Ditto call SCENARIO node on use
                Out.Write((byte)0); 
            else Out.Write(Scenario.ter_types[x].special);  //Special property

            //Write the 'transform to' property as the terrain id to transform to
            Out.Write(Scenario.ter_types[x].trans_to_what == 0
                ? string.Empty
                : GetTerrainID(Scenario.ter_types[x].trans_to_what));

            //Write Flag 1, type dependent on the special property.
            int tsp = Scenario.ter_types[x].special;
            if (tsp == 1 || (tsp >= 7 && tsp <= 10) || tsp == 22) //Flag 1 is a terrain id
                Out.Write(GetTerrainID(Scenario.ter_types[x].flag1));
            else
                Out.Write((short)Scenario.ter_types[x].flag1);  //Extra data for special property

            //Write Flag 2, type dependent on the special property
            if (tsp == 1)
                Out.Write(GetSoundID(Scenario.ter_types[x].flag2));
            else                
                Out.Write((short)Scenario.ter_types[x].flag2);

            switch (Scenario.ter_types[x].special)
            {
                //Special to call
                case 12:
                    Out.Write(true); //This terrain HAS a trigger.
                    Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.STEP_ON_CMBT | eTriggerSpot.PCS_TRIGGER)); //Triggered by stepping on, including during combat
                    Out.Write("TerrainLocal_" + GetFriendlyIDString(m) + "_" + x); //Function name
                    Out.Write((short)0); //No extra variables.
                    break;
                case 13:
                //Called SCENARIO node
                case 23:
                {
                    Out.Write(true); //This terrain HAS a trigger.
                    if (Scenario.ter_types[x].special == 23)
                        Out.Write((byte)(eTriggerSpot.USE | eTriggerSpot.PCS_TRIGGER)); //Triggered by Using
                    else
                        Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.STEP_ON_CMBT | eTriggerSpot.PCS_TRIGGER)); //Triggered by stepping on, NOT searching
                    Out.Write(GetNodeToFuncName(Scenario.ter_types[x].flag1, 0, 0, 0));   //Function name
                    Out.Write((short)0); //No extra variables.
                    break;
                }
                //Conveyor belt trigger
                case >= 16 and <= 19:
                    Out.Write(true); //This terrain HAS a trigger.
                    Out.Write((byte)(eTriggerSpot.STEP_ON | eTriggerSpot.STEP_ON_CMBT | eTriggerSpot.STOOD_ON | eTriggerSpot.PCS_TRIGGER | eTriggerSpot.NPCS_TRIGGER)); //Triggered by stepping on, and being stood on at end of turn, including by NPCs
                    Out.Write("Do_Conveyor_Belt");
                    Out.Write((short)1); //1 extra variable
                    Out.Write("Dir");   //...With this ID
                    Out.Write((byte)0); //...and it's an integer
                    Out.Write((int)(Scenario.ter_types[x].special - 16)); //And this is its value - the direction of this piece of conveyor belt.
                    break;
                default:
                    Out.Write(false); //This terrain doesn't have a trigger.
                    break;
            }

            if (x == 85 || x == 86)
                Out.Write("PlaceRubbleCave"); ///Editor script
            else if (x == 88 || x == 89)
                Out.Write("PlaceRubbleGrass");
            else if (x is >= 22 and <= 35 || (Scenario.ter_types[x].picture is >= 18 and <= 31) || (Scenario.ter_types[x].picture is >= 192 and <= 195))
                Out.Write("PlaceMountain");
            else
                Out.Write("");
        }

        #endregion

        #region TERRAIN OVERLAYS

        SaveFolder(1, "Overlays", Out);
        //Save terrain records (overlays)
        for (x = 0; x < 15; x++)
        {
            Out.Write((byte)1);
            Out.Write("Road_" + x);
            Out.Write("\t1"); //Folder;
            Out.Write((short)(x+1)); //Terrain number
            Out.Write((byte)1); //Overlay layer.

            Out.Write("Road");
            Out.Write((int)(x + 260)); //Picture
            Out.Write((byte)0); //Blockage
            Out.Write((byte)0); //Obscurity
            Out.Write((byte)0); //Extra stuff
            Out.Write(false); //Destroy barrel
            Out.Write(Scenario.ter_types[0].step_sound);
            Out.Write(Scenario.ter_types[0].light_radius);
            Out.Write((byte)255);
            Out.Write(Scenario.ter_types[0].special);
            Out.Write(""); //Change to short to allow more than 256 terrains
            Out.Write((short)Scenario.ter_types[0].flag1);  //Extra data for special property
            Out.Write((short)Scenario.ter_types[0].flag2);
            Out.Write(false); //This terrain doesn't have a trigger.
            Out.Write(""); //Editor script
        }

        Out.Write((byte)1);
        Out.Write("Special"); //ID
        Out.Write("\t1"); //Folder;
        Out.Write((short)(16)); //Terrain number
        Out.Write((byte)1); //Overlay layer.
        Out.Write("Special"); //Name
        Out.Write((int)14 + 65536);
        Out.Write((byte)1); // Blockage
        Out.Write((byte)0);
        Out.Write((byte)0); //Extra stuff
        Out.Write(false); //Destroy barrel
        Out.Write(Scenario.ter_types[0].step_sound);
        Out.Write(Scenario.ter_types[0].light_radius);
        Out.Write((byte)255);
        Out.Write(Scenario.ter_types[0].special);
        Out.Write(""); //Change to short to allow more than 256 terrains
        Out.Write((short)Scenario.ter_types[0].flag1);  //Extra data for special property
        Out.Write((short)Scenario.ter_types[0].flag2);
        Out.Write(false); //This terrain doesn't have a trigger.
        Out.Write(""); ///Editor script

        for (x = 0; x < 5; x++)
        {
            Out.Write((byte)1);
            Out.Write("Walkway_" + x);
            Out.Write("\t1"); //Folder;
            Out.Write((short)(x + 17)); //Terrain number
            Out.Write((byte)1); //Overlay layer.
            Out.Write("Walkway");

            if (x == 4)
                Out.Write((int)215);
            else
                Out.Write((int)(x + 275)); //Picture
            Out.Write((byte)0); //Blockage
            Out.Write((byte)0); //Obscurity
            Out.Write((byte)0); //Extra stuff
            Out.Write(false); //Destroy barrel
            Out.Write(Scenario.ter_types[0].step_sound);
            Out.Write(Scenario.ter_types[0].light_radius);
            Out.Write((byte)255);
            Out.Write(Scenario.ter_types[0].special);
            Out.Write(""); //Change to short to allow more than 256 terrains
            Out.Write((short)Scenario.ter_types[0].flag1);  //Extra data for special property
            Out.Write((short)Scenario.ter_types[0].flag2);
            Out.Write(false); //This terrain doesn't have a trigger.
            Out.Write(""); ///Editor script
        }
        Out.Write((byte)0);

        #endregion

        //Write Spells
        MagicSpell.WriteSpells(Out);

        #region ITEMS

        for (x = 0; x < 400; x++)
        {
            var m = Encoding.ASCII.GetString(ScenItems.scen_items[x].full_name);
            m = m.Remove(m.IndexOf((char)0));
            if (m == "Empty") continue;

            Out.Write((byte)1);
            Out.Write(GetItemID(x));
            Out.Write(""); //Folder
            Out.Write(m);

            m = Encoding.ASCII.GetString(ScenItems.scen_items[x].name);
            m = m.Remove(m.IndexOf((char)0));
            Out.Write(m);

            Out.Write(ScenItems.scen_items[x].variety); Out.Write(ScenItems.scen_items[x].item_level);                                                  //4
            Out.Write(ScenItems.scen_items[x].awkward); Out.Write(ScenItems.scen_items[x].bonus);
            Out.Write(ScenItems.scen_items[x].protection); Out.Write((short)ScenItems.scen_items[x].charges);
            Out.Write(ScenItems.scen_items[x].type); Out.Write(ScenItems.scen_items[x].magic_use_type);

            if (ScenItems.scen_items[x].graphic_num >= 150)
                Out.Write((short)(UpdateCustomList(CustomItemList, ScenItems.scen_items[x].graphic_num - 150)));
            else
                Out.Write((short)ScenItems.scen_items[x].graphic_num);

            if (ScenItems.scen_items[x].ability >= 110 && ScenItems.scen_items[x].ability <= 135) Out.Write((byte)177);
            else if (ScenItems.scen_items[x].ability >= 150 && ScenItems.scen_items[x].ability <= 157) Out.Write((byte)0);
            else Out.Write(ScenItems.scen_items[x].ability);

            Out.Write(ScenItems.scen_items[x].ability_strength); Out.Write(ScenItems.scen_items[x].type_flag);
            Out.Write(ScenItems.scen_items[x].is_special); Out.Write(ScenItems.scen_items[x].a);      //6
            Out.Write(ScenItems.scen_items[x].value);                                                                //2
            Out.Write(ScenItems.scen_items[x].weight); Out.Write(ScenItems.scen_items[x].special_class);
            SaveLocation(ScenItems.scen_items[x].item_loc, Out);                                                        //2
            Out.Write(ScenItems.scen_items[x].treas_class); Out.Write(ScenItems.scen_items[x].item_properties);//, reserved1, reserved2;                    //4

            switch (ScenItems.scen_items[x].ability)
            {
                case 110: Out.Write("m_flame"); break;     //Same as mage spell - target
                case 111: Out.Write("m_fireball"); break;  //t
                case 112: Out.Write("m_fire_storm"); break; //t 
                case 113: Out.Write("m_kill"); break;      //t
                case 114: Out.Write("m_ice_bolt"); break;  //t
                case 115: Out.Write("m_slow"); break;      //t
                case 116: Out.Write("m_shockwave"); break;  //*** no target
                case 117: Out.Write("p_dispel_undead"); break;
                case 118: Out.Write("p_ravage_spirit"); break;
                case 119: Out.Write("i_summoning"); break;    //*** no target
                case 120: Out.Write("i_mass_summoning"); break; //*** no target
                case 121: Out.Write("i_acid_spray"); break;   //Unique to items
                case 122: Out.Write("i_stinking_cloud"); break; //Unique to items
                case 123: Out.Write("m_sleep_cloud"); break;
                case 124: Out.Write("m_poison"); break;
                case 125: Out.Write("m_shockstorm"); break;
                case 126: Out.Write("i_paralysis"); break; //Unique to items
                case 127: Out.Write("i_web"); break;        //Unique to items
                case 128: Out.Write("i_strengthen"); break; //Unique to items wand of carrunos effect
                case 129: Out.Write("i_quickfire"); break;  //Unique to items - no target
                case 130: Out.Write("i_mass_charm"); break; //Unique to items - no target
                case 131: Out.Write("i_magic_map"); break;  //Unique to items - no target
                case 132: Out.Write("m_dispel_barrier"); break;
                case 133: Out.Write("i_make_ice_wall"); break; //Unique to items
                case 134: Out.Write("p_charm_foe"); break;
                case 135: Out.Write("m_antimagic_cloud"); break;
                default: Out.Write(""); break;
            }
            switch (ScenItems.scen_items[x].ability)
            {
                case 150: Out.Write("holly"); break;
                case 151: Out.Write("comfrey_root"); break;
                case 152: Out.Write("glowing_nettle"); break;
                case 153: Out.Write("wormgrass"); break;
                case 154: Out.Write("asptongue"); break;
                case 155: Out.Write("ember_flowers"); break;
                case 156: Out.Write("graymold"); break;
                case 157: Out.Write("mandrake"); break;
                default: Out.Write(""); break;
            }
        }
        Out.Write((byte)0); //End of items

        #endregion

        #region PERSONALITIES

        //Save talking personalities - we save them all here rather than in each town so we can have as many as we like and they can move between towns
        //DataStore3.talk_strs: index 0-9 = Personality Name  10-19=Look  20-29=Name (Response to asking)  30-39=Job     160-169=Don't understand response
        //                      40-159 - Talking node strings (part 1 followed by part 2)
        Console.WriteLine("Writing all personalities");

        //Each personality can also link to another personality to use their dialogue too. This is to be used for where
        //dialogue nodes use personality '-2' so everyone in that town responds to it.

        count = 0;

        for (x = 0; x < Scenario.num_towns; x++)
        {
            short towncount = 0;
            LoadTown(x);

            for (y = 0; y < 10; y++)
                if (DataStore3.talk_strs[y] != "Unused") towncount++;
            var has_general_personality = "";

            SaveFolder((short)x, DataStore1.town_strs[0], Out);

            //Are there any -2 dialogue nodes in this town? If so we make an abstract personality and all the real personalities
            //in the town will link to it.
            for (var n = 0; n < 60; n++)
            {
                if (Talking.talk_nodes[n].personality == -2)
                {
                    Console.WriteLine("  " + count + ": General dialogue for everyone in " + DataStore1.town_strs[0]);
                    Out.Write((byte)1);

                    has_general_personality = string.Format("Everyone_in_{0}_{1}", GetFriendlyIDString(DataStore1.town_strs[0]), count);
                    Out.Write(has_general_personality); //ID
                    Out.Write("\t" + x); //Folder
                    Out.Write(""); //Parent
                    Out.Write(""); //Name
                    Out.Write(""); //Look
                    Out.Write(""); //Name response
                    Out.Write(""); //Job response
                    Out.Write(""); //Don't Understand
                    SaveTalkNodes(Out, x, -2);
                    Personality_IDs.Add(-1);
                    count++;
                    break;
                }
            }

            for (y = 0; y < 10; y++)
            {
                if (towncount == 0) break;
                if (DataStore3.talk_strs[y] != "Unused")
                {
                    Console.WriteLine("  " + count + ": " + DataStore3.talk_strs[y]);
                    Out.Write((byte)1);
                    Out.Write(string.Format("{0}_{1}", GetFriendlyIDString(DataStore3.talk_strs[y]), count)); //ID
                    Out.Write("\t" + x); //Folder
                    Out.Write(has_general_personality); //Parent
                    Out.Write(DataStore3.talk_strs[y]);     //Name
                    Out.Write(DataStore3.talk_strs[y + 10]);  //Look
                    Out.Write(DataStore3.talk_strs[y + 20]);  //Name Response
                    Out.Write(DataStore3.talk_strs[y + 30]);  //Job Response

                    if (DataStore3.talk_strs[y + 160] != "")
                        Out.Write(DataStore3.talk_strs[y + 160]); //Don't Understand Response
                    else
                        Out.Write("You get no response.");

                    SaveTalkNodes(Out, x, x * 10 + y);
                    towncount--;

                    Personality_IDs.Add(x * 10 + y);
                    count++;
                }
            }
        }
        Out.Write((byte)0); //End of personalities

        #endregion

        #region SHOPS
        //Save shops
        Console.WriteLine("WritingShops");

        //First write the 'Jumble Shops'
        for (x = 0; x < 5; x++)
        {
            foreach (var shop in ItemShops)
            {
                if (shop.JumbleShop && shop.JumbleShopNo == x)
                {
                    Out.Write((byte)1);
                    Out.Write("Jumble_Shop_" + x); //ID
                    Out.Write("");
                    Out.Write((byte)shop.Type);
                    Out.Write(4000); //How often in turns the Restock function runs.
                    Out.Write("Restock_Jumble_Shop_" + x); //The script function to restock the shop.
                    Out.Write((short)shop.CostLevel);
                    Out.Write(shop.Name);
                    Out.Write((uint)0); //Won't buy anything from the player
                    count++;
                    break;
                }
            }

        }

        //Now all the normal shops (except the Jumble Shops in the list)
        foreach (var shop in ItemShops)
        {
            if (!shop.JumbleShop)
            {
                Out.Write((byte)1);
                Out.Write(shop.ID);
                Out.Write("");
                Out.Write((byte)shop.Type);
                Out.Write(-1); //INT  Normal shops never restock after the first time.
                Out.Write("Restock_" + shop.ID);
                Out.Write((short)shop.CostLevel);
                Out.Write(shop.Name);
                Out.Write(shop.BuysOffPlayer); //UINT;
                count++;
            }
        }
        Out.Write((byte)0); //End of shops

        #endregion

        #region NPC Records

        //Save Monster records
        for (x = 0; x < 256; x++)
        {
            Out.Write((byte)1);
            Out.Write(GetNPCID(x));
            Out.Write(""); //Folder
            var m = Encoding.ASCII.GetString(ScenItems.monst_names, x * 20, 20);
            m = m.Remove(m.IndexOf((char)0));
            Out.Write(m);

            Out.Write((short)Scenario.scen_monsters[x].m_num); 
            Out.Write((short)Scenario.scen_monsters[x].level);                                              //2
            Out.Write(Scenario.scen_monsters[x].health); 
            Out.Write((short)Scenario.scen_monsters[x].armor); 
            Out.Write((short)Scenario.scen_monsters[x].skill);                                              //2
                    
            //Split attack amount and multiplier out to separate values
            Out.Write((short)(Scenario.scen_monsters[x].a[0] / 100 + 1));
            Out.Write((short)(Scenario.scen_monsters[x].a[0] % 100));
            Out.Write((short)(Scenario.scen_monsters[x].a[1] / 100 + 1));
            Out.Write((short)(Scenario.scen_monsters[x].a[1] % 100));
            Out.Write((short)(Scenario.scen_monsters[x].a[2] / 100 + 1));
            Out.Write((short)(Scenario.scen_monsters[x].a[2] % 100));

            Out.Write(Scenario.scen_monsters[x].a1_type); Out.Write(Scenario.scen_monsters[x].a23_type);
            Out.Write(Scenario.scen_monsters[x].m_type);

            if (x == 38 || x == 39) { Out.Write("033_gethit2"); Out.Write(""); }
            else if (x == 45 || Scenario.scen_monsters[x].m_type == 9) { Out.Write("029_monsterdeath2"); Out.Write(""); }
            else
            {
                switch (Scenario.scen_monsters[x].m_type)
                {
                    case 3:
                    case 4:
                    case 5:
                    case 0:
                        Out.Write("029_monsterdeath2"); Out.Write("030_monsterdeath3");
                        break;
                    case 1:
                    case 2:
                    case 7:
                    case 8:
                    case 11:
                        Out.Write("031_monsterdeath4"); Out.Write("032_gethit1");
                        break;
                    default:
                        Out.Write("033_gethit2"); Out.Write("");
                        break;
                }
            }

            Out.Write(Scenario.scen_monsters[x].speed);
            Out.Write(Scenario.scen_monsters[x].mu);
            Out.Write(Scenario.scen_monsters[x].cl);
            Out.Write(Scenario.scen_monsters[x].breath);
            Out.Write(Scenario.scen_monsters[x].breath_type); 
            Out.Write(Scenario.scen_monsters[x].treasure);
            Out.Write(Scenario.scen_monsters[x].spec_skill); 
            Out.Write(Scenario.scen_monsters[x].poison);
            Out.Write(GetItemID(Scenario.scen_monsters[x].corpse_item));
            Out.Write(Scenario.scen_monsters[x].corpse_item_chance);                          //4                    
            Out.Write(Scenario.scen_monsters[x].immunities);
            Out.Write(Scenario.scen_monsters[x].x_width);
            Out.Write(Scenario.scen_monsters[x].y_width);

            if (Scenario.scen_monsters[x].radiate_1 >= 10 && Scenario.scen_monsters[x].radiate_1 <= 12)
                Out.Write((byte)10);
            else
                Out.Write(Scenario.scen_monsters[x].radiate_1);

            if (Scenario.scen_monsters[x].radiate_1 == 10)
            {
                Out.Write((byte)5);
                Out.Write(GetNPCID(Scenario.scen_monsters[x].radiate_2));
            }
            else if (Scenario.scen_monsters[x].radiate_1 == 11)
            {
                Out.Write((byte)20);
                Out.Write(GetNPCID(Scenario.scen_monsters[x].radiate_2));
            }
            else if (Scenario.scen_monsters[x].radiate_1 == 12)
            {
                Out.Write((byte)50);
                Out.Write(GetNPCID(Scenario.scen_monsters[x].radiate_2));
            }
            else
            {
                Out.Write(Scenario.scen_monsters[x].radiate_2); //6
                Out.Write("");
            }

            Out.Write(Scenario.scen_monsters[x].default_attitude);
            Out.Write(Scenario.scen_monsters[x].summon_type);

            Out.Write((short)((short)Scenario.scen_monsters[x].default_facial_pic-1)); //BoE doesn't allow custom face graphics in default facial pic
                    

            Out.Write(GetMonsterPicNum(Scenario.scen_monsters[x].picture_num));
            if (Scenario.scen_monsters[x].radiate_1 == 15) //Death trigger function
                Out.Write(GetNodeToFuncName(Scenario.scen_monsters[x].radiate_2, 0, 0, 0));   
            else Out.Write("");
        }

        Out.Write((byte)0); //End of NPC records

        #endregion

        #region Outside Encounters

        short foldercount = 0;
        for (var x2 = 0; x2 < Scenario.out_width; x2++)
        for (var y2 = 0; y2 < Scenario.out_height; y2++)
        {
            LoadOutdoors(x2, y2);

            //Write wandering monsters
            var donethis = false;
            for (x = 0; x < 4; x++)
            {
                if (!donethis && (IsUsedEncounter(Outdoors.wandering[x]) || IsUsedEncounter(Outdoors.special_enc[x])))
                {
                    SaveFolder(foldercount, DataStore4.outdoor_text[0], Out);
                    donethis = true;
                }
                SaveNPCGroupRecord(x2, y2, x, Outdoors.wandering[x], foldercount, Out);
                SaveNPCGroupRecord(x2, y2, x + 4, Outdoors.special_enc[x], foldercount, Out);
            }
            if (donethis) foldercount++;
        }
        Out.Write((byte)0); //Write 0 to indicate there are no more NPCGroupRecords

        #endregion

        //That's it for the scenario. Now we know where to write our outdoor sections.

        for (x = 0; x < Scenario.out_width; x++)
        for (y = 0; y < Scenario.out_height; y++)
        {
            LoadOutdoors(x, y);
            Console.WriteLine("Writing outdoors \"" + DataStore4.outdoor_text[0] + "\" (" + x + ", " + y + ") ...");
            FixBoatSpecialNodes(ref Outdoors.specials);
            SaveOutdoors(Out, x, y);
        }

        //Now write the towns
        for (x = 0; x < Scenario.num_towns; x++)
        {
            LoadTown(x);
            Console.WriteLine("Writing town \"" + DataStore1.town_strs[0] + "\" (" + x + ") ...");
            FixBoatSpecialNodes(ref Town.specials);

            SaveTown(x, Out);
        }

        Recipe.WriteRecipes(Out);
    }

    private static void SaveFolder(short num, string name, BinaryWriter Out)
    {
        Out.Write((byte)2); //Write 2 to indicate a folder follows
        Out.Write("\t" + num); //Folder ID
        Out.Write(name); //Folder Name - Same as outside section
        Out.Write(true); //Folder is open
        Out.Write(""); // Folder containing this folder
    }

    private static void SaveTalkNodes(BinaryWriter o, int townnum, int personality)
    {
        //Saves all the talk nodes for a personality with that personality, rather than with the town

        LoadTown(townnum);

        //Write the number of nodes
        var count = 0;
        for (var x = 0; x < 60; x++)
        {
            if (Talking.talk_nodes[x].personality == personality) count++;
        }
        var filepos = o.BaseStream.Position;
        o.Write((short)count);

        //Write node
        for (var x = 0; x < 60; x++)
        {
            if (Talking.talk_nodes[x].personality == personality)
            {
                switch (Talking.talk_nodes[x].type)
                {
                    case 7: case 9: case 10: case 11:
               
                        var shop = ItemShops.Find(s => !s.Outdoors && s.TownNo == townnum && s.NodeNo == x);
                        if (shop != null)
                        {
                            o.Write((byte)2); //To indicate shop
                            o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                            o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                            o.Write(""); //Text response unused
                            o.Write(shop.ID); //ID of the shop here
                            o.Write((byte)0); //Condition type
                            o.Write(""); //Condition variable
                            o.Write((int)0);//Condition value
                            o.Write(false); //Also Set condition variable
                            o.Write(false); //Force end conversation
                        }
                        break;
                    case 23:
                    
                        shop = ItemShops.Find(s => !s.Outdoors && s.TownNo == townnum && s.NodeNo == x);
                        if (shop != null)
                        {
                            if (!shop.JumbleShop) throw new Exception("Jumble shop error!");

                            o.Write((byte)2); //To indicate item shop
                            o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                            o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                            o.Write(""); //Text response unused
                            o.Write("Jumble_Shop_" + shop.JumbleShopNo); //ID of the shop here
                            o.Write((byte)0); //Condition type
                            o.Write(""); //Condition variable
                            o.Write((int)0);//Condition value
                            o.Write(false); //Also Set condition variable
                            o.Write(false); //Force end conversation
                        }
                        break;
                    case 13: case 14: case 15:

                        shop = ItemShops.Find(s => !s.Outdoors && s.TownNo == townnum && s.NodeNo == x);
                        if (shop != null)
                        {
                            o.Write((byte)2); //To indicate item shop
                            o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                            o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                            o.Write(""); //Text response unused
                            o.Write(shop.ID); //ID of the shop here
                            o.Write((byte)0); //Condition type
                            o.Write(""); //Condition variable
                            o.Write((int)0);//Condition value
                            o.Write(false); //Also Set condition variable
                            o.Write(false); //Force end conversation
                        }
                        else
                        {
                            shop = ItemShops.Find(s => s.OtherBuyOffNodes.Contains(x));
                            if (shop != null)
                            {
                                o.Write((byte)2); //To indicate item shop
                                o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                                o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                                o.Write(""); //Text response unused
                                o.Write(shop.ID); //ID of the shop here
                                o.Write((byte)0); //Condition type
                                o.Write(""); //Condition variable
                                o.Write((int)0);//Condition value
                                o.Write(false); //Also Set condition variable
                                o.Write(false); //Force end conversation
                            }
                        }
                        break;
                    case 1: //Depends on flag
                        o.Write((byte)0); //To indicate regular node
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40]); //Talk text (if condition passed)
                        o.Write(""); //Func/Shop ID unused
                        o.Write((byte)4); //Condition type(Less than or equal to) 
                        o.Write(Talking.talk_nodes[x].extras[0] + "_" + Talking.talk_nodes[x].extras[1]); //Condition variable
                        o.Write((int)Talking.talk_nodes[x].extras[2]);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Force end conversation
                        count++;
                        //We add another talking node for the opposite condition

                        o.Write((byte)0); //To indicate regular node
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 41]); //Talk text (if condition passed)
                        o.Write(""); //Func/Shop ID unused
                        o.Write((byte)5); //Condition type (Greater than) 
                        o.Write(Talking.talk_nodes[x].extras[0] + "_" + Talking.talk_nodes[x].extras[1]); //Condition variable
                        o.Write((int)Talking.talk_nodes[x].extras[2]);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Force end conversation
                        break;
                    case 2: //Set flag to 1
                        o.Write((byte)0); //To indicate regular node
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40] + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "\n" + DataStore3.talk_strs[x * 2 + 41] : "")); //Talk text (if condition passed)
                        o.Write(""); //Func/Shop ID unused
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(Talking.talk_nodes[x].extras[0] + "_" + Talking.talk_nodes[x].extras[1]); //Condition variable
                        o.Write((int)1);//Condition value
                        o.Write(true); //Also Set condition variable (YES!)
                        o.Write(false); //Force end conversation
                        break;
                    case 3: case 4: case 5: case 6: case 18: case 19: case 20: case 21: case 22: case 24:
                    case 26: case 27: case 28:
                        //These run a generic function
                        o.Write((byte)1); //To indicate a function is run
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(""); //Text response not used
                        o.Write(string.Format("Talking_{0}_{1}", townnum, x)); //Script function name
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        if (Talking.talk_nodes[x].type >= 26)
                            o.Write(true); //Force end conversation
                        else
                            o.Write(false);
                        break;
                    case 25: //End conversation
                        o.Write((byte)0); //To indicate regular node
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40] + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "\n" + DataStore3.talk_strs[x * 2 + 41] : ""));
                        o.Write(""); //Shop/Func ID not used
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(true); //Force End conversation
                        break;
                    case 8: //Training
                        o.Write((byte)4); //To indicate Trainer
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(""); //Text response not used
                        o.Write(""); //Not used
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Don't force End conversation
                        break;
                    case 12: //Healer
                        o.Write((byte)3); //To indicate Healer
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40]); //Name of the Healer
                        o.Write((byte)Talking.talk_nodes[x].extras[0]); //Price level of healer (NOT A STRING)
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Don't force End conversation
                        break;
                    case 16: //Identify
                        o.Write((byte)5); //To indicate Healer
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40]); //Text response
                        o.Write((int)Talking.talk_nodes[x].extras[0]); //Cost of identification (NOT A STRING)
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Don't force End conversation
                        break;
                    case 17: //Enchant
                        o.Write((byte)6); //To indicate Healer
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40]); //Text response
                        o.Write((byte)Talking.talk_nodes[x].extras[0]); //Type of enchantment (NOT A STRING)
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Don't force End conversation
                        break;
                    case 0: //Regular
                        o.Write((byte)0); //To indicate regular node
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40] + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "\n" + DataStore3.talk_strs[x * 2 + 41] : ""));
                        o.Write(""); //Func/Shop ID unused
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Force End conversation
                        break;
                    case 29: case 30: //Script function
                        o.Write((byte)1); //To indicate a function
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link1));
                        o.Write(Encoding.ASCII.GetChars(Talking.talk_nodes[x].link2));
                        o.Write(DataStore3.talk_strs[x * 2 + 40] + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "\n" + DataStore3.talk_strs[x * 2 + 41] : ""));
                        if (Talking.talk_nodes[x].type == 29)
                            o.Write(GetNodeToFuncName(Talking.talk_nodes[x].extras[0], 1, townnum, 0)); //Function
                        else
                            o.Write(GetNodeToFuncName(Talking.talk_nodes[x].extras[0], 0, 0, 0));
                        o.Write((byte)0); //Condition type (None) 
                        o.Write(""); //Condition variable
                        o.Write((int)0);//Condition value
                        o.Write(false); //Also Set condition variable
                        o.Write(false); //Force End conversation
                        break;
                }
            }
        }

        //Update count, if we've put any more in there.
        var curpos = o.BaseStream.Position;
        o.BaseStream.Seek(filepos, SeekOrigin.Begin);
        o.Write((short)count);
        o.BaseStream.Seek(curpos, SeekOrigin.Begin);
    }

}