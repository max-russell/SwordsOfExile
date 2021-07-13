using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace SoE_Converter
{
    partial class Program
    {
        public enum eNodeFields
        {
            None, SD1, SD2, Msg1, Msg2, Pic, Ex1a, Ex1b, Ex2a, Ex2b, JumpTo, BREAK
        }

        class ScriptInstruction
        {
            public int NodeType;
            public eNodeFields Branch1To, Branch2To;
            public string NodeString;

            //Whether this type of node has the option for a standard 2 paragraph message window to appear, if there are strings set in Msg1 or Msg2
            public bool StandardMsg=false;

            //Whether this node type checks whether Stuff Done flag at SD1,SD2 is 250, and stops the script if not
            public bool StdSDCheck = false; 

            //Whether this node type sets the SD flag straight after the StdSDCheck. Ignored if StdSDCheck not set
            public bool StdSDSet = true;

            //public bool AddedInCBoE = false; //True if this is an extra instruction in CBoE, not in the original BoE editor

            public ScriptInstruction() { }
            public ScriptInstruction(int n, string s, eNodeFields b1 = eNodeFields.None, eNodeFields b2 = eNodeFields.None)
            {
                NodeType = n;
                NodeString = s;
                Branch1To = b1;
                Branch2To = b2;
            }
            public ScriptInstruction(int n, string s, bool msg, eNodeFields b1 = eNodeFields.None, eNodeFields b2 = eNodeFields.None)
            {
                NodeType = n;
                NodeString = s;
                Branch1To = b1;
                Branch2To = b2;
                StandardMsg = msg;
            }

            static public ScriptInstruction Get(special_node_type n)
            {
                foreach(ScriptInstruction i in Instructions)
                    if (i.NodeType == n.type) return i;
                return null;
            }

        }

        static ScriptInstruction[] Instructions = {
            new ScriptInstruction{NodeType = 1, NodeString = "Set Flag", StandardMsg=true},
            new ScriptInstruction{NodeType = 2, NodeString = "Increment Flag", StandardMsg=true},
            new ScriptInstruction{NodeType = 3, NodeString = "Display Message", StandardMsg=true},
            new ScriptInstruction{NodeType = 4, NodeString = "Secret Passage"},
            new ScriptInstruction{NodeType = 5, NodeString = "Display Small Message"},
            new ScriptInstruction{NodeType = 6, NodeString = "Flip Flag", StandardMsg=true},
            new ScriptInstruction{NodeType = 7, NodeString = "Out Block"},
            new ScriptInstruction{NodeType = 8, NodeString = "Town block"},
            new ScriptInstruction{NodeType = 9, NodeString = "Combat block"},
            new ScriptInstruction{NodeType = 10, NodeString = "Looking block"},
            new ScriptInstruction{NodeType = 11, NodeString = "Cant Enter"},
            new ScriptInstruction{NodeType = 12, NodeString = "Change Time", StandardMsg=true},
            new ScriptInstruction{NodeType = 13, NodeString = "Start General Timer", StandardMsg = true},
            new ScriptInstruction{NodeType = 14, NodeString = "Play a sound"},
            new ScriptInstruction{NodeType = 15, NodeString = "Change Horse Possession", StandardMsg=true},
            new ScriptInstruction{NodeType = 16, NodeString = "Change Boat Possession", StandardMsg=true},
            new ScriptInstruction{NodeType = 17, NodeString = "Show/Hide Town", StandardMsg=true},
            new ScriptInstruction{NodeType = 18, NodeString = "Major Event Has Occurred", StandardMsg=true},
            new ScriptInstruction{NodeType = 19, NodeString = "Forced Give", StandardMsg=true},
            new ScriptInstruction{NodeType = 20, NodeString = "Buy Items of Type"}, 
            new ScriptInstruction{NodeType = 21, NodeString = "Call Global Special"},
            new ScriptInstruction{NodeType = 22, NodeString = "Set Many Flags"},
            new ScriptInstruction{NodeType = 23, NodeString = "Copy Flag"},
            new ScriptInstruction{NodeType = 24, NodeString = "Ritual of Sanct. Block", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 25, NodeString = "Have a rest", StandardMsg=true},
            new ScriptInstruction{NodeType = 26, NodeString = "Wandering Will Fight"},
            new ScriptInstruction{NodeType = 27, NodeString = "End Scenario"},

            new ScriptInstruction{NodeType = 50, NodeString = "Give Item", Branch1To = eNodeFields.Ex2b, StandardMsg=true, StdSDCheck = true},                              
            new ScriptInstruction{NodeType = 51, NodeString = "Give Special Item", StandardMsg=true, StdSDCheck = true},
            new ScriptInstruction{NodeType = 52, NodeString = "One-Time Do Nothing", StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 53, NodeString = "One-Time Nothing and Set", StdSDCheck = true},
            new ScriptInstruction{NodeType = 54, NodeString = "One-Time Text Message", StandardMsg=true, StdSDCheck = true},
            new ScriptInstruction{NodeType = 55, NodeString = "Display Dialog (Dialog pic)", Branch1To = eNodeFields.Ex1b, Branch2To = eNodeFields.Ex2b, StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 56, NodeString = "Display Dialog (Terrain pic)", Branch1To = eNodeFields.Ex1b, Branch2To = eNodeFields.Ex2b, StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 57, NodeString = "Display Dialog (Monster pic)", Branch1To = eNodeFields.Ex1b, Branch2To = eNodeFields.Ex2b, StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 58, NodeString = "Give Item (Dialog pic)", Branch1To = eNodeFields.Ex2b, StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 59, NodeString = "Give Item (Terrain pic)", Branch1To = eNodeFields.Ex2b, StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 60, NodeString = "Give Item (Monster pic)", Branch1To = eNodeFields.Ex2b, StdSDCheck = true, StdSDSet = false},
            new ScriptInstruction{NodeType = 61, NodeString = "One-Time Place Outdoor Encounter", StandardMsg=true, StdSDCheck = true},
            new ScriptInstruction{NodeType = 62, NodeString = "One-Time Place Town Encounter ", StandardMsg=true, StdSDCheck = true},
            new ScriptInstruction{NodeType = 63, NodeString = "Trap", StdSDCheck = true, StdSDSet = false},

            new ScriptInstruction{NodeType = 80, NodeString = "Select a PC", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 81, NodeString = "Do Damage", StandardMsg=true},
            new ScriptInstruction{NodeType = 82, NodeString = "Affect Health", StandardMsg=true},
            new ScriptInstruction{NodeType = 83, NodeString = "Affect Spell Points", StandardMsg=true},
            new ScriptInstruction{NodeType = 84, NodeString = "Affect Experience", StandardMsg=true},
            new ScriptInstruction{NodeType = 85, NodeString = "Affect Skill points", StandardMsg=true},
            new ScriptInstruction{NodeType = 86, NodeString = "Kill/Raise", StandardMsg=true},
            new ScriptInstruction{NodeType = 87, NodeString = "Affect Poison", StandardMsg=true},
            new ScriptInstruction{NodeType = 88, NodeString = "Affect Slow/Haste", StandardMsg=true},
            new ScriptInstruction{NodeType = 89, NodeString = "Affect Invulnerability", StandardMsg=true},
            new ScriptInstruction{NodeType = 90, NodeString = "Affect Magic Resistance", StandardMsg=true},
            new ScriptInstruction{NodeType = 91, NodeString = "Affect Webs", StandardMsg=true},
            new ScriptInstruction{NodeType = 92, NodeString = "Affect Disease", StandardMsg=true},
            new ScriptInstruction{NodeType = 93, NodeString = "Affect Sanctuary", StandardMsg=true},
            new ScriptInstruction{NodeType = 94, NodeString = "Affect Curse/Bless", StandardMsg=true},
            new ScriptInstruction{NodeType = 95, NodeString = "Affect Dumbfounding", StandardMsg=true},
            new ScriptInstruction{NodeType = 96, NodeString = "Affect Sleep", StandardMsg=true},
            new ScriptInstruction{NodeType = 97, NodeString = "Affect Paralysis", StandardMsg=true},
            new ScriptInstruction{NodeType = 98, NodeString = "Affect Statistic", StandardMsg=true},
            new ScriptInstruction{NodeType = 99, NodeString = "Give Mage Spell", StandardMsg=true},
            new ScriptInstruction{NodeType = 100, NodeString = "Give Priest Spell", StandardMsg=true},
            new ScriptInstruction{NodeType = 101, NodeString = "Affect Gold", StandardMsg=true},
            new ScriptInstruction{NodeType = 102, NodeString = "Affect Food", StandardMsg=true},
            new ScriptInstruction{NodeType = 103, NodeString = "Give Alchemy", StandardMsg=true},
            new ScriptInstruction{NodeType = 104, NodeString = "Give Stealth", StandardMsg=true},
            new ScriptInstruction{NodeType = 105, NodeString = "Give Firewalk", StandardMsg=true},
            new ScriptInstruction{NodeType = 106, NodeString = "Give Flying", StandardMsg=true},

            new ScriptInstruction{NodeType = 130, NodeString = "Stuff Done Flag?", Branch1To = eNodeFields.Ex1b, Branch2To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 131, NodeString = "Town Number?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 132, NodeString = "Random Number?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 133, NodeString = "Have special item?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 134, NodeString = "Stuff Done Compare?", Branch1To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 135, NodeString = "Terrain this type? (town)", Branch1To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 136, NodeString = "Terrain this type? (outdoors)", Branch1To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 137, NodeString = "Has Gold?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 138, NodeString = "Has food?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 139, NodeString = "Item class on space?", Branch1To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 140, NodeString = "Have item with class?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 141, NodeString = "Equipped item with class?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 142, NodeString = "Has Gold? (and take)", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 143, NodeString = "Has Food? (and take)", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 144, NodeString = "Item Class on space? (and take)", Branch1To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 145, NodeString = "Have Item with class? (and take)", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 146, NodeString = "Equipped item with class? (and take)", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 147, NodeString = "Day reached?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 148, NodeString = "Any barrels?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 149, NodeString = "Any crates?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 150, NodeString = "Special Thing happened?", Branch1To = eNodeFields.Ex2b},
            new ScriptInstruction{NodeType = 151, NodeString = "Has Cave Lore?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 152, NodeString = "Has Woodsman?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 153, NodeString = "Has Enough Mage Lore?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 154, NodeString = "Text response?", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 155, NodeString = "Stuff done equal?", Branch1To = eNodeFields.Ex1b},
	
            new ScriptInstruction{NodeType = 170, NodeString = "Make town hostile", StandardMsg=true},
            new ScriptInstruction{NodeType = 171, NodeString = "Change terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 172, NodeString = "Swap Terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 173, NodeString = "Transform terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 174, NodeString = "Move Party", StandardMsg=true},
            new ScriptInstruction{NodeType = 175, NodeString = "Hit Space", StandardMsg=true},
            new ScriptInstruction{NodeType = 176, NodeString = "Explosion on space", StandardMsg=true},
            new ScriptInstruction{NodeType = 177, NodeString = "Lock space", StandardMsg=true},
            new ScriptInstruction{NodeType = 178, NodeString = "Unlock space", StandardMsg=true},
            new ScriptInstruction{NodeType = 179, NodeString = "Do Sfx Burst", StandardMsg=true},
            new ScriptInstruction{NodeType = 180, NodeString = "Make Wandering monster", StandardMsg=true},
            new ScriptInstruction{NodeType = 181, NodeString = "Place a monster", StandardMsg=true},
            new ScriptInstruction{NodeType = 182, NodeString = "Destroy monster", StandardMsg=true},
            new ScriptInstruction{NodeType = 183, NodeString = "Destroy all monsters", StandardMsg=true},
            new ScriptInstruction{NodeType = 184, NodeString = "Generic Lever", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 185, NodeString = "Generic Portal", Branch1To = eNodeFields.BREAK},
            new ScriptInstruction{NodeType = 186, NodeString = "Generic button", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 187, NodeString = "Generic stairway", Branch1To = eNodeFields.BREAK},
            new ScriptInstruction{NodeType = 188, NodeString = "Lever", Branch1To = eNodeFields.Ex1b},
            new ScriptInstruction{NodeType = 189, NodeString = "Portal", Branch1To = eNodeFields.BREAK},
            new ScriptInstruction{NodeType = 190, NodeString = "Stairway", Branch1To = eNodeFields.BREAK},
            new ScriptInstruction{NodeType = 191, NodeString = "Relocate outdoors", StandardMsg=true},
            new ScriptInstruction{NodeType = 192, NodeString = "Place items", StandardMsg=true},
            new ScriptInstruction{NodeType = 193, NodeString = "Split party"},
            new ScriptInstruction{NodeType = 194, NodeString = "Reunite party", StandardMsg=true},
            new ScriptInstruction{NodeType = 195, NodeString = "Start General Timer", StandardMsg=true},
	
            new ScriptInstruction{NodeType = 200, NodeString = "Place Fire Wall", StandardMsg=true},
            new ScriptInstruction{NodeType = 201, NodeString = "Place Force Wall", StandardMsg=true},
            new ScriptInstruction{NodeType = 202, NodeString = "Place Ice Wall", StandardMsg=true},
            new ScriptInstruction{NodeType = 203, NodeString = "Place Blade Wall", StandardMsg=true},
            new ScriptInstruction{NodeType = 204, NodeString = "Place Stinking Cloud", StandardMsg=true},
            new ScriptInstruction{NodeType = 205, NodeString = "Place Sleep Field", StandardMsg=true},
            new ScriptInstruction{NodeType = 206, NodeString = "Place Quickfire", StandardMsg=true},
            new ScriptInstruction{NodeType = 207, NodeString = "Place Fire Barrier", StandardMsg=true},
            new ScriptInstruction{NodeType = 208, NodeString = "Place Force Barrier", StandardMsg=true},
            new ScriptInstruction{NodeType = 209, NodeString = "Cleanse Rectangle", StandardMsg=true},
            new ScriptInstruction{NodeType = 210, NodeString = "Place sfx", StandardMsg=true},
            new ScriptInstruction{NodeType = 211, NodeString = "Place Barrels etc", StandardMsg=true},
            new ScriptInstruction{NodeType = 212, NodeString = "Move Items", StandardMsg=true},
            new ScriptInstruction{NodeType = 213, NodeString = "Destroy Items", StandardMsg=true},
            new ScriptInstruction{NodeType = 214, NodeString = "Change Rectangle terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 215, NodeString = "Swap rectangle terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 216, NodeString = "Transform rectangle terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 217, NodeString = "Lock rectangle", StandardMsg=true},
            new ScriptInstruction{NodeType = 218, NodeString = "Unlock rectangle", StandardMsg=true},
	
            new ScriptInstruction{NodeType = 225, NodeString = "Make Outdoor Wandering"},
            new ScriptInstruction{NodeType = 226, NodeString = "Change Out Terrain", StandardMsg=true},
            new ScriptInstruction{NodeType = 227, NodeString = "Place Outdoor encounter", StandardMsg=true},
            new ScriptInstruction{NodeType = 228, NodeString = "Outdoor move party", StandardMsg=true},
            new ScriptInstruction{NodeType = 229, NodeString = "Outdoor store"}
                                                  
            //Add in the extra special nodes from CBoE here.                                     
            //General: Display Picture
            //If-Thens: Has Enough of Species
            //Town: Change Town Lighting
            //Town: Change Creature Attitude
        };

        class ScriptEntryPoint
        {
            public string FuncName;
            public int Node;
            public int Domain; //0: Global 1: Town 2: Outdoors
            public int X, Y; //X is town number, if Domain is 1
            public eTrigger Trigger;

            public int TileDot = -1; //Used for erasing Trigger Dots from the map when SD flag for node is set.
            public location TileDotLocation = new location();
        }


        enum eTrigger
        {
            //NORMAL, 
            GENERAL,
            MAPTRIGGER,
            TERRAINTRIGGER,
            NPCDEATH,
            OUTDOOR_ENCOUNTER,
            USE_SPECIAL_ITEM,
            CAST_SPELL,
            SANCTIFICATION, 
            TALKING, 
            TOWNEXIT=100, 
            TOWNENTRY
        }

        static List<ScriptEntryPoint> EntryPoints = new List<ScriptEntryPoint>();
        static List<ScriptEntryPoint> LoopbackEntryPoints = new List<ScriptEntryPoint>();

        public static special_node_type GetNode(int node_num, int domain, int x, int y = 0)
        {
            switch (domain)
            {
            case 0:
                return Scenario.scen_specials[node_num];
            case 1:
                LoadTown(x);
                return Town.specials[node_num];
            default:
                LoadOutdoors(x, y);
                return Outdoors.specials[node_num];
            }
        }

        static List<sd> StuffDoneList = new List<sd>(); //Keep track of all the stuff done flags used in the script - to convert to script global variables.
        static int indent = 0;
        static bool specific_pc_selected = false;
        static List<int> NodesVisited = new List<int>();
        static bool TalkingFunc = false;

        static int LoopbackCount = 0;
        static bool WritingScript = false;

        public static void WriteScriptFile()
        {
            //Save all the Town IDs so we can refer to them without having to load the town each time
            for (int x = 0; x < Scenario.num_towns; x++)
            {
                LoadTown(x);
                Town_IDs.Add(GetFriendlyIDString(DataStore1.town_strs[0]) + "_" + x); 
            }


            Console.WriteLine("Getting special items...");
            GetSpecialItems();

            Console.WriteLine("Finding script entry points...");
            GetScriptEntryPoints();

            WritingScript = true;

            //First we write the general script functions for the scenario in 'Main.py'
            Console.WriteLine("Writing 'Main.py'...");

            FileStream f = new FileStream("Scripts\\Main.py", FileMode.Create);
            ScriptFile = new StreamWriter(f);

            WriteScript("def Initialise_Scenario():");
            WriteScript("    pass");
            WriteScript("");

            //We make the introductory message into its own function, called 'Intro_Message()'
            ScriptFile.WriteLine("def Intro_Message(p):");

                string m = "";
                for (int n = 0; n < 6; n++)
                {
                    string s = GetString(1004 + n, 0);
                    if (s != null && s != "") m += (n == 0 ? s : ("\\n\\n" + s));
                }

            if (m == "")
                ScriptFile.WriteLine("    pass");
            else
                WriteScript("    ChoiceBox(\"{0}\", eDialogPic.SCENARIO, {1}, [\"OK\"])", m, Scenario.intro_pic);

            if (HasTownPreEntryFunc)
            {
                ScriptFile.WriteLine("");
                ScriptFile.WriteLine("def Town_Pre_Entry(town):");

                for (int t = 0; t < 10; t++)

                    if (Scenario.town_to_add_to[t] != -1)
                    {
                        WriteScript("    if town.Num=={0}:", Scenario.town_to_add_to[t]);
                        WriteScript("        return TownMap.List[town.Num + StuffDone[\"{0}_{1}\"]]", Scenario.flag_to_add_to_town[t * 2], Scenario.flag_to_add_to_town[t * 2 + 1]);
                    }
                WriteScript("    return town"); 
            }

            WriteScript("");
            //Now parse the rest of the functions from the scenario's special node branches.

            //First the global functions
            foreach (ScriptEntryPoint entry in EntryPoints)
            {
                if (entry.Domain == 0 && entry.Trigger != eTrigger.TERRAINTRIGGER)
                    ParseFunction(entry);
            }

            ScriptFile.Close(); //That's the end of 'main.py'

            //Now write 'shops.py':
            Console.WriteLine("Writing 'Shops.py'...");
            f = new FileStream(String.Format("Scripts\\Shops.py"), FileMode.Create);
            ScriptFile = new StreamWriter(f);
            indent = 0;

            ///Write Restock Shop scripts here!
            bool[] donejumbleshop = new bool[5];
            foreach (ItemShop shop in ItemShops)
            {
                if (shop.JumbleShop && !donejumbleshop[shop.JumbleShopNo])
                {
                    donejumbleshop[shop.JumbleShopNo] = true;
                    ScriptFile.WriteLine("");
                    ScriptFile.WriteLine("def Restock_Jumble_Shop_{0}(shop):", shop.JumbleShopNo);
                    ScriptFile.WriteLine("    shop.Clear()");
                    ScriptFile.WriteLine("    loot_index = [1,1,1,1,2,2,2,3,3,4]");
                    ScriptFile.WriteLine("    for a in range(10):");
                    ScriptFile.WriteLine("        item = Item.GetTreasure(loot_index[a])");
                    ScriptFile.WriteLine("        if item.Variety != eVariety.None and item.Variety != eVariety.Food and item.Variety != eVariety.Gold:");
                    ScriptFile.WriteLine("            item.Identified = True");
                    ScriptFile.WriteLine("            shop.AddItem(item, False)");
                }
                else
                {
                    ScriptFile.WriteLine("");
                    ScriptFile.WriteLine("def Restock_{0}(shop):", shop.ID);
                    ScriptFile.WriteLine("    shop.Clear()");
                    if (shop.SellsStuff)
                    {

                        for (int a = shop.FirstItem; a < shop.FirstItem + shop.NumItems; a++)
                        {
                            if (shop.Type == 0)
                            {
                                if (a >= 0 && a < ScenItems.scen_items.Length)
                                {
                                    m = GetItemID(a);
                                    if (ScenItems.scen_items[a].variety == 11) //Food
                                    {
                                        //For food, offer it in quantities of 1, 10 or 50.
                                        ScriptFile.WriteLine("    shop.AddItem(Item.List[\"{0}\"].Copy(True,1), False)", m);
                                        ScriptFile.WriteLine("    shop.AddItem(Item.List[\"{0}\"].Copy(True,10), False)", m);
                                        ScriptFile.WriteLine("    shop.AddItem(Item.List[\"{0}\"].Copy(True,50), False)", m);
                                    }
                                    else
                                        ScriptFile.WriteLine("    shop.AddItem(Item.List[\"{0}\"].Copy(True), False)", m);
                                }
                            }
                            else if (shop.Type == 1)
                            {
                                if (!shop.SpecificallyPriest)
                                {
                                    if (a >= 0 && a < MageSpellIDs.Length)
                                        ScriptFile.WriteLine("    shop.AddSpell(\"{0}\")", MageSpellIDs[a]);
                                }
                                else
                                    if (a >= 0 && a < PriestSpellIDs.Length)
                                        ScriptFile.WriteLine("    shop.AddSpell(\"{0}\")", PriestSpellIDs[a]);
                            }
                            else if (shop.Type == 2)
                            {
                                if (a >= 0 && a < AlchemyIndex.Length)
                                    ScriptFile.WriteLine("    shop.AddRecipe(\"{0}\")", AlchemyIndex[a]);
                            }
                        }

                    }
                }

            }

            ScriptFile.Close();

            //Now write 'Terrains.py':
            Console.WriteLine("Writing 'Terrains.py'...");
            f = new FileStream(String.Format("Scripts\\Terrains.py"), FileMode.Create);
            ScriptFile = new StreamWriter(f);
            indent = 0;
            WriteScript("def Do_Sign(p):");
            WriteScript("    MessageBox(p.Vars[\"Msg\"])");

            //Write the behaviour for waterfalls here (No longer a terrain type, but a map trigger that calls this function)
            WriteScript("");
            WriteScript("def Do_Waterfall(p):");
            WriteScript("    Sound.Play(\"028_waterfall\")");
            WriteScript("    p.CancelAction = True");
            WriteScript("    p.PC.ForceMove(Location(p.Target.X, p.Target.Y + 2), Direction(eDir.S))");
            WriteScript("    Wait()");
            WriteScript("    if Party.HasTrait(Trait.CaveLore) and Maths.Rand(1,0,1) == 0:");
            WriteScript("        Message(\"  (No supplies lost.)\")");
            WriteScript("    elif Party.Food > 1800:");
            WriteScript("        Party.Food -= 50");
            WriteScript("    else:");
            WriteScript("        Party.Food = (Party.Food * 19) / 20");

            //Write the behaviour for conveyor belts (but only if there's a conveyor belt terrain record in the scenario)
            for (int z = 0; z < 256; z++) //Go through each terrain...
            {
                if (Scenario.ter_types[z].special >= 16 && Scenario.ter_types[z].special <= 19)
                {
                    WriteScript("");
                    WriteScript("def Do_Conveyor_Belt(p):"); //0:N 1:E 2:S 3:W
                    WriteScript("    d = p.Vars[\"Dir\"]");
                    WriteScript("    if p.Origin == eCallOrigin.MOVING:");
                    WriteScript("        if (p.PC.Pos.X > p.Target.X and d == 1) or \\");
                    WriteScript("           (p.PC.Pos.X < p.Target.X and d == 3) or \\");
                    WriteScript("           (p.PC.Pos.Y > p.Target.Y and d == 2) or \\");
                    WriteScript("           (p.PC.Pos.Y < p.Target.Y and d == 0):");
                    WriteScript("            p.CancelAction = True");
                    WriteScript("            Message(\"The moving floor prevents you.\")");
                    WriteScript("    if p.Origin == eCallOrigin.PC_STOOD_ON:");
                    WriteScript("        Message(\"You get pushed.\")");
                    WriteScript("        if d == 0:");
                    WriteScript("            p.PC.ForceMove(p.PC.Pos.Mod(0,-1), Direction(eDir.N))");
                    WriteScript("        elif d == 1:");
                    WriteScript("            p.PC.ForceMove(p.PC.Pos.Mod(1,0), Direction(eDir.E))");
                    WriteScript("        elif d == 2:");
                    WriteScript("            p.PC.ForceMove(p.PC.Pos.Mod(0,1), Direction(eDir.S))");
                    WriteScript("        elif d == 3:");
                    WriteScript("            p.PC.ForceMove(p.PC.Pos.Mod(-1,0), Direction(eDir.W))");
                    WriteScript("    if p.Origin == eCallOrigin.NPC_STOOD_ON:");
                    WriteScript("        if d == 0:");
                    WriteScript("            p.NPCTarget.Walk(eDir.N)");
                    WriteScript("        elif d == 1:");
                    WriteScript("            p.NPCTarget.Walk(eDir.E)");
                    WriteScript("        elif d == 2:");
                    WriteScript("            p.NPCTarget.Walk(eDir.S)");
                    WriteScript("        elif d == 3:");
                    WriteScript("            p.NPCTarget.Walk(eDir.W)");
                    break;
                }
            }

            //First the terrain trigger global functions
            foreach (ScriptEntryPoint entry in EntryPoints)
            {
                if (entry.Domain == 0 && entry.Trigger == eTrigger.TERRAINTRIGGER)
                    ParseFunction(entry);
            }
            indent = 0;

            //Now the special function for a terrain record that calls a LOCAL special node when stepped on. It just runs another script depending on where the player is when they step on it.
            for (int z = 0; z < 256; z++) //Go through each terrain...
            {
                if (Scenario.ter_types[z].special == 12) //...Looking for one that triggers a local special node 
                {
                    string tername = Encoding.ASCII.GetString(ScenItems.ter_names, z * 30, 30);
                    tername = tername.Remove(tername.IndexOf((char)0));
                    tername = GetFriendlyIDString(tername);

                    WriteScript("");
                    WriteScript("def TerrainLocal_{0}_{1}(p):", tername, z);

                    //First, count if there are any actual functions
                    int count = 0;
                    for (int t = 0; t < Scenario.num_towns; t++)
                        if (GetNodeToFuncName(Scenario.ter_types[z].flag1, 1, t, 0) != "") count++;
                    for (int y = 0; y < Scenario.out_height; y++)
                        for (int x = 0; x < Scenario.out_width; x++)
                            if (GetNodeToFuncName(Scenario.ter_types[z].flag1, 2, x, y) != "") count++;

                    if (count == 0)
                        WriteScript("    pass");
                    else
                    {
                        for (int t = 0; t < Scenario.num_towns; t++)
                        {
                            if (GetNodeToFuncName(Scenario.ter_types[z].flag1, 1, t, 0) != "")
                            {
                                WriteScript("    if Game.Mode != eMode.OUTSIDE and Town.Num == {0}:", t);
                                WriteScript("        RunScript(\"{0}\", p)", GetNodeToFuncName(Scenario.ter_types[z].flag1, 1, t, 0));
                                WriteScript("        return");
                            }
                        }
                        for (int y = 0; y < Scenario.out_height; y++)
                            for (int x = 0; x < Scenario.out_width; x++)
                                if (GetNodeToFuncName(Scenario.ter_types[z].flag1, 2, x, y) != "")
                                {
                                    WriteScript("    if Game.Mode == eMode.OUTSIDE and WorldMap.SectorAt(p.Target).SectorPos == Location({0}, {1}):", x, y);
                                    WriteScript("        RunScript(\"{0}\", p)", GetNodeToFuncName(Scenario.ter_types[z].flag1, 2, x, y));
                                    WriteScript("        return");
                                }
                    }
                }
            }

            ScriptFile.Close();

            //Now each town's functions into its own python file

            for (int townno = 0; townno < Scenario.num_towns; townno++)
            {
                LoadTown(townno);
                Console.WriteLine("Writing 'Town_{0:000}_{1}.py'...", townno, GetFriendlyIDString(DataStore1.town_strs[0]));
                f = new FileStream(String.Format("Scripts\\Town_{0:000}_{1}.py", townno, GetFriendlyIDString(DataStore1.town_strs[0])), FileMode.Append);
                ScriptFile = new StreamWriter(f);
                indent = 0;
                WriteWanderingMonstFunc(townno);

                foreach (ScriptEntryPoint entry in EntryPoints)
                {
                    if (entry.Domain == 1 && entry.X == townno)
                        ParseFunction(entry);
                }

                indent = 0;
                //Now each talking node in the town that doesn't call a special node, but does something other than just display text. Eg, talking node type 18 - Display response if the party has enough gold.
                //This is now handled by a script
                for (int x = 0; x < 60; x++)
                {
                    talking_node_type tn = Talking.talk_nodes[x];
                    if (tn.personality == -1) continue;

                    switch (Talking.talk_nodes[x].type)
                    {
                        case 3: //Inn
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Gold < {0}:", tn.extras[0]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            WriteScript("    else:");
                            WriteScript("        Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("        Party.Pos = Location({0}, {1})", tn.extras[2], tn.extras[3]);
                            WriteScript("        Town.UpdateVisible()");
                            WriteScript("        Party.HealAll({0}, True)", 30 * tn.extras[1]);
                            WriteScript("        Party.RestoreSP({0})", 25 * tn.extras[1]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("        CentreView(Party.Pos, False)");
                            break;
                        case 4: //Depends on time
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Day <= {0}:", tn.extras[0]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 5: //Depends on time w/event
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.DayReached({0}, \"Event_{1}\"):", tn.extras[0] + (LEGACY_DAY_DELAY ? 20 : 0), tn.extras[1]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 6: //Depends on town
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Town.ID == \"{0}\":", Town_IDs[tn.extras[0]]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 18: //Buy response
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Gold >= {0}:", tn.extras[0]);
                            WriteScript("        Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 19: //Buy response, change flag
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Gold >= {0}:", tn.extras[0]);
                            WriteScript("        Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("        StuffDone[\"{0}_{1}\"] = {2}", tn.extras[1], tn.extras[2], tn.extras[3]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 20: //Ship shop
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Gold >= {0}:", tn.extras[0]);
                            string boatids = "";
                            for(int a = 0; a < tn.extras[2]; a++)
                            {
                                if (a > 0) boatids += ", ";
                                boatids += "\"Boat_" + (tn.extras[1]+a) + "\"";
                            }
                            WriteScript("        boat_ids = [{0}]", boatids);
                            WriteScript("        boat_sold = False");
                            WriteScript("        for s in boat_ids:");
                            WriteScript("            if Vehicle.List[s].PartyOwns == False:");
                            WriteScript("                Vehicle.List[s].PartyOwns = True");
                            WriteScript("                Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("                boat_sold = True");
                            WriteScript("                break");
                            WriteScript("        if boat_sold == False:");
                            WriteScript("            p.TalkingText = \"There are no boats left.\"");
                            WriteScript("        else:");
                            WriteScript("            p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 21: //Horse shop
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Gold >= {0}:", tn.extras[0]);
                            string horseids = "";
                            for(int a = 0; a < tn.extras[2]; a++)
                            {
                                if (a > 0) horseids += ", ";
                                horseids += "\"Horse_" + (tn.extras[1]+a) + "\"";
                            }
                            WriteScript("        horse_ids = [{0}]", horseids);
                            WriteScript("        horse_sold = False");
                            WriteScript("        for s in horse_ids:");
                            WriteScript("            if Vehicle.List[s].PartyOwns == False:");
                            WriteScript("                Vehicle.List[s].PartyOwns = True");
                            WriteScript("                Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("                horse_sold = True");
                            WriteScript("                break");
                            WriteScript("        if horse_sold == False:");
                            WriteScript("            p.TalkingText = \"There are no horses left.\"");
                            WriteScript("        else:");
                            WriteScript("            p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 22: //Buy special item
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if SpecialItem.PartyHas(\"{0}\"):", SpecialItemList[tn.extras[0]]);
                            WriteScript("        p.TalkingText = \"You already have that.\"");
                            WriteScript("    else:");
                            WriteScript("        if Party.Gold >= {0}:", tn.extras[0]);
                            WriteScript("            Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("            SpecialItem.Give(\"{0}\")", SpecialItemList[tn.extras[0]]);
                            WriteScript("            p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("        else:");
                            WriteScript("            p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 24: //Reveal town location
                            WriteScript("");
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    if Party.Gold >= {0}:", tn.extras[0]);
                            WriteScript("        if TownMap.List[\"{0}\"].Hidden == True:", Town_IDs[tn.extras[1]]);
                            WriteScript("            Party.Gold -= {0}", tn.extras[0]);
                            WriteScript("            TownMap.List[\"{0}\"].Hidden = False", Town_IDs[tn.extras[1]]);
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true));
                            WriteScript("    else:");
                            WriteScript("        p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 41], true));
                            break;
                        case 26: //Hostile conversation end
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    p.NPCTarget.Attitude = eAttitude.HOSTILE_A");
                            WriteScript("    p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true) + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "@n" + FixYeah(DataStore3.talk_strs[x * 2 + 41], true) : ""));
                            break;
                        case 27: //Town hostile conv end
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    Town.MakeTownHostile()");
                            WriteScript("    p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true) + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "@n" + FixYeah(DataStore3.talk_strs[x * 2 + 41], true) : ""));
                            break;
                        case 28: //Eliminate creature
                            WriteScript("def Talking_{0}_{1}(p):", townno, x);
                            WriteScript("    Town.NPCList.Remove(p.NPCTarget)");
                            WriteScript("    if p.NPCTarget.Start.LifeVariable != \"\":");
                            WriteScript("        StuffDone[p.NPCTarget.Start.LifeVariable] = 1");
                            WriteScript("    p.TalkingText = \"{0}\"", FixYeah(DataStore3.talk_strs[x * 2 + 40], true) + (DataStore3.talk_strs[x * 2 + 41].Length > 0 ? "@n" + FixYeah(DataStore3.talk_strs[x * 2 + 41], true) : ""));
                            break;
                    }
                }



                ScriptFile.Close();

            }

            int outx = -1, outy = -1;
            //Now each outdoor section
            foreach (ScriptEntryPoint entry in EntryPoints)
            {
                if (entry.Domain == 2)
                {
                    if (entry.X != outx || entry.Y != outy)
                    {
                        ScriptFile.Close();
                        outx = entry.X; outy = entry.Y;
                        LoadOutdoors(outx, outy);
                        Console.WriteLine("Writing 'Out_{0:000}_{1:000}_{2}.py'...", outx, outy, GetFriendlyIDString(DataStore4.outdoor_text[0]));
                        f = new FileStream(String.Format("Scripts\\Out_{0:000}_{1:000}_{2}.py", outx, outy, GetFriendlyIDString(DataStore4.outdoor_text[0])), FileMode.Append);
                        ScriptFile = new StreamWriter(f);
                        indent = 0;
                    }
                    ParseFunction(entry);
                }
            }
            ScriptFile.Close();

            //Write Loopback functions
            for(int n = 0; n < LoopbackEntryPoints.Count; n++)
            {
                ScriptEntryPoint entry = LoopbackEntryPoints[n];

                Console.WriteLine("Writing '{0}.py'...", FindFuncName(entry.Node, entry.Domain, entry.X, entry.Y));

                if (entry.Domain == 0)
                    f = new FileStream("Scripts\\Main.py", FileMode.Append);
                else if (entry.Domain == 1)
                {
                    LoadTown(entry.X);
                    f = new FileStream(String.Format("Scripts\\Town_{0:000}_{1}.py", entry.X, GetFriendlyIDString(DataStore1.town_strs[0])), FileMode.Append);
                }
                else
                {
                    LoadOutdoors(entry.X, entry.Y);
                    f = new FileStream(String.Format("Scripts\\Out_{0:000}_{1:000}_{2}.py", entry.X, entry.Y, GetFriendlyIDString(DataStore4.outdoor_text[0])), FileMode.Append);
                }
                ScriptFile = new StreamWriter(f);
                indent = 0;
                ParseFunction(entry);
                ScriptFile.Close();
            }

        }

        static void WriteWanderingMonstFunc(int townno)
        {
            bool has_wandering = false;

            for (int x = 0; x < 4; x++)
            {
                if (Town.wandering_locs[x].x >= 0 || Town.wandering_locs[x].y >= 0)
                {
                    has_wandering = true;
                    break;
                }
            }

            if (!has_wandering) return;
          
            has_wandering = false;

                for (int x = 0; x < 4; x++)
                    if (!(Town.wandering[x].monst[0] == 0 && Town.wandering[x].monst[1] == 0 && Town.wandering[x].monst[2] == 0 && Town.wandering[x].monst[3] == 0))
                    {
                        has_wandering = true;
                        break;
                    }

            if (!has_wandering) return;

            //Write function to generate wandering monsters for this town
            WriteScript("def Generate_Wandering_" + townno + "_" + GetFriendlyIDString(DataStore1.town_strs[0]) + "(p):");
            WriteScript("    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation");
            WriteScript("        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return");
            WriteScript("        r1 = Maths.Rand(1,0,3)");
            WriteScript("        npcs = []");

            for (int x = 0; x < 4; x++)
                if (!(Town.wandering[x].monst[0] == 0 && Town.wandering[x].monst[1] == 0 && Town.wandering[x].monst[2] == 0 && Town.wandering[x].monst[3] == 0))
                {
                    WriteScript("        {0} r1 == {1}:", x == 0 ? "if" : "elif", x);
                    if (Town.wandering[x].monst[0] > 0) WriteScript("            npcs.append([1,NPCRecord.List[\"{0}\"]])", GetNPCID(Town.wandering[x].monst[0]));
                    if (Town.wandering[x].monst[1] > 0) WriteScript("            npcs.append([1,NPCRecord.List[\"{0}\"]])", GetNPCID(Town.wandering[x].monst[1]));
                    if (Town.wandering[x].monst[2] > 0) WriteScript("            npcs.append([1,NPCRecord.List[\"{0}\"]])", GetNPCID(Town.wandering[x].monst[2]));
                    if (Town.wandering[x].monst[3] > 0) WriteScript("            npcs.append([2,NPCRecord.List[\"{0}\"]])", GetNPCID(Town.wandering[x].monst[3]));
                }

            WriteScript("        if len(npcs) > 0:");
            WriteScript("            l = Location.Zero");
            WriteScript("            num_tries = 0");
            WriteScript("            ");
            WriteScript("            while l == Location.Zero and num_tries < 100:");
            WriteScript("                num_tries += 1");
            WriteScript("                r2 = Maths.Rand(1,0,3)");
            for (int l = 0; l < 4; l++)
            {
                if (Town.wandering_locs[l].x >= 0 && Town.wandering_locs[l].y >= 0)
                    WriteScript("                {0} r2 == {1}: l = Location({2},{3})",l==0 ? "if" : "elif", l, Town.wandering_locs[l].x, Town.wandering_locs[l].y);
            }
            WriteScript("                ");
            WriteScript("                if Town.InActArea(l):");
            WriteScript("                    for pc in Party.EachIndependentPC():");
            WriteScript("                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero");
            WriteScript("                else:");
            WriteScript("                    l = Location.Zero");
            WriteScript("                    ");
            WriteScript("            if l != Location.Zero:");
            WriteScript("                for n in npcs:");
            WriteScript("                    for m in range(n[0]):");
            WriteScript("                       if m == 0 or Maths.Rand(1,0,1) == 1:");
            WriteScript("                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)");
            WriteScript("                           Town.PlaceNewNPC(n[1], p_loc, False)");

        }

        static void ParseFunction(ScriptEntryPoint entry)
        {
            //This the start point for parsing each function.
            ScriptFile.WriteLine("");
            ScriptFile.WriteLine("def " + entry.FuncName + "(p):");
            Console.WriteLine("  Writing script function: " + entry.FuncName);

            NodesVisited.Clear();
            indent = 4;
            specific_pc_selected = false;
            int domain = entry.Domain;
            int x = entry.X;
            int y = entry.Y;
            int nextnode = entry.Node;
            TalkingFunc = entry.Trigger == eTrigger.TALKING;
            
            string[] dirstr = { "North", "West", "South", "East" };
            //Exit town position is now subsumed into the exit town function
            if (entry.Trigger == eTrigger.TOWNEXIT)
            {
                
                bool elif_yet = false;

                List<int> exitDirSpecs = new List<int>();

                for (int n = 0; n < Town.exit_specs.Length; n++)
                {
                    if (Town.exit_specs[n] >= 0 && !exitDirSpecs.Contains(Town.exit_specs[n]))
                        exitDirSpecs.Add(Town.exit_specs[n]);

                    if (Town.exit_locs[n].x != -1)
                    {
                        if (!elif_yet)
                        {
                            WriteScript("if p.Dir.Is{0}:", dirstr[n]);
                            elif_yet = true;
                        }
                        else
                            WriteScript("elif p.Dir.Is{0}:", dirstr[n]);

                        if (Town.exit_locs[n].x != -1)
                        {
                            int nx = Town.exit_locs[n].x, ny = Town.exit_locs[n].y;
                            if (n == 0) ny++;
                            if (n == 1) nx++;
                            if (n == 2) ny--;
                            if (n == 3) nx--;
                            WriteScript("    Party.OutsidePos = WorldMap.ToGlobal(Location({0}, {1}),WorldMap.SectorAt(Party.OutsidePos))", nx, ny);
                        }
                    }
                }

                elif_yet = false;
                foreach(int spec in exitDirSpecs)
                {
                    StringBuilder ifline = new StringBuilder();
                    bool first = true;
                    if (!elif_yet) {ifline.Append("if "); elif_yet = true;}
                    else ifline.Append("elif ");

                    for (int n = 0; n < Town.exit_specs.Length; n++)
                    {
                        if (Town.exit_specs[n] == spec)
                        {
                            if (!first) ifline.Append(" or "); else first = false;
                            ifline.Append("p.Dir.Is");
                            ifline.Append(dirstr[n]);
                        }
                    }
                    ifline.Append(":");
                    WriteScript(ifline.ToString());
                    indent += 4;
                    nextnode = spec;
                    while (IsValidNodeNumber(nextnode, domain))
                        nextnode = ParseNode(nextnode, domain, x, y);
                    indent -= 4;
                }
            }
            else if (entry.Trigger == eTrigger.TOWNENTRY)
            {
                if (Town.spec_on_entry >= 0 && Town.spec_on_entry_if_dead >= 0 && Town.spec_on_entry != Town.spec_on_entry_if_dead)
                {
                    WriteScript("if Town.Abandoned:");
                    indent += 4;
                    nextnode = Town.spec_on_entry_if_dead;
                    while (IsValidNodeNumber(nextnode, domain))
                        nextnode = ParseNode(nextnode, domain, x, y);
                    indent -= 4;
                    WriteScript("else:");
                    indent += 4;
                    nextnode = Town.spec_on_entry;
                    while (IsValidNodeNumber(nextnode, domain))
                        nextnode = ParseNode(nextnode, domain, x, y);
                    indent -= 4;
                }
                else if (Town.spec_on_entry == Town.spec_on_entry_if_dead)
                {
                    nextnode = Town.spec_on_entry;
                    while (IsValidNodeNumber(nextnode, domain))
                        nextnode = ParseNode(nextnode, domain, x, y);
                }
                else if (Town.spec_on_entry >= 0)
                {
                    WriteScript("if not Town.Abandoned:");
                    indent += 4;
                    nextnode = Town.spec_on_entry;
                    while (IsValidNodeNumber(nextnode, domain))
                        nextnode = ParseNode(nextnode, domain, x, y);
                    indent -= 4;
                }
                else if (Town.spec_on_entry_if_dead >= 0)
                {
                    WriteScript("if Town.Abandoned:");
                    indent += 4;
                    nextnode = Town.spec_on_entry_if_dead;
                    while (IsValidNodeNumber(nextnode, domain))
                        nextnode = ParseNode(nextnode, domain, x, y);
                    indent -= 4;
                }
            }
            else
            {
                if (entry.Trigger == eTrigger.SANCTIFICATION)
                {
                    WriteScript("if p.Spell.ID != \"p_sanctify\":");
                    WriteScript("    return");
                }

                while (IsValidNodeNumber(nextnode, domain))
                {
                    nextnode = ParseNode(nextnode, domain, x, y);
                }
            }
        }


        static bool IsValidNodeNumber(int num, int domain)
        {
            if (domain == 0) //Global
                return num >= 0 && num < 256;
            else if (domain == 1) //Town
                return num >= 0 && num < 100;
            else if (domain == 2) //Outside
                return num >= 0 && num < 60;
            return false;
        }

        static void AddStuffDone(int x, int y)
        {
             if (x >= 0 && x < 300 && y >= 0 && y < 10)
             {
                 if (!StuffDoneList.Contains(new sd{ X = x, Y = y }))
                 {
                     StuffDoneList.Add(new sd{X=x,Y=y});
                 }
             }
        }

        static short GetStuffDoneIndex(int x, int y)
        {  
            return (short)StuffDoneList.FindIndex(n => n.X == x && n.Y == y);
        }


        static int ParseNode(int node_num, int ParseDomain, int ParseX, int ParseY = 0)
        {
            special_node_type nd = GetNode(node_num, ParseDomain, ParseX, ParseY);

            if (nd.type == 0) { WriteScript("return"); return -1; }

            if (NodesVisited.Contains(node_num)) 
            {
                AddToEntryPoints(node_num, ParseDomain, ParseX, ParseY, String.Format("Loopback_{0}_{1}", node_num, LoopbackCount++), eTrigger.GENERAL);
                WriteScript("RunScript(\"{0}\", p)", FindFuncName(node_num, ParseDomain, ParseX, ParseY)); 
                Console.WriteLine("  This node chain loops back on itself - implemented as a RunScript call");
                return -1;
            }
            NodesVisited.Add(node_num);

            ScriptInstruction i = ScriptInstruction.Get(nd);
            if (i == null) return nd.jumpto; //Unrecognised node - by default just move onto jumpto.

            //Standard stuff done check here
            if (i.StdSDCheck && nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
            {
                WriteScript("if StuffDone[\"{0}_{1}\"] == 250:", nd.sd1, nd.sd2);
                AddStuffDone(nd.sd1, nd.sd2);
                WriteScript("    return");

                if (i.StdSDSet)// && i.NodeString != "One-Time Do Nothing")
                {
                    WriteScript("StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                    WriteEraseDotsScript(nd.sd1, nd.sd2, 0);
                    GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                }

            }
                    
            //Standard message display
            if (i.StandardMsg && !(nd.m1 == -1 && nd.m2 == -1))
            {
                if (TalkingFunc)
                    WriteScript("p.TalkingText = \"{0}\"", GetStandardMessage(nd, ParseDomain)); //If this is a function called by a talking node - return the text to display in the conversation window
                else
                    WriteScript("MessageBox(\"{0}\")", GetStandardMessage(nd, ParseDomain));
            }

            switch (i.NodeType)
            {
            case 1: //Set Flag
                WriteScript("StuffDone[\"{0}_{1}\"] = {2}", nd.sd1, nd.sd2, nd.ex1a); 
                AddStuffDone(nd.sd1, nd.sd2); 
                if (nd.ex1a == 250)
                    WriteEraseDotsScript(nd.sd1, nd.sd2, 0);
                break;
            case 2: //Increment Flag
                WriteScript("StuffDone[\"{0}_{1}\"] {2}= {3}", nd.sd1, nd.sd2, nd.ex1b == 0 ? "+" : "-", nd.ex1a); 
                AddStuffDone(nd.sd1, nd.sd2);

                WriteScript("if StuffDone[\"{0}_{1}\"] == 250:", nd.sd1, nd.sd2);
                if (!WriteEraseDotsScript(nd.sd1, nd.sd2, 4)) WriteScript("    pass");

                break;
            case 3: break; //Display Message (already handled by StdMessage)
            case 4: break; //Secret passage. Ignored. To be removed and implemented not in script.
            case 5: //Display small message
                if (nd.m1 != -1)
                    WriteScript("Message(\"{0}\")", GetString(nd.m1, ParseDomain));
                if (nd.m2 != -1)
                    WriteScript("Message(\"{0}\")", GetString(nd.m2, ParseDomain));
                break;
            case 6:
                WriteScript("if StuffDone[\"{0}_{1}\"] == 0: StuffDone[\"{0}_{1}\"] = 1", nd.sd1, nd.sd2); //Flip flag
                WriteScript("else: StuffDone[\"{0}_{1}\"] = 0", nd.sd1, nd.sd2);
                AddStuffDone(nd.sd1, nd.sd2);
                break;
            case 7: //Out Block 
                WriteScript("if Game.Mode == eMode.OUTSIDE:");
                if (nd.ex1a == 1)
                    WriteScript("    p.CancelAction = True");
                WriteScript("    return;");
                break;
            case 8: //Town Block 
                WriteScript("if Game.Mode == eMode.TOWN:");
                if (nd.ex1a == 1)
                    WriteScript("    p.CancelAction = True");
                WriteScript("    return;");
                break;
            case 9: //Combat Block 
                WriteScript("if Game.Mode == eMode.COMBAT:");
                if (nd.ex1a == 1)
                    WriteScript("    p.CancelAction = True");
                WriteScript("    return;");
                break;
            case 10: //Looking block
                WriteScript("if p.Origin == eCallOrigin.SEARCHING: return"); break;
            case 11: //Can't enter
                WriteScript("p.CancelAction = {0}", nd.ex1a == 1 ? "True" : "False");
                if (nd.m1 != -1 || nd.m2 != -1)
                {
                    WriteScript("if p.Origin == eCallOrigin.MOVING:");
                    WriteScript("    MessageBox(\"{0}\")", GetStandardMessage(nd, ParseDomain));
                }
                break;
            case 12: //Change time
                WriteScript("Party.Age += {0}", nd.ex1a); break;
            case 13: //Start General timer (scenario)
                WriteScript("Timer(None, {0}, False,  \"{1}\")", nd.ex1a, FindFuncName(nd.ex1b, 0, 0, 0));
                  break;
            case 14: //Play sound
                if (TalkingFunc)
                    WriteScript("Sound.Play({0})", GetSoundID(nd.ex1a));
                else
                {
                    WriteScript("Animation_Hold(-1, {0})", GetSoundID(nd.ex1a));
                    WriteScript("Wait()");
                }
                break;

            case 15: case 16:
                //Boats and horses are merged together now on one list.
                WriteScript("Vehicle.List[{0}].PartyOwns = {1}", (nd.type == 15 ? "Horse_" : "Boat_") + nd.ex1a, nd.ex2a == 0 ? "True" : "False"); 
                break;
            case 17: //Show/Hide town
                WriteScript("TownMap.List[\"{0}\"].Hidden = {1}", Town_IDs[nd.ex1a], nd.ex1b == 0 ? "True" : "False"); break;
            case 18: //Major event has occurred
                WriteScript("StuffDone[\"Event_{0}\"] = Party.Day", nd.ex1a); break; //'Events' just become global variables.
            case 19: //Forced give
                WriteScript("Party.GiveNewItem(\"{0}\")", GetItemID(nd.ex1a)); break; 
            case 20:
                WriteScript("count = Party.CountItemClass({0}, True)", nd.ex1a);
                if (nd.ex1b != -1)
                {
                    WriteScript("if count == 0:");
                    ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                }

                WriteScript("Party.Gold += count * {0}", nd.ex2a);
                //Standard message display (only if some items taken)
                if (!(nd.m1 == -1 && nd.m2 == -1))
                {
                    if (TalkingFunc)
                        WriteScript("p.TalkingText = \"{0}\"", GetStandardMessage(nd, ParseDomain)); //If this is a function called by a talking node - return the text to display in the conversation window
                    else
                        WriteScript("MessageBox(\"{0}\")", GetStandardMessage(nd, ParseDomain));
                }
                break;
            case 21:
                WriteScript("RunScript(\"{0}\", ScriptParameters(eCallOrigin.CUSTOM))", FindFuncName(nd.jumpto, 0, 0, 0)); break;
            case 22: //Set many flags
                for (int n = 0; n < 10; n++)
                {
                    WriteScript("StuffDone[\"{0}_{1}\"] = {2}", nd.sd1, n, nd.ex1a);
                    if (nd.ex1a == 250)
                        WriteEraseDotsScript(nd.sd1, (short)n, 0);
                    AddStuffDone(nd.sd1, n);
                }
                break;
            case 23: //Copy flag
                WriteScript("StuffDone[\"{0}_{1}\"] = StuffDone[\"{2}_{3}\"]", nd.sd1, nd.sd2, nd.ex1a, nd.ex1b); 
                AddStuffDone(nd.sd1, nd.sd2);
                AddStuffDone(nd.ex1a, nd.ex1b);

                WriteScript("if StuffDone[\"{0}_{1}\"] == 250:", nd.sd1, nd.sd2);
                if (!WriteEraseDotsScript(nd.sd1, nd.sd2, 4)) WriteScript("   pass");

                break;
            case 24: //Ritual of sanct block
                WriteScript("if p.Origin != eCallOrigin.SANCTIFY:");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break; //Condition if origin was not sanctification spell
            case 25: //Have a rest
                WriteScript("if Game.Mode != eMode.COMBAT:");
                WriteScript("    Party.Age += {0}", nd.ex1a);
                WriteScript("    Party.HealAll({0})", nd.ex1b);
                WriteScript("    Party.RestoreSP({0})", nd.ex1b);
                break;
            case 26: //Wandering will fight
                WriteScript("p.CancelAction = {0}",/*.CancelOutdoorEncounter = {0}",*/ nd.ex1a == 0 ? "True" : "False");
                break;
            case 27:
                WriteScript("Scenario.End()"); 
                if (nd.jumpto != -1) WriteScript("return");
                break;
            case 50: //Give item
                if (nd.ex1a != -1)
                    WriteScript("Party.GiveNewItem(\"{0}\")", GetItemID(nd.ex1a));
                if (nd.ex1b > 0)
                    WriteScript("Party.Gold += {0}", nd.ex1b);
                if (nd.ex2a > 0)
                    WriteScript("Party.Food += {0}", nd.ex2a);
                break;
            case 51: //Give special item
                if (nd.ex1a != -1)
                    if (nd.ex1b == 0)
                        WriteScript("SpecialItem.Give(\"{0}\")", GetSpecialItemName(nd.ex1a));
                    else
                        WriteScript("SpecialItem.Take(\"{0}\")", GetSpecialItemName(nd.ex1a));
                break;
            case 52: break;//One time-do nothing:      }
            case 53: break;//One time nothing and set  }--- Automatically handled with StdMessage, StdSDCheck & StdSDSet
            case 54: break;//One time text message     }
            case 55:
            case 56:
            case 57: //Display Dialog

                string pic = "";
                int picnum = GetDialogPic(nd.pic, i.NodeType - 55, out pic);

                string m1 = "";
                for (int n = 0; n < 6; n++)
                {
                    string s = GetString(nd.m1 + n, ParseDomain);
                    if (s != null && s != "") m1 += (n == 0 ? s : ("\\n\\n" + s));
                }

                if (!ValidButtonLabel(nd.ex1a) && !ValidButtonLabel(nd.ex2a)) //No 2nd and 3rd buttons
                {
                    if (nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
                    {
                        WriteScript("StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                        AddStuffDone(nd.sd1, nd.sd2);
                        WriteEraseDotsScript(nd.sd1, nd.sd2, 0);
                        GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                    }
                    WriteScript("ChoiceBox(\"{0}\", {1}, {2}, [\"OK\"])", m1, pic, picnum);
                }
                else if (!ValidButtonLabel(nd.ex1a)) //No 2nd button
                {
                    WriteScript("result = ChoiceBox(\"{0}\", {1}, {2}, [{4}\"{3}\"])", m1, pic, picnum, ButtonLabel[nd.ex2a], nd.m2 == 1 ? "\"Leave\", " : "");
                    WriteScript("if result == {0}:", nd.m2==1 ? 1 : 0);
                    if (nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
                    {
                        WriteScript("    StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                        WriteEraseDotsScript(nd.sd1, nd.sd2, 4);
                        GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                        AddStuffDone(nd.sd1, nd.sd2);
                    }
                    ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                }
                else if (!ValidButtonLabel(nd.ex2a)) //No 3rd button
                {
                    WriteScript("result = ChoiceBox(\"{0}\", {1}, {2}, [{4}\"{3}\"])", m1, pic, picnum, ButtonLabel[nd.ex1a], nd.m2 == 1 ? "\"Leave\", " : "");
                    WriteScript("if result == {0}:", nd.m2==1 ? 1 : 0);
                    if (nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
                    {
                        WriteScript("    StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                        WriteEraseDotsScript(nd.sd1, nd.sd2, 4);
                        GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                        AddStuffDone(nd.sd1, nd.sd2);
                    }
                    ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                }
                else //2nd and 3rd buttons
                {
                    WriteScript("result = ChoiceBox(\"{0}\", {1}, {2}, [{5}\"{3}\", \"{4}\"])", m1, pic, picnum, ButtonLabel[nd.ex1a], ButtonLabel[nd.ex2a], nd.m2 == 1 ? "\"Leave\", " : "");
                    WriteScript("if result == {0}:", nd.m2==1 ? 1 : 0);
                    if (nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
                    {
                        WriteScript("    StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                        WriteEraseDotsScript(nd.sd1, nd.sd2, 4);
                        GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                        AddStuffDone(nd.sd1, nd.sd2);
                    }
                    ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                    WriteScript("elif result == {0}:", nd.m2==1 ? 2 : 1);
                    if (nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
                    {
                        WriteScript("    StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                        WriteEraseDotsScript(nd.sd1, nd.sd2, 4);
                        GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                        AddStuffDone(nd.sd1, nd.sd2);
                    }
                    ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                }
                break;

            case 58: //Give item
            case 59:
            case 60:

                pic = "";

                picnum = GetDialogPic(nd.pic, i.NodeType - 58, out pic);

                m1 = "";
                for (int n = 0; n < 6; n++)
                {
                    string s = GetString(nd.m1 + n, ParseDomain);
                    if (s != null && s != "") m1 += (n == 0 ? s : ("\\n\\n" + s));
                }
                WriteScript("result = ChoiceBox(\"{0}\", {1}, {2}, [\"Take\", \"Leave\"])", m1, pic, picnum);

                WriteScript("if result == 0:");
                if (ValidStuffDone(nd.sd1, nd.sd2))
                {
                    WriteScript("    StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                    WriteEraseDotsScript(nd.sd1, nd.sd2, 4);
                    AddStuffDone(nd.sd1, nd.sd2);
                }
                GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                if (nd.m2 != -1) WriteScript("    SpecialItem.Give(\"{0}\")", GetSpecialItemName(nd.m2)); 
                if (nd.ex1a != -1) WriteScript("    Party.GiveNewItem(\"{0}\")", GetItemID(nd.ex1a));
                if (nd.ex1b > 0) WriteScript("    Party.Gold += {0}", nd.ex1b);
                if (nd.ex2a > 0) WriteScript("    Party.Food += {0}", nd.ex2a);

                if (nd.ex2b != -1)
                    ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                WriteScript("return"); //This node ends the node chain if player doesn't take item, for some reason.

                break;
            case 61: case 227://One-Time Place Outdoor Encounter  

                if (ParseDomain == 2)
                    WriteScript("WorldMap.SpawnEncounter(\"Group_{0}_{1}_{2}\", p.Target)", ParseX, ParseY, nd.ex1a + 4);

                break;
            case 62: //One_time Place Town enocunter
                if (ParseDomain == 1)
                    WriteScript("Town.PlaceEncounterGroup({0})", nd.ex1a);
                break;
            case 63: //Trap
                string msg = GetStandardMessage(nd, ParseDomain);
                if (msg == null) msg = "You've found a trap. Do you want to try to disarm it?";
                string[] traptype = {
                    "RANDOM",
                    "BLADE",
                    "DART",
                    "GAS",
                    "EXPLOSION",	// damages all => uses c_town.difficulty rather than level to calculates damages (and even c_town.difficulty /13).
                    "SLEEP_RAY",
                    "FALSE_ALARM",
                    "DRAIN_XP",
                    "ALERT",		// makes town hostile
                    "FLAMES",		// damages all => uses level (*5) to calculates damages.
                    "DUMBFOUND",   //dumbfound all
                    "DISEASE",
                    "DISEASE_ALL"
                };
                string t = nd.ex1a >= 0 && nd.ex1a < traptype.Length ? traptype[nd.ex1a] : "BLADE";

                WriteScript("if Game.Mode == eMode.COMBAT:");
                WriteScript("    if ChoiceBox(\"{0}\", eDialogPic.NONE, 0, [\"Disarm\", \"Leave\"]) == 1:", msg);
                WriteScript("        p.CancelAction = True");
                WriteScript("        return");
                WriteScript("    pc = p.PC");
                WriteScript("else:");
                WriteScript("    pc = SelectPCBox(\"{0}\")", msg); 
                WriteScript("    if pc == None:");
                WriteScript("        p.CancelAction = True");
                WriteScript("        return");
                if (nd.sd1 >= 0 && nd.sd1 < 300 && nd.sd2 >= 0 && nd.sd2 < 10)
                {
                    WriteScript("StuffDone[\"{0}_{1}\"] = 250", nd.sd1, nd.sd2);
                    WriteEraseDotsScript(nd.sd1, nd.sd2, 0);
                    GetNode(node_num, ParseDomain, ParseX, ParseY); //To load back whatever map this node was from.
                    AddStuffDone(nd.sd1, nd.sd2);
                }
                WriteScript("pc.RunTrap(eTrapType.{0}, {1}, {2})", t, nd.ex1b, nd.ex2a);
                break;

            case 80: //Select a PC

                if (nd.ex1a == 2) //This doesn't run the dialog but sets further Affect PC nodes to target the whole party.
                    specific_pc_selected = false;
                else
                {
                    WriteScript("pc = SelectPCBox(\"{0}\",{1})", (nd.m1 == -1 && nd.m2 == -1) ? "Select a member of your party:" : GetStandardMessage(nd, ParseDomain), nd.ex1a == 0 ? "True" : "False");
                    WriteScript("if pc == None:");
                    specific_pc_selected = false;
                    ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                    specific_pc_selected = true;
                }
                break;
            case 81: //Do Damage
                string damtype = GetDamageTypeString(nd.ex2b);

                if (specific_pc_selected)
                    WriteScript("pc.Damage()");
                else
                    WriteScript("Party.Damage(Maths.Rand({0}, 1, {1}) + {2}, {3})", nd.ex1a, nd.ex1b, nd.ex2a, damtype);
                WriteScript("Wait()");
                break;

            case 82: //Affect health
                if (specific_pc_selected)
                    WriteScript("pc.Health {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                else
                    WriteScript("Party.HealAll({0}{1})", nd.ex1b == 0 ? "" : "-", nd.ex1a);
                break;
            case 83: //Affect spell points
                if (specific_pc_selected) WriteScript("pc.SP {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.SP{0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                }
                break;
            case 84: //Affect Experience
                if (specific_pc_selected) WriteScript("pc.AwardXP({0}{1})", nd.ex1b == 0 ? "" : "-", nd.ex1a);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.AwardXP({0}{1})", nd.ex1b == 0 ? "" : "-", nd.ex1a);
                }
                break;
            case 85: //Affect skill points
                if (specific_pc_selected) WriteScript("pc.SkillPoints {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.SkillPoints {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                }
                break;
            case 86: //Kill/Raise

                if (nd.ex1b == 0) //Raise

                    if (specific_pc_selected)
                    {
                        WriteScript("if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:");
                        WriteScript("    pc.LifeStatus = eLifeStatus.ALIVE");
                    }
                    else
                    {
                        WriteScript("for pc in Party.EachAlivePC():");
                        WriteScript("    if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:");
                        WriteScript("        pc.LifeStatus = eLifeStatus.ALIVE");
                    }
                else
                {
                    string deathtype;
                    if (nd.ex1b == 1) deathtype = "eLifeStatus.DUST";
                    else if (nd.ex1b == 2) deathtype = "eLifeStatus.STONE";
                    else deathtype = "eLifeStatus.DEAD";

                    if (specific_pc_selected)
                    {
                        WriteScript("pc.Kill(None, {0}, True)", deathtype);
                        WriteScript("Wait()");
                    }
                    else
                    {
                        WriteScript("for pc in Party.EachAlivePC():");
                        WriteScript("    if pc.LifeStatus == eLifeStatus.ALIVE:");
                        WriteScript("        pc.Kill(None, {0}, True)", deathtype);
                        WriteScript("        Wait()");
                    }
                }
                break;
            case 87: //Affect poison
                string what = nd.ex1b == 0 ? "Cure" : "Poison";

                if (specific_pc_selected) WriteScript("pc.{0}({1})", what, nd.ex1a);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.{0}({1})", what, nd.ex1a);
                }
                break;
            case 88:
            case 89:
            case 90:
            case 91:
            case 92:
            case 93:
            case 94:
            case 95:
            case 96:
            case 97://Affect slow/haste

                bool zero_adds = true; int min = 0, max = 8;
                string stat = "";
                switch (i.NodeType)
                {
                case 88: stat = "HASTE_SLOW"; min = -8; break;
                case 89: stat = "INVULNERABLE"; break;
                case 90: stat = "MAGIC_RESISTANCE"; break;
                case 91: stat = "WEBS"; zero_adds = false; break;
                case 92: stat = "DISEASE"; zero_adds = false; break;
                case 93: stat = "INVISIBLE"; break;
                case 94: stat = "BLESS_CURSE"; min = -8; break;
                case 95: stat = "DUMB"; zero_adds = false; max = 7; break;
                case 96: stat = "ASLEEP"; zero_adds = false; break;
                case 97: stat = "PARALYZED"; zero_adds = false; max = 5000; break;
                }

                if (specific_pc_selected)
                    WriteScript("pc.SetStatus(eAffliction.{0}, Maths.MinMax({1}, {2}, pc.Status(eAffliction.{0}) {3} {4}))", stat, min, max, ((nd.ex1b == 0 && zero_adds) || (nd.ex1b != 0 && !zero_adds)) ? "+" : "-", nd.ex1a);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.SetStatus(eAffliction.{0}, Maths.MinMax({1}, {2}, pc.Status(eAffliction.{0}) {3} {4}))", stat, min, max, ((nd.ex1b == 0 && zero_adds) || (nd.ex1b != 0 && !zero_adds)) ? "+" : "-", nd.ex1a);
                }
                break;
            case 98: //Affect statistic
                stat = "";
                switch (nd.ex2a)
                {
                case 0: stat = "STRENGTH"; break;
                case 1: stat = "DEXTERITY"; break;
                case 2: stat = "INTELLIGENCE"; break;
                case 3: stat = "EDGED_WEAPONS"; break;
                case 4: stat = "BASHING_WEAPONS"; break;
                case 5: stat = "POLE_WEAPONS"; break;
                case 6: stat = "THROWN_MISSILES"; break;
                case 7: stat = "ARCHERY"; break;
                case 8: stat = "DEFENSE"; break;
                case 9: stat = "MAGE_SPELLS"; break;
                case 10: stat = "PRIEST_SPELLS"; break;
                case 11: stat = "MAGE_LORE"; break;
                case 12: stat = "ALCHEMY"; break;
                case 13: stat = "ITEM_LORE"; break;
                case 14: stat = "DISARM_TRAPS"; break;
                case 15: stat = "LOCKPICKING"; break;
                case 16: stat = "ASSASSINATION"; break;
                case 17: stat = "POISON"; break;
                case 18: stat = "LUCK"; break;
                }
                if (specific_pc_selected)
                    WriteScript("pc.SetSkill(eSkill.{0}, pc.GetSkill(eSkill.{0}) {1} {2})", stat, nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.SetSkill(eSkill.{0}, pc.GetSkill(eSkill.{0}) {1} {2})", stat, nd.ex1b == 0 ? "+" : "-", nd.ex1a);
                }
                break;
            case 99: //Give mage spell
                if (specific_pc_selected) WriteScript("pc.LearnSpell(\"{0}\")", MageSpellIDs[nd.ex1a]);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.LearnSpell(\"{0}\")", MageSpellIDs[nd.ex1a]);
                }
                break;
            case 100: //Give priest spell
                if (specific_pc_selected) WriteScript("pc.LearnSpell(\"{0}\")", PriestSpellIDs[nd.ex1a]);
                else
                {
                    WriteScript("for pc in Party.EachAlivePC():");
                    WriteScript("    pc.LearnSpell(\"{0}\")", PriestSpellIDs[nd.ex1a]);
                }
                break;
            case 101: //Affect gold
                WriteScript("Party.Gold {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a); break;
            case 102: //Affect food
                WriteScript("Party.Food {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a); break;
            case 103: //Give alchemy
                WriteScript("Party.LearnRecipe(\"{0}\")", AlchemyIndex[nd.ex1a]); break;
            case 104: //Give stealth
                WriteScript("Party.Stealth {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a); break;
            case 105: //Give Firewalk
                WriteScript("Party.Firewalk {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a); break;
            case 106: //Give flying
                WriteScript("Party.Flying {0}= {1}", nd.ex1b == 0 ? "+" : "-", nd.ex1a); break;

            
            case 130: //Stuff Done Flag?
                if (nd.ex1a != -1)
                {
                    WriteScript("if StuffDone[\"{0}_{1}\"] >= {2}:", nd.sd1, nd.sd2, nd.ex1a);
                    AddStuffDone(nd.sd1, nd.sd2);
                    ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                }
                if (nd.ex2a != -1)
                {
                    WriteScript("if StuffDone[\"{0}_{1}\"] < {2}:", nd.sd1, nd.sd2, nd.ex2a);
                    AddStuffDone(nd.sd1, nd.sd2);
                    ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                }
                break;
            case 131: //Town number?
                WriteScript("if Game.Mode != eMode.OUTSIDE and Town.Num == {0}:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 132: //Random number?
                WriteScript("if Maths.Rand(1,0,100) < {0}:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 133: //Has special item
                WriteScript("if SpecialItem.PartyHas(\"{0}\"):", GetSpecialItemName(nd.ex1a));//"if Party.HasSpecialItem({0}):", GetSpecialItemName(nd.ex1a));
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 134: //Stuff done compare?
                WriteScript("if StuffDone[\"{0}_{1}\"] >= StuffDone[\"{2}_{3}\"]:", nd.sd1, nd.sd2, nd.ex1a, nd.ex1b);
                AddStuffDone(nd.sd1, nd.sd2);
                AddStuffDone(nd.ex1a, nd.ex1b);
                ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                break;               
            case 135: //Terrain this type (town)
                WriteScript("if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location({0},{1})).Num == {2}:", nd.ex1a, nd.ex1b, nd.ex2a);
                ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                break;
            case 136: //Terrain this type (outdoors)
                WriteScript("if Game.Mode == eMode.OUTSIDE and WorldMap.TerrainAt(Location({0},{1})).Num == {2}:", ParseX * 48 + nd.ex1a, ParseY * 48 + nd.ex1b, nd.ex2a);
                ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                break;
            case 137: //Has gold?
                WriteScript("if Party.Gold >= {0}:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 138: //Has food?
                WriteScript("if Party.Food >= {0}:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 139: //Item class on space?
                WriteScript("itemthere = False");
                WriteScript("if Game.Mode != eMode.OUTSIDE:");
                WriteScript("    for i in Town.EachItemThere(Location({0},{1}), True):", nd.ex1a, nd.ex1b);
                WriteScript("        if i.SpecialClass == {0}:", nd.ex2a);
                WriteScript("            itemthere = True");
                WriteScript("            break");
                WriteScript("if itemthere == True:");
                ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                break;
            case 140: //Have item with class?
                WriteScript("if Party.CountItemClass({0}, False) > 0:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 141: //Equipped item with class?
                WriteScript("if Party.CountItemClassEquipped({0}, False) > 0:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 142: //Has Gold? (and take)
                WriteScript("if Party.Gold >= {0}:", nd.ex1a);
                WriteScript("    Party.Gold -= {0}", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 143: //Has Food? (and take)
                WriteScript("if Party.Food >= {0}:", nd.ex1a);
                WriteScript("    Party.Food -= {0}", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 144: //Item class on space? (and take)
                WriteScript("itemthere = False");
                WriteScript("if Game.Mode != eMode.OUTSIDE:");
                WriteScript("    for n in range(Town.ItemList.Count - 1, -1, -1):");//i in Town.EachItemThere(Location({0},{1}), True):", nd.ex1a, nd.ex1b);
                WriteScript("        i = Town.ItemList[n]");
                WriteScript("        if i.Pos == Location({0},{1}) and i.SpecialClass == {2}:", nd.ex1a, nd.ex1b, nd.ex2a);
                WriteScript("            Town.ItemList.Remove(i)");
                WriteScript("            itemthere = True");
                WriteScript("            break");
                WriteScript("if itemthere == True:");
                ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                break;
            case 145: //Have item with class? (and take)
                WriteScript("if Party.CountItemClass({0}, True) > 0:",nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 146: //Equipped item with class? (and take)
                WriteScript("if Party.CountItemClassEquipped({0}, True) > 0:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 147:
                WriteScript("if Party.Day >= {0}:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 148: case 149: //Any barrels?
                WriteScript("foundit = False");
                WriteScript("if Game.Mode != eMode.OUTSIDE:");
                WriteScript("    for x in range(Town.Width):");
                WriteScript("        for y in range(Town.Height):");
                WriteScript("            if Town.FieldThere(Location(x,y), Field.{0}):", nd.type == 148 ? "BARREL" : "CRATE");
                WriteScript("                foundit = True");
                WriteScript("                break");
                WriteScript("        if foundit == True: break");
                WriteScript("if foundit == True:");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 150: //It's day x and a special thing hasn't happened?
                
                if (nd.ex1b > 0)
                    WriteScript("if Party.DayReached({0}, \"Event_{1}\"):", nd.ex1a + (LEGACY_DAY_DELAY ? 20 : 0), nd.ex1b);
                else
                    WriteScript("if Party.Day >= {0}:", nd.ex1a + (LEGACY_DAY_DELAY ? 20 : 0));
                ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                break;                
            case 151:
                WriteScript("if Party.HasTrait(Trait.CaveLore):");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;      
            case 152:
                WriteScript("if Party.HasTrait(Trait.Woodsman):");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 153:
                WriteScript("if Party.GetSkillTotal(eSkill.MAGE_LORE) > {0}:", nd.ex1a);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break; 

            case 154: //Text Response?
                WriteScript("response = InputTextBox(\"Enter something:\", \"\")"); 
                WriteScript("response = response[0:{0}].upper()", nd.pic);
                if (nd.ex1a != -1)
                {
                    string response = GetString(nd.ex1a + 1000, 0).ToUpper();
                    if (nd.pic < response.Length) response = response.Substring(0, nd.pic);
                    WriteScript("if response == \"{0}\":", response);
                    ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                }
                if (nd.ex2a != -1)
                {
                    string response = GetString(nd.ex2a + 1000, 0).ToUpper();
                    if (nd.pic < response.Length) response = response.Substring(0, nd.pic);
                    WriteScript("elif response == \"{0}\":", response);
                    ParseBranch(nd.ex2b, ParseDomain, ParseX, ParseY);
                }
                break;
            case 155: //Stuff done equal?
                WriteScript("if StuffDone[\"{0}_{1}\"] == {2}:", nd.sd1, nd.sd2, nd.ex1a);
                AddStuffDone(nd.sd1, nd.sd2);
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;

            case 170: //Town Hostile
                WriteScript("Town.MakeTownHostile()"); break;
            case 171: //Change Terrain
                WriteScript("Town.AlterTerrain(Location({0},{1}), 0, TerrainRecord.UnderlayList[{2}])", nd.ex1a, nd.ex1b, nd.ex2a); break;
            case 172: //Swap terrain
                WriteScript("t = Town.TerrainAt(Location({0},{1}))", nd.ex1a, nd.ex1b);
                WriteScript("if t == TerrainRecord.UnderlayList[{0}]: Town.AlterTerrain(Location({1},{2}), 0, TerrainRecord.UnderlayList[{3}])", nd.ex2a, nd.ex1a, nd.ex1b, nd.ex2b);
                WriteScript("elif t == TerrainRecord.UnderlayList[{0}]: Town.AlterTerrain(Location({1},{2}), 0, TerrainRecord.UnderlayList[{3}])", nd.ex2b, nd.ex1a, nd.ex1b, nd.ex2a);
                break;
            case 173: //Transform Terrain
                WriteScript("t = Town.TerrainAt(Location({0},{1})).TransformTo", nd.ex1a, nd.ex1b);
                WriteScript("Town.AlterTerrain(Location({0},{1}), 0, t)", nd.ex1a, nd.ex1b); break;
            case 174: //Move party
                WriteScript("if Game.Mode == eMode.COMBAT:");
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");

                if (nd.ex2a == 0)
                    WriteScript("Party.Reposition(Location({0},{1}))", nd.ex1a, nd.ex1b);
                else
                {
                    WriteScript("Animation_Vanish(Party.LeaderPC, True, \"010_teleport\")");
                    WriteScript("for n in range(9):");
                    WriteScript("    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)");
                    WriteScript("    Animation_Pause(50)");
                    WriteScript("Wait()");
                    WriteScript("Party.Reposition(Location({0},{1}))", nd.ex1a, nd.ex1b);
                    WriteScript("p.CancelAction = True");
                    WriteScript("Animation_Vanish(Party.LeaderPC, False, \"010_teleport\");");
                    WriteScript("for n in range(9):");
                    WriteScript("    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)");
                    WriteScript("    Animation_Pause(50)");
                }
                WriteScript("p.CancelAction = True");
                break;
            case 175: //Hit space
                WriteScript("Town.HitArea(Location({0},{1}), 1, {2}, 0, {3}, Pattern.Single, False, None)", nd.ex1a, nd.ex1b, nd.ex2a, GetDamageTypeString(nd.ex2b));
                WriteScript("Wait()");
                break;
            case 176: //Explosion on space
                WriteScript("for ch in Town.EachCharacterInRange(Location({0},{1}), {2}):", nd.ex1a, nd.ex1b, nd.pic);
                WriteScript("    ch.Damage(None, {0}, 0, {1})", nd.ex2a, GetDamageTypeString(nd.ex2b));
                break;
            case 177: //Lock space
                WriteScript("t = Town.TerrainAt(Location({0},{1}))", nd.ex1a, nd.ex1b);
                WriteScript("if t.InGroup(\"Lockable\"):");
                WriteScript("    t = Town.TerrainAt(Location({0},{1})).TransformTo", nd.ex1a, nd.ex1b);
                WriteScript("    Town.AlterTerrain(Location({0},{1}), 0, t)", nd.ex1a, nd.ex1b);

                //WriteScript("t = Town.TerrainAt(Location({0},{1})).GetLocked()", nd.ex1a, nd.ex1b);
                //WriteScript("Town.AlterTerrain(Location({0},{1}), t)", nd.ex1a, nd.ex1b);
                break;
            case 178: //Unlock space
                WriteScript("t = Town.TerrainAt(Location({0},{1}))", nd.ex1a, nd.ex1b);
                WriteScript("if t.InGroup(\"Unlockable\"):");
                WriteScript("    t = Town.TerrainAt(Location({0},{1})).TransformTo", nd.ex1a, nd.ex1b);
                WriteScript("    Town.AlterTerrain(Location({0},{1}), 0, t)", nd.ex1a, nd.ex1b);

                //WriteScript("t = Town.TerrainAt(Location({0},{1})).GetUnlocked()", nd.ex1a, nd.ex1b);
                //WriteScript("Town.AlterTerrain(Location({0},{1}), t)", nd.ex1a, nd.ex1b);
                break;
            case 179: //Do sfx burst
                WriteScript("Animation_Explosion(Location({0},{1}), {2}, \"005_explosion\")", nd.ex1a, nd.ex1b, nd.ex2a);
                WriteScript("Animation_Hold()");
                WriteScript("Wait()");
                break;
            case 180: //Make wandering monster
                WriteScript("RunScript(\"Generate_Wandering_{0}_{1}\", ScriptParameters(eCallOrigin.CUSTOM))", ParseX, GetFriendlyIDString(DataStore1.town_strs[0]));
                break;
            case 181: //Place a monster
                WriteScript("Town.PlaceNewNPC(NPCRecord.List[\"{0}\"], Location({1},{2}), {3})", GetNPCID(nd.ex2a), nd.ex1a, nd.ex1b, nd.ex2b == 0 ? "False" : "True");
                break;
            case 182: //Destroy 
                WriteScript("for n in range(Town.NPCList.Count-1, -1, -1):");
                WriteScript("    npc = Town.NPCList[n]");
                WriteScript("    if npc.Record.ID == \"{0}\": Town.NPCList.Remove(npc)", GetNPCID(nd.ex1a));
                break;
            case 183: //Destroy all monsters
                if (nd.ex1a == 0) WriteScript("Town.NPCList.Clear()");
                else
                {
                    WriteScript("for n in range(Town.NPCList.Count-1, -1, -1):");
                    WriteScript("    npc = Town.NPCList[n]");
                    if (nd.ex1a == 1) WriteScript("    if not npc.IsABaddie: Town.NPCList.Remove(npc)");
                    else WriteScript("    if  npc.IsABaddie: Town.NPCList.Remove(npc)");
                }
                break;
            case 184: //Generic lever
                WriteScript("if ChoiceBox(\"There is a stout wooden lever protruding from the ground here. Pull it?\", eDialogPic.STANDARD, 9, [\"Yes\", \"No\"]) == 0:"); 
                WriteScript("    t = Town.TerrainAt(p.Target).TransformTo");
                WriteScript("    Town.AlterTerrain(p.Target, 0, t)");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 185: //Generic portal
                WriteScript("if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:");
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");
                WriteScript("if ChoiceBox(\"There is a glowing teleporter here. Do you step through?\", eDialogPic.STANDARD, 22, [\"Enter\", \"Leave\"]) == 0:");
                WriteScript("    Animation_Vanish(Party.LeaderPC, True, \"010_teleport\");");
                WriteScript("    for n in range(9):");
                WriteScript("        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)");
                WriteScript("        Animation_Pause(50)");
                WriteScript("    Wait()");
                WriteScript("    Party.Reposition(Location({0},{1}))", nd.ex1a, nd.ex1b);
                WriteScript("    p.CancelAction = True");
                WriteScript("    Animation_Vanish(Party.LeaderPC, False, \"010_teleport\");");
                WriteScript("    for n in range(9):");
                WriteScript("        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)");
                WriteScript("        Animation_Pause(50)");
                WriteScript("    return");
                break;
            case 186: //Generic button
                WriteScript("if ChoiceBox(\"There is a large button here, waiting to be pressed. Do you?\", eDialogPic.STANDARD, 11, [\"Yes\", \"No\"]) == 0:");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;
            case 187: //Generic Stairway
                WriteScript("if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:");
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");
                string desc = "";
                switch (nd.ex2b)
                {
                case 0: desc = "You find a stairway heading up."; break;
                case 1: desc = "You find a stairway heading down."; break;
                case 2: desc = "The passageway you're walking down slopes sharply upward here."; break;
                case 3: desc = "The passageway you're walking down slopes sharply downward here."; break;
                case 4: desc = "You find a stairway heading up. The steps are covered with a thin layer of slick, unpleasant slime."; break;
                case 5: desc = "You find a stairway heading down. You will have to be careful - the steps are covered with a thin layer of slick, unpleasant slime."; break;
                case 6: desc = "The passageway you're walking down slopes upward into darkness."; break;
                case 7: desc = "The passageway you're walking down slopes downward here, descending steeply into total darkness."; break;
                }
                WriteScript("if ChoiceBox(\"{0}\", eDialogPic.STANDARD, 19, [\"Climb\", \"Leave\"]) == 1:", desc);
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");
                WriteScript("Animation_FadeDown()");
                WriteScript("Wait()");
                WriteScript("Party.Pos = Location({0},{1})", nd.ex1a, nd.ex1b);
                WriteScript("Party.MoveToMap(TownMap.List[\"{0}\"])", Town_IDs[nd.ex2a]);
                if (IsValidNodeNumber(nd.jumpto, 1) && nd.ex2a > 0 && nd.ex2a <= Scenario.num_towns)
                    WriteScript("RunScript(\"{0}\", ScriptParameters(eCallOrigin.CUSTOM))", FindFuncName(nd.jumpto, 1, nd.ex2a, 0));

                return -1; //nd.jumpto is used for the node in the destination town, which is called with a new script, so no need to carry on this branch.

            case 188: //Lever

                m1 = "";
                for (int n = 0; n < 6; n++)
                {
                    string s = GetString(nd.m1 + n, ParseDomain);
                    if (s != null && s != "") m1 += (n==0 ? s : ("\\n" + s));
                }
                WriteScript("if ChoiceBox(\"{0}\", eDialogPic.STANDARD, {1}, [\"Yes\", \"No\"]) == 0:", m1, nd.pic);
                WriteScript("    t = Town.TerrainAt(p.Target).TransformTo");
                WriteScript("    Town.AlterTerrain(p.Target, 0, t)");
                ParseBranch(nd.ex1b, ParseDomain, ParseX, ParseY);
                break;

            case 189: //Portal
                WriteScript("if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:");
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");
                m1 = "";
                for (int n = 0; n < 6; n++)
                {
                    string s = GetString(nd.m1 + n, ParseDomain);
                    if (s != null && s != "") m1 += (n == 0 ? s : ("\\n" + s));
                }
                WriteScript("if ChoiceBox(\"{0}\", eDialogPic.STANDARD, {1}, [\"Yes\", \"No\"]) == 0:", m1, nd.pic);
                WriteScript("    Animation_Vanish(Party.LeaderPC, True, \"010_teleport\");");
                WriteScript("    for n in range(9):");
                WriteScript("        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)");
                WriteScript("        Animation_Pause(50)");
                WriteScript("    Wait()");
                WriteScript("    Party.Reposition(Location({0},{1}))", nd.ex1a, nd.ex1b);
                WriteScript("    p.CancelAction = True");
                WriteScript("    Animation_Vanish(Party.LeaderPC, False, \"010_teleport\");");
                WriteScript("    for n in range(9):");
                WriteScript("        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)");
                WriteScript("        Animation_Pause(50)");
                WriteScript("    return");
                break;

            case 190: //Stairway
                //Generic Stairway & Stairway are the only nodes that can change the town mid-script. nd.jumpto in this case refers to a node in the town the party has
                //just moved to - it is not called and execution ends if the player cancels the dialog.

                WriteScript("if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:");
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");

                if (nd.ex2b != 1) // 1 means the move is forced and no window is displayed.
                {
                    m1 = "";
                    for (int n = 0; n < 6; n++)
                    {
                        string s = GetString(nd.m1 + n, ParseDomain);
                        if (s != null && s != "") m1 += (n == 0 ? s : ("\\n" + s));
                    }
                    WriteScript("if ChoiceBox(\"{0}\", eDialogPic.STANDARD, {1}, [\"Yes\", \"No\"]) == 1:", m1, nd.pic);
                    WriteScript("    p.CancelAction = True");
                    WriteScript("    return");
                    WriteScript("Animation_FadeDown()");
                    WriteScript("Wait()");
                    WriteScript("Party.Pos = Location({0},{1})", nd.ex1a, nd.ex1b);
                    WriteScript("Party.MoveToMap(TownMap.List[\"{0}\"])", Town_IDs[nd.ex2a]);
                    if (IsValidNodeNumber(nd.jumpto, 1) && nd.ex2a > 0 && nd.ex2a <= Scenario.num_towns)
                        WriteScript("RunScript(\"{0}\", ScriptParameters(eCallOrigin.CUSTOM))", FindFuncName(nd.jumpto, 1, nd.ex2a, 0));
                    return -1; //nd.jumpto is used for the node in the destination town, which is called with a new script, so no need to carry on this branch.
                }
                else
                {
                    WriteScript("Animation_FadeDown()");
                    WriteScript("Wait()");
                    WriteScript("Party.Pos = Location({0},{1})", nd.ex1a, nd.ex1b);
                    WriteScript("Party.MoveToMap(TownMap.List[\"{0}\"])", Town_IDs[nd.ex2a]);
                    if (IsValidNodeNumber(nd.jumpto, 1) && nd.ex2a > 0 && nd.ex2a <= Scenario.num_towns)
                        WriteScript("RunScript(\"{0}\", ScriptParameters(eCallOrigin.CUSTOM))", FindFuncName(nd.jumpto, 1, nd.ex2a, 0));
                    return -1; //nd.jumpto is used for the node in the destination town, which is called with a new script, so no need to carry on this branch.
                }

            case 191: //Relocate outdoors
                WriteScript("Party.OutsidePos = Location({0}, {1})", nd.ex1a * 48 + nd.ex2a, nd.ex1b * 48 + nd.ex2b);
                break;
            case 192: //Place item
                WriteScript("Town.PlaceItem(Item.List[\"{0}\"].Copy(), Location({1},{2}))", GetItemID(nd.ex2a), nd.ex1a, nd.ex1b);
                break;
            case 193: //Split party
                WriteScript("pc = SelectPCBox(\"{0}\",True)", (nd.m1 == -1 && nd.m2 == -1) ? "Select one member of your party?" : GetStandardMessage(nd, ParseDomain));
                WriteScript("if pc == None:");
                WriteScript("    p.CancelAction = True");
                WriteScript("    return");
                WriteScript("Party.Split(pc, Location({0},{1}))", nd.ex1a, nd.ex1b);
                if (nd.ex2a != 0) WriteScript("Sound.Play(\"010_teleport\")");
                break;
            case 194: //Reunite party
                WriteScript("if Party.IsSplit:");
                WriteScript("    Party.Reunite()");
                if (nd.ex1a != 0) WriteScript("    Sound.Play(\"010_teleport\")");
                break;
            case 195: //Start general timer
                WriteScript("Timer(Town, {0}, False, \"{1}\", eTimerType.DELETE)", nd.ex1a, FindFuncName(nd.ex1b, ParseDomain, ParseX, ParseY));
                break;

            case 200:
            case 201:
            case 202:
            case 203:
            case 204:
            case 205:
            case 206:
            case 207:
            case 208:
            case 209:
                string field = "";
                switch (nd.type)
                {
                case 200: field = "FIRE_WALL"; break;
                case 201: field = "FORCE_WALL"; break;
                case 202: field = "ICE_WALL"; break;
                case 203: field = "BLADE_WALL"; break;
                case 204: field = "STINK_CLOUD"; break;
                case 205: field = "SLEEP_CLOUD"; break;
                case 206: field = "QUICKFIRE"; break;
                case 207: field = "FIRE_BARRIER"; break;
                case 208: field = "FORCE_BARRIER"; break;
                //case 209: field = "DISPEL"; break;
                }

                if ((nd.ex2a == -1 && nd.ex2b == -1) || (nd.ex2a == nd.ex1a && nd.ex2b == nd.ex1b))
                {
                    if (nd.type != 209)
                    {
                        if (nd.sd1 < 100)
                        {
                            WriteScript("if Maths.Rand(1,0,100) <= {0}:", nd.sd1);
                            WriteScript("    Town.PlaceField(Location({0},{1}), Field.{2})", nd.ex1b, nd.ex1a, field);
                        }
                        else
                            WriteScript("Town.PlaceField(Location({0},{1}), Field.{2})", nd.ex1b, nd.ex1a, field);
                    }
                    else
                        WriteScript("Town.DispelFields(Location({0},{1}), {2})", nd.ex1b, nd.ex1a, nd.sd1 == 0 ? 1 : 2);
                }
                else
                {
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);


                    if (nd.type != 209)
                    {
                        if (nd.sd1 < 100)
                        {
                            WriteScript("        if Maths.Rand(1,0,100) <= {0}:", nd.sd1);
                            WriteScript("            Town.PlaceField(Location(x,y), Field.{0})", field);
                        }
                        else
                            WriteScript("        Town.PlaceField(Location(x,y), Field.{0})", field);
                    }
                    else
                        WriteScript("        Town.DispelFields(Location(x,y), {0})", nd.sd1 == 0 ? 1 : 2);
                }
                break;
            case 210: //Place sfx
                string[] fields = { "SMALL_BLOOD", "MEDIUM_BLOOD", "LARGE_BLOOD", "SMALL_SLIME", "LARGE_SLIME", "CRATER", "BONES", "ROCKS" };
                field = nd.sd2 >= 0 && nd.sd2 < fields.Length ? fields[nd.sd2] : fields[0];

                if (nd.ex2a == -1 || nd.ex2b == -1 || (nd.ex2a == nd.ex1a && nd.ex2b == nd.ex1b))
                {
                    WriteScript("if Maths.Rand(1,0,100) <= {0}:", nd.sd1);
                    WriteScript("    Town.PlaceField(Location({0},{1}), Field.{2})", nd.ex1b, nd.ex1a, field);
                }
                else
                {
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        if Maths.Rand(1,0,100) <= {0}:", nd.sd1);
                    WriteScript("            Town.PlaceField(Location(x,y), Field.{0})", field);
                }
                break;

            case 211: //Place barrels etc
                fields = new string[] { "WEB", "BARREL", "CRATE" };
                field = nd.sd2 >= 0 && nd.sd2 < fields.Length ? fields[nd.sd2] : fields[0];

                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("if Maths.Rand(1,0,100) <= {0}:", nd.sd1);
                    WriteScript("    Town.PlaceField(Location({0},{1}), Field.{2})", nd.ex1b, nd.ex1a, field);
                }
                else
                {
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        if Maths.Rand(1,0,100) <= {0}:", nd.sd1);
                    WriteScript("            Town.PlaceField(Location(x,y), Field.{0}):", field);
                }
                break;
            case 212: //Move items

                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("for i in Town.EachItemThere({0},{1}):", nd.ex1b, nd.ex1a);
                    WriteScript("    Town.PlaceItem(i, Location({0},{1}))", nd.sd1, nd.sd2);
                }
                else
                {
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        for i in Town.EachItemThere(x,y):");
                    WriteScript("            Town.PlaceItem(i, Location({0},{1}))", nd.sd1, nd.sd2);
                }
                break;

            case 213: //Destroy items
                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("for i in Town.EachItemThere({0},{1}):", nd.ex1b, nd.ex1a);
                    WriteScript("    Town.ItemList.Remove(i)");
                }
                else
                {
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        for i in Town.EachItemThere(x,y,True):");
                    WriteScript("            Town.ItemList.Remove(i)");
                }
                break;

            case 214: //Change rectangle terrain
                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("if Maths.Rand(1,0,100) <= {0}:", nd.sd2);
                    WriteScript("    Town.AlterTerrain(Location({0},{0}), 0, TerrainRecord.UnderlayList[{0}])", nd.ex1b, nd.ex1a, nd.sd1);
                }
                else
                {
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        if Maths.Rand(1,0,100) <= {0}:", nd.sd2);
                    WriteScript("            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[{0}])", nd.sd1);
                }
                break;

            case 215://Swap rectangle terrain
                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("if Town.TerrainAt(Location({0},{1})) == TerrainRecord.UnderlayList[{2}]:", nd.ex1b, nd.ex1a, nd.sd1);
                    WriteScript("    Town.AlterTerrain(Location({0},{1}), 0, TerrainRecord.UnderlayList[{2}])", nd.ex1b, nd.ex1a, nd.sd2);
                    WriteScript("elif Town.TerrainAt(Location({0},{1})) == TerrainRecord.UnderlayList[{2}]:", nd.ex1b, nd.ex1a, nd.sd2);
                    WriteScript("    Town.AlterTerrain(Location({0},{1}), 0, TerrainRecord.UnderlayList[{2}])", nd.ex1b, nd.ex1a, nd.sd1);
                }
                else
                {
                    WriteScript("SuspendMapUpdate()");
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[{0}]:", nd.sd1);
                    WriteScript("            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[{0}])", nd.sd2);
                    WriteScript("        elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[{0}]:", nd.sd2);
                    WriteScript("            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[{0}])", nd.sd1);
                    WriteScript("ResumeMapUpdate()");
                }
                break;
            case 216://Transform rectangle terrain
                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("t = Town.TerrainAt(Location({0},{1})).TransformTo", nd.ex1a, nd.ex1b);
                    WriteScript("Town.AlterTerrain(Location({0},{1}), 0, t)", nd.ex1a, nd.ex1b);
                }
                else
                {
                    WriteScript("SuspendMapUpdate()");
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        t = Town.TerrainAt(Location(x,y)).TransformTo");
                    WriteScript("        Town.AlterTerrain(Location(x,y), 0, t)");
                    WriteScript("ResumeMapUpdate()");
                }
                break;
            case 217://Lock rectangle
                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("t = Town.TerrainAt(Location({0},{1}))", nd.ex1a, nd.ex1b);
                    WriteScript("t = t.GetLocked()");
                    WriteScript("Town.AlterTerrain(Location({0},{1}), 0, t)", nd.ex1a, nd.ex1b);
                }
                else
                {
                    WriteScript("SuspendMapUpdate()");
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        t = Town.TerrainAt(Location(x,y))");
                    WriteScript("        t = t.GetLocked()");
                    WriteScript("        Town.AlterTerrain(Location(x,y), 0, t)");
                    WriteScript("ResumeMapUpdate()");
                }
                break;
            case 218://Unlock rectangle
                if (nd.ex2a == -1 && nd.ex2b == -1)
                {
                    WriteScript("t = Town.TerrainAt(Location({0},{1}))", nd.ex1a, nd.ex1b);
                    WriteScript("t = t.GetUnlocked()");
                    WriteScript("Town.AlterTerrain(Location({0},{1}), 0, t)", nd.ex1a, nd.ex1b);
                }
                else
                {
                    WriteScript("SuspendMapUpdate()");
                    WriteScript("for x in range({0}, {1}):", nd.ex1b, nd.ex2b == -1 ? nd.ex1b + 1 : nd.ex2b + 1);
                    WriteScript("    for y in range({0}, {1}):", nd.ex1a, nd.ex2a == -1 ? nd.ex1a + 1 : nd.ex2a + 1);
                    WriteScript("        t = Town.TerrainAt(Location(x,y))");
                    WriteScript("        t = t.GetUnlocked()");
                    WriteScript("        Town.AlterTerrain(Location(x,y), 0, t)");
                    WriteScript("ResumeMapUpdate()");
                }
                break;

            case 225: //Make outdoor wandering
                WriteScript("WorldMap.SpawnWanderingGroup()");
                break;

            case 226: //Change out terrain
                WriteScript("WorldMap.AlterTerrain(Location({0},{1}), 0, TerrainRecord.UnderlayList[{2}])", ParseX * 48 + nd.ex1a, ParseY * 48 + nd.ex1b, nd.ex2a);
                break;

            case 228: //Outdoor move party

                WriteScript("Party.Reposition(Location({0}, {1}))", ParseX * 48 + nd.ex1a, ParseY * 48 + nd.ex1b);
                WriteScript("p.CancelAction = True");
                break;

            case 229: //Outdoor Store
                switch (nd.ex1b)
                {
                    case 0: //Item store
                        WriteScript("OpenShop(\"Shop_Items_Outside_{0}_{1}_{2}\")", node_num, ParseX, ParseY);
                        break;
                    case 1:
                        WriteScript("OpenShop(\"Shop_Mage_Outside_{0}_{1}_{2}\")", node_num, ParseX, ParseY);
                        break;
                    case 2:
                        WriteScript("OpenShop(\"Shop_Priest_Outside_{0}_{1}_{2}\")", node_num, ParseX, ParseY);
                        break;
                    case 3:
                        WriteScript("OpenShop(\"Shop_Alchemy_Outside_{0}_{1}_{2}\")", node_num, ParseX, ParseY);
                        break;
                    case 4:
                        WriteScript("OpenHealingShop({0})", nd.ex2b);
                        break;
                }
                WriteScript("p.CancelAction = True");
                break;

            }
            return nd.jumpto;
        }

        static bool ValidButtonLabel(int b)
        {
            return b >= 0 && b < ButtonLabel.Length;
        }

        static int GetDialogPic(int picnum, int pictype,  out string pic)
        {
            //pictype: 0=Dialog 1=Terrain 2=Monster

            if (picnum < 400) //Terrain
            {
                pic = "eDialogPic.TERRAIN";
            }
            else if (picnum < 700) //Creature
            {
                picnum -= 400;
                if (m_pic_index_x[picnum] == 1 && m_pic_index_y[picnum] == 1) pic = "eDialogPic.CREATURE";
                else if (m_pic_index_x[picnum] == 2 && m_pic_index_y[picnum] == 1) pic = "eDialogPic.CREATURE2x1";
                else if (m_pic_index_x[picnum] == 1 && m_pic_index_y[picnum] == 2) pic = "eDialogPic.CREATURE1x2";
                else pic = "eDialogPic.CREATURE2x2";
                picnum = GetMonsterPicNum(picnum);
            }
            else if (picnum < 1000)
            {
                picnum -= 700;
                pic = "eDialogPic.STANDARD";
            }
            else //Custom
            {
                if (pictype == 0) //Dialog
                {
                    pic = "eDialogPic.STANDARD";
                    picnum = UpdateCustomList(CustomDialogPicList, picnum - 1000);
                }
                else if (pictype == 1) //Terrain
                {
                    pic = "eDialogPic.TERRAIN";
                    picnum = UpdateCustomList(CustomTerrainList, picnum - 1000);
                }
                else 
                {
                    pic = "eDialogPic.CREATURE"; 
                    picnum = UpdateCustomList(CustomNPC1x1List, picnum - 1000);
                }
            }
            return picnum;
        }

        static bool WriteEraseDotsScript(short sd1, short sd2, int indent)
        {
            //Go through all special triggers on all maps. If the first node in the chain the trigger sets off has it's sd1 and sd2 properties the same as
            //the 'nd' parameter, write script to deactivate this trigger
            //Need to check if this script was called from stepping on a terrain with a dot, and then put in a script line to erase that
            //dot on the map. IN ALL maps, both towns and outside.

            bool wrotesomething = false;
            string indentstr = "";
            while (indent-- > 0) indentstr += " ";

            int ct = CurrentlyLoadedTown, ctx = CurrentlyLoadedOutX, cty = CurrentlyLoadedOutY;

            //First towns
            for (int m = 0; m < Scenario.num_towns; m++)
            {
                LoadTown(m);
                for (int n = 0; n < 50; n++)
                {
                    if (Town.special_locs[n].x != 100)
                    {
                        var nd2 = Town.specials[Town.spec_id[n]];
                        if (nd2.sd1 == sd1 && nd2.sd2 == sd2)
                        {
                            //If terrain at this special_loc is a dot, write script line to remove it.
                            int wd = 0;
                            if (Scenario.town_size[m] == 0) wd = 64;//Big
                            else if (Scenario.town_size[m] == 1) wd = 48; //Average
                            else if (Scenario.town_size[m] == 2) wd = 32; //Small
                            int t = Town.special_locs[n].x * wd + Town.special_locs[n].y;
                            int changeto = -1;
                            switch (Scenario.ter_types[TownTerrain.terrain[t]].picture)// >= 207 && TownTerrain.terrain[t] <= 212)
                            {
                                case 207: changeto = 0; break;
                                case 208: changeto = 170; break;
                                case 209: changeto = 210; break;
                                case 210: changeto = 217; break;
                                case 211: changeto = 2; break;
                                case 212: changeto = 36; break;
                            }
                            if (changeto != -1)
                                WriteScript("{3}TownMap.List[\"{0}\"].AlterTerrain(Location({1},{2}), 1, None)", Town_IDs[m], Town.special_locs[n].x, Town.special_locs[n].y, indentstr);//TerrainRecord.List[{3}])", m, Town.special_locs[n].x, Town.special_locs[n].y, changeto);
                            WriteScript("{3}TownMap.List[\"{0}\"].DeactivateTrigger(Location({1},{2}))", Town_IDs[m], Town.special_locs[n].x, Town.special_locs[n].y, indentstr);
                            wrotesomething = true;
                        }
                    }
                }
            }

            //Now outdoors
            for (int sx = 0; sx < Scenario.out_width; sx++)
                for (int sy = 0; sy < Scenario.out_height; sy++)
                {
                    LoadOutdoors(sx, sy);

                    for (int n = 0; n < 18; n++)
                    {
                        if (Outdoors.special_locs[n].x != 100)
                        {
                            var nd2 = Outdoors.specials[Outdoors.special_id[n]];
                            if (nd2.sd1 == sd1 && nd2.sd2 == sd2)
                            {
                                int t = Outdoors.special_locs[n].x * 48 + Outdoors.special_locs[n].y;
                                int changeto = -1;
                                switch (Scenario.ter_types[Outdoors.terrain[t]].picture)// >= 207 && TownTerrain.terrain[t] <= 212)
                                {
                                    case 207: changeto = 0; break;
                                    case 208: changeto = 170; break;
                                    case 209: changeto = 210; break;
                                    case 210: changeto = 217; break;
                                    case 211: changeto = 2; break;
                                    case 212: changeto = 36; break;
                                }
                                if (changeto != -1)
                                    WriteScript("{2}WorldMap.AlterTerrain(Location({0},{1}), 1, None)"/*TerrainRecord.List[{2}])"*/, sx * 48 + Outdoors.special_locs[n].x, sy * 48 + Outdoors.special_locs[n].y, indentstr);//, changeto);
                                WriteScript("{2}WorldMap.DeactivateTrigger(Location({0},{1}))"/*TerrainRecord.List[{2}])"*/, sx * 48 + Outdoors.special_locs[n].x, sy * 48 + Outdoors.special_locs[n].y, indentstr);//, changeto);
                                wrotesomething = true;
                            }
                        }
                    }
                }

            //Get back original town and outdoors
            LoadTown(ct);
            LoadOutdoors(ctx, cty);
            return wrotesomething;
        }


        static void ParseBranch(int nextnode, int domain, int x, int y = 0)
        {
            indent += 4;

            if (!IsValidNodeNumber(nextnode, domain))
            {
                WriteScript("return");
                indent -= 4;
                return;
            }

            int nodesvisitedupto = NodesVisited.Count;
            bool backup_s_pc_s = specific_pc_selected;

            do
            {
                nextnode = ParseNode(nextnode, domain, x, y);
            }
            while (IsValidNodeNumber(nextnode, domain));

            WriteScript("return");
            indent -= 4;
            specific_pc_selected = backup_s_pc_s;

            if (NodesVisited.Count > nodesvisitedupto)
                NodesVisited.RemoveRange(nodesvisitedupto, NodesVisited.Count - nodesvisitedupto);
        }

        static short GetVehicleIndex(bool horse, int no)
        {
            short ind = -1;
            //ex1a is the horse or boat to change
            for (int y = 0; y < 30; y++)
            {
                if (Scenario.scen_horses[y].which_town != -1)
                {
                    ind++;
                    if (horse && no == y) return ind; //spcs[x].ex1a = i;
                }
            }
            for (int y = 0; y < 30; y++)
            {
                if (Scenario.scen_boats[y].which_town != -1)
                {
                    ind++;
                    if (!horse && no == y) return ind;
                }
            }
            return -1;
        }


        static string GetStandardMessage(special_node_type nd, int domain)
        {
            string m1="", m2="";

            if (nd.m1 != -1 || nd.m2 != -1)
            {
                m1 = GetString(nd.m1, domain);
                m2 = GetString(nd.m2, domain);

                if (nd.m1 == -1)
                    return m2;
                else if (nd.m2 == -1)
                    return m1;
                else
                    return m1 + "\\n\\n" + m2;
            }
            else return null;
        }

        static void WriteScript(String s, params object[] args)
        {
            s = String.Format(s,args);
            ScriptFile.WriteLine(s.PadLeft(s.Length + indent));
        }

        static string GetString(int n, int domain, bool not_a_script_string = false)
        {
            string s = ""; ;
            //Assumes the correct town/outdoors is loaded!
            if (n == -1) return s;
            if (domain == 0)
            {
                if (n > 1000)
                {
                    //This is a kludge for the 'Input Text' special node, which uses any scenario text string, not just the ones reserved for global specials
                    //Also for Intro_Message function script
                    n -= 1000;
                    if (n < 160)
                        s = DataStore5.scen_strs[n];
                    else
                        s = scen_strs_2[n - 160];
                }
                else
                    s = scen_strs_2[n];
            }
            else if (domain == 1) 
                s = DataStore1.town_strs[n + 20];
            else 
                s = DataStore4.outdoor_text[n + 10];

            return FixYeah(s, !not_a_script_string);
        }

        public static string FixYeah(string s, bool in_python_script)
        {
            if (in_python_script)
            {
                s = s.Replace(@"\", @"\\"); //   \ -> \\
                s = s.Replace("@", "@@");   //   @ -> @@
                s = s.Replace("\"", "\\\"");//   " -> \"
                s = s.Replace("'", "\\'");  //   ' -> \'
                s = s.Replace("|", "\\n");  //   | -> \n
                s = s.Replace("\r", "\\n"); //   [carriage return] -> \n
            }
            else
            {
                s = s.Replace("@", "@@");
                s = s.Replace("|", "\n");
            }
            return s;
        }

        static string GetDamageTypeString(int n)
        {
            switch (n)
            {
            case 1: return "eDamageType.FIRE"; 
            case 2: return "eDamageType.POISON"; 
            case 3: return "eDamageType.MAGIC";
            case 4: return "eDamageType.UNBLOCKABLE";
            case 5: return "eDamageType.COLD"; 
            case 6: return "eDamageType.UNDEAD"; 
            case 7: return "eDamageType.DEMON"; 
            default: return "eDamageType.WEAPON"; 
            }
        }

        static string[] ButtonLabel = {"Done ","OK", "Yes", "No", "Ask","Keep", "Cancel","Buy","Enter", "Leave",
						"Get","1","2","3","4","5","6","Cast","Save", "Take", "Leave", "Steal","Attack",
                        "Step In","Climb",
						"Flee","Onward","Answer","Drink","Approach","Land",
						"Under","Quit","Rest","Read","Pull","Push","Pray","Wait","Give",
				/*100*/		"Destroy","Pay","Free","Touch", "Burn","Insert","Remove","Accept","Refuse","Open","Close","Sit","Stand"};

        static string FindFuncName(int ndno, int domain, int x, int y)
        {
            foreach (ScriptEntryPoint ep in EntryPoints)
            {
                if (ep.Domain == domain && ep.X == x && ep.Y == y && ndno == ep.Node) return ep.FuncName;
            }

            foreach (ScriptEntryPoint ep in LoopbackEntryPoints)
            {
                if (ep.Domain == domain && ep.X == x && ep.Y == y && ndno == ep.Node) return ep.FuncName;
            }
            return "_UNKNOWN_";
        }

        static List<string> SpecialItemList = new List<string>();
        static void GetSpecialItems()
        {
            for (int n = 0; n < 50; n++)
            {
                string s = GetFriendlyIDString(DataStore5.scen_strs[n * 2 + 60]);

                if (SpecialItemList.Contains(s))
                {
                    s = s + "_" + n;
                }
                SpecialItemList.Add(s);
            }
        }

        static string GetItemID(int n)
        {
            if (n == -1) return "";
            if (n == 0) return "gold";
            string m = Encoding.ASCII.GetString(ScenItems.scen_items[n].full_name);
            m = m.Remove(m.IndexOf((char)0));
            return String.Format("{0}_{1}", GetFriendlyIDString(m), n);
        }

        static string GetNPCID(int n)
        {
            if (n == -1) return "";
            string m = Encoding.ASCII.GetString(ScenItems.monst_names, n * 20, 20);
            m = m.Remove(m.IndexOf((char)0));
            return String.Format("{0}_{1}", GetFriendlyIDString(m), n);
        }

        static string GetTerrainID(int n)
        {
            string m = Encoding.ASCII.GetString(ScenItems.ter_names, n * 30, 30);
            m = m.Remove(m.IndexOf((char)0));
            return String.Format("{0}_{1}", GetFriendlyIDString(m), n);
        }

        static string GetSoundID(int n)
        {
            string[] sounds = { "000_highbeep",
                    "001_lowbeep",
                    "002_swordswish",
                    "003_cough",
                    "004_bless",
                    "005_explosion",
                    "006_eating",
                    "007_cool",
                    "008_bubbles",
                    "009_lockpick",
                    "010_teleport",
                    "011_3booms",
                    "012_longbow",
                    "013_partydeath",
                    "014_missile",
                    "015_cash",
                    "016_townentry",
                    "017_shortcough",
                    "018_drawingsword",
                    "019_swordswish",
                    "020_yawn",
                    "021_pcdying",
                    "022_openingmusic",
                    "023_startoutdoorcombat",
                    "024_priestspell",
                    "025_magespell",
                    "026_gremlin",
                    "027_monsterdeath1",
                    "028_waterfall",
                    "029_monsterdeath2",
                    "030_monsterdeath3",
                    "031_monsterdeath4",
                    "032_gethit1",
                    "033_gethit2",
                    "034_button1",
                    "035_spiderhi",
                    "036_spiderhello",
                    "037_button2",
                    "038_coinsoncounter",
                    "039_coinsjingle",
                    "040_thankyou",
                    "041_darn",
                    "042_dang",
                    "043_stoning",
                    "044_breathe",
                    "045_onwho",
                    "046_growl",
                    "047_walkgravel",
                    "048_boatmove",
                    "049_step1",
                    "050_step2",
                    "051_magic1",
                    "052_magic2",
                    "053_magic3",
                    "054_scream",
                    "055_walksquish",
                    "056_swallow",
                    "057_specialnoise",
                    "058_opendoor",
                    "059_closedoor",
                    "060_smallboom",
                    "061_summoning",
                    "062_mmm",
                    "063_ow",
                    "064_spit",
                    "065_draining",
                    "066_disease",
                    "067_huh",
                    "068_identify",
                    "069_sword1",
                    "070_sword2",
                    "071_sword3",
                    "072_club",
                    "073_fireimpact",
                    "074_fireball",
                    "075_cold",
                    "076_chirp1",
                    "077_chirp2",
                    "078_drip1",
                    "079_drip2",
                    "080_bark",
                    "081_meow",
                    "082_baa",
                    "083_moo",
                    "084_neigh",
                    "085_gallop",
                    "086_claw",
                    "087_bite",
                    "088_slime",
                    "089_zap",
                    "090_paralyze",
                    "091_chirp3",
                    "092_chicken",
                    "093_sheathe",
                    "094_lever",
                    "095_enterdungeon",
                    "096_sleep",
                    "097_damageuh",
                    "098_missilehit",
                    "099_nuttin"};
            if (n < 0 || n > 99) return "";
            else return sounds[n];
        }

        static string GetSpecialItemName(int no)
        {
            if (no < 0 || no >= 50) return "UNKNOWN";
            string s = SpecialItemList[no];

            return s;
        }

        static string GetNodeToFuncName(int nd, int d, int x, int y, bool sanctify_only=false)
        {
            foreach (ScriptEntryPoint e in EntryPoints)
            {
                if (nd == e.Node && d == e.Domain && x == e.X && y == e.Y)

                    if ((e.Trigger == eTrigger.SANCTIFICATION && sanctify_only) || (e.Trigger != eTrigger.SANCTIFICATION && !sanctify_only))
                        return e.FuncName;
            }
            return "";
        }

        static void AddToEntryPoints(int nd, int d, int x, int y, string s, eTrigger what, bool no_duplicate_check = false)
        {
            if (!IsValidNodeNumber(nd, d)) return;

            if (!no_duplicate_check)
                if (EntryPoints.FindIndex(n => n.Node == nd && n.Domain == d && n.X == x && n.Y == y) != -1 ||
                    LoopbackEntryPoints.FindIndex(n => n.Node == nd && n.Domain == d && n.X == x && n.Y == y) != -1)
                    return;

            ScriptEntryPoint ep = new ScriptEntryPoint { Node = nd, Domain = d, X = x, Y = y, Trigger = what };
            ep.FuncName = s;

            if (!WritingScript)
                EntryPoints.Add(ep);
            else
                LoopbackEntryPoints.Add(ep);
        }

        static string DirToString(int dir)
        {
            if (dir == 0) return "North";
            if (dir == 1) return "West";
            if (dir == 2) return "South";
            return "East";
        }

        static string GetFriendlyIDString(string s)
        {
            var sb = new StringBuilder();
            if (s.Length == 0 || !char.IsLetter(s[0])) sb.Append("_");
            foreach (char c in s)
            {
                if (char.IsLetterOrDigit(c)) sb.Append(c);
            }
            return sb.ToString();
        }

        public static void GetScriptEntryPoints()
        {
            int count=0;

            //---------------------------------------------- TOWNS ----------------------------------------------
            for (int t = 0; t < Scenario.num_towns; t++)
            {
                LoadTown(t);

                string functownname = GetFriendlyIDString(DataStore1.town_strs[0]); 

                //Find all the possible entry points for special node chains in this town. So we can convert them to script functions.

                //Map specials
                for (int n = 0; n < Town.spec_id.Length; n++)
                    if (Town.special_locs[n].x != 100)
                    {
                        if (Town.specials[Town.spec_id[n]].type == 24) //Ritual of sanctification block!
                        {
                            if (Town.specials[Town.spec_id[n]].jumpto != -1)
                                AddToEntryPoints(Town.specials[Town.spec_id[n]].jumpto, 1, t, 0, String.Format("{0}_{1}_SanctifyTrigger_{2}_{3}", functownname, count++, Town.special_locs[n].x, Town.special_locs[n].y), eTrigger.SANCTIFICATION);
                            if (Town.specials[Town.spec_id[n]].ex1b != -1)
                                AddToEntryPoints(Town.specials[Town.spec_id[n]].ex1b, 1, t, 0, String.Format("{0}_{1}_MapTrigger_{2}_{3}", functownname, count++, Town.special_locs[n].x, Town.special_locs[n].y), eTrigger.MAPTRIGGER);
                        }
                        else if (!(Town.specials[Town.spec_id[n]].type == 4 && Town.specials[Town.spec_id[n]].jumpto == -1))
                            AddToEntryPoints(Town.spec_id[n], 1, t, 0, String.Format("{0}_{1}_MapTrigger_{2}_{3}", functownname, count++, Town.special_locs[n].x, Town.special_locs[n].y), eTrigger.MAPTRIGGER);
                    }

                //Town timers (Saved with the town, not created by node type 195
                for (int n = 0; n < Town.timer_specs.Length; n++)
                    if (Town.timer_spec_times[n] > 0)
                        AddToEntryPoints(Town.timer_specs[n], 1, t, 0, String.Format("{0}_{1}_TownTimer_{2}", functownname, count++, n), eTrigger.GENERAL);

                //Town timers (Created by node type 195) - not recurring, and deleted when the party leaves town.
                for (int n = 0; n < Town.specials.Length; n++)
                {
                    if (Town.specials[n].type == 195 && Town.specials[n].ex1a > 0)
                    {
                        AddToEntryPoints(Town.specials[n].ex1b, 1, t, 0, String.Format("{0}_{1}_TownTimer_{2}", functownname, count++, n), eTrigger.GENERAL);
                    }
                }

                //Town entry
                if (IsValidNodeNumber(Town.spec_on_entry, 1) || IsValidNodeNumber(Town.spec_on_entry_if_dead,1))
                    AddToEntryPoints(0, 1, t, 777, String.Format("{0}_{1}_OnEntry", functownname, count++), eTrigger.TOWNENTRY);//Town.spec_on_entry, 1, t, 0, String.Format("{0}_{1}_OnEntry", functownname, count++),eTrigger.GENERAL);

                if (!LEGACY_NO_TOWN_ANGRY_FUNC)
                {
                    if (Town.res1 >= 0)
                        AddToEntryPoints(Town.res1, 1, t, 0, String.Format("{0}_{1}_OnTownTurnsHostile", functownname, count++), eTrigger.GENERAL);
                }

                //Town exits
                for (int n = 0; n < Town.exit_specs.Length; n++)
                {
                    if (IsValidNodeNumber(Town.exit_specs[n], 1) || Town.exit_locs[n].x != -1)
                    {
                        AddToEntryPoints(0, 1, t, 888, functownname + "_" + (count++) + "_ExitTown", eTrigger.TOWNEXIT);
                        break;
                    }
                }


                for (int n = 0; n < TownTerrain.creatures.Length; n++)
                    if (TownTerrain.creatures[n].number > 0 && TownTerrain.creatures[n].special_on_kill >= 0)
                        AddToEntryPoints(TownTerrain.creatures[n].special_on_kill, 1, t, 0, String.Format("{0}_{1}_CreatureDeath{2}", functownname, count++, n),eTrigger.NPCDEATH);

                //Talking nodes
                for (int n = 0; n < Talking.talk_nodes.Length; n++)
                    if (Talking.talk_nodes[n].type == 29 && Talking.talk_nodes[n].extras[0] >= 0)
                    { //Calls town special node
                        if ((Talking.talk_nodes[n].personality >= t * 10 && Talking.talk_nodes[n].personality < t * 10 + 10) || Talking.talk_nodes[n].personality == -2)
                            AddToEntryPoints(Talking.talk_nodes[n].extras[0], 1, t, 0, String.Format("{0}_{1}_TalkingTrigger{2}", functownname, count++, n), eTrigger.TALKING);
                    }
                    else if (Talking.talk_nodes[n].type == 30 && Talking.talk_nodes[n].extras[0] >= 0 && Talking.talk_nodes[n].personality != -1)
                    { //Calls global special node
                        AddToEntryPoints(Talking.talk_nodes[n].extras[0], 0, 0, 0, String.Format("{0}_{1}_GlobalTalkingTrigger_{2}", functownname, count++, n), eTrigger.TALKING);
                    }

                for (int n = 0; n < Town.specials.Length; n++)
                    if (Town.specials[n].type == 195 && Town.specials[n].ex1b >= 0)
                        AddToEntryPoints(Town.specials[n].ex1b, 1, t, 0, String.Format("{0}_{1}_NewTownTimerFrom{2}", functownname, count++, n), eTrigger.GENERAL);

            }

            //Check for a town that has a 'Stairway' or 'Generic Stairway' special node. When the player triggers that node, they will move to a new town and trigger
            //a special node in that new town.
            for (int t = 0; t < Scenario.num_towns; t++)
            {
                LoadTown(t);

                for (int n = 0; n < Town.specials.Length; n++)
                {
                    if (Town.specials[n].type == 187 || Town.specials[n].type == 190) //Generic stairway or stairway
                    {
                        if (Town.specials[n].ex2a >= 0 && Town.specials[n].ex2a < Scenario.num_towns && IsValidNodeNumber(Town.specials[n].jumpto, 1))

                        {
                            LoadTown(Town.specials[n].ex2a);
                            string functownname = GetFriendlyIDString(DataStore1.town_strs[0]);
                            LoadTown(t);
                            AddToEntryPoints(Town.specials[n].jumpto, 1, Town.specials[n].ex2a, 0, String.Format("{0}_{1}_StairwayDestination{2}", functownname, count++, Town.specials[n].jumpto), eTrigger.GENERAL);
                        }
                    }
                }

            }

            //---------------------------------------------- OUTSIDE AREAS ---------------------------------------------- 
            for (int y = 0; y < Scenario.out_height; y++)
            {
                for (int x = 0; x < Scenario.out_width; x++)
                {
                    LoadOutdoors(x, y);

                    string outdoorsid = GetFriendlyIDString(DataStore4.outdoor_text[0]);

                    for (int n = 0; n < Outdoors.special_id.Length; n++)
                        if (Outdoors.special_locs[n].x != 100)
                            if (!(Outdoors.specials[Outdoors.special_id[n]].type == 4 && Outdoors.specials[Outdoors.special_id[n]].jumpto == -1))
                                AddToEntryPoints(Outdoors.special_id[n], 2, x, y, String.Format("{0}_{1}_MapTrigger_{2}_{3}", outdoorsid, count++, Outdoors.special_locs[n].x, Outdoors.special_locs[n].y), eTrigger.MAPTRIGGER);

                    for (int n = 0; n < Outdoors.wandering.Length; n++)
                    {
                        bool notempty = false;
                        foreach (byte b in Outdoors.wandering[n].monst)
                            if (b > 0) notempty = true;
                        if (notempty)
                        {
                            if (Outdoors.wandering[n].spec_on_meet >= 0)
                                AddToEntryPoints(Outdoors.wandering[n].spec_on_meet, 2, x, y, String.Format("{0}_{1}_WanderingOnMeet{2}", outdoorsid, count++, n), eTrigger.OUTDOOR_ENCOUNTER);
                            if (Outdoors.wandering[n].spec_on_win >= 0)
                                AddToEntryPoints(Outdoors.wandering[n].spec_on_win, 2, x, y, String.Format("{0}_{1}_WanderingOnWin{2}", outdoorsid, count++, n), eTrigger.OUTDOOR_ENCOUNTER);
                            if (Outdoors.wandering[n].spec_on_flee >= 0)
                                AddToEntryPoints(Outdoors.wandering[n].spec_on_flee, 2, x, y, String.Format("{0}_{1}_WanderingOnFlee{2}", outdoorsid, count++, n), eTrigger.OUTDOOR_ENCOUNTER);
                        }
                    }
                    for (int n = 0; n < Outdoors.special_enc.Length; n++)
                    {
                        bool notempty = false;
                        foreach (byte b in Outdoors.special_enc[n].monst)
                            if (b > 0) notempty = true;
                        if (notempty)
                        {
                            if (Outdoors.special_enc[n].spec_on_meet >= 0)
                                AddToEntryPoints(Outdoors.special_enc[n].spec_on_meet, 2, x, y, String.Format("{0}_{1}_SpecialOnMeet{2}", outdoorsid, count++, n), eTrigger.OUTDOOR_ENCOUNTER);
                            if (Outdoors.special_enc[n].spec_on_win >= 0)
                                AddToEntryPoints(Outdoors.special_enc[n].spec_on_win, 2, x, y, String.Format("{0}_{1}_SpecialOnWin{2}", outdoorsid, count++, n), eTrigger.OUTDOOR_ENCOUNTER);
                            if (Outdoors.special_enc[n].spec_on_flee >= 0)
                                AddToEntryPoints(Outdoors.special_enc[n].spec_on_flee, 2, x, y, String.Format("{0}_{1}_SpecialOnFlee{2}", outdoorsid, count++, n), eTrigger.OUTDOOR_ENCOUNTER);
                        }
                    }

                }
            }

            //-----------------------------------------------GLOBAL SCRIPTS-----------------------------------------------------------------
            //On using a special item
            for (int n = 0; n < Scenario.special_item_special.Length; n++)
                if (Scenario.special_item_special[n] >= 0)
                    AddToEntryPoints(Scenario.special_item_special[n], 0, 0, 0, String.Format("On_Using_SI_{0}_{1}", GetSpecialItemName(n), count++), eTrigger.USE_SPECIAL_ITEM);

            //On death of an NPC
            for (int n = 0; n < Scenario.scen_monsters.Length; n++)
            {
                monster_record_type mon = Scenario.scen_monsters[n];
                if (mon.radiate_1 == 15)
                {
                    string monname = Encoding.ASCII.GetString(ScenItems.monst_names, n * 20, 20);
                    monname = monname.Remove(monname.IndexOf((char)0));
                    monname = GetFriendlyIDString(monname);
                    AddToEntryPoints(mon.radiate_2, 0, 0, 0, String.Format("On_Death_Of_{0}_{1}",monname, count++), eTrigger.NPCDEATH);
                }
            }

            //Stepping on/using a terrain type
            for (int n = 0; n < Scenario.ter_types.Length; n++)
            {
                terrain_type_type ter = Scenario.ter_types[n];
                string tername = Encoding.ASCII.GetString(ScenItems.ter_names, n * 30, 30);
                tername = tername.Remove(tername.IndexOf((char)0));
                tername = GetFriendlyIDString(tername);

                if (ter.special == 13)
                    AddToEntryPoints(ter.flag1, 0, 0, 0, String.Format("TerrainTypeStepOn_{0}_{1}", tername, count++), eTrigger.TERRAINTRIGGER);
                if (ter.special == 23)
                    AddToEntryPoints(ter.flag1, 0, 0, 0, String.Format("TerrainTypeUse_{0}_{1}", tername, count++), eTrigger.TERRAINTRIGGER);
            }

            //Global timers (not created by special nodes)
            for (int n = 0; n < Scenario.scenario_timer_times.Length; n++)
                if (Scenario.scenario_timer_times[n] > 0 && Scenario.scenario_timer_specs[n] >= 0)
                    AddToEntryPoints(Scenario.scenario_timer_specs[n], 0, 0, 0, String.Format("ScenarioTimer{0}_{1}", n, count++), eTrigger.GENERAL);

            //Global timers (created by special node)
            for (int n = 0; n < Scenario.scen_specials.Length; n++)
                if (Scenario.scen_specials[n].type == 13 && Scenario.scen_specials[n].ex1a > 0)
                    AddToEntryPoints(Scenario.scen_specials[n].ex1b, 0, 0, 0, String.Format("ScenarioTimer_x_{0}", count++), eTrigger.GENERAL);
            
            for (int t = 0; t < Scenario.num_towns; t++)
            {
                LoadTown(t);
                string functownname = GetFriendlyIDString(DataStore1.town_strs[0]);

                for (int n = 0; n < Town.specials.Length; n++)
                {
                    //Town Local node directly calling a global node: node type 21
                    if (Town.specials[n].type == 21 && Town.specials[n].jumpto >= 0)
                        AddToEntryPoints(Town.specials[n].jumpto, 0, 0, 0, String.Format("GlobalCall_{0}_{1}", functownname, count++), eTrigger.GENERAL);

                    //Town local node setting up a global timer
                    if (Town.specials[n].type == 13 && Town.specials[n].ex1a > 0)
                        AddToEntryPoints(Town.specials[n].ex1b, 0, 0, 0, String.Format("ScenarioTimer_x_{0}", count++), eTrigger.GENERAL);
                }
            }

            for (int y = 0; y < Scenario.out_height; y++)
                for (int x = 0; x < Scenario.out_width; x++)
                {
                    LoadOutdoors(x, y);
                    string outdoorsid = GetFriendlyIDString(DataStore4.outdoor_text[0]);

                    for (int n = 0; n < Outdoors.specials.Length; n++)
                    {
                        //Outdoors Local node directly calling a global node
                        if (Outdoors.specials[n].type == 21 && Outdoors.specials[n].jumpto >= 0)
                            AddToEntryPoints(Outdoors.specials[n].jumpto, 0, 0, 0, String.Format("GlobalCall_{0}_{1}", outdoorsid, count++), eTrigger.GENERAL);
                        
                        //Outdoors local node setting up a global timer
                        if (Outdoors.specials[n].type == 13 && Outdoors.specials[n].ex1a > 0)
                            AddToEntryPoints(Outdoors.specials[n].ex1b, 0, 0, 0, String.Format("ScenarioTimer_x_{0}", count++), eTrigger.GENERAL);
                    }
                }

            //A terrain type can trigger a LOCAL special. This could lead to conversion problems as every town/outdoor section might potentially have this terrain and need a local node set up to trigger,
            //and the terrain could change during play by a special node!
            for (int n = 0; n < Scenario.ter_types.Length; n++)
            {
                if (Scenario.ter_types[n].special == 12)
                {
                    string tername = Encoding.ASCII.GetString(ScenItems.ter_names, n * 30, 30);
                    tername = tername.Remove(tername.IndexOf((char)0));
                    tername = GetFriendlyIDString(tername);

                    for (int t = 0; t < Scenario.num_towns; t++)
                        if (theDreadedTerrainTypeCallsLocalSpecialCheckPart1_Towns(n, t))
                        {
                            string functownname = GetFriendlyIDString(DataStore1.town_strs[0]);

                            AddToEntryPoints(Scenario.ter_types[n].flag1, 1, t, 0, String.Format("TerrainTypeStepOn_{0}_{1}_{2}", tername, functownname, count++), eTrigger.TERRAINTRIGGER);
                        }
                    for (int y = 0; y < Scenario.out_height; y++)
                        for (int x = 0; x < Scenario.out_width; x++)
                            if (theDreadedTerrainTypeCallsLocalSpecialCheckPart2_Outdoors(n, x, y))
                            {
                                string outdoorsid = GetFriendlyIDString(DataStore4.outdoor_text[0]);
                                AddToEntryPoints(Scenario.ter_types[n].flag1, 2, x, y, String.Format("TerrainTypeStepOn_{0}_{1}_{2}", tername, outdoorsid, count++), eTrigger.TERRAINTRIGGER);
                            }
                }
            }

        }

        static bool theDreadedTerrainTypeCallsLocalSpecialCheckPart1_Towns(int n, int t)
        {
            terrain_type_type ter = Scenario.ter_types[n];
            LoadTown(t);

            //Does this town's terrain have...
            // - Any squares of this terrain
            // - Any squares that change to this terrain
            // - Any local special nodes that might change a square to this terrain.
            // If so, we should except a script entry.

            int sz;
            if (Scenario.town_size[t] == 0) sz = 64;
            else if (Scenario.town_size[t] == 1) sz = 48;
            else sz = 32;

            for (int y = 0; y < sz; y++)
                for (int x = 0; x < sz; x++)
                {
                    if (TownTerrain.terrain[y * sz + x] == n) return true;

                    terrain_type_type tt = Scenario.ter_types[TownTerrain.terrain[y * sz + x]];
                    if (tt.flag1 == n)
                    {
                        if (tt.special == 1 || //Change when step on
                            tt.special == 7 || //Crumbling terrain (cast priest spell 'shatter' or 'move mountains') (only town)
                            tt.special == 8 || tt.special == 9 || tt.special == 10 || //Lockable/Unlockable/bashable terrain (only town)
                            tt.special == 22) //Change when used (only town)
                            return true;
                    }
                }

            for (int s = 0; s < Town.specials.Length; s++)
            {
                special_node_type nd = Town.specials[s];
                if (nd.type == 171 && nd.ex2a == n) return true; //Change terrain
                if (nd.type == 172 && (nd.ex2a == n || nd.ex2b == n)) return true; //Swap terrain
                if (nd.type == 173 || nd.type == 216 || nd.type == 184 || nd.type == 188) //Transform terrain, Rectangle transform terrain, generic lever, lever
                {
                    for (int q = 0; n < Scenario.ter_types.Length; n++) //Check if any terrain type has our terrain as the 'transform to' property.
                    {
                        if (Scenario.ter_types[q].trans_to_what == n)
                        {
                            return true;
                        }
                    }
                }
                if (nd.type == 214 && nd.sd1 == n) return true; //Rectangle change terrain
                if (nd.type == 215 && (nd.sd1 == n || nd.sd2 == n)) return true;
            }
            return false;
        }

        static bool theDreadedTerrainTypeCallsLocalSpecialCheckPart2_Outdoors(int n, int ox, int oy)
        {
            terrain_type_type ter = Scenario.ter_types[n];
            LoadOutdoors(ox, oy);

            for (int y = 0; y < 48; y++)
                for (int x = 0; x < 48; x++)
                {
                    if (Outdoors.terrain[y * 48 + x] == n) return true;

                    terrain_type_type tt = Scenario.ter_types[Outdoors.terrain[y * 48 + x]];
                    if (tt.flag1 == n)
                    {
                        if (tt.special == 1 || //Change when step on
                            tt.special == 21) //Alternative terrain for Hidden Town entrance (only outside)
                            return true;
                    }
                }

            for (int s = 0; s < Outdoors.specials.Length; s++)
            {
                special_node_type nd = Outdoors.specials[s];
                if (nd.type == 226 && nd.ex2a == n) return true;
            }
            return false;
        }

        static byte[] m_pic_index_x = {

            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,2,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,

            1,2,1,1,1,2,1,1,1,1, // 100
            2,1,1,1,1,1,1,1,2,1,
            1,2,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,2,1,

            2,2,2,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1};

        static byte[] m_pic_index_y = {
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,2,
            2,2,2,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,2,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,

            1,1,1,1,1,1,1,1,1,1,
            1,1,2,2,1,1,1,1,2,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,2,1,
            2,1,1,2,1,1,1,1,1,1,

            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1};


    }
}
