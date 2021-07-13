
def NorthwesternAgran_2684_MapTrigger_4_34(p):
    if StuffDone["15_7"] == 0:
        result = ChoiceBox("Cramped away in these hills is the campsite of a band of brigands. You are still unnoticed at this point, so you could easily walk away. Of course, your duty as Empire soldiers calls you to arrest them.", eDialogPic.CREATURE, 18, ["Flee", "Attack"])
        if result == 0:
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You decide to ignore your duty and leave this band to their ill behavior. You hope your superiors never hear about this.")
            return
        elif result == 1:
            StuffDone["15_7"] = 1
            MessageBox("Unfortunately the brigands do not want to be arrested and thrown into jail for their crimes. Instead, they draw their weapons. You have no choice but to respond with attack!")
            WorldMap.SpawnNPCGroup("Group_2_4_4", p.Target)
            return
        return
    MessageBox("There is nothing here except the remains of a campsite.")

def NorthwesternAgran_2685_MapTrigger_21_45(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran Sector. Care to look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        MessageBox("You enter the small village and they are glad to see Empire Soldiers. From the villagers, you learn that there has been a recent series of robberies by bandits.")
        return
    p.CancelAction = True

def NorthwesternAgran_2686_MapTrigger_28_17(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran Sector. Care to look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        MessageBox("Not only does this village farm, it also does a lot of fishing. You learn from the villagers that they have had to depend a lot on fishing lately because some fungus has recently ravaged the last crop. Otherwise, little else of interest.")
        return
    p.CancelAction = True

def NorthwesternAgran_2687_MapTrigger_37_10(p):
    result = ChoiceBox("A small cozy hut lies on the shore. A sign out front says in bold capital letters, \"WELCOME TRAVELERS!\" Care to knock at the door?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        result = ChoiceBox("You knock at the door and a humanoid comes to answer it. The humanoid is a lizard man just over two meters tall. It is very muscular and covered in sweat. \"Ah soldiers! Come on in. I am Savasskari. How may I be of service to you?\"\n\nYou know of this race, it is one of the Slithzerikai -- a race of cave dwelling lizard men who were originally discovered in the depths of Avernum. Most of the race chose to remain in the caves, but a few are occasionally found on the surface.\n\nYou look around his home and see a large anvil, bars of metal, and several other tools for blacksmithing. He looks at you and states in a raspy voice. \"I make my living out here making tools and such. I sell them to the local shops.\n\nPerhaps you would like to purchase some of my wares. It will be at discount price for Empire soldiers, of course. I have (1) Weapons or (2) Armor. Which set would interest you?\"", eDialogPic.CREATURE, 47, ["Leave", "2", "1"])
        if result == 1:
            OpenShop("Shop_Items_Outside_16_2_4")
            p.CancelAction = True
            return
        elif result == 2:
            OpenShop("Shop_Items_Outside_15_2_4")
            p.CancelAction = True
            return
        MessageBox("You decline the Slith\'s offer. \"Well, if you change your mind, be sure to come back.\"")
        p.CancelAction = True
        return
    p.CancelAction = True

def NorthwesternAgran_2688_MapTrigger_41_41(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran Sector. Care to look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        MessageBox("You enter the village and try to learn any news. Unfortunately, the hard working farmers don\'t really have any information that could prove useful.")
        return
    p.CancelAction = True

def NorthwesternAgran_2689_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NorthwesternAgran_2690_SpecialOnWin0(p):
    MessageBox("With those criminals taken care of, you decide that you should take back their ill gotten gains. You search their campsite and find several scattered gold pieces and a broadsword. All in a good day\'s work!")
    Party.GiveNewItem("BronzeBroadsword_45")
    Party.Gold += 124
