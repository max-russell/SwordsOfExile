
def WatchpointTowerL2_995_MapTrigger_23_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(23,6)
    Party.MoveToMap(TownMap.List["WatchpointTower_42"])

def WatchpointTowerL2_997_MapTrigger_6_27(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(6,28)).Num == 128:
        if SpecialItem.PartyHas("BoneKey"):
            MessageBox("This door has an imposing lock in the shape of a skull attached to the door. Using your bone key does the trick!")
            SuspendMapUpdate()
            for x in range(6, 8):
                for y in range(28, 29):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("This door is held shut by a lock in the shape of a skull. Despite your best attempts, you cannot get past this lock.")
        return

def WatchpointTowerL2_998_SanctifyTrigger_35_24(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["22_3"] == 0:
        StuffDone["22_3"] = 1
        Town.AlterTerrain(Location(35,24), 0, TerrainRecord.UnderlayList[166])
        MessageBox("You cast the Ritual of Sanctification on the altar. Immediately after the ritual, the dark energy within is released violently! The release was so violent that the altar exploded and caused the floor to collapse in!")
        Animation_Explosion(Location(35,24), 0, "005_explosion")
        Animation_Hold()
        Wait()
        return

def WatchpointTowerL2_999_MapTrigger_35_24(p):
    if StuffDone["22_3"] == 0:
        MessageBox("This altar radiates a dark energy. You can feel it warping your mind.")
        return
    result = ChoiceBox("The altar\'s destruction caused the floor below it to collapse, leaving a small hole. It would be a tight squeeze, but you all could probably fit through it. The for sure thing is you won\'t be able to get back up. Do you climb down?", eDialogPic.TERRAIN, 244, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(35,23)
        Party.MoveToMap(TownMap.List["WatchpointTower_42"])
        return
    p.CancelAction = True

def WatchpointTowerL2_1000_MapTrigger_13_13(p):
    if StuffDone["23_4"] == 1:
        return
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(15,14)
    Party.MoveToMap(TownMap.List["WatchpointTower_42"])

def WatchpointTowerL2_1003_MapTrigger_27_5(p):
    if StuffDone["22_4"] == 250:
        return
    StuffDone["22_4"] = 250
    TownMap.List["WatchpointTowerL2_43"].DeactivateTrigger(Location(27,5))
    TownMap.List["WatchpointTowerL2_43"].DeactivateTrigger(Location(27,6))
    ChoiceBox("Suddenly Astervis stops. \"I sense something going on somewhere in this tower. I think I can...here see for yourselves.\" Astervis casts a spell so you can perceive the image too.\n\nYou see a chamber with a grim faced wizard with robes of dark red sitting in a throne. His head his shaved with many tattoos and his eyes are as black as midnight. You feel an deep inner evil from that man.\n\nSuddenly, a younger mage bursts into the throne room. The grim faced wizard speaks, \"They have infiltrated the second floor. Your defenses are failing. I hope you have your next move figured out.\"\n\nThe younger mage retorts. \"It was a freak accident that they managed to make it to the second floor. One of our barriers collapsed and we could not repair it in time. The creators of the initial barrier were slain while attempting its repair.\n\nBut don\'t worry sire, I have examined the situation on the second floor. Our defenses will hold! There is no way they will get to your barrier research!\"\n\nThe grim faced one replies, \"Let us hope so, for your sake.\"", eDialogPic.STANDARD, 0, ["OK"])

def WatchpointTowerL2_1005_MapTrigger_6_15(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["22_8"] == 250:
        return
    StuffDone["22_8"] = 250
    MessageBox("You have arrived in a room with three Wyverns and a wizard. Off to the east, is the familiar site of a barrier being established. This must be from the scene in your vision!")

def WatchpointTowerL2_1007_MapTrigger_11_17(p):
    if StuffDone["22_9"] == 0:
        if StuffDone["22_7"] == 0:
            StuffDone["22_7"] = 1
            ChoiceBox("You near the near completed barrier. This time, you were not quite fast enough. There is a loud boom, like the sound of thunder as the barrier instantly solidifies from an insubstantial glow like cloud into a solid wall of fiery, red energy.\n\nIt looks like this round goes to the home team. Now to find away to get back in the game!", eDialogPic.TERRAIN, 231, ["OK"])
            for x in range(13, 14):
                for y in range(18, 20):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[169])
            return
        return

def WatchpointTowerL2_1010_MapTrigger_10_9(p):
    result = ChoiceBox("This pedestal is labeled: PORTAL DESTINATION CONTROLS. In addition there are two buttons labeled accordingly. 1 -- ANCIENT SCHOOL BASE. 2 -- AUDIENCE CHAMBER. Do you try to make settings?", eDialogPic.STANDARD, 22, ["Leave", "2", "1"])
    if result == 1:
        MessageBox("You push the button and hear a soft click.")
        StuffDone["23_1"] = 1
        return
    elif result == 2:
        MessageBox("You push the button and hear a soft click.")
        StuffDone["23_1"] = 0
        return

def WatchpointTowerL2_1011_MapTrigger_7_8(p):
    if StuffDone["23_4"] == 1:
        return
    result = ChoiceBox("A large, crackling brightly glowing portal stands here. It looks quite powerful and well maintained. It should be safe to use assuming that the targeting has been done properly.\n\nDo you enter?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if StuffDone["23_1"] == 0:
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(49,59)
            Party.MoveToMap(TownMap.List["ForgottenAcademy_60"])
            return
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(24,29)
        Party.MoveToMap(TownMap.List["WatchpointTower_42"])
        return
    p.CancelAction = True

def WatchpointTowerL2_1012_MapTrigger_5_32(p):
    result = ChoiceBox("A large ancient magical tome that is probably filled with juicy arcane secrets is before you. You can hardly resist the temptation to sit down and read the powerful secrets of old contained inside.\n\nDo you dare take a seat and attempt to learn some knowledge from this book?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        MessageBox("You begin to read, and at first it seems to make sense. However, you soon find yourself having to go back and reread the previous sentences, having forgotten the sentence before it.\n\nThis book must have been trapped with some kind of memory erasing spell! Frustrated, you close the book leaving not quite as smart as you were when you first opened it.")
        for pc in Party.EachAlivePC():
            pc.AwardXP(-20)
        return

def WatchpointTowerL2_1016_MapTrigger_10_34(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["23_2"] == 250:
        return
    StuffDone["23_2"] = 250
    MessageBox("You lean against this wall, and a small section gives way! You have just discovered some shoddily built, but well concealed, secret passage. On the other side are a rows of potion racks. Why would a passage connect these two rooms?\n\nYour best guess is some authorized person may have been sneaking in and reading the texts. It looks like this passage was either not known about or forgotten for this may be your big break.")

def WatchpointTowerL2_1017_MapTrigger_14_36(p):
    if StuffDone["22_6"] == 250:
        return
    StuffDone["22_6"] = 250
    TownMap.List["WatchpointTowerL2_43"].DeactivateTrigger(Location(14,36))
    TownMap.List["WatchpointTowerL2_43"].DeactivateTrigger(Location(14,37))
    ChoiceBox("Astervis turns to you. \"Looks like we\'re getting close. Take a look!\" You see the image of the same room as in the previous vision. Golems and mages are quickly moving into position.\n\nAn image of the young mage floats in the center shouting. \"Hurry! They\'ve gotten through by way of a passage we did not know about! They\'re almost here. Battle positions, quickly.\"\n\nThe young mage mutters. \"If we get out of this, I\'m going to find out who\'s been sneaking in and that person is going to pay dearly.\" The vision fades away.", eDialogPic.STANDARD, 0, ["OK"])

def WatchpointTowerL2_1019_MapTrigger_15_34(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["23_3"] == 250:
        return
    StuffDone["23_3"] = 250
    ChoiceBox("You open the door and find yourself in a large room. The room is dominated by a slightly elevated platform. At the focus of the platform is a large jumbling of red sparkling crystals.\n\nThe crystalline mass is similar to the one you smashed in the Barrier Spire way back at Halloth\'s Citadel, but larger and brighter. The projection of the young mage is there, floating in the air, facing the crystal away from you.\n\nHe turns around and looks at you angrily. He makes a motion of attack and fades away. You look around to see large hulking Golems and wizards preparing spells. This is going to be a BIG fight!", eDialogPic.CREATURE, 123, ["OK"])
    Town.PlaceEncounterGroup(1)
    StuffDone["23_4"] = 1

def WatchpointTowerL2_1021_MapTrigger_21_43(p):
    StuffDone["23_4"] = 2
    StuffDone["17_3"] = 27
    ChoiceBox("With a mighty blow, the Power Crystal shatters releasing an strong shockwave that pushes everyone to the floor. You look at the barriers blocking a southern passage. They are growing more and more unstable.\n\nIt takes only a few seconds for them to reach the critical point before they decay and disappear completely. It looks like you have disabled the barriers throughout the tower! But what about that grim mage from your vision?\n\nAstervis relays an image to you. The grim faced wizard rises from his throne, in front of him is the young mage kneeling before him. \"Please forgive me sire! Have mercy, oh please.\"\n\nThe grim faced wizard laughs. \"Ha! You have failed me. The only punishment for failure is death! And in the worst imaginable way.\" The young mage continues to beg as the grim mage extends his right hand.\n\nA beam of black energy fires from it and strikes the poor mage. He screams as the life force is sucked from his body. It does not take too long. All that is left is a pathetic husk. The image fades away.\n\nAstervis turns to you, \"It is he who is responsible. We must stop him!\"", eDialogPic.CREATURE, 123, ["OK"])
    for x in range(13, 14):
        for y in range(18, 20):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
    for x in range(15, 16):
        for y in range(8, 10):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
    for x in range(32, 33):
        for y in range(32, 34):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
    for x in range(24, 26):
        for y in range(34, 35):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])

def WatchpointTowerL2_1022_MapTrigger_24_37(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,37)
    Party.MoveToMap(TownMap.List["WatchpointTowerL3_44"])

def WatchpointTowerL2_1024_OnEntry(p):
    if StuffDone["22_3"] >= 1:
        Town.AlterTerrain(Location(35,24), 0, TerrainRecord.UnderlayList[166])
        if StuffDone["17_3"] >= 28:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            if StuffDone["17_3"] >= 27:
                for x in range(13, 14):
                    for y in range(18, 20):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
                for x in range(15, 16):
                    for y in range(8, 10):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
                for x in range(32, 33):
                    for y in range(32, 34):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
                for x in range(24, 26):
                    for y in range(34, 35):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
                return
            if StuffDone["22_7"] == 1:
                for x in range(13, 14):
                    for y in range(18, 20):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[169])
                return
            return
        if StuffDone["17_3"] >= 27:
            for x in range(13, 14):
                for y in range(18, 20):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(15, 16):
                for y in range(8, 10):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(32, 33):
                for y in range(32, 34):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(24, 26):
                for y in range(34, 35):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            return
        if StuffDone["22_7"] == 1:
            for x in range(13, 14):
                for y in range(18, 20):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[169])
            return
        return
    if StuffDone["17_3"] >= 28:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if  npc.IsABaddie: Town.NPCList.Remove(npc)
        if StuffDone["17_3"] >= 27:
            for x in range(13, 14):
                for y in range(18, 20):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(15, 16):
                for y in range(8, 10):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(32, 33):
                for y in range(32, 34):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            for x in range(24, 26):
                for y in range(34, 35):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
            return
        if StuffDone["22_7"] == 1:
            for x in range(13, 14):
                for y in range(18, 20):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[169])
            return
        return
    if StuffDone["17_3"] >= 27:
        for x in range(13, 14):
            for y in range(18, 20):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
        for x in range(15, 16):
            for y in range(8, 10):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
        for x in range(32, 33):
            for y in range(32, 34):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
        for x in range(24, 26):
            for y in range(34, 35):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[173])
        return
    if StuffDone["22_7"] == 1:
        for x in range(13, 14):
            for y in range(18, 20):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[169])
        return
