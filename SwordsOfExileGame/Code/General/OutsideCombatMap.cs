using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;


namespace SwordsOfExileGame
{
    public class CombatMap : TownMap
    {
        public static int GenerateWidth, GenerateHeight;
        public static string GenerateFunc;

        PartyType Party { get { return Game.CurrentParty; } }
        public EncounterRecord NPCGroup;

        /// <summary>
        /// Constructor for making a TownMap for the purposes of an outdoor combat encounter.
        /// </summary>
        /// <param name="encounter">The group of NPCs we've encountered here</param>
        /// <param name="underterrain">3x3 array of terrain types The terrain type on the world map the combat map will be based on (mainly the central one)</param>
        /// <param name="overterrain">As above for overlay terrain</param>
        public CombatMap(EncounterRecord encounter, TerrainRecord[,] underterrain, TerrainRecord[,] overterrain)
        {
            //const int COMBAT_MAP_WIDTH = 28, COMBAT_MAP_HEIGHT = 28;

            NPCGroup = encounter;

            Width = GenerateWidth;// COMBAT_MAP_WIDTH;
            Height = GenerateHeight;  //COMBAT_MAP_HEIGHT;
            Boundary = new Rectangle(1, 1, Width - 2, Height - 2);

            _Terrain = new ushort[Width, Height];
            _Explored = new bool[Width, Height];
            Misc = new uint[Width, Height];

            Script.RunGenerateMap(GenerateFunc, this, encounter, underterrain, overterrain);

        //    /////////////////////////////////////////////////////////////////////////////////////////////////////
        //    //////////////////////////////////////////// BASE TERRAIN ///////////////////////////////////////////

        //    //Generate the Combat terrain
        //    int[] general_types =  {1,1,0,0,0,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,2,2,
        //                            2,2,2,2,2,2,2,2,2,2,
        //                            2,2,2,2,2,2,2,2,2,2,
        //                            2,2,2,2,2,2,0,0,0,0,
        //                            0,0,0,0,0,0,0,0,0,0,// 50
        //                            0,3,3,3,3,3,3,5,5,5,
        //                            6,6,7,7,1,1,8,9,10,11,
        //                            11,11,12,13,13,9,9,9,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,// 100
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,// 150
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,0,1,1,1,1,1,1,1,0,
        //                            0,0,0,0,0,0,0,0,0,0,
        //                            0,0,14,15,16,0,0,1,1,1,// 200
        //                            1,0,2,1,1,1,0,1,1,1,
        //                            1,1,0,0,0,0,1,0,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1,
        //                            1,1,1,1,1,1,1,1,1,1};// 250
        //    byte[] ter_base = { 2, 0, 36, 50, 71, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 36 };
        //    int[,] terrain_odds = {
        //                                {3,80, 4,40, 115,20, 114,10, 112,1},    // 0 : Grass
        //                                {1,50,93,25,94,5,98,10,95,1},           // 1 : Cave
        //                                {37,20,0,0,0,0,0,0,0,0},                // 2 : Hills
        //                                {64,3,63,1,0,0,0,0,0,0},                // 3 : Grass Bridge
        //                                {74,1,0,0,0,0,0,0,0,0},                 // 4 : Cave Bridge 
        //                                {84,700,97,30,98,20,92,4,95,1},         // 5 : Rocky Cave
        //                                {93,280,91,300,92,270,95,7,98,10},      // 6 : Woody cave
        //                                {1,800,93,600,94,10,92,10,95,4},        // 7 : Shroomy cave
        //                                {1,700,96,200,95,100,92,10,112,5},      // 8 : Swampy cave
        //                                {3,600,87,90,110,20,114,6,113,2},       // 9 : Rocky grass
        //                                {3,200,4,400,111,250,0,0,0,0},          // 10 : Swampy grass
        //                                {3,200,4,300,112,50,113,60,114,100},    // 11 : Woody grass
        //                                {3,100,4,250,115,120,114,30,112,2},     // 12 : Little woody grass
        //                                {1,25,84,15,98,300,97,280,0,0},         // 13 : Stalagmity cave
        //                                {1,50,93,25,94,5,98,10,95,1},           // 14 : Cave road  *
        //                                {3,80,4,40,115,20,114,10,112,1},        // 15 : Grass road *
        //                                {37,20,0,0,0,0,0,0,0,0}                 // 16 : Hills road *
        //                          }; // ter then odds then ter then odds ...

        //    //Find the right base terrain
        //    int ter_type = underterrain[1,1].picture;
        //    if (ter_type == 401 || ter_type == 402) //Cave bridge
        //        ter_type = 4;
        //    else if (ter_type >= 260)
        //        ter_type = 1;
        //    else ter_type = general_types[ter_type];

            

        //    for (int i = 0; i < Width; i++)
        //        for (int j = 0; j < Height; j++)
        //        {
        //            _Explored[i, j] = false;
        //            Misc[i, j] = 0;
        //            //if ((j <= 8) || (j >= 35) || (i <= 8) || (i >= 35))
        //            //    _Terrain[i, j] = 90;
        //            //else 
        //            _Terrain[i, j] = ter_base[ter_type];
        //        }

        //    for (int i = 0; i < Width; i++)
        //        for (int j = 0; j < Height; j++)
        //            for (int k = 0; k < 5; k++)
        //                if (/*(_Terrain[i, j] != 90) &&*/ Maths.Rand(1, 1, 1000) < terrain_odds[ter_type, k * 2 + 1])
        //                    _Terrain[i, j] = (ushort)terrain_odds[ter_type, k * 2];

        //    ushort base_terrain = ter_base[ter_type];

        //    //_Terrain[0, 0] = ter_base[ter_type];


        //    //WAS 48x48 from 9 to 34 inclusive)   Bridge 11 wide
        //    //NOW 27x27 from 1 to 25 inclusive)   Bridge 27/2.4 wide


        //    /////////////////////////////////////////////////////////////////////////////////////////////////////
        //    //////////////////////////////////////////// BRIDGES/ROADS //////////////////////////////////////////


        //    if (ter_type == 3) //Grass Bridge
        //    {
        //        base_terrain = 83; //Walkway on grass
        //        for (int i = 7; i <= 17; i++) //PIT BORDER:0-8 [9]  Water:9-14 [6]  BRIDGE:15-25 [11]   WATER:26-34 [9]    PIT BORDER: 35-47 [13]   
        //                                      //Edge 0         [1]  Water: 1-6 [6]  BRIDGE:7-17  [11]   WATER:18-26 [9]    EDGE: 27 [1]
        //            for (int j = 0; j < Height; j++)
        //                _Terrain[i, j] = 82;
        //    }

        //    if (ter_type == 4) //Cave bridge
        //    {
        //        base_terrain = 82; //Walkway on cave
        //        for (int i = 7; i <= 17; i++)
        //            for (int j = 0; j < Height; j++)
        //                _Terrain[i, j] = 82;
        //    }


        //    if (overterrain != null && overterrain[1,1].picture >= 260 && overterrain[1,1].picture < 276) //Has a road on the terrain
        //    {
        //        base_terrain = 82;
        //        for (int i = 11; i <= 14; i++)    //PIT: 0-8 [9] Ground: 9-18 [10]   ROAD: 19-22 [4]  GROUND: 23-34 [12]   PIT: 35-47 [13]
        //            for (int j = 0; j < Height; j++)
        //                _Terrain[i, j] = 82;
        //    }

        //    /////////////////////////////////////////////////////////////////////////////////////////////////////
        //    //////////////////////////////////////////// TERRAIN FEATURES ///////////////////////////////////////

        //    // Now place special lakes, etc.
        //    byte[,] cave_pillar = { { 0, 14, 11, 1 }, { 14, 19, 20, 11 }, { 17, 18, 21, 8 }, { 1, 17, 8, 0 } };
        //    byte[,] mntn_pillar = { { 37, 29, 27, 36 }, { 29, 33, 34, 27 }, { 31, 32, 35, 25 }, { 36, 31, 25, 37 } };
        //    byte[,] surf_lake = { { 56, 55, 54, 3 }, { 57, 50, 61, 54 }, { 58, 51, 59, 53 }, { 3, 4, 58, 52 } };
        //    byte[,] cave_lake = { { 93, 96, 71, 71 }, { 96, 71, 71, 71 }, { 71, 71, 71, 96 }, { 71, 71, 71, 96 } };
        //    Location[] special_ter_locs =
        //    {
        //        new Location(3,2),new Location(3,6),new Location(2,12),new Location(3,18),new Location(1,24),
        //        new Location(7,11),new Location(15,11),new Location(11,21),new Location(12,3),new Location(20,8),
        //        new Location(20,16),new Location(19,11),new Location(19,21),new Location(7,20),new Location(11,11)
        //    };

        //    if (ter_type == 2)
        //        for (int i = 0; i < 15; i++)
        //            if (Maths.Rand(1, 0, 5) == 1)
        //            {
        //                Location stuff_ul = special_ter_locs[i];
        //                for (int j = 0; j < 4; j++)
        //                    for (int k = 0; k < 4; k++)
        //                        _Terrain[stuff_ul.x + j, stuff_ul.y + k] = mntn_pillar[k, j];
        //            }
        //    if (base_terrain == 0)
        //        for (int i = 0; i < 15; i++)
        //            if (Maths.Rand(1, 0, 25) == 1)
        //            {
        //                Location stuff_ul = special_ter_locs[i];
        //                for (int j = 0; j < 4; j++)
        //                    for (int k = 0; k < 4; k++)
        //                        _Terrain[stuff_ul.x + j, stuff_ul.y + k] = cave_pillar[k, j];
        //            }
        //    if (base_terrain == 0)
        //        for (int i = 0; i < 15; i++)
        //            if (Maths.Rand(1, 0, 40) == 1)
        //            {
        //                Location stuff_ul = special_ter_locs[i];
        //                for (int j = 0; j < 4; j++)
        //                    for (int k = 0; k < 4; k++)
        //                        _Terrain[stuff_ul.x + j, stuff_ul.y + k] = cave_lake[k, j];
        //            }
        //    if (base_terrain == 2)
        //        for (int i = 0; i < 15; i++)
        //            if (Maths.Rand(1, 0, 40) == 1)
        //            {
        //                Location stuff_ul = special_ter_locs[i];
        //                for (int j = 0; j < 4; j++)
        //                    for (int k = 0; k < 4; k++)
        //                        _Terrain[stuff_ul.x + j, stuff_ul.y + k] = surf_lake[k, j];
        //            }

        //    /////////////////////////////////////////////////////////////////////////////////////////////////////
        //    //////////////////////////////////////////// EDGE WALLS /////////////////////////////////////////////



        //    int[] walls = {5,6,7,8,9, 10,11,12,13,14, 15,16,17,18,19, 20,21,22,23,24,
        //                    25,26,27,28,29, 30,31,32,33,34, 35};
        //    int num_walls = 0;

        //    for (int k = 0; k < 31; k++)
        //    {
        //        if (underterrain[2, 1].Num == walls[k]) num_walls++;
        //        if (underterrain[0, 1].Num == walls[k]) num_walls++;
        //        if (underterrain[1, 2].Num == walls[k]) num_walls++;
        //        if (underterrain[1, 0].Num == walls[k]) num_walls++;
        //    }

        //    if (ter_base[ter_type] == 0) //Cave floor
        //    {
        //        for (int i = 0; i < num_walls; i++)
        //        {
        //            int r1 = Maths.Rand(1, 0, 3);
        //            for (int j = 0; j < ((r1 == 0 || r1 == 2) ? Width : Height); j++)
        //                switch (r1)
        //                {
        //                    case 0:
        //                        _Terrain[j, 0] = 6;
        //                        break;
        //                    case 1:
        //                        _Terrain[0, j] = 9;
        //                        break;
        //                    case 2:
        //                        _Terrain[j, Height - 1] = 12;
        //                        break;
        //                    case 3:
        //                        _Terrain[Width - 1, j] = 15;
        //                        break;
        //                }
        //        }
        //        if ((_Terrain[9, 0] == 6) && (_Terrain[0, 12] == 9)) //Corner bits?
        //            _Terrain[0, 0] = 21;
        //        if ((_Terrain[24, 12] == 15) && (_Terrain[9, 27] == 12))
        //            _Terrain[24, 27] = 19;
        //        if ((_Terrain[9, 0] == 6) && (_Terrain[30, 12] == 15))
        //            _Terrain[24, 0] = 32;
        //        if ((_Terrain[0, 12] == 9) && (_Terrain[9, 27] == 12))
        //            _Terrain[0, 27] = 20;
        //    }
        //    if (ter_base[ter_type] == 36) //Hills
        //    {
        //        for (int i = 0; i < num_walls; i++)
        //        {
        //            int r1 = Maths.Rand(1, 0, 3);
        //            for (int j = 0; j < ((r1 == 0 || r1 == 2) ? Width : Height); j++)
        //                switch (r1)
        //                {
        //                    case 0:
        //                        _Terrain[j, 0] = 24;
        //                        break;
        //                    case 1:
        //                        _Terrain[0, j] = 26;
        //                        break;
        //                    case 2:
        //                        _Terrain[j, Height-1] = 28;
        //                        break;
        //                    case 3:
        //                        _Terrain[Width-1, j] = 30;
        //                        break;
        //                }
        //        }
        //        if ((_Terrain[9, 0] == 24) && (_Terrain[0, 12] == 26)) //Corner bits?
        //            _Terrain[0, 0] = 21;
        //        if ((_Terrain[24, 12] == 30) && (_Terrain[9, 27] == 28))
        //            _Terrain[24, 27] = 19;
        //        if ((_Terrain[9, 0] == 24) && (_Terrain[30, 12] == 30))
        //            _Terrain[24, 0] = 32;
        //        if ((_Terrain[0, 12] == 26) && (_Terrain[9, 27] == 28))
        //            _Terrain[0, 27] = 20;
        //    }

        //    //TODO: make_town_trim(1);

        //    /////////////////////////////////////////////////////////////////////////////////////////////////////
        //    //////////////////////////////////////////// CHARACTERS /////////////////////////////////////////////

        //    // place PCs
        //    Party.Pos = new Location(12, 15);
        //    UpdateVisible();
        //    PlacePartyForCombat(eDir.N);
        //    foreach (PCType pc in Party.EachAlivePC())
        //    {
        //        if (TerrainAt(pc.Pos).DoNotPlacePC) _Terrain[pc.Pos.x, pc.Pos.y] = base_terrain;
        //    }
        //    Gfx.CentreView(Party.Pos, true);

        //    //// Place NPCs
        //    foreach (Tuple<NPCRecord, eAttitude> z in encounter.EachNPC())
        //    {
        //        NPCList.Add(NPCType.Instantiate(z.Item1, Location.Zero, z.Item2));
        //    }

        //    //Now put them on the map.
        //    foreach (NPCType npc in NPCList)
        //    {
        //        int num_tries = 0;
        //        Location pos;
        //        do
        //        {
        //            pos = new Location(Maths.Rand(1, 7, 17), Maths.Rand(1, 6, 10));
        //            if (npc.Attitude == eAttitude.FRIENDLY)
        //                pos = pos.Mod(0, 9);
        //            else if (npc.Record.MageLevel > 0 || npc.Record.PriestLevel > 0)
        //                pos = pos.Mod(0, -4);
        //        } while (!CharacterCanBeThere(pos, npc) && num_tries++ < 50);

        //        npc.Pos = pos;

        //        if (TerrainAt(npc.Pos).BlocksNPC)
        //            _Terrain[npc.Pos.x, npc.Pos.y] = base_terrain;
        //    }

        //}

        ////        /// <summary>
        /////// Constructor for making a TownMap for the purposes of an outdoor combat encounter.
        /////// </summary>
        /////// <param name="encounter">The group of NPCs we've encountered here</param>
        /////// <param name="in_which_terrain">The terrain type on the world map the combat map will be based on</param>
        /////// <param name="num_walls">Is map hemmed in on the sides with walls?</param>
        ////public CombatMap(NPCGroupRecord encounter, TerrainRecord in_which_terrain, int num_walls)
        ////{
        ////    NPCGroup = encounter;

        ////    Width = Constants.COMBAT_MAP_WIDTH;
        ////    Height = Constants.COMBAT_MAP_HEIGHT;
        ////    Boundary = new RECT(0, 0, Constants.COMBAT_MAP_WIDTH - 1, Constants.COMBAT_MAP_HEIGHT - 1);

        ////    //Terrain = new TerrainMap(this, In);
        ////    _Terrain = new ushort[Width, Height];
        ////    _Explored = new bool[Width, Height];
        ////    Misc = new uint[Width, Height];

        ////    //Generate the Combat terrain
        ////    int[] general_types =  {1,1,0,0,0,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,2,2,
        ////                            2,2,2,2,2,2,2,2,2,2,
        ////                            2,2,2,2,2,2,2,2,2,2,
        ////                            2,2,2,2,2,2,0,0,0,0,
        ////                            0,0,0,0,0,0,0,0,0,0,// 50
        ////                            0,3,3,3,3,3,3,5,5,5,
        ////                            6,6,7,7,1,1,8,9,10,11,
        ////                            11,11,12,13,13,9,9,9,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,// 100
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,// 150
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,0,1,1,1,1,1,1,1,0,
        ////                            0,0,0,0,0,0,0,0,0,0,
        ////                            0,0,14,15,16,0,0,1,1,1,// 200
        ////                            1,0,2,1,1,1,0,1,1,1,
        ////                            1,1,0,0,0,0,1,0,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1,
        ////                            1,1,1,1,1,1,1,1,1,1};// 250
        ////    byte[] ter_base = {2,0,36,50,71, 0,0,0,0,2, 2,2,2,0, 0,2,36};

        ////    Location[] special_ter_locs =
        ////    {
        ////        new Location(11,10),new Location(11,14),new Location(10,20),new Location(11,26),new Location(9,30),
        ////        new Location(15,19),new Location(23,19),new Location(19,29),new Location(20,11),new Location(28,16),
        ////        new Location(28,24),new Location(27,19),new Location(27,29),new Location(15,28),new Location(19,19)
        ////    };

        ////    int[,] terrain_odds       = {
        ////                                    {3,80, 4,40, 115,20, 114,10, 112,1},    // 0 : Grass
        ////                                    {1,50,93,25,94,5,98,10,95,1},           // 1 : Cave
        ////                                    {37,20,0,0,0,0,0,0,0,0},                // 2 : Hills
        ////                                    {64,3,63,1,0,0,0,0,0,0},                // 3 : Grass Bridge
        ////                                    {74,1,0,0,0,0,0,0,0,0},                 // 4 : Cave Bridge 
        ////                                    {84,700,97,30,98,20,92,4,95,1},         // 5 : Rocky Cave
        ////                                    {93,280,91,300,92,270,95,7,98,10},      // 6 : Woody cave
        ////                                    {1,800,93,600,94,10,92,10,95,4},        // 7 : Shroomy cave
        ////                                    {1,700,96,200,95,100,92,10,112,5},      // 8 : Swampy cave
        ////                                    {3,600,87,90,110,20,114,6,113,2},       // 9 : Rocky grass
        ////                                    {3,200,4,400,111,250,0,0,0,0},          // 10 : Swampy grass
        ////                                    {3,200,4,300,112,50,113,60,114,100},    // 11 : Woody grass
        ////                                    {3,100,4,250,115,120,114,30,112,2},     // 12 : Little woody grass
        ////                                    {1,25,84,15,98,300,97,280,0,0},         // 13 : Stalagmity cave
        ////                                    {1,50,93,25,94,5,98,10,95,1},           // 14 : Cave road  *
        ////                                    {3,80,4,40,115,20,114,10,112,1},        // 15 : Grass road *
        ////                                    {37,20,0,0,0,0,0,0,0,0}                 // 16 : Hills road *
        ////                                }; // ter then odds then ter then odds ...

        ////    int ter_type = in_which_terrain.picture;
        ////    if (ter_type == 401 || ter_type == 402)
        ////        ter_type = 4;
        ////    else if (ter_type > 260)
        ////        ter_type = 1;
        ////    else ter_type = general_types[ter_type];

        ////    for (int i = 0; i < Constants.COMBAT_MAP_WIDTH; i++)
        ////        for (int j = 0; j < Constants.COMBAT_MAP_HEIGHT; j++)
        ////        {
        ////            _Explored[i,j] = false;
        ////            Misc[i,j] = 0;
        ////            if ((j <= 8) || (j >= 35) || (i <= 8) || (i >= 35))
        ////                _Terrain[i,j] = 90;
        ////            else _Terrain[i,j] = ter_base[ter_type];
        ////        }

        ////    for (int i = 0; i < Constants.COMBAT_MAP_WIDTH; i++)
        ////        for (int j = 0; j < Constants.COMBAT_MAP_HEIGHT; j++)
        ////            for (int k = 0; k < 5; k++)
        ////                if ((_Terrain[i,j] != 90) && (Maths.Rand(1, 1, 1000) < terrain_odds[ter_type,k * 2 + 1]))
        ////                    _Terrain[i,j] = (byte)terrain_odds[ter_type,k * 2];

        ////    _Terrain[0,0] = ter_base[ter_type];


        ////    //26 x 26 (on 48x48 from 9 to 34 inclusive)

        ////    if (ter_type == 3) //Grass Bridge
        ////    {
        ////        _Terrain[0,0] = 83; //Walkway on grass
        ////        for (int i = 15; i < 26; i++)
        ////            for (int j = 9; j < 35; j++)
        ////                _Terrain[i,j] = 83;
        ////    }

        ////    if (ter_type == 4) //Cave bridge
        ////    {
        ////        _Terrain[0,0] = 82; //Walkway on cave
        ////        for (int i = 15; i < 26; i++)
        ////            for (int j = 9; j < 35; j++)
        ////                _Terrain[i,j] = 82;
        ////    }

        ////    if (ter_type == 14 || ter_type == 15 || ter_type == 16) //Road?
        ////    {
        ////        _Terrain[0,0] = 82;
        ////        for (int i = 19; i < 23; i++)
        ////            for (int j = 9; j < 35; j++)
        ////                _Terrain[i,j] = 82;
        ////    }

        ////    // Now place special lakes, etc.
        ////    byte[,] cave_pillar = { { 0, 14, 11, 1 }, { 14, 19, 20, 11 }, { 17, 18, 21, 8 }, { 1, 17, 8, 0 } };
        ////    byte[,] mntn_pillar = { { 37, 29, 27, 36 }, { 29, 33, 34, 27 }, { 31, 32, 35, 25 }, { 36, 31, 25, 37 } };
        ////    byte[,] surf_lake = { { 56, 55, 54, 3 }, { 57, 50, 61, 54 }, { 58, 51, 59, 53 }, { 3, 4, 58, 52 } };
        ////    byte[,] cave_lake = { { 93, 96, 71, 71 }, { 96, 71, 71, 71 }, { 71, 71, 71, 96 }, { 71, 71, 71, 96 } };

        ////    if (ter_type == 2)
        ////        for (int i = 0; i < 15; i++)
        ////            if (Maths.Rand(1, 0, 5) == 1)
        ////            {
        ////                Location stuff_ul = special_ter_locs[i];
        ////                for (int j = 0; j < 4; j++)
        ////                    for (int k = 0; k < 4; k++)
        ////                        _Terrain[stuff_ul.x + j,stuff_ul.y + k] = mntn_pillar[k,j];
        ////            }
        ////    if (_Terrain[0,0] == 0)
        ////        for (int i = 0; i < 15; i++)
        ////            if (Maths.Rand(1, 0, 25) == 1)
        ////            {
        ////                Location stuff_ul = special_ter_locs[i];
        ////                for (int j = 0; j < 4; j++)
        ////                    for (int k = 0; k < 4; k++)
        ////                        _Terrain[stuff_ul.x + j,stuff_ul.y + k] = cave_pillar[k,j];
        ////            }
        ////    if (_Terrain[0,0] == 0)
        ////        for (int i = 0; i < 15; i++)
        ////            if (Maths.Rand(1, 0, 40) == 1)
        ////            {
        ////                Location stuff_ul = special_ter_locs[i];
        ////                for (int j = 0; j < 4; j++)
        ////                    for (int k = 0; k < 4; k++)
        ////                        _Terrain[stuff_ul.x + j,stuff_ul.y + k] = cave_lake[k,j];
        ////            }
        ////    if (_Terrain[0,0] == 2)
        ////        for (int i = 0; i < 15; i++)
        ////            if (Maths.Rand(1, 0, 40) == 1)
        ////            {
        ////                Location stuff_ul = special_ter_locs[i];
        ////                for (int j = 0; j < 4; j++)
        ////                    for (int k = 0; k < 4; k++)
        ////                        _Terrain[stuff_ul.x + j,stuff_ul.y + k] = surf_lake[k,j];
        ////            }

        ////    if (ter_base[ter_type] == 0) //Cave floor
        ////    {
        ////        for (int i = 0; i < num_walls; i++)
        ////        {
        ////            int r1 = Maths.Rand(1, 0, 3);
        ////            for (int j = 9; j < 35; j++)
        ////                switch (r1)
        ////                {
        ////                case 0:
        ////                    _Terrain[j,8] = 6;
        ////                    break;
        ////                case 1:
        ////                    _Terrain[8,j] = 9;
        ////                    break;
        ////                case 2:
        ////                    _Terrain[j,35] = 12;
        ////                    break;
        ////                case 3:
        ////                    _Terrain[32,j] = 15;
        ////                    break;
        ////                }
        ////        }
        ////        if ((_Terrain[17,8] == 6) && (_Terrain[8,20] == 9)) //Corner bits?
        ////            _Terrain[8,8] = 21;
        ////        if ((_Terrain[32,20] == 15) && (_Terrain[17,35] == 12))
        ////            _Terrain[32,35] = 19;
        ////        if ((_Terrain[17,8] == 6) && (_Terrain[32,20] == 15))
        ////            _Terrain[32,8] = 32;
        ////        if ((_Terrain[8,20] == 9) && (_Terrain[17,35] == 12))
        ////            _Terrain[8,35] = 20;
        ////    }
        ////    if (ter_base[ter_type] == 36) //Hills
        ////    {
        ////        for (int i = 0; i < num_walls; i++)
        ////        {
        ////            int r1 = Maths.Rand(1, 0, 3);
        ////            for (int j = 9; j < 35; j++)
        ////                switch (r1)
        ////                {
        ////                case 0:
        ////                    _Terrain[j,8] = 24;
        ////                    break;
        ////                case 1:
        ////                    _Terrain[8,j] = 26;
        ////                    break;
        ////                case 2:
        ////                    _Terrain[j,35] = 28;
        ////                    break;
        ////                case 3:
        ////                    _Terrain[32,j] = 30;
        ////                    break;
        ////                }
        ////        }
        ////        if ((_Terrain[17,8] == 6) && (_Terrain[8,20] == 9))
        ////            _Terrain[8,8] = 35;
        ////        if ((_Terrain[32,20] == 15) && (_Terrain[17,35] == 12))
        ////            _Terrain[32,35] = 33;
        ////        if ((_Terrain[17,8] == 6) && (_Terrain[32,20] == 15))
        ////            _Terrain[32,8] = 32;
        ////        if ((_Terrain[8,20] == 9) && (_Terrain[17,35] == 12))
        ////            _Terrain[8,35] = 34;
        ////    }

        ////    //TODO: make_town_trim(1);

        ////    // place PCs
        ////    Party.Pos = new Location(20, 23);
        ////    UpdateVisible();
        ////    PlacePartyForCombat(eDir.N);
        ////    foreach (PCType pc in Party.EachAlivePC())
        ////    {
        ////        if (TerrainAt(pc.Pos).DoNotPlacePC) _Terrain[pc.Pos.x, pc.Pos.y] = _Terrain[0, 0];
        ////    }
        ////    Gfx.CentreView(Party.Pos, true);

        ////    //// Place NPCs
        ////    foreach (Tuple<NPCRecord, eAttitude> z in encounter.EachNPC())
        ////    {
        ////        NPCList.Add(NPCType.Instantiate(z.Item1, Location.Zero, z.Item2));
        ////    }

        ////    //Now put them on the map.
        ////    foreach (NPCType npc in NPCList)
        ////    {
        ////        int num_tries = 0;
        ////        Location pos;
        ////        do
        ////        {
        ////            pos = new Location(Maths.Rand(1, 15, 25), Maths.Rand(1, 14, 18));
        ////            if (npc.Attitude == eAttitude.FRIENDLY)
        ////                pos = pos./*npc.Pos.*/Mod(0, 9);
        ////            else if (npc.Record.MageLevel > 0 || npc.Record.PriestLevel > 0)
        ////                pos = pos/*npc.Pos*/.Mod(0, -4);
        ////        } while ((!CharacterCanBeThere(pos, npc) || _Terrain[pos.x, pos.y] == 180) && num_tries++ < 50);

        ////        npc.Pos = pos;

        ////        if (TerrainAt(npc.Pos).BlocksNPC)
        ////            _Terrain[npc.Pos.x, npc.Pos.y] = _Terrain[0,0];
        ////    }

        }


    }
}