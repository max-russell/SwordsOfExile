
def BarrierSpire_371_MapTrigger_22_42(p):
    if StuffDone["6_4"] < 3:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You still haven\'t destroyed the barrier\'s power source. Dervish Montcalm would be very upset with you if you return without doing this.")
        return

def BarrierSpire_375_MapTrigger_42_41(p):
    if SpecialItem.PartyHas("ElevatorKey"):
        return
    result = ChoiceBox("There is a small brass key lying on this pedestal. Considering the efforts which the Troglodytes took to hide this, it must be important.", eDialogPic.TERRAIN, 125, ["Leave", "Take"])
    if result == 1:
        StuffDone["72_7"] = 1
        Message("You got \'Elevator Key\'")
        SpecialItem.Give("ElevatorKey")
        return

def BarrierSpire_376_MapTrigger_34_41(p):
    ChoiceBox("This desk has a page written on the Spire. \"The Spire consists of five levels. The levels are connected by an elevator accessible in the central chamber of the first level. The intent is to hold back intruders from reaching the top level.\n\nTo help further this, we had ensured that the elevator require additional power to reach each additional level. To give the elevator additional power, a hidden lever must be pulled on each level.\n\nUsing the elevator is fairly simple. All one needs to do is press the button to go \'up\' or \'down\'. The elevator will only go up if the energy is turned \'on\', on that floor as stated earlier...\"", eDialogPic.STANDARD, 21, ["OK"])

def BarrierSpire_377_MapTrigger_38_36(p):
    MessageBox("You find a small note. \"Remember the pattern on the second floor is: 3,2,4,1,4.\"")

def BarrierSpire_378_MapTrigger_4_38(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(13,37)).Num == 28:
        result = ChoiceBox("Upon this altar is a small stone that is out of place. It looks like you can press it down. Do you?", eDialogPic.STANDARD, 11, ["Leave", "Push"])
        if result == 1:
            Town.PlaceEncounterGroup(1)
            MessageBox("You push the button and you hear stone scraping against stone. After it stops, the runes flash! Two demons have appeared upon them and they don\'t look friendly.")
            Town.AlterTerrain(Location(13,37), 0, TerrainRecord.UnderlayList[36])
            return
        return

def BarrierSpire_379_MapTrigger_14_33(p):
    if ChoiceBox("There is a lever here labeled, \"Elevator Power\". Do you pull it?", eDialogPic.STANDARD, 213, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(14,33)).Num == 209:
            StuffDone["72_8"] += 1
            if StuffDone["72_8"] == 250:
                pass
            return
        StuffDone["72_8"] -= 1
        if StuffDone["72_8"] == 250:
            pass
        return

def BarrierSpire_380_MapTrigger_23_34(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(23,33)).Num == 145:
        if SpecialItem.PartyHas("ElevatorKey"):
            MessageBox("You use the key and the doors open revealing the elevator.")
            SuspendMapUpdate()
            for x in range(23, 25):
                for y in range(33, 34):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("These large metallic doors are locked and reinforced with magic. You could only get through if you had the right key.")
        return

def BarrierSpire_382_MapTrigger_23_30(p):
    result = ChoiceBox("This pedestal is has two buttons and is labeled \"Elevator Controls: 1 - Up, 2 - Down\".", eDialogPic.STANDARD, 11, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("Nothing happens.")
        return
    elif result == 2:
        if StuffDone["72_8"] >= 1:
            MessageBox("You press the button and the elevator moves up to the next level.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(4,25))
            p.CancelAction = True
            return
        MessageBox("Nothing happens.")
        return

def BarrierSpire_383_MapTrigger_18_27(p):
    Animation_Hold(-1, 068_identify)
    Wait()

def BarrierSpire_384_MapTrigger_18_26(p):
    Animation_Hold(-1, 061_summoning)
    Wait()

def BarrierSpire_385_MapTrigger_18_25(p):
    Animation_Hold(-1, 053_magic3)
    Wait()

def BarrierSpire_386_MapTrigger_18_24(p):
    Animation_Hold(-1, 008_bubbles)
    Wait()

def BarrierSpire_387_MapTrigger_14_22(p):
    Animation_Hold(-1, 053_magic3)
    Wait()
    StuffDone["72_9"] = 1

def BarrierSpire_388_MapTrigger_13_27(p):
    Animation_Hold(-1, 061_summoning)
    Wait()
    if StuffDone["72_9"] == 1:
        StuffDone["72_9"] += 1
        if StuffDone["72_9"] == 250:
            pass
        return
    StuffDone["72_9"] = 0

def BarrierSpire_389_MapTrigger_15_22(p):
    Animation_Hold(-1, 008_bubbles)
    Wait()
    if StuffDone["72_9"] == 2:
        StuffDone["72_9"] += 1
        if StuffDone["72_9"] == 250:
            pass
        return
    if StuffDone["72_9"] == 4:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(18,23)).Num == 147:
            MessageBox("You touch the pedestal and you hear the sound of chains to the east.")
            t = Town.TerrainAt(Location(18,23))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(18,23)).TransformTo
                Town.AlterTerrain(Location(18,23), 0, t)
            return
        return
    StuffDone["72_9"] = 0

def BarrierSpire_390_MapTrigger_15_27(p):
    Animation_Hold(-1, 068_identify)
    Wait()
    if StuffDone["72_9"] == 3:
        StuffDone["72_9"] += 1
        if StuffDone["72_9"] == 250:
            pass
        return
    StuffDone["72_9"] = 0

def BarrierSpire_391_MapTrigger_18_22(p):
    if ChoiceBox("There is a lever here labeled, \"Elevator Power\". Do you pull it?", eDialogPic.STANDARD, 213, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(18,22)).Num == 209:
            StuffDone["72_8"] += 1
            if StuffDone["72_8"] == 250:
                pass
            return
        StuffDone["72_8"] -= 1
        if StuffDone["72_8"] == 250:
            pass
        return

def BarrierSpire_392_MapTrigger_3_25(p):
    result = ChoiceBox("This pedestal is has two buttons and is labeled \"Elevator Controls: 1 - Up, 2 - Down\".", eDialogPic.STANDARD, 11, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("You push the button and the elevator takes you down.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(24,30))
        p.CancelAction = True
        return
    elif result == 2:
        if StuffDone["72_8"] >= 2:
            MessageBox("You press the button and the elevator moves up to the next level.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(25,17))
            p.CancelAction = True
            return
        MessageBox("Nothing happens.")
        return

def BarrierSpire_393_MapTrigger_32_15(p):
    if StuffDone["7_0"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Yikes! This floor is REALLY hot. Your feet are instantly burnt as you pull them back. You doubt even your \'Firewalk\' spell would work here. As long as it is so hot there is no way you will be able to cross it.")
        Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.FIRE)
        Wait()
        return

def BarrierSpire_396_MapTrigger_8_21(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_1"] == 250:
        return
    StuffDone["7_1"] = 250
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(6,7))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(10,11))
    MessageBox("The moment you touch this door, you pull your hand back in pain. It is extremely hot! You wrap several layers of cloth around your hand and manage to get it open with only minor scalds.\n\nYou are instantly assaulted by oppressively hot air. You look inside and see a large brazier burning a very hot magical flame.")
    Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.FIRE)
    Wait()

def BarrierSpire_397_MapTrigger_8_20(p):
    if StuffDone["7_0"] == 0:
        Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.FIRE)
        Wait()
        return

def BarrierSpire_402_MapTrigger_8_19(p):
    if StuffDone["7_0"] == 0:
        if Party.CountItemClass(7, False) > 0:
            result = ChoiceBox("The flames are not exactly very large, just magically made to burn hot. If you had a bucket of water, you could easily douse the flames.\n\nIn fact, you just happen to be carrying such a bucket. You probably won\'t be able to start the flames up again, so you best know what your doing. Do you douse the flames?", eDialogPic.TERRAIN, 136, ["No", "Yes"])
            if result == 0:
                return
            elif result == 1:
                count = Party.CountItemClass(7, True)
                Party.Gold += count * 0
                MessageBox("You douse the flames with your bucket of water. They instantly go out and the temperature instantly decreases.")
                Party.GiveNewItem("Bucket_187")
                StuffDone["7_0"] = 1
                return
            return
        MessageBox("The flames are not exactly very large, just magically made to burn hot. If you had a bucket of water, you could easily douse the flames.")
        return

def BarrierSpire_403_MapTrigger_29_28(p):
    if Party.CountItemClass(6, False) > 0:
        result = ChoiceBox("Right now you have an empty bucket. If for some crazy reason you wanted to fill the bucket with water, you could. Fill the bucket?", eDialogPic.STANDARD, 18, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            count = Party.CountItemClass(6, True)
            Party.Gold += count * 0
            Party.GiveNewItem("BucketwWater_188")
            return
        return

def BarrierSpire_406_MapTrigger_32_13(p):
    if ChoiceBox("There is a lever here labeled, \"Elevator Power\". Do you pull it?", eDialogPic.STANDARD, 213, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,13)).Num == 209:
            StuffDone["72_8"] += 1
            if StuffDone["72_8"] == 250:
                pass
            return
        StuffDone["72_8"] -= 1
        if StuffDone["72_8"] == 250:
            pass
        return

def BarrierSpire_407_MapTrigger_24_17(p):
    result = ChoiceBox("This pedestal is has two buttons and is labeled \"Elevator Controls: 1 - Up, 2 - Down\".", eDialogPic.STANDARD, 11, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("You push the button and the elevator takes you down.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(4,25))
        p.CancelAction = True
        return
    elif result == 2:
        if StuffDone["72_8"] >= 3:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(4,2))
            p.CancelAction = True
            return
        MessageBox("Nothing happens.")
        return

def BarrierSpire_408_MapTrigger_11_11(p):
    if ChoiceBox("There is a lever here labeled, \"Elevator Power\". Do you pull it?", eDialogPic.STANDARD, 213, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(11,11)).Num == 209:
            if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(4,7)).Num == 189:
                Animation_Hold(-1, 053_magic3)
                Wait()
                MessageBox("You pull the lever and you hear the sound of shattering stone. You turn around to see that the statues have turned into Troglodyte Defenders! They come at you like zombies ready to hack you apart.")
                SuspendMapUpdate()
                for x in range(3, 9):
                    for y in range(6, 13):
                        if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[166]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[189])
                        elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[189]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[166])
                ResumeMapUpdate()
                Town.PlaceEncounterGroup(2)
                StuffDone["72_8"] += 1
                if StuffDone["72_8"] == 250:
                    pass
                return
            StuffDone["72_8"] += 1
            if StuffDone["72_8"] == 250:
                pass
            return
        StuffDone["72_8"] -= 1
        if StuffDone["72_8"] == 250:
            pass
        return

def BarrierSpire_409_MapTrigger_3_2(p):
    result = ChoiceBox("This pedestal is has two buttons and is labeled \"Elevator Controls: 1 - Up, 2 - Down\".", eDialogPic.STANDARD, 11, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("You push the button and the elevator takes you down.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(25,17))
        p.CancelAction = True
        return
    elif result == 2:
        if StuffDone["72_8"] >= 4:
            MessageBox("You press the button and the elevator moves up to the next level.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(45,2))
            p.CancelAction = True
            return
        MessageBox("Nothing happens.")
        return

def BarrierSpire_410_MapTrigger_44_2(p):
    result = ChoiceBox("This pedestal is has two buttons and is labeled \"Elevator Controls: 1 - Up, 2 - Down\".", eDialogPic.STANDARD, 11, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("You push the button and the elevator takes you down.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(4,2))
        p.CancelAction = True
        return
    elif result == 2:
        MessageBox("Nothing happens.")
        return

def BarrierSpire_411_MapTrigger_13_22(p):
    Animation_Hold(-1, 004_bless)
    Wait()

def BarrierSpire_412_MapTrigger_14_27(p):
    Animation_Hold(-1, 052_magic2)
    Wait()

def BarrierSpire_413_OnEntry(p):
    if StuffDone["72_6"] == 250:
        return
    StuffDone["72_6"] = 250
    ChoiceBox("You step through and are in a small encampment of mages and wizards. They are busily making final checks on the Golems. To your north, you see a massive basalt structure. That must be Halloth\'s Citadel.\n\nAround the Citadel, you see innumerable small motes of light flickering in and out. You are guessing that is the barrier surrounding it. You are approached by Dervish Montcalm.\n\n\"Welcome. I suppose you have noticed the barriers. Come, let us take care of that. Time is not unlimited.\" He casts a spell and you both are teleported to the base of a tall spire. Atop the spire, you see motes like you saw around the Citadel, but more.\n\nTwo heavy basalt doors lie at the entrance to the spire. \"Stand back!\" commands Montcalm. You do so as he begins to chant. Energy builds up around him as he concentrates it into a bright red ball.\n\nIn a sudden thrust, he blasts the ball against the door. A powerful explosion blasts a hole right into the spire, allowing entry. Dervish Montcalm turns to you. \"Now it\'s your turn. Make your way to the top and destroy the energy source.\n\nThe barrier will lose its stability and fall. Quickly return to the battle encampment to the west and we will begin the assault. Good luck!\" Montcalm teleports away. You begin moving into the spire.", eDialogPic.CREATURE, 27, ["OK"])

def BarrierSpire_414_CreatureDeath13(p):
    StuffDone["6_4"] = 3
    Party.OutsidePos = Location(89, 181)
    ChoiceBox("With a mighty strike, the Power Crystal shatters into hundreds of tiny shards. Instantly, the electric charges within the air fade away. You can bet the barrier holding back the assault is degenerating rapidly.\n\nNow, it\'s time to get down to the true matter at hand.", eDialogPic.CREATURE, 123, ["OK"])
