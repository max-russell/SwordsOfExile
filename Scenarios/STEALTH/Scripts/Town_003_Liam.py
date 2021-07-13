
def Liam_30_MapTrigger_12_28(p):
    if StuffDone["3_1"] == 250:
        return
    StuffDone["3_1"] = 250
    TownMap.List["Liam_3"].DeactivateTrigger(Location(12,28))
    TownMap.List["Liam_3"].DeactivateTrigger(Location(12,19))
    MessageBox("Feudal states are rare in the Empire these days, and serfs\' barracks are an uncommon sight. This low, cramped chamber would be quite a historical novelty, were it not for the fact that it\'s right here in front of you and clearly still in use.\n\nNormally, serfs have barracks instead of hovels only in very recently settled and poor areas. Morrow\'s Isle, however, is quite well off. Very odd.")

def Liam_32_MapTrigger_7_22(p):
    if StuffDone["3_2"] == 250:
        return
    StuffDone["3_2"] = 250
    TownMap.List["Liam_3"].DeactivateTrigger(Location(7,22))
    MessageBox("You\'ve stumbled upon a hidden weapon storeroom. It looks like some of the rebels have cached blades here, in preparation for something unpleasant.")

def Liam_33_MapTrigger_6_21(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(7,22)).Num == 128:
        if SpecialItem.PartyHas("BrassKey"):
            MessageBox("You try the door just ahead. It\'s quite locked. Fortunately, the brass key you found fits nicely. The door is now unlocked.")
            Town.AlterTerrain(Location(7,22), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("The door ahead has a massive padlock on it, and is heavy and iron bound as well. It\'ll be tricky to get through.")
        return

def Liam_35_MapTrigger_8_41(p):
    if StuffDone["3_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["3_3"] = 250
    TownMap.List["Liam_3"].DeactivateTrigger(Location(8,41))
    pc.RunTrap(eTrapType.GAS, 2, 30)

def Liam_36_MapTrigger_15_41(p):
    if StuffDone["3_4"] == 250:
        return
    StuffDone["3_4"] = 250
    TownMap.List["Liam_3"].DeactivateTrigger(Location(15,41))
    MessageBox("At first, it looks like this chest only contains robes and old linens. Being suspicious types, you search it carefully. Sure enough, you find a brass key hidden at the bottom!")
    SpecialItem.Give("BrassKey")

def Liam_37_MapTrigger_41_24(p):
    if StuffDone["3_6"] == 250:
        return
    StuffDone["3_6"] = 250
    TownMap.List["Liam_3"].DeactivateTrigger(Location(41,24))
    MessageBox("The sign by the door said \"Punishment Cells.\" The cells are quiet now, but there is a strange, sour smell in the air. People have been kept here recently.")

def Liam_38_MapTrigger_34_27(p):
    if Party.Day >= 40:
        if StuffDone["3_6"] == 250:
            return
        StuffDone["3_6"] = 250
        TownMap.List["Liam_3"].DeactivateTrigger(Location(41,24))
        MessageBox("The city hall is empty. The throne and floor are splattered with blood stains.")
        return

def Liam_39_MapTrigger_15_33(p):
    if StuffDone["3_0"] >= 1:
        MessageBox("There is a note on the door. It says \"Temporarily closed. Will be back soon.\"")
        return

def Liam_40_OnEntry(p):
    if StuffDone["101_1"] >= 1:
        MessageBox("Word of your notorious deeds has reached the town of Liam. The guards call out an alarm ...")
        Town.MakeTownHostile()
        if Party.Day >= 40:
            if Maths.Rand(1,0,100) <= 100:
                Town.PlaceField(Location(40,27), Field.LARGE_BLOOD)
            return
        return
    if Party.Day >= 40:
        if Maths.Rand(1,0,100) <= 100:
            Town.PlaceField(Location(40,27), Field.LARGE_BLOOD)
        return

def Liam_41_TalkingTrigger14(p):
    if StuffDone["100_4"] >= 1:
        if StuffDone["1_1"] >= 1:
            StuffDone["3_0"] = 1
            StuffDone["100_6"] = 1
            SpecialItem.Give("OGradyScroll")
            return
        p.TalkingText = "\"Your mission is the same. Consult the note I gave you to review.\" (Click on the Spec button on the inventory screen to see the note.)"
        return
    p.TalkingText = "\"In the mountains to the northwest of the city of Selathni, there\'s an abandoned Empire fort. When the fort was abandoned, certain valuable papers were left behind.\"\n\n\"Go there, find those papers, and put them in the large crack of the floor in the southwest storage shed in Selathni. Then return to me.\" He gives you a piece of paper describing the mission."
    TownMap.List["AbandonedFort_7"].Hidden = False
    SpecialItem.Give("PapersMissionScroll")
    StuffDone["100_4"] = 1

def Liam_42_TalkingTrigger23(p):
    count = Party.CountItemClass(1, True)
    Party.Gold += count * 50
    p.TalkingText = "She takes the geodes, and pays you for them. \"Thank you! This will be a great help in my research.\""

def Talking_3_19(p):
    if Party.Day <= 40:
        p.TalkingText = "\"You won\'t have to talk to many people to find out what a torn, violent place this has become. Granted, there is great injustice, but things are only being made worse.\""
    else:
        p.TalkingText = "He looks upset. \"Our Lord, Houlihan, was murdered! We are even striking down our leaders now! I can hardly stand to talk about it. This bitter discord seems to be beyond the control of all powers.\""

def Talking_3_24(p):
    if Party.Day <= 40:
        p.TalkingText = "\"Yes. I\'ve been trying to watch it with an impartial eye. You see, it has to do with the serfs on the isle, and their receiving of land.\""
    else:
        p.TalkingText = "\"Yes. I\'ve been trying to watch it with an impartial eye, but it was difficult after the assassination. You see, it has to do with the serfs on the isle, and their receiving of land.\""
