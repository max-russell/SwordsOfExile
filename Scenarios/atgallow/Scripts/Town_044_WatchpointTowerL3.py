
def WatchpointTowerL3_1026_MapTrigger_24_24(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["23_5"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(24,9))
        p.CancelAction = True
        ChoiceBox("Suddenly, you are surrounded by a thick black fog. You can see nothing around you and will have to wander around blindly. You can barely even see your own hands let alone each other.\n\nYou hear Astervis say, \"This is really starting to get spooky. There is definitely something here...\"", eDialogPic.STANDARD, 0, ["OK"])
        Timer(Town, 10, False, "WatchpointTowerL3_1053_TownTimer_5", eTimerType.DELETE)
        return

def WatchpointTowerL3_1028_MapTrigger_24_8(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(25,8)).Num == 216:
        if StuffDone["23_5"] == 0:
            StuffDone["23_5"] = 1
            SuspendMapUpdate()
            for x in range(23, 26):
                for y in range(5, 8):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
            ResumeMapUpdate()
            Town.AlterTerrain(Location(24,6), 0, TerrainRecord.UnderlayList[215])
            Town.PlaceEncounterGroup(1)
            Animation_Explosion(Location(24,6), 2, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("Finally, after a show of lights the feared figure of Morbane appears! He is sitting in his chair, completely still, and radiating darkness. His eyes glow red as the voice you remember from Fort Nether all too well booms out.\n\n\"At last, you have come.\" Astervis looks quite afraid, but asks, \"Why have you done all of this?\"  Morbane replies, \"For over a millennium I have been imprisoned. I have finally been able to return. I will make the world the way it was supposed to be!\"\n\n\"How? Killing people? Taking their minds away. I sure don\'t think it\'s better!\" Morbane answers, \"Ah, but you do not understand. I need strength after so many years. I must harvest the life force of others so I can do my work.\"\n\nAstervis questions, \"And what will this work of yours accomplish?\" Morbane answers, \"For twelve centuries, the world has been ruled by those unworthy. I shall restore the great Empire\'s dream! Sure there are costs now. But good things shall come!\n\nI shall transform this world into one of peace, order, and even greater prosperity!\" Astervis retorts, \"Yeah! But who gives YOU the authority!?\" Morbane laughs. \"It is my birthright as true eternal ruler of Ermarian!\n\nNow join with me. You can be princes and princesses in my new world...\" Astervis shouts out, \"Never! We will not let you continue.\" Morbane\'s figure becomes very dark. \"Then I must remove you, I\'m afraid.\"", eDialogPic.CREATURE, 60, ["OK"])
            ChoiceBox("Morbane raises his skeletal arms and pure dark energy flows from his hands into your bodies! You are being drained of your life force. Trying as much as you can, there is nothing you can do. There is too much pain.\n\nAstervis is trying to cast a spell. He shouts with agony, \"Take that!\" A large explosive fireball moves out from his hands toward Morbane...", eDialogPic.STANDARD, 4, ["OK"])
            Animation_Explosion(Location(24,6), 0, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("The fireball misses Morbane completely and strikes the ceiling! You think all is lost until the pain suddenly stops. You hear an echoing yell throughout the room. You look at Morbane to see his body emitting a black smoke.\n\nAstervis\'s fireball missed Morbane, but created a whole in the ceiling. The bright sunlight shines through, right on Morbane. Sunlight! That must be Morbane\'s weakness!\n\nSuddenly, the skeletal body moves out of the rays of sunlight to safety. It clearly looks severely damaged. It begins to glow a brilliant white, getting brighter and brighter. Then there is an amazing flash! Morbane is gone.\n\nHowever, Morbane\'s voice booms out. \"This time you were lucky. But it is not over yet. I shall eventually prevail!\" And then, he is gone. All that is left is the thick, acrid, black smoke and some ashes.\n\nYou are all beginning to recover the whole ordeal. Astervis, laying on the ground along with the rest of you, turns to you and smiles, \"He\'s escaped, but we\'ve won!\"\n\nAfter more recovery, you think you have enough strength to walk again and stand victorious. Time to return and tell of your deeds here.", eDialogPic.CREATURE, 60, ["OK"])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Morbane_203": Town.NPCList.Remove(npc)
            Party.HealAll(-250)
            for pc in Party.EachAlivePC():
                pc.SP-= 150
            StuffDone["17_3"] = 28
            Town.AlterTerrain(Location(24,13), 0, TerrainRecord.UnderlayList[125])
            StuffDone["23_6"] = 1
            return
        return

def WatchpointTowerL3_1029_MapTrigger_21_6(p):
    p.CancelAction = True

def WatchpointTowerL3_1037_MapTrigger_23_5(p):
    if StuffDone["23_5"] == 0:
        p.CancelAction = True
        return

def WatchpointTowerL3_1044_MapTrigger_24_38(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,36)
    Party.MoveToMap(TownMap.List["WatchpointTowerL2_43"])

def WatchpointTowerL3_1046_MapTrigger_5_9(p):
    if StuffDone["27_2"] == 0:
        result = ChoiceBox("You open this chest and wrapped in velvet is a small golden glowing disc with a diameter of about ten centimeters. It has strange writing that you do not recognize on one side and on the other is a sketch of a nephil shaman.\n\nYou have no idea what the purpose of the disc is, but it could be valuable to some nephilim tribe or something. Do you take it?", eDialogPic.TERRAIN, 138, ["Leave", "Take"])
        if result == 1:
            StuffDone["27_2"] = 1
            SpecialItem.Give("GlowingDisc")
            return
        return

def WatchpointTowerL3_1047_MapTrigger_6_9(p):
    if StuffDone["27_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["27_3"] = 250
    TownMap.List["WatchpointTowerL3_44"].DeactivateTrigger(Location(6,9))
    pc.RunTrap(eTrapType.DART, 2, 60)

def WatchpointTowerL3_1048_MapTrigger_5_29(p):
    ChoiceBox("This monument is dedicated to those who are prominent members of the Blades community.\n\nNames listed are: Aceron, Alcritas, Brett Bixler, Ben Frank, Drizzt, and Zaloopa.", eDialogPic.TERRAIN, 133, ["OK"])

def WatchpointTowerL3_1049_MapTrigger_12_29(p):
    ChoiceBox("This monument is dedicated to those who beta tested this scenario.\n\nNames listed are: Jamie Clark, Luz Piazuelo, Ryan Phelps, Morgan Wild, Jayne Holt, Terrors Martyr, and Imban.", eDialogPic.TERRAIN, 133, ["OK"])

def WatchpointTowerL3_1050_MapTrigger_7_29(p):
    ChoiceBox("This monument is dedicated to those first twenty players who have completed the game.\n\nAlcritas, Bruce Mitchell, Janet Cone\n\n[THIS BRANCH IS STILL OPEN]", eDialogPic.TERRAIN, 133, ["OK"])

def WatchpointTowerL3_1051_MapTrigger_10_29(p):
    ChoiceBox("This monument is dedicated to those first five players who managed to discover the recipes for the weak, medium, and strong skill potions, and find the workstation to produce them.\n\nNo names are currently listed as of version 1.0.1.\n\n[THIS BRANCH IS STILL OPEN]", eDialogPic.TERRAIN, 133, ["OK"])

def WatchpointTowerL3_1052_MapTrigger_28_37(p):
    ChoiceBox("This is the journal of the (former) leader of the Order of Watchpoint. It details the plans of developing the perfect magical barrier to be used in the holy war of Morbane that will forever purge the world of all suffering.\n\nIt also speaks of the teleportation snare within the forgotten academy that was used to capture mages. Morbane used the essence of these mages to further enhance his own powers in preparation for the strike.\n\nIt speaks of enlisting the service of the Imperial mage (Odix) responsible for the investigation of the vanishing mages to ensure that the order\'s true purposes are not discovered.\n\nThere is also reference to you. At first it does not seem the author did not think you a minor threat. However, when you uncovered the ruined school, efforts were made to prevent you from progressing.\n\nThese ranged from the capturing of Zarmond\'s soul, to influencing the mind of the archaeology professor in Malachite, up until the final defenses of this tower by your assault.\n\nThe last line reads, \"Our defenses will surely stop them! We cannot fail!\" He was obviously wrong.", eDialogPic.CREATURE, 60, ["OK"])

def WatchpointTowerL3_1053_TownTimer_5(p):
    SuspendMapUpdate()
    for x in range(20, 23):
        for y in range(5, 8):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    Town.AlterTerrain(Location(21,6), 0, TerrainRecord.UnderlayList[214])
    Animation_Explosion(Location(21,6), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Timer(Town, 10, False, "WatchpointTowerL3_1054_TownTimer_9", eTimerType.DELETE)

def WatchpointTowerL3_1054_TownTimer_9(p):
    SuspendMapUpdate()
    for x in range(25, 29):
        for y in range(10, 13):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    Town.AlterTerrain(Location(26,11), 0, TerrainRecord.UnderlayList[214])
    Animation_Explosion(Location(26,11), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Timer(Town, 7, False, "WatchpointTowerL3_1055_TownTimer_13", eTimerType.DELETE)

def WatchpointTowerL3_1055_TownTimer_13(p):
    SuspendMapUpdate()
    for x in range(26, 29):
        for y in range(7, 10):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    SuspendMapUpdate()
    for x in range(25, 26):
        for y in range(8, 10):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    Town.AlterTerrain(Location(27,8), 0, TerrainRecord.UnderlayList[214])
    Animation_Explosion(Location(27,8), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Timer(Town, 13, False, "WatchpointTowerL3_1056_TownTimer_17", eTimerType.DELETE)

def WatchpointTowerL3_1056_TownTimer_17(p):
    SuspendMapUpdate()
    for x in range(20, 25):
        for y in range(10, 13):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    Town.AlterTerrain(Location(22,11), 0, TerrainRecord.UnderlayList[214])
    Animation_Explosion(Location(22,11), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Timer(Town, 8, False, "WatchpointTowerL3_1057_TownTimer_22", eTimerType.DELETE)

def WatchpointTowerL3_1057_TownTimer_22(p):
    SuspendMapUpdate()
    for x in range(20, 25):
        for y in range(8, 10):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    Town.AlterTerrain(Location(21,8), 0, TerrainRecord.UnderlayList[214])
    Animation_Explosion(Location(21,8), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Timer(Town, 15, False, "WatchpointTowerL3_1058_TownTimer_26", eTimerType.DELETE)

def WatchpointTowerL3_1058_TownTimer_26(p):
    SuspendMapUpdate()
    for x in range(26, 29):
        for y in range(5, 7):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[210]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[179]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[210])
    ResumeMapUpdate()
    Town.AlterTerrain(Location(27,6), 0, TerrainRecord.UnderlayList[214])
    Animation_Explosion(Location(27,6), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Timer(Town, 4, False, "WatchpointTowerL3_1059_TownTimer_30", eTimerType.DELETE)

def WatchpointTowerL3_1059_TownTimer_30(p):
    Town.AlterTerrain(Location(23,8), 0, TerrainRecord.UnderlayList[216])
    Town.AlterTerrain(Location(25,8), 0, TerrainRecord.UnderlayList[216])
    Animation_Hold(-1, 053_magic3)
    Wait()

def TerrainTypeStepOn_Mist_WatchpointTowerL3_2903(p):
    return
