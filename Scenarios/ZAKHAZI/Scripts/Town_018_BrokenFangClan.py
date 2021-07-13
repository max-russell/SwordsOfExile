def Generate_Wandering_18_BrokenFangClan(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Troglodyte_149"]])
            npcs.append([1,NPCRecord.List["Troglodyte_149"]])
            npcs.append([1,NPCRecord.List["Troglodyte_149"]])
            npcs.append([2,NPCRecord.List["TroglodyteWarrior_150"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Slith_47"]])
            npcs.append([1,NPCRecord.List["Slith_47"]])
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(18,31)
                elif r2 == 1: l = Location(17,14)
                elif r2 == 2: l = Location(17,22)
                elif r2 == 3: l = Location(17,23)
                
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

def BrokenFangClan_429_MapTrigger_11_24(p):
    if StuffDone["18_0"] == 250:
        return
    StuffDone["18_0"] = 250
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(11,24))
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(11,23))
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(11,22))
    MessageBox("The Empire slew most of the troglodytes on the surface. The few survivors, their existing hatred of humanity inflamed to a fever pitch, fled into the underworld. A large group of them have moved here.\n\nIt looks like this is not just a fortress, but a meeting point for all manner of human-hating creatures. Several of them are nearby, ready to fight and die to keep you out.")

def BrokenFangClan_432_MapTrigger_16_19(p):
    if StuffDone["18_1"] == 250:
        return
    StuffDone["18_1"] = 250
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(16,19))
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(17,19))
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(19,18))
    MessageBox("This section of the fortress is dedicated to several small shops, where evil creatures can come to trade and sell their ill-gotten gains and gain new weapons to do horrible deeds with. It\'s time to put them out of business ...")

def BrokenFangClan_435_MapTrigger_18_33(p):
    if StuffDone["18_2"] == 250:
        return
    StuffDone["18_2"] = 250
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(18,33))
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(13,30))
    MessageBox("Spiny Worms are incredibly stupid, ill-tempered creatures. Not so stupid and ill-tempered, however, that they can\'t be tamed and raised by the even more ill-tempered (though not stupid) troglodytes.\n\nThe worms are raised in this ruined section of castle. There\'s currently several of them here, and they are, as always, hungry.")

def BrokenFangClan_437_MapTrigger_33_6(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["18_3"] >= 1:
            MessageBox("You can\'t budge the lever. You already destroyed the mechanism. Nobody will be able to close the gate again any time soon.")
            return
        MessageBox("With the loud shrieking of heavy gears, the portcullis outside blocking the river slowly opens, clearing a path for a boat to pass. You take a few moments to smash the mechanism, so that the troglos can\'t close it once you\'re gone.")
        t = Town.TerrainAt(Location(28,5))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(28,5), 0, TerrainRecord.UnderlayList[71])
        elif t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(28,5), 0, TerrainRecord.UnderlayList[130])
        StuffDone["18_3"] = 1
        return

def BrokenFangClan_438_MapTrigger_34_40(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["18_4"] >= 1:
            MessageBox("You can\'t budge the lever. You already destroyed the mechanism. Nobody will be able to close the gate again any time soon.")
            return
        MessageBox("With the loud shrieking of heavy gears, the portcullis outside blocking the river slowly opens, clearing a path for a boat to pass. You take a few moments to smash the mechanism, so that the troglos can\'t close it once you\'re gone.")
        StuffDone["18_4"] = 1
        Town.AlterTerrain(Location(28,42), 0, TerrainRecord.UnderlayList[71])
        return

def BrokenFangClan_439_MapTrigger_44_32(p):
    if StuffDone["18_5"] == 250:
        return
    StuffDone["18_5"] = 250
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(44,32))
    MessageBox("This room is filled with a large pit. Its ten feet deep, and the floor is covered with a large number of bones. A narrow stone bridge spans the hole.")

def BrokenFangClan_440_MapTrigger_44_35(p):
    if StuffDone["18_6"] == 250:
        return
    StuffDone["18_6"] = 250
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(44,35))
    MessageBox("Suddenly, you trip a trap! The bridge you\'re on is hinged at the north and south ends. It splits apart in the middle, and both sides swing down, dumping you into the pit. Insubstantial creatures step forward from the shadows to kill you.\n\nYou try to get up quickly to fight them, but the fall has left you shaken up. It\'ll take you a moment to regain your wits ...")
    Town.PlaceEncounterGroup(1)
    for x in range(42, 47):
        for y in range(33, 37):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[82])
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 4))

def BrokenFangClan_441_MapTrigger_46_41(p):
    if StuffDone["18_7"] == 250:
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
    StuffDone["18_7"] = 250
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(46,41))
    pc.RunTrap(eTrapType.GAS, 1, 40)

def BrokenFangClan_442_MapTrigger_42_31(p):
    MessageBox("The troglodyte chief has written a journal of his dealings with the evil slithzerikai army. They\'ve been trying to buy troglodyte help, so that they can get through the Za-Khazi Run easily.\n\nThe troglos and sliths seem to get along very well. If this deal went through, it could be trouble for Exile. Fortunately, killing so many of the troglos here has probably put a kink in their plans.")

def BrokenFangClan_443_MapTrigger_38_28(p):
    if StuffDone["18_8"] == 250:
        return
    result = ChoiceBox("The troglodyte\'s altar has several large prayer mats in front of it, all of which are worn and threadbare from constant use. The altar itself is a black and grisly affair, covered with gross, meaty offerings from the tribe\'s warriors.\n\nYou\'re warriors too. Maybe the altar will help you if you bow to it.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        MessageBox("The altar was built by troglodytes, for troglodytes. It has no interest in your obedience. It drains quite of bit of life energy out of you before you finally manage to pull yourselves away.")
        Party.HealAll(-100)
        return

def BrokenFangClan_444_SanctifyTrigger_38_27(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["18_8"] == 250:
        return
    StuffDone["18_8"] = 250
    TownMap.List["BrokenFangClan_18"].AlterTerrain(Location(38,28), 1, None)
    TownMap.List["BrokenFangClan_18"].DeactivateTrigger(Location(38,28))
    MessageBox("The power of the altar is strong, but it\'s no match for your holy spells. The stone cracks, and a cloud of sulphurous smoke belches forth.\n\nThe power source of the altar is liberated by your action. Unfortunately, that power takes physical form in order to get its revenge upon you.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(10)
    Town.PlaceEncounterGroup(2)

def BrokenFangClan_445_OnEntry(p):
    if StuffDone["18_3"] >= 1:
        Town.AlterTerrain(Location(28,5), 0, TerrainRecord.UnderlayList[71])
        if StuffDone["18_4"] >= 1:
            Town.AlterTerrain(Location(28,42), 0, TerrainRecord.UnderlayList[71])
            return
        return
    if StuffDone["18_4"] >= 1:
        Town.AlterTerrain(Location(28,42), 0, TerrainRecord.UnderlayList[71])
        return
