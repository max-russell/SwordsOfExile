
def OpalMines_261_MapTrigger_3_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You are at a stairway leading upward. The steps are large and clumsy, roughly hewn out of granite. Flecks of tiny gemstones in the rock reflect the light.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(20,42)
    Party.MoveToMap(TownMap.List["OpalCitadel_11"])

def OpalMines_262_MapTrigger_7_3(p):
    if StuffDone["12_0"] == 250:
        return
    StuffDone["12_0"] = 250
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(7,3))
    ChoiceBox("The soldiers in this fortress get their food from this cavern. Hundreds of mushrooms, large, fleshy, edible fungi, grow in long straight rows. It\'s not an interesting diet, but it keeps people going.\n\nA large band of soldiers are waiting for you here. They\'re all stationed on the other side of a narrow stream, ready to carry out a final, desperate defense against you.", eDialogPic.TERRAIN, 72, ["OK"])

def OpalMines_263_MapTrigger_8_5(p):
    if StuffDone["12_1"] == 250:
        return
    StuffDone["12_1"] = 250
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(8,5))
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(7,5))
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(6,5))
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(5,5))
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(5,4))
    MessageBox("Suddenly, the air around you turns incredibly, harmfully cold.")
    for x in range(4, 10):
        for y in range(4, 7):
            Town.PlaceField(Location(x,y), Field.ICE_WALL)

def OpalMines_268_MapTrigger_45_17(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a grinding noise.")
        t = Town.TerrainAt(Location(41,16))
        if t == TerrainRecord.UnderlayList[187]: Town.AlterTerrain(Location(41,16), 0, TerrainRecord.UnderlayList[174])
        elif t == TerrainRecord.UnderlayList[174]: Town.AlterTerrain(Location(41,16), 0, TerrainRecord.UnderlayList[187])
        return

def OpalMines_269_MapTrigger_45_13(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        t = Town.TerrainAt(Location(41,16))
        if t == TerrainRecord.UnderlayList[170]: Town.AlterTerrain(Location(41,16), 0, TerrainRecord.UnderlayList[174])
        elif t == TerrainRecord.UnderlayList[174]: Town.AlterTerrain(Location(41,16), 0, TerrainRecord.UnderlayList[170])
        return

def OpalMines_270_MapTrigger_41_15(p):
    if StuffDone["12_2"] == 250:
        return
    result = ChoiceBox("You open the chest and see a small pillow, covered by a single piece of dirty, torn velvet. You pull the velvet aside, revealing the most beautiful gemstone you have ever seen.\n\nIt\'s a massive oval opal, carefully polished, about three inches long and two wide. It is utterly without flaw, and at its heart you can see more colors than you could have imagined.\n\nIt\'s a priceless treasure, and you have but to reach out and take it.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
    if result == 0:
        StuffDone["12_2"] = 250
        TownMap.List["OpalMines_12"].DeactivateTrigger(Location(41,15))
        SpecialItem.Give("MeloraOpal")
        MessageBox("You must have already passed the traps. Nothing awful happens when you pick up the gem.")
        return
    return

def OpalMines_271_MapTrigger_38_11(p):
    Town.AlterTerrain(Location(42,10), 0, TerrainRecord.UnderlayList[155])

def OpalMines_272_MapTrigger_39_11(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(39,9))
    p.CancelAction = True

def OpalMines_273_MapTrigger_41_11(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(41,9))
    p.CancelAction = True

def OpalMines_274_MapTrigger_43_11(p):
    Town.AlterTerrain(Location(40,10), 0, TerrainRecord.UnderlayList[155])

def OpalMines_275_MapTrigger_40_11(p):
    Town.AlterTerrain(Location(37,12), 0, TerrainRecord.UnderlayList[155])

def OpalMines_276_MapTrigger_19_2(p):
    Town.AlterTerrain(Location(26,4), 0, TerrainRecord.UnderlayList[97])

def OpalMines_277_MapTrigger_28_10(p):
    Town.AlterTerrain(Location(26,4), 0, TerrainRecord.UnderlayList[0])

def OpalMines_278_MapTrigger_24_41(p):
    if StuffDone["12_3"] == 250:
        return
    StuffDone["12_3"] = 250
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(24,41))
    MessageBox("You are standing at the entrance to the Empire soldier\'s opal mines. They painstakingly bored narrow winding tunnels through solid rock, probably using very inadequate tools, burrowing away a stone at a time.\n\nIt\'s hard to imagine the combination of boredom and greed that inspired them to do this. They spent their lives digging out stone they could never use, and dreaming of war with a people their nation was at peace with.")

def OpalMines_279_MapTrigger_22_35(p):
    MessageBox("Hidden away in this cavern, you find a series of commander\'s logs, detailing the original mission of the Empire forces here, and their progress in the war since. Their original mission was to harry Exile forces, and they\'ve done the best they could.\n\nSince this colony was first founded, they have found four groups of Exile travelers trying to pass through the run. The soldiers here ambushed and butchered all of them. All of them passed by long after the war with the Empire ended.")

def OpalMines_280_MapTrigger_1_46(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        MessageBox("Click.")
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,33)).Num == 71:
            Town.AlterTerrain(Location(9,33), 0, TerrainRecord.UnderlayList[72])
            Town.AlterTerrain(Location(19,43), 0, TerrainRecord.UnderlayList[162])
            return
        Town.AlterTerrain(Location(9,33), 0, TerrainRecord.UnderlayList[71])
        Town.AlterTerrain(Location(19,43), 0, TerrainRecord.UnderlayList[163])
        return

def OpalMines_281_MapTrigger_9_33(p):
    if StuffDone["12_4"] == 250:
        return
    StuffDone["12_4"] = 250
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(9,33))
    Town.PlaceEncounterGroup(1)

def OpalMines_282_MapTrigger_38_7(p):
    if StuffDone["12_5"] == 250:
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
    StuffDone["12_5"] = 250
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(38,7))
    pc.RunTrap(eTrapType.GAS, 1, 80)

def OpalMines_283_MapTrigger_41_3(p):
    if StuffDone["12_6"] == 250:
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
    StuffDone["12_6"] = 250
    TownMap.List["OpalMines_12"].DeactivateTrigger(Location(41,3))
    pc.RunTrap(eTrapType.EXPLOSION, 1, 80)
