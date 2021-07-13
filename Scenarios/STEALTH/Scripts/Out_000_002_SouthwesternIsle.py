
def SouthwesternIsle_454_MapTrigger_9_13(p):
    if Game.Mode == eMode.OUTSIDE and WorldMap.TerrainAt(Location(10,109)).Num == 112:
        if Party.HasTrait(Trait.Woodsman):
            MessageBox("Your Woodsman skill comes in handy! You see a narrow, windy path leading through the woods to the east.")
            WorldMap.AlterTerrain(Location(10,109), 0, TerrainRecord.UnderlayList[114])
            return
        return

def SouthwesternIsle_455_MapTrigger_10_11(p):
    if StuffDone["208_1"] == 250:
        return
    result = ChoiceBox("What luck! In this isolated glade, you find a patch of valuable alchemical ingredients!", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["208_1"] = 250
        WorldMap.DeactivateTrigger(Location(10,107))
        Party.GiveNewItem("EmberFlowers_369")
    return

def SouthwesternIsle_456_MapTrigger_13_10(p):
    if StuffDone["208_0"] == 250:
        return
    result = ChoiceBox("What luck! In this isolated glade, you find a patch of valuable alchemical ingredients!", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["208_0"] = 250
        WorldMap.DeactivateTrigger(Location(13,106))
        Party.GiveNewItem("Graymold_368")
    return

def SouthwesternIsle_457_MapTrigger_15_10(p):
    if StuffDone["208_2"] == 250:
        return
    result = ChoiceBox("What luck! In this isolated glade, you find a patch of valuable alchemical ingredients!", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["208_2"] = 250
        WorldMap.DeactivateTrigger(Location(15,106))
        Party.GiveNewItem("Graymold_368")
    return

def SouthwesternIsle_458_MapTrigger_18_30(p):
    if StuffDone["208_3"] == 250:
        return
    StuffDone["208_3"] = 250
    WorldMap.AlterTerrain(Location(18,126), 1, None)
    WorldMap.DeactivateTrigger(Location(18,126))
    result = ChoiceBox("You stumble upon a scene of violence and horror. A band of ogres has trapped a patrol of soldiers, and is rapidly closing in on them. Many of the soldiers have fallen already, and things don\'t look good for the remainder.\n\nWhen the soldiers see you, not knowing whether you\'re working for the Empire or the rebels, they shout for help. Their situation is pretty desperate.\n\nDo you help?", eDialogPic.CREATURE, 42, ["No", "Yes"])
    if result == 0:
        MessageBox("Ogres are serious business. You flee, hearing the final shouts of the Empire troops behind you. Unfortunately, ogres can move surprisingly fast on those stumpy legs of theirs, and you looked like good prey.\n\nBefore you can get out of the winding mountain valley, they catch you.")
        WorldMap.SpawnEncounter("Group_0_2_4", p.Target)
        return
    elif result == 1:
        MessageBox("Even with the soldiers\' help, this is going to be an ugly fight. You draw your blades and charge to help ...")
        WorldMap.SpawnEncounter("Group_0_2_5", p.Target)
        return

def SouthwesternIsle_459_MapTrigger_26_17(p):
    if StuffDone["208_4"] == 250:
        return
    result = ChoiceBox("Looks like an unfortunate ogre became lost in this forest, and was eaten by mean wolves before he had a chance to find his way out. Fortunately, the wolves didn\'t find his big, pretty sword edible.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["208_4"] = 250
        WorldMap.AlterTerrain(Location(26,113), 1, None)
        WorldMap.DeactivateTrigger(Location(26,113))
        Party.GiveNewItem("CursedGreatsword_374")
    return

def SouthwesternIsle_460_SpecialOnWin0(p):
    MessageBox("Battered and bleeding, you stagger away from the battlefield. There isn\'t too much loot to be found, although one suit of chain mail pulled off an Empire soldier is of fairly high quality.")
    Party.GiveNewItem("SteelChainMail_131")

def SouthwesternIsle_461_SpecialOnWin1(p):
    MessageBox("Once the battle is won, the soldiers walk up to greet you. It\'s an awkward moment ... they are unsure whether you are on their side or on the side of the rebels.\n\nStill, they thank you profusely for your help. Then, watching you over their shoulders, they pick up their dead and wounded and limp back to Selathni.")

def SouthwesternIsle_462_SpecialOnFlee1(p):
    MessageBox("You flee, leaving the Empire soldiers behind to suffer grim fates. You manage to make your way back down the mountain path without ogre pursuit.")
