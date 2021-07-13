
def NearSelathni_463_MapTrigger_18_12(p):
    if StuffDone["209_0"] == 250:
        return
    StuffDone["209_0"] = 250
    WorldMap.DeactivateTrigger(Location(66,108))
    WorldMap.DeactivateTrigger(Location(66,106))
    WorldMap.DeactivateTrigger(Location(67,105))
    WorldMap.DeactivateTrigger(Location(74,108))
    WorldMap.DeactivateTrigger(Location(74,106))
    WorldMap.DeactivateTrigger(Location(70,105))
    WorldMap.DeactivateTrigger(Location(71,105))
    MessageBox("As you enter the countryside of Morrow\'s Isle, you idly put your hand in your pocket. There\'s something unfamiliar there! You pull it out. It\'s a piece of paper. (A special item. To see it, click on the \'Spec\' button on the items screen.)\n\nYou read it. It says \'The rebellion needs help. We can reward you well. Go to Canizares, in the town of Liam. Say \'Invisible\' to him. He will tell you of us. Fight for justice!\'")
    SpecialItem.Give("ContactNote")

def NearSelathni_470_MapTrigger_18_38(p):
    if StuffDone["209_1"] == 250:
        return
    result = ChoiceBox("In the far corner of this grim fen, you find a large depression. You could climb down into it, although it would be tricky. After all, everything is covered with a thin layer of smelly, viscous goo.", eDialogPic.TERRAIN, 78, ["Leave", "Enter"])
    if result == 1:
        StuffDone["209_1"] = 250
        WorldMap.AlterTerrain(Location(66,134), 1, None)
        WorldMap.DeactivateTrigger(Location(66,134))
        MessageBox("You make your gooey way down into the hollow. At first, the huge piles of bilious muck and goo make you think you\'ve just found a large, abandoned trash pit. Then the piles of goo start to move!")
        WorldMap.SpawnEncounter("Group_1_2_4", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Probably a wise idea. Some things are better left alone. Especially gooey things.")

def NearSelathni_471_MapTrigger_42_22(p):
    result = ChoiceBox("You find an isolated cluster of farmhouses, surrounded by a low, stone wall. You see some people working in and around it. When they catch sight of you, they shout to each other, and huddle nervously. Some have weapons.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        ChoiceBox("As you walk up, two of the farmers, each wielding a rusty broadsword, approach and greet you. In a brief, unhelpful conversation, they convey to you their nervousness with strangers in these troubled times, and the perceived extreme danger from rebels.\n\nWhen it becomes clear there\'s no help for you here, you depart.", eDialogPic.TERRAIN, 190, ["OK"])
        return

def NearSelathni_472_MapTrigger_42_34(p):
    if StuffDone["209_2"] == 250:
        return
    result = ChoiceBox("You find an isolated cluster of farmhouses, surrounded by a low, stone wall. You see some people working in and around it. When they catch sight of you, they shout to each other, and huddle nervously. Some have weapons.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        StuffDone["209_2"] = 250
        WorldMap.AlterTerrain(Location(90,130), 1, None)
        WorldMap.DeactivateTrigger(Location(90,130))
        ChoiceBox("As you walk closer, you realize that the number of weapons visible is increasingly rapidly. You also notice that these \"farmers\" are wearing leather jerkins, and other sorts of non-agrarian oriented armor items.\n\nIt would appear you\'ve interrupted a particularly industrious group of brigands ...", eDialogPic.CREATURE, 18, ["OK"])
        WorldMap.SpawnEncounter("Group_1_2_5", p.Target)
        return

def NearSelathni_473_MapTrigger_3_6(p):
    MessageBox("You stumble upon the remains of a small skirmish. The grass has been scorched by fireballs, and broken arrows and reddish brown stains mar the ground.")

def NearSelathni_474_MapTrigger_4_28(p):
    MessageBox("Wandering through these lush, grassy fields, you can\'t help but notice how rich the land on the island is. The potential wealth here, for someone determined to work it hard, is considerable.\n\nAnd you\'ve only seen a small part of Morrow\'s Isle. You\'re starting to see why people are so determined to fight over this place.")

def NearSelathni_475_MapTrigger_41_2(p):
    if StuffDone["209_3"] == 250:
        return
    StuffDone["209_3"] = 250
    WorldMap.DeactivateTrigger(Location(89,98))
    ChoiceBox("Oh, no! Spiders! The mean kind!", eDialogPic.CREATURE, 97, ["OK"])
    WorldMap.SpawnEncounter("Group_1_2_6", p.Target)

def NearSelathni_476_SpecialOnWin0(p):
    MessageBox("The slugs dead, you wade through the acidic goo surrounding their lair, looking for loot. Most of their victims\' possessions have either dissolved or sunk into the swampy mire.\n\nYou do find one interesting thing. It\'s a halberd, which someone has placed up in the branches of a gnarled tree. It\'s still in decent condition.")
    Party.GiveNewItem("BronzeHalberd_48")

def NearSelathni_477_SpecialOnWin1(p):
    ChoiceBox("The brigands slain, you investigate the farmhouses. Fortunately, you arrived in time. You find the residents inside, tightly bound. After freeing them and receiving many heartfelt thanks and a few apple pies, you loot the bandits\' bodies.\n\nThey\'ve had a so-so career. You find a fair amount of gold, but their armor and weapons are sub par. Only the mage\'s robes are of high quality. You help yourselves, and, after receiving many hugs and flowers from the farmers, you depart.", eDialogPic.CREATURE, 18, ["OK"])
    MessageBox("(You later find that the apple pies are very tasty.)")
    Party.GiveNewItem("MagicRobes_383")
    Party.Gold += 500
    Party.Food += 50

def NearSelathni_478_SpecialOnWin2(p):
    MessageBox("Phew! That was close!")
