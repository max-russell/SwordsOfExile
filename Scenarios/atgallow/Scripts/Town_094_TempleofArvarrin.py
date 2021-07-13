
def TempleofArvarrin_2180_MapTrigger_47_9(p):
    MessageBox("This door has rusted shut. There is no way you will be able to open it.")

def TempleofArvarrin_2181_MapTrigger_44_11(p):
    if StuffDone["70_7"] == 250:
        return
    StuffDone["70_7"] = 250
    TownMap.List["TempleofArvarrin_94"].DeactivateTrigger(Location(44,11))
    MessageBox("On the other side of this moldy wall is a small dusty library. Judging by all the dust, nobody has been here in decades at least. Most of the books here have rotted away but a few are intact.")

def TempleofArvarrin_2182_MapTrigger_47_11(p):
    MessageBox("You discover a small memo that has been crammed between the books. It reads: The sanctuary of Arvarrin can now be accessed by placing the respective skulls in the braziers in the audience chamber.")

def TempleofArvarrin_2184_MapTrigger_2_1(p):
    MessageBox("Sharaki vanishes in a puff of smoke! You highly doubt that you managed to kill her.")
    Town.MakeTownHostile()

def TempleofArvarrin_2185_MapTrigger_30_30(p):
    if StuffDone["70_8"] == 1:
        Town.AlterTerrain(Location(37,34), 0, TerrainRecord.UnderlayList[210])
        return

def TempleofArvarrin_2187_MapTrigger_49_44(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(56,17))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2188_MapTrigger_55_23(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(4,18))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2189_MapTrigger_61_62(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(62,44))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2190_MapTrigger_52_30(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(52,52))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2192_MapTrigger_45_45(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(58,12))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2193_MapTrigger_59_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(50,58))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2194_MapTrigger_62_59(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(45,54))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2196_MapTrigger_62_18(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(33,45))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2197_MapTrigger_33_44(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(62,17))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2198_MapTrigger_36_60(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(13,44))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2199_MapTrigger_13_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(36,61))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def TempleofArvarrin_2200_MapTrigger_20_50(p):
    if StuffDone["71_0"] == 0:
        StuffDone["71_0"] = 1
        StuffDone["70_9"] = 1
        ChoiceBox("Sharaki looks unafraid. As you approach her, she places her hands upon the altar and shouts, \"Prepare to face the wrath of the Nephil goddess of war! Arvarrin, I invoke thee! Come forth and help me slay these infidels.\"\n\nA flash of lightning shoots from the altar, striking Sharaki in the chest. She falls back and...", eDialogPic.CREATURE, 40, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "NephilWarlock_240": Town.NPCList.Remove(npc)
        Town.PlaceEncounterGroup(1)
        Animation_Explosion(Location(19,41), 0, "005_explosion")
        Animation_Hold()
        Wait()
        ChoiceBox("As she falls back, her body bursts into flames! The fire quickly grows and assumes the shape of a large blue demon!\n\n\"Now prepare to face the power of Arvarrin!\"", eDialogPic.STANDARD, 13, ["OK"])
        Animation_Hold(-1, 024_priestspell)
        Wait()
        Message("Sharaki casts:")
        Message("  Excommunicate")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 8))
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 8))
        p.CancelAction = True
        return

def TempleofArvarrin_2201_MapTrigger_25_55(p):
    if StuffDone["70_9"] == 0:
        Town.PlaceEncounterGroup(2)
        return

def TempleofArvarrin_2204_MapTrigger_17_46(p):
    StuffDone["53_3"] = 1
    Town.AlterTerrain(Location(19,51), 0, TerrainRecord.UnderlayList[210])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if  npc.IsABaddie: Town.NPCList.Remove(npc)
    Animation_Hold(-1, 005_explosion)
    Wait()
    ChoiceBox("With a mighty explosion, the daemonic figure of Sharaki bursts apart and crumbles into a hollow shell of ash. Immediately, the captured Nephilim souls bound to Arvarrin fade away as does a section of the southern wall.\n\nThis territory has been freed from the treacherous Arvarrin.", eDialogPic.STANDARD, 13, ["OK"])

def TempleofArvarrin_2205_MapTrigger_22_39(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 20:
        Party.LearnRecipe("strong_energy_potion")
        Animation_Hold(-1, 062_mmm)
        Wait()
        ChoiceBox("You discover a large book of very advanced arcane alchemical recipes. Although most of them are a bit out of your reach despite your extensive knowledge on the topic, you manage to pick up the recipe for the strong power potion!", eDialogPic.TERRAIN, 135, ["OK"])
        return
    MessageBox("You discover a large ancient book on alchemy. The recipes contained within are quite arcane and a bit beyond you. Since it is too bulky to carry, you will need to return when acquire more skill in these matters to comprehend it.")

def TempleofArvarrin_2206_MapTrigger_6_61(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_death_arrows")
        Animation_Hold(-1, 062_mmm)
        Wait()
        ChoiceBox("You discover a large tome of magical spells. The contents are very arcane and are near the level of those used by archmagi. However, your level of skill allows you to decipher the spell called \'Death Arrows\'!", eDialogPic.TERRAIN, 135, ["OK"])
        return
    MessageBox("You discover a large ancient book of magical spells. The incantations contained within are quite arcane and way beyond you. Since it is too bulky to carry, you will need to return when you acquire more skill in these matters to comprehend it.")

def TempleofArvarrin_2207_TownTimer_0(p):
    if StuffDone["70_8"] == 0:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(29,32), True):
                if i.SpecialClass == 53:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,32), True):
                    if i.SpecialClass == 53:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(36,36), True):
                        if i.SpecialClass == 53:
                            itemthere = True
                            break
                if itemthere == True:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(34,39), True):
                            if i.SpecialClass == 53:
                                itemthere = True
                                break
                    if itemthere == True:
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(31,39), True):
                                if i.SpecialClass == 53:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,39), True):
                                    if i.SpecialClass == 53:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(26,36), True):
                                        if i.SpecialClass == 53:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    MessageBox("You hear a rumbling from the eastern wall of the chamber. You look to see part of the wall sliding away revealing a cavernous passage.")
                                    StuffDone["70_8"] = 1
                                    Town.AlterTerrain(Location(37,34), 0, TerrainRecord.UnderlayList[210])
                                    return
                                return
                            return
                        return
                    return
                return
            return
        return

def TempleofArvarrin_2210_TalkingTrigger0(p):
    if StuffDone["53_3"] == 0:
        ChoiceBox("\"Arvarrin is the Nephilim goddess of war and these mountains are her sanctuary. In order for you to traverse these lands, you must pay her homage. She has proclaimed there are three acceptable paths.\n\nThe first is gold. The gods created gold as a symbol of their power. The transaction of gold between mortals is an act of worship. Also an act of worship is returning gold to the gods. Arvarria believes that 5000 gold is acceptable for passage.\n\nIf you do not want to give gold, Arvarrin has use for rare magical objects. If you believe you have an artifact worthy of offering, inquire about that.\n\nThe third option is the gift of life itself. For those who are not successful in their pursuits, she has decreed that a mortal may surrender some of his or her life force to proceed. We take exactly 500 units of experience from each.\"", eDialogPic.CREATURE, 40, ["OK"])
        p.TalkingText = "\"So do you wish to pay gold, artifacts, or will it be life?\""
        return

def TempleofArvarrin_2211_TalkingTrigger1(p):
    if StuffDone["53_3"] == 0:
        if Party.Gold >= 5000:
            Party.Gold -= 5000
            Sound.Play(015_cash)
            p.TalkingText = "You pay the gold. The priestess says a brief prayer and the coins vanish! \"Arvarria thanks you for paying your respects to her. In return she has granted you passage into her lands.\""
            StuffDone["53_3"] = 1
            return
        p.TalkingText = "\"Silly mortals! You cannot afford Arvarria\'s demands. Perhaps you have an artifact, or you could always give the gift of life.\""
        return
    p.TalkingText = "\"You have already paid tribute to the great Arvarria. You are free to travel her lands at your pleasure.\""

def TempleofArvarrin_2212_TalkingTrigger2(p):
    if StuffDone["53_3"] == 0:
        Sound.Play(068_identify)
        if SpecialItem.PartyHas("OnyxScepter"):
            result = ChoiceBox("\"Arvarria senses you have an artifact called an Onyx Scepter. She has been looking for such an item to add to her power. She agrees that the scepter would be an acceptable tribute.\"\n\nDo you give up the Onyx Scepter?", eDialogPic.CREATURE, 40, ["Leave", "Give"])
            if result == 1:
                SpecialItem.Take("OnyxScepter")
                p.TalkingText = "You decide to give her the Onyx Scepter. She whispers a prayer and the artifact vanishes before your eyes. \"Arvarria has graciously accepted your gift. In return, you may traverse her lands at your will.\""
                StuffDone["53_3"] = 1
                return
            return
        p.TalkingText = "\"Alas, you do not have anything that Arvarria would want. Perhaps you would be willing to offer life or gold?\""
        return
    p.TalkingText = "\"You have already paid tribute to the great Arvarria. You are free to travel her lands at your pleasure.\""

def TempleofArvarrin_2213_TalkingTrigger3(p):
    if StuffDone["53_3"] == 0:
        Sound.Play(024_priestspell)
        for pc in Party.EachAlivePC():
            pc.AwardXP(-500)
        p.TalkingText = "The priestess shouts a prayer. You feel an invisible hand on your soul, seeming to suck the energy right out of you. After what seems like hours of pain, it stops. \"Arvarria has accepted your life. You may now traverse her lands.\""
        StuffDone["53_3"] = 1
        return
    p.TalkingText = "\"You have already paid tribute to the great Arvarria. You are free to travel her lands at your pleasure.\""
