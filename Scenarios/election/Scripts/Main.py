def Initialise_Scenario():
    pass

def Intro_Message(p):
    ChoiceBox("This year, the harvest failed.\n\nThe Gods have deserted Skargol Province, and the people are starving. In times of need, people must band together. They tend to band together against a common enemy. A scapegoat.\n\nThis time, that scapegoat is your people - the Exiles. For twenty years, the Exiles have lived in uneasy peace with the people of the Empire, but now that has broken.\n\nThe troubles started in the South, and you along with many others have been forced to flee Northwards. You have found this town, appropriately named Refuge, where the hatred has not yet been brought to the boil.\n\nBut the reserve rations won\'t last forever.\n\nYou wake to a new day in your room in the inn. Outside you hear raised voices - and for a moment you panic. But there is no hatred in the voices, just excitement. You get up to investigate.", eDialogPic.SCENARIO, 3, ["OK"])


def RefugeSouth_70_GlobalTalkingTrigger_51(p):
    if StuffDone["4_5"] >= 1:
        p.TalkingText = "She lowers her voice to a whisper. \"So you know about me and Mike. We\'ve been together for almost a year now, and you\'re the only one who knows. Please, tell no-one.\n\n\"It\'s perfect, now. HE\'S perfect.\" She starts to cry gently. \"Don\'t tell Cyril. He\'s - he\'s not stable. I don\'t know what he\'d do. Please don\'t tell him. I\'ll do anything. Just tell me what you want, I\'ll do it.\""
        return
    if StuffDone["4_5"] < 1:
        if SpecialItem.PartyHas("Awfullovepoem"):
            p.TalkingText = "She lowers her voice to a whisper. \"So you know about me and Mike. We\'ve been together for almost a year now, and you\'re the only one who knows. Please, tell no-one.\n\n\"It\'s perfect, now. HE\'S perfect.\" She starts to cry gently. \"Don\'t tell Cyril. He\'s - he\'s not stable. I don\'t know what he\'d do. Please don\'t tell him. I\'ll do anything. Just tell me what you want, I\'ll do it.\""
            return
        return

def RefugeSouth_71_GlobalTalkingTrigger_52(p):
    if StuffDone["4_5"] >= 1:
        if StuffDone["1_7"] >= 1:
            p.TalkingText = "She looks at you sternly. \"You\'re already blackmailing me. You\'ll get nothing more from me.\""
            return
        if StuffDone["1_7"] < 1:
            if StuffDone["50_0"] >= 1:
                p.TalkingText = "She looks at you sternly. \"You\'re already blackmailing me. You\'ll get nothing more from me.\""
                return
            if StuffDone["50_0"] < 1:
                response = InputTextBox("Enter something:", "")
                response = response[0:4].upper()
                if response == "VOTE":
                    p.TalkingText = "She closes her eyes, breathes deeply. \"OK. I\'ll vote for you, if that\'s what you need to keep your mouth shut.\" She practically spits this out, with real venom in her voice. And yet she seems somehow relieved that you asked no worse of her.\n\n\"Now go away. I\'d rather not make conversation with my blackmailer.\""
                    StuffDone["50_0"] = 1
                    StuffDone["100_0"] -= 1
                    if StuffDone["100_0"] == 250:
                        pass
                    StuffDone["100_2"] += 1
                    if StuffDone["100_2"] == 250:
                        pass
                    return
                elif response == "FUCK":
                    p.TalkingText = "She looks at you hollowly, just looking through you for a while. She puts her head in her hands for a minute, then looks up. \"OK.\" She says, shaking her head, seeing what she has been reduced to.\n\n\"OK. I\'ll do it, if that really is the price you ask.\" You can\'t quite believe it is, but you can\'t just pass up the opportunity. \"I\'ll meet you in your room tonight. Now just go away.\""
                    StuffDone["1_7"] = 1
                    return
                p.TalkingText = "She frowns. \"I don\'t think I can fulfil that particular request. Sorry.\"\n\n\"If there\'s anything else you want, just tell me. Of course, if you\'re going to blackmail me, and just won\'t tell Cyril, or anyone else, then thank you.\""
                return
            return
        return
    if StuffDone["4_5"] < 1:
        if SpecialItem.PartyHas("Awfullovepoem"):
            if StuffDone["1_7"] >= 1:
                p.TalkingText = "She looks at you sternly. \"You\'re already blackmailing me. You\'ll get nothing more from me.\""
                return
            if StuffDone["1_7"] < 1:
                if StuffDone["50_0"] >= 1:
                    p.TalkingText = "She looks at you sternly. \"You\'re already blackmailing me. You\'ll get nothing more from me.\""
                    return
                if StuffDone["50_0"] < 1:
                    response = InputTextBox("Enter something:", "")
                    response = response[0:4].upper()
                    if response == "VOTE":
                        p.TalkingText = "She closes her eyes, breathes deeply. \"OK. I\'ll vote for you, if that\'s what you need to keep your mouth shut.\" She practically spits this out, with real venom in her voice. And yet she seems somehow relieved that you asked no worse of her.\n\n\"Now go away. I\'d rather not make conversation with my blackmailer.\""
                        StuffDone["50_0"] = 1
                        StuffDone["100_0"] -= 1
                        if StuffDone["100_0"] == 250:
                            pass
                        StuffDone["100_2"] += 1
                        if StuffDone["100_2"] == 250:
                            pass
                        return
                    elif response == "FUCK":
                        p.TalkingText = "She looks at you hollowly, just looking through you for a while. She puts her head in her hands for a minute, then looks up. \"OK.\" She says, shaking her head, seeing what she has been reduced to.\n\n\"OK. I\'ll do it, if that really is the price you ask.\" You can\'t quite believe it is, but you can\'t just pass up the opportunity. \"I\'ll meet you in your room tonight. Now just go away.\""
                        StuffDone["1_7"] = 1
                        return
                    p.TalkingText = "She frowns. \"I don\'t think I can fulfil that particular request. Sorry.\"\n\n\"If there\'s anything else you want, just tell me. Of course, if you\'re going to blackmail me, and just won\'t tell Cyril, or anyone else, then thank you.\""
                    return
                return
            return
        return

def RefugeSouth_72_GlobalTalkingTrigger_54(p):
    if StuffDone["4_5"] >= 1:
        if StuffDone["50_5"] >= 1:
            p.TalkingText = "\"Look. I\'m voting for Vogel, and that\'s the limit of my blackmailability.\n\n\"Now just go away and leave us all alone.\""
            return
        if StuffDone["50_5"] < 1:
            if SpecialItem.PartyHas("Awfullovepoem"):
                p.TalkingText = "His eyes widen perceptibly as you point out that you COULD tell his lover\'s husband about the affair, likely resulting in Mike\'s bloody death.\n\nYou proceed to show him the evidence you have - the poems. He swallows noisily. \"OK, OK. You want my vote, yes? Well you can\'t have it. But I will, I suppose, vote for Vogel, if you agree never to reveal your knowledge.\" You agree."
                StuffDone["50_5"] = 1
                StuffDone["100_1"] -= 1
                if StuffDone["100_1"] == 250:
                    pass
                StuffDone["100_0"] += 1
                if StuffDone["100_0"] == 250:
                    pass
                return
            p.TalkingText = "His eyes widen perceptibly as you point out that you COULD tell his lover\'s husband about the affair, likely resulting in Mike\'s bloody death.\n\n\"Ah, but he would never take the word of an Exile like you. So try and tell him, if you want.\""
            return
        return

def RefugeNorth_99_GlobalTalkingTrigger_1(p):
    if StuffDone["12_4"] == 250:
        return
    result = ChoiceBox("His expression takes on a serious edge, his eyes now eager. \"We like it here. We\'ve put a lot of work into this place. We do not want to have to leave it. Now we\'ve been in this situation many times over the last few weeks.\n\nEvery time, Empire-Exile tensions have grown rapidly, until the already weak bond between us snaps completely. You can see the same process starting here. But here we have an advantage over the situation elsewhere.\n\nHere the process is put on a semi-official basis by the election. If Nash wins, we all get chucked out. If, on the other hand, Vogel wins, then the situation will become basically equivalent to that in the other towns -\n\na well-meaning Mayor who nonetheless is too weak-willed to have any control over the people\'s passions. We would have no guarantee of safety. No. I have a better idea. I understand that you are already running in this election, officially.\n\nWell we want to make it a reality. We want you to WIN the election, so you can be spokesman for the Exiles, for fairness, for rationality, for love not hate. And don\'t think you can\'t do it - with our help, you can.\n\nYou\'d have two votes right here. And we\'ll campaign on your behalf - make sure everyone understands that you are a likely candidate, not a wasted vote. You can do it. We really believe you can. So what do you say - will you give it a go?\"", eDialogPic.CREATURE, 2, ["Yes", "No"])
    if result == 0:
        StuffDone["12_4"] = 250
        StuffDone["Event_1"] = Party.Day
        p.TalkingText = "With that one word, his earnest face breaks into a great grin, as he pats you hard on the back. \"I knew you\'d do it! Thank you. Thank you very much. But we\'re relying on you, now, you understand. You must win.\n\n\"But we\'ll help. In fact,\" He confers briefly with his wife, \"yes. Meet us tonight, North end of the market. Our campaign will start there!\""
        StuffDone["2_3"] = 1
        StuffDone["2_1"] = 1
        StuffDone["3_1"] = 1
        StuffDone["100_0"] -= 2
        if StuffDone["100_0"] == 250:
            pass
        StuffDone["100_2"] += 2
        if StuffDone["100_2"] == 250:
            pass
        return
    elif result == 1:
        StuffDone["12_4"] = 250
        p.TalkingText = "He reacts as if your \'no\' was a blow to the stomach. He sits down heavily. \"I see. You have your reasons, I suppose?\" You try to explain, but he waves you silent. \"No, no, you don\'t have to explain.\n\n\"But just - if you reconsider, just tell me. Well, it looks like we had better start packing.\" Your not sure exactly what they\'ve got to pack, but you admit it sounded good."
        StuffDone["12_4"] = 0
        return

def Townname_172_GlobalTalkingTrigger_8(p):
    if StuffDone["50_2"] >= 2:
        p.TalkingText = "\"Well I\'m voting for you, of course!\"\n\n\"And I sincerely hope you win. I\'m sure you\'d do a good job.\""
        return
    if StuffDone["50_2"] < 1:
        if StuffDone["1_4"] >= 1:
            if StuffDone["2_1"] >= 1:
                p.TalkingText = "\"I hear that you are now considered a serious contender for these elections, and, despite the fact that I barely know you, I do know that you are an Exile - probably a good person, using the logic I once used to condemn your people.\n\n\"And I do know that you are intelligent enough to be able to change my mind - not easy once I\'ve decided something. My vote is yours.\""
                StuffDone["50_2"] = 2
                StuffDone["100_1"] -= 1
                if StuffDone["100_1"] == 250:
                    pass
                StuffDone["100_2"] += 1
                if StuffDone["100_2"] == 250:
                    pass
                return
            if StuffDone["2_1"] < 1:
                p.TalkingText = "\"I understand that, although you are officially campaigning, you aren\'t really, in that you have done nothing to advertise your condition as an eligible candidate. Therefore...\n\n\"I shall vote for Vogel. But understand that I would much rather vote for you, being an Exile.\" He smiles at this last. \"Just prove you want to win, and I will.\""
                StuffDone["50_2"] = 1
                StuffDone["100_1"] -= 1
                if StuffDone["100_1"] == 250:
                    pass
                StuffDone["100_0"] += 1
                if StuffDone["100_0"] == 250:
                    pass
                return
            return
        if StuffDone["1_4"] < 1:
            return
        return
    if StuffDone["2_1"] >= 1:
        p.TalkingText = "\"I hear that you are now considered a serious contender for these elections, and, despite the fact that I barely know you, I do know that you are an Exile - probably a good person, using the logic I once used to condemn your people.\n\n\"And I do know that you are intelligent enough to be able to change my mind - not easy once I\'ve decided something. My vote is yours.\""
        StuffDone["50_2"] = 2
        StuffDone["100_0"] -= 1
        if StuffDone["100_0"] == 250:
            pass
        StuffDone["100_2"] += 1
        if StuffDone["100_2"] == 250:
            pass
        return
    if StuffDone["2_1"] < 1:
        p.TalkingText = "\"I shall vote for Vogel. But understand that I would much rather vote for you, being an Exile.\" He smiles at this last. \"Just prove you want to win, and I will.\"\n\n\"I think you should try. You\'d make a good Mayor.\""
        return

def Townname_173_GlobalTalkingTrigger_12(p):
    if StuffDone["1_2"] >= 1:
        if StuffDone["3_2"] >= 1:
            return
        return
    if StuffDone["1_2"] < 1:
        p.TalkingText = "You try to attack his argument, but he cuts you off.\n\n\"At least let me explain my case before you try to rubbish it.\""
        return

def Townname_175_GlobalTalkingTrigger_14(p):
    if StuffDone["1_2"] >= 1:
        if StuffDone["1_3"] >= 1:
            p.TalkingText = "You show him the book, pointing out the \'crimes\' of Exiles. \"Oh God. You\'re right. These people have done nothing wrong. I mean \"Being Cursed at Birth\"! That\'s just a euphemism for a birth anomaly - for being a \'freak\'!\n\n\"And most people have done nothing more or less than challenge authority - fair enough, considering.\" He thinks awhile. \"OK. I\'m convinced.\""
            StuffDone["1_4"] = 1
            return
        if StuffDone["1_3"] < 1:
            return
        return
    if StuffDone["1_2"] < 1:
        p.TalkingText = "You try to attack his argument, but he cuts you off.\n\n\"At least let me explain my case before you try to rubbish it.\""
        return

def Townname_176_GlobalTalkingTrigger_21(p):
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 8))
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) - 7))
    for pc in Party.EachAlivePC():
        pc.Cure(8)

def Townname_177_GlobalTalkingTrigger_25(p):
    if StuffDone["4_5"] >= 1:
        if SpecialItem.PartyHas("Awfullovepoem"):
            p.TalkingText = "You try to tell him about his wife\'s affair with Mike. But you find it increasingly difficult, as he moves his not inconsiderable head nearer and nearer to yours, an expression of pure contempt a vital component of it.\n\nYou conclude by triumphantly revealing the poem you found. He looks briefly at it. \"Anyone could have written this. I\'m not going to believe your slander.\""
            return
        p.TalkingText = "You try to tell him about his wife\'s affair with Mike. But you find it increasingly difficult, as he moves his not inconsiderable head nearer and nearer to yours, an expression of pure contempt a vital component of it.\n\n\"You think,\" he says slowly, \"that I am going to take the unsupported word of YOU,\" he pokes your chest as qualification, \"an Exile. You\'re wrong.\""
        return
    if StuffDone["4_5"] < 1:
        return

def RefugeSouthnight_234_GlobalTalkingTrigger_47(p):
    if StuffDone["50_1"] >= 1:
        if StuffDone["4_6"] >= 1:
            p.TalkingText = "\"I don\'t know what you\'re talking about, so I think it might just be best if I went to sleep whilst you marshal your thoughts. OK?\"\n\nYou don\'t get a chance to answer. She begins snoring pretty much straight away."
            return
        if StuffDone["4_6"] < 1:
            StuffDone["4_6"] = 1
            if StuffDone["50_1"] >= 2:
                StuffDone["100_2"] += 1
                if StuffDone["100_2"] == 250:
                    pass
                return
            if StuffDone["50_1"] < 1:
                return
            StuffDone["100_0"] += 1
            if StuffDone["100_0"] == 250:
                pass
            return
        return
    if StuffDone["50_1"] < 1:
        p.TalkingText = "\"I don\'t know what you\'re talking about, so I think it might just be best if I went to sleep whilst you marshal your thoughts. OK?\"\n\nYou don\'t get a chance to answer. She begins snoring pretty much straight away."
        return

def On_Using_SI_HealingSceptre_235(p):
    MessageBox("You touch the tip of the sceptre to your head and hold it there for a few seconds. Bright blue bathes your head and mind. You feel the crippling weakness flowing from you to the glowing head of the sceptre.\n\nDrained, you collapse to the floor, spending a few seconds in blissful unconsciousness. The blue recedes, you get up. Such a powerful experience, undiminished by repetition.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 8))
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.ASLEEP, Maths.MinMax(0, 8, pc.Status(eAffliction.ASLEEP) + 2))

def ScenarioTimer0_236(p):
    if StuffDone["111_0"] >= 1:
        MessageBox("You can feel yourself weakening. One of the many effects of your disease is that you cannot handle too much excitement. The thrill of combat, the heightened senses, the increased speed - all that a drawn blade means, basically.\n\nA good feeling at first, but now it\'s starting to get to you.")
        Party.Damage(Maths.Rand(1, 1, 5) + 0, eDamageType.UNBLOCKABLE)
        Wait()
        StuffDone["111_0"] = 1
        if Game.Mode == eMode.COMBAT:
            return;
        StuffDone["111_0"] = 0
        if StuffDone["111_1"] >= 1:
            StuffDone["111_1"] = 0
            MessageBox("As you are heading back towards the inn, you suddenly realise that something is wrong. You can\'t see where you are going any more - all you can see is yourself in this small room, a white dot on the floor in front of you.\n\nA side effect of your disease, you see, is that you have these hallucinations every now and then, generally when you are tired. You find that stepping on the white dot tends to make them go away.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(38,42))
            p.CancelAction = True
            return
        if StuffDone["111_2"] >= 1:
            StuffDone["111_2"] = 0
            MessageBox("As you are heading back towards the inn, you suddenly realise that something is wrong. You can\'t see where you are going any more - all you can see is yourself in this small room, a white dot on the floor in front of you.\n\nA side effect of your disease, you see, is that you have these hallucinations every now and then, generally when you are tired. You find that stepping on the white dot tends to make them go away.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(38,42))
            p.CancelAction = True
            return
        return
    StuffDone["111_0"] = 1
    if Game.Mode == eMode.COMBAT:
        return;
    StuffDone["111_0"] = 0
    if StuffDone["111_1"] >= 1:
        StuffDone["111_1"] = 0
        MessageBox("As you are heading back towards the inn, you suddenly realise that something is wrong. You can\'t see where you are going any more - all you can see is yourself in this small room, a white dot on the floor in front of you.\n\nA side effect of your disease, you see, is that you have these hallucinations every now and then, generally when you are tired. You find that stepping on the white dot tends to make them go away.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(38,42))
        p.CancelAction = True
        return
    if StuffDone["111_2"] >= 1:
        StuffDone["111_2"] = 0
        MessageBox("As you are heading back towards the inn, you suddenly realise that something is wrong. You can\'t see where you are going any more - all you can see is yourself in this small room, a white dot on the floor in front of you.\n\nA side effect of your disease, you see, is that you have these hallucinations every now and then, generally when you are tired. You find that stepping on the white dot tends to make them go away.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(38,42))
        p.CancelAction = True
        return

def ScenarioTimer_x_237(p):
    StuffDone["111_1"] = 1
    if Game.Mode == eMode.COMBAT:
        return;
    StuffDone["111_1"] = 0
    MessageBox("As you are heading back towards the inn, you suddenly realise that something is wrong. You can\'t see where you are going any more - all you can see is yourself in this small room, a white dot on the floor in front of you.\n\nA side effect of your disease, you see, is that you have these hallucinations every now and then, generally when you are tired. You find that stepping on the white dot tends to make them go away.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(38,42))
    p.CancelAction = True

def ScenarioTimer_x_238(p):
    if StuffDone["10_4"] >= 1:
        StuffDone["10_4"] -= 1
        if StuffDone["10_4"] == 250:
            pass
        return
    if StuffDone["10_4"] < 1:
        MessageBox("It\'s starting to get light outside, and if you don\'t get some more sleep you know you\'ll feel the effects tomorrow. You\'d better go back to your room in a minute. Just finish what you\'re doing first.")
        Timer(None, 10, False,  "ScenarioTimer_x_239")
        return

def ScenarioTimer_x_239(p):
    StuffDone["111_2"] = 1
    if Game.Mode == eMode.COMBAT:
        return;
    StuffDone["111_2"] = 0
    MessageBox("As you are heading back towards the inn, you suddenly realise that something is wrong. You can\'t see where you are going any more - all you can see is yourself in this small room, a white dot on the floor in front of you.\n\nA side effect of your disease, you see, is that you have these hallucinations every now and then, generally when you are tired. You find that stepping on the white dot tends to make them go away.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(38,42))
    p.CancelAction = True

def ScenarioTimer_x_240(p):
    if StuffDone["10_3"] >= 1:
        StuffDone["10_3"] -= 1
        if StuffDone["10_3"] == 250:
            pass
        return
    if StuffDone["10_3"] < 1:
        MessageBox("You notice that it\'s starting to get dark. You had probably better head back to the inn in a minute. You decide to quickly finish what you are doing.")
        Timer(None, 10, False,  "ScenarioTimer_x_237")
        return

def GlobalCall_RefugeSouth_241(p):
    MessageBox("There are a number of stone pedestals lined against this wall, comprising the city museum. It seems quite pathetic at first glance, the few exhibits here mainly dealing with the history of the city.\n\nBut a second look reveals - no. You can\'t deny it. Whatever grand and noble ideals they may represent, the actual exhibits are deathly dull - a sample of the actual kind of brick used to build the place! Maps through the ages!")
    MessageBox("Actually, the maps are quite interesting, in a way. You can see the rise and rise of the city in its early days - more and more buildings appearing, and then the Southern section materialising. So not that interesting at all.\n\nBut you do notice one thing. About fifty years ago, a smuggler\'s entrance started being labelled in the Southern wall, presumably when it was discovered. But then it stopped being labelled again. Why you don\'t know.")
    StuffDone["1_5"] = 1

def ScenarioTimer_x_242(p):
    if StuffDone["10_3"] >= 1:
        StuffDone["10_3"] -= 1
        if StuffDone["10_3"] == 250:
            pass
        return
    if StuffDone["10_3"] < 1:
        MessageBox("You notice that it\'s starting to get dark. You had probably better head back to the inn in a minute. You decide to quickly finish what you are doing.")
        Timer(None, 10, False,  "ScenarioTimer_x_237")
        return

def GlobalCall_RefugeSouth_243(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if p.Origin == eCallOrigin.SEARCHING: return
    result = ChoiceBox("If you really want to, you can stay in bed until night fall, though you doubt you\'ll be able to get much sleep.\n\nDo you?", eDialogPic.TERRAIN, 143, ["No", "Yes"])
    if result == 0:
        return
    elif result == 1:
        if StuffDone["0_3"] >= 1:
            StuffDone["10_3"] += 1
            if StuffDone["10_3"] == 250:
                pass
            if StuffDone["200_0"] >= 1:
                if StuffDone["1_7"] >= 1:
                    if StuffDone["10_1"] >= 1:
                        MessageBox("Still tired after last night\'s escapades, you decide to skip the evening\'s festivities in the pub. You can\'t stand Mike\'s brand of \'comedy\', anyway. You get into bed, and sleep.\n\nYou wake up in the middle of the night, for no obvious reason. Just fretting about your future, you suppose. Anyway, you doubt you\'ll be able to get back to sleep anytime soon, so you might as well get up for a quick wonder.")
                        if StuffDone["4_5"] >= 1:
                            Timer(None, 240, False,  "ScenarioTimer_x_238")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                            return
                        if StuffDone["4_5"] < 1:
                            StuffDone["4_4"] = 0
                            Timer(None, 240, False,  "ScenarioTimer_x_238")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                            return
                        return
                    if StuffDone["10_1"] < 1:
                        MessageBox("You wake to a knocking on the door. It\'s Cilla - come to fulfil her promise. You get up, motion her in. You put your arm round her thin frame, guide her to the bed. Then you have your way with her.\n\nShe is compliant, if not willing. You are impressed that she barely sheds a tear as you go at her. She says not a word through the whole ordeal. Satisfied, you let her leave, off to her real lover, no doubt.")
                        StuffDone["10_1"] = 1
                        MessageBox("You find you cannot sleep, afterwards. Perhaps a stab of conscience, probably just the effect of recent physical exertion. You get up.")
                        if StuffDone["4_5"] >= 1:
                            Timer(None, 240, False,  "ScenarioTimer_x_238")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                            return
                        if StuffDone["4_5"] < 1:
                            StuffDone["4_4"] = 0
                            Timer(None, 240, False,  "ScenarioTimer_x_238")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                            return
                        return
                    return
                MessageBox("Still tired after last night\'s escapades, you decide to skip the evening\'s festivities in the pub. You can\'t stand Mike\'s brand of \'comedy\', anyway. You get into bed, and sleep.\n\nYou wake up in the middle of the night, for no obvious reason. Just fretting about your future, you suppose. Anyway, you doubt you\'ll be able to get back to sleep anytime soon, so you might as well get up for a quick wonder.")
                if StuffDone["4_5"] >= 1:
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                if StuffDone["4_5"] < 1:
                    StuffDone["4_4"] = 0
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                return
            if StuffDone["200_0"] < 1:
                MessageBox("You attend the evening festivities at the inn. Almost everyone from the town is there, except Nash, Gwyneth and the Mayor of course, who have to stay in the town hall. But the numbers are made up, you notice, by the two out-of-towners.\n\nYou wonder why they are still here, but they are talking to Jonathan, so you keep away. Instead you just drink with everyone else and watch Mike\'s show. It\'s terrible, but no-one cares. A great time is had by all, but you eventually retire to your room.")
                MessageBox("You wake from your dreams. You thought you heard a voice, but listening now you can hear nothing. Oh, no, you can hear voices talking from the South - probably just Cilla and Cyril. You relax and try to get back to sleep.")
                MessageBox("\"Worm,\" someone whispers breathily and loudly from outside. \"Worm.\" You snap back into wakefulness. \"Come here, worm. Come.\"\n\nYou hear someone tapping on the wall outside. \"Worm. Time to die, worm.\" You hear the sound of metal against stone - inside your room. Something\'s been thrown threw the window! You get up quickly.")
                Timer(None, 240, False,  "ScenarioTimer_x_238")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                return
            return
        if StuffDone["0_3"] < 1:
            MessageBox("You ought to at least find out what all the fuss is about outside before you go to sleep. Of course you\'re tired, you remonstrate yourself, but where has burying your head in the sand ever got you? Get out there.")
            return
        return

def GlobalCall_RefugeSouth_244(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["200_0"] >= 1:
        if StuffDone["1_7"] >= 1:
            if StuffDone["10_1"] >= 1:
                MessageBox("Still tired after last night\'s escapades, you decide to skip the evening\'s festivities in the pub. You can\'t stand Mike\'s brand of \'comedy\', anyway. You get into bed, and sleep.\n\nYou wake up in the middle of the night, for no obvious reason. Just fretting about your future, you suppose. Anyway, you doubt you\'ll be able to get back to sleep anytime soon, so you might as well get up for a quick wonder.")
                if StuffDone["4_5"] >= 1:
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                if StuffDone["4_5"] < 1:
                    StuffDone["4_4"] = 0
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                return
            if StuffDone["10_1"] < 1:
                MessageBox("You wake to a knocking on the door. It\'s Cilla - come to fulfil her promise. You get up, motion her in. You put your arm round her thin frame, guide her to the bed. Then you have your way with her.\n\nShe is compliant, if not willing. You are impressed that she barely sheds a tear as you go at her. She says not a word through the whole ordeal. Satisfied, you let her leave, off to her real lover, no doubt.")
                StuffDone["10_1"] = 1
                MessageBox("You find you cannot sleep, afterwards. Perhaps a stab of conscience, probably just the effect of recent physical exertion. You get up.")
                if StuffDone["4_5"] >= 1:
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                if StuffDone["4_5"] < 1:
                    StuffDone["4_4"] = 0
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                return
            return
        MessageBox("Still tired after last night\'s escapades, you decide to skip the evening\'s festivities in the pub. You can\'t stand Mike\'s brand of \'comedy\', anyway. You get into bed, and sleep.\n\nYou wake up in the middle of the night, for no obvious reason. Just fretting about your future, you suppose. Anyway, you doubt you\'ll be able to get back to sleep anytime soon, so you might as well get up for a quick wonder.")
        if StuffDone["4_5"] >= 1:
            Timer(None, 240, False,  "ScenarioTimer_x_238")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(27,35)
            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
            return
        if StuffDone["4_5"] < 1:
            StuffDone["4_4"] = 0
            Timer(None, 240, False,  "ScenarioTimer_x_238")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(27,35)
            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
            return
        return
    if StuffDone["200_0"] < 1:
        MessageBox("You attend the evening festivities at the inn. Almost everyone from the town is there, except Nash, Gwyneth and the Mayor of course, who have to stay in the town hall. But the numbers are made up, you notice, by the two out-of-towners.\n\nYou wonder why they are still here, but they are talking to Jonathan, so you keep away. Instead you just drink with everyone else and watch Mike\'s show. It\'s terrible, but no-one cares. A great time is had by all, but you eventually retire to your room.")
        MessageBox("You wake from your dreams. You thought you heard a voice, but listening now you can hear nothing. Oh, no, you can hear voices talking from the South - probably just Cilla and Cyril. You relax and try to get back to sleep.")
        MessageBox("\"Worm,\" someone whispers breathily and loudly from outside. \"Worm.\" You snap back into wakefulness. \"Come here, worm. Come.\"\n\nYou hear someone tapping on the wall outside. \"Worm. Time to die, worm.\" You hear the sound of metal against stone - inside your room. Something\'s been thrown threw the window! You get up quickly.")
        Timer(None, 240, False,  "ScenarioTimer_x_238")
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(27,35)
        Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
        return

def GlobalCall_RefugeSouth_245(p):
    result = ChoiceBox("Right then. This is it.\n\nIf you want to call the election, all you have to do is strike the table thrice. Why, you don\'t know, and you\'re going to feel a bit silly doing it, but then this is an old town, with old customs.\n\nSo, if you\'re absolutely sure that the vote\'s going to go the right way, that no loose ends remain to be tied, then go for it.\n\nDo you?", eDialogPic.TERRAIN, 128, ["Yes", "No"])
    if result == 0:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(13,21)
        Party.MoveToMap(TownMap.List["Townname_4"])
        return
    elif result == 1:
        return

def GlobalCall_RefugeSouth_246(p):
    if StuffDone["10_0"] >= 1:
        if SpecialItem.PartyHas("Scrap"):
            return
        MessageBox("Just as you are about to give up following in the footsteps of you\'re attacker, you find this. A few sharp twigs stick up from the ground here, and hanging off one is a scrap of red material, presumably torn off someone\'s clothing.\n\nYou can\'t be sure it belonged to your attacker, but it seems likely. And thinking back to the shock-clouded memory of the brief glimpse you got of him, you seem to remember him wearing something red. You take the scrap.")
        SpecialItem.Give("Scrap")
        StuffDone["3_3"] = 1
        return
    if StuffDone["10_0"] < 1:
        return

def GlobalCall_RefugeSouth_247(p):
    MessageBox("And so with that last blow you slew the townsperson. You had your reasons for the murder, and your murderee had a fair share of enemies in the town. But nonetheless, even in this town at this time, the law prevails.\n\nYou try to flee, but are soon caught and tried. Found guilty of murder you are exiled from the town. The elections are held and Nash wins - now there is actual PROOF that Exiles are heartless criminals who eat baby\'s heads. Probably.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def GlobalCall_RefugeNorth_248(p):
    StuffDone["100_1"] -= 1
    if StuffDone["100_1"] == 250:
        pass
    StuffDone["100_2"] += 1
    if StuffDone["100_2"] == 250:
        pass

def GlobalCall_RefugeNorth_249(p):
    if StuffDone["200_0"] >= 1:
        if StuffDone["1_7"] >= 1:
            if StuffDone["10_1"] >= 1:
                MessageBox("Still tired after last night\'s escapades, you decide to skip the evening\'s festivities in the pub. You can\'t stand Mike\'s brand of \'comedy\', anyway. You get into bed, and sleep.\n\nYou wake up in the middle of the night, for no obvious reason. Just fretting about your future, you suppose. Anyway, you doubt you\'ll be able to get back to sleep anytime soon, so you might as well get up for a quick wonder.")
                if StuffDone["4_5"] >= 1:
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                if StuffDone["4_5"] < 1:
                    StuffDone["4_4"] = 0
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                return
            if StuffDone["10_1"] < 1:
                MessageBox("You wake to a knocking on the door. It\'s Cilla - come to fulfil her promise. You get up, motion her in. You put your arm round her thin frame, guide her to the bed. Then you have your way with her.\n\nShe is compliant, if not willing. You are impressed that she barely sheds a tear as you go at her. She says not a word through the whole ordeal. Satisfied, you let her leave, off to her real lover, no doubt.")
                StuffDone["10_1"] = 1
                MessageBox("You find you cannot sleep, afterwards. Perhaps a stab of conscience, probably just the effect of recent physical exertion. You get up.")
                if StuffDone["4_5"] >= 1:
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                if StuffDone["4_5"] < 1:
                    StuffDone["4_4"] = 0
                    Timer(None, 240, False,  "ScenarioTimer_x_238")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
                    return
                return
            return
        MessageBox("Still tired after last night\'s escapades, you decide to skip the evening\'s festivities in the pub. You can\'t stand Mike\'s brand of \'comedy\', anyway. You get into bed, and sleep.\n\nYou wake up in the middle of the night, for no obvious reason. Just fretting about your future, you suppose. Anyway, you doubt you\'ll be able to get back to sleep anytime soon, so you might as well get up for a quick wonder.")
        if StuffDone["4_5"] >= 1:
            Timer(None, 240, False,  "ScenarioTimer_x_238")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(27,35)
            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
            return
        if StuffDone["4_5"] < 1:
            StuffDone["4_4"] = 0
            Timer(None, 240, False,  "ScenarioTimer_x_238")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(27,35)
            Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
            return
        return
    if StuffDone["200_0"] < 1:
        MessageBox("You attend the evening festivities at the inn. Almost everyone from the town is there, except Nash, Gwyneth and the Mayor of course, who have to stay in the town hall. But the numbers are made up, you notice, by the two out-of-towners.\n\nYou wonder why they are still here, but they are talking to Jonathan, so you keep away. Instead you just drink with everyone else and watch Mike\'s show. It\'s terrible, but no-one cares. A great time is had by all, but you eventually retire to your room.")
        MessageBox("You wake from your dreams. You thought you heard a voice, but listening now you can hear nothing. Oh, no, you can hear voices talking from the South - probably just Cilla and Cyril. You relax and try to get back to sleep.")
        MessageBox("\"Worm,\" someone whispers breathily and loudly from outside. \"Worm.\" You snap back into wakefulness. \"Come here, worm. Come.\"\n\nYou hear someone tapping on the wall outside. \"Worm. Time to die, worm.\" You hear the sound of metal against stone - inside your room. Something\'s been thrown threw the window! You get up quickly.")
        Timer(None, 240, False,  "ScenarioTimer_x_238")
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(27,35)
        Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])
        return

def GlobalCall_RefugeNorth_250(p):
    StuffDone["100_1"] -= 1
    if StuffDone["100_1"] == 250:
        pass
    StuffDone["100_0"] += 1
    if StuffDone["100_0"] == 250:
        pass

def GlobalCall_RefugeNorthnight_253(p):
    MessageBox("You get back into bed and rest uneventfully until morning.")
    StuffDone["200_0"] += 1
    if StuffDone["200_0"] == 250:
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(24,34))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(32,34))
    if StuffDone["3_1"] >= 1:
        StuffDone["3_5"] = 1
        if StuffDone["200_0"] >= 2:
            if StuffDone["12_1"] >= 1:
                StuffDone["2_4"] = 0
                if StuffDone["200_0"] >= 3:
                    if StuffDone["200_0"] >= 4:
                        MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(13,21)
                        Party.MoveToMap(TownMap.List["Townname_4"])
                        return
                    if StuffDone["200_0"] < 4:
                        if StuffDone["12_1"] >= 1:
                            Timer(None, 390, False,  "ScenarioTimer_x_240")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                            return
                        MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                        SpecialItem.Take("HealingSceptre")
                        MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                        SpecialItem.Give("Blackmailnote")
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    return
                if StuffDone["200_0"] < 3:
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["12_1"] < 1:
                StuffDone["2_4"] = 2
                if StuffDone["200_0"] >= 3:
                    if StuffDone["200_0"] >= 4:
                        MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(13,21)
                        Party.MoveToMap(TownMap.List["Townname_4"])
                        return
                    if StuffDone["200_0"] < 4:
                        if StuffDone["12_1"] >= 1:
                            Timer(None, 390, False,  "ScenarioTimer_x_240")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                            return
                        MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                        SpecialItem.Take("HealingSceptre")
                        MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                        SpecialItem.Give("Blackmailnote")
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    return
                if StuffDone["200_0"] < 3:
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            return
        if StuffDone["200_0"] < 2:
            StuffDone["2_4"] = 0
            if StuffDone["200_0"] >= 3:
                if StuffDone["200_0"] >= 4:
                    MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(13,21)
                    Party.MoveToMap(TownMap.List["Townname_4"])
                    return
                if StuffDone["200_0"] < 4:
                    if StuffDone["12_1"] >= 1:
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                    SpecialItem.Take("HealingSceptre")
                    MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                    SpecialItem.Give("Blackmailnote")
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["200_0"] < 3:
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        return
    if StuffDone["200_0"] >= 2:
        if StuffDone["12_1"] >= 1:
            StuffDone["2_4"] = 0
            if StuffDone["200_0"] >= 3:
                if StuffDone["200_0"] >= 4:
                    MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(13,21)
                    Party.MoveToMap(TownMap.List["Townname_4"])
                    return
                if StuffDone["200_0"] < 4:
                    if StuffDone["12_1"] >= 1:
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                    SpecialItem.Take("HealingSceptre")
                    MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                    SpecialItem.Give("Blackmailnote")
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["200_0"] < 3:
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        if StuffDone["12_1"] < 1:
            StuffDone["2_4"] = 2
            if StuffDone["200_0"] >= 3:
                if StuffDone["200_0"] >= 4:
                    MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(13,21)
                    Party.MoveToMap(TownMap.List["Townname_4"])
                    return
                if StuffDone["200_0"] < 4:
                    if StuffDone["12_1"] >= 1:
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                    SpecialItem.Take("HealingSceptre")
                    MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                    SpecialItem.Give("Blackmailnote")
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["200_0"] < 3:
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        return
    if StuffDone["200_0"] < 2:
        StuffDone["2_4"] = 0
        if StuffDone["200_0"] >= 3:
            if StuffDone["200_0"] >= 4:
                MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(13,21)
                Party.MoveToMap(TownMap.List["Townname_4"])
                return
            if StuffDone["200_0"] < 4:
                if StuffDone["12_1"] >= 1:
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                SpecialItem.Take("HealingSceptre")
                MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                SpecialItem.Give("Blackmailnote")
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        if StuffDone["200_0"] < 3:
            Timer(None, 390, False,  "ScenarioTimer_x_240")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(27,35)
            Party.MoveToMap(TownMap.List["RefugeSouth_0"])
            return
        return

def GlobalCall_RefugeSouthnight_256(p):
    return

def GlobalCall_RefugeSouthnight_257(p):
    Party.Food -= 1
    MessageBox("You get back into bed and rest uneventfully until morning.")
    StuffDone["200_0"] += 1
    if StuffDone["200_0"] == 250:
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(24,34))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(32,34))
    if StuffDone["3_1"] >= 1:
        StuffDone["3_5"] = 1
        if StuffDone["200_0"] >= 2:
            if StuffDone["12_1"] >= 1:
                StuffDone["2_4"] = 0
                if StuffDone["200_0"] >= 3:
                    if StuffDone["200_0"] >= 4:
                        MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(13,21)
                        Party.MoveToMap(TownMap.List["Townname_4"])
                        return
                    if StuffDone["200_0"] < 4:
                        if StuffDone["12_1"] >= 1:
                            Timer(None, 390, False,  "ScenarioTimer_x_240")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                            return
                        MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                        SpecialItem.Take("HealingSceptre")
                        MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                        SpecialItem.Give("Blackmailnote")
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    return
                if StuffDone["200_0"] < 3:
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["12_1"] < 1:
                StuffDone["2_4"] = 2
                if StuffDone["200_0"] >= 3:
                    if StuffDone["200_0"] >= 4:
                        MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(13,21)
                        Party.MoveToMap(TownMap.List["Townname_4"])
                        return
                    if StuffDone["200_0"] < 4:
                        if StuffDone["12_1"] >= 1:
                            Timer(None, 390, False,  "ScenarioTimer_x_240")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(27,35)
                            Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                            return
                        MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                        SpecialItem.Take("HealingSceptre")
                        MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                        SpecialItem.Give("Blackmailnote")
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    return
                if StuffDone["200_0"] < 3:
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            return
        if StuffDone["200_0"] < 2:
            StuffDone["2_4"] = 0
            if StuffDone["200_0"] >= 3:
                if StuffDone["200_0"] >= 4:
                    MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(13,21)
                    Party.MoveToMap(TownMap.List["Townname_4"])
                    return
                if StuffDone["200_0"] < 4:
                    if StuffDone["12_1"] >= 1:
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                    SpecialItem.Take("HealingSceptre")
                    MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                    SpecialItem.Give("Blackmailnote")
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["200_0"] < 3:
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        return
    if StuffDone["200_0"] >= 2:
        if StuffDone["12_1"] >= 1:
            StuffDone["2_4"] = 0
            if StuffDone["200_0"] >= 3:
                if StuffDone["200_0"] >= 4:
                    MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(13,21)
                    Party.MoveToMap(TownMap.List["Townname_4"])
                    return
                if StuffDone["200_0"] < 4:
                    if StuffDone["12_1"] >= 1:
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                    SpecialItem.Take("HealingSceptre")
                    MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                    SpecialItem.Give("Blackmailnote")
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["200_0"] < 3:
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        if StuffDone["12_1"] < 1:
            StuffDone["2_4"] = 2
            if StuffDone["200_0"] >= 3:
                if StuffDone["200_0"] >= 4:
                    MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(13,21)
                    Party.MoveToMap(TownMap.List["Townname_4"])
                    return
                if StuffDone["200_0"] < 4:
                    if StuffDone["12_1"] >= 1:
                        Timer(None, 390, False,  "ScenarioTimer_x_240")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(27,35)
                        Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                        return
                    MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                    SpecialItem.Take("HealingSceptre")
                    MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                    SpecialItem.Give("Blackmailnote")
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                return
            if StuffDone["200_0"] < 3:
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        return
    if StuffDone["200_0"] < 2:
        StuffDone["2_4"] = 0
        if StuffDone["200_0"] >= 3:
            if StuffDone["200_0"] >= 4:
                MessageBox("You get up in the morning, Cilla knocking on the door. This time, you know what it\'s about. This is the morning of the election! Your time is up, now all that is left is to pray that your efforts have been sufficient.\n\nYou follow the stream of people towards the town hall and approach the table, only for Gwyneth to wave you back.")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(13,21)
                Party.MoveToMap(TownMap.List["Townname_4"])
                return
            if StuffDone["200_0"] < 4:
                if StuffDone["12_1"] >= 1:
                    Timer(None, 390, False,  "ScenarioTimer_x_240")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(27,35)
                    Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                    return
                MessageBox("You wake in the morning. A few minutes later, you open your eyes, decide to get up. You grab for your staff, which you always sleep with. You miss. You try again. Nope. You pull back the covers - it\'s gone! And you could have sworn you left it there!\n\nPanic starts to set in. You need that staff, you really do. You get up, frantically search the room. Maybe it got knocked under the bed? No. Behind the dresser? Where could it have gone? Unless... it\'s then you find the note.")
                SpecialItem.Take("HealingSceptre")
                MessageBox("Scrawled on a scrap of paper, left on top of the dresser : \"Give up, Worm. You don\'t belong. Nash is Mayor. Give up, you get your \'sentimental value\' back.\" The handwriting changes with each word - obviously the author doesn\'t want to be caught.\n\nWell you won\'t be blackmailed into leaving. You\'ll find that staff, find who stole it. You realise now how stupid that lie you told was. But who would have thought? You take the note.")
                SpecialItem.Give("Blackmailnote")
                Timer(None, 390, False,  "ScenarioTimer_x_240")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(27,35)
                Party.MoveToMap(TownMap.List["RefugeSouth_0"])
                return
            return
        if StuffDone["200_0"] < 3:
            Timer(None, 390, False,  "ScenarioTimer_x_240")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(27,35)
            Party.MoveToMap(TownMap.List["RefugeSouth_0"])
            return
        return

def ScenarioTimer_x_260(p):
    MessageBox("You notice that it\'s starting to get dark. You had probably better head back to the inn in a minute. You decide to quickly finish what you are doing.")
    Timer(None, 10, False,  "ScenarioTimer_x_237")
