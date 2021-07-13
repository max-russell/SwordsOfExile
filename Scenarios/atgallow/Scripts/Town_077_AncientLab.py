
def AncientLab_1882_MapTrigger_21_9(p):
    if StuffDone["63_8"] == 250:
        return
    StuffDone["63_8"] = 250
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(21,9))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(24,9))
    ChoiceBox("Upon entering the structure you are greeted by the the typical entrance hall of most Imperial structures. Yet this one has two peculiarities.\n\nTo the south, the hallway abruptly ends with a solid wall of bubbly basalt. It appears almost as if the stone was actually grown within the structure itself. Those walls look much more vibrant than the others. They must be much newer.\n\nThe other unpleasant feature is much more menacing. Blocking the halls to the sides are large hulking Golems, similar to Imperial style, perhaps the most fearsome construct ever created.\n\nCurrently they make no move to attack you, they just obstruct your progress. You have a feeling that getting past them will not be easy.", eDialogPic.CREATURE, 119, ["OK"])

def AncientLab_1884_MapTrigger_38_16(p):
    if StuffDone["63_9"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("Before you lies a series of runes. As you approach, they glow a threatening red. These runes are typical methods used to repel intruders. They can easily be passed with a magic word or something. But that is a luxury you do not have.\n\nYou will have to attempt to disarm this one. That will not be easy.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("Before you lies a series of runes. As you approach, they glow a threatening red. These runes are typical methods used to repel intruders. They can easily be passed with a magic word or something. But that is a luxury you do not have.\n\nYou will have to attempt to disarm this one. That will not be easy.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["63_9"] = 250
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(38,16))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(39,16))
    pc.RunTrap(eTrapType.DART, 3, 80)

def AncientLab_1886_MapTrigger_38_19(p):
    if StuffDone["64_0"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("Before you lies a series of runes. As you approach, they glow a threatening red. These runes are typical methods used to repel intruders. They can easily be passed with a magic word or something. But that is a luxury you do not have.\n\nYou will have to attempt to disarm this one. That will not be easy.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("Before you lies a series of runes. As you approach, they glow a threatening red. These runes are typical methods used to repel intruders. They can easily be passed with a magic word or something. But that is a luxury you do not have.\n\nYou will have to attempt to disarm this one. That will not be easy.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["64_0"] = 250
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(38,19))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(39,19))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 80)

def AncientLab_1888_MapTrigger_38_22(p):
    if StuffDone["64_1"] == 0:
        result = ChoiceBox("Before you lies a series of runes. As you approach, they glow a threatening red. These runes are typical methods used to repel intruders. They can easily be passed with a magic word or something. But that is a luxury you do not have.\n\nYou will have to attempt to disarm this one. That will not be easy.", eDialogPic.STANDARD, 27, ["No", "Yes"])
        if result == 0:
            p.CancelAction = True
            return
        elif result == 1:
            pc = SelectPCBox("Select a member of your party:",True)
            if pc == None:
                p.CancelAction = True
                return
            StuffDone["64_1"] = 1
            if Maths.Rand(1,0,100) < 80:
                Animation_Hold(-1, 053_magic3)
                Wait()
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
                return
            Message("Trap Disarmed!")
            return
        return

def AncientLab_1890_MapTrigger_37_27(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(37,31))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def AncientLab_1891_MapTrigger_37_31(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(37,35))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def AncientLab_1892_MapTrigger_39_27(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(22,14))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def AncientLab_1896_MapTrigger_38_35(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(40,31))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def AncientLab_1902_MapTrigger_35_36(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["64_2"] == 250:
        return
    StuffDone["64_2"] = 250
    Timer(Town, 3, False, "AncientLab_1918_TownTimer_16", eTimerType.DELETE)

def AncientLab_1905_MapTrigger_8_17(p):
    if StuffDone["64_3"] == 250:
        return
    StuffDone["64_3"] = 250
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(8,17))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(9,17))
    Animation_Hold(-1, 046_growl)
    Wait()
    Town.PlaceEncounterGroup(1)

def AncientLab_1907_MapTrigger_20_29(p):
    if StuffDone["64_4"] == 250:
        return
    StuffDone["64_4"] = 250
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(20,29))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(21,29))
    MessageBox("You open these doors to find a large wall. When the central section was grown, it was without mercy or resistance from the other parts of the structure. It is as if it was just sloppily inserted here.")

def AncientLab_1909_MapTrigger_15_10(p):
    if StuffDone["64_5"] == 250:
        return
    StuffDone["64_5"] = 250
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(15,10))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(16,10))
    TownMap.List["AncientLab_77"].DeactivateTrigger(Location(38,34))
    MessageBox("These records are very old and have rotted away long ago. You will find no clues about this place here.")

def AncientLab_1915_MapTrigger_33_32(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,31)).Num == 139:
        if StuffDone["63_3"] >= 3:
            Town.AlterTerrain(Location(32,31), 0, TerrainRecord.UnderlayList[217])
            MessageBox("Doing as Aroal explained, you touch the statue on the forehead and speak the word \'Dhev\'. Suddenly the wall behind it fades away. You may now enter the central chamber!")
            Town.AlterTerrain(Location(34,31), 0, TerrainRecord.UnderlayList[217])
            return
        MessageBox("You encounter an out of place statue of a Vahnatai carrying a massive waveblade. This relic was probably placed here recently.")
        return

def AncientLab_1916_MapTrigger_22_19(p):
    if StuffDone["63_3"] < 4:
        if StuffDone["64_6"] >= 17:
            result = ChoiceBox("You reach the control panel for the chamber holding the captured spore people. \"They others. Come to rescue us? Yes, I sense it so. About time. Yes, push button! Open gate. Please!\" a bunch of voices chime in your head.\n\nPush the release button?", eDialogPic.TERRAIN, 169, ["Leave", "Push"])
            if result == 1:
                StuffDone["63_3"] = 4
                Town.AlterTerrain(Location(20,20), 0, TerrainRecord.UnderlayList[148])
                ChoiceBox("You push the button and the gate on the observation cell silently slides open. Instantly you are greeted with chimes of mental \"thank yous\". The about seven spore people quickly move to the east, to the outside.\n\nOh well, a small victory has been achieved against your mighty foe. Whether or not it will assist in helping you achieve your main objective remains to be seen.", eDialogPic.CREATURE, 69, ["OK"])
                return
            return
        ChoiceBox("You have reached the control panel operating the gates to the holding cell containing the captured spore people.\n\n\"They others. Come to rescue us? Yes, I sense it so. About time. Wait! Not able to escape unless all evil visitors gone. Must be gone before can leave,\" chimes a sequence of various voices in your mind.\n\nIn order for the spore people to escape, you will need to slay all the remaining Vahnatai in this base.", eDialogPic.CREATURE, 69, ["OK"])
        return

def AncientLab_1917_MapTrigger_1_1(p):
    StuffDone["64_6"] += 1
    if StuffDone["64_6"] == 250:
        TownMap.List["AncientLab_77"].DeactivateTrigger(Location(1,1))
    if StuffDone["64_6"] >= 17:
        MessageBox("You have slain the last of the Vahnatai in this base. Unfortunately, none of them had anything directly helping you with the true matter at hand.")
        return

def AncientLab_1918_TownTimer_16(p):
    Animation_Hold(-1, 010_teleport)
    Wait()
    ChoiceBox("You have just uncovered another trap. Several horrible Vahnatai undead are summoned by the runes! This could be bad.", eDialogPic.CREATURE, 61, ["OK"])
    Town.PlaceEncounterGroup(2)

def AncientLab_1919_OnEntry(p):
    if StuffDone["63_7"] == 250:
        return
    StuffDone["63_7"] = 250
    ChoiceBox("You approach this large structure. It is clearly quite ancient, probably over a thousand years old. However, the walls are quite intact. Old Imperial structures were definitely built to last.\n\nThe one peculiarity is the strange bulbous dome atop the structure. It gives you a vague, chilling reminder of your short stay in Gynai and of their Vahnatai based structures.\n\nIt is very likely that the enemy is nearby.", eDialogPic.STANDARD, 8, ["OK"])

def TerrainTypeStepOn_Mist_AncientLab_2905(p):
    return
