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

def TerrainTypeStepOn_HeavyRubble_691(p):
    Party.Age += 30
    Message("The rubble is very heavy.")
    Message("It takes a while to pass it.")

def TerrainTypeStepOn_BigMushrooms_692(p):
    if SpecialItem.PartyHas("MushroomTalisman"):
        if StuffDone["204_4"] == 250:
            return
        StuffDone["204_4"] = 250
        MessageBox("As you walk through these mushrooms, you accidentally step on one. A huge cloud of soporific spores sprays out, covering you. The spores make you feel woozy and light headed. You also start to giggle uncontrollably.\n\nAmazingly, however, you stay somewhat awake and moderately alert. Instead of stopping you in your tracks, the spores just slow you down a little. Something must be protecting you.")
        return
    MessageBox("As you walk through these mushrooms, clouds of gray spores rise from them. Inhaling them makes you feel very drowsy. You wobble for a bit and then fall over.\n\nYou wake up a few hours later. More time has been lost.")
    Party.Age += 400
