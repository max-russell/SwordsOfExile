
def FieldofBattle_445_MapTrigger_6_55(p):
    if StuffDone["18_6"] == 250:
        return
    result = ChoiceBox("These beds are reserved for you, to insure you are fully rested when the sliths strike here. Locke assures you he will wake you if they arrive.", eDialogPic.TERRAIN, 143, ["Leave", "Rest"])
    if result == 1:
        StuffDone["18_6"] = 250
        TownMap.List["FieldofBattle_18"].AlterTerrain(Location(6,55), 1, None)
        TownMap.List["FieldofBattle_18"].DeactivateTrigger(Location(6,55))
        if Game.Mode != eMode.COMBAT:
            Party.Age += 200
            Party.HealAll(100)
            Party.RestoreSP(100)
        if StuffDone["18_9"] == 250:
            return
        result = ChoiceBox("You soon fall into exhausted sleep. For some time you drift aimlessly around in the world of dreams. Then you are drawn together by the sound of a commercial jingle.\n\nA shining portal opens before you, radiant light streaming out, and you hear a rough, masculine voice speak: \"Exile will be back shortly\". Do you enter the gateway of Commercials?", eDialogPic.STANDARD, 22, ["Step In", "Refuse"])
        if result == 0:
            StuffDone["18_9"] = 250
            StuffDone["18_7"] = 1
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(20,11)
            Party.MoveToMap(TownMap.List["CommercialBreak_20"])
            return
        elif result == 1:
            StuffDone["18_9"] = 250
            if StuffDone["18_3"] == 250:
                return
            StuffDone["18_3"] = 250
            MessageBox("You sleep fitfully, trusting in your guards. Several hours must have passed when a soldier bursts into the room. \"They?re coming! They?re coming! The northern outposts have been overrun!\" He runs out, almost in panic. You try to remain calm.")
            Town.PlaceEncounterGroup(1)
            return
        return

def FieldofBattle_446_MapTrigger_18_59(p):
    if StuffDone["18_4"] >= 1:
        return
    MessageBox("\"Please, don?t go too far. The reports say that the sliths have already struck at our northern outposts. They may arrive at any moment.\" The expression of the guard is friendly, but you feel it is safer not to cross him. You return to the square.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(17,50))
    p.CancelAction = True

def FieldofBattle_453_TownTimer_0(p):
    if StuffDone["18_1"] >= 12:
        if StuffDone["18_8"] == 250:
            return
        StuffDone["18_8"] = 250
        WorldMap.AlterTerrain(Location(85,62), 1, None)
        WorldMap.DeactivateTrigger(Location(85,62))
        ChoiceBox("The situation is getting desperate. At first, the battle seemed to be going well. Under the cover of the Cave Archers, you kept the first line of attackers at bay.\n\nBut when the slith mages arrived, burning a path for the deadly spears of the slith Dervishes, you understood which way this was going.\n\nOne by one, the soldiers fall around you, until you feel like you are the only ones left standing in a sea of corpses.\n\nThen you hear screams from the lines of the sliths. A Dervish falls with an arrow through his neck, then another. Slith mages and priests run screaming from a hail of barbed arrows of a design everyone in Chimney knows: Nephilim.\n\nPowerful feline shapes arrive around the house corners, brandishing their scimitars and striking fear into their enemies. You sag to the ground in exhaustion. It is over. And you owe your lives to the Cat Paw mercenaries.\n\nThrough a haze, you see the cat warriors surge south, driving the Yvoss-tai into a rout. For the moment, gathering your breath and nursing your countless wounds is more than enough. Besides, the battle field glitters with abandoned possessions...", eDialogPic.STANDARD, 1024, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        Town.PlaceEncounterGroup(2)
        StuffDone["18_4"] = 1
        return
    if StuffDone["18_0"] >= 32:
        if StuffDone["18_8"] == 250:
            return
        StuffDone["18_8"] = 250
        WorldMap.AlterTerrain(Location(85,62), 1, None)
        WorldMap.DeactivateTrigger(Location(85,62))
        ChoiceBox("When the slith charge slammed into your lines, recollections of the disastrous battle at Brattaskar Fort took over your minds. Once again, you saw Captain Mathias falling, clutching the arrow in his chest. You saw your post burning and friends dying.\n\n\"This time we will not flee!\" You cry to one another as you join the battle, filling up the positions where you are most needed. Your heroic effort sways the battle.\n\nThe soldiers are thrown back by the ferocious Yvoss-tai, but you stand rock still. The charge is broken, and you lead a countermove towards the slith spell casters. Supported by the Cave Archers, you crush the slith Dervishes, and the invaders falter.\n\nYet beyond your position at the farm house other slith war parties are storming the defensive wall. Chimney soldiers drop their equipment and run, unprepared for attack. You have taken too long!\n\nThen you hear screams from the lines of the sliths. A Dervish falls with an arrow through his neck, then another. Slith priests and mages run screaming from a hail of barbed arrows of a design everyone in Chimney knows: Nephilim.\n\nYou raise your weapons in greeting as a host of powerful feline shapes rush past, driving the Yvoss-tai into a rout. You breathe deeply, letting the Cat Paws do the rest. You have done your part.  And the battlefield glitters with abandoned possessions...", eDialogPic.STANDARD, 1024, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        Town.PlaceEncounterGroup(2)
        StuffDone["18_4"] = 1
        return

def FieldofBattle_454_OnEntry(p):
    if StuffDone["18_7"] >= 1:
        if StuffDone["18_3"] == 250:
            return
        StuffDone["18_3"] = 250
        MessageBox("You sleep fitfully, trusting in your guards. Several hours must have passed when a soldier bursts into the room. \"They?re coming! They?re coming! The northern outposts have been overrun!\" He runs out, almost in panic. You try to remain calm.")
        Town.PlaceEncounterGroup(1)
        return
    if StuffDone["18_2"] == 250:
        return
    StuffDone["18_2"] = 250
    ChoiceBox("You are received with joy by the remains of Chimney?s army. Any fighting man is welcome in their camp, but seeing the Brattaskar Heroes among them gives the demoralized troops new hope.\n\nWhen they hear that Sss-Chross is dead, they cheer. Their leader, Captain Locke, comes to thank you. \"Once again, we are in debt to you. But even this time, we must ask for more. The Yvoss-tai are approaching. Even without their leader, they are powerful.\n\nWe have been beaten before, and they are eager to finish us and conquer all of Chimney. Will you help us in this final battle?\"\n\nYou sense that only gratitude keeps Locke from commanding instead of asking you to stay, and even gratitude has its limits. They need your help to live, and you had better offer your help willingly.\n\nYou agree. Locke thanks you and brings you and a number of other crack troops with him to hold an important position at an old farm house, abandoned during the war.\n\nThe soldiers erect a simple barricade of barrels and carts, incremented by the occasional force spell. Then all you can do is wait.", eDialogPic.CREATURE, 16, ["OK"])

def FieldofBattle_455_ExitTown(p):
    if p.Dir.IsNorth or p.Dir.IsWest or p.Dir.IsSouth or p.Dir.IsEast:
        if StuffDone["18_4"] >= 1:
            return
        MessageBox("\"Please, don?t go too far. The reports say that the sliths have already struck at our northern outposts. They may arrive at any moment.\" The expression of the guard is friendly, but you feel it is safer not to cross him. You return to the square.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(17,50))
        p.CancelAction = True

def FieldofBattle_456_CreatureDeath0(p):
    StuffDone["18_0"] += 1
    if StuffDone["18_0"] == 250:
        pass

def FieldofBattle_480_CreatureDeath24(p):
    StuffDone["18_1"] += 1
    if StuffDone["18_1"] == 250:
        pass
    if StuffDone["18_1"] >= 12:
        if StuffDone["18_8"] == 250:
            return
        StuffDone["18_8"] = 250
        WorldMap.AlterTerrain(Location(85,62), 1, None)
        WorldMap.DeactivateTrigger(Location(85,62))
        ChoiceBox("The situation is getting desperate. At first, the battle seemed to be going well. Under the cover of the Cave Archers, you kept the first line of attackers at bay.\n\nBut when the slith mages arrived, burning a path for the deadly spears of the slith Dervishes, you understood which way this was going.\n\nOne by one, the soldiers fall around you, until you feel like you are the only ones left standing in a sea of corpses.\n\nThen you hear screams from the lines of the sliths. A Dervish falls with an arrow through his neck, then another. Slith mages and priests run screaming from a hail of barbed arrows of a design everyone in Chimney knows: Nephilim.\n\nPowerful feline shapes arrive around the house corners, brandishing their scimitars and striking fear into their enemies. You sag to the ground in exhaustion. It is over. And you owe your lives to the Cat Paw mercenaries.\n\nThrough a haze, you see the cat warriors surge south, driving the Yvoss-tai into a rout. For the moment, gathering your breath and nursing your countless wounds is more than enough. Besides, the battle field glitters with abandoned possessions...", eDialogPic.STANDARD, 1024, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        Town.PlaceEncounterGroup(2)
        StuffDone["18_4"] = 1
        return
    if StuffDone["18_0"] >= 32:
        if StuffDone["18_8"] == 250:
            return
        StuffDone["18_8"] = 250
        WorldMap.AlterTerrain(Location(85,62), 1, None)
        WorldMap.DeactivateTrigger(Location(85,62))
        ChoiceBox("When the slith charge slammed into your lines, recollections of the disastrous battle at Brattaskar Fort took over your minds. Once again, you saw Captain Mathias falling, clutching the arrow in his chest. You saw your post burning and friends dying.\n\n\"This time we will not flee!\" You cry to one another as you join the battle, filling up the positions where you are most needed. Your heroic effort sways the battle.\n\nThe soldiers are thrown back by the ferocious Yvoss-tai, but you stand rock still. The charge is broken, and you lead a countermove towards the slith spell casters. Supported by the Cave Archers, you crush the slith Dervishes, and the invaders falter.\n\nYet beyond your position at the farm house other slith war parties are storming the defensive wall. Chimney soldiers drop their equipment and run, unprepared for attack. You have taken too long!\n\nThen you hear screams from the lines of the sliths. A Dervish falls with an arrow through his neck, then another. Slith priests and mages run screaming from a hail of barbed arrows of a design everyone in Chimney knows: Nephilim.\n\nYou raise your weapons in greeting as a host of powerful feline shapes rush past, driving the Yvoss-tai into a rout. You breathe deeply, letting the Cat Paws do the rest. You have done your part.  And the battlefield glitters with abandoned possessions...", eDialogPic.STANDARD, 1024, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        Town.PlaceEncounterGroup(2)
        StuffDone["18_4"] = 1
        return

def FieldofBattle_490_CreatureDeath35(p):
    MessageBox("Captain Locke, one of Groul?s staunchest supporters, falls to a slith blow. You have no time for mourning, keeping blades away from yourselves is more than enough at the moment. But still you know that a good and noble man has passed away.")
    StuffDone["18_1"] += 1
    if StuffDone["18_1"] == 250:
        pass
    if StuffDone["18_1"] >= 12:
        if StuffDone["18_8"] == 250:
            return
        StuffDone["18_8"] = 250
        WorldMap.AlterTerrain(Location(85,62), 1, None)
        WorldMap.DeactivateTrigger(Location(85,62))
        ChoiceBox("The situation is getting desperate. At first, the battle seemed to be going well. Under the cover of the Cave Archers, you kept the first line of attackers at bay.\n\nBut when the slith mages arrived, burning a path for the deadly spears of the slith Dervishes, you understood which way this was going.\n\nOne by one, the soldiers fall around you, until you feel like you are the only ones left standing in a sea of corpses.\n\nThen you hear screams from the lines of the sliths. A Dervish falls with an arrow through his neck, then another. Slith mages and priests run screaming from a hail of barbed arrows of a design everyone in Chimney knows: Nephilim.\n\nPowerful feline shapes arrive around the house corners, brandishing their scimitars and striking fear into their enemies. You sag to the ground in exhaustion. It is over. And you owe your lives to the Cat Paw mercenaries.\n\nThrough a haze, you see the cat warriors surge south, driving the Yvoss-tai into a rout. For the moment, gathering your breath and nursing your countless wounds is more than enough. Besides, the battle field glitters with abandoned possessions...", eDialogPic.STANDARD, 1024, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        Town.PlaceEncounterGroup(2)
        StuffDone["18_4"] = 1
        return
    if StuffDone["18_0"] >= 32:
        if StuffDone["18_8"] == 250:
            return
        StuffDone["18_8"] = 250
        WorldMap.AlterTerrain(Location(85,62), 1, None)
        WorldMap.DeactivateTrigger(Location(85,62))
        ChoiceBox("When the slith charge slammed into your lines, recollections of the disastrous battle at Brattaskar Fort took over your minds. Once again, you saw Captain Mathias falling, clutching the arrow in his chest. You saw your post burning and friends dying.\n\n\"This time we will not flee!\" You cry to one another as you join the battle, filling up the positions where you are most needed. Your heroic effort sways the battle.\n\nThe soldiers are thrown back by the ferocious Yvoss-tai, but you stand rock still. The charge is broken, and you lead a countermove towards the slith spell casters. Supported by the Cave Archers, you crush the slith Dervishes, and the invaders falter.\n\nYet beyond your position at the farm house other slith war parties are storming the defensive wall. Chimney soldiers drop their equipment and run, unprepared for attack. You have taken too long!\n\nThen you hear screams from the lines of the sliths. A Dervish falls with an arrow through his neck, then another. Slith priests and mages run screaming from a hail of barbed arrows of a design everyone in Chimney knows: Nephilim.\n\nYou raise your weapons in greeting as a host of powerful feline shapes rush past, driving the Yvoss-tai into a rout. You breathe deeply, letting the Cat Paws do the rest. You have done your part.  And the battlefield glitters with abandoned possessions...", eDialogPic.STANDARD, 1024, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        Town.PlaceEncounterGroup(2)
        StuffDone["18_4"] = 1
        return
