
def DarkMaze_619_MapTrigger_36_20(p):
    if StuffDone["208_1"] == 250:
        return
    result = ChoiceBox("You start to enter this large cavern and immediately back away. It\'s filled with snakes! And not just small snakes either, but huge ones, fifteen feet long, with massive fangs dripping poison.\n\nIf you entered, they might let you by unharmed. But probably not.", eDialogPic.CREATURE, 84, ["Leave", "Enter"])
    if result == 1:
        StuffDone["208_1"] = 250
        WorldMap.DeactivateTrigger(Location(36,404))
        WorldMap.DeactivateTrigger(Location(41,404))
        MessageBox("Sure enough, the moment you enter the cavern, the snakes rise up as one and start slithering towards you. The synchronized behavior is bizarre, until you notice that several of the snakes are unusually large. And have human heads.")
        WorldMap.SpawnEncounter("Group_0_8_4", p.Target)
        return
    p.CancelAction = True

def DarkMaze_621_MapTrigger_41_34(p):
    if StuffDone["208_3"] == 250:
        return
    StuffDone["208_3"] = 250
    WorldMap.DeactivateTrigger(Location(41,418))
    MessageBox("You notice an unusually large number of shedded lizard scales on the ground.")

def DarkMaze_622_MapTrigger_38_29(p):
    if StuffDone["208_2"] == 250:
        return
    StuffDone["208_2"] = 250
    WorldMap.DeactivateTrigger(Location(38,413))
    MessageBox("Ahead of you, you see several lizards peek their heads around the corner. Then you realize that there\'s not several lizards there, but, in fact, only a few. They just have a lot of heads each.")
    WorldMap.SpawnEncounter("Group_0_8_5", p.Target)

def DarkMaze_623_MapTrigger_31_29(p):
    if StuffDone["208_4"] == 250:
        return
    StuffDone["208_4"] = 250
    WorldMap.DeactivateTrigger(Location(31,413))
    MessageBox("You feel a slight draft. It\'s not moist and cool, as expected. Instead, it\'s warm, and there is a hint of sulphur in the air. As you look around to see where the sulphur came from, you hear a roar. There are hydras nearby.\n\nYou try to avoid them, but their many heads give the creatures an acute sense of smell. They soon find you.")
    WorldMap.SpawnEncounter("Group_0_8_6", p.Target)

def DarkMaze_624_MapTrigger_12_32(p):
    if StuffDone["208_0"] == 250:
        return
    StuffDone["208_0"] = 250
    WorldMap.DeactivateTrigger(Location(12,416))
    ChoiceBox("You stand at the entrance to a maze of twisty, winding passages, all alike.\n\nThe tunnels are unusually narrow and winding, even for Exile. The glowing roof fungus is very sparse, and the floor is very uneven. These tunnels will probably be difficult to navigate.", eDialogPic.STANDARD, 8, ["OK"])

def DarkMaze_625_MapTrigger_42_3(p):
    if StuffDone["208_5"] == 250:
        return
    result = ChoiceBox("Exile has many thousands of small, natural pools and springs. Many of those are thought to have magical properties.\n\nFew, however, flaunt their magical nature are much as this tiny pool. The water has many small chips of mica suspended in it, which flicker and catch the light, and the air around the pool has the pronounced smell of mint.\n\nThese pools are often beneficial. Sometimes, however, they aren\'t.", eDialogPic.STANDARD, 18, ["Leave", "Drink"])
    if result == 1:
        StuffDone["208_5"] = 250
        WorldMap.AlterTerrain(Location(42,387), 1, None)
        WorldMap.DeactivateTrigger(Location(42,387))
        MessageBox("You take deep swigs of the water. It makes you feel pleasantly energized. Even in the middle of this dark, alarming maze, you manage to feel somewhat relaxed.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 3))
        for pc in Party.EachAlivePC():
            pc.SP+= 100
        return

def DarkMaze_626_SpecialOnWin0(p):
    MessageBox("The serpents didn\'t have much in the way of useful treasure. You are, fortunately, able to tap some nice weapon poison from their massive fangs.")
    Party.GiveNewItem("KillerPoison_175")
