
def WatchpointTower_971_MapTrigger_18_17(p):
    if StuffDone["17_5"] < 3:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        Animation_Hold(-1, 068_identify)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(34,30)
        Party.MoveToMap(TownMap.List["Xanthor_37"])
        return

def WatchpointTower_975_MapTrigger_24_33(p):
    if StuffDone["17_3"] == 25:
        MessageBox("A thin opaque barrier covers this passage way. Astervis chuckles, \"My this one\'s pretty easy! This was one of the first barriers we researched. Stand back.\" Astervis chants and shatters the barrier. You may now proceed.")
        StuffDone["17_3"] = 26
        Town.AlterTerrain(Location(24,32), 0, TerrainRecord.UnderlayList[170])
        if StuffDone["17_3"] >= 27:
            for x in range(31, 33):
                for y in range(25, 26):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(32, 33):
                for y in range(13, 15):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            Town.AlterTerrain(Location(32,10), 0, TerrainRecord.UnderlayList[173])
            if StuffDone["17_3"] >= 28:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if  npc.IsABaddie: Town.NPCList.Remove(npc)
                return
            if StuffDone["17_3"] >= 24:
                if StuffDone["21_9"] == 250:
                    return
                StuffDone["21_9"] = 250
                ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
                return
            return
        if StuffDone["17_3"] >= 28:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            return
        if StuffDone["17_3"] >= 24:
            if StuffDone["21_9"] == 250:
                return
            StuffDone["21_9"] = 250
            ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
            return
        return

def WatchpointTower_976_MapTrigger_31_26(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(31,25)).Num == 169:
        if StuffDone["22_0"] == 250:
            return
        StuffDone["22_0"] = 250
        ChoiceBox("Astervis approaches the barrier and begins to scry it. After a minute he turns to you and frowns, \"I\'m afraid this one is a doozy. I\'m supposed to keep this a secret, but I suppose it doesn\'t matter anymore.\n\nThe intent of this research, as you may have guessed, was to develop a better magical barrier. Wizards have spoken of the \'ultimate barrier\' since they were first developed thousands of years ago.\n\nIt would be the barrier that no one, except those who were supposed to, could break. Most barriers are destroyed by a simple Dispel Barrier spell because of their matrix. The new kind of barrier discovered 400 years ago uses different methods.\n\nThese barriers are a bit more difficult to break because of their radical and alien approach. This new kind of barrier is a field of its own as the kinds of barriers that can be created are virtually limitless.\n\nOdix and I were working with this promising new matrix. The only problem was that it was kind of unstable and would only hold for a short, and unpredictable amount of time.\n\nJust before you came back with evidence against Odix, he was saying that he may have found a way to counteract this instability problem. Unfortunately, he did not give me the details.", eDialogPic.TERRAIN, 231, ["OK"])
        ChoiceBox("The matrix is very similar to the one we were working on, but with a few modifications. I\'m guessing this is Odix\'s latest product. I really don\'t know the specs and would need days of analysis.\n\nAlso, if this barrier is all Odix was making it up to be, we\'re in trouble. The only way we could then deactivate this barrier would be to attack its power source, which I know from my conversations with Odix, is on the second floor.\n\nIt is a special kind of energy crystal. If we could shatter it, we could disable the barriers! Of course, we have to hope we can find a way around the barriers to get to the crystal, which I\'m sure is very well defended.\"", eDialogPic.TERRAIN, 231, ["OK"])
        return

def WatchpointTower_979_MapTrigger_14_13(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(12,13)
    Party.MoveToMap(TownMap.List["WatchpointTowerL2_43"])

def WatchpointTower_981_MapTrigger_5_15(p):
    if StuffDone["22_1"] == 250:
        return
    StuffDone["22_1"] = 250
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(5,15))
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(6,15))
    MessageBox("You hear a loud chanting to the north. You look to see a small opening on the other side of the room. Energy hangs in the air forming. It appears they are manufacturing some kind of magical barrier!")

def WatchpointTower_983_MapTrigger_8_10(p):
    if StuffDone["22_2"] == 250:
        return
    StuffDone["22_2"] = 250
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(8,10))
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(9,10))
    MessageBox("As you approach the energy cloud, it becomes disrupted and fades away. The wizards break out of their trance and don\'t look too happy.")
    Town.PlaceEncounterGroup(1)

def WatchpointTower_985_MapTrigger_24_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,5)
    Party.MoveToMap(TownMap.List["WatchpointTowerL2_43"])

def WatchpointTower_990_MapTrigger_17_13(p):
    if StuffDone["22_5"] == 250:
        return
    StuffDone["22_5"] = 250
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(17,13))
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(17,14))
    ChoiceBox("Astervis manages to sense another image and relay it to you. You see the same young mage in a room with several other mages. The situation is one of panicked preparation.\n\n\"We must get that barrier up now!\" shouts the young mage at several wizards trying to put up a barrier. \"We\'re going as fast as we can, sir,\" one of them replies. The mage yells, \"Are the Wyverns in place? What about the Golems?\"\n\nYou hear another shout off in the distance. \"I\'m bringing the Wyverns in at this moment. The golems should be in place.\" The young mage is clearly nervous. \"Hurry! They\'re going to be here any moment!\"", eDialogPic.STANDARD, 0, ["OK"])

def WatchpointTower_992_MapTrigger_33_7(p):
    if StuffDone["23_0"] == 250:
        return
    StuffDone["23_0"] = 250
    TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(33,7))
    MessageBox("A search of this desk turns up some administrative papers, more papers, and a LOT more papers. The owner of this desk is very disorganized. In fact, in a stack of papers, you discover a misplaced key made of bone!")
    SpecialItem.Give("BoneKey")

def WatchpointTower_993_OnEntry(p):
    if StuffDone["17_3"] >= 25:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Odix_233": Town.NPCList.Remove(npc)
        if StuffDone["17_3"] >= 26:
            Town.AlterTerrain(Location(24,32), 0, TerrainRecord.UnderlayList[170])
            if StuffDone["17_3"] >= 27:
                for x in range(31, 33):
                    for y in range(25, 26):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
                for x in range(32, 33):
                    for y in range(13, 15):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
                Town.AlterTerrain(Location(32,10), 0, TerrainRecord.UnderlayList[173])
                if StuffDone["17_3"] >= 28:
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if  npc.IsABaddie: Town.NPCList.Remove(npc)
                    return
                if StuffDone["17_3"] >= 24:
                    if StuffDone["21_9"] == 250:
                        return
                    StuffDone["21_9"] = 250
                    ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
                    return
                return
            if StuffDone["17_3"] >= 28:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if  npc.IsABaddie: Town.NPCList.Remove(npc)
                return
            if StuffDone["17_3"] >= 24:
                if StuffDone["21_9"] == 250:
                    return
                StuffDone["21_9"] = 250
                ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
                return
            return
        if StuffDone["17_3"] >= 27:
            for x in range(31, 33):
                for y in range(25, 26):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(32, 33):
                for y in range(13, 15):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            Town.AlterTerrain(Location(32,10), 0, TerrainRecord.UnderlayList[173])
            if StuffDone["17_3"] >= 28:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if  npc.IsABaddie: Town.NPCList.Remove(npc)
                return
            if StuffDone["17_3"] >= 24:
                if StuffDone["21_9"] == 250:
                    return
                StuffDone["21_9"] = 250
                ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
                return
            return
        if StuffDone["17_3"] >= 28:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            return
        if StuffDone["17_3"] >= 24:
            if StuffDone["21_9"] == 250:
                return
            StuffDone["21_9"] = 250
            ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
            return
        return
    if StuffDone["17_3"] >= 26:
        Town.AlterTerrain(Location(24,32), 0, TerrainRecord.UnderlayList[170])
        if StuffDone["17_3"] >= 27:
            for x in range(31, 33):
                for y in range(25, 26):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(32, 33):
                for y in range(13, 15):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            Town.AlterTerrain(Location(32,10), 0, TerrainRecord.UnderlayList[173])
            if StuffDone["17_3"] >= 28:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if  npc.IsABaddie: Town.NPCList.Remove(npc)
                return
            if StuffDone["17_3"] >= 24:
                if StuffDone["21_9"] == 250:
                    return
                StuffDone["21_9"] = 250
                ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
                return
            return
        if StuffDone["17_3"] >= 28:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            return
        if StuffDone["17_3"] >= 24:
            if StuffDone["21_9"] == 250:
                return
            StuffDone["21_9"] = 250
            ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
            return
        return
    if StuffDone["17_3"] >= 27:
        for x in range(31, 33):
            for y in range(25, 26):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
        for x in range(32, 33):
            for y in range(13, 15):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
        Town.AlterTerrain(Location(32,10), 0, TerrainRecord.UnderlayList[173])
        if StuffDone["17_3"] >= 28:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            return
        if StuffDone["17_3"] >= 24:
            if StuffDone["21_9"] == 250:
                return
            StuffDone["21_9"] = 250
            ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
            return
        return
    if StuffDone["17_3"] >= 28:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        return
    if StuffDone["17_3"] >= 24:
        if StuffDone["21_9"] == 250:
            return
        StuffDone["21_9"] = 250
        ChoiceBox("At last, you have arrived at Watchpoint Tower. The structure is quite old and dignified. Lush green strands of ivy grow along the walls. The sounds of songbirds sing out accompanying the waves of the nearby ocean. It all seems so tranquil.\n\nAstervis turns to you, \"Well here we are. It seems so peaceful from out here. But there is no telling what foul traps they have set within.\" He closes his eyes and stands straight up for several seconds.\n\n\"I sense great evil from within. A force so strong...I feel, whatever it is, is reaching out to us, touching us, sensing our inner minds. It...it...it\'s so chilling and dark that I cannot describe it.\n\nIt knows I\'m looking at it. I cannot probe further...it\'s blocking out my mind.\" Astervis returns to a normal position and looks at you grimly. \"Whatever it is, it cannot be good.\"\n\nYou have your own suspicions.", eDialogPic.TERRAIN, 197, ["OK"])
        return

def WatchpointTower_994_TalkingTrigger2(p):
    StuffDone["17_5"] = 2
