def Generate_Wandering_45_Gwas(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([2,NPCRecord.List["Nephil_40"]])
        elif r1 == 1:
            npcs.append([2,NPCRecord.List["Nephil_40"]])
        elif r1 == 2:
            npcs.append([2,NPCRecord.List["Nephil_40"]])
        elif r1 == 3:
            npcs.append([2,NPCRecord.List["Nephil_40"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(12,49)
                elif r2 == 1: l = Location(26,50)
                elif r2 == 2: l = Location(39,46)
                elif r2 == 3: l = Location(46,53)
                
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

def Gwas_1067_MapTrigger_50_30(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You have discovered a well concealed cave-like opening in the rocks. It is quite small, but you should be able to fit through. The cave slopes downward, and you are not sure if you\'ll be able to get back up this way, do you climb down?", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(50,36)
    Party.MoveToMap(TownMap.List["Gwas_45"])

def Gwas_1068_MapTrigger_50_35(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This passage is too steep to go back up. You\'ll just have to continue on. You hope that you have not inadvertently trapped yourselves here. It would be a long time until someone found you.")

def Gwas_1069_MapTrigger_47_58(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever and creaky machinery is activated. As you assumed, it affects the portcullis just outside.")
        t = Town.TerrainAt(Location(44,57)).TransformTo
        Town.AlterTerrain(Location(44,57), 0, t)
        if StuffDone["35_1"] == 0: StuffDone["35_1"] = 1
        else: StuffDone["35_1"] = 0
        return

def Gwas_1070_MapTrigger_44_58(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(44,57)).Num == 130:
        MessageBox("You appear to have discovered some sort of underground Nephilim bandit lair. Sadly, the entrance is closed and no one is going to open it for you. You aren\'t going to get in this way.")
        return

def Gwas_1071_MapTrigger_31_54(p):
    if StuffDone["35_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("This hallway is lined with runes. Although you cannot be completely sure, they appear to be some kind of trap. You will need to disarm it to continue.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("This hallway is lined with runes. Although you cannot be completely sure, they appear to be some kind of trap. You will need to disarm it to continue.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["35_2"] = 250
    TownMap.List["Gwas_45"].DeactivateTrigger(Location(31,54))
    pc.RunTrap(eTrapType.GAS, 0, 60)

def Gwas_1072_MapTrigger_29_54(p):
    if StuffDone["35_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("This hallway is lined with runes. Although you cannot be completely sure, they appear to be some kind of trap. You will need to disarm it to continue.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("This hallway is lined with runes. Although you cannot be completely sure, they appear to be some kind of trap. You will need to disarm it to continue.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["35_3"] = 250
    TownMap.List["Gwas_45"].DeactivateTrigger(Location(29,54))
    pc.RunTrap(eTrapType.DISEASE, 3, 60)

def Gwas_1073_ExitTown(p):
    if p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 40),WorldMap.SectorAt(Party.OutsidePos))
    if p.Dir.IsSouth:
        StuffDone["35_1"] = 0

def Gwas_1074_CreatureDeath8(p):
    MessageBox("You strike down the rogue trader captain, the leader of the bandits. You decide to take his sash as proof of his death. Undoubtedly, these bandits will be much weaker without his leadership.")
    StuffDone["24_2"] = 1

def Gwas_1075_TalkingTrigger27(p):
    if StuffDone["34_9"] == 0:
        if StuffDone["35_1"] == 1:
            StuffDone["34_9"] = 1
            StuffDone["35_0"] = 1
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Witch_31": Town.NPCList.Remove(npc)
            Party.GiveNewItem("WeakSkillP_266")
            return
        p.TalkingText = "\"The exit is not far from here. My scrys tell me the gate is still closed. It would be risky for me to try to reach the controls in my condition. If you could open the gate for me, I could escape.\""
        return

def Talking_45_22(p):
    if Party.Gold >= 10:
        Party.Gold -= 10
        p.TalkingText = "\"That will be ten gold.\" You pay up and receive a round of drinks. The beer is probably some of the lowest grade you\'ve ever had."
    else:
        p.TalkingText = "\"That will be ten gold.\" Sadly, you can\'t afford it."

def Talking_45_23(p):
    if Party.Gold < 20:
        p.TalkingText = "\"That will be twenty gold!\" Sadly, you cannot afford it."
    else:
        Party.Gold -= 20
        Party.Pos = Location(54, 20)
        Town.UpdateVisible()
        Party.HealAll(0, True)
        Party.RestoreSP(0)
        p.TalkingText = "\"That will be twenty gold!\" You hand it over and are pointed out to a room. You are sorry you decided to spend the night. The beds are very uncomfortable and noisy."
        CentreView(Party.Pos, False)
