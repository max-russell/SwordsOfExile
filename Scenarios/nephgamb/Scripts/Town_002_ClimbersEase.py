
def ClimbersEase_45_MapTrigger_11_16(p):
    if StuffDone["2_1"] >= 1:
        return
    result = ChoiceBox("The door in the end of the corridor shows signs of battering. Someone has tried to force it. The door is still locked, however. There is no visible keyhole, so if you want to enter, you must try your own muscles.", eDialogPic.TERRAIN, 90, ["Leave", "Push"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        pc.Damage()
        Wait()
        StuffDone["2_0"] += 1
        if StuffDone["2_0"] == 250:
            pass
        if StuffDone["2_0"] >= 3:
            result = ChoiceBox("Flustered, you fall back from your attempts to force the door, discussing what to try next. Upon hearing your human voices, a small voice calls: \"Who?s there?\"", eDialogPic.TERRAIN, 90, ["Leave", "Answer"])
            if result == 1:
                MessageBox("You reassure the voice, saying you are Exile soldiers, come to investigate the raid. The answer is a soft cry of relief and the sound of a bolt sliding away.")
                Town.AlterTerrain(Location(10,15), 0, TerrainRecord.UnderlayList[129])
                StuffDone["2_1"] = 1
                return
            return
        RunScript("ClimbersEase_45_MapTrigger_11_16", p)
        return

def ClimbersEase_47_OnEntry(p):
    if not Town.Abandoned:
        MessageBox("The Climber?s Ease has a good reputation among travellers on the Brattaskar Road. The innkeeper is friendly and is well informed of the conditions of the road.\n\n")
