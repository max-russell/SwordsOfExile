
def NorthwesternSorcrega_2538_MapTrigger_24_9(p):
    MessageBox("You reach the Nelon-Sorcrega border. The guards at the gatehouse check your papers and allow you to proceed.")

def NorthwesternSorcrega_2539_MapTrigger_24_11(p):
    if StuffDone["44_5"] == 250:
        return
    StuffDone["44_5"] = 250
    WorldMap.DeactivateTrigger(Location(216,107))
    WorldMap.DeactivateTrigger(Location(216,103))
    ChoiceBox("A neat little land bridge separates the Nelon and the Sorcrega sectors. The bridge is made to give the appearance of an isthmus, but there are gateways beneath it to allow the passage of water and vessels.\n\nYou are quite sure this wasn\'t natural. It appears far too straight and linear to be so. However, it has an unusual aesthetic beauty over the traditional utilitarian Imperial bridge.", eDialogPic.TERRAIN, 65, ["OK"])

def NorthwesternSorcrega_2541_MapTrigger_10_13(p):
    ChoiceBox("This place is a saw and paper mill. Harvested trees are brought here, and sawed into appropriate sizes. Some of the product is reduced to pulp and turned into paper by massive, high temperature and pressure rollers.\n\nThe Empire really has an efficient operation here. If you ever wondered where all the wood for tables, chairs, beds, and other things came from, this may have been the place.\n\nYou manage to learn from the millworkers that there have been spottings of pesky gray unicorns while venturing out in the forest. There have been a few close calls, but no serious incidents yet.\n\nSo if you decide to look around the local forests, you may wish to be careful.", eDialogPic.TERRAIN, 148, ["OK"])
    p.CancelAction = True

def NorthwesternSorcrega_2542_MapTrigger_16_24(p):
    if StuffDone["44_6"] == 250:
        return
    StuffDone["44_6"] = 250
    WorldMap.DeactivateTrigger(Location(208,120))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Uh oh! You have just encountered a large herd of gray unicorns. Unfortunately, gray unicorns are considered to be pests, and are very ornery and destructive. Many a traveler have fallen prey to these beasts.\n\nYou hope that you are not next!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_2_4", p.Target)

def NorthwesternSorcrega_2543_MapTrigger_7_17(p):
    if StuffDone["44_7"] == 250:
        return
    StuffDone["44_7"] = 250
    WorldMap.DeactivateTrigger(Location(199,113))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Uh oh! You have just encountered a large herd of gray unicorns. Unfortunately, gray unicorns are considered to be pests, and are very ornery and destructive. Many a traveler have fallen prey to these beasts.\n\nYou hope that you are not next!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_2_4", p.Target)

def NorthwesternSorcrega_2544_MapTrigger_29_18(p):
    if StuffDone["44_8"] == 250:
        return
    StuffDone["44_8"] = 250
    WorldMap.DeactivateTrigger(Location(221,114))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Uh oh! You have just encountered a large herd of gray unicorns. Unfortunately, gray unicorns are considered to be pests, and are very ornery and destructive. Many a traveler have fallen prey to these beasts.\n\nYou hope that you are not next!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_2_4", p.Target)

def NorthwesternSorcrega_2545_MapTrigger_43_20(p):
    MessageBox("These docks are private and the boats are well guarded. The guards do not allow you access to this dock even though you are Empire soldiers.")
    p.CancelAction = True

def NorthwesternSorcrega_2547_MapTrigger_13_34(p):
    if StuffDone["44_9"] == 250:
        return
    StuffDone["44_9"] = 250
    WorldMap.DeactivateTrigger(Location(205,130))
    ChoiceBox("This small pile of rubble is the ruins of several Golems. It looks like it was smashed by some violent, powerful, force. You wonder what could have possibly shattered these mighty creatures of stone.\n\nFrom the linear fashion which the Golems were set, you are can deduce that this scrapping was staged. You know not whether this was for simply scrapping excess Golems or the more frightening process of testing a new weapon.\n\nSeeing the destructive nature of whatever destroyed these generally hardy creatures, you know you would not like to be on its receiving end. Your search of the rubble turns up a small Golem Gem that must have been forgotten.\n\nPerhaps you can sell it for some profit.", eDialogPic.CREATURE, 119, ["OK"])
    Party.GiveNewItem("GolemGem_185")

def NorthwesternSorcrega_2548_MapTrigger_29_12(p):
    if StuffDone["45_0"] == 0:
        result = ChoiceBox("You discover a dead body. The corpse appears to have been trampled to death by some creatures with hooves. You also see several puncture wounds upon the abdomen. If you wouldn\'t know better, this would be the work of Unicorns.\n\nYou notice that he had a weapon at his side, a broadsword. Do you rob the dead and take the broadsword? After all, it\'s not any use to him now.", eDialogPic.TERRAIN, 179, ["Leave", "Take"])
        if result == 1:
            StuffDone["45_0"] = 1
            MessageBox("You take the broadsword off the dead corpse. It has an odd coolness to the touch. Oh well, it\'s yours now!")
            Party.GiveNewItem("CursedBroadsword_373")
            return
        MessageBox("Stealing from the dead just gives you the creeps. Besides, it is dishonorable without cause. You decide to leave the sword in its place.")
        return

def NorthwesternSorcrega_2549_MapTrigger_43_19(p):
    ChoiceBox("The Sorcrega Sector is the world\'s seat for magical research. Mage towers performing various experiments and projects dot the landscape much as farms do in the Agran Sector.\n\nThis specific mage tower performs research on the ecosystems of marine wildlife. The lake to the south is kind of their playground where they experiment with all sorts of water enchantments.\n\nAlthough you do not get to look around because access to the tower is restricted, you manage to get a glimpse of some of the research. They are developing new kinds of water plants and species of fish.\n\nTo what end, you do not know.", eDialogPic.TERRAIN, 197, ["OK"])
    p.CancelAction = True

def NorthwesternSorcrega_2550_MapTrigger_23_41(p):
    ChoiceBox("This is one of the several magical training facilities in the Sorcrega Sector. This specific one is a private training center, unlike the public ones.\n\nThe system works by having groups or corporations lease out towers where magical instruction is taught. The specific admission requirements and the instruction is determined by the holders of the lease.\n\nOften one of the conditions for accepting training here is to sign a contract to work with the specific sponsor after the completion of education. Usually the instruction is geared toward specific training in the sponsor\'s field.\n\nFor instance, mining corporations often train mages. The courses taught are involve identification of minerals, scry surveying, geological structure engineering (to create or expand mine shafts), and various other basic courses.\n\nThis system allows for the recruitment of mages in specific fields on demand. Four centuries ago, this system would not have been possible. The Empire kept strict oversight over all magical instruction.\n\nAlthough they still oversee this, the regulations are much more lax. It is kinder times in which we live.", eDialogPic.CREATURE, 25, ["OK"])
    p.CancelAction = True

def NorthwesternSorcrega_2551_MapTrigger_10_43(p):
    ChoiceBox("Mage towers are quite commonplace in the Sorcrega Sector. So you are not surprised to arrive at one, and you are sure there are many more like these.\n\nThis tower specializes mostly in research, although there is some magical instruction here. The wizards here are a bit secretive about their research, but they tell you it has something to do with developing Golems and counter measures.\n\nCounter measures against Golems! That would be very effective in combat indeed.", eDialogPic.TERRAIN, 197, ["OK"])
    p.CancelAction = True

def NorthwesternSorcrega_2552_MapTrigger_36_44(p):
    MessageBox("This is a residential suburb of Xanthor. Many of the residents here are normal people, however a significantly higher concentration of magi exists. This area is mostly residential, so there is little of interest.")

def NorthwesternSorcrega_2554_MapTrigger_36_45(p):
    MessageBox("This is a small suburb of Xanthor. Although most of this area is residential, you find a blacksmith who is crafting some nice pieces of armor. You decide to look at his stock.")
    OpenShop("Shop_Items_Outside_23_4_2")
    p.CancelAction = True

def NorthwesternSorcrega_2555_MapTrigger_37_45(p):
    MessageBox("This is a residential suburb of Xanthor. Although the area is mostly residential, there are a few merchants selling goods scattered about. One of the stores selling exotic potions attracts your attention.")
    OpenShop("Shop_Items_Outside_25_4_2")
    p.CancelAction = True

def NorthwesternSorcrega_2556_WanderingOnMeet2(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
