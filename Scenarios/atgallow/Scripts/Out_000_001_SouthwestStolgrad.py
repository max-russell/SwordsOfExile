
def SouthwestStolgrad_2389_MapTrigger_34_26(p):
    ChoiceBox("The southern region of Stolgrad is home to lush woodlands containing many exotic species of trees. The wood of these trees is often of high quality and used to make the luxury pieces of furniture and other wooden fixtures.\n\nA few of the species actually have strong magical properties. Now just about every type of tree has some magical use, but some are stronger than others. The wood is often used to make high quality, and sometimes enchanted, bows and arrows.\n\nBeing Empire soldiers does not allow you to get close to this woodcutting facility. The Stolgrad Sector is one of the few remaining sectors to support its own military and they are the only ones allowed besides the workers.\n\nHowever, from a distance you are able to see working conditions here are not comfortable in the least. Although sawmills are generally not known for their comfort, the working conditions here are much more stark than others.\n\nOne other feature of interest is a small structure called the \'Punishment Cells\'. You have heard that regulations are much stricter in Stolgrad. Workers who fall behind are punished severely though intense flogging.\n\nThe motivation is to keep productivity high through fear, and in most cases it succeeds.", eDialogPic.TERRAIN, 129, ["OK"])
    p.CancelAction = True

def SouthwestStolgrad_2390_MapTrigger_43_38(p):
    ChoiceBox("You approach a small hut that provides home to a small group of Nephilim. You notice that upon your approach, there was one stationed on lookout. However, announced the \'all clear\' when he identified you.\n\nYou wonder what that Nephilim was looking out for. One of the older Nephilim comes out to welcome you.\n\n\"Good day soldiers of the Empire. You must forgive us for being careful for it is not a good thing to be, or I should say, not to be Humans.\" You inquire further along these lines.\n\n\"You see, all people here are not treated well. There is always constant supervision with strict wake-up and curfew times. The working conditions are harsh and the punishments even more so.\n\nHumans do not have it well off, but Nephilim are even worse. Non-humans are considered to be inferior here and are always given the lowest standards of living and the toughest work.\n\nWe could take it no longer and we fled our labor camp. The Stolgradian soldiers are definitely out looking for us, so we hide here, hoping one day we can sneak past the border. Please, I beg you, do not inform them of our hiding place!\"", eDialogPic.CREATURE, 37, ["OK"])
    ChoiceBox("You assure them that you have no intention of informing the soldiers of Stolgrad. You are of the Empire and do not fall under their rules. The Nephil thanks you profusely and invites you inside for some food.\n\nThe meal is a kind of herbal stew with some avian meat spliced in. It is not all that delicious, but you\'ve had worse in training. \"I know it is not as good as you are used to, but we do our best.\"\n\nYou thank them for the meal. Before you leave, the Nephilim informs you to be careful, keep a low profile, and follow rules without question. The Stolgradian authority are very strict and even soldiers are not exempt from their laws.", eDialogPic.CREATURE, 37, ["OK"])
    p.CancelAction = True

def SouthwestStolgrad_2391_MapTrigger_6_14(p):
    ChoiceBox("The Stolgrad Sector has a rather different way of exploiting labor than the rest of the continent. They prefer the old fashioned way that was practiced centuries ago of instilling fear to extract productivity.\n\nThis labor camp is a perfect example of how this is carried out. Laborers are busy out in the fields under the close supervision of the Stolgradian military, an independent branch from the Empire\'s\n\nThe soldiers, of course, perform no work but merely supervise with whips on their belts. These whips are often employed to keep the workers in line and to keep productivity high.\n\nThe other branch that this working camp partakes is fishing. Large fishing boats are moved out to sea when the laborers cast their nets into the ocean. All under the direct supervision of the soldiers, of course.\n\nSeeing the horrible working conditions you know that you would not want to have to man these fields. You are glad they did not have anything like this back in the Agran Sector.", eDialogPic.TERRAIN, 189, ["OK"])
    p.CancelAction = True

def SouthwestStolgrad_2393_MapTrigger_19_24(p):
    ChoiceBox("This fortress is one of the Stolgradian military outposts that keeps tabs on the sector. The Stolgrad Sector is unique in many ways. One of them is the fact that it maintains its own military.\n\nThe troops are a completely separate branch from yours. The soldiers are trained and maintained solely by the Stolgradian authority to serve and protect their rulers. Nobles, by custom, have the authority to raise their own armies.\n\nIndeed, this is a rarity in today\'s world. At one time, every sector was ruled by some noble order and most maintained their own armies. However, over the years, the bloodlines have died out or were disposed of by residents.\n\nRather than selecting new bloodlines, the Empire has decided to grant the authority to the residents with oversight by the center. This was done as a way to maintain power by the Empire.\n\nThe noble orders were quite powerful and kept restraints on the Emperor\'s power, so they were grandfathered out instead of just eliminated to avoid bloodshed. In fact, all but one order on Pralgad is gone and that is the one in Stolgrad.\n\nStolgrad is ruled by the Order of Odin, one of the most powerful groups in the world with a long history of powerful archwizards.", eDialogPic.CREATURE, 13, ["OK"])
    p.CancelAction = True

def SouthwestStolgrad_2395_MapTrigger_41_26(p):
    if StuffDone["45_8"] == 250:
        return
    StuffDone["45_8"] = 250
    WorldMap.DeactivateTrigger(Location(41,74))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    result = ChoiceBox("You encounter a fair sized patrol of Stolgradian soldiers. Being a separate military organism from the standard military all together, many of their ilk consider themselves to be above the law in their sector.\n\nSo it is not a surprise when the captain tells you that you are trespassing on the noble\'s private property and must pay a fine of 500 gold. You know this charge is false, but they threaten to arrest you if you refuse to pay.\n\nYou also know that people arrested here are often placed in prisons, forgotten about, or die in some mysterious accident. Do you accept the fee, or see if the soldiers will try to arrest you?", eDialogPic.CREATURE, 13, ["Accept", "Refuse"])
    if result == 0:
        if Party.Gold >= 500:
            Party.Gold -= 500
            Animation_Hold(-1, 040_thankyou)
            Wait()
            MessageBox("You decide to go against your pride and pay the unreasonable and illegal 500 gold fine. The soldiers tell you not to continue trespassing or punishment will be more severe.")
            return
        MessageBox("Unfortunately, you lack the necessary gold for the fine. Being greedy and not really wanting to arrest you, they decide to take what you have and wander off. However, they promise if they catch you again, they will not be so friendly.")
        Party.Gold -= 500
        return
    elif result == 1:
        MessageBox("You laugh at their demands seeing if they make good on their promise to arrest you. They were not kidding, they pull their weapons and demand you to surrender. You tell them to shove it and a fight ensues!")
        WorldMap.SpawnNPCGroup("Group_0_1_4", p.Target)
        return

def SouthwestStolgrad_2396_MapTrigger_32_5(p):
    ChoiceBox("This is a very grim site indeed. This tree has been converted to a gallows. Hanging from the nooses are three middle aged men and one older woman. Upon the tree is nailed a piece of paper. It reads:\n\nBY DECREE OF OUR GREAT RULER AUSPIRE: These men and women are condemned to death by hanging for repeated offenses against the state. These involve the interference of productivity by refusing to obey orders, insubordination...\n\n...lack of punctuality, and an unacceptable level of efficiency. Know that failure to perform ones duty is punishable by the strictest means. Let this be an example to all who witness or read this note. Signed, Captain Havos.\"\n\nNext to the signature is the seal of the noble order of Stolgrad who is currently ruled by a woman named Auspire.\n\nYou have heard that the authorities of Stolgrad were harsh, but you never realized the extend of the cruelty. These people were probably just too slow at their work and were executed because of it.\n\nYou would hate to see the fates awaiting those accused of more serious crimes.", eDialogPic.STANDARD, 1024, ["OK"])

def SouthwestStolgrad_2397_MapTrigger_21_43(p):
    if StuffDone["45_9"] == 250:
        return
    StuffDone["45_9"] = 250
    WorldMap.DeactivateTrigger(Location(21,91))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("You have heard that crime and banditry are much lower in Stolgrad than in any other sector. However, even the ironclad methods of the sector must have a few flaws off the beaten path.\n\nYou have encountered a group of bandits. Knowing that the punishment for banditry is death, they decide not to take any chances and attack you!", eDialogPic.CREATURE, 4, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_1_5", p.Target)

def SouthwestStolgrad_2398_WanderingOnMeet2(p):
    if StuffDone["9_0"] >= 7:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    if StuffDone["9_0"] < 3:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    if Maths.Rand(1,0,100) < 35:
        MessageBox("You encounter a patrol of Stolgradian soldiers. They stop, question you, and check your papers. Unfortunately one of them realizes you are wanted by the authorities. You decide not to go peacefully.")
        return
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SouthwestStolgrad_2400_SpecialOnWin0(p):
    MessageBox("You manage to kill off the corrupt soldiers. Although you are now guilty of slaying Stolgradian soldiers, a serious crime punishable by death, you doubt that anyone will be able to catch you.")

def SouthwestStolgrad_2401_SpecialOnFlee0(p):
    MessageBox("You manage to outrun the soldiers. My these troops are much better trained than you would have expected. You knew the Stolgradian army had high standards, but you are impressed.")
