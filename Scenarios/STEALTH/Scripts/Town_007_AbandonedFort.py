def Generate_Wandering_7_AbandonedFort(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([1,NPCRecord.List["Ogre_45"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["OgreWarrior_47"]])
            npcs.append([2,NPCRecord.List["Ogre_45"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["OgreFreak_49"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(33,29)
                elif r2 == 1: l = Location(43,6)
                elif r2 == 2: l = Location(27,39)
                elif r2 == 3: l = Location(25,38)
                
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

def AbandonedFort_76_MapTrigger_24_41(p):
    if StuffDone["7_0"] == 250:
        return
    StuffDone["7_0"] = 250
    TownMap.List["AbandonedFort_7"].DeactivateTrigger(Location(24,41))
    TownMap.List["AbandonedFort_7"].DeactivateTrigger(Location(26,41))
    ChoiceBox("You step, for the first time, into the ruins of an old, abandoned Empire outpost. It was quite a structure. These thick walled, reinforced stone tunnels looks like they burrow deep into the hillside.\n\nAlthough Empire soldiers have abandoned the fort, it is clearly occupied. The trash and stench are quite fresh, and you hear deep, guttural mumblings from deep inside the tunnels.", eDialogPic.TERRAIN, 189, ["OK"])

def AbandonedFort_78_MapTrigger_35_26(p):
    MessageBox("This room was used for tactical discussions, and to plan troop movements, and the paperwork needed to be kept somewhere. You approach this bookshelf eagerly, hoping to find, mixed in among the trash, the papers you were sent here to find.\n\nUnfortunately, all you find are scraps of paper, few of them readable. All the papers and journals have been hauled out of here.")

def AbandonedFort_79_MapTrigger_40_18(p):
    if StuffDone["7_1"] == 250:
        return
    StuffDone["7_1"] = 250
    TownMap.List["AbandonedFort_7"].DeactivateTrigger(Location(40,18))
    MessageBox("This room has, for the most part, been left alone by the ogres. This must be where the commander here did most of his planning and logistics. There are charts on the walls, still barely readable, and old pens and scraps of paper litter the floor.\n\nAt the far corner of the room, you see a large bookshelf. Maybe that\'s where the papers you\'re looking for were kept!")

def AbandonedFort_80_MapTrigger_28_17(p):
    if StuffDone["7_2"] == 250:
        return
    StuffDone["7_2"] = 250
    TownMap.List["AbandonedFort_7"].DeactivateTrigger(Location(28,17))
    MessageBox("This was the fort\'s dining hall, and has been kept intact to be used for the same purpose by the ogres. The stew congealing in the pots at the other end of the room smells rotten and horrible. Good for ogres. Not for you.")

def AbandonedFort_81_MapTrigger_22_7(p):
    if StuffDone["7_3"] == 250:
        return
    result = ChoiceBox("Under the blood, muck, and evil markings, you can see that this was once a good altar. The ogres, however, have converted it to their own sinister purposes. It radiates darkness and malevolence.", eDialogPic.TERRAIN, 154, ["Leave", "Pray", "Destroy"])
    if result == 1:
        pc = SelectPCBox("Who prays?",True)
        if pc == None:
            return
        MessageBox("Despite your most sincere intentions, the altar is inclined to reject even the most devout prayers from a human. You feel incredibly ill. Waves of nausea tear through you. When you recover, you feel a bit weaker.")
        pc.SetSkill(eSkill.STRENGTH, pc.GetSkill(eSkill.STRENGTH) - 2)
        return
    elif result == 2:
        MessageBox("You draw your weapons and advance, ready to smash the evil altar into pieces. You don\'t even get near it. Waves of nausea tear through you, knocking you to the ground. When the vomiting and spasms pass, you feel very weak.")
        for pc in Party.EachAlivePC():
            pc.SetSkill(eSkill.STRENGTH, pc.GetSkill(eSkill.STRENGTH) - 2)
        return

def AbandonedFort_82_SanctifyTrigger_22_6(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["7_3"] >= 1:
        MessageBox("The altar has already been destroyed. Your work is done here.")
        return
    if StuffDone["7_3"] == 250:
        return
    StuffDone["7_3"] = 250
    TownMap.List["AbandonedFort_7"].AlterTerrain(Location(22,7), 1, None)
    TownMap.List["AbandonedFort_7"].DeactivateTrigger(Location(22,7))
    MessageBox("Sure, it\'s a powerful evil altar, but nothing a little exorcism can\'t handle. As you sing the holy chants, the altar vibrates, makes a horrible keening noise, and cracks down the middle. You feel satisfied. Good work.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(25)

def AbandonedFort_83_MapTrigger_8_7(p):
    ChoiceBox("You stand at the edge of a dark, dank pit. Tossing a pebble in, you estimate it must be 40 feet deep, maybe more. The breeze blowing up from the pit is icy cold, and the walls are covered with slippery frost. Climbing down won\'t work.\n\nShining a light down, you can barely make out broken ogre bodies at the bottom. Interesting - this pit may be used for executions or sacrifices. You just can\'t be sure why.", eDialogPic.TERRAIN, 244, ["OK"])

def AbandonedFort_84_MapTrigger_12_3(p):
    ChoiceBox("The ogres have created a crude mosaic here, by hammering gaudily painted stones in the crumbling rock of the wall.\n\nYou have to stare for a while, but you eventually figure out what the mosaics are of. One is of ogres being hurled into the pit by other ogres. The ogres being thrown have wide, red smiles.\n\nThe other mosaic is of an enormous blue lizard, breathing a cloud of frost. Ogres are cowering before it, offering it gold and what looks (though you can\'t be sure) like books.", eDialogPic.CREATURE2x1, 2, ["OK"])

def AbandonedFort_85_MapTrigger_20_23(p):
    MessageBox("You search eagerly through and around the commander\'s desk, hoping to find the papers. No luck.")

def AbandonedFort_86_MapTrigger_22_21(p):
    if ChoiceBox("You find a heavy lever. There\'s a lot of rust on the mechanism where it meets the ground. It doesn\'t look too useful.", eDialogPic.STANDARD, 213, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("When you pull the lever, there is a raspy, grinding noise. Nothing else happens.")
        return

def AbandonedFort_87_MapTrigger_20_21(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear the sound of long dormant machinery grinding painfully to life. Then, abruptly, the noise ceases.")
        t = Town.TerrainAt(Location(9,13))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(9,13), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(9,13), 0, TerrainRecord.UnderlayList[130])
        return

def AbandonedFort_88_MapTrigger_24_21(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear the sound of long dormant machinery grinding painfully to life. Then, abruptly, the noise ceases.")
        t = Town.TerrainAt(Location(19,26))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(19,26), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(19,26), 0, TerrainRecord.UnderlayList[130])
        return

def AbandonedFort_89_MapTrigger_11_14(p):
    MessageBox("Most of the useful magical papers and tomes have been removed from here, rather hastily from the looks of things. Some of the papers left behind seem vaguely useful. None, however, are what the Hill Runners seemed to want.")

def AbandonedFort_94_MapTrigger_2_43(p):
    if StuffDone["7_4"] == 250:
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
    StuffDone["7_4"] = 250
    TownMap.List["AbandonedFort_7"].DeactivateTrigger(Location(2,43))
    pc.RunTrap(eTrapType.BLADE, 3, 80)

def AbandonedFort_95_MapTrigger_9_18(p):
    if StuffDone["8_0"] >= 1:
        MessageBox("You return to the stairway down to the drake\'s lair. Unfortunately, the ogres have filled the stairway up with massive chunks of rubble. Looks like that area\'s blocked off.")
        return
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(46,46)
    Party.MoveToMap(TownMap.List["IcyTunnels_8"])
