
def ByRiverMyld_543_MapTrigger_15_4(p):
    if StuffDone["121_0"] == 250:
        return
    StuffDone["121_0"] = 250
    WorldMap.DeactivateTrigger(Location(111,52))
    WorldMap.DeactivateTrigger(Location(111,53))
    WorldMap.DeactivateTrigger(Location(113,53))
    WorldMap.DeactivateTrigger(Location(104,51))
    WorldMap.DeactivateTrigger(Location(105,51))
    WorldMap.DeactivateTrigger(Location(103,51))
    WorldMap.DeactivateTrigger(Location(102,51))
    WorldMap.DeactivateTrigger(Location(114,53))
    WorldMap.DeactivateTrigger(Location(115,53))
    MessageBox("You take a deep breath and savour the fresh air of the Chimney cave. Unlike most other caverns in Exile, the air is moist, and drifts past you as a gentle breeze. Looking up and to the south, you can make out the great opening in the cave ceiling.\n\nIt serves as a vent for the warm, humid slith caverns and is the cause of Chimney?s unique climate. The result is visible all around you: Plants sprout from the fertile soil, enlivening the terrain. This is what the Surface must look like, you think.")

def ByRiverMyld_546_MapTrigger_13_13(p):
    result = ChoiceBox("The paved road ends at a solid pier, struggling against the currents of Myld River. Sheltering behind the pier lies a heavy barge, unloading its cargo. This barge could make a trip south a lot easier. Will you approach and demand passage?", eDialogPic.TERRAIN, 49, ["Leave", "Approach"])
    if result == 1:
        if SpecialItem.PartyHas("Commandeerletter"):
            ChoiceBox("You approach the captain on board the barge, showing him your commandeer letter. He reads it through twice, checks the seal and nods to you. Then he turns about and shouts to his crew to stop unloading cargo and prepare to go south.\n\nThe crew looks confused and the merchants carrying the goods roar in infuriated surprise, but the ship?s captain insists. These orders are more important. So after a very short discussion, you pull away from the docks.\n\n\"I can take you as far as Tuva,\" the captain says. \"finding a connection south should be no problem.\" You find comfortable seats on the nearly empty deck of the barge and enjoy your trip south.\n\nThe fierce current in this part of the river makes even the heavy barge unsteady. To counter this, thick ropes are tied to teams of giant lizards on both banks. Their bulk and muscles keep the boat in place on the way down and pulls the load back north.\n\nYou quickly tire of the dull lizards and their drivers and study the river banks. The terrain grows more humid as you travel south, filled with vegetation that would startle a surface worlder. Yet it holds an eerie beauty that never fails to charm you.\n\nWhat does the future hold for Chimney? Will the sliths take it all over and convert it into poisonous swampland? Finally, your destination appears and puts a stop to your sombre thoughts.", eDialogPic.TERRAIN, 1026, ["OK"])
            Party.Age += 200
            Party.Reposition(Location(127, 95))
            p.CancelAction = True
            return
        MessageBox("You corner the captain on board the barge and request passage. He brusquely fends you off. \"I?m sorry, but your errands will have to wait. My ferry has been commandeered for military service.\" He leaves without looking at you again.")
        return

def ByRiverMyld_553_MapTrigger_31_46(p):
    result = ChoiceBox("The north pier of Tuva Isle is just as busy as the other harbours you have seen on river Myld. As you approach, a barge is preparing to go north. \"Last call for Lushwater Toll!\"", eDialogPic.TERRAIN, 63, ["Leave", "Enter"])
    if result == 1:
        MessageBox("Rushing on board, you wave your document at the captain, who barely looks at it. He is going north anyway, and has room for passengers. You settle and watch the lizards pulling you north. After many hours you land at Lushwater.")
        Party.Age += 300
        Party.Reposition(Location(109, 61))
        p.CancelAction = True
        return

def ByRiverMyld_554_MapTrigger_23_1(p):
    if StuffDone["6_0"] >= 1:
        result = ChoiceBox("An old fisherman rows hard against the current on the way to his favourite fishing spot. You hail him, but he ignores you at first. But he must have been studying you after all, for suddenly he shouts and steers towards the shore.\n\n\"Are you the Heroes of Brattaskar?\" he shouts. \"Well done! Can I give you a lift?\" His offer is of some help if you intend to cross the river Myld. The closest bridge is a long way south.", eDialogPic.TERRAIN, 46, ["Leave", "Accept"])
        if result == 1:
            Party.Reposition(Location(123, 49))
            p.CancelAction = True
            return
        return
    MessageBox("An old fisherman rows hard against the stream on the way to his favourite fishing spot. You hail him, but he ignores you, intent on crossing the river.")

def ByRiverMyld_555_MapTrigger_27_1(p):
    result = ChoiceBox("An old fisherman rows hard against the current on the way to his favourite fishing spot. You hail him, but he ignores you at first. But he must have been studying you after all, for suddenly he shouts and steers towards the shore.\n\n\"Are you the Heroes of Brattaskar?\" he shouts. \"Well done! Can I give you a lift?\" His offer is of some help if you intend to cross the river Myld. The closest bridge is a long way south.", eDialogPic.TERRAIN, 46, ["Leave", "Accept"])
    if result == 1:
        Party.Reposition(Location(119, 49))
        p.CancelAction = True
        return

def ByRiverMyld_556_MapTrigger_16_8(p):
    if StuffDone["121_1"] == 250:
        return
    StuffDone["121_1"] = 250
    WorldMap.DeactivateTrigger(Location(112,56))
    MessageBox("The chute connecting the slith caverns to central Exile opens up in the ceiling just above this island. A curious meteorological effect causes the moistness in the air to fall like rain, enabling the growth of what is probably the biggest forest in Exile.\n\nAn old town nestles by the stone bridge spanning the river Myld. It dates back to one of the old robber barons that settled Chimney.")
