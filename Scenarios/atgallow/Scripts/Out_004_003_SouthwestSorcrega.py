
def SouthwestSorcrega_2637_MapTrigger_28_31(p):
    MessageBox("This bridge is the Wrynn-Sorcrega border. The guards go through the routine of checking your papers and allow you to proceed.")

def SouthwestSorcrega_2638_MapTrigger_11_5(p):
    result = ChoiceBox("This small cavern provides home to a small tribe of Slithzerikai of about ten to twelve. The lizardmen are very welcoming to Empire soldiers and are eager to discuss news and hear stories of your adventures.\n\nDuring the conversation, you learn about some order of evil wizards who live in the forests to the south. The wizards mostly keep to themselves, but they occasionally commit various atrocities, one involving the possession of a Slith.\n\nOne of the warriors is so impressed by your tales that he offers to sell you some of his spears. Do you take him up on his offer?", eDialogPic.CREATURE, 46, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_4_4_3")
        p.CancelAction = True
        return
    p.CancelAction = True

def SouthwestSorcrega_2639_MapTrigger_17_20(p):
    if StuffDone["45_1"] == 0:
        result = ChoiceBox("The sign wasn\'t kidding when it said to keep out. Whoever lives in this grove does not want visitors judging by the line of Golems guarding the passage ahead. Golems are extremely enduring guards, and will not be easy to take.\n\nThere is no way around them. If you want to get through, you will have to go through the Golems.", eDialogPic.CREATURE, 119, ["Leave", "Attack"])
        if result == 1:
            StuffDone["45_1"] = 1
            MessageBox("You engage the Golems. They immediately move to defend the passage.")
            WorldMap.SpawnNPCGroup("Group_4_3_5", p.Target)
            return
        MessageBox("You decide to heed the sign. The Golems are probably a bit too tough for you anyway.")
        p.CancelAction = True
        return

def SouthwestSorcrega_2640_MapTrigger_17_22(p):
    if StuffDone["45_2"] == 0:
        if StuffDone["45_2"] == 250:
            return
        StuffDone["45_2"] = 250
        WorldMap.DeactivateTrigger(Location(209,166))
        ChoiceBox("This field is a grove where the residents of this grove grow various crops ranging from food to herbs for alchemy. The field is tended by several Golems who are pruning and watering the crops.\n\nBeing caretakers is not their only duty apparently. They are also tasked with the defense of the grove. As soon as one of the Golems detects you, obviously a trespasser, the other Golems close in on you.", eDialogPic.CREATURE, 119, ["OK"])
        WorldMap.SpawnNPCGroup("Group_4_3_5", p.Target)
        return
    if StuffDone["113_1"] == 0:
        result = ChoiceBox("With the Golems cleared out, you are able to explore the field. Most of the herbs here are not all that useful or in too immature for you to harvest. However, there is one patch of Wormgrass that may be of use.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You harvest the wormgrass. It will be several days before you will be able to get anymore.")
            Party.GiveNewItem("Wormgrass_366")
            RunScript("ScenarioTimer_x_2829", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("The wormgrass has not yet had a chance to regenerate yet. You will need to give it another day or two.")

def SouthwestSorcrega_2641_MapTrigger_15_21(p):
    result = ChoiceBox("This tower is quite foreboding. The outside is decorated with pikes with skulls impaled upon their tips. This tower does not require another sign to warn about staying away. The image in of itself does this.\n\nDo you dare take a look inside?", eDialogPic.TERRAIN, 197, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["45_3"] == 0:
            ChoiceBox("The tower is spooky but quite small. It is only a short walk until you reach the main chamber where several wizards are performing some strange experiment involving some strange six-legged reptiles.\n\nIt also does not take long for you to be spotted. Immediately the alarm is sounded and the wizards emerge to defend their home. Worse, they sic those vicious six-legged beasts after you!", eDialogPic.CREATURE, 126, ["OK"])
            StuffDone["45_3"] = 1
            Message("Wizard Casts:")
            Message("  Mindshock")
            Animation_Hold(-1, 053_magic3)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 6))
            WorldMap.SpawnNPCGroup("Group_4_3_4", p.Target)
            return
        MessageBox("Returning to this tower does not cause you to learn anything new. The evil wizards are dead, and whatever purpose they were trying to achieve still remains a mystery.")
        p.CancelAction = True
        return
    MessageBox("You decide this place is a bit too foreboding, even for brave Empire soldiers like yourself.")
    p.CancelAction = True

def SouthwestSorcrega_2642_MapTrigger_35_7(p):
    ChoiceBox("This mage tower is called the INSTITUTE OF ALCHEMY AND DRUIDIC STUDIES. The sign says that visitors are welcome so you decide to pay the institute a visit.\n\nYou are greeted by a kind receptionist. She is a young woman in her late teens or early twenties. She serves you with some special kind of energizing herbal tea. It is quite soothing and it seems to energize you.\n\nAfter a small wait, an older woman comes to show you around the institute. The place is what you would expect consisting of classrooms, dormitories, and laboratories. Nothing really all that out of the ordinary.\n\nAt the end of the tour, you are taken to a shop where they sell a large variety of potions. Most of them are utterly useless to you. However, there are a few intended for combat and your line of work.", eDialogPic.CREATURE, 30, ["OK"])
    OpenShop("Shop_Items_Outside_35_4_3")
    p.CancelAction = True

def SouthwestSorcrega_2643_MapTrigger_38_24(p):
    ChoiceBox("Mage towers are fairly common in the Sorcrega Sector, so it is not surprising to run into one. Usually towers tend to be fairly secluded from large cities, and this one is no exception.\n\nFrom the residents, you learn this tower is a private magical training institute operated by three archwizards. They offer general training in a variety of magical arts.\n\nOne peculiarity is the fact that the apprentice dormitories are much more comfortable than the typical one located in other places. You are sure this is meant to attract prospective apprentices to this tower.\n\nGraduates of this institute go into various fields such as scrying or assisting with research. However, the people admit that this is not exactly the most prestigious institution.", eDialogPic.TERRAIN, 197, ["OK"])
    p.CancelAction = True

def SouthwestSorcrega_2644_MapTrigger_10_40(p):
    if StuffDone["45_4"] == 250:
        return
    StuffDone["45_4"] = 250
    WorldMap.DeactivateTrigger(Location(202,184))
    Animation_Hold(-1, 012_longbow)
    Wait()
    ChoiceBox("Suddenly an arrow whizzes past your head! You quickly draw your weapons and look around. Nephilim slowly emerge from the woods, dropping their weapons and placing their arms in the air.\n\nHow unusual! Could they be surrendering so easily. One of them approaches you. \"I am sorry! It was an accident, I swear! We were out hunting for game and we saw something move so I fired. I didn\'t realize...\"\n\nYou tell the Nephil that it is all right but that he should be more careful next time. The Nephilim are very gracious that you did not take too much offense to the incident and they scamper off to continue their hunt.\n\nThat was a close call!", eDialogPic.CREATURE, 39, ["OK"])

def SouthwestSorcrega_2645_WanderingOnMeet2(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SouthwestSorcrega_2647_SpecialOnWin0(p):
    ChoiceBox("The evil wizards and their bizarre pets are defeated! You decide to examine their tower and find some interesting goodies. Among them is a glowing potion, an elegant wand, and a glowing ring.\n\nYou still wonder what the wizards were doing here or what their intentions were. If they wrote anything about their plot down, it must be well hidden, for you do not manage to find any of it.", eDialogPic.CREATURE, 27, ["OK"])
    Party.GiveNewItem("RingofSpeed_316")
    Party.GiveNewItem("BrewofIronskin_212")
    Party.GiveNewItem("WandofSlow_287")

def SouthwestSorcrega_2648_SpecialOnFlee0(p):
    MessageBox("You manage to escape the wizards. Before you are able to get out of the range of their attacks, they place some disease spell on you.")
    StuffDone["45_3"] = 0
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 8))
