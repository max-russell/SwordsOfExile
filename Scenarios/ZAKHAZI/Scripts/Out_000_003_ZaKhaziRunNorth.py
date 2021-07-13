
def ZaKhaziRunNorth_562_MapTrigger_38_37(p):
    if StuffDone["203_0"] == 250:
        return
    StuffDone["203_0"] = 250
    WorldMap.DeactivateTrigger(Location(38,181))
    WorldMap.DeactivateTrigger(Location(39,181))
    ChoiceBox("After a long, arduous trip over land, you finally reach another part of the river you began your journey on. Unfortunately, your boat is still many miles behind you.\n\nUnless either the path continues or you find another boat, your rescue mission is about to come to an abrupt end.", eDialogPic.STANDARD, 31, ["OK"])

def ZaKhaziRunNorth_563_MapTrigger_35_13(p):
    if StuffDone["203_1"] == 250:
        return
    StuffDone["203_1"] = 250
    WorldMap.DeactivateTrigger(Location(35,157))
    MessageBox("You get a sinking feeling as you look north. There was a path alongside the river up until very recently. Then it was destroyed, probably by a cave quake. You can\'t go any farther north on foot.")

def ZaKhaziRunNorth_565_MapTrigger_10_39(p):
    if StuffDone["203_2"] == 250:
        return
    StuffDone["203_2"] = 250
    WorldMap.DeactivateTrigger(Location(10,183))
    MessageBox("At first, you though it was a natural basalt spire, perched on the shore of this subterranean river. As you got closer, however, you came to realize that it was man-made.\n\nIt\'s a black, windowless tower, about fifty feet high, jutting out slightly into the river. The stone is dark, cracked, and mottled by mold and lichen. It\'s a dark, quiet building, and it doesn\'t look like anyone has visited it for some time.")

def ZaKhaziRunNorth_566_MapTrigger_23_10(p):
    if StuffDone["203_3"] == 250:
        return
    StuffDone["203_3"] = 250
    WorldMap.DeactivateTrigger(Location(23,154))
    WorldMap.DeactivateTrigger(Location(23,153))
    MessageBox("As you row your barge into this underground lake, darkness envelops you. Snaky tentacles of shadow slide up the sides of your craft and envelop you. It\'s as if the darkness is a palpable living thing, so persistent is its advance.")

def ZaKhaziRunNorth_568_MapTrigger_43_20(p):
    result = ChoiceBox("As you stare down into this massive chasm, you notice that a crude stairway has been hewn into its side, spiraling down far beyond the range of your lights into the darkness.\n\nYou toss a pebble over the side and count seconds until you hear it hit the bottom. The sound never comes. This might be a long stairway.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        MessageBox("You climb down, hoping to find a shortcut to Fort Cavalier or, failing that, an interesting encounter. Instead, you just keep climbing. The stairway continues downward, not ending and never coming in sight of the end.\n\nAfter a few hours, you turn back. As intrigued as you are by this stairway, you don\'t have enough time to explore it.")
        Party.Age += 900
        return

def ZaKhaziRunNorth_569_MapTrigger_44_13(p):
    if StuffDone["203_4"] == 250:
        return
    StuffDone["203_4"] = 250
    WorldMap.DeactivateTrigger(Location(44,157))
    MessageBox("As you walk down the path, you meet travelers coming the other way. They look tired and bedraggled by their journey. However, they aren\'t human.\n\nThey\'re humanoids, but their heads and hands are feline. Their fur is matted and scruffy, and they look very hungry. They quickly decide that you would make a good meal for them.")
    WorldMap.SpawnEncounter("Group_0_3_4", p.Target)

def ZaKhaziRunNorth_570_SpecialOnWin0(p):
    MessageBox("You aren\'t sure where they were heading, but you have a guess of why. One of them was carrying a chest filled with gold and edible delicacies, as well as several potions.\n\nThey must have been going to trade with someone. Fortunately, their wealth has ended up in better hands. Yours.")
    Party.GiveNewItem("MediumHealingP_254")
    Party.Gold += 400
    Party.Food += 100
    Party.GiveNewItem("MediumSkillP_259")
    Party.GiveNewItem("MediumInvulnP_258")
