def Generate_Wandering_70_MandahlAscent(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([2,NPCRecord.List["Salamander_127"]])
        elif r1 == 1:
            npcs.append([2,NPCRecord.List["Basilisk_103"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["PackLeader_167"]])
            npcs.append([2,NPCRecord.List["AlienBeast_166"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["PackLeader_167"]])
            npcs.append([2,NPCRecord.List["AlienBeast_166"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(26,49)
                elif r2 == 1: l = Location(54,28)
                elif r2 == 2: l = Location(5,47)
                elif r2 == 3: l = Location(32,44)
                
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

def MandahlAscent_1748_MapTrigger_46_52(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(50,58))
    p.CancelAction = True

def MandahlAscent_1749_MapTrigger_50_59(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(46,53))
    p.CancelAction = True

def MandahlAscent_1750_MapTrigger_46_46(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(60,35))
    p.CancelAction = True

def MandahlAscent_1751_MapTrigger_60_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(46,47))
    p.CancelAction = True

def MandahlAscent_1752_MapTrigger_46_34(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(42,31))
    p.CancelAction = True
    if StuffDone["54_5"] == 1:
        for x in range(34, 38):
            for y in range(27, 28):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
        StuffDone["55_3"] = 0
        Party.OutsidePos = Location(41, 196)
        return

def MandahlAscent_1753_MapTrigger_42_32(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(46,35))
    p.CancelAction = True

def MandahlAscent_1754_MapTrigger_49_28(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(55,22))
    p.CancelAction = True

def MandahlAscent_1755_MapTrigger_55_23(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(49,29))
    p.CancelAction = True

def MandahlAscent_1756_MapTrigger_30_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(52,7))
    p.CancelAction = True
    StuffDone["55_3"] = 3
    Party.OutsidePos = Location(66, 233)

def MandahlAscent_1757_MapTrigger_52_6(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(30,35))
    p.CancelAction = True
    if StuffDone["54_5"] == 1:
        for x in range(34, 38):
            for y in range(27, 28):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
        StuffDone["55_3"] = 0
        Party.OutsidePos = Location(41, 196)
        return

def MandahlAscent_1758_MapTrigger_19_44(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(46,5))
    p.CancelAction = True
    StuffDone["55_3"] = 2
    Party.OutsidePos = Location(69, 216)

def MandahlAscent_1759_MapTrigger_46_4(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(19,43))
    p.CancelAction = True
    StuffDone["55_3"] = 0
    Party.OutsidePos = Location(41, 196)

def MandahlAscent_1760_MapTrigger_60_25(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(48,24))
    p.CancelAction = True

def MandahlAscent_1761_MapTrigger_48_25(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(60,26))
    p.CancelAction = True
    StuffDone["54_6"] = 0

def MandahlAscent_1762_MapTrigger_26_54(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(8,55))
    p.CancelAction = True
    if StuffDone["54_9"] == 1:
        for x in range(6, 7):
            for y in range(37, 41):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[37])
        return

def MandahlAscent_1763_MapTrigger_8_54(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(26,55))
    p.CancelAction = True

def MandahlAscent_1764_MapTrigger_15_36(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(20,18))
    p.CancelAction = True

def MandahlAscent_1765_MapTrigger_20_19(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(15,37))
    p.CancelAction = True

def MandahlAscent_1766_MapTrigger_15_30(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(18,11))
    p.CancelAction = True
    StuffDone["55_3"] = 1
    Party.OutsidePos = Location(82, 233)

def MandahlAscent_1767_MapTrigger_18_12(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(15,31))
    p.CancelAction = True
    StuffDone["55_3"] = 0
    Party.OutsidePos = Location(41, 196)

def MandahlAscent_1768_MapTrigger_32_55(p):
    if StuffDone["54_3"] == 250:
        return
    StuffDone["54_3"] = 250
    TownMap.List["MandahlAscent_70"].DeactivateTrigger(Location(32,55))
    TownMap.List["MandahlAscent_70"].DeactivateTrigger(Location(33,55))
    MessageBox("Just ahead you see the remnants of a campfire. Junk of all sort has been scattered about. You wonder who was camping out here in the mountains.")

def MandahlAscent_1770_MapTrigger_55_20(p):
    if StuffDone["54_4"] == 250:
        return
    StuffDone["54_4"] = 250
    TownMap.List["MandahlAscent_70"].DeactivateTrigger(Location(55,20))
    ChoiceBox("Ahead is a smoky lava vent. Emerging from the smog, you see a bright fiery figure. The figure is quite tall, with a height of about four meters. You manage to make out the figure as an Efreet, an ancient race of fire.\n\nThe creature seems to care little about your presence. He just casually watches you as he paces about on his lava bed. He must think that you are no threat to him.", eDialogPic.CREATURE1x2, 6, ["OK"])

def MandahlAscent_1771_MapTrigger_37_27(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(37,27)).Num == 251:
        MessageBox("Judging from the short plank, there was probably once a bridge here. However, that bridge that was is now gone. The current is far to strong for you to swim across. You will just have to find another way.")
        return

def MandahlAscent_1772_MapTrigger_43_16(p):
    if StuffDone["54_5"] == 0:
        if StuffDone["54_6"] == 0:
            result = ChoiceBox("\"Mwa, ha, ha!\" An booming laughter echoes throughout the cavern. You look around to see several globs of multicolored light appearing, disappearing, moving, and reshaping all around you.\n\n\"Mortals! State your purpose for coming here.\" You tell him that the Efreet sent you. \"Mwa, ha, ha! That foolish creature. He must be a fool to send someone like you. You are far too puny for me to waste my time on you. Be gone!\"\n\nThe voice pauses, seeming to await your response. You could \'leave\' and obey the strange creature. You could attempt to \'attack\' it. Or you could even try to \'give\' the heat consuming creature some magical flame to attempt to appease it.", eDialogPic.STANDARD, 13, ["Leave", "Attack", "Give"])
            if result == 1:
                MessageBox("You draw your weapons. The globs of light seem to expand. \"Mwa, ha, ha! Do you really think those crude tools of yours are capable of harming me? Take that!\" A bolt of electricity shocks you.")
                StuffDone["54_6"] = 1
                if StuffDone["54_6"] == 1:
                    Party.Damage(Maths.Rand(5, 1, 6) + 10, eDamageType.MAGIC)
                    Wait()
                    Timer(Town, 3, False, "MandahlAscent_1782_TownTimer_33", eTimerType.DELETE)
                    return
                return
            elif result == 2:
                Animation_Hold(-1, 074_fireball)
                Wait()
                if SpecialItem.PartyHas("PhoenixEgg"):
                    SpecialItem.Take("PhoenixEgg")
                    StuffDone["54_5"] = 1
                    ChoiceBox("Remembering the Phoenix Egg you found on the Efreet altar, you throw it at the globs. The egg shatters and begins to emit a massive inferno. \"Ah heat!\" The flames seem to vanish before your eyes.\n\n\"Such great power! Oh yes! I have never had such a wonderful meal.\" A brief pause follows. Suddenly, the globs of light begins to grow and move toward you. \"Thank you mortals, now I shall consume you as well! Mwa, ha, ha!\"\n\nA large bolt of electricity strikes you, searing your skin. It is definitely time to get out of here!", eDialogPic.STANDARD, 13, ["OK"])
                    Party.Damage(Maths.Rand(5, 1, 6) + 20, eDamageType.MAGIC)
                    Wait()
                    Timer(Town, 3, False, "MandahlAscent_1783_TownTimer_42", eTimerType.DELETE)
                    return
                MessageBox("Using your magic, you propel the strongest fire spells you have. As they approach the creature, they seem to vanish. You hear an echoing sigh. \"These crumbs do little to appease me. Be gone mortals.\"")
                for pc in Party.EachAlivePC():
                    pc.SP-= 25
                return
            return
        return

def MandahlAscent_1774_MapTrigger_22_26(p):
    if StuffDone["54_7"] == 250:
        return
    StuffDone["54_7"] = 250
    TownMap.List["MandahlAscent_70"].DeactivateTrigger(Location(22,26))
    TownMap.List["MandahlAscent_70"].DeactivateTrigger(Location(23,26))
    ChoiceBox("The hill slopes steeply down into a small valley of smoking lava. Among the smog, you see several large fiery figures. You make them out to be Efreeti. Although it is hard to see through the smoke, you manage to make out the scene.\n\nThey appear to be performing some kind of ceremony. At the other end of the valley is a pedestal with a large altar. The priest, for lack of a better term, is holding up a bright red rock of some sort. You listen to the chanting.\n\n\"We give ourselves to the holy flame for it is the creator of heaven and earth. Oh holy flame, infinite is your heat. We worship you, we give you thanks, we praise you for your fire.\n\nFor within this holy egg lies flames that burn for all eternity. Lord, we beg you for your power. Grant this to us, not because it is our will, but your own. We praise the almighty fire, one with the holy heat, we praise you. Amen!\"\n\nSuddenly, from the red stone flames come pouring out smothering the entire valley and bathing the worshiping Efreets. After several seconds, the flames subside. The Efreeti solemnly sink into the lava.\n\nThe \'priest\' sets the egg back on the altar, whispers a prayer, and departs. The Efreeti are gone.", eDialogPic.CREATURE1x2, 6, ["OK"])

def MandahlAscent_1776_MapTrigger_22_33(p):
    if StuffDone["54_8"] == 0:
        result = ChoiceBox("Upon this altar rests that red stone that emitted the fire. It is actually quite large and shaped kind of like an egg. Roaring flames spark from within the translucent surface of the egg. It emits a very strong heat also.\n\nSome wizard or someone is sure likely to want to study it. It appears the Efreeti are not looking. Do you take the egg?", eDialogPic.TERRAIN, 159, ["Leave", "Take"])
        if result == 1:
            StuffDone["54_8"] = 1
            SpecialItem.Give("PhoenixEgg")
            Town.PlaceEncounterGroup(1)
            Animation_Hold(-1, 005_explosion)
            Wait()
            ChoiceBox("As soon as you remove the egg from its proper place, you hear a loud booming sound that echoes throughout this smoky valley. Suddenly, the Efreeti rise from the lava and they do not look very happy to find you stealing their holy artifact.", eDialogPic.CREATURE1x2, 6, ["OK"])
            Message("Efreet casts:")
            Message("  Slow Group")
            Animation_Hold(-1, 024_priestspell)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 8))
            Message("Efreet casts:")
            Message("  Curse All")
            Animation_Hold(-1, 024_priestspell)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 8))
            return
        return

def MandahlAscent_1777_MapTrigger_6_39(p):
    if StuffDone["54_9"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        StuffDone["54_9"] = 1
        Animation_Hold(-1, 060_smallboom)
        Wait()
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(6,41))
        p.CancelAction = True
        Party.Damage(Maths.Rand(5, 1, 8) + 20, eDamageType.WEAPON)
        Wait()
        MessageBox("Uh oh! You seem to have just been passing through at just the wrong time. Rocks bounce up and rain upon this passage. You manage to run back and survive. But the pass is now inaccessible.\n\nTo make matters worse, you find that a group of hungry Slithzerikai has arrived to kill you leading you to believe that this was indeed not a natural occurrence.")
        Town.PlaceEncounterGroup(2)
        for x in range(6, 7):
            for y in range(37, 41):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[37])
        return

def MandahlAscent_1778_MapTrigger_6_40(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(6,40)).Num == 37:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The rock slide has blocked this passage. The rocks are too heavy to move yourself. You will either need to find a way to move these rocks or find another way around.")
        return

def MandahlAscent_1779_MapTrigger_9_27(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,26)).Num == 145:
        if SpecialItem.PartyHas("ScaleKey"):
            MessageBox("The scale key that you found off the Slith leader unlocks this door.")
            t = Town.TerrainAt(Location(9,26))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(9,26)).TransformTo
                Town.AlterTerrain(Location(9,26), 0, t)
            if StuffDone["55_4"] == 250:
                return
            StuffDone["55_4"] = 250
            ChoiceBox("Inside the strange structure is, no surprise, a band of Slithzerikai. What is intriguing is the decor of this structure. It is strangely alien and of a unique style that is usually not associated with Slithzerikai.\n\nHowever, the bunker appears quite old. It is very likely that this was built by someone else, a long time ago.", eDialogPic.CREATURE, 47, ["OK"])
            return
        return

def MandahlAscent_1780_MapTrigger_12_17(p):
    if StuffDone["54_9"] == 1:
        result = ChoiceBox("This is a strange piece of alien equipment. You sit down and the crystal begins to interact directly with your mind. You learn that this is a device called a \'Gravitational Broiler\'.\n\nIt causes \'bubbles\' to form in gravity for a short time. The application is to create distant, small, and silent explosions. The device is currently targeted at that pass with the rockfall.\n\nThat must be how the Sliths triggered the slide. Perhaps if you create more \'gravitational bubbles\', you could clear the path. There is a red button on the pedestal that will allow you to access the machine.", eDialogPic.TERRAIN, 168, ["Leave", "Push"])
        if result == 1:
            MessageBox("You push the button. The crystal interaction with the optical parts of your mind allows you to see invisible bubbles form to move the rocks out the path, clearing it!")
            StuffDone["54_9"] = 2
            Animation_Hold(-1, 008_bubbles)
            Wait()
            for x in range(6, 7):
                for y in range(37, 41):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[36])
            return
        return

def MandahlAscent_1781_MapTrigger_17_4(p):
    if StuffDone["55_3"] >= 2:
        if StuffDone["55_3"] < 3:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(25,4))
            p.CancelAction = True
            return
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(57,4))
        p.CancelAction = True
        return
    if StuffDone["55_3"] < 1:
        return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(4,4))
    p.CancelAction = True

def MandahlAscent_1782_TownTimer_33(p):
    if StuffDone["54_6"] == 1:
        Party.Damage(Maths.Rand(5, 1, 6) + 10, eDamageType.MAGIC)
        Wait()
        Timer(Town, 3, False, "MandahlAscent_1782_TownTimer_33", eTimerType.DELETE)
        return

def MandahlAscent_1783_TownTimer_42(p):
    Party.Damage(Maths.Rand(5, 1, 6) + 30, eDamageType.MAGIC)
    Wait()
    Timer(Town, 2, False, "MandahlAscent_1784_TownTimer_44", eTimerType.DELETE)

def MandahlAscent_1784_TownTimer_44(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    ChoiceBox("Suddenly you hear a loud boom that echoes throughout the cavern. You look to see the globs of light seemingly splatter. You hear a loud shout. \"Noooo! I cannot make it stop. Stop! Too much. Stop this thing! Ahhhhhhh!\"\n\nYou believe the creature is now gone. The Efreet will be very pleased.", eDialogPic.STANDARD, 13, ["OK"])

def MandahlAscent_1785_OnEntry(p):
    if StuffDone["55_3"] >= 2:
        if StuffDone["55_3"] < 3:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(25,4))
            p.CancelAction = True
            return
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(57,4))
        p.CancelAction = True
        return
    if StuffDone["55_3"] < 1:
        return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(4,4))
    p.CancelAction = True

def MandahlAscent_1786_CreatureDeath37(p):
    MessageBox("You manage to slay the leader of the Slithzerikai hunters. On his necklace are bits of bone and teeth. Also kept there is a key made of scales. You pocket the key in hopes that it may be of use later.")
    SpecialItem.Give("ScaleKey")

def MandahlAscent_1787_TalkingTrigger1(p):
    if StuffDone["54_5"] == 0:
        p.TalkingText = "\"If you could dispose of that being, I would be indebted to you. I will repay your deed by creating a bridge to allow you to cross the nearby river. The beast\'s lair is back down the cave and to the east, you cannot miss it.\""
        Town.AlterTerrain(Location(60,25), 0, TerrainRecord.UnderlayList[240])
        return
