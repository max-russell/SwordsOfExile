
def FortCavalier_508_MapTrigger_24_39(p):
    if StuffDone["21_1"] == 250:
        return
    StuffDone["21_1"] = 250
    TownMap.List["FortCavalier_21"].DeactivateTrigger(Location(24,39))
    ChoiceBox("When you enter Fort Cavalier, Commander Malak, leader of the besieged fortress, immediately runs up, greets you, and relieves you of your bundle of wands. The straps around the wands obligingly snap open, and the wands are passed around.\n\nAs Commander Malak shouts \"Fire them carefully! There won\'t be any more!\" three of them are taken up to the ramparts.\n\nAs the sliths below pepper the walls with javelins, the guards return fire. From beyond the wall, you hear the screams of surprised sliths and massive firestorms and shockstorms rain down, causing major casualties and breaking their momentum.\n\nSoon, the battle is over. The sliths flee to regroup, and the guards cheer. For the first time in weeks, Fort Cavalier gets a respite.\n\nA guard eventually approaches you and says \"Commander Malak would like to see you in his quarters, when you have the time.\"", eDialogPic.STANDARD, 31, ["OK"])
    Town.AlterTerrain(Location(24,41), 0, TerrainRecord.UnderlayList[0])
    StuffDone["100_3"] = 1
    SpecialItem.Take("BundleofWands")

def FortCavalier_509_MapTrigger_23_9(p):
    if StuffDone["21_2"] == 250:
        return
    StuffDone["21_2"] = 250
    TownMap.List["FortCavalier_21"].DeactivateTrigger(Location(23,9))
    TownMap.List["FortCavalier_21"].DeactivateTrigger(Location(24,9))
    TownMap.List["FortCavalier_21"].DeactivateTrigger(Location(25,9))
    MessageBox("You walk up to the north gate and look at the wheel you could use to open them.\n\nWhen you do, guards run up to you. \"Don\'t open those,\" a captain yells. \"Do you want to let the sliths in on us all?\" They tell you to back away, and you oblige.")

def FortCavalier_512_MapTrigger_5_8(p):
    if StuffDone["21_3"] == 250:
        return
    StuffDone["21_3"] = 250
    TownMap.List["FortCavalier_21"].DeactivateTrigger(Location(5,8))
    TownMap.List["FortCavalier_21"].DeactivateTrigger(Location(41,8))
    MessageBox("You climb the stairway to the north walls and look out over the carnage. A few hundred feet away, hundreds of sliths camp, planning the next assault. Below the walls, many bodies, some fresh, some rotten, are piled up.\n\nThe north wall is cracked and scarred by the impacts of dozens of fireballs, and blood is splattered everywhere. That Fort Cavalier withstood this much punishment and remained standing is truly a miracle.")

def FortCavalier_514_MapTrigger_46_24(p):
    result = ChoiceBox("You find a long secret passage, leading out of the fortress and back towards civilization. It will take you past the slith lines, and from there you can go to Dharmon, the nearest Exile city.\n\nYour mission has been triumphantly completed. Do you go back to Exile?", eDialogPic.STANDARD, 31, ["Leave", "Wait"])
    if result == 0:
        ChoiceBox("The passage stretches for about two thousand feet, and deposits you well away from slith lines. From there, you maneuver your way through neutral territory. A few close escapes and minor skirmishes later, you return to Exile territory.\n\nThe Exile army gives you 3000 gold for your services, and throw in a pretty medal as well. Even better, you get the satisfaction of knowing that you\'ve made a difference for the better.\n\nFort Cavalier holds. It easily fends off the slithzerikai until reinforcements are able to fight there way there some weeks later. Without your help, the fort would have fallen for sure.\n\nThe outcome of the war is still in doubt, but Exile has won a major victory, and they have you to thank for it.\n\nTHE END", eDialogPic.STANDARD, 31, ["OK"])
        Party.Gold += 3000
        for pc in Party.EachAlivePC():
            pc.AwardXP(50)
        RunScript("GlobalCall_FortCavalier_694", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    elif result == 1:
        return

def FortCavalier_515_OnEntry(p):
    if StuffDone["21_0"] == 250:
        return
    StuffDone["21_0"] = 250
    ChoiceBox("As you arrive at the fort, the guards at the south wall raise a cheer and open the gate for you to enter. You aren\'t here a moment too soon ... you can hear a massive battle going on at the north gate.", eDialogPic.STANDARD, 31, ["OK"])

def FortCavalier_516_TalkingTrigger12(p):
    p.TalkingText = "Veronica takes you aside for a moment and teaches you some magical rituals. You can now cast the spell Major Summoning."
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_major_summon")

def FortCavalier_517_TalkingTrigger17(p):
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_wall_of_blades")
