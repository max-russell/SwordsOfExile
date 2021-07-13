
def IcyTunnels_96_MapTrigger_41_42(p):
    if StuffDone["8_1"] == 250:
        return
    StuffDone["8_1"] = 250
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(41,42))
    MessageBox("You enter a large chamber. In the ceiling, you see a shaft extending straight up about 30 or 40 feet to a brightly lit chamber. At the top, you see ogres peering down at you, laughing and pointing.\n\nThe floor of this chamber is littered with broken ogre bodies. Bloody tracks leading to the south, however, indicate that not all of the ogres died in the fall. Some other unpleasant fate must have awaited them.")

def IcyTunnels_97_MapTrigger_42_45(p):
    if StuffDone["8_2"] == 250:
        return
    StuffDone["8_2"] = 250
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(42,45))
    MessageBox("As you make your way down the dark tunnel, there\'s one thing you notice before anything else: it\'s cold! That\'s to be expected to some extent in any system of caves, but this is unnatural. The walls and floor are covered with ice.\n\nYour teeth start to chatter. You\'d better get moving, before hypothermia sets in.")

def IcyTunnels_98_MapTrigger_27_31(p):
    if StuffDone["8_3"] == 250:
        return
    StuffDone["8_3"] = 250
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(27,31))
    ChoiceBox("As you leave the underground lake, you experience an all too familiar phenomenon: a disembodied voice, coming from the air around you. It\'s a slow, calm, sibilant, reptilian voice, icy and malevolent.\n\nIt says \"Ah! So yet another group of pitiful ogres has been sent to amuse me. Do not fear, little ogrelings. Do not concern yourselves. Your death is assured. There is no need to waste your energy on fear.\"\n\n\"You don\'t want your sacrifice to be in vain, do you? I thought not. Please move on. My pets are waiting to greet you.\"", eDialogPic.STANDARD, 8, ["OK"])

def IcyTunnels_99_MapTrigger_11_25(p):
    ChoiceBox("The reptilian voice reappears. This time, it\'s less disdainful, and more amused. \"I sense you are still with us. That is much better than most of you little ogres do.\"\n\n\"Do not concern yourselves with my anger at your killing my children. If they were not able to handle the likes of you, they deserved to die. We are cruel down here, but fair. To some extent.\"\n\n\"I am amused by your progress. Continue. If you make it to the end, you will certainly have shown yourselves worthy of being eaten by me. It\'s more of an honor to my race than you might think.\"", eDialogPic.STANDARD, 8, ["OK"])

def IcyTunnels_100_MapTrigger_19_18(p):
    if StuffDone["8_5"] == 250:
        return
    StuffDone["8_5"] = 250
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(19,18))
    ChoiceBox("You hear the voice again. It is no longer amused, by quite surprised. \"Still with us, I see? Now you ogres aren\'t cheating with your payments and throwing down a mage or two, are you?\"\n\n\"Were that the case, rest assured I\'ll be up there before long to eat quite a few of you. Such surprises were not part of the deal.\"\n\nThere is a pause. \"Please, move on. I am eager to meet you. The new friend in the next cave, I\'m sure you will have no trouble dispatching.\"", eDialogPic.STANDARD, 8, ["OK"])

def IcyTunnels_101_MapTrigger_35_9(p):
    if StuffDone["8_6"] == 250:
        return
    StuffDone["8_6"] = 250
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(35,9))
    ChoiceBox("The voice is starting to grow annoyed. \"Now I am truly surprised by your progress. Surprised and angered. I see now I should have not put my valuable pets at risk, even to a bumbling group of ogres.\"\n\n\"Do not fret. Your ordeal is almost ended. Soon you will be face to face with me! Prepare well!\"", eDialogPic.STANDARD, 8, ["OK"])

def IcyTunnels_102_MapTrigger_25_46(p):
    if StuffDone["8_7"] == 250:
        return
    result = ChoiceBox("You find a large pool of brackish, iced over water, made slightly green by the algae imprisoned by the cold.\n\nBy the main pool is a smaller pool, which, oddly, is not frozen. The pool is in a natural basin composed of a white, chalky substance. The stuff has infused the water, which has a milky appearance.", eDialogPic.TERRAIN, 75, ["Leave", "Drink"])
    if result == 1:
        StuffDone["8_7"] = 250
        TownMap.List["IcyTunnels_8"].AlterTerrain(Location(25,46), 1, None)
        TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(25,46))
        MessageBox("You drink the water, and almost immediately start to feel invigorated! The chalky stuff must be doing it. You all bend down and drink more, almost immediately sucking up all of the small pool.\n\nThe pool is gone, but your wounds are fully healed. You\'re ready to continue.")
        Party.HealAll(200)
        return

def IcyTunnels_103_MapTrigger_46_31(p):
    if StuffDone["8_8"] == 250:
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
    StuffDone["8_8"] = 250
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(46,31))
    pc.RunTrap(eTrapType.DART, 2, 39)

def IcyTunnels_104_MapTrigger_18_11(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["8_9"] == 250:
        return
    StuffDone["8_9"] = 250
    result = ChoiceBox("At last, you reach the far end of this icy gauntlet and come face to face with your tormentor. You soon wish you hadn\'t. It\'s a ice drake! It\'s an enormous lizard, slightly smaller cousin to dragonkind, 40 feet from head to tail.\n\nWhen the fearsome blue creature sees you enter his cavern, it rears up, ready to breathe doom upon you. However, when it gets a good look at you, it lowers its forelegs to the ground, and looks at you, confused.\n\nThis moment may be the distraction you can use to attack safely!", eDialogPic.CREATURE2x1, 2, ["Attack", "Wait"])
    if result == 0:
        MessageBox("The drake\'s delay in attacking was only temporary. It emits an amused, arrogant snort. Then, with a deafening roar, it moves forward to join with you in battle!")
        Town.PlaceEncounterGroup(1)
        return
    elif result == 1:
        result = ChoiceBox("You stare at each other for several stressful moments. Then the drake breaks into laughter! It roars with amusement, looks at you, then roars again!\n\n\"Oh, this is amusing,\" it chortles. \"All this time I though you were just another ogre sacrifice that got lucky, and here you are, a fully equipped group of adventurers. How droll!\"\n\n\"Well, I imagine you\'ve just come to kill me and take my horde, or something tedious and futile like that. If that is the case, you might as well just attack me and get this over with.\"\n\nIt thinks \"Of course, you might be here for some other purpose. Sometimes humans, far in the past, before the dark days of the Empire, came to me for my wisdom. Have you some to see me for any other reason?\"\n\nThe drake might know what happened to the papers you\'re looking for. Of course, this could also be a trap. Do you talk to it and say what you\'re after?", eDialogPic.CREATURE2x1, 2, ["No", "Yes"])
        if result == 0:
            MessageBox("The drake\'s delay in attacking was only temporary. It emits an amused, arrogant snort. Then, with a deafening roar, it moves forward to join with you in battle!")
            Town.PlaceEncounterGroup(1)
            return
        elif result == 1:
            result = ChoiceBox("You describe to the drake the papers you\'re looking for. It thinks. \"Old Empire records. Come to think of it, yes, I do have something like that.\" It leaves the cavern for a moment, and then returns.\n\n\"Yes! The ogres once thought that they could appease me with something besides sacrifices, and threw down to me everything they could get their hands on, including a bunch of old records.\"\n\n\"Normally, I would charge you a stiff price for these papers, like a human sacrifice or some such, but I have the nagging feeling the Empire really doesn\'t want you to have these.\"\n\n\"The Empire has killed almost all of my kind. Anything that annoys them, I will help with. Therefore, I will give you these papers for only 500 gold, or however much gold you have if you don\'t have that.\"\n\nIt snorts a powerful cloud of frost from its enormous nostrils. \"Do you agree?\"", eDialogPic.CREATURE2x1, 2, ["No", "Yes"])
            if result == 0:
                MessageBox("The drake\'s delay in attacking was only temporary. It emits an amused, arrogant snort. Then, with a deafening roar, it moves forward to join with you in battle!")
                Town.PlaceEncounterGroup(1)
                return
            elif result == 1:
                ChoiceBox("It nods, satisfied (and perhaps slightly relieved at avoiding a combat with you). You pay it your gold, and it leaves the cavern to retrieve the Empire papers. It gives the thick bundle to you.\n\nIt chuckles again, and says \"Good luck with your efforts. The only thing I enjoy more than the taste of your kind\'s flesh is the thought of your leader\'s misfortune.\"\n\nWith that benediction, it shows to you a rear exit at the far end of its lair, and slams a portcullis closed behind you with an enormous, clawed foot. It turns and walks away, leaving you with your prize, and the exit before you!", eDialogPic.CREATURE2x1, 2, ["OK"])
                StuffDone["8_0"] = 1
                SpecialItem.Give("EmpirePapers")
                Town.AlterTerrain(Location(4,7), 0, TerrainRecord.UnderlayList[130])
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(3,7))
                p.CancelAction = True
                Party.Gold -= 500
                return
            return
        return

def IcyTunnels_105_MapTrigger_7_15(p):
    if StuffDone["7_9"] == 250:
        return
    StuffDone["7_9"] = 250
    TownMap.List["IcyTunnels_8"].AlterTerrain(Location(7,15), 1, None)
    TownMap.List["IcyTunnels_8"].DeactivateTrigger(Location(7,15))
    MessageBox("Searching greedily through the drake\'s treasure trove, you notice a thick sheaf of papers tossed carelessly off in the corner. You look them over and realize that they\'re a packet of Empire troop orders and patrol rosters!\n\nThese must be the papers you were sent to get. You put them safely in your pack.")
    SpecialItem.Give("EmpirePapers")
    StuffDone["8_0"] = 1

def IcyTunnels_106_MapTrigger_2_5(p):
    if SpecialItem.PartyHas("EmpirePapers"):
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You see sunlight ahead. Looks like you\'re near the exit. You hesitate. Maybe it\'s not a good idea to leave here until you\'ve got the papers you need. You turn back.")

def IcyTunnels_107_TownTimer_0(p):
    MessageBox("The unnatural cold of these tunnels is starting to get to you.")
    Party.Damage(Maths.Rand(3, 1, 6) + 0, eDamageType.COLD)
    Wait()

def IcyTunnels_108_OnEntry(p):
    MessageBox("As you start walking down the stairs, you hear a clang behind you. You look back, and see that the ogres have closed the huge portcullis behind you. With a sinking feeling, you realize you\'re trapped down here.")

def IcyTunnels_109_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(7, 28),WorldMap.SectorAt(Party.OutsidePos))
    if p.Dir.IsNorth:
        MessageBox("As you leave the drake\'s lair, you try to make a note of the location of the rear exit, so that you can return later and find more loot. Unfortunately, when you walk outside and look back, you see the tunnel you\'ve emerged from is gone!\n\nYou feel the natural stone walls, looking for a hidden entrance. The drake must have placed powerful magic here ... the entrance is completely gone.")
