
def ImperialPalace_470_MapTrigger_31_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,5)
    Party.MoveToMap(TownMap.List["Solaria_25"])

def ImperialPalace_473_MapTrigger_37_30(p):
    p.CancelAction = True
    if StuffDone["100_1"] == 0:
        MessageBox("The guards stop you from entering. \"You do not have business with the Prime Director. He is currently meeting with important Empire officials and is unavailable. Should you have any messages for him, see his secretary.\"")
        return
    if StuffDone["100_0"] >= 5:
        if StuffDone["100_0"] >= 7:
            if StuffDone["100_0"] < 8:
                if StuffDone["55_0"] == 0:
                    ChoiceBox("The Prime Director is, once again, not pleased. Your intrusion into the Gynai Sanctuary has really caused tension between the the Empire and Gynai, and Axarus is not happy to deal with it. Nevertheless, you explain what you learned.\n\n\"Well, at least you managed to learn what is going on. Too bad you could not find out where Altrus\' main base was in time. Nevertheless, we have some leads that need to be checked out.\n\nI\'m not exactly sure what Altrus\' intentions would be. I have heard reference to this race before in tales and such. I always thought that the race was simply a myth. I guess all myths have a grain of truth to them, eh?\n\nI\'ll have to have my staff check the Archives for anything we can find on this. This will take a while, we have four archives to look through you know. From the urgent sound of that Crystal Soul, this may take too long.\n\nWe need to find out what we can as soon as possible. There may have been clues left in the three locations and need to be checked out. Your assignment is to check out the three locations.\n\nJust a reminder, they are: An abandoned mine in the Nelon Mountains, an ancient ruins in the Mandahl Mountains, and a lab in the Stolgrad Forest. If you find anything, report it immediately to me. You are now dismissed.\"", eDialogPic.CREATURE, 124, ["OK"])
                    StuffDone["55_0"] = 1
                    return
                if StuffDone["55_1"] == 1:
                    MessageBox("You report your observations of Argadon\'s Lab. The Prime Director seems interested, but he is not pleased that your search has so far turned up nothing important.")
                    StuffDone["55_1"] = 2
                    return
                if StuffDone["55_2"] == 1:
                    MessageBox("You report your observations of the mine in Nelon. The Prime Director seems interested, but he is not pleased that your search has so far turned up nothing important.")
                    StuffDone["55_2"] = 2
                    return
                MessageBox("You return to the Prime Director. He reminds you that the places you must search are: A mine in the Nelon Mountains, some ruins in the Mandahl Mountains, and an ancient lab in the Stolgrad forest.")
                return
            ChoiceBox("You return to the Prime Director with the phrase \'at the gallows\' from the Alien Bunker. The Director calls in several scholars who have previously been researching the Altrus menace. He tells them the new information.\n\nThe eldest of the scholars reports their previous findings. \"Our search of the record hall leads us to believe that the Gynai worship a race called the Vahnatai. We called upon records dating to about the ninth century.\n\nIt appears there was a war between the Empire and the rebel underworld nation known as Avernum. Somehow, the Vahnatai were harmed by the Empire. We believe some artifacts called Crystal Souls were stolen.\n\nAnyway, the Vahnatai recovered their artifacts and struck back against the Empire. Their magic was more than a match for the Imperial forces in Avernum and they were repelled. However, the struggle did not end there.\n\nThe Vahnatai created races of monsters and unleashed them on Valorim. With the help of the former enemy, Avernum, the plot was thwarted. Before they left, they pledged a horrific vengeance upon the Empire.\n\nRecords on the Vahnatai after that point are fairly scarce. However, we believe that Altrus (if he is of them) is not acting alone. The Vahnatai are a threat that must not be underestimated sir.\"", eDialogPic.CREATURE, 31, ["OK"])
            ChoiceBox("The Prime Director asks, \"What of this \'at the gallows\' thing?\" The scholars ponder. One interjects, \"It could have been referring to an execution place, perhaps an older one.\"\n\n\"Perhaps that crystal was a ploy!\" suggests another. The debate goes on focusing on popular, and deserted, places of death. Then one of the scholars suggests, \"There is a place called Gallows, Gallows Isle. A forbidden place it is.\n\nYou shant not find it on maps, yet it be there. The story of this place is a grim one. Our mages carried out experiments that would help eradicate the hostile nations during the years of conquest. The research hoped to yield a way to poison the land.\n\nPoison it, not permanently, but for a significant time. They used malevolent artifacts and metals and built machines to enhance them. The research left the island with a powerful curse. Any who stayed there would become ill and sterile.\n\nIt was determined that this method was too risky to work effectively. The isle was forgotten about and shrouded in curses. It would be the perfect place for the Vahnatai to hide for our ships do not near the isle.\n\nI believe that it is not too far off the shore north of Evergold. I believe this theory should be tested.\" The other scholars affirm this. The Director sends them out to scry the premises.", eDialogPic.CREATURE, 31, ["OK"])
            StuffDone["62_5"] = 1
            RunScript("GlobalCall_ImperialPalace_2838", ScriptParameters(eCallOrigin.CUSTOM))
            return
        if StuffDone["100_0"] < 6:
            if StuffDone["31_1"] == 1:
                StuffDone["31_1"] = 2
                ChoiceBox("You return to the Prime Director with the news that you have slain the Lich Morbane. After the usual debriefing, he rises from his chair and walks over to you.\n\n\"I must say that I am duly impressed with what you\'ve managed to do. Five times you have thwarted the efforts of that fiend who wished to take over the Empire. For this the entire Empire owes a great deal of gratitude.\n\nIn fact, I have spoken with the Emperor and he authorized me to bestow the Empire\'s highest honor upon you should you succeed. Well of course you have. Please kneel, Elite Guardians.\"\n\nHe draws a sword from a sheath he has around his belt and dubs each one of you on each shoulder. He produces a box and signals you to rise. He opens the box. Within is the Royal Seal of the Empire Dervish, one for each of you.\n\nThe seal is pinned on your uniform and he smiles. \"By the authority of Emperor Tahvan IV, I pronounce you Dervishes of the Empire. Go forth and protect your nation!\" Axarus shakes each of your hands individually and sits down.\n\n\"I really don\'t have anything else for you at this moment. You shall be summoned when I need you again. Of course, if you find anything interesting, be sure to report it to me. You are dismissed, Dervishes!\"", eDialogPic.CREATURE, 17, ["OK"])
                for pc in Party.EachAlivePC():
                    pc.AwardXP(100)
                if StuffDone["32_0"] == 1:
                    StuffDone["32_0"] = 2
                    StuffDone["100_0"] = 6
                    ChoiceBox("You report to Axarus about the strange machine you encountered in Morbane\'s lair, describing it in great detail and mentioning that mysterious Apieron. Axarus ponders for a minute.\n\n\"Interesting, Dervishes. I really don\'t like the sound of this Apieron or the machine. It is possible that we may have the next great threat on our hands. I also am apprehensive as to what this \'Dark Metal\' is as well.\n\nThe unconventional engineering of this machine sounds like something you might find in the Gynai Sector. They have very different practices than the rest of the Empire, you know.\" He sees you are a bit confused.\n\n\"Allow me to explain. Since the Aizonic Empire, the people of Gynai have been around with their strange practices. That first fallen Empire signed a non-interference treaty with them which was later agreed to by Sol I, the first ruler of this Empire.\n\nThrough the generations, the Empire has taken a long practice of not interfering with their internal affairs. They are best known for their trade of specially enhanced delicacies that only the wealthiest can afford and their crystal based artwork.\n\nThey are masters at creating impressive crystals and other things you mentioned seem to indicate their style.", eDialogPic.STANDARD, 1026, ["OK"])
                    ChoiceBox("\"Although we do not directly interfere with internal matters, we, for security reasons, send over \'guests\' and \'inspectors\' to keep an eye on day to day affairs. Last I heard, all things were going well there.\n\nOnly the Emperor or I can authorize a special pass that will allow you to visit there, as I shall do.\" He summons an aide who later returns with several silver passes. He personally signs each of the passes and stamps the Emperor\'s seal upon it.\n\nHe distributes the passes. \"These will allow you to pass into the Gynai Sector. In case you did not know, just travel north to get there. The Sector is the smallest in the Empire so you should not have too much ground to cover.\n\nI want you to go there and learn anything you can. And a word of caution. You are their guest and answerable to their laws, regulations, and customs bizarre as they may be. Disobeying them would not be advisable.\n\nI really don\'t have much else to add other than to say that I hope this lead turns up something, which there is no guarantee of. I have nothing else Dervishes, you are dismissed!\"", eDialogPic.STANDARD, 1026, ["OK"])
                    StuffDone["100_1"] = 0
                    return
                if StuffDone["24_0"] == 0:
                    ChoiceBox("After an hour delay of having to wait \"your\" turn between other bureaucrats and dignitaries, you finally get in to see the Prime Director. Upon your entry he smiles. \"I have heard of your deeds in Sorcrega. Well done! Please, be seated.\"\n\nYou sit as instructed and are debriefed. \"This Morbane character is beginning to be a real cause for concern to myself and other officials. Many of my constituents requested that something be done. I told them I had the right soldiers for the job!\"\n\nHe looks at you and grins sardonically. \"So far you have a flawless record of four victories over the lich. It\'s too bad that he had to escape the last time. You almost had him! At least now his plots in Sorcrega are stopped.\n\nMore important, to you at least, is that we have discovered that Morbane is vulnerable to sunlight! I am sure that you will figure out a way to use this to your advantage.\n\nYour next assignment is to simply locate Morbane and slay him. I know that it is crude, but I fear it is the only way to stop the menace.\" You ask him if he has any useful information.\n\n\"You are my main source of information. What you know is what I know on the subject. Sorry I can\'t tell you where he is hiding, but I have faith in you. Good luck. You are dismissed!\"", eDialogPic.CREATURE, 31, ["OK"])
                    StuffDone["24_0"] = 1
                    StuffDone["100_1"] = 0
                    return
                return
            if StuffDone["32_0"] == 1:
                StuffDone["32_0"] = 2
                StuffDone["100_0"] = 6
                ChoiceBox("You report to Axarus about the strange machine you encountered in Morbane\'s lair, describing it in great detail and mentioning that mysterious Apieron. Axarus ponders for a minute.\n\n\"Interesting, Dervishes. I really don\'t like the sound of this Apieron or the machine. It is possible that we may have the next great threat on our hands. I also am apprehensive as to what this \'Dark Metal\' is as well.\n\nThe unconventional engineering of this machine sounds like something you might find in the Gynai Sector. They have very different practices than the rest of the Empire, you know.\" He sees you are a bit confused.\n\n\"Allow me to explain. Since the Aizonic Empire, the people of Gynai have been around with their strange practices. That first fallen Empire signed a non-interference treaty with them which was later agreed to by Sol I, the first ruler of this Empire.\n\nThrough the generations, the Empire has taken a long practice of not interfering with their internal affairs. They are best known for their trade of specially enhanced delicacies that only the wealthiest can afford and their crystal based artwork.\n\nThey are masters at creating impressive crystals and other things you mentioned seem to indicate their style.", eDialogPic.STANDARD, 1026, ["OK"])
                ChoiceBox("\"Although we do not directly interfere with internal matters, we, for security reasons, send over \'guests\' and \'inspectors\' to keep an eye on day to day affairs. Last I heard, all things were going well there.\n\nOnly the Emperor or I can authorize a special pass that will allow you to visit there, as I shall do.\" He summons an aide who later returns with several silver passes. He personally signs each of the passes and stamps the Emperor\'s seal upon it.\n\nHe distributes the passes. \"These will allow you to pass into the Gynai Sector. In case you did not know, just travel north to get there. The Sector is the smallest in the Empire so you should not have too much ground to cover.\n\nI want you to go there and learn anything you can. And a word of caution. You are their guest and answerable to their laws, regulations, and customs bizarre as they may be. Disobeying them would not be advisable.\n\nI really don\'t have much else to add other than to say that I hope this lead turns up something, which there is no guarantee of. I have nothing else Dervishes, you are dismissed!\"", eDialogPic.STANDARD, 1026, ["OK"])
                StuffDone["100_1"] = 0
                return
            if StuffDone["24_0"] == 0:
                ChoiceBox("After an hour delay of having to wait \"your\" turn between other bureaucrats and dignitaries, you finally get in to see the Prime Director. Upon your entry he smiles. \"I have heard of your deeds in Sorcrega. Well done! Please, be seated.\"\n\nYou sit as instructed and are debriefed. \"This Morbane character is beginning to be a real cause for concern to myself and other officials. Many of my constituents requested that something be done. I told them I had the right soldiers for the job!\"\n\nHe looks at you and grins sardonically. \"So far you have a flawless record of four victories over the lich. It\'s too bad that he had to escape the last time. You almost had him! At least now his plots in Sorcrega are stopped.\n\nMore important, to you at least, is that we have discovered that Morbane is vulnerable to sunlight! I am sure that you will figure out a way to use this to your advantage.\n\nYour next assignment is to simply locate Morbane and slay him. I know that it is crude, but I fear it is the only way to stop the menace.\" You ask him if he has any useful information.\n\n\"You are my main source of information. What you know is what I know on the subject. Sorry I can\'t tell you where he is hiding, but I have faith in you. Good luck. You are dismissed!\"", eDialogPic.CREATURE, 31, ["OK"])
                StuffDone["24_0"] = 1
                StuffDone["100_1"] = 0
                return
            return
        return
    if StuffDone["100_0"] < 4:
        ChoiceBox("The guards stop you. \"The Prime Director is having an important discussion on trade with the Minister of the Karnold Sector of Valorim. He will see you once the meeting is over.\" You sit for about twenty minutes and are called in.\n\nYou are brought into a large and elegant office. Behind a polished marble table, sits a man in his late fifties flanked by two imposing Elite Guards. He puts his hand on his chin and nods. \"Greetings, I am Prime Director Axarus. Please be seated.\"\n\nYou sit at the table. \"First, the Empire wishes to know anything important you have learned during your quest to slay the Vampyre Halloth.\" You explain. He takes interest in your mention of Morbane, but does not comment on it. You finish.\n\n\"That is fine and well, Guardians. Now for the true matter at hand. One thing you must understand about the Empire is where the power lies. Sure in the schools they tell you the Emperor has absolute power.\n\nHowever, that is only partly true in today\'s climate. For the most part, the Empire runs itself and is dependent upon each sector to maintain stability. A defunct sector can outweigh the Emperor\'s power.\n\nYou were selected for the role of Imperial Guardians because you show promise. Thus far, our expectations of you have come to pass. Now, however, I will put you to a true test of skill.\"", eDialogPic.CREATURE, 31, ["OK"])
        ChoiceBox("I had mentioned earlier the Emperor\'s power is limited by today\'s political climate. Our intelligence informs us that the officials of the Stolgrad Sector are planning to seize the Imperial throne.\n\nNow, we could call forward an army and arrest the traitors with ease. However, the Empire only maintains its stability if all of the sectors believe they have autonomy. Our evidence, although reliable, is insufficient to prove treason.\n\nShould we take such actions, the other sectors will see this as an aggressive move. They will become more distrustful of us, as we had set a precedent of violating a sector\'s sovereignty with seemingly unjustified acts. This will lead to instability.\n\nWe cannot traverse down that slippery slope. That is why our power is limited. We could send our best Dervishes, but that would be too conspicuous. You are just perfect for this -- highly skilled, but not too famous to attract attention.\n\nYour orders are to travel to Zenith, the Capital of Stolgrad. There, you are to meet with a man who goes by the name of Vale in the \'Red Dragon Inn\'. He is our hidden set of eyes and ears in Zenith. He will give you details of the matter at hand.\n\nRemember, you are now under his command. You are to do everything possible to preempt this takeover. And at no time are you to mention this meeting to anyone!\" With that, you are escorted outside. Looks like you have a new path ahead!", eDialogPic.CREATURE, 1025, ["OK"])
        StuffDone["9_0"] = 1
        StuffDone["100_1"] = 0
        return
    ChoiceBox("The Prime Director looks up at you and narrows his eyes. He does not seem happy to see you and you know why. \"My, you\'ve caused me a great amount of trouble in the past few days. Officials round the world breathing down my neck!\"\n\nHe sighs. \"Please sit down.\" You do so and he debriefs you with a laundry list of questions. After he is through, he rises. \"You have done superb! Your deeds, although troublesome, have saved many more lives than sacrificed.\n\nWe know that you had little alternative in taking the scepter, so we forgive you. However, Vale did overstep his bounds and paid for it. But for you...\" He pauses and signals you to keel.\n\n\"By the power of the Emperor, I bestow the rank of Elite Guardian upon all of you. Please rise.\" You do so. \"Congratulations on your promotion. In fact, I have already decided on your next assignment.\n\nRecently the Sorcrega Sector, where most of the Imperial mages are trained, has been experiencing trouble. Mages have been mysteriously vanishing. Our best experts have been trying but have been unable to solve the mystery.\n\nI believe this is an excellent task for you. You are to head east and speak with the mayor of Xanthor, Miranda. She will fill you in on the details. Oh and try not to cause too much trouble this time...\"", eDialogPic.CREATURE, 31, ["OK"])
    StuffDone["17_3"] = 1
    StuffDone["17_4"] = 1
    StuffDone["100_1"] = 0

def ImperialPalace_474_MapTrigger_6_52(p):
    MessageBox("This is a statue of Ironclad I, fourth ruler of the great Empire. He succeeded his brother Sol III after he was assassinated. He led the campaigns which led to the Empire\'s global dominance.")

def ImperialPalace_475_MapTrigger_6_12(p):
    MessageBox("This is a statue of Sol I, the first Emperor. He was the first ruler who successfully united much of fractured Pralgad into what is now the Empire that spans the world. He built this palace and is regarded with the highest reverence.")

def ImperialPalace_476_MapTrigger_20_6(p):
    MessageBox("This is a statue of Odin I, often referred to as the Archmage Emperor. He rose to power during an unstable time and led the Empire into an era of peace. His magical prowess extended his lifespan making him the longest lived Emperor in history.")

def ImperialPalace_477_MapTrigger_24_6(p):
    MessageBox("This statue is of Empress Prazac I. Although there is debate as to her effectiveness as a ruler, most historians agree that her policies served to unite the world, despite the fact their true impact occurred years after her death.")

def ImperialPalace_478_MapTrigger_22_6(p):
    MessageBox("This is a statue of Frankis II.")

def ImperialPalace_479_MapTrigger_21_57(p):
    MessageBox("This is a statue of Hawthorne II. Regarded as one of the most ruthless figures in history, only to be exceeded by his heir Hawthorne III who was assassinated, he managed to drive the world through much progress and innovation.")

def ImperialPalace_480_MapTrigger_24_57(p):
    MessageBox("This is an emperor.")

def ImperialPalace_481_MapTrigger_44_41(p):
    ChoiceBox("This stairway leads quite far down into the well guarded and well refrigerated cellars of the Palace. This level is huge with crates upon crates of food, supplies, and weapons that could last an army for well over a year!\n\nYou notice in one section, workers are throwing away some of the older food and replacing it with new stocks. You wonder how often the food in these stores get replaced.\n\nOnly a small section of it is actually consumed by the members of the palace, which is usually kept fresh. The preserves are there just in case they are needed.\n\nThe Empire is well prepared to defend this city for well over a year from an all out attack if it had to. Seeing there is little to do here and you are getting frostbite from the magical coldness, you make your way back up to the first floor.", eDialogPic.STANDARD, 19, ["OK"])
    p.CancelAction = True

def ImperialPalace_482_MapTrigger_35_22(p):
    ChoiceBox("You descend these stairs and find yourselves in a large hall of records and references. Scholars and bureaucrats mill about from shelf to shelf, taking them, and putting some back.\n\nAll of these records seem quite recent, like within the past month. You wonder what happens to the records after they are a month old. Are they destroyed, or relocated somewhere else?\n\nFinding little of interest, you decide to leave this massive pile of paper to the bureaucrats.", eDialogPic.TERRAIN, 135, ["OK"])
    p.CancelAction = True

def ImperialPalace_483_MapTrigger_52_5(p):
    ChoiceBox("These stairs lead up to the second floor. The guards immediately stop you. True, the first floor is open to the public, but that only. All subsequent floors are only open to specially authorized personnel.\n\nThis is done in the name of security, above are the offices and quarters of many of the Imperial Ministers and all of their highly sensitive information.\n\nNot to mention, the Emperor Tahvan IV himself is probably somewhere up there at this time as well. There is no way that they are going to let some low level soldiers like yourselves up there without proper authorization.", eDialogPic.CREATURE, 16, ["OK"])
    p.CancelAction = True

def ImperialPalace_485_MapTrigger_55_29(p):
    result = ChoiceBox("These barracks are currently empty. There is no sign that they have been used for quite some time. You could use them to rest and recover. Also, you could store your items here if you wanted to. They would probably be safe.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        Animation_Hold(-1, 020_yawn)
        Wait()
        Party.HealAll(150)
        for pc in Party.EachAlivePC():
            pc.SP+= 80
        MessageBox("You decide to kick back and relax in the unused barracks. Unlike most other barracks you have seen, these ones are quite spacious and comfortable. You manage to get an excellent rest.")
        Party.Age += 1000
        return

def ImperialPalace_486_TalkingTrigger43(p):
    if StuffDone["100_3"] == 0:
        Sound.Play(015_cash)
        if StuffDone["100_0"] >= 6:
            p.TalkingText = "He checks his records. \"Empire Dervishes, quite impressive. It appears you are supposed to get 250 gold per diem. Here you go!\" He hands you a sack of coins."
            Party.Gold += 250
            RunScript("ScenarioTimer_x_2827", ScriptParameters(eCallOrigin.CUSTOM))
            return
        if StuffDone["100_0"] < 4:
            p.TalkingText = "He checks his records. \"Imperial Guardians, don\'t see many of them anymore. Anyway, you are assigned a payment of 50 gold per diem.\" He hands you a small sack of coins."
            Party.Gold += 50
            RunScript("ScenarioTimer_x_2827", ScriptParameters(eCallOrigin.CUSTOM))
            return
        p.TalkingText = "He checks his records. \"Elite Guardians. I suppose that will get you a salary of 100 gold per diem. Here you go!\" He hands you a sack of gold."
        Party.Gold += 100
        RunScript("ScenarioTimer_x_2827", ScriptParameters(eCallOrigin.CUSTOM))
        return
