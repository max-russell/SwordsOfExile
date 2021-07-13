
def Mines_560_MapTrigger_13_10(p):
    if StuffDone["17_7"] >= 1:
        MessageBox("A bottomless crevice crosses the road and denies you entrance to the fortress beyond. Rumours say this is the entrance to the last nephilim refuges. The guards manning the walls are certainly nephilim. You smile and wave, hoping they will help you across.\n\nTwo agile nephilim guides leap over the walls on their side and climb on sure paws around the crevice. They do their best to show you where to put your feet. Nevertheless, the experience of crossing is among the most frightening of your lives.")
        Party.Reposition(Location(206, 56))
        p.CancelAction = True
        return
    MessageBox("A bottomless crevice crosses the road and denies you entrance to the fortress beyond. Rumours say this is the entrance to the last nephilim refuges. The guards manning the walls are certainly nephilim. You smile and wave, hoping they will help you across.\n\nThey won?t. They shout at you to go away and leave them alone.")

def Mines_561_MapTrigger_11_35(p):
    result = ChoiceBox("One of the mine shafts that riddle northern Chimney opens out into the tunnel in front of you. From where you stand, you get no clues as to whether or not the mine is in use.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["141_0"] >= 1:
            return
        MessageBox("You enter and quickly understand that this mine has fallen into disuse. Shovels and picks are scattered in the corridor as if the miners left in a hurry. Suddenly your light reveals the corpse of one of the miners, and you wonder if you too should leave.\n\nBut you are too late. You sense movement as the undead are drawn towards your sphere of light.")
        WorldMap.SpawnNPCGroup("Group_4_1_4", p.Target)
        return

def Mines_562_MapTrigger_29_19(p):
    result = ChoiceBox("One of the mine shafts that riddle northern Chimney opens out into the tunnel in front of you. From where you stand, you get no clues as to whether or not the mine is in use.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["141_1"] >= 1:
            return
        MessageBox("The mine is abandoned. Perhaps the tin ran out. You wander about, looking into the closed shacks of the miners. Without warning you come across a small group of nephilim. They stand over the body of a human, talking eagerly.\n\nThey are just as surprised as you when you meet. They had never expected anyone to come here to see an abandoned mine. After a moment of surprise, they draw their weapons and charge. You have no choice but to fight.")
        WorldMap.SpawnNPCGroup("Group_4_1_5", p.Target)
        return

def Mines_563_MapTrigger_16_18(p):
    result = ChoiceBox("One of the mine shafts that riddle northern Chimney opens out into the tunnel in front of you. From where you stand, you get no clues as to whether or not the mine is in use.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        MessageBox("As you approach, you find that this mine is fully operational. Shafts burrow deep into the ground, searching for tin ore. As tin melts at a low temperature, it is easier to burn the ore at the dig site than transporting the heavy ore to a smithy.\n\nHuge bonfires are lit at the entrance to the mine. As the rock gets hot, liquid tin drips out and cools in solid bar shapes. You do not stay long. Mining is one of the main occupations in Chimney, and you entered the army partly to avoid it.")
        return

def Mines_566_SpecialOnWin0(p):
    if SpecialItem.PartyHas("Vampirebox"):
        SpecialItem.Take("Vampirebox")
        if StuffDone["141_0"] == 250:
            return
        StuffDone["141_0"] = 250
        MessageBox("The vampire plundering Zarr?s mine has been put to rest. For the moment, if you understand his plans. You pull out your chest and shove the withered remains of the vampire into it. You make sure the nails are in place when you leave.")
        SpecialItem.Give("Fullvampirebox")
        return
    if StuffDone["141_0"] == 250:
        return
    StuffDone["141_0"] = 250
    MessageBox("Perhaps now the miners can return to this mine. You leave the mine without further challenge.")

def Mines_567_SpecialOnWin1(p):
    if StuffDone["141_1"] == 250:
        return
    StuffDone["141_1"] = 250
    MessageBox("Once you have made sure all the rogue nephilim are dead, you look at the human. He is alive, but barely. It appears the nephilim stabbed him and stood waiting for him to die. When you bow over him, he strains to see you \"Humans?\" he whispers.\n\nYou reassure him, and he relaxes somewhat. \"Find Bill,\" he croaks. \"hidden in my archives.\" These are his last words, just as vague as words of this kind always are. A key marked \"Archives\" gives some enlightenment. But who is Bill?")
    SpecialItem.Give("Archivekey")
    StuffDone["17_7"] = 1
