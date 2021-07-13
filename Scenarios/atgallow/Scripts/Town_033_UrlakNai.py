def Generate_Wandering_33_UrlakNai(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["MadMonk_37"]])
            npcs.append([1,NPCRecord.List["Priest_223"]])
            npcs.append([1,NPCRecord.List["Acolyte_222"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["MadMonk_37"]])
            npcs.append([1,NPCRecord.List["Priest_223"]])
            npcs.append([1,NPCRecord.List["Acolyte_222"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["MadMonk_37"]])
            npcs.append([1,NPCRecord.List["Priest_223"]])
            npcs.append([1,NPCRecord.List["Acolyte_222"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["MadMonk_37"]])
            npcs.append([1,NPCRecord.List["Priest_223"]])
            npcs.append([1,NPCRecord.List["Acolyte_222"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(32,17)
                elif r2 == 1: l = Location(16,18)
                elif r2 == 2: l = Location(4,34)
                elif r2 == 3: l = Location(32,5)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def UrlakNai_651_MapTrigger_27_53(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if StuffDone["12_4"] < 2:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(26,56))
            p.CancelAction = True
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Your ascent up the stairwell is blocked by tons of melted rock. Skol-Trok did a thorough job of destroying this spire.")
        return
    p.CancelAction = True

def UrlakNai_653_MapTrigger_27_56(p):
    result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(28,53))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_655_MapTrigger_37_53(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if StuffDone["12_4"] < 2:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(38,56))
            p.CancelAction = True
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Your ascent up the stairwell is blocked by tons of melted rock. Skol-Trok did a thorough job of destroying this spire.")
        return
    p.CancelAction = True

def UrlakNai_657_MapTrigger_37_56(p):
    result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(36,53))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_659_MapTrigger_57_44(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(61,41))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_661_MapTrigger_60_42(p):
    result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(57,45))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_663_MapTrigger_53_20(p):
    result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(57,15))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_665_MapTrigger_57_16(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(53,21))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_667_MapTrigger_32_12(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(32,15))
        p.CancelAction = True
        Town.PlaceEncounterGroup(2)
        return
    p.CancelAction = True

def UrlakNai_668_MapTrigger_32_14(p):
    result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(32,11))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_669_MapTrigger_32_40(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if StuffDone["12_5"] >= 7:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(33,38))
            p.CancelAction = True
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You try to climb the steps. But no matter how far you get, you never seem to get any closer to the top. You turn back and you hear a whisper. \"Shame on you! You have not said all your prayers today.\"")
        return
    p.CancelAction = True

def UrlakNai_670_MapTrigger_32_38(p):
    result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(32,41))
        p.CancelAction = True
        return
    p.CancelAction = True

def UrlakNai_671_MapTrigger_62_26(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(55,26))
    p.CancelAction = True

def UrlakNai_672_MapTrigger_55_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(62,24))
    p.CancelAction = True

def UrlakNai_674_MapTrigger_52_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(62,20))
    p.CancelAction = True

def UrlakNai_675_MapTrigger_2_39(p):
    result = ChoiceBox("These cauldrons are filled with a strange greenish stew. Care to take a sip?", eDialogPic.STANDARD, 20, ["Leave", "Drink"])
    if result == 1:
        MessageBox("You take a sip of the offensive stew. It was not a good idea. You instantly start to feel dizzy and tired.")
        for pc in Party.EachAlivePC():
            pc.SP-= 20
        return

def UrlakNai_677_MapTrigger_2_40(p):
    result = ChoiceBox("These cauldrons are filled with a strange greenish stew. Care to take a sip?", eDialogPic.STANDARD, 20, ["Leave", "Drink"])
    if result == 1:
        MessageBox("You take a sip of the stew and feel very dizzy. You vision begins to fade in and out. When your senses return, you see an opening to the south. You could have sworn that was not there before!")
        Town.AlterTerrain(Location(3,42), 0, TerrainRecord.UnderlayList[170])
        return

def UrlakNai_678_MapTrigger_22_39(p):
    result = ChoiceBox("This chest is empty. However, an inscription at its base reads, \"Place offerings for spirits past here.\" Do you throw in some coins?", eDialogPic.STANDARD, 2, ["Leave", "Give"])
    if result == 1:
        Party.Gold -= 200
        MessageBox("You throw in a few of your coins. As they hit the bottom, they vanish! You feel a strange sense of satisfaction from your offering.")
        Town.AlterTerrain(Location(14,47), 0, TerrainRecord.UnderlayList[170])
        return

def UrlakNai_679_MapTrigger_50_15(p):
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(50,15), True):
            if i.SpecialClass == 18:
                itemthere = True
                break
    if itemthere == True:
        MessageBox("The prayer book seems to fit perfectly here.")
        return
    MessageBox("This pedestal feels empty. You believe some important book should be placed here.")

def UrlakNai_680_MapTrigger_53_15(p):
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(53,15), True):
            if i.SpecialClass == 18:
                itemthere = True
                break
    if itemthere == True:
        MessageBox("The prayer book seems to fit perfectly here.")
        return
    MessageBox("This pedestal feels empty. You believe some important book should be placed here.")

def UrlakNai_681_MapTrigger_50_13(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(50,13)).Num == 191:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(50,15), True):
                if i.SpecialClass == 18:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(53,15), True):
                    if i.SpecialClass == 18:
                        itemthere = True
                        break
            if itemthere == True:
                MessageBox("You touch the bookshelf, and it vanishes before your eyes!")
                Town.AlterTerrain(Location(50,13), 0, TerrainRecord.UnderlayList[170])
                return
            return
        return

def UrlakNai_682_MapTrigger_3_45(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["12_6"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["12_6"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_683_MapTrigger_32_8(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 159, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["12_7"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["12_7"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_684_MapTrigger_57_19(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["12_8"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["12_8"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_685_MapTrigger_51_10(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["12_9"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["12_9"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_686_MapTrigger_47_49(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["13_0"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["13_0"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_687_MapTrigger_17_49(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["13_1"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["13_1"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_688_MapTrigger_30_49(p):
    result = ChoiceBox("As you approach this altar, it reaches out to your mind. You get a strange desire to kneel and say a prayer.", eDialogPic.TERRAIN, 159, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["13_2"] < 1:
            MessageBox("You nervously kneel at the altar and meditate. You feel the altar reaching into your deepest parts of your mind, seeming to search you. After a while, it stops. You rise with a strange sense of satisfaction.")
            StuffDone["13_2"] = 1
            StuffDone["12_5"] += 1
            if StuffDone["12_5"] == 250:
                pass
            return
        MessageBox("You kneel at the altar and say a prayer. This time you do not feel as fulfilled.")
        return
    MessageBox("You back away and manage to break away from the altar\'s influence.")

def UrlakNai_689_MapTrigger_27_31(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Animation_Vanish(Party.LeaderPC, True, "010_teleport")
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    Wait()
    Party.Reposition(Location(35,37))
    p.CancelAction = True
    Animation_Vanish(Party.LeaderPC, False, "010_teleport");
    for n in range(9):
        Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
        Animation_Pause(50)
    p.CancelAction = True

def UrlakNai_694_MapTrigger_39_27(p):
    Town.AlterTerrain(Location(32,22), 0, TerrainRecord.UnderlayList[210])

def UrlakNai_695_MapTrigger_23_26(p):
    Town.AlterTerrain(Location(32,22), 0, TerrainRecord.UnderlayList[139])

def UrlakNai_697_MapTrigger_43_29(p):
    Town.AlterTerrain(Location(39,33), 0, TerrainRecord.UnderlayList[210])

def UrlakNai_698_MapTrigger_39_35(p):
    Town.AlterTerrain(Location(39,33), 0, TerrainRecord.UnderlayList[139])

def UrlakNai_699_MapTrigger_32_33(p):
    if Game.Mode == eMode.COMBAT:
        return;
    result = ChoiceBox("Upon this pedestal rests the reason you came here. It is standing upright, firmly held in place in its holder. You wonder why this artifact is so revered by the Urlak-Nai. No matter, the scepter is yours!\n\nJust as you are about to take it, you hear a shout. You look and see Tyrann, the High Priest of the Urlak-Nai. You can see fear in his eyes. \"Stop! You do not understand what you are doing! Allow me to explain first.\" You listen.\n\n\"Before the Empire came to be, a powerful Haakai Lord called Skol-Trok terrorized the world. Our order waged war upon the creature and succeeded for the most part. In order to secure its defeat eternally, we imprisoned it.\n\nSkol-Trok is held in his prison by the Onyx Scepter. Not even his powers are capable of escaping the field. Over the centuries, we harnessed its power and used it to aide ourselves and your Empire.\n\nI urge you not to remove this scepter. For if you do, Skol-Trok will escape and will resume his reign of terror. That is a fate, no matter at what cost, that should not be inflicted upon the world again.\"\n\nSo the dilemma presents itself, do you follow your orders and release the mighty Skol-Trok? Or do you disobey for the greater good and allow the throne to fall in the hands of Auspire? What is your decision?", eDialogPic.CREATURE, 131, ["Leave", "Take"])
    if result == 1:
        ChoiceBox("You quickly grab the Onyx Scepter. Tyrann yells out, \"Nooo! You fools!\", as he fires out a bolt of electricity. You are all blasted against the wall, but he was too late to stop you.\n\nImmediately, the entire Spire begins to shake. The room becomes uncomfortably warm. In the center of the room, you see a massive tear in space begin to open. It continues to expand at an exponential rate.\n\nTyrann has an expression of utter horror. \"What have you done! Now nothing can stop it! We must get out of here before we are all destroyed!\" He shouts out a prayer and the world begins to twist around you. Everything goes black.\n\n* * *\n\nWith no Onyx Scepter holding Skol-Trok in his interdimensional prison, he immediately breaks out. The fury of over a thousand years of imprisonment basks the Spire in waves of destructive heat.\n\nAt the end of the rage, the Spire is no more...", eDialogPic.STANDARD, 13, ["OK"])
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(32,57))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        ChoiceBox("You awaken in the entrance hall of the temple. You rise to see a depressed Tyrann sitting in the Throne. He looks at you bitterly.\n\n\"You imperial brutes! Now you have your silly Onyx Scepter. Look at what you have done! Look at all the destruction. Think of all who have died -- over 6,000 loyal members of the Urlak-Nai. Our spire, everything gone.\n\nAnd what for, so the Empire could have the powers of our Onyx Scepter?\" He lets out a sigh and pauses for a long time. You see tears in his eyes. \"But there is no point in anger now. Nothing will bring back countless lost friends.\n\nNothing will bring back this glorious Spire. I fear that this is only a taste of the true power of Skol-Trok. We can take comfort that it will be many years before it shall be able to return. It needs time to regenerate its energies.\n\nAnd once it does, I pray that we shall be able to defeat it again.\" He looks down at the table. He looks up at you and says, \"Please leave. You have done enough damage here. I only hope that the use for the Onyx Scepter proves valuable.\"", eDialogPic.CREATURE, 131, ["OK"])
        StuffDone["12_4"] = 2
        SpecialItem.Give("OnyxScepter")
        Town.NPCList.Clear()
        Town.PlaceEncounterGroup(1)
        return
    ChoiceBox("You pull away from the Onyx Scepter. Tyrann lets out a great sigh of relief. \"I\'m glad you have come to your senses. Now you had best be gone before you cause any more trouble.\"\n\nHe begins to chant and the world twists around you. Next thing you know, you are outside. You return to Zenith and are greeted by an angry Vale. However, an explanation of the situation calms him down.\n\n\"Well, let us hope that our mages can come up with an alternative to destroying the Nethergate. All we can do now is wait.\" Unfortunately, the efforts of the magi are in vain. They could not figure out how to duplicate the Onyx Scepter.\n\nIn the mean time, you are sent on various missions. After four months, you are recalled. The powerful army of Auspire attacked! The battle is long and hard. But the human soldiers and mages are no match for the arcane forces.\n\nDuring the battle your entire band is slain. After a bloody conflict lasting for just over a year, Auspire manages to take the throne. Unfortunately, you had chosen incorrectly.\n\nTHE END", eDialogPic.CREATURE, 21, ["OK"])
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def UrlakNai_700_OnEntry(p):
    if StuffDone["12_4"] >= 2:
        Town.NPCList.Clear()
        return
    if StuffDone["12_4"] < 1:
        return
    Town.MakeTownHostile()
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Tyrann_224": Town.NPCList.Remove(npc)

def UrlakNai_701_CreatureDeath0(p):
    StuffDone["12_4"] = 1
