
def AttheGallows_2026_MapTrigger_23_21(p):
    if StuffDone["67_1"] == 250:
        return
    StuffDone["67_1"] = 250
    TownMap.List["AttheGallows_81"].DeactivateTrigger(Location(23,21))
    TownMap.List["AttheGallows_81"].DeactivateTrigger(Location(24,21))
    ChoiceBox("At last, you have reached the main chamber. Currently, Rentar-Ihrno, sworn enemy of your nation, is preparing its destruction.\n\nSuddenly the crystal soul begins to glow. \"Rentar, the Imperials have reached the main chamber.\" Rentar turns around and looks at you with horror.\n\n\"So once again a band comes attempting to stop me. I suggest you not take any further action for you are no match for me. If I was not preoccupied, I could reduce you to dust in a fraction of a second.\n\nHowever, I shall have to leave a few of my creations to deal with you.\" She waves her arms and the runes flash. Horrific, fluid-like beings appear upon the runes and stare at you hungrily.\n\nRentar returns her attention to the control panel, ignoring you. She is probably too powerful for you to even touch and she knows it. The question remains: How do you stop her?\n\nYour entire world now sits at the gallows. You must stop the execution at all costs!", eDialogPic.STANDARD, 1024, ["OK"])
    Town.PlaceEncounterGroup(1)
    Timer(Town, 4, False, "AttheGallows_2044_TownTimer_2", eTimerType.DELETE)

def AttheGallows_2028_MapTrigger_23_2(p):
    ChoiceBox("After a long drawn out battle with the mighty being, you manage to conquer it. The structure of the crystal immediately shatters as a chilling smoke rises from the shards.\n\nCaffen-Bok is finally dead and at peace after centuries of suffering from the experiments performed on him by your ancestors so long ago.\n\nYou turn to see Rentar-Ihrno looking giving you a glare of pure hatred. It is a glare that literally sends chills down your spine.", eDialogPic.STANDARD, 1029, ["OK"])
    Town.PlaceEncounterGroup(2)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Nightmare_252": Town.NPCList.Remove(npc)
    ChoiceBox("\"Quick we must stop her! With the Crystal Soul and the barrier gone, we may be able to hold her from activating the machine until reinforcements arrive. It\'s the only shot we have.\"", eDialogPic.CREATURE, 1029, ["OK"])
    Timer(Town, 4, False, "AttheGallows_2045_TownTimer_29", eTimerType.DELETE)

def AttheGallows_2029_MapTrigger_21_37(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["67_3"] == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        p.CancelAction = True
        Animation_Hold(-1, 004_bless)
        Wait()
        ChoiceBox("You make your way back down to the first floor. Immediately upon leaving the elevator, you meet with Dervish Lin. You inform her of the events that just conspired. She nods and orders her troops back.\n\nThe walk back to Fort Gallows is a long and quiet one. Although Rentar-Ihrno\'s plans have been stopped, there is little motivation for celebration. As you enter the fort, Astervis turns to you and says.\n\n\"We tried our best, yet still we have failed.\"", eDialogPic.STANDARD, 1024, ["OK"])
        ChoiceBox("After several hours of debriefing by the Dervish, you are dismissed to your chambers. Several hours later, you are called back to the office and meet a hologram of the Prime Director. He wears a grim expression.\n\n\"I have been informed of your efforts. First I must give my congratulations on behalf of Emperor Tahvan IV. Had it not been for you, the entire Empire would have been reduced to a lifeless waste within a decade.\n\nHowever, our victory is not a full one for Altrus has still succeeded. Although the politics are too complex for you to understand, I must say that further efforts against the Vahnatai are pointless for two reasons.\n\nThe first being the futility of such an attack, there would be no point. Secondly, lacking an immediate threat, our nation lacks the motivation for a war. The High Council has convened and decided that it is best to simply forget about this event.\n\nWe do not want to instill panic into our people, so all knowledge of the events on Gallows Isle have been declared forbidden. You are hereby ordered to forget all events that have conspired here.\n\nTomorrow morning, a ship will take you back to the mainland. You are to report to the palace where your group will be decommissioned and reassigned to various tasks throughout the Empire. That is all.\"", eDialogPic.CREATURE, 31, ["OK"])
        ChoiceBox("The hologram fades away, as does all hope of any more adventure. Following orders, you \'forget\' about Gallows Isle, never mentioning it to anyone -- not even your families, future spouses, and children.\n\nUpon reporting to the palace, your group is immediately decommissioned. Each of you are sent separate ways performing certain symbolic tasks for the Empire the rest of your careers.\n\nMost of that time is spent as either in charge of security for various Imperial cities or the commander of fortresses. Ironically, one of you spends a five year term as commander of Fort Lemmix, your initial post.\n\nNear the end of your careers, you manage to meet up with the others in the group. As far as you can tell, the Empire has taken no action due to the events at Gallows. Why would they care anyway? The consequences are centuries off.\n\nAlthough all of you wish more could have been done there, you realize there is probably nothing you could have done. You could not have stopped Altrus no matter how hard you tried.\n\nYou take comfort in the fact you did what you could. At least you have prolonged the life of the Empire by nearly four centuries and that is nothing to be ashamed of.", eDialogPic.STANDARD, 1024, ["OK"])
        Animation_Hold(-1, 004_bless)
        Wait()
        ChoiceBox("...Remember victory cannot always be achieved, but defeat is always attainable. So long as you try your hardest, take no sorrow. Fate does not always travel on a path we may wish...\n\n...the dye is cast and the future has begun...", eDialogPic.STANDARD, 1030, ["OK"])
        ChoiceBox("THE END", eDialogPic.STANDARD, 1024, ["OK"])
        Animation_Hold(-1, 022_openingmusic)
        Wait()
        Scenario.End()
        return

def AttheGallows_2031_MapTrigger_17_10(p):
    StuffDone["67_6"] = 1

def AttheGallows_2043_TownTimer_0(p):
    if StuffDone["67_6"] == 2:
        StuffDone["67_6"] = 3
        Town.PlaceEncounterGroup(2)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Nightmare_252": Town.NPCList.Remove(npc)
        ChoiceBox("\"Quick we must stop her! With the Crystal Soul and the barrier gone, we may be able to hold her from activating the machine until reinforcements arrive. It\'s the only shot we have.\"", eDialogPic.CREATURE, 1029, ["OK"])
        Timer(Town, 4, False, "AttheGallows_2045_TownTimer_29", eTimerType.DELETE)
        return

def AttheGallows_2044_TownTimer_2(p):
    if StuffDone["67_2"] == 0:
        if Maths.Rand(1,0,100) < 50:
            if Maths.Rand(1,0,100) < 50:
                Message("Crystal Soul casts:")
                Message("  Deathstrike")
                Animation_Hold(-1, 024_priestspell)
                Wait()
                Party.Damage(Maths.Rand(10, 1, 10) + 100, eDamageType.UNBLOCKABLE)
                Wait()
                Timer(Town, 4, False, "AttheGallows_2044_TownTimer_2", eTimerType.DELETE)
                return
            Message("Crystal Soul casts:")
            Message("  Psychic Pulse")
            Animation_Hold(-1, 053_magic3)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 4))
            Timer(Town, 4, False, "AttheGallows_2044_TownTimer_2", eTimerType.DELETE)
            return
        if Maths.Rand(1,0,100) < 50:
            Message("Crystal Soul casts:")
            Message("  Excommunicate")
            Animation_Hold(-1, 024_priestspell)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 8))
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 8))
            Timer(Town, 4, False, "AttheGallows_2044_TownTimer_2", eTimerType.DELETE)
            return
        if Maths.Rand(1,0,100) < 50:
            Message("Crystal Soul casts:")
            Message("  Energy Vacuum")
            Animation_Hold(-1, 043_stoning)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SP-= 50
            Timer(Town, 4, False, "AttheGallows_2044_TownTimer_2", eTimerType.DELETE)
            return
        Message("Crystal Soul casts:")
        Message("  Shatter Essence")
        Animation_Hold(-1, 090_paralyze)
        Wait()
        for pc in Party.EachAlivePC():
            pc.SetSkill(eSkill.STRENGTH, pc.GetSkill(eSkill.STRENGTH) - 1)
        for pc in Party.EachAlivePC():
            pc.SetSkill(eSkill.DEXTERITY, pc.GetSkill(eSkill.DEXTERITY) - 1)
        for pc in Party.EachAlivePC():
            pc.SetSkill(eSkill.INTELLIGENCE, pc.GetSkill(eSkill.INTELLIGENCE) - 1)
        Timer(Town, 4, False, "AttheGallows_2044_TownTimer_2", eTimerType.DELETE)
        return

def AttheGallows_2045_TownTimer_29(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "AltrusIhrno_205": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(3)
    Timer(Town, 2, False, "AttheGallows_2046_TownTimer_33", eTimerType.DELETE)

def AttheGallows_2046_TownTimer_33(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "RentarIhrno_206": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(4)
    Animation_Explosion(Location(23,11), 2, "005_explosion")
    Animation_Hold()
    Wait()
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "AltrusIhrno_205": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(5)
    ChoiceBox("The drained Altrus fires a bolt of energy at Rentar, catching her off guard. She is knocked away from the control panel. Altrus lunges toward the panel in his severely weakened state and attempts to operate the controls.", eDialogPic.STANDARD, 1028, ["OK"])
    Timer(Town, 2, False, "AttheGallows_2047_TownTimer_38", eTimerType.DELETE)

def AttheGallows_2047_TownTimer_38(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "AltrusIhrno_205": Town.NPCList.Remove(npc)
    if Maths.Rand(1,0,100) <= 100:
        Town.PlaceField(Location(23,11), Field.CRATER)
    Town.AlterTerrain(Location(24,12), 0, TerrainRecord.UnderlayList[239])
    Animation_Explosion(Location(23,11), 0, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("Rentar-Ihrno, angered by Altrus\' betrayal, strikes back with a searing bolt of flame. Altrus, drained of his defensive power while being held by Caffen-Bok, is powerless to defend.\n\nThe blast hits him directly, pushing him to the ground. He is surprisingly still alive, but beyond all hope of healing.", eDialogPic.STANDARD, 1029, ["OK"])
    ChoiceBox("\"Too late...Rentar. Had...just enough...time...complete activation cycle. Intensity of 3.72...locked...change impossible. Empire...fall in...four...centuries...life on...surface...survives...\n\nMay you have...your honor restored...\"", eDialogPic.STANDARD, 1028, ["OK"])
    Message("  Altrus-Ihrno dies.")
    Timer(Town, 2, False, "AttheGallows_2048_TownTimer_43", eTimerType.DELETE)

def AttheGallows_2048_TownTimer_43(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "RentarIhrno_206": Town.NPCList.Remove(npc)
    Animation_Explosion(Location(22,10), 1, "005_explosion")
    Animation_Hold()
    Wait()
    StuffDone["67_3"] = 1
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if  npc.IsABaddie: Town.NPCList.Remove(npc)
    Timer(Town, 2, False, "AttheGallows_2049_TownTimer_47", eTimerType.DELETE)

def AttheGallows_2049_TownTimer_47(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Astervis_204": Town.NPCList.Remove(npc)
    ChoiceBox("\"Our forces should be well into the structure by now. We can meet them on our descent. There is nothing left to do here, let us get going.\"", eDialogPic.CREATURE, 1029, ["OK"])
