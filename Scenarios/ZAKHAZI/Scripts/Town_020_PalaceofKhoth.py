
def PalaceofKhoth_457_MapTrigger_40_8(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(45,4)).Num == 130:
        if StuffDone["20_0"] >= 1:
            MessageBox("When you walk around the corner, the massive iron gates blocking your exit from Khoth\'s fortress come into view. They\'re still closed. At first, you get the uncomfortable suspicion that Khoth won\'t meet his end of the bargain.\n\nThen one of Khoth\'s spirits floats by you towards the gates. It makes a few motions with its spectral hands. With a deafening creaking sound, one of the gates opens. At last, escape from the Za-Khazi Run is in your grasp.")
            Town.AlterTerrain(Location(45,4), 0, TerrainRecord.UnderlayList[131])
            return
        return

def PalaceofKhoth_458_MapTrigger_31_7(p):
    result = ChoiceBox("Looking through the opening, you can see several bookshelves, each heavily laden with all manner of intriguing tomes, scrolls, palimpsests, almanacs, maps, spell books, and works of fiction.\n\nA large part of the amazing body of knowledge amassed by Khoth the dragon lies before you, and the only thing keeping you from it is a large protective rune engraved on the floor in front of you.\n\nPass it, and you can have access to some of Khoth\'s knowledge. Do you?", eDialogPic.TERRAIN, 124, ["Leave", "Enter"])
    if result == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You try to force yourself over the rune, taking the punishment it can deal out in return for the rewarding knowledge beyond. Alas, the power of the rune is too great for you to overcome.\n\nEventually, you are thrown backwards, but not before the magical guardian sears you thoroughly.")
        Party.Damage(Maths.Rand(8, 1, 9) + 1, eDamageType.FIRE)
        Wait()
        return
    p.CancelAction = True

def PalaceofKhoth_470_MapTrigger_37_7(p):
    if StuffDone["20_1"] == 250:
        return
    StuffDone["20_1"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(37,7))
    MessageBox("You look longingly through this opening, staring greedily at the variety of tomes beyond. Unfortunately, a powerful magical rune is etched into the floor in front of you, preventing you from entering.\n\nThen you notice that the rune is damaged. Somehow, the floor has become cracked, and the glyph has been broken slightly. You are able to pass it completely unharmed.")

def PalaceofKhoth_471_MapTrigger_22_12(p):
    if StuffDone["20_2"] == 250:
        return
    StuffDone["20_2"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(22,12))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(22,11))
    ChoiceBox("At last, you come face to face with the dangerous and duplicitous Khoth, a member of that most ancient and feared race - the dragons. He may well be the largest creatures you\'ve ever seen, eighty feet and ten tons of pure danger.\n\nEven though he told his golems to kill you and though you are heavily armed and well prepared to face him, he seems completely relaxed and unconcerned by your presence. When he sees you, he lazily motions with a massive claw for you to approach.\n\nWhen you hesitate, he says \"Oh, don\'t waste my time. Trying to slay you was a whim. My whim is now to let you live. I know what you want. I know you are heading to the north. Come to me, so that we may deal.\"", eDialogPic.STANDARD, 12, ["OK"])

def PalaceofKhoth_473_MapTrigger_27_20(p):
    if StuffDone["20_3"] == 250:
        return
    StuffDone["20_3"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(27,20))
    MessageBox("You enter the northern half of Khoth\'s fortress, where the mighty beast resides. As you do, a shade walks past you towards the libraries. You see several of the insubstantial creatures flitting about, carrying books, cleaning, and being useful.\n\nKhoth, like all dragons, has some treasure. However, it\'s in front of you, scattered about and covered with dust. Khoth\'s interest is in books and knowledge, and his avarice for ancient tomes is all consuming.")

def PalaceofKhoth_474_MapTrigger_43_13(p):
    result = ChoiceBox("You step over the charred and splintered bones and look through this opening. You can\'t help but feel twinges of greed for what you see beyond. Here is where Khoth keeps his most valued and ancient scrolls and tomes.\n\nEven from here, you think you can sense the energy emanating from these works, books which must contain only the most arcane of knowledge and powerful of rituals.\n\nOf course, that energy might instead be coming from the protective glyphs in front of you, glyphs you have no trouble recognizing as powerful, protective, and totally lethal. Trying to cross them would be an incredible risk. But the rewards ...", eDialogPic.TERRAIN, 124, ["Leave", "Enter"])
    if result == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You knew the effects of the glyphs when you crossed them would be bad. You had know idea they would be this strong. Waves of force pummel you. Flames envelop you. Searing wind throws you back.\n\nAs you get tossed about, you grit your teeth and try your best to survive ...")
        Party.Damage(Maths.Rand(20, 1, 10) + 0, eDamageType.WEAPON)
        Wait()
        Party.Damage(Maths.Rand(20, 1, 10) + 0, eDamageType.MAGIC)
        Wait()
        Party.Damage(Maths.Rand(20, 1, 10) + 0, eDamageType.UNBLOCKABLE)
        Wait()
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Probably a wise choice. The bones surrounding you are warning enough.")

def PalaceofKhoth_476_MapTrigger_39_4(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 14:
        MessageBox("The scrolls in this rack are dedicated to religious rituals, from all times and all races. One of the scrolls is of extra interest - it describes how to raise people from the dead.\n\nThe paper is old, cracked, and faded, and the ritual is described in peculiar and hard to understand terms. Fortunately, your trained eye picks out the key details. You can now cast the spell Resurrect.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_resurrect")
        return
    MessageBox("The scrolls in this rack are dedicated to religious rituals, from all times and all races. One of the scrolls is of extra interest - it describes how to raise people from the dead.\n\nUnfortunately, it\'s written in a rather obscure tongue, and you are unable to understand several key parts of the ritual. Not wanted to risk angering Khoth, you leave the valuable scroll behind.")

def PalaceofKhoth_477_MapTrigger_23_19(p):
    if StuffDone["140_0"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_0"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(23,19))
    pc.RunTrap(eTrapType.RANDOM, 3, 20)

def PalaceofKhoth_478_MapTrigger_23_17(p):
    if StuffDone["140_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_1"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(23,17))
    pc.RunTrap(eTrapType.RANDOM, 3, 13)

def PalaceofKhoth_479_MapTrigger_30_18(p):
    if StuffDone["140_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_2"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(30,18))
    pc.RunTrap(eTrapType.RANDOM, 3, 25)

def PalaceofKhoth_480_MapTrigger_31_16(p):
    if StuffDone["140_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_3"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(31,16))
    pc.RunTrap(eTrapType.RANDOM, 3, 20)

def PalaceofKhoth_481_MapTrigger_24_15(p):
    if StuffDone["140_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_4"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(24,15))
    pc.RunTrap(eTrapType.RANDOM, 3, 15)

def PalaceofKhoth_482_MapTrigger_30_14(p):
    if StuffDone["140_5"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_5"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(30,14))
    pc.RunTrap(eTrapType.RANDOM, 3, 13)

def PalaceofKhoth_483_MapTrigger_23_8(p):
    if StuffDone["140_6"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["140_6"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(23,8))
    pc.RunTrap(eTrapType.RANDOM, 3, 14)

def PalaceofKhoth_484_MapTrigger_4_29(p):
    if StuffDone["20_4"] == 250:
        return
    StuffDone["20_4"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(4,29))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(3,28))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(2,27))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(1,26))
    ChoiceBox("One of the statues in this huge hall turns to speak with you. \"Khoth sends his congratulations to you. Not all are able to pass his labyrinth of shifting floors.\"\n\n\"However, in the intervening time, he has realized that it would be much simpler and easier to simply have you slain and take for himself whatever treasures you have to offer him. Goodbye.\"\n\nSeveral of the other statues begin to move. You notice that they have an odd, gleaming metallic sheen, and several of them have large crystals set into their bodies. They move to attack you.", eDialogPic.TERRAIN, 133, ["OK"])
    Town.PlaceEncounterGroup(1)

def PalaceofKhoth_488_MapTrigger_7_44(p):
    Town.AlterTerrain(Location(13,45), 0, TerrainRecord.UnderlayList[131])

def PalaceofKhoth_489_MapTrigger_17_45(p):
    Town.AlterTerrain(Location(25,45), 0, TerrainRecord.UnderlayList[131])

def PalaceofKhoth_490_MapTrigger_38_38(p):
    Town.AlterTerrain(Location(38,44), 0, TerrainRecord.UnderlayList[131])

def PalaceofKhoth_491_MapTrigger_59_55(p):
    if StuffDone["20_5"] == 250:
        return
    result = ChoiceBox("Your progress east is suddenly and painfully stopped by an invisible wall. You try to feel your way around it, but it stretches all the way across the hall.\n\nAs you look for a way past, the statue comes to life. It turns towards you and begins to speak. \"I bring you greetings from Khoth the dragon. This is his palace, and he welcomes all who have something to offer him.\"\n\n\"The only thing Khoth values more than knowledge is privacy. Thus, he only wishes to see you if you have some valuable treasure to offer him. In return for, say, passage through this fortress.\"\n\n\"If you have nothing valuable, you will have no choice but to turn back. Do you have a treasure?\"", eDialogPic.TERRAIN, 133, ["No", "Yes"])
    if result == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("\"Fine, then. Then Khoth has no interest in seeing you. You can easily depart to the south, and can return when you have something of value.\" The invisible wall of force remains.")
        return
    elif result == 1:
        if StuffDone["20_5"] == 250:
            return
        StuffDone["20_5"] = 250
        TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(59,55))
        TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(59,53))
        TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(59,57))
        MessageBox("\"Excellent. You may progress. If you have the intelligence and persistence to pass through the maze of shifting floors, you are worthy to see Khoth.\" The wall in front of you disappears, and the statue is still again.")
        return

def PalaceofKhoth_494_MapTrigger_31_58(p):
    if StuffDone["20_6"] == 250:
        return
    StuffDone["20_6"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(31,58))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(32,58))
    ChoiceBox("You step into the awesome entry hall of this huge fortress. If you want to escape the Za-Khazi Run, you have no choice but to find your way through here.\n\nAs you enter, one of the statues turns to you. \"The dragon Khoth welcomes you to his private home, and assures you that, if he feels you are wasting his time, you will pay severely.\"\n\nKhoth! You have heard of this legendary creature, one of the five dragons in Exile when it was first founded. He is renowned for his love of knowledge and his hatred of those who interrupt his solitude.\n\nYou hear a peculiar humming sound. You look around the periphery of the hall, and see that some of the floors are metallic. Stranger still, they are moving! The floors are shifting around, no doubt to confuse and delay progress through this fortress.\n\nThis is your final test. You have little choice but to be up to it.", eDialogPic.TERRAIN, 232, ["OK"])

def PalaceofKhoth_496_MapTrigger_55_32(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(54,55))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def PalaceofKhoth_497_MapTrigger_1_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(14,45))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def PalaceofKhoth_498_MapTrigger_10_31(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(2,44))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def PalaceofKhoth_499_MapTrigger_21_31(p):
    if StuffDone["20_7"] == 250:
        return
    StuffDone["20_7"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(21,31))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(20,32))
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(19,31))
    Town.PlaceEncounterGroup(2)

def PalaceofKhoth_500_MapTrigger_1_43(p):
    if StuffDone["20_8"] == 250:
        return
    StuffDone["20_8"] = 250
    TownMap.List["PalaceofKhoth_20"].DeactivateTrigger(Location(1,43))
    Town.PlaceEncounterGroup(3)

def PalaceofKhoth_503_MapTrigger_53_5(p):
    Town.AlterTerrain(Location(45,4), 0, TerrainRecord.UnderlayList[131])

def PalaceofKhoth_506_CreatureDeath0(p):
    MessageBox("Well, Khoth sure didn\'t expect that. He falls and dies. Another of their arrogant race has been and gone.")

def PalaceofKhoth_507_TalkingTrigger12(p):
    if StuffDone["20_0"] >= 1:
        p.TalkingText = "\"You humans are so foolish. You have already paid me, and, when it suits me, I am a creature of my word. Go to the north gates, and the way will be opened.\""
        return
    if SpecialItem.PartyHas("ScrollofDragons"):
        result = ChoiceBox("Khoth sniffs the air around you and thinks. \"Ah, yes! You have Morog\'s scroll of draconian history. For years now, he has taunted me with it. Give it to me, and passage is yours.\"", eDialogPic.STANDARD, 12, ["Leave", "Give"])
        if result == 1:
            SpecialItem.Take("ScrollofDragons")
            p.TalkingText = "Khoth takes the item. \"Fine, then. It has been a pleasure doing business with you. Go to the north gate, and the way will be open.\"\n\nSuddenly, he casts a brief spell! You feel slightly light headed for a moment. Then the feeling passes. Khoth carries on as if nothing has happened."
            StuffDone["20_0"] = 1
            return
        p.TalkingText = "Khoth shrugs, his huge scales shifting and creaking. \"Fine, then. You can rot here.\""
        return
    if SpecialItem.PartyHas("CrystalofPurity"):
        result = ChoiceBox("Khoth sniffs the air around you and thinks. \"What is that smell?\" He sniffs again.\n\n\"Ah, yes. That is the scent of Vahnatai magic. You have a Crystal of Purity. I have been longing for one of their artifacts for some time. Give it to me, and you can have passage.\"", eDialogPic.STANDARD, 12, ["Leave", "Give"])
        if result == 1:
            SpecialItem.Take("CrystalofPurity")
            p.TalkingText = "Khoth takes the item. \"Fine, then. It has been a pleasure doing business with you. Go to the north gate, and the way will be open.\"\n\nSuddenly, he casts a brief spell! You feel slightly light headed for a moment. Then the feeling passes. Khoth carries on as if nothing has happened."
            StuffDone["20_0"] = 1
            return
        p.TalkingText = "Khoth shrugs, his huge scales shifting and creaking. \"Fine, then. You can rot here.\""
        return
    if SpecialItem.PartyHas("MeloraOpal"):
        result = ChoiceBox("Khoth sniffs the air around you and thinks. \"Hmm. Smelles like gems.\" He sniffs again. \"An opal! A large one! You must have had harsh words with those Empire fools in their opal mine.\"\n\n\"Gemstones are of little interest to me, but they can be traded for books with great ease. I suppose it will do. Give me your opal, and I will let you pass.\"", eDialogPic.STANDARD, 12, ["Leave", "Give"])
        if result == 1:
            SpecialItem.Take("MeloraOpal")
            p.TalkingText = "Khoth takes the item. \"Fine, then. It has been a pleasure doing business with you. Go to the north gate, and the way will be open.\"\n\nSuddenly, he casts a brief spell! You feel slightly light headed for a moment. Then the feeling passes. Khoth carries on as if nothing has happened."
            StuffDone["20_0"] = 1
            return
        p.TalkingText = "Khoth shrugs, his huge scales shifting and creaking. \"Fine, then. You can rot here.\""
        return
