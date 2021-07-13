
def RefugeSouthnight_178_MapTrigger_38_43(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if p.Origin == eCallOrigin.SEARCHING: return
    RunScript("GlobalCall_RefugeSouthnight_257", ScriptParameters(eCallOrigin.CUSTOM))

def RefugeSouthnight_179_MapTrigger_23_29(p):
    if StuffDone["4_1"] < 2:
        if StuffDone["4_3"] == 250:
            return
        StuffDone["4_3"] = 250
        MessageBox("Ah, a cunning idea - get the well armed guards in here to deal with your assassins. You wake them up with a few calls and quickly explain. \"OK,\" one says nervously, speaking for the rest. \"But you understand we can\'t move from our posts here.\"\n\n\"We\'re being paid very good money not to. No. You bring \'em in here and we\'ll deal with them alright.\"")
        return

def RefugeSouthnight_181_MapTrigger_30_31(p):
    if StuffDone["4_1"] < 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("There\'s no point in trying to run away - these young men could easily outrun an old cripple like you.")
        return

def RefugeSouthnight_185_MapTrigger_9_19(p):
    RunScript("GlobalCall_RefugeSouth_241", ScriptParameters(eCallOrigin.CUSTOM))
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Assassin_35": Town.NPCList.Remove(npc)

def RefugeSouthnight_190_MapTrigger_32_42(p):
    if StuffDone["4_5"] >= 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Yep. They\'re still at it, despite their knowledge of your knowledge. Young love, eh? You leave them to it.")
        return
    if StuffDone["4_5"] < 1:
        MessageBox("You open the end door quietly to discover two people in a lovers\' embrace. Aaah. Isn\'t that sweet. And it would explain the whispers as well. You try to back up through the short tunnel without disturbing them. But your foot catches on something.\n\nHearing your scrabblings, they turn to you as one, the fear of discovery on their face. Then you see who they are. Cilla, and Mike. The married, friendly innkeeper and the awful poet. You see now why they chose to meet here.")
        MessageBox("Cilla\'s eyes widen in recognition. \"Vandell!\" She whispers loudly. \"Please, Vandell, just leave us. We can talk about this tomorrow. And please, please don\'t tell Cyril. Please?\" You promise nothing but leave nonetheless. Intriguing.")
        StuffDone["4_5"] = 1
        return

def RefugeSouthnight_191_MapTrigger_26_35(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["200_0"] >= 1:
        if StuffDone["4_2"] >= 2:
            if StuffDone["4_4"] == 250:
                return
            StuffDone["4_4"] = 250
            MessageBox("You move about in your room. Suddenly, you stop walking. You thought you heard voices again. There they are! They seem  to be coming from outside, from the window, and yet also from the South, from Cilla and Cyril\'s room. Very odd.")
            if StuffDone["2_3"] == 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                return
            return
        if StuffDone["4_2"] < 2:
            return
        if StuffDone["2_3"] == 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
            return
        return
    if StuffDone["200_0"] < 1:
        if StuffDone["4_1"] >= 2:
            if StuffDone["4_2"] >= 2:
                if StuffDone["4_4"] == 250:
                    return
                StuffDone["4_4"] = 250
                MessageBox("You move about in your room. Suddenly, you stop walking. You thought you heard voices again. There they are! They seem  to be coming from outside, from the window, and yet also from the South, from Cilla and Cyril\'s room. Very odd.")
                if StuffDone["2_3"] == 1:
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                    return
                return
            if StuffDone["4_2"] < 2:
                return
            if StuffDone["2_3"] == 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                return
            return
        if StuffDone["4_1"] < 2:
            if StuffDone["4_0"] == 250:
                return
            StuffDone["4_0"] = 250
            MessageBox("Just as you get out of bed in the darkness you think you hear a gentle hissing. You realise what it is before it has a chance to get to you - that was a gas bomb thrown in here! Someone really wants you outside.\n\nYou run out of the room, closing the door behind you.")
            for x in range(36, 31):
                for y in range(25, 37):
                    Town.PlaceField(Location(x,y), Field.SLEEP_CLOUD)
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(24,35))
            p.CancelAction = True
            if StuffDone["2_3"] == 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                return
            return
        return

def RefugeSouthnight_193_MapTrigger_15_6(p):
    MessageBox("Here the floor slopes steeply, forming the method of access from the city below to the ramparts above.")

def RefugeSouthnight_194_MapTrigger_24_4(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,42)
    Party.MoveToMap(TownMap.List["RefugeNorthnight_3"])

def RefugeSouthnight_196_MapTrigger_15_18(p):
    if StuffDone["0_6"] == 250:
        return
    StuffDone["0_6"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(15,18))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(15,18))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(15,18))
    MessageBox("Ah. The library. You\'ve been meaning to come in here ever since you arrived at the town a week ago, but until now hadn\'t got round to it. You can see now that this is an extremely old building - probably as old as the town itself.\n\nBut it looks like it\'s being taken good care of - the floor\'s clean if cracked, and you can see a variety of techniques have been used to cover up the holes in the crumbling walls. Indeed, it reminds you in many ways of your old home at Silvar, Exile.")

def RefugeSouthnight_198_MapTrigger_22_5(p):
    if StuffDone["0_7"] >= 1:
        MessageBox("You barely have the strengh to push this lever, and it makes very slow going. As you push, you can both feel and hear the portcullus outside slowly working its way up. Once it is completely open you experimentally release the force. The mechanism holds.")
        StuffDone["0_7"] = 0
        t = Town.TerrainAt(Location(24,6)).TransformTo
        Town.AlterTerrain(Location(24,6), 0, t)
        return
    MessageBox("You pull the lever towards you. At first it seems to be stuck, but as you strain harder you can hear the mechanism beginning to give way. Another tug and the lever accelerates towards you and hits you squarely in the chest as the portcullus crashes shut.")
    StuffDone["0_7"] = 1
    t = Town.TerrainAt(Location(24,6)).TransformTo
    Town.AlterTerrain(Location(24,6), 0, t)

def RefugeSouthnight_199_MapTrigger_16_17(p):
    if StuffDone["50_1"] >= 1:
        if StuffDone["0_9"] == 250:
            return
        StuffDone["0_9"] = 250
        MessageBox("You leave the library, happy with the successful conversion of another voter, when you suddenly realise that Cornelius wasn\'t at that preliminary meeting and so isn\'t elegible to vote. Hmmm. Better ask Gwyneth about the matter.")
        return

def RefugeSouthnight_202_MapTrigger_39_34(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(39,34))
    TownMap.List["RefugeSouthnight_2"].DeactivateTrigger(Location(39,34))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(39,34))
    MessageBox("Hmmm. No one told you about this. The Mayor\'s job is looking better and better. Looks like this place is a perk of the job, and a very nice perk it is too. Very plush, though the ornate pillars are maybe a bit too much.")

def RefugeSouthnight_204_MapTrigger_6_13(p):
    RunScript("GlobalCall_RefugeSouth_246", ScriptParameters(eCallOrigin.CUSTOM))

def RefugeSouthnight_205_MapTrigger_34_22(p):
    if StuffDone["4_7"] == 250:
        return
    StuffDone["4_7"] = 250
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(34,22))
    MessageBox("You look through Mike\'s poetry, now he\'s not here to stop you. He\'s certainly written a lot of stuff. Shame it\'s all terrible, though. You pick one at random. \"I guess/I guess it is just a stupid guess/I guess it\'s just a another guess/I guess.\"\n\nBrilliant. You do find some stuff here of real interest, though - a collection of love poems, all addressed to Cilla! You decide to take one to read later.")
    SpecialItem.Give("Awfullovepoem")

def RefugeSouthnight_206_MapTrigger_37_25(p):
    MessageBox("You take a look at a few of the titles on these shelves. \"How to be a Poet in Ten Easy Steps\". \"Cut\'n\'Paste Similes and Metephors (now anyone can be a poet!)\". A well-thumbed dictionary. A never-thumbed Encyclopedia Imperatus. You can bear no more.")

def RefugeSouthnight_207_MapTrigger_6_39(p):
    if StuffDone["1_1"] == 250:
        return
    StuffDone["1_1"] = 250
    TownMap.List["RefugeSouth_0"].DeactivateTrigger(Location(6,39))
    TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(6,39))
    MessageBox("Now this is a shameful sight. Tucked away in the corner of the town, hidden from common view like some facial eruption self-consciously covered by its owner\'s stray hand. From outside you could see the cracked, moldy walls.\n\nAnd looking inside you can see that much of the floor of this ancient, shameful site is damaged or missing. Rats scurry around shadowy recesses of the place. And then, oh, you feel sick. A rat the size of which rivals Exile\'s worst lurches into view.")
    Town.PlaceNewNPC(NPCRecord.List["CaveRat_78"], Location(6,35), True)

def RefugeSouthnight_208_MapTrigger_24_34(p):
    if StuffDone["200_0"] >= 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Assassin_35": Town.NPCList.Remove(npc)
        return
    if StuffDone["200_0"] < 1:
        if StuffDone["4_2"] == 250:
            return
        StuffDone["4_2"] = 250
        MessageBox("You open the door, still high from the rush of the flight, only to see the two out-of-towners you saw in the inn earlier. They draw their weapons and start circling you.\n\nThey seem pretty quick on their feet, and you think you see the slick glint of liquid on one of their blades. \"Come on then, worm. Time to die, worm,\" One says, sneeringly.")
        return

def RefugeSouthnight_209_MapTrigger_24_7(p):
    if StuffDone["2_3"] == 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
        return

def RefugeSouthnight_212_MapTrigger_32_41(p):
    if StuffDone["1_5"] >= 1:
        if StuffDone["1_6"] == 250:
            return
        StuffDone["1_6"] = 250
        MessageBox("You search the South end of this dead-end alley, just where the smugglers\' entrance is meant to be, and sure enough a push of a brick, the pull of a handle reveals a narrow tunnel. You crawl into it, shutting the door behind you.")
        return
    p.CancelAction = True

def RefugeSouthnight_213_MapTrigger_32_34(p):
    if StuffDone["200_0"] >= 1:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Assassin_35": Town.NPCList.Remove(npc)
        return

def RefugeSouthnight_216_MapTrigger_28_35(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["200_0"] >= 1:
        RunScript("GlobalCall_RefugeSouthnight_256", ScriptParameters(eCallOrigin.CUSTOM))
        return
    if StuffDone["200_0"] < 1:
        if StuffDone["4_1"] >= 2:
            if StuffDone["4_2"] >= 2:
                if StuffDone["4_4"] == 250:
                    return
                StuffDone["4_4"] = 250
                MessageBox("You move about in your room. Suddenly, you stop walking. You thought you heard voices again. There they are! They seem  to be coming from outside, from the window, and yet also from the South, from Cilla and Cyril\'s room. Very odd.")
                if StuffDone["2_3"] == 1:
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                    return
                return
            if StuffDone["4_2"] < 2:
                return
            if StuffDone["2_3"] == 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                return
            return
        if StuffDone["4_1"] < 2:
            if StuffDone["4_0"] == 250:
                return
            StuffDone["4_0"] = 250
            MessageBox("Just as you get out of bed in the darkness you think you hear a gentle hissing. You realise what it is before it has a chance to get to you - that was a gas bomb thrown in here! Someone really wants you outside.\n\nYou run out of the room, closing the door behind you.")
            for x in range(36, 31):
                for y in range(25, 37):
                    Town.PlaceField(Location(x,y), Field.SLEEP_CLOUD)
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(24,35))
            p.CancelAction = True
            if StuffDone["2_3"] == 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "MayorVogel_188": Town.NPCList.Remove(npc)
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Gwyneth_190": Town.NPCList.Remove(npc)
                return
            return
        return

def RefugeSouthnight_222_MapTrigger_25_36(p):
    if StuffDone["4_1"] < 2:
        if StuffDone["200_0"] >= 1:
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You don\'t want to go back in that gas-filled room - who knows what toxic effects it might have?")
        return

def RefugeSouthnight_223_MapTrigger_25_40(p):
    if StuffDone["4_1"] >= 2:
        if StuffDone["4_8"] == 250:
            return
        StuffDone["4_8"] = 250
        MessageBox("You enter Cilla and Cyril\'s room quietly, expecting to find them asleep in bed. Instead, you find Cyril asleep in bed. Cilla is nowhere to be found. You can\'t help but wonder where she\'s gone.\n\nAnd then you hear the whispers again. They seem to be coming from the South, through the wall, but also from the East, through the window.")
        return
    if StuffDone["4_1"] < 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You come in, hoping to get Cilla and Cyril to help you. You can only find Cyril, asleep on the bed. You try to wake him, explain the problem.\n\n\"Go away, Exile. I need to sleep.\" He murmurs sleepily before burying his face deep in the cushions. You give up and return to the main part of the inn to face the threat alone.")
        return

def RefugeSouthnight_224_CreatureDeath0(p):
    StuffDone["4_1"] += 1
    if StuffDone["4_1"] == 250:
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(23,29))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(25,29))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(30,31))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(30,30))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(30,32))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(30,33))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(18,30))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(18,31))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(18,32))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(18,33))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(25,36))
        TownMap.List["RefugeSouthnight_5"].DeactivateTrigger(Location(25,40))
    if StuffDone["4_1"] >= 2:
        MessageBox("Blood still pounding in your ears, you sit down. That was close, you have to admit. You search the bodies for any clues as to why they might be attacking you, but find nothing.\n\nAll you know is that they were those two you saw in the inn earlier today, and that they called you a Worm. Not much to go on. You have a quick look through the window of your room - looks like it\'s safe to go back in now.")
        for x in range(25, 31):
            for y in range(35, 37):
                Town.DispelFields(Location(x,y), 2)
        return
    if StuffDone["4_1"] < 0:
        return

def RefugeSouthnight_225_CreatureDeath3(p):
    RunScript("GlobalCall_RefugeSouth_247", ScriptParameters(eCallOrigin.CUSTOM))
    if StuffDone["200_0"] >= 1:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You don\'t want to go back in that gas-filled room - who knows what toxic effects it might have?")
