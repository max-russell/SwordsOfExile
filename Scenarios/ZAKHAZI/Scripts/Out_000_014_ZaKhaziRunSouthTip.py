
def ZaKhaziRunSouthTip_673_MapTrigger_8_37(p):
    if StuffDone["214_0"] == 250:
        return
    StuffDone["214_0"] = 250
    WorldMap.DeactivateTrigger(Location(8,709))
    WorldMap.DeactivateTrigger(Location(8,710))
    WorldMap.DeactivateTrigger(Location(8,711))
    MessageBox("To the west, the river becomes too rough and fast to row against. It looks like you have no choice but to continue down the Za-Khazi Run, to the east.")

def ZaKhaziRunSouthTip_676_MapTrigger_21_37(p):
    if StuffDone["214_1"] == 250:
        return
    StuffDone["214_1"] = 250
    WorldMap.DeactivateTrigger(Location(21,709))
    WorldMap.DeactivateTrigger(Location(21,708))
    ChoiceBox("You row your boat out onto the river, moving downriver to the east into the Za-Khazi run. It\'s reputed to be 200 miles of the most unpleasant, savage, untamed caverns in all of Exile.\n\nIt\'s between you and your goal, and you have only 21 days to get through it. Normally, it would be no problem to move two hundred miles in three weeks, but not when you\'re heading into unknown caves, filled with all manner of monsters.\n\nOf course, it may be just an easy simple boat trip, over in 2 days. There\'s only one way to find out ...", eDialogPic.STANDARD, 1024, ["OK"])

def ZaKhaziRunSouthTip_678_MapTrigger_22_28(p):
    if StuffDone["214_2"] == 250:
        return
    StuffDone["214_2"] = 250
    WorldMap.DeactivateTrigger(Location(22,700))
    WorldMap.DeactivateTrigger(Location(22,698))
    ChoiceBox("The river so far is calm and peaceful, and, in fact, quite pleasant. The cave ceiling is covered with the glowing green fungus common in Exile, and covers the water with a soft light. Small flecks of mica in the wall catch the light. It\'s quite lovely.\n\nThis trip may not be bad after all. Just a relaxing vacation.", eDialogPic.STANDARD, 31, ["OK"])

def ZaKhaziRunSouthTip_680_MapTrigger_9_12(p):
    MessageBox("On the shore of the river, you find the wreck of a small cavewood rowboat, remarkably similar to the one you\'re using. It looks like the bottom was torn out by one of the many sharp rocks just under the water surface.\n\nThere are no bodies, though. You do, however, find tracks leading to the north.")

def ZaKhaziRunSouthTip_681_MapTrigger_13_2(p):
    if StuffDone["214_3"] == 250:
        return
    result = ChoiceBox("You find a cold campsite, with several crude stone cairns nearby. A band of Exile soldiers, stranded here, starved to death. The final survivor covered the bodies of the others with stone and then died himself.\n\nThe survivor\'s armor and weapons have corroded, but you notice a ring on its skeletal finger. You can take it with you, if you\'re comfortable robbing the dead.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["214_3"] = 250
        WorldMap.AlterTerrain(Location(13,674), 1, None)
        WorldMap.DeactivateTrigger(Location(13,674))
        Party.GiveNewItem("BronzeRingofSkill_310")
        MessageBox("You help yourself to the ring and cover the body with a few stones. There\'s nothing left to do here. You leave this depressing scene behind.")
        return
    return

def ZaKhaziRunSouthTip_682_MapTrigger_24_12(p):
    if StuffDone["214_4"] == 250:
        return
    StuffDone["214_4"] = 250
    WorldMap.DeactivateTrigger(Location(24,684))
    WorldMap.DeactivateTrigger(Location(24,683))
    ChoiceBox("The peaceful ride is about to come to an end. When people told you about the Za-Khazi Run, they mentioned nothing about the rapids.\n\nAnd yet, here they are. Rough, fast, and dangerous looking. Worse, there are no portages, and the water is far too fast to row against. If you go through these rapids, there is no guarantee that you will be able to go back.\n\nIt looks like the adventure is truly about to begin.", eDialogPic.STANDARD, 31, ["OK"])

def ZaKhaziRunSouthTip_684_MapTrigger_28_21(p):
    if StuffDone["214_5"] == 250:
        return
    StuffDone["214_5"] = 250
    WorldMap.DeactivateTrigger(Location(28,693))
    MessageBox("You made it through the rapids safely, but now there\'s no going back. Welcome to the Za-Khazi Run.")

def ZaKhaziRunSouthTip_685_MapTrigger_39_40(p):
    if StuffDone["214_7"] == 250:
        return
    StuffDone["214_7"] = 250
    WorldMap.DeactivateTrigger(Location(39,712))
    WorldMap.DeactivateTrigger(Location(40,712))
    MessageBox("This arm of the river ends in a dead end. There\'s a small patch of uninteresting land to the west. You\'ve lost some valuable time.")

def ZaKhaziRunSouthTip_686_MapTrigger_37_42(p):
    if StuffDone["214_6"] == 250:
        return
    StuffDone["214_6"] = 250
    WorldMap.AlterTerrain(Location(37,714), 1, None)
    WorldMap.DeactivateTrigger(Location(37,714))
    MessageBox("This quiet, peaceful beach has suddenly become active with activity. A pile of small, chattering blue creatures just came out of nowhere, jumping up and down, baring small fangs, and running hungrily towards you.\n\nThis must be the Run\'s welcoming committee.")
    WorldMap.SpawnEncounter("Group_0_14_4", p.Target)

def ZaKhaziRunSouthTip_688_SpecialOnWin0(p):
    MessageBox("Searching the gremlins, you\'re able to find some grubby (but still edible) food. Waste not, want not.")
    Party.Food += 50
