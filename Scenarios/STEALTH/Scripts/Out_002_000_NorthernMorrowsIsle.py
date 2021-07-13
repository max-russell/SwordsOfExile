
def NorthernMorrowsIsle_368_MapTrigger_30_19(p):
    result = ChoiceBox("A group of seedy types have set up a small fort here, in order to do things of questionable legality. Adventurers are always welcome. They gladly welcome you in.\n\nThere\'s all manner of brigands and rebels inside, drinking and bartering under a temporary truce. Other people are running a small bazaar of goods with a variety of origins. Do you shop?", eDialogPic.TERRAIN, 190, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_1_2_0")
        p.CancelAction = True
        return
    if StuffDone["202_0"] == 250:
        return
    StuffDone["202_0"] = 250
    WorldMap.DeactivateTrigger(Location(118,17))
    WorldMap.DeactivateTrigger(Location(118,19))
    WorldMap.DeactivateTrigger(Location(118,18))
    MessageBox("You depart the bazaar. It doesn\'t appear your departure went unnoticed. A band of brigands watches you carefully as you go.")

def NorthernMorrowsIsle_369_MapTrigger_22_17(p):
    if StuffDone["202_0"] >= 1:
        if StuffDone["202_1"] == 250:
            return
        StuffDone["202_1"] = 250
        MessageBox("The brigands who watched you when you left the bazaar apparently decided that you looked like an easy target. They have set up an ambush for you here. They dispense with the tiresome demands for you to give up all your goods, and attack immediately.")
        WorldMap.SpawnEncounter("Group_2_0_4", p.Target)
        return

def NorthernMorrowsIsle_372_MapTrigger_31_41(p):
    if StuffDone["101_5"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You are surprised to find what looks like a platoon of Empire soldiers here, guarding a gate. Looking closer, you see that some are Empire defectors, and others are rebels in stolen Empire armor (with insignia removed).\n\nUnfortunately, when you reach the gate, the guards tell you that you aren\'t allowed to pass. You have to turn back.")
        return

def NorthernMorrowsIsle_373_MapTrigger_30_39(p):
    if StuffDone["202_3"] == 250:
        return
    StuffDone["202_3"] = 250
    WorldMap.DeactivateTrigger(Location(126,39))
    WorldMap.DeactivateTrigger(Location(127,39))
    WorldMap.DeactivateTrigger(Location(128,39))
    WorldMap.DeactivateTrigger(Location(142,28))
    WorldMap.DeactivateTrigger(Location(141,28))
    ChoiceBox("You reach a valley high up in the mountains of Morrow\'s Isle. The miners that have been burrowing through these mountains haven\'t quite reached here yet. They\'re still working on other areas.\n\nThe valley is quite nice and peaceful. Alpine evergreens grow all around, and bits of snow are visible here and there. No brigands. No signs of battles. It\'s a nice change of pace.", eDialogPic.TERRAIN, 19, ["OK"])

def NorthernMorrowsIsle_378_MapTrigger_7_33(p):
    MessageBox("The road ends abruptly here, the ambitious Empire construction halted by the beginning of the war with the Hill Runners.")
