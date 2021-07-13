
def Aguara_454_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 35),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 36),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(21, 36),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(21, 36),WorldMap.SectorAt(Party.OutsidePos))

def Aguara_455_TalkingTrigger22(p):
    count = Party.CountItemClass(5, True)
    Party.Gold += count * 15
    p.TalkingText = "You hand over your asp fangs and he pays you 15 gold coins per pair."

def Aguara_456_TalkingTrigger30(p):
    if SpecialItem.PartyHas("ShimmeringPendant"):
        SpecialItem.Take("ShimmeringPendant")
        p.TalkingText = "You return the Pendant to Challor. \"Well, I guess I can tell you. When we slew Halloth, we returned the sword. Lyra is located in a hidden pit in the center of the Aguara Swamps. You\'ll need a boat to get there.\""
        StuffDone["5_5"] = 2
        TownMap.List["LyraCave_19"].Hidden = False
        return
    if StuffDone["5_5"] >= 2:
        p.TalkingText = "\"Thank you for returning my pendant.\""
        return

def Aguara_457_TalkingTrigger40(p):
    if StuffDone["5_5"] >= 2:
        p.TalkingText = "\"Thank you for returning my pendant.\""
        return
    StuffDone["5_5"] = 1

def Talking_24_1(p):
    if Party.Gold >= 200:
        boat_ids = ["Boat_0", "Boat_1"]
        boat_sold = False
        for s in boat_ids:
            if Vehicle.List[s].PartyOwns == False:
                Vehicle.List[s].PartyOwns = True
                Party.Gold -= 200
                boat_sold = True
                break
        if boat_sold == False:
            p.TalkingText = "There are no boats left."
        else:
            p.TalkingText = "You pay the rental fee. \"Thank you. The boat is yours for the rest of the season. Be careful out there in the swamps!\""
    else:
        p.TalkingText = "You can\'t afford it."

def Talking_24_7(p):
    if Party.Gold >= 10:
        Party.Gold -= 10
        p.TalkingText = "He serves up some icy cold beer. It is very good. \"If you\'re going up to the swamps, you might want to try snake hunting. A guy named Gustor will pay for every asp fang you bring him.\""
    else:
        p.TalkingText = ""

def Talking_24_9(p):
    if Party.Gold < 25:
        p.TalkingText = "You can\'t afford it."
    else:
        Party.Gold -= 25
        Party.Pos = Location(13, 27)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "You pay up and are led to a comfortable room where you spend the night."
        CentreView(Party.Pos, False)
