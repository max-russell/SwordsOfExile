def Do_Sign(p):
    MessageBox(p.Vars["Msg"])

def Do_Waterfall(p):
    Sound.Play("028_waterfall")
    p.CancelAction = True
    p.PC.ForceMove(Location(p.Target.X, p.Target.Y + 2), Direction(eDir.S))
    Wait()
    if Party.HasTrait(Trait.CaveLore) and Maths.Rand(1,0,1) == 0:
        Message("  (No supplies lost.)")
    elif Party.Food > 1800:
        Party.Food -= 50
    else:
        Party.Food = (Party.Food * 19) / 20

def Do_Conveyor_Belt(p):
    d = p.Vars["Dir"]
    if p.Origin == eCallOrigin.MOVING:
        if (p.PC.Pos.X > p.Target.X and d == 1) or \
           (p.PC.Pos.X < p.Target.X and d == 3) or \
           (p.PC.Pos.Y > p.Target.Y and d == 2) or \
           (p.PC.Pos.Y < p.Target.Y and d == 0):
            p.CancelAction = True
            Message("The moving floor prevents you.")
    if p.Origin == eCallOrigin.PC_STOOD_ON:
        Message("You get pushed.")
        if d == 0:
            p.PC.ForceMove(p.PC.Pos.Mod(0,-1), Direction(eDir.N))
        elif d == 1:
            p.PC.ForceMove(p.PC.Pos.Mod(1,0), Direction(eDir.E))
        elif d == 2:
            p.PC.ForceMove(p.PC.Pos.Mod(0,1), Direction(eDir.S))
        elif d == 3:
            p.PC.ForceMove(p.PC.Pos.Mod(-1,0), Direction(eDir.W))
    if p.Origin == eCallOrigin.NPC_STOOD_ON:
        if d == 0:
            p.NPCTarget.Walk(eDir.N)
        elif d == 1:
            p.NPCTarget.Walk(eDir.E)
        elif d == 2:
            p.NPCTarget.Walk(eDir.S)
        elif d == 3:
            p.NPCTarget.Walk(eDir.W)

def TerrainLocal_Mist_179(p):
    if Game.Mode != eMode.OUTSIDE and Town.Num == 23:
        RunScript("TerrainTypeStepOn_Mist_UnderSiege_2902", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 32:
        RunScript("BalkisEstate_645_MapTrigger_36_20", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 44:
        RunScript("TerrainTypeStepOn_Mist_WatchpointTowerL3_2903", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 55:
        RunScript("Sanctuary_1359_TownTimer_86", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 56:
        RunScript("TerrainTypeStepOn_Mist_Aerie_2904", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 72:
        RunScript("IsolatedVillage_1834_MapTrigger_7_59", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 77:
        RunScript("TerrainTypeStepOn_Mist_AncientLab_2905", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 79:
        RunScript("GallowsKeep_1988_MapTrigger_32_29", p)
        return
    if Game.Mode != eMode.OUTSIDE and Town.Num == 80:
        RunScript("TerrainTypeStepOn_Mist_GallowsKeep_2906", p)
        return
