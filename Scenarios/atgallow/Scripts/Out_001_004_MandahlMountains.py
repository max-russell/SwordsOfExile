
def MandahlMountains_2675_MapTrigger_21_36(p):
    if StuffDone["55_5"] == 250:
        return
    StuffDone["55_5"] = 250
    WorldMap.DeactivateTrigger(Location(69,228))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("The Mandahl Mountains are one of the few hostile places still remaining on the continent. The rugged terrain and lack of fertile soil has made settlement of this region a virtual impossibility.\n\nBecause of the lack of settlements, there are a lack of soldiers. In these situations, nasty beasts tend to proliferate and thrive. So it is no surprise to you when a group of red lizards decides to try and prey on you.", eDialogPic.CREATURE, 64, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_4_4", p.Target)

def MandahlMountains_2676_MapTrigger_21_35(p):
    if StuffDone["55_6"] == 250:
        return
    StuffDone["55_6"] = 250
    WorldMap.DeactivateTrigger(Location(69,227))
    Animation_Hold(-1, 020_yawn)
    Wait()
    ChoiceBox("All of this fighting and traveling has really begun to tire you. You look ahead to find a grassy plateau with an inn at its apex. Suddenly you imagine a nice warm bed and having a sleep not possible while camping out on this terrain.\n\nYou can barely resist the temptation to just kick back and relax for a night after your long, trying ascent up the mountain. You doubt you will have any more opportunities like this.", eDialogPic.TERRAIN, 230, ["OK"])

def MandahlMountains_2677_MapTrigger_15_30(p):
    if StuffDone["55_7"] == 0:
        Animation_Hold(-1, 020_yawn)
        Wait()
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You are really feeling tired and craving a comfortable bed. Camping just will not do in this hostile region. It is almost as if the inn is beckoning you.")
        return

def MandahlMountains_2678_MapTrigger_7_22(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("An avalanche has made further travel down this area an impossibility. You will need to go down a different route.")

def MandahlMountains_2679_MapTrigger_15_3(p):
    if StuffDone["115_0"] == 0:
        result = ChoiceBox("Although usually only found in caves, occasionally Graymold grows in rocky crags that are hidden from sunlight. Graymold is one of the rarest and most valuable alchemy ingredients and this patch is yours for the taking!", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You harvest some of the Graymold, careful to leave enough so that it can grow back to its present state in a few days. If you return then, you should be able to get more.")
            Party.GiveNewItem("Graymold_368")
            RunScript("ScenarioTimer_x_2834", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("The patch of Graymold has not yet had a chance to fully regenerate. You will need to wait another day or so before harvesting more.")

def MandahlMountains_2680_MapTrigger_30_13(p):
    if StuffDone["61_1"] < 1:
        ChoiceBox("The passage leads upward into a thick layer of clouds. Streaks of lightning decorate the gray opaque cover. Not only can you not see through it, it would also be unwise to travel through it.\n\nIf you were to do so, the lightning would surely cause your deaths.", eDialogPic.STANDARD, 0, ["OK"])
        p.CancelAction = True
        return
    if StuffDone["61_3"] == 250:
        return
    StuffDone["61_3"] = 250
    ChoiceBox("The passage leads upward into a thick layer of clouds. Streaks of lightning decorate the gray opaque cover. Not only can you not see through it, it would also be unwise to travel through it.\n\nHowever, as you near the clouds, they begin to dissipate. Eventually, a passage forms allowing you to proceed in between the clouds. It appears that device at the northern cave served some purpose after all.", eDialogPic.STANDARD, 0, ["OK"])

def MandahlMountains_2682_MapTrigger_40_28(p):
    result = ChoiceBox("There is a small grassy valley high in the Mandahl Mountain range. In the center is a lone hut. You wonder who would live this far away from civilization. Of course, there is only one way to find out.", eDialogPic.TERRAIN, 189, ["Leave", "Approach"])
    if result == 1:
        if StuffDone["61_2"] == 1:
            result = ChoiceBox("You approach the hut and greeted by an ancient woman, a witch. You follow her inside to have a fresh meal. The meal consists of fried lizard, berries, and a musty herbal tea. Not exactly pleasing, but you could not ask for more up here.\n\nYou get to talking of your adventures and she mentions the mountains. One particular item of interest is the cloud layer that perpetually covers a small section of hills not too far north of here.\n\nShe says in all her thirty years here, she has only once see the clouds clear up. This occurred a couple years ago for about a week. She has no idea why they seemed to do this or what is concealed within the clouds.\n\nYou mention that you have encountered something interesting in the hills. You tell her of the alien statue that spoke of you having the incorrect aura. The witch thinks and leaves the kitchen for a store room.\n\nA minute later she emerges with a vial of black liquid. She explains that like the color of this liquid it can mask your aura black so you can pretend to be anything you want it to be.\n\nShe offers to sell you the brew for a sum of 2000 gold which she periodically uses when she descends to purchase rare ingredients. Do you \'Accept\' this offer, or you call \'Buy\' other potions at a discounted rate.", eDialogPic.CREATURE, 29, ["Leave", "Accept", "Buy"])
            if result == 1:
                if Party.Gold >= 2000:
                    Party.Gold -= 2000
                    ChoiceBox("You pay her the gold and she gives you the brew. She says that you may drink it at any point, your aura will remain masked. Being that this is as good of a time as any, you drink up.\n\nThe liquid is perhaps the most foul tasting substance that has ever passed your lips. When you finish consuming it, you feel no effects, adverse or beneficial. You turn to the witch and she whispers a spell.\n\n\"Ah, it has worked! Your aura is anything I imagine it to be. Quite deceptive.\" After thanking the witch, you depart.", eDialogPic.STANDARD, 20, ["OK"])
                    StuffDone["61_2"] = 2
                    p.CancelAction = True
                    return
                Message("You cannot afford it.")
                p.CancelAction = True
                return
            elif result == 2:
                OpenShop("Shop_Items_Outside_24_1_4")
                p.CancelAction = True
                return
            p.CancelAction = True
            return
        result = ChoiceBox("You approach the hut and greeted by an ancient woman, a witch. You follow her inside to have a fresh meal. The meal consists of fried lizard, berries, and a musty herbal tea. Not exactly pleasing, but you could not ask for more up here.\n\nYou get to talking of your adventures and she mentions the mountains. One particular item of interest is the cloud layer that perpetually covers a small section of hills not too far north of here.\n\nShe says in all her thirty years here, she has only once see the clouds clear up. This occurred a couple years ago for about a week. She has no idea why they seemed to do this or what is concealed within the clouds.\n\nThe witch does have fair skill in alchemy. Being one of her seldom visitors, she offers to sell you some potions at discount price.", eDialogPic.CREATURE, 29, ["Leave", "Buy"])
        if result == 1:
            OpenShop("Shop_Items_Outside_24_1_4")
            p.CancelAction = True
            return
        p.CancelAction = True
        return
    p.CancelAction = True

def MandahlMountains_2683_MapTrigger_32_6(p):
    result = ChoiceBox("You enter this small cavern. After a long walk through narrow tunnels, you come to a room of alien decor. In the center is a large glowing crystal, it seems to reach out to your minds.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
    if result == 1:
        if StuffDone["61_2"] >= 3:
            MessageBox("You return to the chamber. There is still nothing of any significance.")
            p.CancelAction = True
            return
        if StuffDone["61_2"] < 2:
            StuffDone["61_2"] = 1
            ChoiceBox("You touch the crystal. Instantly, you receive a surge of energy through your body. Although it is slightly painful, it does not cause any real damage. You can feel it probe deep within you.\n\nThen the probing sensation stops. You attempt to let go, but find your arm incapable of movement. Then a mechanical voice comes from the crystal.\n\n\"Only the creators are allowed within the sanctuary. Your aura is not that of the creators. You may not proceed.\" The voice goes away and the crystal dims slightly. You are now able to pull your arm away.\n\nYou continue to investigate the chamber but find nothing of importance. You are going to have to find a way to get the proper \'aura\' if you hope to investigate this further.\n\nYou depart the cavern.", eDialogPic.TERRAIN, 168, ["OK"])
            p.CancelAction = True
            return
        StuffDone["61_2"] = 3
        ChoiceBox("You touch the crystal. Instantly, you receive a surge of energy through your body. Although it is slightly painful, it does not cause any real damage. You can feel it probe deep within you.\n\nThen the probing sensation stops. You attempt to let go, but find your arm incapable of movement. Then a mechanical voice comes from the crystal.\n\n\"Welcome creators, it is wonderful to see you have decided to return. You may now proceed into the sanctuary.\" The crystal grows dim and you can pull your hand away. However, nothing seems to change here at least.\n\nYou look around but find no difference. You start to wonder if the device is still working properly. Discovering nothing else, you depart the cavern. Perhaps the solution lies somewhere else.", eDialogPic.TERRAIN, 168, ["OK"])
        StuffDone["61_1"] = 1
        p.CancelAction = True
        return
    p.CancelAction = True
