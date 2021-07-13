
def SmallCave_367_MapTrigger_4_11(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You stand at the far end of a long path, leading back down to the lowest depths of the School of Magery.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(43,13)
    Party.MoveToMap(TownMap.List["ExperimentHalls_14"])

def SmallCave_368_MapTrigger_5_11(p):
    Party.OutsidePos = Location(18, 136)

def SmallCave_369_MapTrigger_25_24(p):
    Party.OutsidePos = Location(64, 5)
