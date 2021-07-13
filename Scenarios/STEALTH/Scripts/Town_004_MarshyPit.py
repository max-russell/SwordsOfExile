def Generate_Wandering_4_MarshyPit(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
            npcs.append([1,NPCRecord.List["SwampFolk_189"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(3,21)
                elif r2 == 1: l = Location(45,20)
                elif r2 == 2: l = Location(25,6)
                elif r2 == 3: l = Location(25,40)
                
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

def MarshyPit_43_MapTrigger_45_28(p):
    if StuffDone["4_0"] == 250:
        return
    StuffDone["4_0"] = 250
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(45,28))
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(42,36))
    MessageBox("You find the remains of a patrol of Empire soldiers, bodies scorched and seared by the acid of the swamp folk. Oh well. At least the weird humanoids didn\'t eat them.")

def MarshyPit_45_MapTrigger_44_37(p):
    MessageBox("On the body of this former captain, you find a note. \"Go ahead to swamp point. An informer has told us that there was a Hill Runner outpost out there. He seemed trustworthy. - Valek\"")

def MarshyPit_46_MapTrigger_45_11(p):
    if StuffDone["4_1"] == 250:
        return
    StuffDone["4_1"] = 250
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(45,11))
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(46,25))
    MessageBox("The swamp folk might be vegetarians. They\'re using this room to cultivate large, white toadstools. Piles of compost are arranged about the room to aid growth, and the crop seems to be quite successful.")

def MarshyPit_48_MapTrigger_35_18(p):
    if StuffDone["4_2"] == 250:
        return
    StuffDone["4_2"] = 250
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(35,18))
    MessageBox("At first, you think the Swamp Folk have piled huge piles of slime and gook in their lairs. Then you realize that these are the creature\'s beds. They sleep in large heaps of compost!\n\nThe result of all this compost is that these caves are very warm and smelly. At least there don\'t seem to be lethal amounts of methane.")

def MarshyPit_49_MapTrigger_13_18(p):
    if StuffDone["4_3"] == 250:
        return
    StuffDone["4_3"] = 250
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(13,18))
    TownMap.List["MarshyPit_4"].DeactivateTrigger(Location(18,14))
    MessageBox("Like most humanoid races, the swamp folk seem to have a freaky religion all their own. They\'ve painstakingly carved out several obelisks here, and etched drawings in the sides with their own acidic secretions.\n\nThere are also piles of rocks, each topped with one or two of the pretty geodes you\'ve found in these caves.")
