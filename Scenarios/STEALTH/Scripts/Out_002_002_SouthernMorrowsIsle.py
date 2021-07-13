
def SouthernMorrowsIsle_479_MapTrigger_2_25(p):
    result = ChoiceBox("Although much of Morrow\'s Isle seems to be run feudally, these farmers, at least, own their own farms. They\'re arranged in a neat, tight clusters, and surrounded by a small number of moderately armed guards.\n\nNeither the guards nor the farmers seem pleased to see you.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("When you get close to the walls, halberds start appearing along the walls, some held by guards, some by edgy farmers. They don\'t even bother to say anything to you. They watch grimly and wait until you go away.")
        return

def SouthernMorrowsIsle_480_MapTrigger_5_35(p):
    result = ChoiceBox("Although much of Morrow\'s Isle seems to be run feudally, these farmers, at least, own their own farms. They\'re arranged in neat, tight clusters and surrounded by a small number of moderately armed guards.\n\nWhen you get close, several of the farmers come to the walls, and watch you nervously. At least they aren\'t attacking.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        if StuffDone["210_0"] >= 1:
            MessageBox("The farmers here recognize you, and wave. They don\'t want to talk, however, and don\'t bring you pie. Oh well.")
            return
        ChoiceBox("You walk up slowly and carefully, weapons sheathed and hands out. After a few minutes of whispered discussion, one of the farmers comes out to see you. He has a sword in one hand and a pie in the other.\n\nWhen you don\'t attack, he puts the sword away, and you can settle down to talk and eat. He introduces himself. \"I\'m Charmo, head of this homestead.\"\n\n\"My apologies for the cold welcome. In these days of the rebels, the hospitality of these parts has suffered of late. Can\'t blame us, though, considering what happened in Fahl.\"\n\nYou ask about it. \"It was just a peaceful logging village, up in the forests to the north. Those damned rebels, those Hill Runners, they leveled the place. Killed everyone. Burned the place to the ground. No survivors.\"\n\n\"Anyone who could do something like that isn\'t human. Nobody here wants to be the next. That\'s for sure.\" He stands. \"Well, sorry to be so short, but we have crops that need tending.\"\n\nYou thank him for the snack, and depart.", eDialogPic.CREATURE, 2, ["OK"])
        StuffDone["210_0"] = 1
        return

def SouthernMorrowsIsle_481_MapTrigger_40_30(p):
    result = ChoiceBox("The clusters of farmhouses in these parts are newer than elsewhere, only built a few years before. Farmers work hard among their neat rows. When you get close, however, all work stops, and people watch your approach nervously.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("When you get close, the farmers struggle to decide between giving in to their natural hospitality and succumbing to caution and common sense. Caution wins.\n\nBefore you get close, they shout out that perhaps it would increase the happiness of all concerned if you just turned back. Since there\'s not much else for you to do here, you leave.")
        return

def SouthernMorrowsIsle_483_MapTrigger_39_20(p):
    result = ChoiceBox("The clusters of farmhouses in these parts are newer than elsewhere, only built a few years before. Farmers work hard among their neat rows. When you get close, however, all work stops, and people watch your approach nervously.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        if StuffDone["210_1"] >= 1:
            if StuffDone["206_0"] >= 1:
                if StuffDone["210_3"] >= 1:
                    MessageBox("When they recognize you as their helpers, one of them comes out, greets you, and gives you a pie. It\'s tasty.")
                    Party.Food += 3
                    return
                if StuffDone["210_3"] == 250:
                    return
                StuffDone["210_3"] = 250
                ChoiceBox("You return to the farms, bringing news of your victory against the giants. Their worries about you gone, they invite you in for a traditional, hearty welcome dinner, complete with folk songs and homemade pies.\n\nAt the end of the meal, after all the speeches of gratitude, Bella brings you a reward: a beautiful silver ring. \"This heirloom has been in my family for many years.\"\n\n\"It hurts to give it away, but that pain is nothing compared to that I felt when the giants burnt down my farm. Thank you for your help, and good luck to you in your adventures.\"\n\nAfter they weigh you down with leftovers, you depart. They wave to you until you\'re out of sight.", eDialogPic.CREATURE, 8, ["OK"])
                Party.GiveNewItem("SilverRingofSkill_303")
                Party.Food += 50
                return
            MessageBox("Bella comes out and speaks with you. When she finds out you haven\'t killed the giants, the conversation comes to an abrupt end.")
            return
        ChoiceBox("When the farmers see that you\'re adventurers, they launch into a spirited debate. You hear the arguments going on for several minutes. Finally, one of them, a middle aged woman, walks briskly out to greet you.\n\n\"I\'m Bella,\" she says quickly. \"The others don\'t approve of this, but hell with them. This is important. They\'re worried about rebels, but we have a worse problem. Our farms have been raided by hill giants lately.\"\n\n\"That\'s right. Hill giants. They aren\'t all dead. There\'s a band of them in the forest to the north, and we can pay well anyone who wipes them out. They live at the south end of the woods, at a path with two boulders by it.\"\n\n\"Kill them and return, and we\'ll pay you. Now I have to return. Sorry I can\'t offer some pie. Bye.\" She walks back the way she came.", eDialogPic.CREATURE, 8, ["OK"])
        StuffDone["210_1"] = 1
        return

def SouthernMorrowsIsle_484_MapTrigger_42_6(p):
    if StuffDone["210_1"] >= 1:
        MessageBox("You reach the end of the path Bella described to you, and, indeed, you find a place which was, up until recently, settled by giants. The flattened earth and toppled trees are evidence enough of that.\n\nHowever, the tribe has packed up and moved on to somewhere else. The massive tracks lead off to the north.")
        return

def SouthernMorrowsIsle_485_MapTrigger_20_18(p):
    if StuffDone["210_4"] == 250:
        return
    result = ChoiceBox("At the end of the path, you find a patch of holly. It\'s a powerful (and fast growing) alchemical ingredient.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["210_4"] = 250
        WorldMap.DeactivateTrigger(Location(116,114))
        WorldMap.DeactivateTrigger(Location(130,122))
        WorldMap.DeactivateTrigger(Location(131,123))
        Party.GiveNewItem("Holly_363")
    return

def SouthernMorrowsIsle_486_MapTrigger_34_26(p):
    StuffDone["210_4"] = 0

def SouthernMorrowsIsle_488_MapTrigger_30_4(p):
    if StuffDone["210_5"] == 250:
        return
    result = ChoiceBox("Someone boating down this river had an unfortunate accident. You find his body by his gutted boat. His neck was broken. His clothes were torn, but his axe is still intact.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["210_5"] = 250
        WorldMap.AlterTerrain(Location(126,100), 1, None)
        WorldMap.DeactivateTrigger(Location(126,100))
        Party.GiveNewItem("MagicAxe_80")
    return
