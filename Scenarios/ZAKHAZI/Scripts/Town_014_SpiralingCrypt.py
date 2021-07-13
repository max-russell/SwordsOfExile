def Generate_Wandering_14_SpiralingCrypt(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["IcyShade_193"]])
            npcs.append([1,NPCRecord.List["IcyShade_193"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["CryptGuardian_194"]])
            npcs.append([1,NPCRecord.List["CryptGuardian_194"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["CryptGuardian_194"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["IcyShade_193"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(26,22)
                elif r2 == 1: l = Location(5,24)
                elif r2 == 2: l = Location(8,10)
                elif r2 == 3: l = Location(21,10)
                
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

def SpiralingCrypt_288_MapTrigger_11_8(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(7,12))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def SpiralingCrypt_293_MapTrigger_10_7(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(18,25))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def SpiralingCrypt_299_MapTrigger_6_7(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(11,23))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def SpiralingCrypt_304_MapTrigger_27_27(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(19,28)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_307_MapTrigger_26_10(p):
    if StuffDone["14_0"] == 250:
        return
    StuffDone["14_0"] = 250
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(26,10))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(23,9))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(22,8))
    MessageBox("An icy wind blows through the room.")
    Town.PlaceEncounterGroup(1)

def SpiralingCrypt_309_MapTrigger_4_27(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(2,19)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_311_MapTrigger_9_12(p):
    if StuffDone["14_1"] == 250:
        return
    StuffDone["14_1"] = 250
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(9,12))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(7,8))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(6,11))
    MessageBox("You catch a blur out of the corner of your eye. Turning, you see that a snarling creature has suddenly appeared. Looking around, you see that it isn\'t the only one ...")
    Town.PlaceEncounterGroup(2)

def SpiralingCrypt_314_MapTrigger_4_7(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(11,2)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_315_MapTrigger_6_22(p):
    if StuffDone["14_2"] == 250:
        return
    StuffDone["14_2"] = 250
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(6,22))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(8,24))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(11,25))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(5,21))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(9,21))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(9,25))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(9,27))
    MessageBox("Something in this room feels different. You feel as if you\'re being watched.")
    Town.PlaceEncounterGroup(3)

def SpiralingCrypt_322_MapTrigger_24_21(p):
    if StuffDone["14_3"] == 250:
        return
    StuffDone["14_3"] = 250
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(24,21))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(24,23))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(25,26))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(22,27))
    MessageBox("You hear loud snarling. Looking into the shadows of the chamber, you see several savage beasts staring at you. You\'re sure that they weren\'t there before. They attack ...")
    Town.PlaceEncounterGroup(4)

def SpiralingCrypt_325_MapTrigger_27_7(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(28,11)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_327_MapTrigger_18_9(p):
    if StuffDone["14_4"] == 250:
        return
    StuffDone["14_4"] = 250
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(18,9))
    TownMap.List["SpiralingCrypt_14"].DeactivateTrigger(Location(13,9))
    MessageBox("You finally reach the crypt\'s stone docks. There are two funeral biers chained here. The wide, flat boats are made of cavewood, surprisingly intact despite the many years they\'ve been here. Steering poles are lashed to the sides.\n\nA barge is a slow, inelegant way to make your way downriver. However, considering the circumstances, they\'re much, much better than turning back.")

def SpiralingCrypt_329_MapTrigger_7_20(p):
    result = ChoiceBox("You carefully examine the pillar. Looking at the stone carefully, you notice that what had at first looked like a few cracks are, in fact, the edges of a small panel.\n\nUsing a knife, you pry the panel open. There is a large, inviting red button behind it.", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        MessageBox("You press the button. You hear a distant hum. Nothing else of interest happens.")
        if StuffDone["14_5"] == 0: StuffDone["14_5"] = 1
        else: StuffDone["14_5"] = 0
        return

def SpiralingCrypt_330_MapTrigger_15_17(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(15,26))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def SpiralingCrypt_334_MapTrigger_22_23(p):
    MessageBox("You hear a distant clang.")

def SpiralingCrypt_337_MapTrigger_23_13(p):
    for x in range(20, 28):
        for y in range(7, 15):
            Town.PlaceField(Location(x,y), Field.SLEEP_CLOUD)

def SpiralingCrypt_338_OnEntry(p):
    if StuffDone["15_0"] >= 1:
        Town.AlterTerrain(Location(13,10), 0, TerrainRecord.UnderlayList[0])
        Town.AlterTerrain(Location(18,10), 0, TerrainRecord.UnderlayList[0])
        return
