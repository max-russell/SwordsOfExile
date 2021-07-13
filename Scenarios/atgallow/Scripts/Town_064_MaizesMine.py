def Generate_Wandering_64_MaizesMine(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Imp_84"]])
            npcs.append([2,NPCRecord.List["Hordling_88"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Imp_84"]])
            npcs.append([2,NPCRecord.List["Hordling_88"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Imp_84"]])
            npcs.append([2,NPCRecord.List["Hordling_88"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["Imp_84"]])
            npcs.append([2,NPCRecord.List["Hordling_88"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(4,37)
                elif r2 == 1: l = Location(60,29)
                elif r2 == 2: l = Location(7,6)
                elif r2 == 3: l = Location(32,27)
                
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

def MaizesMine_1572_MapTrigger_31_53(p):
    if StuffDone["40_0"] == 250:
        return
    StuffDone["40_0"] = 250
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(31,53))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(32,53))
    ChoiceBox("Ahead, you see the remnants of buildings typical in mines. You know some creatures had a lovely time blasting this place apart. Clues on the walls tell you it happened awhile back.\n\nHowever, you must be careful as they may still be here.", eDialogPic.STANDARD, 8, ["OK"])

def MaizesMine_1574_MapTrigger_5_19(p):
    if StuffDone["40_4"] == 250:
        return
    StuffDone["40_4"] = 250
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(5,19))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(6,19))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(7,19))
    MessageBox("To the north, the demons have assembled a wall to apparently defend something. It is not all that impressive, but serves its purpose. Several small imps peer out from small holes.")

def MaizesMine_1577_MapTrigger_20_5(p):
    if StuffDone["40_5"] == 0:
        result = ChoiceBox("Upon this pedestal lies a small glowing deep red orb. You peer inside and see a kind of mist within. As you look, you begin to feel the onset of a headache. You wonder what kind of magical device this is.\n\nWhatever it is, it makes you feel very uneasy. You do know, however, that the demons have some kind of cult worship with the orb. You don\'t know why. Perhaps you could steal it from the demons; you bet some wizard would pay for it.", eDialogPic.STANDARD, 13, ["Leave", "Take"])
        if result == 1:
            StuffDone["40_5"] = 1
            Town.PlaceEncounterGroup(1)
            ChoiceBox("You pick up the orb and are immediately shocked by it. You pull your hands away, and the orb falls to the floor, shattering. The odd smog like substance disperses into the atmosphere.\n\nYou think nothing else is about to happen, but then you see the smog recondense in the northern section of the room. It is followed by a high-pitched, horrific laughter. A massive demon forms right in front of you!\n\n\"Oh yes! It was about time someone came here and freed me.\" He eyes you carefully. \"Allow me to introduce myself, I am Quixus, lord of demons. For centuries I have been trapped in that dreadful orb, imprisoned by some wizard.\n\nMy demon servants were unable to free me, the orb would repel any of my kind. However, that all changes now. If you will excuse me, the centuries have made me weak. I will now consume your life forces.\"", eDialogPic.STANDARD, 13, ["OK"])
            return
        return

def MaizesMine_1578_MapTrigger_33_4(p):
    if StuffDone["23_9"] == 0:
        if Party.CountItemClass(12, False) > 0:
            MessageBox("You discover a very ancient cart. You investigate the controls and discover it is lacking a power source. You notice the small glowing crystal you found fits perfectly!\n\nThe ancient machine begins to hum. Surprising that such an ancient device still works. It must be centuries old. Anyway, only one person will be able to use the cart due to size.")
            StuffDone["23_9"] = 1
            result = ChoiceBox("Going up?", eDialogPic.STANDARD, 6, ["Leave", "Yes"])
            if result == 1:
                pc = SelectPCBox("Select one member of your party?",True)
                if pc == None:
                    p.CancelAction = True
                    return
                Party.Split(pc, Location(38,4))
                return
            p.CancelAction = True
            return
        MessageBox("There is an ancient small cart here which leads up a shaft. One of you gets in and unsuccessfully attempts to use the controls. Upon investigation, you discover an empty alcove for a power source. Sadly, you have nothing to place there.")
        return
    if Party.CountItemClass(12, False) > 0:
        result = ChoiceBox("Going up?", eDialogPic.STANDARD, 6, ["Leave", "Yes"])
        if result == 1:
            pc = SelectPCBox("Select one member of your party?",True)
            if pc == None:
                p.CancelAction = True
                return
            Party.Split(pc, Location(38,4))
            return
        p.CancelAction = True
        return
    MessageBox("You will need your glowing crystal to use this cart.")
    p.CancelAction = True

def MaizesMine_1579_MapTrigger_37_4(p):
    result = ChoiceBox("Going down?", eDialogPic.STANDARD, 6, ["Leave", "Yes"])
    if result == 1:
        if Party.IsSplit:
            Party.Reunite()
        return
    p.CancelAction = True

def MaizesMine_1580_MapTrigger_52_13(p):
    if StuffDone["6_6"] == 250:
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
    StuffDone["6_6"] = 250
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(52,13))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(52,14))
    pc.RunTrap(eTrapType.RANDOM, 2, 50)

def MaizesMine_1582_MapTrigger_55_13(p):
    if StuffDone["6_7"] == 250:
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
    StuffDone["6_7"] = 250
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(55,13))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(55,14))
    pc.RunTrap(eTrapType.RANDOM, 2, 50)

def MaizesMine_1584_MapTrigger_58_13(p):
    if StuffDone["6_8"] == 250:
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
    StuffDone["6_8"] = 250
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(58,13))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(58,14))
    pc.RunTrap(eTrapType.RANDOM, 2, 50)

def MaizesMine_1585_MapTrigger_55_9(p):
    if StuffDone["40_9"] == 250:
        return
    StuffDone["40_9"] = 250
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(55,9))
    TownMap.List["MaizesMine_64"].DeactivateTrigger(Location(55,10))
    ChoiceBox("You enter this room, and the magical lighting goes out leaving you in darkness! However, total darkness only lasts for a few seconds as an image of an old man appears the glowing runes. The image is choppy, but still visible.\n\n\"Greetings, I am Valgin the sage. Or at least I was. To those of you who are viewing my image, I congratulate you whether you are friend or foe. You are the first to have made it past my defenses.\n\nIt is my guess that I am long dead in your time. I created this image shortly before my death. I am sad to say that I will not live to see the death of my enemy, the cruel Emperor Hawthorne III. I hope that helps you realize the time I live.\n\nHere is my story. I was a teacher of magery at Wrynn University and a philosopher. My musings about the world caused a stir and I was captured by the Empire. With the help of rebels, I managed to escape.\n\nAfter a decade of fleeing around the world, I came to this cave to write my legacy. It is my knowledge that I sought to protect. I hide here several scrolls of my experiments. The knowledge must survive and not be destroyed by the powerful.\n\nIt is my hope you are viewing from a peaceful time where my knowledge will be secure in your hands. I entrust in you my life\'s work. Now I may rest.\" He bows and the image fades away. The lighting returns.", eDialogPic.CREATURE, 27, ["OK"])

def MaizesMine_1587_MapTrigger_61_3(p):
    if StuffDone["40_1"] == 0:
        MessageBox("You open the chest and discover several ancient scrolls. The vellum has been preserved by magic. You try to read them, but the script has been ciphered, out of your reach of knowledge.\n\nYou take them in the hopes that someone may be interested in Valgin\'s works.")
        SpecialItem.Give("ScrollsofValgin")
        StuffDone["40_1"] = 1
        return

def MaizesMine_1588_MapTrigger_49_2(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever and the ancient machinery works upon the portculli. Surprising how this machinery has lasted throughout the centuries.")
        t = Town.TerrainAt(Location(48,3)).TransformTo
        Town.AlterTerrain(Location(48,3), 0, t)
        return

def MaizesMine_1590_MapTrigger_53_2(p):
    MessageBox("An ancient human skeleton rests peacefully in the bed. This must have been Valgin.")

def MaizesMine_1591_CreatureDeath5(p):
    MessageBox("The figure of the demon lord Quixus fades away. After spending several centuries trapped within some orb, he made a fatal mistake by trying to kill his saviors. Well, another evil thing destroyed.")
    Town.PlaceItem(Item.List["Crystal_222"].Copy(), Location(20,2))
