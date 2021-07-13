
def ValeInfestation_335_MapTrigger_42_17(p):
    if StuffDone["17_1"] == 250:
        return
    StuffDone["17_1"] = 250
    TownMap.List["ValeInfestation_17"].DeactivateTrigger(Location(42,17))
    MessageBox("How odd. You find a tunnel leading into the valley wall, carefully concealed by branches and shrubs. The path is worn smooth by the passage of many feet. You wonder who\'s hiding down here ...")

def ValeInfestation_336_MapTrigger_32_36(p):
    if StuffDone["17_2"] == 250:
        return
    StuffDone["17_2"] = 250
    TownMap.List["ValeInfestation_17"].DeactivateTrigger(Location(32,36))
    MessageBox("Well, whoever\'s down here, they don\'t like you. This is probably a hideout for a variety of brigands!")

def ValeInfestation_337_MapTrigger_14_11(p):
    MessageBox("The books on these shelves are greasy, well thumbed, and, shall we say, highly adult themed. Certainly nothing that would interest bold, virtuous adventurers such as yourselves.")

def ValeInfestation_340_MapTrigger_1_25(p):
    if StuffDone["17_4"] == 250:
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
    StuffDone["17_4"] = 250
    TownMap.List["ValeInfestation_17"].DeactivateTrigger(Location(1,25))
    TownMap.List["ValeInfestation_17"].DeactivateTrigger(Location(1,24))
    pc.RunTrap(eTrapType.RANDOM, 1, 10)

def ValeInfestation_341_MapTrigger_2_41(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(2,38)).Num == 0:
        MessageBox("You trip a trap! Rubble falls from the ceiling behind you, barring your way back!")
        Town.AlterTerrain(Location(2,38), 0, TerrainRecord.UnderlayList[97])
        return

def ValeInfestation_343_MapTrigger_5_41(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(5,38)).Num == 0:
        MessageBox("You trip a trap! Rubble falls from the ceiling behind you, barring your way back!")
        Town.AlterTerrain(Location(5,38), 0, TerrainRecord.UnderlayList[97])
        return

def ValeInfestation_344_MapTrigger_42_42(p):
    if StuffDone["17_5"] == 250:
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
    StuffDone["17_5"] = 250
    TownMap.List["ValeInfestation_17"].DeactivateTrigger(Location(42,42))
    pc.RunTrap(eTrapType.GAS, 1, 40)

def ValeInfestation_345_OnEntry(p):
    if StuffDone["17_0"] == 250:
        return
    StuffDone["17_0"] = 250
    MessageBox("You wouldn\'t have noticed it if you weren\'t right on top of it. It\'s a small valley, concealed from view by rubble and small stands of trees. It\'s very quiet and peaceful.")
