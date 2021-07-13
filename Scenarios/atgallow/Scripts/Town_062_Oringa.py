
def Oringa_1532_MapTrigger_54_26(p):
    ChoiceBox("This stairway leads up into the guard tower where an Empire Archer watches the gate from above. Watching for what, you do not know. The archer probably just serves the traditional role of sentry.\n\nFor only a fool would leave his or her fortress or city unwatched and undefended, no matter what the chances are of an attack. The sentry does not have much to say to you.\n\nAnyway, there is not really anything to do here so you climb back down.", eDialogPic.CREATURE, 20, ["OK"])
    p.CancelAction = True

def Oringa_1534_TalkingTrigger2(p):
    if StuffDone["41_0"] == 1:
        p.TalkingText = "Remembering the mage back in Praddor, you hand him the note. \"I remember him. Let\'s see, sounds like something I discovered a while back. I believe this should work!\"\n\nHe writes a bunch of notes and hands it to you. \"This should help. Always willing to help out a fellow lizard lover.\""
        StuffDone["41_0"] = 2
        return

def Oringa_1535_TalkingTrigger10(p):
    if StuffDone["40_1"] >= 2:
        return
    if StuffDone["40_1"] < 1:
        p.TalkingText = "\"I have tracked Valgin across the world after his escape. I know after a decade of flight, he returned to Pralgad and hid in these mountains. I wish to recover his lost scrolls if possible. Alas, I am unsuccessful.\""
        return
    p.TalkingText = "You show her Valgin\'s Scrolls. Her face lights up with joy. \"After years of searching! Finally, my dreams of reading them can be fulfilled. I am indebted to you greatly. I have no treasure to offer, but knowledge will do.\"\n\nShe teaches you the prayer \'Firewalk\'."
    StuffDone["40_1"] = 2
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_firewalk")
    SpecialItem.Take("ScrollsofValgin")

def Talking_62_12(p):
    if Party.Gold < 40:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 40
        Party.Pos = Location(20, 8)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "You pay the fee. \"Your room is the first one on your left. If you need anything, come and get me!\" You head off to your room and have an excellent night\'s sleep."
        CentreView(Party.Pos, False)

def Talking_62_14(p):
    if Party.Gold >= 12:
        Party.Gold -= 12
        p.TalkingText = "He pours you some drinks. They are cold and refreshing! As you are sipping the brew he turns to you. \"Enjoying everything?\" You nod in approval. \"Good! Anything interesting in the world?\""
    else:
        p.TalkingText = "You cannot afford it."
