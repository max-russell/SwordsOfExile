
def CunningCrypt_14_MapTrigger_40_34(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(40,34))
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(7,35))
    Town.AlterTerrain(Location(7,40), 0, TerrainRecord.UnderlayList[147])

def CunningCrypt_15_MapTrigger_7_35(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(40,34))
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(7,35))
    Town.AlterTerrain(Location(41,39), 0, TerrainRecord.UnderlayList[147])

def CunningCrypt_16_MapTrigger_17_29(p):
    if StuffDone["1_1"] == 250:
        return
    StuffDone["1_1"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(17,29))
    MessageBox("You hear strange, demonic laughter.")
    Town.PlaceEncounterGroup(1)

def CunningCrypt_17_MapTrigger_16_13(p):
    if StuffDone["1_2"] == 250:
        return
    StuffDone["1_2"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(16,13))
    MessageBox("You hear eerie, ghoulish cackling.")
    Town.PlaceEncounterGroup(2)

def CunningCrypt_18_MapTrigger_27_23(p):
    if StuffDone["1_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The tiles on the floor ahead look like they don\'t fit very well. It could be poor craftsmanship. It could also be a trap.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The tiles on the floor ahead look like they don\'t fit very well. It could be poor craftsmanship. It could also be a trap.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["1_3"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(27,23))
    pc.RunTrap(eTrapType.BLADE, 2, 20)

def CunningCrypt_19_MapTrigger_27_19(p):
    if StuffDone["1_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The tiles on the floor ahead look like they don\'t fit very well. It could be poor craftsmanship. It could also be a trap.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The tiles on the floor ahead look like they don\'t fit very well. It could be poor craftsmanship. It could also be a trap.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["1_4"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(27,19))
    pc.RunTrap(eTrapType.DART, 2, 30)

def CunningCrypt_20_MapTrigger_27_15(p):
    if StuffDone["1_5"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The tiles on the floor ahead look like they don\'t fit very well. It could be poor craftsmanship. It could also be a trap.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The tiles on the floor ahead look like they don\'t fit very well. It could be poor craftsmanship. It could also be a trap.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["1_5"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(27,15))
    pc.RunTrap(eTrapType.GAS, 1, 40)

def CunningCrypt_21_MapTrigger_38_9(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["1_6"] >= 1:
            MessageBox("Nothing happens.")
            return
        Animation_Hold(-1, 005_explosion)
        Wait()
        if StuffDone["1_6"] == 250:
            return
        StuffDone["1_6"] = 250
        MessageBox("When you pull the lever, there is a loud explosion. The screams of tortured souls, freshly released, vibrate through the air. The masters of this crypt have been released.")
        Town.PlaceEncounterGroup(3)
        for x in range(34, 37):
            for y in range(16, 17):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
        return

def CunningCrypt_22_MapTrigger_34_23(p):
    if StuffDone["1_7"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The vampire\'s dark altar is positively dripping with all manner of evil, harmful, nasty energy. So strong is its malevolent presence that it throws you away from it with a minimum effort, harming you in the process.")
        Party.Damage(Maths.Rand(6, 1, 6) + 0, eDamageType.COLD)
        Wait()
        return

def CunningCrypt_27_SanctifyTrigger_35_23(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["1_7"] >= 1:
        MessageBox("The altar is as destroyed as you\'re going to get it.")
        return
    if StuffDone["1_7"] == 250:
        return
    StuffDone["1_7"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(34,23))
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(36,23))
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(36,22))
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(35,22))
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(34,22))
    MessageBox("With great concentration and holy force, you intone the words of exorcism. Subjected to such pure, undiluted goodness, the altar begins to waver and warp, the stone itself turning soft and gooey.\n\nAt last, the altar cracks, and the evil force held inside is released. Said evil force then takes solid form, in order to serve you up a good old-fashioned pile of demon whup-ass.")
    Town.PlaceEncounterGroup(4)
    for pc in Party.EachAlivePC():
        pc.AwardXP(25)

def CunningCrypt_28_MapTrigger_38_25(p):
    if StuffDone["1_8"] == 250:
        return
    StuffDone["1_8"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(38,25))
    MessageBox("In addition to the other pleasant goodies in this chest, you find a small, intricately carved statuette of a Slithzerikai warrior.")
    SpecialItem.Give("SlithStatuette")

def CunningCrypt_29_MapTrigger_35_33(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("This chamber is dominated by a large, magical portal. You aren\'t sure why someone would put one of these in a crypt. They are, after all, quite expensive, and magical contractors rarely bring them in under cost.\nMaybe the crypt builders made it to get out of their creation after it was completed. Or maybe it was put here so mourners and relatives could get in to pay their respects. Or maybe it was so that the souls of the dead could escape.\nEither way, it has been poorly maintained. It wavers and flickers, and sometimes looks like it\'s ready to disappear altogether. However, it still looks strong enough to carry you somewhere, if you want.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(35,15))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return
    MessageBox("Unfortunately, the portal is unstable, and shifts you around a bit as it transports you. The cells of your body are painfully disrupted.")
    Party.HealAll(-50)

def CunningCrypt_30_MapTrigger_33_37(p):
    result = ChoiceBox("How interesting. The makers of the crypt built a large cubicle here, with several small bunks packed inside. The floor at the entrance to the cubicle is marked with a large rune, which still glows with power.\n\nMaybe if you step inside and lie on the bunks something wonderful will happen.", eDialogPic.TERRAIN, 170, ["Leave", "Step In"])
    if result == 1:
        MessageBox("You step inside and lie down on the bunks. There is a brief flash of light. Nothing else happens. You feel no different. Your wounds haven\'t been healed. No new injuries have been inflicted. Nothing\'s changed.\n\nConfused, you step out of the cubicle. How odd.")
        Party.Age += 3000
        return

def CunningCrypt_31_MapTrigger_32_39(p):
    result = ChoiceBox("How interesting. The makers of the crypt built a large cubicle here, with several small bunks packed inside. The floor at the entrance to the cubicle is marked with a large rune, which still glows with power.\n\nMaybe if you step inside and lie on the bunks something wonderful will happen.", eDialogPic.TERRAIN, 165, ["Leave", "Step In"])
    if result == 1:
        MessageBox("You step inside and lie down. Nothing happens. You wait. Nothing happens. Confused and bored, you get up and step back outside.\n\nMaybe it\'s broken.")
        return

def CunningCrypt_32_MapTrigger_30_26(p):
    if StuffDone["1_9"] == 250:
        return
    StuffDone["1_9"] = 250
    TownMap.List["CunningCrypt_1"].DeactivateTrigger(Location(30,26))
    ChoiceBox("This room is filled with several rows of scroll racks. It is also filled with thick, choking clouds of dust, the inevitable result of leaving thousands of scrolls in a dank room to rot.\n\nAmong the crumbling heaps of vellum and parchment, you might find something of value. Stranger things have happened.", eDialogPic.TERRAIN, 252, ["OK"])

def CunningCrypt_33_MapTrigger_23_37(p):
    MessageBox("The only thing in this desk is a very old map of the caves immediately surrounding this crypt. One point of interest: you see that there are five waterways leaving the body of water outside this crypt.\n\nHowever, four of the waterways dead end some miles to the north. Only the middle river continues unimpeded. This information may help you save some time, if it\'s still accurate.")

def CunningCrypt_34_OnEntry(p):
    if StuffDone["1_6"] >= 1:
        for x in range(34, 37):
            for y in range(16, 17):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
        return
