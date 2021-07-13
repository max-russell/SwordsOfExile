
def NorthwestMandahl_2662_MapTrigger_29_1(p):
    result = ChoiceBox("You have reached one of the Empires many flourishing mines. Care to take a look inside?", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["38_8"] == 0:
            if Maths.Rand(1,0,100) < 30:
                StuffDone["38_8"] = 1
                result = ChoiceBox("You enter the mine, not expecting to get very far. When you come to the guardpost at the beginning of the mine, you find it empty! The guards must have decided to take a break.\n\nOh well, that means you will be able to get to look around. Unfortunately, you don\'t get very far before you are picked out of the crowd. The guards escort you to the office where you encounter an official.\n\n\"How did you get this far in the mine?\" You tell him about the unmanned guardpost. He nods. \"I see. I can assure you that the problem will be taken care of. You see, I cannot allow you to be trudging through the mines.\n\nThere is a policy that says only authorized persons are allowed here. I know you\'re soldiers, but it\'s for security and safety reasons.\" He thinks for a bit. \"You know, before I let you go, I think I\'ll make an offer to you.\n\nThis mine, unlike the others in the region does much of its own processing. We do so, because it\'s hard to get our carts through the rocky terrain. I can sell you some of our iron weapons for wholesale price, if you\'re interested.\n\nIt\'s a one-time offer. Do you want to take it or not?\"", eDialogPic.CREATURE, 31, ["Leave", "Buy"])
                if result == 1:
                    OpenShop("Shop_Items_Outside_31_0_4")
                    p.CancelAction = True
                    return
                MessageBox("You turn down the offer and are promptly escorted out of the mines.")
                p.CancelAction = True
                return
            ChoiceBox("You do not get very far. About fifty meters into the mine, you encounter a guardpost. They check for passes, and of course you are turned away.\n\nThey tell you even though you are Empire Soldiers, you cannot be allowed in without the proper authorization for security reasons. Oh well, you probably would not have seen all that much anyway.", eDialogPic.CREATURE, 12, ["OK"])
            p.CancelAction = True
            return
        ChoiceBox("You do not get very far. About fifty meters into the mine, you encounter a guardpost. They check for passes, and of course you are turned away.\n\nThey tell you even though you are Empire Soldiers, you cannot be allowed in without the proper authorization for security reasons. Oh well, you probably would not have seen all that much anyway.", eDialogPic.CREATURE, 12, ["OK"])
        p.CancelAction = True
        return
    p.CancelAction = True

def NorthwestMandahl_2663_MapTrigger_43_44(p):
    if StuffDone["38_3"] == 250:
        return
    StuffDone["38_3"] = 250
    WorldMap.DeactivateTrigger(Location(43,236))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("The Mandahl Mountains provide a home to many of the world\'s wild creatures. Unfortunately, you have just had the displeasure of meeting one of them.\n\nA pack of hungry fire-breathing giant lizards jump out from the rocks to have you for dinner!", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_4_4", p.Target)

def NorthwestMandahl_2664_MapTrigger_42_14(p):
    if StuffDone["38_4"] == 250:
        return
    StuffDone["38_4"] = 250
    WorldMap.DeactivateTrigger(Location(42,206))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("The Mandahl Mountains provide a home to many of the world\'s wild creatures. Unfortunately, you have just had the displeasure of meeting one of them.\n\nA pack of hungry fire-breathing giant lizards jump out from the rocks to have you for dinner!", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_4_4", p.Target)

def NorthwestMandahl_2665_MapTrigger_44_35(p):
    if StuffDone["114_1"] == 0:
        result = ChoiceBox("This is your lucky day! These rocks are home to a special kind of mold called Asptongue Mold. The fungus has powerful alchemetical properties and is a key ingredient in many potions.\n\nYou could harvest some today and come back in a few days to get some more.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You take some of the Asptongue Mold, careful to leave enough so that it will be able to grow back within a reasonable amount of time. If you want, you can come back in a few days and harvest more.")
            Party.GiveNewItem("AsptongueMold_367")
            RunScript("ScenarioTimer_x_2826", ScriptParameters(eCallOrigin.CUSTOM))
            return
        p.CancelAction = True
        return
    MessageBox("You return to the area where you found some Asptongue Mold earlier. The source has not yet been able to grow back yet. You will need to wait another day or so.")
    p.CancelAction = True

def NorthwestMandahl_2666_MapTrigger_33_4(p):
    if StuffDone["38_5"] == 250:
        return
    StuffDone["38_5"] = 250
    WorldMap.DeactivateTrigger(Location(33,196))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Suddenly, you hear a loud battle cry. You look to see several hulking Ogres moving toward you as fast as they can (which is not saying much considering their size). Their intentions don\'t look friendly either.\n\nOff in the distance, you see another Ogre. He is just waiting, watching. You swear that his skin has a kind of blue tint to it. Anyway, you have some Ogres to deal with!", eDialogPic.CREATURE, 42, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_4_5", p.Target)

def NorthwestMandahl_2667_MapTrigger_26_15(p):
    if StuffDone["38_6"] == 250:
        return
    StuffDone["38_6"] = 250
    WorldMap.DeactivateTrigger(Location(26,207))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Suddenly, you hear a loud battle cry. You look to see several hulking Ogres moving toward you as fast as they can (which is not saying much considering their size). Their intentions don\'t look friendly either.\n\nOff in the distance, you see another Ogre. He is just waiting, watching. You swear that his skin has a kind of blue tint to it. Anyway, you have some Ogres to deal with!", eDialogPic.CREATURE, 42, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_4_5", p.Target)

def NorthwestMandahl_2668_MapTrigger_37_19(p):
    if StuffDone["38_7"] == 250:
        return
    StuffDone["38_7"] = 250
    WorldMap.DeactivateTrigger(Location(37,211))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("What a lovely sight. Down by the river is a heard of horses drinking. You move in to take a closer look and realize that these are not just horses, but unicorns!\n\nUnfortunately, they are of the common gray variety. They are ornery, intelligent, and very protective of their territory. They are generally considered one of the Empire\'s pests, being several steps up from Goblins.\n\nAlthough Goblins are smarter than your average unicorn, unicorns are much more dangerous. There have been many a tale about travelers being trampled to death by these creatures.\n\nYou start to move away, but unfortunately one of them notices you. He quickly alerts the others that food is near. Oh dear, now you\'ve got a bunch of hungry unicorns to deal with!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_4_6", p.Target)

def NorthwestMandahl_2669_MapTrigger_23_6(p):
    ChoiceBox("You arrive at a small Empire fortress. It appears that this fort is used to coordinate the area\'s mining activity. From conversations with the miners, you learn that the chief mineral here is iron, quite common in the Mandahl Mountains.\n\nFurther exploration of the fort reveals deeper into the operation. Very little, if any of the processing is actually done here. The storerooms are filled with bins full of iron ore.\n\nThe bins are being wheeled down into another larger room. Although the guards will not let you enter, they allow you to look inside. Several mages are maintaining an Empire portal.\n\nYou watch them push a cart through the red gateway. Several minutes later, an empty cart emerges. That cart is taken away and a full cart is pushed through the portal and the process is repeated.\n\nFrom a conversation with a mage, you discover the portal is linked to a processing plant in the Nelon Sector, far to the northeast of here. You move to the receiving area where new carts from the mines are being wheeled in.\n\nIt is amazing actually how much iron is in these mountains. You wonder if the supplies will ever run out.", eDialogPic.TERRAIN, 189, ["OK"])
    p.CancelAction = True

def NorthwestMandahl_2670_MapTrigger_18_3(p):
    result = ChoiceBox("You have reached one of the Empires many flourishing mines. Care to take a look inside?", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        ChoiceBox("You do not get very far. About fifty meters into the mine, you encounter a guardpost. They check for passes, and of course you are turned away.\n\nThey tell you even though you are Empire Soldiers, you cannot be allowed in without the proper authorization for security reasons. Oh well, you probably would not have seen all that much anyway.", eDialogPic.CREATURE, 12, ["OK"])
        p.CancelAction = True
        return
    p.CancelAction = True

def NorthwestMandahl_2673_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NorthwestMandahl_2674_SpecialOnWin1(p):
    if Maths.Rand(1,0,100) < 50:
        MessageBox("With the Ogres killed, you search their hiding places. It appears that they were having a mildly successful day with their banditry. You manage to gather up a fair sized collection of gold coins. All in a days work!")
        Party.Gold += 222
        return
    MessageBox("With the Ogres defeated, you search their hiding places. It appears they were not having a very successful day as to the lack of loot. Too bad, it looks like what you found on their persons will have to do.")
