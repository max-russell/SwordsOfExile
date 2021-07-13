
def RefugeSouth_0_MapTrigger_25_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["10_9"] == 250:
        return
    StuffDone["10_9"] = 250
    MessageBox("Just as you open the door, you see the innkeeper, Cilla, just about to knock from the other side. \"Come on!\" She says. \"We\'ve all been called to the town hall.\" Seeing your expression of confusion, she explains.\n\n\"Don\'t you know? It\'s the election tomorrow. This is something to do with that. Now come on.\" You follow her to the town hall.")
    StuffDone["100_0"] = 6
    StuffDone["100_1"] = 11
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(24,27))
    p.CancelAction = True
    if StuffDone["0_0"] == 250:
        return
    StuffDone["0_0"] = 250
    ChoiceBox("The town hall is completely packed. It looks like everyone from the town is here. They nod happily to you and Cilla as you enter. The hall has been completely rearranged for the occasion - guards surround a bench in the centre on which are two pots.\n\nBehind that sits Gwyneth, who runs the potion shop. To her left is Mayor Vogel, and to her right is Nash - someone whom you know to be Exile-hater, however polite. As the last file in, Gwyneth claps her hands loudly to call attention to her.\n\n\"As you probably all know, tomorrow we will be holding the election for Mayor. I, who have volunteered to oversee the proceedings, have called you all here today to allow the candidates to each give a short speech on their suitability as Mayor.\"\n\n\"After these, we will hold a brief mock election. This will give you practice in the process, ensuring no mishaps tomorrow, and will let us see how things are shaping up. OK? Right. First up, our current Mayor, Vogel.\"\n\nMayor Vogel stands up, still wearing his sash of office. \"Hello, my citizens.\" He smiles. \"Right. My case is pretty simple. I have served as your Mayor for four years now, and I would like to think that I\'ve done a good job.\" cheers from the audience.\n\n\"And as far as I\'m concerned, there is no reason to change now. OK, I know we\'ve got a bit of a food problem, but I\'m sure that if we all pull together and eat no more than we need then we should be alright. Ummm, well that\'s it really.\" Mild applause.", eDialogPic.CREATURE, 31, ["OK"])
    ChoiceBox("Next Nash stands up. \"Thank you, Mayor. But I think, frankly, that you hugely underestimate the situation. Yes, we\'re OK now. But the reserves are running out. Soon we will go the way of the Southern territories - children starving, dying in the streets.\n\n\"Already we are being swamped by hoards of refugees from the South. The Mayor has been forced to close the gates to all trying to get in, starting today.\" Vogel nods sadly. \"But still we won\'t all be able to make it through the coming months.\"\n\n\"Now I want to quote a statistic for you, one which should point the way forwards. There are 21 people living in this town. I calculate that there is enough food for 17 to last until next harvest. Of those 21 people, four of them come from Exile.\"\n\nThe reaction to his words is a mix of shock, fear and, in a few cases, violent approval. Most just keep silent, turning to watch the pale-skinned of the room. Yourself included. Mayor Vogel looks truly shocked, his gentle eyes staring at his opponent\'s.\n\n\"We have put up with these \'people\' in our realm for too long. We Exiled them from here with good reason. I don\'t even suggest we do the same again, only that they are here at our sufferance, as a token of our peace and generosity.\n\n\"AND AS SUCH,\" he shouts over the cries of protest from the Exiles. \"They should, in times of emergency such as these, have a priority lower than we true citizens of the Empire. They can come back into this town next year.\"", eDialogPic.CREATURE, 2, ["OK"])
    result = ChoiceBox("Nash sits down, calmly. Gwyneth takes a deep breath and stands. \"Right,\" she says voice aflutter, \"Th-thank you, candidates. Now,\" She swallows, remembering her position as an independent chairperson, \"now we will take a preliminary vote.\n\n\"Understand that this is NOT the vote which will decide who will be Mayor. That comes tomorrow. This is for interest only.\"\n\n\"Now for those of you who are not familiar with the rules of voting here, I will explain them now. All of you here today over the age of 25 will be eligible to vote tomorrow.\" She writes down the names.\n\n\"That\'s 18 in all. Now, as we have just two candidates the voting system is extremely simple. Each of you will be given a stone, which you will put into one of the two pots on the table here.\" A stone is handed out to each of those present.\n\n\"Approach the table one at a time with both hands clenched, the stone in one, and open both over the pots. Put the stone in the left to vote for Vogel, right for Nash, or neither to abstain. Make sure no-one sees how you vote - this is a SECRET ballot.\"\n\n\"Right. Go for it.\" One by one, the people conceal a stone and approach the table, yourself included. How do you vote? (\'1\' for Vogel, \'2\' for Nash or \'Leave\' to abstain)", eDialogPic.CREATURE, 6, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There are six votes for our current Mayor Vogel, twelve for Nash and no abstentions.\"")
        MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")
        return
    elif result == 2:
        MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There were seven votes for our current Mayor Vogel, eleven for Nash and no abstentions.\"")
        MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")
        return
    MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There are six votes for our current Mayor Vogel, eleven for Nash and one abstention.\"")
    MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")

def RefugeSouth_1_MapTrigger_23_29(p):
    if StuffDone["0_1"] < 1:
        MessageBox("You leave the hall and spend the rest of the day trying to persuade people to vote for Vogel, to little avail. The next morning, the election is held. Nash wins by a reasonable margin. His first act as Mayor is to cast you and the other Exiles out.\n\nYou manage to eke out a feeble existence from what you and you fellow outcasts manage to forage. After a few months you succeed in secreting yourself on an outgoing ship. On to adventures new!")
        Scenario.End()
        return
    if StuffDone["0_2"] == 250:
        return
    StuffDone["0_2"] = 250
    MessageBox("OK! Time to go and - wait a minute! You suddenly realise that your hand is grasping empty air. Where\'s your staff? After the initial panic, you manage to calm yourself and mentally retrace the morning\'s steps.\n\nYou decide that you must have left it in your room when you got up. That or someone\'s stolen it. You can only hope the former, and give yourself a few punishing blows to the head. Better go and look for it (The inn\'s south).")
    StuffDone["0_4"] = 2

def RefugeSouth_3_MapTrigger_30_30(p):
    if StuffDone["0_3"] >= 1:
        return
    if StuffDone["0_3"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("OY! What do you think this is? Some kind of non-linear adventure? Or  what? Look. Just get that damned staff and stop messing about. Alright? And in future, you bloody well DO WHAT I SAY! OK?\n\n(Sorry. Temporary lapse there. That should of read as follows.) You are just about to go and explore the town a bit more when you suddenly realise that you forgot to get your staff! How stupid of you. You recall that your room is in the inn, south.")
        return

def RefugeSouth_7_MapTrigger_9_19(p):
    RunScript("GlobalCall_RefugeSouth_241", ScriptParameters(eCallOrigin.CUSTOM))
    if StuffDone["0_1"] >= 1:
        MessageBox("She frowns. \"I think we\'ve done all we can to delay the election. Now go! Use the delay! Win this town back for the people!\"\n\nShe motions you away. \"Well, go on then.\"")
        return
    if StuffDone["0_1"] < 1:
        result = ChoiceBox("\"I have just been looking through the statute books - this is an old city, which was once much more densely populated, and the number of laws that were made is amazing - it makes truly compelling reading.\" She smiles gently.\n\n\"Anyway. One of these laws concerns this very matter. Only one thing can delay an election - or at least only one appropriate to our situation - the introduction of a new candidate.\"\n\n\"If someone else decides to stand for election then four days must be allowed for that candidate to operate a campaign. It\'s the law.\" She smiles. \"That should be plenty of time for you and the Mayor\'s other supporters to turn popular opinion around.\"\n\n\"So the only problem is finding a suitable and willing candidate.\" She sits in silence for a while. She obviously expects you to volunteer, but you feel like making her spell it out. Eventually she sighs and resumes talking.\n\n\"I can\'t stand, being chairperson, and I doubt anyone else feels strongly enough about the matter to stand. Unless, of course.....?\" Looks like you\'re going to have to respond.\n\nSo what about it, hey? Fancy starting a life in politics by campaigning for your own safety? And of course in the interests of humanity and the common good. Of course. Well, offer to stand for election?", eDialogPic.CREATURE, 6, ["Stand", "Refuse"])
        if result == 0:
            MessageBox("She smiles broadly: \"Excellent! Of course, you understand that you shouldn\'t actually try to win the election. This just gives us time to change the vote.\" NOW she tells you. You were rather looking forward to being Mayor.\n\nOf course you could still try to win.....You realise that she\'s still speaking. \"...the Mayor wins.\"")
            StuffDone["0_1"] = 1
            return
        elif result == 1:
            return
        return

def RefugeSouth_13_MapTrigger_26_35(p):
    if StuffDone["0_4"] >= 1:
        if StuffDone["0_3"] < 1:
            MessageBox("You immediately rush towards your bed and rip off the sheets. Sure enough, the staff is there. You sigh in relief, taking it. How could you have been so stupid? This staff is the most valuable thing you have, all that prevents a painful, lingering death.\n\nYou feel you\'ll be needing to use it anytime soon - that murky, queasy feeling in your stomach which you have had to live with for the past twenty years is starting to well up again. (The staff is now on the special items screen. Use it when you get ill)")
            StuffDone["0_3"] = 2
            SpecialItem.Give("HealingSceptre")
            Timer(None, 290, False,  "ScenarioTimer_x_242")
            return
        if StuffDone["2_3"] == 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
            Town.PlaceEncounterGroup(1)
            if StuffDone["200_0"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Innvisitor_192": Town.NPCList.Remove(npc)
                return
            return
        if StuffDone["200_0"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Innvisitor_192": Town.NPCList.Remove(npc)
            return
        return
    if StuffDone["2_3"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
        Town.PlaceEncounterGroup(1)
        if StuffDone["200_0"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Innvisitor_192": Town.NPCList.Remove(npc)
            return
        return
    if StuffDone["200_0"] >= 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Innvisitor_192": Town.NPCList.Remove(npc)
        return

def RefugeSouth_15_MapTrigger_15_6(p):
    MessageBox("Here the floor slopes steeply, forming the method of access from the city below to the ramparts above.")
    if StuffDone["10_0"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("But you\'ve got no reason to go up there. Anyway, you think you hear movement ahead - probably a guard up there, who would maybe not take too kindly to your interference. No - better stay down here for now.")
        return

def RefugeSouth_16_MapTrigger_24_4(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,42)
    Party.MoveToMap(TownMap.List["RefugeNorth_1"])

def RefugeSouth_17_MapTrigger_24_34(p):
    if StuffDone["0_5"] == 250:
        return
    StuffDone["0_5"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(24,34))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(24,34))
    MessageBox("You look around the main room of this small inn, the only spare room of which you have been staying in for the past week or so (it\'s first on the left). It\'s pretty empty now, being day time - most people are out working.\n\nThere are a couple of out-of-towners drinking at the table, probably the last to be allowed through the city gates. The inn\'s owner, Cilla, is behind the bar, and her husband Cyril is serving.")
    MessageBox("You tell her that you are looking for your staff, and ask if anyone\'s seen it. No one answers in the positive, but Cyril looks at you oddly and asks \"Why do you always carry that thing with you? You obviously don\'t need it for support.\"\n\nYou realise you had better choose your answer carefully. To tell all these strange people here its true value could be disastrous. \"It\'s of great sentimental value, my last memento of my late father.\" you respond cunningly, if nervously.")

def RefugeSouth_18_MapTrigger_15_18(p):
    if StuffDone["0_6"] == 250:
        return
    StuffDone["0_6"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(15,18))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(15,18))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(15,18))
    MessageBox("Ah. The library. You\'ve been meaning to come in here ever since you arrived at the town a week ago, but until now hadn\'t got round to it. You can see now that this is an extremely old building - probably as old as the town itself.\n\nBut it looks like it\'s being taken good care of - the floor\'s clean if cracked, and you can see a variety of techniques have been used to cover up the holes in the crumbling walls. Indeed, it reminds you in many ways of your old home at Silvar, Exile.")

def RefugeSouth_20_MapTrigger_22_5(p):
    if StuffDone["0_7"] >= 1:
        MessageBox("You pull the lever towards you. At first it seems to be stuck, but as you strain harder you can hear the mechanism beginning to give way. Another tug and the lever accelerates towards you and hits you squarely in the chest as the portcullis crashes shut.")
        StuffDone["0_7"] = 0
        t = Town.TerrainAt(Location(24,6)).TransformTo
        Town.AlterTerrain(Location(24,6), 0, t)
        return
    MessageBox("You barely have the strength to push this lever, and it makes very slow going. As you push, you can both feel and hear the portcullis outside slowly working its way up. Once it is completely open you experimentally release the force. The mechanism holds.")
    StuffDone["0_7"] = 1
    t = Town.TerrainAt(Location(24,6)).TransformTo
    Town.AlterTerrain(Location(24,6), 0, t)

def RefugeSouth_21_MapTrigger_24_6(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["0_8"] == 250:
        return
    StuffDone["0_8"] = 250
    MessageBox("You are about to walk under this massive portcullis, but stop briefly to admire the architecture. Such a massive structure is this join between the sections of the town. The point being, you understand, is that when the place is besieged, if the -\n\nSuddenly you notice that the massive steel portcullis that separates the two sections is descending rapidly. As it crashes down you realise that, had you not been stopped by the breathtaking view, you would now by a pulpy mess skewered by hard steel.")
    MessageBox("Your senses heightened by fear, you hear cursing from the guard window to your left followed by footsteps. Once your heart has returned to its usual position in your chest you run on after this person.\n\nHe rounds the exit from the battlements before you are even halfway there and without a glance in your direction flees you behind the library. He is much faster than you and you soon give up the chase. You have no idea who it was.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(15,7))
    p.CancelAction = True
    StuffDone["10_0"] = 1
    t = Town.TerrainAt(Location(24,6)).TransformTo
    Town.AlterTerrain(Location(24,6), 0, t)

def RefugeSouth_22_MapTrigger_16_17(p):
    if StuffDone["50_1"] >= 1:
        if StuffDone["0_9"] == 250:
            return
        StuffDone["0_9"] = 250
        MessageBox("You leave the library, happy with the successful conversion of another voter, when you suddenly realise that Cornelius wasn\'t at this morning\'s meeting and so isn\'t eligible to vote. Hmmm. Better ask Gwyneth about the matter.")
        return

def RefugeSouth_25_MapTrigger_39_34(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(39,34))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(39,34))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(39,34))
    MessageBox("Hmmm. No one told you about this. The Mayor\'s job is looking better and better. Looks like this place is a perk of the job, and a very nice perk it is too. Very plush, though the ornate pillars are maybe a bit too much.")

def RefugeSouth_26_MapTrigger_13_15(p):
    MessageBox("You have a look at the books on these shadowy shelves, with the help of the candle ensconced by the door. Records. Row upon row of boring, dull, insignificant, records. A quick look at the dates reveal that they cover from about two centuries ago\n\nright up to the present day, although the earlier you go the more stuff there is. You refuse to search the shelves book by book until you find something of interest. Unless you can think of something particular to search for, you might as well leave.")
    response = InputTextBox("Enter something:", "")
    response = response[0:4].upper()
    if response == "EXIL":
        if StuffDone["1_3"] == 250:
            return
        StuffDone["1_3"] = 250
        MessageBox("You can find nothing specifically on the Exiles, but you do find records of criminal trials and judgements for various periods of the town\'s history. You take one dating from about seventy years ago, a time when they were still Exiling people.\n\n\"Mind if I borrow this?\" You call to Cornelius in the next room. \"Of course, carry on!\" He sounds surprised and pleased that someone is actually interested enough to borrow a book from the library.")
        SpecialItem.Give("Criminalrecords")
        return
    elif response == "CRIM":
        if StuffDone["1_3"] == 250:
            return
        StuffDone["1_3"] = 250
        MessageBox("You can find nothing specifically on the Exiles, but you do find records of criminal trials and judgements for various periods of the town\'s history. You take one dating from about seventy years ago, a time when they were still Exiling people.\n\n\"Mind if I borrow this?\" You call to Cornelius in the next room. \"Of course, carry on!\" He sounds surprised and pleased that someone is actually interested enough to borrow a book from the library.")
        SpecialItem.Give("Criminalrecords")
        return
    MessageBox("You have a quick look, which only confirms your suspicions that the chances of finding anything of interest on that subject on these shelves are positively anorexic.")

def RefugeSouth_27_MapTrigger_9_15(p):
    MessageBox("It hits you as soon as you open the door. That sickly sweet smell of ageing paper. It brings back long lost memories of the Tower of Magi in Exile, where you spent two years of your early life. There they had collections of books (mostly stolen).\n\nBut even there they had nothing to compare with this. You sense a great concentration of information here. You only wish you had time to absorb it in its entirety. But you don\'t. Unless you can think of something specific to look for, you should leave.")
    response = InputTextBox("Enter something:", "")
    response = response[0:4].upper()
    if response == "MAGI":
        MessageBox("A quick search DOES reveal some spell books, but you realise that it has been so long since you did any sort of magical study that it might take days to learn a new spell from a book. You put the books back.")
        return
    elif response == "SPEL":
        MessageBox("A quick search DOES reveal some spell books, but you realise that it has been so long since you did any sort of magical study that it might take days to learn a new spell from a book. You put the books back.")
        return
    MessageBox("You have a quick look, which only confirms your suspicions that the chances of finding anything of interest on that subject on these shelves are positively anorexic.")

def RefugeSouth_28_MapTrigger_34_22(p):
    MessageBox("You try to have a look through some of Mike\'s poetry, but he stops you. \"Not until their published.\" He says. Somehow you doubt that that will be happening soon.")

def RefugeSouth_29_MapTrigger_37_25(p):
    MessageBox("You take a look at a few of the titles on these shelves. \"How to be a Poet in Ten Easy Steps\". \"Cut\'n\'Paste Similes and Metaphors (Now Anyone Can be a Poet!)\". A well-thumbed dictionary. A never-thumbed Encyclopaedia Imperatus. You can bear no more.")

def RefugeSouth_30_MapTrigger_6_39(p):
    if StuffDone["1_1"] == 250:
        return
    StuffDone["1_1"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(6,39))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(6,39))
    MessageBox("Now this is a shameful sight. Tucked away in the corner of the town, hidden from common view like some facial eruption self-consciously covered by its owner\'s stray hand. From outside you could see the cracked, mouldy walls.\n\nAnd looking inside you can see that much of the floor of this ancient, shameful site is damaged or missing. Rats scurry around shadowy recesses of the place. And then, oh, you feel sick. A rat the size of which rivals Exile\'s worst lurches into view.")
    Town.PlaceNewNPC(NPCRecord.List["CaveRat_78"], Location(6,35), True)

def RefugeSouth_32_MapTrigger_24_7(p):
    if StuffDone["2_3"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
        Town.PlaceEncounterGroup(1)
        if StuffDone["200_0"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Innvisitor_192": Town.NPCList.Remove(npc)
            return
        return
    if StuffDone["200_0"] >= 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Innvisitor_192": Town.NPCList.Remove(npc)
        return

def RefugeSouth_35_MapTrigger_32_41(p):
    if StuffDone["1_5"] >= 1:
        if StuffDone["1_6"] == 250:
            return
        StuffDone["1_6"] = 250
        MessageBox("You search the South end of this dead-end alley, just where the smugglers\' entrance is meant to be, and sure enough a push of a brick, the pull of a handle reveals a narrow tunnel. You crawl into it, shutting the door behind you.")
        return
    p.CancelAction = True

def RefugeSouth_36_MapTrigger_24_28(p):
    if StuffDone["2_8"] >= 1:
        if StuffDone["10_2"] == 250:
            return
        StuffDone["10_2"] = 250
        MessageBox("You tell everyone about the Cody\'s hoarding. They seem rather less horrified than you had hoped. Nash looks like he isn\'t even bothering to listen to you - after all, what useful information could a Worm have to give?\n\nGwyneth looks faintly surprised, even perturbed, but no more. The most promising reaction is from Mayor Vogel. Not that he looks angry, but at least he speaks. \"Well, come over here and talk to me about it,\" he says.")
        return

def RefugeSouth_37_MapTrigger_6_13(p):
    RunScript("GlobalCall_RefugeSouth_246", ScriptParameters(eCallOrigin.CUSTOM))

def RefugeSouth_38_MapTrigger_28_35(p):
    RunScript("GlobalCall_RefugeSouth_243", ScriptParameters(eCallOrigin.CUSTOM))

def RefugeSouth_39_MapTrigger_37_42(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    RunScript("GlobalCall_RefugeSouth_244", ScriptParameters(eCallOrigin.CUSTOM))

def RefugeSouth_44_MapTrigger_32_43(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You look around, outside the city for the first time for over a week. Such expanses of green you\'d forgotten the beauty of. But then it\'s not safe out there. Roving bands of re-exiled Exiles, desperate and hungry.\n\nNo. You belong to the city now. You have committed yourself to preserving its Exile friendly nature, and you refuse to just leave now. You head back to the relative safety of Refuge.")

def RefugeSouth_48_MapTrigger_24_25(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["1_9"] >= 1:
        RunScript("GlobalCall_RefugeSouth_245", ScriptParameters(eCallOrigin.CUSTOM))
        if StuffDone["2_8"] >= 1:
            if StuffDone["10_2"] == 250:
                return
            StuffDone["10_2"] = 250
            MessageBox("You tell everyone about the Cody\'s hoarding. They seem rather less horrified than you had hoped. Nash looks like he isn\'t even bothering to listen to you - after all, what useful information could a Worm have to give?\n\nGwyneth looks faintly surprised, even perturbed, but no more. The most promising reaction is from Mayor Vogel. Not that he looks angry, but at least he speaks. \"Well, come over here and talk to me about it,\" he says.")
            return
        return

def RefugeSouth_49_MapTrigger_30_40(p):
    MessageBox("This chest is adorned with a large padlock. You doubt you could break it, and, prying with your mind, you find the lock too intricate for your magic to handle.")

def RefugeSouth_50_CreatureDeath0(p):
    RunScript("GlobalCall_RefugeSouth_247", ScriptParameters(eCallOrigin.CUSTOM))
    ChoiceBox("Next Nash stands up. \"Thank you, Mayor. But I think, frankly, that you hugely underestimate the situation. Yes, we\'re OK now. But the reserves are running out. Soon we will go the way of the Southern territories - children starving, dying in the streets.\n\n\"Already we are being swamped by hoards of refugees from the South. The Mayor has been forced to close the gates to all trying to get in, starting today.\" Vogel nods sadly. \"But still we won\'t all be able to make it through the coming months.\"\n\n\"Now I want to quote a statistic for you, one which should point the way forwards. There are 21 people living in this town. I calculate that there is enough food for 17 to last until next harvest. Of those 21 people, four of them come from Exile.\"\n\nThe reaction to his words is a mix of shock, fear and, in a few cases, violent approval. Most just keep silent, turning to watch the pale-skinned of the room. Yourself included. Mayor Vogel looks truly shocked, his gentle eyes staring at his opponent\'s.\n\n\"We have put up with these \'people\' in our realm for too long. We Exiled them from here with good reason. I don\'t even suggest we do the same again, only that they are here at our sufferance, as a token of our peace and generosity.\n\n\"AND AS SUCH,\" he shouts over the cries of protest from the Exiles. \"They should, in times of emergency such as these, have a priority lower than we true citizens of the Empire. They can come back into this town next year.\"", eDialogPic.CREATURE, 2, ["OK"])
    result = ChoiceBox("Nash sits down, calmly. Gwyneth takes a deep breath and stands. \"Right,\" she says voice aflutter, \"Th-thank you, candidates. Now,\" She swallows, remembering her position as an independent chairperson, \"now we will take a preliminary vote.\n\n\"Understand that this is NOT the vote which will decide who will be Mayor. That comes tomorrow. This is for interest only.\"\n\n\"Now for those of you who are not familiar with the rules of voting here, I will explain them now. All of you here today over the age of 25 will be eligible to vote tomorrow.\" She writes down the names.\n\n\"That\'s 18 in all. Now, as we have just two candidates the voting system is extremely simple. Each of you will be given a stone, which you will put into one of the two pots on the table here.\" A stone is handed out to each of those present.\n\n\"Approach the table one at a time with both hands clenched, the stone in one, and open both over the pots. Put the stone in the left to vote for Vogel, right for Nash, or neither to abstain. Make sure no-one sees how you vote - this is a SECRET ballot.\"\n\n\"Right. Go for it.\" One by one, the people conceal a stone and approach the table, yourself included. How do you vote? (\'1\' for Vogel, \'2\' for Nash or \'Leave\' to abstain)", eDialogPic.CREATURE, 6, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There are six votes for our current Mayor Vogel, twelve for Nash and no abstentions.\"")
        MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")
        return
    elif result == 2:
        MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There were seven votes for our current Mayor Vogel, eleven for Nash and no abstentions.\"")
        MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")
        return
    MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There are six votes for our current Mayor Vogel, eleven for Nash and one abstention.\"")
    MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")

def RefugeSouth_64_TalkingTrigger0(p):
    if StuffDone["0_1"] >= 1:
        p.TalkingText = "\"Thank you for what you\'re doing. With you\'re help, we have a chance.\"\n\n\"And that means that I can sleep easy at night. Well, as easy as you can in a hard wooden chair!\" She laughs humourlessly."
        return

def RefugeSouth_65_TalkingTrigger3(p):
    if StuffDone["0_1"] >= 1:
        p.TalkingText = "She frowns. \"I think we\'ve done all we can to delay the election. Now go! Use the delay! Win this town back for the people!\"\n\nShe motions you away. \"Well, go on then.\""
        return
    if StuffDone["0_1"] < 1:
        result = ChoiceBox("\"I have just been looking through the statute books - this is an old city, which was once much more densely populated, and the number of laws that were made is amazing - it makes truly compelling reading.\" She smiles gently.\n\n\"Anyway. One of these laws concerns this very matter. Only one thing can delay an election - or at least only one appropriate to our situation - the introduction of a new candidate.\"\n\n\"If someone else decides to stand for election then four days must be allowed for that candidate to operate a campaign. It\'s the law.\" She smiles. \"That should be plenty of time for you and the Mayor\'s other supporters to turn popular opinion around.\"\n\n\"So the only problem is finding a suitable and willing candidate.\" She sits in silence for a while. She obviously expects you to volunteer, but you feel like making her spell it out. Eventually she sighs and resumes talking.\n\n\"I can\'t stand, being chairperson, and I doubt anyone else feels strongly enough about the matter to stand. Unless, of course.....?\" Looks like you\'re going to have to respond.\n\nSo what about it, hey? Fancy starting a life in politics by campaigning for your own safety? And of course in the interests of humanity and the common good. Of course. Well, offer to stand for election?", eDialogPic.CREATURE, 6, ["Stand", "Refuse"])
        if result == 0:
            p.TalkingText = "She smiles broadly: \"Excellent! Of course, you understand that you shouldn\'t actually try to win the election. This just gives us time to change the vote.\" NOW she tells you. You were rather looking forward to being Mayor.\n\nOf course you could still try to win.....You realise that she\'s still speaking. \"...the Mayor wins.\""
            StuffDone["0_1"] = 1
            return
        elif result == 1:
            return
        return

def RefugeSouth_66_TalkingTrigger25(p):
    if StuffDone["50_1"] >= 2:
        p.TalkingText = "\"I\'ve already said I\'ll vote for you. How much more do you want?\"\n\n\"And if your worried about me remembering to vote, don\'t be. I\'ll make sure I don\'t miss it, I\'ll keep my ears open to news of when it will be.\""
        return
    if StuffDone["50_1"] < 1:
        return
    p.TalkingText = "He frowns. \"I thought I told you. I\'m going to vote for Vogel.\"\n\n\"And if your worried about me remembering to vote, don\'t be. I\'ll make sure I don\'t miss it, I\'ll keep my ears open to news of when it will be.\""

def RefugeSouth_67_TalkingTrigger26(p):
    if StuffDone["50_1"] >= 1:
        p.TalkingText = "\"No, my vote is decided, and I won\'t change my mind now.\""
        return
    p.TalkingText = "For some reason, you feel like telling him to vote for Nash. You tell him of the warped politician\'s policies, of his plans to effectively re-exile the Exiles. You try to sound positive, but still -\n\n\"Oh no.\" He replies, eyeing you strangely. \"I don\'t like the sound of that at all. And I don\'t see why you do, either. You said that that Vogel chap\'s standing for re-election? I\'ll vote for him.\""
    StuffDone["50_1"] = 1
    StuffDone["100_0"] += 1
    if StuffDone["100_0"] == 250:
        pass

def RefugeSouth_68_TalkingTrigger27(p):
    if StuffDone["50_1"] >= 1:
        p.TalkingText = "\"No, my vote is decided, and I won\'t change my mind now.\""
        return
    p.TalkingText = "You explain the distasteful ideas of Nash, to which he reacts with suitable fear and loathing, and explain that Nash\'s only realistic opponent is the current Mayor, Vogel.\n\n\"OK,\" He replies, \"I\'ll trust your opinion on this. From what little I know of him, Vogel seems to be a fine man. And I don\'t like the sound of this Nash at all.\""
    StuffDone["50_1"] = 1
    StuffDone["100_0"] += 1
    if StuffDone["100_0"] == 250:
        pass

def RefugeSouth_69_TalkingTrigger28(p):
    if StuffDone["50_1"] >= 1:
        p.TalkingText = "\"No, my vote is decided, and I won\'t change my mind now.\""
        return
    if StuffDone["50_1"] < 1:
        p.TalkingText = "Seeing an opportunity to grab a vote, you quickly pounce on it. You explain that although you\'ve been here only for a short time, you feel that an injection of fresh enthusiasm is just what this town needs\n\n\"Oh! I hadn\'t realised that you were running! Yes of course, my vote is yours.\" Although this doesn\'t seem like a very considered decision, you can\'t complain about the result."
        StuffDone["50_1"] = 2
        StuffDone["100_2"] += 1
        if StuffDone["100_2"] == 250:
            pass
        return
