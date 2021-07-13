
def TraderCamp_102_MapTrigger_14_23(p):
    if StuffDone["5_5"] >= StuffDone["5_6"]:
        StuffDone["5_6"] = 10
        MessageBox("You search the chest. It is filled with personal affects. However, a Shimmering Pendant catches your attention. You bet this was the artifact that Challor lost. Nobody is looking so you take it.")
        SpecialItem.Give("ShimmeringPendant")
        return
    MessageBox("This chest is full of garments, bits of bone, a journal, and some other personal affects. None of it is of any use to you.")

def TraderCamp_103_MapTrigger_13_26(p):
    if StuffDone["6_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The floor looks a little suspicious. It is obviously a trap. Do you try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The floor looks a little suspicious. It is obviously a trap. Do you try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["6_3"] = 250
    TownMap.List["TraderCamp_10"].DeactivateTrigger(Location(13,26))
    pc.RunTrap(eTrapType.ALERT, 0, 30)

def TraderCamp_104_OnEntry(p):
    if StuffDone["24_6"] == 1:
        MessageBox("The traders know that you have attacked them. You doubt that they will be friendly to you.")
        Town.MakeTownHostile()
        return

def TraderCamp_105_CreatureDeath0(p):
    MessageBox("You have slain the Trader Captain. You decide to pocket the key around his neck on the chance that it may be useful.")
    SpecialItem.Give("TraderKey")
    if StuffDone["24_6"] == 0:
        StuffDone["24_6"] = 1
        return

def TraderCamp_106_CreatureDeath1(p):
    if StuffDone["24_6"] == 0:
        StuffDone["24_6"] = 1
        return

def Talking_10_6(p):
    if Party.Gold >= 4:
        Party.Gold -= 4
        p.TalkingText = "You are served some fairly refreshing drinks. They are what you might expect from a trader camp, not horrible, but not of high quality."
    else:
        p.TalkingText = "You cannot afford it."

def Talking_10_7(p):
    if Party.Gold < 15:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 15
        Party.Pos = Location(12, 31)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "You pay the gold and are escorted to your room. The quarters are cramped, but better than you would get from sleeping under the stars."
        CentreView(Party.Pos, False)
