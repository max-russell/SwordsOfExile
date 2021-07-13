
def PortalFortress_166_MapTrigger_43_55(p):
    if StuffDone["3_2"] == 250:
        return
    StuffDone["3_2"] = 250
    TownMap.List["PortalFortress_13"].DeactivateTrigger(Location(43,55))
    MessageBox("You\'re in luck. The Troglos had kept a hidden entrance (or exit) to their fortress. It was well concealed with magic, but you discovered it anyway.")

def PortalFortress_167_MapTrigger_46_57(p):
    if StuffDone["3_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("Apparently the Troglos didn\'t leave this tunnel completely undefended. These runes ahead look like a trap. They don\'t look easy to disarm either.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("Apparently the Troglos didn\'t leave this tunnel completely undefended. These runes ahead look like a trap. They don\'t look easy to disarm either.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["3_3"] = 250
    TownMap.List["PortalFortress_13"].DeactivateTrigger(Location(46,57))
    pc.RunTrap(eTrapType.GAS, 2, 80)

def PortalFortress_168_MapTrigger_48_57(p):
    if StuffDone["3_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("Apparently the Troglos didn\'t leave this tunnel completely undefended. These runes ahead look like a trap. They don\'t look easy to disarm either.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("Apparently the Troglos didn\'t leave this tunnel completely undefended. These runes ahead look like a trap. They don\'t look easy to disarm either.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["3_4"] = 250
    TownMap.List["PortalFortress_13"].DeactivateTrigger(Location(48,57))
    pc.RunTrap(eTrapType.SLEEP_RAY, 3, 80)

def PortalFortress_169_MapTrigger_50_45(p):
    if StuffDone["3_5"] == 0:
        Animation_Hold(-1, 025_magespell)
        Wait()
        MessageBox("You hear a very loud noise of magic from the north. It sounds like somebody has activated a portal.")
        StuffDone["3_5"] = 1
        return

def PortalFortress_172_MapTrigger_31_36(p):
    if StuffDone["3_5"] == 1:
        StuffDone["3_5"] = 2
        Animation_Hold(-1, 053_magic3)
        Wait()
        ChoiceBox("You look out the gate and see a large basalt dome. It arches about fifteen meters high and radiates a strange vibration. You can see some ritual occurring through its massive entrance. That must be the portal!\n\nSuddenly, there is a brilliant flash of light within the dome. White light begins to collect within the dome. It is an awe inspiring sight to see such magics. The ritual must be nearing completion.\n\nYou aren\'t sure whether people are coming or going. You have a feeling that you will soon find out.", eDialogPic.STANDARD, 22, ["OK"])
        return

def PortalFortress_175_MapTrigger_31_26(p):
    if StuffDone["3_5"] >= 4:
        StuffDone["3_5"] = 5
        Animation_Hold(-1, 005_explosion)
        Wait()
        MessageBox("You hear a series of loud explosions. You turn around to see molten rock burst through the floor. The lava leaks out onto the surface rapidly devouring everything in it\'s wake!")
        Town.PlaceField(Location(26,8), Field.QUICKFIRE)
        return
    if StuffDone["3_5"] < 3:
        StuffDone["3_5"] = 3
        Animation_Hold(-1, 010_teleport)
        Wait()
        Town.PlaceEncounterGroup(1)
        ChoiceBox("As you enter the dome, you are nearly blinded by another flash. You look onward to see that about ten Troglodytes have appeared on the dais. This fortress must act as some sort of transport station for Troglos to move around.\n\nBeyond them, you see a Troglodyte in black clad robes at a massive control panel. Unfortunately, he notices your presence and he is none too happy. He orders the somewhat disoriented arrivals to attack!", eDialogPic.STANDARD, 22, ["OK"])
        StuffDone["4_0"] = 1
        StuffDone["4_2"] = 1
        return

def PortalFortress_178_MapTrigger_32_4(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["3_5"] >= 4:
        MessageBox("Now is not the time to have fun with these controls. This entire place is falling apart! You had better get out quickly!")
        return
    if StuffDone["3_6"] == 14:
        if StuffDone["3_7"] == 1:
            result = ChoiceBox("Remembering the instructions you had read, you believe you can open a portal using this control panel. You\'re not sure if it will accomplish your goals, but heck, you may just cause catastrophic failure or something like that!\n\nDo you want to try to use the controls now?", eDialogPic.STANDARD, 22, ["No", "Yes"])
            if result == 0:
                return
            elif result == 1:
                if StuffDone["4_0"] == 1:
                    if StuffDone["4_1"] == 1:
                        if StuffDone["4_2"] == 1:
                            if StuffDone["4_3"] == 1:
                                Animation_Hold(-1, 005_explosion)
                                Wait()
                                MessageBox("Wow! That was even better than the one you saw coming in. Also, that explosion didn\'t sound too good; you may have broken something. Unfortunately, you have company at the other side of the dome.")
                                Town.PlaceEncounterGroup(2)
                                StuffDone["3_6"] += 1
                                if StuffDone["3_6"] == 250:
                                    pass
                                return
                            MessageBox("You use the panels and it works! You get an awesome light show. Unfortunately, you have not any closer to your goal.")
                            return
                        MessageBox("You use the panels and it works! You get an awesome light show. Unfortunately, you have not any closer to your goal.")
                        return
                    MessageBox("You use the panels and it works! You get an awesome light show. Unfortunately, you have not any closer to your goal.")
                    return
                MessageBox("You use the panels and it works! You get an awesome light show. Unfortunately, you have not any closer to your goal.")
                return
            return
        MessageBox("These controls are a bit over your head. If only you had taken the time to read that lousy instruction manual... Oh well, you must have left it lying around this dungeon somewhere!")
        return
    if StuffDone["3_6"] == 22:
        result = ChoiceBox("Remembering the instructions you had read, you believe you can open a portal using this control panel. You\'re not sure if it will accomplish your goals, but heck, you may just cause catastrophic failure or something like that!\n\nDo you want to try to use the controls now?", eDialogPic.STANDARD, 22, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            Animation_Hold(-1, 005_explosion)
            Wait()
            MessageBox("Oh dear! You must have really done something wrong! There are a series of explosions causing the entire dome to shake. Parts of the ceiling fall as the quake continues.\n\nIt appears you have succeeded in destroying the portal. If you don\'t hurry, you may not escape. You had better leave now!")
            StuffDone["3_5"] = 4
            Timer(Town, 6, False, "PortalFortress_196_TownTimer_78", eTimerType.DELETE)
            return
        return
    MessageBox("As much as you would like to use these controls at this moment, there are some Troglodytes out to kill you right now. These controls will take some time to figure out, which you can\'t do while being attacked!")

def PortalFortress_179_MapTrigger_17_41(p):
    if StuffDone["3_8"] == 250:
        return
    StuffDone["3_8"] = 250
    TownMap.List["PortalFortress_13"].DeactivateTrigger(Location(17,41))
    TownMap.List["PortalFortress_13"].DeactivateTrigger(Location(17,42))
    for x in range(15, 20):
        for y in range(40, 41):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[133])
    for x in range(16, 19):
        for y in range(40, 41):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[166])
    Animation_Explosion(Location(17,40), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Party.Damage(Maths.Rand(3, 1, 4) + 10, eDamageType.WEAPON)
    Wait()
    for x in range(15, 20):
        for y in range(43, 44):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[133])
    for x in range(16, 19):
        for y in range(43, 44):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[166])
    Animation_Explosion(Location(17,43), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Party.Damage(Maths.Rand(3, 1, 4) + 10, eDamageType.WEAPON)
    Wait()
    MessageBox("Those Troglodytes have set up a trap for you! The walls on both sides are blasted by a Khazi in each hidden compartments. Not only are you hit with the rubble, you also have to deal with them as well!")

def PortalFortress_181_MapTrigger_4_39(p):
    result = ChoiceBox("This appears to be some Troglodyte spell book. Perhaps you should flip through it and you can learn a spell or two.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
            MessageBox("This is a Troglodyte prayer book. Most of the contents are arcane chants to their god \'Halloth\'. However, there are a few prayers that may be of use to you.\n\nOn further investigation, only one is really within your grasp. You memorize the prayer \'Major Heal\'!")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("p_major_heal")
            return
        MessageBox("This is a Troglodyte prayer book. Most of the contents are arcane chants to their god \'Halloth\'. However, there are a few prayers that may be of use to you.\n\nUnfortunately, those few prayers which appear useful to you are a bit over your head. You would need more \'Mage Lore\' to figure this book out.")
        return

def PortalFortress_182_MapTrigger_2_39(p):
    result = ChoiceBox("This appears to be some Troglodyte spell book. Perhaps you should flip through it and you can learn a spell or two.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        MessageBox("You start to read the book and before you realize it, the book is trapped! The words become gibberish to you. You pull away, but you still feel like your minds are full of fog.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 3))
        return

def PortalFortress_183_MapTrigger_3_39(p):
    result = ChoiceBox("This appears to be some Troglodyte spell book. Perhaps you should flip through it and you can learn a spell or two.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        StuffDone["3_7"] = 1
        ChoiceBox("This book was written to teach people how to use the Troglodytes teleporter. It looks like you\'ve struck gold! You read a summary of portal use.\n\n\"The portal is built on volcanic vents. From these vents, the machines is able to generate energy to open a portal of a specified size. These vents may be opened or closed at the four side terminals to ensure the proper energy input.\n\nFour vents can be opened and closed. General guidelines: No Vents -- No Portal, One Vent -- Weak Portal (1-5 entrants), Two Vents -- Average Portal (6-15 entrants), Three Vents -- Strong Portal (16-25 entrants), Four Vents -- Massive Portal (untested)\n\nThe use of four vents open is not recommended as it could cause damage to the machines. Even on conservative use, the energy generators need to be properly maintained from time to time. [Long and boring section on maintenance]\n\nShould the portal be operated with damaged energy generators, it could cause a system malfunction leading to catastrophic failure including the release of the pressurized magma beneath the foundation.\"\n\nYou continue to flip through and discover instructions for the control panel. You now know how to operate the portal controls!", eDialogPic.STANDARD, 22, ["OK"])
        return

def PortalFortress_184_MapTrigger_21_7(p):
    if StuffDone["4_0"] == 0:
        MessageBox("This panel has a lever on it. It is currently facing \'Closed\' on the panel. You could easily flip it to say \'Open\' if you wish.")
        result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
        if result == 0:
            if StuffDone["4_0"] == 0: StuffDone["4_0"] = 1
            else: StuffDone["4_0"] = 0
            Animation_Hold(-1, 094_lever)
            Wait()
            return
        elif result == 1:
            return
        return
    MessageBox("This panel has a lever on it. It is currently facing \'Open\' on the panel. You could easily flip it to say \'Closed\' if you wish.")
    result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
    if result == 0:
        if StuffDone["4_0"] == 0: StuffDone["4_0"] = 1
        else: StuffDone["4_0"] = 0
        Animation_Hold(-1, 094_lever)
        Wait()
        return
    elif result == 1:
        return

def PortalFortress_185_MapTrigger_21_20(p):
    if StuffDone["4_1"] == 0:
        MessageBox("This panel has a lever on it. It is currently facing \'Closed\' on the panel. You could easily flip it to say \'Open\' if you wish.")
        result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
        if result == 0:
            if StuffDone["4_1"] == 0: StuffDone["4_1"] = 1
            else: StuffDone["4_1"] = 0
            Animation_Hold(-1, 094_lever)
            Wait()
            return
        elif result == 1:
            return
        return
    MessageBox("This panel has a lever on it. It is currently facing \'Open\' on the panel. You could easily flip it to say \'Closed\' if you wish.")
    result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
    if result == 0:
        if StuffDone["4_1"] == 0: StuffDone["4_1"] = 1
        else: StuffDone["4_1"] = 0
        Animation_Hold(-1, 094_lever)
        Wait()
        return
    elif result == 1:
        return

def PortalFortress_186_MapTrigger_43_7(p):
    if StuffDone["4_2"] == 0:
        MessageBox("This panel has a lever on it. It is currently facing \'Closed\' on the panel. You could easily flip it to say \'Open\' if you wish.")
        result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
        if result == 0:
            if StuffDone["4_2"] == 0: StuffDone["4_2"] = 1
            else: StuffDone["4_2"] = 0
            Animation_Hold(-1, 094_lever)
            Wait()
            return
        elif result == 1:
            return
        return
    MessageBox("This panel has a lever on it. It is currently facing \'Open\' on the panel. You could easily flip it to say \'Closed\' if you wish.")
    result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
    if result == 0:
        if StuffDone["4_2"] == 0: StuffDone["4_2"] = 1
        else: StuffDone["4_2"] = 0
        Animation_Hold(-1, 094_lever)
        Wait()
        return
    elif result == 1:
        return

def PortalFortress_187_MapTrigger_43_20(p):
    if StuffDone["4_3"] == 0:
        MessageBox("This panel has a lever on it. It is currently facing \'Closed\' on the panel. You could easily flip it to say \'Open\' if you wish.")
        result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
        if result == 0:
            if StuffDone["4_3"] == 0: StuffDone["4_3"] = 1
            else: StuffDone["4_3"] = 0
            Animation_Hold(-1, 094_lever)
            Wait()
            return
        elif result == 1:
            return
        return
    MessageBox("This panel has a lever on it. It is currently facing \'Open\' on the panel. You could easily flip it to say \'Closed\' if you wish.")
    result = ChoiceBox("Pull the lever in the opposite direction?", eDialogPic.STANDARD, 9, ["Yes", "No"])
    if result == 0:
        if StuffDone["4_3"] == 0: StuffDone["4_3"] = 1
        else: StuffDone["4_3"] = 0
        Animation_Hold(-1, 094_lever)
        Wait()
        return
    elif result == 1:
        return

def PortalFortress_188_MapTrigger_27_52(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear the sounds of nearby machinery operating the main gates.")
        SuspendMapUpdate()
        for x in range(31, 34):
            for y in range(53, 54):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def PortalFortress_189_MapTrigger_29_57(p):
    if StuffDone["3_5"] == 5:
        Animation_Hold(-1, 005_explosion)
        Wait()
        Animation_Hold(-1, 060_smallboom)
        Wait()
        SuspendMapUpdate()
        for x in range(30, 37):
            for y in range(59, 64):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[97])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[97]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
        ResumeMapUpdate()
        StuffDone["3_5"] = 6
        MessageBox("That last explosion sent out a massive shockwave triggering a cave in. Unfortunately, that cave in blocked at your only escape route! Now what?")
        Timer(Town, 3, False, "PortalFortress_197_TownTimer_90", eTimerType.DELETE)
        return

def PortalFortress_190_MapTrigger_32_56(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,56)).Num == 78:
        ChoiceBox("It looks like you have no other choice but to use this portal. You can only hope it takes you back to the safety of Fort Reflection. Wherever it leads, you will soon find out! You all quickly jump in as the entire cavern crumbles.", eDialogPic.STANDARD, 22, ["OK"])
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(5,52)
        Party.MoveToMap(TownMap.List["Azaklan_14"])
        return

def PortalFortress_196_TownTimer_78(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    Timer(Town, 6, False, "PortalFortress_196_TownTimer_78", eTimerType.DELETE)

def PortalFortress_197_TownTimer_90(p):
    Animation_Hold(-1, 052_magic2)
    Wait()
    MessageBox("Suddenly, a mysterious portal appears! The mages at Fort Reflection must have managed to make your escape route. It looks like your only option is to go through this portal.")
    Town.AlterTerrain(Location(32,56), 0, TerrainRecord.UnderlayList[78])

def PortalFortress_198_OnEntry(p):
    if StuffDone["3_1"] == 250:
        return
    StuffDone["3_1"] = 250
    ChoiceBox("This must be the Portal Fortress. You look forward to see a foreboding sign, a large wall with closed portculli. This place is locked up tight. Not surprising, though, considering its proximity to Empire territory.\n\nYou notice the hairs on your arms begin to stand up. The air is dry and full of static. These are typical signs that you are near a portal. More powerful portals tend to give off a larger effect, so you must be in the right place.\n\nNow, getting in...", eDialogPic.TERRAIN, 232, ["OK"])

def PortalFortress_199_CreatureDeath4(p):
    StuffDone["3_6"] += 1
    if StuffDone["3_6"] == 250:
        pass

def Talking_13_8(p):
    if Party.Gold >= 18:
        Party.Gold -= 18
        p.TalkingText = "She pours you some fresh, cold brew. It has an odd greenish tint that queases you a bit. But, you decide to take a sip. As soon as you do, you down the whole drink. Glania smiles gleefully. \"Perhaps you would like some more?\""
    else:
        p.TalkingText = "You cannot afford it."

def Talking_13_9(p):
    if Party.Gold >= 18:
        Party.Gold -= 18
        p.TalkingText = "You eagerly watch as she pours you another glass of the brew. You down it, trying to savor the every delicious drop. She smiles. \"I see you are enjoying it. Say, you want to here about a tad of information?\""
    else:
        p.TalkingText = "You cannot afford it."
