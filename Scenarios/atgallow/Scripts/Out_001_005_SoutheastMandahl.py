
def SoutheastMandahl_2746_MapTrigger_19_32(p):
    if StuffDone["37_1"] == 250:
        return
    StuffDone["37_1"] = 250
    WorldMap.DeactivateTrigger(Location(67,272))
    WorldMap.DeactivateTrigger(Location(67,271))
    Animation_Hold(-1, 046_growl)
    Wait()
    result = ChoiceBox("Suddenly, a small band of ogres emerges. It was not a planned meeting by either side, both just kind of ran into each other. At first the ogres look kind of surprised to see you, but then they begin to talk.\n\n\"I say we smash the runts!\" says one of them. One of them retorts, \"Oh, but it might be more fun to torture them first. Then we can kill \'em!\" Another one continues, \"Yes, let\'s tear off their arms and legs!\"\n\nOne near the back replies dumbly. \"Maybe we should let them go?\" The others glare at the one who just spoke. \"Are you serious!? Look how puny they are, we could crush them in no time!\"\n\nThen another, probably the leader, speaks up, \"I say we make \'em pay us a whole bunch!\" \"Yeah boss! Good idea, but how much?\" asks one of the ogres. \"One million gold pieces!\" replies the one who first suggested that they smash you.\n\nThe leader retorts, \"Yeah right! Who do they look like, the Emperor\'s children? Now let\'s see, I think 400 gold will do!\" The others reply in agreement.\n\nThe leaders turns to you. \"Pay us 400 gold coins, no less, and we\'ll leave you alone. If you don\'t...well, we\'ll do awful things to you. Come on, decide, I don\'t have all day you know!\"", eDialogPic.CREATURE, 42, ["Pay", "Refuse"])
    if result == 0:
        if Party.Gold >= 400:
            Party.Gold -= 400
            Animation_Hold(-1, 040_thankyou)
            Wait()
            return
        MessageBox("\"What you mean you don\'t have it!? Well, this looks like your unlucky day. Smash \'em!\" The ogres grab their clubs and saunter toward you.")
        WorldMap.SpawnNPCGroup("Group_1_5_4", p.Target)
        return
    elif result == 1:
        MessageBox("You laugh at the ogres demand and respond by drawing your weapons. \"Ah, brave little fools we\'ve got today. Don\'t think they\'ll be so confident when we\'re tearing them apart! Get \'em!\"")
        WorldMap.SpawnNPCGroup("Group_1_5_4", p.Target)
        return

def SoutheastMandahl_2748_MapTrigger_24_17(p):
    result = ChoiceBox("You are at the entrance to one of the Empire\'s many mines. Care to enter and have a look around?", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        ChoiceBox("It does not take too long for the guards to figure out you don\'t belong here. Neither do you get very far so see very much. Several of the guards detain you and escort you outside.\n\n\"I\'m sorry soldiers. Nobody comes in here without authorization. The Empire does not want to risk anyone it doesn\'t have to down there, especially young soldiers like yourself. It would be a pity if there were a cave in you know.\"\n\nWell, it looks like you are not going to get to see the mines today.", eDialogPic.CREATURE, 12, ["OK"])
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheastMandahl_2750_MapTrigger_7_36(p):
    result = ChoiceBox("On the beach rests a small inn and tavern. The sign out front says: Spire Tavern & Inn -- Travelers Welcome! Lodgings and Meals at Reasonable Prices.\n\nThis looks like a good place to get a rest if tired or a bite to eat if hungry. You can imagine the inn makes a fair living as a respite out here in between towns. Anyway, the service is available if you want it.\n\nLodgings are 25 gold per night and meals are somewhat pricey.", eDialogPic.TERRAIN, 190, ["Leave", "Buy", "Rest"])
    if result == 1:
        OpenShop("Shop_Items_Outside_17_1_5")
        p.CancelAction = True
        return
    elif result == 2:
        if StuffDone["37_2"] >= 1:
            MessageBox("You mention McCuster and the deed you did for him to the owner. \"That is very kind of you. I suppose I should repay your kindness for him. After all, what are brothers for?\" You are led to your room free of charge!")
            Animation_Hold(-1, 020_yawn)
            Wait()
            Party.HealAll(125)
            MessageBox("You are given a fairly large and comfortable room. You emerge well rested after a good night\'s sleep!")
            for pc in Party.EachAlivePC():
                pc.SP+= 75
            Party.Age += 1000
            return
        if Party.Gold >= 25:
            Party.Gold -= 25
            Animation_Hold(-1, 020_yawn)
            Wait()
            Party.HealAll(125)
            MessageBox("You are given a fairly large and comfortable room. You emerge well rested after a good night\'s sleep!")
            for pc in Party.EachAlivePC():
                pc.SP+= 75
            Party.Age += 1000
            return
        MessageBox("Unfortunately, you do not have the gold. It looks like you are just going to have to camp outdoors tonight.")
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheastMandahl_2751_MapTrigger_4_18(p):
    result = ChoiceBox("There is a campfire at the summit of the hill. You wonder what anyone would be doing out here. Care to check things out?", eDialogPic.TERRAIN, 311, ["Leave", "Approach"])
    if result == 1:
        if StuffDone["37_2"] == 0:
            ChoiceBox("You reach the campsite to find four men huddled around a campfire enjoying some kind of animal. It appears to be (or have been) some kind of giant lizard. Suddenly one of them notices you and draws a sword.\n\nHe shouts, \"Who\'s there?\" You respond by saying that you are Empire soldiers. At first the man seems suspicious, but seeing your uniforms with the sword and sun insignia relieves him a bit.\n\nAnother one of the men approaches. \"You\'ll have to excuse my friend, he\'s a bit edgy at times. How rude of me, I forgot to introduce us. I am McCuster, this is Terrance, and Jacob, and I suppose you\'ve already met Derrick.\n\nIt\'s not that common that anyone, let alone soldiers comes up here. So we have to be a bit cautious. What are you doing out here, by the way?\" You respond by telling him that you are on patrol.\n\nHe nods. \"Well, we\'re up here as surveyors looking for new sites for a mine. The wizards say there might be an iron deposit here. They\'re too wimpy to come up and risk their asses, so the Empire sent us to survey the land.\n\nWe\'ve not had a good last couple of days. Both of our ropes broke! Imagine that! In all my years of doing this, I\'ve never had a rope break, let alone two of them. That setback really slows us down you know.\"", eDialogPic.CREATURE, 4, ["OK"])
            if Party.CountItemClass(24, True) > 0:
                MessageBox("He notices that you have some rope. \"Would you be willing to part with that rope?\" You decide to give him the rope. \"Thank you friends! I really should repay you, but none of us have anything of value right now you understand.\"\n\nJust as you are leaving. \"Hey! It\'s not much but if you stop by the Spire Inn be sure to mention my name. That\'s McCuster in case you\'ve forgotten. My brother\'s the owner, I\'m sure he\'ll let you stay for free.\"")
                StuffDone["37_2"] = 1
                return
            MessageBox("\"Well I suppose you should get going right now. I think we can fend for ourselves. Thanks though! It was nice chattin\'. Oh and if you find some rope lying around, be sure to bring some here. We\'d really appreciate it!\" You descend the hill.")
            return
        MessageBox("You return to the surveyors campsite to find it vacant. They must be out doing their work. Oh well, perhaps you should come back later.")
        return

def SoutheastMandahl_2752_MapTrigger_14_30(p):
    if StuffDone["37_3"] == 250:
        return
    StuffDone["37_3"] = 250
    WorldMap.DeactivateTrigger(Location(62,270))
    Animation_Hold(-1, 060_smallboom)
    Wait()
    Animation_Hold(-1, 060_smallboom)
    Wait()
    Animation_Hold(-1, 060_smallboom)
    Wait()
    WorldMap.AlterTerrain(Location(61,270), 0, TerrainRecord.UnderlayList[37])
    WorldMap.AlterTerrain(Location(62,270), 0, TerrainRecord.UnderlayList[37])
    WorldMap.AlterTerrain(Location(63,270), 0, TerrainRecord.UnderlayList[37])
    MessageBox("Traveling in the mountains is never without risk. That fact is proven by the recent rockslide. It\'s a pity you were caught in the middle of it! Perhaps you should have stayed not strayed from the beaten path today.")
    Party.Damage(Maths.Rand(6, 1, 5) + 10, eDamageType.WEAPON)
    Wait()

def SoutheastMandahl_2753_MapTrigger_32_24(p):
    if StuffDone["37_4"] == 250:
        return
    StuffDone["37_4"] = 250
    WorldMap.DeactivateTrigger(Location(80,264))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("Suddenly you run into a small group of people in dark red robes. You have just encountered more of those cultists! They look kind of surprised to see you and you are kind of surprised to see them out here too.\n\nAnyway, they aren\'t going to come peacefully.", eDialogPic.CREATURE, 23, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_5_5", p.Target)

def SoutheastMandahl_2754_MapTrigger_10_5(p):
    result = ChoiceBox("In the center of the plain lies a crumbling ruin. It appears to have been some kind of fortress. The main entrance portculli are closed, but the walls are crumbling. It does not look like anyone has been here for quite some time.\n\nDo you enter and look around hoping the place is not trapped or haunted?", eDialogPic.TERRAIN, 189, ["Leave", "Enter"])
    if result == 1:
        ChoiceBox("You enter the ruins expecting the worst. After a thorough investigation, however, you are convinced that the fortress is completely safe. So, you decide to take a closer look.\n\nYou were correct about your guess from outside. This is, or was, indeed a fortress. How long ago it was abandoned is yet unclear. From the signs that are still intact, you learn that many of the large storage spaces are used for ore.\n\nIt is quite likely then, that this fortress was used long ago to coordinate the mining efforts in the vicinity. Eventually, you make it to the administration and discover an archive containing records of the fort\'s activity.\n\nThe archive room is lined with bookshelves filled with thick volumes of records. Some of the labels are still legible. All that you can read at least are administrative reports of the fortress.\n\nYou decide to go to the bookshelf furthest to the back which is ironically dated the earliest. You open it up and read the first entry. It is by a certain Bladesman Wayne and dated Suncome 4, 488 IE.\n\nThese records are nearly a thousand years old and still mostly intact! The archive hall must have not been disturbed for a really, really long time.", eDialogPic.TERRAIN, 135, ["OK"])
        ChoiceBox("The first entry reads: \"There is really no way to begin one of these but by offering an introduction. This is the first official day of business for Fort Antross. I and many of the soldiers arrived early this morning.\n\nRight now all that is completed is the barracks and the administrative sections. However, the soldiers are rapidly working on building several store rooms which will be used to house ore once mining operations begin sometime next month.\n\nOf course, quarters for the miners and all the basic necessities will have to be ready for that time. However, much of our efforts must be spent putting up the protective wall. These mountains are filled with treacherous wild beasts.\n\nBut for now we will have to rely on sentries during the night to keep watch. It shall be a daunting task to have all of this completed in 45 days, when the miners are to arrive, with so little help.\n\nI was a bit skeptical when I was moved up to here. I was also a bit disappointed, believing that a promotion to Bladesman would be a bit more rewarding. Now I have arid terrain and bitter winters to face.\n\nHowever, I must admit that I have come to see this as an adventure. Sure it\'s not as exciting as it could be, but I can swallow it. I guess it\'s time to do the reporting.\" It continues with a report of tasks done and goods used during the day.", eDialogPic.TERRAIN, 135, ["OK"])
        ChoiceBox("You flip through a few more of the entries. Eventually the creative comments begin to disappear and are replaced by the everyday administrative reporting and recordkeeping.\n\nYou now have a good idea of what this place was for, but now to see what became of it. You go to the opposite end of the room and find the most recent book. The final entry is dated Leafloss, 2 777 IE by a Bladesman Archerwood.\n\n\"Four more days would have marked the fourteenth anniversary of my arrival at this place. However, that jubilee is never to be reached. This is the last official day of operations for Fort Antross.\n\nAs I am writing this, my soldiers are going through the final check for anything left. I don\'t expect them to turn anything up, I ran through the routine this morning. Everything of value has been loaded onto the carts.\n\nIn only a couple of hours, the gates shall be closed for the final time and the fort sealed forever. This record will remain here until somebody in the future arrives to read it.\n\nEven before my arrival here, the mines began to produce less than desired. They were running dry as all mines do eventually. Efforts to locate new sources of metal or gems have been fruitless, so the Empire declared the mines closed.", eDialogPic.TERRAIN, 135, ["OK"])
        ChoiceBox("\"The miners, and many of my men, left about two months ago. It was definitely sad to see them go. All that remains is my skeleton crew of eight soldiers who have held down the fort and prepared it for closing.\n\nThe days have been strictly business and the nights have been much quieter. Sure the remaining ones and I had fun times, but it could not match the days when the rest were still around.\n\nIt is now almost ten o\'clock in the morning and we will not be returning to Damasnica until very late. I have heard that new mining techniques have allowed several new mines to be set up way over in Vantanas.\n\nRumors say that I may be considered for the position of commanding one. But, that is uncertain. All that is certain is that this chapter of my life, along with this fort, is forever closed.\" The passage is signed and there is nothing more.\n\nThis area must have once been a very rich source of minerals. From the notes you gather that mostly iron was mined here. However, there were a few gemstone veins found, albeit not many.\n\nThe mines were plundered for just under two centuries before they ran dry. Perhaps if you look around the surrounding mines, you may find something that was missed. There is little else in this fort, so you leave.", eDialogPic.TERRAIN, 135, ["OK"])
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheastMandahl_2755_MapTrigger_14_6(p):
    result = ChoiceBox("You are at the entrance to one of the Empire\'s many mines. Care to enter and have a look around?", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        MessageBox("This mine has been closed for a very long time. Many of the passages have already caved in. Your search finds not a single thing of value. Anything of value must have been taken a long time ago.")
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheastMandahl_2757_MapTrigger_21_3(p):
    result = ChoiceBox("You are at the entrance to one of the Empire\'s many mines. Care to enter and have a look around?", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["38_2"] == 0:
            StuffDone["38_2"] = 1
            Animation_Hold(-1, 046_growl)
            Wait()
            MessageBox("This mine was closed a long time ago, but is not uninhabited unfortunately. The new residents are a large number of wild giant lizards, many of them the fire breathing variety. They look pleased to see you, even though the feeling is not mutual.")
            WorldMap.SpawnNPCGroup("Group_1_5_6", p.Target)
            return
        MessageBox("This mine has been closed for a very long time. Many of the passages have already caved in. Your search finds not a single thing of value. Anything of value must have been taken a long time ago.")
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheastMandahl_2758_MapTrigger_43_27(p):
    if StuffDone["100_0"] >= 2:
        MessageBox("This is the border separating the Agran Sector from the Mandahl Sector. You present your papers and are allowed to proceed.")
        return
    MessageBox("This is the border separating the Agran Sector from the Mandahl Sector. Travel between the sectors is restricted, even to soldiers. You will need special permission to cross this border.")
    p.CancelAction = True

def SoutheastMandahl_2759_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    result = ChoiceBox("In the center of the plain lies a crumbling ruin. It appears to have been some kind of fortress. The main entrance portculli are closed, but the walls are crumbling. It does not look like anyone has been here for quite some time.\n\nDo you enter and look around hoping the place is not trapped or haunted?", eDialogPic.TERRAIN, 189, ["Leave", "Enter"])
    if result == 1:
        ChoiceBox("You enter the ruins expecting the worst. After a thorough investigation, however, you are convinced that the fortress is completely safe. So, you decide to take a closer look.\n\nYou were correct about your guess from outside. This is, or was, indeed a fortress. How long ago it was abandoned is yet unclear. From the signs that are still intact, you learn that many of the large storage spaces are used for ore.\n\nIt is quite likely then, that this fortress was used long ago to coordinate the mining efforts in the vicinity. Eventually, you make it to the administration and discover an archive containing records of the fort\'s activity.\n\nThe archive room is lined with bookshelves filled with thick volumes of records. Some of the labels are still legible. All that you can read at least are administrative reports of the fortress.\n\nYou decide to go to the bookshelf furthest to the back which is ironically dated the earliest. You open it up and read the first entry. It is by a certain Bladesman Wayne and dated Suncome 4, 488 IE.\n\nThese records are nearly a thousand years old and still mostly intact! The archive hall must have not been disturbed for a really, really long time.", eDialogPic.TERRAIN, 135, ["OK"])
        ChoiceBox("The first entry reads: \"There is really no way to begin one of these but by offering an introduction. This is the first official day of business for Fort Antross. I and many of the soldiers arrived early this morning.\n\nRight now all that is completed is the barracks and the administrative sections. However, the soldiers are rapidly working on building several store rooms which will be used to house ore once mining operations begin sometime next month.\n\nOf course, quarters for the miners and all the basic necessities will have to be ready for that time. However, much of our efforts must be spent putting up the protective wall. These mountains are filled with treacherous wild beasts.\n\nBut for now we will have to rely on sentries during the night to keep watch. It shall be a daunting task to have all of this completed in 45 days, when the miners are to arrive, with so little help.\n\nI was a bit skeptical when I was moved up to here. I was also a bit disappointed, believing that a promotion to Bladesman would be a bit more rewarding. Now I have arid terrain and bitter winters to face.\n\nHowever, I must admit that I have come to see this as an adventure. Sure it\'s not as exciting as it could be, but I can swallow it. I guess it\'s time to do the reporting.\" It continues with a report of tasks done and goods used during the day.", eDialogPic.TERRAIN, 135, ["OK"])
        ChoiceBox("You flip through a few more of the entries. Eventually the creative comments begin to disappear and are replaced by the everyday administrative reporting and recordkeeping.\n\nYou now have a good idea of what this place was for, but now to see what became of it. You go to the opposite end of the room and find the most recent book. The final entry is dated Leafloss, 2 777 IE by a Bladesman Archerwood.\n\n\"Four more days would have marked the fourteenth anniversary of my arrival at this place. However, that jubilee is never to be reached. This is the last official day of operations for Fort Antross.\n\nAs I am writing this, my soldiers are going through the final check for anything left. I don\'t expect them to turn anything up, I ran through the routine this morning. Everything of value has been loaded onto the carts.\n\nIn only a couple of hours, the gates shall be closed for the final time and the fort sealed forever. This record will remain here until somebody in the future arrives to read it.\n\nEven before my arrival here, the mines began to produce less than desired. They were running dry as all mines do eventually. Efforts to locate new sources of metal or gems have been fruitless, so the Empire declared the mines closed.", eDialogPic.TERRAIN, 135, ["OK"])
        ChoiceBox("\"The miners, and many of my men, left about two months ago. It was definitely sad to see them go. All that remains is my skeleton crew of eight soldiers who have held down the fort and prepared it for closing.\n\nThe days have been strictly business and the nights have been much quieter. Sure the remaining ones and I had fun times, but it could not match the days when the rest were still around.\n\nIt is now almost ten o\'clock in the morning and we will not be returning to Damasnica until very late. I have heard that new mining techniques have allowed several new mines to be set up way over in Vantanas.\n\nRumors say that I may be considered for the position of commanding one. But, that is uncertain. All that is certain is that this chapter of my life, along with this fort, is forever closed.\" The passage is signed and there is nothing more.\n\nThis area must have once been a very rich source of minerals. From the notes you gather that mostly iron was mined here. However, there were a few gemstone veins found, albeit not many.\n\nThe mines were plundered for just under two centuries before they ran dry. Perhaps if you look around the surrounding mines, you may find something that was missed. There is little else in this fort, so you leave.", eDialogPic.TERRAIN, 135, ["OK"])
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheastMandahl_2760_SpecialOnWin1(p):
    MessageBox("The cultists are beaten. You wonder what they were doing out in these hills.")

def SoutheastMandahl_2761_SpecialOnWin2(p):
    MessageBox("With the fire lizards gone. You search through the mine. It seems that in one of the lizard\'s nests is a small emerald! A further investigation reveals little else.")
    Party.GiveNewItem("Emerald_179")
