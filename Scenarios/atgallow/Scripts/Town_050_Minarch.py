def Generate_Wandering_50_Minarch(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["AmberSlime_138"]])
            npcs.append([1,NPCRecord.List["OchreSlime_139"]])
            npcs.append([1,NPCRecord.List["EmeraldSlime_140"]])
            npcs.append([2,NPCRecord.List["MauveSlime_141"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["OchreSlime_139"]])
            npcs.append([1,NPCRecord.List["EmeraldSlime_140"]])
            npcs.append([1,NPCRecord.List["MauveSlime_141"]])
            npcs.append([2,NPCRecord.List["AmberSlime_138"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["EmeraldSlime_140"]])
            npcs.append([1,NPCRecord.List["MauveSlime_141"]])
            npcs.append([1,NPCRecord.List["AmberSlime_138"]])
            npcs.append([2,NPCRecord.List["OchreSlime_139"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["MauveSlime_141"]])
            npcs.append([1,NPCRecord.List["AmberSlime_138"]])
            npcs.append([1,NPCRecord.List["OchreSlime_139"]])
            npcs.append([2,NPCRecord.List["EmeraldSlime_140"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(52,27)
                elif r2 == 1: l = Location(32,16)
                elif r2 == 2: l = Location(21,6)
                elif r2 == 3: l = Location(10,20)
                
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

def Minarch_1154_MapTrigger_3_38(p):
    if StuffDone["26_4"] < 1:
        p.CancelAction = False
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The guard stops you. \"Sorry, the mine has been closed until further notice. No one without permission of the mayor can get through.\"")
        return

def Minarch_1155_MapTrigger_33_59(p):
    if SpecialItem.PartyHas("MalthosNPC"):
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Malthos turns to you. \"Hey! I\'m not going on some big adventure. The mine\'s to the northwest. Let\'s get going!\"")
        return

def Minarch_1159_MapTrigger_49_26(p):
    if SpecialItem.PartyHas("MalthosNPC"):
        if StuffDone["26_6"] == 250:
            return
        StuffDone["26_6"] = 250
        MessageBox("Malthos points to the north. \"See that stream up there. Looks like there\'s no way to cross, eh. Guess again! I know how. Just go over to the cave wall by the water and I\'ll show you!\"")
        return

def Minarch_1163_MapTrigger_47_21(p):
    if SpecialItem.PartyHas("MalthosNPC"):
        result = ChoiceBox("Malthos speaks, \"Okay. See those step like things jutting out from the cave wall?  We\'ll have to grab onto those. Were going to have to get our feet wet as there are some beneath the water. Hold on so you don\'t get caught in the current!\"\n\nDo you attempt to cross?", eDialogPic.STANDARD, 8, ["Leave", "Onward"])
        if result == 1:
            MessageBox("You cross the stream safely.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(48,18))
            p.CancelAction = True
            return
        return
    if StuffDone["26_7"] == 1:
        MessageBox("You cross the stream safely.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(48,18))
        p.CancelAction = True
        return

def Minarch_1164_MapTrigger_48_18(p):
    if SpecialItem.PartyHas("MalthosNPC"):
        result = ChoiceBox("Malthos speaks, \"Okay. See those step like things jutting out from the cave wall?  We\'ll have to grab onto those. Were going to have to get our feet wet as there are some beneath the water. Hold on so you don\'t get caught in the current!\"\n\nDo you attempt to cross?", eDialogPic.STANDARD, 8, ["Leave", "Onward"])
        if result == 1:
            MessageBox("You cross the stream safely.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(47,21))
            p.CancelAction = True
            return
        return
    if StuffDone["26_7"] == 1:
        MessageBox("You cross the stream safely.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(47,21))
        p.CancelAction = True
        return

def Minarch_1165_MapTrigger_49_15(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if SpecialItem.PartyHas("MalthosNPC"):
        MessageBox("Malthos turns to you. \"I\'m stayin\' here. The caverns to the north are haunted. That\'s were the other party got killed. Wouldn\'t go there if I were you.\"")
        SpecialItem.Take("MalthosNPC")
        Message("  Malthos leaves the party")
        return

def Minarch_1167_MapTrigger_49_16(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["26_8"] < 1:
        if SpecialItem.PartyHas("MalthosNPC"):
            return
        MessageBox("You return to Malthos. \"Wised up, eh? Come on, let\'s continue our search. They wouldn\'t go up there anyway.\"")
        SpecialItem.Give("MalthosNPC")
        Message("  Malthos joins the party!")
        return

def Minarch_1169_MapTrigger_45_4(p):
    if StuffDone["26_9"] == 250:
        return
    StuffDone["26_9"] = 250
    TownMap.List["Minarch_50"].DeactivateTrigger(Location(45,4))
    TownMap.List["Minarch_50"].DeactivateTrigger(Location(45,5))
    TownMap.List["Minarch_50"].DeactivateTrigger(Location(45,6))
    MessageBox("A chilling wind assaults your bodies. You hear quiet movements of several creatures. Malthos was correct! This place is haunted and you\'ve just stumbled into an ambush.")
    Town.PlaceEncounterGroup(2)

def Minarch_1172_MapTrigger_57_4(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["26_8"] >= 2:
        if StuffDone["26_8"] == 2:
            if Party.CountItemClass(24, False) > 0:
                StuffDone["26_8"] = 3
                StuffDone["26_4"] = 2
                ChoiceBox("Using your rope, you create a system to bring the miners up one by one. Each of them grant you immense thanks. After everyone has been rescued, you return to the town. The miners reunite with their families and friends.\n\nYou report back to the mayor. \"Excellently done! The Empire owes you a great deal of gratitude. Take this sack of gold as due payment. In addition, if you need anything else, do not be afraid to ask. Thank you and long live the Empire!\"", eDialogPic.STANDARD, 8, ["OK"])
                Party.Gold += 500
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(3,51))
                p.CancelAction = True
                return
            MessageBox("Unfortunately, you have no means to rescue the miners. You will need some kind of rope in order to rescue them.")
            return
        return
    if StuffDone["26_8"] < 1:
        StuffDone["26_8"] = 1
        Town.PlaceEncounterGroup(1)
        ChoiceBox("You hear several voices at the bottom of this chasm. You look down and discover about twenty people standing at the bottom. These must be the missing miners! Now all you have to do is get them out.\n\nOne of them yells. \"Watch out, that Malthos he\'s the one. He\'s not human, he\'s really a...\" From behind you hear a twisted laughter. You turn around to see Malthos accompanied by two spectres.\n\nMalthos transmutes into his true form, a Vampire! \"Yes indeed! The other adventurers that I told you about. I forgot to mention that I was the undead creature that killed them! Gwa, ha, ha!\n\nWhy you ask? Hey, a Vampire needs feeding too! I figure one victim per week for the next six months or so would really improve my powers. After that, I can finally take over this entire town! But now, to take over your lives...\"", eDialogPic.CREATURE, 59, ["OK"])
        return

def Minarch_1173_MapTrigger_49_6(p):
    if StuffDone["26_4"] == 2:
        Town.AlterTerrain(Location(57,4), 0, TerrainRecord.UnderlayList[0])
        return

def Minarch_1174_MapTrigger_3_35(p):
    result = ChoiceBox("There is a cart that is designed to take you up or down this shaft. You should be able to use the controls yourself. Do you step in the cart?", eDialogPic.STANDARD, 8, ["Leave", "Step In"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(15,15))
        p.CancelAction = True
        return
    p.CancelAction = True

def Minarch_1175_MapTrigger_15_14(p):
    result = ChoiceBox("There is a cart that is designed to take you up or down this shaft. You should be able to use the controls yourself. Do you step in the cart?", eDialogPic.STANDARD, 8, ["Leave", "Step In"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(3,36))
        p.CancelAction = True
        return
    p.CancelAction = True

def Minarch_1176_MapTrigger_42_41(p):
    if StuffDone["27_0"] >= 2:
        return
    if StuffDone["27_0"] < 1:
        result = ChoiceBox("Upon this altar is an alcove. Within rests a sphere like stone. It emits a kind of eerie moon like glow. This must be the moonstone! Being near it calms your nerves and lifts your spirits. You can feel yourself being rejuvenated.\n\nYou could meditate here to get the full effect.", eDialogPic.TERRAIN, 137, ["Leave", "Pray"])
        if result == 1:
            MessageBox("You meditate before the moonstone and feel your natural energies replenished!")
            for pc in Party.EachAlivePC():
                pc.SP+= 50
            return
        return
    result = ChoiceBox("Upon this altar rests the Moonstone. As you near it, you can feel the calming waves of rejuvenation it emits. Your cares seem to float away as your natural energies are slowly restored.\n\nYou have been given permission to take this Moonstone to be used in the conversion to a Sunstone. But perhaps you should meditate a bit first and let the moonstone restore you.", eDialogPic.TERRAIN, 137, ["Leave", "Take", "Pray"])
    if result == 1:
        MessageBox("You carefully lift the Moonstone from the altar. Immediately as it leaves the altar, the effect of the regenerating effect is vastly diminished. You kind of feel a slight remorse, but you are doing what you have to do.")
        StuffDone["27_0"] = 2
        SpecialItem.Give("Moonstone")
        RunScript("GlobalCall_Minarch_2843", ScriptParameters(eCallOrigin.CUSTOM))
        result = ChoiceBox("Upon this altar is an alcove. Within rests a sphere like stone. It emits a kind of eerie moon like glow. This must be the moonstone! Being near it calms your nerves and lifts your spirits. You can feel yourself being rejuvenated.\n\nYou could meditate here to get the full effect.", eDialogPic.TERRAIN, 137, ["Leave", "Pray"])
        if result == 1:
            MessageBox("You meditate before the moonstone and feel your natural energies replenished!")
            for pc in Party.EachAlivePC():
                pc.SP+= 50
            return
        return
    elif result == 2:
        MessageBox("You meditate before the moonstone and feel your natural energies replenished!")
        for pc in Party.EachAlivePC():
            pc.SP+= 50
        return

def Minarch_1177_MapTrigger_4_58(p):
    if StuffDone["41_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The owner of this chest placed a fairly simple trap to protect its contents. You will need to disarm it, to see what is inside.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The owner of this chest placed a fairly simple trap to protect its contents. You will need to disarm it, to see what is inside.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["41_2"] = 250
    TownMap.List["Minarch_50"].DeactivateTrigger(Location(4,58))
    pc.RunTrap(eTrapType.BLADE, 1, 30)

def Minarch_1178_CreatureDeath0(p):
    MessageBox("You slay the treacherous Vampire. His body crumples and dissolves into the air. It will be some time before this creature will be able to gather enough power to reform himself. Now, to rescue the miners.")
    StuffDone["26_8"] = 2

def Minarch_1179_TalkingTrigger2(p):
    if StuffDone["26_4"] < 2:
        p.TalkingText = "She grins. \"You really want to help? The entrance to the mine is to the north. If you could rescue the miners, we would reward you well.\" She thinks for a moment.\n\n\"Oh, you may wish to speak with some of the miners that we still have. They hang out at the pub.\""
        StuffDone["26_4"] = 1
        return

def Minarch_1180_TalkingTrigger6(p):
    if StuffDone["26_4"] == 1:
        p.TalkingText = "You agree to allow him to be your guide. He nods, goes off and gathers his equipment. \"Well then, let\'s get going! The mines await.\""
        StuffDone["26_5"] = 1
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Brigand_18": Town.NPCList.Remove(npc)
        SpecialItem.Give("MalthosNPC")
        Message("  Malthos joins the party!")
        return

def Minarch_1181_TalkingTrigger9(p):
    if StuffDone["100_0"] >= 5:
        if StuffDone["27_1"] == 1:
            if StuffDone["26_4"] >= 2:
                p.TalkingText = "You tell of your mission to stop Morbane which requires a Sunstone to be converted from a Moonstone. She thinks it over. \"I would generally say no. But seeing how you rescued those miners and the greater good of the Empire,\n\nI will grant you permission to take the Moonstone.\""
                if StuffDone["27_0"] == 0:
                    StuffDone["27_0"] = 1
                    return
                return
            p.TalkingText = "You tell of your mission to stop Morbane which requires a Sunstone to be converted from a Moonstone. \"I cannot allow you to have the Moonstone, especially in such times. I must care for the well being of this town first.\""
            return
        return

def Talking_50_16(p):
    if Party.Gold >= 6:
        Party.Gold -= 6
        p.TalkingText = "You are served up a round of drinks. One sip makes you feel ill! It is quite different stuff. \"They call it mushroom ale. Has an interesting flavor and takes some getting used to.\" You think you will pass on it from now on."
    else:
        p.TalkingText = "You cannot afford it."

def Talking_50_17(p):
    if Party.Gold < 20:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 20
        Party.Pos = Location(30, 34)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "\"We have a taker!\" He points out your room and wishes you a good night. Unfortunately that wish does not come true. Your sleep is constantly disturbed and brings you little rest."
        CentreView(Party.Pos, False)
