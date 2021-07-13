
def Malachite_1457_MapTrigger_28_24(p):
    if StuffDone["17_3"] >= 3:
        if StuffDone["17_3"] < 10:
            Town.AlterTerrain(Location(28,20), 0, TerrainRecord.UnderlayList[142])
            return
        return

def Malachite_1458_MapTrigger_28_21(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(28,20)).Num == 145:
        MessageBox("The sign on the door says, \"CURRENTLY UNAVAILABLE.\"")
        return

def Malachite_1459_MapTrigger_11_35(p):
    if StuffDone["17_3"] < 8:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The door is locked. A sign reads, \"NO ADMITTANCE -- EXPERIMENT IN PROGRESS!\"")
        return
    if StuffDone["19_4"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The guard stops you. \"I\'m sorry. You are not authorized to enter the crime scene. You must speak with Borazi first.\"")
        return
    if StuffDone["19_5"] == 250:
        return
    StuffDone["19_5"] = 250
    ChoiceBox("With authorization, the guards allow you to enter the lab. You immediately look to the southern end of the room, where you see young men and women slouched on the tables, dead.\n\nOn each table is the dissected body of a Giant Spider, just left unattended. Various tools such as probes and scalpels lie on the table and in the hands of the murdered students.\n\nThis entire place is quite creepy. Perhaps you should have a closer look.", eDialogPic.TERRAIN, 179, ["OK"])

def Malachite_1461_MapTrigger_11_40(p):
    if StuffDone["19_6"] == 0:
        MessageBox("You examine one of the bodies. It looks very similar to the one you saw under dissection (except this one\'s not cut up). The face is frozen in an expression of sheer agony and the pupils of the eyes are severely dilated.\n\nOtherwise, this killing was done quite cleanly. Clean like the rest of the disappearances. You wonder if there is any connections between this massacre and the abductions.")
        StuffDone["19_6"] = 1
        Timer(Town, 2, False, "Malachite_1468_TownTimer_17", eTimerType.DELETE)
        return

def Malachite_1465_MapTrigger_14_28(p):
    if StuffDone["17_3"] >= 8:
        if StuffDone["17_3"] < 10:
            Town.PlaceEncounterGroup(3)
            return
        return

def Malachite_1466_MapTrigger_28_20(p):
    if StuffDone["17_3"] >= 8:
        Town.PlaceEncounterGroup(4)
        return

def Malachite_1468_TownTimer_17(p):
    Animation_Hold(-1, 051_magic1)
    Wait()
    Message("A Ghost appears!")
    Town.PlaceEncounterGroup(2)

def Malachite_1469_OnEntry(p):
    if StuffDone["17_3"] >= 3:
        Town.PlaceEncounterGroup(1)
        return

def Malachite_1470_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(37, 31),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(36, 32),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(37, 32),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(37, 32),WorldMap.SectorAt(Party.OutsidePos))

def Malachite_1471_TalkingTrigger17(p):
    if StuffDone["56_3"] == 0:
        StuffDone["56_3"] = 1
        StuffDone["17_3"] += 1
        if StuffDone["17_3"] == 250:
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(19,56))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(17,55))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(15,20))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(17,20))
            TownMap.List["ZarmondsHut_39"].DeactivateTrigger(Location(20,14))
            TownMap.List["ZarmondsHut_39"].DeactivateTrigger(Location(16,9))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(56,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(55,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(57,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(50,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(52,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(53,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(55,16))
            TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(24,33))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(28,24))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(11,35))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(11,36))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(14,28))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(28,20))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(15,28))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(56,33))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(29,51))
            TownMap.List["ForgottenAcademy_60"].AlterTerrain(Location(4,13), 1, None)
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(4,13))
            TownMap.List["ForgottenAcademy_60"].AlterTerrain(Location(5,13), 1, None)
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(5,13))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(4,10))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(5,10))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(3,4))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(9,11))
        ChoiceBox("\"This philote detector can detect philotes in close proximity to the lab. Events like teleportation involves a massive transfer of philotes which this detector will register.\n\nI remember watching the detector taking note of the occasional sparking that you see. Suddenly, the sparking became more and more rapid over a few minutes before the occurrence. I didn\'t think much of it as this occasionally does happen.\n\nHowever, the mechanism suddenly went haywire with flashes everywhere! As I left this room to find Dr. Jenkins I saw a flash of light out of the corner of my eye. I turned to see the figure of a person vanish before my eyes!\n\nI went and got Dr. Jenkins and we came back to the lab together. The philote detector appeared to have settled down and Sapphire was no where to be found. We contacted the administrator who presumably contacted you guys.\n\nI\'m sorry I cannot be of more help, but this is all I know.\"", eDialogPic.CREATURE, 26, ["OK"])
        return

def Malachite_1472_TalkingTrigger23(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Ghost_61": Town.NPCList.Remove(npc)
    ChoiceBox("\"I have come to deliver a warning from my masters. This killing is only a taste of what will come if you continue to meddle in our affairs. More and more innocents will perish until you stop the crusade against us.\n\nWe do what we do with the greater interests in mind. Some lives must be sacrificed for the greater good. That is the way it has been and is the way it shall be. You are not to interfere further in these proceedings, is that understood?\n\nLest you do, more examples of this incident will arise until you cease.\"", eDialogPic.CREATURE, 43, ["OK"])
    StuffDone["17_3"] = 9
    StuffDone["19_6"] = 2

def Malachite_1473_TalkingTrigger28(p):
    if StuffDone["17_3"] >= 12:
        p.TalkingText = "You give him the tablets to analyze. He looks them over for several minutes. \"Interesting, but not overly important. I\'m fairly certain that these are just administrative announcements. Nothing more.\""
        return

def Malachite_1474_TalkingTrigger33(p):
    if StuffDone["17_3"] >= 12:
        if StuffDone["17_3"] < 13:
            ChoiceBox("You show him the tablets. His eyes grow wide upon seeing them. \"Ah yes! These are in old Imperial tongue, my personal specialty. Give me a few minutes to analyze them please.\" He carefully looks them over and looks up at you.\n\n\"Amazing! Where did you get these?\" You tell him. \"Wow! It gives a complete description of the old school, almost a kind of map.\" He begins to tell you about the old workings of the school, reading off the tablet.\n\nWhen he gets to the second level, it peaks your interest. You do not remember seeing any reference to a second level. You ask him about it. \"Ah, yes.\" He looks for it in the tablet. \"To get there, you have to go into the passage in the northeast section.\"\n\nYou ask for more information. He shifts to another tablet and begins to decipher. \"It appears that was the main area of experimentation and research. The area you were in was just a bunch of classrooms and such.\"\n\nSuddenly he thinks. \"Oh dear! I had better finish up this lunch or I\'m going to be late for class. I hope I was of assistance.\"\n\nYou take back the tablets. Strange, you wonder why the \'expert\' did not catch this. You have a feeling someone is going to great lengths to keep the ruins shrouded in mystery. Perhaps you should check out the second floor of the ruins.", eDialogPic.TERRAIN, 125, ["OK"])
            StuffDone["17_3"] = 13
            StuffDone["19_9"] = 1
            return
        return
    p.TalkingText = "\"I don\'t believe I\'ve learned about that yet.\""
