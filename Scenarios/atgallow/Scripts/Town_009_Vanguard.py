
def Vanguard_83_MapTrigger_18_20(p):
    if StuffDone["2_0"] == 0:
        StuffDone["2_0"] = 1
        ChoiceBox("Several important Empire officials are having a meeting. They are in a heated discussion and have not noticed you, or if they have are not bothered by your presence.\n\nAt the head of the table is an aging man wearing the mayoral robes. On your right side nearest the mayor sits a younger man in officials garb recording everything said. Further down sits a highly decorated Empire Dervish.\n\nAcross them are two mages. Closest to the mayor is the elder one. His robes bear markings that he too is an Empire Dervish. At his side sits a young man in his late twenties in purple robes. You listen to their meeting.\n\nThe Mayor speaks, \"I understand your concern, Dervish Montcalm.\" Referring to the elder wizard. \"However, we too have problems within the city that must be addressed. Our security is at the utmost!\"\n\nThe elder wizard responds, \"Mayor Vanderat, I know you must worry for the city. However, the source of our problems should have our greatest attention. The city will not last so long as he exists.\"\n\nThe younger wizard chimes in, \"Dervish Montcalm is correct. It is our belief at Fort Reflection that if we do not strike now, the entire Aizic Sector could be in for long hardships.\"", eDialogPic.CREATURE, 31, ["OK"])
        ChoiceBox("The Dervish on the other side of the table responds. \"But security within the city is most important. Should the city fall, the entire sector would be lost! As you know, unrest has been growing and threats of civil aggression is high.\"\n\nThe younger mage retorts. \"All respect Dervish Saab, but the cause of this is Halloth! If you could spare soldiers so our mission may be successful, it would take out the chance of riots.\"\n\nDervish Saab shakes his head, \"All respect Bladesman Sidor,\" he responds in a sarcastic tone. \"But, quite honestly I stand resolved that Dervish Montcalm\'s plan cannot and will not succeed! There is no need to risk lives on this doomed operation!\"\n\nDervish Montcalm retorts, \"Well then, Dervish Saab, what do you propose?\" There is a long pause. The other Dervish replies, \"Halloth is too strong. We must attack his resources. A direct invasion of his Citadel will not work!\"\n\nThe mayor interjects. \"Yes, the Troglodytes under his control are his arms and legs. If we can take them out, he will be helpless like a man with no appendages. Raids on Troglo forts are easier than a risky raid on a Vampyre Lord\'s domain.\"\n\nThe mayor looks up at you. \"And who do we have here?\" You tell your names and ranks. All of the men (except the official recording everything) smile. \"Imperial Guardians!\" He points to you. \"There is your answer, Dervish Montcalm!\"", eDialogPic.CREATURE, 17, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "EmpireDervish_17": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Official_33": Town.NPCList.Remove(npc)
        ChoiceBox("The mayor rises followed by his secretary. \"My ruling is that you will receive no soldiers from the city of Vanguard. Instead, you will convince these Imperial Guardians to aid you.\"\n\nThe two magi shake their heads. Dervish Saab rises, \"It was a great discussion Dervish Montcalm, Bladesman Sidor. But I have work to attend to. If you will excuse me.\" The three men leave the room, leaving the two mages.\n\nDervish Montcalm waves you to the table. You all take seats. \"Allow me to introduce myself. I am Dervish Montcalm, commander of Fort Reflection, and this is my apprentice, Bladesman Sidor.\" Sidor nods.\n\n\"I am sure you have heard the discussion at hand. However, allow me to elucidate the problem. We of the Vanguard Sector are plagued by a powerful Troglodyte Vampyre lord called Halloth.\n\nThirty years ago, Halloth terrorized this sector and I helped fight him. I hired a group of five mercenaries to slay Halloth and they succeeded. I cannot take credit for their work, they were a resourceful band.\n\nAs you know, Vampyres are immortal and after being defeated are banished to the lower planes. A powerful, and I mean really powerful, entity must have summoned him back. We have no idea as to the identity of this entity.", eDialogPic.CREATURE, 27, ["OK"])
        ChoiceBox("A century ago, several Troglodytes emigrated from the continent of Valorim and settled in the mountains in the southern Aizic Sector. Thirty years ago, Halloth managed to enslave the poor and misguided humanoids.\n\nEven after he was defeated, the Troglodytes continued to worship the creature. True, the Troglodytes are a race with many talents and powerful magi, I doubt that they could have been capable of summoning back Halloth.\n\nNow that Halloth is back, he once again has the Troglodytes under his control. They are a race of great numbers, skilled fighters, and talented magi. They are a severe threat to us, but only so long as Halloth is around to command them.\n\nDervish Saab believes that by eliminating the Troglos, you stop the problem. But let me assure you that his reasoning is flawed. Halloth doesn\'t need any Troglodytes to cause damage. His powers are great enough to do without.\n\nThe Sector has suffered greatly. Troglo raids are wiping out the farmers. They unleashed quickfire that obliterated the small town of Widesprint. We believe Halloth is also behind the unrest going on here.\n\nAs you can see, this Halloth is quite a menace. However, we have a plan to stop him.", eDialogPic.CREATURE, 116, ["OK"])
        ChoiceBox("We are constructing many golems at Fort Reflection. We plan to use these golems and our forces at Fort Reflection to raid Halloth\'s Citadel. Unfortunately, the citadel is well defended from a full scale attack.\n\nThat is why we must sneak some brave souls in to slay Halloth. We were here in Vanguard to request five of the finest warriors in the Aizic Sector. However, Dervish Saab and the Mayor were not willing to share them.\n\nIt looks like I must ask you to be that strike force. I know that Imperial Guardians are a rare breed and are specially suited for such work. I can put in a good word to the Prime Director for you if you succeed.\n\nIf you decide to help, you can find me at Fort Reflection. It was nice meeting you, but Sidor and I have much work to do back at the Fort.\" They rise and bow. Then they teleport away.\n\nThe room is now empty.", eDialogPic.STANDARD, 1025, ["OK"])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Montcalm_194": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Sidor_195": Town.NPCList.Remove(npc)
        Animation_Hold(-1, 010_teleport)
        Wait()
        Town.PlaceEncounterGroup(2)
        return

def Vanguard_86_MapTrigger_23_25(p):
    if StuffDone["2_0"] == 0:
        Town.PlaceEncounterGroup(1)
        return
    Town.PlaceEncounterGroup(2)

def Vanguard_90_MapTrigger_53_50(p):
    if StuffDone["42_9"] >= 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(54,51)).Num == 128:
            Town.AlterTerrain(Location(54,51), 0, TerrainRecord.UnderlayList[125])
            return
        return

def Vanguard_96_MapTrigger_52_55(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("This stairway leads down. The corridor reeks with the smell of rotting trash. You are not sure you want to go down here.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(60,58)
    Party.MoveToMap(TownMap.List["VanguardSewers_83"])

def Vanguard_97_MapTrigger_36_14(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(53,13)
    Party.MoveToMap(TownMap.List["VanguardSewers_83"])

def Vanguard_98_MapTrigger_25_11(p):
    if StuffDone["43_7"] == 1:
        if StuffDone["43_9"] == 250:
            return
        StuffDone["43_9"] = 250
        ChoiceBox("You return to Dervish Saab reporting that you had slain Dervish Lennon, leader of the rebel group, the Red Spear. You also inform him of the link between the garrison and the rebel base in the sewers. He looks infuriated.\n\n\"Traitors within my own ranks! That really burns me. I have always trusted my men to the fullest, yet some of them have betrayed me to that Red Spear, to Lennon.\" He pauses to think things over.\n\n\"I guess, now that they are gone, things will be going a lot better for us. I just don\'t know if I will ever be able to trust my men again. To think the supposed full search of the sewers was merely a plant!\"\n\nHe thinks for a bit. \"I suppose you would like some kind of compensation.\" He opens his desk and removes a glowing gold ring. \"Have one of your warriors wear this. It will improve his skill during combat. Thanks again for the help.\"", eDialogPic.CREATURE, 17, ["OK"])
        Party.GiveNewItem("GoldRingofSkill_296")
        return

def Vanguard_99_MapTrigger_35_12(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(35,11)).Num == 191:
        MessageBox("You push the bookshelf and you find yourself in the office of a garrison! This is very suspicious indeed.")
        Town.AlterTerrain(Location(35,11), 0, TerrainRecord.UnderlayList[170])
        return

def Vanguard_100_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(28, 26),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(24, 30),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(28, 34),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(32, 30),WorldMap.SectorAt(Party.OutsidePos))

def Vanguard_101_TalkingTrigger14(p):
    if StuffDone["43_7"] == 0:
        return
    p.TalkingText = "\"The rebels have largely fallen apart, now that their masterminds are gone. Thanks to you of course!\""

def Talking_9_50(p):
    if Party.Gold >= 8:
        Party.Gold -= 8
        p.TalkingText = "You pay the gold and are served a round of drinks. \"Here ya go! Enjoy!\" The beer is not all that great."
    else:
        p.TalkingText = "You cannot afford it!"

def Talking_9_51(p):
    if Party.Gold < 30:
        p.TalkingText = "You cannot afford it!"
    else:
        Party.Gold -= 30
        Party.Pos = Location(45, 29)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "You pay the gold. The Troglo points out which room is yours. \"It\'s over there! If you need anything, just ask.\" You set out to your room and have a fairly nice rest."
        CentreView(Party.Pos, False)
