
def RefugeSouthnight_109_MapTrigger_25_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["0_0"] == 250:
        return
    StuffDone["0_0"] = 250
    MessageBox("Just as you open the door, you see the innkeeper, NAME, just about to knock from the other side. \"Come on!\" She says. \"We\'ve all been called to the town hall.\" Seeing your expression of confususion, she elucidates.\n\n\"Don\'t you know? It\'s the election tomorrow. This is something to do with that. Now come on.\" You run on after her to the town hall.")
    StuffDone["100_0"] = 6
    StuffDone["100_1"] = 10
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(24,27))
    p.CancelAction = True
    MessageBox("The town hall is completely packed. It looks like everyone from the town is here. They nod happily to you and NAME as you enter. The hall has been completely rearranged for the occasion - guards surround a bench in the centre on which are two pots.\n\nBehind that sits Gwyneth, who runs the potion shop. To her left is Mayor Vogel, and to her right is Nash - someone whom you know to be Exile-hater, however polite. As the last file in, Gwyneth claps her hands loudly to call attention to her.")
    MessageBox("\"As you probably all know, tomorrow we will be holding the election for Mayor. I, who have voluntered to oversee the proceedings, have called you all here today to allow the candidates to each give a short speech on their suitablity as Mayor.\"\n\n\"After these, we will hold a brief mock election. This will give you practice in the process, ensuring no mishaps tomorrow, and will let us see how things are shaping up. OK? Right. First up, our current Mayor, Vogel.\"")
    MessageBox("Mayor Vogel stands up, still wearing his sash of office. \"Hello, my citizens.\" He smiles. \"Right. My case is pretty simple. I have served as your Mayor for four years now, and I would like to think that I\'ve done a good job.\" cheers from the audience.\n\n\"And as far as I\'m concerned, there is no reason to change now. OK, I know we\'ve got a bit of a food problem, but I\'m sure that if we all pull together and eat no more than we need then we should be alright. Ummm, well that\'s it really.\" Mild applause.")
    MessageBox("Next Nash stands up. \"Thank you, Mayor. But I think, frankly, that you hugely underestimate the situation. Yes, we\'re OK now. But the reserves are running out. Soon we will go the way of the Southern territories - children starving, dying in the streets.\n\n\"Already we are being swamped by hoardes of refugees from the South. The Mayor has been forced to close the gates to all trying to get in, starting today.\" Vogel nods sadly. \"But still we won\'t all be able to make it through the coming months.\"")
    MessageBox("\"Now I want to quote a statistic for you, one which should point the way forwards. There are 20 people living in this town. I calculate that there is enough food for 16 to last until next harvest. Of those 20 people, four of them come from Exile.\"\n\nThe reaction to his words is a mix of shock, fear and, in a few cases, violent approval. Most just keep silent, turning to watch the pale-skinned of the room. Yourself included. Mayor Vogel looks truly shocked, his gentle eyes staring at his opponent\'s.")
    MessageBox("\"We have put up with these \'people\' in our realm for too long. We Exiled them from here with good reason. I don\'t even suggest we do the same again, only that they are here at our sufference, as a token of peace and genorosity.\n\n\"AND AS SUCH,\" he shouts over the cries of protest from the Exiles, \"they should, in times of emergency such as these, have a priority lower than we true citizens of the Empire. They can come back into this town next year.\"")
    result = ChoiceBox("Nash sits down, calmly. Gwyneth takes a deep breath and stands. \"Right,\" she says voice aflutter, \"Th-thankyou, candidates. Now,\" She swallows, remembering her position as an independent chairperson, \"now we will take a preliminary vote.\n\n\"Understand that this is NOT the vote which will decide who will be Mayor. That comes tomorrow. This is for interest only.\"\n\n\"Now for those of you who are not familiar with the rules of voting here, I will explain them now. All of you here today over the age of 25 will be eligible to vote tomorrow.\" She writes down the names.\n\n\"That\'s 18 in all. Now, as we have just two candidates the voting system is extremely simple. Each of you will be given a stone, which you will put into one of the two pots on the table here.\" A stone is handed out to each of those present.\n\n\"Approach the table one at a time with both hands clenched, the stone in one, and open both over the pots. Put the stone in the left to vote for Vogel, right for Nash, or neither to abstein. Make sure no-one sees how you vote - this is a SECRET ballot.\"\n\n\"Right. Go for it.\" One by one, the people conceal a stone and approach the table, yourself included. How do you vote? (\'1\' for Vogel, \'2\' for Nash or \'Leave\' to abstein)", eDialogPic.CREATURE, 8, ["Leave", "1", "2"])
    if result == 1:
        MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There were seven votes for our current Mayor Vogel, ten for Nash and one abstention.\"")
        MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")
        return
    elif result == 2:
        MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There are six votes for our current Mayor Vogel, eleven for Nash and one abstention.\"")
        MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")
        return
    MessageBox("After everyone has voted, the votes are counted while everyone watches to ensure no foul play. The result is whispered to Gwyneth for her to announce. She blinks rapidly and takes a deep breath before announcing :\n\n\"There are six votes for our current Mayor Vogel, ten for Nash and two abstentions.\"")
    MessageBox("You feel sick. A hole deep in the heart of your stomach. You can\'t believe it\'s happening AGAIN! But no. You are determined. This time you won\'t LET it happen. You\'ll convince them.\n\nBut just one day. Just one.....the chances are slim, but not non-existent. Everyone files out of the hall leaving just you, Gwyneth, Vogel and Nash. Probably best to start by talking to them.")

def RefugeSouthnight_110_MapTrigger_23_29(p):
    if StuffDone["0_1"] < 1:
        MessageBox("You leave the hall and spend the rest of the day trying to persuade people to vote for Vogel, to little avail. The next morning, the election is held. Nash wins by a reasonable margin. His first act as Mayor is to cast you and the other Exiles out.\n\nYou manage to eek out a feeble existence from what you and you fellow outcasts manage to forage. After a few months you succeed in secreting yourself on an outgoing ship. On to adventures new!")
        Scenario.End()
        return
    if StuffDone["0_2"] == 250:
        return
    StuffDone["0_2"] = 250
    MessageBox("OK! Time to go and - wait a minute! You suddenly realise that your hand is grasping empty air. Where\'s your staff? After the initial panic, you manage to calm yourself and mentally retrace the morning\'s steps.\n\nYou decide that you must have left it in your room when you got up. That or someone\'s stolen it. You can only hope the former, and give yourself a few punishing blows to the head. Better go and look for it (The inn\'s south).")
    StuffDone["0_4"] = 2

def RefugeSouthnight_112_MapTrigger_30_30(p):
    if StuffDone["0_3"] >= 1:
        return
    if StuffDone["0_3"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("OY! What do you think this is? Some kind of non-linear adventure? Or  what? Look. Just get that damned staff and stop messing about. Alright? And in future, you bloody well DO WHAT I SAY! OK?\n\n(Sorry. Temporary lapse there. That should of read as follows.) You are just about to go and explore the town a bit more when you suddenly realise that you forgot to get your staff! How stupid of you. You recall that your room is in the inn, south.")
        return

def RefugeSouthnight_122_MapTrigger_26_35(p):
    if StuffDone["0_4"] >= 1:
        if StuffDone["0_3"] < 1:
            MessageBox("You immediately rush towards your bed and rip off the sheets. Sure enough, the staff is there. You sigh in relief, taking it. How could you have been so stupid? This staff is the most valuable thing you have, all that prevents a painful, lingering death.\n\nYou feel you\'ll be needing to use it anytime soon - that murky, queasy feeling in your stomach which you have had to live with for the past twenty years is starting to well up again. (The staff is now on the special items screen. Use it when you get ill)")
            StuffDone["0_3"] = 2
            SpecialItem.Give("HealingSceptre")
            return
        return

def RefugeSouthnight_124_MapTrigger_15_6(p):
    MessageBox("Here the floor slopes steeply, forming the method of access from the city below to the ramparts above.")

def RefugeSouthnight_126_MapTrigger_24_34(p):
    if StuffDone["0_5"] == 250:
        return
    StuffDone["0_5"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(24,34))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(24,34))
    MessageBox("You look around the main room of this small inn, the only spare room of which you have been staying in for the past week or so (it\'s first on the right). It\'s pretty empty now, being day time - most people are out working.\n\nThere are a few out-of-towners here, probably the last to be allowed through the city gates. The inn\'s owner, Cilla, is behind the bar, and her husband Cyril is serving. You ask if anyone\'s seen your staff.")
    MessageBox("You tell her that you are looking for your staff, and ask if anyones seen it. No one answers in the positive, but Cyril looks at you oddly and asks \"Why do you always carry that thing with you? You obviously don\'t need it for support.\"\n\nYou realise you had better choose your answer carefully. To tell all these strange people here its true value could be disasterous. \"It is of great sentimental value, my last momento of my late father.\" you respond cunningly, if nervously.")

def RefugeSouthnight_127_MapTrigger_15_18(p):
    if StuffDone["0_6"] == 250:
        return
    StuffDone["0_6"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(15,18))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(15,18))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(15,18))
    MessageBox("Ah. The library. You\'ve been meaning to come in here ever since you arrived at the town a week ago, but until now hadn\'t got round to it. You can see now that this is an extremely old building - probably as old as the town itself.\n\nBut it looks like it\'s being taken good care of - the floor\'s clean if cracked, and you can see a variety of techniques have been used to cover up the holes in the crumbling walls. Indeed, it reminds you in many ways of your old home at Silvar, Exile.")

def RefugeSouthnight_129_MapTrigger_22_5(p):
    if StuffDone["0_7"] >= 1:
        MessageBox("You barely have the strengh to push this lever, and it makes very slow going. As you push, you can both feel and hear the portcullus outside slowly working its way up. Once it is completely open you experimentally release the force. The mechanism holds.")
        StuffDone["0_7"] = 0
        t = Town.TerrainAt(Location(24,6)).TransformTo
        Town.AlterTerrain(Location(24,6), 0, t)
        return
    MessageBox("You pull the lever towards you. At first it seems to be stuck, but as you strain harder you can hear the mechanism beginning to give way. Another tug and the lever accelerates towards you and hits you squarely in the chest as the portcullus crashes shut.")
    StuffDone["0_7"] = 1
    t = Town.TerrainAt(Location(24,6)).TransformTo
    Town.AlterTerrain(Location(24,6), 0, t)

def RefugeSouthnight_130_MapTrigger_24_6(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["0_8"] == 250:
        return
    StuffDone["0_8"] = 250
    MessageBox("You are about to walk under this massive portcullis, but stop briefly to admire the architecture. Such a massive structure is this join between the sections of the town. You understand that the point is that, when the place is besieged, if the -\n\nSuddenly you realise that the massive steel portcullis that seperates the two sections is descending rapidly. As it crashes down you realise that, had you not been stopped by the breathtaking view, you would now by a pulpy mess skewered by hard steel.")
    MessageBox("Your senses heightened by fear, you hear cursing from the guard window to your left followed by footsteps. Once your heart has returned to its usual position in your chest you run on after this person.\n\n He rounds the exit from the battlements before you are even halfway there and without a glance in your direction flees you behind a building. He is much faster than you and you soon give up the chase. You have no idea who it was.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(15,7))
    p.CancelAction = True

def RefugeSouthnight_131_MapTrigger_16_17(p):
    if StuffDone["50_1"] >= 1:
        if StuffDone["0_9"] == 250:
            return
        StuffDone["0_9"] = 250
        MessageBox("You leave the library, happy with the successful conversion of another voter, when you suddenly realise that Cornelius wasn\'t at this morning\'s meeting and so isn\'t elegible to vote. Hmmm. Better ask Gwyneth about the matter.")
        return

def RefugeSouthnight_134_MapTrigger_39_34(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(39,34))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(39,34))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(39,34))
    MessageBox("Hmmm. No one told you about this. The Mayor\'s job is looking better and better. Looks like this place is a perk of the job, and a very nice perk it is too. Very plush, though the ornate pillars are maybe a bit too much.")

def RefugeSouthnight_135_MapTrigger_13_15(p):
    MessageBox("You have a quick look at the books on these shadowy shelfs with the help of the candle ensconced by the door. Records. Row upon row of boring, dull, insignificant, records. A quick look at the dates reveal that they cover from about two centuries ago\n\nright up to the present day, although the earlier you go the more stuff there is. Still, there seems little point in searching the shelves more thoroughly - you really don\'t have the time or energy.")

def RefugeSouthnight_136_MapTrigger_9_15(p):
    MessageBox("It hits you as soon as you open the door. That sickly sweet smell of ageing paper. It brings back long lost memories of the Tower of Magi in Exile, where you spent two years of your early life. There they had collections of books, mostly stolen from the\n\nBut even there they had nothing to compare with this. You sense a great concentration of information here. You only wish you had time to absorb it in its entirety. But you don\'t. Unless you can think of something specific to look for, you should leave.")
    response = InputTextBox("Enter something:", "")
    response = response[0:0].upper()
