
def LairofCasserBok_396_MapTrigger_32_26(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(35,29)).Num == 148:
        Town.AlterTerrain(Location(35,29), 0, TerrainRecord.UnderlayList[147])
        Town.AlterTerrain(Location(36,29), 0, TerrainRecord.UnderlayList[148])
        Message("Click.")
        return
    Message("Clang.")
    for x in range(35, 40):
        for y in range(29, 30):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])
    Town.AlterTerrain(Location(35,29), 0, TerrainRecord.UnderlayList[148])

def LairofCasserBok_397_MapTrigger_42_26(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(37,29)).Num == 148:
        Town.AlterTerrain(Location(37,29), 0, TerrainRecord.UnderlayList[147])
        Town.AlterTerrain(Location(38,29), 0, TerrainRecord.UnderlayList[148])
        Message("Click.")
        return
    Message("Clang.")
    for x in range(35, 40):
        for y in range(29, 30):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])
    Town.AlterTerrain(Location(35,29), 0, TerrainRecord.UnderlayList[148])

def LairofCasserBok_398_MapTrigger_42_22(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(36,29)).Num == 148:
        Town.AlterTerrain(Location(36,29), 0, TerrainRecord.UnderlayList[147])
        Town.AlterTerrain(Location(37,29), 0, TerrainRecord.UnderlayList[148])
        Message("Click.")
        return
    Message("Clang.")
    for x in range(35, 40):
        for y in range(29, 30):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])
    Town.AlterTerrain(Location(35,29), 0, TerrainRecord.UnderlayList[148])

def LairofCasserBok_399_MapTrigger_32_22(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(38,29)).Num == 148:
        Town.AlterTerrain(Location(38,29), 0, TerrainRecord.UnderlayList[147])
        Town.AlterTerrain(Location(39,29), 0, TerrainRecord.UnderlayList[148])
        Message("Click.")
        return
    Message("Clang.")
    for x in range(35, 40):
        for y in range(29, 30):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[147])
    Town.AlterTerrain(Location(35,29), 0, TerrainRecord.UnderlayList[148])

def LairofCasserBok_400_MapTrigger_15_42(p):
    if StuffDone["17_0"] == 250:
        return
    StuffDone["17_0"] = 250
    TownMap.List["LairofCasserBok_17"].DeactivateTrigger(Location(15,42))
    ChoiceBox("You enter the hall of Casser-Bok. He (or she, or it) is a Crystal Soul. These are the most sacred beings of the Vahnatai people, their Gods, for all practical purposes. They are the physical form of the spirits of their most valued ancestors.\n\nNormally, they are kept at the heart of Vahnatai lands, in order to to protect them from all harm. Yet, this Crystal Soul is here, far away from Vahnatai lands, isolated in this chilly tomb.\n\nThis treatment would normally be unthinkable to the Vahnatai. You wonder why it\'s out here.\n\nYou hear a gentle voice in your head, making itself felt inside your mind. The crystal soul says \"I am Casser-Bok. Welcome to my home. Please, approach my glory.\"", eDialogPic.CREATURE, 88, ["OK"])

def LairofCasserBok_401_MapTrigger_30_42(p):
    if StuffDone["17_2"] >= 1:
        MessageBox("When you approach the portal, a strange force holds you back. You try to get close to it, but invisible hands hold you away. Casser-Bok no longer wants your company.")
        return
    result = ChoiceBox("When you try to get close to this portal, you find that only the nearest person can approach unimpeded. Everyone else in your group is held back by invisible hands.\n\nA little experimentation reveals that the portal will only let one of you close to it. Whoever enters this place will have to do so alone.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        pc = SelectPCBox("One of you steps inside the portal. There is a brief moment of vertigo, and you find yourself in a different place.",True)
        if pc == None:
            p.CancelAction = True
            return
        Party.Split(pc, Location(25,42))
        Sound.Play("010_teleport")
        return
    p.CancelAction = True

def LairofCasserBok_402_MapTrigger_26_42(p):
    if StuffDone["17_2"] >= 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You try to enter the portal to escape from the now erratic crystal soul. Unfortunately, you don\'t get within ten feet of it. Whenever you get close, an invisible force strikes you in the chest and throws you back.\n\nYou\'ll have to find another way out.")
        return
    result = ChoiceBox("This portal has been placed here to reunite you with your party, if you\'re done here for now.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        if Party.IsSplit:
            Party.Reunite()
            Sound.Play("010_teleport")
        return
    p.CancelAction = True

def LairofCasserBok_403_MapTrigger_4_30(p):
    MessageBox("When you step on this rune, your lips feel slightly numb for a moment. Nothing else happens.")

def LairofCasserBok_404_MapTrigger_2_32(p):
    result = ChoiceBox("The Vahnatai rely on crystals for their needs as much as possible. For example, crystals such as this are used as magical books. Peering into one and concentrating, you can see words move slowly by for you to read.\n\nThis crystal looks very dark and old. You suspect that the magic of such stones fades with time, and this one has probably been here for centuries. Still, you might be able to read something inside it.", eDialogPic.TERRAIN, 168, ["Leave", "Read"])
    if result == 1:
        MessageBox("You stare into the murky depths of the stone until you give yourself a mild headache. You can\'t make out anything.")
        return

def LairofCasserBok_407_MapTrigger_6_32(p):
    result = ChoiceBox("The Vahnatai rely on crystals for their needs as much as possible. For example, crystals such as this are used as magical books. Peering into one and concentrating, you can see words move slowly by for you to read.\n\nThis crystal looks very dark and old. You suspect that the magic of such stones fades with time, and this one has probably been here for centuries. Still, you might be able to read something inside it.", eDialogPic.TERRAIN, 168, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
            MessageBox("At first, you think this crystal is dark and dead. Then, looking deep inside, you realize that magical formulae are scrolling by inside. You concentrate on them, trying to make some sense of them.\n\nFortunately, your massive knowledge of Mage Lore pays off. You manage to understand the spell the crystal is showing you. You can now cast Quickfire.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_quickfire")
            return
        MessageBox("At first, you think this crystal is dark and dead. Then, looking deep inside, you realize that magical formulae are scrolling by inside. You concentrate on them, trying to make some sense of them.\n\nUnfortunately, it\'s to no avail. They\'re too alien, too confusing, and too dim. You leave the crystal behind, getting nothing for your troubles but a splitting headache.")
        return

def LairofCasserBok_408_MapTrigger_2_1(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("When you try to enter the portal, it disappears. When you back away, it reappears. Casser-Bok must want you to stay right here.")

def LairofCasserBok_409_MapTrigger_2_3(p):
    if StuffDone["17_4"] == 250:
        return
    StuffDone["17_4"] = 250
    TownMap.List["LairofCasserBok_17"].DeactivateTrigger(Location(2,3))
    MessageBox("This cavern has a smooth, flat floor, with long, winding cobblestone walkways set into it. The walkways seem like sort of a waste of effort. Maybe they appealed to Casser-Bok\'s sense of aesthetics.")

def LairofCasserBok_410_MapTrigger_24_20(p):
    if StuffDone["17_5"] == 250:
        return
    StuffDone["17_5"] = 250
    TownMap.List["LairofCasserBok_17"].DeactivateTrigger(Location(24,20))
    MessageBox("When you walk through the door, the first things you see are bones. Piles of them. They\'re very long and delicate, with large, rounded skulls with huge eye sockets. It doesn\'t take long to figure out what they are - Vahnatai remains.\n\nWorse, they were clearly killed by violence. Some are scarred by fire. Others have been crushed by weapon blows. Casser-Bok must be even more mad than you thought ... he\'s been killing his own people.")

def LairofCasserBok_411_MapTrigger_25_26(p):
    if StuffDone["17_6"] == 250:
        return
    StuffDone["17_6"] = 250
    TownMap.List["LairofCasserBok_17"].DeactivateTrigger(Location(25,26))
    MessageBox("You find yourself face to face with Casser-Bok\'s heavy squad. They\'re Vahnavoi. They\'re sort of like Vahnatai zombies, only much worse ...")
    Town.PlaceEncounterGroup(1)

def LairofCasserBok_412_MapTrigger_28_10(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(40,5)).Num == 147:
        MessageBox("You hear, echoing down the corridors, what sounds like a portcullis opening.")
        Town.AlterTerrain(Location(40,5), 0, TerrainRecord.UnderlayList[148])
        return

def LairofCasserBok_414_MapTrigger_30_8(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(40,5)).Num == 148:
        MessageBox("You hear what sounds like a gate slamming shut.")
        Town.AlterTerrain(Location(40,5), 0, TerrainRecord.UnderlayList[147])
        return

def LairofCasserBok_423_MapTrigger_39_36(p):
    if StuffDone["17_3"] == 250:
        return
    result = ChoiceBox("Finally, you reach your prize, the reward for all this pain and inconvenience. You open the box and find a quartz crystal, about as long as your hand.\n\nAt first, you\'re disappointed. It seems like nothing more than an ordinary rock. Then you pick it up and look through it. It\'s remarkable! When you peer through it, everything beyond is visible in incredibly clear detail.\n\nEvery mote of dust, every crack, every blemish in the stone walls becomes apparent to you. When light passes through the stone, it seems to come through brighter on the other side.\n\nFor an adventurer, this thing is not very useful. To a magical researcher, however, this crystal is quite a prize.", eDialogPic.TERRAIN, 167, ["Take", "Leave"])
    if result == 0:
        StuffDone["17_3"] = 250
        TownMap.List["LairofCasserBok_17"].DeactivateTrigger(Location(39,36))
        SpecialItem.Give("CrystalofPurity")
    return

def LairofCasserBok_424_MapTrigger_34_34(p):
    result = ChoiceBox("At long last, you have reached the portal out of here. Looking through it, you can just make out your compatriots waiting on the other side. Do you rejoin them?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        if Party.IsSplit:
            Party.Reunite()
            Sound.Play("010_teleport")
        return

def LairofCasserBok_425_MapTrigger_11_33(p):
    if StuffDone["17_2"] >= 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
            Animation_Vanish(Party.LeaderPC, True, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(2,2))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This portal has very little energy coursing through it. It isn\'t able to take you anywhere.")

def LairofCasserBok_426_CreatureDeath0(p):
    MessageBox("Your final blow shatters Casser-Bok. As the shards fly across the room, a spirit rises from the fragments, floats up to the ceiling, and disappears. As you watch it rise, its final trap roars into action.\n\nQuickfire appears all throughout the crypt. The portals you counted on for your escape disappear. The crypt entrance caves in, making escape impossible. All of this happens in the span of moments. You\'re trapped inside, and burn up.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def LairofCasserBok_427_TalkingTrigger8(p):
    if StuffDone["17_1"] == 0:
        p.TalkingText = "\"There is a Vahnatai outpost hidden to the north. I want you to take a message to them. I wish you to tell them I wish to rejoin my people. The outpost is hidden, but I can help you find it.\"\n\n\"If you carry this message and return this response to me, I will give you the Crystal of Purity.\""
        StuffDone["17_1"] = 1
        TownMap.List["WormyHollow_19"].Hidden = False
        return
    if StuffDone["17_2"] == 0:
        if StuffDone["17_7"] >= 1:
            p.TalkingText = "You tell Casser-Bok about the Vahnatai\'s rejection. The creature screams in fury! The force of its yell throws you to the floor. Then it speaks. \"Fine, then. My return to glory must wait. One day, they will accept my rule! I am sure of it!\"\n\n\"For now, I owe you a reward. Fine. Enter the northern portal. But I doubt you will survive to reach it.\""
            StuffDone["17_2"] = 1
            return
        p.TalkingText = "\"As I said, take my message to the Vahnatai outpost to the north, to the west of the troglodyte castle. Then return their response to me, and I will give you the Crystal of Purity.\""
        return

def LairofCasserBok_428_TalkingTrigger10(p):
    TownMap.List["WormyHollow_19"].Hidden = False
