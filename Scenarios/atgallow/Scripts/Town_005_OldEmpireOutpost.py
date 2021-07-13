def Generate_Wandering_5_OldEmpireOutpost(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Soldier_13"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Archer_19"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Cultist_24"]])
        elif r1 == 3:
            npcs.append([2,NPCRecord.List["Brigand_18"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(22,55)
                elif r2 == 1: l = Location(29,45)
                elif r2 == 2: l = Location(25,18)
                elif r2 == 3: l = Location(45,32)
                
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

def OldEmpireOutpost_36_MapTrigger_59_32(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,28)
    Party.MoveToMap(TownMap.List["BeneathVega_4"])

def OldEmpireOutpost_38_MapTrigger_55_30(p):
    if StuffDone["0_7"] == 250:
        return
    StuffDone["0_7"] = 250
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(55,30))
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(55,31))
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(55,32))
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(55,33))
    ChoiceBox("You near the \'Main Temple\' of the Followers. You discover that it is not really a temple at all! The outside walls are decorated with the \'Sword and Sun\' insignia of the Empire. The structure itself looks quite old, but still very stable.\n\nYou have heard of these places. In more unstable times, the Empire built and maintained secret underground fortresses throughout the world to serve as an internal gate into invaded areas.\n\nIn times of security such as these, many of these fortresses have been abandoned to cut military costs. Apparently, another group (the Followers) has decided to take up residence.\n\nYou can bet this underground fortress was not built with the same care as the highly protected surface forts which are actually threatened by invasion. So infiltrating it should not be overly difficult.", eDialogPic.TERRAIN, 232, ["OK"])

def OldEmpireOutpost_42_MapTrigger_15_50(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["0_8"] == 250:
        return
    StuffDone["0_8"] = 250
    MessageBox("It looks like the cultists are raising giant spiders. You shudder when you see the bodies of fellow Empire soldiers thrown to the creatures. You notice something strange about the spiders, they can cast spells!")

def OldEmpireOutpost_43_MapTrigger_15_18(p):
    if StuffDone["0_9"] == 250:
        return
    StuffDone["0_9"] = 250
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(15,18))
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(14,18))
    TownMap.List["OldEmpireOutpost_5"].DeactivateTrigger(Location(16,18))
    ChoiceBox("You\'ve made your way into the Main Temple of the \'Followers\'. You had expected something more impressive. However, it is little more elegant than the temples found in Empire forts. You can bet this temple was converted to fit their needs.\n\nAs you noticed on the sign outside, a ritual is currently in progress. You have no idea at all what the intent of the ritual was. All you know, is its practitioners are not at all pleased at having it interrupted.\n\nYou look around but do not see Zaine anywhere in this temple. He must be somewhere else right now. Nevertheless, you have some angry cultists ready to destroy you.", eDialogPic.CREATURE, 24, ["OK"])

def OldEmpireOutpost_46_MapTrigger_13_13(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(13,12)).Num == 128:
        if SpecialItem.PartyHas("IronKey"):
            MessageBox("This door has a large lock built into it. You try the key you found around the Cult Priest\'s neck. It unlocks the padlock with no trouble!")
            t = Town.TerrainAt(Location(13,12))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(13,12)).TransformTo
                Town.AlterTerrain(Location(13,12), 0, t)
            return
        MessageBox("There is a large lock built into this door. Try as you might to open it, you cannot. You will need a the right key to get in here.")
        return

def OldEmpireOutpost_47_MapTrigger_18_10(p):
    result = ChoiceBox("It looks like you have found Zaine\'s journal. You may find some valuable information inside. Care to take a peek?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("The journal contains many of Zaine\'s personal thoughts and his visions from the dark god called Morbane. In the more recent entries, you read about the curse he intends to place upon the crops of the Agran Sector.\n\nThe cultists are growing some mutant mold which can overtake most of the staple crops grown. Once sufficient quantities have grown, they plan to unleash it into the water where it can infect the crops from irrigation.\n\nThe location of the mold factory is in a small cave north of Lake Praddor. You also determine from Zaine\'s last entry, that he has gone there to oversee the final processes. It does not specify how long those will take.\n\nHowever, he does make some interesting comments. \"Soon Morbane will make his coming. It is imperative that the fungus be released by that time. There will be a small war, which the Empire will have no choice but to surrender to the control of Morbane.\n\nThe destruction of the crops in Agran will, obviously, cause food shortages throughout the continent. Once the war breaks out, the people will be starving and demanding an answer to their needs. The Empire will have to surrender or face rebellion.\n\nIn the end, more lives shall be saved because the conflict will end earlier. Once Morbane has control, it shall be the beginning of a new age!\" You had better report this to Bladesman Kelli!", eDialogPic.STANDARD, 20, ["OK"])
        if StuffDone["0_2"] == 3:
            StuffDone["0_2"] = 4
            return
        return

def OldEmpireOutpost_48_MapTrigger_7_56(p):
    result = ChoiceBox("You\'ve found somebody\'s spell book. Perhaps you could learn some useful knowledge from its contents. However, many mages do trap their spell books. Do you read it and hope it\'s not trapped?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 8:
            MessageBox("The spell book\'s contents are remedial at best detailing the simplest of spells such as \'Flame\' or \'Slow\'. You doubt its owner could have trapped it even if he wanted to.\n\nAlthough most of the spells are too simple for you. The spell \'Ice Bolt\' is of interest. You learn  the ritual for later use.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_ice_bolt")
            return
        MessageBox("The spell book\'s contents are remedial at best detailing the simplest of spells such as \'Flame\' or \'Slow\'. You doubt its owner could have trapped it even if he wanted to.\n\nEven with your simple level of competency, you can understand this. However, there are a couple spells out of your grasp. You will need more \'Mage Lore\' to understand them.")
        return

def OldEmpireOutpost_49_MapTrigger_14_6(p):
    MessageBox("The Prophet, Zaine, has a fair collection of classical works, he must have refined literary pursuits. Among them you discover something interesting called the \"Beginner\'s Golem Handbook.\"")

def OldEmpireOutpost_50_MapTrigger_13_6(p):
    MessageBox("The Prophet, Zaine, has a fair collection of classical works, he must have refined literary pursuits in addition to seeking death and destruction.")

def OldEmpireOutpost_53_TownTimer_6(p):
    Animation_Hold(-1, 066_disease)
    Wait()
    MessageBox("Suddenly, you start to feel quite ill. You believe that the priest\'s curse placed upon you at his death has come into effect.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 1))

def OldEmpireOutpost_54_CreatureDeath2(p):
    MessageBox("You slay the cult\'s priest. He falls to the ground, in defeat. As he is dying, he mutters some arcane words that you do not comprehend. After he dies, you take a key around his neck.")
    SpecialItem.Give("IronKey")
    Timer(Town, 20, False, "OldEmpireOutpost_53_TownTimer_6", eTimerType.DELETE)

def Talking_5_35(p):
    if Party.Gold >= 13:
        Party.Gold -= 13
        p.TalkingText = "You pay the gold and are poured a round of drinks. This has got to be the best beer you have ever had. The bartender turns to you. \"Impressed? Thought you would be. The drinks are magically enhanced in flavor.\" That would explain it."
    else:
        p.TalkingText = "You cannot afford it."

def Talking_5_36(p):
    if Party.Gold < 40:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 40
        Party.Pos = Location(44, 41)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "You are escorted to your rooms. \"Have a good night\'s sleep. I\'m sure you will. The owners have employed some good wizards to make everything comfortable.\" He wasn\'t lying either. You had one of the best rests ever! Well worth the money."
        CentreView(Party.Pos, False)
