def Generate_Wandering_67_FloodedMine(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Salamander_127"]])
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([1,NPCRecord.List["Basilisk_103"]])
            npcs.append([2,NPCRecord.List["FireLizard_73"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Salamander_127"]])
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([1,NPCRecord.List["Basilisk_103"]])
            npcs.append([2,NPCRecord.List["FireLizard_73"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Salamander_127"]])
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([1,NPCRecord.List["Basilisk_103"]])
            npcs.append([2,NPCRecord.List["FireLizard_73"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["Salamander_127"]])
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([1,NPCRecord.List["Basilisk_103"]])
            npcs.append([2,NPCRecord.List["FireLizard_73"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(36,36)
                elif r2 == 1: l = Location(16,48)
                elif r2 == 2: l = Location(8,49)
                elif r2 == 3: l = Location(9,34)
                
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

def FloodedMine_1641_MapTrigger_2_41(p):
    if StuffDone["58_9"] == 250:
        return
    StuffDone["58_9"] = 250
    TownMap.List["FloodedMine_67"].DeactivateTrigger(Location(2,41))
    TownMap.List["FloodedMine_67"].DeactivateTrigger(Location(3,41))
    TownMap.List["FloodedMine_67"].DeactivateTrigger(Location(4,41))
    Town.PlaceEncounterGroup(1)
    Animation_Explosion(Location(1,1), 1, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("It appears that these caves have been trapped by some fairly intelligent beings. There are flashes of light from ahead and behind. Emerging are six fearsome golems that are ready to tear you apart.", eDialogPic.CREATURE, 122, ["OK"])

def FloodedMine_1644_MapTrigger_51_17(p):
    if StuffDone["59_8"] == 250:
        return
    StuffDone["59_8"] = 250
    TownMap.List["FloodedMine_67"].DeactivateTrigger(Location(51,17))
    Town.PlaceEncounterGroup(3)
    Animation_Hold(-1, 068_identify)
    Wait()
    MessageBox("You open this chest and there is an immense flash of light. The flash seemed to have an effect on your mind, seeming to disable it. To make matters worse, you are now surrounded by some fearsome spirits!")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 7))

def FloodedMine_1645_MapTrigger_11_27(p):
    if StuffDone["59_1"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(59,41))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        StuffDone["59_0"] += 1
        if StuffDone["59_0"] == 250:
            pass
        if StuffDone["59_0"] >= 3:
            MessageBox("This time you are teleported straight into solid rock causing quick death for all of you. Perhaps you should have heeded the warning. As they say, hindsight is twenty, twenty.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(44,58))
            p.CancelAction = True
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        if StuffDone["59_0"] < 2:
            MessageBox("You find yourself in a fair sized room. Suddenly, a voice rings out. \"Intruders! You are not welcome here. This is your only warning. Leave now and never return.\"")
            Party.Damage(Maths.Rand(5, 1, 4) + 10, eDamageType.UNBLOCKABLE)
            Wait()
            return
        MessageBox("You are, once again, teleported to the room. This time, you are greeted with an assortment of Ruby Skeletons! It appears the owner of this place means business.")
        Town.PlaceEncounterGroup(2)
        Party.HealAll(-250)
        return

def FloodedMine_1646_MapTrigger_54_32(p):
    MessageBox("This pedestal displays a pentagon.")

def FloodedMine_1647_MapTrigger_56_32(p):
    MessageBox("This pedestal displays a diamond.")

def FloodedMine_1648_MapTrigger_54_34(p):
    MessageBox("This pedestal displays a circle.")

def FloodedMine_1649_MapTrigger_58_34(p):
    MessageBox("This pedestal displays a hexagon.")

def FloodedMine_1651_MapTrigger_56_36(p):
    MessageBox("This pedestal displays a triangle.")

def FloodedMine_1654_MapTrigger_56_34(p):
    MessageBox("This pedestal has a message: Display the appropriate shape. (write the name of the shape you wish to draw in the text box)")
    response = InputTextBox("Enter something:", "")
    response = response[0:5].upper()
    if response == "PENTA":
        StuffDone["59_1"] = 1
        return
    StuffDone["59_1"] = 0

def FloodedMine_1655_MapTrigger_54_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(1,55))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def FloodedMine_1656_MapTrigger_3_17(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("A strange forcefield is holding you back. No matter how hard you try, your muscles refuse to move any farther. You know that you are not going to be able to defeat this barrier.")

def FloodedMine_1659_MapTrigger_54_8(p):
    if StuffDone["59_2"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("There is a powerful forcefield surrounding the dragon. You cannot move any closer to him despite your best attempts.")
        return

def FloodedMine_1673_MapTrigger_30_6(p):
    result = ChoiceBox("A massive chasm awaits you here. Although it would not be too difficult to climb down, you would have a difficult, if not impossible, time climbing back up.", eDialogPic.TERRAIN, 244, ["Leave", "Climb"])
    if result == 1:
        MessageBox("You carefully make your way down the sharp wall of the chasm, using many of the stones as stepping stones. You manage to make it down unharmed, but you will not be able to make it back up. You hope you are not trapped.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(28,14))
        p.CancelAction = True
        return

def FloodedMine_1674_MapTrigger_49_13(p):
    if StuffDone["59_2"] == 0:
        if StuffDone["59_3"] == 250:
            return
        StuffDone["59_3"] = 250
        ChoiceBox("Ahead of you is a sight of true amazement. A massive domed cavern is before you. At the top of dome\'s curvature is a large gaping hole where sunlight pours down. Beneath that lies the master of this lair.\n\nIt sits upon a raised pedestal like the majestic creature it is. It is a creature of myth, seen by only a few. It is the most awesome creature to ever roam the earth, a dragon.\n\nThe enormous reptile is about ten times your size, and undoubtedly immensely powerful. The dragon just watches you casually, uncaring and definitely unthreatened by your presence.\n\nYou are unsure if it would be wise to move in closer.", eDialogPic.STANDARD, 12, ["OK"])
        return

def FloodedMine_1676_MapTrigger_58_14(p):
    if StuffDone["59_4"] == 0:
        if StuffDone["59_2"] == 0:
            ChoiceBox("You try to go down this passage but are greeted with a strange magical barrier and a loud \"ahem\" from the north. You turn to see the dragon glaring at you. He is clearly not pleased with you trying to go down this passage.", eDialogPic.STANDARD, 12, ["OK"])
            p.CancelAction = True
            return
        return

def FloodedMine_1678_MapTrigger_39_5(p):
    MessageBox("You discover a book entitled: Classic Riddles and Puzzles. Designed for entertainment, it\'s puzzles are not too difficult. One puzzle is the exact same pedestal shape puzzle used on you earlier! Looks like the owner either lacks creativity or motivation.")

def FloodedMine_1679_MapTrigger_41_2(p):
    ChoiceBox("You discover a hand written journal that pertains to the nearby volcano you saw earlier. It appears Khross, the dragon owner of these caves, is planning to perform a ritual to create adamantite.\n\nAdamantite is an extremely rare metal and can only be forged in the heat and energy in a volcanic eruption. It seems that the volcano is on the eve of eruption. However, this is in a dragon\'s terms.\n\nIt appears that the eruption is probably a couple years off, but could occur at any time. Upon the eruption, Khross plans to travel to the volcano and cast the necessary spells to create and form adamantite objects.\n\nAdamantite items are supposedly a sign of prowess and statue in draconian culture. It appears the rituals would take days to complete, due to the density of the metal.\n\nThe tome also contains several detailed maps of the volcano. Although the interior ones are a bit sketchy, the surrounding area is quite detailed. You take note of the small cavern that allows entrance to the volcano.", eDialogPic.STANDARD, 30, ["OK"])
    TownMap.List["VolcanicCavern_95"].Hidden = False

def FloodedMine_1680_MapTrigger_59_21(p):
    if StuffDone["59_6"] == 250:
        return
    StuffDone["59_6"] = 250
    TownMap.List["FloodedMine_67"].DeactivateTrigger(Location(59,21))
    TownMap.List["FloodedMine_67"].DeactivateTrigger(Location(60,21))
    MessageBox("You open the door revealing chambers in the typical alien style. A nearby crystal illuminates the room. At the end is an odd shaped container and beds that are far too fragile for any of you to sleep on.")

def FloodedMine_1682_MapTrigger_52_26(p):
    ChoiceBox("You have discovered another one of those machines that Altrus constructed. It looks very similar to the one you found back at Morbane\'s Crypt. You touch the crystal, hoping to learn a little bit more.\n\nThis time you are more prepared for the mental rush. You see many of the same references to Dark Metal, mentions about energy nodes, and an assortment of other alien terms.\n\nFinally, you must withdraw. You pull away none the smarter. It looks like this lead has ended cold so far. However, there may be other information lying around.", eDialogPic.STANDARD, 1026, ["OK"])
    StuffDone["55_2"] = 1

def FloodedMine_1684_MapTrigger_50_19(p):
    if StuffDone["121_2"] == 0:
        result = ChoiceBox("Within this box you find a few scrolls and an pyramid shaped crystal. On the base of the pyramid are four terminated spikes. From reading the scrolls, you learn this is a device called a Soul Crystal.\n\nIt is used to capture and store the essence of creatures in the four spikes (called slots) which can later be summoned. The methods of doing this are not detailed here. However, if you wanted this crystal, it is yours.", eDialogPic.TERRAIN, 178, ["Leave", "Take"])
        if result == 1:
            StuffDone["121_2"] = 1
            SpecialItem.Give("SoulCrystal")
            if StuffDone["121_0"] == 1:
                for pc in Party.EachAlivePC():
                    pc.LearnSpell("m_capture_soul")
                if StuffDone["121_1"] == 1:
                    for pc in Party.EachAlivePC():
                        pc.LearnSpell("m_simulacrum")
                    return
                return
            if StuffDone["121_1"] == 1:
                for pc in Party.EachAlivePC():
                    pc.LearnSpell("m_simulacrum")
                return
            return
        return

def FloodedMine_1685_MapTrigger_53_19(p):
    if StuffDone["59_7"] == 0:
        result = ChoiceBox("You open this cabinet and discover one object, a crystal. However, this crystal is unlike any other crystal you have seen. It radiates a kind of mental energy that touches your minds.\n\nIt is almost as if the crystal is trying to teach you something. It also almost feels that the crystal has a kind of life within it, although not sentient. This could be very interesting to use or some mage may wish to study it.", eDialogPic.TERRAIN, 178, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("LearningCrystal_343")
            MessageBox("You take the crystal, it seems to radiate knowledge upon coming into contact with it.")
            StuffDone["59_7"] = 1
            return
        return

def FloodedMine_1686_MapTrigger_59_18(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(59,19)).Num == 169:
        if SpecialItem.PartyHas("BlessedAtheme"):
            MessageBox("The Blessed Atheme cuts right through the waxy magic seal like a knife cutting through butter. As soon as you make the first slice, the entire seal begins to melt away. You may now proceed.")
            for x in range(59, 61):
                for y in range(19, 20):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[224])
            return
        ChoiceBox("You encounter a strange kind of barrier you have never seen before. Although it is clearly a magical construct, it is not made from magical energy. This barrier has a material, and wax-like form.\n\nThe wax looks very easy to slice through, but your weapons just slide right off and your spells are deflected. No matter how hard you try, you cannot slice through this barrier.\n\nPerhaps you should consult an expert in these matters.", eDialogPic.TERRAIN, 231, ["OK"])
        StuffDone["54_2"] = 1
        return

def FloodedMine_1688_OnEntry(p):
    if StuffDone["59_5"] == 0:
        StuffDone["59_5"] = 1
        ChoiceBox("This flooded cavern continues for a ways. As you row down the watery passage, you take note of the few ruined structures. One seems to have been for lodgings, one for administrative, and several for storage.\n\nIt basically looks like the typical mine accommodations except for the fact that they are flooded out. From the looks of things, this occurred generations ago. Now it looks like you have reached the end of the gallery.\n\nYou notice that there are several small passages that continue from the cavernous shore. You swear that you see statues on the shore at the entrance of each passage.", eDialogPic.STANDARD, 31, ["OK"])
        return
    if StuffDone["59_2"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Khross_177": Town.NPCList.Remove(npc)
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(31,19), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(31,19))
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(60,47), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(60,47))
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(56,14), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(47,19), True):
                                        if i.SpecialClass == 52:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    if Maths.Rand(1,0,100) < 20:
                                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                        return
                                    return
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(47,19), True):
                                    if i.SpecialClass == 52:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                if Maths.Rand(1,0,100) < 20:
                                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                    return
                                return
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(56,14), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(47,19), True):
                                    if i.SpecialClass == 52:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                if Maths.Rand(1,0,100) < 20:
                                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                    return
                                return
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(56,14), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(60,47), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(60,47))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(56,14), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(47,19), True):
                                    if i.SpecialClass == 52:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                if Maths.Rand(1,0,100) < 20:
                                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                    return
                                return
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(56,14), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(56,14), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(60,47), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(60,47))
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(56,14), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(56,14), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(56,14), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(47,19), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                return
            return
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(31,19), True):
            if i.SpecialClass == 52:
                itemthere = True
                break
    if itemthere == True:
        if Maths.Rand(1,0,100) < 20:
            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(31,19))
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(60,47), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(60,47))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(56,14), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(47,19), True):
                                    if i.SpecialClass == 52:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                if Maths.Rand(1,0,100) < 20:
                                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                    return
                                return
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(56,14), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(56,14), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(60,47), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(60,47))
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(56,14), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(47,19), True):
                                if i.SpecialClass == 52:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            if Maths.Rand(1,0,100) < 20:
                                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                                return
                            return
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(56,14), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(56,14), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(47,19), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                return
            return
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(60,47), True):
            if i.SpecialClass == 52:
                itemthere = True
                break
    if itemthere == True:
        if Maths.Rand(1,0,100) < 20:
            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(60,47))
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(56,14), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(47,19), True):
                            if i.SpecialClass == 52:
                                itemthere = True
                                break
                    if itemthere == True:
                        if Maths.Rand(1,0,100) < 20:
                            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                            return
                        return
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(56,14), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(47,19), True):
                        if i.SpecialClass == 52:
                            itemthere = True
                            break
                if itemthere == True:
                    if Maths.Rand(1,0,100) < 20:
                        Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                        return
                    return
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(47,19), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                return
            return
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(56,14), True):
            if i.SpecialClass == 52:
                itemthere = True
                break
    if itemthere == True:
        if Maths.Rand(1,0,100) < 20:
            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(56,14))
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(47,19), True):
                    if i.SpecialClass == 52:
                        itemthere = True
                        break
            if itemthere == True:
                if Maths.Rand(1,0,100) < 20:
                    Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                    return
                return
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(47,19), True):
                if i.SpecialClass == 52:
                    itemthere = True
                    break
        if itemthere == True:
            if Maths.Rand(1,0,100) < 20:
                Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
                return
            return
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(47,19), True):
            if i.SpecialClass == 52:
                itemthere = True
                break
    if itemthere == True:
        if Maths.Rand(1,0,100) < 20:
            Town.PlaceItem(Item.List["DragonScales_397"].Copy(), Location(47,19))
            return
        return

def FloodedMine_1689_TalkingTrigger7(p):
    if StuffDone["59_4"] == 0:
        Sound.Play(068_identify)
        if SpecialItem.PartyHas("OnyxScepter"):
            result = ChoiceBox("You receive the sensation of being scryed. The dragon emits a few puffs of smoke and thinks. \"I sense you have an artifact called an Onyx Scepter. I have heard my dragon brothers speak of such an object.\n\nIt is extremely sought out and quite valuable to dragon kind. I shall make a deal with you. If you surrender the Onyx Scepter, I shall look the other way and let you explore the experiment. Do we have a deal?\"", eDialogPic.STANDARD, 12, ["Leave", "Give"])
            if result == 1:
                SpecialItem.Take("OnyxScepter")
                p.TalkingText = "You lay the Onyx Scepter on the pedestal. He raises his arms and it vanishes! The dragon turns to you. \"A deal is a deal. I shall now ignore your intrusion into the Vahnatai chambers. Just remember, that you are still on my turf.\""
                StuffDone["59_4"] = 1
                return
            p.TalkingText = "You refuse the offer. \"Very well. Seeing that you have nothing else to offer me, you should be leaving.\""
            return
        p.TalkingText = "You receive the sensation of being scryed. The dragon sighs. \"Alas, your trinkets will hardly improve my trove. Be gone and return only with more worthy loot.\""
        return
