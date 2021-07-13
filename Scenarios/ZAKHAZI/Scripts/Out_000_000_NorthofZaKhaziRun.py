
def NorthofZaKhaziRun_525_MapTrigger_27_41(p):
    ChoiceBox("You pass through the illusionary wall north of Khoth\'s fortress, the wall he counted on to keep his fortress hidden. As you move through, however, something strange happens.\n\nThe spell Khoth cast on you when you paid him finally has its affect. Your minds reel, and you stumble forward. Memories twist, fade, and fall from you. You try to think about Khoth, but it becomes harder, and you stumble again, and ...", eDialogPic.STANDARD, 31, ["OK"])
    ChoiceBox("That\'s odd. What were you thinking about? Something about a dragon? That\'s odd. You didn\'t meet any dragons. You\'ve just emerged from the Za-Khazi Run.\n\nBut why are you standing with your backs to this wall? Well, no matter. Victory is almost yours! You have done what few ever thought possible. You have made it through the Za-Khazi Run!\n\nNow, you need to find Fort Cavalier.", eDialogPic.STANDARD, 31, ["OK"])
    Party.Reposition(Location(28, 39))
    p.CancelAction = True

def NorthofZaKhaziRun_527_MapTrigger_18_36(p):
    if StuffDone["200_0"] == 250:
        return
    StuffDone["200_0"] = 250
    WorldMap.DeactivateTrigger(Location(18,36))
    WorldMap.DeactivateTrigger(Location(18,34))
    WorldMap.DeactivateTrigger(Location(6,34))
    WorldMap.DeactivateTrigger(Location(7,34))
    MessageBox("Here, you can get your last look at the river you\'ve been trying, with uneven success, to follow for the last 200 miles. It sedately flows by you, out of the Run and into the lower caverns.")

def NorthofZaKhaziRun_531_MapTrigger_39_28(p):
    if StuffDone["200_1"] == 250:
        return
    StuffDone["200_1"] = 250
    WorldMap.DeactivateTrigger(Location(39,28))
    WorldMap.DeactivateTrigger(Location(35,36))
    WorldMap.DeactivateTrigger(Location(35,35))
    MessageBox("The floor in this secluded cave is strewn with rubble and bones. Fresh bones. As often happens during a war, predators and scavengers have taken up residence. And considering the size of the tracks, the scavengers here are pretty big.")

def NorthofZaKhaziRun_534_MapTrigger_37_34(p):
    if StuffDone["200_2"] == 250:
        return
    StuffDone["200_2"] = 250
    WorldMap.DeactivateTrigger(Location(37,34))
    WorldMap.DeactivateTrigger(Location(39,32))
    WorldMap.DeactivateTrigger(Location(37,31))
    MessageBox("You come across the party of scavengers. They aren\'t your ordinary bottom feeders - they\'re drakes, creatures powerful enough to stake a claim in this wild area and greedy enough to take all the armor and weapons of the fallen.")
    WorldMap.SpawnEncounter("Group_0_0_4", p.Target)

def NorthofZaKhaziRun_537_MapTrigger_6_17(p):
    if StuffDone["200_3"] == 250:
        return
    StuffDone["200_3"] = 250
    WorldMap.DeactivateTrigger(Location(6,17))
    WorldMap.DeactivateTrigger(Location(19,9))
    ChoiceBox("You detect a peculiar scent as you hike down this long gallery. A peculiar, sweet, comforting, familiar scent. So comforting, in fact, that it makes you very nervous.\n\nThere\'s poppy shrooms ahead. A lot of them.", eDialogPic.TERRAIN, 73, ["OK"])

def NorthofZaKhaziRun_539_MapTrigger_23_10(p):
    if StuffDone["200_4"] == 250:
        return
    StuffDone["200_4"] = 250
    WorldMap.DeactivateTrigger(Location(23,10))
    WorldMap.DeactivateTrigger(Location(27,11))
    ChoiceBox("At last, your goal is before you. Fort Cavalier looms in the path above you. Even now, you can hear the distant roars of battle. Smoke rises from the ramparts, and you see the glow of hostile spells.\n\nThe way for you is clear. The slithzerikai are mainly attacking the front of the fort ... this rear approach is unguarded. You can make your delivery at last.", eDialogPic.STANDARD, 31, ["OK"])

def NorthofZaKhaziRun_541_MapTrigger_37_13(p):
    if StuffDone["200_5"] == 250:
        return
    result = ChoiceBox("Your path is not clear. You can see a slithzerikai scouting party ahead. A large one. There\'s dozens of warriors, sitting around a fire and eating something unpleasant. Several others keep watch, and a few are studying spell books.\n\nThey haven\'t seen you yet, but if you are going to continue down this passage, you\'re going to have to fight for it. It will be an ugly battle.", eDialogPic.CREATURE, 47, ["Leave", "Attack"])
    if result == 1:
        StuffDone["200_5"] = 250
        WorldMap.DeactivateTrigger(Location(37,13))
        WorldMap.DeactivateTrigger(Location(37,12))
        MessageBox("Sure enough, they see you in plenty of time to grab their weapons and prepare. They look fully confidant of victory against your small group, but not so confidant that they\'re going to make any mistakes ...")
        WorldMap.SpawnEncounter("Group_0_0_5", p.Target)
        return
    p.CancelAction = True

def NorthofZaKhaziRun_543_SpecialOnWin0(p):
    MessageBox("You find something the drakes scavenged nearby: a beautiful broadsword.")
    Party.GiveNewItem("MagicBroadsword_84")

def NorthofZaKhaziRun_544_SpecialOnWin1(p):
    MessageBox("Yet another obstacle overcome, yet another group of foes dispatched. You\'re getting very tired, and time keeps getting shorter and shorter. You hope you\'re not that far from your goal ...")
