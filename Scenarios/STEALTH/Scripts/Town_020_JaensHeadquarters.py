def Generate_Wandering_20_JaensHeadquarters(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Soldier_13"]])
            npcs.append([1,NPCRecord.List["Soldier_13"]])
            npcs.append([1,NPCRecord.List["Soldier_13"]])
            npcs.append([2,NPCRecord.List["Captain_14"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["EmpireArcher_20"]])
            npcs.append([1,NPCRecord.List["Soldier_13"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Captain_14"]])
            npcs.append([1,NPCRecord.List["Captain_14"]])
            npcs.append([1,NPCRecord.List["Champion_15"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["Champion_15"]])
            npcs.append([1,NPCRecord.List["EmpireArcher_20"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(34,50)
                elif r2 == 1: l = Location(51,27)
                elif r2 == 2: l = Location(51,37)
                elif r2 == 3: l = Location(51,30)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def JaensHeadquarters_318_MapTrigger_13_41(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(13,42)).Num == 145:
        if SpecialItem.PartyHas("JaensKey"):
            MessageBox("When you get close to the door, a keyhole suddenly appears under the handle, surrounded by a circle of flames. On a hunch, you quickly insert Jaen\'s key into the hole and turn it. The flames disappear, and the door becomes unlocked.")
            Town.AlterTerrain(Location(13,42), 0, TerrainRecord.UnderlayList[142])
            return
        MessageBox("When you get close to the door, a keyhole suddenly appears under the handle, surrounded by a circle of flames. You try to get the door open, but you don\'t have a key that fits.\n\nThe flames around the keyhole suddenly flare out at you, searing you! The keyhole then disappears. The door must be able to sense the improperness of your presence here.")
        Party.Damage(Maths.Rand(7, 1, 6) + 8, eDamageType.FIRE)
        Wait()
        return

def JaensHeadquarters_319_MapTrigger_13_40(p):
    if StuffDone["20_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["20_1"] = 250
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(13,40))
    pc.RunTrap(eTrapType.RANDOM, 3, 60)

def JaensHeadquarters_320_MapTrigger_13_43(p):
    if StuffDone["20_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["20_2"] = 250
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(13,43))
    pc.RunTrap(eTrapType.RANDOM, 3, 70)

def JaensHeadquarters_321_MapTrigger_20_39(p):
    result = ChoiceBox("The shelves of Jaen\'s study are filled with ledgers, journals, and tomes, recording the movements, numbers, and supplies of his troops. The complete records of his forces are arrayed before you.\n\nEven one book from these shelves would be an incredibly valuable prize to present to Stalker and his minions.", eDialogPic.TERRAIN, 135, ["Leave", "Take"])
    if result == 1:
        MessageBox("Jaen is, unfortunately, very paranoid about spies. That is why every single tome on these shelves has a magical, protective rune on it.\n\nYou don\'t know how to deactivate the runes. You only know how to make them explode.")
        Party.Damage(Maths.Rand(6, 1, 7) + 6, eDamageType.FIRE)
        Wait()
        return

def JaensHeadquarters_325_MapTrigger_13_34(p):
    result = ChoiceBox("A heavy, impressive tome, filled with all manner of fascinating magical inscriptions, is chained to this pedestal.", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("The book records the magical experiments currently being performed by Jaen\'s men. There are currently two paths of study. Half of his mages are trying to figure out how to recreate Stalker\'s exploding boxes for their own use.\n\nTheir guess is that Stalker\'s troops are filling the boxes with equal parts sulphur, saltpeter, and charcoal and somehow imbuing the mixture with extra magical power. They have not been able to do this themselves.\n\nThe rest of the mages are trying to create their own magical weapons to use against the Hill Runners. Quickfire bombs are being worked on, as are ways of spreading plague from a distance, and of summoning dragons to firebomb the rebel cities.\n\nYou have heard of a cult, called the Anama, who believe that magic is far too destructive a force and should be resisted entirely. Reading of all these potential tools for mass destruction, you can almost see their point.", eDialogPic.TERRAIN, 130, ["OK"])
        return

def JaensHeadquarters_327_MapTrigger_41_20(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        t = Town.TerrainAt(Location(40,25))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(40,25), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(40,25), 0, TerrainRecord.UnderlayList[147])
        MessageBox("You pull the lever, and hear the massive winches and gears of the fort\'s gate mechanism kick into action.")
        t = Town.TerrainAt(Location(40,26))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(40,26), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(40,26), 0, TerrainRecord.UnderlayList[147])
        return

def JaensHeadquarters_328_MapTrigger_43_31(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        t = Town.TerrainAt(Location(45,25))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(45,25), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(45,25), 0, TerrainRecord.UnderlayList[147])
        MessageBox("You pull the lever, and hear the massive winches and gears of the fort\'s gate mechanism kick into action.")
        t = Town.TerrainAt(Location(45,26))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(45,26), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(45,26), 0, TerrainRecord.UnderlayList[147])
        return

def JaensHeadquarters_329_MapTrigger_37_57(p):
    if StuffDone["20_4"] == 250:
        return
    StuffDone["20_4"] = 250
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(37,57))
    MessageBox("This cramped, shadowy passage is thick with the stenches of smoke, sour sweat, and despair. You hear a single, constant, low moan, coming from farther down the corridor.")

def JaensHeadquarters_330_MapTrigger_10_18(p):
    if StuffDone["20_5"] == 250:
        return
    StuffDone["20_5"] = 250
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(10,18))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(11,18))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(10,33))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(11,33))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(22,32))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(25,30))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(25,21))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(22,19))
    ChoiceBox("You stand at the entrance to a huge meeting hall, dominated by a huge oak table and many massive, granite pillars. The place is a strange echo of Stalker\'s meeting chamber, eerily similar in many ways.\n\nAt last, you have come face to face with the leader of the Empire troops on Morrow\'s Isle. As imposing as the architecture is, however, it is nothing compared to the infamous Jaen himself.\n\nThis is no spy, or diplomat. This man has clearly spent much of his life as a soldier. He stands well over six feet tall, and his massive frame is clad in equally imposing plate armor. The enormous hammer at his side could fell an ox in a single blow.\n\nYou seem to have intruded on one of his strategy sessions, and all his lieutenants are present. A nastier bunch of heavily armed men, you\'d have a hard time imagining. But here they all are, and they\'re all about to try and kill you.", eDialogPic.CREATURE, 1025, ["OK"])
    Town.PlaceEncounterGroup(1)

def JaensHeadquarters_338_MapTrigger_9_60(p):
    result = ChoiceBox("You find a small hole in the ground. Not so small you couldn\'t slide down it, but small enough that it would be a painful process. You may not be able to make it back up, either.\n\nStill, if this is the only safe way into Jaen\'s fortress, you may have no choice ...", eDialogPic.TERRAIN, 244, ["Leave", "Climb"])
    if result == 1:
        if StuffDone["20_6"] >= 1:
            MessageBox("You shimmy down the hole. Again. And fall into a massive pile of filth. Again.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(13,60))
            p.CancelAction = True
            return
        StuffDone["20_6"] = 1
        MessageBox("You start to shimmy down the hole. At first, you climb down carefully and in a controlled way. Unfortunately, the hole becomes rather slick. Before long, you lose your grip, and start sliding down.\n\nYou don\'t have long to fall. Soon, you\'re dumped out of a crack in the ceiling of a small cave, and fall into a huge pile of rotting garbage. It breaks your fall, but not in a pleasant way. You\'re now in Jaen\'s Fortress.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(13,60))
        p.CancelAction = True
        return

def JaensHeadquarters_339_MapTrigger_5_48(p):
    if StuffDone["20_7"] >= 1:
        MessageBox("After you broke into Jaen\'s Fortress for the first time, Jaen spared no effort to find the hole in his defenses. He found it, and, expecting someone would try to use it again, placed 100 strong men here to ambush whoever came through.\n\nAfter you are overwhelmed and captured and before you are executed, Jaen\'s interrogators get you to tell them everything they need to know about Jaen\'s forces and defenses.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def JaensHeadquarters_340_MapTrigger_5_61(p):
    if StuffDone["20_6"] >= 1:
        StuffDone["20_7"] = 1
        return

def JaensHeadquarters_341_MapTrigger_5_50(p):
    if StuffDone["20_8"] == 250:
        return
    StuffDone["20_8"] = 250
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(5,50))
    ChoiceBox("As you get close to the gate into the main part of the fortress, you hear the all too familiar report of a Hill Runner explosive box. The blast is of comparable power to the one which destroyed Lord Volpe\'s fortress.\n\nThe explosion was to the east. On the down side, the forces here will be alerted. On the up side, the distraction should be enough to get you in to kill Jaen.", eDialogPic.TERRAIN, 105, ["OK"])

def JaensHeadquarters_342_MapTrigger_54_32(p):
    if StuffDone["20_9"] == 250:
        return
    StuffDone["20_9"] = 250
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(54,32))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(54,33))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(54,26))
    TownMap.List["JaensHeadquarters_20"].DeactivateTrigger(Location(54,39))
    MessageBox("From here, you can see the result of the explosion. They destroyed the front gate of Jaen\'s fortress. You\'re thankful for it now. The hole in the wall will make it much easier for you to escape.")

def JaensHeadquarters_346_TownTimer_0(p):
    if StuffDone["20_8"] >= 1:
        MessageBox("You hear many shouts of alarm and readiness. More guards have arrived from outside the fortress.")
        RunScript("Generate_Wandering_20_JaensHeadquarters", ScriptParameters(eCallOrigin.CUSTOM))
        return

def JaensHeadquarters_347_OnEntry(p):
    ChoiceBox("After a long march north, you reach the river. At first, you think that you have made some sort of mistake - you were supposed to have reached Jaen\'s fortress by now.\n\nAs you wander around, you notice a hole in the ground. It\'s a recently dug shaft, framed with rough timbers. You walk up to it to investigate. As you peer over the edge, you notice people approaching you from all sides.\n\nThey\'re Hill Runners. Only they could be this stealthy. One of them says \"We\'ve been waiting for you. Everything is in place. It is time. Climb down the hole.\"\n\nWhen you express your doubts about entering the hole, they don\'t hesitate to grab you and chuck you in. You land on a thick pile of furs below ...", eDialogPic.TERRAIN, 196, ["OK"])

def JaensHeadquarters_348_ExitTown(p):
    if p.Dir.IsEast:
        if StuffDone["20_0"] >= 1:
            MessageBox("You emerge from the well concealed cave entrance. It\'s covered by a magical illusion. It\'s amazing the rebels were able to find it. You\'ll be surprised if you\'re able to find it again.\n\nNot that you would want to ... you were lucky to survive this attack. The next time they will be more than ready for you. Your mission was completed. Stalker will be very pleased.")
            return
        MessageBox("You are very relieved to have escaped Jaen\'s fortress with your hides intact. Unfortunately, Jaen is still alive, and he spares no effort to chase you down before you can get far. Hordes of troops swarm over the countryside.\n\nAfter you are overwhelmed and captured and before you are executed, Jaen\'s interrogators get you to tell them everything they need to know about Stalker\'s forces and defenses.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()

def JaensHeadquarters_349_CreatureDeath2(p):
    ChoiceBox("When he takes his death blow, Jaen has no final words, no dying speech to rally his followers. His final sound is a scream of fury. He howls out his anger at you, and his frustration with his failure.\n\nThen his scream fades to a gurgle, and ends. With the crash of armor on cobblestones, he keels over. The rebels have achieved another great victory.\n\nJaen\'s men are stunned by his loss, but not for long. Professionals to the last, they soon return to the attack, but not before you\'re able to pick up and pocket the key that bounced out of Jaen\'s pocket.", eDialogPic.CREATURE, 1025, ["OK"])
    StuffDone["20_0"] = 1
    SpecialItem.Give("JaensKey")
    for pc in Party.EachAlivePC():
        pc.AwardXP(100)
