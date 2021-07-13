
def SouthwesternAgran_2762_MapTrigger_37_36(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You return to the town of Ardent. The residents have huddled together to clean up and rebuild. There is nothing you can do here anymore.")

def SouthwesternAgran_2766_MapTrigger_32_17(p):
    if StuffDone["100_0"] == 2:
        if StuffDone["1_8"] == 250:
            return
        StuffDone["1_8"] = 250
        ChoiceBox("You step outside of Fort Lemmix once more. This time it is completely different. As you walk along the path, it starts to sink in that you are no longer regular soldiers of the Empire.\n\nOnly the Emperor can authorize a promotion to Imperial Guardian. He, or more likely his Prime Director, must have taken notice of your troop and decided to push you into new ranks. You are now members of an elite circle.\n\nBut still, you do not know what to do next. For the past three years of service in the Empire army, you have been told exactly what to do. Now you are, for the most part, in charge of your own decisions. You have a new autonomy you are unaccustomed to.\n\nIt may be wise to head east to the forested Wrynn Sector. Right now there is a savage war between the local Nephilim tribes. Perhaps you could gain even more status and experience there.\n\nOn the other hand, you may wish to head northward to Imperial Sector. At Vertex, the capital of the Empire and the world, you may be able to see the Prime Director and he may be able to give you direction.\n\nIn more turbulent times, heroic tales of Imperial Guardians were written. You have taken the first steps into that circle. Perhaps, you too may assume your place among the legends.", eDialogPic.STANDARD, 6, ["OK"])
        Animation_Hold(-1, 016_townentry)
        Wait()
        ChoiceBox("CHAPTER II -- AN UNEXPECTED PROMOTION", eDialogPic.STANDARD, 16, ["OK"])
        return

def SouthwesternAgran_2767_MapTrigger_32_42(p):
    if StuffDone["16_0"] >= 2:
        MessageBox("You return to the Follower\'s hut. The place appears to be the same as you left it. If anyone else visited since your last visit, you cannot tell.")
        return
    if StuffDone["16_0"] < 1:
        result = ChoiceBox("A large hut lies on the beach. The place looks to be somewhat in disrepair. You wonder if anyone is home. Care to find out?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
        if result == 1:
            StuffDone["16_0"] = 1
            ChoiceBox("The door is answered by a man in a red robe. The same kind of robe that the Followers would wear! He speaks in a raspy voice, \"We\'re not doing anything illegal here. Just having a peaceful religious worship. Please leave.\"\n\nHowever, one of the other cultists comes over and points at you. \"Hey, it\'s them! They\'re the ones who stopped our raid on Ardent. Get them!\" With that the cultists chase after you.", eDialogPic.CREATURE, 23, ["OK"])
            WorldMap.SpawnNPCGroup("Group_2_5_5", p.Target)
            return
        p.CancelAction = True
        return
    MessageBox("You return to find the Follower\'s hut abandoned. Everything has been taken. All that remains is a bloodstained sacrificial altar. You can\'t help to wonder what kind of horrid rituals were performed there.")
    p.CancelAction = True

def SouthwesternAgran_2768_MapTrigger_19_28(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran sector. Care to look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        MessageBox("You enter the village and have small talk with the farmers. However, none of them really has anything interesting to report.")
        return
    p.CancelAction = True

def SouthwesternAgran_2769_MapTrigger_5_30(p):
    if StuffDone["16_1"] == 250:
        return
    StuffDone["16_1"] = 250
    WorldMap.AlterTerrain(Location(101,270), 1, None)
    WorldMap.DeactivateTrigger(Location(101,270))
    MessageBox("You have stumbled upon a group of goblins hiding out in the hills. They don\'t take too friendly to your disturbance.")
    WorldMap.SpawnNPCGroup("Group_2_5_6", p.Target)

def SouthwesternAgran_2770_MapTrigger_12_15(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran sector. Care to look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["16_2"] >= 1:
            MessageBox("You enter the village and have small talk with the farmers. However, none of them really has anything interesting to report.")
            return
        if StuffDone["16_2"] < 1:
            MessageBox("You enter the village. Suddenly you hear a voice yell, \"Damned dirty Imperial fascists!\" You turn around to see a muscular farmer accompanied by several trained vicious giant lizards!")
            WorldMap.SpawnNPCGroup("Group_2_5_7", p.Target)
            return
        return
    p.CancelAction = True

def SouthwesternAgran_2772_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SouthwesternAgran_2773_SpecialOnWin1(p):
    StuffDone["16_0"] = 2
    ChoiceBox("With the cultists defeated, you take a look around their place. The hut is particularly mundane with the standard kitchen and living quarters. Inside you find several gold coins and some rations. However, one room is not found in a regular house.\n\nThe small room has been made into a sacrificial temple to their dark god. Bloodstains cover the altar as evidence attesting to that fact. You wonder who or what met their fate at this altar.\n\nIn a compartment beneath the altar you find a dagger. It is perfectly clean and etched with a rune. It feels oddly pleasant to the touch. You decide to take that as payment for this assault.", eDialogPic.TERRAIN, 154, ["OK"])
    Party.GiveNewItem("MagicKnife_77")
    Party.Gold += 182
    Party.Food += 34

def SouthwesternAgran_2774_SpecialOnFlee1(p):
    MessageBox("Like cowards, you managed to flee the clutches of the Followers this time.")

def SouthwesternAgran_2775_SpecialOnWin3(p):
    MessageBox("The aggressive farmer is now dead. You wonder why he would give up his life attacking Empire soldiers. It is possible that he was a member of the Followers.")
    StuffDone["16_2"] = 1

def SouthwesternAgran_2776_SpecialOnFlee3(p):
    MessageBox("The farmer cheers as you flee. \"Yeah, run away you puny wimps. Look who\'s tough now!\" You have just disgraced the Empire.")
