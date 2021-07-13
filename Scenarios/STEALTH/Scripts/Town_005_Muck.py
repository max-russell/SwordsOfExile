
def Muck_51_MapTrigger_41_35(p):
    if StuffDone["5_0"] == 250:
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
    StuffDone["5_0"] = 250
    TownMap.List["Muck_5"].DeactivateTrigger(Location(41,35))
    pc.RunTrap(eTrapType.RANDOM, 2, 25)

def Muck_52_MapTrigger_38_34(p):
    if StuffDone["5_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The floor stones in the doorway look a little bit loose. Could be shoddy construction. It could also be a trap.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The floor stones in the doorway look a little bit loose. Could be shoddy construction. It could also be a trap.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["5_1"] = 250
    TownMap.List["Muck_5"].DeactivateTrigger(Location(38,34))
    pc.RunTrap(eTrapType.ALERT, 0, 30)

def Muck_53_MapTrigger_25_16(p):
    if StuffDone["5_2"] == 250:
        return
    StuffDone["5_2"] = 250
    TownMap.List["Muck_5"].DeactivateTrigger(Location(25,16))
    TownMap.List["Muck_5"].DeactivateTrigger(Location(25,9))
    MessageBox("The smell of freshly cut and cleaned herbs is overpowering in here. Alchemical ingredients freshly recovered from the swamp are brought here to be sorted, treated, and packaged for sale to alchemists.\n\nTired, pale serfs with stone knives are processing the herbs at a hectic pace. They\'re working as fast as they can, as if they were afraid of being punished for slow performance. They probably would be.")

def Muck_55_OnEntry(p):
    if StuffDone["101_1"] >= 1:
        MessageBox("The word of your notoriety has reached this remote town. The guards draw their weapons, and move to intercept you.")
        Town.MakeTownHostile()
        return
    if StuffDone["5_3"] == 250:
        return
    StuffDone["5_3"] = 250
    MessageBox("You reach the aptly named town of Muck, a sickly village on the border of the massive, foul Morrow Marsh. Muck\'s main business is farming alchemical ingredients, which tend to grow in large swamps.\n\nIt\'s lucrative work, but dangerous, dirty, exhausting, and disease ridden. Not surprisingly, the serfs are tired, thin, and dangerously pale.")

def Muck_56_TalkingTrigger11(p):
    if StuffDone["1_1"] >= 1:
        p.TalkingText = "\"You need to get a box in Selathni, and deliver it to the city of Zaskiva. To get the box, go to Elinor in Selathni, and say \'sainthood.\' Then go to Zaskiva.\"\n\n\"Zaskiva is restricted, but we\'ll see that you can get there. Once there, search the city for a marble statue. Put the box in the niche in the wall behind the statue.\" He gives you a paper reviewing this."
        StuffDone["100_8"] = 1
        SpecialItem.Give("BoxMissionScroll")
        return
