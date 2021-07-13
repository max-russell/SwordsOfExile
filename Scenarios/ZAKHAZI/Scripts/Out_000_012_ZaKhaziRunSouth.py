
def ZaKhaziRunSouth_654_MapTrigger_25_10(p):
    if StuffDone["212_0"] == 250:
        return
    StuffDone["212_0"] = 250
    WorldMap.DeactivateTrigger(Location(25,586))
    WorldMap.DeactivateTrigger(Location(26,586))
    WorldMap.DeactivateTrigger(Location(20,590))
    WorldMap.DeactivateTrigger(Location(22,590))
    WorldMap.DeactivateTrigger(Location(9,583))
    MessageBox("You see a small group of slithzerikai. They see you. As you size each other up, you wonder if these are friendly or hostile sliths. You aren\'t kept in suspense for long.")
    WorldMap.SpawnEncounter("Group_0_12_4", p.Target)

def ZaKhaziRunSouth_659_MapTrigger_10_3(p):
    if StuffDone["212_1"] == 250:
        return
    StuffDone["212_1"] = 250
    WorldMap.DeactivateTrigger(Location(10,579))
    MessageBox("This cave is guarded by a band of about a dozen slithzerikai. In the dim green light of the caves, they manage to spot you from about a thousand feet away. However, instead of attacking, they immediately flee.\n\nYou\'re a tough band, but you didn\'t think you looked that fearsome. You wonder where they went.")

def ZaKhaziRunSouth_660_MapTrigger_5_4(p):
    if StuffDone["212_3"] >= 1:
        MessageBox("The slith fortress has finally been cleaned out. You don\'t find much of anything to loot, unfortunately, all of the slith\'s possessions were carried with them.")
        return
    if StuffDone["212_2"] >= 1:
        result = ChoiceBox("You have returned to the entrance of the Slithzerikai lair. Again, there are no guards outside, but you can hear the muttering of the creatures inside. Do you assault them again?", eDialogPic.TERRAIN, 244, ["Leave", "Enter"])
        if result == 1:
            if StuffDone["212_3"] == 250:
                return
            StuffDone["212_3"] = 250
            WorldMap.AlterTerrain(Location(5,580), 1, None)
            WorldMap.DeactivateTrigger(Location(5,580))
            MessageBox("You charge into the slith lair, surprising a band of the reptilian creatures. Amazingly, they seem to have thought you wouldn\'t dare attack them again. They underestimated how persistent adventurers can be.\n\nThere\'s quite a lot of them, however, and their surprise doesn\'t last for long. They grab their wicked, two-tined spears, and attack.")
            WorldMap.SpawnEncounter("Group_0_12_5", p.Target)
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Battling sliths, while admirable, isn\'t part of your mission. You back away.")
        return
    result = ChoiceBox("This pit was probably where the sliths you saw earlier fled. It\'s a narrow tunnel sloping steeply down into the ground. You see several totems and crude sculptures nearby, which look like they were created by the lizard people.\n\nListening at the cave entrance, you hear alert, sibilant voices inside.", eDialogPic.TERRAIN, 244, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["212_2"] == 250:
            return
        StuffDone["212_2"] = 250
        MessageBox("The tunnel leads to a wide, low cave, which is filled with dozens of Slithzerikai. A band of them immediately charge you, pushing you back out of their outpost with muscular, scaled arms.\n\nOnce outside the cave, they attack you. Fortunately, so far the sliths have deemed only a small part of their number adequate to deal with you.")
        WorldMap.SpawnEncounter("Group_0_12_4", p.Target)
        p.CancelAction = True
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Battling sliths, while admirable, isn\'t part of your mission. You back away.")

def ZaKhaziRunSouth_661_MapTrigger_23_36(p):
    if StuffDone["212_4"] >= 1:
        if StuffDone["212_5"] == 250:
            return
        StuffDone["212_5"] = 250
        MessageBox("At the end of this passage, you find the pile of gray, chalky stones Aleel told you about. Digging in the pile, you find 3 stones with just the right shade of mottled gray. They\'re large and heavy, but you manage to fit them into your packs.")
        SpecialItem.Give("GrayStones")
        return
    MessageBox("The corridor dead ends at a large pile of gray, chalky looking stones. You poke around in them, but you don\'t find anything of interest.")

def ZaKhaziRunSouth_662_MapTrigger_35_4(p):
    if StuffDone["212_6"] == 250:
        return
    result = ChoiceBox("There are moldy stones jumbled all throughout this isolated cave. Most of them are dull. Worthless. Gray. One small rock, however, is rounded and glitters slightly.\n\nYou poke it gingerly with your finger and find that it\'s warm to the touch. Could be interesting.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["212_6"] = 250
        WorldMap.AlterTerrain(Location(35,580), 1, None)
        WorldMap.DeactivateTrigger(Location(35,580))
        Party.GiveNewItem("PowerGeode_338")
    return

def ZaKhaziRunSouth_663_MapTrigger_26_20(p):
    if StuffDone["212_8"] == 250:
        return
    StuffDone["212_8"] = 250
    WorldMap.DeactivateTrigger(Location(26,596))
    MessageBox("You find a small patch of comfrey root!")
    Party.GiveNewItem("ComfreyRoot_364")

def ZaKhaziRunSouth_664_MapTrigger_26_23(p):
    if StuffDone["212_7"] == 250:
        return
    StuffDone["212_7"] = 250
    WorldMap.DeactivateTrigger(Location(26,599))
    MessageBox("You find a small patch of holly!")
    Party.GiveNewItem("Holly_363")

def ZaKhaziRunSouth_665_SpecialOnWin1(p):
    MessageBox("Many of the sliths had large, leather satchels slung over their shoulders. Looking inside, you find that this outpost carries most of its supplies on its back. You find a ration-free supply of dried fish, mushrooms, and other tasty goodies.\n\nThe leader also wore a bone necklace, with several semi-precious stones. You take it with you. It might be valuable.")
    Party.GiveNewItem("FangNecklace_323")
    Party.Food += 200
