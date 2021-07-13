
def NortheasternWrynn_2713_MapTrigger_30_21(p):
    if Party.HasTrait(Trait.Woodsman):
        if StuffDone["114_0"] == 0:
            result = ChoiceBox("With the aid of your woodsman skill, you locate a small patch of Asptongue Mold. Such mold is fairly uncommon and fairly valuable to alchemists. Do you take some of it with you?", eDialogPic.STANDARD, 20, ["Leave", "Take"])
            if result == 1:
                MessageBox("You harvest some of the Asptongue Mold. Now that you know where to look, you can come back in a few days after the patch regenerates to get some more!")
                Party.GiveNewItem("AsptongueMold_367")
                RunScript("ScenarioTimer_x_2825", ScriptParameters(eCallOrigin.CUSTOM))
                return
            return
        MessageBox("The Asptongue Mold has not grown back to the point where picking some more would be viable. You will need to wait another day or so.")
        return

def NortheasternWrynn_2714_MapTrigger_35_11(p):
    if StuffDone["36_0"] == 250:
        return
    result = ChoiceBox("You had noticed a strange sparkling off in the distance. Upon closer investigation, it reveals that you have stumbled onto a gemstone. You wonder how it got here. No matter, it\'s yours now if you want it.", eDialogPic.STANDARD, 30, ["Take", "Leave"])
    if result == 0:
        StuffDone["36_0"] = 250
        WorldMap.AlterTerrain(Location(275,203), 1, None)
        WorldMap.DeactivateTrigger(Location(275,203))
        Party.GiveNewItem("Sapphire_177")
    return

def NortheasternWrynn_2715_MapTrigger_35_29(p):
    if StuffDone["36_1"] == 0:
        result = ChoiceBox("In the distance, you notice the corpse of a Nephil Trader. Although it\'s far away, you believe you can make out several large spikes which appear to have impaled the body.\n\nTraders often carry lots of loot with them. Do you take a closer look?", eDialogPic.TERRAIN, 179, ["Leave", "Approach"])
        if result == 1:
            ChoiceBox("You reach the body and do a search of it. You find his sash, which is completely empty! Oh well, someone must have got here first.\n\nYou are about to leave when you see a spike land near you! You turn to see that several gigantic Spiny Worms have emerged from the hills. They are more agile then you would expect them. They are too close to escape, you must fight!", eDialogPic.CREATURE2x1, 5, ["OK"])
            StuffDone["36_1"] = 1
            WorldMap.SpawnNPCGroup("Group_5_4_4", p.Target)
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You decide it is a bit too suspicious to go out take a closer look. Oh well, someone braver soul can face the dangers and acquire the loot.")
        return
    MessageBox("The Traders body is still here, rotting away. It appears that nobody has bothered to come out here since you last visited.")

def NortheasternWrynn_2716_MapTrigger_25_11(p):
    if StuffDone["36_2"] == 250:
        return
    StuffDone["36_2"] = 250
    WorldMap.DeactivateTrigger(Location(265,203))
    Animation_Hold(-1, 064_spit)
    Wait()
    ChoiceBox("Adventuring in swamps is often said to be dangerous. Right now, you encounter a prime example of why people say that.\n\nYou find yourselves surrounded by several slugs. Normally that would not be a problem except for the fact they nearly thrice the size of you, spit highly corrosive acids, and are hungry.", eDialogPic.CREATURE2x1, 3, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_4_5", p.Target)

def NortheasternWrynn_2717_MapTrigger_26_17(p):
    if StuffDone["36_3"] == 250:
        return
    StuffDone["36_3"] = 250
    WorldMap.DeactivateTrigger(Location(266,209))
    return

def NortheasternWrynn_2718_MapTrigger_12_22(p):
    if Maths.Rand(1,0,100) < 20:
        MessageBox("The sign said to beware of snakes. It looks like you have encountered a horde of them!")
        WorldMap.SpawnNPCGroup("Group_5_4_6", p.Target)
        return

def NortheasternWrynn_2722_MapTrigger_20_20(p):
    if StuffDone["36_5"] == 250:
        return
    StuffDone["36_5"] = 250
    WorldMap.DeactivateTrigger(Location(260,212))
    MessageBox("You land on this small swampy island. The swamp gas here is very strong. In fact, the fumes are so noxious that they make you feel very ill. Perhaps you should get off this island soon and not come back.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 8))

def NortheasternWrynn_2723_MapTrigger_27_28(p):
    if StuffDone["36_6"] == 250:
        return
    result = ChoiceBox("A young Druid is trudging through the swamps. She looks at you and smiles. \"Hello. You know, I\'ve had the most wonderful day! I came out here looking for some Asptongue Mold and I struck it rich.\n\nAnyway, I found so much that there is no way I can use it all. I would sell some of it off to you dirt cheap.\"", eDialogPic.CREATURE, 30, ["Leave", "Buy"])
    if result == 1:
        StuffDone["36_6"] = 250
        WorldMap.DeactivateTrigger(Location(267,220))
        OpenShop("Shop_Items_Outside_31_5_4")
        p.CancelAction = True
        return

def NortheasternWrynn_2724_WanderingOnMeet2(p):
    if StuffDone["24_6"] == 0:
        p.CancelAction = True
        MessageBox("You are approached by a small group of Nephil Traders. They seem to take little interest in you and depart.")
        return
    if Maths.Rand(1,0,100) < 50:
        p.CancelAction = True
        MessageBox("You are approached by a small group of Nephil Traders. They seem to take little interest in you and depart.")
        return
    MessageBox("You are approached by a small group of Nephilim Traders. Apparently, they heard about your past acts against them and don\'t take too kindly to it. They decide to attack!")

def NortheasternWrynn_2725_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NortheasternWrynn_2726_SpecialOnWin1(p):
    if StuffDone["36_4"] == 250:
        return
    StuffDone["36_4"] = 250
    MessageBox("With the slugs reduced to giant acidic heaps of bloody slime, you are safe. During the course of the battle, one of you literally stumbled on a nice looking greathelmet. You go back and retrieve it.")
    Party.GiveNewItem("SteelGreathelm_162")
