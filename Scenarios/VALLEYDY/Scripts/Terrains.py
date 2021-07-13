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

def TerrainTypeStepOn_ConcentratedFilth_457(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Here, the poisonous goo is so concentrated that stepping in it would probably mean a quick, unpleasant death. You decide not to risk it.")

def TerrainTypeStepOn_VirulentFilth_458(p):
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 4))
    Message("The filth diseases you.")
    if StuffDone["100_6"] == 250:
        return
    StuffDone["100_6"] = 250
    MessageBox("You wade through the thin trickle of goo. At first, it seems like it\'s just nasty smelling mud. Then it starts to eat away at your boots, and the vapors begin to burn your skin. You feel violently ill.\n\nWhatever this stuff is, it\'s incredibly poisonous. Worse, it\'s pouring directly into the river that feeds the valley. Also, now it\'s all over you.")
