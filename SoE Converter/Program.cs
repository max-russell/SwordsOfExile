using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Runtime.InteropServices;
using System.Reflection;
using System.Drawing;
using System.Drawing.Imaging;

namespace SoE_Converter
{
    internal partial class Program
    {
        private const ushort SCENARIO_FILE_VERSION = 3;
        private const string SCENARIO_FILE_KEY = "SWORDSOFEXILESCENARIO";

        private static bool LEGACY_DAY_DELAY = true; //If true, 20 days are added before an event day is triggered (As in original Blades of Exile)
        private static bool LEGACY_NO_TOWN_ANGRY_FUNC = true; //To ignore counting the town res1 property as the special node to call when Town gets Angry 
        private static bool LEGACY_NO_WATERFALL_IN_TOWN = true;

        private static bool DoStartupMap = false;

        private static string Filename = "", NewFilename;

        private static scenario_data_type Scenario;
        private static scen_item_data_type ScenItems;
        private static piles_of_stuff_dumping_type5 DataStore5;
        private static string[] scen_strs_2;

        private static town_record_type Town;
        private static big_tr_type TownTerrain;
        private static piles_of_stuff_dumping_type DataStore1;
        private static talking_record_type Talking;
        private static piles_of_stuff_dumping_type3 DataStore3;

        private static outdoor_record_type Outdoors;
        private static piles_of_stuff_dumping_type4 DataStore4;

        private static bool MacFormat = false;
        private static bool HasTownPreEntryFunc = false;

        private static List<ushort[]> NewTownTerrain = new List<ushort[]>();
        private static ushort[,][] NewOutsideTerrain;

        private static StreamWriter ScriptFile;

        private static int CurrentlyLoadedTown = -1;
        private static int CurrentlyLoadedOutX = -1, CurrentlyLoadedOutY = -1;

        private static List<string> Town_IDs = new List<string>();
        private static List<int> Personality_IDs = new List<int>();

        //Custom graphics lists - used for slicing up the BoE custom graphics into new graphics sheets for SoE
        private static List<int> CustomTerrainList = new List<int>();
        private static List<int> CustomAnimTerrainList = new List<int>();
        private static List<int> CustomNPC1x1List = new List<int>();
        private static List<int> CustomNPC2x1List = new List<int>();
        private static List<int> CustomNPC1x2List = new List<int>();
        private static List<int> CustomNPC2x2List = new List<int>();
        private static List<int> CustomItemList = new List<int>();
        private static List<int> CustomDialogPicList = new List<int>();
        private static List<int> CustomFacePicList = new List<int>();

        private static int Main(string[] args)
        {
#if DEBUG
            Directory.SetCurrentDirectory(@"..\..\..\..");
#endif

            var legacy = true;
            foreach (var s in args)
            {
                if (s.ToUpper() == "-L") {}
                else
                {
                    if (!File.Exists(s))
                    {
                        Console.WriteLine("File not found.");
                        return -1;
                    }
                    Filename = s;
                }
            }
            if (!legacy)
            {
                LEGACY_DAY_DELAY = false;
                LEGACY_NO_TOWN_ANGRY_FUNC = false;
                LEGACY_NO_WATERFALL_IN_TOWN = false;
            }

            Console.WriteLine("Swords of Exile Converter, version: " + System.Reflection.Assembly.GetExecutingAssembly().GetName().Version);

            if (Filename == "")
            {
                Console.WriteLine("Pass a valid Blades of Exile EXS file to this program to convert it.");
                return -1;
            }

            Console.WriteLine("Loading BOE scenario: " + Filename);
            if (LoadScenario())
            {
                NewFilename = Path.GetFileNameWithoutExtension(Filename) + ".EXS2";

                Console.WriteLine("Setting up directories");
                string BaseDirectory;
                BaseDirectory = Path.Combine(Directory.GetCurrentDirectory(), "Base");
                Directory.SetCurrentDirectory("Scenarios");

                Directory.CreateDirectory(Path.GetFileNameWithoutExtension(Filename));
                Directory.SetCurrentDirectory(Path.GetFileNameWithoutExtension(Filename));

                if (Directory.Exists("Images")) Directory.Delete("Images", true);
                Directory.CreateDirectory("Images");
                if (!Directory.Exists("Images")) throw new Exception("Could not create directory 'Images'");

                if (Directory.Exists("Scripts")) Directory.Delete("Scripts", true);
                Directory.CreateDirectory("Scripts");
                if (!Directory.Exists("Scripts")) throw new Exception("Could not create directory 'Scripts'");
                foreach (var f in Directory.EnumerateFiles(Path.Combine(BaseDirectory, "Scripts")))
                    File.Copy(f, Path.Combine("Scripts", Path.GetFileName(f)));

                if (Directory.Exists("EditorScripts")) Directory.Delete("EditorScripts", true);
                Directory.CreateDirectory("EditorScripts");
                if (!Directory.Exists("EditorScripts")) throw new Exception("Could not create directory 'EditorScripts'");
                foreach (var f in Directory.EnumerateFiles(Path.Combine(BaseDirectory, "EditorScripts")))
                    File.Copy(f, Path.Combine("EditorScripts", Path.GetFileName(f)));

                if (Directory.Exists("Data")) Directory.Delete("Data", true);
                Directory.CreateDirectory("Data");
                if (!Directory.Exists("Data")) throw new Exception("Could not create directory 'Data'");

                if (Directory.Exists("Sounds")) Directory.Delete("Sounds", true);
                Directory.CreateDirectory("Sounds");
                if (!Directory.Exists("Sounds")) throw new Exception("Could not create directory 'Sounds'");

                WriteScriptFile();

                SaveScenario();

                var customgfxfile = Path.ChangeExtension(Filename, "BMP");//"PNG");
                SaveCustomGraphics(customgfxfile);
                Console.WriteLine("ALL DONE!");
                Console.WriteLine("FINISH");
                return 0;
            }
            Console.WriteLine("Couldn't load scenario.");
            return -1;
        }

        private static void CopyBitmapArea(Bitmap dest_bmp, Bitmap src_bmp, int sx, int sy, int dx, int dy, int w, int h, bool opaque)
        {
            for (var y = 0; y < h; y++)
            {
                if (sy + y >= src_bmp.Height) continue;
                for (var x = 0; x < w; x++)
                {
                    if (sx + x >= src_bmp.Width) continue;

                    var c = src_bmp.GetPixel(sx + x, sy + y);
                    if (c.R == 255 && c.G == 255 && c.B == 255 && !opaque)
                        c = Color.FromArgb(0, c);
                    else
                        c = Color.FromArgb(255, c);
                    dest_bmp.SetPixel(dx + x, dy + y, c);
                }
            }
        }

        private static void SaveCustomGraphics(string customgfxfile)
        {
            //Convert BMP to PNG
            //We need to work out if a custom tile is used for terrain, dialog picture or custom face. If so, do not make white pixels transparent.
            if (File.Exists(customgfxfile))
            {
                Console.WriteLine("Converting custom graphics sheet to PNG");

                var oldbmp = new Bitmap(customgfxfile);
                

                if (oldbmp.Width != 280)
                {
                    Console.WriteLine("  Failed... Width of custom graphics sheet must be 280 pixels");
                    return;
                }

                //Cut out graphics from custom sheet and make new graphics files in each category.

                //First static terrains
                Bitmap newbmp;

                if (CustomTerrainList.Count > 0)
                {
                    newbmp = new Bitmap(280, (int)Math.Ceiling((double)CustomTerrainList.Count / 10d) * 36);
                    var dn = 0;
                    foreach (var sn in CustomTerrainList)
                    {
                        CopyBitmapArea(newbmp, oldbmp, (sn % 10) * 28, (sn / 10) * 36, (dn % 10) * 28, (dn / 10) * 36, 28, 36, true);
                        dn++;
                    }

                    //Resize terrains from 28x36 to 48x48
                    var b = new Bitmap(480, (int)Math.Ceiling((double)CustomTerrainList.Count / 10d) * 48);
                    using (var g = Graphics.FromImage((Image)b))
                    {
                        g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.NearestNeighbor;// HighQualityBicubic;
                        g.DrawImage(newbmp, 0, 0, b.Width, b.Height);
                    }
                    b.Save(Path.Combine("Images", "Terrains_01.png"), ImageFormat.Png);
                }

                if (CustomAnimTerrainList.Count > 0)
                {
                    //Now animated terrains
                    newbmp = new Bitmap(336, (int)Math.Ceiling((double)CustomAnimTerrainList.Count / 3d) * 36);
                    var dn = 0;
                    foreach (var sn in CustomAnimTerrainList)
                    {
                        for (var f = 0; f < 4; f++)
                        {
                            CopyBitmapArea(newbmp, oldbmp, ((sn + f) % 10) * 28, ((sn + f) / 10) * 36, ((dn * 4 + f) % 12) * 28, (dn / 3) * 36, 28, 36, true);
                        }
                        dn++;
                    }

                    //Resize terrains from 28x36 to 48x48
                    var b = new Bitmap(576, (int)Math.Ceiling((double)CustomAnimTerrainList.Count / 3d) * 48);
                    using (var g = Graphics.FromImage((Image)b))
                    {
                        g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.NearestNeighbor;
                        g.DrawImage(newbmp, 0, 0, b.Width, b.Height);
                    }
                    b.Save(Path.Combine("Images", "TerrainsAnim_01.png"), ImageFormat.Png);
                }
               

                if (CustomNPC1x1List.Count > 0)
                {
                    //Now NPCs 1x1
                    newbmp = new Bitmap(560, (int)Math.Ceiling((double)CustomNPC1x1List.Count / 5d) * 36);
                    var dn = 0;
                    foreach (var sn in CustomNPC1x1List)
                    {
                        for (var f = 0; f < 4; f++)
                        {
                            CopyBitmapArea(newbmp, oldbmp, ((sn + f) % 10) * 28, ((sn + f) / 10) * 36, 
                                (f * 28) + (dn % 5) * 28 * 4, (dn / 5) * 36, 28, 36, false);
                        }
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "Npcs1x1_01.png"), ImageFormat.Png);
                }

                if (CustomNPC2x1List.Count > 0)
                {
                    //Now NPCs 2x1
                    newbmp = new Bitmap(224, CustomNPC2x1List.Count * 36);
                    var dn = 0;
                    foreach (var sn in CustomNPC2x1List)
                    {
                        for (var f = 0; f < 8; f++)
                        {
                            CopyBitmapArea(newbmp, oldbmp, ((sn + f) % 10) * 28, ((sn + f) / 10) * 36, 
                                f * 28, dn * 36, 28, 36, false);
                        }
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "Npcs2x1_01.png"), ImageFormat.Png);
                }

                if (CustomNPC1x2List.Count > 0)
                {
                    //Now NPCs 1x2
                    newbmp = new Bitmap(112, CustomNPC1x2List.Count * 36 * 2);
                    var dn = 0;
                    foreach (var sn in CustomNPC1x2List)
                    {
                        for (var f = 0; f < 8; f++)
                        {
                            CopyBitmapArea(newbmp, oldbmp, ((sn + f) % 10) * 28, ((sn + f) / 10) * 36,
                                (f / 2) * 28, (f % 2) * 36 + (dn * 36) * 2, 28, 36, false);
                        }
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "Npcs1x2_01.png"), ImageFormat.Png);
                }

                if (CustomNPC2x2List.Count > 0)
                {
                    //Now NPCs 2x2
                    newbmp = new Bitmap(224, CustomNPC2x2List.Count * 36 * 2);
                    var dn = 0;
                    foreach (var sn in CustomNPC2x2List)
                    {
                        for (var f = 0; f < 16; f++)
                        {
                            CopyBitmapArea(newbmp, oldbmp, ((sn + f) % 10) * 28, ((sn + f) / 10) * 36,
                                ((f % 2) * 28) + ((f / 4) * (28 * 2)),
                                ((f % 4) / 2) * 36 + ((dn * 36) * 2),
                                28, 36, false);
                        }
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "Npcs2x2_01.png"), ImageFormat.Png);
                }

                if (CustomItemList.Count > 0)
                {
                    newbmp = new Bitmap(280, (int)Math.Ceiling((double)CustomItemList.Count / 10d) * 36);
                    var dn = 0;
                    foreach (var sn in CustomItemList)
                    {
                        CopyBitmapArea(newbmp, oldbmp, (sn % 10) * 28, (sn / 10) * 36, (dn % 10) * 28, (dn / 10) * 36, 28, 36, false);
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "Items_01.png"), ImageFormat.Png);
                }

                if (CustomDialogPicList.Count > 0)
                {
                    newbmp = new Bitmap(360, (int)Math.Ceiling((double)CustomDialogPicList.Count / 10d) * 36);
                    var dn = 0;
                    foreach (var sn in CustomDialogPicList)
                    {
                        CopyBitmapArea(newbmp, oldbmp, (sn % 10) * 28, (sn / 10) * 36, (dn % 10) * 36, (dn / 10) * 36, 18, 36, true);
                        CopyBitmapArea(newbmp, oldbmp, ((sn+1) % 10) * 28, ((sn+1) / 10) * 36, (dn % 10) * 36 + 18, (dn / 10) * 36, 18, 36, true);
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "DialogPics_01.png"), ImageFormat.Png);
                }

                if (CustomFacePicList.Count > 0)
                {
                    newbmp = new Bitmap(320, (int)Math.Ceiling((double)CustomFacePicList.Count / 10d) * 32);
                    var dn = 0;
                    foreach (var sn in CustomFacePicList)
                    {
                        CopyBitmapArea(newbmp, oldbmp, (sn % 10) * 28, (sn / 10) * 36, (dn % 10) * 32, (dn / 10) * 32, 16, 32, true);
                        CopyBitmapArea(newbmp, oldbmp, ((sn + 1) % 10) * 28, ((sn + 1) / 10) * 36, (dn % 10) * 32 + 16, (dn / 10) * 32, 16, 32, true);
                        dn++;
                    }
                    newbmp.Save(Path.Combine("Images", "TalkPortraits_01.png"), ImageFormat.Png);
                }
            }
        }

#if DEBUG
        private static void SaveStartupMap()
        {
            using (var fs = new FileStream(@"..\..\Base\Data\Startupmap.dat", FileMode.Create, FileAccess.Write))
            using (var Out = new BinaryWriter(fs))
            {
                Out.Write((short)256);
                for (var x = 0; x < 256; x++)
                {
                    Out.Write(Scenario.ter_types[x].picture);
                }

                Out.Write((short)16);
                for (var x = 0; x < 15; x++)
                    Out.Write((short)(x + 260)); //Picture
                Out.Write((short)414);

                Out.Write(Scenario.out_width * 48);
                Out.Write(Scenario.out_height * 48);

                for(var y = 0; y < Scenario.out_height * 48; y++)
                    for (var x = 0; x < Scenario.out_width * 48; x++)
                    {
                        var sx = x / 48;
                        var sy = y / 48;
                        var lx = x % 48;
                        var ly = y % 48;
                        Out.Write(NewOutsideTerrain[sx, sy][lx * 48 + ly]);
                    }
            }
        }
#endif

        private static int GetTownSize(int townnum)
        {
            switch (Scenario.town_size[townnum])
            {
                case 0: return 64;
                case 1: return 48;
                default: return 32;
            }
        }

        private static int UpdateCustomList(List<int> list, int index)
        {
            if (!list.Contains(index))
                list.Add(index);

            if (list == CustomAnimTerrainList)
                return list.IndexOf(index) + 1024 + 65536;
            else
                return list.IndexOf(index) + 1024;
        }

        private static bool IsUsedEncounter(out_wandering_type o)
        {
            for (var n = 0; n < 7; n++)
                if (o.monst[n] != 0) return true;
            return false;
        }

        private static void SaveNPCGroupRecord(int x, int y, int num, out_wandering_type o, short foldernum, BinaryWriter Out)
        {
            //Don't write anything if this group is empty (has no hostile NPCs in it)
            if (!IsUsedEncounter(o)) return;

            short[] low = { 15, 7, 4, 3, 2, 1, 1, 7, 2, 1 };
            short[] high = { 30, 10, 6, 5, 3, 2, 1, 10, 4, 1 };

            Out.Write((byte)1); //Write 1 to indicate a group follows

            Out.Write(String.Format("Group_{0}_{1}_{2}", x, y, num)); //Write ID for this group
            Out.Write("\t" + foldernum); //Folder ID

            for (var n = 0; n < 7; n++)
            {
                if (o.monst[n] == 0) continue; //No NPCs in this slot
                Out.Write(true); //Write true to indicate an npc component follows
                Out.Write((short)o.monst[n]); //Write monster record no
                Out.Write((short)1); //Write eAttitude (Hostile)
                Out.Write(low[n]); //Write minimum number;
                Out.Write(high[n]); //Write maximum number;
            }
            for (var n = 0; n < 3; n++)
            {
                if (o.friendly[n] == 0) continue; //No NPCs in this slot
                Out.Write(true); //Write true to indicate an npc component follows
                Out.Write((short)o.friendly[n]); //Write monster record no
                Out.Write((short)2); //Write eAttitude (Friendly)
                Out.Write(low[n+7]); //Write minimum number;
                Out.Write(high[n+7]); //Write maximum number;
            }
            Out.Write(false); //Write false to indicate that's it for the NPC components in the group
            Out.Write(o.cant_flee % 10 == 1 ? true : false); //Can't flee
            Out.Write(o.cant_flee > 10 ? true : false);  //Forced
            Out.Write(String.Format("{0}_{1}", o.end_spec1, o.end_spec2)); //Variable to eliminate encounter
            Out.Write(GetNodeToFuncName(o.spec_on_meet, 2, x, y)); 
            Out.Write(GetNodeToFuncName(o.spec_on_flee, 2, x, y)); 
            Out.Write(GetNodeToFuncName(o.spec_on_win, 2, x, y));  
        }

        private static int GetMonsterPicNum(int num)
        {
            int[] pic_index = {
                        1,2,3,4,5,6,7,8,9,10, //0 - 9
                        11,12,13,14,15,16,17,18,19,20, //10 - 19
                        21,22,23,24,25, 26,27,28,29,30,  //20 - 29
                        31,32,33,34,35, 36,37,38,39,40,  //30 - 39
                                  //44             49
                        41,42,43,44,46,47,48,49,50,/*100*/0, //40 - 49
                                     //53
                        /*100*/1,/*100*/2,/*100*/3,51,52,53,54,55,56,57, //50 - 59
                        58,59,60,61,62, 63,64, 65,66,67, //60 - 69
                        //    72    //74          77
                        68,69,70,/*200*/1,71, 72,/*100*/4,73,74,75, //70 - 79
                        76,77,78,79,80, 81,82,83,84,85, //80-89
                        86,87,88,89,90, 91,92,93,94,95, //90-99
                        //  101             105  
                        96, /*200*/0,97,98,99,  /*200*/2,100,101,102,103, //100-109
                        //                 114
                        /*200*/3,104,/*100*/5,/*100*/6,105, 106,107,108,/*300*/0,109, //110-119

                        //  121  
                        110,/*200*/4,111,112,113,114,115,116,117,118, //120-129
                        119,120,121,122,123,124,125,126,/*300*/1,127, //130 -139
                        /*300*/2,/*200*/5,/*200*/6,/*100*/7,128,129,130,131,132,133, //140
                        134,135,136,137,138,139,140,141,142,143, //150

                        144,145,146,147,148,149,150,151,152,153, //160
                        154,155,156,0,0,0,0,0,0,0, //170

                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0};

            if (num < 1000)
                return pic_index[num];
            else
            {
                //Uses custom graphic. Write index in custom sheet as a +10,000 value
                if (num >= 4000)
                    return UpdateCustomList(CustomNPC2x2List, num - 4000);
                else if (num >= 3000)
                    return UpdateCustomList(CustomNPC1x2List, num - 3000);//10000 + (num - 3000);
                else if (num >= 2000)
                    return UpdateCustomList(CustomNPC2x1List, num - 2000);//10000 + (num - 2000);
                else
                    return UpdateCustomList(CustomNPC1x1List, num - 1000);//10000 + (num - 1000);
            }
        }

        private static string[] MageSpellIDs = {"m_poison", "m_ice_bolt", "m_slow_group", "m_magic_map", "m_capture_soul", "m_simulacrum", "m_venom_arrows", "m_wall_of_ice",
                            "m_stealth", "m_major_haste", "m_fire_storm", "m_dispel_barrier", "m_fire_barrier", "m_summoning", "m_shockstorm",
                            "m_spray_fields", "m_major_poison", "m_group_fear", "m_kill", "m_paralyze", "m_daemon", "m_antimagic_cloud",
                            "m_mindduel", "m_flight", "m_shockwave", "m_major_blessing", "m_mass_paralysis", "m_protection", "m_major_summon",
                            "m_force_barrier", "m_quickfire", "m_death_arrows"};

        private static string[] PriestSpellIDs = {"p_cure_all_poison", "p_curse_all", "p_dispel_undead",
                            "p_remove_curse", "p_sticks_to_snakes", "p_martyrs_shield", "p_cleanse", "p_firewalk", "p_bless_party",
                            "p_major_heal", "p_raise_dead", "p_flamestrike", "p_mass_sanctuary", "p_summon_host", "p_shatter",
                            "p_dispel_fields", "p_heal_all", "p_revive", "p_hyperactivity", "p_destone", "p_summon_guardian",
                            "p_mass_charm", "p_protective_circle", "p_pestilence", "p_revive_all", "p_ravage_spirit", "p_resurrect",
                            "p_divine_thud", "p_avatar", "p_wall_of_blades", "p_word_of_recall", "p_major_cleansing"};

        private static string[] AlchemyIndex = 
        {
            "weak_curing", "weak_healing", "weak_poison", "weak_speed", "medium_poison",
            "medium_healing_potion", "strong_curing_potion", "medium_speed", "graymold_salve", "weak_energy_potion",
            "potion_of_clarity", "strong_poison", "strong_healing_potion", "killer_poison", "resurrection_balm",
            "medium_energy_potion", "knowledge_brew", "strength_potion", "bliss_potion", "strong_energy_potion"
        };

        [Flags]
        public enum eTriggerSpot
        {
            STEP_ON = 1,       //-------1 //Triggered by step on in non-combat mode (town or outdoors)
            SEARCH = 2,       //------1- //PC triggers by Searching
            USE = 4,       //-----1-- //PC triggers by Using
            STOOD_ON = 8,      //----1--- //Triggered at the end of every turn character is stood there. TO DO
            PCS_TRIGGER = 16,  //---1---- //Set if this is triggered by PCs (The PC triggering is set in the PC script parameter passed to the function)
            NPCS_TRIGGER = 32, //--1----- //Set if this is triggered by NPCs (The NPC triggering is set in the NPC script parameter passed to the function)
            CAST_SPELL = 64,   //-1------ //Triggered by a spell being cast on the spot
            STEP_ON_CMBT = 128,//1------- //Triggered by step on in combat mode
        }

        private static bool ValidStuffDone(int x, int y)
        {
            return x >= 0 && x < 300 && y >= 0 && y < 10;
        }

        private static void SaveLocation(location l, BinaryWriter Out)
        {
            Out.Write((short)l.x);
            Out.Write((short)l.y);
        }

        private static void SaveRECT16(RECT16 r, BinaryWriter Out)
        {
            if (MacFormat)
            {
                Out.Write(r.top);
                Out.Write(r.left);
                Out.Write(r.bottom);
                Out.Write(r.right);
            }
            else
            {
                Out.Write(r.left);
                Out.Write(r.top);
                Out.Write(r.right);
                Out.Write(r.bottom);
            }
        }

        private static bool LoadScenario() {

            using (var fs = new FileStream(Filename, FileMode.Open, FileAccess.Read))
            using (var In = new BinaryReader(fs)) {

                MarshallyFunkyRead(ref Scenario, In);

                switch (Scenario.CheckFlags()) {
                    case 0:
                        Console.WriteLine("This is a Windows formatted scenario."); 
                        break;
                    case 1:
                        Console.WriteLine("This is a Mac formatted scenario");
                        MacFormat = true;
                        
                        break;
                    default:
                        Console.WriteLine("Not a recognised scenario file."); return false;
                }

                Port(ref Scenario);
                MarshallyFunkyRead(ref ScenItems, In);
                Port(ref ScenItems);

                DataStore5.scen_strs = new string[160];
                scen_strs_2 = new string[270 - 160];

                for (var i = 0; i < 270; i++) {
                    int len = Scenario.scen_str_len[i];

                    if (i < 160) {
                        DataStore5.scen_strs[i] = Encoding.ASCII.GetString(In.ReadBytes(len)).TrimEnd();
                    } else {
                        scen_strs_2[i - 160] = Encoding.ASCII.GetString(In.ReadBytes(len)).TrimEnd();
                    }
                }

                //Are there any variable town entry things?
                for (var y = 0; y < 10; y++)
                    if (Scenario.town_to_add_to[y] != -1)
                    {
                        HasTownPreEntryFunc = true; break;
                    }

                Console.WriteLine("Converting terrain maps...");

                //Convert all the terrain to NEW terrain (with ushorts not bytes)
                for (var x = 0; x < Scenario.num_towns; x++)
                {
                    LoadTown(x);
                    Console.WriteLine("  Town " + x + ": " + DataStore1.town_strs[0]);
                    var sz = Scenario.town_size[x] == 0 ? 64 : (Scenario.town_size[x] == 1 ? 48 : 32);
                    NewTownTerrain.Add(new ushort[sz * sz]);
                    ConvertTerrain(NewTownTerrain[x], true, sz);
                }


                NewOutsideTerrain = new ushort[Scenario.out_width, Scenario.out_height][];
                for (var x = 0; x < Scenario.out_width; x++)
                    for (var y = 0; y < Scenario.out_height; y++)
                    {                       
                        NewOutsideTerrain[x, y] = new ushort[48 * 48];
                        LoadOutdoors(x, y);
                        Console.WriteLine("  Outside " + x + ", " + y + ": " + DataStore4.outdoor_text[0]);
                        ConvertTerrain(NewOutsideTerrain[x,y], false, 48, x, y);
                    }
            }
            MakeShops();
            return true;
        }

        private static void ConvertTerrain(ushort[] ter, bool is_town, int sz, int secx = 0, int secy = 0)
        {
            var pos = 0;
            for(var x = 0; x < sz; x++)
                for (var y = 0; y < sz; y++)
                {
                    ter[pos] = is_town ? TownTerrain.terrain[pos] : Outdoors.terrain[pos];

                    int to_n, to_s, to_e, to_w;

                    if (is_town)
                    {
                        to_n = y == 0 ? -1 : TownTerrain.terrain[x * sz + (y-1)];
                        to_s = y == sz-1 ? -1 : TownTerrain.terrain[x * sz + (y+1)];
                        to_e = x == sz-1 ? -1 : TownTerrain.terrain[(x+1) * sz + y];
                        to_w = x == 0 ? -1 : TownTerrain.terrain[(x - 1) * sz + y];
                    }
                    else
                    {
                        if (y == 0)
                            if (secy == 0) to_n = -1;
                            else
                            {
                                LoadOutdoors(secx, secy - 1);
                                to_n = Outdoors.terrain[x * 48 + 47];
                                LoadOutdoors(secx, secy);
                            }
                        else to_n = Outdoors.terrain[x * 48 + (y - 1)];

                        if (y == 47)
                            if (secy == Scenario.out_height-1) to_s = -1;
                            else
                            {
                                LoadOutdoors(secx, secy + 1);
                                to_s = Outdoors.terrain[x * 48 + 0];
                                LoadOutdoors(secx, secy);
                            }
                        else to_s = Outdoors.terrain[x * 48 + (y + 1)];

                        if (x == 47)
                            if (secx == Scenario.out_width - 1) to_e = -1;
                            else
                            {
                                LoadOutdoors(secx + 1, secy);
                                to_e = Outdoors.terrain[0 * 48 + y];
                                LoadOutdoors(secx, secy);
                            }
                        else to_e = Outdoors.terrain[(x+1) * 48 + y];

                        if (x == 0)
                            if (secx == 0) to_w = -1;
                            else
                            {
                                LoadOutdoors(secx - 1, secy);
                                to_w = Outdoors.terrain[47 * 48 + y];
                                LoadOutdoors(secx, secy);
                            }
                        else to_w = Outdoors.terrain[(x-1) * 48 + y];
                    }

                    const int CAVE_WALKWAY = 82;
                    const int GRASS_WALKWAY = 83;
                    const int CAVE_ROAD = 79,
                              GRASS_ROAD = 80,
                              HILLS_ROAD = 81;

                    bool roadon = false, spec_dot_on = false;
                    int Num = ter[pos];

                    switch (ter[pos])
                    {
                        case CAVE_WALKWAY:
                            ter[pos] = 0;
                            if (is_nature(to_w) && is_nature(to_s)) ter[pos] |= (ushort)(17 << 8);//246; //SW walkway cave corner
                            else if (is_nature(to_e) && is_nature(to_s)) ter[pos] |= (ushort)(20 << 8);//81; //SE Walkway cave corner
                            else if (is_nature(to_e) && is_nature(to_n)) ter[pos] |= (ushort)(19 << 8);//80; //NE Walkway cave corner
                            else if (is_nature(to_w) && is_nature(to_n)) ter[pos] |= (ushort)(18 << 8);//79; //NW Walkway cave corner
                            else ter[pos] |= (ushort)(21 << 8);
                                break;
                        case GRASS_WALKWAY:
                            ter[pos] = 2;
                            if (is_nature(to_w) && is_nature(to_s)) ter[pos] |= (ushort)(17 << 8);//246; //SW walkway cave corner
                            else if (is_nature(to_e) && is_nature(to_s)) ter[pos] |= (ushort)(20 << 8);//81; //SE Walkway cave corner
                            else if (is_nature(to_e) && is_nature(to_n)) ter[pos] |= (ushort)(19 << 8);//80; //NE Walkway cave corner
                            else if (is_nature(to_w) && is_nature(to_n)) ter[pos] |= (ushort)(18 << 8);//79; //NW Walkway cave corner
                            else ter[pos] |= (ushort)(21 << 8);

                            break;
                        case HILLS_ROAD:
                            if (to_n == GRASS_ROAD || to_n == CAVE_ROAD) ter[pos] = 42;       //Road on - Grass N / Hills S
                            else if (to_s == GRASS_ROAD || to_s == CAVE_ROAD) ter[pos] = 38;  //          Grass S / Hills N
                            else if (to_w == GRASS_ROAD || to_w == CAVE_ROAD) ter[pos] = 44;  //          Grass W / Hills E
                            else if (to_e == GRASS_ROAD || to_e == CAVE_ROAD) ter[pos] = 40;  //          Grass E / Hills W
                            else ter[pos] = 36;
                            roadon = true;
                            break;
                        case CAVE_ROAD:
                            ter[pos] = 0;
                            roadon = true;
                            break;
                        case GRASS_ROAD:
                            ter[pos] = 2;
                            roadon = true;
                            break;

                        default:
                            if (Scenario.ter_types[ter[pos]].picture >= 207 && Scenario.ter_types[ter[pos]].picture <= 212)
                            {
                                spec_dot_on = true;
                                ushort[] tbl = { 0, 170, 210, 217, 2, 36 };
                                ter[pos] = tbl[Scenario.ter_types[ter[pos]].picture - 207];
                            }
                        break;
                    }

                    if (roadon)
                    {
                        ushort road = 0;
                        if (extend_road_terrain(to_n)) road += 1;
                        if (extend_road_terrain(to_e)) road += 2;
                        if (extend_road_terrain(to_s)) road += 4;
                        if (extend_road_terrain(to_w)) road += 8;
                        ter[pos] |= (ushort)(road << 8);
                    }
                    if (spec_dot_on) ter[pos] |= (16 << 8);
                    pos++;
                }

            //Terrain is now stored in two bytes, not one. The lower byte contains the terrain types as before (mostly)
            //The upper byte contains the number of the 'overlay' terrain types (Just road and special dot at the moment), or if 0, nothing 

            //Old terrain changes:
            //  79-81 are no longer roads & 246-250 no longer special dots, but the various walkway corners
            //  (Each corner on both grass and cave floor has its own tile type instead of being calculated in-game)
            //
            //New terrains:
            //  New terrains start at 256 and are a top layer above the underlay with transparency
            //  256 - 271: the various road permutations
            //  272: Special node dot
        }

        private static bool is_nature(int n)
        {
            if (n == -1) 
                return false;
            int picture = Scenario.ter_types[n].picture;
            if (picture >= 0 && picture <= 45) return true;
            if (picture >= 67 && picture <= 73) return true;
            if (picture >= 75 && picture <= 87) return true;
            if (picture >= 121 && picture <= 122) return true;
            if (picture >= 179 && picture <= 208) return true;
            if (picture >= 211 && picture <= 212) return true;
            if (picture >= 217 && picture <= 246) return true;
            return false;
        }

        private static bool extend_road_terrain(int n) 
        {
            if (n == -1) return true;
            int picture = Scenario.ter_types[n].picture;
            short[] extend_pics = {61,62,63,64,65, 66,401,402,406,202,
							    203,204,215,216,90, 91,92,93,102,103,
							    104,105,112,113,114, 115,187,188,189,190,
							    192,193,194,195,196, 197,191,200,201};
            for (var i = 0; i < 39; i++)
                if (picture == extend_pics[i]) return true;
            return false;
        }

        private static bool LoadTown(int which_town)
        {

            if (which_town == CurrentlyLoadedTown) return true;
            CurrentlyLoadedTown = which_town;

            long len_to_jump = scenario_data_type.SIZE;
            len_to_jump += scen_item_data_type.SIZE;
            int i,j;

            for (i = 0; i < 300; i++) len_to_jump += Scenario.scen_str_len[i];
            long store = 0;
            for (i = 0; i < 100; i++)
                for (j = 0; j < 2; j++)
                    store += Scenario.out_data_size[i * 2 + j];
            for (i = 0; i < which_town; i++)
                for (j = 0; j < 5; j++)
                    store += (Scenario.town_data_size[i * 5 + j]);
            len_to_jump += store;

            using (var fs = new FileStream(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, Filename), FileMode.Open, FileAccess.Read))
            using (var In = new BinaryReader(fs)) {

                fs.Seek(len_to_jump, SeekOrigin.Begin);
                MarshallyFunkyRead(ref Town, In);
                Port(ref Town);

                switch (Scenario.town_size[which_town])
                {
                    case 0:
                        MarshallyFunkyRead(ref TownTerrain, In);
                        break;
                    case 1:
                        var ave_t =new ave_tr_type();
                        MarshallyFunkyRead(ref ave_t, In);
                        TownTerrain.terrain = ave_t.terrain;
                        TownTerrain.lighting = ave_t.lighting;
                        TownTerrain.room_rect = ave_t.room_rect;
                        TownTerrain.creatures = ave_t.creatures;
                        break;
                    case 2:
                        var tiny_t = new tiny_tr_type();
                        MarshallyFunkyRead(ref tiny_t, In);
                        TownTerrain.terrain = tiny_t.terrain;
                        TownTerrain.lighting = tiny_t.lighting;
                        TownTerrain.room_rect = tiny_t.room_rect;
                        TownTerrain.creatures = tiny_t.creatures;
                        break;
                }

                Port(ref TownTerrain);

                //Load town strings
                DataStore1.town_strs = new string[140];
                for (i = 0; i < 140; i++)
                {
                    int len = Town.strlens[i];
                    DataStore1.town_strs[i] = Encoding.ASCII.GetString(In.ReadBytes(len)).TrimEnd();

                }

                //Load talking
                MarshallyFunkyRead(ref Talking, In);
                Port(ref Talking);

                DataStore3.talk_strs = new string[170];
                for (i = 0; i < 170; i++)
                {
                    int len = Talking.strlens[i];
                    DataStore3.talk_strs[i] = Encoding.ASCII.GetString(In.ReadBytes(len)).TrimEnd();
                }

            }

            
            return true;


        }

        private static bool LoadOutdoors(int x, int y) {

            if (CurrentlyLoadedOutX == x && CurrentlyLoadedOutY == y) return true;
            CurrentlyLoadedOutX = x;
            CurrentlyLoadedOutY = y;

            var out_sec_num = Scenario.out_width * y + x;
            int i, j;

            var len_to_jump = scenario_data_type.SIZE;
            len_to_jump += scen_item_data_type.SIZE;
            for (i = 0; i < 300; i++)
                len_to_jump += Scenario.scen_str_len[i];
            var store = 0;
            for (i = 0; i < out_sec_num; i++)
                for (j = 0; j < 2; j++)
                    store += Scenario.out_data_size[i * 2 + j];
            len_to_jump += store;

            using (var fs = new FileStream(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, Filename), FileMode.Open, FileAccess.Read))
            using (var In = new BinaryReader(fs)) {

                fs.Seek(len_to_jump, SeekOrigin.Begin);
                MarshallyFunkyRead(ref Outdoors, In);

                if (x == 2 && y == 0)
                {
                }

                Port(ref Outdoors);

                DataStore4.outdoor_text = new string[120];
                for (i = 0; i < 120; i++) {
                    int len = Outdoors.strlens[i];
                    DataStore4.outdoor_text[i] = Encoding.ASCII.GetString(In.ReadBytes(len)).TrimEnd();
                }	
            }
            return true;

        }

        private static List<ItemShop> ItemShops = new List<ItemShop>();

        private class ItemShop
        {
            public string ID;
            public string Name;
            public bool Outdoors;
            public int TownNo; //If not outdoors
            public int OutdoorsX, OutdoorsY; //If outdoors
            public int NodeNo; //Talking node if a town, outdoor sector special node if outdoors.

            public uint BuysOffPlayer=0; //What the player can sell to the shop
            public List<int> OtherBuyOffNodes = new List<int>();
            public bool SellsStuff;

            public int CostLevel;
            public int FirstItem;
            public int NumItems;

            public int Type; //0: Items, 1: Spells, 2: Alchemy
            public bool SpecificallyPriest = false; //Only relevant if Type is magic spells - just to distinguish mage and priest spells when generating the restock scripts

            public bool JumbleShop;
            public int JumbleShopNo;
        }

        private static void MakeShops()
        {

            Console.WriteLine("Making shops...");

            //First do all the outdoor shops. These are triggered by an outside  special node
            for(var x = 0; x < Scenario.out_width; x++)
                for (var y = 0; y < Scenario.out_height; y++)
                {
                    LoadOutdoors(x, y);

                    for (var n = 0; n < Outdoors.specials.Length; n++)
                    {
                        if (Outdoors.specials[n].type == 229 && Outdoors.specials[n].ex1b < 4) //Outdoor store
                        {
                            var shop = new ItemShop();
                            shop.Type = Outdoors.specials[n].ex1b == 0 ? 0 : (Outdoors.specials[n].ex1b == 3 ? 2 : 1);
                            if (Outdoors.specials[n].ex1b == 2) shop.SpecificallyPriest = true;
                            shop.Outdoors = true;
                            shop.OutdoorsX = x;
                            shop.OutdoorsY = y;
                            shop.NodeNo = n;
                            shop.Name = FixYeah(GetString(Outdoors.specials[n].m1, 2, true), false);
                            string[] s = { "Items", "Mage", "Priest", "Alchemy" };
                            shop.ID = string.Format("Shop_{3}_Outside_{0}_{1}_{2}", n, x, y, s[Outdoors.specials[n].ex1b]);
                            shop.SellsStuff = true;
                            shop.CostLevel = Outdoors.specials[n].ex2b;
                            shop.FirstItem = Outdoors.specials[n].ex1a;
                            shop.NumItems = Outdoors.specials[n].ex2a;
                            ItemShops.Add(shop);
                        }
                    }
                }

            //Now do all the town item shops. There are triggered by a talking node
            for (var n = 0; n < Scenario.num_towns; n++)
            {
                LoadTown(n);

                //Make a quick list of all the personalities in the town and what they will sell: Weapons, Armour, All
                var psell = new Dictionary<int, Tuple<bool, bool, bool, int, bool>>();
                for (var x = 0; x < 60; x++) //Go through all talking nodes
                {
                    if (Talking.talk_nodes[x].personality >= 0)
                    {
                        if (!psell.ContainsKey(Talking.talk_nodes[x].personality)) //Add to list if it doesn't contain this personality
                            psell.Add(Talking.talk_nodes[x].personality, new Tuple<bool, bool, bool, int, bool>(false, false, false,-1, false));

                        var ps = psell[Talking.talk_nodes[x].personality];

                        if (Talking.talk_nodes[x].type == 13) //Sell weapons
                            ps = psell[Talking.talk_nodes[x].personality] = new Tuple<bool, bool, bool, int, bool>(true, ps.Item2, ps.Item3, ps.Item4, ps.Item5);

                        if (Talking.talk_nodes[x].type == 14) //Sell Armour
                            ps = psell[Talking.talk_nodes[x].personality] = new Tuple<bool, bool, bool, int, bool>(ps.Item1, true, ps.Item3, ps.Item4, ps.Item5);

                        if (Talking.talk_nodes[x].type == 15) //Sell All
                            ps = psell[Talking.talk_nodes[x].personality] = new Tuple<bool, bool, bool, int, bool>(ps.Item1, ps.Item2, true, ps.Item4, ps.Item5);

                        if (Talking.talk_nodes[x].type == 7)
                            psell[Talking.talk_nodes[x].personality] = new Tuple<bool, bool, bool, int, bool>(ps.Item1, ps.Item2, ps.Item3, x, ps.Item5);

                         if (Talking.talk_nodes[x].type == 23)
                             psell[Talking.talk_nodes[x].personality] = new Tuple<bool, bool, bool, int, bool>(ps.Item1, ps.Item2, ps.Item3, ps.Item4, true);
                    }
                }

                for (var x = 0; x < 60; x++) //Now go through all talking nodes and get the shops
                {
                    var t = Talking.talk_nodes[x];

                    if (t.personality == -1) continue;

                    if (t.type == 7 || t.type == 23 || t.type == 13 || t.type == 14 || t.type == 15) //7 is Buy items - 23 is Jumble shop
                    {
                        //Don't yet consider a shop that buys off the player but whose personality also has a shop that sells to the player.
                        if ((t.type == 13 || t.type == 14 || t.type == 15) && psell[t.personality].Item4 != -1 /*&& !psell[t.personality].Item5*/) continue;

                        var sellall = psell[t.personality].Item3;
                        var sellweapons = psell[t.personality].Item1;
                        var sellarmour = psell[t.personality].Item2;

                        

                        var shop = new ItemShop(); 
                        shop.Outdoors = false;
                        shop.TownNo = n;
                        shop.NodeNo = x;
                        shop.ID = string.Format("Shop_Items_{0}_{1}", n, x);
                        shop.Name = DataStore3.talk_strs[x * 2 + 40];

                        /*          None = 0, OneHanded = 1, TwoHanded = 2, Gold = 3, Bow = 4, Arrows = 5, Thrown=6, Potion=7, Scroll=8,
                                    Wand = 9, Tool = 10, Food = 11, Shield = 12, Armour=13, Helm = 14, Gloves=15, Shield2=16, Boots=17, Ring=18,
                                    Necklace = 19, Poison=20, NonUse=21, Trousers=22, Crossbow = 23, Bolts = 24, RangedNoAmmo=25, Unused1=26, Unused2=27
                          */
                        if (sellall) shop.BuysOffPlayer = uint.MaxValue;
                        else
                        {                                                      //   27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0
                            if (sellweapons) shop.BuysOffPlayer += 0x03800056; //   0  0  1  1  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  1  0  1  1  0
                            if (sellarmour) shop.BuysOffPlayer +=  0x0043F000; //   0  0  0  0  0  1  0  0  0  0  1  1  1  1  1  1  0  0  0  0  0  0  0  0  0  0  0  0
                        }

                        if (t.type == 7) //Buy items
                        {
                            shop.JumbleShop = false;
                            shop.SellsStuff = true;
                            shop.CostLevel = t.extras[0];
                            shop.FirstItem = t.extras[1];
                            shop.NumItems = t.extras[2];
                        }
                        else if (t.type == 23)
                        {

                            shop.JumbleShop = true;
                            shop.SellsStuff = true;
                            shop.CostLevel = t.extras[0];
                            shop.JumbleShopNo = t.extras[1];
                        }
                        else if (t.type == 13 || t.type == 14 || t.type == 15)
                        {
                            shop.JumbleShop = false;
                            shop.SellsStuff = false;
                        }
                        ItemShops.Add(shop);
                    }
                    else if (t.type >= 9 && t.type <= 11) //Mage spells, priest spells, recipes
                    {
                        var shop = new ItemShop();
                        shop.Type = t.type == 11 ? 2 : 1;
                        if (t.type == 10) shop.SpecificallyPriest = true;
                        shop.Outdoors = false;
                        shop.TownNo = n;
                        shop.NodeNo = x;
                        string[] s = { "Mage", "Priest", "Alchemy" };
                        shop.ID = string.Format("Shop_{2}_{0}_{1}", n, x, s[t.type-9]);
                        shop.Name = DataStore3.talk_strs[x * 2 + 40];
                        shop.SellsStuff = true;
                        shop.CostLevel = t.extras[0];
                        shop.FirstItem = t.extras[1];
                        shop.NumItems = t.extras[2];
                        ItemShops.Add(shop);
                    }
                }

                //NOW - go through the nodes again and look for nodes that buy stuff off the player. If the personality with that node also has an item shop that sells to the player, link to that shop instead.
                for (var x = 0; x < 60; x++)
                {
                    var t = Talking.talk_nodes[x];
                    if (t.personality == -1) continue;

                    if (t.type == 13 || t.type == 14 || t.type == 15)
                    {
                        if (psell[t.personality].Item4 != -1) //This personality that buys stuff off the player, also sells stuff to the player (in at least one other talking node) so link to that shop
                        {
                            var shop = ItemShops.Find(s => s.Type == 0 && !s.Outdoors && s.TownNo == n && s.NodeNo == psell[t.personality].Item4 && !s.JumbleShop);
                            if (shop != null)
                            {
                                shop.OtherBuyOffNodes.Add(x);
                            }
                        }
                    }
                }


            }

        }

        private static void FixBoatSpecialNodes(ref special_node_type[] spcs)
        {
            for(var x = 0; x < spcs.Length; x++)
                if (spcs[x].type == 15 || spcs[x].type ==16) //15 is horses, 16 boats
                {
                    short i=-1;
                    //Extra1a is the horse or boat to change
                    for (var y = 0; y < 30; y++)
                    {
                        if (Scenario.scen_horses[y].which_town != -1)
                        {
                            i++;
                            if (spcs[x].type == 15 && spcs[x].ex1a == y) spcs[x].ex1a = i;
                        }
                    }
                    for (var y = 0; y < 30; y++)
                    {
                        if (Scenario.scen_boats[y].which_town != -1)
                        {
                            i++;
                            if (spcs[x].type == 16 && spcs[x].ex1a == y) spcs[x].ex1a = i;
                        }
                    }
                }
        }

        //Very spiffy generic function that will automatically load in any of our legacy structures, provided we've put its data size in a 'SIZE' field
        private static void MarshallyFunkyRead<T>(ref T o, BinaryReader In)
        {
            var f = o.GetType().GetField("SIZE");
            if (f == null || f.FieldType != typeof(int)) throw new Exception("Object must have a 'SIZE' field wot is an integer!");

            var size = (int) f.GetValue(o);

            var packet = In.ReadBytes(size);
            var pinnedPacket = GCHandle.Alloc(packet, GCHandleType.Pinned);
            o = (T) Marshal.PtrToStructure(
                pinnedPacket.AddrOfPinnedObject(),
                o.GetType());
            pinnedPacket.Free();
        }

        private static void Port<T>(ref T o)
        {
            if (!MacFormat) return;

            var fields = o.GetType().GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);

            foreach (var f in fields)
            {
                if (f.FieldType.IsArray)
                {
                    if (f.FieldType == typeof(short[]))
                    {
                        var arr = (short[])f.GetValue(o);
                        for(var x =0;x<arr.Length;x++)
                        {
                            var b = BitConverter.GetBytes(arr[x]);
                            var c = b[0];
                            b[0] = b[1];
                            b[1] = c;
                            arr[x] = BitConverter.ToInt16(b, 0);
                        }
                        f.SetValue(o, arr);
                    }
                    else
                    {
                        if (f.FieldType == typeof(byte[]) || f.FieldType == typeof(sbyte[]) || f.FieldType == typeof(location[])) continue;

                        var arr = (Array) f.GetValue(o);
                        for(var x = 0; x < arr.Length;x++)
                        {
                            var o2 = arr.GetValue(x);
                            Port(ref o2);
                            arr.SetValue(o2, x);
                        }
                        f.SetValue(o, arr);
                    }

                } else {
                    if (f.FieldType == typeof(short))
                    {
                        var b = BitConverter.GetBytes((short)f.GetValue(o));
                        var c = b[0];
                        b[0] = b[1];
                        b[1] = c;

                        var tr = __makeref(o);
                        f.SetValueDirect(tr, BitConverter.ToInt16(b, 0));
                    }
                    else
                    {
                        if (f.FieldType == typeof(byte) || f.FieldType == typeof(sbyte) || f.FieldType == typeof(location)) continue;

                        var o2 = f.GetValue(o);
                        Port(ref o2);
                        var tr = __makeref(o);
                        f.SetValueDirect(tr, o2);
                    }
                } 
                

            }
        }

    }

}
