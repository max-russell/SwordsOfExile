
def ZaKhaziRunSouth_666_MapTrigger_41_37(p):
    if StuffDone["213_0"] == 250:
        return
    result = ChoiceBox("You see dim, flickering light coming from the cave ahead, and smell a little bit of smoke. The sound of someone or something talking echoes down the corridor.\n\nYou can keep going, but whoever\'s there might not be happy to see you.", eDialogPic.STANDARD, 8, ["Leave", "Approach"])
    if result == 1:
        StuffDone["213_0"] = 250
        WorldMap.DeactivateTrigger(Location(41,661))
        MessageBox("You move carefully into the cavern, round a corner, and come face to face with a slith guard. It shouts an alarm, and in a moment the sliths in the cavern ahead pour out and attack you.")
        WorldMap.SpawnEncounter("Group_0_13_4", p.Target)
        return
    p.CancelAction = True

def ZaKhaziRunSouth_667_MapTrigger_40_44(p):
    if StuffDone["213_1"] == 250:
        return
    result = ChoiceBox("The slith patrol you encountered had recently created a supply cache here. There\'s a bundle of dried fish, and a nice slith spear as well.", eDialogPic.TERRAIN, 178, ["Take", "Leave"])
    if result == 0:
        StuffDone["213_1"] = 250
        WorldMap.AlterTerrain(Location(40,668), 1, None)
        WorldMap.DeactivateTrigger(Location(40,668))
        Party.GiveNewItem("SteelSlithSpear_91")
        Party.Food += 150
    return

def ZaKhaziRunSouth_668_MapTrigger_19_20(p):
    if StuffDone["213_2"] == 250:
        return
    result = ChoiceBox("You\'ve managed to sneak up on a circle of gremlins, dancing around, drinking wine, and carrying on. You notice they\'re dancing around a huge hydra, which they\'ve tied down with large ropes. It must be dinner.\n\nYou could probably attack them with surprise, if you wanted.", eDialogPic.CREATURE, 98, ["Leave", "Attack"])
    if result == 1:
        StuffDone["213_2"] = 250
        WorldMap.DeactivateTrigger(Location(19,644))
        MessageBox("You charge out of the woods, rushing the gremlins with weapons raised. Seeing you coming, they pull loose the ropes holding the hydra down. Even though the gremlins were about to eat it, the hydra seems to prefer to attack you. Ungrateful!")
        WorldMap.SpawnEncounter("Group_0_13_5", p.Target)
        return

def ZaKhaziRunSouth_669_MapTrigger_9_41(p):
    if StuffDone["213_3"] == 250:
        return
    StuffDone["213_3"] = 250
    WorldMap.DeactivateTrigger(Location(9,665))
    MessageBox("There is a sweet, relaxing smell coming from the cave to the south.")

def ZaKhaziRunSouth_670_MapTrigger_34_21(p):
    MessageBox("You find the skeleton of a drake. The bones of this mighty, twenty foot long lizard have been picked clean, and gnawed to boot. Several wine bottles have been discarded around the corpse. Probably hungry gremlins.")

def ZaKhaziRunSouth_671_SpecialOnWin0(p):
    MessageBox("You don\'t find any extra treasure or loot in the slith\'s campsite, although there are several empty bags and boxes. It\'s like they got rid of all their supplies recently.")

def ZaKhaziRunSouth_672_SpecialOnWin1(p):
    MessageBox("The gremlins and hydra slain, you look around the wreckage of their party. There\'s not much left. Just a few broken knives, forks, and plates, and a large bottle of gremlin wine. You take the wine.")
    Party.GiveNewItem("GremlinWine_214")
