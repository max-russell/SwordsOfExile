
def Coraeon_2057_MapTrigger_39_35(p):
    ChoiceBox("You are not authorized to proceed into the tunnel construction site. The guards will not allow you to proceed.", eDialogPic.CREATURE, 12, ["OK"])
    p.CancelAction = True

def Coraeon_2059_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 35),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 35),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(27, 36),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(27, 36),WorldMap.SectorAt(Party.OutsidePos))

def Coraeon_2060_TalkingTrigger4(p):
    if StuffDone["67_5"] >= 1:
        p.TalkingText = "\"My research is progressing nicely. I have successfully managed to synthesize a thought crystal, a living crystalline intelligence! I could still use anymore learning crystals you may find, however.\""
        return

def Coraeon_2061_TalkingTrigger5(p):
    if Party.CountItemClass(51, False) > 0:
        if StuffDone["67_5"] >= 2:
            return
        if StuffDone["67_5"] < 1:
            result = ChoiceBox("He requires a Learning Crystal which you happen to have. When you show it to him, his eyes widen greedily. \"That is exactly what I need to conduct my research! I shall pay you a generous 6500 gold if you will sell it.\"", eDialogPic.TERRAIN, 168, ["Leave", "Accept"])
            if result == 1:
                if Party.CountItemClass(51, True) > 0:
                    p.TalkingText = "You hand over the crystal in exchange for a large sum of gold coins. He looks very anxious to conduct his research. \"I can hardly wait to perform my experiments. Oh if you find any more, I am still interested.\""
                    Party.Gold += 6500
                    StuffDone["67_5"] += 1
                    if StuffDone["67_5"] == 250:
                        pass
                    return
                return
            return
        result = ChoiceBox("You present another Learning Crystal to him. \"Excellent! My research on the first one has produced positive results. I have managed to synthesize a true living crystalline being called a Thought Crystal!\n\nNow here is the deal. I would be glad to do the following: (1) Give you a payment of 6500 gold OR (2) give you the Thought Crystal I produce.\n\nLet me tell you that the Thought Crystal will serve as a permanent source for knowledge, offering you experience as you travel. There is a definite plus in having this artifact.\"", eDialogPic.TERRAIN, 168, ["Leave", "2", "1"])
        if result == 1:
            if Party.CountItemClass(51, True) > 0:
                Sound.Play(053_magic3)
                p.TalkingText = "\"Enjoy your crystal. If you find any more Learning Crystals, be sure to bring them around. I still wish to conduct more research.\""
                SpecialItem.Give("ThoughtCrystal")
                ChoiceBox("You hand him the crystal and Kaeyn leaves into the side room telling you to wait here. After about ten minutes, you here a loud burst of energy. Kaeyn emerges from the room with a glowing crystal and presents it to you.\n\n\"Now listen carefully. From carrying this device with you, you will receive a slow progression of experience throughout your travels. Although the effect is not rapid, it is in theory, infinite.\n\nAt any time, you may use your crystal. At this time, all of the knowledge contained shall be released and the crystal shall dissolve. This will give you a lot of knowledge fast, but you will lose your crystal.\n\nAlso, I noticed some strange effects with the other crystal after I made this. They seem to destabilize as they come into proximity with each other. So in other words, I would advise against using this in proximity of other crystalline intelligences.\n\nThe effects could be rather catastrophic due to the interference between them. Anyway, I hope this device proves useful.\"", eDialogPic.TERRAIN, 168, ["OK"])
                Timer(None, 50, False,  "ScenarioTimer_x_2836")
                StuffDone["67_5"] += 1
                if StuffDone["67_5"] == 250:
                    pass
                return
            return
        elif result == 2:
            if Party.CountItemClass(51, True) > 0:
                p.TalkingText = "You hand over the crystal in exchange for a large sum of gold coins. He looks very anxious to conduct his research. \"I can hardly wait to perform my experiments. Oh if you find any more, I am still interested.\""
                Party.Gold += 6500
                StuffDone["67_5"] += 1
                if StuffDone["67_5"] == 250:
                    pass
                return
            return
        return

def Coraeon_2062_TalkingTrigger16(p):
    if StuffDone["67_4"] >= 2:
        p.TalkingText = "\"You have already been rewarded.\""
        return
    if StuffDone["67_4"] < 1:
        p.TalkingText = "\"First you must accomplish the task.\""
        return
    Party.Gold += 500
    p.TalkingText = "He hands you a small sack of gold coins, kind of a disappointment. \"Thank you for your service. I am sorry we do not have an ample supply of gold to spare, but know we here truly appreciate your efforts.\""
    StuffDone["67_4"] = 2

def Talking_82_15(p):
    if Party.Gold >= 0:
        if TownMap.List["DisposalSite_97"].Hidden == True:
            Party.Gold -= 0
            TownMap.List["DisposalSite_97"].Hidden = False
        p.TalkingText = "\"Within each disposal facility is a device which spreads quickfire throughout the structure, eradicating all dangerous substances. If you could activate the device and escape, you would be rewarded.\""
    else:
        p.TalkingText = ""

def Talking_82_22(p):
    if Party.Gold >= 3:
        Party.Gold -= 3
        p.TalkingText = "He pours you some beers and you exchange a few coins for them. They are definitely refreshing, but not of overly high quality. \"You know, I may have a little hint for you if you\'re looking for work.\""
    else:
        p.TalkingText = "You cannot afford it."

def Talking_82_24(p):
    if Party.Gold < 10:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 10
        Party.Pos = Location(13, 31)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "You pay your gold and are told to go to the common room. There are several cramped and uncomfortable beds. However, you do manage to get a fairly decent rest."
        CentreView(Party.Pos, False)

def Talking_82_36(p):
    if Party.Gold < 150:
        p.TalkingText = "She snickers when you realize that you cannot afford the room."
    else:
        Party.Gold -= 150
        Party.Pos = Location(50, 34)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "She sighs realizing that she failed to dissuade you from staying here. Reluctantly taking your gold, she escorts you to your room not taking the time to check up on you. Despite this, you have a wonderful night."
        CentreView(Party.Pos, False)
