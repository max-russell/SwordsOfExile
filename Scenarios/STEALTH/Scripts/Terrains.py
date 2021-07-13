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

def TerrainTypeStepOn_FloorwRune_495(p):
    MessageBox("You step on one of Jaen\'s specially designed runes, placed here to help defend his fortress in case of just this sort of emergency. Either the world has just sped up, or you\'ve slowed down. Either way, it\'s bad.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 4))
