
def Buzzard_152_MapTrigger_35_27(p):
    if StuffDone["12_0"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("It looks like this door has a magical alarm wired into it.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("It looks like this door has a magical alarm wired into it.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["12_0"] = 250
    TownMap.List["Buzzard_12"].DeactivateTrigger(Location(35,27))
    pc.RunTrap(eTrapType.ALERT, 0, 75)

def Buzzard_153_MapTrigger_38_33(p):
    if StuffDone["12_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("It looks like this door has a magical alarm wired into it.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("It looks like this door has a magical alarm wired into it.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["12_1"] = 250
    TownMap.List["Buzzard_12"].DeactivateTrigger(Location(38,33))
    pc.RunTrap(eTrapType.ALERT, 0, 50)

def Buzzard_154_MapTrigger_38_37(p):
    if StuffDone["12_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("It looks like this door has a magical alarm wired into it.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("It looks like this door has a magical alarm wired into it.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["12_2"] = 250
    TownMap.List["Buzzard_12"].DeactivateTrigger(Location(38,37))
    pc.RunTrap(eTrapType.ALERT, 0, 50)

def Buzzard_155_MapTrigger_17_18(p):
    if StuffDone["12_3"] == 250:
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
    StuffDone["12_3"] = 250
    TownMap.List["Buzzard_12"].DeactivateTrigger(Location(17,18))
    pc.RunTrap(eTrapType.RANDOM, 3, 50)

def Buzzard_156_MapTrigger_22_18(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(26,18)).Num == 154:
        MessageBox("You look behind the pot, and find a small switch in the wall. You flip it, and a section of the east wall slides away. Luna smirks. \"When the Empire controlled this city, that really came in handy.\"")
        Town.AlterTerrain(Location(26,18), 0, TerrainRecord.UnderlayList[170])
        return

def Buzzard_157_MapTrigger_27_19(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(26,18)).Num == 154:
        MessageBox("You knock on the wall. Luna opens the concealed door to let you out.")
        Town.AlterTerrain(Location(26,18), 0, TerrainRecord.UnderlayList[170])
        return

def Buzzard_158_MapTrigger_27_22(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(27,26)
    Party.MoveToMap(TownMap.List["UnderBuzzard_13"])

def Buzzard_159_OnEntry(p):
    if StuffDone["12_4"] == 250:
        return
    StuffDone["12_4"] = 250
    ChoiceBox("You have reached the city of Buzzard, a heavily fortified fortress perched in the mountains of northeast Morrow\'s Isle.\n\nYou have suspected for some time that the unthinkable was true: that this city is not under Empire control. A brief look at the soldiers guarding the city indicates that this is, indeed, true.\n\nThe Empire has not announced that the rebels control Buzzard, and you can see why they have kept it quiet. For the Empire to not have control of a city on its lands is almost unprecedented, and an amazing achievement for the Hill Runners.\n\nNormally, any sort of rebellion, even one only a fraction as serious as this one, is met by massive, violent Empire retaliation. Ask any Exile. Yet, Buzzard has managed to remain independent. For as long as it lasts, this is truly an amazing place.", eDialogPic.TERRAIN, 189, ["OK"])

def Buzzard_160_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(38, 8),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(38, 8),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(38, 8),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(39, 8),WorldMap.SectorAt(Party.OutsidePos))

def Talking_12_12(p):
    if Party.Gold < 10:
        p.TalkingText = "She shakes her head. \"Sorry, but the price is firm.\""
    else:
        Party.Gold -= 10
        Party.Pos = Location(33, 11)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "Rita takes a moment from her hard work to show you around back to your room. It\'s simple but comfortable, and you have a restful night."
        CentreView(Party.Pos, False)

def Talking_12_13(p):
    if Party.Gold >= 6:
        Party.Gold -= 6
        p.TalkingText = "She serves you up a few shots of strong mountain liquor. The harsh liquid inflicts great pain and suffering on the inside of your mouth and throat, but in a good way."
    else:
        p.TalkingText = "You don\'t have the gold."

def Talking_12_28(p):
    if Party.Gold >= 1:
        Party.Gold -= 1
        p.TalkingText = "You give him a gold piece. \"Thanks,\" he says. \"Things haven\'t been going right since the mess in Fahl.\""
    else:
        p.TalkingText = "You don\'t have a gold piece."
