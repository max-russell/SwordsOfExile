
def BeneathZenithKeep_1117_MapTrigger_24_22(p):
    result = ChoiceBox("This stairway leads back up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if StuffDone["26_0"] == 1:
            MessageBox("Trying to leave was not wise. You hear the voice, \"How utterly rude! I\'ll show them. Take that!\" You feel a jolt of energy burst through you, as if something had exploded inside of you. Without your vital organs, you quickly die.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(25,20)
        Party.MoveToMap(TownMap.List["ZenithKeep_30"])
        return

def BeneathZenithKeep_1119_MapTrigger_33_40(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        SuspendMapUpdate()
        for x in range(32, 36):
            for y in range(29, 41):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetUnlocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        if StuffDone["25_4"] == 250:
            return
        StuffDone["25_4"] = 250
        MessageBox("Pulling the lever causes all of the cells to open up. Suddenly, you hear loud moans. It seems you have quite literally awakened the dead!")
        Town.PlaceEncounterGroup(1)
        return

def BeneathZenithKeep_1120_MapTrigger_41_14(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["25_5"] == 0:
            MessageBox("You pull the lever. You hear loud, clanky machinery begin to turn within the walls. Soon, a smooth deafening hum emerges. You believe you have just turned on the power.")
            StuffDone["25_5"] = 1
            if StuffDone["26_0"] == 0:
                StuffDone["26_0"] = 1
                ChoiceBox("Suddenly, you hear a growl like voice. \"What is this? Energy? Finally, I am awake! How long has it been...\" the voice trails off. Suddenly you get the sensation that you have just been scryed.\n\nThe voice returns, \"Ah, so someone has decided to come and visit. Now I don\'t want them leaving on me, that would be rude. Let\'s see, what should I do? Ah, I know! I should place a curse on them!\n\nYes, a curse. What an excellent idea! Now they will never be able to leave!\" You begin to feel quite heavy. It is as if a heavy weight has been placed inside of you. \"Won\'t this be fun? If they try to leave, the curse will kill them! Mwa, ha, ha!\"\n\nOh dear! It appears that you have awakened something evil and whatever it is does not want you to leave.", eDialogPic.STANDARD, 8, ["OK"])
                return
            return
        MessageBox("You hear the loud machinery grind to a screeching halt. The room is now completely silent.")
        StuffDone["25_5"] = 0
        return

def BeneathZenithKeep_1121_MapTrigger_54_15(p):
    if StuffDone["25_6"] == 0:
        Party.GiveNewItem("Prismitite_388")
        MessageBox("Among the rubble, you notice a shiny glint. You move the stones away to reveal a nice looking gemstone!")
        StuffDone["25_6"] = 1
        return

def BeneathZenithKeep_1122_MapTrigger_31_49(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(31,46)).Num == 173:
            if StuffDone["25_5"] == 1:
                MessageBox("You press the button and begin to hear a loud crackling sound. Something ethereal begins to take shape over the runes. After about ten minutes, a portal has materialized. My this instrument is quite crude!")
                Town.AlterTerrain(Location(31,46), 0, TerrainRecord.UnderlayList[78])
                return
            MessageBox("You press the button, but nothing happens. Perhaps the apparatus is broken.")
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(29,45), True):
                if i.SpecialClass == 26:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 26:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 1
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 0
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 31:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 2
                return
            MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
            StuffDone["25_7"] = 0
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(29,45), True):
                if i.SpecialClass == 30:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 26:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 0
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 3
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 31:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 4
                return
            MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
            StuffDone["25_7"] = 0
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(29,45), True):
                if i.SpecialClass == 31:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 26:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 5
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 6
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,45), True):
                    if i.SpecialClass == 31:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
                StuffDone["25_7"] = 7
                return
            MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
            StuffDone["25_7"] = 0
            return
        MessageBox("You press the button and see the portal waiver for a few seconds before returning to stability. You\'re not sure if anything happened or not.")
        StuffDone["25_7"] = 0
        return

def BeneathZenithKeep_1123_MapTrigger_31_46(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(31,46)).Num == 78:
        result = ChoiceBox("There is a glowing portal here. It is not nearly as stable as you are accustomed to with such crude technologies behind it. However, if everything is done correctly, it should work. Do you dare enter?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            if StuffDone["25_8"] == 0:
                if StuffDone["25_7"] >= 2:
                    if StuffDone["25_7"] >= 4:
                        if StuffDone["25_7"] >= 6:
                            if StuffDone["25_7"] < 7:
                                if Game.Mode == eMode.COMBAT:
                                    p.CancelAction = True
                                    return
                                Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                                for n in range(9):
                                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                                    Animation_Pause(50)
                                Wait()
                                Party.Reposition(Location(22,25))
                                p.CancelAction = True
                                Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                                for n in range(9):
                                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                                    Animation_Pause(50)
                                p.CancelAction = True
                                return
                            if Game.Mode == eMode.COMBAT:
                                p.CancelAction = True
                                return
                            Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                            for n in range(9):
                                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                                Animation_Pause(50)
                            Wait()
                            Party.Reposition(Location(59,50))
                            p.CancelAction = True
                            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                            for n in range(9):
                                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                                Animation_Pause(50)
                            p.CancelAction = True
                            return
                        if StuffDone["25_7"] < 5:
                            if Game.Mode == eMode.COMBAT:
                                p.CancelAction = True
                                return
                            Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                            for n in range(9):
                                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                                Animation_Pause(50)
                            Wait()
                            Party.Reposition(Location(20,35))
                            p.CancelAction = True
                            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                            for n in range(9):
                                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                                Animation_Pause(50)
                            p.CancelAction = True
                            return
                        if Game.Mode == eMode.COMBAT:
                            p.CancelAction = True
                            return
                        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                        for n in range(9):
                            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                            Animation_Pause(50)
                        Wait()
                        Party.Reposition(Location(7,23))
                        p.CancelAction = True
                        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                        for n in range(9):
                            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                            Animation_Pause(50)
                        p.CancelAction = True
                        return
                    if StuffDone["25_7"] < 3:
                        if Game.Mode == eMode.COMBAT:
                            p.CancelAction = True
                            return
                        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                        for n in range(9):
                            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                            Animation_Pause(50)
                        Wait()
                        Party.Reposition(Location(22,45))
                        p.CancelAction = True
                        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                        for n in range(9):
                            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                            Animation_Pause(50)
                        p.CancelAction = True
                        return
                    if Game.Mode == eMode.COMBAT:
                        p.CancelAction = True
                        return
                    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                    for n in range(9):
                        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                        Animation_Pause(50)
                    Wait()
                    Party.Reposition(Location(37,3))
                    p.CancelAction = True
                    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                    for n in range(9):
                        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                        Animation_Pause(50)
                    p.CancelAction = True
                    return
                if StuffDone["25_7"] < 1:
                    MessageBox("You enter this portal and your matter is propelled on a parallel trajectory, never to converge and reform again. Perhaps using these portals so liberally was not a good idea.")
                    for pc in Party.EachAlivePC():
                        if pc.LifeStatus == eLifeStatus.ALIVE:
                            pc.Kill(None, eLifeStatus.DUST, True)
                            Wait()
                    return
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                Wait()
                Party.Reposition(Location(31,13))
                p.CancelAction = True
                Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                p.CancelAction = True
                return
            MessageBox("You enter this portal and your matter is propelled on a parallel trajectory, never to converge and reform again. Perhaps using these portals so liberally was not a good idea.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        p.CancelAction = True
        return

def BeneathZenithKeep_1124_MapTrigger_30_51(p):
    ChoiceBox("Most of these ancient documents are rotted away. The ones that you can partially make out have dates from the Aizonic Empire! These documents are over a thousand years old.\n\nOne document that survived details the portal research. Apparently teleportation was a rather new field back when this place was constructed and they were doing experiments on targeting.\n\n\"Unlike other portals of the day, this portal will allow a user to target a specific location and readily change the settings to choose new targets. The control panel first activates the portal, and second targets based on gem configuration.\n\n[Next section has rotted away, but some gemstone listings are intact]. DREAM QUARTZ -- Color: pink-red, Density: 6.02, Refractability: 1.64, Structure Type: III, Shattering Point: 418 C, Relative Durability: 68%, Enchantability Rating: II.\n\nPRISMITITE -- Color: clear, Density: 3.37, Refractability: 1.12, Structure Type: III, Shattering Point: 112 C, Relative Durability: 9%, Enchantability Rating: IV.\n\nVULCAN AMBER -- Color: pale green, Density: 7.77, Refractability: 1.54, Structure Type: II, Shattering Point: 189 C, Relative Durability: 41%, Enchantability Rating: II.\"", eDialogPic.STANDARD, 22, ["OK"])

def BeneathZenithKeep_1125_MapTrigger_31_51(p):
    MessageBox("Most of these ancient documents are rotted away. The ones that you can partially make out have dates from the Aizonic Empire! These documents are over a thousand years old.")

def BeneathZenithKeep_1131_MapTrigger_28_53(p):
    MessageBox("Most of these ancient documents are rotted away. The ones that you can partially make out have dates from the Aizonic Empire! These documents are over a thousand years old.\n\nYou find some intact information on the portal. \"To target, place appropriate gemstones on two northern pedestals and press button. It is imperative that...[rotted away]...for targeting to be successful.\"")

def BeneathZenithKeep_1132_MapTrigger_16_10(p):
    result = ChoiceBox("There is a glowing portal here. It is not nearly as stable as you are accustomed to with such crude technologies behind it. However, if everything is done correctly, it should work. Do you dare enter?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["25_8"] == 0:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Animation_Vanish(Party.LeaderPC, True, "010_teleport")
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(42,38))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            p.CancelAction = True
            return
        MessageBox("You enter this portal and your matter is propelled on a parallel trajectory, never to converge and reform again. Perhaps using these portals so liberally was not a good idea.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return
    p.CancelAction = True

def BeneathZenithKeep_1133_MapTrigger_18_17(p):
    ChoiceBox("This desk contains several rotted documents. One that is probably of interest is still intact:\n\nPARALLEL STRUCTURE DISPERSION -- One important concept to the success of teleportation with gem targeting is to remember that a portal will reassemble its user at the point of convergence.\n\nThis point of convergence is determined by the structure of the gemstones. It is important to remember that using DIFFERENT gemstones of the same structure type will yield parallel solutions, which lack convergence points.\n\nThe outcome to the user of the portal is fatal. Their sub-particles will be broken down and NEVER converge at any point because of the parallel targeting. Also, it is important to consider heavily enchanted objects.\n\nThese can act as AGENTS OF PARALLELIZATION when carried by the user which cause the path to become more parallel depending on the degree of enchantment. Highly enchanted, or many enchanted objects carried will yield a lethal parallel solution.\n\nOf course, there is work on correcting these problems. The research looks encouraging, but we have yet to yield definitive results.", eDialogPic.STANDARD, 22, ["OK"])

def BeneathZenithKeep_1138_MapTrigger_39_6(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(40,4)).Num == 149:
            Town.AlterTerrain(Location(40,4), 0, TerrainRecord.UnderlayList[166])
            Animation_Explosion(Location(40,4), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Town.AlterTerrain(Location(40,5), 0, TerrainRecord.UnderlayList[166])
            Animation_Explosion(Location(40,5), 0, "005_explosion")
            Animation_Hold()
            Wait()
            if StuffDone["26_1"] == 250:
                return
            StuffDone["26_1"] = 250
            Town.PlaceEncounterGroup(2)
            ChoiceBox("You pull the lever expecting some gate to open or something like that. Instead the lever set off some violent explosives that blasted apart the wall ahead. Inside you hear several pale moans with a growling laughter.\n\nYou look inside to see a gallery of undead creatures. At the helm is an imposing Lich. \"At last, I am finally free!\" You realize that Lich has the exact same voice as the one that placed the curse upon you earlier. That must be him!\n\nUnfortunately, his undead servants look very hungry after centuries of imprisonment.", eDialogPic.CREATURE, 60, ["OK"])
            return
        return

def BeneathZenithKeep_1139_MapTrigger_52_4(p):
    MessageBox("You strike down the Lich. It\'s skeletal body quickly crumbles. The bones immediately shatter and turn to ash upon hitting the floor. You feel a great burden lifted from you.")
    StuffDone["26_0"] = 2

def BeneathZenithKeep_1140_MapTrigger_55_50(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(54,50)).Num == 147:
        MessageBox("The portculli slide open.")
        SuspendMapUpdate()
        for x in range(54, 55):
            for y in range(50, 52):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetUnlocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        if SpecialItem.PartyHas("SphereofThralni"):
            if SpecialItem.PartyHas("SphereofThralni_20"):
                MessageBox("The portculli slam shut!")
                SuspendMapUpdate()
                for x in range(54, 55):
                    for y in range(50, 52):
                        t = Town.TerrainAt(Location(x,y))
                        t = t.GetLocked()
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                return
            return
        return
    if SpecialItem.PartyHas("SphereofThralni"):
        if SpecialItem.PartyHas("SphereofThralni_20"):
            MessageBox("The portculli slam shut!")
            SuspendMapUpdate()
            for x in range(54, 55):
                for y in range(50, 52):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetLocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        return

def BeneathZenithKeep_1142_MapTrigger_53_50(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(54,50)).Num == 147:
        if SpecialItem.PartyHas("SphereofThralni"):
            SuspendMapUpdate()
            for x in range(54, 55):
                for y in range(50, 52):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        if SpecialItem.PartyHas("SphereofThralni_20"):
            SuspendMapUpdate()
            for x in range(54, 55):
                for y in range(50, 52):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        return
    if SpecialItem.PartyHas("SphereofThralni"):
        return
    if SpecialItem.PartyHas("SphereofThralni_20"):
        return
    MessageBox("The portculli slam shut!")
    SuspendMapUpdate()
    for x in range(54, 55):
        for y in range(50, 52):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetLocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()

def BeneathZenithKeep_1144_MapTrigger_59_59(p):
    if StuffDone["25_8"] == 0:
        result = ChoiceBox("There is a glowing sphere sitting in a small alcove on this pedestal. Its label says: SPHERE OF THRALNI. It looks like you have just located an extremely valuable magical artifact. Do you take it?", eDialogPic.TERRAIN, 125, ["Leave", "Take"])
        if result == 1:
            StuffDone["25_8"] = 1
            SpecialItem.Give("SphereofThralni")
            return
        return
    result = ChoiceBox("This is the same pedestal where you recovered the Orb of Thralni from. Do you put the artifact back in its appropriate spot?", eDialogPic.TERRAIN, 125, ["Leave", "Give"])
    if result == 1:
        StuffDone["25_8"] = 0
        SpecialItem.Take("SphereofThralni")
        return

def BeneathZenithKeep_1145_MapTrigger_57_59(p):
    if StuffDone["25_9"] == 0:
        result = ChoiceBox("There is a glowing sphere sitting in a small alcove on this pedestal. Its label says: SPHERE OF THRALNI. It looks like you have just located an extremely valuable magical artifact. Do you take it?", eDialogPic.TERRAIN, 125, ["Leave", "Take"])
        if result == 1:
            StuffDone["25_9"] = 1
            SpecialItem.Give("SphereofThralni_20")
            return
        return
    result = ChoiceBox("This is the same pedestal where you recovered the Orb of Thralni from. Do you put the artifact back in its appropriate spot?", eDialogPic.TERRAIN, 125, ["Leave", "Give"])
    if result == 1:
        StuffDone["25_9"] = 0
        SpecialItem.Take("SphereofThralni_20")
        return
