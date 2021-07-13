
def YvosstaiCamp_336_MapTrigger_23_27(p):
    if StuffDone["15_2"] >= 1:
        MessageBox("Your victory over the slith champion has won you the admiration you so long for in this world. You get approving nods from everyone.")
        return
    result = ChoiceBox("You wander thoughtlessly into the lair of a squadron of new Yvoss-tai, -Worker slith warriors. They stand to stare as you enter, fingering their brand new bronze spears and wheezing silently.\n\nYou stop uncomfortably in the middle of a crowd. Surely, you reassure yourself, surely the sliths know who you are? That you are invited here by their great leader? Honoured guests! You wonder if telling them as much would help.\n\nStill, the young warriors seem outright hostile. Taking a step backwards, one of you stumbles over a lizard foot. Its owner roars in fury as you whirl to face him.\n\nHe is a big slith, skin glowing green and heavy with muscles. Yet he has none of the dignity or style of the Ssara-tai, the warrior caste. He is three hundred ponds of fury, defiance and aggression, and armed with a gleaming new spear.\n\n\"Ape men!\" he stutters in your language, and lifts his spear. No further vocabulary is needed. He is challenging you. The crowd cheers, and you notice the scales tied to his spear. He is a Slith Dervish, an elite soldier of the lizard kin.\n\nYou have innocently placed yourselves in quite a situation. The sliths will allow you to back off and submit yourselves, but that would be terribly humiliating. On the other hand, you could accept his challenge to a duel ...", eDialogPic.TERRAIN, 185, ["Accept", "Refuse"])
    if result == 0:
        Town.PlaceEncounterGroup(1)
        pc = SelectPCBox("Exchanging glances, you decide to award yourselves the showdown between sliths and humans that you have been aching for. Your champion steps forwards, sneering back at the Yvoss-tai, to the cheers of the crowd.\n\nThe two of you are taken to a small practice field. You are both free to leave the field, but that means acknowledging defeat. You may leave the field with honour only if your opponent is down. You roar, and arms clash.",True)
        if pc == None:
            p.CancelAction = True
            return
        Party.Split(pc, Location(19,38))
        return
    elif result == 1:
        MessageBox("You back away from the ferocious warrior, muttering the name of your host. The sliths jeer and laugh at you, making you blush with shame. You leave, but your self confidence has suffered a severe dent.")
        for pc in Party.EachAlivePC():
            pc.AwardXP(-8)
        return

def YvosstaiCamp_337_MapTrigger_27_35(p):
    if StuffDone["15_2"] >= 1:
        if StuffDone["15_1"] == 250:
            return
        StuffDone["15_1"] = 250
        ChoiceBox("Your onslaught staggered the slith champion. Blow by blow, you forced him back, until he was pressed up against the wall and must surrender. \"Lizard man!\" you sneered as he slumped in front of you, then you turned your back on him and left.\n\nSsara-tai etiquette requires that a defeated duellist must give away his spear, and this slith worker mimics the rule, offering you his weapon. You accept it with a brusque nod.\n\nThe slith audience regards you with new respect.", eDialogPic.CREATURE, 1025, ["OK"])
        Party.GiveNewItem("BronzeSlithSpear_388")
        for pc in Party.EachAlivePC():
            pc.AwardXP(25)
        if Party.IsSplit:
            Party.Reunite()
        return
    MessageBox("Cringing from the blows of the Dervish, you stumble off the island and back to safety between your friends. The slith howls with scorn, shaking his bronze spear. Swallowing shame, you leave, feeling puny.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(-20)
    if Party.IsSplit:
        Party.Reunite()

def YvosstaiCamp_338_MapTrigger_25_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;

def YvosstaiCamp_339_MapTrigger_10_19(p):
    if StuffDone["15_3"] >= 1:
        if StuffDone["17_0"] >= 1:
            return
        result = ChoiceBox("You open the lid and find the pile of gold that Sss-Chross promised you. Still, you hesitate. You are about to give up all the values you have been fighting for. If you back out of the conflict now, you truly are nothing more than mercenaries.\n\nDo you?", eDialogPic.TERRAIN, 178, ["Leave", "Take"])
        if result == 1:
            Party.Gold += 1000
            RunScript("GlobalCall_RoyalSector_599", ScriptParameters(eCallOrigin.CUSTOM))
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("Peeking through a hole in the wall at the end of the corridor, you can see Sss-Chross conferring with two of his lieutenants. For the moment, it might be best if he thought you dead, or you will face an entire army alone. You remain hidden.")
            return
        return

def YvosstaiCamp_340_MapTrigger_27_33(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This island is of special importance to the sliths. You do not understand their shouted protests, but you get their meaning. They don?t want tourists out there.")

def YvosstaiCamp_341_MapTrigger_6_17(p):
    if StuffDone["17_0"] >= 1:
        return
    if StuffDone["15_4"] >= 1:
        MessageBox("You stand uncertainly in the room of the Yvoss-tai warlord, wondering why he takes no action to punish your insolence. After a moment, a part of the southern wall slides away with a rumbling sound. \"Behold, Zahr, God of true Warriors!\" Chross says.")
        Town.AlterTerrain(Location(7,19), 0, TerrainRecord.UnderlayList[0])
        Animation_Hold(-1, 060_smallboom)
        Wait()
        ChoiceBox("You step back an involuntary step as a figure appears in the hole. He is no taller than you, but that is about the only feature you can make out, for he is cowled and masked in a wide cloak that obscures his face and body.\n\nAs the Masked Aide steps out to regard you, Sss-Chross falls on his knees. \"Divine lord, I have captured the saboteurs from Howling Gap. If it please thee, I shall punish them as fits their crime.\"\n\nIf Zahr is surprised, angry or pleased, he shows no reaction. He just considers you curiously as Chross calls his guards forward. Ten warriors step out of the shadows and lower their spears. You have no time to defend yourselves as they advance.\n\nStep by step, you are forced back, until you find yourselves on the brink of an abyss. One more push from the Yvoss-tai, and you topple over, to the applause of Sss-Chross.\n\nThe mysterious Aide remains silent as you tumble down the chute.", eDialogPic.CREATURE1x2, 4, ["OK"])
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(9,38)
        Party.MoveToMap(TownMap.List["LizardPit_9"])
        return

def YvosstaiCamp_342_MapTrigger_13_13(p):
    if StuffDone["17_0"] >= 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Venturing out into the slith camp is sheer folly. You have another destination in mind. If not less dangerous, it is at least heroic.")
        return

def YvosstaiCamp_346_MapTrigger_7_20(p):
    if StuffDone["17_0"] >= 1:
        Town.MakeTownHostile()
        if StuffDone["15_7"] == 250:
            return
        StuffDone["15_7"] = 250
        MessageBox("You kick the secret door open and enter Sss-Chross? room. You find him alone. His face is rigid with surprise as you enter the room instead of his Masked Aide, as he had expected. He gathers himself enough to put up a fight, however.")
        Town.AlterTerrain(Location(7,19), 0, TerrainRecord.UnderlayList[0])
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Peeking through a hole in the wall at the end of the corridor, you can see Sss-Chross conferring with two of his lieutenants. For the moment, it might be best if he thought you dead, or you will face an entire army alone. You remain hidden.")

def YvosstaiCamp_347_MapTrigger_6_26(p):
    if StuffDone["17_0"] >= 1:
        return
    if ChoiceBox("Upon close inspection you find a lever hidden inside a crack in the mountain side. Perhaps it could help you to freedom. On the other hand, you do not want to call the attention of the sliths on shore.", eDialogPic.STANDARD, 8, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("As you pull, a solid bridge rises out of the water and connects the ledge to the sacred island of the sliths. This must be how Zahr, the Masked Aide, arrived so suddenly in Sss-Chross? room, you think. You hope this will provide a way of escape.")
        for x in range(8, 9):
            for y in range(27, 32):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[72])
        return

def YvosstaiCamp_348_MapTrigger_21_7(p):
    if StuffDone["17_0"] >= 1:
        MessageBox("The guards are dead, and the way out is free at the moment. You hurry through, relishing in your success. This may well turn the tide of the war in Chimney.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Burly slith guards keep you away from this exit. An even stream of troops and supplies come and go this way, giving the impression of being an important connection.")

def YvosstaiCamp_349_MapTrigger_8_37(p):
    result = ChoiceBox("An imposing portal is the centrepiece of this room. Closer examination reveals it to be of Vahnatai design. Multilingual text lines the arch: \"Provided by Verundis\". You wonder if the sliths know that this is how their \"Zahr\" arrives.", eDialogPic.STANDARD, 22, ["Leave", "Step In"])
    if result == 1:
        StuffDone["15_5"] = 1
        if StuffDone["17_0"] >= 1:
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("Something is wrong. The portal that was glowing with energy a moment ago has suddenly stopped pulsing. Stepping inside now would be very dangerous. Staying here could also be very dangerous, but that is a danger you can defeat with weapons.")
            return
        Party.OutsidePos = Location(205, 56)
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(8,52)
        Party.MoveToMap(TownMap.List["FelineFrontier_17"])
        return

def YvosstaiCamp_350_MapTrigger_7_32(p):
    if ChoiceBox("You find a small lever set into the wall. Do you pull it?", eDialogPic.STANDARD, 214, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        for x in range(8, 9):
            for y in range(27, 32):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[72])
        return

def YvosstaiCamp_351_MapTrigger_5_14(p):
    if StuffDone["17_0"] >= 1:
        if StuffDone["15_6"] >= 1:
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You cannot leave this room without killing Sss-Chross.")
        return
    if StuffDone["15_4"] >= 1:
        MessageBox("You stand uncertainly in the room of the Yvoss-tai warlord, wondering why he takes no action to punish your insolence. After a moment, a part of the southern wall slides away with a rumbling sound. \"Behold, Zahr, God of true Warriors!\" Chross says.")
        Town.AlterTerrain(Location(7,19), 0, TerrainRecord.UnderlayList[0])
        Animation_Hold(-1, 060_smallboom)
        Wait()
        ChoiceBox("You step back an involuntary step as a figure appears in the hole. He is no taller than you, but that is about the only feature you can make out, for he is cowled and masked in a wide cloak that obscures his face and body.\n\nAs the Masked Aide steps out to regard you, Sss-Chross falls on his knees. \"Divine lord, I have captured the saboteurs from Howling Gap. If it please thee, I shall punish them as fits their crime.\"\n\nIf Zahr is surprised, angry or pleased, he shows no reaction. He just considers you curiously as Chross calls his guards forward. Ten warriors step out of the shadows and lower their spears. You have no time to defend yourselves as they advance.\n\nStep by step, you are forced back, until you find yourselves on the brink of an abyss. One more push from the Yvoss-tai, and you topple over, to the applause of Sss-Chross.\n\nThe mysterious Aide remains silent as you tumble down the chute.", eDialogPic.CREATURE1x2, 4, ["OK"])
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(9,38)
        Party.MoveToMap(TownMap.List["LizardPit_9"])
        return

def YvosstaiCamp_353_MapTrigger_16_5(p):
    if StuffDone["17_0"] >= 1:
        MessageBox("There is nobody here to stop you from going through the personal things of the Yvoss-tai chieftains. You throw aside roots and dried skins and smooth rocks, picking up a book instead. Reading through it, you memorize the mage spell `Spray Fields?.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_spray_fields")
        return
    MessageBox("The slith chieftains will not let you near this chest. In the opposite situation, you would probably not have let them go through your personal things, either.")

def YvosstaiCamp_354_MapTrigger_43_40(p):
    MessageBox("You try to slip off into the slith jungle on your own, but do not get far. You struggle to find your way through marshes and tight woods, but are almost relieved when a slith hunting party finds you and brings you back on spear point.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(41,41))
    p.CancelAction = True

def YvosstaiCamp_361_MapTrigger_25_4(p):
    Party.OutsidePos = Location(68, 83)

def YvosstaiCamp_363_OnEntry(p):
    if StuffDone["17_0"] >= 1:
        MessageBox("One step brings you into the lush jungles at the foot of the Dividing Wall. You arrive in a small temple in the camp of the Yvoss-tai.")
        return
    if StuffDone["15_0"] == 250:
        return
    StuffDone["15_0"] = 250
    ChoiceBox("Voss-Roder leads you for hours through an alien landscape. Peeking over the edge of the Dividing Wall, even visiting the embassy of the sliths could never prepare you for the sight of the subterranean jungle.\n\nClouds of scorching steam erupt from miniature volcanoes, creating a permanent layer of mist that hides the ceiling. Rain drizzles continuously, soaking you within minutes. And trees and plants burst from the ground everywhere, unlike the arid Exile.\n\nYou bend to study various plants as you pass, but Voss-Roder warns you to stay away. The subterranean plants survive only partly from photosynthesis. Extra energy comes from hunting, the slith says.\n\nYou do not take him seriously until you see a palm tree snap together around a small bird. After that you move around the carnivore plants.\n\nYou walk for half a day, following the Dividing Wall west. You stop only for short breaks before insects set in and drive you on. Finally, Voss-Roder stops at the edge of a clearing. Several streams run into a small lake, base for the slith rebels.\n\nHe points to a cave in the great wall. \"Sss-Chross.\" he says, bows to you and leaves you alone. You would have preferred that he stayed with you as a guide.", eDialogPic.TERRAIN, 1025, ["OK"])

def YvosstaiCamp_364_ExitTown(p):
    if p.Dir.IsNorth:
        MessageBox("You follow the corridor north and upwards for more than a day, until you guess you are about level with Chimney. Your exact position is impossible to tell. You keep your lights low and talk little at first, to avoid the attention of the Yvoss-tai.\n\n You are discovered once or twice by groups of sliths, but it turns out they are no match for veterans like yourselves. After a while, you walk openly, preferring to make haste rather than hiding from common soldiers.")
