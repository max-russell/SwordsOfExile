
def NorthwesternVale_372_MapTrigger_42_15(p):
    p.CancelAction = False
    result = ChoiceBox("At the end of the peaceful forest path, you find that a druid has set herself up a small, pleasant grove. She is kneeling outside, busily planting a small row of comfrey root. Deer graze happily around her.\n\nAs you approach, she sees you and waves. For whatever reason, she seems to want to talk to you.", eDialogPic.TERRAIN, 190, ["Leave", "Approach"])
    if result == 1:
        result = ChoiceBox("The druid stands up and greets you. As she does, bluebirds land on her shoulders and chirp a happy song. Deer walk up and nuzzle against her. It\'s all a bit much, really.\n\nShe says \"Welcome, bold saviors. I am Athia, guardian of the Vale. Alas, sadly, my efforts to end the curse afflicting us have been in vain.\" A chipmunk runs up and sits on her foot.\n\n\"Fortunately, you have come. I wish to help you if I can. I know how to create some herbal concoctions that you may be able to use in your travels. Do you wish to learn how to make them?\"", eDialogPic.CREATURE, 26, ["Yes"])
        if result == 0:
            OpenShop("Shop_Alchemy_Outside_4_0_0")
            p.CancelAction = True
            return
        return
    MessageBox("You back away. She shrugs sadly, and returns to her work, as birds and squirrels play and frolic around her.")

def NorthwesternVale_373_MapTrigger_7_4(p):
    if StuffDone["200_0"] == 250:
        return
    result = ChoiceBox("At the far end of the goblin\'s valley, you find what looks like a temple. Of course, it\'s goblin architecture, so it also strongly resembles a huge pile of random rocks, prone to fall over at any moment.", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["200_0"] == 250:
            return
        result = ChoiceBox("You work your way in, quite reasonably afraid that the whole structure will collapse in on you. The building is about 30 feet long and 20 feet wide, and, fortunately, currently bereft of goblins.\n\nAt the far end, you find the standard evil altar, with the standard disturbing brown stains on it. There is also a gold necklace, probably left as some sort of sacrifice. There\'s nothing stopping you from helping yourself.", eDialogPic.TERRAIN, 154, ["Take", "Leave"])
        if result == 0:
            StuffDone["200_0"] = 250
            WorldMap.AlterTerrain(Location(7,4), 1, None)
            WorldMap.DeactivateTrigger(Location(7,4))
            Party.GiveNewItem("RubyCharm_321")
            MessageBox("When you pick up the gold necklace, you hear a loud, shrill keening. At first, you think that some sort of foul demon has been summoned. No such luck.\n\nIt was a crude alarm system. You run to the entrance to the temple and see a bunch of shrieking, evil monsters running up to punish you for your theft.")
            WorldMap.SpawnNPCGroup("Group_0_0_5", p.Target)
            return
        return
        return
    p.CancelAction = False

def NorthwesternVale_374_MapTrigger_26_14(p):
    if StuffDone["200_1"] == 250:
        return
    StuffDone["200_1"] = 250
    WorldMap.DeactivateTrigger(Location(26,14))
    MessageBox("The hills become more jagged, the animals become scarcer, and the air becomes even more acrid. Shards of bone crunch underfoot. You seem to be approaching one of the Vale\'s less welcoming areas.")

def NorthwesternVale_375_MapTrigger_20_15(p):
    if StuffDone["200_2"] == 250:
        return
    StuffDone["200_2"] = 250
    WorldMap.DeactivateTrigger(Location(20,15))
    MessageBox("You reach the entrance to a smaller, more remote valley. You detect the smells of cooking fires and hear rhythmic grunting echoing in the distance. Goblins. It can only be goblins.\n\nAs if to punctuate this realization, a band of goblins comes up from behind you, on the way back from an unsuccessful hunting trip. Unsuccessful, until now ...")
    WorldMap.SpawnNPCGroup("Group_0_0_4", p.Target)

def NorthwesternVale_376_MapTrigger_7_44(p):
    MessageBox("The valley ends at a small, highly active hot spring.")

def NorthwesternVale_377_MapTrigger_34_33(p):
    if StuffDone["200_3"] == 250:
        return
    StuffDone["200_3"] = 250
    WorldMap.DeactivateTrigger(Location(34,33))
    ChoiceBox("As you cross the bridge, mist from the river below settles on your skin. It burns your eyes and gives you rashes. You shudder to think what effect drinking it must have.\n\nThe water is also eating away at the bridge supports. Another year or two, and this bridge will be gone.", eDialogPic.TERRAIN, 65, ["OK"])

def NorthwesternVale_378_SpecialOnWin1(p):
    MessageBox("You survey the carnage around you. For a moment, it\'s hard to believe you survived. You finish looting the temple. There\'s not much there, just a few coins and bits of silver. You help yourself.")
    Party.Gold += 200
