
def BrightHope_2129_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(36, 7),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(36, 7),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(37, 8),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(37, 7),WorldMap.SectorAt(Party.OutsidePos))

def Talking_89_2(p):
    if Party.Gold >= 75:
        Party.Gold -= 75
        p.TalkingText = "\"I can see that you have great potential in you. If you push it to its fullest, you will achieve heroic fame. However, I can also see the dye has already been cast and true success is unattainable. I can tell no more.\""
    else:
        p.TalkingText = "\"But I must make a living as well.\""

def Talking_89_25(p):
    if Party.Gold >= 4:
        Party.Gold -= 4
        p.TalkingText = "You pay the gold and are poured a round of milk. \"Fresh from the cows this morning. Enjoy!\" The drink is cool and refreshing. You wonder why they do not have the usual alcohol around here."
    else:
        p.TalkingText = "You cannot afford it."

def Talking_89_27(p):
    if Party.Gold < 35:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 35
        Party.Pos = Location(40, 16)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "You pay the gold and are led to your room. \"Have a wonderful rest soldiers!\" You get a fairly comfortable sleep with no distractions."
        CentreView(Party.Pos, False)
