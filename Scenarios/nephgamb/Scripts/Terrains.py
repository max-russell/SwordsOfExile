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
