
def Garnet_2126_MapTrigger_11_13(p):
    if SpecialItem.PartyHas("SackofMessages_32"):
        SpecialItem.Take("SackofMessages_32")
        Animation_Hold(-1, 015_cash)
        Wait()
        MessageBox("You deliver your sack of messages from Rune to the delivery service here. You are paid the promised amount of 200 gold.")
        Party.Gold += 200
        return

def Garnet_2127_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(10, 13),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(10, 13),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(10, 14),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(11, 14),WorldMap.SectorAt(Party.OutsidePos))

def Garnet_2128_TalkingTrigger35(p):
    if SpecialItem.PartyHas("SackofMessages"):
        return
    p.TalkingText = "You are handed a large sack containing several letters and light weight packages. \"Here you are. Please deliver this to Rune as soon as possible.\""
    SpecialItem.Give("SackofMessages")

def Talking_87_9(p):
    if Party.Gold >= 6:
        Party.Gold -= 6
        p.TalkingText = "She pours you a round of beers. \"Like, here you go!\" The beer is all right as far as beers go. It is about average in quality."
    else:
        p.TalkingText = "\"Like you can\'t afford it.\""

def Talking_87_10(p):
    if Party.Gold < 25:
        p.TalkingText = "\"Like, you can\'t afford it!\""
    else:
        Party.Gold -= 25
        Party.Pos = Location(40, 25)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "You pay her the gold. \"Your rooms, like over there.\" You head off to your room and have a good rest."
        CentreView(Party.Pos, False)
