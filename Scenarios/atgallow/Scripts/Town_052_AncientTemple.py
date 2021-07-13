
def AncientTemple_1183_MapTrigger_32_57(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,56)).Num == 145:
        if SpecialItem.PartyHas("GlowingDisc"):
            MessageBox("Alas, this passage is blocked by a grim basalt wall and a massive imposing black metallic door. Small bright golden runes are inscribed about its surface. Needless to say, it is locked. Whoever built this really wanted to seal this place well.\n\nIn the center of the door is a circular indentation. On a hunch, you take the glowing disc you found and insert it. A perfect fit! The golden runes flash a bright fiery red as the massive door creaks open.")
            t = Town.TerrainAt(Location(32,56))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(32,56)).TransformTo
                Town.AlterTerrain(Location(32,56), 0, t)
            return
        MessageBox("Alas, this passage is blocked by a grim basalt wall and a massive imposing black metallic door. Small bright golden runes are inscribed about its surface. Needless to say, it is locked. Whoever built this really wanted to seal this place well.")
        return

def AncientTemple_1184_MapTrigger_32_46(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    result = ChoiceBox("There is a glowing portal here. You have no idea where it will take you. Could be a room filled with treasure beyond your wildest dreams or into solid rock, meaning instant death. Decisions, decisions...", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(7,57))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        ChoiceBox("Well, it sure isn\'t a room filled with awesome treasures. However, you are still alive, at least you think you are alive at least.\n\nYou look around and appear to be what is in some kind of banquet hall. People are crowded about everywhere dancing, drinking, talking, and all about having a good time.\n\nYou feel a bit awkward about being at one minute, in some dark gloomy dungeon, and the next at some festive party. You look at the head table and see a young man in what appears to be the Emperor\'s robes! Are you in the Imperial palace?\n\nYou turn to a guard and ask, \"Why you are in our majesty\'s banquet hall. Welcome to the festivities and may you enjoy yourselves. Hail Sol III!\" Sol III!? Isn\'t the current Emperor Tahvan IV? You are getting very confused.\n\n\"Who is this Tahvan IV character? Can\'t say I\'ve ever heard of him. Are you sure you haven\'t had too much to drink? You appear sober!\" You believe you are sober, but you are not so sure about your sanity. You ask what year it is.\n\n\"Why this is 73 Imperial Era, during the rule of the great Sol III!\" The year 73! That was over a thousand years ago. Could it be that your trip through the portal took you backward in time?", eDialogPic.CREATURE, 130, ["OK"])
        return
    p.CancelAction = True

def AncientTemple_1185_MapTrigger_9_48(p):
    if StuffDone["28_0"] >= 5:
        MessageBox("As you approach the door, you fall through to the other side! You look around and appear to be in some kind of study. The room is pretty elegant. To your west, you see the Emperor, his wife, and that Raven character.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(9,46))
        p.CancelAction = True
        return

def AncientTemple_1187_MapTrigger_8_43(p):
    if StuffDone["28_5"] == 250:
        return
    StuffDone["28_5"] = 250
    TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(8,43))
    TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(8,44))
    TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(8,45))
    TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(8,46))
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Emperor_231": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(1)

def AncientTemple_1190_MapTrigger_2_46(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Raven_232": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Official_34": Town.NPCList.Remove(npc)
    ChoiceBox("Right before your eyes, Raven removes a dagger from his belt and plunges it into the Emperor\'s heart! He lets out a blood curdling scream as Raven twists and removes the bloody dagger.\n\nThe Emperor\'s body crumbles to the ground, like a rag doll. The Emperor is dead. Lady Vera lets out a very loud scream. Raven turns to her and says, \"I\'m sorry my Lady, I must not leave any witnesses.\"\n\nShe begins to fight him off, but her skills are no match for the fierce assassin\'s. Just as he is about to slay her, several guards burst into the room. Raven turns around, looking quite shocked.\n\nHe grabs a metallic sphere from his belt, and slams it on the ground. It cracks, releasing a thick smoke screen. When the smoke clears, Raven is gone! You try to speak with the guards and the people, but they seem to ignore you.\n\nThis all feels like some kind of play on some director\'s stage. The only time people speak with you, it seems, is when whoever scripted this act wanted you to be spoken to. Reminds you of narration.\n\nIt looks like there is more ahead.", eDialogPic.CREATURE, 130, ["OK"])
    Town.PlaceEncounterGroup(3)

def AncientTemple_1192_MapTrigger_7_43(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;

def AncientTemple_1195_MapTrigger_4_41(p):
    if StuffDone["28_7"] == 250:
        return
    StuffDone["28_7"] = 250
    TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(4,41))
    MessageBox("This door leads to what appears to be the throne room. Upon the royal throne sits Duke (Emperor?) Ironclad, now garbed in the official robes of the Emperor. Before him stands an ominous man in red robes.")

def AncientTemple_1196_MapTrigger_8_37(p):
    if StuffDone["28_6"] == 1:
        MessageBox("You slide through the door and find yourself in what appears to be some sort of reading room. At a table sits Lady Vera and that Dervish you spoke with earlier back at the party.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(10,37))
        p.CancelAction = True
        return

def AncientTemple_1197_MapTrigger_13_34(p):
    if StuffDone["28_8"] >= 1:
        if StuffDone["28_9"] >= 1:
            MessageBox("You approach the door and slide into another room. Mages and apprentices scuttle back and forth with scrolls, potions, and books. You smell the aroma of magical experimentation in the air. This must be some kind of mage academy.\n\nIn the center of the room is a table. At one end sits a mage garbed in purple robes with small golden runes sewn in. At the other end is Dervish Skyle and Lady Vera, who appears to be quite pregnant!")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(13,32))
            p.CancelAction = True
            return
        return

def AncientTemple_1198_MapTrigger_8_26(p):
    if StuffDone["29_0"] >= 1:
        if StuffDone["29_1"] >= 1:
            if StuffDone["29_2"] >= 1:
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(8,24))
                p.CancelAction = True
                Town.PlaceEncounterGroup(2)
                ChoiceBox("You approach the door and are pulled into a sequence of images. You see Lady Vera and Dervish Skyle leave the mage academy (the same one you visited back in Sorcrega 1200 years later).\n\nYou watch their travels as they try to seek refuge. They finally arrive in a port town and try to board a ship to Valorim. However, they are recognized by Imperial agents. A hot pursuit ensues and Vera and Skyle manage to elude them.\n\nThey manage to seek refuge in a monastery. However, it does not take long for the Imperials to track them down. Empire soldiers, led by that conniving Raven, now a decorated Empire Dervish, burst into their room to arrest them.\n\nRaven speaks, \"At last Skyle. You should have known that it was only a matter of time before we tracked you down. I\'m afraid that we have to see to your immediate execution by order of our great Emperor Ironclad I!\"\n\nSkyle retorts. \"Great Emperor, ha! Fratricidal traitor who paved his way to the throne with his brother\'s body! It is only a matter of time before the people find out what really happened that night, one year ago.\"\n\nRaven chuckles. \"I\'m afraid that we have everybody quite convinced that it was you and the mistress who assassinated Sol III over some petty love quarrel. Both of you, time to die.\" The soldiers grab their weapons for a fight.", eDialogPic.STANDARD, 4, ["OK"])
                return
            return
        return

def AncientTemple_1199_MapTrigger_16_21(p):
    ChoiceBox("Dervish Skyle fought nobly, but he was no match for four well trained warriors. He falls to the ground and says in a choked voice, \"Burn in the abyss traitor! You and your false Emperor...\"\n\nClutching Vera\'s dead hand, he closes his eyes and takes his last breath.\n\nRaven grins and turns to the others. \"Well done, men. I assure that all of you will receive due promotions for slaying these foul traitors. You have done your Empire a great service. Feel proud!\"\n\nThe soldiers all look grim faced. They all know the truth, but dare not speak up for fear that they too will be executed. Raven begins to walk away and turns around. \"Take the bodies outside and have them incinerated.\n\nOh, and be sure to spread the ashes. We don\'t want them resurrected on us, now do we? I\'m going back into town. Take the night off, I\'ll see you in the barracks by noon tomorrow.\"\n\nRaven leaves as the soldiers gather the bodies and take them outside. What a sad tale.", eDialogPic.CREATURE, 17, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "EmpireDervish_17": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "EliteGuard_16": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(4)

def AncientTemple_1200_MapTrigger_7_21(p):
    if StuffDone["29_3"] >= 1:
        MessageBox("You slide through the door and find yourself in what appears to be some kind of mage\'s dormitory. Two mages are talking, an old one and a young one. You immediately recognize the older one as Alcritas. You must be back at the Sorcrega Academy!")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(5,21))
        p.CancelAction = True
        return

def AncientTemple_1201_MapTrigger_5_18(p):
    if StuffDone["29_4"] >= 1:
        if StuffDone["29_5"] >= 1:
            MessageBox("You find yourself in a large conference room. At the head of the table sits the cruel Emperor Ironclad I. He is much older than the last time you saw him, but you can still recognize him. Near him is the Dervish Raven. The Emperor does not look too happy.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(5,16))
            p.CancelAction = True
            return
        return

def AncientTemple_1202_MapTrigger_9_11(p):
    if StuffDone["29_6"] >= 1:
        if StuffDone["29_7"] >= 1:
            MessageBox("You slide through the door to find yourself in an empty hallway. You wonder what could be next.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(9,9))
            p.CancelAction = True
            return
        return

def AncientTemple_1203_MapTrigger_9_4(p):
    ChoiceBox("You reach the end of the hallway and are pulled onto a battle field. The two armies charge each other. One is led by Raven and the other by Alexander or now Sol IV. They clash on the battle fields where you hear explosions, screams, and swords clanking.\n\nBoth armies are not equally matched. Raven\'s Imperial soldiers are much better trained and outnumber Sol IV\'s collection of peasants and rogues. It does not take long for Raven\'s army to achieve a clear advantage.\n\nDuring the fray, you make out Sol IV, casting spells. A large fireball is flung toward him and explodes upon direct impact! Sol IV falls to the ground, lifeless. With that final blow, the forces disperse. Once again, Raven has won.\n\nThe entire scene turns dark. You wonder why you are being shown all of this. Suddenly, your vision begins to return as you find yourself in some sort of grim laboratory. A low chanting can be heard. You wonder what is going on.", eDialogPic.STANDARD, 1027, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(17,3))
    p.CancelAction = True
    ChoiceBox("You look around to see the Emperor and Raven watching a ritual in progress. Several mages and priests are huddled around a pentagram. In the center is a robed skeletal body.\n\nSuddenly, there is a flash of light! The skeletal body begins to glow with great intensity. It is a deep red glow, one that chills you. After a few moments, the skeleton rises and speaks in a seemingly far off voice.\n\n\"Wh..wh..where am I?\" He looks down at his hands to see only bones. \"What have you done to me?\" He notices the Emperor. \"What is this? Why are you here. You..you killed my father. I will destroy you!\"\n\nThe lich attempts to cast a spell on the Emperor, but it fizzles out. \"My powers! What have you done?\" Ironclad laughs bitterly, \"I\'m afraid you\'re powers are useless against me. I made sure of that before I reanimated you.\n\nI suppose you wanted to know why I went to this trouble. You see, I really didn\'t want anyone to go to the trouble of resurrecting you, so I took the liberty. I\'m not worried, you won\'t be able to harm me.\n\nYou see, I made sure that one, I am immune to specifically your magic. Also, I have given you a key weakness. An ironic weakness. One that fits you so poetically.\" The lich replies, \"What is that?\"", eDialogPic.CREATURE, 60, ["OK"])
    ChoiceBox("\"Sol, means the sun. Your great grandfather picked that name. He wanted to be known as the sun of his people, the guiding light of his nation. And that sun you shall never see again! For if you expose yourself to sunlight, your soul shall perish forever!\"\n\nHe laughs again. \"How ironic. Sol IV, king of the sun, never to see the sun again. Your name turned against you, nephew,\" emphasizing the word \'nephew\' harshly. Sol replies, \"I will find a way uncle, I swear I will destroy you!\"\n\nIronclad rolls his eyes. \"Oh and we\'ve even found the perfect prison for you. There is this massive shrine that used to belong to the Nephilim. I\'m going to seal you there and at the same time teach those Nephil their inferiority.\n\nImagine, killing two birds with one stone! You and your influence will never be able to leave the shrine. Once inside, our spells will curse you so that you must spend the rest of eternity there!\"\n\nSol shouts, \"Why are you doing this uncle?\" He smiles gleefully. \"Because I like power. I rather enjoy seeing you suffer. It is my destiny to be ruler of the world!\"", eDialogPic.CREATURE, 60, ["OK"])

def AncientTemple_1204_MapTrigger_20_8(p):
    MessageBox("You slide into a fairly elegant, but gloomy throne room. Upon the throne sits Sol IV in his Lich form. Suddenly, an ancient man in dark purple robes moves through the wall and faces Sol. You try to look at his face, but it hurts your mind.\n\nThe purple robed one calls out, \"Sol!\" The Lich looks up and says, \"Sol, I am no longer. All that is left is Morbane.\" The purple robed one says, \"Well then, Morbane. Either way, I still am talking to the same.\"")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(20,10))
    p.CancelAction = True

def AncientTemple_1206_MapTrigger_26_13(p):
    if StuffDone["29_8"] >= 1:
        if StuffDone["29_9"] >= 1:
            MessageBox("You approach the door and as usual find yourself on the \"other\" side. You are in some kind of office. You see morbane standing before two mages. One seated at the desk, the other standing beside him.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(28,14))
            p.CancelAction = True
            return
        return

def AncientTemple_1208_MapTrigger_33_11(p):
    if StuffDone["30_0"] >= 1:
        if StuffDone["30_1"] >= 1:
            if StuffDone["30_2"] >= 1:
                MessageBox("You find yourself in the office of another one of your nemeses. In the throne adjacent to you, sits Auspire, (former) ruler of Stolgrad. At the other end is the ominous figure of Morbane.")
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(35,11))
                p.CancelAction = True
                return
            return
        return

def AncientTemple_1209_MapTrigger_40_12(p):
    if StuffDone["30_3"] >= 1:
        if StuffDone["30_4"] >= 1:
            MessageBox("You find yourself in a summoning room with a large pentagram inscribed into the floor. In front of it stands Morbane who is facing a familiar Vampyric Troglodyte, Halloth!")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(40,14))
            p.CancelAction = True
            return
        return

def AncientTemple_1210_MapTrigger_40_20(p):
    if StuffDone["30_5"] >= 1:
        if StuffDone["30_6"] >= 1:
            MessageBox("You now are in Odix\'s house, the next logical step in the series. You find Morbane seducing Odix. You wonder how much longer this will last.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(39,22))
            p.CancelAction = True
            return
        return

def AncientTemple_1211_MapTrigger_40_25(p):
    if StuffDone["30_7"] >= 1:
        if StuffDone["30_8"] >= 1:
            MessageBox("You emerge in another long hallway. At the end is a reddish glow. You wonder if you are near the end and what comes next. Will you meet Morbane himself? The answer will arrive at the end of this hallway.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(40,27))
            p.CancelAction = True
            return
        return

def AncientTemple_1212_MapTrigger_40_39(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    result = ChoiceBox("You arrive at the end of this hallway to find a portal. Are you ready to step inside and face whatever is on the other side?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        StuffDone["31_0"] = 1
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(32,48)
        Party.MoveToMap(TownMap.List["MorbanesLair_53"])
        return
    p.CancelAction = True

def AncientTemple_1215_TalkingTrigger3(p):
    if StuffDone["27_9"] == 0:
        StuffDone["27_9"] = 1
        StuffDone["28_0"] += 1
        if StuffDone["28_0"] == 250:
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(9,48))
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(10,48))
        return

def AncientTemple_1216_TalkingTrigger6(p):
    if StuffDone["28_1"] == 0:
        StuffDone["28_1"] = 1
        StuffDone["28_0"] += 1
        if StuffDone["28_0"] == 250:
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(9,48))
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(10,48))
        return

def AncientTemple_1217_TalkingTrigger9(p):
    if StuffDone["28_2"] == 0:
        StuffDone["28_2"] = 1
        StuffDone["28_0"] += 1
        if StuffDone["28_0"] == 250:
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(9,48))
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(10,48))
        return

def AncientTemple_1218_TalkingTrigger11(p):
    if StuffDone["28_3"] == 0:
        StuffDone["28_3"] = 1
        StuffDone["28_0"] += 1
        if StuffDone["28_0"] == 250:
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(9,48))
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(10,48))
        return

def AncientTemple_1219_TalkingTrigger13(p):
    if StuffDone["28_4"] == 0:
        StuffDone["28_4"] = 1
        StuffDone["28_0"] += 1
        if StuffDone["28_0"] == 250:
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(9,48))
            TownMap.List["AncientTemple_52"].DeactivateTrigger(Location(10,48))
        return
