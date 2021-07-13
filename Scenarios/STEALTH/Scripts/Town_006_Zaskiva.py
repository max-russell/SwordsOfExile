
def Zaskiva_57_MapTrigger_23_18(p):
    p.CancelAction = True
    ChoiceBox("You nonchalantly try to stroll into Lord Volpe\'s mansion. You don\'t even make it three steps inside before you find yourself surrounded by guards on all sides. Fortunately, their weapons aren\'t out yet.\n\nAn Empire Dervish walks up to you and says \"What is your business here? Why should Lord Volpe want to piss away his time with the likes of you?\"\n\nYou don\'t really have a satisfactory answer for that. Satisfied that you have no place here, the guards grab you and hustle you back out into the courtyard.", eDialogPic.CREATURE, 17, ["OK"])

def Zaskiva_59_MapTrigger_40_37(p):
    if StuffDone["6_1"] == 250:
        return
    StuffDone["6_1"] = 250
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(40,37))
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(40,38))
    MessageBox("You nervously step into the Zaskiva School of Magery. You\'ve heard nasty rumors regarding trouble at other Schools of Magery in Valorim, and are on your guard.\n\nThe place is dusty and quiet. You doubt school is in session - you only see one mage, sitting and reading at the far end of the room.")

def Zaskiva_61_MapTrigger_35_33(p):
    if StuffDone["6_2"] == 250:
        return
    StuffDone["6_2"] = 250
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(35,33))
    MessageBox("This is a small laboratory, well equipped for simple magical and alchemical experiments. You notice that an alcove in the southeast corner of the room has been sealed off.")

def Zaskiva_62_MapTrigger_31_34(p):
    if StuffDone["6_3"] == 250:
        return
    StuffDone["6_3"] = 250
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(31,34))
    MessageBox("This is a dusty lecture hall. The mages in your party have unpleasant flashbacks of years of grueling, mind numbing study in rooms just like this one.")

def Zaskiva_63_MapTrigger_43_33(p):
    if StuffDone["6_4"] == 250:
        return
    StuffDone["6_4"] = 250
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(43,33))
    MessageBox("This is a small shrine. There\'s no priest here. It\'s a quiet, mildly holy place, like many others across the Empire, where soldiers and sailors can stop, leave a few coins, and say a few prayers for luck in the travels ahead.\n\nIt\'s a pity there\'s no attendant here ... the floor could use a seriously good mopping.")

def Zaskiva_64_MapTrigger_44_16(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You stumble in on a half dozen heavily armed men and women, talking and planning. When they see you, they freeze, alarmed. At first, you think they\'re about to attack you. Then they recognize you.\n\n\"What do you think you\'re doing?\" one of them hisses. \"Go about your mission, and don\'t come back here. You\'ll bring the Empire down upon us all!\" A woman in plate armor gets up and pushes you back out through the door.")
    Town.AlterTerrain(Location(44,16), 0, TerrainRecord.UnderlayList[128])

def Zaskiva_65_MapTrigger_42_8(p):
    MessageBox("You find a small, concealed room, containing mops, brooms, and other powerful tools of cleaning. As you look around, a streetsweeper comes in, seizes a broom of formidable might, and walks out again.")

def Zaskiva_67_MapTrigger_42_24(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This room is packed with merchants, who are bunking together while waiting for permission to leave Zaskiva. They don\'t want to talk to you, and don\'t appreciate your intrusion. They push you out.")

def Zaskiva_68_MapTrigger_37_20(p):
    MessageBox("Right behind the concealed passage, you find a massive door, reinforced with steel bands. The words \"TO SEWERS - KEEP OUT\" are painted on it in big, red letters.")

def Zaskiva_70_MapTrigger_34_12(p):
    if StuffDone["6_5"] == 250:
        return
    StuffDone["6_5"] = 250
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(34,12))
    ChoiceBox("You enter a solemn memorial to former lords of Morrow\'s Isle. There are three statues in here. the two on the right aren\'t that nice, only carved out of granite. The statue to the left, of Lord Volpe, is carved out of beautiful white marble.", eDialogPic.TERRAIN, 133, ["OK"])

def Zaskiva_71_MapTrigger_33_8(p):
    if SpecialItem.PartyHas("OakBox"):
        result = ChoiceBox("Having found the marble statue, you look around for the hole in the wall you\'re supposed to put the box into. The instructions you\'ve received were wrong. The crack isn\'t behind the statue, but off to the side.\n\nA brick has been removed from the wall of Lord Volpe\'s palace, leaving a hole just big enough to fit the oak box inside. This mission is almost complete. Do you insert the box?", eDialogPic.TERRAIN, 107, ["Leave", "Insert"])
        if result == 1:
            ChoiceBox("You slide the box into the hole, turn around, and find yourself face to face with 20 Empire soldiers, five of them Empire dervishes. Their weapons are drawn.\n\nTheir commander smirks, and says \"Well, well. The attempt on Volpe\'s life has come at last. You fools could not have been more obvious in your attempt. We\'ve been following you even since you arrived here.\"\n\n\"Trying to blow up Volpe\'s mansion was an intriguing plan, but you must have been insane to think you can outwit ...\"\n\nThat\'s all he manages to say, before the whole world falls apart.", eDialogPic.CREATURE, 17, ["OK"])
            Animation_Explosion(Location(30,10), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Animation_Explosion(Location(32,7), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Animation_Explosion(Location(32,11), 0, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("The explosion didn\'t come from the box you delivered. It came from the front of Lord Volpe\'s palace. The commander shouts \"It\'s a decoy! Damn them!\" The soldiers try to run back out, but they don\'t make it.\n\nThere are two more explosions, both from the front of the palace. The Hill Runner\'s magical devices are more powerful than you would have expected. You see the palace walls start to shake and buckle.\n\nYou try to get away from the collapsing palace, but you don\'t get far. The whole place caves in, almost on top of you.", eDialogPic.STANDARD, 17, ["OK"])
            Party.Damage(Maths.Rand(8, 1, 8) + 4, eDamageType.WEAPON)
            Wait()
            ChoiceBox("Dazed, you stagger through the wreckage and rubble. Kenny, the statue caretaker, was crushed under a falling pillar. Casualties are all around you, and not all of them are soldiers. Moans of pain come from all directions. The palace has been destroyed.\n\nYou stagger through the dust, barely able to keep standing. You are dimly aware of guards searching the area, looking for people to arrest for this heinous crime. They\'re getting close to you.\n\nBefore you can think of trying to get away (or even think of anything coherent), rough hands grab you. Someone whispers \"Come with us, quick!\" You\'re in no position to refuse.\n\nThey hustle you across the corridor, through a secret door, and down a passage. As you\'re pushed down a flight of stairs, one of them says \"Make your way through here, and we\'ll get you on the other end. Good work, rebels.\"\n\nThe effects of the blast start to fade, and your ears stop ringing. Little by little, you return to your senses. When you are fully aware, however, you realize you\'re not in Zaskiva anymore.\n\nYou\'re in a crumbling room underground. And a portcullis has just been slammed shut behind you, blocking your retreat.", eDialogPic.TERRAIN, 107, ["OK"])
            SpecialItem.Take("OakBox")
            StuffDone["101_0"] = 1
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(1,23)
            Party.MoveToMap(TownMap.List["ZaskivaSewers_9"])
            return
        return
    MessageBox("You notice, off to one side of the marble statue, that a small stone has been removed from the wall of Lord Volpe\'s palace. Maybe someone should come here and fix that.")

def Zaskiva_72_MapTrigger_6_10(p):
    if StuffDone["6_6"] == 250:
        return
    StuffDone["6_6"] = 250
    TownMap.List["Zaskiva_6"].DeactivateTrigger(Location(6,10))
    MessageBox("These are the Zaskiva docks. Not many boats are coming and going. The island has been pretty well closed up by the cautious leaders of Morrow\'s Isle.")

def Zaskiva_73_OnEntry(p):
    if StuffDone["101_0"] >= 1:
        MessageBox("You return to the city of Zaskiva, which is still reeling from the effects of the explosion. One such effect is bands of uncontrolled guards roaming the streets, carrying out a vigilante \"investigation\" of the crime.\n\nThey recognize you from a description gotten from a bystander at the explosion, and take you in for harsh questioning. By the time Jaen finds you, the questioning has gotten a bit out of hand. Fatally so.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return
    if StuffDone["6_0"] == 250:
        return
    StuffDone["6_0"] = 250
    MessageBox("You enter the city of Zaskiva for the first time. It\'s a beautiful city, clean and prosperous, and relatively new. It was, in fact, only built in the last ten or so years, with construction starting when Lord Volpe arrived here.\n\nThe city is beautiful, but the people are haggard. The streets are crowded with edgy merchants and sailors, held up here because of Lord Volpe\'s restrictions on traffic to and from here. It\'s a hectic place, reeking of stress and fear.")

def Zaskiva_74_TalkingTrigger4(p):
    if StuffDone["0_6"] >= 1:
        p.TalkingText = "He laughs. \"What can I say? Love makes one greedy! One letter isn\'t enough. I will always want more, and more, until I can finally see her again.\""
        return
    if SpecialItem.PartyHas("LetterforZulli"):
        p.TalkingText = "You give Madeleine\'s letter to Zulli. He lifts the visor of his helmet to look at it. You\'ve obviously made his day. \"This is wonderful! Thank you!\" As a reward, he doesn\'t forget to give you 10 gold.\n\nYou\'ve done a very good deed."
        SpecialItem.Take("LetterforZulli")
        StuffDone["0_6"] = 1
        Party.Gold += 10
        for pc in Party.EachAlivePC():
            pc.AwardXP(5)
        return

def Talking_6_22(p):
    if Town.ID == "Zaskiva_6":
        p.TalkingText = "\"Yes. I\'d gladly be somewhere else, but they won\'t let me leave. The movements of all mages are tightly controlled.\""
    else:
        p.TalkingText = "\"Yes. Boy, was I ever glad to get out of there. Fortunately, someone took care of Volpe once and for all. Buzzard is a lot easier to live in.\""

def Talking_6_23(p):
    if Town.ID == "Zaskiva_6":
        p.TalkingText = "She smiles ironically. \"A great man. A model of behavior for us all.\""
    else:
        p.TalkingText = "\"I\'m not going to pretend to like the man. I\'m glad he\'s dead.\""

def Talking_6_24(p):
    if Town.ID == "Zaskiva_6":
        p.TalkingText = "\"It\'s closed for business. I was just left here to look after it. All mages capable of serving in any capacity were press ganged to fight the rebels. The ones who didn\'t join the rebels, that is. Apprentices on the front lines. Ridiculous.\""
    else:
        p.TalkingText = "\"It\'s closed for business, probably permanently now. All mages capable of serving in any capacity were press ganged to fight the rebels, and the empty school was heavily damaged by the explosion in Zaskiva, the one that killed Volpe.\""

def Talking_6_32(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "You give her a few gold. Her face lights up. \"Thank you so much! What a good omen! Lord Volpe will see me soon for sure!\""
    else:
        p.TalkingText = "She looks at your empty purse. \"No, never mind. You\'re worse off than me.\""

def Talking_6_37(p):
    if Party.Gold < 2:
        p.TalkingText = "You don\'t have the gold."
    else:
        Party.Gold -= 2
        Party.Pos = Location(5, 42)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "She points at the door to the filthy, overcrowded common room. \"Over there.\" You go, force people to give you room, and spend the longest night you\'ve ever spent."
        CentreView(Party.Pos, False)

def Talking_6_39(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "You buy some ridiculously watered down ale. \"Sorry it\'s a bit weak,\" Helena says. \"Can\'t get new supplies. Everything\'s blockaded.\""
    else:
        p.TalkingText = "You don\'t have the gold."
