
def FortReflection_321_MapTrigger_46_31(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["2_1"] == 0:
        StuffDone["2_1"] = 1
        Timer(Town, 5, False, "FortReflection_347_TownTimer_5", eTimerType.DELETE)
        return

def FortReflection_325_MapTrigger_44_31(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["2_1"] = 0

def FortReflection_329_MapTrigger_31_52(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,53)).Num == 147:
        MessageBox("The guard recognizes you and opens the gate.")
        SuspendMapUpdate()
        for x in range(31, 34):
            for y in range(53, 54):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetUnlocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def FortReflection_335_MapTrigger_27_34(p):
    result = ChoiceBox("This was Sidor\'s spellbook. It is a thick volume filled with the many teachings of the wise Dervish Montcalm. It serves no purpose for him anymore, so you are free to read it.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_major_haste")
            MessageBox("Sidor\'s spellbook contains a progression of spells, from simple to extremely complex. The book was written as a reference to Sidor, not as a teaching book. However, you still think you pick up some knowledge.\n\nMany of the spells are a bit too difficult to understand by the way they are written. However, Sidor nicely describes a few so you could understand. You can now cast \'Firestorm\' and \'Major Haste\'!")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_fire_storm")
            return
        MessageBox("Sidor\'s spellbook contains a progression of spells, from simple to extremely complex. The book was written as a reference to Sidor, not as a teaching book. However, you still think you pick up some knowledge.\n\nUnfortunately, you can only understand the simpler spells that you already know. You could probably grasp the moderately advanced ones if you had more \'Mage Lore\'.")
        return

def FortReflection_336_MapTrigger_31_57(p):
    if StuffDone["6_4"] >= 4:
        return
    if StuffDone["6_4"] < 1:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Although nobody would stop you from leaving, it would not be honorable to do so. The mages are expecting you to be at their assault.")

def FortReflection_339_MapTrigger_48_42(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["6_4"] >= 2:
        if StuffDone["-1_-1"] < 3:
            MessageBox("Now is no time to rest. Dervish Montcalm is expecting you very soon. You had better head to the portal and go through.")
            return
        result = ChoiceBox("This room has been set aside for your use. You may rest here if you like.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
        if result == 1:
            MessageBox("You have an excellent resting period. You awaken fully recovered.")
            if Game.Mode != eMode.COMBAT:
                Party.Age += 1000
                Party.HealAll(250)
                Party.RestoreSP(250)
            return
        return
    if StuffDone["6_4"] < 1:
        result = ChoiceBox("This room has been set aside for your use. You may rest here if you like.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
        if result == 1:
            MessageBox("You have an excellent resting period. You awaken fully recovered.")
            if Game.Mode != eMode.COMBAT:
                Party.Age += 1000
                Party.HealAll(250)
                Party.RestoreSP(250)
            return
        return
    result = ChoiceBox("This room has been set aside for your use. You may rest here if you like.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        if Game.Mode != eMode.COMBAT:
            Party.Age += 500
            Party.HealAll(250)
            Party.RestoreSP(250)
        Animation_Hold(-1, 023_startoutdoorcombat)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(46,43)
        Party.MoveToMap(TownMap.List["UnderSiege_23"])
        return

def FortReflection_340_MapTrigger_36_28(p):
    if StuffDone["6_4"] >= 2:
        Town.AlterTerrain(Location(36,24), 0, TerrainRecord.UnderlayList[78])
        return

def FortReflection_342_MapTrigger_36_24(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(36,24)).Num == 78:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        result = ChoiceBox("The portal quietly awaits here, ready to take you to your destination.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            Animation_Hold(-1, 010_teleport)
            Wait()
            if StuffDone["100_0"] == 2:
                StuffDone["72_6"] = 0
                StuffDone["72_7"] = 0
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(23,40)
                Party.MoveToMap(TownMap.List["BarrierSpire_20"])
                return
            Party.OutsidePos = Location(120, 120)
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(37,25)
            Party.MoveToMap(TownMap.List["Solaria_25"])
            return
        return

def FortReflection_343_MapTrigger_35_34(p):
    if StuffDone["2_0"] >= 7:
        Town.AlterTerrain(Location(36,34), 0, TerrainRecord.UnderlayList[142])
        return

def FortReflection_344_MapTrigger_40_34(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
        MessageBox("You read the spell that Dervish Montcalm\'s book is open to. It is a complex spell, but you are able to understand it. You can now cast \'Major Blessing\'!")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_major_blessing")
        return
    MessageBox("You read the spell that Dervish Montcalm\'s book is open to. The spell is quite complex and a bit over your head. You will require more \'Mage Lore\' to understand this spell.")

def FortReflection_345_MapTrigger_32_36(p):
    if StuffDone["9_0"] >= 6:
        if StuffDone["12_1"] == 0:
            StuffDone["12_1"] = 1
            ChoiceBox("You return to Dervish Montcalm\'s office. He is sitting at his desk, filling out papers. Apparently, in the wake of Halloth\'s destruction, he has returned to his administrative duties. When you look up he smiles.\n\n\"At last I can take a break from this. I almost forgot about the joys of paperwork! It almost makes me wish for some other major threat to resurface. Anyway, welcome back! And how have your adventures been?\" You tell him and he nods.\n\n\"Well I suppose we should get down to business. Back in the Wizardry Academy, I had a friend named Balkis. He was the son of an exorbitantly wealthy merchant. Very arrogant and extremely talented.\n\nWe (us mages) had to submit to certain regulations. Balkis was too independent minded, and always pushed the limits of his position. Well, our superiors finally had enough of him and he was dishonorably discharged from the academy.\n\nI had not heard from him since. But I remember he was extremely bitter about his discharge and vowed revenge against the Empire. He is talented and wealthy, I have no doubt he has the resources to carry out a plan.\n\nHe is so talented, that I doubt you will be able to handle him yourself. Don\'t get me wrong, you handled Halloth all right, but Balkis is a different story. He is a world class wizard, and the only way to fight magic is with magic.", eDialogPic.CREATURE, 27, ["OK"])
            ChoiceBox("I have done some scrying of the Fort Nether. Unfortunately, my ability to perceive much of anything was distorted by the immensely strong field surrounding the area -- presumably created by Balkis.\n\nThe field not only blocks attempts to scry its interior, but teleportation as well. So, you\'re just going to have to get in the old fashioned way. I seriously doubt that will be of a problem to you.\n\nNow we do have something to neutralize such fields.\" He produces a crystal from his robes and hands it to you. \"However, its range and duration are very limited. Especially with the talented creation we are working with.\n\nShould you face Balkis, you must shatter this crystal. Doing so will release a nullification field over a short radius. I will then be able to teleport in via our portal and assist you. Do you understand all of this?\"\n\nYou nod. \"It is an honor that we get to work together again. Best of luck and gods speed!\"", eDialogPic.CREATURE, 27, ["OK"])
            SpecialItem.Give("NullityCrystal")
            return
        if StuffDone["43_0"] == 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Montcalm_194": Town.NPCList.Remove(npc)
            return
        return

def FortReflection_346_MapTrigger_28_40(p):
    if StuffDone["43_0"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Vaila_254": Town.NPCList.Remove(npc)
        Town.PlaceEncounterGroup(2)
        return

def FortReflection_347_TownTimer_5(p):
    if StuffDone["2_1"] == 1:
        Animation_Hold(-1, 074_fireball)
        Wait()
        Animation_Explosion(Location(51,25), 0, "005_explosion")
        Animation_Hold()
        Wait()
        for ch in Town.EachCharacterInRange(Location(51,25), 1):
            ch.Damage(None, 15, 0, eDamageType.FIRE)
        Timer(Town, 5, False, "FortReflection_347_TownTimer_5", eTimerType.DELETE)
        return

def FortReflection_348_OnEntry(p):
    if StuffDone["2_0"] >= 7:
        Town.PlaceEncounterGroup(1)
        if StuffDone["12_3"] == 250:
            return
        StuffDone["12_3"] = 250
        ChoiceBox("Making your way out of the citadel is not nearly as difficult as getting in. All of Halloth\'s servants and his traps are gone. On your way out, you free the prisoners in Halloth\'s Citadel.\n\nYou leave the Citadel and head to the encampment. There you find a portal. You enter and you find yourselves back at Fort Reflection. You make your way to Dervish Montcalm\'s office. He greets you with joy.\n\n\"I knew that you would succeed! Now that Halloth is gone, our work will be much easier. As a reward, you may read the selected page on my spellbook in my quarters. Also, I have some goodies in the chest set for you.\n\nAnyway, our struggle is not over. The Troglodytes, although weakened, are still hostile towards the Empire. Unfortunately we will have to fight them until their flames of war die out.\n\nHowever, this will not be a task for you. The Empire has a much more dire mission. The Prime Director has demanded an audience with you at the Imperial Palace. You may use our portal. It will take you to Vertex, the Capital of the Empire.\n\nIt was an honor to have worked with such noble soldiers. If you continue on the path you are now, you will definitely achieve Dervishhood. I will do everything in my power to ensure that. Now, go forth and serve the Empire!\"", eDialogPic.CREATURE, 27, ["OK"])
        StuffDone["100_0"] = 3
        Animation_Hold(-1, 010_teleport)
        Wait()
        ChoiceBox("CHAPTER III - GATEWAY TO THE THRONE", eDialogPic.STANDARD, 22, ["OK"])
        return
    if StuffDone["2_0"] < 6:
        if StuffDone["5_4"] == 250:
            return
        StuffDone["5_4"] = 250
        ChoiceBox("You arrive at the lab. Several mages, including Dervish Montcalm, were waiting for you to appear. On your entrance, all the mages cheer. Except for Dervish Montcalm, who looks solemn.\n\n\"Welcome back, Guardians. Much has happened in the four days you have been gone.\" Four days! It didn\'t seem nearly that long. However, you probably spent most of the time unconscious in Azaklan.\n\n\"We had suffered no further attacks after the destruction of the Portal Fortress. During this time, we had convinced the Prime Director to spare some mages to help with the construction of Golems. We are progressing rapidly on them.\n\nIt is sad to say that Sidor\'s life was a forfeit in the attempt to rescue you. However, mourning must wait until after the true matter at hand -- the assault on Halloth\'s Citadel.\n\nFortunately, you had given us a great tradeoff for Sidor\'s sacrifice. The Troglodytes lost their two wisest and most powerful leaders. Without them, their forces are crippled! They should no longer hinder our efforts.\n\nIt is late now, and we should all retire for the night. We all need our rest for the upcoming assault. Come see me in the morning.\" You are led to your quarters and fall into a deep and comfortable sleep.", eDialogPic.CREATURE, 27, ["OK"])
        Party.HealAll(250)
        for pc in Party.EachAlivePC():
            pc.SP+= 150
        Party.Age += 1500
        return
    ChoiceBox("You awaken with a cold sweat. Dervish Montcalm is standing over you, looking fearful. \"Halloth was attacking your mind. It\'s fortunate, I showed up and was able to dispel his influence.\" So it was all a dream! Or was it...\n\n\"I can tell you believe you may be in a dream and this is a trick. But let me assure you that it is not a trick.\" You think it over and decide to trust him. \"Anyway, I have some unfortunate news to convey onto you.\n\nLast night, everything has went as planed. We were able to repair the Portal and send out some troops to scout out. However, something we had not anticipated has occurred.\n\nA massive magical barrier has appeared around Halloth\'s Citadel. That creature is pulling out all the stops to halt our attack. It shows that he fears us. It was quite easy to determine how to take out the barrier.\n\nThe barrier is emitted by four spires around the citadel. If we can break into one and smash the power source, the barrier will fall. This should not be a problem for soldiers like yourselves.\" He smiles gleefully.\n\n\"I know it\'s more than you bargained for, but all of our forces are preparing for the main assault. Meals will be brought to you. Eat them, and head off to the portal. I will meet you on the other side.\"", eDialogPic.CREATURE, 27, ["OK"])
    MessageBox("Meals are promptly brought to you. You enjoy your food greatly. A dark thought enters your mind. You realize this may be your last meal. No, you must keep a positive attitude. You are finished, time to set out to the portal.")
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Montcalm_194": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Mage_28": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Wizard_29": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Golem_196": Town.NPCList.Remove(npc)
    Party.HealAll(250)
    for pc in Party.EachAlivePC():
        pc.SP+= 150
    Party.Age += 1500

def FortReflection_349_TalkingTrigger1(p):
    if StuffDone["2_0"] == 5:
        ChoiceBox("\"Our preparations are nearing completion. Now that those filthy Troglodytes are out of the way, we should have no problem finishing our preparations. However, I suggest you prepare too.\n\nI know of an artifact that you may wish to find. When I hired those mercenaries thirty years back, they had a certain sword. This sword is a mighty weapon named after the legendary Vampyre Hunter, Lyra whose spirit lives within the blade.\n\nWhen near a powerful Vampyre such as Halloth, Lyra\'s spirit awakens and the sword will be deadly! It would definitely be an asset to have such a weapon during the combat with Halloth.\n\nUnfortunately, I do not know exactly where to find it. However, there may be somebody who does. One member of the mercenary group named Challor still lives. Last I heard he resides as a priest in the Wrynn Sector.\n\nIf you find him, he may be able to tell you where the blade is. If it is within reach, I highly suggest you get it. Also, you may have whatever is in Sidor\'s quarters just to the west. He would have wanted you to have them for the assault.\n\nOther than that, make sure you have done the usual preparations. If we fail, we won\'t get another chance!\"", eDialogPic.STANDARD, 1025, ["OK"])
        return

def FortReflection_350_TalkingTrigger3(p):
    if StuffDone["6_4"] < 1:
        result = ChoiceBox("\"We will begin launching the assault when you are prepared. Are you absolutely sure you are ready?\"", eDialogPic.STANDARD, 6, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            p.TalkingText = "\"Very well. We still have to finish repairing the portal, but we should be able to accomplish that overnight. We will be attacking midmorning. Normally we would at night, but undead do not care how bright it is.\n\nIt is getting late, you should have a rest. I will see you in the morning then.\""
            StuffDone["6_4"] = 1
            return
        return
