
def ZenithKeep_525_MapTrigger_50_49(p):
    if StuffDone["9_1"] == 0:
        Timer(Town, 40, False, "ZenithKeep_547_TownTimer_2", eTimerType.DELETE)
        Animation_Hold(-1, 068_identify)
        Wait()
        if StuffDone["9_1"] == 0: StuffDone["9_1"] = 1
        else: StuffDone["9_1"] = 0
        return

def ZenithKeep_526_MapTrigger_31_57(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["9_1"] = 0
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,7)
    Party.MoveToMap(TownMap.List["Zenith_28"])

def ZenithKeep_529_MapTrigger_41_23(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["9_1"] == 0:
        MessageBox("The guards stop you. \"This is a restricted area. You are not authorized to enter here.\"")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(40,23))
        p.CancelAction = True
        return
    if StuffDone["9_2"] == 250:
        return
    StuffDone["9_2"] = 250
    MessageBox("For some reason, the guards do not even notice you. You easily slip by them.")

def ZenithKeep_532_MapTrigger_36_14(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The guards stop you. \"This is a restricted area. You are not authorized to enter here.\"")

def ZenithKeep_536_MapTrigger_45_15(p):
    if SpecialItem.PartyHas("StolgradDisc"):
        return
    result = ChoiceBox("You do a detailed search of the dresser and only find personal effects and clothing. However, there is a bronze disk with the insignia of the Stolgrad Sector that attracts your attention.\n\nIt\'s owner is sleeping, he probably wouldn\'t notice if you borrowed it.", eDialogPic.TERRAIN, 145, ["Leave", "Take"])
    if result == 1:
        SpecialItem.Give("StolgradDisc")
        return

def ZenithKeep_537_MapTrigger_46_18(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["9_3"] == 250:
        return
    StuffDone["9_3"] = 250
    MessageBox("You break into this wizard\'s quarters and find him in a deep slumber. Wizards are known for their sensitivity, so you will have to be really quiet as not to disturb him.")

def ZenithKeep_538_MapTrigger_11_30(p):
    if Party.CountItemClassEquipped(13, False) > 0:
        if StuffDone["8_8"] == 250:
            return
        StuffDone["8_8"] = 250
        MessageBox("Since one of you is wearing the traditional Scribe\'s Robe, the guard only gives you a subtle glance. He also has no objections to bringing along your friends.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The guards stop you. \"This is a restricted area. You are not authorized to enter here.\"")

def ZenithKeep_540_MapTrigger_19_21(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(19,22)).Num == 145:
        if SpecialItem.PartyHas("StolgradDisc"):
            MessageBox("Before you stands a massive steel door. The door has no handles but a circular alcove in the center. You insert the disc you found earlier and it fits perfectly! The massive door opens smoothly.")
            SuspendMapUpdate()
            for x in range(19, 21):
                for y in range(22, 23):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            Timer(Town, 2, False, "ZenithKeep_548_TownTimer_25", eTimerType.DELETE)
            return
        MessageBox("Before you stands a massive steel door. The door has no handles but a circular alcove in the center. You have no way of opening this and you doubt bashing or magic will work.")
        return

def ZenithKeep_542_MapTrigger_19_25(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["8_9"] == 250:
        return
    StuffDone["8_9"] = 250
    Town.PlaceEncounterGroup(1)
    Animation_Explosion(Location(21,26), 2, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("Suddenly, there is a flash! A young boy of about eight years of age appears. \"There you are kitty! I\'ve been looking all over for you. How did you get into here? Come on, let\'s play!\" He turns to look at you and shrieks!\n\n\"Hey! You\'re not supposed to be here. Mamaaaa!\" Several scribes pour into the room followed by many guards. You have no choice but to surrender. Uh oh! It looks like you made a possibly fatal error!\n\nYou are carried off to your cell where you are held for four days. Then, two guards come and instruct that you are being put on trial for espionage. You are led to the Hall of Justice...", eDialogPic.CREATURE, 9, ["OK"])
    SpecialItem.Take("StolgradDisc")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(28,25))
    p.CancelAction = True
    ChoiceBox("You find yourself standing before Auspire herself! She sits in the throne as your judge. \"We are gathered here to decide the fate of these renegades. The charges are espionage. Would any of you like to speak in your own defense?\"\n\nYou really have nothing to say, so you decline. \"Very well. Garrow, assistant of the Prime Director would like to address the court.\" A young official approaches Auspire\'s table and speaks.\n\n\"It is unfortunate that these promising Imperial Guardians should turn to banditry and betray the Empire. The Prime Director has decided to revoke their status of Imperial Guardians and dishonorably discharge them from the Imperial Army.\n\nThe Emperor places them at your mercy.\" The young official steps down. \"Thank you, Garrow. You are free to depart.\" He does so. Auspire looks at you coldly.\n\n\"Our laws are very clear. The only punishment for espionage in the Stolgrad Sector is death. Your executions will be carried out tomorrow morning. With no objections, I dismiss this court. Guards! Take them away!\"", eDialogPic.CREATURE, 1025, ["OK"])
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(9,53))
    p.CancelAction = True
    ChoiceBox("So now you sit in your cells, awaiting your executions. You look back on a similar time in Azaklan. At least there, you could hope that the Empire would come -- and they did. However, this situation is completely different.\n\nThe Empire has completely turned its back on you. You cannot think of anybody who would bail you out. And why? It is seemingly so foolish. A small child, Sirius, the son of Auspire happened to sneak in at the same time as you!\n\nHad you been a minute later, you would have been in and out with the needed records. And why will the Empire not make any move to help you? Politics, simply politics. So here you sit, victims of chance and politics.\n\nGoing into the Army, you had hoped for careers filled with glory and honors. However, after a short spurt of glory, it all gets taken away because of politics! The records will show you as traitors to the Empire. The truth will never be known.\n\nShould you tell them your real mission. No, that could only make things worse. They would not listen anyway. The Empire would deny any accusations that you could make.\n\nAs your executions approach, you reflect on the times past...", eDialogPic.STANDARD, 1024, ["OK"])
    Timer(Town, 20, False, "ZenithKeep_549_TownTimer_35", eTimerType.DELETE)

def ZenithKeep_546_MapTrigger_8_50(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(8,50)).Num == 78:
        result = ChoiceBox("This portal is your only way out. Cylene is waiting for you to go through. Enter?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            Animation_Hold(-1, 010_teleport)
            Wait()
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(12,54)
            Party.MoveToMap(TownMap.List["Zenith_28"])
            return
        p.CancelAction = True
        return

def ZenithKeep_547_TownTimer_2(p):
    Animation_Hold(-1, 068_identify)
    Wait()
    if StuffDone["9_1"] == 0: StuffDone["9_1"] = 1
    else: StuffDone["9_1"] = 0

def ZenithKeep_548_TownTimer_25(p):
    Animation_Hold(-1, 081_meow)
    Wait()

def ZenithKeep_549_TownTimer_35(p):
    MessageBox("Suddenly, the door opens! Impossible! You swear it is not morning yet. Two figures enter. A beautiful looking young woman and the child who called the alarm on you. They are not accompanied by any guards. You wonder what is up.")
    Town.PlaceEncounterGroup(2)

def ZenithKeep_550_CreatureDeath0(p):
    MessageBox("You were told not to use violence. Well, choosing to go against your orders ended in you being captured by numerous soldiers, quickly tried, and executed. The Empire disavowed any knowledge of your actions.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def ZenithKeep_573_TalkingTrigger8(p):
    if StuffDone["9_4"] == 250:
        return
    StuffDone["9_4"] = 250
    ChoiceBox("\"For too long I have watched this horrid plot unfold. It all started after those two wizards -- a master and his apprentice -- came to speak with mother. He made an offer, promising a return to glory for the order.\n\nLong ago, the order of Odin held the throne, and lost it during a power struggle and since always believed itself to be the rightful rulers of the world. Mother could not pass the offer up, her pride in the order would not allow it.\n\nUncle Raiden did not agree with this plot and managed to discover the identity of the two wizards. He went to the Empire with what he knew. They found out and imprisoned him. They wanted him executed, but I was able to convince mother not to.\n\nNow he is held high atop Mount Bleak in a secret prison. I fear the only way to stop this evil is for someone to rescue him. I was able to read your thoughts. I know not exactly what you were doing in the Records Hall, but I can see you intended good.\n\nI have looked back and heard about your heroic deeds. I know now that if Raiden is to be rescued, you are his only hope. I will grant you your freedom, but you must never return here so long the wizards live.\"\n\nShe casts a spell, a small portal appears. \"This will take you to the outskirts of the city, away from here. Remember, Raiden is trapped on Mount Bleak. I beg of you to rescue him!\"", eDialogPic.CREATURE, 132, ["OK"])
    Town.AlterTerrain(Location(8,50), 0, TerrainRecord.UnderlayList[78])
    Sound.Play(052_magic2)
    StuffDone["9_0"] = 3

def Talking_29_14(p):
    if Party.Gold < 0:
        p.TalkingText = ""
    else:
        Party.Gold -= 0
        Party.Pos = Location(32, 47)
        Town.UpdateVisible()
        Party.HealAll(0, True)
        Party.RestoreSP(0)
        p.TalkingText = "The wizard opens his eyes looking surprised to see you. \"What is it? Who are you?\" He shakes his head realizing that you are not from around here. \"Whoever you are get out!\" He waves a hand and you find yourself somewhere else."
        CentreView(Party.Pos, False)
