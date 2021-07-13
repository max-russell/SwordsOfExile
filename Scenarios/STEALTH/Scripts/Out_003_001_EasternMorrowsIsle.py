
def EasternMorrowsIsle_440_MapTrigger_2_14(p):
    if StuffDone["101_5"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You reach another gate manned by Hill Runners. The guards here, however, aren\'t as friendly as at the earlier gate. While they\'re friendly and sociable, they make it clear that you aren\'t allowed to pass.")
        return

def EasternMorrowsIsle_441_MapTrigger_16_2(p):
    result = ChoiceBox("You find an abandoned mine. Well, maybe not totally abandoned. There\'s a crude painted sign placed just outside the entrance: \"Haunted Mine. Keep out!\"\n\nOf course, it\'s probably not serious. Someone\'s probably just trying to keep claim jumpers away. There\'s probably plenty of gold inside.", eDialogPic.TERRAIN, 195, ["Leave", "Enter"])
    if result == 1:
        MessageBox("Wouldn\'t you know it? The sign was, in fact, perfectly sincere. There are spirits in here, and they seem to be intent on eating you.")
        WorldMap.SpawnEncounter("Group_3_1_4", p.Target)
        return

def EasternMorrowsIsle_442_MapTrigger_26_42(p):
    if StuffDone["206_4"] >= 1:
        if StuffDone["207_1"] == 250:
            return
        StuffDone["207_1"] = 250
        MessageBox("It was almost completely overgrown with moss, and placed several feet off the path, but by this time, you were able to recognize it pretty well. It was a large rock, slightly larger and darker than those around it.\n\nYou turn it over, and find the words \"Final Stone.\" carved underneath. You also find a gold ring. You pocket the ring. You\'ll probably never know what all that stone stuff was about, but you might as well profit from it.")
        Party.GiveNewItem("GoldRingofProt_294")
        return

def EasternMorrowsIsle_443_MapTrigger_36_23(p):
    if StuffDone["101_7"] >= 1:
        if StuffDone["207_2"] == 250:
            return
        StuffDone["207_2"] = 250
        MessageBox("As you wander up this path, wondering if you\'re heading the right direction to reach Stalker\'s fort, someone in the hills above you shouts \"Keep going north! We\'ll direct you from there!\"")
        return

def EasternMorrowsIsle_444_MapTrigger_40_15(p):
    if StuffDone["207_3"] == 250:
        return
    StuffDone["207_3"] = 250
    WorldMap.DeactivateTrigger(Location(184,63))
    MessageBox("You find some creatures sunning themselves on the beach. They insist on maintaining their privacy.")
    WorldMap.SpawnEncounter("Group_3_1_5", p.Target)

def EasternMorrowsIsle_445_MapTrigger_40_10(p):
    if StuffDone["101_7"] >= 1:
        WorldMap.AlterTerrain(Location(183,52), 0, TerrainRecord.UnderlayList[36])
        return

def EasternMorrowsIsle_447_MapTrigger_20_4(p):
    ChoiceBox("You reach one of these mountains\' many productive mines. Tired, dirty miners, guarded by Hill Runner soldiers, work the tunnels for valuable ores to be smelted and taken down to Buzzard.\n\nBeing adventurers, deep, dark tunnels don\'t have much appeal to you unless they contain monsters and treasure in discrete, easily taken piles. You depart.", eDialogPic.TERRAIN, 195, ["OK"])

def EasternMorrowsIsle_449_MapTrigger_27_12(p):
    result = ChoiceBox("A small smelter has been set up in this valley. They produce iron bars at a decent rate. When you arrive, they greet you, chat with you for a bit, and offer to sell you iron at a reasonable rate.", eDialogPic.TERRAIN, 194, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_14_3_1")
        p.CancelAction = True
        return

def EasternMorrowsIsle_450_MapTrigger_8_14(p):
    if StuffDone["207_4"] == 250:
        return
    StuffDone["207_4"] = 250
    WorldMap.DeactivateTrigger(Location(152,62))
    MessageBox("To the east, you can see many mines. Many have been played out and boarded up. Some are still active. The path has been heavily used, and tailings are piled everywhere. This looks like a rich area. No wonder the Empire wants it.")

def EasternMorrowsIsle_451_MapTrigger_6_27(p):
    if StuffDone["207_5"] == 250:
        return
    StuffDone["207_5"] = 250
    WorldMap.DeactivateTrigger(Location(150,75))
    MessageBox("There is a narrow bridge up here, built over a thinner section of the river. You cross it with care, the water pounding over the rapids not far below you.")

def EasternMorrowsIsle_452_MapTrigger_35_1(p):
    WorldMap.AlterTerrain(Location(183,52), 0, TerrainRecord.UnderlayList[36])

def EasternMorrowsIsle_453_SpecialOnWin0(p):
    MessageBox("The spirits dead, you search the mine. It was pretty played out. That\'s why it was so easily abandoned to the ghosts. You do find a bar of gold, though, and some coins as well. Not too shabby.")
    Party.GiveNewItem("Goldbar_334")
    Party.Gold += 200
