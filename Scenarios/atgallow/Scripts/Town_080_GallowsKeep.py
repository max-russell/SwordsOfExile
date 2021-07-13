def Generate_Wandering_80_GallowsKeep(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["VahnataiBlade_97"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_95"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_96"]])
            npcs.append([2,NPCRecord.List["VahnataiWarrior_91"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["VahnataiBlade_97"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_95"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_96"]])
            npcs.append([2,NPCRecord.List["VahnataiWarrior_92"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["VahnataiBlade_97"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_95"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_96"]])
            npcs.append([2,NPCRecord.List["VahnataiShaper_93"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["VahnataiBlade_97"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_95"]])
            npcs.append([1,NPCRecord.List["VahnataiKeeper_96"]])
            npcs.append([2,NPCRecord.List["VahnataiShaper_94"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(28,10)
                elif r2 == 1: l = Location(54,40)
                elif r2 == 2: l = Location(19,37)
                elif r2 == 3: l = Location(28,47)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def GallowsKeep_1991_MapTrigger_5_35(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,31)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_1992_MapTrigger_6_31(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(17,50))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_1993_MapTrigger_18_50(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(5,31))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_1994_MapTrigger_13_31(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_0"] == 0: StuffDone["66_0"] = 1
        else: StuffDone["66_0"] = 0
        t = Town.TerrainAt(Location(15,29)).TransformTo
        Town.AlterTerrain(Location(15,29), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_1995_MapTrigger_31_6(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(31,5)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_1996_MapTrigger_22_3(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(60,45))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_1997_MapTrigger_60_46(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(23,3))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_1998_MapTrigger_44_49(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(47,49)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_1999_MapTrigger_41_45(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_4"] == 0: StuffDone["66_4"] = 1
        else: StuffDone["66_4"] = 0
        t = Town.TerrainAt(Location(39,47)).TransformTo
        Town.AlterTerrain(Location(39,47), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2000_MapTrigger_13_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(52,22))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_2001_MapTrigger_51_22(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(13,44))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_2002_MapTrigger_10_43(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_3"] == 0: StuffDone["66_3"] = 1
        else: StuffDone["66_3"] = 0
        t = Town.TerrainAt(Location(10,47)).TransformTo
        Town.AlterTerrain(Location(10,47), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2003_MapTrigger_61_33(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_6"] == 0: StuffDone["66_6"] = 1
        else: StuffDone["66_6"] = 0
        t = Town.TerrainAt(Location(59,31)).TransformTo
        Town.AlterTerrain(Location(59,31), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2004_MapTrigger_61_39(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(61,45)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_2005_MapTrigger_22_14(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(21,16)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_2006_MapTrigger_35_8(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_7"] == 0: StuffDone["66_7"] = 1
        else: StuffDone["66_7"] = 0
        t = Town.TerrainAt(Location(33,9)).TransformTo
        Town.AlterTerrain(Location(33,9), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2007_MapTrigger_27_4(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_8"] == 0: StuffDone["66_8"] = 1
        else: StuffDone["66_8"] = 0
        SuspendMapUpdate()
        for x in range(30, 33):
            for y in range(3, 4):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def GallowsKeep_2008_MapTrigger_49_6(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(49,5)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_2009_MapTrigger_49_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(49,30)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_2010_MapTrigger_49_16(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_9"] == 0: StuffDone["66_9"] = 1
        else: StuffDone["66_9"] = 0
        t = Town.TerrainAt(Location(42,22)).TransformTo
        Town.AlterTerrain(Location(42,22), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2011_MapTrigger_42_27(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["67_0"] == 0: StuffDone["67_0"] = 1
        else: StuffDone["67_0"] = 0
        SuspendMapUpdate()
        for x in range(45, 48):
            for y in range(25, 26):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2012_MapTrigger_54_33(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["66_1"] == 0: StuffDone["66_1"] = 1
        else: StuffDone["66_1"] = 0
        t = Town.TerrainAt(Location(54,31)).TransformTo
        Town.AlterTerrain(Location(54,31), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2013_MapTrigger_44_32(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(5,58))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_2014_MapTrigger_20_54(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(51,28))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def GallowsKeep_2015_MapTrigger_32_25(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(50,17)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_2016_MapTrigger_21_26(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["65_7"] == 0: StuffDone["65_7"] = 1
        else: StuffDone["65_7"] = 0
        t = Town.TerrainAt(Location(22,23)).TransformTo
        Town.AlterTerrain(Location(22,23), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2017_MapTrigger_28_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(50,26)
    Party.MoveToMap(TownMap.List["GallowsKeep_79"])

def GallowsKeep_2018_MapTrigger_34_38(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["65_6"] == 0: StuffDone["65_6"] = 1
        else: StuffDone["65_6"] = 0
        t = Town.TerrainAt(Location(32,35)).TransformTo
        Town.AlterTerrain(Location(32,35), 0, t)
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def GallowsKeep_2019_MapTrigger_30_28(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(29,28)).Num == 145:
        SuspendMapUpdate()
        for x in range(29, 36):
            for y in range(28, 29):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[142]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[145])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[145]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[142])
        ResumeMapUpdate()
        return

def GallowsKeep_2023_MapTrigger_32_29(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        return;
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(5,5))
        p.CancelAction = True
        Animation_Hold(-1, 004_bless)
        Wait()
        ChoiceBox("\"At last, everything is set! The instruments are prepared for activation. Soon the Empire will be inflicted with a permanent and irreversible plague that will ravage the land!\n\nAll that remains is one final protocol...\"", eDialogPic.STANDARD, 1028, ["OK"])
        ChoiceBox("\"Halt, Altrus! It is not enough that the Empire slowly decline, it must suffer the greatest possible damage. Only then will justice truly be served. I order you to reset the intensity setting to maximum!\"", eDialogPic.STANDARD, 1029, ["OK"])
        ChoiceBox("\"But Rentar, rest assured the Empire will fall. Such an intensity would truly be devastating. The entire surface world will perish! Hundreds of millions of people will die.\n\nI cannot follow that order Rentar.\"", eDialogPic.STANDARD, 1028, ["OK"])
        ChoiceBox("\"Altrus, you have four to five centuries of your life remaining whereas I have but a half century. I do not have time to wait centuries. I want to regain my glory within my lifetime.\n\nListen, if you do as I say I will immediately resign as director of Egli and appoint you my successor. Think, you shall have you wish sooner and just for one minor thing.\"", eDialogPic.STANDARD, 1029, ["OK"])
        ChoiceBox("\"There is nothing you can offer that will make me reset the intensity. Think of the consequences! If we do it with the normal intensity, the Empire will simply forget (or at least not care) until several centuries by now.\n\nBy then, the Empire will be too weak to possibly challenge our civilization. Whereas if we set the intensity to maximum, the Empire will have ten years. We will have literally pronounced their death sentence.\n\nWith nothing to lose, the Empire will strike at us with full force. Our magic may be superior, but they have many more than us. A full assault by the Empire would completely wipe us out.\n\nBesides, this machine is only set to respond to my influence. Just stand back and allow me to complete my work. Not even if you tried, you could not reconfigure the intensity.\"", eDialogPic.STANDARD, 1028, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if not npc.IsABaddie: Town.NPCList.Remove(npc)
        Town.PlaceEncounterGroup(1)
        Animation_Explosion(Location(4,7), 2, "005_explosion")
        Animation_Hold()
        Wait()
        ChoiceBox("Suddenly Rentar blasts Altrus with a bolt of energy, knocking him back. The crystal soul glows brightly as an eerie glow descends upon him. Altrus struggles to move, but he is trapped.\n\nRentar approaches the controls.\n\n\"I am afraid I cannot allow you to oppose me. Caffen-Bok has suffered permanent damage for so long due to the tortures received from the Empire. Once the Empire is destroyed, he can simply dissolve himself like the other two.\n\nThe Empire condemned three of our greatest to a prolonged slow death. I shall see that they receive the same punishment -- complete annihilation! Although these controls will take time to reconfigure, I can accomplish it.\n\nI must simply change the alteration restrictions which may take some time.\" Altrus tries harder to resist. Rentar simply grins darkly.\n\n\"Save your strength, you are no match for the great Caffen-Bok. Just sit back, for no one is going to help you.\"", eDialogPic.STANDARD, 1029, ["OK"])
        Animation_Hold(-1, 004_bless)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(24,37)
        Party.MoveToMap(TownMap.List["AttheGallows_81"])
        return

def GallowsKeep_2024_TownTimer_0(p):
    if StuffDone["65_3"] >= 8:
        return
    if StuffDone["65_3"] < 1:
        return
    StuffDone["65_3"] += 1
    if StuffDone["65_3"] == 250:
        TownMap.List["GallowsKeep_79"].DeactivateTrigger(Location(61,46))
    if StuffDone["65_3"] >= 4:
        if StuffDone["65_3"] >= 6:
            if StuffDone["65_3"] >= 8:
                return
            if StuffDone["65_3"] < 7:
                ChoiceBox("\"So then it will be approximately 400 years before the Empire falls. I see... Just out of curiosity, how does the maximum setting work?\"", eDialogPic.STANDARD, 1029, ["OK"])
                return
            ChoiceBox("\"The intensity of ten would be catastrophic. The release time is about ten years and the magnitude is about 250. Also, the poison would be so concentrated that it would eradicate all life.\n\nIn ten years, the surface world would become nothing more than a barren rock. All life shall become extinct. Even after the time period, life would have to be artificially planted from below. Nothing would survive.\n\nWith my current setting, there shall be a chance for life. Sure many may starve, but in about 250 years the Empire will notice something. The surface dwellers would have generations to prepare and minimize the suffering.\n\nThis could be accomplished by restricted breeding to match the decreasing crop yields. Currently the world supports several hundred million and could support many times that.\n\nI would estimate that the world in the post release should be able to support ten or twenty million at most. Life will be too harsh, rebellions will come, and the Empire shall fall. Rest assured that this setting is sufficient.\n\nNow the setting is almost complete. Soon I shall begin the activation protocols...\"", eDialogPic.STANDARD, 1028, ["OK"])
            return
        if StuffDone["65_3"] < 5:
            ChoiceBox("\"Of course Altrus. You shall receive what you have earned. Tell me about the intensity settings, Altrus. The planned setting, the parameters, the duration, and so forth.\"", eDialogPic.STANDARD, 1029, ["OK"])
            return
        ChoiceBox("\"The intensity is a scale of zero to ten. Zero has no effect and ten is the maximum. The intensity setting decides how fast the dark metal fuel is inserted into the node. My calculations indicate a ratio of 25 to 1.\n\nIn another words, if our intensity setting is to last for two hundred years. The radioactive poisoning will grow until the fuel will expires (two hundred years). Afterward, the effect will plateau for 25 times that amount.\n\nIn another words, the nodes upon the surface world shall remain poisoned for another 5000 years. After this time expires, the surface world would slowly return to normal.\n\nAs we lower the setting, the actual intensity of the irradiation decreases as well. A setting of one would take so long and be so thin that the effect would be minimal. That is why I have chosen a setting of 3.72.\n\nThe release takes about 400 years and the duration is about 10000. The actual intensity shall not turn the surface into a waste. Life will be very difficult, but possible. The Empire will surely lose its control and fall in such an environment.\n\nThey shall pay through a slow and long suffering.\"", eDialogPic.STANDARD, 1028, ["OK"])
        return
    if StuffDone["65_3"] < 3:
        return
    ChoiceBox("Meanwhile...\n\n\"At last, all of the devices are configured! Now I must simply specify the intensity setting and then activate the firing sequence. Victory is so close Rentar. Soon, your dignity shall be restored.\n\nAnd of course, I shall be guaranteed your chair...\"", eDialogPic.STANDARD, 1028, ["OK"])

def GallowsKeep_2025_OnEntry(p):
    if StuffDone["65_9"] == 1:
        t = Town.TerrainAt(Location(16,50)).TransformTo
        Town.AlterTerrain(Location(16,50), 0, t)
        if StuffDone["66_4"] == 1:
            t = Town.TerrainAt(Location(39,47)).TransformTo
            Town.AlterTerrain(Location(39,47), 0, t)
            if StuffDone["66_6"] == 1:
                t = Town.TerrainAt(Location(59,31)).TransformTo
                Town.AlterTerrain(Location(59,31), 0, t)
                if StuffDone["66_3"] == 1:
                    t = Town.TerrainAt(Location(10,47)).TransformTo
                    Town.AlterTerrain(Location(10,47), 0, t)
                    if StuffDone["66_7"] == 1:
                        t = Town.TerrainAt(Location(33,9)).TransformTo
                        Town.AlterTerrain(Location(33,9), 0, t)
                        if StuffDone["66_8"] == 1:
                            SuspendMapUpdate()
                            for x in range(30, 33):
                                for y in range(3, 4):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_9"] == 1:
                                t = Town.TerrainAt(Location(42,22)).TransformTo
                                Town.AlterTerrain(Location(42,22), 0, t)
                                if StuffDone["67_0"] == 1:
                                    SuspendMapUpdate()
                                    for x in range(45, 48):
                                        for y in range(25, 26):
                                            t = Town.TerrainAt(Location(x,y)).TransformTo
                                            Town.AlterTerrain(Location(x,y), 0, t)
                                    ResumeMapUpdate()
                                    if StuffDone["66_1"] == 1:
                                        t = Town.TerrainAt(Location(54,31)).TransformTo
                                        Town.AlterTerrain(Location(54,31), 0, t)
                                        if StuffDone["65_7"] == 1:
                                            t = Town.TerrainAt(Location(22,23)).TransformTo
                                            Town.AlterTerrain(Location(22,23), 0, t)
                                            return
                                        return
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_9"] == 1:
                            t = Town.TerrainAt(Location(42,22)).TransformTo
                            Town.AlterTerrain(Location(42,22), 0, t)
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_8"] == 1:
                        SuspendMapUpdate()
                        for x in range(30, 33):
                            for y in range(3, 4):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_9"] == 1:
                            t = Town.TerrainAt(Location(42,22)).TransformTo
                            Town.AlterTerrain(Location(42,22), 0, t)
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_7"] == 1:
                    t = Town.TerrainAt(Location(33,9)).TransformTo
                    Town.AlterTerrain(Location(33,9), 0, t)
                    if StuffDone["66_8"] == 1:
                        SuspendMapUpdate()
                        for x in range(30, 33):
                            for y in range(3, 4):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_9"] == 1:
                            t = Town.TerrainAt(Location(42,22)).TransformTo
                            Town.AlterTerrain(Location(42,22), 0, t)
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_3"] == 1:
                t = Town.TerrainAt(Location(10,47)).TransformTo
                Town.AlterTerrain(Location(10,47), 0, t)
                if StuffDone["66_7"] == 1:
                    t = Town.TerrainAt(Location(33,9)).TransformTo
                    Town.AlterTerrain(Location(33,9), 0, t)
                    if StuffDone["66_8"] == 1:
                        SuspendMapUpdate()
                        for x in range(30, 33):
                            for y in range(3, 4):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_9"] == 1:
                            t = Town.TerrainAt(Location(42,22)).TransformTo
                            Town.AlterTerrain(Location(42,22), 0, t)
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_7"] == 1:
                t = Town.TerrainAt(Location(33,9)).TransformTo
                Town.AlterTerrain(Location(33,9), 0, t)
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_6"] == 1:
            t = Town.TerrainAt(Location(59,31)).TransformTo
            Town.AlterTerrain(Location(59,31), 0, t)
            if StuffDone["66_3"] == 1:
                t = Town.TerrainAt(Location(10,47)).TransformTo
                Town.AlterTerrain(Location(10,47), 0, t)
                if StuffDone["66_7"] == 1:
                    t = Town.TerrainAt(Location(33,9)).TransformTo
                    Town.AlterTerrain(Location(33,9), 0, t)
                    if StuffDone["66_8"] == 1:
                        SuspendMapUpdate()
                        for x in range(30, 33):
                            for y in range(3, 4):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_9"] == 1:
                            t = Town.TerrainAt(Location(42,22)).TransformTo
                            Town.AlterTerrain(Location(42,22), 0, t)
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_7"] == 1:
                t = Town.TerrainAt(Location(33,9)).TransformTo
                Town.AlterTerrain(Location(33,9), 0, t)
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_3"] == 1:
            t = Town.TerrainAt(Location(10,47)).TransformTo
            Town.AlterTerrain(Location(10,47), 0, t)
            if StuffDone["66_7"] == 1:
                t = Town.TerrainAt(Location(33,9)).TransformTo
                Town.AlterTerrain(Location(33,9), 0, t)
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_7"] == 1:
            t = Town.TerrainAt(Location(33,9)).TransformTo
            Town.AlterTerrain(Location(33,9), 0, t)
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_8"] == 1:
            SuspendMapUpdate()
            for x in range(30, 33):
                for y in range(3, 4):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_9"] == 1:
            t = Town.TerrainAt(Location(42,22)).TransformTo
            Town.AlterTerrain(Location(42,22), 0, t)
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_4"] == 1:
        t = Town.TerrainAt(Location(39,47)).TransformTo
        Town.AlterTerrain(Location(39,47), 0, t)
        if StuffDone["66_6"] == 1:
            t = Town.TerrainAt(Location(59,31)).TransformTo
            Town.AlterTerrain(Location(59,31), 0, t)
            if StuffDone["66_3"] == 1:
                t = Town.TerrainAt(Location(10,47)).TransformTo
                Town.AlterTerrain(Location(10,47), 0, t)
                if StuffDone["66_7"] == 1:
                    t = Town.TerrainAt(Location(33,9)).TransformTo
                    Town.AlterTerrain(Location(33,9), 0, t)
                    if StuffDone["66_8"] == 1:
                        SuspendMapUpdate()
                        for x in range(30, 33):
                            for y in range(3, 4):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_9"] == 1:
                            t = Town.TerrainAt(Location(42,22)).TransformTo
                            Town.AlterTerrain(Location(42,22), 0, t)
                            if StuffDone["67_0"] == 1:
                                SuspendMapUpdate()
                                for x in range(45, 48):
                                    for y in range(25, 26):
                                        t = Town.TerrainAt(Location(x,y)).TransformTo
                                        Town.AlterTerrain(Location(x,y), 0, t)
                                ResumeMapUpdate()
                                if StuffDone["66_1"] == 1:
                                    t = Town.TerrainAt(Location(54,31)).TransformTo
                                    Town.AlterTerrain(Location(54,31), 0, t)
                                    if StuffDone["65_7"] == 1:
                                        t = Town.TerrainAt(Location(22,23)).TransformTo
                                        Town.AlterTerrain(Location(22,23), 0, t)
                                        return
                                    return
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_7"] == 1:
                t = Town.TerrainAt(Location(33,9)).TransformTo
                Town.AlterTerrain(Location(33,9), 0, t)
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_3"] == 1:
            t = Town.TerrainAt(Location(10,47)).TransformTo
            Town.AlterTerrain(Location(10,47), 0, t)
            if StuffDone["66_7"] == 1:
                t = Town.TerrainAt(Location(33,9)).TransformTo
                Town.AlterTerrain(Location(33,9), 0, t)
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_7"] == 1:
            t = Town.TerrainAt(Location(33,9)).TransformTo
            Town.AlterTerrain(Location(33,9), 0, t)
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_8"] == 1:
            SuspendMapUpdate()
            for x in range(30, 33):
                for y in range(3, 4):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_9"] == 1:
            t = Town.TerrainAt(Location(42,22)).TransformTo
            Town.AlterTerrain(Location(42,22), 0, t)
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_6"] == 1:
        t = Town.TerrainAt(Location(59,31)).TransformTo
        Town.AlterTerrain(Location(59,31), 0, t)
        if StuffDone["66_3"] == 1:
            t = Town.TerrainAt(Location(10,47)).TransformTo
            Town.AlterTerrain(Location(10,47), 0, t)
            if StuffDone["66_7"] == 1:
                t = Town.TerrainAt(Location(33,9)).TransformTo
                Town.AlterTerrain(Location(33,9), 0, t)
                if StuffDone["66_8"] == 1:
                    SuspendMapUpdate()
                    for x in range(30, 33):
                        for y in range(3, 4):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_9"] == 1:
                        t = Town.TerrainAt(Location(42,22)).TransformTo
                        Town.AlterTerrain(Location(42,22), 0, t)
                        if StuffDone["67_0"] == 1:
                            SuspendMapUpdate()
                            for x in range(45, 48):
                                for y in range(25, 26):
                                    t = Town.TerrainAt(Location(x,y)).TransformTo
                                    Town.AlterTerrain(Location(x,y), 0, t)
                            ResumeMapUpdate()
                            if StuffDone["66_1"] == 1:
                                t = Town.TerrainAt(Location(54,31)).TransformTo
                                Town.AlterTerrain(Location(54,31), 0, t)
                                if StuffDone["65_7"] == 1:
                                    t = Town.TerrainAt(Location(22,23)).TransformTo
                                    Town.AlterTerrain(Location(22,23), 0, t)
                                    return
                                return
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_7"] == 1:
            t = Town.TerrainAt(Location(33,9)).TransformTo
            Town.AlterTerrain(Location(33,9), 0, t)
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_8"] == 1:
            SuspendMapUpdate()
            for x in range(30, 33):
                for y in range(3, 4):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_9"] == 1:
            t = Town.TerrainAt(Location(42,22)).TransformTo
            Town.AlterTerrain(Location(42,22), 0, t)
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_3"] == 1:
        t = Town.TerrainAt(Location(10,47)).TransformTo
        Town.AlterTerrain(Location(10,47), 0, t)
        if StuffDone["66_7"] == 1:
            t = Town.TerrainAt(Location(33,9)).TransformTo
            Town.AlterTerrain(Location(33,9), 0, t)
            if StuffDone["66_8"] == 1:
                SuspendMapUpdate()
                for x in range(30, 33):
                    for y in range(3, 4):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_9"] == 1:
                    t = Town.TerrainAt(Location(42,22)).TransformTo
                    Town.AlterTerrain(Location(42,22), 0, t)
                    if StuffDone["67_0"] == 1:
                        SuspendMapUpdate()
                        for x in range(45, 48):
                            for y in range(25, 26):
                                t = Town.TerrainAt(Location(x,y)).TransformTo
                                Town.AlterTerrain(Location(x,y), 0, t)
                        ResumeMapUpdate()
                        if StuffDone["66_1"] == 1:
                            t = Town.TerrainAt(Location(54,31)).TransformTo
                            Town.AlterTerrain(Location(54,31), 0, t)
                            if StuffDone["65_7"] == 1:
                                t = Town.TerrainAt(Location(22,23)).TransformTo
                                Town.AlterTerrain(Location(22,23), 0, t)
                                return
                            return
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_8"] == 1:
            SuspendMapUpdate()
            for x in range(30, 33):
                for y in range(3, 4):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_9"] == 1:
            t = Town.TerrainAt(Location(42,22)).TransformTo
            Town.AlterTerrain(Location(42,22), 0, t)
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_7"] == 1:
        t = Town.TerrainAt(Location(33,9)).TransformTo
        Town.AlterTerrain(Location(33,9), 0, t)
        if StuffDone["66_8"] == 1:
            SuspendMapUpdate()
            for x in range(30, 33):
                for y in range(3, 4):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_9"] == 1:
                t = Town.TerrainAt(Location(42,22)).TransformTo
                Town.AlterTerrain(Location(42,22), 0, t)
                if StuffDone["67_0"] == 1:
                    SuspendMapUpdate()
                    for x in range(45, 48):
                        for y in range(25, 26):
                            t = Town.TerrainAt(Location(x,y)).TransformTo
                            Town.AlterTerrain(Location(x,y), 0, t)
                    ResumeMapUpdate()
                    if StuffDone["66_1"] == 1:
                        t = Town.TerrainAt(Location(54,31)).TransformTo
                        Town.AlterTerrain(Location(54,31), 0, t)
                        if StuffDone["65_7"] == 1:
                            t = Town.TerrainAt(Location(22,23)).TransformTo
                            Town.AlterTerrain(Location(22,23), 0, t)
                            return
                        return
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_9"] == 1:
            t = Town.TerrainAt(Location(42,22)).TransformTo
            Town.AlterTerrain(Location(42,22), 0, t)
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_8"] == 1:
        SuspendMapUpdate()
        for x in range(30, 33):
            for y in range(3, 4):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        if StuffDone["66_9"] == 1:
            t = Town.TerrainAt(Location(42,22)).TransformTo
            Town.AlterTerrain(Location(42,22), 0, t)
            if StuffDone["67_0"] == 1:
                SuspendMapUpdate()
                for x in range(45, 48):
                    for y in range(25, 26):
                        t = Town.TerrainAt(Location(x,y)).TransformTo
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                if StuffDone["66_1"] == 1:
                    t = Town.TerrainAt(Location(54,31)).TransformTo
                    Town.AlterTerrain(Location(54,31), 0, t)
                    if StuffDone["65_7"] == 1:
                        t = Town.TerrainAt(Location(22,23)).TransformTo
                        Town.AlterTerrain(Location(22,23), 0, t)
                        return
                    return
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_9"] == 1:
        t = Town.TerrainAt(Location(42,22)).TransformTo
        Town.AlterTerrain(Location(42,22), 0, t)
        if StuffDone["67_0"] == 1:
            SuspendMapUpdate()
            for x in range(45, 48):
                for y in range(25, 26):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["66_1"] == 1:
                t = Town.TerrainAt(Location(54,31)).TransformTo
                Town.AlterTerrain(Location(54,31), 0, t)
                if StuffDone["65_7"] == 1:
                    t = Town.TerrainAt(Location(22,23)).TransformTo
                    Town.AlterTerrain(Location(22,23), 0, t)
                    return
                return
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["67_0"] == 1:
        SuspendMapUpdate()
        for x in range(45, 48):
            for y in range(25, 26):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        if StuffDone["66_1"] == 1:
            t = Town.TerrainAt(Location(54,31)).TransformTo
            Town.AlterTerrain(Location(54,31), 0, t)
            if StuffDone["65_7"] == 1:
                t = Town.TerrainAt(Location(22,23)).TransformTo
                Town.AlterTerrain(Location(22,23), 0, t)
                return
            return
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["66_1"] == 1:
        t = Town.TerrainAt(Location(54,31)).TransformTo
        Town.AlterTerrain(Location(54,31), 0, t)
        if StuffDone["65_7"] == 1:
            t = Town.TerrainAt(Location(22,23)).TransformTo
            Town.AlterTerrain(Location(22,23), 0, t)
            return
        return
    if StuffDone["65_7"] == 1:
        t = Town.TerrainAt(Location(22,23)).TransformTo
        Town.AlterTerrain(Location(22,23), 0, t)
        return

def TerrainTypeStepOn_Mist_GallowsKeep_2906(p):
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 2))
