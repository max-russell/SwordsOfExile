
def EmptyRoad_521_MapTrigger_40_28(p):
    MessageBox("You stand uncertainly at a crossroads. You should hurry to the human settlements to warn of the slith renegade band. But on the other hand, the slith attack caught you with only crude weapons and almost no equipment.\n\nYou are poorly prepared for encounters. The path to the south leads to a small arms depot. You have never visited it, but you have heard Mathias mention the emergency reserve. You weigh the necessity of speed against your own safety.")

def EmptyRoad_522_MapTrigger_21_26(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The ruins of your old fort are a painful memory, and you are hesitant to enter. Moreover, slith assassins might still lurk inside, waiting for more easy booty. You stay out.")

def EmptyRoad_523_MapTrigger_45_21(p):
    result = ChoiceBox("A burned-out hut tells the story of relentless invaders. You knew its occupant, an old hermit who stopped by your station once or twice. You hardly believe that he could have survived the attack. Still, you feel an obligation to investigate.", eDialogPic.TERRAIN, 239, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["100_2"] == 250:
            return
        StuffDone["100_2"] = 250
        MessageBox("You do not find out much. The place is utterly ruined, and the attackers are long gone. However, scavengers have already moved in, and do not take kindly to your intrusion.")
        WorldMap.SpawnNPCGroup("Group_0_0_5", p.Target)
        return

def EmptyRoad_524_MapTrigger_8_22(p):
    MessageBox("At this point, the road turns steeply upwards and enters the Brattaskar Pass. The road climbs for three of four days from here before it enters the caverns of central Exile.")

def EmptyRoad_527_MapTrigger_30_27(p):
    MessageBox("This sight confirms your worst fear: The attack on the fort was not an isolated act of terrorism. The smoking remains of a large caravan lie scattered over the road. Several wagons have been overturned, looted and put on fire.\n\nAmong the numerous dead you find two slith corpses that confirm the identity of the attackers. You notice that they wear a necklace similar to the one you found on the slith leader. Your sense of urgency grows as you hurry on past this sinister scene.")

def EmptyRoad_528_MapTrigger_42_32(p):
    if StuffDone["100_0"] == 250:
        return
    StuffDone["100_0"] = 250
    WorldMap.DeactivateTrigger(Location(42,32))
    MessageBox("Goblins dare not leave the woods these days. But entering the shelter of the trees, you are invading their territory. A small team of hunters eagerly seizes the opportunity to take you on on their own ground.")
    WorldMap.SpawnNPCGroup("Group_0_0_4", p.Target)

def EmptyRoad_529_MapTrigger_32_34(p):
    if StuffDone["100_1"] == 250:
        return
    StuffDone["100_1"] = 250
    WorldMap.DeactivateTrigger(Location(32,34))
    MessageBox("Goblins dare not leave the woods these days. But entering the shelter of the trees, you are invading their territory. A small team of hunters eagerly seizes the opportunity to take you on on their own ground.")
    WorldMap.SpawnNPCGroup("Group_0_0_4", p.Target)

def EmptyRoad_530_MapTrigger_4_21(p):
    p.CancelAction = False
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Your country needs your help. At this time you should put every effort into saving your home, not run away.")

def EmptyRoad_533_MapTrigger_40_34(p):
    MessageBox("The forest has taken over the road. You can barely make out the track from here, much less continue through the tangled undergrowth.")

def EmptyRoad_534_SpecialOnWin0(p):
    MessageBox("You defeated this band of goblins. Still, you get the feeling that you have not seen the last of them.")

def EmptyRoad_535_SpecialOnWin1(p):
    MessageBox("After beating off the scavengers, you search the hut. You see no signs of the hermit. Instead, you find that one of the potions he made for a living has survived the fire. You feel entitled to keep it as compensation for the investigation.")
    Party.GiveNewItem("MediumEnergyP_255")
