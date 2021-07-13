
def NorthwesternWrynn_2699_MapTrigger_6_16(p):
    if StuffDone["27_8"] == 250:
        return
    StuffDone["27_8"] = 250
    WorldMap.DeactivateTrigger(Location(198,208))
    WorldMap.DeactivateTrigger(Location(199,208))
    MessageBox("Ahead is a massive chasm. The sheer cliff extends down gods know how far. The bottom is so deep that you cannot even see it. You\'re not going to be able to make it through or around this unless you can fly or something.")

def NorthwesternWrynn_2701_MapTrigger_30_36(p):
    if StuffDone["34_7"] >= 1:
        WorldMap.AlterTerrain(Location(223,228), 0, TerrainRecord.UnderlayList[4])
        if StuffDone["35_4"] == 250:
            return
        StuffDone["35_4"] = 250
        MessageBox("Following the druid\'s directions, you look into this seemingly impassible wall of forest. As you approach one area, the thick brush seems to slide away! You may now enter the Druid\'s Grove.")
        return

def NorthwesternWrynn_2703_MapTrigger_35_34(p):
    result = ChoiceBox("You approach a series of huts. Several druids are outside tending to their gardens or praying to their outdoor altars. One of them is sitting in a rocking chair, reading a book. He motions you to come over.\n\n\"Good day friends. Tis\' not often that wayfarers visit these parts, not that they are encouraged anyway. Being here means that you have been chosen by nature and your willingness to come means you seek oneness with nature.\n\nIf you have come seeking knowledge, you have come to the right place. I often take delight in teaching the arts to those worthy of this grove. Unfortunately, this grove requires gold to maintain. Not even druids are exempt from taxes!\"\n\nHe chuckles. \"My point being, there will be a small donation. However, what you shall learn will be well worth it. Interested in purchasing some of our secrets?\"", eDialogPic.CREATURE, 30, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Alchemy_Outside_6_4_4")
        p.CancelAction = True
        return

def NorthwesternWrynn_2704_MapTrigger_40_31(p):
    result = ChoiceBox("This cluster of huts has a large outdoor area where several tables have been set out. Several women are chopping up herbs at the tables. One of the elder women approaches you.\n\n\"Welcome friendly travelers! This is where we process our herbs and alchemetical ingredients and sell them at extremely reasonable rates to customers. Yes, many of the herbs for sale are available in the communal stores.\n\nHowever, these are already cut and ready for alchemetical use. Also, we have as much as you could conceivably need, where in the communal sources you are limited. Do you want to buy some alchemeticals?\"", eDialogPic.CREATURE, 29, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_8_4_4")
        p.CancelAction = True
        return

def NorthwesternWrynn_2705_MapTrigger_45_34(p):
    if Maths.Rand(1,0,100) < 20:
        if StuffDone["35_5"] == 0:
            MessageBox("You approach this collection of huts. The pastures are full of grazing gray unicorns. However, something is not right! A large collection of unicorns is in one area. You know unicorns are fairly intelligent animals.\n\nThey are also quite wild. The druids must have found some way to tame them. Unfortunately, their wild instincts have overcome their controls and they charge you! Several druids rush to assist.")
            WorldMap.SpawnNPCGroup("Group_4_4_4", p.Target)
            return
        if StuffDone["35_6"] == 0:
            result = ChoiceBox("You approach the pastures and this time are approached by a Golden Unicorn! You\'ve heard legends of this species of unicorn. Supposedly, they are quite magical and intelligent. Also, they are extremely rare and are adept at hiding.\n\nThis one, like all Golden Unicorns you have heard about, looks very friendly and speaks in gruff voice, \"Good afternoon visitors! Is it not a fine say?\" You are unsure of what to say. Should you answer him?", eDialogPic.CREATURE, 149, ["Leave", "Answer"])
            if result == 1:
                ChoiceBox("You decide to answer the Golden Unicorn. He begins to strike up conversation with you. \"I was watching back when my brutish brothers decided to attack. You behaved quite bravely and protected my friends, the Druids, quite well.\n\nIt\'s a pity that they have to be so mean all the time and it\'s even more a pity that they end up getting killed for it. Oh well, I guess they\'ll have to learn some time or another. No, they don\'t attack me at all. If they tried, I\'d give \'em a shock!\"\n\nThe unicorn jumps back and shouts a chant. A small bolt of electricity falls from the sky and strikes the ground in front of you. \"It\'ll hurt \'em a bit, but they\'ll get over it. You want to know some things?\" You say yes.\n\n\"There was one time where golden unicorns were extinct on the surface world. Do you know where we went?\" You respond, \"No.\" He answers, \"Our few survivors fled into the caves of Avernum. Not a very happy place, you know.\n\nBut wherever we went, the beauty of nature would seem to follow us. It was very dangerous down there. Eventually, some of us got fed up with those depressing caves and came back up here.\n\nAt least that\'s what my parents did. Well, my parents found this place and were cared for by the druids at the time. That was about 150 years ago. Gold unicorns live a long time you know!\"", eDialogPic.CREATURE, 149, ["OK"])
                result = ChoiceBox("\"Anyways, the druids took care of us and my parents had me and my two sisters. They are frolicking somewhere about the continent. They stop by from time to time. I often go places, but personally I prefer this grove.\n\nThese druids sure are nice, you know. They feed us and do everything for us. That\'s unlike what the humans up here used to do. They used to slaughter us and you know why?\" You ask why.\n\n\"They killed us for our horn! Not only did it make a grizzly trophy for them, but those wizards would use our horns. They\'re very magical you know. After my parents died, they gave their horns to the druids here in a gesture of friendship.\n\nThey were very grateful for this gift and did lots of good things with their horns. When I find a mate and have children and die after a few centuries, I\'m going to make sure that they\'ll get my horn too.\n\nYou know, you\'ve been very nice to talk to. I sense you do a lot of traveling and I know something that may be useful. I can teach you the special ways to find hidden herbs while traveling outdoors.\n\nIf you invest at all in alchemy, I\'m sure you will find this useful. All I ask in return is you make a donation of say, 1000 gold to my druid friends to keep this grove running. Do we have a deal, travelers?\"", eDialogPic.CREATURE, 149, ["Leave", "Accept"])
                if result == 1:
                    if Party.Gold >= 1000:
                        Party.Gold -= 1000
                        MessageBox("You produce the gold. \"Give it to one of the druids and come back here.\" You do so and the druid happily takes the donation. You return to the waiting unicorn. \"Now I\'ll need you to kneel for this.\" You kneel as he instructed.\n\nThe unicorn begins to chant. The air begins to crackle with energy. Suddenly, your entire bodies begin to glow a bright blue! Then it is all over. \"You now have the secret knowledge of finding herbs! Good luck with it. Goodbye now!\" He trots off.")
                        StuffDone["35_6"] = 1
                        RunScript("ScenarioTimer_x_2820", ScriptParameters(eCallOrigin.CUSTOM))
                        return
                    MessageBox("You don\'t have the gold. The unicorn looks kind of sad. \"I really would like to teach the skill to you, but my Druid friends really need the money. If you get it, come back here. You may find me here, then again you may not! Bye!\" He trots off.")
                    return
                MessageBox("You decline the unicorn\'s offer. He says, \"Oh well. If you change your mind, come looking back here. I may be here, but then again I may not. Do a lot of traveling myself you know. Bye!\" The unicorn trots off.")
                return
            MessageBox("You are not used to the species and are a bit frightened. You wave and back away. He yells out, \"Good day to you!\" and trots off quickly.")
            return
        MessageBox("This collection of huts has several stables surrounded by grazing pastures. However, there are not horses in the pastures. Several gray unicorns graze in the pastures and are tended to by a few druids.\n\nYou have heard that the horns of unicorns make fairly useful alchemical ingredients. It is no wonder they raise them.")
        return
    MessageBox("This collection of huts has several stables surrounded by grazing pastures. However, there are not horses in the pastures. Several gray unicorns graze in the pastures and are tended to by a few druids.\n\nYou have heard that the horns of unicorns make fairly useful alchemical ingredients. It is no wonder they raise them.")

def NorthwesternWrynn_2706_MapTrigger_38_37(p):
    result = ChoiceBox("This island contains a small outdoor shrine with a beautifully carved altar. Several flowers decorate the entire area. This place is very serene. You could easily meditate before the altar.", eDialogPic.TERRAIN, 158, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["35_7"] == 0:
            if Maths.Rand(1,0,100) < 25:
                StuffDone["35_7"] = 1
                MessageBox("You crouch before the altar and meditate. The serenity of the place seems to open your minds. Some knowledge floats into your mind during this. You rise knowing how to create \'Strong Healing Potions\'!")
                Party.LearnRecipe("strong_healing_potion")
                return
            Party.HealAll(100)
            MessageBox("You crouch before the altar and meditate. The area brings you a new kind of peace and revitalizes your mind and body! You rise reenergized!")
            for pc in Party.EachAlivePC():
                pc.SP+= 50
            return
        Party.HealAll(100)
        MessageBox("You crouch before the altar and meditate. The area brings you a new kind of peace and revitalizes your mind and body! You rise reenergized!")
        for pc in Party.EachAlivePC():
            pc.SP+= 50
        return

def NorthwesternWrynn_2707_MapTrigger_30_41(p):
    result = ChoiceBox("You approach this small collection of open huts. Inside each, potions are brewed. The Druids all direct you to the large center hut. Once inside, you are greeted by a young woman with brown hair and thick glasses.\n\nShe is behind an oak counter. The back walls are lined with potions. Most of them are quite obscure. The young woman begins, \"I suppose you came looking for some brews. Allow me to show you the selection you might like!\"\n\nDo you take a look?", eDialogPic.CREATURE, 30, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_32_4_4")
        p.CancelAction = True
        return

def NorthwesternWrynn_2708_MapTrigger_24_45(p):
    if StuffDone["35_8"] == 0:
        if Party.CountItemClass(33, False) > 0:
            result = ChoiceBox("You approach a small collection of druid huts. These are all living quarters. You notice one druid is quite frustrated. \"I can\'t seem to find that Mandrake Root anywhere! If only I remember where I put it? Do you know?\" Unfortunately, you don\'t.\n\nHowever, you just happen to have some Mandrake Root on you. You could give the root to her. It would be quite kind of you to do so. Of course, Mandrake Root is a very valuable and extremely rare ingredient that one does not part with.", eDialogPic.CREATURE, 30, ["Leave", "Give"])
            if result == 1:
                if Party.CountItemClass(33, True) > 0:
                    StuffDone["35_8"] = 1
                    MessageBox("You give her your Mandrake Root. She looks somewhat shocked. \"My that is a very druid like thing to do. Even most druids are not so giving. I must repay this act! I am not a wealthy druid, so I will share some knowledge.\"\n\nShe teaches you how to create a potion that will completely clear the mind of the drinker. You can now create the \'Potion of Clarity\'!")
                    Party.LearnRecipe("potion_of_clarity")
                    return
                return
            return
        MessageBox("You approach a small collection of druid huts. These are all living quarters. You notice one druid is quite frustrated. \"I can\'t seem to find that Mandrake Root anywhere! If only I remember where I put it? Do you know?\" Unfortunately, you don\'t.")
        return
    MessageBox("You approach a small collection of druid huts. You have a feeling these are vastly living quarters as to the lack of shops. Not much of interest to you here.")

def NorthwesternWrynn_2709_MapTrigger_35_28(p):
    if StuffDone["34_9"] == 1:
        result = ChoiceBox("Tucked away in this area is a lone hut. You knock on the door and a Witch answers it. You recognize this as the same woman who you freed back at the Nephil Bandit lair beneath Gwas! She invites you in.\n\n\"Come in, my dears! I have just made some of my famous herbal tea.\" She distributes the tea in several small cups. You take a sip and it is extremely good and energizing. \"Like it?\" You nod.\n\n\"Well, I never thought I\'d see you again! I hope you found my gift to be quite useful.\" You respond that you appreciated the gift. \"That\'s good. I didn\'t realize you were also a guest of the Druids as well. Came here looking for good deals, no doubt.\"\n\nShe thinks for a bit. \"You know, seeing your good deeds toward myself and other druids, I may be able to make a proposal to you. Are you interested?\" You nod.\n\n\"You see, I\'m one of the few druids who have the knowledge to create Skill Potions. I can teach you how to make the weaker variety, but you will need to find a stable workstation. I\'m afraid I am too busy to lend you mine.\n\nThe only other condition is a payment. The secret is priceless, but I\'m willing to teach it to you for only 3500 gold. The money will be used to support this grove, of course. Do we have a deal?\"", eDialogPic.CREATURE, 29, ["Leave", "Accept"])
        if result == 1:
            if StuffDone["120_0"] == 0:
                if Party.Gold >= 3500:
                    Party.Gold -= 3500
                    ChoiceBox("You give her the gold. She takes you into a back room and sets up the work station. You now see why this requires a stable station. Most of the equipment required is not for the casual alchemist. You will have to find such a station, but that comes later.\n\n\"Now shall we get started...\" She shows you the complicated process. It has many steps and you run through it several times. Eventually, she lets you try as she directs you through.\n\n\"Now you take the Ambrosia and add the Aelithic Acid and stir. Then run it through the filter. Now take the filtrate and add the unicorn horn which you ground earlier to a fine powder and put it over the hot plate and let it boil.\n\nSoon you should be getting a thick greenish goo. Remove the goo and add more Aelithic Acid and the Buffer, mix thoroughly and filter. Remove the filtrate and add the ember flowers and boil them in.\"\n\nThe steps proceed on and on. You go through the procedure twice and both times you fail! \"That\'s all right. It\'s a hard one to make, takes lots of practice,\" she says after both.\n\nAfter she feels confident you know the protocol, she says, \"Any work area you find worth the name will have most of the reagents. You will probably need to supply the Ambrosia, Unicorn Horn, and Ember Flowers though.\"", eDialogPic.STANDARD, 20, ["OK"])
                    StuffDone["120_0"] = 1
                    return
                MessageBox("You don\'t have the gold. \"Well, I\'m afraid I dare not sell it for any cheaper. I trust you, but I have to do my part to keep this grove going. Come back when you have the gold if you are still interested.\"")
                return
            MessageBox("\"No, no, there is no need to pay me again. I\'ll be glad to show you once more, it\'s a very difficult thing to make, after all!\" She shows you the complex method again. \"Just remember you will need Ambrosia, Ember Flowers, and a Unicorn Horn!\"")
            return
        MessageBox("You decline the offer. \"If you change your minds, be sure to come back here.\"")
        return
    MessageBox("There is a lone hut tucked away in these woods. You knock on the door, but nobody appears to be home.")

def NorthwesternWrynn_2710_WanderingOnMeet2(p):
    p.CancelAction = True
    MessageBox("You are approached by a small Nephilim patrol. Seeing you are soldiers of the Empire and more of a threat to them than they are to you, they greet you and pass on by.")

def NorthwesternWrynn_2711_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    if StuffDone["34_9"] == 1:
        result = ChoiceBox("Tucked away in this area is a lone hut. You knock on the door and a Witch answers it. You recognize this as the same woman who you freed back at the Nephil Bandit lair beneath Gwas! She invites you in.\n\n\"Come in, my dears! I have just made some of my famous herbal tea.\" She distributes the tea in several small cups. You take a sip and it is extremely good and energizing. \"Like it?\" You nod.\n\n\"Well, I never thought I\'d see you again! I hope you found my gift to be quite useful.\" You respond that you appreciated the gift. \"That\'s good. I didn\'t realize you were also a guest of the Druids as well. Came here looking for good deals, no doubt.\"\n\nShe thinks for a bit. \"You know, seeing your good deeds toward myself and other druids, I may be able to make a proposal to you. Are you interested?\" You nod.\n\n\"You see, I\'m one of the few druids who have the knowledge to create Skill Potions. I can teach you how to make the weaker variety, but you will need to find a stable workstation. I\'m afraid I am too busy to lend you mine.\n\nThe only other condition is a payment. The secret is priceless, but I\'m willing to teach it to you for only 3500 gold. The money will be used to support this grove, of course. Do we have a deal?\"", eDialogPic.CREATURE, 29, ["Leave", "Accept"])
        if result == 1:
            if StuffDone["120_0"] == 0:
                if Party.Gold >= 3500:
                    Party.Gold -= 3500
                    ChoiceBox("You give her the gold. She takes you into a back room and sets up the work station. You now see why this requires a stable station. Most of the equipment required is not for the casual alchemist. You will have to find such a station, but that comes later.\n\n\"Now shall we get started...\" She shows you the complicated process. It has many steps and you run through it several times. Eventually, she lets you try as she directs you through.\n\n\"Now you take the Ambrosia and add the Aelithic Acid and stir. Then run it through the filter. Now take the filtrate and add the unicorn horn which you ground earlier to a fine powder and put it over the hot plate and let it boil.\n\nSoon you should be getting a thick greenish goo. Remove the goo and add more Aelithic Acid and the Buffer, mix thoroughly and filter. Remove the filtrate and add the ember flowers and boil them in.\"\n\nThe steps proceed on and on. You go through the procedure twice and both times you fail! \"That\'s all right. It\'s a hard one to make, takes lots of practice,\" she says after both.\n\nAfter she feels confident you know the protocol, she says, \"Any work area you find worth the name will have most of the reagents. You will probably need to supply the Ambrosia, Unicorn Horn, and Ember Flowers though.\"", eDialogPic.STANDARD, 20, ["OK"])
                    StuffDone["120_0"] = 1
                    return
                MessageBox("You don\'t have the gold. \"Well, I\'m afraid I dare not sell it for any cheaper. I trust you, but I have to do my part to keep this grove going. Come back when you have the gold if you are still interested.\"")
                return
            MessageBox("\"No, no, there is no need to pay me again. I\'ll be glad to show you once more, it\'s a very difficult thing to make, after all!\" She shows you the complex method again. \"Just remember you will need Ambrosia, Ember Flowers, and a Unicorn Horn!\"")
            return
        MessageBox("You decline the offer. \"If you change your minds, be sure to come back here.\"")
        return
    MessageBox("There is a lone hut tucked away in these woods. You knock on the door, but nobody appears to be home.")

def NorthwesternWrynn_2712_SpecialOnWin0(p):
    MessageBox("One of the druids turns to you. \"They usually don\'t act up like that. Sometimes the beasts manage to break control of our domestication spells. Pity we had to kill them. It may have been possible to tame some of them again.\n\nOh, and have you been to the altar? It\'s out on that small island on the lake. There is a path with shallow water that you may use to get there. You should visit it, I\'m sure you will enjoy the serenity of it.\" The druids return to their work.")
    StuffDone["35_5"] = 1
