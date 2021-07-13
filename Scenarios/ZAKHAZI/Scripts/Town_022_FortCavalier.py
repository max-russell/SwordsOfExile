def Generate_Wandering_22_FortCavalier(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
            npcs.append([1,NPCRecord.List["SlithPriest_49"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
            npcs.append([1,NPCRecord.List["SlithWarrior_48"]])
            npcs.append([1,NPCRecord.List["SlithMage_50"]])
        elif r1 == 3:
            npcs.append([2,NPCRecord.List["SlithWarrior_48"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(12,7)
                elif r2 == 1: l = Location(39,13)
                elif r2 == 2: l = Location(23,10)
                elif r2 == 3: l = Location(7,17)
                
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

def FortCavalier_518_MapTrigger_10_5(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The fort must have fallen when the sliths punched this hole through the wall. It looks like it was done with massed fireballs. The stone didn\'t so much break as melt.\n\nLooking outside, you see slithzerikai. Lots and lots of them. You back away. Going out there will get you killed, and fast.")

def FortCavalier_522_MapTrigger_46_24(p):
    result = ChoiceBox("Although the fort fell, you may be able to keep yourselves from dying with it. Fort Cavalier had a secret back exit - a hidden tunnel leading out of this outpost.\n\nYou aren\'t sure where it leads, but considering how many sliths are swarming around near here, it may be your best chance to get away.", eDialogPic.STANDARD, 31, ["Leave", "Wait"])
    if result == 0:
        ChoiceBox("The tunnel winds for about two thousand feet, and emerges at a concealed exit behind the slith encirclement. There, you find a pleasant surprise. Not all of Fort Cavalier\'s guardians fell with it.\n\nYou meet 50 Exile soldiers, who escaped when the wall fell. Their leader, Commander Malak, greets you. They\'re rather cold to you, but do agree to take you along in their flight back to Exile.\n\nIt\'s a nasty hike back to Dharmon, the nearest Exile city. There are plenty of skirmishes and close calls, and several casualties. At last, you make it back to safety.\n\nYou are paid 500 gold for your efforts, but get little more acknowledgement. Two weeks later, the slithzerikai attack the city of Dharmon.\n\nThe loss of Fort Cavalier was only one battle of many. However, it is clear that this war is nowhere near over. In fact, it\'s just getting started.\n\nTHE END", eDialogPic.STANDARD, 31, ["OK"])
        Party.Gold += 500
        RunScript("GlobalCall_FortCavalier_694", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    elif result == 1:
        return

def FortCavalier_523_OnEntry(p):
    if StuffDone["22_0"] == 250:
        return
    StuffDone["22_0"] = 250
    ChoiceBox("Hopes high, you march into Fort Cavalier. When you pass through the smoky haze and get a look inside, your high spirits are smashed into the stony ground.\n\nYou were too late.\n\nThe bodies of the brave defenders of Fort Cavalier are scattered in front of you, strewn randomly among the ruined shells of the smoldering buildings they tried to defend.\n\nSlithzerikai are scavenging and looting the ruins. If you\'re going to make it back to Exile, you will need to fight your way through here.\n\nYou look at the bundle of wands, hoping of getting some extra firepower, only to find that it has crumbled into dust. The mages of the Tower of Magi must have thought it better they be destroyed than fall into the hands of the sliths.\n\nWhat a mess.", eDialogPic.CREATURE, 47, ["OK"])
    SpecialItem.Take("BundleofWands")
