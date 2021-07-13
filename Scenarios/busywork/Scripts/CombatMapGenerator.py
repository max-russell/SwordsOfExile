# When the party encounters a group of wandering NPCs outside, the program generates a temporary map on which the combat takes place.
# This is handled in this script. The parameters are:
#    town: TownMap that is the new temporary town being generated. Its dimensions are specified in the scenario but the terrain data
#           is empty.
#    encounter: object of type NPCGroupRecord containing info on the NPCs in the encounter
#    underterrain: 3x3 array of TerrainRecord objects containing the underlay terrain at the player's location on the world map when the
#                  encounter began. [1,1] is the terrain the party is standing on, the others all the adjacent squares.
#    overterrain: As above for overlay terrain. Null object ('None') for each element where there is no overlay terrain.

def Generate_Combat_Map(town, encounter, underterrain, overterrain):

    general_types =(1,1,0,0,0,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,2,2,
                    2,2,2,2,2,2,2,2,2,2,
                    2,2,2,2,2,2,2,2,2,2,
                    2,2,2,2,2,2,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,# 50
                    0,3,3,3,3,3,3,5,5,5,
                    6,6,7,7,1,1,8,9,10,11,
                    11,11,12,13,13,9,9,9,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,# 100
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,# 150
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,0,1,1,1,1,1,1,1,0,
                    0,0,0,0,0,0,0,0,0,0,
                    0,0,14,15,16,0,0,1,1,1,# 200
                    1,0,2,1,1,1,0,1,1,1,
                    1,1,0,0,0,0,1,0,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1) # 250
    ter_base =  2, 0, 36, 50, 71, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 36
    terrain_odds =( ((3,80), (4,40), (115,20), (114,10), (112,1)),    # 0 : Grass
                    ((1,50),(93,25),(94,5),(98,10),(95,1)),           # 1 : Cave
                    ((37,20),),                                       # 2 : Hills
                    ((64,3),(63,1)),                                  # 3 : Grass Bridge
                    ((74,1),),                                        # 4 : Cave Bridge
                    ((84,700),(97,30),(98,20),(92,4),(95,1)),         # 5 : Rocky Cave
                    ((93,280),(91,300),(92,270),(95,7),(98,10)),      # 6 : Woody cave
                    ((1,800),(93,600),(94,10),(92,10),(95,4)),        # 7 : Shroomy cave
                    ((1,700),(96,200),(95,100),(92,10),(112,5)),      # 8 : Swampy cave
                    ((3,600),(87,90),(110,20),(114,6),(113,2)),       # 9 : Rocky grass
                    ((3,200),(4,400),(111,250)),                      # 10 : Swampy grass
                    ((3,200),(4,300),(112,50),(113,60),(114,100)),    # 11 : Woody grass
                    ((3,100),(4,250),(115,120),(114,30),(112,2)),     # 12 : Little woody grass
                    ((1,25),(84,15),(98,300),(97,280)),               # 13 : Stalagmity cave
                    ((1,50),(93,25),(94,5),(98,10),(95,1)),           # 14 : Cave road  *
                    ((3,80),(4,40),(115,20),(114,10),(112,1)),        # 15 : Grass road *
                    ((37,20),))                                       # 16 : Hills road *
                    # ter then odds then ter then odds ...

    #Find the right base terrain
    ter_type = underterrain[1,1].Picture
    if ter_type == 401 or ter_type == 402: #Cave bridge
        ter_type = 4
    elif ter_type >= 260:
        ter_type = 1
    else:
        ter_type = general_types[ter_type]

    for i in range(town.Width):
        for j in range(town.Height):
            town.AlterTerrain(Location(i, j), 0, TerrainRecord.UnderlayList[ter_base[ter_type]])

    for i in range(town.Width):
        for j in range(town.Height):
            for k in terrain_odds[ter_type]:
                if Maths.Rand(1, 1, 1000) < k[1]:
                    town.AlterTerrain(Location(i,j),0,TerrainRecord.UnderlayList[k[0]])

    base_terrain = ter_base[ter_type]

    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////// BRIDGES ////////////////////////////////////////////////

    if ter_type == 3 or ter_type == 4: #Bridge
        base_terrain = 83 #Walkway on grass
        for i in range(7,18):
            for j in range(town.Height):
                town.AlterTerrain(Location(i, j), 0, TerrainRecord.UnderlayList[82])

    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////// TERRAIN FEATURES ///////////////////////////////////////

    #Now place special lakes, etc.
    cave_pillar = ( ( 0, 14, 11, 1 ), ( 14, 19, 20, 11 ), ( 17, 18, 21, 8 ), ( 1, 17, 8, 0 ) )
    mntn_pillar = ( ( 37, 29, 27, 36 ), ( 29, 33, 34, 27 ), ( 31, 32, 35, 25 ), ( 36, 31, 25, 37 ) )
    surf_lake = ( ( 56, 55, 54, 3 ), ( 57, 50, 61, 54 ), ( 58, 51, 59, 53 ), ( 3, 4, 58, 52 ) )
    cave_lake = ( ( 93, 96, 71, 71 ), ( 96, 71, 71, 71 ), ( 71, 71, 71, 96 ), ( 71, 71, 71, 96 ) )
    special_ter_locs = (Location(3,2), Location(3,6), Location(2,12), Location(3,18), Location(1,24),
                        Location(7,11), Location(15,11), Location(11,21), Location(12,3), Location(20,8),
                        Location(20,16), Location(19,11), Location(19,21), Location(7,20), Location(11,11))

    if ter_type == 2:
        for i in range(15):
            if Maths.Rand(1, 0, 5) == 1:
                stuff_ul = special_ter_locs[i]
                for j in range(4):
                    for k in range(4):
                        town.AlterTerrain(Location(stuff_ul.X + j, stuff_ul.Y + k), 0, TerrainRecord.UnderlayList[mntn_pillar[k][j]])

    if base_terrain == 0:
        for i in range(15):
            if Maths.Rand(1, 0, 25) == 1:
                stuff_ul = special_ter_locs[i]
                for j in range(4):
                    for k in range(4):
                        town.AlterTerrain(Location(stuff_ul.X + j, stuff_ul.Y + k), 0, TerrainRecord.UnderlayList[cave_pillar[k][j]])

    if base_terrain == 0:
        for i in range(15):
            if Maths.Rand(1, 0, 40) == 1:
                stuff_ul = special_ter_locs[i]
                for j in range(4):
                    for k in range(4):
                        town.AlterTerrain(Location(stuff_ul.X + j, stuff_ul.Y + k), 0, TerrainRecord.UnderlayList[cave_lake[k][j]])

    if base_terrain == 0:
        for i in range(15):
            if Maths.Rand(1, 0, 40) == 1:
                stuff_ul = special_ter_locs[i]
                for j in range(4):
                    for k in range(4):
                        town.AlterTerrain(Location(stuff_ul.X + j, stuff_ul.Y + k), 0, TerrainRecord.UnderlayList[surf_lake[k][j]])

    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////// EDGE WALLS /////////////////////////////////////////////

    walls = (5,6,7,8,9, 10,11,12,13,14, 15,16,17,18,19, 20,21,22,23,24,
             25,26,27,28,29, 30,31,32,33,34, 35);
    num_walls = 0

    for k in walls:
        if underterrain[2,1].Num == k: num_walls += 1
        if underterrain[0,1].Num == k: num_walls += 1
        if underterrain[1,2].Num == k: num_walls += 1
        if underterrain[1,0].Num == k: num_walls += 1

    if ter_base[ter_type] == 0: #Cave floor
        for i in range(num_walls):
            r1 = Maths.Rand(1, 0, 3)

            for j in range(town.Width if (r1 == 0 or r1 == 2) else town.Height):
                if r1 == 0:
                    town.AlterTerrain(Location(j, 0), 0, TerrainRecord.UnderlayList[6])
                elif r1 == 1:
                    town.AlterTerrain(Location(0, j), 0, TerrainRecord.UnderlayList[9])
                elif r1 == 2:
                    town.AlterTerrain(Location(j, town.Height-1), 0, TerrainRecord.UnderlayList[12])
                elif r1 == 3:
                    town.AlterTerrain(Location(town.Width-1, j), 0, TerrainRecord.UnderlayList[15])

        if town.TerrainAt(Location(9, 0)).Num == 6 and town.TerrainAt(Location(0, 12)).Num == 9:
            town.AlterTerrain(Location(0, 0), 0, TerrainRecord.UnderlayList[21])
        if town.TerrainAt(Location(24, 12)).Num == 15 and town.TerrainAt(Location(9, 27)).Num == 12:
            town.AlterTerrain(Location(24, 27), 0, TerrainRecord.UnderlayList[19])
        if town.TerrainAt(Location(9, 0)).Num == 6 and town.TerrainAt(Location(27, 12)).Num == 15:
            town.AlterTerrain(Location(24, 0), 0, TerrainRecord.UnderlayList[32])
        if town.TerrainAt(Location(0, 12)).Num == 9 and town.TerrainAt(Location(9, 27)).Num == 12:
            town.AlterTerrain(Location(0, 27), 0, TerrainRecord.UnderlayList[20])

    if ter_base[ter_type] == 36: #Cave floor
        for i in range(num_walls):
            r1 = Maths.Rand(1, 0, 3)

            for j in range(town.Width if (r1 == 0 or r1 == 2) else town.Height):
                if r1 == 0:
                    town.AlterTerrain(Location(j, 0), 0, TerrainRecord.UnderlayList[24])
                elif r1 == 1:
                    town.AlterTerrain(Location(0, j), 0, TerrainRecord.UnderlayList[26])
                elif r1 == 2:
                    town.AlterTerrain(Location(j, town.Height-1), 0, TerrainRecord.UnderlayList[28])
                elif r1 == 3:
                    town.AlterTerrain(Location(town.Width-1, j), 0, TerrainRecord.UnderlayList[30])

        if town.TerrainAt(Location(9, 0)).Num == 24 and town.TerrainAt(Location(0, 12)).Num == 26:
            town.AlterTerrain(Location(0, 0), 0, TerrainRecord.UnderlayList[21])
        if town.TerrainAt(Location(24, 12)).Num == 30 and town.TerrainAt(Location(9, 27)).Num == 28:
            town.AlterTerrain(Location(24, 27), 0, TerrainRecord.UnderlayList[19])
        if town.TerrainAt(Location(9, 0)).Num == 24 and town.TerrainAt(Location(27, 12)).Num == 30:
            town.AlterTerrain(Location(24, 0), 0, TerrainRecord.UnderlayList[32])
        if town.TerrainAt(Location(0, 12)).Num == 26 and town.TerrainAt(Location(9, 27)).Num == 28:
            town.AlterTerrain(Location(0, 27), 0, TerrainRecord.UnderlayList[20])

    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////// ROADS //////////////////////////////////////////////////
    if overterrain[1,1] != None and overterrain[1,1].picture >= 260 and overterrain[1,1].picture < 276: #Has a road on the terrain
        base_terrain = 82
        for i in range(11,15):
            for j in range(town.Height):
                town.AlterTerrain(Location(i, j), 0, TerrainRecord.UnderlayList[82])


    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////// CHARACTERS /////////////////////////////////////////////

    # place PCs
    Party.Pos = Location(12, 15)
    town.UpdateVisible()
    town.PlacePartyForCombat(eDir.N);
    for pc in Party.EachAlivePC():
        if town.TerrainAt(pc.Pos).DoNotPlacePC:
            town.AlterTerrain(pc.Pos, 0, TerrainRecord.UnderlayList[base_terrain]);
    CentreView(Party.Pos, True)

    # Place NPCs
    for z in encounter.EachNPC():
        town.NPCList.Add(NPCType.Instantiate(z.Item1, Location.Zero, z.Item2))

    #Now put them on the map.
    for npc in town.NPCList:
        num_tries = 0
        pos = Location.Zero
        condition = True
        while condition:
            num_tries+=1

            pos = Location(Maths.Rand(1, 7, 17), Maths.Rand(1, 6, 10))
            if npc.Attitude == eAttitude.FRIENDLY:
                pos = pos.Mod(0, 9)
            elif npc.Record.MageLevel > 0 or npc.Record.PriestLevel > 0:
                pos = pos.Mod(0, -4)
            condition = not town.CharacterCanBeThere(pos, npc) and num_tries < 50

        npc.Pos = pos

        if town.TerrainAt(npc.Pos).BlocksNPC:
            town.AlterTerrain(npc.Pos, 0, TerrainRecord.UnderlayList[base_terrain]);
