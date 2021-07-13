
def Damasnica_1513_MapTrigger_10_39(p):
    if StuffDone["39_1"] < 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("There is an invisible forcefield here holding you back. You will not be able to enter this storeroom this way.")
        return

def Damasnica_1515_MapTrigger_17_7(p):
    ChoiceBox("The guards checks for a pass. Unfortunately, you do not have one so he does not let you pass.\n\n\"Sorry guys. The law specifically states that I can only let people in here with a specific pass. It\'s for safety reasons, you understand.\"", eDialogPic.CREATURE, 12, ["OK"])
    p.CancelAction = True

def Damasnica_1527_MapTrigger_35_43(p):
    if StuffDone["100_0"] >= 6:
        Town.PlaceEncounterGroup(1)
        return

def Damasnica_1529_OnEntry(p):
    if StuffDone["41_1"] == 250:
        return
    StuffDone["41_1"] = 250
    ChoiceBox("You arrive at the city of Damasnica, capital of the Mandahl Sector. The first thing you notice is the lack of noise typical of cities of this size. Normally such places are very loud, but the place is dead quiet.\n\nA few townspeople and soldiers wander by, not paying much attention to you. It is immediately apparent that something is severely wrong with them. Their skin is extremely pale and they have far off looks in their eyes.\n\nThey all look very weak and tired. You have heard whispers that there was some sickness up here, but you did not realize that it was like this. You hope you do not come down with the same condition as well.", eDialogPic.TERRAIN, 93, ["OK"])

def Damasnica_1530_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(22, 24),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 32),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(30, 30),WorldMap.SectorAt(Party.OutsidePos))

def Damasnica_1531_TalkingTrigger2(p):
    if StuffDone["39_1"] >= 2:
        return
    if StuffDone["39_1"] < 1:
        p.TalkingText = "\"As you\'ve probably noticed, everyone in this city has some kind of energy-sucking illness. Our healers are being pushed to the limit, but it keeps on occurring. Our mages are also stumped as to its cause.\n\nHowever, they suspect the plague has some arcane roots. If you could solve the curse, you would be paid well.\""
        return
    p.TalkingText = "You return with the story of your adventure at the Cursed Mine. \"Ingenious! Even one vindictive mage can trouble many. Are any of us truly safe? Hopefully now the problem will clear up.\" He thinks.\n\n\"Your reward is in the storeroom just north of here. It contains items found by our miners that are of no use to us. You may have them as payment.\""
    StuffDone["39_1"] = 2

def Talking_61_7(p):
    if Party.Gold >= 9:
        Party.Gold -= 9
        p.TalkingText = "He hands you a round of drinks. \"Enjoy! Hey, see that guy in the corner. I wouldn\'t get him started on his stories if I were you. He\'ll never shut up!\""
    else:
        p.TalkingText = "You can\'t afford it."

def Talking_61_8(p):
    if Party.Gold < 20:
        p.TalkingText = "You can\'t afford it."
    else:
        Party.Gold -= 20
        Party.Pos = Location(32, 37)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "You are shown a nice room. A bit cramped, but you have a nice sleep. You awaken refreshed.\""
        CentreView(Party.Pos, False)

def Talking_61_16(p):
    if Party.Gold >= 0:
        if TownMap.List["Vega_3"].Hidden == True:
            Party.Gold -= 0
            TownMap.List["Vega_3"].Hidden = False
        p.TalkingText = "\"It\'s in the mountains north of the city. You\'ll have to climb over some to get there, out of the way you know. Wouldn\'t go there if I were you. I\'ve seen far too many disasters there.\""
    else:
        p.TalkingText = ""
