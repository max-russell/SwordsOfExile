
def MrrnahHollow_56_MapTrigger_35_31(p):
    MessageBox("Someone was building a road out this way, but construction ended abruptly when the bandit attacks started. Piles of gravel and rusted picks and shovels are littered nearby.\n\nInterestingly, there are fresh tracks nearby. They seem to be leading to the east.")

def MrrnahHollow_57_MapTrigger_11_26(p):
    if StuffDone["201_0"] == 250:
        return
    StuffDone["201_0"] = 250
    WorldMap.DeactivateTrigger(Location(11,74))
    WorldMap.DeactivateTrigger(Location(14,73))
    WorldMap.DeactivateTrigger(Location(15,73))

def MrrnahHollow_58_MapTrigger_14_25(p):
    if StuffDone["201_0"] == 250:
        return
    result = ChoiceBox("One thing you can say about the bandits here - they\'re arrogant. A dozen of them are sitting here, bold and confidant as can be, waiting to shake you down.\n\nAs you approach, they get up from around their cozy campfire and grab their weapons. One of them yells \"Greetings, wanderers! I\'m afraid we must require a small toll of you before you can pass!\"\n\nOne of their mages seems to be preparing a spell as their leader yells \"Only 100 gold to pass! What could be more reasonable? Do you accept, or must we sadly come to blows?\"", eDialogPic.CREATURE, 18, ["Leave", "Pay", "Attack"])
    if result == 1:
        if StuffDone["201_0"] == 250:
            return
        StuffDone["201_0"] = 250
        WorldMap.DeactivateTrigger(Location(11,74))
        WorldMap.DeactivateTrigger(Location(14,73))
        WorldMap.DeactivateTrigger(Location(15,73))
        if Party.Gold >= 100:
            MessageBox("You pay the bandits their 100 gold. They thank you, sheathe their weapons, and disappear into the hills.\n\nAfter a short time, you try to track them, only to find that they\'re experts at concealing all traces of their passages. You can\'t figure out where they disappeared to.")
            Party.Gold -= 100
            return
        MessageBox("When the bandits see that you don\'t have 100 gold, they laugh. \"Oh, well,\" the leader says. \"We can\'t blame you for trying.\" They take what gold you do have and disappear into the hills.\n\nAfter a short time, you try to track them, only to find that they\'re experts at concealing all traces of their passages. You can\'t figure out where they disappeared to.")
        Party.Gold -= 100
        return
    elif result == 2:
        if StuffDone["201_0"] == 250:
            return
        StuffDone["201_0"] = 250
        WorldMap.DeactivateTrigger(Location(11,74))
        WorldMap.DeactivateTrigger(Location(14,73))
        WorldMap.DeactivateTrigger(Location(15,73))
        MessageBox("The bandits clearly would have preferred for you to have just paid them off. Combat is very inconvenient and messy, and makes muscles sore, and there\'s wounds and death and all.\n\nStill, they stoicly accept combat as an occasional part of the job. They approach you to do battle. You have to admire their dedication.")
        WorldMap.SpawnEncounter("Group_0_1_4", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You back away. The bandits yell to you as you leave. \"All right, then. No worries. We\'ll be here when you get back.\"")

def MrrnahHollow_60_MapTrigger_39_20(p):
    MessageBox("There was a big combat here, probably about a month ago. There\'s still some chips of bone and shards of broken weapons. No other signs of what happened, or who did what to whom.")

def MrrnahHollow_61_SpecialOnWin0(p):
    MessageBox("Victory is yours! You search the bandits\' camp, looking for treasure and some evidence of where there hide-out is. Unfortunately, you find neither. They were making some rabbit soup. That\'s all you get from them.")
    Party.Food += 10
