
def AncientRuins_885_MapTrigger_9_55(p):
    if StuffDone["18_3"] == 250:
        return
    StuffDone["18_3"] = 250
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(9,55))
    MessageBox("The cavern merges into an extremely narrow tunnel. Judging from the cutting marks and rubble behind, this tunnel must have been created quite recently. This must be were Zarmond\'s students tunneled into the school.\n\nUnfortunately, (or perhaps fortunately) you do not see any sign of the apprentices. No bodies or equipment. They must either be inside or left. Your betting that they are somewhere within, not likely to be alive.")

def AncientRuins_886_MapTrigger_9_49(p):
    if StuffDone["18_4"] == 250:
        return
    StuffDone["18_4"] = 250
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(9,49))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(8,49))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(10,49))
    ChoiceBox("This wall appears to have been blasted away. You carefully climb past the rubble and find a very old and decayed room. A large piece of the ceiling has fallen and landed onto the floor long ago.\n\nThis place must be over a thousand years old to have been ravaged by time the way this room has. Judging from this room, it is likely that the rest of the ruins are much the same. You had better walk softly as to not make a cave-in.", eDialogPic.STANDARD, 4, ["OK"])
    Timer(Town, 3, False, "AncientRuins_914_TownTimer_2", eTimerType.DELETE)

def AncientRuins_889_MapTrigger_15_32(p):
    if StuffDone["18_5"] == 250:
        return
    StuffDone["18_5"] = 250
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(15,32))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(16,32))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(17,32))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(24,44))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(24,45))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Once more, you hear the low growling. This time, you can make out its source. You believe you have just encountered more Wyverns! Unfortunately, they have already seen you and are as hungry and ferocious as ever.\n\nYou thought that you were finished with these horrid creatures upon the fall of Fort Nether. You were mistaken. A colony must have managed to survive the aeons in these ruins, hidden away from the Imperial purges.\n\nYour hopes of finding Zarmond\'s apprentices alive has just decreased significantly.", eDialogPic.CREATURE, 144, ["OK"])

def AncientRuins_894_MapTrigger_58_52(p):
    ChoiceBox("Clumsily thrown away in this alcove is the body of a human male. The body is horribly scarred. Severe burns cover much of the corpse and make the face totally unidentifiable. This body seems quite fresh and was probably killed recently.\n\nJudging from the heavy claw marks and scorches you bet this person was killed by the Wyverns. This person was also wearing what appeared to have been mage robes, but not certainly.\n\nThe body is quite gruesome and difficult to look at -- even for hardened Empire soldiers like yourself.  However, you try to find any identifying marks, but everything is altered beyond recognition.\n\nOne thing of interest is a small dark point on his chest right over his heart. A Wyvern\'s fiery breath is much less concentrated whereas this appears to be a very strong and concentrated blast.\n\nThe wounds match a mage\'s kill spell, powerful, concentrated, and efficient. Such a direct blow to the heart would most likely cause instant death to the victim. But Wyverns cannot cast kill spells, let alone any magic!\n\nSomeone or something else must have killed him. Something much more powerful. You believe this is probably one of Zarmond\'s apprentices, but you cannot be sure. And where is the other apprentice?", eDialogPic.TERRAIN, 179, ["OK"])
    if StuffDone["18_6"] == 1:
        StuffDone["18_6"] = 2
        return

def AncientRuins_895_MapTrigger_26_12(p):
    if StuffDone["18_8"] == 250:
        return
    StuffDone["18_8"] = 250
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(26,12))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(27,12))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(33,17))
    TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(33,18))
    ChoiceBox("Upon entering this room, the smell of sulfur assaults your noses. This room is somewhat different than the others. The walls appear to be much newer as if they were recently refurbished.\n\nHowever, the walls seem to have been blasted apart and quite recently at that. The floor is covered with evidence of explosions and bloodstains are everywhere. You wonder who or what was here. The Wyverns could not have done this.\n\nThe mystery begins to grow. Apparently Zarmond\'s apprentices were not the first intelligent beings to occupy this school recently. You can only wonder what happened to them.", eDialogPic.STANDARD, 4, ["OK"])

def AncientRuins_899_MapTrigger_8_27(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(3,17)).Num == 122:
        if StuffDone["18_6"] >= 2:
            Town.AlterTerrain(Location(3,17), 0, TerrainRecord.UnderlayList[133])
            return
        return

def AncientRuins_902_MapTrigger_5_13(p):
    if StuffDone["18_6"] == 2:
        result = ChoiceBox("Huddled in this corner is the body of a young mage. The corpse is covered with many wounds of battle -- mortal wounds that probably led to his death. He could not have died too long ago as his body is barely even decayed.\n\nBut why would a corpse be hidden? Perhaps someone placed him there, trying to cover up whatever has been going on here.\n\nA search for anything to identify the mage reveals a small book. It appears to be some kind of daily log or journal. Inside may contain the answers to many questions. Do you read the book?", eDialogPic.TERRAIN, 179, ["Leave", "Read"])
        if result == 1:
            StuffDone["18_6"] = 3
            SpecialItem.Give("PrescottsJournal")
            ChoiceBox("Looking in the front of the journal reveals this mage\'s identity. As you had suspected, this was one of Zarmond\'s apprentices -- Prescott in particular. You continue to flip through the notes and discover something interesting at the end of the journal.\n\n\"If you are reading this, you shall know the last moments of Flayde and myself. We were two apprentices of the mage Zarmond. We came to these ruins to learn about the history of magical education.\n\nHowever, we had encountered something very unexpected. Near the center of the ruins we found an lab, fully repaired and active! Inside several mages were doing experiments. Flayde recognized one of them as a friend of his, so we approached.\n\nAs soon as we entered, I realized something was wrong. His friend had been one of the mages who had vanished in the recent streak of disappearances. The mages seemed like zombies, under someone\'s control.\n\nFlayde\'s friend said no words. He simply cast a quick spell -- a kill spell that struck poor Flayde right in the heart, killing him instantly. I had no choice but to try to run. In the process, I was severely wounded by several of their spells.\n\nEscape was too risky in my condition. I managed to outrun them and discovered a small alcove in the ruins. I bundled up rocks in front of the wall and hid myself away, in the hopes that a moment would arise for my escape...", eDialogPic.STANDARD, 24, ["OK"])
            ChoiceBox("...I knew I did not have too long to live and needed healing. After a few hours, I heard a large explosion that shook several stones loose from the ceiling. My scrying had revealed that they had just destroyed that lab.\n\nThrough additional scrys, I detected the presence of several horrible creatures that had not been there before. They are gigantic fire breathing lizards which I believe are called Wyverns -- an extinct species supposedly, but all too real for me!\n\nThey were everywhere! I knew that escape was futile. I doubt I could have even taken one in peak condition, let alone a hoard of them and while in need of medical attention.\n\nSo I decided to write this resigned to my certain death. If you are friend an reading this, please return it to my master Zarmond. May the gods be with you!\" Prescott signed his name after the message and wrote nothing more.\n\nZarmond will be very interested in this. You pocket the book.", eDialogPic.STANDARD, 24, ["OK"])
            return
        return

def AncientRuins_903_MapTrigger_59_25(p):
    if StuffDone["18_6"] >= 7:
        MessageBox("These pedestals have empty alcoves where the stone tablets once lay.")
        return
    if StuffDone["18_6"] < 6:
        ChoiceBox("Upon each pedestal rests a stone tablet. These ancient stones are engraved in a language that you have no comprehension of. Whether these were magical tomes, historical records, or plain entertainment, you cannot know for sure.\n\nSince they are quite heavy and could break easily, you decide that it would be best to leave them alone and let the experts examine them.", eDialogPic.TERRAIN, 125, ["OK"])
        return
    StuffDone["18_6"] = 7
    ChoiceBox("These must be the stone tablets that Zarmond wanted you to recover. The language engraved on each is ancient and above your level of scholarly pursuits. You have no idea how these will help in any way, but you oblige.\n\nThe tomes are set into the pedestals and you have to be careful when you remove them. Since the years of neglect have made them quite fragile, you wrap them up securely,so they won\'t take any damage on your return trip.\n\nThe tablets are heavy and bulky, but you\'ll just have to manage.", eDialogPic.TERRAIN, 125, ["OK"])
    SpecialItem.Give("StoneTablets")

def AncientRuins_904_MapTrigger_56_8(p):
    if StuffDone["17_3"] == 13:
        StuffDone["17_3"] = 14
        ChoiceBox("Well, it looks like you\'ve gone just about as far northeast as you can go in the ruins.  Where you suspect the passage to be, you discover a huge basalt wall. The wall is etched with strange glowing glyphs.\n\nTo add to the enigma, unlike the other walls of the ruins, this wall appears to be brand new! You try to analyze the wall as much as you can. Whoever built this wall wanted to keep the area beyond concealed.\n\nYou doubt that you will have the power to bring it down. Perhaps Astervis has an answer.", eDialogPic.TERRAIN, 0, ["OK"])
        return
    if StuffDone["17_3"] == 16:
        if Game.Mode == eMode.COMBAT:
            return;
        result = ChoiceBox("Well, you now have the explosives and you are at your target. A piece of paper attached to the barrel lists the instructions. TO ARM EXPLOSIVES:\n\n(1) REMOVE TOP OF BARREL TO REVEAL CONTROLS.\n\n(2) SET SAFETY LEVER IN \"OFF\" POSITION.\n\n(3) TURN WHEEL CLOCKWISE UNTIL A CLICK IS HEARD. EXPLOSIVES ARE NOW ARMED.\n\n(4) WHEN READY, PULL FUSE LEVER DOWN. EXPLOSIVES WILL ACTIVATE IN EXACTLY TEN MINUTES. BE SURE TO TAKE COVER AS BLAST IS VERY CONCENTRATED!\n\nAre you ready?", eDialogPic.TERRAIN, 106, ["Yes", "No"])
        if result == 0:
            SpecialItem.Take("BarrelofExplosives")
            StuffDone["17_3"] = 17
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(9,58))
            p.CancelAction = True
            Animation_Hold(-1, 005_explosion)
            Wait()
            ChoiceBox("You follow the instructions perfectly. After the explosives are armed, you quickly make your way back to near the entrance and wait. After the ten minutes have expired, you hear a loud blast!\n\nHopefully, the explosives have done their job and not caused a cave in. Time to check things out.", eDialogPic.STANDARD, 25, ["OK"])
            for x in range(55, 58):
                for y in range(7, 8):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[166])
            if StuffDone["17_3"] == 19:
                MessageBox("Just ahead, you make out a humanoid figure in blue robes. You take a few steps closer and make out the face of Astervis. He looks very dejected.")
                Town.PlaceEncounterGroup(1)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Wyvern_225": Town.NPCList.Remove(npc)
                return
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Wyvern_225": Town.NPCList.Remove(npc)
            return
        elif result == 1:
            return
        return

def AncientRuins_907_MapTrigger_50_16(p):
    if StuffDone["17_3"] >= 17:
        if StuffDone["20_0"] == 250:
            return
        StuffDone["20_0"] = 250
        MessageBox("From a distance, you can see a large opening where the wall once was! It appears the explosives have done the trick. You wonder what dangers you will find on the other side.")
        return

def AncientRuins_911_MapTrigger_55_3(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["21_3"] >= 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(40,40)
        Party.MoveToMap(TownMap.List["ForgottenAcademy_60"])
        return
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(40,40)
    Party.MoveToMap(TownMap.List["ForgottenAcademy_41"])

def AncientRuins_914_TownTimer_2(p):
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("Suddenly you flinch back and draw your weapons! You look around, and after a few minutes you put them away. You would swear that you just heard some kind of low-pitched growl. Of course, that could just be your imagination.\n\nOn the bright side, that may have been one or both of Zarmond\'s students. However, with your luck it is probably something much worse.\n\nYou better be even more cautious now. There is no way of telling what magical creation managed to live here for over a thousand years. Tread lightly.", eDialogPic.STANDARD, 6, ["OK"])
    Timer(Town, 5, False, "AncientRuins_915_TownTimer_5", eTimerType.DELETE)

def AncientRuins_915_TownTimer_5(p):
    Animation_Hold(-1, 046_growl)
    Wait()
    MessageBox("You hear that mysterious growl again! This time it could not have been simply imagination. You look around and still no sign of anything. You wonder what could be making that noise.")

def AncientRuins_916_OnEntry(p):
    if StuffDone["17_3"] >= 17:
        for x in range(55, 58):
            for y in range(7, 8):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[166])
        if StuffDone["17_3"] == 19:
            MessageBox("Just ahead, you make out a humanoid figure in blue robes. You take a few steps closer and make out the face of Astervis. He looks very dejected.")
            Town.PlaceEncounterGroup(1)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Wyvern_225": Town.NPCList.Remove(npc)
            return
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Wyvern_225": Town.NPCList.Remove(npc)
        return
    if StuffDone["17_3"] >= 10:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Wyvern_225": Town.NPCList.Remove(npc)
        return

def AncientRuins_917_TalkingTrigger0(p):
    SpecialItem.Give("AstervisNPC")
    StuffDone["17_3"] = 20
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Astervis_204": Town.NPCList.Remove(npc)
