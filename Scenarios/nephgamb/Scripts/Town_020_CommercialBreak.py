
def CommercialBreak_520_MapTrigger_21_11(p):
    result = ChoiceBox("This door leads back into the real world, where the grand battle is brewing, just waiting for you to wake up. Do you return to your harsh lives?", eDialogPic.STANDARD, 25, ["Leave", "Step In"])
    if result == 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(6,55)
        Party.MoveToMap(TownMap.List["FieldofBattle_18"])
        return
    p.CancelAction = True
