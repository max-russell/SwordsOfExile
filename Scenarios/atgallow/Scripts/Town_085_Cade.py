
def Cade_2093_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(32, 27),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(32, 28),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(33, 28),WorldMap.SectorAt(Party.OutsidePos))

def Cade_2094_TalkingTrigger1(p):
    if StuffDone["24_2"] >= 2:
        return
    if StuffDone["24_2"] < 1:
        p.TalkingText = "\"Before you can be rewarded, I will need proof of the trader\'s death.\""
        return
    p.TalkingText = "You show him the trader captain\'s sash. \"Indeed, that is the sash worn only by trader captains. Our scouts have confirmed his death.\" He stands and grabs a displayed helmet atop of his bookshelf.\n\n\"This magical helmet was given to me by my former captain. You may have it.\""
    StuffDone["24_2"] = 2
    Party.GiveNewItem("MagicHelm_158")

def Cade_2095_TalkingTrigger26(p):
    if StuffDone["34_2"] >= 5:
        p.TalkingText = "\"Thanks again! The brew was a great success. Oh, would you like directions to the Grove again?\""
        return
    if StuffDone["34_2"] < 4:
        return
    p.TalkingText = "Having given her all of the needed ingredients, \"Now I can help that poor woman! You have shown great kindness. To repay it I will grant you access to the Druid\'s Grove. To find it, head north into the forest.\n\nYou should see a circle of stones, head due east and you will find the entrance.\""
    StuffDone["34_2"] = 5
    StuffDone["34_7"] = 1
    Sound.Play(040_thankyou)

def Cade_2096_TalkingTrigger27(p):
    if StuffDone["34_3"] == 0:
        if Party.CountItemClass(17, True) > 0:
            StuffDone["34_3"] = 1
            StuffDone["34_2"] += 1
            if StuffDone["34_2"] == 250:
                pass
            return
        p.TalkingText = "\"Ember flowers are not especially rare or anything, it\'s just I don\'t have any. I should really get some since they are extremely useful in powerful healing potions.\""
        return
    p.TalkingText = "\"That\'s quite all right, I already have enough of that. Thanks again!\""

def Cade_2097_TalkingTrigger28(p):
    if StuffDone["34_4"] == 0:
        if Party.CountItemClass(15, True) > 0:
            StuffDone["34_4"] = 1
            StuffDone["34_2"] += 1
            if StuffDone["34_2"] == 250:
                pass
            return
        p.TalkingText = "Unicorns are fairly common in this area. Any old gray unicorn will do. Customs forbid me from going out and killing one myself. I\'ve seen a lot of alive unicorns, but not any dead ones with an intact horns lately.\""
        return
    p.TalkingText = "\"That\'s quite all right, I already have enough of that. Thanks again!\""

def Cade_2098_TalkingTrigger29(p):
    if StuffDone["34_5"] == 0:
        if Party.CountItemClass(10, True) > 0:
            StuffDone["34_5"] = 1
            StuffDone["34_2"] += 1
            if StuffDone["34_2"] == 250:
                pass
            return
        p.TalkingText = "\"There aren\'t many Naga\'s out in the open. Their blood is extremely poisonous, corrosive, and if drank without treatment will cause paralysis. Yet, the blood loses the negatives when mixed in special ways.\""
        return
    p.TalkingText = "\"That\'s quite all right, I already have enough of that. Thanks again!\""

def Cade_2099_TalkingTrigger30(p):
    if StuffDone["34_6"] == 0:
        if Party.CountItemClass(14, True) > 0:
            StuffDone["34_6"] = 1
            StuffDone["34_2"] += 1
            if StuffDone["34_2"] == 250:
                pass
            return
        p.TalkingText = "\"Quicksilver is a naturally occurring liquid found within the earth. It\'s fairly expensive and not used all that often, so I haven\'t invested in any.\""
        return
    p.TalkingText = "\"That\'s quite all right, I already have enough of that. Thanks again!\""

def Cade_2100_TalkingTrigger45(p):
    count = Party.CountItemClass(32, True)
    Party.Gold += count * 2
    p.TalkingText = "You hand over all of your books that you were carrying around. Satisfied with the condition of each, she hands you 2 gold coins for each book."

def Talking_85_9(p):
    if Party.Gold >= 9:
        Party.Gold -= 9
        p.TalkingText = "He pours you a round of whiskey. \"So you\'re them Imperial Guardians right? Haven\'t seen many bold adventurers lately. But, I know one retired one who lives nearby.\""
    else:
        p.TalkingText = "\"I think you need to go out and slay some dragons or something! What kind of adventurers are you, poor and all?\""

def Talking_85_12(p):
    if Party.Gold < 30:
        p.TalkingText = "\"I think you need to go out and slay some dragons or something! What kind of adventurers are you, poor and all?\""
    else:
        Party.Gold -= 30
        Party.Pos = Location(39, 36)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "You hand him the payment and he points out your room. \"Sleep well. You should find the room most comfortable!\" And you do get an excellent night\'s sleep."
        CentreView(Party.Pos, False)
