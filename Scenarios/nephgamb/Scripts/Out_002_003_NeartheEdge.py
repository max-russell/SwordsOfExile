
def NeartheEdge_585_MapTrigger_18_10(p):
    if StuffDone["123_0"] >= 1:
        return
    result = ChoiceBox("As you move out onto the bridge, you hear a voice call \"Halt!\", and soldiers emerge from the bushes surrounding the bridge head. \"The terrain beyond the bridge is forbidden area.\" their captain informs you. \"Commander Groul lets no one in.\"\n\nThen he notices your army uniforms and brightens. \"Ah, I see we are on the same side. Sorry to disturb you, I mistook you for common adventurers. Foolish youngsters scramble into the lands of the undead every other week, and we have to rescue them.\n\n\"Makes me wonder if closing off the area around Whitstone was a good idea after all. There is nothing like a good prohibition to attract troublemakers.\"\n\nYou tell the captain who you are and why you need to enter the area. He nods in approval, then asks: \"As a matter of fact, we were just on our way in to save some of our local heroes. They went in two weeks ago and never returned.\n\nIt?s time to go looking for them. Would you care to join us in the rescue operation?\"", eDialogPic.TERRAIN, 65, ["Accept", "Refuse"])
    if result == 0:
        MessageBox("\"Excellent! We know they headed for a cave to the south, reputed to house undead. Follow us to the mouth of the cave, south of the giant stalagmite you see over there!\" The captain and his patrol walk south.")
        StuffDone["123_1"] = 250
        WorldMap.DeactivateTrigger(Location(114,164))
        return
    elif result == 1:
        MessageBox("You can see his disappointment clearly. \"Well, in that case, good luck to you on your important quest. We common soldiers must be on our way, rescuing people. Good day.\" The patrol continues south, leaving you with a bad feeling.")
        return

def NeartheEdge_586_MapTrigger_18_20(p):
    if StuffDone["123_1"] >= 1:
        if StuffDone["123_2"] == 250:
            return
        StuffDone["123_2"] = 250
        MessageBox("The army patrol is scouting the area around a giant crack in the rock. One of the soldiers waves, and the captain smiles. \"They are in there.\" You carefully enter the cave.")
        WorldMap.SpawnNPCGroup("Group_2_3_4", p.Target)
        return

def NeartheEdge_587_SpecialOnWin0(p):
    if StuffDone["123_0"] == 250:
        return
    StuffDone["123_0"] = 250
    WorldMap.DeactivateTrigger(Location(114,154))
    MessageBox("The last bone lies unmoving, and no more rattling is to be heard. The soldiers enter the cave and find, miraculously, the young bravos from the village. They look stunned, but happy to be back outside. Meanwhile, you plunder the bodies.\n\nYou find some gold and an interesting bottle, which you keep. The captain thanks you and returns to the north with the would-be adventurers. You shake your heads over the foolishness of youth and continue your perilous travel.")
    Party.GiveNewItem("StrongEnergyP_248")
    Party.Gold += 300
