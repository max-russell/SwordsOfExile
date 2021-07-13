
def SwampyArea_489_MapTrigger_21_22(p):
    if StuffDone["211_0"] == 250:
        return
    result = ChoiceBox("Way out here, deep in the grim marshes, you find a small, sod hut. A thin wisp of smoke rises from its chimney. It\'s surrounded by herb gardens on all sides. The door is closed, but you could knock on it.", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        result = ChoiceBox("When you reach the door, you don\'t even have time to knock. The door flies open, and a withered, scowling crone peers out at you. She\'s ancient and twisted, and looks very dangerous.", eDialogPic.CREATURE, 29, ["Leave", "Attack", "Wait"])
        if result == 1:
            if StuffDone["211_0"] == 250:
                return
            StuffDone["211_0"] = 250
            WorldMap.AlterTerrain(Location(165,118), 1, None)
            WorldMap.DeactivateTrigger(Location(165,118))
            MessageBox("You pull out your swords. She jumps back, startled. As you start to enter her hut, she casts a spell. The hut shimmers around you, and disappears.\n\nAs you stand alone in the fen, you hear a harsh, screeching voice coming from somewhere nearby: \"You\'ll pay for your rudeness, children!\"")
            Timer(None, 50, False,  "ScenarioTimer_x_496")
            MessageBox("Oh well. Her herb garden stayed behind. You\'re able to pick some useful alchemical ingredients.")
            Party.GiveNewItem("MandrakeRoot_370")
            return
        elif result == 2:
            result = ChoiceBox("When she sees that you don\'t intend to be rude, she smiles. Her teeth are a charming green color. She says \"Come in, my children! Come in! It is so rare I have someone to share my skills with.\"\n\nShe sees your hesitance at entering her hovel, and shrugs. \"Oh well. Just as easy out here. I\'m known as Fallatina, or I was, before I came out here to spend time with my cauldron and my herbs.\"\n\n\"Oh, the wonderful potions I can make! And I will share them with you, if you pay the price. Will you?\"", eDialogPic.CREATURE, 29, ["Leave", "Buy"])
            if result == 1:
                OpenShop("Shop_Items_Outside_11_3_2")
                p.CancelAction = True
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You respectfully decline. The witch shakes her head. \"Ah, children, you do not know when you have had a generous offer made. Oh, well. I don\'t plan to go anywhere. Come back anytime.\" She withdraws into her hut, and slams the door.")
            return
        return

def SwampyArea_490_MapTrigger_7_32(p):
    if StuffDone["211_1"] == 250:
        return
    result = ChoiceBox("Deep in the swamp, you find a deep, dank cave, almost overgrown with roots and reeds. There are large lizard tracks and gnawed bones everywhere, and the area stinks of reptilian malice.", eDialogPic.TERRAIN, 78, ["Leave", "Enter"])
    if result == 1:
        StuffDone["211_1"] = 250
        WorldMap.AlterTerrain(Location(151,128), 1, None)
        WorldMap.DeactivateTrigger(Location(151,128))
        MessageBox("Sure enough, inside the cavern, you find one of the many predatory, unfriendly denizens of the swamp. Its many heads growl hungrily, and it lumbers towards you.")
        WorldMap.SpawnEncounter("Group_3_2_4", p.Target)
        return

def SwampyArea_491_MapTrigger_30_6(p):
    if StuffDone["211_2"] == 250:
        return
    result = ChoiceBox("Deep in the swamp, you find a deep, dank cave, almost overgrown with roots and reeds. There are large lizard tracks and gnawed bones everywhere, and the area stinks of reptilian malice.", eDialogPic.TERRAIN, 78, ["Leave", "Enter"])
    if result == 1:
        StuffDone["211_2"] = 250
        WorldMap.AlterTerrain(Location(174,102), 1, None)
        WorldMap.DeactivateTrigger(Location(174,102))
        MessageBox("Sure enough, inside the cavern, you find one of the many predatory, unfriendly denizens of the swamp. Its many heads growl hungrily, and it lumbers towards you.")
        WorldMap.SpawnEncounter("Group_3_2_4", p.Target)
        return

def SwampyArea_492_MapTrigger_5_7(p):
    MessageBox("As you walk through the trees, you suddenly stub your toe. Looking down, you see a stone slab, partially concealed by brush.\n\nClearing away the brush, you see that the stone reads \"First Stone.\" Odd.")
    StuffDone["211_3"] = 1
