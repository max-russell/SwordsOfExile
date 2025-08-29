
def Blinlock_20_MapTrigger_27_17(p):
    if StuffDone["2_1"] == 250:
        return
    StuffDone["2_1"] = 250
    TownMap.List["Blinlock_2"].DeactivateTrigger(Location(27,17))
    TownMap.List["Blinlock_2"].DeactivateTrigger(Location(40,20))
    MessageBox("There must not be very much going on at the mine. The stuff in this storeroom looks like it hasn\'t been used in a while.")

def Blinlock_21_MapTrigger_40_20(p):
    if StuffDone["2_1"] == 250:
        return
    StuffDone["2_1"] = 250
    TownMap.List["Blinlock_2"].DeactivateTrigger(Location(27,17))
    TownMap.List["Blinlock_2"].DeactivateTrigger(Location(40,20))
    MessageBox("You enter the Blinlock Mines for the first time. It\'s unusually cold inside, and you detect the familiar and unwelcoming smell of decay.")

def Blinlock_22_MapTrigger_42_43(p):
    if StuffDone["2_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?", True)
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["2_2"] = 250
    TownMap.List["Blinlock_2"].DeactivateTrigger(Location(42,43))
    pc.RunTrap(eTrapType.RANDOM, 2, 15)

def Blinlock_23_MapTrigger_5_2(p):
    Message("It\'s hot back here!")

def Blinlock_24_OnEntry(p):
    if not Town.Abandoned:
        if StuffDone["2_4"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Skeleton_58": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Zombie_60": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Ghoul_62": Town.NPCList.Remove(npc)
            return

def Blinlock_25_CreatureDeath31(p):
    MessageBox("With a final, confidant blow, you strike down the spirit haunting the mines. With a long, painful keen, it fades away.\n\nThe sinister forces haunting the mine may still return from time to time, but now that the source has been removed, it will be a much more manageable problem.")

def Blinlock_27_TalkingTrigger24(p):
    if StuffDone["2_4"] >= 1:
        p.TalkingText = "\"Typical greedy adventurers!\" He laughs. \"Your reward has already been received!\""
        return
    if StuffDone["2_3"] >= 1:
        if StuffDone["2_4"] == 250:
            return
        StuffDone["2_4"] = 250
        p.TalkingText = "\"Good news at last! You destroyed the evil spirit! As a reward, let me give you a piece of Blinlock\'s fine craftsmanship.\" He has an aide bring you a lovely broadsword.\n\n\"Thank goodness,\" he exclaims. \"At last, some good news in this valley.\""
        Party.GiveNewItem("SteelBroadsword_71")
        return
