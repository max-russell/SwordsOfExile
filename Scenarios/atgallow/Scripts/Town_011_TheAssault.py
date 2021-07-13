
def TheAssault_124_MapTrigger_24_41(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        return;
    ChoiceBox("Dervish Montcalm looks at you happily. \"I knew you would succeed in bringing down the barrier. Well, as you can see you only brought down the first barrier -- the magical one.\n\nNow we are faced with this massive physical one. Never fear, we have brought several powerful explosives to create an opening in this magically strengthened wall. Ready?\" You nod accordingly.\n\n\"Okay! Stand back!\"", eDialogPic.CREATURE, 27, ["OK"])
    Animation_Hold(-1, 025_magespell)
    Wait()
    Animation_Explosion(Location(22,38), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Explosion(Location(24,38), 0, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Explosion(Location(26,38), 0, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("Dervish Montcalm and the rest of the mages look utterly shocked. The explosives had little effect on the massive foreboding wall. The mages begin to talk amongst themselves of solutions, but Dervish Montcalm interjects.\n\n\"Apparently we have miscalculated the degree which Halloth has strengthened this wall. However, we shall not fail. I guess I have no other choice...\"\n\nDervish Montcalm walks up to the wall and places his hands upon it. He begins to chant loudly as bolts of energy move into the wall, shaking it. You are impressed by the degree of skill your fellow wizard has.", eDialogPic.CREATURE, 27, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Montcalm_194": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(2)
    Animation_Explosion(Location(24,38), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Explosion(Location(23,38), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Explosion(Location(25,38), 2, "005_explosion")
    Animation_Hold()
    Wait()
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Montcalm_194": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(3)
    for x in range(23, 26):
        for y in range(35, 39):
            if Maths.Rand(1,0,100) <= 60:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[87])
    for x in range(23, 26):
        for y in range(38, 39):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[87])
    Animation_Explosion(Location(24,38), 0, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("Suddenly, a massive shockwave blasts Dervish Montcalm\'s body back several meters. The wall fares even worse as rubble is propelled forward in a brilliant shatter. Several mages rush to Dervish Montcalm\'s body.\n\nDervish Montcalm is visibly drained from the ultra powerful Shatter spell. He stands up slowly and says, \"I\'ll be all right. Come on now, let us get moving.\" Dervish Montcalm shakes his head, he is clearly in bad shape.\n\nA wizard steps forward. \"Dervish, I respectfully order, as my duty as an Empire Bladesman, that you not participate in the assault. You are clearly in no shape to go into battle and it would be suicide for you.\"\n\nDervish Montcalm grows angry. \"So noted, Bladesman. However, I must overrule that order, as is my authority as an Empire Dervish. I assure you, I am fine!\" Even though he is clearly not fine. \"This is no time for bickering. Move out!\"\n\nAnother mage shouts out. \"No!\" The Dervish is getting furious. \"You are not fine, sir. If we must, we will restrain you from going onto the battlefield. Stay behind commander, we implore you!\"\n\nYou would have to agree with the dissenting mages. Dervish Montcalm looks at you and you shake your heads. \"Well, it looks like I have no choice. I will stay behind. But first, I must give my final orders.\"", eDialogPic.CREATURE, 27, ["OK"])
    ChoiceBox("The Dervish speaks directly to you. \"As soon as we get out there, move quickly to the gates. Do not tarry on the Spectral Knights, our Golems will take care of them. Once you are at the gates, you will need to get them open.\n\nTo do this, you must blast the levers on both sides. After they are both gone, the gates will open and you will be able to enter Halloth\'s Citadel. Afterward, our survivors will retreat and you will be on your own.\n\nTake care, Halloth is a very powerful and deceptive creature. However, he can be defeated. Some mercenaries proved that thirty years ago and I have greater confidence in you than I did in them.\n\nI know you will succeed.\" He nods and issues the command to move out.", eDialogPic.CREATURE, 27, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(24,24))
    p.CancelAction = True
    Town.NPCList.Clear()
    Town.PlaceEncounterGroup(1)
    ChoiceBox("Leaving Dervish Montcalm behind. You and the forces quickly move across the courtyard of Halloth\'s Citadel. When you are about halfway through, four imposing suits of armor appear ahead of you and behind you.\n\nThe mages quickly order the bulky Golems into the proper formation. The Spectral Knights begin to close in as the mages prepare their spells and the Golems stand ready to smash the Knights.\n\nIt\'s time for you to make your dash to the gates!", eDialogPic.CREATURE, 99, ["OK"])
    if StuffDone["2_6"] == 0:
        Timer(Town, 5, False, "TheAssault_131_TownTimer_24", eTimerType.DELETE)
        return

def TheAssault_125_MapTrigger_24_38(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Dervish Montcalm stands behind the wall. He looks furious upon seeing you back here. After using many expletives he shouts, \"Get back out there cowards! This is our only chance!\"")

def TheAssault_128_MapTrigger_24_4(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    ChoiceBox("You look back and see the last of the mages get crushed by the Spectral Knights. No matter, you are past them. You rush inside as fast as you can through a long dark hallway.\n\nWhen you are partway into an antechamber, the portculli behind you slam shut. You are trapped within Halloth\'s Citadel!", eDialogPic.CREATURE, 26, ["OK"])
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,57)
    Party.MoveToMap(TownMap.List["HallothsCitadel_21"])

def TheAssault_131_TownTimer_24(p):
    Animation_Hold(-1, 053_magic3)
    Wait()
    ChoiceBox("A spirit materializes in the air above the Citadel gates. He raises his arms and sends out a shockwave! You brace yourselves, but it has no effect upon you. However, it was not so with the Golems.\n\nWithin seconds, the Golems crumble to the ground! Halloth must have known how to disable these Golems ahead of time. You\'re betting he learned this from the stolen Golem back in Fort Khazar. Now you and the mages are on your own.\n\nSidor was correct. Your failure did come back to haunt you!", eDialogPic.CREATURE, 118, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Golem_196": Town.NPCList.Remove(npc)

def TheAssault_132_CreatureDeath32(p):
    Town.AlterTerrain(Location(21,4), 0, TerrainRecord.UnderlayList[170])
    if Maths.Rand(1,0,100) <= 100:
        Town.PlaceField(Location(21,4), Field.CRATER)
    StuffDone["7_3"] += 1
    if StuffDone["7_3"] == 250:
        TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(3,37))
    if StuffDone["7_3"] < 2:
        MessageBox("You have destroyed one of the levers! However, the other one on the other side remains.")
        return
    SuspendMapUpdate()
    for x in range(23, 26):
        for y in range(4, 5):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetUnlocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()
    ChoiceBox("Just as Dervish Montcalm had told you, the destruction of both levers caused the gates open. You look inside and only see pitch blackness. Ahead lies an eerie and quite dangerous place.\n\nYou look back to see the mages losing their battle. But no matter, you are just about inside. The confrontation with Halloth draws nearer.", eDialogPic.TERRAIN, 105, ["OK"])

def TheAssault_133_CreatureDeath33(p):
    Town.AlterTerrain(Location(27,4), 0, TerrainRecord.UnderlayList[170])
    if Maths.Rand(1,0,100) <= 100:
        Town.PlaceField(Location(27,4), Field.CRATER)
    StuffDone["7_3"] += 1
    if StuffDone["7_3"] == 250:
        TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(3,37))
    if StuffDone["7_3"] < 2:
        MessageBox("You have destroyed one of the levers! However, the other one on the other side remains.")
        return
    SuspendMapUpdate()
    for x in range(23, 26):
        for y in range(4, 5):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetUnlocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()
    ChoiceBox("Just as Dervish Montcalm had told you, the destruction of both levers caused the gates open. You look inside and only see pitch blackness. Ahead lies an eerie and quite dangerous place.\n\nYou look back to see the mages losing their battle. But no matter, you are just about inside. The confrontation with Halloth draws nearer.", eDialogPic.TERRAIN, 105, ["OK"])

def Talking_11_10(p):
    if Party.Gold >= 7:
        Party.Gold -= 7
        p.TalkingText = "You ask for the drinks and she immediate goes to pour them. She is very fast and efficient. She returns and asks, \"Seven gold please.\" You pay and receive your drinks as she rushes to wait on the next customer. The drinks are quite refreshing!"
    else:
        p.TalkingText = "You cannot afford it."

def Talking_11_11(p):
    if Party.Gold < 30:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 30
        Party.Pos = Location(38, 24)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "You pay your gold and at the next available moment, leads you to your room. The room is a bit cramped, but you manage to have a decent rest."
        CentreView(Party.Pos, False)
