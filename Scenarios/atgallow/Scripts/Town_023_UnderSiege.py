
def UnderSiege_449_MapTrigger_26_21(p):
    if StuffDone["6_5"] == 250:
        return
    StuffDone["6_5"] = 250
    TownMap.List["UnderSiege_23"].DeactivateTrigger(Location(26,21))
    Town.PlaceEncounterGroup(1)
    Animation_Explosion(Location(26,14), 2, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("You enter this room and notice all of the Golems have been totaled! You then notice two other figures, you can hardly believe your eyes. It is Sidor! Could he really be alive!? He is having a confrontation with Dervish Montcalm.\n\nMontcalm speaks, \"But you were killed?\" Sidor replies, \"Ha! I was, but the almighty Halloth brought me back and has shown me his true power. I was unknowing before, but now I see how I must serve him.\"\n\nMontcalm shouts back, \"You filthy traitor! I was the one who took you off the streets and trained you for twenty years. Take that!\" He shoots a large fireball. Sidor parries. \"Sorry old fool, guess you had me wrong! Mwa, ha, ha!\"\n\nSidor casts a kill spell, Montcalm deflects it. \"I have taught you well. But you are not nearly as strong as your master. Prepare to die traitor!\"", eDialogPic.CREATURE, 28, ["OK"])
    Message("Montcalm Casts:")
    Message("  Kill")
    Animation_Hold(-1, 025_magespell)
    Wait()
    Animation_Explosion(Location(27,18), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Message("Sidor Casts:")
    Message("  Hellbolt")
    Animation_Hold(-1, 074_fireball)
    Wait()
    Message("Montcalm Deflects Spell!")
    Animation_Explosion(Location(27,19), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Message("Montcalm Casts:")
    Message("  Aura of Resistance")
    Animation_Hold(-1, 024_priestspell)
    Wait()
    Animation_Hold(-1, 051_magic1)
    Wait()
    Message("Montcalm is protected!")
    Message("Sidor Casts:")
    Message("  Bolt of Darkness")
    Animation_Hold(-1, 043_stoning)
    Wait()
    Animation_Explosion(Location(25,18), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Message("Montcalm Casts:")
    Message("  Rain of Fireballs")
    Animation_Hold(-1, 025_magespell)
    Wait()
    Animation_Hold(-1, 074_fireball)
    Wait()
    Animation_Hold(-1, 074_fireball)
    Wait()
    Animation_Hold(-1, 074_fireball)
    Wait()
    Message("Sidor Absorbs Magic!")
    Animation_Hold(-1, 053_magic3)
    Wait()
    Message("Sidor Casts:")
    Message("  Time Freeze")
    Animation_Hold(-1, 025_magespell)
    Wait()
    Animation_Hold(-1, 075_cold)
    Wait()
    Message("Montcalm is Frozen!")
    ChoiceBox("Montcalm radiates a dark blue. \"Wh..I can\'t move!\" Sidor laughs maniacally. \"Mwa, ha, ha! I\'ve been doing a little studying on my own. That one took me a month to master Weren\'t prepared for that I reckon. Oh well.\"\n\nSidor laughs. \"Fool! It looks like you\'re the one doing the dying...\" Sidor fires back the fireballs that he had just absorbed. Dervish Montcalm is helplessly hit by the searing blasts.", eDialogPic.CREATURE, 27, ["OK"])
    Animation_Explosion(Location(25,18), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Explosion(Location(25,18), 0, "005_explosion")
    Animation_Hold()
    Wait()
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Montcalm_194": Town.NPCList.Remove(npc)
    Town.AlterTerrain(Location(25,18), 0, TerrainRecord.UnderlayList[165])
    Message("Montcalm Dies.")
    Animation_Explosion(Location(25,18), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Hold(-1, 029_monsterdeath2)
    Wait()
    ChoiceBox("Sidor turns to face you. \"Well, who do we have here? It looks like the same people that I helped rescue before I died. You look angry. Well, I\'m afraid it\'s your turn to die too!\"", eDialogPic.CREATURE, 28, ["OK"])

def UnderSiege_450_TownTimer_41(p):
    for x in range(0, 64):
        for y in range(0, 64):
            if Maths.Rand(1,0,100) <= 10:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
    Timer(Town, 10, False, "UnderSiege_450_TownTimer_41", eTimerType.DELETE)

def UnderSiege_451_OnEntry(p):
    ChoiceBox("You awaken to the sounds of swords clanking, fireball spells, and screams. You instinctively grab your equipment. This can only mean one thing: Fort Reflection is under attack!", eDialogPic.STANDARD, 4, ["OK"])

def UnderSiege_452_CreatureDeath43(p):
    StuffDone["6_4"] = 2
    ChoiceBox("You have slain Sidor. You pause for a moment, realizing that everything is over. You wonder: How did the Troglodytes break in? How did Halloth enslave Sidor? Is even he that powerful. Everything just doesn\'t make sense.\n\nPerhaps this was all a dream...", eDialogPic.STANDARD, 4, ["OK"])
    for x in range(0, 64):
        for y in range(0, 64):
            if Maths.Rand(1,0,100) <= 10:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[179])
    Timer(Town, 10, False, "UnderSiege_450_TownTimer_41", eTimerType.DELETE)

def TerrainTypeStepOn_Mist_UnderSiege_2902(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    StuffDone["2_0"] = 6
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(46,43)
    Party.MoveToMap(TownMap.List["FortReflection_17"])
