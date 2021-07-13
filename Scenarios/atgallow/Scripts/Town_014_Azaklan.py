def Generate_Wandering_14_Azaklan(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["TroglodyteKhazi_152"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["TroglodyteDefender_153"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["TroglodyteKhazi_152"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["TroglodyteKhazi_152"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(32,43)
                elif r2 == 1: l = Location(53,36)
                elif r2 == 2: l = Location(12,36)
                elif r2 == 3: l = Location(32,21)
                
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

def Azaklan_222_MapTrigger_4_51(p):
    if StuffDone["4_4"] >= 5:
        if Game.Mode == eMode.COMBAT:
            return;
        Animation_Hold(-1, 013_partydeath)
        Wait()
        MessageBox("Nycraogos speaks, \"That is enough. You will now be transferred to your cells where you will await your ultimate fate.\" The runes begin to glow, your bodies wrack with pain, everything goes black!")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(22,55))
        p.CancelAction = True
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Nycraogos_210": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Vulcaroc_211": Town.NPCList.Remove(npc)
        ChoiceBox("You awaken who knows how long later in a small cell full of uncomfortable beds. You instantly notice that you have collars around your necks -- the same collar that you saw the Nephil wearing. Your equipment remains, not that it really matters.\n\nThe entrance has one of those shocking runes blocking it. This cell was designed not to allow your escape. You begin to ponder about the mention of that Morbane. The name sounds familiar to you.\n\nThen it hits you. Morbane is the same god that the cult you defeated back in the Agran Sector worshiped! This Morbane creature also summoned Halloth back from the void. You wonder what this all means.\n\nYou hear voices outside your cell. One is that of Nycraogos, the other is one you do not recognize. \"So Sephoth, how does the rewriting of prayer books go?\", inquires the familiar voice of Nycraogos.\n\nThe other replies, \"Fine, master. Soon all of the prayer books will be updated to give praise to Morbane. My one concern is that many people will see this as heresy and not follow.\"\n\nNycraogos rebuts, \"You know little of our people. They will believe as we tell them. It just may take time. But soon, we will return to the glory days of our people. Now for those prisoners.\"", eDialogPic.CREATURE, 115, ["OK"])
        ChoiceBox("The rune deactivates and the two Khazis enter. You instinctively reach for your weapons but Nycraogos waves you down. \"Do not bother. Those collars will effectively inhibit you from doing anything.\" You put down your weapons.\n\n\"I would like you to meet one of my students, Sephoth.\" Sephoth bows. \"He will be conducting research on you for the next few hours. I suggest you cooperate as we can make this even more painful than it has to be.\"\n\nYou decide to cooperate and are led back to the lab. On one of the tables, you see the dissected remains of that Nephil prisoner you had spoken with earlier. Apparently, she had met her grizzly fate. A fate, you believe you will soon meet.\n\nAfter hours of painful tests with several vials of strange potions, you are returned to your cell exhausted. You instantly fall asleep and awaken the next morning. Someone has left food for you to eat.\n\nIt doesn\'t look appetizing at all, but it\'s the best you\'ve got. Things are starting to look pretty bleak for you right now. You wonder how the soldiers at Fort Reflection are doing. You know that you\'ll probably never find out.\n\nYou look up to see Sephoth standing outside your cell. He\'s probably waiting to do more studying on you.", eDialogPic.CREATURE, 115, ["OK"])
        StuffDone["4_4"] += 1
        if StuffDone["4_4"] == 250:
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))
        return
    if StuffDone["4_4"] < 1:
        ChoiceBox("After a rough ride through the crudely linked portal, you find yourselves in a cell of glowing runes. The runes give off sparks, so you can bet it would not be a good idea to cross them. It looks like you\'re trapped in this prison.\n\nYou have not seen this place before. You doubt that this is in some part of Fort Reflection that you have not been, but you can hope. All you can do now is hope you are not in hostile hands.\n\nBut you wonder, who else would create a portal allowing your escape from the crumbling Portal Fortress? You would think anyone hostile would have let you perish, or would they?\n\nAs your vision begins to clear up, you notice a haggard Nephilim watching you in an adjacent cell. You call him over. He moves to the edge of his cell, careful not to come into contact with the runes.\n\nPerhaps you can get a few questions answered.", eDialogPic.STANDARD, 6, ["OK"])
        StuffDone["4_4"] += 1
        if StuffDone["4_4"] == 250:
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))
        return

def Azaklan_231_MapTrigger_18_56(p):
    if StuffDone["4_4"] == 6:
        MessageBox("You approach the edge of the cell, Sephoth deactivates the rune. You inquire about more tests, but he shakes his head. \"Master Vulcaroc has promised you torture for the destruction of the Portal Fortress, you will be receiving that now.\"")
        Animation_Hold(-1, 010_teleport)
        Wait()
        Animation_Hold(-1, 074_fireball)
        Wait()
        Animation_Hold(-1, 005_explosion)
        Wait()
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Sephoth_212": Town.NPCList.Remove(npc)
        Town.AlterTerrain(Location(16,56), 0, TerrainRecord.UnderlayList[165])
        Animation_Explosion(Location(16,56), 2, "005_explosion")
        Animation_Hold()
        Wait()
        Animation_Hold(-1, 029_monsterdeath2)
        Wait()
        ChoiceBox("Suddenly, you hear the sound of teleportation followed by an explosion that sounds like a firestorm spell. You hear several screams from the room to the north. Sephoth looks and screams as he is pierced by a kill spell.\n\nYou now see what happened. Sidor has come to rescue you! \"We managed to break the anti-teleportation field around this place. We must hurry, the escape will not last very long.\" Sidor casts a spell to break your collars and runs north.\n\nPerhaps hope is not lost. You may now be able to break out of Azaklan!", eDialogPic.CREATURE, 28, ["OK"])
        StuffDone["4_4"] += 1
        if StuffDone["4_4"] == 250:
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))
        return

def Azaklan_232_MapTrigger_53_19(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["4_8"] == 250:
        return
    StuffDone["4_8"] = 250
    MessageBox("You have just interrupted a meeting between Vulcaroc and two of his generals. He looks at you in anger, \"Ah creatures! We were just discussing your fate. It looks like we\'ve just come to a conclusion!\" They attack.")
    Town.PlaceEncounterGroup(3)

def Azaklan_234_MapTrigger_15_47(p):
    if StuffDone["4_4"] == 7:
        Town.AlterTerrain(Location(13,45), 0, TerrainRecord.UnderlayList[170])
        if Maths.Rand(1,0,100) <= 100:
            Town.PlaceField(Location(13,45), Field.CRATER)
        Animation_Explosion(Location(13,45), 2, "005_explosion")
        Animation_Hold()
        Wait()
        Town.PlaceEncounterGroup(2)
        Animation_Explosion(Location(14,45), 1, "005_explosion")
        Animation_Hold()
        Wait()
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Sidor_195": Town.NPCList.Remove(npc)
        Town.AlterTerrain(Location(14,46), 0, TerrainRecord.UnderlayList[165])
        Animation_Explosion(Location(14,46), 0, "005_explosion")
        Animation_Hold()
        Wait()
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Nycraogos_210": Town.NPCList.Remove(npc)
        Animation_Explosion(Location(14,45), 1, "005_explosion")
        Animation_Hold()
        Wait()
        ChoiceBox("As you near the portal, it explodes sending out a numbing shockwave. The wave leaves you completely helpless to watch the action unfold. Nycraogos teleports in and begins to duel Sidor.\n\nThe duel does not take too long, but Sidor loses. The wounded and drained Nycraogos stares at you. \"This is your lucky day creatures. I\'m too weak to take you on now, I\'ll just have to let my soldiers kill you.\" Nycraogos teleports away.\n\nYou go to Sidor\'s body. He is barely alive but can still speak. \"Well it looks like I was a bit too slow. They managed to destroy our escape route and that Khazi did a number on me. But, I returned the favor.\n\nListen carefully, we had planned what to do in case they destroyed the portal. The reason we didn\'t come sooner was because of the strong anti-teleportation field around this place. We managed to puncture a hole, but it was repaired.\n\nIt can be brought down if you take out the source. The Khazi\'s have a small hidden shrine where they pray to Halloth (not the main shrine for the regular Troglos). It radiates the field. If it is destroyed, we may be able to get you out.\n\nIt looks like the assault will have to go on without me...\" Sidor dies. Well, your hopes went from bleak, to high, to not so great again. However, you now have a method for escape.", eDialogPic.CREATURE, 115, ["OK"])
        StuffDone["4_4"] += 1
        if StuffDone["4_4"] == 250:
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))
        return

def Azaklan_236_MapTrigger_44_58(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(44,57)).Num == 145:
        if SpecialItem.PartyHas("MalachiteKey"):
            MessageBox("This door is locked. Fortunately, you have the key to open it.")
            t = Town.TerrainAt(Location(44,57))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(44,57)).TransformTo
                Town.AlterTerrain(Location(44,57), 0, t)
            return
        MessageBox("This door is locked. Unfortunately, you will require a key and you do not have it.")
        return

def Azaklan_237_MapTrigger_50_43(p):
    if StuffDone["5_0"] == 0:
        StuffDone["5_0"] = 1
        Animation_Hold(-1, 004_bless)
        Wait()
        Town.PlaceEncounterGroup(4)
        ChoiceBox("You hear the sound of a spell cast behind you. You turn around and see only an empty table. You hear the familiar voice of Nycraogos, \"Going somewhere?\" His invisibility spell fades away and you see him sitting at the table.\n\n\"My, my, you\'ve caused much trouble for us. Not only have you destroyed our Portal Fortress, you\'ve killed the commander of our armies. But, no matter, Vulcaroc was an arrogant fool anyway and will be easily replaced.\n\nHowever, I cannot let you destroy master Halloth\'s altar.\" You look behind Nycraogos and see a suit of armor. It begins to glow and start moving toward you! It doesn\'t look that difficult to destroy.\n\n\"Not impressed, eh? Ever heard of a Doomguard? No? Well, you will be!\"", eDialogPic.CREATURE, 115, ["OK"])
        return

def Azaklan_238_MapTrigger_51_44(p):
    if StuffDone["5_0"] == 1:
        Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.FIRE)
        Wait()
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange forcefield holds you back.")
        return

def Azaklan_243_SanctifyTrigger_57_44(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["5_2"] < 10:
        StuffDone["5_2"] = 10
        ChoiceBox("Your assault on the altar disrupted it. Several cracks for on its surface and a black smoke pours out. The altar is dead! You sure hope that the mages back at Fort Reflection can ensure your escape soon.", eDialogPic.TERRAIN, 159, ["OK"])
        Timer(Town, 10, False, "Azaklan_259_TownTimer_62", eTimerType.DELETE)
        return

def Azaklan_244_MapTrigger_57_44(p):
    if StuffDone["5_2"] < 10:
        result = ChoiceBox("This must be the Triad\'s altar that Sidor told you about in his dying words. It radiates evil energy. You are sure that this altar has its defenses. Try to destroy the altar?", eDialogPic.TERRAIN, 159, ["Leave", "Destroy"])
        if result == 1:
            if StuffDone["5_2"] >= 2:
                if StuffDone["5_2"] >= 4:
                    if StuffDone["5_2"] >= 6:
                        if StuffDone["5_2"] >= 8:
                            if StuffDone["5_2"] < 9:
                                Party.Damage(Maths.Rand(3, 1, 5) + 10, eDamageType.FIRE)
                                Wait()
                                MessageBox("You strike the altar, flames pour out and engulf you.")
                                Party.Damage(Maths.Rand(3, 1, 5) + 10, eDamageType.FIRE)
                                Wait()
                                StuffDone["5_2"] += 1
                                if StuffDone["5_2"] == 250:
                                    pass
                                return
                            StuffDone["5_2"] = 10
                            ChoiceBox("Your assault on the altar disrupted it. Several cracks for on its surface and a black smoke pours out. The altar is dead! You sure hope that the mages back at Fort Reflection can ensure your escape soon.", eDialogPic.TERRAIN, 159, ["OK"])
                            Timer(Town, 10, False, "Azaklan_259_TownTimer_62", eTimerType.DELETE)
                            return
                        if StuffDone["5_2"] < 7:
                            MessageBox("You strike the altar again. This time poisonous gas pours out of the stone! However, you have managed to make another dent in the stone.")
                            for pc in Party.EachAlivePC():
                                pc.Poison(8)
                            StuffDone["5_2"] += 1
                            if StuffDone["5_2"] == 250:
                                pass
                            return
                        MessageBox("You strike the altar again, knocking away a large chunk. However, you feel the altar begin to drain you of all of your life force. You are left alive, but barely.")
                        Party.HealAll(-250)
                        StuffDone["5_2"] += 1
                        if StuffDone["5_2"] == 250:
                            pass
                        return
                    if StuffDone["5_2"] < 5:
                        MessageBox("You strike the altar and are thrown back by a bolt of electricity. However, you have succeeded in scarring the stone.")
                        Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.MAGIC)
                        Wait()
                        StuffDone["5_2"] += 1
                        if StuffDone["5_2"] == 250:
                            pass
                        return
                    MessageBox("You strike the altar again and this time it sends out a powerful wave of mental energy. You end up with massive headaches.")
                    for pc in Party.EachAlivePC():
                        pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 7))
                    StuffDone["5_2"] += 1
                    if StuffDone["5_2"] == 250:
                        pass
                    return
                if StuffDone["5_2"] < 3:
                    Animation_Hold(-1, 005_explosion)
                    Wait()
                    MessageBox("You strike the altar yet again. This time it glows a deep red. Two fireballs shoot out from the stone and land on the floor to your sides. The flames form into two demons!")
                    Town.PlaceEncounterGroup(5)
                    StuffDone["5_2"] += 1
                    if StuffDone["5_2"] == 250:
                        pass
                    return
                MessageBox("You strike the altar and are thrown back by a bolt of electricity. However, you have succeeded in scarring the stone.")
                Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.MAGIC)
                Wait()
                StuffDone["5_2"] += 1
                if StuffDone["5_2"] == 250:
                    pass
                return
            if StuffDone["5_2"] < 1:
                MessageBox("You strike the altar and are thrown back by a bolt of electricity. However, you have succeeded in scarring the stone.")
                Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.MAGIC)
                Wait()
                StuffDone["5_2"] += 1
                if StuffDone["5_2"] == 250:
                    pass
                return
            MessageBox("You strike the altar again. This time poisonous gas pours out of the stone! However, you have managed to make another dent in the stone.")
            for pc in Party.EachAlivePC():
                pc.Poison(8)
            StuffDone["5_2"] += 1
            if StuffDone["5_2"] == 250:
                pass
            return
        return

def Azaklan_245_MapTrigger_57_48(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(57,48)).Num == 78:
        result = ChoiceBox("This small portal awaits your entry. It will probably take you back to Fort Reflection, but it could be another trick. This is probably your only hope for escape.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            MessageBox("You hold your breath and jump in hoping that it will take you back into friendly hands. This ride is probably your most traumatic yet, you are torn apart and flung far away. You rematerialize in a familiar lab.")
            StuffDone["2_0"] = 5
            StuffDone["2_2"] = 2
            Animation_Hold(-1, 010_teleport)
            Wait()
            Party.OutsidePos = Location(70, 123)
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(48,42)
            Party.MoveToMap(TownMap.List["FortReflection_17"])
            return
        return

def Azaklan_246_MapTrigger_48_58(p):
    MessageBox("This door is locked. Unfortunately, you will require a key and you do not have it.")

def Azaklan_248_MapTrigger_2_24(p):
    result = ChoiceBox("You have found a Troglodyte spellbook. It could be full of valuable spells. But then again, it could be trapped.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
            MessageBox("You flip through the prayer book. It is full of religious enchantments and rituals of no use to you. However, there is a section on that may be of use.\n\nMost of the rituals are a bit too esoteric to be of use to soldiers like yourselves. However, the prayer \'Summon Host\' is efficient enough that it may be of some use.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("p_summon_host")
            return
        MessageBox("You flip through the prayer book. It is full of religious enchantments and rituals of no use to you. However, there is a section on that may be of use.\n\nUnfortunately, the rituals are a bit too esoteric for you. There are a few \'simpler\' ones, but you lack the \'Mage Lore\' to understand them.")
        return

def Azaklan_249_MapTrigger_55_60(p):
    result = ChoiceBox("You have found a Troglodyte spellbook. It could be full of valuable spells. But then again, it could be trapped.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
            MessageBox("You flip through the prayer book. It is full of religious enchantments and rituals of no use to you. However, there is a section on that may be of use.\n\nHowever, Nycraogos did keep track of a few powerful rituals. One of them, called \'Wall of Blades\', is within your reach!")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("p_wall_of_blades")
            return
        MessageBox("You flip through the prayer book. It is full of religious enchantments and rituals of no use to you. However, there is a section on that may be of use.\n\nUnfortunately, the rituals are a bit too esoteric for you. There are a few \'simpler\' ones, but you lack the \'Mage Lore\' to understand them.")
        return

def Azaklan_250_MapTrigger_31_5(p):
    ChoiceBox("You peer out the gates. The road slopes down to the north and leads into a massive underground Troglodyte city! There must be at least a thousand Troglos living there. You have heard the Troglos reproduce quickly, you are guessing that is correct.\n\nEven if you could leave this fortress, there is no way you could make it through that massive cloud of Troglos. Everyone who told you escape or rescue was futile, was probably correct.\n\nBut, there is still hope of proving them all wrong!", eDialogPic.CREATURE, 112, ["OK"])

def Azaklan_253_MapTrigger_57_51(p):
    if StuffDone["5_3"] == 250:
        return
    StuffDone["5_3"] = 250
    TownMap.List["Azaklan_14"].DeactivateTrigger(Location(57,51))
    TownMap.List["Azaklan_14"].DeactivateTrigger(Location(57,52))
    TownMap.List["Azaklan_14"].DeactivateTrigger(Location(57,53))
    MessageBox("In back of the fortress is a small dock with a boat that can seat four people. You would guess that the Troglodyte Triad has wisely left an escape route just in case. There are runes blocking it, so you won\'t be able to use it.")

def Azaklan_256_MapTrigger_55_56(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(55,57)).Num == 145:
        MessageBox("This door is locked. Unfortunately, you will require a key and you do not have it.")
        return

def Azaklan_258_TownTimer_4(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Nephil_40": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(1)
    ChoiceBox("You hear two Troglodytes talking outside. The conversation sounds pretty important so you listen in.\n\n\"I really don\'t see why we took the effort to get those creatures here, Nycraogos. We should have let them perish in the destruction of our brilliant Portal. I think bringing them here is a waste of time.\"\n\nNycraogos replies, \"Ah Vulcaroc, I would normally agree with you, but the master requested it.\" Vulcaroc asks, \"Master Halloth himself requested they be taken prisoners?\" Nycraogos answers, \"No, the request came from even higher.\"\n\nVulcaroc sounds surprised, \"The master\'s master requested it!? What use would the almighty Morbane have for these creatures?\" Nycraogos answers, \"I don\'t know, all I know is we were to hold them until further orders.\"\n\nVulcaroc inquires, \"What is this Morbane anyway?\" Nycraogos sighs. \"I have questioned Halloth, all I know is that it is an all powerful ancient spirit that summoned back Halloth from the void. I know nothing more.\"\n\nThe two enter the room. The Khazi speaks, \"And who do we have here? Those villains who destroyed our portal I presume. I am Nycraogos and this is Vulcaroc. We have come to speak with you.\"", eDialogPic.CREATURE, 115, ["OK"])
    StuffDone["4_4"] += 1
    if StuffDone["4_4"] == 250:
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))

def Azaklan_259_TownTimer_62(p):
    Animation_Hold(-1, 051_magic1)
    Wait()
    MessageBox("Suddenly, a small portal materializes by the southern wall of the chamber. You are pretty sure this won\'t land you into any more trouble. However, you still recall the last time you used a mysterious portal.")
    Town.AlterTerrain(Location(57,48), 0, TerrainRecord.UnderlayList[78])

def Azaklan_260_CreatureDeath0(p):
    if StuffDone["4_4"] == 1:
        Timer(Town, 8, False, "Azaklan_258_TownTimer_4", eTimerType.DELETE)
        StuffDone["4_4"] += 1
        if StuffDone["4_4"] == 250:
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
            TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))
        return

def Azaklan_261_CreatureDeath1(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Nycraogos_210": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Vulcaroc_211": Town.NPCList.Remove(npc)
    ChoiceBox("You awaken who knows how long later in a small cell full of uncomfortable beds. You instantly notice that you have collars around your necks -- the same collar that you saw the Nephil wearing. Your equipment remains, not that it really matters.\n\nThe entrance has one of those shocking runes blocking it. This cell was designed not to allow your escape. You begin to ponder about the mention of that Morbane. The name sounds familiar to you.\n\nThen it hits you. Morbane is the same god that the cult you defeated back in the Agran Sector worshiped! This Morbane creature also summoned Halloth back from the void. You wonder what this all means.\n\nYou hear voices outside your cell. One is that of Nycraogos, the other is one you do not recognize. \"So Sephoth, how does the rewriting of prayer books go?\", inquires the familiar voice of Nycraogos.\n\nThe other replies, \"Fine, master. Soon all of the prayer books will be updated to give praise to Morbane. My one concern is that many people will see this as heresy and not follow.\"\n\nNycraogos rebuts, \"You know little of our people. They will believe as we tell them. It just may take time. But soon, we will return to the glory days of our people. Now for those prisoners.\"", eDialogPic.CREATURE, 115, ["OK"])
    ChoiceBox("The rune deactivates and the two Khazis enter. You instinctively reach for your weapons but Nycraogos waves you down. \"Do not bother. Those collars will effectively inhibit you from doing anything.\" You put down your weapons.\n\n\"I would like you to meet one of my students, Sephoth.\" Sephoth bows. \"He will be conducting research on you for the next few hours. I suggest you cooperate as we can make this even more painful than it has to be.\"\n\nYou decide to cooperate and are led back to the lab. On one of the tables, you see the dissected remains of that Nephil prisoner you had spoken with earlier. Apparently, she had met her grizzly fate. A fate, you believe you will soon meet.\n\nAfter hours of painful tests with several vials of strange potions, you are returned to your cell exhausted. You instantly fall asleep and awaken the next morning. Someone has left food for you to eat.\n\nIt doesn\'t look appetizing at all, but it\'s the best you\'ve got. Things are starting to look pretty bleak for you right now. You wonder how the soldiers at Fort Reflection are doing. You know that you\'ll probably never find out.\n\nYou look up to see Sephoth standing outside your cell. He\'s probably waiting to do more studying on you.", eDialogPic.CREATURE, 115, ["OK"])
    StuffDone["4_4"] += 1
    if StuffDone["4_4"] == 250:
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))

def Azaklan_263_CreatureDeath6(p):
    MessageBox("You\'ve just slain the mighty Vulcaroc, member of the Troglodyte Triad and traitor to the Empire. You search his body and find a small key in his pocket. Perhaps it will be useful.")
    SpecialItem.Give("MalachiteKey")

def Azaklan_264_CreatureDeath9(p):
    MessageBox("You strike the final blow to Nycraogos. In the wake of his death, his body disintegrates into ash. Also, the Doomguard loses its magic and vanishes. You notice a small key in the pile of ash.\n\nWell, you have really dealt the Troglos another setback. You have killed their general as well as their high priest. However, that may all be in vain if you cannot find an escape.")
    StuffDone["5_0"] = 2
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Doomguard_123": Town.NPCList.Remove(npc)
    SuspendMapUpdate()
    for x in range(50, 57):
        for y in range(57, 63):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[142]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[145])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[145]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[142])
    ResumeMapUpdate()

def Azaklan_266_TalkingTrigger18(p):
    if StuffDone["4_6"] == 250:
        return
    StuffDone["4_6"] = 250
    StuffDone["4_4"] += 1
    if StuffDone["4_4"] == 250:
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))

def Azaklan_267_TalkingTrigger25(p):
    if StuffDone["4_7"] == 250:
        return
    StuffDone["4_7"] = 250
    StuffDone["4_4"] += 1
    if StuffDone["4_4"] == 250:
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,51))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,52))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(4,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(5,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(6,53))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,56))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(18,57))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(15,47))
        TownMap.List["Azaklan_14"].DeactivateTrigger(Location(16,47))
