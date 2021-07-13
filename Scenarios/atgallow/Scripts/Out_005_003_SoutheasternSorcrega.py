
def SoutheasternSorcrega_2649_MapTrigger_9_10(p):
    ChoiceBox("This is the Sorcrega Mage Academy. For the about the past one thousand years, mages have been trained for service of the Empire within these walls. The mages instructed here are forced to take loyalty oaths to the Empire.\n\nMost of them, after graduation, are pulled into the military. However, some of the more talented ones are assigned to special posts that require magical knowledge.\n\nJust about every mage you have known personally in the army was trained here. But, this is not the only place the Empire teaches mages. Each continent has its own mage academy. Also, there are bunches of privately operated institutions.\n\nBut, you would have to say the Sorcrega Mage Academy is definitely the most prestigious. Graduates here serve in the highest functions whereas graduates of say the Valorim Mage Academy are less prone to serve there.\n\nThis is due to the facilities here -- there are simply none better.", eDialogPic.CREATURE, 25, ["OK"])
    p.CancelAction = True

def SoutheasternSorcrega_2650_MapTrigger_38_4(p):
    ChoiceBox("Not all of the magical reagents that are required by mages can be harvested on Pralgad. In fact, many of the reagents used in the academy and other institutions are imported from other continents.\n\nThe reagent trade has been kindest to tropical Vantanas. Not only are they wealthy in gemstones, an important feature in all disciplines, but they have special kinds of herbs that grow nowhere else in the world.\n\nHowever, not all reagents can even be found on Vantanas. There are special herbs native to Valorim or special metals that can only be mined in Aizo. Even Pralgad has a few useful reagents found nowhere else in the world.\n\nThe trade of magical reagents is a major industry which transfers millions of gold coins a day! The business has made many men and women quite wealthy.", eDialogPic.CREATURE, 27, ["OK"])
    p.CancelAction = True

def SoutheasternSorcrega_2651_MapTrigger_33_11(p):
    ChoiceBox("This is one of the privately operated towers of magical instruction in the Sorcrega Sector. This specific tower is run by a major mining corporation based in Vantanas.\n\nThe lessons taught here are specific to the field of mining. For instance, mages are commonly used to scry for mine sites or locate rich veins. Also, the construction of tunnels and shafts are often the work of mages.\n\nThe mining industry is not the only one to capitalize on specialized magical training. Other industries such as agriculture, construction, shipping, and manufacturing to name a few, have set up private institutions to offer training to mages.", eDialogPic.TERRAIN, 197, ["OK"])
    p.CancelAction = True

def SoutheasternSorcrega_2652_MapTrigger_14_25(p):
    if StuffDone["45_5"] == 250:
        return
    StuffDone["45_5"] = 250
    WorldMap.DeactivateTrigger(Location(254,169))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Several eye creatures float down to the ground from mid-air. Such creatures are often very reclusive and extremely territorial. Unfortunately, you have just trespassed onto their territory!", eDialogPic.CREATURE, 85, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_3_5", p.Target)

def SoutheasternSorcrega_2653_MapTrigger_13_28(p):
    if StuffDone["110_1"] == 0:
        result = ChoiceBox("The Gazers were protecting this small orchard. Most of the trees bear common fruit such as apples, cherries, or pears. However, you notice that a couple of the bushes bear Holly, a useful ingredient in weaker alchemy.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You pick the ripe Holly berries. The bushes contain many more that have not yet reached maturity. If you come back in a few days, they will probably be ripe enough to pick.")
            Party.GiveNewItem("Holly_363")
            RunScript("ScenarioTimer_x_2830", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("The bushes of Holly berries have not been able to ripen anymore yet. The process usually takes a few days.")

def SoutheasternSorcrega_2654_MapTrigger_33_19(p):
    if StuffDone["45_6"] == 250:
        return
    StuffDone["45_6"] = 250
    WorldMap.DeactivateTrigger(Location(273,163))
    WorldMap.DeactivateTrigger(Location(273,164))
    WorldMap.DeactivateTrigger(Location(273,165))
    Animation_Hold(-1, 043_stoning)
    Wait()
    ChoiceBox("Oh dear! This peninsula is home to a small group of deadly Basilisks. These lizards tend to be quite territorial and they don\'t like your intrusion one bit. Remember, their gaze is fatal.", eDialogPic.CREATURE, 86, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_3_4", p.Target)

def SoutheasternSorcrega_2657_MapTrigger_24_34(p):
    result = ChoiceBox("This hut is home to a kind Witch. At first when you see her, you are kind of afraid. The site of an old hag in black robes is generally not a pleasant sight. However, she invites you inside for some herbal tea.\n\nDuring the visit you tell of your adventures as you share the energizing drink. During the conversation, she asks if you would like to purchase a few of her excess alchemy herbs.", eDialogPic.CREATURE, 29, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_20_5_3")
        p.CancelAction = True
        return
    MessageBox("You turn down the offer and finish up your visit. Before you leave, she welcomes you to return.")
    p.CancelAction = True

def SoutheasternSorcrega_2658_MapTrigger_7_24(p):
    if StuffDone["45_7"] == 0:
        result = ChoiceBox("At the end of this forest you find the body of an apprentice mage. He was obviously mauled to death by some large creature such as a bear or an ursag. The apprentice clutches a wand in his hand, not that it did him any good.\n\nYou could easily relieve him of the wand. However, this would be robbing the dead which is generally not a good thing. But, on the other hand, why let a good wand go to waste?", eDialogPic.TERRAIN, 179, ["Leave", "Take"])
        if result == 1:
            StuffDone["45_7"] = 1
            MessageBox("You decide to take the wand. It is a fairly typical wand, but elegantly decorated. The tip feels kind of warm.")
            Party.GiveNewItem("WandofFlame_285")
            return
        MessageBox("You decide to choose the honorable path and leave the corpse and his treasure alone. Of course, if you change your mind, you know where to look.")
        return

def SoutheasternSorcrega_2659_MapTrigger_40_35(p):
    if StuffDone["116_0"] == 0:
        result = ChoiceBox("This is your lucky day! This island happens to be home to a small patch of valuable Ember Flowers. These flowers are one of the most useful ingredients in alchemy and they are free for the picking!", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You harvest some of the Ember Flowers. They feel nice and warm to the touch. If you wait a few days, more will probably grow back.")
            Party.GiveNewItem("EmberFlowers_369")
            RunScript("ScenarioTimer_x_2831", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("The Ember Flower patch has not quite grown back yet. You will need to wait another few days.")

def SoutheasternSorcrega_2660_WanderingOnMeet2(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
