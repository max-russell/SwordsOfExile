
def SouthwesternWrynn_2787_MapTrigger_23_42(p):
    if StuffDone["34_8"] == 250:
        return
    StuffDone["34_8"] = 250
    WorldMap.DeactivateTrigger(Location(215,282))
    MessageBox("Oh dear! Nephilim were hiding in the mountains and charge toward you. Their intentions don\'t look too friendly. You have no choice but to fight them!")
    WorldMap.SpawnNPCGroup("Group_4_5_4", p.Target)

def SouthwesternWrynn_2788_MapTrigger_21_3(p):
    MessageBox("You approach a collection of Druid huts. One of them speaks to you, \"Good day visitors. We help maintain the Communal Patches. You are welcome to take what you need. Please, do not abuse the privilege.\"")

def SouthwesternWrynn_2789_MapTrigger_19_2(p):
    if StuffDone["110_0"] == 0:
        result = ChoiceBox("This is the communal patch of Holly. You are invited to pick some.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You pick some of the ingredient. When you feel you\'ve taken enough you stop. There is no need to overextend the Druids\' generosity.")
            Party.GiveNewItem("Holly_363")
            RunScript("ScenarioTimer_x_2821", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("You don\'t think the druids would like it much if you picked any more right now. You should wait a few days and come back when more has grown.")

def SouthwesternWrynn_2790_MapTrigger_19_5(p):
    if StuffDone["111_0"] == 0:
        result = ChoiceBox("This is the communal patch of Comfrey Root. You are invited to pick some.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You pick some of the ingredient. When you feel you\'ve taken enough you stop. There is no need to overextend the Druids\' generosity.")
            Party.GiveNewItem("ComfreyRoot_364")
            RunScript("ScenarioTimer_x_2822", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("You don\'t think the druids would like it much if you picked any more right now. You should wait a few days and come back when more has grown.")

def SouthwesternWrynn_2791_MapTrigger_25_7(p):
    if StuffDone["112_0"] == 0:
        result = ChoiceBox("This is the communal patch of Glowing Nettle. You are invited to pick some.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You pick some of the ingredient. When you feel you\'ve taken enough you stop. There is no need to overextend the Druids\' generosity.")
            Party.GiveNewItem("GlowingNettle_365")
            RunScript("ScenarioTimer_x_2823", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("You don\'t think the druids would like it much if you picked any more right now. You should wait a few days and come back when more has grown.")

def SouthwesternWrynn_2792_MapTrigger_22_5(p):
    if StuffDone["113_0"] == 0:
        result = ChoiceBox("This is the communal patch of Wormgrass. You are invited to pick some.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You pick some of the ingredient. When you feel you\'ve taken enough you stop. There is no need to overextend the Druids\' generosity.")
            Party.GiveNewItem("Wormgrass_366")
            RunScript("ScenarioTimer_x_2824", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("You don\'t think the druids would like it much if you picked any more right now. You should wait a few days and come back when more has grown.")

def SouthwesternWrynn_2793_MapTrigger_40_28(p):
    if StuffDone["37_0"] == 0:
        if Party.HasTrait(Trait.Woodsman):
            result = ChoiceBox("Your skill of woodsman allows you to detect several Nephilim hiding in the trees. Most likely, they are waiting to ambush the next passerby which could easily have been you.\n\nNow that you know about the upcoming ambush, you can easily turn this toward your advantage and get the first strike.", eDialogPic.CREATURE, 39, ["Flee", "Attack"])
            if result == 0:
                p.CancelAction = True
                return
            elif result == 1:
                StuffDone["37_0"] = 1
                MessageBox("You launch the first strike upon the Nephil. They recover surprisingly well and now you are at even footing.")
                WorldMap.SpawnNPCGroup("Group_4_5_5", p.Target)
                return
            return
        Party.Damage(Maths.Rand(4, 1, 5) + 10, eDamageType.WEAPON)
        Wait()
        StuffDone["37_0"] = 1
        MessageBox("This is not your lucky day. Some hostile Nephilim have decided to set up an ambush on this road. Unfortunately, you just happen to be the ones who passed through it. They pepper you with arrows, rocks, and spells, before they move out to finish you.")
        return

def SouthwesternWrynn_2794_WanderingOnMeet1(p):
    MessageBox("A small group of Nephilim, mostly comprised of archers, is nearby. Considering they make no hostile actions, you believe it is simply a patrol. However, then they fire a volley of arrows at you! Looks like you will have to fight back.")
    Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.WEAPON)
    Wait()

def SouthwesternWrynn_2795_WanderingOnMeet2(p):
    p.CancelAction = True
    MessageBox("You are approached by a small patrol of Nephilim. After a short friendly exchange one of them warns, \"There be bandits of our kind in this area posing as patrols, so keep your whiskers in the air!\" They quickly depart.")

def SouthwesternWrynn_2796_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def SouthwesternWrynn_2797_SpecialOnWin1(p):
    MessageBox("With the Nephil Bandits beaten, you check their hiding places and discover the loot they had extracted from other travelers. It\'s not all that much, but it\'s a nice bonus.")
    Party.Gold += 250
