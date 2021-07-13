
def Zenith_505_MapTrigger_40_34(p):
    if StuffDone["9_0"] >= 1:
        Town.PlaceEncounterGroup(1)
        if StuffDone["8_7"] == 250:
            return
        StuffDone["8_7"] = 250
        MessageBox("You enter the Red Dragon Inn. The place is quite lively, with plenty of drinking and conversation. You hear a whisper in the back of your head. \"Go to the southwest room.\" You turn around to see nobody.")
        return

def Zenith_506_MapTrigger_31_6(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,56)
    Party.MoveToMap(TownMap.List["ZenithKeep_29"])

def Zenith_509_MapTrigger_32_7(p):
    if StuffDone["9_0"] >= 3:
        if StuffDone["9_0"] < 7:
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("You had once already almost been killed within here. You doubt that anyone would rescue you if you were to enter again.")
            return
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(32,56)
        Party.MoveToMap(TownMap.List["ZenithKeep_30"])
        return
    if StuffDone["9_0"] < 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The guards stop you from entering Zenith Keep. You are clearly not welcome here.")
        return

def Zenith_512_MapTrigger_30_41(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["9_0"] == 3:
        if StuffDone["9_5"] == 250:
            return
        StuffDone["9_5"] = 250
        ChoiceBox("You enter Vale\'s room. He is inside filling out paper he looks up, shocked to see you. \"Oh my! How did you?\" You explain Cylene\'s rescue to him. He nods. \"Indeed, this is a significant improvement in status. You have even learned what we wanted to know.\"\n\nHe begins to think. \"Well, our next course of action is clear. We must send you to Mount Bleak to rescue Raiden. I will see that your status of Imperial Guardian is restored. Secretly, of course.\"\n\nHe reaches into a large sack and pulls out a map. He points to a large mountain on the northern shore just north of Zenith. \"That is where Raiden is being held captive. The best way to begin the assent is right there.\" You take note of the location.\n\n\"We must hurry. It is certain that Auspire will soon find out that you have escaped and she may begin to suspect the Empire. This could force her to kill Raiden, which would seriously set back our operations.\"\n\n\"Go to Mount Bleak (It is north of Zenith) and rescue Raiden. I would like to speak with him, so bring him here. Understood?\"", eDialogPic.STANDARD, 29, ["OK"])
        TownMap.List["MountBleak_31"].Hidden = False
        return
    if StuffDone["12_4"] >= 2:
        if StuffDone["13_4"] == 250:
            return
        StuffDone["13_4"] = 250
        ChoiceBox("You return to find Vale very furious. He begins shouting as soon as you enter. \"Do you really have any idea what you have done!? You\'ve just made me into one of the worst mass murderers of all time!\n\nWhen I said get the Onyx Scepter, I did not mean that unconditionally. Perhaps we could have devised an alternative. I mean, did you really have to go about causing the deaths of thousands of people.\n\nI would not be surprised if they don\'t charge us or something! You better have a good explanation!\" You do your best to explain your situation to him. It appears to calm him down somewhat.\n\nAfter a long pause and a half-bottle of beer, he continues, \"Well, you had better put that Onyx Scepter to good use. Go to Fort Nether once all of your preparations are complete.\"", eDialogPic.CREATURE, 23, ["OK"])
        return

def Zenith_516_MapTrigger_33_30(p):
    if StuffDone["48_5"] == 250:
        return
    StuffDone["48_5"] = 250
    TownMap.List["Zenith_28"].DeactivateTrigger(Location(33,30))
    Town.PlaceEncounterGroup(2)

def Zenith_517_MapTrigger_11_54(p):
    if StuffDone["9_0"] == 3:
        if StuffDone["48_7"] == 250:
            return
        StuffDone["48_7"] = 250
        ChoiceBox("It appears you have managed to dodge the gallows once again. However, you may not be out of the woods yet. It will not be too long before Auspire and her cronies realize you have escaped.\n\nThere will surely be some sort of search for you. However, for now you are in the clear. You can probably stay safe if you keep a low profile for a while. Now you should report back to Agent Vale.", eDialogPic.STANDARD, 1024, ["OK"])
        return

def Zenith_521_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(25, 36),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(29, 40),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(33, 36),WorldMap.SectorAt(Party.OutsidePos))

def Zenith_522_CreatureDeath47(p):
    MessageBox("You hear a horrible scream from the cell to the south. Then there is silence. It is an unmistakable sound of someone being killed. These punishment cells are a grim place.")

def Zenith_523_TalkingTrigger0(p):
    if StuffDone["9_0"] >= 4:
        if StuffDone["9_0"] >= 6:
            p.TalkingText = "\"You are to: Speak with Dervish Montcalm and find out what he has to say. Find out anything you can about the Onyx Scepter at the Imperial Library. Then, go to Fort Nether and destroy the Nethergate.\""
            return
        if StuffDone["9_0"] < 5:
            StuffDone["9_0"] = 5
            SpecialItem.Take("RaidenNPC")
            TownMap.List["BalkisEstate_32"].Hidden = False
            TownMap.List["FortNether_34"].Hidden = False
            ChoiceBox("You return to Vale. He immediately begins to interview Raiden. \"I am glad to see our Guardians managed to bring you back safely. We have little time to lose. What have you discovered about the Nethergate?\" inquires Vale.\n\n\"I know its location and its creators. The portal has been constructed in a place called Fort Nether. Do you have a map?\" Vale nods and produces one. Raiden points out a group of cliffs on the western shore. \"There you shall find it.\"\n\n\"But I must warn you that it is well guarded and its creators powerful.\" Vale interjects. \"Who are the creators?\" Raiden replies, \"As I was just about to say. A sorcerer named Balkis and his apprentice named Zaine.\"\n\nZaine! You remember the conflict you had with him in the Agran Sector. You share your knowledge. Vale thinks for a while. \"It appears these two have greater interests in seeing the Empire fall. I detect something much deeper.\n\nHowever, that is only speculation. After all, it may be a different Zaine we are referring to.\" You agree. Raiden begins again, \"They own an estate not far south of this city deep in the forest, it may be worthwhile to check it out.\"\n\nVale replies. \"Agreed Raiden, you have been of great assistance.\" Four Elite Guardians appear and escort Vale away. \"Fear not, the Empire shall keep you safe.\" With Raiden gone, Vale turns to you.", eDialogPic.CREATURE, 27, ["OK"])
            ChoiceBox("\"So Guardians, the task at hand is clear. Your mission now becomes the destruction of the Nethergate. Although we know its location, we know little about it. I believe vital information lies in Balkis\'s Estate.\n\nIf you can find any notes or something on the Nethergate, it may give us clues how to destroy it. I would not advise going directly to Fort Nether as we do not know exactly what we\'re up against.\n\nI will speak with my superiors and try to get any information I can from them. Well, it looks like the fate of the Emperor\'s throne lies on us.\"", eDialogPic.STANDARD, 22, ["OK"])
            if StuffDone["12_0"] >= 1:
                StuffDone["9_0"] = 6
                ChoiceBox("You return to Vale with the information on the Nethergate. \"Well, that may provide some problems. I\'ve never heard of an \'Onyx Scepter\' before. However, the Imperial Library has a book of artifacts with locations of many of them.\n\nYou may wish to check that out. We are pleased that you managed to execute one of the traitors, Zaine. Too bad you could not get that Balkis guy also.\" You also confirm Zaine\'s connection to the cult in Agran.\n\nHe shrugs. \"I really can\'t tell you much about that. All that matters now is he is gone. We shall deal with this Morbane matter at a later time. The destruction of the Nethergate before Auspire can amass a powerful army is our top priority!\n\nAnyway, I have some good news. Remember Dervish Montcalm back in the Aizic Sector? Well, it turns out that he and that Balkis guy go way back. He has even agreed to help us by doing some scry work of Fort Nether.\n\nYou should probably check out what he has accomplished. His help may be vital to the completion of this mission. Oh, and as for the Onyx Scepter, return here when you find out anything about it. I\'ll ask our wizards if they can generate an alternative.\n\nJust in case one is unavailable. Well, we had better get started.\"", eDialogPic.STANDARD, 22, ["OK"])
                p.TalkingText = "\"You are to: Speak with Dervish Montcalm and find out what he has to say. Find out anything you can about the Onyx Scepter at the Imperial Library. Then, go to Fort Nether and destroy the Nethergate.\""
                return
            p.TalkingText = "\"Return here with any information on the Nethergate you can find.\""
            return
        if StuffDone["12_0"] >= 1:
            StuffDone["9_0"] = 6
            ChoiceBox("You return to Vale with the information on the Nethergate. \"Well, that may provide some problems. I\'ve never heard of an \'Onyx Scepter\' before. However, the Imperial Library has a book of artifacts with locations of many of them.\n\nYou may wish to check that out. We are pleased that you managed to execute one of the traitors, Zaine. Too bad you could not get that Balkis guy also.\" You also confirm Zaine\'s connection to the cult in Agran.\n\nHe shrugs. \"I really can\'t tell you much about that. All that matters now is he is gone. We shall deal with this Morbane matter at a later time. The destruction of the Nethergate before Auspire can amass a powerful army is our top priority!\n\nAnyway, I have some good news. Remember Dervish Montcalm back in the Aizic Sector? Well, it turns out that he and that Balkis guy go way back. He has even agreed to help us by doing some scry work of Fort Nether.\n\nYou should probably check out what he has accomplished. His help may be vital to the completion of this mission. Oh, and as for the Onyx Scepter, return here when you find out anything about it. I\'ll ask our wizards if they can generate an alternative.\n\nJust in case one is unavailable. Well, we had better get started.\"", eDialogPic.STANDARD, 22, ["OK"])
            p.TalkingText = "\"You are to: Speak with Dervish Montcalm and find out what he has to say. Find out anything you can about the Onyx Scepter at the Imperial Library. Then, go to Fort Nether and destroy the Nethergate.\""
            return
        p.TalkingText = "\"Return here with any information on the Nethergate you can find.\""
        return
    if StuffDone["9_0"] < 3:
        StuffDone["9_0"] = 2
        ChoiceBox("He takes no time to get to the heart of the matter. \"Okay, Guardians. Here is what we\'re up against. The ruling oligarchy, the Odin, is a large order of magi. They are led by a powerful sorceress named Auspire.\n\nThe Odin secretly believe they are the true rulers of the Empire. Many centuries ago, the order sat upon the throne for about seventy years. However, they were forced to abdicate after a power struggle and passed down their hatred to their descendants.\n\nTo accomplish the takeover, they are building a large portal called a Nethergate. This will allow them to summon armies of powerful creatures from other dimensions. Should this be completed, they would have little trouble taking the throne.\n\nUnfortunately, we have established no direct link to the Odin. The family has powerful political influences -- which is one of the reasons we cannot use the army. We believe Auspire has hired some third party to construct the portal.\n\nWe don\'t know who has been hired or where the portal is. Our best lead was a wizard named Raiden, a member of the Odin but loyal to the Empire. Unfortunately, his betrayal was discovered. We know he is alive and imprisoned somewhere.\n\nWe know this information can be obtained within their Hall of Records. However, Auspire just won\'t give up their secret documents to us. Our past attempts have failed, so we\'re giving you a shot.\"", eDialogPic.CREATURE, 21, ["OK"])
        ChoiceBox("\"Our agent has already taken the liberty of placing you on Zenith Keep\'s \'Guest Registry\'. So you shall be able to enter the Keep. Unfortunately, there are many well-guarded restricted areas  you cannot enter -- the Records Hall is one.\n\nOur agent in the Keep is named Fione. You should speak with her first as she may have some useful information for you. In addition, I have convinced the Imperial Magical Learning Bureau to let you learn the spell \'Dispel Barrier\'.\n\nI suggest you return to Solaria now, and go to the Imperial Library. Ask the librarian about the spell and you will be directed to the appropriate volume. It is quite likely you will run up against several magical barriers on this mission.\n\nThis mission must be done discretely! There must be no violence, period. We must ensure that the Odin remain unaware of our intentions. Should you be captured, the Empire will have no choice but to disavow knowledge of this mission.\n\nTo summarize: First, get the \'Dispel Barrier\' spell at the Imperial Library. Secondly, enter the Keep and speak with Fione. Then, do whatever you need to do to find out where they are holding Raiden, so he may be rescued.\n\nBut at no time, may you use violence or be discovered. Return here with the required information.\"", eDialogPic.CREATURE, 21, ["OK"])
        p.TalkingText = "\"You must sneak into the Records Hall in Zenith Keep undetected. This will be a difficult feat, but we have faith in you. Once in, find out where Raiden is imprisoned. Now go.\""
        return
    p.TalkingText = "\"Go to Mount Bleak (It is north of Zenith) and rescue Raiden. I would like to speak with him, so bring him here. Understood?\""

def Zenith_524_TalkingTrigger1(p):
    if StuffDone["9_0"] == 6:
        if StuffDone["12_2"] >= 2:
            if StuffDone["12_2"] < 3:
                p.TalkingText = "\"Go to the Spire of Urlak-Nai and recover the Onyx Scepter. It is located on an isle in the northeastern corner of the Imperial Sector. Good luck!\""
                StuffDone["12_2"] = 2
                return
            p.TalkingText = "\"After the cost of getting that, you had better put it to excellent use.\""
            return
        if StuffDone["12_2"] < 1:
            p.TalkingText = "\"Information on the Onyx Scepter can be found in the Imperial Library. I really don\'t know much about it.\""
            return
        ChoiceBox("You tell Vale about what you learned. \"Well, it looks like we only have one option. I have spoken with our greatest magi, and they are doubtful that they can duplicate the effects of an Onyx Scepter. So, it looks like we will have to produce one.\n\nCombing every rock in Avernum is out of the question. Although I don\'t like it, we are going to have to break into Urlak-Nai and steal their valuable scepter. Really never liked that place. Went their once, and I hated those arrogant priests.\n\nI suppose you should know the history. Back when the Empire first started up, it made an alliance with the Order of Urlak-Nai. The stipulations were so the order could maintain its sovereignty at the expense of its priests joining the military.\n\nFor a majority of the Imperial rule, most of the priests in the Empire army came from the order. It was only in the last couple centuries that the powers of the Empire started to look down upon their barbaric practices.\n\nWell, after the Empire began to train its own priests in academies, the two nations (for lack of a better term) split off communications. From then on, contact between the two has been minimal.\n\nSince the Urlak-Nai is essentially separate from the Empire, we cannot compel them to give up their artifact and I doubt the officials will agree to an invasion. So it falls on you to go their and steal the Onyx Scepter.\"", eDialogPic.CREATURE, 24, ["OK"])
        TownMap.List["UrlakNai_33"].Hidden = False
        p.TalkingText = "\"Go to the Spire of Urlak-Nai and recover the Onyx Scepter. It is located on an isle in the northeastern corner of the Imperial Sector. Good luck!\""
        StuffDone["12_2"] = 2
        return
def Talking_28_4(p):
    Town.NPCList.Remove(p.NPCTarget)
    if p.NPCTarget.Start.LifeVariable != "":
        StuffDone[p.NPCTarget.Start.LifeVariable] = 1
    p.TalkingText = "\"I\'m referring to Captain Norn. He\'s in charge of punishments and stuff. Have to report on the last peon. Excuse me, my shift is over.\" He walks away and speaks with the captain for a short time. The two nod and the soldier departs."

def Talking_28_36(p):
    if Party.Gold >= 3:
        Party.Gold -= 3
        p.TalkingText = "She pours you each a glass of milk. It is cold and refreshing. \"I see you are not from around here. Let me give you a bit of advice.\""
    else:
        p.TalkingText = "You cannot afford it."

def Talking_28_40(p):
    if Party.Gold < 30:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 30
        Party.Pos = Location(35, 44)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "She takes your gold and leads you to your room. You have a fairly pleasant night\'s rest."
        CentreView(Party.Pos, False)
