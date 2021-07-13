
def _RuinsofWhitstone_322_MapTrigger_33_20(p):
    if StuffDone["14_3"] == 250:
        return
    result = ChoiceBox("This was once a place devoted to goodness. Blood stains on the tablecloth of the altar warn you that this is so no longer. An inhuman skull with long fangs rests on the altar next to a golden statuette, clearly valuable. do you dare to loot?", eDialogPic.TERRAIN, 137, ["Take", "Leave"])
    if result == 0:
        StuffDone["14_3"] = 250
        TownMap.List["_RuinsofWhitstone_14"].AlterTerrain(Location(33,20), 1, None)
        TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(33,20))
        Party.Gold += 200
        MessageBox("You reach out and snatch the statuette away from the skull, prepared for anything. Nothing happens. What kind of evil resides here, that allows you to rob its temple without vengeance? You shudder in apprehension.")
        return
    return

def _RuinsofWhitstone_323_MapTrigger_44_23(p):
    MessageBox("These are public records, ending with the disaster that struck ten years ago. \"River water is rising above the level of the town, drowning houses one by one. We must abandon the town, I realize that. But where can we go?\n\n\"A third of our townspeople, including our just lord White, were killed in the cave-in, the rest are famished, cold and drained. The soldiers from Myldres that brought food and help are becoming ever more arrogant and demanding. They are our masters now.\"")

def _RuinsofWhitstone_324_MapTrigger_9_23(p):
    if StuffDone["14_0"] >= 1:
        MessageBox("You are allowed into the corridor leading down into the marble works.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You start down the mine shaft, but bump off a wall. You look again, but see nothing. You stretch out a hand, and it passes the barrier. But as you try to enter the shaft, you are flung back again. A powerful, psychic force is behind this.")

def _RuinsofWhitstone_326_MapTrigger_26_55(p):
    if StuffDone["14_1"] == 250:
        return
    StuffDone["14_1"] = 250
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(26,55))
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(27,55))
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(28,55))
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(25,55))
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(24,55))
    ChoiceBox("Passing through the halls of the marble citadel, you notice how clean and well kept everything still is. Why isn?t the castle falling apart like all the other buildings?\n\nYour sense of unease grows as you enter the throne room. Torches are burning, and two canary birds sit on a statue, singing merrily. The first living sounds you have heard in ages, it seems.\n\nWhen you look away, there is a man on the throne. You startle, and reach for your weapons, but the man appears not to see you. He sits in deep thought, twining his fingers through greying beard, humming absently in tune with the birds.\n\nSuddenly, there is a sound of clashing steel, screaming and running feet. You turn around, and see a gaunt man in long robes enter. Lord White rises from his throne as the visitor laughs, revealing pointed teeth. He raises his hand and snaps.\n\nThe ground trembles, throwing you and the Lord off your feet. The ceiling explodes as a boulder crushes the wall, trapping the throne and Lord White under it. The gaunt man laughs again, leaving without looking back.\n\nYou get to your feet, wondering how much of this apparition is real and what is in your minds. One thing seems certain. You are no longer alone in the town. The darkness resounds with all the noises you missed earlier.", eDialogPic.CREATURE, 131, ["OK"])
    for x in range(22, 30):
        for y in range(56, 60):
            if Maths.Rand(1,0,100) <= 75:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
    for x in range(25, 28):
        for y in range(57, 60):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[5])
    if StuffDone["14_0"] == 250:
        return
    StuffDone["14_0"] = 250
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(9,23))
    TownMap.List["_RuinsofWhitstone_14"].DeactivateTrigger(Location(9,24))
    Town.PlaceEncounterGroup(1)
    Animation_Hold(-1, 011_3booms)
    Wait()

def _RuinsofWhitstone_327_MapTrigger_5_23(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(57,7)
    Party.MoveToMap(TownMap.List["BelowWhitstone_16"])

def _RuinsofWhitstone_333_TownTimer_5(p):
    if StuffDone["14_2"] == 250:
        return
    StuffDone["14_2"] = 250
    MessageBox("The town is eerily quiet. Chimney folklore is full of stories of Whitstone, the haunted town. You had expected to meet a skeleton or two, at least. But you see no movement, hear no sounds. That is even more frightening, somehow.")

def _RuinsofWhitstone_334_OnEntry(p):
    if not Town.Abandoned:
        if StuffDone["14_4"] == 250:
            return
        StuffDone["14_4"] = 250
        MessageBox("Much of Whitstone was destroyed when the cave ceiling fell in ten years ago. The rest of the town drowned. The same cave-in blocked the course of the river, causing it to rise and create a shallow lake. That caused the end of the prosperous town.\n\nToday, only the buildings on top of the hill remain. To the south, you can see the great marble citadel of House White, once the mightiest lords of Chimney. Their palace is falling apart and looks rather grim.")
        Timer(Town, 40, False, "_UNKNOWN_", eTimerType.DELETE)
