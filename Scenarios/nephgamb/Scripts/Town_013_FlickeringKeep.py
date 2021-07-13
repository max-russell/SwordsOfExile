
def FlickeringKeep_289_MapTrigger_28_13(p):
    if StuffDone["13_4"] >= 1:
        return
    result = ChoiceBox("You present yourselves to the guards and ask to be taken to the ruler of the castle. The guards take stock of you. \"Lord Fray is not in residence,\" one says gruffly, \"but the Lady is having supper in the Hall of Flickers. I can take you to her.\"", eDialogPic.CREATURE, 14, ["Leave", "Step In"])
    if result == 1:
        MessageBox("The guard reluctantly opens a door and ushers you into a dark hallway. \"Follow me!\" he mutters and starts down the passage.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(28,15))
        p.CancelAction = True
        return

def FlickeringKeep_292_MapTrigger_23_21(p):
    if StuffDone["200_0"] >= 1:
        if StuffDone["13_0"] == 250:
            return
        StuffDone["13_0"] = 250
        result = ChoiceBox("In the shadows between two torches, you suddenly think you see movement. You turn your heads, and feel drawn to a dark corner in the hallway. Further down, the surly guard calls for you to follow him. Do you stop and examine?", eDialogPic.CREATURE, 127, ["Approach", "Onward"])
        if result == 0:
            MessageBox("You approach the dim corner, shadows shifting as you move. Suddenly, the shadows shape into the outline of a face.\"You are in great danger!\" a faint voice whispers. \"Come see me in the temple tonight!\"\n\nYou all recognize the shape and the fleeting voice, and meekly discuss the event as you hurry to overtake your guard. It was Karolynna. Afterwards, as one of you chances to put a hand in a pocket, you find a small key. You have no idea how it got there.")
            SpecialItem.Give("Ghostlykey")
            return
        elif result == 1:
            return
        return

def FlickeringKeep_295_MapTrigger_19_30(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("An old manservant guards these narrow stairs linking the Hall and the private rooms. When you approach, he stands to block your way. Only direct orders from Lord Fray will allow you to pass. The man seems unaware that Fray died ten years ago.")

def FlickeringKeep_296_MapTrigger_31_38(p):
    if StuffDone["13_3"] >= 1:
        MessageBox("You shudder as you recognize the scene of your nightmare. Even worse, you find your gear lying in little piles of ashes on the floor!")
        return

def FlickeringKeep_297_MapTrigger_27_22(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You hear a whining voice: \"Rashtarra?s orders are explicit. Nobody is allowed into Whitstone except in the company of the Frays!\" You cannot enter.")

def FlickeringKeep_298_MapTrigger_21_7(p):
    if StuffDone["63_0"] == 250:
        return
    StuffDone["63_0"] = 250
    TownMap.List["FlickeringKeep_13"].AlterTerrain(Location(21,7), 1, None)
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(21,7))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(8,27))
    MessageBox("Strong winds assault you as you climb up onto the ramparts. The drop down appears bottomless. Far, far down there lie the slith lands. You steady yourselves towards the wall and avoid looking into the abyss.")

def FlickeringKeep_300_MapTrigger_24_34(p):
    if StuffDone["13_4"] >= 1:
        if StuffDone["13_8"] == 250:
            return
        StuffDone["13_8"] = 250
        MessageBox("Entering the temple, you come across Lady Fray, dressed for combat. She kneels before the altar with her back towards you, and apparently has not heard you enter.")
        Town.PlaceEncounterGroup(1)
        return
    if StuffDone["13_5"] == 250:
        return
    StuffDone["13_5"] = 250
    MessageBox("You shove open the door and look one more time over your shoulder. Then you enter the dimly lit temple. Much of the light comes from a glowing shape standing next to the altar. You approach warily, expecting a trap. Suddenly the glow shapes into a vision.\n\nKarolynna?s face looks out at you from the mist. \"You must be steadfast tonight, whatever happens. Remember this, for bravery will win the day. Falter, and you may never see me again!\" She looks away, as if something distracts her, then disappears.")

def FlickeringKeep_301_MapTrigger_15_33(p):
    if StuffDone["13_1"] == 250:
        return
    StuffDone["13_1"] = 250
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(15,33))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(16,33))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(17,33))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(18,33))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(19,33))
    ChoiceBox("The old guard leads you to a set of heavy doors and bows you into a lofty hall, draped in shadows.\n\nAt this hour, the room is full of people having supper, but the Hall of Flickers is still only half lit. Servants walk on soft slippers to serve whispering soldiers and retainers, making the whole scene look almost ghostly.\n\nThe sombre mood is increased by a strange tableau at the end of the Hall. A row of pillars lead up to a seat of honour, raised above the other tables.\n\nAn imposing throne has been placed with its back to the room, facing instead an open portcullis. Wind blows into the room, making shadows chase one another as the torches flicker.\n\nFor outside the portcullis is darkness. Nothing, except an eight hundred meter drop.\n\nYou stop to gape in the doorway, and silence falls completely in the room. The guard prods you, and points to a figure seated alone in the other end of the Hall. Lady Fray beckons.", eDialogPic.TERRAIN, 144, ["OK"])

def FlickeringKeep_302_MapTrigger_23_35(p):
    if StuffDone["13_4"] >= 1:
        if StuffDone["13_9"] == 250:
            return
        StuffDone["13_9"] = 250
        Town.AlterTerrain(Location(23,38), 0, TerrainRecord.UnderlayList[213])
        Animation_Hold(-1, 054_scream)
        Wait()
        Town.MakeTownHostile()
        return

def FlickeringKeep_305_MapTrigger_34_23(p):
    if StuffDone["13_4"] >= 1:
        return
    result = ChoiceBox("Lord Fray?s great bed is the momentous centrepiece of the room, big enough to allow rest for all six of you. It would have been a lot more comfortable without the statue of the late Lord Fray looming over you.\n\nYou aren?t sure if you dare sleep with the vengeful spirit glaring at you.", eDialogPic.TERRAIN, 143, ["Leave", "Rest"])
    if result == 1:
        MessageBox("Exchanging wary glances, you settle into the large bed and try in vain to rest. The flickering lights, minute noises and the accusing stare of the statue deny you sleep. You feel the hours pass in silence, waiting for something terrible to happen.")
        Town.NPCList.Clear()
        MessageBox("When it happens, it catches you unawares, shaking you out of a light doze. War horns sound from the battlements, followed by shouts, cries and rattling armour. The door is flung up by a steward, calling for you to help defend the castle.\n\nHurriedly donning your equipment, you burst into the corridor along with other soldiers. Nobody knows what is going on, but you follow the general surge through the Hall up onto the parapets. A frightening attack is taking place.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(31,40))
        p.CancelAction = True
        result = ChoiceBox("You stand at a high curtain wall placed on the very edge of the ledge. Outside the parapet is a bottomless drop into darkness. The defence should be impregnable from this side.\n\nStill, the wall is being stormed. Scaling ladders and hooks are continuously thrown over the wall, and hundreds of sliths climb out of the darkness to assault the fort.\n\nPanicking soldiers try to throw the ladders back, and confused officers do their best to keep the attackers out. They might succeed, except for the attacks of a giant Drake Lord, harassing the defenders with its fiery breath.\n\nAs you watch, a soldier climbs the tallest tower on the wall and fires an arrow at the Drake. It clatters off the scaly hide of the monster, and it turns its horned head at the him. He falls in a ball of flame, landing on top of a pile of defenders.\n\nYou look at the charred victims of the Drake Lord and at the fires spreading around the monster. There is only one way you can save the brave defenders. You must climb the tower and defy the lizard. You know it might cost you your life.\n\nDo you?", eDialogPic.CREATURE, 144, ["Climb", "Flee"])
        if result == 0:
            pc = SelectPCBox("Select a member of your party:",True)
            if pc == None:
                ChoiceBox("\"This is not our battle,\" you think, \"it is foolish to risk all in this encounter when our skills are desperately needed elsewhere.\" So you hold back, leaving the Drake to rampage freely over the battlements.\n\nYou avert your eyes as soldiers are burned by the dozens, close your ears to the wails of the frightened civilians covering in the courtyard. You step back as roaring flames engulf the parapets, and suddenly all goes silent.\n\nThe flames die, leaving the wall empty of both defenders and attackers. Only the Drake, circling the walls and roaring in triumph remains. \"I won the bet!\" it laughs. \"Admit it, your heroes failed you!\"\n\n\"I do, Rashtarra.\" a familiar voice sighs behind you. You whirl and meet the grim smile of Karolynna. \"I have lost the right to speak to you. I counted on your courage to outweigh your caution. The demon holding me captive tricked me.\"\n\n\"Enough!\" the Drake roars, and Karolynna fades away. Great clouds of smoke stream from the nostrils of the great lizard as it laughs with scorn. \"Cowards!\"\n\nYou feel weak.", eDialogPic.CREATURE, 127, ["OK"])
                for pc in Party.EachAlivePC():
                    pc.AwardXP(-15)
                for pc in Party.EachAlivePC():
                    if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:
                        pc.LifeStatus = eLifeStatus.ALIVE
                MessageBox("You wake to find yourselves wet and trembling, but alive, back in the great bed. Going back to sleep is out of the question. You rise and find that the equipment of those of you who \"died\" is gone!\n\nYou discuss the events of the dream as little as possible, trying to lay the experience quickly behind you.")
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(34,23))
                p.CancelAction = True
                SuspendMapUpdate()
                for x in range(6, 35):
                    for y in range(27, 35):
                        t = Town.TerrainAt(Location(x,y))
                        t = t.GetUnlocked()
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                StuffDone["13_4"] = 1
                return
            MessageBox("You throw yourself forward and climb the stairs in three bounds, shouting at the flying lizard. It turns towards you, hovering well outside your range. Then fire sprouts around you, and you fall to join the growing pile of valiant corpses.")
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
            StuffDone["13_3"] += 1
            if StuffDone["13_3"] == 250:
                TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(31,38))
            if StuffDone["13_3"] >= 5:
                ChoiceBox("Fighting panic, you prepare for the final sacrifice. Standing alone at the parapet, you take a last look at the scene before following your friends in their last, hopeless  battle. \"So this is the end.\" you think. \"Why just here?\"\n\nBut as you look over the wall, you see no more slith attackers. The defenders are also gone, leaving the curtain wall empty and deadly silent after the commotion of the battle. The Drake looks down at you and roars in fury, but does not attack.\n\n\"I won the bet. Now leave us alone!\" The voice rings through the darkness, and the Drake roars again, but flies off. \"Dealing with demons is tricky business,\" a familiar voice says behind you. \"It?s so much easier by sword point.\"\n\nKarolynna leans over the breastworks next to you. \"I?m sorry you had to go through all this, but it was the only way. It amused him, and he doesn?t realize how dangerous you are. Yet.\" She grabs your shoulder.\n\n\"Listen well, for you must relay this to your friends, when they rejoin you. I am held prisoner by the haakai Rashtarra. He has taken control of this household. You must free me, for I hold evidence that will sway the outcome of this entire war!\n\n\"There is an amulet. Lady Fray owns it, and she too is charmed by the demon. And a key, somewhere in Myldres. Find these, then come to me, below the ruins of Whitstone! Now leave this place. But beware Lady Fray! She means you no good!\"", eDialogPic.CREATURE, 127, ["OK"])
                pc.AwardXP(20)
                for pc in Party.EachAlivePC():
                    if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:
                        pc.LifeStatus = eLifeStatus.ALIVE
                MessageBox("You wake to find yourselves wet and trembling, but alive, back in the great bed. Going back to sleep is out of the question. You rise and find that the equipment of those of you who \"died\" is gone!\n\nYou discuss the events of the dream as little as possible, trying to lay the experience quickly behind you.")
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(34,23))
                p.CancelAction = True
                SuspendMapUpdate()
                for x in range(6, 35):
                    for y in range(27, 35):
                        t = Town.TerrainAt(Location(x,y))
                        t = t.GetUnlocked()
                        Town.AlterTerrain(Location(x,y), 0, t)
                ResumeMapUpdate()
                StuffDone["13_4"] = 1
                return
            RunScript("Loopback_23_1", p)
            return
        elif result == 1:
            ChoiceBox("\"This is not our battle,\" you think, \"it is foolish to risk all in this encounter when our skills are desperately needed elsewhere.\" So you hold back, leaving the Drake to rampage freely over the battlements.\n\nYou avert your eyes as soldiers are burned by the dozens, close your ears to the wails of the frightened civilians covering in the courtyard. You step back as roaring flames engulf the parapets, and suddenly all goes silent.\n\nThe flames die, leaving the wall empty of both defenders and attackers. Only the Drake, circling the walls and roaring in triumph remains. \"I won the bet!\" it laughs. \"Admit it, your heroes failed you!\"\n\n\"I do, Rashtarra.\" a familiar voice sighs behind you. You whirl and meet the grim smile of Karolynna. \"I have lost the right to speak to you. I counted on your courage to outweigh your caution. The demon holding me captive tricked me.\"\n\n\"Enough!\" the Drake roars, and Karolynna fades away. Great clouds of smoke stream from the nostrils of the great lizard as it laughs with scorn. \"Cowards!\"\n\nYou feel weak.", eDialogPic.CREATURE, 127, ["OK"])
            for pc in Party.EachAlivePC():
                pc.AwardXP(-15)
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:
                    pc.LifeStatus = eLifeStatus.ALIVE
            MessageBox("You wake to find yourselves wet and trembling, but alive, back in the great bed. Going back to sleep is out of the question. You rise and find that the equipment of those of you who \"died\" is gone!\n\nYou discuss the events of the dream as little as possible, trying to lay the experience quickly behind you.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(34,23))
            p.CancelAction = True
            SuspendMapUpdate()
            for x in range(6, 35):
                for y in range(27, 35):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            StuffDone["13_4"] = 1
            return
        return

def FlickeringKeep_307_MapTrigger_32_28(p):
    if StuffDone["13_4"] >= 1:
        return
    if SpecialItem.PartyHas("Ghostlykey"):
        if StuffDone["13_7"] == 250:
            return
        StuffDone["13_7"] = 250
        MessageBox("The door has been securely locked. The good people of Flickering Keep do not want you roaming the halls at night. You, however, have an errand before bed time. You turn the mysterious key you were given by the spirit, and the door opens.")
        t = Town.TerrainAt(Location(32,29))
        if t.InGroup("Unlockable"):
            t = Town.TerrainAt(Location(32,29)).TransformTo
            Town.AlterTerrain(Location(32,29), 0, t)
        return
    MessageBox("You shake the door knob. It is locked. The kind Lady Fray wants to help you stay the entire night in this room, so you can find out what happened to Karolynna. Perhaps you can even share her fate.")

def FlickeringKeep_308_MapTrigger_21_30(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The stairways have been closed by a heavy door for the night. No amount of hammering or shouting can open it.")

def FlickeringKeep_311_MapTrigger_34_24(p):
    if StuffDone["13_2"] == 250:
        return
    StuffDone["13_2"] = 250
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(34,24))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(35,25))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(35,26))
    TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(33,25))
    MessageBox("\"The Lady lies,\" the old manservant mutters as he leaves. \"The guest never left this room.\" The heavy door slams shut behind him. Footsteps grow fainter as the manservant leaves, underlining the silence of the room in front of you.\n\nExquisite paintings of heroic battles and a pool of water makes for a luxurious suite, yet you feel cold. The torches fail to light or warm the room. You wonder what happened to Karolynna during her night in this room.")

def FlickeringKeep_320_ExitTown(p):
    if p.Dir.IsNorth:
        if StuffDone["13_4"] >= 1:
            if StuffDone["13_6"] == 250:
                return
            StuffDone["13_6"] = 250
            MessageBox("You escape the sinister castle in confusion. Was that really Lord Fray you saw in the Hall of Flickers? He looked just like the pictures you have seen of him. But why did he resemble the Drake in your dream? You must find Karolynna, she knows the answers.")
            return

def FlickeringKeep_321_CreatureDeath8(p):
    MessageBox("The wicked woman tumbles to the ground, calling out the name of her husband as she dies. You lower your weapons and examine her. Her only ornament is a rough rock hanging in a chain around her neck. You pick it up.\n\nSuddenly, Lady Fray?s last plea is answered. The right wall cracks and crumbles. There is a loud boom, and the entire wall falls apart, revealing the Hall of Flickers.")
    SpecialItem.Give("Frayamulet")
    MessageBox("The torches are burning low. A gaunt man sits on the throne. \"So the Frays die!\" he mutters. He advances, teeth glittering, for a moment resembling the Drake in your dream. Suspecting that the demon is too tough for you, you look for routes of escape.")
    for x in range(19, 22):
        for y in range(36, 41):
            if Maths.Rand(1,0,100) <= 80:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
    Town.PlaceEncounterGroup(2)
    for x in range(16, 19):
        for y in range(32, 33):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[160])

def Talking_13_0(p):
    if Party.Gold < 0:
        p.TalkingText = ""
    else:
        Party.Gold -= 0
        Party.Pos = Location(34, 25)
        Town.UpdateVisible()
        Party.HealAll(0, True)
        Party.RestoreSP(0)
        p.TalkingText = "\"Granted.\" the lady announces. You stay and have supper with the quiet crowd, then you are lead to the lord?s rooms. A manservant unlocks the heavy door for you."
        CentreView(Party.Pos, False)

def Talking_13_10(p):
    if Party.Gold < 0:
        p.TalkingText = ""
    else:
        Party.Gold -= 0
        Party.Pos = Location(28, 12)
        Town.UpdateVisible()
        Party.HealAll(0, True)
        Party.RestoreSP(0)
        p.TalkingText = "Lady Fray considers you for a moment, just to make a point of her decision. \"Very well, since you ask so nicely. Guards! Escort the errand runners out!\" You leave, feeling embarrassed."
        CentreView(Party.Pos, False)

def Loopback_23_1(p):
    result = ChoiceBox("You stand at a high curtain wall placed on the very edge of the ledge. Outside the parapet is a bottomless drop into darkness. The defence should be impregnable from this side.\n\nStill, the wall is being stormed. Scaling ladders and hooks are continuously thrown over the wall, and hundreds of sliths climb out of the darkness to assault the fort.\n\nPanicking soldiers try to throw the ladders back, and confused officers do their best to keep the attackers out. They might succeed, except for the attacks of a giant Drake Lord, harassing the defenders with its fiery breath.\n\nAs you watch, a soldier climbs the tallest tower on the wall and fires an arrow at the Drake. It clatters off the scaly hide of the monster, and it turns its horned head at the him. He falls in a ball of flame, landing on top of a pile of defenders.\n\nYou look at the charred victims of the Drake Lord and at the fires spreading around the monster. There is only one way you can save the brave defenders. You must climb the tower and defy the lizard. You know it might cost you your life.\n\nDo you?", eDialogPic.CREATURE, 144, ["Climb", "Flee"])
    if result == 0:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            ChoiceBox("\"This is not our battle,\" you think, \"it is foolish to risk all in this encounter when our skills are desperately needed elsewhere.\" So you hold back, leaving the Drake to rampage freely over the battlements.\n\nYou avert your eyes as soldiers are burned by the dozens, close your ears to the wails of the frightened civilians covering in the courtyard. You step back as roaring flames engulf the parapets, and suddenly all goes silent.\n\nThe flames die, leaving the wall empty of both defenders and attackers. Only the Drake, circling the walls and roaring in triumph remains. \"I won the bet!\" it laughs. \"Admit it, your heroes failed you!\"\n\n\"I do, Rashtarra.\" a familiar voice sighs behind you. You whirl and meet the grim smile of Karolynna. \"I have lost the right to speak to you. I counted on your courage to outweigh your caution. The demon holding me captive tricked me.\"\n\n\"Enough!\" the Drake roars, and Karolynna fades away. Great clouds of smoke stream from the nostrils of the great lizard as it laughs with scorn. \"Cowards!\"\n\nYou feel weak.", eDialogPic.CREATURE, 127, ["OK"])
            for pc in Party.EachAlivePC():
                pc.AwardXP(-15)
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:
                    pc.LifeStatus = eLifeStatus.ALIVE
            MessageBox("You wake to find yourselves wet and trembling, but alive, back in the great bed. Going back to sleep is out of the question. You rise and find that the equipment of those of you who \"died\" is gone!\n\nYou discuss the events of the dream as little as possible, trying to lay the experience quickly behind you.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(34,23))
            p.CancelAction = True
            SuspendMapUpdate()
            for x in range(6, 35):
                for y in range(27, 35):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            StuffDone["13_4"] = 1
            return
        MessageBox("You throw yourself forward and climb the stairs in three bounds, shouting at the flying lizard. It turns towards you, hovering well outside your range. Then fire sprouts around you, and you fall to join the growing pile of valiant corpses.")
        pc.Kill(None, eLifeStatus.DUST, True)
        Wait()
        StuffDone["13_3"] += 1
        if StuffDone["13_3"] == 250:
            TownMap.List["FlickeringKeep_13"].DeactivateTrigger(Location(31,38))
        if StuffDone["13_3"] >= 5:
            ChoiceBox("Fighting panic, you prepare for the final sacrifice. Standing alone at the parapet, you take a last look at the scene before following your friends in their last, hopeless  battle. \"So this is the end.\" you think. \"Why just here?\"\n\nBut as you look over the wall, you see no more slith attackers. The defenders are also gone, leaving the curtain wall empty and deadly silent after the commotion of the battle. The Drake looks down at you and roars in fury, but does not attack.\n\n\"I won the bet. Now leave us alone!\" The voice rings through the darkness, and the Drake roars again, but flies off. \"Dealing with demons is tricky business,\" a familiar voice says behind you. \"It?s so much easier by sword point.\"\n\nKarolynna leans over the breastworks next to you. \"I?m sorry you had to go through all this, but it was the only way. It amused him, and he doesn?t realize how dangerous you are. Yet.\" She grabs your shoulder.\n\n\"Listen well, for you must relay this to your friends, when they rejoin you. I am held prisoner by the haakai Rashtarra. He has taken control of this household. You must free me, for I hold evidence that will sway the outcome of this entire war!\n\n\"There is an amulet. Lady Fray owns it, and she too is charmed by the demon. And a key, somewhere in Myldres. Find these, then come to me, below the ruins of Whitstone! Now leave this place. But beware Lady Fray! She means you no good!\"", eDialogPic.CREATURE, 127, ["OK"])
            pc.AwardXP(20)
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:
                    pc.LifeStatus = eLifeStatus.ALIVE
            MessageBox("You wake to find yourselves wet and trembling, but alive, back in the great bed. Going back to sleep is out of the question. You rise and find that the equipment of those of you who \"died\" is gone!\n\nYou discuss the events of the dream as little as possible, trying to lay the experience quickly behind you.")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(34,23))
            p.CancelAction = True
            SuspendMapUpdate()
            for x in range(6, 35):
                for y in range(27, 35):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            StuffDone["13_4"] = 1
            return
        RunScript("Loopback_23_1", p)
        return
    elif result == 1:
        ChoiceBox("\"This is not our battle,\" you think, \"it is foolish to risk all in this encounter when our skills are desperately needed elsewhere.\" So you hold back, leaving the Drake to rampage freely over the battlements.\n\nYou avert your eyes as soldiers are burned by the dozens, close your ears to the wails of the frightened civilians covering in the courtyard. You step back as roaring flames engulf the parapets, and suddenly all goes silent.\n\nThe flames die, leaving the wall empty of both defenders and attackers. Only the Drake, circling the walls and roaring in triumph remains. \"I won the bet!\" it laughs. \"Admit it, your heroes failed you!\"\n\n\"I do, Rashtarra.\" a familiar voice sighs behind you. You whirl and meet the grim smile of Karolynna. \"I have lost the right to speak to you. I counted on your courage to outweigh your caution. The demon holding me captive tricked me.\"\n\n\"Enough!\" the Drake roars, and Karolynna fades away. Great clouds of smoke stream from the nostrils of the great lizard as it laughs with scorn. \"Cowards!\"\n\nYou feel weak.", eDialogPic.CREATURE, 127, ["OK"])
        for pc in Party.EachAlivePC():
            pc.AwardXP(-15)
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.DEAD or pc.LifeStatus == eLifeStatus.DUST or pc.LifeStatus == eLifeStatus.STONE:
                pc.LifeStatus = eLifeStatus.ALIVE
        MessageBox("You wake to find yourselves wet and trembling, but alive, back in the great bed. Going back to sleep is out of the question. You rise and find that the equipment of those of you who \"died\" is gone!\n\nYou discuss the events of the dream as little as possible, trying to lay the experience quickly behind you.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(34,23))
        p.CancelAction = True
        SuspendMapUpdate()
        for x in range(6, 35):
            for y in range(27, 35):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetUnlocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        StuffDone["13_4"] = 1
        return
