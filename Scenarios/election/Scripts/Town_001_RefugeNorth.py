
def RefugeNorth_73_MapTrigger_34_32(p):
    if StuffDone["2_1"] >= 1:
        if StuffDone["2_8"] >= 1:
            if StuffDone["3_2"] < 1:
                result = ChoiceBox("As you open the door, a cunning idea occurs to you.\n\nYou explain to Tarle and Lerta about the Cody\'s and their distasteful activities. They seem suitably disgusted.\n\n\"And I,\" you continue. \"Would like to make the redistribution of that food part of my election campaign.\"\n\nThey nod in hesitant agreement. \"Do you think that would be popular?\" Lerta asks. \"Many people might not appreciate the precedent it would set - it is effectively theft, after all.\"\n\n\"Yes,\" points out Tarle. \"But everyone, except the Cody\'s, would benefit. I think you should do it.\"\n\n\"Hmmm, well, it\'s up to you,\" Lerta concedes. Well, it certainly is. Make it an election promise?", eDialogPic.CREATURE, 7, ["Yes", "No"])
                if result == 0:
                    MessageBox("Tarle appears pleased. \"OK then. Just leave it to us - we\'ll make sure everyone knows of your plans. I\'m convinced it\'s a winner!\" He beams.")
                    StuffDone["3_2"] = 1
                    return
                elif result == 1:
                    MessageBox("\"No,\" You side with Lerta on this one. \"I suppose it\'s not that great an idea.\n\nTarle looks disappointed. \"Well, if you reconsider, just come back here.\"")
                    return
                return
            return
        return
    if StuffDone["2_0"] == 250:
        return
    StuffDone["2_0"] = 250
    MessageBox("This is the first time you\'ve bothered to look in here, previously assuming from its outward appearance that this building was just another neglected relic of a bygone era. But looking inside you can see that the place is actually in reasonable condition\n\nYou also see that it is no longer deserted. A man and a woman, both Exiles judging from their skin, have taken up residence. The place still looks pretty empty, though - the only furniture being two chairs and two wooden boards, being used as beds.")
    MessageBox("As you open the door the two get up from the chairs on which they were sitting. They are fearful at first, but when they see you their faces relax in recognition. \"You must be Vandell\" Says the man.\n\nResponding to your confused smile, he explains \"We heard there was another Exile in the town. I am Tarle, and this is my wife, Lerta. Come, we have much to discuss.")

def RefugeNorth_74_MapTrigger_24_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,5)
    Party.MoveToMap(TownMap.List["RefugeSouth_0"])

def RefugeNorth_75_MapTrigger_24_6(p):
    result = ChoiceBox("\"It\'s an Exile!\" You hear someone shout as you approach the portcullis. \"An Exile?\" You hear, amongst excited murmurs. You realise these voices are actually coming from outside. Tens of people are gathering around the outer portcullis, looking in at you.\n\n\"You\'ve got to help us, brother.\" Almost all of them are Exiles, you realise, with a few Sliths and dark-skinned humans as well. \"So they still allow \'Worms\' in there?\" The first Exile questions, surprised. You explain they do, but maybe not for long.\n\n\"Can you get us some food? We\'re starving out here.\" This is certainly no exaggeration. The sight of so many bare ribs, potbellies, haggard faces make you sick.\n\nBut nonetheless you have to explain that you have barely enough food for yourself, that the rationing inside is very strict. \"So they have got food?\" One asks, excitedly. \"Not much\" You respond.\n\nMany of them are by now starting to give up on you, too tired to keep standing. The cries of multitudes of starving children is high in the air. But a few of the young men are persistent, especially the one who first saw you.\n\nHe now asks hopefully, \"Could you let us in, Brother? Come on, your people need you! Please? We\'ll die, many already have. My mother... Please?\" You could easily open the portculli, the lever is just next to you. Do you?", eDialogPic.TERRAIN, 92, ["Open", "Leave"])
    if result == 0:
        MessageBox("Excising all thought that might prevent you, you pull the lever. The triumphant roar from outside is immense, despite the state of the roarers. \"Thank you, Brother.\" The first man says, clapping you on the back on his way into the city.\n\nWithin an hour the place has been ransacked. The meagre food reserves broken into and shared between hundreds, many killed by those driven mad by hunger and revenge. Soon it is realised that the town is useless, and most leave. You join the Exiles.")
        Scenario.End()
        return
    elif result == 1:
        MessageBox("You shake your head apologetically, and then just turn and leave. Those outside continue to plead with you for some time, then the beggings turn to threats and violent abuse. You just keep on going.")
        return

def RefugeNorth_76_MapTrigger_8_26(p):
    if StuffDone["2_5"] == 250:
        return
    StuffDone["2_5"] = 250
    TownMap.List["RefugeNorth_1"].DeactivateTrigger(Location(8,26))
    MessageBox("This room would appear to serve as a dining room and a living room. The lady of the house is here. She gets up from her seat as you enter, surprised to see a stranger in the house. \"Were you invited here?\" She asks disapprovingly.\n\nShe clears some used plates and cutlery from the table as she speaks. Odd that - you thought the only food left was indiscriminate vegetable matter, nothing warranting cutlery. But then these sorts probably wouldn\'t KNOW how to eat with their fingers.")

def RefugeNorth_77_MapTrigger_7_13(p):
    if StuffDone["2_6"] == 250:
        return
    StuffDone["2_6"] = 250
    TownMap.List["RefugeNorth_1"].DeactivateTrigger(Location(7,13))
    MessageBox("Now this is an unusual room. For a start, the whole design, floor, furniture, walls, even ceiling, looks unfamiliar, alien almost. And yet you sort of recognise it ... Of course! This is Vahnatai design - you saw it at the town they had in Upper Exile.\n\nBut even weirder than that is the contents of the room. Row upon row of strange glass bottles, many filled with exotic coloured liquids. Odder still is the counter along one wall - it\'s distinctly slanted! One end is actually higher than the other.")

def RefugeNorth_78_MapTrigger_9_10(p):
    if StuffDone["6_2"] >= 1:
        MessageBox("That thing destroyed Cody, and you presume it could easily do the same to you. No. You aren\'t going to go obliterating yourself for no reason.")
        p.CancelAction = True
        return
    if StuffDone["6_2"] < 1:
        MessageBox("\"Watch out!\" Cody calls just as you are about to stand on this central sigil. \"That thing it could ... if you stood there it might ... so don\'t!\" He explains, not completely coherently.")
        p.CancelAction = True
        return

def RefugeNorth_79_MapTrigger_7_28(p):
    if StuffDone["2_7"] == 250:
        return
    StuffDone["2_7"] = 250
    TownMap.List["RefugeNorth_1"].DeactivateTrigger(Location(7,28))
    TownMap.List["RefugeNorthnight_3"].DeactivateTrigger(Location(7,28))
    MessageBox("Massive. You can think of absolutely no other word to describe this place, with its gleaming white face towering above, and with a door so imposing and ornate you actually feel yourself cowering there before it.\n\nRighting yourself, you enter.")

def RefugeNorth_80_MapTrigger_5_18(p):
    if StuffDone["2_9"] >= 1:
        MessageBox("You\'ve already taken your fill from this box of goodies, and you feel if you open the chest again you might just stick your head in it and drown in food, glorious food. So you don\'t.")
        return
    if StuffDone["2_9"] < 1:
        StuffDone["2_8"] = 1
        result = ChoiceBox("You open the huge chest, here in this hidden extension to the house. Oddly, it\'s unlocked - probably no-one expected it to be found.\n\nYou open it, slowly so as not to allow it to creak, and find treasure beyond your wildest dreams within.\n\nFood! Glorious, edible food! Salted meets! Fruit conserves! All sorts of tasty, durable nutrition.\n\nThey must have been hoarding this here, and eating this stuff while the rest of us have to eat the paltry rations. And not telling anyone! It makes you sick, it makes you mad.\n\nAnd it makes you hungry. But before you think about that, you decide that the authorities MUST be told about this. It shouldn\'t be allowed, and you sincerely hope it\'s not.\n\nNow back to your stomach. You are sorely tempted to take some of this. They\'ve got far more than enough, after all, and they\'d probably never know. Just enough to get you through the next few days without rations.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
        if result == 0:
            MessageBox("You stuff your pockets, taking food from nearer the bottom of the chest so your thievery won\'t be too noticeable.\n\nYou think you hear footsteps from somewhere in the house - you\'d better get out before you\'re noticed.")
            Party.Food += 5
            StuffDone["2_9"] = 1
            return
        elif result == 1:
            MessageBox("It takes a great strength of will to close the  lid on temptation, but you manage. You can\'t really go around stealing - that\'s just as bit as what they\'re doing.")
            return
        return

def RefugeNorth_81_MapTrigger_14_32(p):
    if StuffDone["2_8"] >= 1:
        if StuffDone["3_0"] >= 1:
            if StuffDone["6_2"] >= 1:
                if StuffDone["3_6"] >= 1:
                    if StuffDone["12_1"] >= 1:
                        return
                    if StuffDone["4_1"] >= 2:
                        if StuffDone["12_0"] >= 1:
                            if StuffDone["3_9"] >= 1:
                                MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if SpecialItem.PartyHas("Blackmailnote"):
                                if StuffDone["12_2"] == 250:
                                    return
                                StuffDone["12_2"] = 250
                                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["12_0"] < 1:
                            MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                            StuffDone["12_0"] = 1
                            if StuffDone["3_8"] >= 1:
                                MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if StuffDone["3_8"] < 1:
                                MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    if StuffDone["12_2"] == 250:
                                        return
                                    StuffDone["12_2"] = 250
                                    MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                    if StuffDone["2_4"] >= 2:
                                        if StuffDone["12_3"] == 250:
                                            return
                                        StuffDone["12_3"] = 250
                                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                        return
                                    return
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            return
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["3_6"] < 1:
                    MessageBox("He looks at you with hollow eyes as you enter. You ask him what is wrong. \"Haven\'t you heard?\" He says sadly. \"Cody\'s dead. Or left, which means he\'s probably dead by now. This morning he just - he just wasn\'t there.\n\n \"We don\'t know what happened, but,\" he breaks down and cries. \"Oh, it\'s terrible, Vandell. He was such a sweet old man. Why? Why?\" You ask him, innocuously enough, if he\'s treating it as a murder. He shakes his head.")
                    StuffDone["3_6"] = 1
                    if StuffDone["12_1"] >= 1:
                        return
                    if StuffDone["4_1"] >= 2:
                        if StuffDone["12_0"] >= 1:
                            if StuffDone["3_9"] >= 1:
                                MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if SpecialItem.PartyHas("Blackmailnote"):
                                if StuffDone["12_2"] == 250:
                                    return
                                StuffDone["12_2"] = 250
                                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["12_0"] < 1:
                            MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                            StuffDone["12_0"] = 1
                            if StuffDone["3_8"] >= 1:
                                MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if StuffDone["3_8"] < 1:
                                MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    if StuffDone["12_2"] == 250:
                                        return
                                    StuffDone["12_2"] = 250
                                    MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                    if StuffDone["2_4"] >= 2:
                                        if StuffDone["12_3"] == 250:
                                            return
                                        StuffDone["12_3"] = 250
                                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                        return
                                    return
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            return
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                return
            if StuffDone["12_1"] >= 1:
                return
            if StuffDone["4_1"] >= 2:
                if StuffDone["12_0"] >= 1:
                    if StuffDone["3_9"] >= 1:
                        MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["12_0"] < 1:
                    MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                    StuffDone["12_0"] = 1
                    if StuffDone["3_8"] >= 1:
                        MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if StuffDone["3_8"] < 1:
                        MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            if StuffDone["12_2"] == 250:
                                return
                            StuffDone["12_2"] = 250
                            MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    return
                return
            if SpecialItem.PartyHas("Blackmailnote"):
                if StuffDone["12_2"] == 250:
                    return
                StuffDone["12_2"] = 250
                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                if StuffDone["2_4"] >= 2:
                    if StuffDone["12_3"] == 250:
                        return
                    StuffDone["12_3"] = 250
                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                    return
                return
            if StuffDone["2_4"] >= 2:
                if StuffDone["12_3"] == 250:
                    return
                StuffDone["12_3"] = 250
                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                return
            return
        if StuffDone["3_0"] < 1:
            MessageBox("You storm into the chamber of the guards and tell Marvin about the Cody family\'s despicable behaviour, expecting him to march over there at once and arrest the lot of them.\n\nInstead, he just says, \"Well, I agree it\'s not very nice of them to keep it to themselves when so many go hungry, but I don\'t think there\'s an actual law against it. Sorry. But you should talk to the Mayor - he\'s the one with the power in emergencies.\"")
            StuffDone["3_0"] = 1
            if StuffDone["6_2"] >= 1:
                if StuffDone["3_6"] >= 1:
                    if StuffDone["12_1"] >= 1:
                        return
                    if StuffDone["4_1"] >= 2:
                        if StuffDone["12_0"] >= 1:
                            if StuffDone["3_9"] >= 1:
                                MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if SpecialItem.PartyHas("Blackmailnote"):
                                if StuffDone["12_2"] == 250:
                                    return
                                StuffDone["12_2"] = 250
                                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["12_0"] < 1:
                            MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                            StuffDone["12_0"] = 1
                            if StuffDone["3_8"] >= 1:
                                MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if StuffDone["3_8"] < 1:
                                MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    if StuffDone["12_2"] == 250:
                                        return
                                    StuffDone["12_2"] = 250
                                    MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                    if StuffDone["2_4"] >= 2:
                                        if StuffDone["12_3"] == 250:
                                            return
                                        StuffDone["12_3"] = 250
                                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                        return
                                    return
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            return
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["3_6"] < 1:
                    MessageBox("He looks at you with hollow eyes as you enter. You ask him what is wrong. \"Haven\'t you heard?\" He says sadly. \"Cody\'s dead. Or left, which means he\'s probably dead by now. This morning he just - he just wasn\'t there.\n\n \"We don\'t know what happened, but,\" he breaks down and cries. \"Oh, it\'s terrible, Vandell. He was such a sweet old man. Why? Why?\" You ask him, innocuously enough, if he\'s treating it as a murder. He shakes his head.")
                    StuffDone["3_6"] = 1
                    if StuffDone["12_1"] >= 1:
                        return
                    if StuffDone["4_1"] >= 2:
                        if StuffDone["12_0"] >= 1:
                            if StuffDone["3_9"] >= 1:
                                MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if SpecialItem.PartyHas("Blackmailnote"):
                                if StuffDone["12_2"] == 250:
                                    return
                                StuffDone["12_2"] = 250
                                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["12_0"] < 1:
                            MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                            StuffDone["12_0"] = 1
                            if StuffDone["3_8"] >= 1:
                                MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                                    SpecialItem.Give("HealingSceptre")
                                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                    StuffDone["12_1"] = 1
                                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                    StuffDone["100_1"] -= 1
                                    if StuffDone["100_1"] == 250:
                                        pass
                                    for n in range(Town.NPCList.Count-1, -1, -1):
                                        npc = Town.NPCList[n]
                                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                    return
                                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                                StuffDone["12_1"] = 1
                                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                                StuffDone["100_1"] -= 1
                                if StuffDone["100_1"] == 250:
                                    pass
                                for n in range(Town.NPCList.Count-1, -1, -1):
                                    npc = Town.NPCList[n]
                                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                                return
                            if StuffDone["3_8"] < 1:
                                MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                                if SpecialItem.PartyHas("Blackmailnote"):
                                    if StuffDone["12_2"] == 250:
                                        return
                                    StuffDone["12_2"] = 250
                                    MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                                    if StuffDone["2_4"] >= 2:
                                        if StuffDone["12_3"] == 250:
                                            return
                                        StuffDone["12_3"] = 250
                                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                        return
                                    return
                                if StuffDone["2_4"] >= 2:
                                    if StuffDone["12_3"] == 250:
                                        return
                                    StuffDone["12_3"] = 250
                                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                    return
                                return
                            return
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                return
            if StuffDone["12_1"] >= 1:
                return
            if StuffDone["4_1"] >= 2:
                if StuffDone["12_0"] >= 1:
                    if StuffDone["3_9"] >= 1:
                        MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["12_0"] < 1:
                    MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                    StuffDone["12_0"] = 1
                    if StuffDone["3_8"] >= 1:
                        MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if StuffDone["3_8"] < 1:
                        MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            if StuffDone["12_2"] == 250:
                                return
                            StuffDone["12_2"] = 250
                            MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    return
                return
            if SpecialItem.PartyHas("Blackmailnote"):
                if StuffDone["12_2"] == 250:
                    return
                StuffDone["12_2"] = 250
                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                if StuffDone["2_4"] >= 2:
                    if StuffDone["12_3"] == 250:
                        return
                    StuffDone["12_3"] = 250
                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                    return
                return
            if StuffDone["2_4"] >= 2:
                if StuffDone["12_3"] == 250:
                    return
                StuffDone["12_3"] = 250
                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                return
            return
        return
    if StuffDone["6_2"] >= 1:
        if StuffDone["3_6"] >= 1:
            if StuffDone["12_1"] >= 1:
                return
            if StuffDone["4_1"] >= 2:
                if StuffDone["12_0"] >= 1:
                    if StuffDone["3_9"] >= 1:
                        MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["12_0"] < 1:
                    MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                    StuffDone["12_0"] = 1
                    if StuffDone["3_8"] >= 1:
                        MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if StuffDone["3_8"] < 1:
                        MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            if StuffDone["12_2"] == 250:
                                return
                            StuffDone["12_2"] = 250
                            MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    return
                return
            if SpecialItem.PartyHas("Blackmailnote"):
                if StuffDone["12_2"] == 250:
                    return
                StuffDone["12_2"] = 250
                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                if StuffDone["2_4"] >= 2:
                    if StuffDone["12_3"] == 250:
                        return
                    StuffDone["12_3"] = 250
                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                    return
                return
            if StuffDone["2_4"] >= 2:
                if StuffDone["12_3"] == 250:
                    return
                StuffDone["12_3"] = 250
                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                return
            return
        if StuffDone["3_6"] < 1:
            MessageBox("He looks at you with hollow eyes as you enter. You ask him what is wrong. \"Haven\'t you heard?\" He says sadly. \"Cody\'s dead. Or left, which means he\'s probably dead by now. This morning he just - he just wasn\'t there.\n\n \"We don\'t know what happened, but,\" he breaks down and cries. \"Oh, it\'s terrible, Vandell. He was such a sweet old man. Why? Why?\" You ask him, innocuously enough, if he\'s treating it as a murder. He shakes his head.")
            StuffDone["3_6"] = 1
            if StuffDone["12_1"] >= 1:
                return
            if StuffDone["4_1"] >= 2:
                if StuffDone["12_0"] >= 1:
                    if StuffDone["3_9"] >= 1:
                        MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if SpecialItem.PartyHas("Blackmailnote"):
                        if StuffDone["12_2"] == 250:
                            return
                        StuffDone["12_2"] = 250
                        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["12_0"] < 1:
                    MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
                    StuffDone["12_0"] = 1
                    if StuffDone["3_8"] >= 1:
                        MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                        MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                            SpecialItem.Give("HealingSceptre")
                            MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                            StuffDone["12_1"] = 1
                            MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                            StuffDone["100_1"] -= 1
                            if StuffDone["100_1"] == 250:
                                pass
                            for n in range(Town.NPCList.Count-1, -1, -1):
                                npc = Town.NPCList[n]
                                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                            return
                        MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                        StuffDone["12_1"] = 1
                        MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                        StuffDone["100_1"] -= 1
                        if StuffDone["100_1"] == 250:
                            pass
                        for n in range(Town.NPCList.Count-1, -1, -1):
                            npc = Town.NPCList[n]
                            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                        return
                    if StuffDone["3_8"] < 1:
                        MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                        if SpecialItem.PartyHas("Blackmailnote"):
                            if StuffDone["12_2"] == 250:
                                return
                            StuffDone["12_2"] = 250
                            MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                            if StuffDone["2_4"] >= 2:
                                if StuffDone["12_3"] == 250:
                                    return
                                StuffDone["12_3"] = 250
                                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                                return
                            return
                        if StuffDone["2_4"] >= 2:
                            if StuffDone["12_3"] == 250:
                                return
                            StuffDone["12_3"] = 250
                            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                            return
                        return
                    return
                return
            if SpecialItem.PartyHas("Blackmailnote"):
                if StuffDone["12_2"] == 250:
                    return
                StuffDone["12_2"] = 250
                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                if StuffDone["2_4"] >= 2:
                    if StuffDone["12_3"] == 250:
                        return
                    StuffDone["12_3"] = 250
                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                    return
                return
            if StuffDone["2_4"] >= 2:
                if StuffDone["12_3"] == 250:
                    return
                StuffDone["12_3"] = 250
                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                return
            return
        return
    if StuffDone["12_1"] >= 1:
        return
    if StuffDone["4_1"] >= 2:
        if StuffDone["12_0"] >= 1:
            if StuffDone["3_9"] >= 1:
                MessageBox("Just as you leave, planning to walk around a bit while Marvin mulls your evidence over, he stops you with a call.\n\n\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                if SpecialItem.PartyHas("Blackmailnote"):
                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                    SpecialItem.Give("HealingSceptre")
                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                    StuffDone["12_1"] = 1
                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                    StuffDone["100_1"] -= 1
                    if StuffDone["100_1"] == 250:
                        pass
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                    return
                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                StuffDone["12_1"] = 1
                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                StuffDone["100_1"] -= 1
                if StuffDone["100_1"] == 250:
                    pass
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                return
            if SpecialItem.PartyHas("Blackmailnote"):
                if StuffDone["12_2"] == 250:
                    return
                StuffDone["12_2"] = 250
                MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                if StuffDone["2_4"] >= 2:
                    if StuffDone["12_3"] == 250:
                        return
                    StuffDone["12_3"] = 250
                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                    return
                return
            if StuffDone["2_4"] >= 2:
                if StuffDone["12_3"] == 250:
                    return
                StuffDone["12_3"] = 250
                MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                return
            return
        if StuffDone["12_0"] < 1:
            MessageBox("You tell Marvin about the attack on your person by the two out-of-towners. He looks worried. \"Have you any idea who, if anyone other than your attackers, was behind this?\"\n\nYou explain that you haven\'t. Except - except you do remember seeing Jonathan talking to the two men the evening before!")
            StuffDone["12_0"] = 1
            if StuffDone["3_8"] >= 1:
                MessageBox("\"OK! Yes. That\'s enough. In my opinion, Jonathan has been trying to kill you. And my opinion is what matters.\" So saying, he marches out of the room, leaving you standing there in the doorway.")
                MessageBox("A few minutes later, just as you are about to collapse, Marvin returns. With Jonathan. His face is freshly bruised, his hands held behind his back by Marvin. He catches sight of you, and you see the hate well up.\n\n\"We\'ve got a full confession out of this one, haven\'t we, eh, Jonathan?\" He says, pinning the struggling little man against the wall. He drags him to the desk and forces him to sign various papers, hitting him hard when he refuses.")
                if SpecialItem.PartyHas("Blackmailnote"):
                    MessageBox("\"Oh, by the way,\" says Marvin whilst mercilessly beating Jonathan, \"I found this, hidden on him.\" He hands you your staff! You stare at it in amazement - you had given up all hope of ever getting it back.")
                    SpecialItem.Give("HealingSceptre")
                    MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                    StuffDone["12_1"] = 1
                    MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                    StuffDone["100_1"] -= 1
                    if StuffDone["100_1"] == 250:
                        pass
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                    return
                MessageBox("This is certainly a side of Marvin that\'s new to you. \"So you did try to kill me?\" You ask Jonathan, thinking you probably ought to check. \"Yes I tried to kill you,\" he replies, venomously. \"And I only wish I\'d managed too, you Exile bastard!\"\n\nIt\'s more than you can handle, seeing this pathetic little creature curse you so vehemently. You can only ask, \"Why?\" \"Don\'t ask,\" Marvin replies. \"The reasons are always terrible. Excuse me.\" He  leaves, dragging Jonathan, cursing and spitting, behind.")
                StuffDone["12_1"] = 1
                MessageBox("A few minutes later he returns, alone. \"What did you do with him?\" You ask, fearing the worst. \"I exiled him.\" He replies, stony-faced.\n\n \"I took him outside the gates, and I told all the refugees out there : \'This man tried to kill an Exile because he was an Exile.\' They did the rest. Now excuse me, I have work to do.")
                StuffDone["100_1"] -= 1
                if StuffDone["100_1"] == 250:
                    pass
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                return
            if StuffDone["3_8"] < 1:
                MessageBox("\"Sorry,\" he says. \"That is purely circumstantial evidence. You\'ll need much more before I can go around arresting people.\"")
                if SpecialItem.PartyHas("Blackmailnote"):
                    if StuffDone["12_2"] == 250:
                        return
                    StuffDone["12_2"] = 250
                    MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
                    if StuffDone["2_4"] >= 2:
                        if StuffDone["12_3"] == 250:
                            return
                        StuffDone["12_3"] = 250
                        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                        return
                    return
                if StuffDone["2_4"] >= 2:
                    if StuffDone["12_3"] == 250:
                        return
                    StuffDone["12_3"] = 250
                    MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
                    return
                return
            return
        return
    if SpecialItem.PartyHas("Blackmailnote"):
        if StuffDone["12_2"] == 250:
            return
        StuffDone["12_2"] = 250
        MessageBox("You tell Marvin about the theft of your staff, showing him the note. \"Well I\'m sorry, but unless you have some idea who took it then I can\'t help. But don\'t give in, we\'ll find it eventually.\"\n\nYou explain that eventually\'s not good enough, you explain it\'s real value to you. \"I see,\" he responds gravely, \"but still there is nothing I can do for you. But try the temple - I understand that Cardus can heal most ills. And free of charge.\"")
        if StuffDone["2_4"] >= 2:
            if StuffDone["12_3"] == 250:
                return
            StuffDone["12_3"] = 250
            MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
            return
        return
    if StuffDone["2_4"] >= 2:
        if StuffDone["12_3"] == 250:
            return
        StuffDone["12_3"] = 250
        MessageBox("\"Someone\'s been messing with the ration list - Jack seems to think I\'ve already had mine today, but I haven\'t!\" You tell Marvin, the words racing from your mouth, propelled by hunger. He just looks at you with contempt.\n\n\"Nice try. But we can\'t afford to give anyone extra food. So if you\'ll excuse me, I have work to do.\" You protest, but he is unwilling to accept your complaint.")
        return

def RefugeNorth_82_MapTrigger_24_40(p):
    if StuffDone["3_5"] >= 1:
        Town.AlterTerrain(Location(25,14), 0, TerrainRecord.UnderlayList[254])
        Town.AlterTerrain(Location(24,14), 0, TerrainRecord.UnderlayList[253])
        if StuffDone["6_2"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
            Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
            if StuffDone["12_1"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                return
            if StuffDone["12_1"] < 1:
                return
            return
        if StuffDone["12_1"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
            return
        if StuffDone["12_1"] < 1:
            return
        return
    if StuffDone["6_2"] >= 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
        Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
        if StuffDone["12_1"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
            return
        if StuffDone["12_1"] < 1:
            return
        return
    if StuffDone["12_1"] >= 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
        return
    if StuffDone["12_1"] < 1:
        return

def RefugeNorth_85_MapTrigger_39_42(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if p.Origin == eCallOrigin.SEARCHING: return
    RunScript("GlobalCall_RefugeNorth_249", ScriptParameters(eCallOrigin.CUSTOM))
    if StuffDone["50_3"] >= 1:
        return
    if StuffDone["50_3"] < 1:
        MessageBox("He thinks for a bit longer. \"OK, then. I\'ll vote for you. I mean, I was only going to vote for Nash in the first place because he seemed to have some sort a solution to our problems, however distasteful that solution was.\n\n\"But your idea is much better. You say their stash is quite large - I don\'t know if there will be enough to feed ALL of us for the whole year, but we\'ve got to try.\"")
        StuffDone["50_3"] = 1
        RunScript("GlobalCall_RefugeNorth_248", ScriptParameters(eCallOrigin.CUSTOM))
        StuffDone["2_8"] = 1
        result = ChoiceBox("You open the huge chest, here in this hidden extension to the house. Oddly, it\'s unlocked - probably no-one expected it to be found.\n\nYou open it, slowly so as not to allow it to creak, and find treasure beyond your wildest dreams within.\n\nFood! Glorious, edible food! Salted meets! Fruit conserves! All sorts of tasty, durable nutrition.\n\nThey must have been hoarding this here, and eating this stuff while the rest of us have to eat the paltry rations. And not telling anyone! It makes you sick, it makes you mad.\n\nAnd it makes you hungry. But before you think about that, you decide that the authorities MUST be told about this. It shouldn\'t be allowed, and you sincerely hope it\'s not.\n\nNow back to your stomach. You are sorely tempted to take some of this. They\'ve got far more than enough, after all, and they\'d probably never know. Just enough to get you through the next few days without rations.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
        if result == 0:
            MessageBox("You stuff your pockets, taking food from nearer the bottom of the chest so your thievery won\'t be too noticeable.\n\nYou think you hear footsteps from somewhere in the house - you\'d better get out before you\'re noticed.")
            Party.Food += 5
            StuffDone["2_9"] = 1
            return
        elif result == 1:
            MessageBox("It takes a great strength of will to close the  lid on temptation, but you manage. You can\'t really go around stealing - that\'s just as bit as what they\'re doing.")
            return
        return

def RefugeNorth_86_MapTrigger_38_18(p):
    if StuffDone["12_1"] >= 1:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("\"What do you think you\'re doing, Worm?\" Inquires Jonathan before you get a chance to nosy around in their personal quarters. \"Nothing,\" you respond innocently, backing away from the door.")

def RefugeNorth_88_MapTrigger_22_40(p):
    RunScript("GlobalCall_RefugeNorth_250", ScriptParameters(eCallOrigin.CUSTOM))
    StuffDone["2_9"] = 1

def RefugeNorth_89_CreatureDeath0(p):
    RunScript("GlobalCall_RefugeSouth_247", ScriptParameters(eCallOrigin.CUSTOM))
    if StuffDone["2_4"] >= 2:
        MessageBox("\"Vandell?\" He looks down a list in front of him, finds your name on it, then looks at you sternly. \"You\'ve already had your rations for today.\" \"What? No I haven\'t! Do you remember me getting them?\" \"It\'s written right here. I don\'t make mistakes.\"\n\nYou HAVEN\'T had your ration today, you know it. You can FEEL it, the hunger welling up inside. What\'s going on?")
        return
    if StuffDone["2_4"] < 1:
        MessageBox("\"OK. Here you go,\" He says, business-like, handing you some indiscriminate foodstuffs. He writes your name down on the list in front of him.\n\n\"Not exactly \'haute cuisine\' I know, but it\'s all we\'ve got left.\"")
        Party.Food += 1
        StuffDone["2_4"] = 1
        return

def RefugeNorth_100_TalkingTrigger8(p):
    if StuffDone["2_4"] >= 2:
        p.TalkingText = "\"Vandell?\" He looks down a list in front of him, finds your name on it, then looks at you sternly. \"You\'ve already had your rations for today.\" \"What? No I haven\'t! Do you remember me getting them?\" \"It\'s written right here. I don\'t make mistakes.\"\n\nYou HAVEN\'T had your ration today, you know it. You can FEEL it, the hunger welling up inside. What\'s going on?"
        return
    if StuffDone["2_4"] < 1:
        p.TalkingText = "\"OK. Here you go,\" He says, business-like, handing you some indiscriminate foodstuffs. He writes your name down on the list in front of him.\n\n\"Not exactly \'haute cuisine\' I know, but it\'s all we\'ve got left.\""
        Party.Food += 1
        StuffDone["2_4"] = 1
        return

def RefugeNorth_101_TalkingTrigger9(p):
    if StuffDone["50_3"] >= 1:
        p.TalkingText = "\"I\'ve already agreed to vote for you, Vandell.\n\n\"What more can you want?\""
        return
    if StuffDone["3_2"] >= 1:
        p.TalkingText = "You tell him about the Cody\'s food hoarding. At last you get a decent reaction. He shakes his head in disgust, sneering. \"Well that\'s just typical.\"\n\nYou explain that the Mayor is going to do nothing about it and neither, to Jack\'s shock, is Nash. However, you point out, YOU do promise to redistribute the food, if elected. He thinks about this. \"Right.\""
        StuffDone["12_5"] = 1
        return

def RefugeNorth_102_TalkingTrigger13(p):
    if StuffDone["12_1"] >= 1:
        p.TalkingText = "He frowns. \"I thought we\'d solved that little problem. Jonathan\'s gone. You\'ve not had any problems since, have you?\" You respond in the negative.\n\n\"Well then.\""
        return

def RefugeNorth_103_TalkingTrigger15(p):
    if StuffDone["50_4"] >= 1:
        p.TalkingText = "\"I\'m going to vote for Mayor Vogel. And don\'t even think about trying to persuade me to vote for you - I won\'t be convinced.\n\n\"It\'s nothing personal, you understand, but I know Vogel and he knows the town.\""
        return
    if StuffDone["50_4"] < 1:
        if StuffDone["12_1"] >= 1:
            p.TalkingText = "He breaths in deeply. Eventually, he speaks. \"I know Jonathan didn\'t actually say so directly, but I don\'t doubt that these attempts were ordered by Nash.\n\n\"And even if not, his having such a friend definitely lowers my estimation of him. I will vote for Mayor Vogel. Sorry I can\'t vote for you - I just don\'t think you\'d be any good.\""
            StuffDone["50_4"] = 1
            RunScript("GlobalCall_RefugeNorth_250", ScriptParameters(eCallOrigin.CUSTOM))
            StuffDone["2_9"] = 1
            return
        return

def RefugeNorth_104_TalkingTrigger36(p):
    if StuffDone["2_8"] >= 1:
        p.TalkingText = "You tell him about the Cody\'s food hoarding. At last you get a decent reaction. He shakes his head in disgust, sneering. \"Well that\'s just typical.\""
        if StuffDone["3_2"] >= 1:
            p.TalkingText = "You tell him about the Cody\'s food hoarding. At last you get a decent reaction. He shakes his head in disgust, sneering. \"Well that\'s just typical.\"\n\nYou explain that the Mayor is going to do nothing about it and neither, to Jack\'s shock, is Nash. However, you point out, YOU do promise to redistribute the food, if elected. He thinks about this. \"Right.\""
            StuffDone["12_5"] = 1
            return
        return

def RefugeNorth_105_TalkingTrigger37(p):
    if StuffDone["50_3"] >= 1:
        return
    if StuffDone["50_3"] < 1:
        p.TalkingText = "He thinks for a bit longer. \"OK, then. I\'ll vote for you. I mean, I was only going to vote for Nash in the first place because he seemed to have some sort a solution to our problems, however distasteful that solution was.\n\n\"But your idea is much better. You say their stash is quite large - I don\'t know if there will be enough to feed ALL of us for the whole year, but we\'ve got to try.\""
        StuffDone["50_3"] = 1
        RunScript("GlobalCall_RefugeNorth_248", ScriptParameters(eCallOrigin.CUSTOM))
        StuffDone["2_8"] = 1
        result = ChoiceBox("You open the huge chest, here in this hidden extension to the house. Oddly, it\'s unlocked - probably no-one expected it to be found.\n\nYou open it, slowly so as not to allow it to creak, and find treasure beyond your wildest dreams within.\n\nFood! Glorious, edible food! Salted meets! Fruit conserves! All sorts of tasty, durable nutrition.\n\nThey must have been hoarding this here, and eating this stuff while the rest of us have to eat the paltry rations. And not telling anyone! It makes you sick, it makes you mad.\n\nAnd it makes you hungry. But before you think about that, you decide that the authorities MUST be told about this. It shouldn\'t be allowed, and you sincerely hope it\'s not.\n\nNow back to your stomach. You are sorely tempted to take some of this. They\'ve got far more than enough, after all, and they\'d probably never know. Just enough to get you through the next few days without rations.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
        if result == 0:
            p.TalkingText = "You stuff your pockets, taking food from nearer the bottom of the chest so your thievery won\'t be too noticeable.\n\nYou think you hear footsteps from somewhere in the house - you\'d better get out before you\'re noticed."
            Party.Food += 5
            StuffDone["2_9"] = 1
            return
        elif result == 1:
            p.TalkingText = "It takes a great strength of will to close the  lid on temptation, but you manage. You can\'t really go around stealing - that\'s just as bit as what they\'re doing."
            return
        return

def RefugeNorth_106_TalkingTrigger38(p):
    if StuffDone["3_3"] >= 1:
        p.TalkingText = "\"Fly,\" you call absently, pointing to the wall behind Jonathan. As he turns casually to take a look, you sneak a peek over the counter at his cloak. You can\'t get a proper look without arising his suspicions, but you can\'t see the tear you were expecting\n\nJonathan turns back after a fruitless search for the fly, interrupting your thoughts. \"If this is some Exile trick...\""
        return

def RefugeNorth_107_TalkingTrigger43(p):
    if StuffDone["3_3"] >= 1:
        p.TalkingText = "You ask her if Jonathan had got her to repair anything recently. \"Oh, yes,\" she responds encouragingly. \"He came round here not long ago.\" She tells you when. You work out that it must have been very soon after your near death!\n\n\"Some rip in his cloak. Fixed it up in minutes. Just had to -\" you cut her off. She\'s given you the proof you need already."
        StuffDone["3_7"] = 1
        return
    if StuffDone["3_3"] < 1:
        return

def RefugeNorth_108_TalkingTrigger44(p):
    if StuffDone["3_3"] >= 1:
        if StuffDone["3_7"] >= 1:
            p.TalkingText = "You tell him about the shred of material you found and the repair work. He thinks awhile.\n\n\"Well, that certainly is pretty convincing evidence. I assume you have this scrap?\" You nod, showing it him. \"Hmmm. Very convincing indeed.\""
            if StuffDone["4_1"] >= 2:
                p.TalkingText = "\"Well, that certainly is pretty convincing evidence. I assume you have this scrap?\" You nod, showing it him. \"Hmmm. Very convincing indeed. Yep. What with the stuff about that attack as well..... Let me think about it awhile. Come back in a few minutes.\""
                StuffDone["3_9"] = 1
                return
            if StuffDone["4_1"] < 2:
                p.TalkingText = "\"Well, that certainly is pretty convincing evidence. I assume you have this scrap?\" You nod, showing it him. \"Hmmm. Very convincing indeed. But, I\'m afraid, not conclusive. We\'ll need more than this before we can nab him. Not much more, but more.\""
                StuffDone["3_8"] = 1
                return
            return
        if StuffDone["3_7"] < 1:
            if StuffDone["6_4"] >= 1:
                p.TalkingText = "You tell him about the shred of material you found, and about the appropriately sized and positioned repair in Jonathan\'s cloak. He thinks awhile.\n\n\"So what you\'re telling me, basically, is that at some point Jonathan may have torn his cloak and repaired it, and that you happened to FIND this scrap soon after the murder attempt. Proves nothing, I\'m afraid.\""
                return
            if StuffDone["6_4"] < 1:
                return
            return
        return
    if StuffDone["3_3"] < 1:
        return
