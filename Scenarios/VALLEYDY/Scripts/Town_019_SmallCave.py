
def SmallCave_354_MapTrigger_6_5(p):
    if StuffDone["19_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You doubtthat  the troglodytes would leave a treasure chest here without some sort of nice, nasty trap on it ...", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You doubtthat  the troglodytes would leave a treasure chest here without some sort of nice, nasty trap on it ...", True)
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["19_4"] = 250
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(6,5))
    pc.RunTrap(eTrapType.GAS, 1, 15)

def SmallCave_355_MapTrigger_10_20(p):
    Party.OutsidePos = Location(101, 118)

def SmallCave_358_MapTrigger_25_10(p):
    Party.OutsidePos = Location(9, 121)

def SmallCave_361_MapTrigger_23_11(p):
    if StuffDone["19_0"] == 250:
        return
    StuffDone["19_0"] = 250
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(23,11))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(23,12))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(23,13))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(22,11))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(22,12))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(22,13))
    MessageBox("This tunnel was a lot longer than it seemed at first ... it wound uphill for what must have been at least a mile. Fortunately, the School\'s magical lights were placed at frequent intervals along the path.\n\nAt last, you\'ve reached the far end of it, and see light ahead. The air also seems fresher ... this must be the School\'s back exit.")

def SmallCave_364_MapTrigger_22_11(p):
    if StuffDone["19_0"] == 250:
        return
    StuffDone["19_0"] = 250
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(23,11))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(23,12))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(23,13))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(22,11))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(22,12))
    TownMap.List["SmallCave_19"].DeactivateTrigger(Location(22,13))
    MessageBox("The passage to the east slopes downward for quite a long way. The School\'s magical lights are placed at frequent intervals. Wherever the corridor leads, it\'s not near here.")
