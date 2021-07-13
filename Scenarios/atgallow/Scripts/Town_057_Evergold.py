
def Evergold_1367_MapTrigger_7_31(p):
    if StuffDone["49_3"] == 250:
        return
    StuffDone["49_3"] = 250
    TownMap.List["Evergold_57"].DeactivateTrigger(Location(7,31))
    TownMap.List["Evergold_57"].DeactivateTrigger(Location(7,32))
    TownMap.List["Evergold_57"].DeactivateTrigger(Location(7,33))
    ChoiceBox("You have arrived at the city of Evergold, capital of the Nelon Sector and of industry. Tens of thousands of residents from the suburbs from outside the city commute each day into these walls to work in the various factories here.\n\nThere are three major factory types in the city. The first produces metalworks of a variety of items. Most of the Empire\'s weapons (at least on Pralgad) are constructed in those factories.\n\nAlso, the creation of potions has been made into a science in another factory. Herbs are grown in greenhouses and harvested. They are then processed and made into a variety of potions in an assembly line fashion.\n\nThe third and most recently constructed factory has been the one that manufactures Golems. New technologies have allowed for automated methods of their construction and indeed Golems are popping up everywhere as guards.\n\nEvergold also has its own seaport run by the Imperial Navy. The import of raw materials and the export of finished products occurs day and night. This is quite the system here.", eDialogPic.TERRAIN, 189, ["OK"])

def Evergold_1370_MapTrigger_27_43(p):
    if StuffDone["49_4"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange forcefield holds you back. The attendant at the desk grins. \"Looks like someone forgot to sign in!\"")
        return

def Evergold_1372_MapTrigger_25_38(p):
    if StuffDone["49_6"] == 1:
        if StuffDone["49_7"] < 3:
            Town.PlaceEncounterGroup(1)
            return
        return

def Evergold_1374_MapTrigger_42_59(p):
    if StuffDone["49_7"] < 2:
        result = ChoiceBox("This gateway leads south into the Golem Factories. It is here that rocks are melted down, placed into molds, and shaped into specifically designed Golems. The products are then sold throughout the world as guards and such.\n\nYou notice that one of the factories appears to be not operational. Several heavily armored guards stand at the entrance and the doors appear to be sealed tightly by magical runes.\n\nFrom the guards you learn that the factory is closed because the golems inside went berserk. No one as of yet seems to be able to solve the problem yet. Perhaps you could enter the factory and give it a try.", eDialogPic.CREATURE, 119, ["Leave", "Enter"])
        if result == 1:
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(6,32)
            Party.MoveToMap(TownMap.List["GolemFactory_58"])
            return
        p.CancelAction = True
        return
    ChoiceBox("You return to the Golem factories. The factory that you helped liberate is still not functional. However, wizards and laborers are actively trying to reactivate the plant. Remembering what you heard, you believe this will take several months.\n\nWell at least it beats the alternative of having to destroy the factory. That would have taken years, or even decades, to fully replace.", eDialogPic.CREATURE, 119, ["OK"])
    p.CancelAction = True

def Evergold_1377_MapTrigger_32_48(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
        ChoiceBox("Among the shelves of magical works, you discover one book that is of particular use, PRACTICAL SPELLS FOR INTERMEDIATE WARRIOR MAGE. Intrigued by the title, you begin to read.\n\nAfter several hours of study, you come away with a high degree of magical knowledge in an entire assortment of intermediate level mage spells. Books like these are rare to come by as they are illegal for public use.\n\nHowever, you bet that this library has been granted a permit to carry such works.", eDialogPic.STANDARD, 14, ["OK"])
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_poison")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_ice_bolt")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_slow_group")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_venom_arrows")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_wall_of_ice")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_stealth")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_fire_barrier")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_summoning")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_shockstorm")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1378_MapTrigger_35_54(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
        ChoiceBox("Among the shelves you find a prayer book entitled: INTERMEDIATE CLERIC\'S PRAYER BOOK. Just flipping through the contents reveals this is a tome which can only be used in registered magical training institutions.\n\nYou start to read through and after a few hours, you achieve mastery of an assortment of intermediate level prayers.", eDialogPic.STANDARD, 15, ["OK"])
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_cure_all_poison")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_curse_all")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_dispel_undead")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_sticks_to_snakes")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_martyrs_shield")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_cleanse")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_bless_party")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_major_heal")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_flamestrike")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_mass_sanctuary")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_summon_host")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1379_MapTrigger_38_52(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 15:
        MessageBox("Among these assorted magical texts, you find a book of prayers to the gods of war and combat. Many prayers are a bit twisted involving practices like animal or even human sacrifice.\n\nThere is one simpler prayer called \'Pestilence\' which unleashes a horrible plague onto a battlefield. You manage to memorize the divine words.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_pestilence")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1380_MapTrigger_34_50(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
        MessageBox("Among these magical works you find a small book called WARDING OFF THE DAEMONIC. Within details several methods for keeping daemons at bay. Most of them are practical ritual such as protections for property.\n\nHowever, there are a couple offensive prayers designed to ward off these low energy beings. The one you feel most useful is called \'Ravage Spirit\' which you take the time to learn.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_ravage_spirit")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1381_MapTrigger_38_48(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
        MessageBox("You come across a huge book entitled: TECHNIQUES IN MAGICAL BARRIER CREATION. Flipping through the pages reveals this is way beyond you. Yet, there is one practical spell for the quick creation of a \'Force Barrier\'.\n\nAlthough it is quite demanding, it could prove useful in some situations. You take some time to learn how to create the barrier.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_force_barrier")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1382_MapTrigger_26_54(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
        MessageBox("Among these magical works is a book all about summoning and the conjuring of various creatures. The topics discussed are quite advanced and you can only grasp one of the simpler summoning spells called \'Major Summon\'.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_major_summon")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1383_MapTrigger_34_47(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 15:
        MessageBox("You discover a book detailing the creation of several more advanced potions. Most of them are a bit too advanced or impossible for you to apply. However, the recipe for \'Potion of Bliss\' may be useful.")
        Party.LearnRecipe("bliss_potion")
        return
    MessageBox("This library contains an assortment of tomes on magical spell casting. Many of them would potentially be quite useful to you assuming you increase your level of magical studies.")

def Evergold_1384_MapTrigger_36_51(p):
    if SpecialItem.PartyHas("KiveksJournal"):
        return
    if StuffDone["50_8"] == 0:
        if StuffDone["49_2"] == 1:
            result = ChoiceBox("While browsing these rare and often magical selection of books you ironically come across Kivek\'s Journal! You take it off the shelf and flip through it. The writing is a bit faded, but you can still make it out.\n\nMost of the work contains Kivek\'s thoughts on the universe and goes into great detail and complexity. You notice some very bold statements such as Ermarian not being the center of the universe, but an insignificant pebble in a vast sea of nothingness.\n\nYou come to the section on the nature of time where the complexity increases greatly. You cannot understand much of this except that he keeps mentioning something called fabric.\n\nThis is definitely what Arcturus in Gynai is looking for.", eDialogPic.TERRAIN, 135, ["Leave", "Take"])
            if result == 1:
                SpecialItem.Give("KiveksJournal")
                return
            return
        return

def Evergold_1385_MapTrigger_27_44(p):
    if SpecialItem.PartyHas("KiveksJournal"):
        MessageBox("As you attempt to leave the library, you hear a beeping noise. The attendant comes out from behind his desk and approaches you. \"Sorry materials cannot be removed from the library, legal reasons you know.\" You are forced to give back Kivek\'s Journal.")
        StuffDone["49_2"] = 1
        SpecialItem.Take("KiveksJournal")
        return

def Evergold_1387_MapTrigger_36_40(p):
    if SpecialItem.PartyHas("KiveksJournal"):
        if StuffDone["49_2"] == 1:
            result = ChoiceBox("You examine the window and find it to be partially open to let fresh air inside. Seeing you cannot get Kivek\'s Journal out the front door, you will need to find another way. It may just be possible to slide the book out the window without anyone noticing.", eDialogPic.TERRAIN, 109, ["No", "Yes"])
            if result == 0:
                return
            elif result == 1:
                MessageBox("While no one is looking, you slide the book out the window. You have to give it a shove, but you manage to get it through. The book falls on the otherside of the wall. You hear a thud as it lands. Now you just need to recover it.")
                StuffDone["50_8"] = 1
                SpecialItem.Take("KiveksJournal")
                return
            return
        return

def Evergold_1389_MapTrigger_37_39(p):
    if StuffDone["50_8"] == 1:
        StuffDone["50_8"] = 0
        MessageBox("You recover Kivek\'s Journal from the ground. Luckily, the old tome was not damaged at all in the fall. Just make sure you don\'t try getting back in the library with this book in hand.")
        StuffDone["49_2"] = 2
        SpecialItem.Give("KiveksJournal")
        return

def Evergold_1391_MapTrigger_51_4(p):
    if StuffDone["62_5"] == 1:
        result = ChoiceBox("You check in at the base. It appears that there is indeed a significant something on Gallows Isle. There is a cargo ship full of materials ready to carry you to the island. The voyage will last for about one day.\n\nThis is your last chance to turn back, but your destiny lies ahead.", eDialogPic.STANDARD, 16, ["Leave", "Onward"])
        if result == 1:
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(24,36)
            Party.MoveToMap(TownMap.List["FortGallows_74"])
            return
        p.CancelAction = True
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This way leads into the naval base where vast amounts of raw materials are shipped in and the products are shipped out. This is one of the most profitable, and important, ports in all of the world.")

def Evergold_1397_MapTrigger_22_59(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This leads into the alchemy processing plants. Within the structures ahead, a river of potions and other chemicals are manufactured here. They are bottled and distributed all throughout the Empire.")

def Evergold_1400_MapTrigger_59_15(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This gate leads to the main manufacturing area. A variety of consumer goods are produced there. However, the area is the primary construction place for weapons and armor used by the Empire.")

def Evergold_1406_TownTimer_9(p):
    Animation_Hold(-1, 059_closedoor)
    Wait()
    ChoiceBox("Suddenly, you hear a door slam shut to your south. You see an elderly wizard, quite frustrated, storming from the library. He takes a seat at one of the tables in the lobby.\n\nYou wonder why this man is so frustrated. Perhaps you should find out.", eDialogPic.CREATURE, 28, ["OK"])
    Town.PlaceEncounterGroup(1)

def Evergold_1407_TalkingTrigger0(p):
    if StuffDone["49_4"] == 0:
        p.TalkingText = "He asks for your names and he searches the registry. He double checks and turns to you. \"I\'m sorry, but you are not on my registry. Remember this is a private library. If you feel this is a mistake, you will need to see an administrator.\""
        if StuffDone["49_6"] == 0:
            StuffDone["49_6"] = 1
            Timer(Town, 3, False, "Evergold_1406_TownTimer_9", eTimerType.DELETE)
            return
        return

def Evergold_1408_TalkingTrigger8(p):
    if StuffDone["49_7"] >= 3:
        return
    if StuffDone["49_7"] < 2:
        p.TalkingText = "\"Thank you for the offer. I cannot tell you how much this research means to me. I hope that you succeed.\""
        StuffDone["49_7"] = 1
        ChoiceBox("\"You would be willing to help? Then there are some things that you will need to know. The rebels managed to take out all the conventional ways of reaching the control center. This means you will need to navigate through the factory.\n\nSo do not expect this to be any kind of cake walk. Additionally, the rebels laid booby traps all over the factory. The most dangerous being the poison gas bombs. They managed to take out three of the five previous attempts.\n\nThe shut down procedure has been locked to prevent anyone from accessing it. To unlock it, you will need to know two things. One is a special combination, and the other is a key.\n\nThe combination is 20-41-16-92-38. Got that? (You take note of this) As for the key, I\'m afraid it was lost with the first attempt. You will need to locate this somewhere in the factory.\n\nIt is labeled as the \'Emergency Shutdown Key\'. You should know it when you find it. Once you have these two things, proceed to the controls. Use the combination and the key to unlock the shutdown lever and pull it.\n\nThat should take care of the Golem production. When you have completed this, return here for your reward.\"", eDialogPic.CREATURE, 119, ["OK"])
        StuffDone["49_5"] = 1
        return
    StuffDone["49_7"] = 3
    StuffDone["49_4"] = 1
    ChoiceBox("You return with news that you have succeeded in shutting down the Golem Factory, thus saving it from demolition. Talon\'s eyes light up with joy upon hearing the news.\n\n\"Then my research, it is safe!\" He puts his arm up in the air as he tilts back in his chair and lets out a sigh of relief. Smiling, he says, \"You will never know how grateful I am for what you did. Now about that reward...\"\n\nHe rises and talks to the attendant at the library desk. After some convincing, he gets your name on the registry. He returns to his seat. \"I noticed you wanted to get into the library. Although it\'s usually reserved for us mages, now you can get in.\"\n\nI\'m sure what you find inside will be quite useful and well deserved payment for services rendered. Now I have to take a look at what\'s going to need to be fixed back at the factory. I\'m sure there\'s months of repairs ahead.\"", eDialogPic.CREATURE, 119, ["OK"])

def Evergold_1409_TalkingTrigger26(p):
    if StuffDone["52_2"] == 0:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            p.TalkingText = "\"I can only train one at a time.\""
            return
        if Party.Gold >= 6000:
            Party.Gold -= 6000
            pc.SetSkill(eSkill.DISARM_TRAPS, pc.GetSkill(eSkill.DISARM_TRAPS) + 6)
            p.TalkingText = "You conclude your training."
            pc.SetSkill(eSkill.LOCKPICKING, pc.GetSkill(eSkill.LOCKPICKING) + 6)
            ChoiceBox("Nemmeth takes one of you aside and begins to show you the techniques of thievery. You cover two major topics: Disarming Traps and Lockpicking. The lessons are in depth and quite advanced.\n\nNemmeth is quite a skilled instructor, showing you all sorts of different traps and locks, and the tricks of the trade for disarming them. After several hours of in depth instruction, you come away much more knowledgeable.", eDialogPic.STANDARD, 27, ["OK"])
            StuffDone["52_2"] = 1
            return
        p.TalkingText = "You cannot afford it."
        return

def Evergold_1410_TalkingTrigger52(p):
    count = Party.CountItemClass(41, True)
    Party.Gold += count * 200
    p.TalkingText = "You show him your watch collection. He looks at them carefully. \"Not the highest quality. I suppose I can pay 200 gold per watch.\""

def Talking_57_17(p):
    if Party.Gold < 60:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 60
        Party.Pos = Location(20, 39)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "The Slith takes your money and points out which room is yours for the night. You find the lodgings to be most comfortable and you have an excellent rest."
        CentreView(Party.Pos, False)

def Talking_57_18(p):
    if Party.Gold >= 15:
        Party.Gold -= 15
        p.TalkingText = "You are served some of the house brew. It has a strange artificial taste to it. It feels very processed like the stuff they served back in training. Ssvasskar turns to you, \"Say you look like adventuring types. Want some advice, only 300 gold.\""
    else:
        p.TalkingText = "You cannot afford it."

def Talking_57_19(p):
    if Party.Gold >= 300:
        Party.Gold -= 300
        p.TalkingText = "\"I used to be an adventurer before I settled down to run this inn. There was person in my group, an expert thief, named Nemmeth. He occasionally trains other adventurers in the trades for a reasonable price. Tell him I sent you.\""
    else:
        p.TalkingText = "\"Really it is wonderful advice. I am sure you will not regret the small payment.\""
