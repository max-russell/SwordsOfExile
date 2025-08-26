
def NearSweetgrove_413_MapTrigger_42_10(p):
    MessageBox("It looks like someone was camped here recently. Whoever they were, they cleaned up well when they left.")

def NearSweetgrove_414_MapTrigger_11_33(p):
    ChoiceBox("You find an empty farmhouse, surrounded by twisted and dying crops. The untended rows of corn around the house look like they\'ve been rotting from the bottom up.\n\nSome plots of corn have moldered entirely away, decomposing into a thick layer of odorous, diseased goo. The smell is hideous.\n\nOn the door of the farmhouse, you find a simple note: \"Help yourself to the farm. And may the Gods help you if you take it.\"\n\nFinding nothing of value, you leave.", eDialogPic.TERRAIN, 78, ["OK"])

def NearSweetgrove_415_MapTrigger_32_29(p):
    result = ChoiceBox("This is quite an anomaly for Skylark Vale: a functioning farm. Smoke spirals up from the chimney, and the farmhouse is defiantly cheery in the face of the sickly crops all around it.\n\nGo knock on the door?", eDialogPic.TERRAIN, 190, ["Yes", "No"])
    if result == 0:
        result = ChoiceBox("You knock on the door, and, after a long pause, it is answered by a huge, deeply tanned man. He looks you over, and lowers the heavy crossbow he held pointed at you.\n\nHe introduces himself as Cole and invites you in for bowls of stew and conversation. You talk for a while. He tells you horror stories of happenings in the valley, and you share news of the rest of the world.\n\nAfter a time, he says \"By the way, this farm is rather sick. The way I make a little extra is by selling supplies on the side. Interested?\"", eDialogPic.CREATURE, 2, ["Leave", "Buy"])
        if result == 1:
            OpenShop("Shop_Items_Outside_6_2_1")
            p.CancelAction = True
            return
        return
    elif result == 1:
        MessageBox("You walk away, reassured that at least a few things in this valley haven\'t been given up for dead.")
        return

def NearSweetgrove_416_MapTrigger_16_20(p):
    if StuffDone["205_0"] == 250:
        return
    StuffDone["205_0"] = 250
    WorldMap.DeactivateTrigger(Location(112,68))
    MessageBox("Ever since you entered the Vale, you\'ve detected this strange, bitter smell. Now, walking over this bridge, it becomes stronger, so strong you feel nauseous and faint.\n\nLooking down, you realize where it must be coming from: the water! The smell coming up from the river burns your nose and makes your eyes water.")

def NearSweetgrove_417_MapTrigger_24_2(p):
    if StuffDone["205_1"] == 250:
        return
    result = ChoiceBox("You hike through the stone circle, and find you\'re surrounded by bushes of wild strawberries. They look sickly, but still edible. Pick some?", eDialogPic.TERRAIN, 4, ["Take", "Leave"])
    if result == 0:
        StuffDone["205_1"] = 250
        WorldMap.DeactivateTrigger(Location(120,50))
        Party.Food += 30
    return

def NearSweetgrove_418_MapTrigger_45_33(p):
    if StuffDone["205_2"] == 250:
        return
    result = ChoiceBox("You see cooking fires at the head of the valley, and approach cautiously. A quick scout ahead confirms your suspicions. A band of bandits are camped up here, counting up loot stolen from the beleaguered people of Skylark Vale.\n\nOf course, you could always attack and teach them a good lesson. They look tough, but you would have the advantage of surprise. And, of course, you would be on the side of goodness, which always helps.", eDialogPic.CREATURE, 18, ["Leave", "Attack"])
    if result == 1:
        MessageBox("You\'re in luck! You charge the bandits, and they draw their weapons and attack you! You will be able to fight a glorious battle for the forces of goodness after all.")
        WorldMap.SpawnEncounter("Group_2_1_4", p.Target)
        StuffDone["205_2"] = 250
        WorldMap.AlterTerrain(Location(141,81), 1, None)
        WorldMap.DeactivateTrigger(Location(141,81))
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You back away nervously. Evil will just have to be vanquished another day.")

def NearSweetgrove_419_MapTrigger_44_23(p):
    MessageBox("You can\'t help but notice that it\'s pretty hot.")

def NearSweetgrove_420_SpecialOnWin0(p):
    MessageBox("You search the brigand camp, and find gold and food, and some nice arrows to boot! This is your lucky day!")
    Party.GiveNewItem("IronArrows_104")
    Party.Gold += 200
    Party.Food += 80
