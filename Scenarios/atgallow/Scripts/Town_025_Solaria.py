
def Solaria_458_MapTrigger_31_4(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,56)
    Party.MoveToMap(TownMap.List["ImperialPalace_26"])

def Solaria_461_MapTrigger_31_59(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,6)
    Party.MoveToMap(TownMap.List["ImperialLibrary_27"])

def Solaria_464_MapTrigger_31_12(p):
    if StuffDone["100_0"] == 6:
        if StuffDone["32_1"] == 0:
            StuffDone["32_1"] = 1
            Animation_Hold(-1, 062_mmm)
            Wait()
            ChoiceBox("CHAPTER VI -- THE TRUTH BE TOLD", eDialogPic.STANDARD, 1026, ["OK"])
            return
        return

def Solaria_469_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 36),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(35, 36),WorldMap.SectorAt(Party.OutsidePos))

def Talking_25_14(p):
    if Party.Gold >= 100:
        Party.Gold -= 100
        p.TalkingText = "You pay the exorbitant fee and are given a bottle of wine. The drink is smooth and one of the best you have ever had. However, you doubt that it is worth the price. But, that is what the locals are willing to pay."
    else:
        p.TalkingText = "\"I\'m sorry the finest wines in the entire world cannot be given away cheaply.\""

def Talking_25_15(p):
    if Party.Gold < 250:
        p.TalkingText = "\"Come now, the rooms are fit for the Emperor. They must be filled by only the finest paying tenants."
    else:
        Party.Gold -= 250
        Party.Pos = Location(16, 13)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "You pay the exorbitant fee and Unger calls a servant to carry your items. The room is one of the most luxurious you have seen and your rest is very comforting. However, your pockets feel much emptier."
        CentreView(Party.Pos, False)
