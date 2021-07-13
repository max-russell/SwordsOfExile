
def WormyHollow_446_MapTrigger_4_11(p):
    if StuffDone["19_4"] == 250:
        return
    StuffDone["19_4"] = 250
    TownMap.List["WormyHollow_19"].DeactivateTrigger(Location(4,11))
    MessageBox("Several massive piles of leaves, moss, and muck at the south end of the cavern shift, heave, and begin to move towards you. At least, that\'s what you think is happening, until you see the pairs of long eyestalks.\n\nOne of them hawks a glob of powerful, acidic spit in your direction. They\'re giant slugs!")
    Town.PlaceEncounterGroup(1)

def WormyHollow_447_MapTrigger_12_22(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(15,24)).Num == 154:
        if StuffDone["17_1"] >= 1:
            if StuffDone["19_5"] >= 1:
                MessageBox("You approach the Vahnatai wall once again. The panel opens, and one of their guards peers out at you. It recognizes you and lets you in.")
                Town.AlterTerrain(Location(15,24), 0, TerrainRecord.UnderlayList[156])
                return
            ChoiceBox("You find signs of intelligent life! There\'s recent construction here - a large, stone wall blocking the corridor. When you get close, a concealed panel in it slides open, and a Vahnatai peers out at you. \"Who being you?\" it asks. \"What doing you here?\"\n\nYou respond that you have seen Casser-Bok. The Vahnatai looks agitated and shuts the panel. After a few minutes, a secret door opens in the wall. The Vahnatai says \"Our leader is speaking with you. Be in peace, or pay much in pain.\"", eDialogPic.CREATURE, 76, ["OK"])
            StuffDone["19_5"] = 1
            Town.AlterTerrain(Location(15,24), 0, TerrainRecord.UnderlayList[156])
            return
        ChoiceBox("You find signs of intelligent life! There\'s recent construction here - a large, stone wall blocking the corridor. When you get close, a concelaed panel in it slides open, and a Vahnatai peers out at you. \"Who being you?\" is asks. \"What doing you here?\"\n\nYou are unable to come up with an answer that satisfies him. He slams the panel shut. Even after a careful search, you can\'t find any cracks or other sign that there was even a panel in the wall, let alone a door.", eDialogPic.CREATURE, 76, ["OK"])
        return

def WormyHollow_448_MapTrigger_15_26(p):
    if StuffDone["19_6"] == 250:
        return
    StuffDone["19_6"] = 250
    TownMap.List["WormyHollow_19"].DeactivateTrigger(Location(15,26))
    TownMap.List["WormyHollow_19"].DeactivateTrigger(Location(16,26))
    MessageBox("Although the Vahnatai were rather angry with Exile after it interfered with their destruction of the surface world some years before, since that time their people and yours have been in a state of uneasy truce.\n\nThat has not stopped the Vahnatai from creating the occasional concealed outpost in Exile lands, such as this one. Such outposts are half diplomatic stations, half dens of espionage. This may be awkward.")

def WormyHollow_450_MapTrigger_27_30(p):
    result = ChoiceBox("The Vahnatai have erected a teleporter here. Being adventurers, you are immediately tempted to leap through it. It seems safe ... you don\'t see fire or lava on the other side.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The portal gives you the wrenching, painful feeling you\'ve come to associate with being teleported a very long distance. You emerge at the other side and come face to face with about 30 very surprised looking Vahnatai.\n\nThe portal must be their shortcut back to their homeland! You don\'t get a chance to look around, though, as they immediately grab you and throw you back into the portal.")
        return
    p.CancelAction = True

def WormyHollow_451_CreatureDeath0(p):
    MessageBox("One of the massive, pale worms blocking your entry into these tunnels has just fallen.")

def WormyHollow_455_CreatureDeath29(p):
    Town.AlterTerrain(Location(26,38), 0, TerrainRecord.UnderlayList[139])
    Town.PlaceField(Location(27,38), Field.QUICKFIRE)

def WormyHollow_456_TalkingTrigger16(p):
    p.TalkingText = "\"I have given the word. The gate to the Crystal Soul has been opened. You may see Presso-Bok now.\""
    Town.AlterTerrain(Location(26,38), 0, TerrainRecord.UnderlayList[148])
