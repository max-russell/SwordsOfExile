
def UnderCavala_26_MapTrigger_1_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(9,13)
    Party.MoveToMap(TownMap.List["Cavala_0"])

def UnderCavala_27_MapTrigger_30_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(39,9)
    Party.MoveToMap(TownMap.List["Cavala_0"])

def UnderCavala_28_MapTrigger_30_12(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(34,21)
    Party.MoveToMap(TownMap.List["Cavala_0"])

def UnderCavala_29_MapTrigger_30_23(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(40,27)
    Party.MoveToMap(TownMap.List["Cavala_0"])

def UnderCavala_30_MapTrigger_19_25(p):
    MessageBox("You kneel in front of the altar and pray for guidance. None is forthcoming. The prayer rug looks like it\'s been used a lot recently.")

def UnderCavala_31_MapTrigger_24_25(p):
    MessageBox("These shelves contain reams of the forms the Empire requires mayors of its villages to complete. They\'re yellowed and boring, and provide no useful information.")

def UnderCavala_36_MapTrigger_22_23(p):
    MessageBox("Among these completed forms, you find a number of building permits. Two people in this town recently had magical alarm systems installed. The forms mention \"Concealed Deactivation Buttons.\"")

def UnderCavala_37_MapTrigger_17_18(p):
    if StuffDone["2_0"] == 250:
        return
    StuffDone["2_0"] = 250
    TownMap.List["UnderCavala_2"].DeactivateTrigger(Location(17,18))
    MessageBox("This chest contains several small bags of gold coins and a few bottles of Hrras juice. In addition, there\'s something reather unusual. It\'s a nice ceramic plate, with a number of runes painted on it in gold paint.\n\nYou can\'t tell what the runes mean, but you doubt they\'re magical. It looks like an heirloom of some sort. Very odd ... what would something like this be doing hidden down here?")

def UnderCavala_38_MapTrigger_15_11(p):
    if StuffDone["2_1"] == 250:
        return
    result = ChoiceBox("A nasty looking magical rune has been etched in the floor here. Disarming won\'t help here. If you cross, it\'s probably going to hurt you.", eDialogPic.TERRAIN, 124, ["Leave", "Onward"])
    if result == 1:
        StuffDone["2_1"] = 250
        TownMap.List["UnderCavala_2"].AlterTerrain(Location(15,11), 1, None)
        TownMap.List["UnderCavala_2"].DeactivateTrigger(Location(15,11))
        MessageBox("The rune flashes brightly and disappears. You feel ill.")
        for pc in Party.EachAlivePC():
            pc.SetSkill(eSkill.STRENGTH, pc.GetSkill(eSkill.STRENGTH) - 1)
        return
    p.CancelAction = True

def UnderCavala_39_MapTrigger_6_10(p):
    if StuffDone["2_2"] == 250:
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
    StuffDone["2_2"] = 250
    TownMap.List["UnderCavala_2"].DeactivateTrigger(Location(6,10))
    pc.RunTrap(eTrapType.BLADE, 2, 20)

def UnderCavala_40_MapTrigger_6_11(p):
    if StuffDone["2_3"] == 250:
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
    StuffDone["2_3"] = 250
    TownMap.List["UnderCavala_2"].DeactivateTrigger(Location(6,11))
    pc.RunTrap(eTrapType.DART, 1, 50)

def UnderCavala_41_MapTrigger_1_4(p):
    if StuffDone["2_4"] == 250:
        return
    StuffDone["2_4"] = 250
    TownMap.List["UnderCavala_2"].DeactivateTrigger(Location(1,4))
    MessageBox("This is the main room where Sourgrass is boiled down to make Hrras juice. It\'s quiet and inactive now. With no merchants arriving to buy the stuff, there\'s not much point in making more.")
