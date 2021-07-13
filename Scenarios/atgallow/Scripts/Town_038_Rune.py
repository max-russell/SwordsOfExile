
def Rune_850_MapTrigger_13_32(p):
    if StuffDone["17_8"] < 1:
        if StuffDone["17_9"] == 250:
            return
        StuffDone["17_9"] = 250
        MessageBox("There is currently a lecture in progress. Upon your entry, all of the students look over. The wizard at the head of the room turns to you and scowls. He clearly does not like that he was interrupted.")
        return

def Rune_851_MapTrigger_28_32(p):
    if StuffDone["17_8"] == 1:
        if StuffDone["18_1"] == 250:
            return
        StuffDone["18_1"] = 250
        MessageBox("This must be the school that Astervis asked you to investigate. Everything is quiet. No students are gathered throughout the halls. No activity at all as if the entire place were in mourning.")
        return

def Rune_852_MapTrigger_22_30(p):
    if StuffDone["18_0"] >= 1:
        if StuffDone["18_2"] == 250:
            return
        StuffDone["18_2"] = 250
        MessageBox("You enter Seth\'s office and find no clear evidence of struggle. Perhaps a closer investigation may turn something up.")
        return

def Rune_853_MapTrigger_21_29(p):
    if StuffDone["18_0"] >= 1:
        MessageBox("On a wild hunch you decide to search Seth\'s potted plant. It is an exotic species which you have not ever seen before. Aside from that, a detailed search turns up nothing.")
        return

def Rune_854_MapTrigger_21_27(p):
    if StuffDone["18_0"] >= 1:
        MessageBox("Seth has copies of many of the standard textbooks and references of magic. A few books for entertainment, but nothing else of real great interest.")
        return

def Rune_855_MapTrigger_23_28(p):
    if StuffDone["18_0"] == 1:
        StuffDone["54_1"] = StuffDone["17_3"]
        if StuffDone["54_1"] == 250:
           pass
        MessageBox("Seth kept his desk in orderly condition. Everything is very well organized and expected of his position. The chair is not fully pushed in, as if he was sitting in it when he vanished.\n\nAlso, a search of the beneath the desk reveals a pen. Your guessing that he was using this to grade his papers. He must have dropped it before or during the abduction. Unfortunately, there is little else out of the ordinary.")
        StuffDone["18_0"] = 2
        StuffDone["17_3"] += 1
        if StuffDone["17_3"] == 250:
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(19,56))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(17,55))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(15,20))
            TownMap.List["Xanthor_37"].DeactivateTrigger(Location(17,20))
            TownMap.List["ZarmondsHut_39"].DeactivateTrigger(Location(20,14))
            TownMap.List["ZarmondsHut_39"].DeactivateTrigger(Location(16,9))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(56,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(55,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(57,8))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(50,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(52,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(53,16))
            TownMap.List["AncientRuins_40"].DeactivateTrigger(Location(55,16))
            TownMap.List["WatchpointTower_42"].DeactivateTrigger(Location(24,33))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(28,24))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(11,35))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(11,36))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(14,28))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(28,20))
            TownMap.List["Malachite_59"].DeactivateTrigger(Location(15,28))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(56,33))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(29,51))
            TownMap.List["ForgottenAcademy_60"].AlterTerrain(Location(4,13), 1, None)
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(4,13))
            TownMap.List["ForgottenAcademy_60"].AlterTerrain(Location(5,13), 1, None)
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(5,13))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(4,10))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(5,10))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(3,4))
            TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(9,11))
        if StuffDone["17_3"] >= StuffDone["54_1"]:
            return
        if StuffDone["54_1"] >= 5:
            StuffDone["17_3"] = 6
            return
        if StuffDone["54_1"] < 4:
            StuffDone["17_3"] = 4
            return
        StuffDone["17_3"] = 5
        return

def Rune_856_MapTrigger_37_13(p):
    if StuffDone["44_0"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The door will not open for you. It seems magically sealed. The attendant at the desk looks over to you, \"I\'m sorry, but access to the labs is restricted. You will need to secure a lease in order to use the facilities.\"")
        return

def Rune_857_MapTrigger_18_13(p):
    if Maths.Rand(1,0,100) < 30:
        Animation_Hold(-1, 036_spiderhello)
        Wait()
        return

def Rune_858_MapTrigger_17_13(p):
    if Maths.Rand(1,0,100) < 30:
        Animation_Hold(-1, 035_spiderhi)
        Wait()
        return

def Rune_863_MapTrigger_36_38(p):
    if SpecialItem.PartyHas("SackofMessages"):
        MessageBox("You deliver your sack of messages from Rune to the delivery service here. You are paid the promised amount of 200 gold.")
        SpecialItem.Take("SackofMessages")
        Animation_Hold(-1, 015_cash)
        Wait()
        Party.Gold += 200
        return

def Rune_864_MapTrigger_39_9(p):
    if StuffDone["120_3"] >= 2:
        result = ChoiceBox("This workstation is currently set up to allow the manufacturing of Strong Skill Potions. You will need to provide a few ingredients, but all standard reagents are present. Do you (1) Attempt to make the Potion OR (2) Change set up.", eDialogPic.STANDARD, 20, ["Leave", "2", "1"])
        if result == 1:
            result = ChoiceBox("You may rearrange the settings using the poster on the wall. There are two others of interest: (1) Weak Skill Potion OR (2) Medium Skill Potion.", eDialogPic.STANDARD, 20, ["Leave", "2", "1"])
            if result == 1:
                MessageBox("You rearrange the setup to allow for the creation of Medium Skill Potions.")
                StuffDone["120_3"] = 1
                return
            elif result == 2:
                MessageBox("You rearrange the setup to allow for the creation of Weak Skill Potions.")
                StuffDone["120_3"] = 0
                return
            return
        elif result == 2:
            if StuffDone["120_2"] == 1:
                if Party.CountItemClass(35, False) > 0:
                    if Party.CountItemClass(52, False) > 0:
                        if Party.CountItemClass(33, False) > 0:
                            if Party.CountItemClass(34, True) > 0:
                                if Party.CountItemClass(35, True) > 0:
                                    if Party.CountItemClass(52, True) > 0:
                                        if Party.CountItemClass(33, True) > 0:
                                            Animation_Hold(-1, 008_bubbles)
                                            Wait()
                                            if Maths.Rand(1,0,100) < 20:
                                                Party.GiveNewItem("StrongSkillP_252")
                                                Message("Success!")
                                                return
                                            Animation_Hold(-1, 041_darn)
                                            Wait()
                                            Message("Unsuccessful!")
                                            return
                                        return
                                    return
                                return
                            MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Dragon Scales, and Gold Unicorn Horn)")
                            return
                        MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Dragon Scales, and Gold Unicorn Horn)")
                        return
                    MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Dragon Scales, and Gold Unicorn Horn)")
                    return
                MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Dragon Scales, and Gold Unicorn Horn)")
                return
            MessageBox("Alas, you lack the knowledge to perform such an operation.")
            return
        return
    if StuffDone["120_3"] < 1:
        result = ChoiceBox("This workstation is currently set up to allow the manufacturing of Weak Skill Potions. You will need to provide a few ingredients, but all standard reagents are present. Do you (1) Attempt to make the Potion OR (2) Change set up.", eDialogPic.STANDARD, 20, ["Leave", "2", "1"])
        if result == 1:
            result = ChoiceBox("You may rearrange the settings using the poster on the wall. There are two others of interest: (1) Medium Skill Potion OR (2) Strong Skill Potion.", eDialogPic.STANDARD, 20, ["Leave", "2", "1"])
            if result == 1:
                MessageBox("You rearrange the setup to allow for the creation of Strong Skill Potions.")
                StuffDone["120_3"] = 2
                return
            elif result == 2:
                MessageBox("You rearrange the setup to allow for the creation of Medium Skill Potions.")
                StuffDone["120_3"] = 1
                return
            return
        elif result == 2:
            if StuffDone["120_0"] == 1:
                if Party.CountItemClass(35, False) > 0:
                    if Party.CountItemClass(17, False) > 0:
                        if Party.CountItemClass(15, True) > 0:
                            if Party.CountItemClass(35, True) > 0:
                                if Party.CountItemClass(17, True) > 0:
                                    Animation_Hold(-1, 008_bubbles)
                                    Wait()
                                    if Maths.Rand(1,0,100) < 80:
                                        Party.GiveNewItem("WeakSkillP_266")
                                        Message("Success!")
                                        return
                                    Animation_Hold(-1, 041_darn)
                                    Wait()
                                    Message("Unsuccessful!")
                                    return
                                return
                            return
                        MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Ember Flowers, Unicorn Horn)")
                        return
                    MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Ember Flowers, Unicorn Horn)")
                    return
                MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Ember Flowers, Unicorn Horn)")
                return
            MessageBox("Alas, you lack the knowledge to perform such an operation.")
            return
        return
    result = ChoiceBox("This workstation is currently set up to allow the manufacturing of Medium Skill Potions. You will need to provide a few ingredients, but all standard reagents are present. Do you (1) Attempt to make the Potion OR (2) Change set up.", eDialogPic.STANDARD, 20, ["Leave", "2", "1"])
    if result == 1:
        result = ChoiceBox("You may rearrange the settings using the poster on the wall. There are two others of interest: (1) Weak Skill Potion OR (2) Strong Skill Potion.", eDialogPic.STANDARD, 20, ["Leave", "2", "1"])
        if result == 1:
            MessageBox("You rearrange the setup to allow for the creation of Strong Skill Potions.")
            StuffDone["120_3"] = 2
            return
        elif result == 2:
            MessageBox("You rearrange the setup to allow for the creation of Weak Skill Potions.")
            StuffDone["120_3"] = 0
            return
        return
    elif result == 2:
        if StuffDone["120_1"] == 1:
            if Party.CountItemClass(35, False) > 0:
                if Party.CountItemClass(33, False) > 0:
                    if Party.CountItemClass(14, True) > 0:
                        if Party.CountItemClass(35, True) > 0:
                            if Party.CountItemClass(33, True) > 0:
                                Animation_Hold(-1, 008_bubbles)
                                Wait()
                                if Maths.Rand(1,0,100) < 40:
                                    Party.GiveNewItem("MediumSkillP_259")
                                    Message("Success!")
                                    return
                                Animation_Hold(-1, 041_darn)
                                Wait()
                                Message("Unsuccessful!")
                                return
                            return
                        return
                    MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Quicksilver)")
                    return
                MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Quicksilver)")
                return
            MessageBox("Alas, you do not have all the required ingredients. (Ambrosia, Mandrake Root, Quicksilver)")
            return
        MessageBox("Alas, you lack the knowledge to perform such an operation.")
        return

def Rune_865_OnEntry(p):
    if StuffDone["17_8"] >= 1:
        Town.PlaceEncounterGroup(1)
        return

def Rune_866_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 9),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(25, 10),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 10),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 10),WorldMap.SectorAt(Party.OutsidePos))

def Rune_867_TalkingTrigger6(p):
    if StuffDone["18_0"] >= 3:
        if StuffDone["17_3"] >= 28:
            p.TalkingText = "\"I am glad the disappearances have ended. It is too bad for my friend Seth. I wish he could have been saved. He must have been possessed by those mages and forced to do their bidding. Probably had to kill him, no?\""
            return
        if StuffDone["17_3"] < 10:
            p.TalkingText = "\"Any new developments on the disappearances?\" You report everything else that happened. \"Well, I hope this matter gets resolved soon. I hope I don\'t go like Seth did!\""
            return
        p.TalkingText = "\"Anything new on the disappearances?\" he asks. You tell him what you know. \"Well, I hope you can get to the bottom of all of this soon. I heard about the massacre at Malachite.\"\n\nHis voice trails off as he shakes his head."
        return
    if StuffDone["18_0"] < 2:
        StuffDone["18_0"] = 1
        return
    p.TalkingText = "You report what little you have learned. He frowns. \"I was hoping you would turn something up. Unfortunately, who or whatever did this was very clean and efficient. Thanks for you help anyway.\""
    StuffDone["18_0"] = 3

def Rune_868_TalkingTrigger12(p):
    if StuffDone["44_0"] == 0:
        if Party.Gold >= 500:
            Party.Gold -= 500
            RunScript("ScenarioTimer_x_2828", ScriptParameters(eCallOrigin.CUSTOM))
            return
        p.TalkingText = "You cannot afford it."
        return

def Rune_869_TalkingTrigger19(p):
    Sound.Play(036_spiderhello)

def Rune_870_TalkingTrigger34(p):
    if SpecialItem.PartyHas("SackofMessages_32"):
        return
    p.TalkingText = "You are handed a large sack containing several letters and light weight packages. \"Here you are. Please deliver this to Garnet as soon as possible.\""
    SpecialItem.Give("SackofMessages_32")
