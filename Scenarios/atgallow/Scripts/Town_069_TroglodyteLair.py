def Generate_Wandering_69_TroglodyteLair(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteDefender_153"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteDefender_153"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteDefender_153"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["TroglodyteWarrior_150"]])
            npcs.append([1,NPCRecord.List["TroglodyteShaman_151"]])
            npcs.append([1,NPCRecord.List["TroglodyteDefender_153"]])
            npcs.append([2,NPCRecord.List["Troglodyte_149"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(43,8)
                elif r2 == 1: l = Location(27,21)
                elif r2 == 2: l = Location(44,42)
                elif r2 == 3: l = Location(25,55)
                
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

def TroglodyteLair_1712_MapTrigger_59_59(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["47_9"] = 0
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(52,9)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def TroglodyteLair_1716_MapTrigger_54_57(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. It controls the machinery to the front gate.")
        SuspendMapUpdate()
        for x in range(55, 56):
            for y in range(54, 56):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def TroglodyteLair_1717_MapTrigger_54_25(p):
    MessageBox("This lever has been smashed. The mechanism is clearing broken. Pull it all you want, nothing is going to happen.")

def TroglodyteLair_1718_MapTrigger_13_52(p):
    MessageBox("This is a body of a young male human. He was slain by a severe puncture wound to the chest appearing to have been caused by a javelin.")

def TroglodyteLair_1719_SanctifyTrigger_19_48(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["47_7"] == 0:
        StuffDone["47_7"] = 1
        Town.AlterTerrain(Location(19,48), 0, TerrainRecord.UnderlayList[166])
        Animation_Explosion(Location(19,48), 0, "005_explosion")
        Animation_Hold()
        Wait()
        MessageBox("You cast the ritual of sanctification and shatter the dark Troglo altar. You feel very much rewarded for slaying this tool of evil.")
        for pc in Party.EachAlivePC():
            pc.AwardXP(20)
        return

def TroglodyteLair_1720_MapTrigger_24_48(p):
    if StuffDone["47_7"] == 1:
        Town.AlterTerrain(Location(19,48), 0, TerrainRecord.UnderlayList[166])
        return

def TroglodyteLair_1721_MapTrigger_17_32(p):
    MessageBox("You have slain the leader of the Troglodytes! Without his leadership, the Troglodyte\'s presence in the area is bound to be weakened. You have just made life easier for the Hill Giants.")
    StuffDone["48_4"] = 1

def TroglodyteLair_1722_MapTrigger_21_35(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a soft click upon pulling the lever. You have no idea what, if anything, was done by doing this.")
        SuspendMapUpdate()
        for x in range(47, 48):
            for y in range(54, 56):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetLocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def TroglodyteLair_1723_MapTrigger_22_35(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a soft click upon pulling the lever. You have no idea what, if anything, was done by doing this.")
        t = Town.TerrainAt(Location(30,36)).TransformTo
        Town.AlterTerrain(Location(30,36), 0, t)
        return

def TroglodyteLair_1724_MapTrigger_23_35(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a soft click upon pulling the lever. You have no idea what, if anything, was done by doing this.")
        Town.PlaceEncounterGroup(1)
        return

def TroglodyteLair_1725_MapTrigger_24_35(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a soft click upon pulling the lever. You have no idea what, if anything, was done by doing this.")
        if StuffDone["47_9"] == 0: StuffDone["47_9"] = 1
        else: StuffDone["47_9"] = 0
        return

def TroglodyteLair_1726_MapTrigger_8_58(p):
    if StuffDone["47_9"] == 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(30,36)).Num == 130:
            MessageBox("One moment you are walking down this hall, the next, you are in some laboratory. The first thing you notice is a Troglodyte Khazi. However, she seems to only casually notice you, as if she didn\'t care about your presence.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Animation_Vanish(Party.LeaderPC, True, "010_teleport")
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(6,39))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            p.CancelAction = True
            return
        return

def TroglodyteLair_1727_MapTrigger_6_40(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(8,58))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TroglodyteLair_1728_MapTrigger_33_35(p):
    if StuffDone["48_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The Troglodytes were not foolish in leaving their valuable loot undefended. They have managed to rig up some fairly complicated magical trap. You shall need to disarm it to gain the contents of this chest.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The Troglodytes were not foolish in leaving their valuable loot undefended. They have managed to rig up some fairly complicated magical trap. You shall need to disarm it to gain the contents of this chest.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["48_1"] = 250
    TownMap.List["TroglodyteLair_69"].DeactivateTrigger(Location(33,35))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 75)

def TroglodyteLair_1729_MapTrigger_33_36(p):
    if StuffDone["48_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The Troglodytes were not foolish in leaving their valuable loot undefended. They have managed to rig up some fairly complicated magical trap. You shall need to disarm it to gain the contents of this chest.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The Troglodytes were not foolish in leaving their valuable loot undefended. They have managed to rig up some fairly complicated magical trap. You shall need to disarm it to gain the contents of this chest.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["48_2"] = 250
    TownMap.List["TroglodyteLair_69"].DeactivateTrigger(Location(33,36))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 75)

def TroglodyteLair_1730_MapTrigger_33_37(p):
    if StuffDone["48_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The Troglodytes were not foolish in leaving their valuable loot undefended. They have managed to rig up some fairly complicated magical trap. You shall need to disarm it to gain the contents of this chest.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The Troglodytes were not foolish in leaving their valuable loot undefended. They have managed to rig up some fairly complicated magical trap. You shall need to disarm it to gain the contents of this chest.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["48_3"] = 250
    TownMap.List["TroglodyteLair_69"].DeactivateTrigger(Location(33,37))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 75)

def TroglodyteLair_1731_MapTrigger_34_2(p):
    MessageBox("This chest has been smashed open and all of the contents that were inside have been looted. Looks like the giants got to this one first.")

def TroglodyteLair_1734_MapTrigger_14_13(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
        MessageBox("Although most of these spell books have been torn apart by the giants, they missed a few. You page through them in the hopes that you might find some powerful spell or something.\n\nMost of these books are quite dry and about magic theory. However, there is one spell book that teaches complex arcane spells. Most of them are out of your reach, but you manage to learn the spell \'Death Arrows\'!")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_death_arrows")
        return
    MessageBox("Although most of these spell books have been torn apart by the giants, they missed a few. You page through them in the hopes that you might find some powerful spell or something.\n\nMost of these books are quite dry and about magic theory. However, there is one spell book which is quite arcane and way over your head. You will need more Mage Lore to understand it.")

def TroglodyteLair_1735_MapTrigger_13_15(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 15:
        MessageBox("Although most of these spell books have been torn apart by the giants, they missed a few. You page through them in the hopes that you might find some powerful spell or something.\n\nMost of these books are dry and about magic theory. However, there is one arcane book on alchemy that has some bizarre recipes. One that may be of use to you is the secret of \'Killer Poison\'.")
        Party.LearnRecipe("killer_poison")
        return
    MessageBox("Although most of these spell books have been torn apart by the giants, they missed a few. You page through them in the hopes that you might find some powerful spell or something.\n\nMost of these books are quite dry and about magic theory. However, there is one spell book which is quite arcane and way over your head. You will need more Mage Lore to understand it.")

def TroglodyteLair_1736_MapTrigger_13_13(p):
    MessageBox("At one time this was a valuable library of magical knowledge. However, the giants managed to get to these works and thoroughly destroyed them. Pity, they could have been of great use to you.")

def TroglodyteLair_1740_MapTrigger_9_25(p):
    if StuffDone["48_4"] == 1:
        Town.AlterTerrain(Location(6,12), 0, TerrainRecord.UnderlayList[0])
        return

def TroglodyteLair_1743_MapTrigger_8_2(p):
    MessageBox("The leader of the Troglodytes managed to survive the giant\'s devastating raid, but he could not duplicate the feat with your assault. With the Troglodyte leader dead, the giants have a much better position.")

def TroglodyteLair_1746_TalkingTrigger2(p):
    if StuffDone["48_0"] == 0:
        if Party.CountItemClass(34, False) > 0:
            result = ChoiceBox("You seem to have the horn of a Golden Unicorn with you. The Khazi smiles. \"That horn will be very helpful. If you give it to me, I shall teach you an ancient secret of alchemy in return.\"", eDialogPic.CREATURE, 149, ["Give", "Keep"])
            if result == 0:
                if Party.CountItemClass(34, True) > 0:
                    Sound.Play(040_thankyou)
                    p.TalkingText = "You hand her the horn. \"Now, a deal is a deal. I shall teach you the secret of making medium strength skill potions. Allow me to teach you the recipe...\""
                    StuffDone["48_0"] = 1
                    return
                return
            elif result == 1:
                p.TalkingText = "You decide not to give up your horn. The Troglodyte looks frustrated. \"I can guarantee you that the secret is well worth the horn, in fact, the secret is much more valuable than that silly horn.\""
                return
            return
        return
    p.TalkingText = "\"Thank you. The horn was very useful. Would you like to go through the recipe of the medium skill potion?\""

def TroglodyteLair_1747_TalkingTrigger3(p):
    if StuffDone["48_0"] == 1:
        ChoiceBox("It takes her several minutes to make the appropriate setup. It is fairly complicated, but she explains it in detail to you. She then fishes out some rare ingredients and reagents and shows you the complex process.\n\nShe has you run through it several times before she is confident that you have adequately learned the recipe. She tells you a few words.\n\n\"Just remember that to make the potion you shall need a stable laboratory to work in. This is very unlike the simpler potions that you are accustomed to in that respect. However, the lab should have all the common reagents.\n\nYou will probably need to supply the rarer ingredients. Just remember these are Ambrosia, Mandrake Root, and Quicksilver. If you forget part of the recipe, just return here and I\'ll go through it with you again.\"", eDialogPic.STANDARD, 20, ["OK"])
        p.TalkingText = "You conclude your business."
        return
