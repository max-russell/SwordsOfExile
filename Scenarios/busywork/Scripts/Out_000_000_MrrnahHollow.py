
def MrrnahHollow_51_MapTrigger_15_30(p):
    MessageBox("A band of maybe 10 to 12 people was camped here recently. There\'s plenty of tracks, horse droppings, and gnawed chicken bones. No sign, however, of who they were or where they went.")

def MrrnahHollow_52_MapTrigger_18_9(p):
    if StuffDone["202_0"] == 250:
        return
    StuffDone["202_0"] = 250
    WorldMap.DeactivateTrigger(Location(18,9))
    MessageBox("Threading your way through this tangled maze of trees, you suddenly come face to face with several other hikers. Startled, they attack you. They must be brigands!")
    WorldMap.SpawnEncounter("Group_0_0_4", p.Target)

def MrrnahHollow_53_MapTrigger_34_11(p):
    if StuffDone["202_1"] == 250:
        return
    result = ChoiceBox("In the marsh by the lake, you find a small patch of comfrey root. What a lucky find!", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["202_1"] = 250
        WorldMap.DeactivateTrigger(Location(34,11))
        Party.GiveNewItem("ComfreyRoot_364")
    return

def MrrnahHollow_54_MapTrigger_25_28(p):
    if StuffDone["202_2"] == 250:
        return
    result = ChoiceBox("Somebody left a bottle at the base of one of these trees. It\'s been here for a while - the label is weather-worn and nearly peeled off. Intriguingly, the bottle still contains two inches of gray fluid.", eDialogPic.TERRAIN, 80, ["Take", "Leave"])
    if result == 0:
        StuffDone["202_2"] = 250
        WorldMap.AlterTerrain(Location(25,28), 1, None)
        WorldMap.DeactivateTrigger(Location(25,28))
        Party.GiveNewItem("HrrasJuice_383")
    return

def MrrnahHollow_55_SpecialOnWin0(p):
    MessageBox("You find a pouch of gold and a bottle of Hrras Juice on one of the bodies. What you don\'t find, unsurprisingly, is any sign of where the bandits are hiding out.")
    Party.GiveNewItem("HrrasJuice_383")
    Party.Gold += 50
