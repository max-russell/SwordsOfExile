
def ZaKhaziRunNorth_545_MapTrigger_37_31(p):
    if StuffDone["201_0"] == 250:
        return
    StuffDone["201_0"] = 250
    WorldMap.DeactivateTrigger(Location(37,79))
    ChoiceBox("You were starting to take free passage down this river a little bit for granted. Sure, there were rapids and falls, but no places where creatures were actually preventing you from passing. Until now.\n\nA fortress has been built here, spanning a narrow region of the river. The river passes underneath. You can take your boat inside, but you can\'t be sure they will let you pass.\n\nYou look up onto the ramparts of the fort, and see several troglodytes pacing back and forth on patrol. When they spot you, they laugh and make certain hand gestures. So much for a warm welcome.", eDialogPic.TERRAIN, 187, ["OK"])

def ZaKhaziRunNorth_546_MapTrigger_37_27(p):
    if StuffDone["201_1"] == 250:
        return
    StuffDone["201_1"] = 250
    WorldMap.DeactivateTrigger(Location(37,75))
    MessageBox("With great relief, you row away from the troglodyte\'s fortress. The river carries you into a large, tranquil lake. By now, you must finally be near the end of the Za-Khazi Run.")

def ZaKhaziRunNorth_547_MapTrigger_29_6(p):
    if StuffDone["201_2"] == 250:
        return
    StuffDone["201_2"] = 250
    WorldMap.DeactivateTrigger(Location(29,54))
    MessageBox("Your period of speedy progress was all too brief, and has come to an end. The river has become very rocky and treacherous. You may not be able to navigate it safely for much longer.\n\nUp on the hills to the north of the river, you see a  massive granite fortress. At first, you think it might be Fort Cavalier. No such luck. Nobody mans the battlements, and nobody in Exile has ever made a structure that dark and grim.")

def ZaKhaziRunNorth_548_MapTrigger_6_8(p):
    if StuffDone["201_3"] == 250:
        return
    StuffDone["201_3"] = 250
    WorldMap.DeactivateTrigger(Location(6,56))
    MessageBox("Going any farther west would only mean a quick death on the rapids. You pole the barge backward quickly, before you get caught in the flow and smashed to bits.")

def ZaKhaziRunNorth_549_MapTrigger_34_29(p):
    if StuffDone["201_4"] == 250:
        return
    StuffDone["201_4"] = 250
    WorldMap.DeactivateTrigger(Location(34,77))
    MessageBox("To the east, you can see a narrow path. It leads around a large forest of stalagmites and into a fort. The fort is built over a narrow part of the river, blocking it.")

def ZaKhaziRunNorth_550_MapTrigger_17_46(p):
    if StuffDone["201_5"] == 250:
        return
    StuffDone["201_5"] = 250
    WorldMap.DeactivateTrigger(Location(17,94))
    WorldMap.DeactivateTrigger(Location(18,94))
    MessageBox("These tunnels are very similar to the tunnels you\'ve been wandering through for the last few days. There\'s only one big difference. The walls, floors, and even the ceiling are covered with a thin layer of slime.\n\nIt must have taken years to cover all these miles of tunnels with slime, top to bottom. These passages must have all kinds of icky creatures in them.")

def ZaKhaziRunNorth_552_MapTrigger_26_10(p):
    result = ChoiceBox("At the lowest point of this long passage, you find a veritable sea of slime. It\'s a fifty foot wide pool of mucous-like substance, green and ten feet deep.\n\nWrithing around in the sea are many huge wyrms. Bigger than huge. Immense. Fifty feet long each. They wiggle around in the slime, occasionally rearing up to grab a bat, lizard, or smaller wyrm.\n\nThey seem unaware of your presence. Of course, you could pick a fight.", eDialogPic.CREATURE2x2, 1, ["Leave", "Attack"])
    if result == 1:
        MessageBox("You walk up to one of the closer creatures and start hitting it. It screeches in alarm, and soon you have all of the things on top of you ...")
        WorldMap.SpawnEncounter("Group_0_1_4", p.Target)
        return

def ZaKhaziRunNorth_553_SpecialOnWin0(p):
    MessageBox("You\'re covered with blood and muck, and every muscle in your bodies is sore. The last of the creatures is dead. Victory is yours.\n\nAt first, you think that none of them have any treasure. Then you figure, since you\'re covered with muck anyway, you might as well look in their stomachs. Sure enough, you find a wicked, curved blade, still in the sheathe, inside one of the wyrms.")
    Party.GiveNewItem("AlienBlade_342")
