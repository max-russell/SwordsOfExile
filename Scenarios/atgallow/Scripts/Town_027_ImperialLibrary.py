
def ImperialLibrary_487_MapTrigger_32_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,58)
    Party.MoveToMap(TownMap.List["Solaria_25"])

def ImperialLibrary_490_MapTrigger_59_32(p):
    if StuffDone["9_0"] >= 2:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
            MessageBox("You sit down and attempt to open the book. Just as your hand approaches the tome, it flies open to the page with \'Dispel Barrier\'! You try to turn the page but are unable to do so.\n\nYou study the intricate spell for a while. Eventually, you manage to learn how to bring down a magical barrier. You can now cast \'Dispel Barrier\'!")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_dispel_barrier")
            return
        MessageBox("You sit down and attempt to open the book. Just as your hand approaches the tome, it flies open to the page with \'Dispel Barrier\'! You try to turn the page but are unable to do so.\n\nYou attempt to study the spell. However, you soon figure out that this one is a bit too difficult for your level of skill. You will require more \'Mage Lore\' to learn this.")
        return
    MessageBox("You attempt to read this book, but powerful magics hold it shut. You wonder what awesome magical secrets this tome contains. However, you may never find out.")

def ImperialLibrary_491_MapTrigger_58_61(p):
    MessageBox("This book reads, \"Encyclopedia of Artifacts -- L-O\" What artifact do you want to know about?")
    response = InputTextBox("Enter something:", "")
    response = response[0:4].upper()
    if response == "ONYX":
        MessageBox("ONYX SCEPTER -- A mysterious onyx staff of about a meter long. It is said to be able to heal tears in space, but is unconfirmed. One was found in Avernum; current location unknown. The other is held by the Order of Urlak-Nai.")
        if StuffDone["12_2"] == 0:
            StuffDone["12_2"] = 1
            return
        return
    elif response == "MOON":
        MessageBox("MOONSTONE -- A spherical stone that glows like the moon. In reality, it is merely a burned out sunstone (see sunstone). Moonstones can be reconverted into sunstones by prolonged exposure to concentrated sunlight. Locations are unknown.")
        return

def ImperialLibrary_492_MapTrigger_60_61(p):
    MessageBox("The book reads, \"Encyclopedia of artifacts -- P-T\" What artifact do you want to know about?")
    response = InputTextBox("Enter something:", "")
    response = response[0:4].upper()
    if response == "SUNS":
        MessageBox("SUNSTONE -- A magical sphere that can be used to contain sunlight. Such objects are extremely rare, but can be produced from a Moonstone (See Moonstone).")
        StuffDone["27_1"] = 1
        return
    elif response == "THRA":
        MessageBox("SPHERE OF THRALNI -- Discovered by an adventurer named Thralni circa 730 IE. The orb, once rubbed, will allow its users to engage in flight for a short amount of time. The sphere was lost during the First Expedition of Avernum in 743 IE.\n\nIt was later recovered and used by Avernum in the Avernum War. In 913 IE, the orb was returned to the rulers of Stolgrad, who sponsored Thralni\'s exploits in Avernum.")
        return

def ImperialLibrary_493_MapTrigger_37_18(p):
    ChoiceBox("The Imperial Library is huge consisting of several floors above and below the ground level. It would take weeks to look through all of the shelves. Perhaps it is best you skip the other levels.", eDialogPic.TERRAIN, 135, ["OK"])
    p.CancelAction = True

def ImperialLibrary_497_MapTrigger_54_61(p):
    MessageBox("This book reads, \"Encyclopedia of Artifacts -- A-D\" What artifact do you want to know about?")
    response = InputTextBox("Enter something:", "")
    response = response[0:4].upper()
    if response == "ATHE":
        MessageBox("ATHEME, BLESSED -- A knife that is said to be gift directly from the gods. Supposedly they can slice through any material. The blade was often used to sever magical seals or daemonic materials.\n\nThe Blessed Atheme was last documented in the ninth century. It was carried by a band of heroic adventurers from Avernum who were last scene leaving for an expedition of the Mandahl Mountains.")
        return

def ImperialLibrary_498_MapTrigger_56_61(p):
    MessageBox("This book reads, \"Encyclopedia of Artifacts -- E-K\" What artifact do you want to know about?")
    response = InputTextBox("Enter something:", "")
    response = response[0:0].upper()

def ImperialLibrary_499_MapTrigger_62_61(p):
    MessageBox("This book reads, \"Encyclopedia of Artifacts -- U-Z\" What artifact do you want to know about?")
    response = InputTextBox("Enter something:", "")
    response = response[0:0].upper()

def ImperialLibrary_500_TalkingTrigger8(p):
    if StuffDone["7_1"] >= 2:
        return
    if StuffDone["7_1"] < 1:
        p.TalkingText = "He sighs in disgust. \"A few weeks ago, some ancient tomes on demonology were uncovered in Nelon. I was charged with bringing them here for duplication. I lost them on the way here!\"\n\nHe scowls. \"All I remember some fog as I was nearing Andromeda. Then all goes blank and I was here without the records! Damn myself!\""
        return
    p.TalkingText = "He rants about some tomes on demonology. You show him the ones you have recovered and his eyes light up with joy. \"That\'s them!\" He grabs them from your hands. \"I am very grateful for your deeds.\"\n\nHe thinks. \"I don\'t have much to offer you. However, I think I can give you some reward that may or may not interest you.\""
    StuffDone["7_1"] = 2
    SpecialItem.Take("MithralMaiden")
    StuffDone["0_1"] += 1
    if StuffDone["0_1"] == 250:
        TownMap.List["FortLemmix_1"].DeactivateTrigger(Location(17,13))

def ImperialLibrary_501_TalkingTrigger9(p):
    if StuffDone["7_1"] == 2:
        p.TalkingText = "\"It\'s not much but I cannot think of anything else. In the bestiary, are hidden some ancient records from the Avernum war of centuries past. There are two reading crystals containing spells!\n\nThey were created by a race called the Vahnatai. Sadly, the information has decayed. However, a spell or two may be left intact.\""
        return

def ImperialLibrary_502_TalkingTrigger39(p):
    if Party.CountItemClass(36, True) > 0:
        Party.GiveNewItem("StrongHealingP_247")
        p.TalkingText = "You hand her one of the books. She cackles loudly and produces a potion. \"Here you go! You should find this very tasty.\" She cackles once more."
        StuffDone["41_3"] += 1
        if StuffDone["41_3"] == 250:
            pass
        return
    if Party.CountItemClass(37, True) > 0:
        Party.GiveNewItem("StrongEnergyP_248")
        p.TalkingText = "You hand her one of the books. She cackles loudly and produces a potion. \"Here you go! You should find this very tasty.\" She cackles once more."
        StuffDone["41_3"] += 1
        if StuffDone["41_3"] == 250:
            pass
        return
    if Party.CountItemClass(38, True) > 0:
        Party.GiveNewItem("StrongInvulnP_251")
        p.TalkingText = "You hand her one of the books. She cackles loudly and produces a potion. \"Here you go! You should find this very tasty.\" She cackles once more."
        StuffDone["41_3"] += 1
        if StuffDone["41_3"] == 250:
            pass
        return
    if StuffDone["41_3"] >= 3:
        p.TalkingText = "\"Thanks for all the books. They are proving most useful. I\'m an expert alchemist! If you need a favor such as deciphering some ancient tome, I\'d be glad to oblige!\" She cackles loudly."
        return

def ImperialLibrary_503_TalkingTrigger44(p):
    if StuffDone["41_4"] == 0:
        if Party.Gold >= 2000:
            Party.Gold -= 2000
            Sound.Play(062_mmm)
            for pc in Party.EachAlivePC():
                pc.SetSkill(eSkill.POLE_WEAPONS, pc.GetSkill(eSkill.POLE_WEAPONS) + 4)
            ChoiceBox("You pay him the gold. \"I guess we have a deal then. Come, I shall meet you at the west gate of Solaria. I don\'t think the scholars would appreciate it much if we were to do this here.\"\n\nYou follow him outside where you receive intensive training in the arts of wielding a spear. You are shown the proper ways to thrust, the handling, how to prevent it from being blocked, and all sorts of other tricks.\n\nYou train for about ten hours of instruction. In that time you learn much in the ways of pole weapons. You could have not asked for a better instructor, for when you are finished, you feel confident in using the pole weapons.\n\nYou return to the library where Sss-Natassh takes his original seat, quite tired. \"I\'ve shown you all the tricks and stuff. The key is practice! Only then can you become an expert at wielding a pole.\"", eDialogPic.CREATURE, 50, ["OK"])
            StuffDone["41_4"] = 1
            return
        p.TalkingText = "You cannot afford it."
        return
    p.TalkingText = "\"I have already taught you all that I know about pole weapons.\""

def ImperialLibrary_504_TalkingTrigger47(p):
    if Party.CountItemClass(54, False) > 0:
        ChoiceBox("You present an ancient book of lost alchemy to her. She grabs it from your hand greedily and pages through it with glee. \"Most of these here spells are advanced, but pretty impractical.\"\n\nThen her eyes widen as she reaches a certain section. \"My, my, you sure have found something interesting. Within this book is...\" her voice becomes a whisper, \"...the recipe for the strong skill potion.\"\n\nShe quietly explains from the book exactly how to produce the skill potion, you take several notes for the procedure is extremely complex. You will need to acquire: Ambrosia, Mandrake Root, Dragon Scales, and a Gold Unicorn Horn.\n\nAll of the other reagents are fairly common for most alchemy workstations which you shall require to produce this potion.\n\nYou now know how to manufacture Strong Skill Potions!", eDialogPic.STANDARD, 20, ["OK"])
        StuffDone["120_2"] = 1
        return
