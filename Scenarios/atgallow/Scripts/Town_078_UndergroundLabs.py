
def UndergroundLabs_1938_MapTrigger_17_23(p):
    result = ChoiceBox("There is a glowing portal here. Do you dare to enter?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(30,23)
        Party.MoveToMap(TownMap.List["AncientLab_75"])
        return
    p.CancelAction = True

def UndergroundLabs_1942_MapTrigger_40_7(p):
    ChoiceBox("Within the desk, you discover a document that gives the coordinates for different points. Apparently the pentagram in the western bunker connects to four different locations each with a programmed system of gems.\n\nHigh Risk Alchemy Cells & Residences -- Vulcan Amber, Prismitite, Prismitite, Dream Quartz, Prismitite.\n\nWestern Storage & Control Center -- Dream Quartz, Dream Quartz, Vulcan Amber, Prismitite, Dream Quartz.\n\nCentral Lab Chambers -- Vulcan Amber, Vulcan Amber, Prismitite, Vulcan Amber, Vulcan Amber.\n\nItem Augmentation -- Prismitite, Vulcan Amber, Dream Quartz, Prismitite, Dream Quartz.", eDialogPic.STANDARD, 21, ["OK"])

def UndergroundLabs_1943_MapTrigger_25_52(p):
    MessageBox("This passage has caved in a long time ago. There is no way you can proceed further this way.")

def UndergroundLabs_1956_MapTrigger_30_28(p):
    if StuffDone["65_0"] == 0:
        Party.Damage(Maths.Rand(6, 1, 5) + 30, eDamageType.MAGIC)
        Wait()
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Yikes! As soon as you attempt to cross these runes, you are thrown back by a massive jolt of energy. These runes are still active and pack quite a punch. You will either have to find a way to deactivate or bypass them.")
        return

def UndergroundLabs_1959_MapTrigger_35_56(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["65_1"] == 0: StuffDone["65_1"] = 1
        else: StuffDone["65_1"] = 0
        if StuffDone["65_1"] == 1:
            for x in range(35, 36):
                for y in range(59, 61):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
            return
        for x in range(35, 36):
            for y in range(59, 61):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])
        return

def UndergroundLabs_1960_MapTrigger_20_23(p):
    if StuffDone["65_1"] == 1:
        for x in range(35, 36):
            for y in range(59, 61):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
        return
    for x in range(35, 36):
        for y in range(59, 61):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])

def UndergroundLabs_1964_MapTrigger_24_40(p):
    result = ChoiceBox("This panel controls the \'SECURITY RUNES\' of this place. Although there are several settings, one lever labeled \'POWER\' stands out. The on/off labels are too faded to read, so you can only guess which setting is which.\n\nDo you pull it?", eDialogPic.STANDARD, 9, ["Leave", "Pull"])
    if result == 1:
        MessageBox("You pull the lever. There is a brief click, but nothing else seems to happen. Perhaps the machine is broken.")
        if StuffDone["65_0"] == 0: StuffDone["65_0"] = 1
        else: StuffDone["65_0"] = 0
        return

def UndergroundLabs_1965_MapTrigger_42_22(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        return;
    if SpecialItem.PartyHas("AstervisNPC"):
        if StuffDone["65_2"] == 0:
            StuffDone["65_2"] = 1
            ChoiceBox("The passage ahead has suffered a serious cave in. It seems that you have encountered a dead end and can travel no further. Your options down here are growing very thin.", eDialogPic.STANDARD, 4, ["OK"])
            result = ChoiceBox("Astervis turns to you and shouts. \"Here it is!\" You look at him in a confused way. \"The focal point of course. Now here is the plan so listen carefully:\n\nWhen we are ready, I shall fire a strong beam of concentrated energy through the focal point directly at the power source. Hopefully, I can take out the power source completely, but it is likely that I can only disrupt it for a short time.\n\nImmediately after this, I shall use a teleport spell to allow us to penetrate the fortress. I shall try to get as deep into it as I can, but I must work quickly and my skill in that matter is not the best.\n\nAssuming the barrier gets reestablished, there will be no way to return to the fort. This is probably the last chance to turn back, are we ready to go?\"", eDialogPic.CREATURE, 1029, ["No", "Yes"])
            if result == 0:
                MessageBox("\"Then we shall return once we are better prepared.\"")
                return
            elif result == 1:
                Party.OutsidePos = Location(264, 20)
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(58,58))
                p.CancelAction = True
                Animation_Hold(-1, 025_magespell)
                Wait()
                Animation_Explosion(Location(57,55), 2, "005_explosion")
                Animation_Hold()
                Wait()
                ChoiceBox("\"It worked! The power source has been disrupted and the barrier has fallen. We have a chance, but not for long. We must hurry!\"", eDialogPic.CREATURE, 1029, ["OK"])
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "AltrusIhrno_205": Town.NPCList.Remove(npc)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "RentarIhrno_206": Town.NPCList.Remove(npc)
                Town.PlaceEncounterGroup(1)
                Animation_Explosion(Location(1,1), 1, "005_explosion")
                Animation_Hold()
                Wait()
                ChoiceBox("Altrus looks in horror and rushes over to the crystal which is now pulsing with unstable light. He places his hands upon it and restores the crystal to a constant blue glow.\n\n\"We have been attacked!\"", eDialogPic.STANDARD, 1028, ["OK"])
                ChoiceBox("\"How did they penetrate our barrier? Give me a damage assessment.\"", eDialogPic.STANDARD, 1029, ["OK"])
                ChoiceBox("The crystal begins to glow. \"The damage is not severe Rentar. It was only a minor jolt. The barrier is now being reestablished and I have refocused it. We should now be immune to another assault of this kind.\n\nWait, I sense that our perimeter has been penetrated by a small group through teleportation during the time the barrier was disabled. I shall now activate our internal defenses.\n\nMy scry analysis reveals that they are only a minor threat. Our forces, combined with our defense measures, should be sufficient to prevent them from reaching the main chamber.\n\nMy analysis indicates that the probability of the invaders reaching here before we are able to activate the devices is near zero. Continue at your normal pace.\"", eDialogPic.CREATURE, 88, ["OK"])
                ChoiceBox("\"Fear not Rentar. The fated moment of execution draws near. Over half of the devices have been configured and are ready for release. I shall only require a few hours more and we shall succeed.\n\nOnce that moment has passed, we shall forever be victorious. No amount of power shall be able to repair them. This shall be the beginning of the end of the Empire and justice shall be had.\"", eDialogPic.STANDARD, 1028, ["OK"])
                ChoiceBox("\"Do not underestimate these creatures Altrus. They are not as primitive as they seem...\"", eDialogPic.STANDARD, 1029, ["OK"])
                Animation_Hold(-1, 004_bless)
                Wait()
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(20,33)
                Party.MoveToMap(TownMap.List["GallowsKeep_79"])
                return
            return
        result = ChoiceBox("Astervis turns to you and shouts. \"Here it is!\" You look at him in a confused way. \"The focal point of course. Now here is the plan so listen carefully:\n\nWhen we are ready, I shall fire a strong beam of concentrated energy through the focal point directly at the power source. Hopefully, I can take out the power source completely, but it is likely that I can only disrupt it for a short time.\n\nImmediately after this, I shall use a teleport spell to allow us to penetrate the fortress. I shall try to get as deep into it as I can, but I must work quickly and my skill in that matter is not the best.\n\nAssuming the barrier gets reestablished, there will be no way to return to the fort. This is probably the last chance to turn back, are we ready to go?\"", eDialogPic.CREATURE, 1029, ["No", "Yes"])
        if result == 0:
            MessageBox("\"Then we shall return once we are better prepared.\"")
            return
        elif result == 1:
            Party.OutsidePos = Location(264, 20)
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(58,58))
            p.CancelAction = True
            Animation_Hold(-1, 025_magespell)
            Wait()
            Animation_Explosion(Location(57,55), 2, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("\"It worked! The power source has been disrupted and the barrier has fallen. We have a chance, but not for long. We must hurry!\"", eDialogPic.CREATURE, 1029, ["OK"])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "AltrusIhrno_205": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "RentarIhrno_206": Town.NPCList.Remove(npc)
            Town.PlaceEncounterGroup(1)
            Animation_Explosion(Location(1,1), 1, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("Altrus looks in horror and rushes over to the crystal which is now pulsing with unstable light. He places his hands upon it and restores the crystal to a constant blue glow.\n\n\"We have been attacked!\"", eDialogPic.STANDARD, 1028, ["OK"])
            ChoiceBox("\"How did they penetrate our barrier? Give me a damage assessment.\"", eDialogPic.STANDARD, 1029, ["OK"])
            ChoiceBox("The crystal begins to glow. \"The damage is not severe Rentar. It was only a minor jolt. The barrier is now being reestablished and I have refocused it. We should now be immune to another assault of this kind.\n\nWait, I sense that our perimeter has been penetrated by a small group through teleportation during the time the barrier was disabled. I shall now activate our internal defenses.\n\nMy scry analysis reveals that they are only a minor threat. Our forces, combined with our defense measures, should be sufficient to prevent them from reaching the main chamber.\n\nMy analysis indicates that the probability of the invaders reaching here before we are able to activate the devices is near zero. Continue at your normal pace.\"", eDialogPic.CREATURE, 88, ["OK"])
            ChoiceBox("\"Fear not Rentar. The fated moment of execution draws near. Over half of the devices have been configured and are ready for release. I shall only require a few hours more and we shall succeed.\n\nOnce that moment has passed, we shall forever be victorious. No amount of power shall be able to repair them. This shall be the beginning of the end of the Empire and justice shall be had.\"", eDialogPic.STANDARD, 1028, ["OK"])
            ChoiceBox("\"Do not underestimate these creatures Altrus. They are not as primitive as they seem...\"", eDialogPic.STANDARD, 1029, ["OK"])
            Animation_Hold(-1, 004_bless)
            Wait()
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(20,33)
            Party.MoveToMap(TownMap.List["GallowsKeep_79"])
            return
        return
    if StuffDone["65_2"] == 250:
        return
    StuffDone["65_2"] = 250
    ChoiceBox("The passage ahead has suffered a serious cave in. It seems that you have encountered a dead end and can travel no further. Your options down here are growing very thin.", eDialogPic.STANDARD, 4, ["OK"])
