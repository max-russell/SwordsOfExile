def Generate_Wandering_9_LizardPit(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["GiantLizard_72"]])
            npcs.append([1,NPCRecord.List["GiantLizard_72"]])
            npcs.append([1,NPCRecord.List["FireLizard_73"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["GiantLizard_72"]])
            npcs.append([1,NPCRecord.List["IceLizard_74"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["ViscousGoo_77"]])
            npcs.append([1,NPCRecord.List["ViscousGoo_77"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["FireLizard_73"]])
            npcs.append([1,NPCRecord.List["IceLizard_74"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(9,34)
                elif r2 == 1: l = Location(11,36)
                elif r2 == 2: l = Location(8,36)
                elif r2 == 3: l = Location(10,34)
                
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

def LizardPit_219_MapTrigger_10_31(p):
    StuffDone["9_0"] = 1

def LizardPit_220_MapTrigger_23_19(p):
    if StuffDone["9_1"] == 250:
        return
    StuffDone["9_1"] = 250
    TownMap.List["LizardPit_9"].DeactivateTrigger(Location(23,19))
    MessageBox("Sweat is gathering on your brows. The corridor is getting warmer as you proceed.")

def LizardPit_221_MapTrigger_38_35(p):
    MessageBox("You have never figured out if the presence of drakes causes hot terrain or if hot terrain attracts drakes. Some law of nature seems to draw them together. As you consider this, you watch the lava. Shifting tides make little islets appear and disappear.")
    SuspendMapUpdate()
    for x in range(38, 40):
        for y in range(37, 38):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_222_MapTrigger_38_37(p):
    SuspendMapUpdate()
    for x in range(34, 35):
        for y in range(35, 37):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_223_MapTrigger_35_37(p):
    t = Town.TerrainAt(Location(36,38))
    if t == TerrainRecord.UnderlayList[75]: Town.AlterTerrain(Location(36,38), 0, TerrainRecord.UnderlayList[0])
    elif t == TerrainRecord.UnderlayList[0]: Town.AlterTerrain(Location(36,38), 0, TerrainRecord.UnderlayList[75])

def LizardPit_224_MapTrigger_36_38(p):
    for x in range(32, 34):
        for y in range(35, 36):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    SuspendMapUpdate()
    for x in range(34, 35):
        for y in range(35, 37):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_225_MapTrigger_38_39(p):
    SuspendMapUpdate()
    for x in range(34, 35):
        for y in range(38, 40):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_226_MapTrigger_34_37(p):
    SuspendMapUpdate()
    for x in range(32, 33):
        for y in range(36, 38):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
    ResumeMapUpdate()
    for x in range(32, 34):
        for y in range(35, 36):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    SuspendMapUpdate()
    for x in range(34, 35):
        for y in range(35, 37):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_227_MapTrigger_34_38(p):
    SuspendMapUpdate()
    for x in range(28, 30):
        for y in range(37, 38):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
    ResumeMapUpdate()

def LizardPit_229_MapTrigger_34_36(p):
    SuspendMapUpdate()
    for x in range(29, 30):
        for y in range(38, 40):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_230_MapTrigger_33_35(p):
    SuspendMapUpdate()
    for x in range(30, 32):
        for y in range(35, 36):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_233_MapTrigger_30_35(p):
    SuspendMapUpdate()
    for x in range(32, 33):
        for y in range(38, 40):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_234_MapTrigger_32_39(p):
    t = Town.TerrainAt(Location(31,38))
    if t == TerrainRecord.UnderlayList[0]: Town.AlterTerrain(Location(31,38), 0, TerrainRecord.UnderlayList[75])
    elif t == TerrainRecord.UnderlayList[75]: Town.AlterTerrain(Location(31,38), 0, TerrainRecord.UnderlayList[0])
    SuspendMapUpdate()
    for x in range(29, 30):
        for y in range(38, 40):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_235_MapTrigger_31_38(p):
    SuspendMapUpdate()
    for x in range(30, 32):
        for y in range(39, 40):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
    ResumeMapUpdate()

def LizardPit_239_MapTrigger_17_35(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("A short set of stairs winds up to the surface, ending at a rock wall. You can see a lever that opens the door from your side. You guess this is a secret door that can?t be seen from the other side.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(7,23)
    Party.MoveToMap(TownMap.List["YvosstaiCamp_15"])

def LizardPit_240_MapTrigger_32_29(p):
    MessageBox("In the combined treasure and garbage pile of the drakes, a finely bound book draws your eye. You pick it up, and find that it is a spell book! You devour it, and in short time learn the priest spell `Flamestrike?.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_flamestrike")

def LizardPit_241_TownTimer_0(p):
    if StuffDone["9_0"] >= 1:
        return
    t = Town.TerrainAt(Location(10,32))
    if t.InGroup("Unlockable"):
        t = Town.TerrainAt(Location(10,32)).TransformTo
        Town.AlterTerrain(Location(10,32), 0, t)
    MessageBox("The commotion draws another group of hungry lizards to the feeding ground. The portcullis opens to admit them.")
    RunScript("Generate_Wandering_9_LizardPit", ScriptParameters(eCallOrigin.CUSTOM))
    Timer(Town, 5, False, "LizardPit_242_TownTimer_4", eTimerType.DELETE)

def LizardPit_242_TownTimer_4(p):
    t = Town.TerrainAt(Location(10,32))
    if t.InGroup("Lockable"):
        t = Town.TerrainAt(Location(10,32)).TransformTo
        Town.AlterTerrain(Location(10,32), 0, t)
    Timer(Town, 20, False, "LizardPit_241_TownTimer_0", eTimerType.DELETE)

def LizardPit_243_OnEntry(p):
    Timer(Town, 20, False, "_UNKNOWN_", eTimerType.DELETE)
