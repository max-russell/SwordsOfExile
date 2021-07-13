
def NorthernMorrowsIsle_355_MapTrigger_34_30(p):
    if StuffDone["110_0"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_0"] = 250
        WorldMap.DeactivateTrigger(Location(82,30))
        Party.GiveNewItem("GlowingNettle_365")
    return

def NorthernMorrowsIsle_356_MapTrigger_39_26(p):
    if StuffDone["110_1"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_1"] = 250
        WorldMap.DeactivateTrigger(Location(87,26))
        Party.GiveNewItem("AsptongueMold_367")
    return

def NorthernMorrowsIsle_357_MapTrigger_31_17(p):
    if StuffDone["110_2"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_2"] = 250
        WorldMap.DeactivateTrigger(Location(79,17))
        Party.GiveNewItem("EmberFlowers_369")
    return

def NorthernMorrowsIsle_358_MapTrigger_18_10(p):
    if StuffDone["110_3"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_3"] = 250
        WorldMap.DeactivateTrigger(Location(66,10))
        Party.GiveNewItem("MandrakeRoot_370")
    return

def NorthernMorrowsIsle_359_MapTrigger_6_27(p):
    if StuffDone["110_4"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_4"] = 250
        WorldMap.DeactivateTrigger(Location(54,27))
        Party.GiveNewItem("Graymold_368")
    return

def NorthernMorrowsIsle_360_MapTrigger_15_34(p):
    if StuffDone["110_5"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_5"] = 250
        WorldMap.DeactivateTrigger(Location(63,34))
        Party.GiveNewItem("Wormgrass_366")
    return

def NorthernMorrowsIsle_361_MapTrigger_26_25(p):
    if StuffDone["110_6"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_6"] = 250
        WorldMap.DeactivateTrigger(Location(74,25))
        SpecialItem.Give("ContactNote")
        Party.GiveNewItem("Wormgrass_366")
    return

def NorthernMorrowsIsle_362_MapTrigger_25_28(p):
    if StuffDone["110_7"] == 250:
        return
    result = ChoiceBox("You notice some unusual plants growing at the base of this large boulder. You look closer. They\'re alchemical ingredients!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["110_7"] = 250
        WorldMap.DeactivateTrigger(Location(73,28))
        Party.GiveNewItem("Graymold_368")
    return

def NorthernMorrowsIsle_363_MapTrigger_2_89(p):
    if StuffDone["201_0"] == 250:
        return
    result = ChoiceBox("As you make your way through these woods, you encounter a camp of Empire soldiers. They\'re an unusually seedy bunch, unwashed and unshaven. When you get close, they stand and approach you.\n\nTheir commander approaches you, smirking, and says \"We\'re guarding this road. Anyone passing must pay a 10 gold toll. Let\'s have it.\" As he says it, the other soldiers laugh. It\'s not friendly laughter.", eDialogPic.CREATURE, 15, ["Leave", "Pay", "Refuse"])
    if result == 1:
        if Party.Gold >= 10:
            MessageBox("You pay the toll, and the smirking guards wave you by.")
            Party.Gold -= 10
            return
        MessageBox("When the guards see that you don\'t even have 10 gold, they share hearty laughter at your expense. They take what you do have, and let you by.")
        Party.Gold -= 10
        return
    elif result == 2:
        if StuffDone["201_0"] == 250:
            return
        StuffDone["201_0"] = 250
        WorldMap.DeactivateTrigger(Location(50,89))
        MessageBox("The soldiers are taken aback. The idea of someone refusing their bullying simply has not occurred to them. As they mutter back and forth about what to do, you notice that none of them have their insignia on their armor.\n\nWhen an Empire soldier is kicked out of the army, the insignia is the first thing torn from him or her. When they see that you\'ve noticed this, they have no choice but to attack.")
        WorldMap.SpawnEncounter("Group_1_0_4", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You decline to pay, and back away. The soldiers let you go.")

def NorthernMorrowsIsle_364_MapTrigger_16_21(p):
    if StuffDone["201_1"] == 250:
        return
    result = ChoiceBox("You come across a large hut. It\'s about two stories high, and in good condition. You would think that it would be very difficult to eke out a living out here in the middle of this enormous swamp, but someone is managing.\n\nAs you get closer, you can see that an old woman is standing at the front door of the hut. She seems to be smiling and eagerly gesturing for you to approach her.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        ChoiceBox("You walk towards the nice looking old lady. As you get closer, you notice she\'s wearing a necklace. As you get even closer, you see that the necklace is decorated with bones. You also notice that the woman has fangs.\n\nYou think twice about approaching, and turn around. Unfortunately, you notice that several more old women are standing behind you, accompanied by their large, reptilian pet.\n\nIt looks like they\'re intent on cooking and eating you. Bad news.", eDialogPic.CREATURE, 29, ["OK"])
        if StuffDone["201_1"] == 250:
            return
        StuffDone["201_1"] = 250
        WorldMap.AlterTerrain(Location(64,21), 1, None)
        WorldMap.DeactivateTrigger(Location(64,21))
        WorldMap.SpawnEncounter("Group_1_0_5", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The poor, lonely old woman looks disappointed by your departure. Soon, she\'s out of sight.")

def NorthernMorrowsIsle_365_MapTrigger_2_36(p):
    if StuffDone["201_3"] == 250:
        return
    result = ChoiceBox("You encounter a band of Empire soldiers, camped alongside the road. They\'re a pretty rough, unshaven bunch - they\'ve been out here for a while.\n\nWhen you get close, they come out and block the road. Their captain says \"Sorry. This area is restricted now. It\'s a 10 gold toll to pass. Let\'s have it.\" As he says it, his troops snicker behind him.", eDialogPic.CREATURE, 15, ["Leave", "Pay", "Refuse"])
    if result == 1:
        if Party.Gold >= 10:
            MessageBox("The soldiers relieve you of your gold, and, smirking, let you pass.")
            Party.Gold -= 10
            return
        MessageBox("The soldiers are quite amused to find that you don\'t even have 10 gold pieces to your name. Laughing harshly, they let you pay what you do have and pass.")
        Party.Gold -= 10
        return
    elif result == 2:
        if StuffDone["201_3"] == 250:
            return
        StuffDone["201_3"] = 250
        WorldMap.DeactivateTrigger(Location(50,36))
        MessageBox("You refuse to pay this extortion. As they quietly discuss amongst themselves what to do, you notice that their armor doesn\'t have its shoulder insignia. When an Empire soldier is booted out, the first thing they do is strip off their insignia!\n\nYou notice this, and they see you notice. Now that they\'ve been discovered, they have no choice but to make sure nobody else finds out.")
        WorldMap.SpawnEncounter("Group_1_0_4", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You refuse to pay and turn away. The guard\'s harsh laughter follows you as you leave.")

def NorthernMorrowsIsle_366_SpecialOnWin0(p):
    MessageBox("In the soldier\'s camp, you find the tolls they\'ve collected from travelers. It adds up to almost 500 gold pieces!")
    Party.Gold += 497

def NorthernMorrowsIsle_367_SpecialOnWin1(p):
    MessageBox("The witches dead, you look for their hut, only to realize it\'s disappeared! You wander around the marshes for hours but can\'t find their intriguing hovel.\n\nThe only interesting thing you manage to recover is a small bone necklace one of the witches was wearing.")
    Party.GiveNewItem("IvoryCharm_331")
