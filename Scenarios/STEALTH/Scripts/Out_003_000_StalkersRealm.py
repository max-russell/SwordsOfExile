
def StalkersRealm_379_MapTrigger_29_17(p):
    if StuffDone["203_0"] == 250:
        return
    StuffDone["203_0"] = 250
    WorldMap.DeactivateTrigger(Location(173,17))
    WorldMap.DeactivateTrigger(Location(187,30))
    ChoiceBox("You finally reach the highest valley in the mountains of Morrow\'s Isle. Here, you see arrayed before you the rebel army of Stalker.\n\nIt\'s surprisingly unimpressive. You see six camps, each with 50 or so people camped around it. They\'re mostly hill folk, rough and crude, with a few mages and Empire defectors thrown in. This is the lot that\'s held off the Empire, in all its might?\n\nApparently so. Stalker\'s stealth and viciousness, combined with the cunning of his troops and the defendability of these hills, have enabled him to succeed where so many others have failed. And you\'re about to meet him.\n\nTo the east you see a massive fort, built into the mountain slope. Stalker\'s fortress awaits.", eDialogPic.TERRAIN, 195, ["OK"])

def StalkersRealm_380_MapTrigger_43_30(p):
    if StuffDone["203_0"] == 250:
        return
    StuffDone["203_0"] = 250
    WorldMap.DeactivateTrigger(Location(173,17))
    WorldMap.DeactivateTrigger(Location(187,30))
    MessageBox("Someone shouts from the hills \"Keep going! You\'re almost to someone who can help you along!\" You look up, but can\'t see who yelled it.")

def StalkersRealm_381_MapTrigger_33_15(p):
    result = ChoiceBox("Stalker\'s army spends its time living in small stone huts, each set circled around a  large bonfire. Dead goats and casks of ale are always handy. His troops are clearly a rowdy lot.\n\nThey\'re also friendly, and they\'ve heard of you. When they see you, they invite you in to eat and drink with them.", eDialogPic.TERRAIN, 190, ["Leave", "Accept"])
    if result == 1:
        if StuffDone["203_2"] >= 1:
            MessageBox("You have another hearty meal with Stalker\'s men, with plenty of ale to chase it down. The food is still good, and they are still scary.")
            return
        ChoiceBox("The rebels welcome you in, and, with many hearty slaps on the back, serve you up huge, steaming chunks of roast goat and mugs of ale. They have all sorts of stories of adventure for you, and want to hear your stories as well.\n\nAs you drink with them, you start to notice something unsettling. These folks seem friendly enough, but their stories are horrifying. They involve burned villages, ambushes that turn into massacres, and vile tortures inflicted on Empire troops.\n\nThey\'re cheery, and clearly are impressed by you, but you detect a subtle undercurrent of barely controlled, psychotic violence, always under the surface, always ready to tear loose.\n\nThere can\'t be more than 500 men and women camped in this valley. But they\'re the most terrifying people you\'ve ever met. When the time comes and the feast ends, you\'re more than ready to move on.", eDialogPic.CREATURE, 18, ["OK"])
        StuffDone["203_2"] = 1
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("They are clearly offended, and walk away. They don\'t even bother to say goodbye.")

def StalkersRealm_387_MapTrigger_30_39(p):
    if StuffDone["203_3"] == 250:
        return
    StuffDone["203_3"] = 250
    WorldMap.DeactivateTrigger(Location(174,39))
    WorldMap.DeactivateTrigger(Location(151,29))
    WorldMap.DeactivateTrigger(Location(151,28))
    result = ChoiceBox("Suddenly, rebel troops are everywhere! They\'re jumping out of holes in the ground, running down the mountain side, and charging towards you from the hills ahead. Their weapons aren\'t out, but they don\'t look friendly either.\n\nWhen they get close, you see that there actually aren\'t many of them. Only about 20. Not a large group. You\'re nervous at first, until you see that they are led by O\' Grady, the man who sent you on your deadly mission to Zaskiva.\n\nYour relief at seeing a familiar face is short lived. He looks at you with disgust, even loathing. The other Hill Runners look no friendlier.\n\nO\' Grady says \"Stalker has given orders. You are to be welcomed into our ranks, and given a high position. Higher even than me! I am not fooled, though. I know the Empire contacted you! I know you were brought here to finish us off.\"\n\n\"Surrender now, and we will take you to a ship and send you away from here. Do not surrender, and you will die.\" The rebels put their hands on their blades. They mean it. Do you surrender?", eDialogPic.CREATURE, 17, ["No", "Yes"])
    if result == 0:
        MessageBox("\"Fine!\" O\' Grady yells. \"We\'ll do this the hard way!\" The rebels shout, and charge.")
        WorldMap.SpawnEncounter("Group_3_0_4", p.Target)
        return
    elif result == 1:
        MessageBox("You give up your weapons, and the Hill Runners tie you up and drag you into the hills. Once there, they do not hesitate to stab each of you in the heart and dump the bodies in a gully.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def StalkersRealm_390_MapTrigger_40_15(p):
    if StuffDone["203_4"] == 250:
        return
    result = ChoiceBox("You are finally near the highest point of these mountains. At the top of the path, you can see a large cave. Guards stand around the entrance. You may have finally reached Stalker\'s fortress.\n\nAhead, between you and the fortress, you can see a large contingent of Hill Runners, waiting for you.", eDialogPic.CREATURE, 17, ["Leave", "Approach"])
    if result == 1:
        StuffDone["203_4"] = 250
        WorldMap.DeactivateTrigger(Location(184,15))
        WorldMap.DeactivateTrigger(Location(184,18))
        result = ChoiceBox("At first, you\'re relieved to see that the troops are led by O\'Grady, the man who sent you on your mission to Zaskiva. Then you see the look on his face. His predatory scowl lets you know that he is not here to help you.\n\nThe rebels move forward, drawing their weapons. O\'Grady says \"It\'s no hope. Don\'t bother to fight. We know you have been going to Willow. We know you\'re working for Jaen. Your refusal to fight Empire troops made us sure.\"\n\n\"We\'re going to take you to Stalker, but I don\'t think you will enjoy it. You have no choice. Surrender.\"\n\nThere are about 100 Hill Runners here, and more running from the fortress ahead. Even you would have difficulty when opposed by such forces. Do you surrender?", eDialogPic.CREATURE, 17, ["Yes", "No"])
        if result == 0:
            MessageBox("O\'Grady looks disappointed. He seems to want a fight. Still, he steps out of your way, and points to the cavern ahead. \"Move on. The soldiers there will take you to your cell, where Stalker will come and see you.\"")
            return
        elif result == 1:
            MessageBox("O\'Grady looks relieved that you\'ve decided to fight. He shouts the order, and leads the charge against you. You manage to kill many of them, including O\' Grady, before a hail of arrows mows you down. Tough luck.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You decide not to meet with them quite yet.")

def StalkersRealm_391_MapTrigger_40_18(p):
    if StuffDone["203_4"] >= 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("O\'Grady and his mass of troops are still here, waiting for you to enter the fortress. It is some small measure of how seriously the rebels take you that they would leave 200 people here to guard you. They keep you from moving further south.")
        return

def StalkersRealm_392_MapTrigger_8_34(p):
    if StuffDone["203_5"] == 250:
        return
    StuffDone["203_5"] = 250
    WorldMap.DeactivateTrigger(Location(152,34))
    WorldMap.DeactivateTrigger(Location(153,34))
    MessageBox("You reach the shores of a beautiful mountain lake. The waters are clear and blue, and the sunlight reflects off it so brightly it almost blinds you.\n\nIt would be beautiful here, were it not for the half dozen skeletons on the shore, covered with scraps of armor. Several Empire soldiers met a hard end here, and the remains were left here as a grisly trophy. Or reminder.")

def StalkersRealm_394_MapTrigger_40_8(p):
    result = ChoiceBox("The boat at the end of the dock is not a complicated affair. It\'s a longboat, designed for easy rowing by a small crew. It will be more than enough to safely get you back to the mainland.\n\nAre you ready to leave Morrow\'s Isle?", eDialogPic.TERRAIN, 66, ["No", "Yes"])
    if result == 0:
        p.CancelAction = True
        return
    elif result == 1:
        ChoiceBox("As you sail away from Morrow\'s Isle, you look back one last time.\n\nYou had arrived expecting a noble battle against a band of brigands. You got a civil war. You expected heroics. You got treachery and deceit. And you expected good and evil, and you found desperate people, brutally tearing each other apart.\n\nIt is only a small rebellion. For now. Should the hatred and fury compressed into this small island burst forth, it could disease the continent of Valorim, and beyond.\n\nBut for now, you breathe a deep sigh of relief. It\'s over. You\'ve escaped. After all, sometimes you can\'t win, and you can\'t break even. Sometimes, all you can do is get out of the game.\n\nTHE END", eDialogPic.STANDARD, 17, ["OK"])
        Scenario.End()
        return

def StalkersRealm_395_SpecialOnWin0(p):
    MessageBox("You search O\' Grady\'s body. You find a scroll, signed by Stalker, saying that you are to be found and escorted safely to his fortress. It would seem O\' Grady decided to take some liberties in following these orders.")
