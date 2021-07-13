
def FortTalrus_0_MapTrigger_8_7(p):
    result = ChoiceBox("This is your room, a haven thoughtfully provided by the commander of Fort Talrus. It\'s dusty, but reasonable.\n\nIf you wish, you can take a quick rest before journeying onward.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        MessageBox("You squeeze into the narrow bunks and sleep (somewhat) comfortably. Soon, you\'re rested, healed, and ready to resume your lives of adventure, danger, and romance.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += 500
            Party.HealAll(100)
            Party.RestoreSP(100)
        return

def FortTalrus_1_MapTrigger_11_7(p):
    if StuffDone["0_1"] == 250:
        return
    StuffDone["0_1"] = 250
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(11,7))
    MessageBox("You leave your quarters, keeping an eye open for the office of Commander Terrance. As you leave, you notice a note which someone has rolled up and tucked between the doorknob and door jamb.\n\nIt reads: \"Feel free to leave your excess items in your chambers. We\'ll keep them safe. - T.\"")

def FortTalrus_2_MapTrigger_7_4(p):
    if StuffDone["0_3"] == 250:
        return
    StuffDone["0_3"] = 250
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(7,4))
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(13,21))
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(19,21))
    MessageBox("You smell decay and hear squeaking. Your keen adventurer\'s senses are telling you that perhaps something unpleasant has taken up residence back here, away from the soldiers.")

def FortTalrus_3_MapTrigger_13_21(p):
    if StuffDone["0_3"] == 250:
        return
    StuffDone["0_3"] = 250
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(7,4))
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(13,21))
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(19,21))
    MessageBox("Empire forts are legendary for their cleanliness, efficiency, and ritual attention to order. Why, then, is this room clearly disused? For that matter, why hasn\'t anyone even bothered to clean up the cobwebs?")

def FortTalrus_4_MapTrigger_10_32(p):
    if StuffDone["0_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The commander clearly doesn\'t want anyone going through his things. The trap is easy to find. Disarming it may be another matter.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The commander clearly doesn\'t want anyone going through his things. The trap is easy to find. Disarming it may be another matter.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["0_4"] = 250
    TownMap.List["FortTalrus_0"].DeactivateTrigger(Location(10,32))
    pc.RunTrap(eTrapType.BLADE, 1, 30)

def FortTalrus_5_MapTrigger_20_39(p):
    result = ChoiceBox("You stare out through the gate at the land beyond. The plants beyond the Vale are healthy, the animals content. You can\'t help but be tempted by the chance to escape, to leave this place of death and never return.\n\nDo you wish to leave the scenario?", eDialogPic.TERRAIN, 93, ["No", "Yes"])
    if result == 0:
        p.CancelAction = True
        return
    elif result == 1:
        MessageBox("You step through the gate and away from the fortress. You feel disappointed that you weren\'t able to reap the rewards and fame saving the valley would provide.\n\nOn the other hand, you\'re safe, and you\'re alive as well. It\'s not the happiest possible ending, but it\'s an ending you can walk away from.\n  The End")
        Scenario.End()
        return
