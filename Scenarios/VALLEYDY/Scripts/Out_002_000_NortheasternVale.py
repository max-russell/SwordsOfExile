
def NortheasternVale_388_MapTrigger_13_43(p):
    result = ChoiceBox("As you walk along the river, you find a small, comfortable beach. The river flows to the south, and the water flowing by looks very tempting. Do you drink some?", eDialogPic.TERRAIN, 49, ["Leave", "Drink"])
    if result == 1:
        MessageBox("You kneel down and drink the water. It tastes incredibly unpleasant and acrid, and your tongue and lips burn as you sip it. At first, it seems like the stuff isn\'t having any other effect. Than you start to feel ill ...")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 1))
        return

def NortheasternVale_389_MapTrigger_27_21(p):
    result = ChoiceBox("As you walk along the river, you find a small, comfortable beach. The river flows by to the southwest, and the water flowing by looks very tempting. Do you drink some?", eDialogPic.TERRAIN, 49, ["Leave", "Drink"])
    if result == 1:
        MessageBox("The water is very pleasant. It\'s cool and refreshing, so much so that it\'s hard to believe that the Vale has been having any troubles at all.")
        return

def NortheasternVale_390_MapTrigger_33_9(p):
    if StuffDone["202_0"] == 250:
        return
    StuffDone["202_0"] = 250
    WorldMap.DeactivateTrigger(Location(129,9))
    MessageBox("You walk up a remote pathway, leading up and away from the river headwaters. As you climb, you notice a chill forming in the air. You pass stones covered with strange markings, worn and unreadable.")

def NortheasternVale_391_MapTrigger_29_4(p):
    if StuffDone["202_1"] == 250:
        return
    result = ChoiceBox("At the end of the path you find, worn away by recent rains, a crypt door. It\'s a stone slab, rolled over a tunnel into the hillside. With a little effort, you could easily work your way inside.", eDialogPic.TERRAIN, 104, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["202_1"] == 250:
            return
        StuffDone["202_1"] = 250
        WorldMap.AlterTerrain(Location(125,4), 1, None)
        WorldMap.DeactivateTrigger(Location(125,4))
        MessageBox("You pull the crypt open and hear a thin, hideous moaning coming from inside. You try to push the stone back into place, but you aren\'t fast enough. Undead creatures come shambling out ...")
        WorldMap.SpawnNPCGroup("Group_2_0_4", p.Target)
        return

def NortheasternVale_392_MapTrigger_25_7(p):
    if StuffDone["202_2"] == 250:
        return
    result = ChoiceBox("At the end of the path you find, worn away by recent rains, a crypt door. It\'s a stone slab, rolled over a tunnel into the hillside. With a little effort, you could easily work your way inside.", eDialogPic.TERRAIN, 104, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["202_2"] == 250:
            return
        StuffDone["202_2"] = 250
        WorldMap.AlterTerrain(Location(121,7), 1, None)
        WorldMap.DeactivateTrigger(Location(121,7))
        MessageBox("You pull the crypt open and hear a thin, hideous moaning coming from inside. You try to push the stone back into place, but you aren\'t fast enough. Undead creatures come shambling out ...")
        WorldMap.SpawnNPCGroup("Group_2_0_4", p.Target)
        return

def NortheasternVale_393_MapTrigger_29_10(p):
    if StuffDone["202_3"] == 250:
        return
    result = ChoiceBox("At the end of the path you find, worn away by recent rains, a crypt door. It\'s a stone slab, rolled over a tunnel into the hillside. With a little effort, you could easily work your way inside.", eDialogPic.TERRAIN, 104, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["202_3"] == 250:
            return
        StuffDone["202_3"] = 250
        WorldMap.AlterTerrain(Location(125,10), 1, None)
        WorldMap.DeactivateTrigger(Location(125,10))
        MessageBox("You pull the crypt open and hear a thin, hideous moaning coming from inside. You try to push the stone back into place, but you aren\'t fast enough. Undead creatures come shambling out ...")
        WorldMap.SpawnNPCGroup("Group_2_0_4", p.Target)
        return

def NortheasternVale_394_MapTrigger_40_37(p):
    if StuffDone["202_4"] == 250:
        return
    result = ChoiceBox("You wouldn\'t have noticed it if you weren\'t right on top of it. For reasons unknown, someone left a small buckler here, barely concealed behind a large rock.\n\nFinders keepers, losers weepers ...", eDialogPic.TERRAIN, 33, ["Take", "Leave"])
    if result == 0:
        StuffDone["202_4"] = 250
        WorldMap.DeactivateTrigger(Location(136,37))
        Party.GiveNewItem("IronBuckler_141")
    return

def NortheasternVale_395_MapTrigger_31_27(p):
    if StuffDone["202_5"] == 250:
        return
    result = ChoiceBox("Interesting. Someone left a skull balanced on a rock here, for no reason you can determine.", eDialogPic.TERRAIN, 77, ["Take", "Leave"])
    if result == 0:
        StuffDone["202_5"] = 250
        WorldMap.AlterTerrain(Location(127,27), 1, None)
        WorldMap.DeactivateTrigger(Location(127,27))
        Party.GiveNewItem("Skull_24")
    return

def NortheasternVale_396_MapTrigger_18_28(p):
    if StuffDone["202_6"] == 250:
        return
    StuffDone["202_6"] = 250
    WorldMap.DeactivateTrigger(Location(114,28))
    MessageBox("As you walk along this path, you notice that a bit of the river splits off into a smaller channel, which then flows under the hill to the south, You wonder where the water goes.")

def NortheasternVale_397_MapTrigger_8_41(p):
    return

def NortheasternVale_398_SpecialOnWin0(p):
    MessageBox("The undead finally put to rest, you are free to search their crypt. Fortunately, the creatures were buried with a variety of trinkets. You leave mildly richer.")
    Party.Gold += 250
