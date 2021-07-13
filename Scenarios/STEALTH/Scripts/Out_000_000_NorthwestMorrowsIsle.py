
def NorthwestMorrowsIsle_350_MapTrigger_39_25(p):
    if StuffDone["100_8"] >= 1:
        if StuffDone["101_1"] >= 1:
            MessageBox("When you try to take the ferry to Zaskiva Isle again, grim faced guards stop you. \"Sorry, but we aren\'t letting anyone through. Since Lord Volpe\'s assassination, the isle is cut off from all visitors.\"\n\nThere\'s nothing you can say to change his mind. You turn back.")
            return
        result = ChoiceBox("You reach the ferry to Zaskiva Isle. The city of Zaskiva, capital of Morrow\'s Isle, is well protected. Guards check you over thoroughly before they let you near the ferry.\n\nThe ride across is 10 gold. Do you go?", eDialogPic.TERRAIN, 66, ["Leave", "Pay"])
        if result == 1:
            if Party.Gold >= 10:
                Party.Gold -= 10
                MessageBox("The ferry ride is quick and uneventful. They aren\'t letting many people go to Zaskiva these days, what with the rebel activity and all. You\'re practically the only people on the ferry. Soon, you land.")
                Party.Reposition(Location(33, 20))
                p.CancelAction = True
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You don\'t have the 10 gold. They shake their heads, and tell you to leave the dock.")
            return
        return
    MessageBox("This is the ferry to the Zaskiva Isle, a smaller island to the northeast, where the capital of Morrow\'s Isle sits, secure and protected. There are a good number of guards, checking to make sure that nobody unwelcome manages to use the ferry.\n\nWhen you identify yourselves, they shake their heads. \"No offense, but we can\'t let you through to the island. Sorry.\"")

def NorthwestMorrowsIsle_351_MapTrigger_33_20(p):
    if StuffDone["101_0"] >= 1:
        result = ChoiceBox("When you\'re almost to the ferry, you notice that a large group of woodsmen has caught up with you and now surrounds you on all sides. One of them gets close to you and hisses, \"What are you doing? Do you want to get killed? Come with us!\"\n\nWhen you hesitate, she says, \"They\'re questioning anybody trying to leave. Hard! This isle has been closed off. Lord Volpe is dead. We\'re with the Hill Runners. Come with us, and we\'ll get you off the isle.\"\n\nYou look at the dock. Sure enough, it does look like the guards are interrogating a group of terrified merchants. Still, it could be a trap. Do you go with them instead of going to the isle?", eDialogPic.CREATURE, 20, ["Yes", "No"])
        if result == 0:
            MessageBox("The rebels take you north, to a concealed, leaky rowboat. From there, two of them row you across the water to an isolated beach north of the ferry dock, and, without a word, head back.\n\nYou look around with relief. It\'s hard to believe, but you managed to escape Zaskiva Isle with your lives after all.")
            Party.Reposition(Location(44, 21))
            p.CancelAction = True
            return
        elif result == 1:
            MessageBox("Escaping the woodsmen, you move on to the docks. Unfortunately, the guards have a description of you as \"suspicious people seen placing a box near the explosion.\" They don\'t even ask you any questions before they seize you and start the beatings.\n\nUnfortunately, by the time Jaen finds out where you are and what\'s happening to you, it\'s too late. In rational times, you might have been held for questioning and put on trial. These are not, alas, rational times.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        return
    result = ChoiceBox("This is the ferry back to Morrow\'s Isle. Only 10 gold. Do you go?", eDialogPic.TERRAIN, 64, ["Leave", "Pay"])
    if result == 1:
        if Party.Gold >= 10:
            Party.Gold -= 10
            MessageBox("The ferry ride is fast and uneventful.")
            Party.Reposition(Location(39, 25))
            p.CancelAction = True
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You don\'t have the 10 gold. They shake their heads, and tell you to leave the dock.")
        return

def NorthwestMorrowsIsle_352_MapTrigger_45_24(p):
    if StuffDone["200_0"] == 250:
        return
    result = ChoiceBox("You stumble across a pitiful campsite, occupied by a single ragged outcast. Or hermit. Or brigand. You aren\'t sure. He sure is a mess, though.\n\nWhen he sees you aren\'t going to butcher him, he scuttles up to you. \"Welcome to my humble camp,\" he rasps. \"I am Bartholomew, a traveler down on his luck. I would offer to share my food, but I have no food to give. I have something else, though.\"\n\nTaking the bait, you ask what he has. He removes a small, wooden wand from his rags. \"This is my only possession, but a valuable item it is. It\'s a wand of massive, searing fireballs! It can be yours for only 500 gold.\"\n\n\"Have pity on me, please! I am poor, bereft of all help. Will you not buy this wand, so I may get a roof over my head?\"\n\nYou examine the wand. It\'s hot to the touch. Clearly magical. Still, this guy might be a con artist. Do you buy it?", eDialogPic.CREATURE, 11, ["Leave", "Pay"])
    if result == 1:
        StuffDone["200_0"] = 250
        WorldMap.AlterTerrain(Location(45,24), 1, None)
        WorldMap.DeactivateTrigger(Location(45,24))
        if Party.Gold >= 500:
            Party.Gold -= 500
            MessageBox("Ecstatic, the man takes your money and runs off through the woods (giving you the wand first, of course). The wand is a beautiful piece of finely carved wood. You hope it\'s worth what you paid.")
            Party.GiveNewItem("WandofFlame_285")
            return
        MessageBox("The man shakes his head. \"I am sorry, but this wand is all I own of value in the world. I can give it for its fair price, no less.\"")
        return
    MessageBox("The man watches you sadly as you go. The last you see of him, he\'s gnawing a dry chicken bone.")

def NorthwestMorrowsIsle_353_MapTrigger_15_42(p):
    if StuffDone["200_1"] == 250:
        return
    StuffDone["200_1"] = 250
    WorldMap.AlterTerrain(Location(15,42), 1, None)
    WorldMap.DeactivateTrigger(Location(15,42))
    MessageBox("With all the political chaos and random patrols roving everywhere, it\'s only natural that some of the few monsters left in Valorim would gravitate here. One of them has just ambushed you, hoping for an easy (and large) meal ...")
    WorldMap.SpawnEncounter("Group_0_0_4", p.Target)

def NorthwestMorrowsIsle_354_MapTrigger_19_14(p):
    if StuffDone["101_0"] >= 1:
        MessageBox("After the explosion in Zaskiva, there\'s no way the people living in these farmhouses are even going to pretend to be friendly to you. They slam shut and lock their doors when they see you coming.")
        return
    result = ChoiceBox("People on Zaskiva Isle are a bit friendlier than people on the mainland. The extra security on the Isle makes them feel a bit more secure.\n\nThat\'s why, when they see you approaching, they don\'t hesitate to come out, welcome you, and invite you in for pie. They ask you for news from the rest of the isle - not many people come out here now, so they take what they can get.\n\nAfter a while, you get up to depart. Before you go, they ask if you\'d like to buy some rations.", eDialogPic.TERRAIN, 190, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_25_0_0")
        p.CancelAction = True
        return
