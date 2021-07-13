
def SoutheasternStolgrad_2421_MapTrigger_20_30(p):
    MessageBox("This guardpost lies along the border of Imperial and Stolgrad. The attendants view your papers and give you the go to proceed.")
    if StuffDone["54_0"] == 250:
        return
    StuffDone["54_0"] = 250
    WorldMap.DeactivateTrigger(Location(156,197))
    ChoiceBox("You arrive at the Imperial Sector, the center of the Empire and the entire world. It is within this Sector that tens of thousands of decisions are made each day about public policy by various officials and bureaucrats.\n\nIt is here where most of Pralgad\'s soldiers (including you) are trained. Armies are housed within the sector to help maintain security and order. The protection of the capital of the Empire, Solaria, is paramount.\n\nThe Imperial Sector is probably the most densely populated sector in the world. Census figures say that about five million people live and work within the sector with jobs ranging from administration to clerical to maintenance.\n\nThe size will soon become apparent as you will see the many residential areas that dot the landscape. Each has its own name, but largely these dwellings are insignificant.\n\nThe Imperial Sector is also the largest consumers of resources. The upper class residents here tend to be the wealthiest in the world. The chief product of the Imperial Sector is policy, and little else also making it the most dependent.\n\nWelcome to the heart of the Empire!", eDialogPic.CREATURE, 130, ["OK"])

def SoutheasternStolgrad_2422_MapTrigger_35_36(p):
    MessageBox("This is one of the guardhouses on the Nelon-Imperial border. The guards check your papers and allow you to proceed.")
    if StuffDone["54_0"] == 250:
        return
    StuffDone["54_0"] = 250
    WorldMap.DeactivateTrigger(Location(156,197))
    ChoiceBox("You arrive at the Imperial Sector, the center of the Empire and the entire world. It is within this Sector that tens of thousands of decisions are made each day about public policy by various officials and bureaucrats.\n\nIt is here where most of Pralgad\'s soldiers (including you) are trained. Armies are housed within the sector to help maintain security and order. The protection of the capital of the Empire, Solaria, is paramount.\n\nThe Imperial Sector is probably the most densely populated sector in the world. Census figures say that about five million people live and work within the sector with jobs ranging from administration to clerical to maintenance.\n\nThe size will soon become apparent as you will see the many residential areas that dot the landscape. Each has its own name, but largely these dwellings are insignificant.\n\nThe Imperial Sector is also the largest consumers of resources. The upper class residents here tend to be the wealthiest in the world. The chief product of the Imperial Sector is policy, and little else also making it the most dependent.\n\nWelcome to the heart of the Empire!", eDialogPic.CREATURE, 130, ["OK"])

def SoutheasternStolgrad_2423_MapTrigger_23_5(p):
    ChoiceBox("This is a guardpost for the Stolgradian army. The Stolgrad Sector is unique in that it is the only sector remaining on Pralgad to raise and maintain its own military forces.\n\nThis is due to the fact that Stolgrad is the only sector that is still under the control of an order of nobility. The nobles have always retained their rights to control their own forces for internal security from other nobles.\n\nAt one time, all of the sectors on Pralgad were like Stolgrad with each one controlled by some noble order or another. However, as the centuries passed, the noble orders were disposed of one by one through rebellion or just died off.\n\nThe Empire decided not to grant new titles of nobility to replace the fallen ones because of the risk to the center associated with powerful figures. So, they let them die off on their own and the Stolgrad Sector is the only one remaining.", eDialogPic.CREATURE, 13, ["OK"])
    p.CancelAction = True

def SoutheasternStolgrad_2425_MapTrigger_3_29(p):
    result = ChoiceBox("There is a spooky hut ahead. The yard is decorated with bones, skulls, and a large pentagram. This place is definitely not anybody\'s summer cottage. Do you dare to take a closer look?", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        if StuffDone["47_2"] == 0:
            if Party.CountItemClass(34, False) > 0:
                result = ChoiceBox("You knock at the door and are greeted by an ancient hag. She cackles upon answering the door and invites you inside for some drinks. You reluctantly follow her inside her home.\n\nUpon your entry, you are serviced by spirits. Your cloaks are removed and you are handed mugs and poured drinks. \"That is my special brew. Do not worry, it is harmless.\"\n\nShe then begins to smell. \"I smell something, a distinct...yes! You have something I am looking for! The horn of a golden unicorn. I simply must have one for these special recipes...\" She begins to think.\n\nAfter a brief pause, she resumes. \"I will tell you what, if you give me the golden unicorn horn, I will give you a very good discount on my most potent brews. What do you say?\"\n\nDo you ACCEPT the offer to give her the gold unicorn horn? OR Do you BUY some of her potions anyway? OR Do you LEAVE?", eDialogPic.CREATURE, 29, ["Leave", "Buy", "Accept"])
                if result == 1:
                    OpenShop("Shop_Items_Outside_8_2_1")
                    p.CancelAction = True
                    return
                elif result == 2:
                    if Party.CountItemClass(34, True) > 0:
                        StuffDone["47_2"] = 1
                        Animation_Hold(-1, 040_thankyou)
                        Wait()
                        OpenShop("Shop_Items_Outside_15_2_1")
                        p.CancelAction = True
                        return
                    return
                MessageBox("You decline the offer and finish up your drink. She asks you many questions about the news around the world and you share what you know. Afterward, you depart.")
                return
            result = ChoiceBox("You knock at the door and an ancient hag emerges. She cackles quite loudly and invites you to come inside for some drinks. You reluctantly follow her inside her home.\n\nThe interior is even more grim than the outside. Skulls adorn the walls as trophies and even a few skeletons hang from the ceiling. You also notice that some spirit is mixing and adding ingredients the many bubbling cauldrons.\n\n\"It is not often that I receive visitors. I guess my outside decorations scare most of them away. Anyway, I should serve you some of my special brew. Do not worry, it is harmless.\"\n\nSeveral spirits come and serve you drinks. \"Well now, since you\'re visiting, I suppose you wouldn\'t want to purchase some nice potions. They are extremely potent, I tell you.\"", eDialogPic.CREATURE, 29, ["Leave", "Buy"])
            if result == 1:
                OpenShop("Shop_Items_Outside_8_2_1")
                p.CancelAction = True
                return
            MessageBox("You decline the offer and finish up your drink. She asks you many questions about the news around the world and you share what you know. Afterward, you depart.")
            return
        result = ChoiceBox("You return to the witch\'s hut. Do you want to buy some of her strong potions at a special discount price?", eDialogPic.CREATURE, 29, ["Leave", "Buy"])
        if result == 1:
            OpenShop("Shop_Items_Outside_15_2_1")
            p.CancelAction = True
            return
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheasternStolgrad_2426_MapTrigger_32_25(p):
    if StuffDone["47_3"] == 250:
        return
    StuffDone["47_3"] = 250
    WorldMap.DeactivateTrigger(Location(128,73))
    MessageBox("Although the continent of Pralgad is relatively dormant as far as volcanos go, there are some hot spots. Ahead of you is a smoking caldera with bubbling molten rock. You should be very careful here!")

def SoutheasternStolgrad_2427_MapTrigger_29_28(p):
    if StuffDone["47_4"] == 0:
        Animation_Hold(-1, 046_growl)
        Wait()
        result = ChoiceBox("These molten regions often provide refuge to reptilian creatures of the fiery variety. This particular region happens to be indicative of this trend. In the crags ahead are several gigantic lizards.\n\nUsually these creatures tend to be quite pesky by snacking on the periodic travelers below. It would definitely be a service to the area if you were to exterminate them.", eDialogPic.CREATURE2x1, 1, ["Leave", "Attack"])
        if result == 1:
            if StuffDone["47_4"] == 250:
                return
            StuffDone["47_4"] = 250
            WorldMap.AlterTerrain(Location(125,76), 1, None)
            WorldMap.DeactivateTrigger(Location(125,76))
            MessageBox("You charge the lizards. Instinctively, more lizards rush out from behind the rocks to aid in the defense of the lair.")
            WorldMap.SpawnNPCGroup("Group_2_1_4", p.Target)
            return
        p.CancelAction = True
        return

def SoutheasternStolgrad_2428_MapTrigger_6_10(p):
    ChoiceBox("The Stolgrad Sector has a different philosophy of work. Most sectors have bought into the system of free enterprise and are moving away from the quaint methods of forced peasantry labor.\n\nHowever, Stolgrad is old fashioned in this sense. The authority assigns work to the peasants based upon their skills. Most of them are forced into various labor camps like this one.\n\nUnder the strict supervision of ruthless soldiers, the peasants carry out their often grueling tasks. The only incentives are the meager meals, the housing provided by the authority, and a reprieve from harsh punishment.\n\nYou would say you prefer the methods in the other sectors over this one.", eDialogPic.CREATURE, 2, ["OK"])
    p.CancelAction = True

def SoutheasternStolgrad_2429_MapTrigger_10_18(p):
    ChoiceBox("Stolgrad, unlike all the other sectors of Pralgad, is still under the control of a group of nobles. These noble orders go back to, or even before, the beginning of the Empire on Pralgad.\n\nHowever, over time most of these nobles have failed to sustain themselves and have died out. In fact, the order of Odin (the ruling nobility of Stolgrad) is the only one left standing on the continent.\n\nIt is no secret that the nobles have some of the highest standards of living in the world. Before you is a well-guarded luxurious mansion which is used as housing for the nobles.\n\nThe mansion, being very ancient is adorned with classical figures of gargoyles and all sorts of creatures. From a distance it looks to be a very imposing sight, but it has a certain classical feel to it.", eDialogPic.CREATURE, 130, ["OK"])
    p.CancelAction = True

def SoutheasternStolgrad_2430_MapTrigger_35_12(p):
    ChoiceBox("The Stolgrad Sector has a fairly profitable system of mines. Although the output pales to that of Vantanas or the Mandahl Sector, the Stolgradian mines do have some influence in trade.\n\nMostly the minerals are used for construction featuring high quality granite, marble, and iron. However, there are also concentrations of rare metals that have magical or industrial applications which net quite a profit.", eDialogPic.TERRAIN, 194, ["OK"])
    p.CancelAction = True

def SoutheasternStolgrad_2431_MapTrigger_29_22(p):
    if StuffDone["47_5"] == 250:
        return
    StuffDone["47_5"] = 250
    WorldMap.DeactivateTrigger(Location(125,70))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Mountains and hills are likely areas to have an encounter with vicious reptiles. A large group of fire lizards, led by a couple intelligent drakes, has decided that you are going to be their next snack!", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_2_1_5", p.Target)

def SoutheasternStolgrad_2432_MapTrigger_41_11(p):
    if StuffDone["47_6"] == 250:
        return
    StuffDone["47_6"] = 250
    WorldMap.DeactivateTrigger(Location(137,59))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Mountains and hills are likely areas to have an encounter with vicious reptiles. A large group of fire lizards, led by a couple intelligent drakes, has decided that you are going to be their next snack!", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_2_1_5", p.Target)

def SoutheasternStolgrad_2433_WanderingOnMeet2(p):
    if StuffDone["9_0"] >= 7:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    if StuffDone["9_0"] < 3:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    if Maths.Rand(1,0,100) < 35:
        MessageBox("You encounter a patrol of Stolgradian soldiers. They stop you, ask questions, and check your papers. Unfortunately one of them realizes you are wanted by the authority. You decide not to go peacefully.")
        return
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SoutheasternStolgrad_2435_SpecialOnWin0(p):
    MessageBox("With the lizards slain, you conduct a more extensive search of the caves. You encounter a few young isolated lizards that you have no trouble with. Apparently they did not have very much in the way of loot. All you find is a small gem.")
    Party.GiveNewItem("Ruby_176")
