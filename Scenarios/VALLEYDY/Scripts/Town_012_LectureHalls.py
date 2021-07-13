
def LectureHalls_229_MapTrigger_8_2(p):
    if StuffDone["12_0"] == 250:
        return
    StuffDone["12_0"] = 250
    TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(8,2))
    ChoiceBox("Now that you\'ve gotten a look at the creatures populating this level, you have to stop and gawk for a moment. They\'re some of the most bizarre little critters you\'ve ever seen.\n\nThey\'re humanoid shaped, each about 3 feet tall. You can\'t quite tell what they\'re made of. It\'s not regular flesh, but it isn\'t stone or metal or any other recognizable material either. It\'s flexible and waxy, and looks seriously tough.\n\nThey\'re fast moving and muscular and have nasty, sharp looking teeth and claws. And, as usual, they seem to regard you less as potential friends and more as potential food.", eDialogPic.CREATURE, 154, ["OK"])

def LectureHalls_230_MapTrigger_1_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(28,45)
    Party.MoveToMap(TownMap.List["StudentQuarters_11"])

def LectureHalls_232_MapTrigger_1_4(p):
    if StuffDone["12_2"] == 250:
        return
    StuffDone["12_2"] = 250
    TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(1,4))
    TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(2,4))
    ChoiceBox("This floor contained the lecture halls for the School. This is where the bulk of the instruction, examination, and study of theory took place.\n\nIn the absence of the School\'s masters, however, something bizarre has happened. Someone or something has been rebuilding this level. The walls have been torn down, and rebuilt into strange, lumpy, rounded tunnels and domes.\n\nThe structures wind and penetrate their way through the wreckage of the lecture halls like strange stone tumors. From inside, you hear the scratching of unseen creatures, tunneling and working.", eDialogPic.TERRAIN, 95, ["OK"])

def LectureHalls_234_MapTrigger_3_10(p):
    MessageBox("Once upon a time, someone ransacked this bookshelf pretty thoroughly. Whatever was here before, there\'s little left of interest now.")

def LectureHalls_235_MapTrigger_1_10(p):
    MessageBox("You find, much to your disappointment, that someone has burned up most of the stuff in this desk. You search through the ashes and find a scrap of paper which escaped the fire. it reads:\n\n\"Vinnia wants to meet with us. Does not bode well. Fortunately, the tools are in place. If the disaster does occurs, it will still be possible to undo ...\" That\'s all there is.")

def LectureHalls_236_MapTrigger_39_39(p):
    if StuffDone["12_3"] == 250:
        return
    StuffDone["12_3"] = 250
    TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(39,39))
    MessageBox("You step inside the strange, short creatures\' warren. The tunnels are low and winding, but if you hunch, you can manage to work your way inside.\n\nThe tunnels are dark and filled with a strange, musky smell. The sounds of the hivelings\' labors echo their way to you.")

def LectureHalls_237_MapTrigger_36_14(p):
    if StuffDone["12_4"] == 250:
        return
    result = ChoiceBox("The floor of this room is covered with neat rows of carefully arranged round, gray stones. At first, you thing that this is some sort of weird creature conceptual art. Then you realize that the things aren\'t rocks. They\'re eggs!\n\nThis is a fascinating insight into the biology of these critters, but not terribly useful. That is, unless you destroy them. Do you?", eDialogPic.CREATURE, 154, ["Leave", "Destroy"])
    if result == 1:
        StuffDone["12_4"] = 250
        TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(36,14))
        MessageBox("You draw a weapon and start smashing the proto-hivelings. Unfortunately, it does about as much good as smacking large chunks of rock. None at all. You quit before you break your weapons.")
        return

def LectureHalls_238_MapTrigger_5_46(p):
    if StuffDone["12_5"] == 250:
        return
    result = ChoiceBox("On the blackboard of this lecture hall, you notice that whoever was lecturing left the class notes on the board. At least, that\'s what the rather business-like runes and glyphs on the blackboard look like.\n\nTo find out more, you\'ll need to spend some time reading them.", eDialogPic.TERRAIN, 170, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("You start reading the runes and realize that they aren\'t instructions for casting a spell. They are a spell, like a scroll but written on the wall! You try to stop reading, but can\'t. Instead, you start to read faster, and then out loud.\n\nThe only reason you can think of that someone would create something like this would be to punish intruders. Clearly, someone wanted to seriously harm anyone who made it down this far. Whatever the reason, you now have to deal with more pressing issues.", eDialogPic.CREATURE, 72, ["OK"])
        if StuffDone["12_5"] == 250:
            return
        StuffDone["12_5"] = 250
        TownMap.List["LectureHalls_12"].AlterTerrain(Location(5,46), 1, None)
        TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(5,46))
        Town.PlaceEncounterGroup(1)
        return

def LectureHalls_239_MapTrigger_5_35(p):
    if StuffDone["12_6"] == 250:
        return
    StuffDone["12_6"] = 250
    TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(5,35))
    MessageBox("One amazing thing about the hivelings is their single-mindedness. Everything to the north of this door has been destroyed, but everything to the south is completely untouched. They\'re concerned with construction and little else.")

def LectureHalls_240_MapTrigger_30_25(p):
    if StuffDone["12_7"] == 250:
        return
    StuffDone["12_7"] = 250
    TownMap.List["LectureHalls_12"].DeactivateTrigger(Location(30,25))
    MessageBox("This bookshelf contains a green book titled \"Wisdom of the School.\" You flip through it. It\'s a textbook. The ink on the pages has ran and the few pages you can read aren\'t too interesting. Still, you can take it if you wish.")

def LectureHalls_241_MapTrigger_1_30(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(1,2)
    Party.MoveToMap(TownMap.List["ExperimentHalls_14"])
