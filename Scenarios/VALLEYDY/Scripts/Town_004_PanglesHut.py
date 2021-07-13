
def PanglesHut_32_MapTrigger_13_13(p):
    if StuffDone["4_4"] == 250:
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
    StuffDone["4_4"] = 250
    TownMap.List["PanglesHut_4"].DeactivateTrigger(Location(13,13))
    pc.RunTrap(eTrapType.GAS, 2, 20)

def PanglesHut_33_MapTrigger_5_23(p):
    if StuffDone["4_0"] == 250:
        return
    StuffDone["4_0"] = 250
    TownMap.List["PanglesHut_4"].DeactivateTrigger(Location(5,23))
    MessageBox("Like most farms, this one has a storage shed. However, the shed seems to be full of trash and old, forgotten stuff instead of the expected tools and seed. It would take weeks to sort through this garbage.")

def PanglesHut_34_MapTrigger_10_22(p):
    MessageBox("For reasons unclear to you, this chest is filled with old scraps of cloth and fur. A quick search reveals nothing of value. You close it.")

def PanglesHut_35_MapTrigger_10_24(p):
    if StuffDone["4_2"] >= 1:
        if StuffDone["4_3"] >= 1:
            MessageBox("For reasons unclear to you, this chest is filled with old scraps of paper and vellum. A quick search reveals nothing of value. You close it.")
            return
        if StuffDone["4_3"] == 250:
            return
        StuffDone["4_3"] = 250
        MessageBox("Remembering what Pangle told you, you carefully search the massive jumble of scraps of paper filling this chest. Sure enough, you soon find your reward. It\'s a sheaf of 8 ancient vellum scrolls.\n\nThe scrolls are covered with intricate designs and notes, explaining how to operate the controls on the lowest level of the School of Magery. This could be very useful.")
        SpecialItem.Give("InstructionsScrolls")
        return
    MessageBox("For reasons unclear to you, this chest is filled with old scraps of paper and vellum. A quick search reveals nothing of value. You close it.")

def PanglesHut_36_MapTrigger_27_5(p):
    if StuffDone["4_5"] == 250:
        return
    result = ChoiceBox("You look under the boulder, and find a collection of dry, heavily chewed bones. On closer inspection, however, you notice that one of the \"bones\" is actually a scroll tube!", eDialogPic.TERRAIN, 77, ["Take", "Leave"])
    if result == 0:
        StuffDone["4_5"] = 250
        TownMap.List["PanglesHut_4"].DeactivateTrigger(Location(27,5))
        Party.GiveNewItem("ScrollMagicRes_207")
    return

def PanglesHut_37_OnEntry(p):
    if not Town.Abandoned:
        if StuffDone["4_1"] == 250:
            return
        StuffDone["4_1"] = 250
        MessageBox("You arrive at a true rarity in Skylark Vale - a working farm. The plants are not afflicted by rot, the animals are not dying. A small lake fails to assails your noses with acrid fumes.\n\nIt\'s a nice change of pace.")

def Talking_4_9(p):
    if Party.Gold >= 500:
        Party.Gold -= 500
        StuffDone["4_2"] = 1
        p.TalkingText = "You pay the 500 gold. He counts it, and says \"The scroll is out in the shed, in the south chest. Look there. And a pleasure doing business with ye\'.\""
    else:
        p.TalkingText = "He frowns. \"I\'m a poor old man. You don\'t give me the gold, I won\'t give you the scroll.\""
