
def RealmofMorog_599_MapTrigger_30_21(p):
    result = ChoiceBox("This cavern has many bone chips littering the ground, but this is the first full-sized body you\'ve found. It looks like it\'s been here for some time, but the specters have sucked it so dry that it didn\'t rot.\n\nAll of its belongings were stripped away by the undead. However, it still has a closed leather satchel at its belt.", eDialogPic.TERRAIN, 179, ["Leave", "Open"])
    if result == 1:
        ChoiceBox("You find a journal inside. Apparently, this body was once the physical form of a man named Coriddo. He came into the Za-Khazi Run to search for a lost mine filled with opals of the highest quality.\n\nThe last entry is of interest:\n\n\"The passage to the mines is just to the north. It is supposed to be then off to the east, and then down through rough territory.\"\n\n\"The mist beings have my trail, though. I will have to hurry. I\'m sure I can afford a little sleep. Then I will be off again, and soon the wealth will be mine!\"", eDialogPic.TERRAIN, 179, ["OK"])
        return

def RealmofMorog_600_MapTrigger_13_34(p):
    result = ChoiceBox("You reach the shore of a frigid, underground lake, devoid of living things. The thick layer of mist covers the surface.\n\nAs you watch, several thick wisps of mist grow more solid and begin to float across the water towards you.", eDialogPic.STANDARD, 31, ["Leave", "Wait"])
    if result == 1:
        MessageBox("When the mist gets close, you realize that they are the same sort of mist beings as the hostile creatures to the south. These spectres, however, don\'t bother to ask you any questions before they attack.")
        WorldMap.SpawnEncounter("Group_0_6_4", p.Target)
        return
    MessageBox("You walk away quickly. As you do, the wisps of mist fade back into the darkness.")

def RealmofMorog_601_MapTrigger_42_33(p):
    MessageBox("You feel funny.")
    Party.Reposition(Location(44, 321))
    p.CancelAction = True

def RealmofMorog_602_MapTrigger_41_37(p):
    MessageBox("You feel funny.")
    Party.Reposition(Location(43, 324))
    p.CancelAction = True

def RealmofMorog_603_MapTrigger_40_46(p):
    MessageBox("You feel very, very odd.")
    Party.Reposition(Location(38, 333))
    p.CancelAction = True

def RealmofMorog_604_MapTrigger_31_42(p):
    if StuffDone["206_1"] == 250:
        return
    result = ChoiceBox("Your sharp eyes spot some of the natural bounty of these caverns. There are several twisted, brown growths growing nearby. A close inspection reveals that they\'re alchemical ingredients!", eDialogPic.STANDARD, 8, ["Take", "Leave"])
    if result == 0:
        StuffDone["206_1"] = 250
        WorldMap.DeactivateTrigger(Location(31,330))
        Party.GiveNewItem("MandrakeRoot_370")
    return
