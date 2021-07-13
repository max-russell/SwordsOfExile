def Generate_Wandering_84_GoblinFarms(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([2,NPCRecord.List["Goblin_38"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([2,NPCRecord.List["Goblin_38"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([2,NPCRecord.List["Goblin_38"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([2,NPCRecord.List["Goblin_38"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(23,18)
                elif r2 == 1: l = Location(16,23)
                elif r2 == 2: l = Location(22,32)
                elif r2 == 3: l = Location(30,18)
                
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

def GoblinFarms_2087_MapTrigger_10_27(p):
    if StuffDone["32_7"] == 250:
        return
    StuffDone["32_7"] = 250
    TownMap.List["GoblinFarms_84"].DeactivateTrigger(Location(10,27))
    TownMap.List["GoblinFarms_84"].DeactivateTrigger(Location(9,27))
    TownMap.List["GoblinFarms_84"].DeactivateTrigger(Location(11,27))
    MessageBox("As soon as you enter this silo, you are assaulted by a horrid smell you will never forget. It is the unmistakable smell of rotting flesh. You look about the silo seeing tens of decaying bodies of murdered farmers. Yuck!")

def GoblinFarms_2090_MapTrigger_33_30(p):
    if StuffDone["32_8"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("There is a wire suspended in this hallway. It is positioned so you cannot go under or above it. You will have to disarm it to pass. Do you try?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("There is a wire suspended in this hallway. It is positioned so you cannot go under or above it. You will have to disarm it to pass. Do you try?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["32_8"] = 250
    TownMap.List["GoblinFarms_84"].DeactivateTrigger(Location(33,30))
    pc.RunTrap(eTrapType.BLADE, 0, 15)

def GoblinFarms_2091_OnEntry(p):
    if StuffDone["32_6"] == 250:
        return
    StuffDone["32_6"] = 250
    MessageBox("Well this appears to be the place Captain Relah told you about. This farming area looks like it hasn\'t been tended to in a while.  The grass overgrown and the crops browning, Goblins were never the lords of maintenance.\n\nWell, perhaps you should have a look around this place.")

def GoblinFarms_2092_CreatureDeath0(p):
    MessageBox("The mage is dead. Now you know why the goblins have been so successful; they were really pawns of a fanatic, power-hungry mage. Now he is gone, the garrison in Linn can make a better stand.")
    StuffDone["32_5"] = 1
