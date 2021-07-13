
def SoutheasternAgran_2777_MapTrigger_18_39(p):
    result = ChoiceBox("You come to a very serene hut. It is made from adobe and has plants growing all over its surface. This entire island is covered in rows of exotic varieties of flowers. The occupants of this place must really be into nature.\n\nKnock at the door and see if anyone is home?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        result = ChoiceBox("You knock and the door is answered by a beautiful young woman. \"Ah Empire solders! What brings you to our humble island? Please, come on in and enjoy some herbal tea.\" You come inside and are seated.\n\nThe inside of the home is no less in tune with nature than the outside. Plants are hanging everywhere. You spot an older woman who enters and smiles. The younger woman brings over the tea. You take a sip and it tastes refreshing.\n\n\"Good is it not? I\'m sorry but I forgot to introduce myself. I am Serenity and this is Sunlight (pointing to the older woman). There are three others out in the pastures, Purity, River, and Rain. We are druids and live in our serene abode.\"\n\nYou tell them that you are just patrolling the countryside like good soldiers. \"It\'s great to see visitors from time to time. The farmers are always so hard working, but they come by from time to time.\n\nSay we grow a few herbs suitable for alchemy here. Perhaps you would like to purchase some. How about it?\"", eDialogPic.CREATURE, 30, ["Leave", "Buy"])
        if result == 1:
            OpenShop("Shop_Items_Outside_5_3_5")
            p.CancelAction = True
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You decline the offer. \"That is very well. Feel free to come back and visit anytime.\"")
        return
    p.CancelAction = True

def SoutheasternAgran_2778_MapTrigger_32_9(p):
    if StuffDone["15_8"] >= 2:
        MessageBox("You return to this grim farming village. The place has been looted, demolished, and burned to the ground. The battered bodies of dead farmers and even children are scattered about. A very sickening sight that could have been prevented.")
        return
    if StuffDone["15_8"] < 1:
        result = ChoiceBox("You approach this farming community and immediately sense something wrong. In the distance you hear the sound of conflict. You rush to the noises and find the source of the trouble.\n\nThe villagers are being attacked by members of that cult, the \"Followers\". The farmers are not faring well. Both sides are too busy to notice you. Your duty as Empire soldiers compels you to assist. However, you could just walk away unnoticed.", eDialogPic.CREATURE, 23, ["Attack", "Flee"])
        if result == 0:
            MessageBox("You join the fray. The Followers look somewhat scared that Empire soldiers should decide to join in. However, their leader commands them to keep on fighting.")
            WorldMap.SpawnNPCGroup("Group_3_5_4", p.Target)
            StuffDone["15_8"] = 2
            return
        elif result == 1:
            MessageBox("You decide to leave the villagers to fend for themselves. You doubt they stand a chance against those lunatics.")
            StuffDone["15_8"] = 2
            p.CancelAction = True
            return
        return
    result = ChoiceBox("You return to the farming village that you helped save. The farmers instantly welcome you and treat you to a nice meal. One of them offers to sell you some rations at very discounted prices. Do you take him up on his offer?", eDialogPic.CREATURE, 2, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_15_3_5")
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheasternAgran_2779_MapTrigger_11_6(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran Sector. Care to have a look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        MessageBox("You take a look around and speak with the locals. Aside from the usual reports, you discover nothing out of the ordinary.")
        return
    p.CancelAction = True

def SoutheasternAgran_2781_MapTrigger_3_42(p):
    if StuffDone["15_9"] == 250:
        return
    StuffDone["15_9"] = 250
    WorldMap.AlterTerrain(Location(147,282), 1, None)
    WorldMap.DeactivateTrigger(Location(147,282))
    MessageBox("Uh oh! You\'ve just stumbled into a group of goblins. They don\'t take too kindly to your disturbance either. The bloodthirsty beasts attack!")
    WorldMap.SpawnNPCGroup("Group_3_5_5", p.Target)

def SoutheasternAgran_2782_MapTrigger_36_21(p):
    if StuffDone["100_0"] < 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("This bridge separates the Agran Sector from the Wrynn Sector. Unfortunately, this is where your jurisdiction ends. The guards will not let you cross without the appropriate paperwork.")
        return
    MessageBox("This bridge is the border between the Wrynn Sector and the Agran Sector. The guards check your papers and allow you to proceed.")

def SoutheasternAgran_2784_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SoutheasternAgran_2785_SpecialOnWin0(p):
    StuffDone["15_8"] = 1
    MessageBox("With the hostile cultists dead, the farmers rejoice. After much joyful celebration, you are presented with a potion and several packs of rations. The farmers invite you back anytime you wish.")
    Party.GiveNewItem("WeakHealingP_261")
    Party.Food += 75

def SoutheasternAgran_2786_SpecialOnFlee0(p):
    MessageBox("You decide to flee the battle. Unfortunately, your intervention was not enough to save the farmers from death. The Followers loot the village and set it ablaze.")
    StuffDone["15_8"] = 2
