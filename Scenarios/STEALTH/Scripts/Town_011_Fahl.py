def Generate_Wandering_11_Fahl(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Bear_117"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Wolf_115"]])
            npcs.append([1,NPCRecord.List["Wolf_115"]])
            npcs.append([1,NPCRecord.List["Wolf_115"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(25,11)
                elif r2 == 1: l = Location(41,8)
                elif r2 == 2: l = Location(25,8)
                elif r2 == 3: l = Location(9,8)
                
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

def Fahl_149_MapTrigger_36_10(p):
    ChoiceBox("As you pick through the rubble here, you notice you\'re seeing a lot of broken weapons and scraps of armor. Several of the scraps of armor have Empire soldier insignia on them.\n\nIt looks like there was a medium to large sized Empire garrison here. It\'s gone now, replaced by mounds of shattered stone.", eDialogPic.TERRAIN, 85, ["OK"])

def Fahl_150_OnEntry(p):
    if StuffDone["11_4"] == 250:
        return
    StuffDone["11_4"] = 250
    ChoiceBox("You enter the ruins of the city of Fahl. In your years of adventuring, you have never seen destruction as stunning and lethal as this.\n\nThe northwest and northeast corners of the city have been completely caved in. A hundred giants could not have destroyed the walls more thoroughly. It was not blows that stove in the walls, however, but fire.\n\nSomehow, a fiery explosion shattered this towns defenses, and the flames greedily spread to other areas of the town. Its northern walls destroyed almost beyond repair, the Empire had no choice but to abandon this city before the rebels attacked.\n\nThat the Hill Runners are capable of doing this, of wreaking devastation of this magnitude, is truly alarming. The Empire has done a good job of keeping this quiet, and you can see why.\n\nWhat is equally disconcerting is that, as far as you can tell, this was nothing but a peaceful logging village. Why would the rebels, supposedly concerned with the lot of the people, target this place?", eDialogPic.TERRAIN, 85, ["OK"])

def Fahl_151_TalkingTrigger10(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "He cooks you up a large, hearty meal of wild turkey with all the trimmings. He even lets you have a healthy pile of leftovers to take with you."
        Party.Food += 10
        return

def Talking_11_11(p):
    if Party.Gold < 6:
        p.TalkingText = "He shakes his head. \"No charity out here, friend. Five gold it is.\""
    else:
        Party.Gold -= 6
        Party.Pos = Location(38, 38)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "You pay the 6 gold, and are shown to the finest room in the hotel. It\'s chilly, and slightly creepy, but the bed is very comfortable, and the next morning Sunde serves you breakfast."
        CentreView(Party.Pos, False)
