def Generate_Wandering_58_GolemFactory(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["GolemX_237"]])
            npcs.append([1,NPCRecord.List["GolemofBlades_159"]])
            npcs.append([1,NPCRecord.List["VulcaniteGolem_160"]])
            npcs.append([2,NPCRecord.List["Golem_190"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["IlluminenceGolem_162"]])
            npcs.append([1,NPCRecord.List["CryogonGolem_161"]])
            npcs.append([1,NPCRecord.List["IlluminenceGolem_162"]])
            npcs.append([2,NPCRecord.List["Golem_190"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["GolemX_237"]])
            npcs.append([1,NPCRecord.List["GargoyleGolem_163"]])
            npcs.append([1,NPCRecord.List["GolemofBlades_159"]])
            npcs.append([2,NPCRecord.List["Golem_190"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["GargoyleGolem_163"]])
            npcs.append([1,NPCRecord.List["VulcaniteGolem_160"]])
            npcs.append([1,NPCRecord.List["CryogonGolem_161"]])
            npcs.append([2,NPCRecord.List["Golem_190"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(19,52)
                elif r2 == 1: l = Location(42,49)
                elif r2 == 2: l = Location(46,22)
                elif r2 == 3: l = Location(19,16)
                
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

def GolemFactory_1412_MapTrigger_5_32(p):
    result = ChoiceBox("Do you want to leave the factory and return to the city of Evergold?", eDialogPic.CREATURE, 12, ["No", "Yes"])
    if result == 0:
        p.CancelAction = True
        return
    elif result == 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(43,58)
        Party.MoveToMap(TownMap.List["Evergold_57"])
        return

def GolemFactory_1414_MapTrigger_32_30(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This door was jammed shut after a trap went off. No matter how hard you try, you seem to be unable to pry it open.")

def GolemFactory_1415_MapTrigger_21_28(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Someone took the liberty of welding this metallic door to the basalt wall. The seal is quite solid and the door is firmly in place. You will need to find another way to get through this.")

def GolemFactory_1419_MapTrigger_50_10(p):
    if StuffDone["49_9"] == 250:
        return
    StuffDone["49_9"] = 250
    TownMap.List["GolemFactory_58"].DeactivateTrigger(Location(50,10))
    MessageBox("This room is a ghastly sight. Three fellow Empire soldiers are dead on the floor here. Their skin has an odd greenish tone to them. Otherwise there is no sign of blunt injury. Perhaps this is the work of some poison.")

def GolemFactory_1420_MapTrigger_51_14(p):
    result = ChoiceBox("This is the control panel for a device called an Electromagnetic Shaping Broiler. There are many buttons and levers. One button, which says \'Power\', attracts your attention. Do you press it hoping that it is not hooked up to a trap.", eDialogPic.STANDARD, 9, ["Leave", "Push"])
    if result == 1:
        if StuffDone["49_8"] == 0:
            MessageBox("You press the button. The control panel grows dark. You believe that you have just turned off the device.")
            StuffDone["49_8"] = 1
            return
        MessageBox("You press the button and as expected the lights turn back on. You believe you have reactivated the machine.")
        StuffDone["49_8"] = 0
        return

def GolemFactory_1421_MapTrigger_54_15(p):
    if StuffDone["49_8"] == 0:
        MessageBox("This corridor is unbelievably hot. You try to hurry through, but the heat is so intense that your flesh instantly begins to burn. It only takes a few seconds to reduce your bodies to ash.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def GolemFactory_1425_MapTrigger_56_16(p):
    if StuffDone["50_0"] == 0:
        result = ChoiceBox("You discover the remains of an Empire soldier. His body was quickly reduced to ash in the intense heat of the broiler. The heat was quite thorough in burning the remains as even the bones are burned.\n\nA search of the ashes reveals a small key that miraculously managed to survive the intense heat. It must be made out of an extremely heat resistant metal. The key is labeled to indicate it would be used to shutdown the plant.\n\nThis key could prove very useful in stopping the Golems.", eDialogPic.STANDARD, 26, ["Leave", "Take"])
        if result == 1:
            StuffDone["50_0"] = 1
            SpecialItem.Give("FactoryKey")
            return
        return

def GolemFactory_1426_MapTrigger_51_41(p):
    if StuffDone["50_1"] == 0:
        StuffDone["50_1"] = 1
        MessageBox("You burst into this control tower. Inside you find a young man, sitting at the controls. He just laughs when you enter. He makes no move to attack you, he just remains seated. You wonder who this man is.")
        Town.PlaceEncounterGroup(1)
        return

def GolemFactory_1429_MapTrigger_31_40(p):
    result = ChoiceBox("This is the Security Control Panel. The magical windows allow you to watch all parts of the factory at once. This must be how they monitor their factory from threats. Too bad the security was not that effective when the rebels broke in.\n\nThe control panel has an assortment of dials to shift the monitors and buttons allowing you to call alarms. The only thing that attracts your attention is a lever that allows you to open and close the air vents.\n\nYou should be careful for the rebels may have trapped this lever in the hopes that some unsuspecting soldier might trip it.", eDialogPic.STANDARD, 9, ["Leave", "Push"])
    if result == 1:
        MessageBox("You hear the sounds of machinery throughout the factory.")
        SuspendMapUpdate()
        for x in range(6, 62):
            for y in range(2, 58):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[147]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[148])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[148]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])
        ResumeMapUpdate()
        if StuffDone["50_5"] == 0:
            MessageBox("The lever was trapped! On the walls of the room are several canisters which are now leaking a pink gas. Your Empire training tells you this is a deadly neurotoxin. You have seconds to escape and the way you came in does not appear to be an option!")
            StuffDone["50_5"] = 1
            StuffDone["50_4"] = 1
            Timer(Town, 6, False, "GolemFactory_1454_TownTimer_35", eTimerType.DELETE)
            return
        return

def GolemFactory_1431_MapTrigger_35_38(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(55,50))
    p.CancelAction = True
    if StuffDone["50_4"] == 1:
        MessageBox("You manage to escape the deadly gas by fleeing through the vent. Hopefully, the gas will dissipate soon.")
        StuffDone["50_4"] = 0
        return

def GolemFactory_1432_MapTrigger_55_51(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["50_5"] == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You probably would not want to go back through here yet. The poisonous gas has not yet had a chance to dissipate.")
        return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(35,39))
    p.CancelAction = True

def GolemFactory_1433_MapTrigger_59_28(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        MessageBox("You press the button and the elevator moves you up to the ground floor.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(55,29))
        p.CancelAction = True
        StuffDone["50_5"] = 2
        return

def GolemFactory_1434_MapTrigger_55_28(p):
    MessageBox("These controls are not operational.")

def GolemFactory_1435_MapTrigger_44_56(p):
    result = ChoiceBox("These controls operate the Electrostatic Field System. From here you can control all sorts of things from pulse range to field density. You have no idea what the aforementioned mean.\n\nThe only thing you really understand is the power button. You look around and believe to have discovered several gas bombs near the door. If they go off, you will have trouble escaping. Push the button?", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        if StuffDone["50_6"] == 0:
            MessageBox("The room behind the windows grows dark. You have just disabled the electric field.")
            StuffDone["50_6"] = 1
            if StuffDone["50_7"] == 0:
                MessageBox("Your suspicions were correct. The gas bombs begin to disperse their contents, filling the room. You will need to quickly get out of here!")
                StuffDone["50_7"] = 1
                StuffDone["50_4"] = 1
                Timer(Town, 6, False, "GolemFactory_1454_TownTimer_35", eTimerType.DELETE)
                return
            return
        MessageBox("You push the button and the room behind the windows lights up again. You have reactivated the electric field.")
        StuffDone["50_6"] = 0
        return

def GolemFactory_1436_MapTrigger_44_53(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(27,9))
    p.CancelAction = True
    if StuffDone["50_4"] == 1:
        MessageBox("You manage to escape the deadly gas by fleeing through the vent. Hopefully, the gas will dissipate soon.")
        StuffDone["50_4"] = 0
        return

def GolemFactory_1437_MapTrigger_43_5(p):
    if StuffDone["50_7"] == 1:
        StuffDone["50_7"] = 2
        return

def GolemFactory_1438_MapTrigger_27_10(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["50_7"] == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You probably would not want to go back through here yet. The poisonous gas has not yet had a chance to dissipate.")
        return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(44,54))
    p.CancelAction = True

def GolemFactory_1439_MapTrigger_45_59(p):
    if StuffDone["50_6"] == 0:
        MessageBox("The electric field here is extremely strong. As you wander into the room, electricity bounces from wall to wall. This amount of voltage is fatal to living things.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def GolemFactory_1442_MapTrigger_60_52(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(35,28))
    p.CancelAction = True

def GolemFactory_1443_MapTrigger_36_28(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(60,53))
    p.CancelAction = True

def GolemFactory_1444_MapTrigger_25_35(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        return;
    result = ChoiceBox("At last you have reached the central controls of the factory. There are several dials, buttons, and levers to perform various functions. Most of them, you do not have a clue what they mean.\n\nThe one thing of interest is the lever labeled \'EMERGENCY SHUT DOWN\'. Do you pull the lever?", eDialogPic.STANDARD, 9, ["Leave", "Pull"])
    if result == 1:
        if SpecialItem.PartyHas("FactoryKey"):
            if StuffDone["49_7"] == 1:
                ChoiceBox("You attempt to pull the lever, only to find it locked. Beside the lever, you discover a combination dial with a keyhole. You attempt to spin the dial using the combination you learned from Talon, but to no avail. The dial is also locked.\n\nThen you remember the key you discovered. You decide to try that on the dial and it unlocks it. You quickly spin the dial with the proper combination. You then pull the shut down lever.\n\nImmediately, you are greeted with the fine sound of the machinery shutting off. Suddenly, the lights go out! Then there is silence and darkness. After a few seconds, however, the emergency safety lights come on.\n\nIt appears you have succeeded in saving the Golem factory. You leave to find many mages very grateful that the factory does not have to be destroyed. You see no sign of Talon, though.\n\nPerhaps you should check back at the library.", eDialogPic.CREATURE, 119, ["OK"])
                StuffDone["49_7"] = 2
                Animation_Hold(-1, 007_cool)
                Wait()
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(43,58)
                Party.MoveToMap(TownMap.List["Evergold_57"])
                return
            MessageBox("You attempt to pull the lever only to discover it is locked! Beside the lever is a combination dial with a keyhole. You try the key you found and it unlocks the dial! The problem is that you do not know the combination.")
            return
        MessageBox("You attempt to pull the lever, but it is locked! You then notice that next to the lever is a combination dial with a keyhole. You try to turn the dial, but it is locked. You will need to find a key to unlock this.")
        return

def GolemFactory_1445_MapTrigger_11_26(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(25,12))
    p.CancelAction = True

def GolemFactory_1446_MapTrigger_25_11(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(10,26))
    p.CancelAction = True

def GolemFactory_1447_MapTrigger_14_21(p):
    ChoiceBox("This book provides information on the shaping of the golem pieces. First, ore is brought in from around the world and stored in the room to the west. When the ore is ready to be used, it must be refined.\n\nIt is done by melting the metal down, removing it of impurities. The metal is then pumped up magically and cooled. This process is repeated an average five times, which is usually enough to purify the material.\n\nNext, the metal must be reinforced and made ready for shaping. The shaping occurs by heating the metal up to high temperatures and using magnets to mold the parts quite quickly and accurately with a low error rate.\n\nHowever, to give the metal this property, it must be chemically processed. It is once again melted down and pumped into reaction chambers where the metal is given the special property to allow shaping. This usually takes several trials.\n\nAfterward, the metal is once again heated in an air broiler which reaches temperatures fatal to any life. Magnetic currents are used to shape the reinforced metal into the appropriate parts.\n\nThe parts are cooled and assembled into the golems through complex mechanical processes.", eDialogPic.CREATURE, 119, ["OK"])

def GolemFactory_1448_MapTrigger_41_53(p):
    ChoiceBox("This book describes the process of animating the Golems. Although the terminology is way beyond you, you manage to decipher the general concept.\n\nThe secret to Golem intelligence is through a Golem Gem. These gems must be specially programed and set through complex processes, the more sophisticated Golem means a more sophisticated gem.\n\nAfter they are shaped, the gem is fused into the golem through heating. However, the gem can only be activated through a strong electrostatic current, strong enough to kill any living thing.\n\nThe Golem is moved into a powerful electrostatic field (which the room to the south contains) where the Golem is blasted with powerful surges of electricity. This binds the gem to the Golem and creates an energy field.\n\nThe Golem is then active and has intelligence as per its programming. Amazing what these magi have developed.", eDialogPic.CREATURE, 119, ["OK"])

def GolemFactory_1449_MapTrigger_24_60(p):
    MessageBox("This book describes the process of giving a Golem resistance to heat, cold, or arcane effects. This procedure is done by grafting resistant metals onto the Golems body. Apparently, the metals are very expensive as is the process.")

def GolemFactory_1450_MapTrigger_8_61(p):
    MessageBox("This book describes the process of programming the Golem Gems. This book is way beyond you. You would need years of training in this field to begin to understand this.")

def GolemFactory_1452_MapTrigger_49_36(p):
    result = ChoiceBox("This is a factory control panel. It contains all sorts of buttons and dials. The controls for the Thermal Fluid Tank catches your attention. There are two buttons:\n\n1 - Fluid Flow\n\n2 - Tank Door", eDialogPic.STANDARD, 9, ["Leave", "2", "1"])
    if result == 1:
        if StuffDone["50_3"] < 2:
            if StuffDone["50_2"] == 0:
                MessageBox("You press the button and hear a soft click in the distance.")
                t = Town.TerrainAt(Location(25,43))
                if t == TerrainRecord.UnderlayList[142]: Town.AlterTerrain(Location(25,43), 0, TerrainRecord.UnderlayList[145])
                elif t == TerrainRecord.UnderlayList[145]: Town.AlterTerrain(Location(25,43), 0, TerrainRecord.UnderlayList[142])
                return
            MessageBox("You press the button. You hear a click and a loud whoosh! Within seconds, you hear a loud alarm go off. It appears you may have just caused an industrial hazard.")
            StuffDone["50_3"] = 2
            for x in range(25, 32):
                for y in range(43, 44):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            return
        MessageBox("The machine emits a loud buzz. Apparently this control is now inactive.")
        return
    elif result == 2:
        if StuffDone["50_3"] == 0:
            MessageBox("You press the button. You hear a loud beep and hear the sound of some kind of liquid being pumped.")
            if StuffDone["50_2"] == 0: StuffDone["50_2"] = 1
            else: StuffDone["50_2"] = 0
            SuspendMapUpdate()
            for x in range(20, 25):
                for y in range(41, 46):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[170]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
            ResumeMapUpdate()
            return
        MessageBox("You press the button and hear a buzz. The door light flashes as if it were beckoning your attention.")
        return

def GolemFactory_1453_TownTimer_0(p):
    for x in range(41, 44):
        for y in range(35, 45):
            if Maths.Rand(1,0,100) <= 75:
                Town.PlaceField(Location(x,y), Field.FORCE_WALL)

def GolemFactory_1454_TownTimer_35(p):
    if StuffDone["50_4"] == 1:
        MessageBox("You were unable to escape the toxic fumes and are knocked unconscious. This variety of neurotoxin is fatal.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def GolemFactory_1455_OnEntry(p):
    if StuffDone["50_3"] >= 2:
        for x in range(25, 32):
            for y in range(43, 44):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
        return
def Talking_58_0(p):
    Town.NPCList.Remove(p.NPCTarget)
    if p.NPCTarget.Start.LifeVariable != "":
        StuffDone[p.NPCTarget.Start.LifeVariable] = 1
    p.TalkingText = "\"It will not matter. In under a minute, I will be gone. On your way up here, I consumed a poison. Quite painless really. So go ahead, do what you will, it does not matter anymore.\" He laughs as he closes his eyes and loses consciousness.@nHe has stopped breathing, and his pulse is gone. This man is dead along with whatever knowledge he had."
