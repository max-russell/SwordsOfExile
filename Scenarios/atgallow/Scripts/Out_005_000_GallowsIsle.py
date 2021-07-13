
def GallowsIsle_2379_MapTrigger_21_20(p):
    ChoiceBox("This hill slopes upward until it meets at a peak where a large tower sits. The tower is extremely twisted and bubbling, much like the architecture of Gynai. Several beams of eerie green light radiates from the openings.\n\nYou attempt to approach the tower, but you find yourself blocked by an invisible force. This must be the barrier that you were told about earlier. Needless to say, there is no way you are getting through this.", eDialogPic.TERRAIN, 188, ["OK"])
    p.CancelAction = True

def GallowsIsle_2385_WanderingOnMeet0(p):
    if StuffDone["63_1"] == 250:
        return
    StuffDone["63_1"] = 250
    ChoiceBox("You have never seen Vahnatai before, so you did not know what to expect. They are extremely tall and impossibly thin. Many of them carry unusual wavy swords and circular discs.\n\nIt is too bad that your first encounter could not be a friendly one.", eDialogPic.CREATURE, 77, ["OK"])

def GallowsIsle_2387_WanderingOnMeet2(p):
    p.CancelAction = True
    MessageBox("In the distance you see what appears to be some mobile fungus. As you attempt to approach it, the fungus quickly retreats.")

def GallowsIsle_2388_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
