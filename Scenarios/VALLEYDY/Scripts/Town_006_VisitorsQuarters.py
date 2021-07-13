def Generate_Wandering_6_VisitorsQuarters(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["GoblinFlinger_40"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([1,NPCRecord.List["Wolf_115"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(9,32)
                elif r2 == 1: l = Location(16,19)
                elif r2 == 2: l = Location(25,31)
                elif r2 == 3: l = Location(26,6)
                
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

def VisitorsQuarters_57_MapTrigger_34_1(p):
    ChoiceBox("You peek inside the dresser and find, much to your surprise, a small piece of paper. It looks like it was torn out of a book. A quick inspection reveals it to be a page from the journal of someone named Palhatis:\n\n\"Curse that Vinnia! It is bad enough that we are being shut down. Must she also force us to abdicate all responsibility? I must do all I can to prevent the disaster I expect. If she finds out, though ...\"\n\n\"It is clear that she listens to the Empire and no one else. She works against us as well. I know that she speaks against me. I can hear her now. \'Palhatis schemes against us. Palhatis is a traitor. Palhatis spreads rumors.\'\"\n\n\"I don\'t know what she plans against me, but my speaking out against the evacuation and what we\'re leaving behind have only made me enemies. I wonder what is to become of me.\"\n\nThat\'s all that was written on the page.", eDialogPic.TERRAIN, 145, ["OK"])

def VisitorsQuarters_58_MapTrigger_46_5(p):
    if StuffDone["6_8"] == 250:
        return
    StuffDone["6_8"] = 250
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(46,5))
    MessageBox("Two bodies are slumped against the wall of this cavern. They must have been mages. Their traditional robes still bear not only the insignia of Empire mages, but the dark blood stains of their owners. These two were stabbed to death.\n\nThey\'ve been here for quite some time. Only bones remain, leaving you to wonder: for what offense were these two mages brought here to be murdered?")

def VisitorsQuarters_59_MapTrigger_36_33(p):
    MessageBox("This desk was quite thoroughly cleaned out.")

def VisitorsQuarters_62_MapTrigger_35_42(p):
    MessageBox("What few books were left on these shelves have long since rotted away.")

def VisitorsQuarters_66_MapTrigger_32_34(p):
    if StuffDone["6_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("It\'s impossible to mistake the meaning of the rune etched on the latch. This chest is clearly magically trapped. You may be able to disarm it, but it\'ll be tricky.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("It\'s impossible to mistake the meaning of the rune etched on the latch. This chest is clearly magically trapped. You may be able to disarm it, but it\'ll be tricky.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["6_2"] = 250
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(32,34))
    pc.RunTrap(eTrapType.BLADE, 2, 15)

def VisitorsQuarters_67_MapTrigger_32_37(p):
    MessageBox("Documents of a sensitive nature were once stored in this case. Most of them are gone now. Of the papers that remain, only one makes much sense. It refers to a new exciting development in the levels below: \"A pair of magical pants.\"")

def VisitorsQuarters_68_MapTrigger_29_25(p):
    ChoiceBox("There is a rough map on the wall here, titled \"The Upper Half of the School.\" The map was a mosaic of pretty stones, set into the wall. Most of the stones have been pried out by goblins, but you can make out some of what remains.\n\nThe upper half of the school has five levels: The Entry Hall, the Visitor\'s Quarters (where you are now), the Holding Cells, the Storage Level, and Administration.\n\nThe Holding Cells and Storage Level are just below you, and are both reached by stairways on this level. From there, they both lead down to Administration. The map doesn\'t make clear what is below Administration.", eDialogPic.TERRAIN, 106, ["OK"])

def VisitorsQuarters_70_MapTrigger_9_26(p):
    ChoiceBox("Not surprisingly, this shrine has been violated by the goblins in a very thorough and disgusting way. You clean it up a little bit, but it doesn\'t do much good.", eDialogPic.TERRAIN, 158, ["OK"])

def VisitorsQuarters_71_MapTrigger_3_24(p):
    if StuffDone["6_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("Goblins are not skilled in the area of trap design. The gas trap on this chest is pretty obvious and shouldn\'t be too difficult to disarm.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("Goblins are not skilled in the area of trap design. The gas trap on this chest is pretty obvious and shouldn\'t be too difficult to disarm.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["6_3"] = 250
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(3,24))
    pc.RunTrap(eTrapType.DART, 1, 0)

def VisitorsQuarters_72_MapTrigger_7_41(p):
    if StuffDone["6_1"] == 250:
        return
    StuffDone["6_1"] = 250
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(7,41))
    MessageBox("You stumble into a goblin kitchen. They seem to be in the process of making a savory toadstool and giant rat stew. You decide to pass.")

def VisitorsQuarters_73_MapTrigger_19_11(p):
    if StuffDone["6_4"] == 250:
        return
    StuffDone["6_4"] = 250
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(19,11))
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(19,12))
    MessageBox("This is very interesting ... the goblins seems to have painstakingly torn up the floor and walls in this area, and constructed their own faux caves walls in their place. It\'s like a simulated goblin cave environment.\n\nTotems are everywhere, as are goblin bones, carvings, and bits of graffiti. This must be some sort of temple or burial ground or sacred place or wherever goblins go to get serious.")

def VisitorsQuarters_75_MapTrigger_25_16(p):
    if StuffDone["6_5"] == 250:
        return
    StuffDone["6_5"] = 250
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(25,16))
    TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(26,16))
    MessageBox("Considering the care and reverence with which the goblin bones in the hall have been laid out, you can only suppose that this is where their most valued and respected heroes have been laid to rest.\n\nYou also see the passage down to the next level. It doesn\'t look like many goblins have gone down it.")

def VisitorsQuarters_77_MapTrigger_24_25(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,28)
    Party.MoveToMap(TownMap.List["SchoolEntry_5"])

def VisitorsQuarters_80_MapTrigger_20_39(p):
    if StuffDone["6_7"] == 250:
        return
    result = ChoiceBox("Once upon a time, a goblin tried to run through a fire barrier to see what was on the other side. It didn\'t quite make it.\n\nNot much left of its body. The gem it had in its pocket, however, still managed to survive.", eDialogPic.CREATURE, 35, ["Take", "Leave"])
    if result == 0:
        StuffDone["6_7"] = 250
        TownMap.List["VisitorsQuarters_6"].AlterTerrain(Location(20,39), 1, None)
        TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(20,39))
        Party.GiveNewItem("PiercingCrystal_182")
    return

def VisitorsQuarters_81_MapTrigger_25_44(p):
    if StuffDone["6_6"] == 250:
        return
    result = ChoiceBox("The audience hall of the School of Magery is dominated by a huge, intricately carved throne, no less impressive for the thick layer of dust that covers it. It almost seems to glow with its own light.\n\nDo you dare to sit in it?", eDialogPic.TERRAIN, 161, ["Leave", "Yes"])
    if result == 1:
        StuffDone["6_6"] = 250
        TownMap.List["VisitorsQuarters_6"].AlterTerrain(Location(25,44), 1, None)
        TownMap.List["VisitorsQuarters_6"].DeactivateTrigger(Location(25,44))
        ChoiceBox("The moment you sit down, a flash of light erupts from the empty air in front of you. At first, you think you\'re done for! Then, you realize the only thing that\'s happened is that an insubstantial shade has appeared. It doesn\'t look hostile.\n\nIt stands before you, staring vacantly at the throne. It\'s the ghost of a female mage, tall and imposing, with grim mien and piercing gaze. After a suitably dramatic pause, it speaks:\n\n\"I was Vinnia, last administration of the School of Magery. I regret to announce that the School has been closed at the direct order of the Emperor. It is considered officially Forbidden.\"\n\n\"That you are hearing this means you are here illegally. Not leaving immediately may result in the receiving of 30 years of probably fatal hard labor. Therefore, I strongly suggest you depart. Thank you.\"\n\nThe shade disappears, and the throne loses its glow. The chamber is quiet once more.", eDialogPic.CREATURE, 127, ["OK"])
        return

def VisitorsQuarters_82_MapTrigger_24_23(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,2)
    Party.MoveToMap(TownMap.List["StorageLevel_8"])

def VisitorsQuarters_85_MapTrigger_35_12(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(1,43)
    Party.MoveToMap(TownMap.List["HoldingCells_7"])
