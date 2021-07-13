
def HallothsCitadel_415_MapTrigger_31_47(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_4"] == 0:
        MessageBox("You had not noticed anything abnormal about these statues. However, they are not your ordinary statue. Their eyes flash red and fire force beams that shoot you back!")
        Party.Damage(Maths.Rand(4, 1, 5) + 5, eDamageType.UNBLOCKABLE)
        Wait()
        p.CancelAction = True
        return

def HallothsCitadel_418_MapTrigger_7_61(p):
    MessageBox("You find a memo on a desk. \"The new statues at the entrance hall will greater ensure master Halloth\'s safety. Nothing alive can pass them!\"")

def HallothsCitadel_419_MapTrigger_14_51(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_5"] == 250:
        return
    StuffDone["7_5"] = 250
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(56,10))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(57,10))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(58,10))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(59,11))
    MessageBox("In the passage ahead, you sight a human mage! Halloth must employ evil humans as well to work in his Citadel for whatever purpose.")

def HallothsCitadel_421_MapTrigger_19_49(p):
    result = ChoiceBox("This is a spell book of the evil magi. It could contain some useful information. However, it is likely that they may have trapped this resource also.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("This book contains many alchemetical recipes listing countless varieties of poisons, torture potions, potions of doom, and just about any vile mixture you can think of. All of them are useless. However, one interests you.\n\nBREW OF UNDEAD SIMULATION\n\nINGREDIENTS -- 2 Vampyre Fangs, 1 Specimen of Wither Moss, 1 Sample of Naga Blood, and 1 Sample Dust of Choking.  [Continues to list instructions]\n\nEFFECTS -- The user will become Undead in most aspects for a very short amount of time. However, this brew can also cause some of the body to decay slightly upon its use. Use sparingly!\n\n(To make this brew, search the cauldron when you have the necessary ingredients.)", eDialogPic.STANDARD, 20, ["OK"])
        StuffDone["7_8"] = 1
        return

def HallothsCitadel_422_MapTrigger_26_39(p):
    result = ChoiceBox("This is a spell book of the evil magi. It could contain some useful information. However, it is likely that they may have trapped this resource also.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        MessageBox("You open the book and begin to read. Suddenly you feel very dizzy. You realize that the book is actually draining some of your experience! You quickly close the book.")
        for pc in Party.EachAlivePC():
            pc.AwardXP(-20)
        return

def HallothsCitadel_423_MapTrigger_12_33(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_6"] == 250:
        return
    StuffDone["7_6"] = 250
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(53,5))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(53,4))
    MessageBox("Before you is a large library. Unfortunately, the books are of the historical and records variety, typical of the Imperial bureaucracy. Interesting! These undead have a bureaucracy just like the Empire.")

def HallothsCitadel_425_MapTrigger_17_20(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_7"] == 250:
        return
    StuffDone["7_7"] = 250
    MessageBox("You open the door and are assaulted by oppressive hot air! You gaze into the room and discover a massive volcanic forge. Several Giants have been enslaved and are manufacturing equipment.\n\nThe bloodthirsty Giants look pleased at your entry. They now get to stop pounding steel, and start pounding your skulls!")

def HallothsCitadel_427_MapTrigger_59_28(p):
    ChoiceBox("This pool has an odd clarity within it. You gaze inside the pool and it displays a bird\'s eye view of many of the places you have visited. You see Fort Reflection, Vanguard, several Troglodyte Forts, and towns throughout the Aizic Sector.\n\nYou have heard that powerful wizards have similar pools to view events and scry locations from far off distances. Halloth has constructed one. This must be part of the reason why he always knows what is going on.\n\nUnfortunately, you have no way to control the visions nor ideas to destroy the pool.", eDialogPic.STANDARD, 18, ["OK"])

def HallothsCitadel_428_MapTrigger_60_52(p):
    result = ChoiceBox("This is a spell book of the evil magi. It could contain some useful information. However, it is likely that they may have trapped this resource also.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        MessageBox("This is a directory of all of the potions in this supply room. Unfortunately, the directory only accounts for the first half of the first row of potion racks! You look through what is there, but find nothing interesting.")
        return

def HallothsCitadel_429_MapTrigger_51_20(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_9"] == 250:
        return
    StuffDone["7_9"] = 250
    MessageBox("Vampyres require blood to remain strong and active. It is only sensible that Halloth and his cronies keep around several captured citizens of the Empire for this use. You have just found their \'feeding cache\'.\n\nIn the center of the room is a bloodstained dais. Several clubs have been strewn about indicating that they harshly beat the prisoners for entertainment. Perhaps some of these people have some useful information.")

def HallothsCitadel_431_MapTrigger_58_60(p):
    if StuffDone["8_0"] == 1:
        if StuffDone["8_1"] == 0:
            Party.GiveNewItem("NagaBlood_195")
            MessageBox("Remembering what you have learned, you easily locate the vial of Naga Blood! There is only one sample here, so you had better use it wisely.")
            StuffDone["8_1"] = 1
            return
        return

def HallothsCitadel_432_MapTrigger_17_50(p):
    if StuffDone["7_8"] == 1:
        if Party.CountItemClass(8, True) > 0:
            if Party.CountItemClass(8, False) > 0:
                if Party.CountItemClass(9, False) > 0:
                    if Party.CountItemClass(10, False) > 0:
                        if Party.CountItemClass(11, False) > 0:
                            result = ChoiceBox("You have all of the required ingredients and the knowledge to make the Brew of Undead Simulation. Do you create the brew?", eDialogPic.STANDARD, 20, ["No", "Yes"])
                            if result == 0:
                                Party.GiveNewItem("VampyreFang_192")
                                return
                            elif result == 1:
                                if Party.CountItemClass(8, True) > 0:
                                    if Party.CountItemClass(9, True) > 0:
                                        if Party.CountItemClass(10, True) > 0:
                                            if Party.CountItemClass(11, True) > 0:
                                                Animation_Hold(-1, 008_bubbles)
                                                Wait()
                                                MessageBox("You have successfully created the \'Brew of Undead Simulation\'! To drink it, use it from the Special Items menu. Be careful, the brew lasts a short time and you only have enough for one drink per each member of your party!")
                                                SpecialItem.Give("BrewofUndeadSimulation")
                                                return
                                            return
                                        return
                                    return
                                return
                            return
                        Party.GiveNewItem("VampyreFang_192")
                        MessageBox("Unfortunately, you do not have all the required ingredients. You will not be able to create the potion until you do.")
                        return
                    Party.GiveNewItem("VampyreFang_192")
                    MessageBox("Unfortunately, you do not have all the required ingredients. You will not be able to create the potion until you do.")
                    return
                Party.GiveNewItem("VampyreFang_192")
                MessageBox("Unfortunately, you do not have all the required ingredients. You will not be able to create the potion until you do.")
                return
            Party.GiveNewItem("VampyreFang_192")
            MessageBox("Unfortunately, you do not have all the required ingredients. You will not be able to create the potion until you do.")
            return
        MessageBox("Unfortunately, you do not have all the required ingredients. You will not be able to create the potion until you do.")
        return

def HallothsCitadel_433_MapTrigger_28_43(p):
    if StuffDone["8_2"] < 2:
        StuffDone["8_2"] += 1
        if StuffDone["8_2"] == 250:
            TownMap.List["HallothsCitadel_21"].DeactivateTrigger(Location(28,43))
            TownMap.List["HallothsCitadel_21"].DeactivateTrigger(Location(36,43))
        Animation_Hold(-1, 034_button1)
        Wait()
        Message("Click!")
        if StuffDone["8_2"] >= 2:
            MessageBox("A large section of the wall begins to fade away revealing a passage!")
            for x in range(31, 34):
                for y in range(36, 38):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
            return
        Timer(Town, 7, False, "HallothsCitadel_439_TownTimer_43", eTimerType.DELETE)
        return

def HallothsCitadel_435_MapTrigger_30_35(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(31,36)).Num == 139:
            MessageBox("A large section of the wall begins to fade away revealing a passage!")
            for x in range(31, 34):
                for y in range(36, 38):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
            return
        MessageBox("Nothing happens!")
        return

def HallothsCitadel_436_MapTrigger_32_32(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(16,28)
    Party.MoveToMap(TownMap.List["UpperTower_22"])

def HallothsCitadel_439_TownTimer_43(p):
    if StuffDone["8_2"] < 2:
        Animation_Hold(-1, 034_button1)
        Wait()
        Message("Click!")
        StuffDone["8_2"] = 0
        return
