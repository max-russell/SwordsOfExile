
def ForgottenAcademy_1476_MapTrigger_20_52(p):
    MessageBox("You were right about you not being able to make it to the controls. Despite your best efforts, you are eventually overcome by the caustic fumes.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
    p.CancelAction = True

def ForgottenAcademy_1480_MapTrigger_31_38(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["21_6"] == 250:
        return
    StuffDone["21_6"] = 250
    ChoiceBox("As soon as you open this door, you are assaulted by a surge of immense heat! A thick sulfurous smog hangs heavy in the air. It is strong enough to make you gag. After you recover you take a look.\n\nThe donut shaped lava container has ruptured spilling molten rock across the room. To make matters worse, several large fiery giants emerge from the lava. One of them speaks in a booming growl-like voice.\n\n\"At last, it is some human flesh! We can finally take vengeance for the centuries that we have been imprisoned in that horrible donut. We shall torture them, just as they have tortured us! Come my brothers!\"\n\nYou turn to see Astervis casting a spell. With a loud chant, encouraging waves of energy move through you. \"Hope this helps! Move fast, for the invulnerability won\'t last too long!\" You are now ready for battle!", eDialogPic.CREATURE1x2, 6, ["OK"])
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) + 8))
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) + 8))
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.INVULNERABLE, Maths.MinMax(0, 8, pc.Status(eAffliction.INVULNERABLE) + 3))

def ForgottenAcademy_1481_MapTrigger_44_10(p):
    if StuffDone["20_4"] == 250:
        return
    StuffDone["20_4"] = 250
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(44,10))
    TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(44,10))
    MessageBox("You were wondering why a chair would be sitting in the middle of a circle of runes. You reach out to touch the chair and your hand passes right through it! The chair is only a holographic image and a very realistic one at that.")

def ForgottenAcademy_1483_MapTrigger_52_47(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["21_7"] == 250:
        return
    StuffDone["21_7"] = 250
    ChoiceBox("You enter this room finding all the furniture removed. If that wasn\'t enough, it had to be replaced by a horde of giant worms! The all turn and move toward you in unison, seemingly to sense your presence.\n\nYou would have rather preferred the tables and chairs...\n\nYou notice Astervis preparing a spell. He fires a searing javelin of flame, that impacts and engulfs the worm in a large conflagration! Astervis continues to concentrate and chant.\n\nThree of the giant worms begin to expand and shriek in pain. The expansion continues and their skin begins to tear. A greenish ooze seeps out of the wounds. They continue to expand.\n\nOne after the other, the three targeted worms explode into massive bulges of slime! Immediately afterward, Astervis crumbles to the ground. His face is covered in sweat as he says.\n\n\"I\'m sorry, but I\'m not a fighting mage remember. I really can\'t help you anymore right now.\" Well, at least he got rid of four of them. There are still six more to go!", eDialogPic.CREATURE2x2, 1, ["OK"])
    Town.PlaceEncounterGroup(2)

def ForgottenAcademy_1485_MapTrigger_56_33(p):
    if StuffDone["17_3"] == 20:
        StuffDone["17_3"] = 21
        ChoiceBox("Returning to Palver\'s cell, you find (or better to say do not find) what you half-expected. Palver is gone.\n\nAstervis, now somewhat recovered, asks \"So this is where Palver was?\" You nod accordingly. \"Too bad. He was probably taken away while you were away. I would have really liked to have spoken with him. Oh well.\"\n\nAstervis thinks for a bit. \"Wait a minute, I have a hunch. I think I detected something unusual back in the room with the shattered heat torus. I didn\'t have time to thoroughly examine it and kind of forgot about it in the heat of battle.\n\nNo pun intended. It\'s just a hunch, but I feel it merits another look. Let\'s hope that I\'m not wrong about this, okay.\"", eDialogPic.CREATURE, 26, ["OK"])
        return

def ForgottenAcademy_1486_MapTrigger_38_47(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["17_3"] == 21:
        StuffDone["17_3"] = 22
        ChoiceBox("You return to the room of the shattered torus. Astervis looks around and points at the ceiling above the circle of runes. \"Look, the ceiling over there!\" You really don\'t notice anything unusual about it.\n\n\"To the untrained eye, it appears to simply be a normal and ordinary ceiling. However, under the scrutiny of an expert on barriers, like myself, one can make out the telltale signs of an illusion.\n\nYou see how that area just appears a bit too smooth to be part of the normal ceiling. Notice the very small glint-like sparkles. The circle of runes gives it away. I\'m willing to bet a my newest magical textbook that there is something above that barrier!\n\nYou coax Astervis on. \"I\'ll show you! Watch the master at work.\" Astervis quickly scampers over the lava and stands underneath the barrier. He begins to chant and direct energy at the ceiling.\n\nAfter a few minutes, the panel begins to flash a brilliant white and disintegrates much as any other magic barrier would. \"Ha! Told you so. Now if we only had some rope so that we could all get up there...\"\n\n(When you have some rope, stand in the center of the circle of runes)", eDialogPic.TERRAIN, 231, ["OK"])
        return

def ForgottenAcademy_1488_MapTrigger_29_51(p):
    if StuffDone["17_3"] >= 22:
        if SpecialItem.PartyHas("AstervisNPC"):
            if Party.CountItemClass(24, False) > 0:
                MessageBox("You give Astervis the rope and he levitates it, making a steady vertical strand to climb on. Astervis goes up first and you follow.")
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(4,12))
                p.CancelAction = True
                if StuffDone["17_3"] >= 23:
                    for x in range(4, 6):
                        for y in range(9, 10):
                            if Maths.Rand(1,0,100) <= 100:
                                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
                    return
                return
            return
        return

def ForgottenAcademy_1489_MapTrigger_4_13(p):
    if StuffDone["17_3"] == 24:
        return
    if Party.CountItemClass(24, False) > 0:
        MessageBox("Astervis resuspends the rope and you all climb back down.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(29,51))
        p.CancelAction = True
        return

def ForgottenAcademy_1491_MapTrigger_23_53(p):
    if StuffDone["20_9"] == 250:
        return
    StuffDone["20_9"] = 250
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(23,53))
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(23,54))
    TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(23,53))
    TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(23,54))
    Animation_Hold(-1, 058_opendoor)
    Wait()
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 8))
    Animation_Hold(-1, 059_closedoor)
    Wait()
    MessageBox("Yuck! As soon as you open the door, you are assaulted by extremely caustic fumes! You try to proceed, but the fumes make you so feel unbearably nauseous that you have to close the door.\n\nOn the other side is a control room. However, the back wall has been eaten away by corrosive, toxic sludge -- probably waste products that have leaked over the centuries. You doubt you could reach the controls alive.")
    p.CancelAction = True

def ForgottenAcademy_1494_MapTrigger_4_10(p):
    if StuffDone["17_3"] == 22:
        ChoiceBox("You confront another barrier. This one is of the large red variety. Astervis spends several minutes scrying the barrier. \"Well, whoever put this up was pretty talented. Not to say the previous one was not good.\n\nBut this one has a lot more strength to it. The person behind these barriers must have been an expert. Something, that Odix would definitely be capable of, I\'m afraid to admit.\n\nAnyway, here\'s the scoop. I\'m going to need some gemstone to conquer this one. A ruby will be the best bet. I\'ll need it to better focus and expand upon my energies.\n\nHopefully, the reagent will amplify it to the point of creating resonance within the barrier, thus shattering it. Now, a ruby, if you will.\"", eDialogPic.TERRAIN, 231, ["OK"])
        if Party.CountItemClass(3, True) > 0:
            ChoiceBox("You hand the ruby to Astervis. He begins to chant and focus his energies through the gemstone. After several minutes, he completes his chanting! He turns to you.\n\n\"Now we\'re going to find out if this worked.\" Astervis holds the ruby up to the barrier. You watch the barrier undulate and become very unstable. Then suddenly, the barrier and the ruby shatter! Astervis smiles victoriously.\n\nYou decide to take a look inside. It does not take long to see the gruesome site of Palver\'s battered body sprawled out on the floor. Astervis shakes his head. \"And so they punished him with a vengeance. Not a way to go.\"\n\nAfter a brief pause, he continues, \"Well, it looks like there are a lot of records here. Perhaps some of them may contain some information on the disappearances or possibly some evidence.\"", eDialogPic.TERRAIN, 231, ["OK"])
            StuffDone["17_3"] = 23
            for x in range(4, 6):
                for y in range(9, 10):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
            return
        return

def ForgottenAcademy_1496_MapTrigger_3_4(p):
    if StuffDone["17_3"] == 23:
        StuffDone["17_3"] = 24
        ChoiceBox("This desk contains a treasure trove of information. Present is a mass of memos and letters between Odix and members of the order of Watchpoint on the disappearances. You look over at Palver\'s body. It looks like he has been vindicated.\n\nAstervis seems visibly disturbed. \"I would have never believed it. My own mentor, the person who I had admired my entire life, a traitor. He fooled me, he fooled you, he fooled everyone.\n\nWe have no choice. We must proceed to Watchpoint Tower and stop them once and for all.\"\n\n\"I\'m afraid I cannot allow you to do that, my apprentice,\" rings out the voice of Odix who is now standing in the antechamber. \"I sure fooled everyone didn\'t I! Ha! But all is not lost so long as the word does not get out.\n\nIt\'s a pity that I will have to destroy all of you in the process. You fought and searched quite valiantly. I am indeed impressed. You overcame roadblock after roadblock. I never thought you would make it this far.\"\n\n\"Master please stop, I implore you!\" shouts Astervis. \"I am sorry, but this is bigger than all of us combined.\"", eDialogPic.CREATURE, 27, ["OK"])
        Town.PlaceEncounterGroup(1)
        Timer(Town, 5, False, "ForgottenAcademy_1505_TownTimer_36", eTimerType.DELETE)
        Timer(Town, 7, False, "ForgottenAcademy_1507_TownTimer_60", eTimerType.DELETE)
        return

def ForgottenAcademy_1497_MapTrigger_9_11(p):
    StuffDone["17_3"] = 25
    ChoiceBox("Odix crumbles to the ground, mortally wounded. Astervis rushes to his mentor\'s side. \"Why master? Why did you do such horrible things?\"\n\nOdix sighs. \"I am truly sorry for what I have done. The mages of Watchpoint, they offered me something I could not resist. You see, before I took you as my apprentice, I was married to a lovely woman.\n\nMy two loves of my life were my research and her. Unfortunately, every time I thought I could spend time with her I was given a lucrative offers -- research expeditions, professorships, promotions, you name it.\n\nBefore I knew it, years went by and she grew very ill. I was in Valorim when she passed away. I could never forgive myself. For over a year I lived in depression, but then I decided to get a new purpose in life.\n\nThat is why I took you as my apprentice, so I could forget about the past.  They promised to use their ancient magics to bring her back. I just could not resist.\" A long silence hangs in the air. Astervis is about to speak, but Odix stops him.\n\n\"Please, no farewells. Just follow my one last request. Go to Watchpoint Tower and stop those magi. Please redeem the lives of all that we have taken.\" Odix closes his eyes and dies.", eDialogPic.CREATURE, 27, ["OK"])
    ChoiceBox("After a few minutes of reflection, Astervis rises and turns to you. He says in a low tone, \"Come on. We\'ve got work to do.\"\n\nYou all begin to leave but Astervis interrupts, \"First we should return to the house. There are a couple of spell books with a few spells that you may wish to know. Let\'s get going!\"", eDialogPic.CREATURE, 27, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "GolemX_237": Town.NPCList.Remove(npc)

def ForgottenAcademy_1498_MapTrigger_49_41(p):
    MessageBox("There used to be a stairway leading back down to the lower level. However, time has caused this corridor to cave in, blocking off whatever lies below. You will not be able to proceed further this way.")
    p.CancelAction = True

def ForgottenAcademy_1500_MapTrigger_39_41(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(56,4)
    Party.MoveToMap(TownMap.List["AncientRuins_40"])

def ForgottenAcademy_1503_MapTrigger_11_40(p):
    if StuffDone["21_0"] == 2:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("A strange forcefield seems to be holding you back. For some reason, the designers of this academy have wanted to make sure that no one unauthorized person entered the waste area.")

def ForgottenAcademy_1505_TownTimer_36(p):
    if StuffDone["21_8"] == 0:
        if Maths.Rand(1,0,100) < 50:
            if Maths.Rand(1,0,100) < 50:
                Message("Odix casts:")
                Message("  Poison Cloud")
                Animation_Hold(-1, 025_magespell)
                Wait()
                for pc in Party.EachAlivePC():
                    pc.Poison(8)
                Timer(Town, 5, False, "ForgottenAcademy_1505_TownTimer_36", eTimerType.DELETE)
                return
            Message("Odix casts:")
            Message("  Lightning Sheet")
            Animation_Hold(-1, 025_magespell)
            Wait()
            Party.Damage(Maths.Rand(10, 1, 10) + 10, eDamageType.MAGIC)
            Wait()
            Timer(Town, 5, False, "ForgottenAcademy_1505_TownTimer_36", eTimerType.DELETE)
            return
        if Maths.Rand(1,0,100) < 50:
            Message("Odix casts:")
            Message("  Excommunicate")
            Animation_Hold(-1, 024_priestspell)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 8))
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 8))
            Timer(Town, 5, False, "ForgottenAcademy_1505_TownTimer_36", eTimerType.DELETE)
            return
        Timer(Town, 5, False, "ForgottenAcademy_1505_TownTimer_36", eTimerType.DELETE)
        return

def ForgottenAcademy_1507_TownTimer_60(p):
    if StuffDone["21_8"] == 0:
        if Maths.Rand(1,0,100) < 50:
            if Maths.Rand(1,0,100) < 50:
                Message("Astervis casts:")
                Message("  Major Blessing")
                Animation_Hold(-1, 004_bless)
                Wait()
                for pc in Party.EachAlivePC():
                    pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) + 8))
                for pc in Party.EachAlivePC():
                    pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) + 8))
                Timer(Town, 7, False, "ForgottenAcademy_1507_TownTimer_60", eTimerType.DELETE)
                return
            Message("Astervis casts:")
            Message("  Aura of Protection")
            Animation_Hold(-1, 075_cold)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.INVULNERABLE, Maths.MinMax(0, 8, pc.Status(eAffliction.INVULNERABLE) + 3))
            Timer(Town, 7, False, "ForgottenAcademy_1507_TownTimer_60", eTimerType.DELETE)
            return
        if Maths.Rand(1,0,100) < 50:
            Message("Astervis casts:")
            Message("  Revitalization")
            Animation_Hold(-1, 051_magic1)
            Wait()
            Party.HealAll(100)
            Timer(Town, 7, False, "ForgottenAcademy_1507_TownTimer_60", eTimerType.DELETE)
            return
        Timer(Town, 7, False, "ForgottenAcademy_1507_TownTimer_60", eTimerType.DELETE)
        return

def ForgottenAcademy_1508_OnEntry(p):
    if StuffDone["21_5"] == 250:
        return
    StuffDone["21_5"] = 250
    ChoiceBox("You return to the academy with Astervis. This time the waiting room is in utter disarray!\n\nAstervis shouts, \"Watch out!\" You turn to see an incoming fireball. You quickly dodge it none to soon. You look to see its source, a fierce Wyvern. Apparently a few have decided to sneak in while you were gone.\n\nNow you get a true taste of Astervis\'s power. He raises his arms and chants, his hands begin to glow a brilliant blue. He slaps them together and a powerful bolt of electricity is released at the Wyvern.\n\nThe reptile screams out in pain as the bolt pierces its body. It falls to the ground, lifeless. Astervis turns to you, \"That was a close one friends. We\'ll have to be on the lookout for more nasties.\"\n\nAfter a brief pause he speaks, \"Since I\'m more of a researching mage than a fighting one, I\'ll stay in back and let you handle most of the hacking. If you need help, please ask!\"\n\nSuddenly there is a growl. \"Uh oh! It looks like we\'ve got company!\"", eDialogPic.CREATURE, 144, ["OK"])
