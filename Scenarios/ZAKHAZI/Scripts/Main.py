def Initialise_Scenario():
    pass

def Intro_Message(p):
    ChoiceBox("The history of Exile is a history of wars, large and small, against humans and bizarre creatures. They were all long and bloody, and all fought purely for survival.\n\nNot all Exiles returned to the surface when the Empire gave them a country of their own. Some stayed in the caves and tunnels they had adopted as their homes. Alas a new threat awaited them.\n\nThe Slithzerikai, the strange subterranean lizard men that fought Exile for much of their existence, have attacked again. Several huge, barbarian tribes of the creatures are attacking Exile, and have had great success against its troops.\n\nNow all in Exile watch the siege at Fort Cavalier, the key defensive outpost between the sliths and the heart of Exile. The fort has held out for months, but it grows weaker with every passing day.\n\nYou have been contacted by the people of Exile and sent here with news of a highly lucrative mission, having something to do with Fort Cavalier. You have just arrived at Fort Goodling to meet with Commander Yale.\n\nShe will tell you what your mission is, should you choose to accept it. All you know is that the stakes are incredibly high, and time is of the essence ...", eDialogPic.SCENARIO, 17, ["OK"])

def Town_Pre_Entry(town):
    if town.Num==21:
        return TownMap.List[town.Num + StuffDone["100_0"]]
    return town


def WurmPit_183_GlobalTalkingTrigger_19(p):
    if SpecialItem.PartyHas("MorogsShrooms"):
        StuffDone["110_0"] = 1
        SpecialItem.Take("MorogsShrooms")
        result = ChoiceBox("Morog eagerly grabs the mushrooms and places them securely in a pocket of her robes. \"Excellent. Now, as I gave my word, I will produce a reward.\"\n\nShe extends a skeletal hand and mutters a few powerful words. A huge scroll appears in front of you, floating in midair. \"This scroll is very old, and tells the history of many ancient dragons. It\'s a rare, highly valuable piece of scholarship.\"\n\n\"Of course, as interesting as this item can be, there are many other things I can do for you. If you wish, instead of the scroll, I can tell you the location of a priceless gemstone, which can easily buy you passage through the northern caverns.\"\n\n\"Would you like this information instead of the scroll?\"", eDialogPic.CREATURE, 60, ["No", "Yes"])
        if result == 0:
            result = ChoiceBox("Morog thinks. \"All right then. How about this, instead of the scroll. There is a huge cavern to the north, which is filled with fungi sometimes called Poppy Shrooms.\"\n\n\"These continuously emit soporific spores. Trying to get through this cavern would take you days, considering how disorienting the spores can be. That is, if you get through the cavern at all.\"\n\n\"If you wish, I can give you an item which will protect you from the spores. These mushrooms are not uncommon. This item will serve you well. Would you like it?\"", eDialogPic.CREATURE, 60, ["No", "Yes"])
            if result == 0:
                p.TalkingText = "Morog nods. \"Fine. Take the scroll.\" You do. \"It will serve you well in the caverns far to the north, whether you know it or not. Good luck to you.\"\n\nShe thinks. \"Oh, and I think I would move on if I were you. At this point, I have no hunger for the flesh of humans. That can always change.\""
                StuffDone["8_3"] = 1
                SpecialItem.Give("ScrollofDragons")
                return
            elif result == 1:
                p.TalkingText = "She mutters a spell. The scroll disappears, and an onyx mushroom talisman appears in its place. \"Wise choice,\" she says. \"Spore Shrooms are a real threat.\"\n\n\"That is all. Thank you for your assistance. Good day to you.\""
                SpecialItem.Give("MushroomTalisman")
                return
            return
        elif result == 1:
            p.TalkingText = "The scroll disappears. \"Excellent,\" Morog says. \"There is a tunnel to the east of my fortress, which leads to an outpost of stranded Empire soldiers.\"\n\n\"In that outpost is the Melora Opal, a massive, priceless stone that will serve you very well in trying to leave these caverns to the north. That is all. You may go.\""
            return
        return

def On_Using_SI_BundleofWands_689(p):
    MessageBox("You try to open the bundle, but the wards the Tower of Magic put on it are too strong. It won\'t come open until you reach Fort Cavalier.")

def On_Death_Of_TentacledUrSlime_690(p):
    MessageBox("The mighty tentacled slime beast falls. The acid in its body immediately starts to burrow a tunnel in the ground. You hope there aren\'t too many more of these terrors around.")

def ScenarioTimer0_693(p):
    if StuffDone["100_0"] == 0:
        if Party.Day >= 21:
            if StuffDone["100_3"] >= 1:
                return
            ChoiceBox("Three weeks have passed since your arrival at Fort Goodling. When you arrived, people guessed that Fort Cavalier had three weeks left before it fell.\n\nThe third week has just passed.", eDialogPic.STANDARD, 31, ["OK"])
            StuffDone["100_0"] = 1
            return
        if Party.Day >= 19:
            if StuffDone["100_1"] == 250:
                return
            StuffDone["100_1"] = 250
            MessageBox("You were only given three weeks to reach Fort Cavalier. You\'re very close to running out of time. If you don\'t complete the Za-Khazi run in the next day or two, all may be lost. Best hurry ...")
            return
        if Party.Day >= 11:
            if StuffDone["100_2"] == 250:
                return
            StuffDone["100_2"] = 250
            MessageBox("When you arrived at Fort Goodling, you were told that they estimated you had three weeks until Fort Cavalier fell. Half of that time has elapsed.")
            return
        return

def GlobalCall_FortCavalier_694(p):
    if SpecialItem.PartyHas("MeloraOpal"):
        MessageBox("As soon as you can, you try to sell the Melora opal. As expected, it\'s quite a prize. You get 2500 gold for it.")
        Party.Gold += 2500
        if SpecialItem.PartyHas("CrystalofPurity"):
            MessageBox("You make an effort to sell the Crystal of Purity. Most people have little interest in it, sages included. Fortunately, you find a traveling mage who sees how useful an item it could be. He gives you 1000 gold for it.")
            Party.Gold += 1000
            if SpecialItem.PartyHas("MalachiteStatue"):
                MessageBox("The malachite statue from the Wurm Pit turns out to have had some unpleasant, malevolent spells placed upon it. Fortunately, this makes it of great interest to some local mages. They give you 1000 gold for it.")
                Party.Gold += 1000
                Scenario.End()
                return
            Scenario.End()
            return
        if SpecialItem.PartyHas("MalachiteStatue"):
            MessageBox("The malachite statue from the Wurm Pit turns out to have had some unpleasant, malevolent spells placed upon it. Fortunately, this makes it of great interest to some local mages. They give you 1000 gold for it.")
            Party.Gold += 1000
            Scenario.End()
            return
        Scenario.End()
        return
    if SpecialItem.PartyHas("CrystalofPurity"):
        MessageBox("You make an effort to sell the Crystal of Purity. Most people have little interest in it, sages included. Fortunately, you find a traveling mage who sees how useful an item it could be. He gives you 1000 gold for it.")
        Party.Gold += 1000
        if SpecialItem.PartyHas("MalachiteStatue"):
            MessageBox("The malachite statue from the Wurm Pit turns out to have had some unpleasant, malevolent spells placed upon it. Fortunately, this makes it of great interest to some local mages. They give you 1000 gold for it.")
            Party.Gold += 1000
            Scenario.End()
            return
        Scenario.End()
        return
    if SpecialItem.PartyHas("MalachiteStatue"):
        MessageBox("The malachite statue from the Wurm Pit turns out to have had some unpleasant, malevolent spells placed upon it. Fortunately, this makes it of great interest to some local mages. They give you 1000 gold for it.")
        Party.Gold += 1000
        Scenario.End()
        return
    Scenario.End()
