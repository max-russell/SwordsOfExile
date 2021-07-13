
def Sirius_2130_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(17, 13),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(16, 14),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(17, 14),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(17, 13),WorldMap.SectorAt(Party.OutsidePos))

def Talking_90_7(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "You pay the gold and are poured some milk. It is cool, but not as fresh as you would like. At least it is not like some of the sour stuff you had to drink back in training."
    else:
        p.TalkingText = "You cannot afford it."

def Talking_90_10(p):
    if Party.Gold < 25:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 25
        Party.Pos = Location(36, 16)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "\"Only the standard room tonight? Well, come with me!\" He leads you to your room. It is kind of cramped and you do not exactly get the best rest in the world. Oh well, buy cheap, get cheap."
        CentreView(Party.Pos, False)

def Talking_90_11(p):
    if Party.Gold < 45:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 45
        Party.Pos = Location(42, 16)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "\"Ah feeling rich tonight are we? Come with me!\" He leads you to your room. You find the accommodations to be quite comfortable and you have a superb rest."
        CentreView(Party.Pos, False)
