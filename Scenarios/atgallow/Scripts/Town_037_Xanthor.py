
def Xanthor_827_MapTrigger_32_30(p):
    if StuffDone["17_5"] == 2:
        StuffDone["17_5"] = 3
        StuffDone["17_3"] = 2
        Town.PlaceEncounterGroup(2)
        return

def Xanthor_828_MapTrigger_35_30(p):
    if StuffDone["17_5"] == 1:
        Animation_Hold(-1, 068_identify)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(17,17)
        Party.MoveToMap(TownMap.List["WatchpointTower_42"])
        return

def Xanthor_829_MapTrigger_16_52(p):
    if StuffDone["17_6"] >= 3:
        if StuffDone["17_6"] == 250:
            return
        StuffDone["17_6"] = 250
        TownMap.List["Xanthor_37"].DeactivateTrigger(Location(16,52))
        MessageBox("You enter one of the crime scenes. Palver\'s place appears fairly clean and orderly. There are no visible signs of struggle. One item of suspicion is the odor of decay in the air. You look around and see the culprit.\n\nA half eaten meal is set on the table and is beginning to rot. It is as if half way through his meal, Palver just got up and left. Strange, there must be more here.")
        return

def Xanthor_830_MapTrigger_19_56(p):
    if StuffDone["17_3"] >= 3:
        MessageBox("Palver\'s desk reveals little clues as to his disappearance. You do note a lot of references to demonology such as papers discussing rituals. None of it is practical to you.")
        return

def Xanthor_831_MapTrigger_17_55(p):
    if StuffDone["17_3"] >= 3:
        result = ChoiceBox("A search underneath Palver\'s dresser reveals a small button set into the floor. Carved into it is an ominously glowing green rune. You wonder why someone would have a button on their floor. Do you dare push it to see what happens?", eDialogPic.TERRAIN, 145, ["Leave", "Push"])
        if result == 1:
            for pc in Party.EachAlivePC():
                pc.Poison(8)
            MessageBox("You press the button and poisonous gas pours out! You manage to clear the area, but not before inhaling some of the toxic fumes. You wonder if your mishap accomplished anything other than poisoning you.")
            Town.AlterTerrain(Location(21,54), 0, TerrainRecord.UnderlayList[140])
            return
        return

def Xanthor_832_MapTrigger_21_55(p):
    if StuffDone["17_7"] == 250:
        return
    StuffDone["17_7"] = 250
    TownMap.List["Xanthor_37"].DeactivateTrigger(Location(21,55))
    MessageBox("Your suspicion begins to peak as you discover a secret passage in Palver\'s home. First a trapped button on the floor, and now a hidden corridor blocked by a magic barrier. You wonder, why he went to so much trouble.")

def Xanthor_833_MapTrigger_23_55(p):
    ChoiceBox("You search this bookshelf in the hopes of finding answers. You find a great store of information on demonology. All of the books far too arcane for your comprehension. Now you probably know why he went to lengths to hide these materials.\n\nWorks on this topic have been forbidden by the Empire. These books are some of the few still considered off limits. And with good cause. Many times have incompetent mages caused great destruction by dabbling in these realms.\n\nOne book, is more of a journal. Most of the ramblings are just technical nonsense to you. However, the book has a few passages mentioning Odix. Apparently, the two have not been getting along all that well lately.\n\nHe even once mentions conjuring up a demonic spirit to follow Odix around and cause him trouble and that sort of thing.\n\nScary stuff. But still no clues pertaining to the disappearances.", eDialogPic.STANDARD, 13, ["OK"])

def Xanthor_834_MapTrigger_15_20(p):
    if StuffDone["17_3"] >= 25:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
            MessageBox("You flip through this textbook. The one spell that is of major use is called \"Protection\" which allows the caster to make a person invulnerable for a short period of time.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_protection")
            return
        MessageBox("Unfortunately, this textbook is a bit too advanced for you. You will need more Mage Lore to understand it.")
        return
    MessageBox("The pages on this spell book are blank! You wonder if this is some kind of device to keep unwanted people from reading it.")

def Xanthor_835_MapTrigger_17_20(p):
    if StuffDone["17_3"] >= 25:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 18:
            MessageBox("Contained within this book are several powerful prayers. Most of them are fairly arcane, but one is within your grasp. You now know how to cast \'Revive All\'!")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("p_revive_all")
            return
        MessageBox("Unfortunately, this textbook is a bit too advanced for you. You will need more Mage Lore to understand it.")
        return
    MessageBox("The pages on this spell book are blank! You wonder if this is some kind of device to keep unwanted people from reading it.")

def Xanthor_836_MapTrigger_29_33(p):
    if StuffDone["100_0"] == 5:
        if StuffDone["23_8"] == 250:
            return
        StuffDone["23_8"] = 250
        Animation_Hold(-1, 095_enterdungeon)
        Wait()
        ChoiceBox("CHAPTER V -- THE FALLEN LORD", eDialogPic.STANDARD, 4, ["OK"])
        return

def Xanthor_839_OnEntry(p):
    if StuffDone["17_3"] >= 6:
        if StuffDone["17_3"] >= 14:
            if StuffDone["17_3"] >= 28:
                if StuffDone["100_0"] < 8:
                    Town.PlaceEncounterGroup(5)
                    if StuffDone["23_7"] == 250:
                        return
                    StuffDone["23_7"] = 250
                    ChoiceBox("You return to Xanthor. Astervis turns to you and smiles. \"It\'s been a good time working with you. I must say that its been an interesting couple of weeks. I\'m going to miss all the excitement.\n\nWhere to next you ask? For me, I\'m returning to my schooling. Now that Odix is gone, I\'m just going to have to be educated like everyone else at the Academy. Of course, I\'ll be at Odix\'s house most of the time, feel free to stop by and visit.\n\nAnd for you, I think Mayor Miranda will want to speak with you. I\'m sure she\'ll want a full report on her desk from me by tonight also.\" He chuckles. \"Good luck soldiers!\"", eDialogPic.STANDARD, 16, ["OK"])
                    SpecialItem.Take("AstervisNPC")
                    Message("Astervis leaves the party.")
                    return
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Astervis_204": Town.NPCList.Remove(npc)
                return
            if StuffDone["17_3"] < 19:
                Town.PlaceEncounterGroup(4)
                return
            return
        if StuffDone["17_3"] < 7:
            StuffDone["17_3"] = 7
            StuffDone["19_2"] = 1
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Astervis_204": Town.NPCList.Remove(npc)
            Town.PlaceEncounterGroup(3)
            return
        Town.PlaceEncounterGroup(3)
        return
    if StuffDone["17_3"] < 1:
        return
    Town.PlaceEncounterGroup(1)
    if StuffDone["17_3"] < 2:
        return
    Town.PlaceEncounterGroup(2)

def Xanthor_840_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(36, 31),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(33, 35),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(36, 39),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(39, 35),WorldMap.SectorAt(Party.OutsidePos))

def Xanthor_841_TalkingTrigger12(p):
    if StuffDone["17_5"] >= 2:
        p.TalkingText = "\"Then you should probably speak with Astervis. Odix\'s house is in the northwest corner of the city. I\'m sure Astervis can inform you further. Thank you for the assistance.\""
        return
    if StuffDone["17_5"] < 1:
        StuffDone["17_5"] = 1
        return

def Xanthor_842_TalkingTrigger16(p):
    ChoiceBox("\"For the past few weeks mages, apprentices, wizards alike have been vanishing without a trace. We are at a total loss to explain how this is happening, what is happening to the mages, and why this is happening.\n\nOur only hope is to inspect each disappearance and find out what clues turn up. So far all of our leads have turned up cold. Although, we suspect that teleportation is somehow involved. Unfortunately, we have little more than postulation on that.\n\nWith the research on barriers reaching a critical stage, I have been unable to investigate a few of the recent occurrences. That is what I am going to have you do. I want you to check out the following:\n\nYesterday a mage named Palver who lives in southwestern Xanthor turned up missing. You may wish to check his home. A professor of the school in Rune vanished while in his office during lunch.\n\nTwo students of an archaeologist named Zarmond were reported missing late last week. He lives in a hut just north of Malachite. And finally, a student in the Malachite Academy vanished while performing an experiment.\"", eDialogPic.CREATURE, 26, ["OK"])
    TownMap.List["ZarmondsHut_39"].Hidden = False
    if StuffDone["17_3"] == 2:
        StuffDone["17_3"] = 3
        StuffDone["17_8"] = 1
        return

def Xanthor_843_TalkingTrigger18(p):
    if StuffDone["17_3"] >= 9:
        if StuffDone["17_3"] < 10:
            StuffDone["17_3"] = 10
            ChoiceBox("You return to Astervis with the report of the massacre. You tell him of the swift, violent, and clean method of killing. Also, you tell of your encounter with the apparition and its threat. Astervis looks concerned.\n\n\"They must think we are getting too close. They have resulted to using threats and typical terror tactics. This may be encouraging because perhaps we are very close to figuring this whole thing out.\n\nThere is much paperwork to be done. Another good sign is the lack of further disappearances since you showed up. I really don\'t have much of anything for you to do right now.\n\nYou may wish to go back to all of the crime scenes and look for anything you may have missed. Just check back in a little while in case something comes up, all right?\"", eDialogPic.CREATURE, 26, ["OK"])
            return
        p.TalkingText = "\"There haven\'t been anymore disappearances lately, which is a very good thing. You may wish to retrace your steps to find anything you may have missed.\""
        return
    if StuffDone["17_3"] < 8:
        StuffDone["17_3"] = 8
        ChoiceBox("You report to Astervis everything about your investigation. He takes detailed notes about the situation, asking many questions. After looking them over, Astervis makes a few comments.\n\n\"Well, this clears up a few questions. We now know how these abductions are occurring. As we had expected, it was done through a process called teleportation snaring -- a difficult but effective method of trapping a target.\n\nI find the ruins in the school of particular interest. It appears Zarmond\'s apprentices had stumbled onto something that they were not supposed to. Assuming they are correct, the mages they found were the ones that vanished!\n\nUnfortunately, whoever or whatever responsible for this did a fair job of keeping the trail cold. My guess is the ruins are now a dead end, anything that was there was cleaned out long ago.\n\nOn the other hand, we are gaining progress. The enemy has made one mistake; there is no reason to believe that it will not make another. In the mean time...\"\n\nSuddenly there is a random flashing of color in the center of the room, it begins to take form.", eDialogPic.CREATURE, 26, ["OK"])
        ChoiceBox("An image of Mayor Miranda materializes! She surveys the scene and turns to you. \"I\'m glad that you are here as well. This was meant to be told to Astervis and relayed on to you. But since you are here, I can just tell you both.\n\nI have just received report from the administrator at Malachite. He has spoken some grave news. About an hour ago, an entire class of students were massacred! The cause of death is magical, but exactly how is yet unknown.\"\n\nShe turns specifically to you. \"I need your group to go there and check out the situation. The incident occurred in the Biology Department. Find out if this massacre has anything to do with the stream of abductions.\"\n\nShe turns to Astervis. \"I will need a report from you on the situation and recent investigations by tomorrow morning. Odix has been informed, and has told me to tell you he has more data for you to analyze.\" Astervis sighs.\n\n\"Now let\'s try to put a stop to these occurrences as soon as we can. Good luck!\" The image disperses in a brilliant spiraling cloud of color. Astervis turns to you.\n\n\"Well you heard the mayor. Get going! In the meantime I guess I\'ll have to write up that report and find some time to do that data. Looks like another sleepless night for me...\"", eDialogPic.CREATURE, 32, ["OK"])
        StuffDone["19_3"] = 1
        return

def Xanthor_844_TalkingTrigger20(p):
    if StuffDone["17_3"] >= 12:
        p.TalkingText = "You show Zarmond the tablets. He looks them over and shrugs. \"This is really outside my area of expertise. You will have to show them to someone much more knowledgeable than myself.\n\nI know that people in Malachite study archaeology. Perhaps the professor will be able to provide a better analysis.\""
        return

def Xanthor_845_TalkingTrigger21(p):
    if StuffDone["17_3"] >= 18:
        p.TalkingText = "Astervis, clearly hurt by the accusations, stands up and storms out the building. Oh dear, what do you do next?"
        StuffDone["17_3"] = 19
        ChoiceBox("You report what you have learned to Astervis. Upon hearing accusations against Odix, he grows very defensive. \"Preposterous! Of all the people in the world, I can assure you that Odix would never betray his friends or Empire for any reason.\n\nAnd from who better than Palver? Palver! The man who was out to get Odix! You don\'t know that man; he would lie, cheat, steal, or do anything that would cause harm to my mentor.\n\nHow do we know he was not just planted there by whomever is doing all this? My guess is this is yet another web of deception set in place to distract us and destroy our operation. After all, what better place to strike than at Odix\'s credibility?\"\n\nYou insist that this matter be investigated. \"Absolutely not! I refuse to believe any of this. Odix is a man of honor. He has given me more than I could have ever hoped for.\"\n\nYou continue to insist and Astervis grows even more frustrated.", eDialogPic.CREATURE, 27, ["OK"])
        StuffDone["21_3"] = 19
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Astervis_204": Town.NPCList.Remove(npc)
        StuffDone["21_4"] = 1
        return
    if StuffDone["17_3"] < 15:
        StuffDone["17_3"] = 15
        ChoiceBox("You report the tablets revealed another level to the school. When you went to investigate where it should be, you literally ran into a wall. You describe the wall and the glyphs as best you can to Astervis. He thinks for a while.\n\n\"Hmmmmm,\" he places his hand on his chin. \"Whoever really wants to keep that place a secret. That wall sounds pretty heavy duty. Although I\'m not a demolition expert, I\'m guessing that a concentrated blast should do the trick.\n\nExcuse me, I\'ll be right back.\" He gets up and enters the room to the north. You take seats and after about five minutes, he returns. \"Well, I\'ve managed to secure a barrel of our best concentrated explosives.\n\nIf they don\'t get the job done, I don\'t know what will!\" He clears his throat. \"Listen carefully. Head across town to the supply house and mention my name. The attendant will give you a barrel of explosives.\n\nBe careful, these explosives are VERY concentrated. They will may only deliver a small blast, but it will be extremely powerful and should knock down the wall. Hopefully, the ruins won\'t cave in, so cross your fingers.\"\n\nHe looks at his textbook and rolls his eyes. \"Looks like I have more work to do. I\'ll get back to you later. Good luck!\"", eDialogPic.CREATURE, 26, ["OK"])
        return

def Xanthor_846_TalkingTrigger24(p):
    if StuffDone["17_3"] >= 16:
        return
    if StuffDone["17_3"] < 15:
        p.TalkingText = "\"Astervis? I believe I\'ve heard of him. He\'s quite talented, about my age I hear. Don\'t know too much about him, sorry!\""
        return
    SpecialItem.Give("BarrelofExplosives")
    p.TalkingText = "\"Ah yes, Astervis said you would be here to pick up some explosives. Just one minute.\" He heads into the back room and emerges with a small, but heavy, barrel. \"Here you go! Be careful, these babies are dangerous!\""
    StuffDone["17_3"] = 16

def Xanthor_847_TalkingTrigger26(p):
    if StuffDone["17_3"] == 28:
        StuffDone["17_3"] = 29
        ChoiceBox("\"I have heard all of what you have done. All the residents are happy, the Prime Director is happy, heck, even I\'m happy! The disappearances have finally ended and things can go back to normal.\n\nAnyway, the Prime Director wished me to relay his congratulations and appreciation to you on this rather complicated assignment. Additionally, he would also like to commend you personally back at the palace!\"", eDialogPic.CREATURE, 32, ["OK"])
        StuffDone["100_0"] = 5
        StuffDone["100_1"] = 1
        return

def Xanthor_848_TalkingTrigger27(p):
    if StuffDone["100_0"] >= 6:
        if StuffDone["100_0"] < 7:
            if StuffDone["49_2"] == 1:
                p.TalkingText = "You mention you are looking Kivek\'s Journal. \"I\'ve heard of Kivek before. Had some pretty advanced ideas for his time. I would check the Imperial Library. If it\'s not there, you may wish to check in Evergold. They have a library for that kind of stuff.\""
                return
            p.TalkingText = "\"So now you have to head off to Gynai? It\'s an interesting place I hear. I would love to join you, but I have my studies you know.\""
            return
        if StuffDone["54_2"] == 1:
            p.TalkingText = "You tell him about the strange waxy barrier. \"Hm, that sounds like a magic seal. They are really effective at protecting things. Real difficult to make, requiring much skill in magic and alchemy. Even more difficult to dispel.\""
            return
        p.TalkingText = "You tell Astervis about your misadventure in Gynai. He seems amused. \"I heard their customs were different. I hope you can find something of use in those three sites you have to explore.\""
        return
    if StuffDone["100_0"] < 5:
        return
    p.TalkingText = "\"So you\'re going after Morbane, eh? Don\'t think I can tag along this time I\'m afraid. Although, I have pondered his weakness.\""

def Xanthor_849_TalkingTrigger31(p):
    if StuffDone["17_3"] >= 28:
        return
    if StuffDone["17_3"] < 1:
        p.TalkingText = "\"Military matters are not overly difficult to handle and are mostly routine -- patrol staffing, you know. Aside from the few recent abnormal cases, the duty is quite easy to satisfy.\""
        return
    p.TalkingText = "\"My job has become quite difficult in the wake of the disappearances. We have investigations on going, but with little luck. This problem is one of those things that no amount of military force can guard against.\""
