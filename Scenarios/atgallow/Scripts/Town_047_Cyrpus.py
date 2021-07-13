
def Cyrpus_1087_MapTrigger_32_52(p):
    if StuffDone["24_6"] == 1:
        if StuffDone["24_7"] == 250:
            return
        StuffDone["24_7"] = 250
        MessageBox("Well some traders have decided to welcome you. As you approach, they raise their weapons. The captain in the back orders them to attack!")
        Town.PlaceEncounterGroup(1)
        Town.MakeTownHostile()
        return

def Cyrpus_1090_MapTrigger_10_18(p):
    if StuffDone["24_6"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        MessageBox("You have stumbled into the dining hall of the Nephil traders. A full meal is currently in progress. The guards are immediately called and you are quickly escorted out. It appears that you will not get in that way now.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(35,30))
        p.CancelAction = True
        return
    if StuffDone["24_8"] == 250:
        return
    StuffDone["24_8"] = 250
    MessageBox("Apparently the traders were not expecting you to sneak in through the storerooms. The forces are probably concentrated around the front gate. You encounter a nearly empty dining hall. You will have to move quickly.")

def Cyrpus_1092_MapTrigger_37_5(p):
    if StuffDone["24_9"] == 0:
        MessageBox("A quick search of this cluttered desk uncovers a small note. \"Mithral Maiden Chest Combination: 46-32-19-84-03\" It sounds useful so you pocket it. Unfortunately, it appears you have company.")
        StuffDone["24_9"] = 1
        Town.PlaceEncounterGroup(2)
        return

def Cyrpus_1093_MapTrigger_52_24(p):
    if StuffDone["25_0"] == 250:
        return
    StuffDone["25_0"] = 250
    TownMap.List["Cyrpus_47"].DeactivateTrigger(Location(52,24))
    TownMap.List["Cyrpus_47"].DeactivateTrigger(Location(52,25))
    TownMap.List["Cyrpus_47"].DeactivateTrigger(Location(52,26))
    Town.PlaceEncounterGroup(3)

def Cyrpus_1096_MapTrigger_58_15(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(58,14)).Num == 128:
        if StuffDone["25_1"] == 1:
            MessageBox("This door has a complex lock built into it. There is no way you will be able to bash or pick it. However, you try the key you found in the trader camp and it works! The door clicks open.")
            t = Town.TerrainAt(Location(58,14))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(58,14)).TransformTo
                Town.AlterTerrain(Location(58,14), 0, t)
            return
        MessageBox("This door has a complex lock built into it. There is no way you will be able to bash or pick it open. Sadly, you do not have the correct key either.")
        return

def Cyrpus_1097_MapTrigger_57_13(p):
    if StuffDone["25_2"] == 250:
        return
    StuffDone["25_2"] = 250
    TownMap.List["Cyrpus_47"].DeactivateTrigger(Location(57,13))
    TownMap.List["Cyrpus_47"].DeactivateTrigger(Location(58,13))
    TownMap.List["Cyrpus_47"].DeactivateTrigger(Location(59,13))
    MessageBox("You enter what appears to be the room where the traders keep their goods. At the other end, several traders have amassed to guard their hard-earned goodies.")
    Town.PlaceEncounterGroup(4)

def Cyrpus_1100_MapTrigger_36_7(p):
    if StuffDone["24_9"] == 1:
        MessageBox("This chest has a combination lock attached to it. You decide to try the combination you learned in the desk. Sadly, it does not work. That combination must be for another chest.")
        return
    MessageBox("This chest has a combination lock built into it. You will not be able to open it until you know the proper combination. Sadly, you have not even an inkling of what to try.")

def Cyrpus_1104_MapTrigger_59_3(p):
    if StuffDone["24_9"] == 1:
        if StuffDone["24_4"] == 0:
            MessageBox("This chest has a combination lock built into it. You decide to try the combination you learned earlier from the desk. It works! The chest pops open revealing your reward.\n\nSadly the chest is totally devoid of treasure except for a finely carved metallic Nephilim Female figure. This must be the Mithral Maiden that was stolen earlier. Now you have proof the traders are really responsible for this war.")
            StuffDone["24_4"] = 1
            SpecialItem.Give("MithralMaiden")
            return
        return
    MessageBox("This chest has a combination lock built into it. You will not be able to open it until you know the proper combination. Sadly, you have not even an inkling of what to try.")

def Cyrpus_1105_MapTrigger_28_27(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        t = Town.TerrainAt(Location(34,28)).TransformTo
        Town.AlterTerrain(Location(34,28), 0, t)
        MessageBox("You pull the lever and you hear machinery at work.")
        t = Town.TerrainAt(Location(35,28)).TransformTo
        Town.AlterTerrain(Location(35,28), 0, t)
        return

def Cyrpus_1106_OnEntry(p):
    if StuffDone["24_6"] == 1:
        MessageBox("The trader fortress of Cyrpus is just ahead. Things are quiet; quiet enough to make you suspicious. You can bet they know you\'re here and that you have attacked them. You can also bet they are not going to welcome you either.")
        Town.MakeTownHostile()
        return

def Cyrpus_1107_CreatureDeath0(p):
    if StuffDone["24_6"] == 0:
        MessageBox("You have struck down a Nephil Trader without any provocation. The guards have been called and have arrived just in time to surround you. It is not long before you are all killed.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def Talking_47_3(p):
    if Party.Gold < 40:
        p.TalkingText = "He smiles upon seeing you having not enough. \"Oh well, looks like you won\'t be staying here tonight. Too bad...\""
    else:
        Party.Gold -= 40
        Party.Pos = Location(3, 54)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "Even though you paid the highly inflated price, he still seems angry that he has to house Empire soldiers. \"Rooms over there. I trust you won\'t be needing anything else, right?\" You go to your rooms and have an average slumber."
        CentreView(Party.Pos, False)
