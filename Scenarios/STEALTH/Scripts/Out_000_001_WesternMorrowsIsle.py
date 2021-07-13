
def WesternMorrowsIsle_396_MapTrigger_42_25(p):
    if StuffDone["204_0"] == 250:
        return
    result = ChoiceBox("You find the remains of a mage who crash landed while flying over these mountains. The wand at his side is still intact. Most everything else has been eaten by bears.", eDialogPic.TERRAIN, 19, ["Take", "Leave"])
    if result == 0:
        StuffDone["204_0"] = 250
        WorldMap.AlterTerrain(Location(42,73), 1, None)
        WorldMap.DeactivateTrigger(Location(42,73))
        WorldMap.AlterTerrain(Location(39,78), 1, None)
        WorldMap.DeactivateTrigger(Location(39,78))
        SpecialItem.Give("ContactNote")
        Party.GiveNewItem("WandofFlame_285")
    return

def WesternMorrowsIsle_397_MapTrigger_34_31(p):
    if StuffDone["204_1"] == 250:
        return
    StuffDone["204_1"] = 250
    WorldMap.DeactivateTrigger(Location(34,79))
    MessageBox("This path up into the mountains is lined with white gravel. It\'s broken up pieces of what looks like marble, broken into thumb sized pieces. Someone has been doing some peculiar, rustic landscaping.")

def WesternMorrowsIsle_398_MapTrigger_39_30(p):
    if StuffDone["204_0"] == 250:
        return
    result = ChoiceBox("At the high end of the path, you find a low, dark cave entrance. The white gravel is piled much higher here, in some places coming up to your waist.", eDialogPic.TERRAIN, 195, ["Leave", "Enter"])
    if result == 1:
        StuffDone["204_0"] = 250
        WorldMap.AlterTerrain(Location(42,73), 1, None)
        WorldMap.DeactivateTrigger(Location(42,73))
        WorldMap.AlterTerrain(Location(39,78), 1, None)
        WorldMap.DeactivateTrigger(Location(39,78))
        ChoiceBox("You work your way slowly into the cave. Rounding a corner in the passage, you come upon an incredibly lifelike statue of a human male.\n\nSomeone or something has been gnawing away at it - large chunks have been broken off, and there are scrapes around the broken bits that look like they were made by claws.\n\nYou suddenly realize that the statue is made of the same material as the gravel. By the time you realize where the statue came from, the basilisks have already found you.", eDialogPic.CREATURE, 86, ["OK"])
        WorldMap.SpawnEncounter("Group_0_1_4", p.Target)
        return

def WesternMorrowsIsle_399_MapTrigger_28_40(p):
    if StuffDone["211_3"] >= 1:
        MessageBox("If you hadn\'t found that peculiar \"First Stone\" at the east end of the island, you wouldn\'t have known to keep an eye open for the peculiar markers. You find another one in this grove.\n\nThe marker is carved from granite. When you scrape off the moss, you reveal the words carved into its side: \"Second Stone.\"")
        StuffDone["204_3"] = 1
        return

def WesternMorrowsIsle_400_MapTrigger_6_36(p):
    if StuffDone["204_4"] == 250:
        return
    result = ChoiceBox("At the far end of this peninsula, you see a small, walled community of stone and wood buildings, surrounded by fairly healthy looking, quite well armed townfolk. A sign reads \"Phalia Colony - Strife will NOT be tolerated.\"\n\nBefore you even get close, a band of soldiers materializes out of the brush around you. Their blades are out.\n\nOne of them says \"Hold on there, visitors. Strangers are welcome here, but you leave your fightin\' ways out there. We\'ll have none of that rebel nonsense here. Agreed?\"", eDialogPic.TERRAIN, 189, ["Yes", "Attack"])
    if result == 0:
        result = ChoiceBox("You are shown into Phalia Colony, where people warily greet you and ask of goings on in the rest of the Isle. This colony was formed by people sickened by the Empire\'s constant, bloody fighting with the rebels.\n\nThey came here to try to avoid the strife, and one person says to you, over mugs of home brewed ale, \"You\'d be best not getting involved in any of that. There\'s no white and black hats, just butchers. If I were you, I\'d leave this place.\"\n\nAfter a while, once you\'ve both traded all of your information, the people start dropping hints that maybe you\'d be happier moving on. Before you go, they ask if you\'d like to barter for some trade goods. Would you?", eDialogPic.TERRAIN, 189, ["Leave", "Buy"])
        if result == 1:
            OpenShop("Shop_Items_Outside_13_0_1")
            p.CancelAction = True
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You bid farewell to the peculiar people of Phalia Colony. You have a hard time condoning their withdrawal from the world, but it\'s certainly easy to understand it.")
        return
    elif result == 1:
        if StuffDone["204_4"] == 250:
            return
        StuffDone["204_4"] = 250
        WorldMap.AlterTerrain(Location(6,84), 1, None)
        WorldMap.DeactivateTrigger(Location(6,84))
        MessageBox("You draw your blades and attack. They shout for help, and you are disconcerted to see the entire colony drop what it\'s doing, grab the nearest weapon, and charge. They sure haven\'t survived out here by being soft.")
        WorldMap.SpawnEncounter("Group_0_1_5", p.Target)
        return

def WesternMorrowsIsle_401_MapTrigger_26_10(p):
    if StuffDone["204_5"] == 250:
        return
    StuffDone["204_5"] = 250
    WorldMap.AlterTerrain(Location(26,58), 1, None)
    WorldMap.DeactivateTrigger(Location(26,58))
    ChoiceBox("Intrigued by this strange, semi-circular rock formation, you walk in to investigate. Soon, however, you find yourself on a path with high outcroppings on all sides. It\'s a perfect location for an ambush.\n\nAs you turn back to get to more secure ground, you realize you\'re being watched. Empire soldiers have moved from concealment above you, surrounding you. Their weapons are out - for a moment, you think they\'re about to attack!\n\nAs you prepare a defense, however, their leader, a massive Empire Dervish, salutes to you. How odd ... he must recognize you from somewhere. He makes a sharp, chopping hand signal, and the soldiers disappear into the rubble.\n\nWhat a lucky break. Word that you\'re supposed to be working for the Empire must have gotten around somehow.", eDialogPic.CREATURE, 17, ["OK"])

def WesternMorrowsIsle_402_MapTrigger_12_16(p):
    if StuffDone["204_6"] == 250:
        return
    result = ChoiceBox("You find a motley network of abandoned log buildings. This used to be a lumberyard. Trees were cut down, shaped into rough planks, and carted out on rough, rutted roads.\n\nIt\'s abandoned now, and not under peaceful circumstances. You find broken arrows, shattered windows, and even a few bloodstains.\n\nBeing adventurers, you look around a little bit for loot. Most of what\'s left is junk. You do find a reasonably nice axe buried in a tree behind the mess hall.", eDialogPic.TERRAIN, 190, ["Take", "Leave"])
    if result == 0:
        StuffDone["204_6"] = 250
        WorldMap.AlterTerrain(Location(12,64), 1, None)
        WorldMap.DeactivateTrigger(Location(12,64))
        Party.GiveNewItem("IronAxe_54")
    return

def WesternMorrowsIsle_403_SpecialOnWin0(p):
    MessageBox("The basilisk\'s lair is now yours to loot. You dive in with enthusiasm. There\'s a wide variety of coins and trinkets waiting for you in the back of the cave.\n\nMost of the weaponry and armor taken off the lizards\' victims (mainly Empire patrols) has been eaten by the peculiar creatures. One small sword, however, was not of interest to them.")
    Party.GiveNewItem("Boltblade_360")
    Party.Gold += 300

def WesternMorrowsIsle_404_SpecialOnWin1(p):
    MessageBox("Bloodied and battered, you look at the Colony, hoping to find some good loot. Crestfallen, you see that the buildings are merrily ablaze. Someone must have put fire to them when they realized you were going to win the battle.\n\nWhat a waste of a perfectly good combat.")
