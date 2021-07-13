
def WarriorsGrove_0_MapTrigger_10_10(p):
    if StuffDone["0_0"] == 250:
        return
    StuffDone["0_0"] = 250
    TownMap.List["WarriorsGrove_0"].DeactivateTrigger(Location(10,10))
    MessageBox("You find a narrow, concealed walkway between two buildings. Webs hang frome ceiling, and the bones of unfortunate rats crunch underfoot.")

def WarriorsGrove_1_MapTrigger_28_22(p):
    result = ChoiceBox("Do you wish to leave the scenario now?", eDialogPic.STANDARD, 16, ["No", "Yes"])
    if result == 0:
        return
    elif result == 1:
        Scenario.End()
        return

def Talking_0_22(p):
    if Party.Gold < 5:
        p.TalkingText = "She shakes her head. \"Sorry, but that\'s 5 gold.\""
    else:
        Party.Gold -= 5
        Party.Pos = Location(31, 38)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "She shows you to your room, and wishes you a pleasant night."
        CentreView(Party.Pos, False)

def Talking_0_24(p):
    if Party.Gold >= 1:
        Party.Gold -= 1
        p.TalkingText = "She serves up the beer. It\'s refreshing, in a nasty sort of way."
    else:
        p.TalkingText = "She looks pityingly upon you. \"Not a gold piece to your name. How sad.\""
