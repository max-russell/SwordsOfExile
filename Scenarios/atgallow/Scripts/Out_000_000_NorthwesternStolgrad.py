
def NorthwesternStolgrad_2303_MapTrigger_14_27(p):
    if StuffDone["13_7"] < 1:
        RunScript("GlobalCall_NorthwesternStolgrad_2852", ScriptParameters(eCallOrigin.CUSTOM))
        StuffDone["14_2"] = 1
        ChoiceBox("Off the shore you make out a large fortress on a barren island. You know of that place. It is called Ironclad Island. The foreboding structure houses the most dangerous criminals in the world. Those sentenced there, never come out.\n\nYou turn your attention north along the shore. There you see two stone docks, no ships are there at present. You guess that is where the ships carrying prisoners to Ironclad Island dock.\n\nNo wonder this area was kept so secure.", eDialogPic.STANDARD, 16, ["OK"])
        if StuffDone["13_5"] < 2:
            StuffDone["13_5"] = 0
            return
        return

def NorthwesternStolgrad_2305_MapTrigger_23_22(p):
    if StuffDone["13_5"] < 2:
        StuffDone["13_5"] = 0
        return

def NorthwesternStolgrad_2307_MapTrigger_22_22(p):
    if StuffDone["13_6"] < 1:
        if StuffDone["13_9"] == 0:
            MessageBox("You see a small guard tower off in the distance and make out several figures standing upon it. They immediately begin to pepper you with arrows!")
            StuffDone["13_9"] = 1
            RunScript("GlobalCall_NorthwesternStolgrad_2852", ScriptParameters(eCallOrigin.CUSTOM))
            StuffDone["14_2"] = 1
            ChoiceBox("Off the shore you make out a large fortress on a barren island. You know of that place. It is called Ironclad Island. The foreboding structure houses the most dangerous criminals in the world. Those sentenced there, never come out.\n\nYou turn your attention north along the shore. There you see two stone docks, no ships are there at present. You guess that is where the ships carrying prisoners to Ironclad Island dock.\n\nNo wonder this area was kept so secure.", eDialogPic.STANDARD, 16, ["OK"])
            if StuffDone["13_5"] < 2:
                StuffDone["13_5"] = 0
                return
            return
        RunScript("GlobalCall_NorthwesternStolgrad_2852", ScriptParameters(eCallOrigin.CUSTOM))
        StuffDone["14_2"] = 1
        ChoiceBox("Off the shore you make out a large fortress on a barren island. You know of that place. It is called Ironclad Island. The foreboding structure houses the most dangerous criminals in the world. Those sentenced there, never come out.\n\nYou turn your attention north along the shore. There you see two stone docks, no ships are there at present. You guess that is where the ships carrying prisoners to Ironclad Island dock.\n\nNo wonder this area was kept so secure.", eDialogPic.STANDARD, 16, ["OK"])
        if StuffDone["13_5"] < 2:
            StuffDone["13_5"] = 0
            return
        return

def NorthwesternStolgrad_2311_MapTrigger_7_21(p):
    if StuffDone["14_2"] == 0:
        StuffDone["14_2"] = 1
        ChoiceBox("Off the shore you make out a large fortress on a barren island. You know of that place. It is called Ironclad Island. The foreboding structure houses the most dangerous criminals in the world. Those sentenced there, never come out.\n\nYou turn your attention north along the shore. There you see two stone docks, no ships are there at present. You guess that is where the ships carrying prisoners to Ironclad Island dock.\n\nNo wonder this area was kept so secure.", eDialogPic.STANDARD, 16, ["OK"])
        if StuffDone["13_5"] < 2:
            StuffDone["13_5"] = 0
            return
        return
    if StuffDone["13_5"] < 2:
        StuffDone["13_5"] = 0
        return

def NorthwesternStolgrad_2313_MapTrigger_7_20(p):
    if StuffDone["13_8"] < 1:
        RunScript("GlobalCall_NorthwesternStolgrad_2852", ScriptParameters(eCallOrigin.CUSTOM))
        StuffDone["14_2"] = 1
        ChoiceBox("Off the shore you make out a large fortress on a barren island. You know of that place. It is called Ironclad Island. The foreboding structure houses the most dangerous criminals in the world. Those sentenced there, never come out.\n\nYou turn your attention north along the shore. There you see two stone docks, no ships are there at present. You guess that is where the ships carrying prisoners to Ironclad Island dock.\n\nNo wonder this area was kept so secure.", eDialogPic.STANDARD, 16, ["OK"])
        if StuffDone["13_5"] < 2:
            StuffDone["13_5"] = 0
            return
        return

def NorthwesternStolgrad_2315_MapTrigger_19_24(p):
    if StuffDone["13_5"] < 2:
        if StuffDone["13_6"] == 0:
            StuffDone["13_6"] = 1
            MessageBox("You get close enough to the tower to engage the archers in melee.")
            WorldMap.SpawnNPCGroup("Group_0_0_4", p.Target)
            StuffDone["13_5"] = 0
            return
        return

def NorthwesternStolgrad_2316_MapTrigger_11_27(p):
    if StuffDone["13_5"] < 2:
        if StuffDone["13_7"] == 0:
            StuffDone["13_7"] = 1
            MessageBox("You get close enough to the tower to engage the archers in melee.")
            WorldMap.SpawnNPCGroup("Group_0_0_4", p.Target)
            StuffDone["13_5"] = 0
            return
        return

def NorthwesternStolgrad_2317_MapTrigger_8_17(p):
    if StuffDone["13_5"] < 2:
        if StuffDone["13_8"] == 0:
            StuffDone["13_8"] = 1
            MessageBox("You get close enough to the tower to engage the archers in melee.")
            WorldMap.SpawnNPCGroup("Group_0_0_4", p.Target)
            StuffDone["13_5"] = 0
            return
        return

def NorthwesternStolgrad_2318_MapTrigger_25_36(p):
    if StuffDone["13_5"] < 2:
        ChoiceBox("You approach an Empire fortress. You are stopped by the gate guard who requests to see a pass. \"This area has been restricted by order of her majesty, Auspire.\" Unfortunately, you do not have any such passes.\n\nThis fort was made to withstand an invasion from an army. There is no way a small force such as yourself will make it through alive.", eDialogPic.TERRAIN, 92, ["OK"])
        p.CancelAction = True
        return
    MessageBox("The Empire has reclaimed this fortress from the former rulers of Stolgrad. You can freely pass through.")
    Party.Reposition(Location(25, 31))
    p.CancelAction = True

def NorthwesternStolgrad_2319_MapTrigger_25_32(p):
    if StuffDone["13_5"] < 2:
        result = ChoiceBox("You approach this fortress and the gate guards ask to see identification. You try to bluff your way out of it, but it does not work. \"I\'m sorry, but you are in violation of code. You are in a restricted area. I\'m going to have to place you under arrest.\"\n\nYou obviously cannot allow that to happen. You could try to attack, but you will most likely be vastly outnumbered by the soldiers in the fortress. Of course you could run away.", eDialogPic.CREATURE, 12, ["Attack", "Flee"])
        if result == 0:
            MessageBox("You try to fight your way through this situation. You manage to fight off the first few, but reinforcements quickly come and surround you. You are arrested and beaten to death.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        elif result == 1:
            if StuffDone["14_0"] == 0:
                StuffDone["14_0"] = 1
                Party.Reposition(Location(29, 28))
                p.CancelAction = True
                MessageBox("You make a break for it. Several of the soldiers immediately chase you. You manage to outrun all but the fastest. It looks like you will have to fight those.")
                WorldMap.SpawnNPCGroup("Group_0_0_5", p.Target)
                return
            MessageBox("It was unwise to think you could get away again. This time they were ready for you to try to escape. You are surrounded, and thrown into a cell. The cruel interrogators beat you to death.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        return
    MessageBox("The Empire has reclaimed this fortress from the former rulers of Stolgrad. You can freely pass through.")
    Party.Reposition(Location(25, 37))
    p.CancelAction = True

def NorthwesternStolgrad_2320_MapTrigger_16_16(p):
    if StuffDone["13_5"] < 2:
        if StuffDone["14_1"] == 250:
            return
        StuffDone["14_1"] = 250
        ChoiceBox("As you near the end of this seemingly ordinary tunnel, you get a strange suspicion. This area is just too quiet. You look around and suddenly you hear some rocks fall. You turn to see the figure of a very large reptile.\n\nIt appears to be a kind of miniature dragon, but different. You believe you have been spotted by a Wyvern, a vicious and wild dragon like predator that was known to live in mountains.\n\nEmphasis on the was -- most scholars believe Wyverns to have been extinct for hundreds of years. However, occasional sightings have been recorded, but never verified.\n\nYou are skeptical of those sightings no longer. It is said that Wyverns hunt in packs. That turns out to be true as well. You are now confronted with a small pack of Wyverns!", eDialogPic.CREATURE, 144, ["OK"])
        WorldMap.SpawnNPCGroup("Group_0_0_6", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The earthquake activity has caused this entire area to collapse. You will not be able to proceed any further.")

def NorthwesternStolgrad_2321_SpecialOnWin1(p):
    MessageBox("You manage to fight off the remaining soldiers. It would be unwise to go back there again.")

def NorthwesternStolgrad_2322_SpecialOnFlee1(p):
    MessageBox("You manage to escape the remaining soldiers. It would be unwise to go back there again.")
