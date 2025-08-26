
def SouthwesternVale_399_MapTrigger_7_44(p):
    MessageBox("Sorry, no Easter Eggs in this game.")

def SouthwesternVale_400_MapTrigger_42_41(p):
    if StuffDone["203_0"] == 250:
        return
    StuffDone["203_0"] = 250
    WorldMap.DeactivateTrigger(Location(42,89))
    WorldMap.DeactivateTrigger(Location(42,88))
    WorldMap.DeactivateTrigger(Location(42,87))
    MessageBox("Oh dear. Now that the curse has decimated the Vale\'s animal population, the creatures higher up on the food chain seem to have decided to hunt other prey.\n\nYou encounter a group of bears. Hunger has made them desperate, and desperation has made them hunt something they normally wouldn\'t: you.")
    WorldMap.SpawnEncounter("Group_0_1_4", p.Target)

def SouthwesternVale_403_MapTrigger_29_36(p):
    if StuffDone["203_1"] == 250:
        return
    StuffDone["203_1"] = 250
    WorldMap.DeactivateTrigger(Location(29,84))
    WorldMap.DeactivateTrigger(Location(22,76))
    MessageBox("You reach a smaller, higher valley, only reachable from inside the Vale. You immediately notice a huge difference between this valley and the Vale: the curse seems to have passed this valley over.\n\nYou see a small lake, surrounded by happy animals and healthy plants. The air is clean and fresh, with no constant scent of decay. It\'s a nice change of pace.")

def SouthwesternVale_405_MapTrigger_41_8(p):
    if StuffDone["203_2"] == 250:
        return
    result = ChoiceBox("Your long march through the marsh has been rewarded. Mixed in among the reeds and cattails, you find several sprigs of fresh comfrey root, ready for picking.", eDialogPic.TERRAIN, 78, ["Take", "Leave"])
    if result == 0:
        StuffDone["203_2"] = 250
        WorldMap.DeactivateTrigger(Location(41,56))
        Party.GiveNewItem("ComfreyRoot_364")
    return

def SouthwesternVale_406_MapTrigger_10_6(p):
    if StuffDone["203_3"] == 250:
        return
    StuffDone["203_3"] = 250
    WorldMap.DeactivateTrigger(Location(10,54))
    MessageBox("There is a dramatic increase in the number of burned and gnawed bones on either side of the trail. This is rarely good news.")

def SouthwesternVale_407_MapTrigger_6_7(p):
    if StuffDone["203_4"] == 250:
        return
    StuffDone["203_4"] = 250
    WorldMap.DeactivateTrigger(Location(6,55))
    MessageBox("You were trying to advance up the valley carefully, in order to not give advance warning to any evil creatures residing here. It didn\'t work. Your scent was detected by hosts of reptilian heads.\n\nYou run, but not fast enough. The hydras are almost immediately upon you.")
    WorldMap.SpawnEncounter("Group_0_1_5", p.Target)

def SouthwesternVale_408_SpecialOnWin0(p):
    ChoiceBox("The monsters are dead. And, of course, where there are monsters, there is loot as well. It doesn\'t take long to find the bear\'s lair. You search inside.\n\nIt\'s pretty disturbing ... there\'s no shortage of dead travelers and broken weapons. The only thing you find worth saving is an old, rusty breastplate. You take it with you - it might be worth something.", eDialogPic.CREATURE2x1, 0, ["OK"])
    Party.GiveNewItem("IronBreastplate_128")

def SouthwesternVale_409_SpecialOnWin1(p):
    MessageBox("Fortunately, victory is yours. Unfortunately, the hydras were poor in everything but bones. You leave without any loot.")
