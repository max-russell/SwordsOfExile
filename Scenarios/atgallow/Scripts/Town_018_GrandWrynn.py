
def GrandWrynn_352_MapTrigger_37_20(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["24_1"] == 1:
        if StuffDone["34_0"] == 250:
            return
        StuffDone["34_0"] = 250
        ChoiceBox("You enter the mayor\'s office. He stands up and greets you. \"Our scouts have reported that it was you who had ended the Nephilim conflict. Tourists have been scared away by their conflicts. Hopefully, things will return to normal now.\"\n\nYou are brought a large sack of gold coins. \"We are grateful for what you have done here. Our policies forbade us for interfering with the Nephilim. But you, acting alone, have brought an end to their struggle.\n\nWhat the traders did is not new. It had been done before several times by others in Imperial history. More often than not, it is too late before anyone finds out the true cause of such fabricated wars.\n\nHowever, in the end, lives were still lost and our industries have paid dearly. The Empire will seek compensation from the traders in due time. Now take your reward and may the Emperor\'s Wisdom be with you on your adventures!\"", eDialogPic.CREATURE, 37, ["OK"])
        Party.Gold += 500
        return

def GrandWrynn_353_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(32, 35),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(29, 38),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(35, 38),WorldMap.SectorAt(Party.OutsidePos))

def GrandWrynn_354_TalkingTrigger25(p):
    if StuffDone["52_4"] == 1:
        p.TalkingText = "You hand him the manuscript and he looks it over. \"This should not be too difficult. I needed a break from that one anyway. I\'ll get on it right away. This may take some time.\" Two hours pass as he translates it.\n\n\"Here you go. A touching story I must say.\""
        StuffDone["52_4"] = 2
        return

def Talking_18_16(p):
    if Party.Gold >= 7:
        Party.Gold -= 7
        p.TalkingText = "\"Well, we\'ll get those right for you!\" He walks over and pours a round of beers and hands them to you. \"Nice and fresh! Enjoy!\""
    else:
        p.TalkingText = "\"Sorry chaps. I don\'t think the owner would like it much if I gave the beer away for free!\""

def Talking_18_17(p):
    if Party.Gold < 25:
        p.TalkingText = "\"Sorry chaps, I don\'t think the owner would like it much if I let you stay for free!\""
    else:
        Party.Gold -= 25
        Party.Pos = Location(12, 42)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "\"Well now, the rooms already for you. Just head to your south and take the door on your left, can\'t miss it! Have a great night\'s sleep!\""
        CentreView(Party.Pos, False)

def Talking_18_48(p):
    if Party.Gold >= 4:
        Party.Gold -= 4
        p.TalkingText = "She serves up some drinks. They are not that great, but she leans over to ask you. \"Ever heard of the Traders?\""
    else:
        p.TalkingText = "\"Hey, I even gave you the Nephilim rate! You don\'t want to know what the human rate is.\""

def Talking_18_58(p):
    if Party.Gold >= 4:
        Party.Gold -= 4
        p.TalkingText = "She pours you a round of drinks. They are quite refreshing."
    else:
        p.TalkingText = "You don\'t have the gold!"
