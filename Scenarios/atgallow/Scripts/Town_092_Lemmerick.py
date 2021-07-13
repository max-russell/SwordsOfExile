
def Lemmerick_2170_MapTrigger_23_5(p):
    ChoiceBox("This is the entrance to the Raymond Naval Base. This is the main hub point for trade between Pralgad and Aizo, the oldest sea trade route in the world. Literally millions of gold in cargo transfer through this post each day.\n\nThe base is limited to strictly Naval personnel. You are part of the army, so you cannot enter.", eDialogPic.STANDARD, 16, ["OK"])
    p.CancelAction = True

def Lemmerick_2173_ExitTown(p):
    if p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(9, 21),WorldMap.SectorAt(Party.OutsidePos))

def Talking_92_1(p):
    if Party.Gold >= 15:
        Party.Gold -= 15
        p.TalkingText = "You pay the gold and are served the drinks. They are quite decent, but not worth the amount you paid for them. Ballimar turns to you, \"Hey, you don\'t look from around here. Want to know some gossip?\""
    else:
        p.TalkingText = "You cannot afford it."

def Talking_92_3(p):
    if Party.Gold < 30:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 30
        Party.Pos = Location(11, 19)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "You pay the gold and are assigned a room. The view is nice, but the quality of the room is not what you would expect. The beds are loud and there is an unpleasant draft. You only manage to get a below average rest."
        CentreView(Party.Pos, False)

def Talking_92_8(p):
    if Party.Gold >= 50:
        Party.Gold -= 50
        p.TalkingText = "You pay up. She smiles. \"As you may know, there has been a rebel group in the area. One of my clients happens to be one of their high up members and he accidentally revealed the location of their secret base.\""
    else:
        p.TalkingText = "You cannot afford it."
