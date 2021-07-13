
def AbandonedOutpost_141_MapTrigger_6_25(p):
    if StuffDone["10_0"] == 250:
        return
    StuffDone["10_0"] = 250
    TownMap.List["AbandonedOutpost_10"].DeactivateTrigger(Location(6,25))
    ChoiceBox("On the other side of the door, you find a table. A note has been left on it. Looks harmless enough. You pick it up and read it.\n\n\"To our brave comrades in arms - well done. The distraction you provided enabled us to carry out our boldest strike against our oppressors yet. Lord Volpe is dead! His palace is in ruins. The opportunities before us are considerable.\"\n\n\"You are in one of our secret hideouts, now abandoned. We suggest you flee the island as soon as possible. This place will be found by the Empire soon, so don\'t linger.\"\n\n\"A small reward is in the chest in the corner. Don\'t poke around this hideout for other goodies ... it\'s been trapped. Get out of here. Go instead to meet your next contact. Her name is Luna, and she is in the city of Buzzard.\n\n\"We\'ll make sure you\'re allowed to get there. Well done. Some of us had our doubts, but you seem trustworthy. - Canizares.\" You memorize the note, and tear it up.", eDialogPic.TERRAIN, 149, ["OK"])
    SpecialItem.Give("LunaNote")
    StuffDone["5_4"] = 1
    MessageBox("Congratulations! For better or worse, you survived the second mission.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(30)

def AbandonedOutpost_142_MapTrigger_2_29(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("If, for some bizarre reason you wanted to go back down into the sewers, the stairway is here.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(36,61)
    Party.MoveToMap(TownMap.List["ZaskivaSewers_9"])

def AbandonedOutpost_143_MapTrigger_9_21(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,20)).Num == 154:
        ChoiceBox("When you step into this alcove, the north wall slides smoothly into the floor. You look out into the Hill Runner hideout. It looks like they stripped the place pretty clean. Even some of the chairs were taken away.\n\nUnfortunately, you weren\'t able to get here fast enough. The Empire troops, enraged by the assassination of Lord Volpe, have already located this place.\n\nWhen they see you, they are relieved. Their investigation might net some victims after all. They draw their swords, and advance. Trying to explain anything about who you are does no good - these soldiers want blood, and nothing else.", eDialogPic.CREATURE, 15, ["OK"])
        Town.AlterTerrain(Location(9,20), 0, TerrainRecord.UnderlayList[170])
        StuffDone["10_2"] = 1
        return

def AbandonedOutpost_144_MapTrigger_13_6(p):
    MessageBox("Unfortunately, the note wasn\'t lying when it said this place was booby trapped. The Hill Runners don\'t take half measures, either. One of their explosive devices was placed inside this chest, and went off before you even got near it.\n\nThe whole hideout caves in. You\'re crushed beyond recognition. Ouch.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def AbandonedOutpost_145_MapTrigger_18_12(p):
    result = ChoiceBox("After that long, nightmarish hike through the sewers, you can\'t think of anything you\'d like more than a nice, long nap. These beds, while slightly dusty, look plenty comfortable.", eDialogPic.TERRAIN, 143, ["Leave", "Rest"])
    if result == 1:
        MessageBox("Oops. Looks like those soldiers you killed were just the advance party. A whole battalion arrives soon after you go to sleep, to find out what happened to their troops.\n\nWhen they find you here, in the room next to their bodies, they seize you and start interrogating you. They\'re still punching you when one of the soldiers trips a booby trap and caves the whole place in.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def AbandonedOutpost_146_MapTrigger_10_6(p):
    if StuffDone["10_1"] == 250:
        return
    StuffDone["10_1"] = 250
    TownMap.List["AbandonedOutpost_10"].DeactivateTrigger(Location(10,6))
    MessageBox("That\'s odd. The rebels were incredibly thorough in stripping this place clean, and yet, in this secret room, they left a closed chest behind. Very odd indeed.")

def AbandonedOutpost_147_MapTrigger_6_28(p):
    if StuffDone["10_2"] >= 1:
        Town.AlterTerrain(Location(9,20), 0, TerrainRecord.UnderlayList[170])
        return

def AbandonedOutpost_148_ExitTown(p):
    if p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(30, 7),WorldMap.SectorAt(Party.OutsidePos))
    if p.Dir.IsEast:
        MessageBox("You leave the abandoned outpost just in time. When you get a half mile away, you look back, and see a whole battalion of Empire troops filing in to investigate.\n\nSoon after, there is an explosion, so massive you can even feel it where you\'re standing. With a mighty cloud of dust, the outpost caves in. Yet another pile of bodies in this insane war.")
