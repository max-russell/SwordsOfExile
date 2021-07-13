
def SouthwestMandahl_2727_MapTrigger_35_31(p):
    if StuffDone["37_5"] == 250:
        return
    StuffDone["37_5"] = 250
    WorldMap.DeactivateTrigger(Location(35,271))
    WorldMap.DeactivateTrigger(Location(36,271))
    ChoiceBox("You have reached the entrance to the famed Raven Naval Base. Being soldiers, the guards let you through the main gate leading into the small \"town\" for the sailor\'s families. The actual base is still further south.\n\nIn the early days of the Empire, its Naval fleets were legendary. The Empire always had the fastest, sturdiest, and most powerful ships in the world. The genius of the Naval engineers and architects outclassed all others in the world.\n\nHowever, when the Empire managed to slay all of its rivals, the importance of Naval power feel dramatically. Funding for new warships was cut and the once bulging budget of the Imperial Navy shrunk considerably.\n\nMuch of this military budget was transferred to the Army, your division. Holding the Empire\'s possessions was, and still is, the duty of the ground forces. No other nations that could challenge the Empire\'s Naval supremacy existed anymore.\n\nSo the Navy, much to the discontent of the Naval Dervishes, was vastly disbanded. Many bases were abandoned and ships dismantled. There are only five major Naval bases left in the world. Two on Pralgad, and one each on the other continents.\n\nToday the Navy is used for three things: Ceremonial occasions, a symbol of the Empire\'s authority, and transport of goods and men when teleporters prove uneconomical.", eDialogPic.STANDARD, 16, ["OK"])

def SouthwestMandahl_2729_MapTrigger_35_37(p):
    ChoiceBox("The gates of the Naval Base are well defended by about ten burly guards. They ask to see your authorization and, of course, you are unable to oblige.\n\n\"Sorry soldiers, not even the army can get into this fine Naval Base without authorization.\" One of guards says. He said the word army with a bit of bitterness. There has always been a rivalry between Navy and Army.\n\nThis bitterness had become quite strong and remained so since centuries ago, when the Empire\'s legitimate enemies were defeated and the Navy became obsolete.\n\nIn fact, there is an old army joke about the Navy that goes something like this, \"There are two kinds of Naval Recruits: The first are the children of the older officers and the second are the rejects of from the Army Recruiting Office.\"\n\nIn part, this stigma is true. The Naval ranks have become vastly hereditary and the Naval Recruiting Office has standards much lower than the Army\'s. This is so, partly because of the lack of resources for training.\n\nAnyway, it does not look like you are going to get in here.", eDialogPic.CREATURE, 12, ["OK"])
    p.CancelAction = True

def SouthwestMandahl_2731_MapTrigger_37_33(p):
    if StuffDone["37_6"] == 0:
        ChoiceBox("You enter a fairly large tavern where sailors on shore leave would come to drink and make merry. There is a large number of sailors near the bar who are obviously drunk. One of them recognizes your uniforms as of the Army and takes offense.\n\n\"What are a bunch of Boot-Licking Army men doin\' in our tavern. If I didn\'t know right from wrong I\'d knock your teeth out!\" You try to ignore the obvious insult, but the other boozed up sailors do not want to let it go.\n\n\"Yeah what do ya think you\'re doin\' on our turf! Go back to Army Land where you belong!\" As you approach the bar and take a seat, one of the discontented men shoves you down onto the floor.\n\n\"Take that Army scum!\" he yells. \"What don\'t want to fight? Army make you soft!? Join the Navy! It\'ll toughen ya up!\" The sailors are really edging for a combat, one of them grabs a bottle and smashes it on the counter.\n\n\"Ready for some of this, huh?\" He swings the bottle at you. You have no choice but to push him to the ground. At this, many of the sailors become quite quarrelsome. \"Who does those Army freaks think they are? Comin\' into our bar and shovin\' us around!\"\n\nFinally, the truce finally decays and one lunges toward you. You easily knock him out, but now you\'ve got the others on you hands!", eDialogPic.CREATURE, 13, ["OK"])
        WorldMap.SpawnNPCGroup("Group_0_5_4", p.Target)
        return
    result = ChoiceBox("You return to the tavern. The place has quieted down a bit since your last visit. You are immediately tended to by the bartender.\n\n\"Visiting the base are we? That was some impressive fighting earlier. The army trained you well, I should know!\" He winks. \"Keep it under the tongue, all right. All the sailors think I was in their Navy. Don\'t want them to come after me too!\"\n\nHe clears his throat. \"Anyway, we\'ve got meals and we have some beer for only 7 gold per round. I know they\'re not of high quality but it\'s better than you would get on any base, Navy or Army!\"", eDialogPic.STANDARD, 3, ["Leave", "Buy", "Drink"])
    if result == 1:
        OpenShop("Shop_Items_Outside_12_0_5")
        p.CancelAction = True
        return
    elif result == 2:
        if Party.Gold >= 7:
            Party.Gold -= 7
            MessageBox("You are poured some drinks. As the bartender said, they are not that impressive, but quite strong. On a scale from one to ten, you would rate them about a three. You feel a bit woozy after drinking them.")
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 8))
            return
        MessageBox("You don\'t have the gold. \"Sorry guys. Can\'t lower the rates for anyone.\"")
        return

def SouthwestMandahl_2732_MapTrigger_33_33(p):
    result = ChoiceBox("This is a small town which is really a collection of homes for the sailors families.\n\nOne of the homes has a sign out front that says: Potions & Alchemetical Supplies. You walk in to find a young woman mixing up a cauldron. She smiles, \"I\'ll be with you in one minute. Please, take a seat.\"\n\nThere is a drawing on the wall of the woman and another young man in an Imperial Navy Uniform with his arm around her. This woman, no surprise, must be the wife of a sailor.\n\nShe enters the room and says, \"Sorry about that. You just came at a bad time. I saw you were looking at the drawing. That\'s David, my husband. As you may have guessed he\'s a sailor. He\'s out on a cargo route between Vantanas and Aizo.\"\n\n\"Anyway, a woman needs to make some money too, you know. I originally studied to be an alchemist, but then I met my David and got pulled away from all that. I figure I can practice this skill and maybe use it seriously some day.\n\nI\'m thinking about opening up a shop somewhere. Probably in Damasnica. But that would be a few years off. Anyway, I\'ve talked far too much, would you like to see some of my potions?\"", eDialogPic.CREATURE, 30, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_15_0_5")
        p.CancelAction = True
        return
    MessageBox("The woman frowns. \"Changed your minds? Well, I\'ll still be here if you change it again!\"")
    p.CancelAction = True

def SouthwestMandahl_2733_MapTrigger_34_34(p):
    MessageBox("This is a small town which is really a collection of homes for the sailors families.")

def SouthwestMandahl_2736_MapTrigger_22_30(p):
    if StuffDone["37_8"] == 250:
        return
    StuffDone["37_8"] = 250
    WorldMap.DeactivateTrigger(Location(22,270))
    WorldMap.DeactivateTrigger(Location(22,271))
    ChoiceBox("After a journey through the mountains, you come to a pleasant sight. From here, the rocky hills slope downward and you can see the ocean. The beach is a very lovely and serene place.\n\nA small resort city called Oringa lies on the shore. You have heard that this place is one of the most popular relaxing sites on southern Pralgad. You can now see why. The fields are covered with lovely flowers and saplings.\n\nTrees dot the landscape, although no collection of them is large enough to justify the title of \'forest\'. Birds chirp in the air as you have reached the edge of Pralgad and the beginning of the lovely blue waters of the Great Ocean.\n\nPerhaps you should take some time off from your journeys and take a small respite here.", eDialogPic.STANDARD, 28, ["OK"])

def SouthwestMandahl_2738_MapTrigger_24_21(p):
    if StuffDone["37_9"] == 0:
        if Party.Gold >= 1000:
            StuffDone["37_9"] = 1
            Animation_Hold(-1, 041_darn)
            Wait()
            Animation_Hold(-1, 028_waterfall)
            Wait()
            Party.Gold -= 1000
            result = ChoiceBox("This bridge is quite covered with a very slippery slime. Unfortunately, one of you slips and falls into the river! Immediately, several of you run to the rescue of your fallen companion.\n\nJust as you manage to pull him/her back onto the bridge. Your companion shouts out and points. You see a man dressed like a monk at your supplies. He looks shocked that you had spotted him. You move toward him\n\nBut he takes off with a large sack of YOUR gold! He is quite fast, but you think you can catch him if you start the chase right now. Do you follow him?", eDialogPic.TERRAIN, 65, ["No", "Yes"])
            if result == 0:
                MessageBox("Too bad. From now on, you will have to keep a closer eye on your supplies.")
                return
            elif result == 1:
                if Party.HasTrait(Trait.Woodsman):
                    ChoiceBox("Your chase leads you off the roads and through the hills and into areas of shrubbery and underbrush. This man is very skilled and knows the area quite well. There are several times where he attempted to fake his path.\n\nHowever, your knowledge of the woodlands and tracking pays off. You easily see through these ruses and continue down the correct path. At one point, you think you lost him, but your keen intuition allows you to find his resting spot.\n\nJust as you are about to ambush him, he hears you and continues up a hill and deeper into the woods. The chase continues until you track him to a well concealed and small hut within the wooded hills.\n\nUnfortunately, the man kept with him a few trained animals to fend you off!", eDialogPic.CREATURE, 34, ["OK"])
                    Party.Reposition(Location(16, 265))
                    p.CancelAction = True
                    Animation_Hold(-1, 046_growl)
                    Wait()
                    WorldMap.SpawnNPCGroup("Group_0_5_5", p.Target)
                    return
                ChoiceBox("The chase leads you off the road and through the hills and into thick areas of shrubbery and brush. You seem to be going good at the chase, but then you lose him!\n\nYou look around, but you can find no indication of where he might have gone. If only you were better at tracking. Frustrated, you return to the bridge.\n\nToo bad. From now on, you will have to keep a closer eye on your supplies.", eDialogPic.CREATURE, 34, ["OK"])
                return
            return
        return

def SouthwestMandahl_2739_MapTrigger_14_8(p):
    ChoiceBox("You come to a small out-of-the-way village. Most of the people make their living as either miners in the nearby hills or as farmers in the mildly fertile surroundings.\n\nEven if you wanted to purchase some of their mineral stock, you could not. You learn the village has a contract with the Empire that all metals are to be sold directly and solely to them.\n\nThe people here are friendly, but struggling to make a living. Food is too scarce to sell any, and the homes too overcrowded to provide lodgings for anyone. So much for expecting beds and meals here.\n\nYou believe the city of Damasnica, capital of the Mandahl Sector, is not that much farther north.", eDialogPic.TERRAIN, 190, ["OK"])
    p.CancelAction = True

def SouthwestMandahl_2740_MapTrigger_41_10(p):
    if StuffDone["38_0"] == 250:
        return
    StuffDone["38_0"] = 250
    WorldMap.DeactivateTrigger(Location(41,250))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("A large group of red lizards descends from the hills. Your training tells you these are the fire breathing variety who prefer their meals nice and toasty. Unfortunately, they want to make you the next meal!", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_5_6", p.Target)

def SouthwestMandahl_2741_MapTrigger_24_9(p):
    if StuffDone["38_1"] == 250:
        return
    StuffDone["38_1"] = 250
    WorldMap.DeactivateTrigger(Location(24,249))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("A large group of red lizards descends from the hills. Your training tells you these are the fire breathing variety who prefer their meals nice and toasty. Unfortunately, they want to make you the next meal!", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_5_6", p.Target)

def SouthwestMandahl_2742_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SouthwestMandahl_2743_SpecialOnWin0(p):
    StuffDone["37_6"] = 1
    ChoiceBox("As soon as you have the sailors at bay, a Naval Bladesman enters the tavern flanked by two guards. He looks quite upset. \"What in the name of the gods is going on here!\"\n\nOne of the beaten sailors gets up and responds. \"These army people came in here and started shoving us around. Said that us Naval officers weren\'t worth the uniform they wear. We had to fight back!\"\n\nThe Bladesman puts his nose up in the air and sniffs. He can obviously smell the alcohol on the sailor\'s breath. \"Thank you sailor. Now get out of here and get cleaned up.\"\n\nThe Bladesman approaches you. He looks at you fiercely and smells your breaths to make sure you haven\'t been drinking. \"Explain to me what really happened.\" You explain the reason for the brawl.\n\nHe turns to the other sailors. \"I\'m so ashamed of you! You\'re members of the Navy! You should know better than to be starting street brawls in taverns.\" One of them interrupts, \"But we didn\'t...\" The bladesman responds, \"I don\'t care!\n\nRegardless of who \'started\' things, we need to show our honor and dignity. Your shore leave is officially canceled. Report to base first thing in the morning.\" The sailors leave, disgusted. The Bladesman says to you, \"Stay out of trouble from now on.\"", eDialogPic.CREATURE, 15, ["OK"])

def SouthwestMandahl_2744_SpecialOnWin1(p):
    MessageBox("The monk and his pets are defeated. You search the home and discover your missing gold along with some extra that can serve as payment for your efforts.")
    Party.Gold += 1350

def SouthwestMandahl_2745_SpecialOnFlee1(p):
    MessageBox("Oh well, it looks like you let him get away with your loot! You find the hut again, but totally vacant. You can bet he\'s going to lay low for a while.")
