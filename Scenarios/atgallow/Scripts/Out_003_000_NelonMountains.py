
def NelonMountains_2356_MapTrigger_25_24(p):
    if StuffDone["58_6"] == 250:
        return
    StuffDone["58_6"] = 250
    WorldMap.DeactivateTrigger(Location(169,24))
    WorldMap.DeactivateTrigger(Location(169,25))
    ChoiceBox("As you row down this river, you notice a large mountain in the distance. Although there are many mountains in the Nelon Mountain Range, that one is peculiar because of the smoke bellowing out of the tip.\n\nAn occasional rumbling can be heard coming from that direction. It is easy to conclude that there is an active volcano not to far from here. Perhaps if you are lucky, you will get to see it erupt.", eDialogPic.STANDARD, 28, ["OK"])

def NelonMountains_2358_MapTrigger_19_44(p):
    if StuffDone["58_7"] == 250:
        return
    StuffDone["58_7"] = 250
    WorldMap.DeactivateTrigger(Location(163,44))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Suddenly there is a chilly wind accompanied by the haunting \'neigh\' of a horse. You look around to see the spectral figures of several gray unicorns, or ghosts of unicorns.\n\nAlthough gray unicorns are not the most intelligent of species, they do have minor societal structure and even a patron goddess. Unfortunately, you have just trespassed on holy territory.", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_3_0_4", p.Target)

def NelonMountains_2359_MapTrigger_16_17(p):
    if StuffDone["58_8"] == 0:
        StuffDone["58_8"] = 1
        Animation_Hold(-1, 043_stoning)
        Wait()
        ChoiceBox("You come to a dead end in this passage, emphasis on the dead. The passage stops here, but you have just stumbled on to a horde of dangerous Basilisks. You would guess that the creatures do not get a lot of food up here.\n\nYou will probably make a delicious snack for them.", eDialogPic.CREATURE, 86, ["OK"])
        WorldMap.SpawnNPCGroup("Group_3_0_5", p.Target)
        return
    if StuffDone["117_0"] == 0:
        result = ChoiceBox("You have heard the legend that Basilisks are the holy guardians of the coveted Mandrake Root. The legend has held true in this instance. At the end of this passage, you find a supply of rare and valuable Mandrake Root!", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You take some of the Mandrake Root. You should be able to harvest more in a couple days.")
            Party.GiveNewItem("MandrakeRoot_370")
            RunScript("ScenarioTimer_x_2835", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return

def NelonMountains_2360_MapTrigger_11_25(p):
    if StuffDone["60_8"] == 1:
        StuffDone["60_8"] = 2
        StuffDone["59_2"] = 1
        Animation_Hold(-1, 005_explosion)
        Wait()
        ChoiceBox("You quickly emerge from the cavern just in time. You hear an extremely loud and violent explosion. You turn around to see lava jet from the tip of the volcano. It is quite a majestic sight.\n\nYou watch for several minutes, enjoying the view. Eventually, you turn to move on when you see a massive shadow emerge from the north. The shadow becomes larger and larger, it seems to be moving toward you.\n\nYou realize that it has wings. It flies overhead, not paying you any heed and descends into the active volcano. That was Khross the dragon! He is probably ready to make his adamantite.\n\nIn the mean time, his lair will not be as well defended.", eDialogPic.STANDARD, 12, ["OK"])
        return

def NelonMountains_2361_SpecialOnWin1(p):
    result = ChoiceBox("You have heard the legend that Basilisks are the holy guardians of the coveted Mandrake Root. The legend has held true in this instance. At the end of this passage, you find a supply of rare and valuable Mandrake Root!", eDialogPic.STANDARD, 20, ["Leave", "Take"])
    if result == 1:
        MessageBox("You take some of the Mandrake Root. You should be able to harvest more in a couple days.")
        Party.GiveNewItem("MandrakeRoot_370")
        RunScript("ScenarioTimer_x_2835", ScriptParameters(eCallOrigin.CUSTOM))
        return

def NelonMountains_2362_SpecialOnFlee1(p):
    StuffDone["58_8"] = 0
