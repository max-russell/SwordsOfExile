def Initialise_Scenario():
    pass

def Intro_Message(p):
    pass

def Town_Pre_Entry(town):
    if town.Num==15:
        return TownMap.List[town.Num + StuffDone["2_2"]]
    if town.Num==29:
        return TownMap.List[town.Num + StuffDone["17_0"]]
    if town.Num==41:
        return TownMap.List[town.Num + StuffDone["21_3"]]
    if town.Num==52:
        return TownMap.List[town.Num + StuffDone["31_0"]]
    return town


def On_Using_SI_BrewofUndeadSimulation_2807(p):
    Animation_Hold(-1, 056_swallow)
    Wait()
    Animation_Hold(-1, 065_draining)
    Wait()
    Animation_Hold(-1, 090_paralyze)
    Wait()
    MessageBox("You all drink the potion. Within seconds, your bodies are wracking with pain. You feel your muscles begin to within inside of you and you are light-headed. Your skin turns deathly pale. So this is how it feels to be undead!")
    StuffDone["7_4"] = 1
    for pc in Party.EachAlivePC():
        pc.SetSkill(eSkill.STRENGTH, pc.GetSkill(eSkill.STRENGTH) - 1)
    Timer(None, 10, False,  "ScenarioTimer_x_2813")
    SpecialItem.Take("BrewofUndeadSimulation")

def On_Using_SI_TroglodyteMap_2808(p):
    if Game.Mode != eMode.OUTSIDE and Town.Num == 31:
        MessageBox("You read the map. The location of the Troglodyte lair is north of the battle plateau and then east.")
        Town.AlterTerrain(Location(52,8), 0, TerrainRecord.UnderlayList[240])
        StuffDone["48_6"] = 1
        return
    if StuffDone["9_8"] >= 1:
        ChoiceBox("You decide to present the Troglodyte map to the Giants. The chieftain looks at you and thinks. \"You want to pass, we want to smash! Give us map and we will let you pass through our village. Else we smash you!\"\n\nGiven your choices, you give up the map to the Giants. Immediately, their excitement and bloodlust grows. They grab their stones and clubs and quickly leave the village, not paying any attention to you.\n\nThe village is now almost abandoned. However, some Giants stayed behind  to protect the village and you doubt they will be friendly to you. Your path through the village may not be completely clear, but the trek will be survivable.", eDialogPic.STANDARD, 21, ["OK"])
        StuffDone["9_9"] = 1
        SpecialItem.Take("TroglodyteMap")
        return

def On_Using_SI_SphereofThralni_2809(p):
    if Game.Mode == eMode.TOWN:
        return;
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["100_2"] == 0:
        StuffDone["100_2"] = 1
        Party.Flying -= 5
        Timer(None, 5, False,  "ScenarioTimer_x_2817")
        return
    Message("Not while flying!")

def On_Using_SI_SphereofThralni_20_2810(p):
    if Game.Mode == eMode.TOWN:
        return;
    if Game.Mode == eMode.COMBAT:
        return;
    Party.Damage(Maths.Rand(10, 1, 10) + 50, eDamageType.UNBLOCKABLE)
    Wait()

def On_Using_SI_ThoughtCrystal_2811(p):
    SpecialItem.Take("ThoughtCrystal")
    Animation_Hold(-1, 053_magic3)
    Wait()
    if StuffDone["67_6"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "CrystalSoul_107": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Nightmare_252": Town.NPCList.Remove(npc)
        StuffDone["67_2"] = 1
        ChoiceBox("Remembering the advice about catastrophic effects when using the Thought Crystal near another crystal intelligence, you decide to use it.\n\nYou raise the crystal and concentrate its energies. The crystal begins to vibrate intensely as does Caffen-Bok. The glowing in both becomes quite erratic and the vibrations quite violent.\n\nSuddenly, both the Thought Crystal and Caffen-Bok shatter! A greenish smoke of a tormented soul rises from the shards.\n\nCaffen-Bok is finally dead and at peace after centuries of suffering from the experiments performed on him by your ancestors so long ago.\n\nYou turn to see Rentar-Ihrno looking giving you a glare of pure hatred. It is a glare that literally sends chills down your spine.", eDialogPic.CREATURE, 88, ["OK"])
        StuffDone["67_6"] = 2
        return
    for pc in Party.EachAlivePC():
        pc.SkillPoints += 25
    Message("The Thought Crystal dissolves...")
    Message("   You gain experience!")

def On_Death_Of_SpectralKnight_2812(p):
    if Maths.Rand(1,0,100) < 50:
        Town.PlaceNewNPC(NPCRecord.List["SpectralKnight_197"], Location(20,17), False)
        if Maths.Rand(1,0,100) < 50:
            Town.PlaceNewNPC(NPCRecord.List["SpectralKnight_197"], Location(28,33), False)
            return
        Town.PlaceNewNPC(NPCRecord.List["SpectralKnight_197"], Location(20,33), False)
        return
    Town.PlaceNewNPC(NPCRecord.List["SpectralKnight_197"], Location(28,17), False)
    if Maths.Rand(1,0,100) < 50:
        Town.PlaceNewNPC(NPCRecord.List["SpectralKnight_197"], Location(28,33), False)
        return
    Town.PlaceNewNPC(NPCRecord.List["SpectralKnight_197"], Location(20,33), False)

def ScenarioTimer_x_2813(p):
    Animation_Hold(-1, 090_paralyze)
    Wait()
    MessageBox("Suddenly, you begin to feel \'normal\' again. Your skin returns to its original color and your mind clears up. Unfortunately, you feel it make have caused some permanent damage to you.")
    StuffDone["7_4"] = 0

def ScenarioTimer_x_2814(p):
    if StuffDone["11_0"] >= 1:
        StuffDone["11_0"] += 1
        if StuffDone["11_0"] == 250:
            pass
        if StuffDone["11_0"] >= 80:
            Party.Damage(Maths.Rand(3, 1, 5) + 15, eDamageType.POISON)
            Wait()
            if StuffDone["11_0"] >= 100:
                for pc in Party.EachAlivePC():
                    if pc.LifeStatus == eLifeStatus.ALIVE:
                        pc.Kill(None, eLifeStatus.DUST, True)
                        Wait()
                MessageBox("After trying to resist the deadly poison, you can do so no more. You fall unconscious and within an hour, die. It looks like Zaine succeeded in stopping you...")
                for pc in Party.EachAlivePC():
                    if pc.LifeStatus == eLifeStatus.ALIVE:
                        pc.Kill(None, eLifeStatus.DUST, True)
                        Wait()
                return
            if StuffDone["11_0"] < 81:
                MessageBox("Zaine\'s poison spell is really starting to take over. You don\'t think you have much more time before you will be incapacitated.")
                for pc in Party.EachAlivePC():
                    pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 1))
                Timer(None, 10, False,  "ScenarioTimer_x_2814")
                return
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 1))
            Timer(None, 10, False,  "ScenarioTimer_x_2814")
            return
        if StuffDone["11_0"] < 40:
            Party.Damage(Maths.Rand(1, 1, 5) + 5, eDamageType.POISON)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 1))
            Timer(None, 10, False,  "ScenarioTimer_x_2814")
            return
        Party.Damage(Maths.Rand(2, 1, 5) + 10, eDamageType.POISON)
        Wait()
        if StuffDone["11_0"] == 40:
            MessageBox("You can feel Zaine\'s poison spell getting stronger. You better find a way to counteract its effects soon. You don\'t know how much more of this you can take.")
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 1))
            Timer(None, 10, False,  "ScenarioTimer_x_2814")
            return
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 1))
        Timer(None, 10, False,  "ScenarioTimer_x_2814")
        return

def ScenarioTimer_x_2815(p):
    if StuffDone["13_5"] == 1:
        Animation_Hold(-1, 012_longbow)
        Wait()
        Party.Damage(Maths.Rand(3, 1, 5) + 10, eDamageType.WEAPON)
        Wait()
        Timer(None, 2, False,  "ScenarioTimer_x_2815")
        return

def ScenarioTimer_x_2816(p):
    StuffDone["19_0"] += 1
    if StuffDone["19_0"] == 250:
        pass
    if StuffDone["19_0"] >= 4:
        StuffDone["19_1"] = 1
        StuffDone["18_6"] = 9
        return
    Timer(None, 500, False,  "ScenarioTimer_x_2816")

def ScenarioTimer_x_2817(p):
    StuffDone["100_2"] = 0

def ScenarioTimer_x_2818(p):
    if SpecialItem.PartyHas("Moonstone"):
        for pc in Party.EachAlivePC():
            pc.SP+= 1
        Timer(None, 5, False,  "ScenarioTimer_x_2818")
        return

def ScenarioTimer_x_2819(p):
    StuffDone["27_6"] += 1
    if StuffDone["27_6"] == 250:
        pass
    if StuffDone["27_6"] >= 20:
        StuffDone["27_5"] = 2
        return
    Timer(None, 250, False,  "ScenarioTimer_x_2819")

def ScenarioTimer_x_2820(p):
    Timer(None, 500, False,  "ScenarioTimer_x_2820")
    if Game.Mode == eMode.TOWN:
        return;
    if Game.Mode == eMode.COMBAT:
        return;
    if Maths.Rand(1,0,100) < 50:
        if Maths.Rand(1,0,100) < 10:
            if Maths.Rand(1,0,100) < 50:
                Party.GiveNewItem("Graymold_368")
                return
            if Maths.Rand(1,0,100) < 30:
                Party.GiveNewItem("MandrakeRoot_370")
                return
            Party.GiveNewItem("EmberFlowers_369")
            return
        if Maths.Rand(1,0,100) < 50:
            if Maths.Rand(1,0,100) < 60:
                Party.GiveNewItem("Holly_363")
                return
            Party.GiveNewItem("ComfreyRoot_364")
            return
        if Maths.Rand(1,0,100) < 20:
            Party.GiveNewItem("AsptongueMold_367")
            return
        if Maths.Rand(1,0,100) < 60:
            Party.GiveNewItem("GlowingNettle_365")
            return
        Party.GiveNewItem("Wormgrass_366")
        return

def ScenarioTimer_x_2821(p):
    StuffDone["110_0"] += 1
    if StuffDone["110_0"] == 250:
        WorldMap.DeactivateTrigger(Location(211,242))
    if StuffDone["110_0"] >= 25:
        StuffDone["110_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2821")

def ScenarioTimer_x_2822(p):
    StuffDone["111_0"] += 1
    if StuffDone["111_0"] == 250:
        WorldMap.DeactivateTrigger(Location(211,245))
    if StuffDone["111_0"] >= 25:
        StuffDone["111_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2822")

def ScenarioTimer_x_2823(p):
    StuffDone["112_0"] += 1
    if StuffDone["112_0"] == 250:
        WorldMap.DeactivateTrigger(Location(217,247))
    if StuffDone["112_0"] >= 25:
        StuffDone["112_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2823")

def ScenarioTimer_x_2824(p):
    StuffDone["113_0"] += 1
    if StuffDone["113_0"] == 250:
        WorldMap.DeactivateTrigger(Location(214,245))
    if StuffDone["113_0"] >= 25:
        StuffDone["113_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2824")

def ScenarioTimer_x_2825(p):
    StuffDone["114_0"] += 1
    if StuffDone["114_0"] == 250:
        pass
    if StuffDone["114_0"] >= 25:
        StuffDone["114_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2825")

def ScenarioTimer_x_2826(p):
    StuffDone["114_1"] += 1
    if StuffDone["114_1"] == 250:
        WorldMap.AlterTerrain(Location(44,227), 1, None)
        WorldMap.DeactivateTrigger(Location(44,227))
    if StuffDone["114_1"] >= 25:
        StuffDone["114_1"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2826")

def ScenarioTimer_x_2827(p):
    StuffDone["100_3"] += 1
    if StuffDone["100_3"] == 250:
        pass
    if StuffDone["100_3"] >= 12:
        StuffDone["100_3"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2827")

def ScenarioTimer_x_2828(p):
    StuffDone["44_0"] += 1
    if StuffDone["44_0"] == 250:
        TownMap.List["Rune_38"].DeactivateTrigger(Location(37,13))
    if StuffDone["44_0"] >= 75:
        StuffDone["44_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2828")

def ScenarioTimer_x_2829(p):
    StuffDone["113_1"] += 1
    if StuffDone["113_1"] == 250:
        pass
    if StuffDone["113_1"] >= 25:
        StuffDone["113_1"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2829")

def ScenarioTimer_x_2830(p):
    StuffDone["110_1"] += 1
    if StuffDone["110_1"] == 250:
        WorldMap.DeactivateTrigger(Location(253,172))
    if StuffDone["110_1"] >= 25:
        StuffDone["110_1"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2830")

def ScenarioTimer_x_2831(p):
    StuffDone["116_0"] += 1
    if StuffDone["116_0"] == 250:
        WorldMap.DeactivateTrigger(Location(280,179))
    if StuffDone["116_0"] >= 25:
        StuffDone["116_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2831")

def ScenarioTimer_x_2832(p):
    StuffDone["111_1"] += 1
    if StuffDone["111_1"] == 250:
        WorldMap.DeactivateTrigger(Location(62,87))
    if StuffDone["111_1"] >= 25:
        StuffDone["111_1"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2832")

def ScenarioTimer_x_2833(p):
    StuffDone["112_1"] += 1
    if StuffDone["112_1"] == 250:
        WorldMap.DeactivateTrigger(Location(186,59))
    if StuffDone["112_1"] >= 25:
        StuffDone["112_1"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2833")

def ScenarioTimer_x_2834(p):
    StuffDone["115_0"] += 1
    if StuffDone["115_0"] == 250:
        WorldMap.AlterTerrain(Location(63,195), 1, None)
        WorldMap.DeactivateTrigger(Location(63,195))
    if StuffDone["115_0"] >= 25:
        StuffDone["115_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2834")

def ScenarioTimer_x_2835(p):
    StuffDone["117_0"] += 1
    if StuffDone["117_0"] == 250:
        pass
    if StuffDone["117_0"] >= 25:
        StuffDone["117_0"] = 0
        return
    Timer(None, 300, False,  "ScenarioTimer_x_2835")

def ScenarioTimer_x_2836(p):
    if SpecialItem.PartyHas("ThoughtCrystal"):
        for pc in Party.EachAlivePC():
            pc.AwardXP(3)
        Timer(None, 50, False,  "ScenarioTimer_x_2836")
        return

def GlobalCall_ImperialPalace_2838(p):
    ChoiceBox("It does not take long for the scry to be completed. Although the curse of the island limits the scry, there is definite activity at the center of the isle. There is a large, unnatural, and alien energy source in the center.\n\nWith that the Prime Director orders one of his Dervishes to oversee the construction of a fortress on the isle. The bureaucracy is informed to allocate resources for the quick construction of this base.\n\n\"Listen up! This may be nothing, but it is the best we have. I feel that time is running out. I will need you to go and investigate the island. As we speak, cargo ships are carrying resources for the construction of a base there.\n\nBy the time you arrive at Evergold, we shall know whether or not a threat exists. If there is, the construction of a base will be well under way. I am sending you there because I feel you are best equipped to deal with this.\n\nBe sure to prepare as best you can. When you are ready to depart, head to the naval base north of Evergold. You will be transferred to the island assuming our theory is correct. After that, there will be no turning back.\n\nNow Dervishes, prepare for your finest hour!\"", eDialogPic.STANDARD, 4, ["OK"])

def ScenarioTimer_x_2841(p):
    StuffDone["18_6"] = 5
    StuffDone["18_9"] = 1

def GlobalCall_Minarch_2843(p):
    Timer(None, 5, False,  "ScenarioTimer_x_2818")

def GlobalCall_SolKeep_2844(p):
    Timer(None, 250, False,  "ScenarioTimer_x_2819")

def GlobalCall_MorbanesLair_2845(p):
    ChoiceBox("This tome describes Morbane\'s plot: Overthrowing the Empire will require the use of non-conventional units, those of a highly magical nature. The problem lies in the difficulty with summoning, but this can be overcome by a device called the Nethergate.\n\nAlthough much research needs to be done, I believe that the brilliant archmage Balkis is capable of developing this Nethergate. In addition, the order of Odin, has granted use of their resources to make this possible.\n\nAnother key part to the attack will be the development of powerful and impenetrable magical barriers. My personal study on this subject has yielded some results. I expect the refinement to be completed by my enlisted order of Watchpoint in Sorcrega.\n\nCreating a disturbance will make the Empire less likely to discover my plans in Stolgrad. I believe the Troglodytes are a capable race, and with the aid of Halloth, they can cause enough trouble to provide a suitable distraction.\n\nTo hasten the surrender of the Empire and limit loss of life, I must attack the Empire\'s food supply prior to the invasion. A fungus released in Agran will do the trick. With an impending famine and war, the Empire will have no choice but surrender.\n\nAfter my takeover, to achieve my omniscient and benevolent rule I shall require life energy from magi. Sorcrega has an excellent supply. I shall employ a certain mage, Odix, to keep the authorities away from my plans.", eDialogPic.CREATURE, 60, ["OK"])

def GlobalCall_Sanctuary_2846(p):
    if StuffDone["51_0"] >= 2:
        if StuffDone["51_0"] >= 4:
            if StuffDone["51_1"] == 36:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_0"] < 3:
            if StuffDone["51_1"] == 28:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 33:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_0"] < 1:
        if StuffDone["51_1"] == 0:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 5:
            StuffDone["51_0"] = 1
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 20:
            StuffDone["51_0"] = 4
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 8:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 13:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_1"] == 21:
        StuffDone["51_1"] += 1
        if StuffDone["51_1"] == 250:
            pass
        return
    StuffDone["51_1"] = 0

def GlobalCall_Sanctuary_2847(p):
    if StuffDone["51_0"] >= 2:
        if StuffDone["51_0"] >= 4:
            if StuffDone["51_1"] == 38:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_0"] < 3:
            if StuffDone["51_1"] == 0:
                StuffDone["51_1"] = 26
                return
            if StuffDone["51_1"] == 30:
                StuffDone["51_0"] = 0
                StuffDone["51_1"] = 0
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 31:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_0"] < 1:
        if StuffDone["51_1"] == 2:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 6:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 15:
            StuffDone["51_0"] = 3
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 0:
            StuffDone["51_1"] = 11
            return
        if StuffDone["51_1"] == 18:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_1"] == 24:
        StuffDone["51_1"] += 1
        if StuffDone["51_1"] == 250:
            pass
        return
    StuffDone["51_1"] = 0

def GlobalCall_Sanctuary_2848(p):
    if StuffDone["51_0"] >= 2:
        if StuffDone["51_0"] >= 4:
            if StuffDone["51_1"] == 0:
                StuffDone["51_1"] = 36
                return
            if StuffDone["51_1"] == 40:
                StuffDone["51_0"] = 0
                StuffDone["51_1"] = 0
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_0"] < 3:
            if StuffDone["51_1"] == 27:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 34:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_0"] < 1:
        if StuffDone["51_1"] == 4:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 9:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 12:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 1:
            StuffDone["51_1"] = 17
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_1"] == 22:
        StuffDone["51_1"] += 1
        if StuffDone["51_1"] == 250:
            pass
        return
    StuffDone["51_1"] = 0

def GlobalCall_Sanctuary_2849(p):
    if StuffDone["51_0"] >= 2:
        if StuffDone["51_0"] >= 4:
            if StuffDone["51_1"] == 37:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_0"] < 3:
            if StuffDone["51_1"] == 29:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 32:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_0"] < 1:
        if StuffDone["51_1"] == 1:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 7:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 14:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 19:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_1"] == 0:
        StuffDone["51_1"] = 21
        return
    if StuffDone["51_1"] == 25:
        StuffDone["51_0"] = 0
        StuffDone["51_1"] = 0
        return
    StuffDone["51_1"] = 0

def GlobalCall_Sanctuary_2850(p):
    if StuffDone["51_0"] >= 2:
        if StuffDone["51_0"] >= 4:
            if StuffDone["51_1"] == 39:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_0"] < 3:
            if StuffDone["51_1"] == 26:
                StuffDone["51_1"] += 1
                if StuffDone["51_1"] == 250:
                    pass
                return
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 0:
            StuffDone["51_1"] = 31
            return
        if StuffDone["51_1"] == 35:
            StuffDone["51_0"] = 0
            StuffDone["51_1"] = 0
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_0"] < 1:
        if StuffDone["51_1"] == 3:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 0:
            StuffDone["51_1"] = 6
            return
        if StuffDone["51_1"] == 10:
            StuffDone["51_0"] = 2
            StuffDone["51_1"] = 0
            return
        if StuffDone["51_1"] == 11:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        if StuffDone["51_1"] == 17:
            StuffDone["51_1"] += 1
            if StuffDone["51_1"] == 250:
                pass
            return
        StuffDone["51_1"] = 0
        return
    if StuffDone["51_1"] == 23:
        StuffDone["51_1"] += 1
        if StuffDone["51_1"] == 250:
            pass
        return
    StuffDone["51_1"] = 0

def GlobalCall_NorthwesternStolgrad_2852(p):
    if StuffDone["13_5"] == 0:
        StuffDone["13_5"] = 1
        if StuffDone["13_5"] == 1:
            Animation_Hold(-1, 012_longbow)
            Wait()
            Party.Damage(Maths.Rand(3, 1, 5) + 10, eDamageType.WEAPON)
            Wait()
            Timer(None, 2, False,  "ScenarioTimer_x_2815")
            return
        return

def GlobalCall_NorthwesternStolgrad_2853(p):
    MessageBox("You are approached by a patrol of Empire soldiers. After a short exchange of news, they depart.")
    p.CancelAction = True
