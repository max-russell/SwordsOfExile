
def Ardent_15_MapTrigger_1_34(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    ChoiceBox("You are awakened by a loud boom! At first you think it\'s probably just an accidental wand discharge, and go back to bed. But then you hear shouting, you decide to get out of bed and grab your equipment.", eDialogPic.STANDARD, 25, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(10,32))
    p.CancelAction = True
    Animation_Hold(-1, 071_sword3)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(11,32))
    p.CancelAction = True
    Town.AlterTerrain(Location(12,32), 0, TerrainRecord.UnderlayList[129])
    Animation_Hold(-1, 058_opendoor)
    Wait()
    Animation_Explosion(Location(14,28), 0, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("You see a flash to the north. Suddenly, the ceiling at the other end of the room caves in under an explosion. It appears to be raining fireballs! In the distance, you hear several screams and the clanking of swords.\n\nArdent is under attack!!\n\nSeveral soldiers, including Captain Tern, are caught beneath the rubble. Most of them were killed instantly but Captain Tern is still alive, barely. You run up to him to try to help.", eDialogPic.STANDARD, 25, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(12,32))
    p.CancelAction = True
    Animation_Hold(-1, 071_sword3)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(13,31))
    p.CancelAction = True
    Animation_Hold(-1, 029_monsterdeath2)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(13,30))
    p.CancelAction = True
    Animation_Hold(-1, 005_explosion)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(14,29))
    p.CancelAction = True
    Animation_Hold(-1, 071_sword3)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(14,28))
    p.CancelAction = True
    ChoiceBox("His voice is very weak. \"It\'s too late for me! You must stop them. We never expected them to have such powerful magics. Their leader is at the center of the square, you must defeat him and perhaps his followers will flee.\"\n\nHe nods and dies. You can hear the sounds of other explosions, each about thirty seconds apart. You look outside and see several cultists raging through the town. You had better hurry or there won\'t be anything left of Ardent.", eDialogPic.CREATURE, 14, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Captain_14": Town.NPCList.Remove(npc)
    Town.AlterTerrain(Location(14,27), 0, TerrainRecord.UnderlayList[165])

def Ardent_16_OnEntry(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    ChoiceBox("You are awakened by a loud boom! At first you think it\'s probably just an accidental wand discharge, and go back to bed. But then you hear shouting, you decide to get out of bed and grab your equipment.", eDialogPic.STANDARD, 25, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(10,32))
    p.CancelAction = True
    Animation_Hold(-1, 071_sword3)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(11,32))
    p.CancelAction = True
    Town.AlterTerrain(Location(12,32), 0, TerrainRecord.UnderlayList[129])
    Animation_Hold(-1, 058_opendoor)
    Wait()
    Animation_Explosion(Location(14,28), 0, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("You see a flash to the north. Suddenly, the ceiling at the other end of the room caves in under an explosion. It appears to be raining fireballs! In the distance, you hear several screams and the clanking of swords.\n\nArdent is under attack!!\n\nSeveral soldiers, including Captain Tern, are caught beneath the rubble. Most of them were killed instantly but Captain Tern is still alive, barely. You run up to him to try to help.", eDialogPic.STANDARD, 25, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(12,32))
    p.CancelAction = True
    Animation_Hold(-1, 071_sword3)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(13,31))
    p.CancelAction = True
    Animation_Hold(-1, 029_monsterdeath2)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(13,30))
    p.CancelAction = True
    Animation_Hold(-1, 005_explosion)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(14,29))
    p.CancelAction = True
    Animation_Hold(-1, 071_sword3)
    Wait()
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(14,28))
    p.CancelAction = True
    ChoiceBox("His voice is very weak. \"It\'s too late for me! You must stop them. We never expected them to have such powerful magics. Their leader is at the center of the square, you must defeat him and perhaps his followers will flee.\"\n\nHe nods and dies. You can hear the sounds of other explosions, each about thirty seconds apart. You look outside and see several cultists raging through the town. You had better hurry or there won\'t be anything left of Ardent.", eDialogPic.CREATURE, 14, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Captain_14": Town.NPCList.Remove(npc)
    Town.AlterTerrain(Location(14,27), 0, TerrainRecord.UnderlayList[165])

def Ardent_17_CreatureDeath0(p):
    ChoiceBox("You strike down Zaine, the leader of the invasion. He shouts out a brief prayer and disappears in a puff of smoke. With the leader beaten, the invading cultists quickly flee the town.\n\nWell, it looks like this originally boring mission turned out to be exciting after all. Although the town is a total loss, many of its lives have been saved thanks to you. It looks like you\'re going to be heroes of the day.\n\nIt looks like the battle is over. It\'s probably time to report back to Fort Lemmix.", eDialogPic.CREATURE, 24, ["OK"])
    for pc in Party.EachAlivePC():
        pc.AwardXP(25)
    SuspendMapUpdate()
    for x in range(1, 48):
        for y in range(1, 48):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[2]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[176])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[176]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[2])
    ResumeMapUpdate()
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if  npc.IsABaddie: Town.NPCList.Remove(npc)
    SuspendMapUpdate()
    for x in range(4, 44):
        for y in range(4, 44):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[2]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[176])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[176]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[2])
    ResumeMapUpdate()
    StuffDone["0_2"] = 2

def Talking_2_31(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "He stares deep into you with his piercing gaze. \"Yes, I see lives of great struggle. I can see your future. It see much danger lying ahead for you.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_32(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"Yes, I can see monsters surrounding you. Your enemies are many. I can see that your bravery will be your undoing. Indeed, your undoing!\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_33(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"You shall find yourself in an impossible situation. You will find yourself at the gallows of despair. Yet, it is not too late, I can see salvation.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_34(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"Yes, salvation in the form of knowledge. You shall fight many kinds of creatures. Yet there is one variety that I foresee as your downfall.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_35(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"It is ironic the ones that will cause your fall will be the fallen themselves. I am referring to the undead! Lost souls reanimated. They shall bring you despair. But there is an answer to them.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_36(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"As I was saying, the answer comes in the form of knowledge. Not just the knowledge of your fate, but knowledge of defense. I can offer you a ritual to ward off the horrid undead and possibly avert your failure!\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_37(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"The ritual is a powerful one. But before I can teach it to you, you must learn the proper way of asking for it.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_38(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"Asking for such powerful knowledge must be done with full knowledge of the consequences. Knowledge is power which incurs responsibility. Before I can tell you how to ask, you must accept the responsibilities.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_39(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"I trust your word you will assume the responsibility. Now for the rite of asking. In asking for power, one must show oneself to have goodness and purity. Now show me these qualities in asking again.\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""

def Talking_2_40(p):
    if Party.Gold >= 20:
        Party.Gold -= 20
        p.TalkingText = "\"Now that you have asked the correct ways, I will deliver on my promise. However, to share such powerful knowledge will not be cheap in the least. Are you ready for me to deliver?\""
    else:
        p.TalkingText = "\"I cannot see any deeper for you lack the generosity for my wisdom.\""
