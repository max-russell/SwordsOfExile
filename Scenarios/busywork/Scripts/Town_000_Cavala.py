
def Cavala_0_MapTrigger_10_36(p):
    result = ChoiceBox("The mayor of Cavala has been kind enough to set a bedroom in the barracks aside for you. When you need to rest, you can always return here.", eDialogPic.TERRAIN, 143, ["Leave", "Rest"])
    if result == 1:
        MessageBox("The beds are soft and comfortable, and the barracks are kept nice and warm. You have a pleasant, restful sleep.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += 300
            Party.HealAll(200)
            Party.RestoreSP(200)
        return

def Cavala_1_MapTrigger_39_26(p):
    StuffDone["0_0"] += 1
    if StuffDone["0_0"] == 250:
        TownMap.List["Cavala_0"].DeactivateTrigger(Location(39,26))
    p.CancelAction = True
    if StuffDone["0_0"] >= 3:
        MessageBox("It\'s the same old routine. An alarm goes off. The guards come running in. Mayor Leondardo comes soon after, giving you a look both annoyed and disappointed.\n\nYou\'re warned not to search private property without permission again, and the guards leave.")
        return
    if StuffDone["0_0"] >= 2:
        ChoiceBox("As you walk down the corridor, an alarm sounds, the same sort of alarm that went off last time. Once again, guards come running almost immediately. They grab you.\n\nNot long after, Mayor Leonardo walks in, looking extremely peeved. \"Not again,\" he says. \"Did I not tell you that we don\'t like strangers peeking into our private homes?\"\n\n\"Release them,\" he says to the guards. \"We appreictae your help, but you still have to live by our rules. Stay out of our private areas.\" He leaves, with the guards following behind.", eDialogPic.CREATURE, 31, ["OK"])
        return
    ChoiceBox("As you walk down the corridor, a loud alarm rings out! You freeze, pull your weapons, and get ready to be attacked.\n\nSoon after, guards come running in, led by Mayor Leonardo. When they see you, they relax. A few of them laugh. The Mayor, looking visibly relieved, says \"Oh, it\'s you. We were afraid it was the bandits.\"\n\n\"While we appreciate your help in this unpleasant manner, we can\'t allow strangers to go poking around in our private quarters. Please respect us in this.\" Having said this, he leads the guards away.", eDialogPic.CREATURE, 31, ["OK"])

def Cavala_2_MapTrigger_34_21(p):
    if StuffDone["0_2"] < 1:
        StuffDone["0_0"] += 1
        if StuffDone["0_0"] == 250:
            TownMap.List["Cavala_0"].DeactivateTrigger(Location(39,26))
        p.CancelAction = True
        if StuffDone["0_0"] >= 3:
            MessageBox("It\'s the same old routine. An alarm goes off. The guards come running in. Mayor Leondardo comes soon after, giving you a look both annoyed and disappointed.\n\nYou\'re warned not to search private property without permission again, and the guards leave.")
            return
        if StuffDone["0_0"] >= 2:
            ChoiceBox("As you walk down the corridor, an alarm sounds, the same sort of alarm that went off last time. Once again, guards come running almost immediately. They grab you.\n\nNot long after, Mayor Leonardo walks in, looking extremely peeved. \"Not again,\" he says. \"Did I not tell you that we don\'t like strangers peeking into our private homes?\"\n\n\"Release them,\" he says to the guards. \"We appreictae your help, but you still have to live by our rules. Stay out of our private areas.\" He leaves, with the guards following behind.", eDialogPic.CREATURE, 31, ["OK"])
            return
        ChoiceBox("As you walk down the corridor, a loud alarm rings out! You freeze, pull your weapons, and get ready to be attacked.\n\nSoon after, guards come running in, led by Mayor Leonardo. When they see you, they relax. A few of them laugh. The Mayor, looking visibly relieved, says \"Oh, it\'s you. We were afraid it was the bandits.\"\n\n\"While we appreciate your help in this unpleasant manner, we can\'t allow strangers to go poking around in our private quarters. Please respect us in this.\" Having said this, he leads the guards away.", eDialogPic.CREATURE, 31, ["OK"])
        return

def Cavala_3_MapTrigger_9_13(p):
    if StuffDone["0_1"] < 1:
        StuffDone["0_0"] += 1
        if StuffDone["0_0"] == 250:
            TownMap.List["Cavala_0"].DeactivateTrigger(Location(39,26))
        p.CancelAction = True
        if StuffDone["0_0"] >= 3:
            MessageBox("It\'s the same old routine. An alarm goes off. The guards come running in. Mayor Leondardo comes soon after, giving you a look both annoyed and disappointed.\n\nYou\'re warned not to search private property without permission again, and the guards leave.")
            return
        if StuffDone["0_0"] >= 2:
            ChoiceBox("As you walk down the corridor, an alarm sounds, the same sort of alarm that went off last time. Once again, guards come running almost immediately. They grab you.\n\nNot long after, Mayor Leonardo walks in, looking extremely peeved. \"Not again,\" he says. \"Did I not tell you that we don\'t like strangers peeking into our private homes?\"\n\n\"Release them,\" he says to the guards. \"We appreictae your help, but you still have to live by our rules. Stay out of our private areas.\" He leaves, with the guards following behind.", eDialogPic.CREATURE, 31, ["OK"])
            return
        ChoiceBox("As you walk down the corridor, a loud alarm rings out! You freeze, pull your weapons, and get ready to be attacked.\n\nSoon after, guards come running in, led by Mayor Leonardo. When they see you, they relax. A few of them laugh. The Mayor, looking visibly relieved, says \"Oh, it\'s you. We were afraid it was the bandits.\"\n\n\"While we appreciate your help in this unpleasant manner, we can\'t allow strangers to go poking around in our private quarters. Please respect us in this.\" Having said this, he leads the guards away.", eDialogPic.CREATURE, 31, ["OK"])
        return

def Cavala_4_MapTrigger_12_15(p):
    result = ChoiceBox("On the wall behind the potted plant, you find a small red button. It\'s pretty small ... you were lucky to notice it. You wonder what it does.", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        MessageBox("The button is very quiet. It doesn\'t make any noise when you push it. It also doesn\'t seem to do anything. It probably had some effect somewhere, but you have no idea what.")
        if StuffDone["0_1"] == 0: StuffDone["0_1"] = 1
        else: StuffDone["0_1"] = 0
        return

def Cavala_5_MapTrigger_40_17(p):
    result = ChoiceBox("On the wall behind the potted plant, you find a small red button. It\'s pretty small ... you were lucky to notice it. You wonder what it does.", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        MessageBox("The button is very quiet. It doesn\'t make any noise when you push it. It also doesn\'t seem to do anything. It probably had some effect somewhere, but you have no idea what.")
        if StuffDone["0_2"] == 0: StuffDone["0_2"] = 1
        else: StuffDone["0_2"] = 0
        return

def Cavala_6_MapTrigger_18_24(p):
    if StuffDone["0_4"] >= 1:
        if StuffDone["0_5"] == 250:
            return
        StuffDone["0_5"] = 250
        MessageBox("As you leave Ilona\'s offices, you see a half dozen guards leaving Cameron\'s smithy. At first, you think they might have captured him. Then you see that they look extremely disappointed.\n\nHe probably got away, but you might still be able to find some useful evidence that was left behind.")
        return

def Cavala_9_MapTrigger_26_19(p):
    if StuffDone["0_4"] >= 1:
        Town.AlterTerrain(Location(34,19), 0, TerrainRecord.UnderlayList[161])
        if StuffDone["0_6"] == 250:
            return
        StuffDone["0_6"] = 250
        ChoiceBox("As you enter Cameron\'s smithy, a guard walks up to you. \"We weren\'t fast enough,\" she says. \"He ran off into the woods before we were able to catch him. He was helping the bandits all along.\"\n\n\"There was a locked up room in there. We knocked the door down. There\'s some stuff in there which might interest you. Be sure to look with.\" With that said, she walks off.", eDialogPic.CREATURE, 12, ["OK"])
        return

def Cavala_10_MapTrigger_35_19(p):
    MessageBox("Cameron emptied out this small chest before he fled. There\'s nothing left. No gold, no maps. However, behind the chest, you find something interesting. It\'s a map! Somehow, it fell back there.\n\nThe map is exactly what you were looking for. It shows, in a small side valley not far to the south, a concealed cave, marked \"Hideout.\" Using the map, you will be able to find the bandit\'s lair.")
    TownMap.List["BanditHideout_3"].Hidden = False

def Cavala_11_MapTrigger_14_23(p):
    MessageBox("The books on these shelves contain records of the Sourgrass harvests and ledgers listing the number of bottles of Hrras juice made and sold. There\'s also descriptions of the caravans lost to bandits.\n\nYou look through these records for a while, but you\'re unable to find anything which helps you uncover the hiding place of the bandits.")

def Cavala_15_MapTrigger_28_11(p):
    if StuffDone["0_7"] == 250:
        return
    StuffDone["0_7"] = 250
    TownMap.List["Cavala_0"].DeactivateTrigger(Location(28,11))
    MessageBox("This shrine is provided for the use of merchants and caravan workers. Unfortunately, it\'s unused and poorly tended. Dust covers everything.")

def Cavala_16_MapTrigger_32_27(p):
    if StuffDone["100_0"] >= 1:
        if StuffDone["0_8"] == 250:
            return
        StuffDone["0_8"] = 250
        ChoiceBox("You meet Mayor Leonardo again and tell him of your victory over the bandits. To say he is overjoyed would be a dramatic understatement. He calls in guards to tell the news, and they soon spread it around town.\n\nLeonardo turns to you and says \"You have done well. Thanks to you, our village has a chance to grow and prosper once again.\"\n\n\"I have received a letter from the city of Krizsan. They tell me that, when you return, if you have completed your mission, you will be amply rewarded. I will send word ahead of you that that reward was well-earned.\"\n\n\"Thank you again, and good luck to you in your travels.\"", eDialogPic.CREATURE, 31, ["OK"])
        return

def Cavala_17_MapTrigger_9_12(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(1,2)
    Party.MoveToMap(TownMap.List["UnderCavala_2"])

def Cavala_18_MapTrigger_38_9(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(30,2)
    Party.MoveToMap(TownMap.List["UnderCavala_2"])

def Cavala_19_MapTrigger_35_21(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(30,12)
    Party.MoveToMap(TownMap.List["UnderCavala_2"])

def Cavala_20_MapTrigger_40_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(30,23)
    Party.MoveToMap(TownMap.List["UnderCavala_2"])

def Cavala_21_OnEntry(p):
    if StuffDone["0_3"] == 250:
        return
    StuffDone["0_3"] = 250
    ChoiceBox("You finally arrive at the remote village of Cavala. Cavala is a very young town, based on the harvest of Sourgrass. Sourgrass is a rare, wiry plant, which can be boiled down to make Hrras juice, a nasty, bitter fluid known for its healing properties.\n\nCavala grew quickly, at first. Then the bandits came. Overnight, a peaceful, properous town became a beseiged colony, on the brink of collapse. To the southwest, you see that they\'re starting to build a wall, meagre protection from the bandits outside.\n\nYour arrival creates quite a stir among the town\'s sparse population. Once they see that you aren\'t bandits, hope appears on their startled faces. Help has finally arrived ...", eDialogPic.TERRAIN, 189, ["OK"])

def Cavala_22_TalkingTrigger15(p):
    if StuffDone["100_0"] >= 1:
        p.TalkingText = "\"No more need! The bandit problem has been solved! Many thanks. When you leave the valley, I\'m sure you will be given a great reward.\""
        return
    if StuffDone["0_4"] >= 1:
        p.TalkingText = "Leonardo struggle to keep his fury from overwhelming him. \"Cameron! It was Cameron all along! Be sure to search his home well. You may yet find the secrets to the bandit\'s location.\"\n\n\"Then find him, and punish him! Make him drown in his own blood, for all I care!\""
        return
    if Party.CountItemClass(45, False) > 0:
        p.TalkingText = "On a hunch, you show Leonardo the runed plate you found in Cameron\'s basement. He looks at it carefully. \"That looks familiar. Can\'t quite place it, though.\" He snaps his fingers. \"Wait! That\'s Ilona\'s!\"\n\n\"Take it to her, and ask about the runed plate. She can tell you about it!\""
        return

def Cavala_23_TalkingTrigger52(p):
    if StuffDone["0_4"] >= 1:
        p.TalkingText = "\"Thank you for returning my plate. Curse that Cameron!\""
        return
    if Party.CountItemClass(45, True) > 0:
        ChoiceBox("\"Did you own a plate with runes on it,\" you ask. \"Why, yes. It was a family heirloom. I sent it out with a caravan, but it was stolen in a bandit raid.\"\n\nYou hand her the plate you found. \"Is this the plate?\" When she sees it, she smiles, then looks confused, then looks angry.\n\n\"Where did you find this?\" You tell her. \"Cameron\'s basement? Why, that means ... that means ... Cameron must be involved in the thefts!\" She jumps up and runs out the door, shouting an alarm.", eDialogPic.CREATURE, 6, ["OK"])
        p.TalkingText = "After a few minutes, she returns. \"Even now, guards are swarming over Cameron\'s home.\" She grins wickedly. \"Soon, we\'ll be able to question him and find out how he found my plate.\"\n\n\"Oh, and thanks for returning it to me.\""
        StuffDone["0_4"] = 1
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Cameron_188": Town.NPCList.Remove(npc)
        return
