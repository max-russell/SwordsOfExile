
def Outskirts_575_MapTrigger_28_21(p):
    if StuffDone["132_1"] == 250:
        return
    StuffDone["132_1"] = 250
    WorldMap.DeactivateTrigger(Location(172,117))
    MessageBox("This narrow entrance is covered with bones and filth. Whatever lives here isn?t too concerned with the appearance of its front yard.")

def Outskirts_576_MapTrigger_27_12(p):
    if StuffDone["132_0"] >= 1:
        return
    result = ChoiceBox("You stand at the entrance to a smelly cave, blackened by fire and disfigured by claw marks. Whatever lives here does not want your company. Nor should you want to visit. Unless of course you are driven by avarice and blood lust.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        MessageBox("You step into the cave and nearly retch at the sulfurous gases you inhale. But you are determined to drive out this monster. You enter the main cavern and at first see nothing. Then you hear a frightening roar, and look down at the ground. Oh no!")
        WorldMap.SpawnNPCGroup("Group_3_2_4", p.Target)
        return

def Outskirts_577_SpecialOnWin0(p):
    if StuffDone["132_0"] == 250:
        return
    StuffDone["132_0"] = 250
    WorldMap.AlterTerrain(Location(171,108), 1, None)
    WorldMap.DeactivateTrigger(Location(171,108))
    MessageBox("You look quickly through the cave, eager to get out. What interests you most is how much damage the Chicken Drake took before it gave in. You tear loose some of its feathers. They feel strong as steel. You decide to bring a few, as a souvenir.")
    Party.GiveNewItem("DrakeFeathers_396")
    Party.Gold += 100
