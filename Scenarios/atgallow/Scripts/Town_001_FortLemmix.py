
def FortLemmix_0_MapTrigger_17_13(p):
    if StuffDone["0_1"] == 250:
        return
    StuffDone["0_1"] = 250
    TownMap.List["FortLemmix_1"].DeactivateTrigger(Location(17,13))
    ChoiceBox("The year is 1247 I.E. You are living in the golden age of the Empire. The great nation encircles the world and oversees everything without question. For as long as history can remember, the Sword and Sun has reigned.\n\nThe last great wars were centuries ago and long forgotten. The last of those was 400 years ago when the Empire failed to conquer the underworld in a bitter and bloody war with those banished to live there.\n\nMuch progress has been made since that time. The people of the underworld have for the most part forgotten the transgressions of long ago and reunified with the Empire. Since then, peace has reigned for the most part.\n\nBeing soldiers in this time is not very exciting. The days where soldiers could become heroes have faded into the past. The Imperial army serves more as a security measure than anything else.", eDialogPic.STANDARD, 1024, ["OK"])
    ChoiceBox("But, it appears that times may be getting a bit more exciting. In recent years, several problems have been occurring throughout the continent of Pralgad. Sure, problems have always been around, but not this widespread in a long time.\n\nMany scholars suggest that the Empire is in decline. Others say that the people are bored and are causing trouble for excitement. Even other theorists say that chaos is the natural order of things.\n\nWhatever the reasons, you are stationed at Fort Lemmix in the Agran Sector -- the continent of Pralgad is divided up into nine sectors. Recently, some bizarre cult has been causing trouble throughout the sector.\n\nFortunately, the cult has been fairly quiet only causing minor threats. However, in the past months, the cult has become increasingly aggressive demanding tributes from several of the local towns.\n\nYou have been given orders to meet with the commander of the fort, Bladesman Kelli. He probably has some sort of routine patrolling mission for you lined up. Whatever it is, you are going to find out soon.", eDialogPic.STANDARD, 1024, ["OK"])
    Animation_Hold(-1, 004_bless)
    Wait()
    ChoiceBox("CHAPTER I -- THE SECT", eDialogPic.STANDARD, 28, ["OK"])

def FortLemmix_1_MapTrigger_17_16(p):
    result = ChoiceBox("These barracks are assigned to your party. You may rest and recover in them if you choose. Also, you may store any of your unwanted items here.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        MessageBox("You have an excellent rest in familiar beds. After eight hours of relaxation, you are ready to go out and do whatever the Imperial army wants you to.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += 1000
            Party.HealAll(250)
            Party.RestoreSP(250)
        return

def FortLemmix_2_MapTrigger_9_26(p):
    if StuffDone["0_2"] >= 2:
        if StuffDone["0_2"] >= 4:
            if StuffDone["0_2"] >= 6:
                if StuffDone["0_2"] < 7:
                    StuffDone["0_2"] = 7
                    ChoiceBox("As soon as you enter, Bladesman Kelli rises and commends you. \"You have done a great service for the Empire today. I must admit I had my doubts about your group, but I was proven wrong.\"\n\nHe draws his blade and places it upon your shoulders. \"I hereby declare you Imperial Guardians! May you go forth and defend the Empire!\" You had expected to be promoted to captains, but he chose to give you greater honors.\n\nBlade Kelli seats himself. \"It will be a pity to lose my best soldiers, but my superiors demanded it for the best of the Empire.\" It now strikes you that your new rank removes you from the standard duties of regular soldiers; now you are special.\n\nAn Imperial Guardian\'s duty is to travel about the land and defend the Empire. You are now considered independent soldiers answerable only to the Emperor himself. Your great deeds have moved you into a new track.\n\n\"It was an honor to be your commanding officer. You may now travel just about anywhere in the Empire. I wish you best of luck on your future adventures!\"\n\nWhere to next? \"That is for you to decide. I have heard of a Nephilim war in the Wrynn Sector to the east and about some powerful Vampyre stalking the Aizic Sector to the north west. Wherever you are, know that I will hope for you.\"", eDialogPic.STANDARD, 16, ["OK"])
                    for pc in Party.EachAlivePC():
                        pc.AwardXP(100)
                    StuffDone["100_0"] = 2
                    StuffDone["1_9"] = 1
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Bladesman_15": Town.NPCList.Remove(npc)
                    Town.PlaceEncounterGroup(1)
                    return
                return
            if StuffDone["0_2"] < 5:
                StuffDone["0_2"] = 5
                ChoiceBox("You tell Bladesman Kelli all that you have learned. He orders an aide to bring several maps. He does so and Bladesman Kelli looks over them for a few minutes. Afterward, he speaks.\n\n\"You have done well men. But now is not the time to rest. You have infiltrated the Follower\'s main base and slain many of their number. But that may be a moot point if Zaine can carry out his plan.\"\n\nHe shows you a map of the area north of Lake Praddor. Blade Kelli points to a small cave labeled \'Cavern PAC-0783\' on the map. \"I believe they are there. It would be dangerous to risk an invasion of the cave as it is probably well defended.\n\nWhat would work best is a small group that could sneak in and sabotage their mold colony.\" He looks up at you and grins. \"It looks like you\'re the best candidates for that mission. Should you be successful, I can all but guarantee a promotion.\n\nYour orders are to go to the \'Cavern PAC-0783\' and destroy the mold colony there. We have new equipment for you in the supply room to aid you. You have your orders men!\"", eDialogPic.STANDARD, 4, ["OK"])
                StuffDone["0_3"] = 0
                TownMap.List["PraddorCave_6"].Hidden = False
                return
            return
        if StuffDone["0_2"] < 3:
            StuffDone["0_2"] = 3
            ChoiceBox("You return victorious to a concerned Bladesman Kelli. He looks up at you with a small smile. \"You\'ve returned. I must commend you on your efforts. Without you, many more surely would have died in the assault.\"\n\nHe pauses. \"As you know, Ardent is a total loss. However, patrols did manage to capture a few of the cultists. They are here and under interrogation. We have learned some useful information from them.\n\nThe \'Followers\' worship a dark god called Morbane and are led by his prophet Zaine. I believe you fought him earlier at Ardent. As you may have guessed, the villain escaped along with many of his fellow cultists.\n\nIt appears that the Followers are also preparing to place a horrid curse upon our crops. As you know, that would severely harm the Empire and we must stop it at all costs!\n\nWhere to next, you ask? We have heard of the cult\'s hidden bunker in Vega. You will have to speak with Captain Wester, who is interrogating the prisoners. He may have some useful information on how to locate it.\n\nYour orders are to find and infiltrate that bunker in Vega (northeast of here). We cannot allow them to carry out the curse! You have your orders men.\"", eDialogPic.CREATURE, 15, ["OK"])
            return
        return
    if StuffDone["0_2"] < 1:
        StuffDone["0_2"] = 1
        ChoiceBox("You arrive at the office of Bladesman Kelli. He is sitting at his desk, filling out troop assignments as you enter. He looks up and smiles, \"Ah, come in! I\'ve been waiting for you.\"\n\nHe clears an area on his desk. \"Okay men, here\'s the situation. As you have heard at yesterday\'s briefing, the town of Ardent to the south has been threatened by the Followers, a cult which has been causing trouble in this sector for the past few months.\n\nThe cult has demanded that it surrender one of its children no older than the age of six to be sacrificed to their dark deity. Of course the leaders of Ardent have refused. The Followers have threatened to destroy Ardent.\n\nWe doubt the wild cult will be able to do much, but the leaders of Ardent have asked us to send some troops just in case. And well, we\'ve chosen to send your group to beef up the defenses.\n\nYour orders are to report to the garrison in Ardent where you will be under the command of Captain Tern. You are to stay there until ordered to return. Any questions?\" You nod in understanding.\n\n\"Oh yes! The quartermaster has some supplies available for you just in case you need them. You have your orders men!\"", eDialogPic.CREATURE, 23, ["OK"])
        return

def FortLemmix_4_MapTrigger_23_40(p):
    if StuffDone["0_2"] >= 2:
        return
    if StuffDone["0_2"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Your orders are to see Bladesman Kelli. If you leave the fort without permission you will surely be reprimanded later.")
        return
    result = ChoiceBox("Your orders are to go to Ardent and report to Captain Tern. Make sure you haven\'t forgotten anything. Are you ready to set out to Ardent?", eDialogPic.TERRAIN, 93, ["Leave", "Onward"])
    if result == 1:
        ChoiceBox("Following your orders, you head south to the town of Ardent. Your transit takes about two hours. It is a nice peaceful journey as you travel through the scenic rural farmlands of the Agran Sector.\n\nThe Agran Sector is the most rural sector of Pralgad. It is chiefly responsible for growing the continent\'s food supply as it provides for over half of Pralgad\'s needs. If somehow these crops were destroyed, much of Pralgad would starve.\n\nAfter two hours you arrive at Ardent. You meet with Captain Tern. He is short and bald but very muscular. \"Greetings men! I am Captain Tern and you must be the troops we requested from Fort Lemmix.\n\nAs you had probably noticed, the town\'s pretty quiet. We\'ve told the civilians to stay indoors just in case something happens. Although we doubt anything will, we\'re just taking all the necessary precautions.\n\nI have business I must attend to. Your quarters await.\" A young recruit leads you to a small room outfitted with cots. It is not very comfortable but it will just have to do for now.", eDialogPic.STANDARD, 28, ["OK"])
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(9,33)
        Party.MoveToMap(TownMap.List["Ardent_2"])
        return
    p.CancelAction = True

def FortLemmix_7_MapTrigger_27_28(p):
    if StuffDone["0_2"] == 3:
        Town.AlterTerrain(Location(34,35), 0, TerrainRecord.UnderlayList[125])
        return

def FortLemmix_9_MapTrigger_11_22(p):
    if StuffDone["0_2"] >= 7:
        Town.PlaceEncounterGroup(1)
        return

def FortLemmix_10_OnEntry(p):
    if StuffDone["0_4"] == 250:
        return
    StuffDone["0_4"] = 250
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(17,15))
    p.CancelAction = True
    MessageBox("You return to Fort Lemmix. Being tired from the fighting, the trip takes twice as long as before. Bladesman Kelli orders you to get some rest and report with him in the morning.")
    if Game.Mode != eMode.COMBAT:
        Party.Age += 5000
        Party.HealAll(250)
        Party.RestoreSP(250)

def FortLemmix_11_ExitTown(p):
    if p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(32, 16),WorldMap.SectorAt(Party.OutsidePos))
    if p.Dir.IsSouth:
        if StuffDone["0_2"] == 5:
            if StuffDone["1_7"] == 250:
                return
            StuffDone["1_7"] = 250
            MessageBox("Just after you leave Fort Lemmix, a small group of cultists jump from behind the bushes. You\'ve been ambushed! The cultists have sent some of their stealthiest warriors to take care of you before you can do any more damage.")
            return

def FortLemmix_12_TalkingTrigger1(p):
    if StuffDone["0_2"] < 2:
        p.TalkingText = "He shakes his head. \"You are to report to Captain Tern, head of the garrison in Ardent. There are supplies for you in storage. Just ask the quartermaster. Any further confusion?\""
        return
    if StuffDone["0_2"] < 4:
        p.TalkingText = "\"Your orders are to infiltrate the hidden bunker in Vega. To find out more, speak with Captain Wester in interrogation. Any questions?\""
        return
    if StuffDone["0_2"] < 6:
        p.TalkingText = "\"Your orders are to go to the Followers cavern north of Lake Praddor which is to the north of here. Infiltrate their base and destroy the mold colony. Understand?\""
        return

def FortLemmix_13_TalkingTrigger2(p):
    if StuffDone["0_2"] == 1:
        if StuffDone["0_3"] == 0:
            p.TalkingText = "He looks through his papers. \"Ah yes, here you are! You may have all of the supplies in the storeroom to your south on the left. Good luck on whatever mission you\'re on!\""
            StuffDone["0_3"] = 1
            Town.AlterTerrain(Location(33,11), 0, TerrainRecord.UnderlayList[129])
            return
        return
    if StuffDone["0_2"] == 5:
        if StuffDone["0_3"] == 0:
            p.TalkingText = "Nathan looks somewhat surprised. \"Well, it looks like Blade Kelli thinks you\'ll need our best equipment. You are allowed the supplies in the lower east chamber.\""
            StuffDone["0_3"] = 1
            Town.AlterTerrain(Location(37,9), 0, TerrainRecord.UnderlayList[129])
            return
        return

def FortLemmix_14_TalkingTrigger18(p):
    if StuffDone["100_0"] >= 6:
        if StuffDone["100_0"] < 9:
            p.TalkingText = "\"Empire Dervishes! I\'m sure impressed. I knew right from the start that your futures were bright, I never realized you\'d accomplish this much in such a short amount of time!\""
            return
        p.TalkingText = "\"What\'s this I hear about you saving the world from some evil aliens? And to think, I was YOUR commanding officer. One day after I retire and you settle down, one of you could take over this fort!\""
        return
    if StuffDone["100_0"] < 4:
        return
    p.TalkingText = "\"You\'ve been promoted to Elite status!? That\'s wonderful! I\'ve heard you\'ve had something to do with that mess up in Stolgrad. Well, keep up the good work!\""
