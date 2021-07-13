def Generate_Wandering_16_PitofPlentifulGoo(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([2,NPCRecord.List["ArmoredSlime_138"]])
        elif r1 == 1:
            npcs.append([2,NPCRecord.List["SearingSlime_139"]])
        elif r1 == 2:
            npcs.append([2,NPCRecord.List["SuckingSlime_140"]])
        elif r1 == 3:
            npcs.append([2,NPCRecord.List["SmartSlime_141"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(25,25)
                elif r2 == 1: l = Location(38,16)
                elif r2 == 2: l = Location(20,21)
                elif r2 == 3: l = Location(7,15)
                
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

def PitofPlentifulGoo_202_MapTrigger_12_2(p):
    result = ChoiceBox("You find a metal strongbox. A small sign on it reads \"PROTECTIVE AMULETS - DO NOT proceed through caves without wearing one.\"", eDialogPic.TERRAIN, 178, ["Leave", "Open"])
    if result == 1:
        MessageBox("The box contains a rack, which looks like it was designed to hold about a dozen necklaces. Considering how the day has gone, you won\'t be surprised to hear that the rack is empty. Disgusted, you close the box.")
        return

def PitofPlentifulGoo_204_MapTrigger_35_22(p):
    result = ChoiceBox("You find a heavy metal strongbox, bolted to the floor. To protect it from the acidic secretions of the slimes, it has been coated with a thin layer of glass. A sign on the front reads \"Sample Storage.\"", eDialogPic.TERRAIN, 178, ["Leave", "Open"])
    if result == 1:
        MessageBox("The box contains several racks of vials. At first, excited, you think you\'ve found a treasure trove of potions. Unfortunately, a closer look reveals that all the bottles contain are bits of the slimes, scraped off for later analysis.\n\nAnnoyed, disappointed, and slightly disgusted, you close the box.")
        return

def PitofPlentifulGoo_207_MapTrigger_10_31(p):
    result = ChoiceBox("You find a heavy metal strongbox, bolted to the floor. To protect it from the acidic secretions of the slimes, it has been coated with a thin layer of glass. A sign on the front reads \"Sample Storage.\"", eDialogPic.TERRAIN, 178, ["Leave", "Open"])
    if result == 1:
        if StuffDone["16_0"] >= 1:
            MessageBox("The box still contains broken bottles of nasty goo. Fortunately, this time no little gelatinous friends are attracted by the smell.")
            return
        if StuffDone["16_0"] == 250:
            return
        StuffDone["16_0"] = 250
        MessageBox("You open the box and immediately wish you hadn\'t. The box is filled with bottles of slime, used by the mages for analysis. Unfortunately, some sort of sharp blow has broken several of them open, and the smell of rotting goop is overpowering.\n\nYou\'re not the only beings to have noticed it, either. The smell seems to have attracted several slimes, and put them in a rather agitated state.")
        Town.PlaceEncounterGroup(1)
        return

def PitofPlentifulGoo_208_MapTrigger_9_42(p):
    if StuffDone["16_1"] == 250:
        return
    StuffDone["16_1"] = 250
    TownMap.List["PitofPlentifulGoo_16"].DeactivateTrigger(Location(9,42))
    ChoiceBox("Well, you\'ve solved the mystery of what happened to the mages who were doing research here. Actually, your nose tells you before your eyes do. They\'re all in here and quite thoroughly dead.\n\nThe burns on their bodies look like they were inflicted by the highly acidic slimes, so it seems likely that the slimes got them all.\n\nHowever, you can\'t help but wonder what they were all doing out here in this cave, and how the slimes were able to best them. They were, after all, quite skilled magic users, and the slimes aren\'t that tough.\n\nYet another mystery, and yet more dead people. This island is starting to depress you.", eDialogPic.TERRAIN, 179, ["OK"])

def PitofPlentifulGoo_209_MapTrigger_14_39(p):
    if StuffDone["16_3"] == 250:
        return
    StuffDone["16_3"] = 250
    TownMap.List["PitofPlentifulGoo_16"].DeactivateTrigger(Location(14,39))
    MessageBox("Your gorge rising, you pick through the stuff on the corpse. Your gross and thankless task is rewarded: you find a small silver key. You wipe it off and take it with you.")
    SpecialItem.Give("SlimeKey2")

def PitofPlentifulGoo_210_MapTrigger_24_44(p):
    if StuffDone["16_2"] == 250:
        return
    StuffDone["16_2"] = 250
    TownMap.List["PitofPlentifulGoo_16"].DeactivateTrigger(Location(24,44))
    MessageBox("You find the body of one of the mages who was working here. It looks like she was ambushed by several of the treacherous giant slimes, and killed in an exceptionally nasty way.\n\nOn a thin chain around her neck, you find a small pewter key. Never hurts to have more keys. You take it.")
    SpecialItem.Give("SlimeKey1")

def PitofPlentifulGoo_211_MapTrigger_34_13(p):
    if StuffDone["16_4"] == 250:
        return
    StuffDone["16_4"] = 250
    TownMap.List["PitofPlentifulGoo_16"].DeactivateTrigger(Location(34,13))
    ChoiceBox("You find a small, hastily built subterranean structure. It looks like it was thrown together very quickly, and pillars have been placed everywhere to shore the ceiling up.\n\nLooking down this long corridor, you can see, in addition to the hostile slimes, 3 other portcullises, each with a protective rune to try to hold the hostile monsters out.\n\nThere\'s something about this whole place that makes you think it involves magic, and maybe magical research. What they were doing down here, around so many hostile monsters, you may be able to find out inside.\n\nYou also notice that the outpost is unusually quiet. There are no signs of people anywhere.", eDialogPic.CREATURE, 108, ["OK"])

def PitofPlentifulGoo_212_MapTrigger_19_9(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear a gentle, chiming noise. Then gears turn and chains clatter.")
        t = Town.TerrainAt(Location(16,13))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(16,13), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(16,13), 0, TerrainRecord.UnderlayList[130])
        return

def PitofPlentifulGoo_213_MapTrigger_21_9(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear a gentle, chiming noise. Then gears turn and chains clatter.")
        t = Town.TerrainAt(Location(22,13))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(22,13), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(22,13), 0, TerrainRecord.UnderlayList[130])
        return

def PitofPlentifulGoo_214_MapTrigger_23_9(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear a gentle, chiming noise. Then gears turn and chains clatter.")
        t = Town.TerrainAt(Location(28,13))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(28,13), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(28,13), 0, TerrainRecord.UnderlayList[130])
        return

def PitofPlentifulGoo_215_MapTrigger_25_9(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear a gentle, chiming noise. Then gears turn and chains clatter.")
        t = Town.TerrainAt(Location(34,13))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(34,13), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(34,13), 0, TerrainRecord.UnderlayList[130])
        return

def PitofPlentifulGoo_216_MapTrigger_19_1(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(18,1)).Num == 128:
        if SpecialItem.PartyHas("SlimeKey2"):
            MessageBox("You find a massive, magically locked door. Fortunately, one of your keys fits in the lock.")
            Town.AlterTerrain(Location(18,1), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("As thieves say, nobody makes a locked door  like a wizard. Bound in mithral bands and covered in protective runes, this door is no exception. Alas, none of your keys fit the lock.")
        return

def PitofPlentifulGoo_217_MapTrigger_26_2(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(25,1)).Num == 128:
        if SpecialItem.PartyHas("SlimeKey1"):
            MessageBox("You find a massive, magically locked door. Fortunately, one of your keys fits in the lock.")
            Town.AlterTerrain(Location(25,1), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("As thieves say, nobody makes a locked door  like a wizard. Bound in mithral bands and covered in protective runes, this door is no exception. Alas, none of your keys fit the lock.")
        return

def PitofPlentifulGoo_219_MapTrigger_27_1(p):
    ChoiceBox("You read through the journals the wizards here were keeping. This place was a rebel research facility, trying to find out ways to harness the magical slimes for military purposes.\n\nIt turns out that the slimes here were specially brought from southern Valorim, where a plague of them caused a lot of trouble a few years back. The mages have been studying and modifying them, trying to to get them under control.\n\nThey\'ve been having luck changing the slimes, but not controlling them. Still, experiments for packing them in bombs have been proceeding rapidly.\n\nExploding boxes. Midnight raids. Now slime bombs. This is all just too weird.", eDialogPic.TERRAIN, 135, ["OK"])

def PitofPlentifulGoo_221_MapTrigger_29_1(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
        MessageBox("Among the journals and tomes (which describe in grinding detail the biologies and mating habits of magical slimes), you find an ancient spell book. With a bit of effort, you manage to decipher the archaic writing.\n\nYou can now cast the spell Death Arrows.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_death_arrows")
        return
    MessageBox("Among the journals and tomes detailing in grinding detail the biologies and mating habits of magical slimes, you find an ancient spell book. Alas, try as you might, you can\'t decipher the archaic writing.")

def PitofPlentifulGoo_222_MapTrigger_5_4(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(6,4)).Num == 130:
        MessageBox("That\'s odd. While you were outside, someone closed this portcullis, and put a fresh lock on it. Someone behind you really has it in for you.")
        return

def PitofPlentifulGoo_223_MapTrigger_7_5(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(6,4)).Num == 130:
        if SpecialItem.PartyHas("SmallOakBox"):
            result = ChoiceBox("Your exit is blocked by a huge, rusty gate. It\'s too heavy for you to knock it down, but the rebels\' exploding boxes might do the trick. There\'s a small depression in the floor you could probably fit the exploding box into.", eDialogPic.TERRAIN, 92, ["Leave", "Insert"])
            if result == 1:
                MessageBox("You put the box in the depression, pull the rope in the side out, and run for it. You don\'t run quite fast enough. The blast partially catches you.")
                Party.Damage(Maths.Rand(6, 1, 6) + 6, eDamageType.FIRE)
                Wait()
                Animation_Explosion(Location(6,4), 0, "005_explosion")
                Animation_Hold()
                Wait()
                MessageBox("Looking back, you see that it worked! The gate is still intact, but the blast broke the lock open. One push swings it open. You can get out now.")
                Town.AlterTerrain(Location(6,4), 0, TerrainRecord.UnderlayList[131])
                SpecialItem.Take("SmallOakBox")
                return
            return
        MessageBox("Your exit is blocked by a huge, iron gate, held shut by a massive padlock. The gate is more than heavy enough to withstand your blows, but you notice that the whole apparatus is quite rusty. Something stronger than you might be able to destroy it.")
        return

def PitofPlentifulGoo_224_MapTrigger_38_42(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(41,44)).Num == 131:
        MessageBox("As you walk around the curved passage, you hear a loud clang behind you. Trying to ignore that grim, sinking feeling, you look back, and see that someone has closed the portcullis behind you. God knows how.\n\nYou hear footsteps receding in the distance. Someone on the other side is walking away, not feeling any need to hurry.")
        Town.AlterTerrain(Location(41,44), 0, TerrainRecord.UnderlayList[130])
        return

def PitofPlentifulGoo_227_MapTrigger_40_44(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(41,44)).Num == 130:
        if SpecialItem.PartyHas("SmallOakBox"):
            if StuffDone["16_5"] >= 1:
                MessageBox("The first explosive didn\'t even mar this gate. You decide to not even bother with wasting the second one.")
                return
            result = ChoiceBox("The massive, steel gate is still here, blocking your escape from these caves. Although the steel looks strong and new, there is a small chance one of the rebel\'s explosive boxes might affect it somehow.\n\nIf you wanted to try, there is a small gap in the floor under the gate you could slide the box into.", eDialogPic.TERRAIN, 92, ["Leave", "Insert"])
            if result == 1:
                MessageBox("You put the box in, pull the rope, and run. Unfortunately, the thing explodes too quickly for you to get away damage-free.")
                Party.Damage(Maths.Rand(6, 1, 6) + 6, eDamageType.FIRE)
                Wait()
                Animation_Explosion(Location(41,44), 0, "005_explosion")
                Animation_Hold()
                Wait()
                if StuffDone["16_5"] == 250:
                    return
                StuffDone["16_5"] = 250
                MessageBox("Unfortunately, the blast was nowhere near strong enough to affect the gate. It\'s not even scratched.")
                SpecialItem.Take("SmallOakBox")
                return
            return
        MessageBox("Yep. The gate is closed all right. The metal is strong and new and properly oiled. No chance you\'ll be able to bash it down.")
        return

def PitofPlentifulGoo_228_MapTrigger_16_1(p):
    if StuffDone["16_7"] == 250:
        return
    if SpecialItem.PartyHas("SmallOakBox"):
        MessageBox("You still have the first box you found and decide to leave the other one behind. They\'re extremely bulky and heavy.")
        return
    if StuffDone["16_6"] == 0:
        result = ChoiceBox("This room contains two pedestals, each with a oak box on it. The boxes have ropes trailing out through holes in their sides.\n\nAt this point, you\'d have no excuse to not recognize some of the rebel\'s exploding boxes when you see them. Your guess is that pulling the rope makes the box explode.\n\nThe boxes are too bulky to take both of them with you, but nothing is stopping you from taking one. You just hope they\'re not too unstable.", eDialogPic.TERRAIN, 125, ["Leave", "Take"])
        if result == 1:
            if StuffDone["16_6"] == 250:
                return
            StuffDone["16_6"] = 250
            SpecialItem.Give("SmallOakBox")
            return
        return
    if StuffDone["16_7"] == 250:
        return
    result = ChoiceBox("There\'s still one explosive box left.", eDialogPic.TERRAIN, 125, ["Take", "Leave"])
    if result == 0:
        StuffDone["16_7"] = 250
        TownMap.List["PitofPlentifulGoo_16"].AlterTerrain(Location(16,1), 1, None)
        TownMap.List["PitofPlentifulGoo_16"].DeactivateTrigger(Location(16,1))
        SpecialItem.Give("SmallOakBox")
    return

def PitofPlentifulGoo_229_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(40, 27),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(42, 27),WorldMap.SectorAt(Party.OutsidePos))
