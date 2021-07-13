
def RefugeNorthnight_137_MapTrigger_24_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,5)
    Party.MoveToMap(TownMap.List["RefugeSouthnight_5"])

def RefugeNorthnight_138_MapTrigger_24_6(p):
    result = ChoiceBox("\"It\'s an Exile!\" You hear someone shout as you approach the portcullis. \"An Exile?\" You hear, amongst excited murmers. You realise these voices are actually coming from outside. Tens of people are gathering around the outer portcullis, looking in at you.\n\n\"You\'ve got to help us, brother.\" Almost all of them are Exiles, you realise, with a few Sliths and dark-skinned humans as well. \"So they still allow \'Worms\' in there?\" The first Exile questions, surprised. You explain they do, but maybe not for long.\n\n\"Can you get us some food? We\'re starving out here.\" This is certainly no exaggeration. The sight of so many bare ribs, potbellies, haggard faces make you sick.\n\nBut nonetheless you have to explain that you have barely enough food for yourself, that the rationing inside is very strict. \"So they have got food?\" One asks, excitedly. \"Not much\" You respond.\n\nMany of them are by now starting to give up on you, too tired to keep standing. The cries of multitudes of starving children is high in the air. But a few of the young men are persistent, especially the one who first saw you.\n\nHe now asks hopefully, \"Could you let us in, Brother? Come on, your people need you! Please? We\'ll die, many already have. My mother... Please?\" You could easily open the portculli, the lever is just next to you. Do you?", eDialogPic.TERRAIN, 92, ["Open", "Leave"])
    if result == 0:
        MessageBox("Excising all thought that might prevent you, you pull the lever. The triumphant roar from outside is immense, despite the state of the roarers. \"Thankyou, Brother.\" The first man says, clapping you on the back on his way into the city.\n\nWithin an hour the place has been ransacked. The meagre food reserves broken into and shared between hundreds, many killed by those driven mad by hunger and revenge. Soon it is realised that the town is useless, and most leave. You join the Exiles.")
        Scenario.End()
        return
    elif result == 1:
        MessageBox("You shake your head apologetically, and then just turn and leave. Those outside continue to plead with you for some time, then the beggings turn to threats and violent abuse. You just keep on going.")
        return

def RefugeNorthnight_139_MapTrigger_25_19(p):
    if StuffDone["3_1"] >= 1:
        if StuffDone["6_0"] == 250:
            return
        StuffDone["6_0"] = 250
        MessageBox("Well they said they were going to publicise your campaign, but you never expected anything like this..... Tarle and Lerta are by the North wall of the market, having somehow got hold of some paint, scrawling on the wall.\n\nYou can\'t work out what it\'s going to say yet, but it\'s certainly going to say it loudly. \"Hello!\" Lerta calls, seeing you. \"What do you think?\"")
        return

def RefugeNorthnight_140_MapTrigger_7_13(p):
    if StuffDone["6_1"] == 250:
        return
    StuffDone["6_1"] = 250
    TownMap.List["RefugeNorthnight_3"].DeactivateTrigger(Location(7,13))
    MessageBox("Cody is sitting there, in front of that central sigil. Looking more closely you can see that he is actually asleep. The sigil itself is, you notice now it is dark, glowing slightly, providing the room with an eerily dim light.\n\nBut even weirder than that is the contents of the room. Row upon row of strange glass bottles, many filled with exotic coloured liquids. Odder still is the counter along one wall - it\'s distinctly slanted! One end is actually higher than the other.")

def RefugeNorthnight_141_MapTrigger_9_10(p):
    MessageBox("You are about to step on the glowing rune, but caution stops you. Long and painful years at the Tower of Magi taught you NEVER to mess with strange magicks you don\'t understand.")
    p.CancelAction = True

def RefugeNorthnight_142_MapTrigger_7_28(p):
    if StuffDone["2_7"] == 250:
        return
    StuffDone["2_7"] = 250
    TownMap.List["RefugeNorth_1"].DeactivateTrigger(Location(7,28))
    TownMap.List["RefugeNorthnight_3"].DeactivateTrigger(Location(7,28))
    MessageBox("Massive. You can think of absolutely no other word to describe this place, with its gleaming white face towering above, and with a door so imposing and ornate you actually feel yourself cowering there before it.\n\nRighting yourself, you enter.")

def RefugeNorthnight_143_MapTrigger_5_18(p):
    if StuffDone["2_9"] >= 1:
        MessageBox("You\'ve already taken your fill from this box of goodies, and you feel if you open the chest again you might just stick your head in it and drown in food, glorious food. So you don\'t.")
        return
    if StuffDone["2_9"] < 1:
        StuffDone["2_8"] = 1
        result = ChoiceBox("You open the huge chest, here in this hidden extension to the house. Oddly, it\'s unlocked - probably no-one expected it to be found.\n\nYou open it, slowly so as not to allow it to creak, and find treasure beyond your wildest dreams within.\n\nFood! Glorious, edible food! Salted meets! Fruit conserves! All sorts of tasty, durable nutrition.\n\nThey must have been hoarding this here, and eating this stuff while the rest of us have to eat the paltry rations. And not telling anyone! It makes you sick, it makes you mad.\n\nAnd it makes you hungry. But before you think about that, you decide that the authorities MUST be told about this. It shouldn\'t be allowed, and you sincerely hope it\'s not.\n\nNow back to your stomach. You are sorely tempted to take some of this. They\'ve got far more than enough, after all, and they\'d probably never know. Just enough to get you through the next few days without rations.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
        if result == 0:
            MessageBox("You stuff your pockets, taking food from nearer the bottom of the chest so your theivery won\'t be too noticeable.\n\nYou think you hear footsteps from somewhere in the house - you\'d better get out before you\'re noticed.")
            Party.Food += 20
            StuffDone["2_9"] = 1
            return
        elif result == 1:
            MessageBox("It takes a great strength of will to close the  lid on temptation, but you manage. You can\'t really go around stealing - that\'s just as bit as what they\'re doing.")
            return
        return

def RefugeNorthnight_144_MapTrigger_24_40(p):
    if StuffDone["3_5"] >= 1:
        Town.AlterTerrain(Location(25,14), 0, TerrainRecord.UnderlayList[254])
        Town.AlterTerrain(Location(24,14), 0, TerrainRecord.UnderlayList[253])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Lerta_193": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Tarle_194": Town.NPCList.Remove(npc)
        if StuffDone["6_2"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
            Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
            if StuffDone["12_1"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                return
            return
        if StuffDone["12_1"] >= 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
            return
        return
    if StuffDone["3_5"] < 1:
        if StuffDone["3_1"] >= 1:
            Town.AlterTerrain(Location(24,14), 0, TerrainRecord.UnderlayList[253])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Tarle_197": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Lerta_198": Town.NPCList.Remove(npc)
            if StuffDone["6_2"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
                Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
                if StuffDone["12_1"] >= 1:
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                    return
                return
            if StuffDone["12_1"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                return
            return
        if StuffDone["3_1"] < 1:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Lerta_193": Town.NPCList.Remove(npc)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Tarle_194": Town.NPCList.Remove(npc)
            if StuffDone["6_2"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
                Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
                if StuffDone["12_1"] >= 1:
                    for n in range(Town.NPCList.Count-1, -1, -1):
                        npc = Town.NPCList[n]
                        if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                    return
                return
            if StuffDone["12_1"] >= 1:
                for n in range(Town.NPCList.Count-1, -1, -1):
                    npc = Town.NPCList[n]
                    if npc.Record.ID == "Jonathan_196": Town.NPCList.Remove(npc)
                return
            return
        return

def RefugeNorthnight_147_MapTrigger_39_42(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if p.Origin == eCallOrigin.SEARCHING: return
    RunScript("GlobalCall_RefugeNorthnight_253", ScriptParameters(eCallOrigin.CUSTOM))
    result = ChoiceBox("You stand behind the strange Vahnatai-style chair in which Cody sits.\n\nIn front of that deadly rune.\n\nIt would, you find yourself thinking, be an easy matter to get rid of this particular Nash voter.\n\nA quick push of the chair, the man would be thrown towards the rune. His own creation would do the rest.\n\nNo evidence.\n\nThe perfect crime.", eDialogPic.CREATURE, 2, ["Push", "No"])
    if result == 0:
        MessageBox("You grab the top of the chair and jerk it forwards. Cody topples towards the rune. You fall to the floor, the chair on top of you, in recoil from the blinding flash the man produces.\n\nFor a few agonising seconds you lie on the floor, the image of a falling man, shining with the light of a million suns, imprinted on your eyes.")
        MessageBox("Shaking your head clear, you get up. You put the chair back where it was. You listen for movement - the man\'s annihilation was itself soundless, but your reaction was not. You hear nothing.\n\nStill disorientated, you search the room for any evidence of the deed. None. Except - the rune\'s glow is now distinctly brighter. You sigh heavily, then leave. This is done.")
        StuffDone["6_2"] = 1
        StuffDone["100_1"] -= 1
        if StuffDone["100_1"] == 250:
            pass
        Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
        return
    elif result == 1:
        MessageBox("NO! You can\'t believe you were actually thinking of murder! Although misguided, this is a sweet old man in front of you.\n\nYou shake your head at yourself and leave.")
        return
    if StuffDone["6_2"] >= 1:
        return
    if StuffDone["6_2"] < 1:
        RunScript("Loopback_51_0", p)
        return

def RefugeNorthnight_149_MapTrigger_9_8(p):
    if StuffDone["6_2"] >= 1:
        return
    if StuffDone["6_2"] < 1:
        result = ChoiceBox("You stand behind the strange Vahnatai-style chair in which Cody sits.\n\nIn front of that deadly rune.\n\nIt would, you find yourself thinking, be an easy matter to get rid of this particular Nash voter.\n\nA quick push of the chair, the man would be thrown towards the rune. His own creation would do the rest.\n\nNo evidence.\n\nThe perfect crime.", eDialogPic.CREATURE, 2, ["Push", "No"])
        if result == 0:
            MessageBox("You grab the top of the chair and jerk it forwards. Cody topples towards the rune. You fall to the floor, the chair on top of you, in recoil from the blinding flash the man produces.\n\nFor a few agonising seconds you lie on the floor, the image of a falling man, shining with the light of a million suns, imprinted on your eyes.")
            MessageBox("Shaking your head clear, you get up. You put the chair back where it was. You listen for movement - the man\'s annihilation was itself soundless, but your reaction was not. You hear nothing.\n\nStill disorientated, you search the room for any evidence of the deed. None. Except - the rune\'s glow is now distinctly brighter. You sigh heavily, then leave. This is done.")
            StuffDone["6_2"] = 1
            StuffDone["100_1"] -= 1
            if StuffDone["100_1"] == 250:
                pass
            Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
            return
        elif result == 1:
            MessageBox("NO! You can\'t believe you were actually thinking of murder! Although misguided, this is a sweet old man in front of you.\n\nYou shake your head at yourself and leave.")
            return
        RunScript("RefugeNorthnight_149_MapTrigger_9_8", p)
        return

def RefugeNorthnight_157_MapTrigger_38_18(p):
    if StuffDone["6_3"] == 250:
        return
    StuffDone["6_3"] = 250
    TownMap.List["RefugeNorthnight_3"].DeactivateTrigger(Location(38,18))
    MessageBox("This is Jonathan\'s room, which it looks like you\'ve managed to break into without waking it\'s occupant. His snoring is gentle, though, so he might not be deeply asleep. Better do whatever you\'re doing here quickly and get out.")

def RefugeNorthnight_158_MapTrigger_39_21(p):
    if SpecialItem.PartyHas("Scrap"):
        if StuffDone["12_1"] >= 1:
            return
        if StuffDone["6_4"] == 250:
            return
        StuffDone["6_4"] = 250
        MessageBox("On a hunch, you search quietly through Jonathan\'s dresser in search of a red cloak. After a painstaking but fruitless search, you stand up.\n\nAnd see it hanging in the corner. Doh! You examine it closely. Looking closely at the hem, you can see that it WAS torn, but then repaired! Looks like Jonathan IS the one with it in for you!")
        if SpecialItem.PartyHas("HealingSceptre"):
            return
        if StuffDone["6_6"] == 250:
            return
        StuffDone["6_6"] = 250
        MessageBox("On a hunch, you search the dresser for your stolen staff. No luck. You widen your search to the rest of the room, but to no avail. Either it wasn\'t Jonathan who stole it, or he\'s hidden it more carefully than you expected.")
        return
    if SpecialItem.PartyHas("HealingSceptre"):
        return
    if StuffDone["6_6"] == 250:
        return
    StuffDone["6_6"] = 250
    MessageBox("On a hunch, you search the dresser for your stolen staff. No luck. You widen your search to the rest of the room, but to no avail. Either it wasn\'t Jonathan who stole it, or he\'s hidden it more carefully than you expected.")

def RefugeNorthnight_159_MapTrigger_36_18(p):
    if StuffDone["6_5"] == 250:
        return
    StuffDone["6_5"] = 250
    TownMap.List["RefugeNorthnight_3"].DeactivateTrigger(Location(36,18))
    MessageBox("This must be Nash\'s room. You search it carefully, but find nothing of interest.")

def RefugeNorthnight_160_CreatureDeath0(p):
    RunScript("GlobalCall_RefugeSouth_247", ScriptParameters(eCallOrigin.CUSTOM))
    if StuffDone["2_4"] >= 2:
        return
    if StuffDone["2_4"] < 1:
        MessageBox("\"Right. Here you go,\" He says, business-like, handing you some indescriminate foodstuffs. He writes your name down on the list in front of him.\n\n\"Not exactly \'haute cuisine\' I know, but it\'s all we\'ve got left.\"")
        Party.GiveNewItem("Emergencyrations_383")
        StuffDone["2_4"] = 1
        return

def Loopback_51_0(p):
    result = ChoiceBox("You stand behind the strange Vahnatai-style chair in which Cody sits.\n\nIn front of that deadly rune.\n\nIt would, you find yourself thinking, be an easy matter to get rid of this particular Nash voter.\n\nA quick push of the chair, the man would be thrown towards the rune. His own creation would do the rest.\n\nNo evidence.\n\nThe perfect crime.", eDialogPic.CREATURE, 2, ["Push", "No"])
    if result == 0:
        MessageBox("You grab the top of the chair and jerk it forwards. Cody topples towards the rune. You fall to the floor, the chair on top of you, in recoil from the blinding flash the man produces.\n\nFor a few agonising seconds you lie on the floor, the image of a falling man, shining with the light of a million suns, imprinted on your eyes.")
        MessageBox("Shaking your head clear, you get up. You put the chair back where it was. You listen for movement - the man\'s annihilation was itself soundless, but your reaction was not. You hear nothing.\n\nStill disorientated, you search the room for any evidence of the deed. None. Except - the rune\'s glow is now distinctly brighter. You sigh heavily, then leave. This is done.")
        StuffDone["6_2"] = 1
        StuffDone["100_1"] -= 1
        if StuffDone["100_1"] == 250:
            pass
        Town.AlterTerrain(Location(9,10), 0, TerrainRecord.UnderlayList[236])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Cody_195": Town.NPCList.Remove(npc)
        return
    elif result == 1:
        MessageBox("NO! You can\'t believe you were actually thinking of murder! Although misguided, this is a sweet old man in front of you.\n\nYou shake your head at yourself and leave.")
        return
    if StuffDone["6_2"] >= 1:
        return
    if StuffDone["6_2"] < 1:
        RunScript("Loopback_51_0", p)
        return
