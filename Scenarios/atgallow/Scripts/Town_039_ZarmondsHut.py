
def ZarmondsHut_871_MapTrigger_21_11(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(21,11)).Num == 191:
        if StuffDone["17_3"] >= 10:
            MessageBox("While searching through this shelf, you grab one of the mundane books. It is really a switch, causing the bookshelf to move aside!")
            Town.AlterTerrain(Location(21,11), 0, TerrainRecord.UnderlayList[170])
            return
        return

def ZarmondsHut_872_MapTrigger_20_14(p):
    if StuffDone["17_3"] == 10:
        result = ChoiceBox("This chest contains the three tablets you recovered from the ruins. You wonder if you should have someone else besides Zarmond give them another look. Do you take them?", eDialogPic.TERRAIN, 125, ["Leave", "Take"])
        if result == 1:
            StuffDone["17_3"] = 11
            for x in range(8, 9):
                for y in range(15, 17):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[128])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "OrderMage_30": Town.NPCList.Remove(npc)
            SpecialItem.Give("StoneTablets")
            StuffDone["19_8"] = 1
            return
        return

def ZarmondsHut_873_MapTrigger_16_9(p):
    if StuffDone["17_3"] == 11:
        if StuffDone["19_7"] == 250:
            return
        StuffDone["19_7"] = 250
        MessageBox("Apparently Zarmond did not take to kindly to you taking the tablets. He has left in his place several nasty creatures to deal with thieves like yourselves.")
        Town.PlaceEncounterGroup(4)
        return

def ZarmondsHut_874_MapTrigger_8_15(p):
    if StuffDone["19_8"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "OrderMage_30": Town.NPCList.Remove(npc)
        return

def ZarmondsHut_876_MapTrigger_9_21(p):
    ChoiceBox("One of Zarmond\'s students is very interested in magical artifacts. In particular, he is really intrigued by an artifact called the Sphere of Thralni, which bestows the ability of flight upon the user for a short time.\n\nAccording to his studies, he believes the orb must be located somewhere within the Stolgrad Sector.", eDialogPic.STANDARD, 2, ["OK"])

def ZarmondsHut_877_TownTimer_0(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Empty_0": Town.NPCList.Remove(npc)

def ZarmondsHut_878_OnEntry(p):
    if StuffDone["18_6"] >= 1:
        if StuffDone["18_6"] < 5:
            Town.PlaceEncounterGroup(1)
            return
        if StuffDone["18_6"] >= 5:
            if StuffDone["18_6"] < 9:
                Town.PlaceEncounterGroup(2)
                return
            if StuffDone["18_6"] >= 9:
                Town.PlaceEncounterGroup(3)
                return
            return
        return

def ZarmondsHut_879_CreatureDeath4(p):
    StuffDone["19_8"] = 1
    SuspendMapUpdate()
    for x in range(8, 9):
        for y in range(15, 17):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetUnlocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()
    StuffDone["17_3"] = 12
    ChoiceBox("You deal the final blow to Zarmond. He falls to the ground and looks relieved for some reason. With his last breaths he says, \"Thank you. I am free from them now...\"\n\nAnother life has been lost in the quest to stop the disappearances. You wonder why someone would go to such great lengths to possess Zarmond and keep these tablets away from you.\n\nThey must contain something really important. Perhaps you could ask Astervis about this.", eDialogPic.CREATURE, 28, ["OK"])

def ZarmondsHut_880_TalkingTrigger4(p):
    StuffDone["18_6"] = 1
    TownMap.List["AncientRuins_40"].Hidden = False
    StuffDone["18_7"] = 1

def ZarmondsHut_881_TalkingTrigger7(p):
    if StuffDone["18_6"] >= 4:
        p.TalkingText = "\"I haven\'t found anything yet. I still need more time to look. Come back a little later.\""
        return
    if StuffDone["18_6"] < 3:
        return
    p.TalkingText = "You hand the book to Zarmond and tell him your findings. He nods solemnly, \"It is as I had suspected.\" He pages through the book. \"I\'m going to look through this for any clues. Come back a little later.\""
    StuffDone["18_6"] = 4
    SpecialItem.Take("PrescottsJournal")
    Timer(None, 500, False,  "ScenarioTimer_x_2841")

def ZarmondsHut_882_TalkingTrigger8(p):
    if StuffDone["18_6"] == 5:
        StuffDone["18_6"] = 6
        return

def ZarmondsHut_883_TalkingTrigger9(p):
    if StuffDone["18_6"] >= 8:
        p.TalkingText = "\"I\'m still not finished with my analysis, please come back later.\""
        return
    if StuffDone["18_6"] < 7:
        return
    SpecialItem.Take("StoneTablets")
    p.TalkingText = "You set the tablets on Zarmond\'s desk. He seems very pleased. \"It will take me a little while to analyze these artifacts. Come back tomorrow and I should be complete.\""
    StuffDone["18_6"] = 8
    Timer(None, 500, False,  "ScenarioTimer_x_2816")

def ZarmondsHut_884_TalkingTrigger10(p):
    if StuffDone["18_6"] < 10:
        StuffDone["18_6"] = 10
        StuffDone["17_3"] += 1
        if StuffDone["17_3"] == 250:
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(19,56))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(17,55))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(15,20))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(17,20))
            TownMap.List["ZarmondsHut_39"].DeactivateTrigger(Location(20,14))
            TownMap.List["ZarmondsHut_39"].DeactivateTrigger(Location(16,9))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(56,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(55,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(57,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(50,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(52,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(53,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(55,16))
            TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(24,33))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(28,24))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(11,35))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(11,36))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(14,28))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(28,20))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(15,28))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(56,33))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(29,51))
            TownMap.List["ForgottenAcademy_60"].AlterTerrain(Location(4,13), 1, None)
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(4,13))
            TownMap.List["ForgottenAcademy_60"].AlterTerrain(Location(5,13), 1, None)
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(5,13))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(4,10))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(5,10))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(3,4))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(9,11))
        ChoiceBox("\"I have analyzed the tablets. Unfortunately, they are just casual administrative announcements explaining the abandonment policies -- nothing more. They provide no clues about the disappearances or much else.\n\nI am sorry they do not provide information you are looking for. But your help has been,\" he pauses, \"most appreciated. I have nothing else for you. You may be leaving now.\"", eDialogPic.STANDARD, 6, ["OK"])
        return
