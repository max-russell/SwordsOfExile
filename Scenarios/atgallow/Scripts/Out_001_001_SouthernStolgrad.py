
def SouthernStolgrad_2402_MapTrigger_14_39(p):
    if StuffDone["111_1"] == 0:
        result = ChoiceBox("Deep within the wooded areas of the forest you discover a path of Comfrey Root, a weak, but useful alchemetical ingredient. It is yours for the picking!", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You harvest some of the Comfrey Root. You are careful to make sure you do not harvest too deep to ensure that the plant will regenerate. This usually takes a couple days.")
            Party.GiveNewItem("ComfreyRoot_364")
            RunScript("ScenarioTimer_x_2832", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("You return to the patch of Comfrey Root, hoping that more has grown back yet. However, there are not sufficient quantities to harvest more. You will need to wait a bit longer.")

def SouthernStolgrad_2403_MapTrigger_22_10(p):
    ChoiceBox("The southern part of Stolgrad are dominated by rich forests, making the sector one of the chief exporters of lumber in the world. This facility is dedicated to the harvesting of these forests.\n\nAdditionally, this sawmill exemplifies the Stolgradian methods of labor. The officials of Stolgrad assign and compel labor through threats and constant beating of the laborers.\n\nThis method of fear is proven effective, but is not used commonly in the world anymore.", eDialogPic.TERRAIN, 152, ["OK"])
    p.CancelAction = True

def SouthernStolgrad_2404_MapTrigger_16_32(p):
    if Party.HasTrait(Trait.Woodsman):
        WorldMap.AlterTerrain(Location(65,80), 0, TerrainRecord.UnderlayList[2])
        if StuffDone["46_0"] == 250:
            return
        StuffDone["46_0"] = 250
        MessageBox("Your knowledge of the woods and forests tells you that this grove of trees has been fairly well traveled. In fact, you are even able to discover a way to get through the trees ahead.")
        return

def SouthernStolgrad_2406_MapTrigger_21_30(p):
    if StuffDone["46_1"] == 250:
        return
    StuffDone["46_1"] = 250
    WorldMap.DeactivateTrigger(Location(69,78))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("Thick forests are very popular places for bandits to hide and this one is no exception. You have just managed to stumble onto a fair sized encampment of tough looking bandits.\n\nUnfortunately, they don\'t take to kindly to soldiers invading their camp.", eDialogPic.CREATURE, 4, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_1_4", p.Target)

def SouthernStolgrad_2407_MapTrigger_21_34(p):
    if StuffDone["46_2"] == 250:
        return
    StuffDone["46_2"] = 250
    WorldMap.DeactivateTrigger(Location(69,82))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("Thick forests are very popular places for bandits to hide and this one is no exception. You have just managed to stumble onto a fair sized encampment of tough looking bandits.\n\nUnfortunately, they don\'t take to kindly to soldiers invading their camp.", eDialogPic.CREATURE, 5, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_1_5", p.Target)

def SouthernStolgrad_2408_MapTrigger_8_14(p):
    if StuffDone["46_3"] == 250:
        return
    StuffDone["46_3"] = 250
    WorldMap.DeactivateTrigger(Location(56,62))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("Forests are typical places for bandits to stage ambushes. Unfortunately, you have just fallen prey to such a one.", eDialogPic.CREATURE, 4, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_1_6", p.Target)

def SouthernStolgrad_2409_MapTrigger_31_17(p):
    if StuffDone["46_4"] == 250:
        return
    StuffDone["46_4"] = 250
    WorldMap.DeactivateTrigger(Location(79,65))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("Forests are typical places for bandits to stage ambushes. Unfortunately, you have just fallen prey to such a one.", eDialogPic.CREATURE, 4, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_1_6", p.Target)

def SouthernStolgrad_2410_MapTrigger_14_35(p):
    if StuffDone["46_5"] == 250:
        return
    StuffDone["46_5"] = 250
    WorldMap.DeactivateTrigger(Location(62,83))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("Forests are typical places for bandits to stage ambushes. Unfortunately, you have just fallen prey to such a one.", eDialogPic.CREATURE, 4, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_1_6", p.Target)

def SouthernStolgrad_2411_MapTrigger_26_23(p):
    if StuffDone["46_6"] == 250:
        return
    StuffDone["46_6"] = 250
    WorldMap.DeactivateTrigger(Location(74,71))
    WorldMap.DeactivateTrigger(Location(79,71))
    Animation_Hold(-1, 065_draining)
    Wait()
    ChoiceBox("You encounter a horrible sight. Just ahead of you is some hideous gigantic creature roaming about. As you move to take a closer look, it turns and sights you! It lets out a horrible high-pitched screech and charges you!", eDialogPic.CREATURE1x2, 3, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_1_7", p.Target)

def SouthernStolgrad_2412_MapTrigger_7_32(p):
    if StuffDone["46_7"] == 0:
        result = ChoiceBox("At the end of this trail you find the body of a young man. It appears he was trying to climb a tree, took a fall, and snapped his neck. He is obviously dead and that means you could have the sash containing several coins around his belt.", eDialogPic.TERRAIN, 179, ["Leave", "Take"])
        if result == 1:
            Party.Gold += 266
            StuffDone["46_7"] = 1
            return
        return

def SouthernStolgrad_2413_MapTrigger_31_44(p):
    result = ChoiceBox("Deep within this grove of trees you manage to uncover a natural spring with refreshing, sparkling water. You are kind of thirsty at the moment, do you take a drink?", eDialogPic.STANDARD, 18, ["Leave", "Drink"])
    if result == 1:
        Animation_Hold(-1, 056_swallow)
        Wait()
        MessageBox("You all drink from the pool. Not too long after, your bodies feel rejuvenated.")
        Party.HealAll(30)
        return

def SouthernStolgrad_2414_MapTrigger_6_21(p):
    MessageBox("Some person traveling through the forest was brutally murdered not too long ago. You look over the body and find no valuables. The body must have been looted. You know that banditry is typical in large forests like these. You should be on the lookout.")

def SouthernStolgrad_2417_WanderingOnMeet2(p):
    if StuffDone["9_0"] >= 7:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        MessageBox("You are approached by a Stolgradian patrol. They stop you, ask questions, and check your papers. Unfortunately one of them realizes that you are wanted by the authorities. You decide not to go peacefully.")
        return
    if StuffDone["9_0"] < 3:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        MessageBox("You are approached by a Stolgradian patrol. They stop you, ask questions, and check your papers. Unfortunately one of them realizes that you are wanted by the authorities. You decide not to go peacefully.")
        return
    if Maths.Rand(1,0,100) < 35:
        MessageBox("You are approached by a Stolgradian patrol. They stop you, ask questions, and check your papers. Unfortunately one of them realizes that you are wanted by the authorities. You decide not to go peacefully.")
        return
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    MessageBox("You are approached by a Stolgradian patrol. They stop you, ask questions, and check your papers. Unfortunately one of them realizes that you are wanted by the authorities. You decide not to go peacefully.")

def SouthernStolgrad_2419_SpecialOnWin0(p):
    MessageBox("Your assault has caused the bandits in this camp to disperse. With the place abandoned, you take a look around. Throughout the tents you manage to gather up a nice collection of gold and loot their food stocks.\n\nAdditionally, you manage to come across a finely carved bow with several runes set into the wood.")
    Party.GiveNewItem("MagicBow_111")
    Party.Gold += 443
    Party.Food += 37

def SouthernStolgrad_2420_SpecialOnWin1(p):
    MessageBox("Your assault has caused the bandits in this camp to disperse. With the place abandoned, you take a look around. Throughout the tents you manage to gather up a nice collection of gold and loot their food stocks.\n\nAlso in the most elegant structure, which was probably home to a wizard judging from the accommodations, you manage to uncover a golden unicorn horn! Quite a rare and valuable find in alchemy.")
    Party.GiveNewItem("GoldUnicornHorn_327")
    Party.Gold += 381
    Party.Food += 52
