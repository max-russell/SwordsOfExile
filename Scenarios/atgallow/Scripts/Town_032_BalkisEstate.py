
def BalkisEstate_623_MapTrigger_48_50(p):
    result = ChoiceBox("You discover a hidden stairway. Proceed?", eDialogPic.STANDARD, 19, ["Leave", "Onward"])
    if result == 1:
        MessageBox("The stairway leads through a straight, narrow passage. At the end, you find another stairway. You climb up and you find yourself in some sort of wine cellar.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(53,25))
        p.CancelAction = True
        return
    p.CancelAction = True

def BalkisEstate_624_MapTrigger_52_25(p):
    result = ChoiceBox("You discover a hidden stairway. Proceed?", eDialogPic.STANDARD, 19, ["Leave", "Onward"])
    if result == 1:
        MessageBox("The tunnel takes you back into the courtyard.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(48,51))
        p.CancelAction = True
        return
    p.CancelAction = True

def BalkisEstate_625_MapTrigger_32_34(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,33)).Num == 128:
        if SpecialItem.PartyHas("GoldKey"):
            MessageBox("This door has a large magical lock on it. You try the key that you found in the estate. With a satisfying click, the door swings open.")
            t = Town.TerrainAt(Location(32,33))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(32,33)).TransformTo
                Town.AlterTerrain(Location(32,33), 0, t)
            return
        MessageBox("This door has a large lock with a golden glow on it. You try to open the door, but it will not budge at all. You can bet that magical lock is holding it shut. You will need to find the proper key.")
        return

def BalkisEstate_626_MapTrigger_4_25(p):
    if SpecialItem.PartyHas("GoldKey"):
        return
    result = ChoiceBox("This dresser only contains clothing and several personal objects of little value. However, one of the drawers contains a velvet case which contains a key. The key has a slight golden glow to it.\n\nTake the key?", eDialogPic.TERRAIN, 145, ["Leave", "Take"])
    if result == 1:
        SpecialItem.Give("GoldKey")
        Message("  You got a special item!")
        return

def BalkisEstate_627_MapTrigger_32_32(p):
    if StuffDone["10_9"] == 250:
        return
    StuffDone["10_9"] = 250
    TownMap.List["BalkisEstate_32"].DeactivateTrigger(Location(32,32))
    TownMap.List["BalkisEstate_32"].DeactivateTrigger(Location(31,32))
    TownMap.List["BalkisEstate_32"].DeactivateTrigger(Location(33,32))
    Town.PlaceEncounterGroup(1)
    Animation_Explosion(Location(32,29), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Hold(-1, 024_priestspell)
    Wait()
    Animation_Hold(-1, 053_magic3)
    Wait()
    ChoiceBox("As soon as you enter this room, you are assaulted by a blinding flash of light! Recovering from the flash, you see a familiar sight ahead. The wizard Zaine has returned for another strike. This time he has two golems instead of one.\n\nBefore you have a chance to react, he casts a spell. It causes you to shiver and feel cold all over. He laughs maniacally. \"I\'m afraid you don\'t have much longer to live, my friends. I have just inflicted you with a poison that will kill you shortly.\n\nHowever, if you surrender your souls now to the great Morbane, you shall receive salvation.\" He pauses waiting for you to reply. Your head begins to hurt as the poison begins to take effect. You do not reply to Zaine.\n\n\"Ah the poison is setting in I see! Soon you shall feel the more damaging effects. Then death! If you want to reconsider, do so now as you do not have much time.\" He pauses. You step forward to challenge him.\n\n\"Mwa, ha, ha! In your weakened state you are no match for my golems and me! But, if you insist...\"", eDialogPic.CREATURE, 1026, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Zaine_208": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(2)
    StuffDone["11_0"] = 1
    RunScript("ScenarioTimer_x_2814", ScriptParameters(eCallOrigin.CUSTOM))
    RunScript("Loopback_21_0", p)

def BalkisEstate_630_MapTrigger_26_28(p):
    if StuffDone["11_1"] == 1:
        MessageBox("You frantically search the desk for any clue on how to cure the poison. You are in luck, you find the spell to create the poison and a recipe for an antidote! You read:\n\n\"Nazyk\'s Poison (Antidote) - Requires one unit of Quicksilver and one unit of Ember Flowers.\" Now if you can just find those ingredients and some place to mix them in.")
        StuffDone["11_2"] = 1
        return

def BalkisEstate_631_MapTrigger_29_13(p):
    if StuffDone["11_2"] == 1:
        MessageBox("You may use this cauldron to create the \'Antidote\' to Zaine\'s Poison spell. It requires Quicksilver and Ember Flowers.")
        result = ChoiceBox("This cauldron was created for alchemetical purposes. Do you attempt to create the brew?", eDialogPic.STANDARD, 20, ["Yes", "No"])
        if result == 0:
            if Party.CountItemClass(14, False) > 0:
                if Party.CountItemClass(17, True) > 0:
                    if Party.CountItemClass(14, True) > 0:
                        Animation_Hold(-1, 008_bubbles)
                        Wait()
                        StuffDone["11_0"] = 0
                        ChoiceBox("Despite the agony you are in, you proceed to mix the potion as carefully as possible. After following the instructions, the brew is ready to be consumed. You don\'t know if you were successful or not, but time is running out so you try it.\n\nYou drink up and nothing happens at first. Then, slowly the poison begins to recede as the antidote neutralizes it. Looks like you will get to live another day!", eDialogPic.STANDARD, 20, ["OK"])
                        return
                    return
                MessageBox("Alas, you don\'t have the necessary ingredients!")
                return
            MessageBox("Alas, you don\'t have the necessary ingredients!")
            return
        elif result == 1:
            return
        return

def BalkisEstate_632_MapTrigger_51_5(p):
    MessageBox("Your search of the many lab journals leads to a book of recipes. One may be useful. \"Oxidizer - Creates a gaseous substance that is highly corrosive to metal, only potent for a short time. Requires Wither Moss, Potion of Doom.\"\n\nIf you could find the proper ingredients and a place to manufacture it, you could create it.")
    StuffDone["11_3"] = 1

def BalkisEstate_633_MapTrigger_59_9(p):
    MessageBox("After a search through much useless information, you discover the recipe to Potion of Doom. \"Causes extreme damage to user, excellent trap and useful in alchemy. Requires Wither Moss, Naga Blood.\"\n\nIf you could find the proper ingredients and a place to manufacture it, you could create it.")
    StuffDone["11_4"] = 1

def BalkisEstate_634_MapTrigger_29_16(p):
    if StuffDone["11_3"] == 1:
        MessageBox("You may use this cauldron to create the \'Oxidizer\'. It requires \'Wither Moss\', and a \'Potion of Doom\'.")
        result = ChoiceBox("This cauldron was created for alchemetical purposes. Do you attempt to create the brew?", eDialogPic.STANDARD, 20, ["Yes", "No"])
        if result == 0:
            if Party.CountItemClass(9, False) > 0:
                if Party.CountItemClass(16, True) > 0:
                    if Party.CountItemClass(9, True) > 0:
                        Animation_Hold(-1, 008_bubbles)
                        Wait()
                        MessageBox("You mix the ingredients together the way the recipe tells you. After a short wait, the liquid begins to boil and create a corrosive gas. Careful not to have it contact your equipment, you bottle it. The Oxidizer won\'t last long.")
                        SpecialItem.Give("Oxidizer")
                        Timer(Town, 50, False, "BalkisEstate_647_TownTimer_48", eTimerType.DELETE)
                        return
                    return
                MessageBox("Alas, you don\'t have the necessary ingredients!")
                return
            MessageBox("Alas, you don\'t have the necessary ingredients!")
            return
        elif result == 1:
            return
        return

def BalkisEstate_635_MapTrigger_27_13(p):
    if StuffDone["11_4"] == 1:
        MessageBox("You may use this cauldron to create the \'Potion of Doom\'. It requires Wither Moss, Naga Blood.")
        result = ChoiceBox("This cauldron was created for alchemetical purposes. Do you attempt to create the brew?", eDialogPic.STANDARD, 20, ["Yes", "No"])
        if result == 0:
            if Party.CountItemClass(9, False) > 0:
                if Party.CountItemClass(10, True) > 0:
                    if Party.CountItemClass(9, True) > 0:
                        Party.GiveNewItem("PotionofDoom_270")
                        Animation_Hold(-1, 008_bubbles)
                        Wait()
                        return
                    return
                MessageBox("Alas, you don\'t have the necessary ingredients!")
                return
            MessageBox("Alas, you don\'t have the necessary ingredients!")
            return
        elif result == 1:
            return
        return

def BalkisEstate_636_MapTrigger_13_8(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(12,8)).Num == 130:
        if SpecialItem.PartyHas("Oxidizer"):
            SpecialItem.Take("Oxidizer")
            if StuffDone["11_7"] < 1:
                MessageBox("You use the \'Oxidizer\' on this portcullis. The mixture quickly eats away at the metal, reducing it to rust. Unfortunately, you did not have enough to fully eat away at the bars. Perhaps another brew will be needed...")
                StuffDone["11_7"] += 1
                if StuffDone["11_7"] == 250:
                    TownMap.List["BalkisEstate_32"].DeactivateTrigger(Location(55,25))
                return
            MessageBox("The \'Oxidizer\' continues to eat away at the metallic bars. By the time the reaction is over, the metals are reduced to rust. You easily knock them over.")
            SuspendMapUpdate()
            for x in range(12, 13):
                for y in range(8, 10):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        return

def BalkisEstate_638_MapTrigger_13_10(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull on the lever, but nothing happens. You suspect that this mechanism is broken.")
        return

def BalkisEstate_639_MapTrigger_25_30(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear the sound of metal rubbing against stone to the south.")
        SuspendMapUpdate()
        for x in range(31, 34):
            for y in range(44, 45):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def BalkisEstate_640_MapTrigger_14_25(p):
    MessageBox("The search of medical tomes reveals the most remedial knowledge. However, an interesting recipe: \"Brew of Coercion - Makes the user susceptible to coercion. Requires Naga Blood, Vampyre Fang.\"\n\nIf you could find the proper ingredients and a place to manufacture it, you could create it.")
    StuffDone["11_5"] = 1

def BalkisEstate_641_MapTrigger_27_16(p):
    if StuffDone["11_5"] == 1:
        MessageBox("You may use this cauldron to create the \'Brew of Coercion\'. It requires a Vampyre Fang, a vial of Naga Blood.")
        result = ChoiceBox("This cauldron was created for alchemetical purposes. Do you attempt to create the brew?", eDialogPic.STANDARD, 20, ["Yes", "No"])
        if result == 0:
            if Party.CountItemClass(8, False) > 0:
                if Party.CountItemClass(10, True) > 0:
                    if Party.CountItemClass(8, True) > 0:
                        SpecialItem.Give("BrewofCoercion")
                        Animation_Hold(-1, 008_bubbles)
                        Wait()
                        return
                    return
                MessageBox("Alas, you don\'t have the necessary ingredients!")
                return
            MessageBox("Alas, you don\'t have the necessary ingredients!")
            return
        elif result == 1:
            return
        return

def BalkisEstate_642_MapTrigger_5_14(p):
    MessageBox("Tucked away among these specimen reports, is a note. \"We have developed a new way of encoding text! The only way for one to read it is to drink a special \'True Vision Potion\'. It requires Quicksilver, and a Unicorn Horn to produce.\"\n\nIf you could find the proper ingredients and a place to manufacture it, you could create it.")
    StuffDone["11_6"] = 1

def BalkisEstate_643_MapTrigger_25_13(p):
    if StuffDone["11_6"] == 1:
        MessageBox("You may use this cauldron to create the \'True Vision Potion\'. It requires Quicksilver and a Unicorn Horn.")
        result = ChoiceBox("This cauldron was created for alchemetical purposes. Do you attempt to create the brew?", eDialogPic.STANDARD, 20, ["Yes", "No"])
        if result == 0:
            if Party.CountItemClass(14, False) > 0:
                if Party.CountItemClass(15, True) > 0:
                    if Party.CountItemClass(14, True) > 0:
                        MessageBox("You prepare the \'True Vision Potion\'. It looks clear and syrupy. You all take a nice drink. It is surprisingly sweet and has a peppermint taste. Other than that, you notice nothing different.")
                        StuffDone["11_8"] = 1
                        return
                    return
                MessageBox("Alas, you don\'t have the necessary ingredients!")
                return
            MessageBox("Alas, you don\'t have the necessary ingredients!")
            return
        elif result == 1:
            return
        return

def BalkisEstate_644_MapTrigger_8_11(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(8,11)).Num == 122:
        if StuffDone["11_9"] == 1:
            MessageBox("You search the wall as the Ogre said. You discover a few small buttons disguised as stones in the wall. You press them all simultaneously and a secret passage opens!")
            Town.AlterTerrain(Location(8,11), 0, TerrainRecord.UnderlayList[124])
            return
        return

def BalkisEstate_645_MapTrigger_36_20(p):
    result = ChoiceBox("This is Balkis\'s journal. You can bet any information on the Nethergate will be located in this book. The Empire would love to get its hands on this.", eDialogPic.STANDARD, 24, ["Leave", "Read", "Take"])
    if result == 1:
        if StuffDone["11_8"] == 1:
            StuffDone["12_0"] = 1
            ChoiceBox("Indeed, this tome contains everything you would ever want to know about the Nethergate. It describes its construction, use, and even a way to deactivate it. You read and memorize the important parts.\n\n\"The Nethergate is a special kind of portal that allows the direct pulling of creatures out of the void. The benefits are great. Large numbers of powerful creatures may be summoned with little energy expenditure.\n\nOnce this army of massive beings are assembled, the Empire will be no match for us. We shall easily take the throne and perpetuate the reign of the great Morbane.\" Again, that name is mentioned. You wonder about that...\n\n\"Once created, this device will be difficult to destroy. The Nethergate is really a tear in spacetime which can only be repaired by massive amounts of energy or an artifact called an Onyx Scepter.\n\nFortunately, such artifacts are not found easily...\" The journal continues with technical information. You are sure this information will be useful to the Empire. Mission accomplished!", eDialogPic.STANDARD, 22, ["OK"])
            return
        MessageBox("You page through the book, but strange magic distorts the writing beyond comprehension. You are starting to get a headache by trying to make out the random scribbles. You give up.")
        return
    elif result == 2:
        MessageBox("Balkis wisely decided to place measures against taking this book. You try to lift it off the pedestal, but a powerful force holds it on. You yank harder and electricity flows through your bodies. Yikes that hurt!")
        Party.Damage(Maths.Rand(4, 1, 10) + 10, eDamageType.MAGIC)
        Wait()
        return

def BalkisEstate_646_MapTrigger_55_25(p):
    if StuffDone["11_7"] >= 2:
        SuspendMapUpdate()
        for x in range(12, 13):
            for y in range(8, 10):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetUnlocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def BalkisEstate_647_TownTimer_48(p):
    SpecialItem.Take("Oxidizer")

def BalkisEstate_648_CreatureDeath13(p):
    ChoiceBox("Zaine lets out a blood curdling scream. He falls to the ground and looks up at you with utter hatred. He shakes his head and laughs. \"How ironic, that after killing me, you will only receive death -- but in a much more horrid way.\n\nNo matter, Morbane\'s reign of terror will go on without me. I can rest knowing that I have taken vengeance against you.\" With a twisted smile on his face, he dies.\n\nYou take no victory in Zaine\'s defeat. After all, you are doomed to die as well. That is unless you can find a way to counteract the poison. You don\'t know exactly how long you have to live, but you know the pain continues to get worse and worse.\n\nIf you\'re going to survive, you had better hurry!", eDialogPic.CREATURE, 1026, ["OK"])

def BalkisEstate_649_TalkingTrigger2(p):
    if SpecialItem.PartyHas("BrewofCoercion"):
        ChoiceBox("You remember that you have something called the \'Brew of Coercion\'. You decide that this would be an excellent time to use it. You quickly move in and hold the ogre down and force the potion down his throat. Messy, but effective.\n\nYou ask him for any useful information. You can visibly see the mental struggle inside not to give in to puny humans like yourself. But, he is unable to resist the effects of the brew.\n\n\"I know the two main wizards do strange experiments here. They\'ve been talking about something called the Nethergate, but I don\'t know much about it. If it helps, they have a secret room.\n\nYou have to search the southern wall very carefully to find it. I don\'t know anything more. Really, I don\'t!\"", eDialogPic.CREATURE, 44, ["OK"])
        p.TalkingText = "The effects of the potion quickly wear off."
        StuffDone["11_9"] = 1
        return

def Loopback_21_0(p):
    Town.PlaceEncounterGroup(2)
    StuffDone["11_0"] = 1
    RunScript("ScenarioTimer_x_2814", ScriptParameters(eCallOrigin.CUSTOM))
    RunScript("Loopback_21_0", p)
