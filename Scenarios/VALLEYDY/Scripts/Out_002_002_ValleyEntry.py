
def ValleyEntry_446_MapTrigger_43_12(p):
    if StuffDone["208_0"] == 250:
        return
    result = ChoiceBox("At the end of the valley, you find a small cave. Investigating, you discover the body of a soldier hidden in the back. Your best guess: he was trying to hide from wolves, but didn\'t quite hide well enough.\n\nOff to one side of the cave, away from the grisly remains, you find a broadsword. It\'s pretty morbid, but, heck, he isn\'t using it anymore.", eDialogPic.TERRAIN, 179, ["Take", "Leave"])
    if result == 0:
        StuffDone["208_0"] = 250
        WorldMap.AlterTerrain(Location(139,108), 1, None)
        WorldMap.DeactivateTrigger(Location(139,108))
        Party.GiveNewItem("IronBroadsword_58")
    return

def ValleyEntry_447_MapTrigger_9_11(p):
    if StuffDone["208_1"] == 250:
        return
    StuffDone["208_1"] = 250
    WorldMap.DeactivateTrigger(Location(105,107))
    WorldMap.DeactivateTrigger(Location(108,107))
    MessageBox("Traveling down this isolated valley may have been a mistake. You hear the harsh howls of wolves and the alien battle cries of goblins. A hunting pack has spotted you, and is closing in for the kill.")
    WorldMap.SpawnNPCGroup("Group_2_2_4", p.Target)

def ValleyEntry_449_MapTrigger_23_35(p):
    if StuffDone["208_2"] == 250:
        return
    StuffDone["208_2"] = 250
    WorldMap.DeactivateTrigger(Location(119,131))
    WorldMap.DeactivateTrigger(Location(118,131))
    WorldMap.DeactivateTrigger(Location(120,131))
    WorldMap.DeactivateTrigger(Location(118,132))
    ChoiceBox("For the first time, you look out over Skylark Vale. It\'s hard not to be shocked by what you see.\n\nIt looks like the life itself has been slowly, painstakingly, inexorably drained out of the land. The trees are withered, the grass is shot through with streaks of gray, and the smell of decay rises from the earth.\n\nTo the north, you see a slow flowing river wind through patches of fen and stands of stunted trees. No birds circle overhead, and no squirrels climb the trees.\n\nSomething is wrong here. Terribly, terribly wrong.", eDialogPic.STANDARD, 29, ["OK"])

def ValleyEntry_453_SpecialOnWin0(p):
    MessageBox("The battle won, you search the corpses of your victims. On the body of the goblin leader, you find a modest reward: a small sack of silver coins.")
    Party.Gold += 50
