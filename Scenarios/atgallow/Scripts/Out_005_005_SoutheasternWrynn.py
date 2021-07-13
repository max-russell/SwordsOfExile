
def SoutheasternWrynn_2798_MapTrigger_12_20(p):
    ChoiceBox("This is a fair sized community of woodcutters. In one department are the lumberjacks who go out and do the actual cutting of trees and hauling them into the sawmill.\n\nAt the sawmill, the trees are cut up into fine boards or as specified. This is done by machines built by mages. The waste, such as the sawdust and unusable cuts are done away with into the ocean.\n\nThe boards are then moved to the woodcarvers who with the aid of machines, cut the wood into smaller pieces. Those pieces are then assembled into objects such as chairs, tables, beds, desks, bookshelves, etc.\n\nSome of the wood is pulped and processed into paper. Heavy rollers driven by magical means press the pulp against a heated surface and turn it into heavy rolls of paper. The paper is then cut into pieces as needed.\n\nAfter they are assembled into the finished product, they are distributed all over the continent via portals for long distances, carts within the Wrynn sector, and placed onto ships to be carried to other continents.\n\nLast, but not least, is the department of planters who plant new magically enhanced trees to replenish the forests. The Empire has quite an efficient operation going here.", eDialogPic.TERRAIN, 149, ["OK"])

def SoutheasternWrynn_2799_MapTrigger_29_19(p):
    if StuffDone["35_9"] == 0:
        result = ChoiceBox("You approach a toll booth. A large metal gate has the bridge blocked off. The soldier behind the gate explains, \"There is a toll of 5 gold per crossing for everyone except those with a special pass.\n\nIf you are planning to use this bridge often, may I suggest you purchase one. It is only 100 gold and will offer you unlimited access to this bridge. Sorry guys, even soldiers have to pay. It\'s the rules, stupid ones, but still those the rules.\"\n\n(Pay = 5 gold to cross bridge.  Buy = Purchase pass for 100 gold for unlimited access)", eDialogPic.TERRAIN, 65, ["Leave", "Buy", "Pay"])
        if result == 1:
            if Party.Gold >= 100:
                Party.Gold -= 100
                StuffDone["35_9"] = 1
                MessageBox("You decide to purchase the pass. He produces a blue piece of paper and signs it, and places a seal on it. \"Just present this pass and you will be allowed to cross the bridge whenever you want.\"\n\nYou present the pass, the soldier opens the gate and you cross.")
                Party.Reposition(Location(269, 263))
                p.CancelAction = True
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You do not have the gold. \"Sorry guys, I have to enforce the rules. Can\'t let you pass until you secure the funds.\"")
            return
        elif result == 2:
            if Party.Gold >= 5:
                Party.Gold -= 5
                MessageBox("You hand him the gold and he opens the gate for you. You cross the bridge.")
                Party.Reposition(Location(269, 263))
                p.CancelAction = True
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You do not have the gold. \"Sorry guys, I have to enforce the rules. Can\'t let you pass until you secure the funds.\"")
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You do not have the gold. \"Sorry guys, I have to enforce the rules. Can\'t let you pass until you secure the funds.\"")
        return
    MessageBox("You present the pass, the soldier opens the gate and you cross.")
    Party.Reposition(Location(269, 263))
    p.CancelAction = True

def SoutheasternWrynn_2800_MapTrigger_29_22(p):
    if StuffDone["35_9"] == 0:
        result = ChoiceBox("You approach a toll booth. A large metal gate has the bridge blocked off. The soldier behind the gate explains, \"There is a toll of 5 gold per crossing for everyone except those with a special pass.\n\nIf you are planning to use this bridge often, may I suggest you purchase one. It is only 100 gold and will offer you unlimited access to this bridge. Sorry guys, even soldiers have to pay. It\'s the rules, stupid ones, but still those the rules.\"\n\n(Pay = 5 gold to cross bridge.  Buy = Purchase pass for 100 gold for unlimited access)", eDialogPic.TERRAIN, 65, ["Leave", "Buy", "Pay"])
        if result == 1:
            if Party.Gold >= 100:
                Party.Gold -= 100
                StuffDone["35_9"] = 1
                MessageBox("You decide to purchase the pass. He produces a blue piece of paper and signs it, and places a seal on it. \"Just present this pass and you will be allowed to cross the bridge whenever you want.\"\n\nYou present the pass, the soldier opens the gate and you cross.")
                Party.Reposition(Location(269, 258))
                p.CancelAction = True
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You do not have the gold. \"Sorry guys, I have to enforce the rules. Can\'t let you pass until you secure the funds.\"")
            return
        elif result == 2:
            if Party.Gold >= 5:
                Party.Gold -= 5
                MessageBox("You hand him the gold and he opens the gate for you. You cross the bridge.")
                Party.Reposition(Location(269, 258))
                p.CancelAction = True
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You do not have the gold. \"Sorry guys, I have to enforce the rules. Can\'t let you pass until you secure the funds.\"")
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You do not have the gold. \"Sorry guys, I have to enforce the rules. Can\'t let you pass until you secure the funds.\"")
        return
    MessageBox("You present the pass, the soldier opens the gate and you cross.")
    Party.Reposition(Location(269, 258))
    p.CancelAction = True

def SoutheasternWrynn_2801_MapTrigger_42_16(p):
    ChoiceBox("This is a fairly small community that is heavy into the fishing industry. The air is not that pleasant. It reeks with the smell of rotting fish! Docked at the piers are several large ships armed with massive magically strengthened nets.\n\nThe docked ships are being attended to by their respective sailors who repair the damages done during the last voyage. One of the recently docked ships is unloading its cargo of fish -- thousands of them!\n\nThese fish are processed within the town and are distributed throughout the Empire via teleporters. If you\'ve ever wondered where your fish dinner came from, this is likely the place.", eDialogPic.STANDARD, 16, ["OK"])

def SoutheasternWrynn_2802_MapTrigger_10_5(p):
    if StuffDone["36_7"] == 250:
        return
    StuffDone["36_7"] = 250
    WorldMap.DeactivateTrigger(Location(250,245))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Uh oh! You have just come across a heard of gray unicorns. Such are the most common variety of unicorn and are the most wild and vicious! Also, they are quite intelligent as far as animals go.\n\nThey don\'t look to happy that you\'ve intruded. They charge you!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_5_4", p.Target)

def SoutheasternWrynn_2803_MapTrigger_30_4(p):
    if StuffDone["36_8"] == 250:
        return
    StuffDone["36_8"] = 250
    WorldMap.DeactivateTrigger(Location(270,244))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Uh oh! You have just come across a heard of gray unicorns. Such are the most common variety of unicorn and are the most wild and vicious! Also, they are quite intelligent as far as animals go.\n\nThey don\'t look to happy that you\'ve intruded. They charge you!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_5_4", p.Target)

def SoutheasternWrynn_2804_MapTrigger_6_20(p):
    if StuffDone["36_9"] == 250:
        return
    StuffDone["36_9"] = 250
    WorldMap.DeactivateTrigger(Location(246,260))
    Animation_Hold(-1, 084_neigh)
    Wait()
    ChoiceBox("Uh oh! You have just come across a heard of gray unicorns. Such are the most common variety of unicorn and are the most wild and vicious! Also, they are quite intelligent as far as animals go.\n\nThey don\'t look to happy that you\'ve intruded. They charge you!", eDialogPic.CREATURE, 128, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_5_4", p.Target)

def SoutheasternWrynn_2805_WanderingOnMeet2(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
