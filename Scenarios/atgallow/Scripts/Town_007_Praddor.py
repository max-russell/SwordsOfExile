
def Praddor_78_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(24, 32),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(24, 33),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(25, 33),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(25, 33),WorldMap.SectorAt(Party.OutsidePos))

def Praddor_79_TalkingTrigger4(p):
    if StuffDone["41_0"] >= 2:
        if StuffDone["41_0"] < 3:
            StuffDone["41_0"] = 3
            p.TalkingText = "You return with the scroll. \"Thank you! I do hope this works. I want nothing more than to see Mickie healthy again! Oh, I guess I can teach you a spell for your efforts.\" He instructs you how to cast \'Wall of Ice\'!"
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_wall_of_ice")
            return
        return
    if StuffDone["41_0"] < 1:
        p.TalkingText = "\"I don\'t know what to do, but I\'m sure he might. I believe his name was Nyrad or something. If you see him give him this.\" He hands you information on his lizard and its disease."
        StuffDone["41_0"] = 1
        return
    p.TalkingText = "\"If anyone would have a treatment it would be him. I believe his name is Nyrad and he lives somewhere out in the Mandahl Sector to the west. I really don\'t know much else. I\'ll be glad for any help I can get!\""

def Talking_7_28(p):
    if Party.Gold >= 3:
        Party.Gold -= 3
        p.TalkingText = "She brusquely hands you a round of drinks. As far as beer goes, you\'ve had better, but you\'ve had a lot worse."
    else:
        p.TalkingText = "\"Gee. They sure don\'t pay soldiers very well!\""

def Talking_7_29(p):
    if Party.Gold < 16:
        p.TalkingText = "\"Go back to the barracks, if you can\'t afford lodging. I\'m sure you can find a bed there!\""
    else:
        Party.Gold -= 16
        Party.Pos = Location(31, 33)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "You pay her the gold. \"You\'re rooms ready for you. I trust you can find it, or do I need to hold your hands?\" You find your rooms. They\'re a bit cramped, but you\'ve slept in worse conditions."
        CentreView(Party.Pos, False)

def Talking_7_32(p):
    if Party.Gold >= 100:
        boat_ids = ["Boat_4"]
        boat_sold = False
        for s in boat_ids:
            if Vehicle.List[s].PartyOwns == False:
                Vehicle.List[s].PartyOwns = True
                Party.Gold -= 100
                boat_sold = True
                break
        if boat_sold == False:
            p.TalkingText = "There are no boats left."
        else:
            p.TalkingText = "He takes your gold and hands you a receipt. \"You\'re in luck. That\'s the last one I have. I\'m building another which should be complete in a couple weeks.\""
    else:
        p.TalkingText = "\"Sorry guys, but I have to turn a profit. 100 gold, take it or leave it!\""
