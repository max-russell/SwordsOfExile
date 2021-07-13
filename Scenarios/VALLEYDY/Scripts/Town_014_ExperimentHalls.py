def Generate_Wandering_14_ExperimentHalls(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["GiantRat_78"]])
            npcs.append([1,NPCRecord.List["GiantRat_78"]])
            npcs.append([1,NPCRecord.List["GiantRat_78"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["RatCreature_195"]])
            npcs.append([1,NPCRecord.List["RatCreature_195"]])
            npcs.append([2,NPCRecord.List["GiantRat_78"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["RatCreature_195"]])
            npcs.append([1,NPCRecord.List["RatCreature_195"]])
            npcs.append([1,NPCRecord.List["MungRat_80"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(24,22)
                elif r2 == 1: l = Location(11,38)
                elif r2 == 2: l = Location(24,26)
                elif r2 == 3: l = Location(22,13)
                
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

def ExperimentHalls_286_MapTrigger_21_5(p):
    if StuffDone["14_0"] == 250:
        return
    StuffDone["14_0"] = 250
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(21,5))
    ChoiceBox("In this chamber, the School of Magery kept their valued school mascot, \'Spiny.\' When they abandoned the school, they left their mascot behind.\n\nUnfortunately, their mascot, a long, vicious worm, is a very long lived creature. Feeding on the denizens of the school has helped it grow large, and it\'s imprisonment has put it in a very bad mood.", eDialogPic.CREATURE2x1, 5, ["OK"])
    Town.PlaceEncounterGroup(1)

def ExperimentHalls_287_MapTrigger_28_5(p):
    p.CancelAction = True
    ChoiceBox("The copious amounts of virulent waste produced by the school\'s experiments were thrown into this portal. The waste disposal faculties were probably at the other end.\n\nThe portal is running on low power now, and is incapable of carrying anything anywhere. The waste here will just have to stay here.", eDialogPic.STANDARD, 22, ["OK"])

def ExperimentHalls_288_MapTrigger_25_5(p):
    if StuffDone["14_1"] == 250:
        return
    StuffDone["14_1"] = 250
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(25,5))
    MessageBox("You detect the too familiar burning scent of unprocessed School waste. Oh no. Not again.")

def ExperimentHalls_289_MapTrigger_45_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(45,45)
    Party.MoveToMap(TownMap.List["Libraries_13"])

def ExperimentHalls_291_MapTrigger_1_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(2,31)
    Party.MoveToMap(TownMap.List["LectureHalls_12"])

def ExperimentHalls_293_MapTrigger_42_1(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You yank the lever. There\'s a brief grinding noise and the smell of smoke. Nothing else happens.")
        return

def ExperimentHalls_294_MapTrigger_5_1(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear the sound of portcullises opening. Or closing. You aren\'t sure.")
        SuspendMapUpdate()
        for x in range(12, 14):
            for y in range(15, 16):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[130]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[131])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[131]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[130])
        ResumeMapUpdate()
        return

def ExperimentHalls_295_MapTrigger_18_27(p):
    MessageBox("Someone has carelessly left a note on top of this desk. It\'s brittle and yellowed with age, but still readable. \"It is time. Get Palhatis and Pergaltho to Visitor\'s Quarters. I will do the rest. - Vinnia\"")

def ExperimentHalls_296_MapTrigger_4_18(p):
    MessageBox("This book still contains notes on experiments carried out on this level. The most recent experiment listed regarded the development of a new acid creation spell. The listing mentions \"High spill potential.\"")

def ExperimentHalls_297_MapTrigger_4_20(p):
    MessageBox("This book still contains notes on experiments carried out on this level. The most recent experiment listed regarded something called \"Garment augmentation.\" Whatever that means.")

def ExperimentHalls_298_MapTrigger_4_22(p):
    MessageBox("This book still contains notes on experiments carried out on this level. The most recent experiment regarded the dissection of creatures called \"Alien beasts.\"\n\nThe beasts were being kept in the holding cells on this level. The book mentions that care should be taken because of their \"High escape potential.\"")

def ExperimentHalls_299_MapTrigger_13_41(p):
    if StuffDone["14_2"] == 250:
        return
    StuffDone["14_2"] = 250
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(13,41))
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(16,39))
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(17,42))
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(12,42))
    MessageBox("You see the holding cells for the Experimentation Level. Unsurprisingly, considering how things have been going so far, whatever was living in here broke its way out some time ago, leaving rubble behind.")

def ExperimentHalls_303_MapTrigger_24_37(p):
    Party.OutsidePos = Location(18, 136)

def ExperimentHalls_305_MapTrigger_24_42(p):
    Party.OutsidePos = Location(64, 99)
    SuspendMapUpdate()
    for x in range(24, 26):
        for y in range(35, 36):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetUnlocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()

def ExperimentHalls_307_MapTrigger_24_34(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(24,35)).Num == 128:
        if SpecialItem.PartyHas("BrassKey"):
            MessageBox("You find a pair of double doors, held shut with a large brass padlock. Fortunately, your brass key fits easily. You unlock the doors.")
            SuspendMapUpdate()
            for x in range(24, 26):
                for y in range(35, 36):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("This exit is barred by two doors. They\'re standard issue heavy wooden doors, with a large padlock holding them closed. You try to get the padlock open, but even heavy blows don\'t affect it in the slightest.\n\nLooks like yet another magical obstruction, and you don\'t have the key.")
        return

def ExperimentHalls_309_MapTrigger_46_19(p):
    if StuffDone["14_3"] == 250:
        return
    StuffDone["14_3"] = 250
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(46,19))
    TownMap.List["ExperimentHalls_14"].DeactivateTrigger(Location(28,42))
    MessageBox("This double reinforced bunker holds the laboratories where the most dangerous and powerful experiments took place. A sour acidic smell reaches your sensitive adventurer\'s noses. There\'s been some sort of nasty spill.")

def ExperimentHalls_311_MapTrigger_42_12(p):
    TownMap.List["SmallCave_20"].Hidden = False

def ExperimentHalls_313_MapTrigger_44_13(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You stand at a hidden rear exit of the School of Magery, a several mile long passage, lit by long-lasting magical lamps, which students and faculty could use to escape quickly, if necessary. The tunnel slopes gently up and out.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(6,11)
    Party.MoveToMap(TownMap.List["SmallCave_20"])
