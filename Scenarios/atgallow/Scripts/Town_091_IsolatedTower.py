
def IsolatedTower_2131_MapTrigger_23_41(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(23,40)).Num == 128:
        MessageBox("You approach the doors and you hear a creepy voice, \"Who visits the master?\" You wait, it seems as if the voice is waiting for you to respond. What do you say?")
        response = InputTextBox("Enter something:", "")
        response = response[0:10].upper()
        if response == "BLOODSWORD":
            Animation_Hold(-1, 009_lockpick)
            Wait()
            MessageBox("The doors click open! The voice returns. \"Welcome to the master\'s tower, guests!\"")
            SuspendMapUpdate()
            for x in range(23, 25):
                for y in range(40, 41):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("You respond and the door shocks you! \"The master does not wish to see you. Please leave.\"")
        Party.Damage(Maths.Rand(1, 1, 1) + 0, eDamageType.UNBLOCKABLE)
        Wait()
        return

def IsolatedTower_2133_MapTrigger_22_27(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(20,30)).Num == 130:
            SuspendMapUpdate()
            for x in range(20, 21):
                for y in range(30, 32):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["33_1"] == 250:
                return
            StuffDone["33_1"] = 250
            Town.PlaceEncounterGroup(1)
            MessageBox("You pull the levers and some of the portculli open. However, that is not all. A platform in the center of the room is quickly elevated from below bringing a small collection of cultists. The welcoming party is here!")
            for x in range(22, 26):
                for y in range(29, 33):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[82])
            return
        MessageBox("Nothing happens.")
        return

def IsolatedTower_2134_MapTrigger_25_27(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(27,30)).Num == 130:
            SuspendMapUpdate()
            for x in range(27, 28):
                for y in range(30, 32):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            if StuffDone["33_1"] == 250:
                return
            StuffDone["33_1"] = 250
            Town.PlaceEncounterGroup(1)
            MessageBox("You pull the levers and some of the portculli open. However, that is not all. A platform in the center of the room is quickly elevated from below bringing a small collection of cultists. The welcoming party is here!")
            for x in range(22, 26):
                for y in range(29, 33):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[82])
            return
        MessageBox("Nothing happens.")
        return

def IsolatedTower_2135_MapTrigger_10_30(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Target_241": Town.NPCList.Remove(npc)

def IsolatedTower_2136_MapTrigger_37_32(p):
    if StuffDone["33_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("These tiles appear to be a little off. It is probably a trap that will need to be disarmed. You will need to disarm it to continue.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("These tiles appear to be a little off. It is probably a trap that will need to be disarmed. You will need to disarm it to continue.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["33_2"] = 250
    TownMap.List["IsolatedTower_91"].DeactivateTrigger(Location(37,32))
    pc.RunTrap(eTrapType.BLADE, 2, 45)

def IsolatedTower_2137_MapTrigger_39_32(p):
    if StuffDone["33_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("These tiles appear to be a little off. It is probably a trap that will need to be disarmed. You will need to disarm it to continue.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("These tiles appear to be a little off. It is probably a trap that will need to be disarmed. You will need to disarm it to continue.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["33_3"] = 250
    TownMap.List["IsolatedTower_91"].DeactivateTrigger(Location(39,32))
    pc.RunTrap(eTrapType.GAS, 2, 30)

def IsolatedTower_2138_MapTrigger_39_34(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever and hear the sounds of machinery. You cannot tell exactly what happened, however.")
        SuspendMapUpdate()
        for x in range(23, 25):
            for y in range(21, 22):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def IsolatedTower_2139_MapTrigger_29_18(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    result = ChoiceBox("You encounter a stairway leading down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(34,27))
        p.CancelAction = True
        return
    p.CancelAction = True

def IsolatedTower_2141_MapTrigger_33_26(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    result = ChoiceBox("You encounter a stairway leading up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(29,19))
        p.CancelAction = True
        return
    p.CancelAction = True

def IsolatedTower_2143_MapTrigger_16_26(p):
    if StuffDone["33_4"] == 250:
        return
    StuffDone["33_4"] = 250
    TownMap.List["IsolatedTower_91"].DeactivateTrigger(Location(16,26))
    TownMap.List["IsolatedTower_91"].DeactivateTrigger(Location(17,26))
    MessageBox("This must be where the cult mages fine tune their fireball spells. At the other end of the room is a shattered and burned brick wall, with another stronger basalt one behind it.")

def IsolatedTower_2145_MapTrigger_8_22(p):
    MessageBox("These books are on the subject of combat -- physical and magical. Unfortunately, most of them are old news for Empire soldiers. Some of them contain new information, but nothing really worthwhile.")

def IsolatedTower_2150_MapTrigger_8_8(p):
    MessageBox("Even the cultists value entertainment. All of these books are simply literature with many of them having, shall we say, more of an adult theme.")

def IsolatedTower_2155_MapTrigger_8_10(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever and hear the sounds of machinery. You cannot tell exactly what happened, however.")
        SuspendMapUpdate()
        for x in range(23, 25):
            for y in range(26, 27):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def IsolatedTower_2156_MapTrigger_23_19(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["33_5"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        Animation_Hold(-1, 021_pcdying)
        Wait()
        MessageBox("Oops! You\'ve just walked right into a trap. The floor beneath you is merely an illusion. You fall down into a slimy pit. Unfortunately, you are injured by the fall.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(36,21))
        p.CancelAction = True
        Party.Damage(Maths.Rand(5, 1, 4) + 10, eDamageType.UNBLOCKABLE)
        Wait()
        if StuffDone["33_6"] == 250:
            return
        StuffDone["33_6"] = 250
        MessageBox("To make matters worse, many of the slimes are not immobile. They rise up and move toward you! Apparently these guys need feeding too, and you are their next meal.")
        Town.PlaceEncounterGroup(2)
        return

def IsolatedTower_2158_MapTrigger_37_29(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a soft click.")
        if StuffDone["33_5"] == 0: StuffDone["33_5"] = 1
        else: StuffDone["33_5"] = 0
        return

def IsolatedTower_2159_MapTrigger_37_26(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(36,27)).Num == 130:
            MessageBox("You pull the lever and the adjacent portcullus opens up.")
            t = Town.TerrainAt(Location(36,27))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(36,27)).TransformTo
                Town.AlterTerrain(Location(36,27), 0, t)
            return
        MessageBox("You pull the lever and the adjacent portcullus slams shut.")
        t = Town.TerrainAt(Location(36,27))
        if t.InGroup("Lockable"):
            t = Town.TerrainAt(Location(36,27)).TransformTo
            Town.AlterTerrain(Location(36,27), 0, t)
        return

def IsolatedTower_2160_MapTrigger_27_10(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["33_7"] == 250:
        return
    StuffDone["33_7"] = 250
    Town.PlaceEncounterGroup(3)
    SuspendMapUpdate()
    for x in range(23, 25):
        for y in range(17, 18):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetLocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()
    ChoiceBox("You enter a fair sized magical laboratory. At the southern end of the room is a priest dressed in the red Followers\' robes kneeling before an altar, chanting. Suddenly, he rises and turns to you, detecting your presence.\n\n\"Who disturbs the great Emitar!?\" He booms as he looks you over. \"Empire assassins! And the same ones who defeated master Zaine. At last, I will avenge my fellow comrades who perished at your hands. Take that!\"\n\nHe hits you with a powerful disease spell, you all begin to feel quite ill. He laughs. \"Now you shall feel the true power of the great Morbane!\"", eDialogPic.CREATURE, 24, ["OK"])
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 6))

def IsolatedTower_2162_MapTrigger_29_8(p):
    if StuffDone["33_8"] == 1:
        ChoiceBox("This is Emitar\'s journal. He has used it mostly for laboratory notes and personal ones as well. You read it over and learn a good amount about Emitar.\n\nEmitar was once the leader of a fairly large group of rather unsuccessful bandits. When the Followers first appeared and began to recruit about a year ago, Emitar approached Zaine and signed his group up.\n\nEmitar was able to move his way through Zaine\'s ranks until he became his right-hand man. It was Emitar who played a major part in the development of the fungus that you exterminated at their base near Praddor.\n\nApparently, Emitar always was secretly jealous of Zaine. He was glad that Zaine decided to leave the Followers after his plans at Praddor were quashed. He quickly took control of the religious cult and hoped to succeed where Zaine failed.\n\nAt this tower, he was attempting to recreate the fungus. However, it appears that he was not having much luck seeing that the ancient text where he originally obtained the knowledge from was lost in the flood. But, he was making slow progress.\n\nWell, it looks like that progress will be halted for good this time!", eDialogPic.STANDARD, 24, ["OK"])
        return

def IsolatedTower_2163_MapTrigger_39_12(p):
    if StuffDone["33_9"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["33_9"] = 250
    TownMap.List["IsolatedTower_91"].DeactivateTrigger(Location(39,12))
    pc.RunTrap(eTrapType.DART, 2, 67)

def IsolatedTower_2164_MapTrigger_36_8(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 8:
        MessageBox("Emitar kept a small collection of spell books. Most of them are fairly simple and many are just theoretical. One prayer book offers a detailed description of a chant that summons serpents. You can now cast Sticks to Snakes!")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_sticks_to_snakes")
        return
    MessageBox("Emitar kept a bookshelf full of spell books. Most of them are quite theoretical. The ones that may contain some useful spells are a bit beyond your level of learning in the magical arts. You will require more Mage Lore!")

def IsolatedTower_2165_CreatureDeath4(p):
    Town.PlaceEncounterGroup(4)
    Message("Emitar casts:")
    Message("  Transmute")
    Animation_Hold(-1, 053_magic3)
    Wait()

def IsolatedTower_2166_CreatureDeath17(p):
    Town.PlaceEncounterGroup(5)
    Message("Emitar casts:")
    Message("  Transmute")
    Animation_Hold(-1, 053_magic3)
    Wait()

def IsolatedTower_2167_CreatureDeath32(p):
    Town.PlaceEncounterGroup(6)
    Message("Emitar casts:")
    Message("  Transmute")
    Animation_Hold(-1, 053_magic3)
    Wait()

def IsolatedTower_2168_CreatureDeath38(p):
    Town.PlaceEncounterGroup(7)
    Message("Emitar casts:")
    Message("  Transmute")
    Animation_Hold(-1, 053_magic3)
    Wait()

def IsolatedTower_2169_CreatureDeath39(p):
    StuffDone["33_0"] = 1
    SuspendMapUpdate()
    for x in range(23, 25):
        for y in range(17, 18):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetUnlocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()
    ChoiceBox("This time, Emitar does not have the strength remaining to change form again. With the final blow, his body falls to the floor, killed instantly. The final expression on his face is one of utter horror and surprise.\n\nHowever, the expression does not last long. The entire body is soon engulfed into roaring flames that quickly consume the body in a matter of seconds. All that remains are a few meager possessions and ashes.\n\nEmitar is now dead, and the Followers will probably die with him. The authorities in Vega will be very happy to hear of this deed. Well done!", eDialogPic.CREATURE, 24, ["OK"])
    for pc in Party.EachAlivePC():
        pc.AwardXP(20)
