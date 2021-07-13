
def Gynai_1270_MapTrigger_10_31(p):
    if StuffDone["48_8"] == 250:
        return
    StuffDone["48_8"] = 250
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(10,31))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(10,32))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(10,33))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(53,31))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(53,32))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(53,33))
    ChoiceBox("You are now inside the legendary city of Gynai. One glance reveals the different nature of this place. All of the buildings are made of a special stone. The stone is shaped into impossible artistic, random, and bubblous patterns.\n\nThe walls have no bricks. It is almost as if the stone here was grown into the curved irregular shapes. It is quite unusual, but has an odd abstract artistic feel to it. It feels so chaotic, but yet so amazing.\n\nYou do not believe the Empire\'s mages could accomplish these feats. You have heard other rumors about Gynai in this respect. They say that the civilization is much more advanced than the Empire.\n\nThe sole reason the Empire could never challenge Gynai was because of their superior magic and technology. Of course, those are just rumors. You really don\'t know what level of technology these people have.\n\nPerhaps they may be able to do a few simple things, such as growing stone, better than the Empire, as evident here. The other strange aspect is the clothing. All of the people wear these strange glowing robes.\n\nThe robes seem to be made of a pressed fungus, quite odd. You are sure that this is only the beginning of your amazement.", eDialogPic.TERRAIN, 168, ["OK"])

def Gynai_1276_MapTrigger_31_31(p):
    if StuffDone["48_9"] == 250:
        return
    StuffDone["48_9"] = 250
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(31,31))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(32,31))
    TownMap.List["Gynai_54"].DeactivateTrigger(Location(33,31))
    ChoiceBox("You stand at the entrance of the second largest building in the city. The first is across the large pool to the north. However, this one seems quite important. People pass in and out at a constant rate. You are guessing this is some kind of city hall.\n\nThe structure, like every other one, is very irregular and like bubbling stone. However, this one is more impressive as the design is like a symphony of stone bubbles. Bubble upon bubble are placed upon each other in random layers.\n\nYou can bet that in each series of bubbles lies some sort of functionary of the city. The levels twist in all sorts of impossible ways. You wonder how each area is accessible, but from the unusual architecture they are somehow connected.\n\nYet another wondrous feat of Gynai.", eDialogPic.TERRAIN, 237, ["OK"])

def Gynai_1279_MapTrigger_33_38(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["49_0"] >= 2:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(30,46))
        p.CancelAction = True
        Animation_Hold(-1, 058_opendoor)
        Wait()
        if StuffDone["49_1"] == 250:
            return
        StuffDone["49_1"] = 250
        ChoiceBox("You open the door and immediately find your destination on the other side. You look around for any indication of other hallways, but find none. The only doors in this other room are the ones behind you.\n\nWhere are all the other offices and facilities? More importantly, where did all the people that were passing in and out of those doors end up? You look around and only see one man, who you have not seen earlier.\n\nThere is some really suspicious magic going on here, unlike any you have ever seen. Not only can Gynai shape stone, they can also warp reality! You wonder what the true extent of their powers are.", eDialogPic.TERRAIN, 103, ["OK"])
        return
    if StuffDone["49_0"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("This door stays firmly shut.")
        return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(33,41))
    p.CancelAction = True
    Animation_Hold(-1, 058_opendoor)
    Wait()
    if StuffDone["49_1"] == 250:
        return
    StuffDone["49_1"] = 250
    ChoiceBox("You open the door and immediately find your destination on the other side. You look around for any indication of other hallways, but find none. The only doors in this other room are the ones behind you.\n\nWhere are all the other offices and facilities? More importantly, where did all the people that were passing in and out of those doors end up? You look around and only see one man, who you have not seen earlier.\n\nThere is some really suspicious magic going on here, unlike any you have ever seen. Not only can Gynai shape stone, they can also warp reality! You wonder what the true extent of their powers are.", eDialogPic.TERRAIN, 103, ["OK"])

def Gynai_1281_MapTrigger_33_40(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(33,37))
    p.CancelAction = True
    Animation_Hold(-1, 058_opendoor)
    Wait()
    if StuffDone["49_1"] == 250:
        return
    StuffDone["49_1"] = 250
    ChoiceBox("You open the door and immediately find your destination on the other side. You look around for any indication of other hallways, but find none. The only doors in this other room are the ones behind you.\n\nWhere are all the other offices and facilities? More importantly, where did all the people that were passing in and out of those doors end up? You look around and only see one man, who you have not seen earlier.\n\nThere is some really suspicious magic going on here, unlike any you have ever seen. Not only can Gynai shape stone, they can also warp reality! You wonder what the true extent of their powers are.", eDialogPic.TERRAIN, 103, ["OK"])

def Gynai_1285_MapTrigger_51_6(p):
    if StuffDone["49_2"] == 5:
        StuffDone["49_2"] = 6
        Town.PlaceEncounterGroup(1)
        SpecialItem.Take("ArcturusNPC")
        Message("Arcturus leaves the party.")
        ChoiceBox("Arcturus suddenly stays behind. \"I believe I have taken you far enough. I have done what I can to help you so this is where we must part. Behind these doors will lead to a stairway which will lead into the sanctuary.\"\n\nYou ask if it will look suspicious if he leaves the library alone. \"Not at all, I\'ll just wait in here for a while. When I leave, I\'ll just tell the attendant that I sent you guys on an errand into the Sanctuary.\n\nJust remember, please don\'t cause any trouble. I do not know what you need from the Sanctuary, but you must not mention to anyone that I helped you get in here! Is that understood?\"\n\nYou assure him that you will not mention his name to anyone. He smiles. \"Well now, time is wasting, I suppose you should get in the Sanctuary while nobody is watching.\"", eDialogPic.CREATURE, 1027, ["OK"])
        return

def Gynai_1287_MapTrigger_42_13(p):
    if StuffDone["49_2"] == 6:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Leaving the library now would not be a good idea. You doubt that you will be able to get back in without Arcturus\' help.")
        return

def Gynai_1289_MapTrigger_4_31(p):
    if SpecialItem.PartyHas("ArcturusNPC"):
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Arcturus shouts out, \"Wait a minute. This is not the way to the library. We want to be in the northeast section of the city. Did you think I was going on some great adventure or something?\"")
        return

def Gynai_1295_MapTrigger_55_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(60,61)
    Party.MoveToMap(TownMap.List["Sanctuary_55"])

def Gynai_1297_TownTimer_0(p):
    SuspendMapUpdate()
    for x in range(25, 27):
        for y in range(44, 45):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
    ResumeMapUpdate()
    for x in range(33, 36):
        for y in range(51, 54):
            if Maths.Rand(1,0,100) <= 90:
                Town.PlaceField(Location(x,y), Field.BLADE_WALL)

def Gynai_1298_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(21, 14),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(30, 14),WorldMap.SectorAt(Party.OutsidePos))

def Gynai_1299_TalkingTrigger0(p):
    if StuffDone["100_0"] == 6:
        for x in range(8, 9):
            for y in range(31, 34):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[148])
        p.TalkingText = "\"I will need to see your pass.\" You show him your identification. He pulls the levers and the gates silently slide open."
        for x in range(55, 56):
            for y in range(31, 34):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[148])
        return

def Gynai_1300_TalkingTrigger5(p):
    StuffDone["49_0"] = 1

def Gynai_1301_TalkingTrigger6(p):
    StuffDone["49_0"] = 2

def Gynai_1302_TalkingTrigger7(p):
    ChoiceBox("You explain that you have recently discovered some hidden mysterious machinery within the Empire that the Prime Director believes to have been engineered here in Gynai. You explain the design from memory as best you can.\n\nHe thinks for a bit. \"As you may know, our treaty signed long ago forbids us to interfere with the Empire. In our long history we have honored this treaty. I can assure you that our government has nothing to do with this machine.\n\nOf course from the sounds of the design, it seems suspiciously like something that our engineers could create. However, I am not an engineer so I cannot give a real informed opinion on the matter.\"\n\nYou ask if the term \'dark metal\' sounds familiar to him. He raises an eyebrow seeming quite surprised at the mention. He phrases his response. \"I really cannot say I know all that much about this dark metal.\n\nI have heard our engineers mention it periodically, though. I\'m guessing they use it for some of their machines. If you want to know more on that, you should speak with the Elder of Engineering and Research.\n\nHowever, I can assure you that our government has not constructed any machines outside of our territory for any purpose. Any further questions?\"", eDialogPic.STANDARD, 1026, ["OK"])

def Gynai_1303_TalkingTrigger9(p):
    ChoiceBox("You describe the strange machine you found in Morbane\'s lair to her in great detail. She listens intently, asking you several probing questions along the way. In the end, she believes she has a pretty good idea of what you are trying to explain.\n\nShe places her hand on her chin and begins to speak, \"Indeed, this does sound like something we could produce. The molded stone and the large flawlessly grown crystals are definitely things we specialize in.\n\nAdditionally, the mental crystal controls are something that we use in place of consoles on our machines. It takes much discipline to interface, but once one masters the technique, the possibilities are limitless.\n\nHowever, the holistic design of the machine is beyond me. I would have to analyze it myself to determine its purpose. Your description does not match any of the recent or past projects we have worked on.\n\nIn fact, I am clueless as to the machine\'s function. I shall need to know more.\"", eDialogPic.STANDARD, 1026, ["OK"])

def Gynai_1304_TalkingTrigger10(p):
    ChoiceBox("Her eyes widen at the mention of the metal. \"Dark metal is a class of metal named after the way it is hazardous to health. Common metals in the class are Uranium, Thorium, Iridium, and other such metals.\n\nThese metals have a tendency to decay. When this decay occurs, energy is released that is harmful to ones health. We call this effect radiation and all dark metals are considered to be radioactive by definition.\n\nAlthough dark metal is not always malevolent. We have managed to harness this radioactive effect and use it to treat diseases. It is just prolonged exposure can cause problems.\n\nThere is also the possibility that these metals could be utilized for creation of large quantities of energy. We believe what is causing these metals to decay can be accelerated to a rate where large quantities of energy could be produced.\n\nHowever, our engineers are perplexed at how to make this theory a practice. We know that this can be done, we just do not understand the methods that are employed in doing this.\n\nPerhaps this machine of yours is some device to utilize this energy in some way. Of course, I can only speculate. That is the only real use I can think of for dark metal.\"", eDialogPic.STANDARD, 1026, ["OK"])

def Gynai_1305_TalkingTrigger14(p):
    if Party.Gold >= 500:
        Party.Gold -= 500
        ChoiceBox("You pay the gold and she dims the lights using magic. She begins to tell the tale. \"A long time ago a race of beings came down from the stars. They brought with them many gifts.\n\nHowever, Humans and Nephilim were not ready for these gifts at the time. They used them to make violent war and settle petty difference. Both races were at the brink of annihilating each other when the visitors decided it was enough.\n\nThey realized that the inhabitants were yet not ready to behold such power and took them away. However, there was one group of humans who saw the possibility in these gifts.\n\nThey did not want to make war, but use the gifts to improve the world. The visitors realized this. They also realized that their pacifistic nature would not allow their survival on this hostile world.\n\nSo they made the greatest gift of all, they took the soul of one of their greatest and made it into a living crystal. This crystal remained when the visitors departed and has guided us ever since.\n\nThey have given us the secrets back so we can defend ourselves from the barbarians. It was through the wisdom of this mighty being that we are able to sustain ourselves until today.\"", eDialogPic.CREATURE, 124, ["OK"])
        ChoiceBox("You ask what happened to the crystal. \"Nothing has happened to the crystal! It remains at the apex of the Sanctuary in a special shrine called the Aerie. Only the Archelder is allowed to access this place to speak with the crystal.\n\nIn fact, the crystal knows all. I sense you are here on a mission of great importance. I am sure the crystal could answer your questions. It will tell you just about anything you could want to know.\"\n\nYou ask how could you see this crystal. She grins. \"I am afraid that this will not be easy. The crystal is the most well protected secret of our society that only a few of the highest elders know of its existence.\n\nThe problem will be getting into the Sanctuary. You are not one of us, so you shall not be allowed in. Yet, it may be possible to convince one of the less dedicated elders to use his or her influence to sneak you inside.\n\nHowever, not I nor even the elders are allowed access to the Aerie. Only the Archelder is allowed within those holy chambers. Getting there will require the most resourcefulness and I cannot help you anymore.\"", eDialogPic.CREATURE, 124, ["OK"])
        return
    p.TalkingText = "\"I am sorry, but these are secrets of my people. I will not divulge them for anything less.\""

def Gynai_1306_TalkingTrigger19(p):
    if StuffDone["49_2"] >= 3:
        p.TalkingText = "\"The journal is proving very useful. Did you think of something that you would like as a reward yet?\""
        return
    if StuffDone["49_2"] < 2:
        StuffDone["49_2"] = 1
        return
    StuffDone["49_2"] = 3
    p.TalkingText = "You hand him the old journal. He grins. \"I hope this will prove useful to my research. Now, we must come up with some kind of reward for doing this little errand for me. Do you have any suggestions?\""
    SpecialItem.Take("KiveksJournal")

def Gynai_1307_TalkingTrigger22(p):
    if StuffDone["49_2"] >= 4:
        p.TalkingText = "\"All right, shall we get going?\""
        return
    if StuffDone["49_2"] < 3:
        return
    result = ChoiceBox("\"You want to get into the Sanctuary? That will be really difficult to do you realize. The security around the gates is really tight, I\'m sure they could pick you out as outsiders instantly. I would be in a lot of trouble too.\n\nHowever, it is possible to enter the Sanctuary from the library. They built access to the library for convenience. Security at the library gate is not nearly as tight. I often bring several students with me and we are never checked.\n\nI suppose if you posed as students, I could sneak you in through the library. I must ask that you try not to cause any trouble once inside. If you keep a low profile, you should be fine.\n\nAre you ready to go to the sanctuary?\"", eDialogPic.TERRAIN, 168, ["No", "Yes"])
    if result == 0:
        p.TalkingText = "\"Well return here and ask me about this again when you want to go.\""
        return
    elif result == 1:
        StuffDone["49_2"] = 4
        SpecialItem.Give("ArcturusNPC")
        ChoiceBox("\"We should probably get you some appropriate clothing and some trinkets so I can easily pass you off as students.\" He goes over to his wardrobe and finds several robes. They are kind of tight on you, but they will suffice.\n\n\"When we get to the library gate, you let me do all the talking. Try not to make yourself look suspicious. All right then!\"", eDialogPic.TERRAIN, 169, ["OK"])
        Message("Arcturus joins the party!")
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Elder_245": Town.NPCList.Remove(npc)
        p.TalkingText = "\"All right, shall we get going?\""
        return

def Gynai_1308_TalkingTrigger23(p):
    if StuffDone["49_2"] >= 5:
        p.TalkingText = "\"Quit wasting my time, you can already go in the library. Do you need help finding something or what?\""
        return
    if StuffDone["49_2"] < 4:
        return
    p.TalkingText = "Arcturus waves you into the library."
    StuffDone["49_2"] = 5
    ChoiceBox("Arcturus approaches the library keeper. The keeper greets Arcturus, apparently they know each other. \"So here with more students?\" asks the keeper. Arcturus replies, \"Yes, we have important research in the library today.\"\n\nThe keeper presses some kind of button beneath the desk and the portculli slide open. Arcturus moves away, but then the keeper shouts, \"Oh you forgot to sign in!\" Arcturus turns around and approaches him.\n\n\"Wait, never mind. I know you\'re legit. I\'ll take care of it for you.\" Arcturus chuckles. \"Glad to see you\'re doing your job.\" He turns to you. \"Come we have much \'work\' to do, right students?\"", eDialogPic.TERRAIN, 135, ["OK"])
    Town.AlterTerrain(Location(42,13), 0, TerrainRecord.UnderlayList[148])
    Town.AlterTerrain(Location(43,13), 0, TerrainRecord.UnderlayList[148])
