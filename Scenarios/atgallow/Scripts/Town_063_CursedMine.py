def Generate_Wandering_63_CursedMine(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([2,NPCRecord.List["Ogre_45"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([2,NPCRecord.List["Ogre_45"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([2,NPCRecord.List["Ogre_45"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([2,NPCRecord.List["Ogre_45"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(12,55)
                elif r2 == 1: l = Location(37,48)
                elif r2 == 2: l = Location(59,41)
                elif r2 == 3: l = Location(58,19)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def CursedMine_1536_MapTrigger_32_8(p):
    if StuffDone["39_2"] == 250:
        return
    StuffDone["39_2"] = 250
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(32,8))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(33,8))
    ChoiceBox("You have found the abandoned supposedly \'Cursed Mine\'. You listen, but hear no noise. Everything is deathly quiet. However, you must be careful; no noise does not equate to no danger.\n\nPerhaps you should have a look around. Who knows? You might just find something valuable!", eDialogPic.STANDARD, 8, ["OK"])

def CursedMine_1538_MapTrigger_45_9(p):
    MessageBox("This chest is empty. It\'s contents were probably taken when the mine was abandoned.")

def CursedMine_1539_MapTrigger_45_25(p):
    if StuffDone["39_3"] == 250:
        return
    StuffDone["39_3"] = 250
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(45,25))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(44,25))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(46,25))
    MessageBox("You see a disclaimer posted on the door; it reads, \"NOTICE! This mine has been abandoned. The Damasnica Mining Corporation revokes all responsibility for this site. Explore at your own risk!\"")

def CursedMine_1542_MapTrigger_45_30(p):
    result = ChoiceBox("There is a cart here designed to move passengers, equipment, and claims up and down this shaft. The controls are pretty straightforward. Do you use the cart?", eDialogPic.STANDARD, 19, ["Leave", "Yes"])
    if result == 1:
        MessageBox("The cart slowly lowers you to the bottom of a long shaft. Thankfully, there are controls here to allow you to ride back up.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(57,8))
        p.CancelAction = True
        return
    p.CancelAction = True

def CursedMine_1543_MapTrigger_57_7(p):
    result = ChoiceBox("There is a cart here designed to move passengers, equipment, and claims up and down this shaft. The controls are pretty straightforward. Do you use the cart?", eDialogPic.STANDARD, 19, ["Leave", "Yes"])
    if result == 1:
        MessageBox("The cart moves your party up the shaft. You have been returned to the residence area.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(45,29))
        p.CancelAction = True
        return
    p.CancelAction = True

def CursedMine_1544_MapTrigger_57_12(p):
    if StuffDone["39_4"] == 250:
        return
    StuffDone["39_4"] = 250
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(57,12))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(56,12))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(58,12))
    MessageBox("Just past this door, you discover a small campfire with Ogres huddled around it. It appears that these creatures now inhabit the mine, and they don\'t look too happy about your intrusion.")

def CursedMine_1547_MapTrigger_32_38(p):
    if StuffDone["39_5"] == 250:
        return
    StuffDone["39_5"] = 250
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(32,38))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(32,39))
    MessageBox("The cavern to the west has suffered a massive cave-in. Rubble is strewn about everywhere. You can smell the tinge of sulfur in the air and melted rock lies about. It was obviously caused by a massive explosion.")

def CursedMine_1549_MapTrigger_29_47(p):
    if StuffDone["39_6"] == 250:
        return
    StuffDone["39_6"] = 250
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(29,47))
    MessageBox("This was presumably a miner. His skull was bashed in by a blunt object. He must have been trapped behind the rubble of the blast. You can\'t tell if he was killed by the cave-in or some other method.")

def CursedMine_1550_MapTrigger_37_57(p):
    if StuffDone["39_7"] == 250:
        return
    StuffDone["39_7"] = 250
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(37,57))
    TownMap.List["CursedMine_63"].DeactivateTrigger(Location(38,57))
    MessageBox("The passage to the south has suffered a cave-in. You can smell sulfur in the air and see melted rock strewn about. This was obviously the work of an explosion.")

def CursedMine_1552_MapTrigger_13_49(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever and machinery that controls the portculli are activated.")
        SuspendMapUpdate()
        for x in range(15, 17):
            for y in range(49, 50):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def CursedMine_1553_MapTrigger_2_61(p):
    MessageBox("This pedestal bears a small alcove with several glowing runes etched into it.")

def CursedMine_1555_MapTrigger_6_58(p):
    if StuffDone["39_8"] == 0:
        StuffDone["39_8"] = 1
        Animation_Explosion(Location(4,59), 2, "005_explosion")
        Animation_Hold()
        Wait()
        MessageBox("Suddenly, the portal in the lab fades out of existence! It wasn\'t that stable to begin with, anyway. The point of the matter is, you will have to find a way to reactivate it in order to make use of it.")
        Town.AlterTerrain(Location(4,59), 0, TerrainRecord.UnderlayList[170])
        return

def CursedMine_1557_MapTrigger_4_61(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(4,59)).Num == 170:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(2,61), True):
                    if i.SpecialClass == 3:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(6,61), True):
                        if i.SpecialClass == 3:
                            itemthere = True
                            break
                if itemthere == True:
                    Town.AlterTerrain(Location(4,59), 0, TerrainRecord.UnderlayList[78])
                    MessageBox("It worked! Using the power of the rubies, the portal was able to reactivate. It looks pretty stable, for now at least.")
                    Animation_Explosion(Location(4,59), 2, "005_explosion")
                    Animation_Hold()
                    Wait()
                    StuffDone["39_8"] = 2
                    return
                MessageBox("Nothing happens.")
                return
            MessageBox("Nothing happens.")
            return
        MessageBox("Nothing happens.")
        return

def CursedMine_1560_MapTrigger_4_59(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(4,59)).Num == 78:
        result = ChoiceBox("The Ogre\'s portal appears to be stable. You have no idea at all where it will take you, however. Unfortunately, the only way to find out is to risk going in. What do you do?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Animation_Vanish(Party.LeaderPC, True, "010_teleport")
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(7,39))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            p.CancelAction = True
            return
        p.CancelAction = True
        return

def CursedMine_1561_MapTrigger_7_40(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(4,58))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def CursedMine_1562_MapTrigger_7_47(p):
    if StuffDone["39_9"] == 0:
        result = ChoiceBox("A large ruby has been placed upon this altar as an offering to the Ogre gods. The gem looks pretty valuable. Do you risk their wraith by taking it?", eDialogPic.TERRAIN, 154, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("SteelWaveBlade_94")
            StuffDone["39_9"] = 1
            MessageBox("Your actions have angered some divine power. Some dark servants have arrived to punish your actions.")
            Town.PlaceEncounterGroup(2)
            return
        return

def CursedMine_1563_MapTrigger_11_61(p):
    ChoiceBox("You flip through the journal of an Ogre Mage. You discover a section on their portal. \"I Gravag, have completed the portal! It is truly the greatest accomplishment of our people ever.\n\nThe complication we were faced with was its instability. However, I have built a method that will hopefully solve the problem. To the south of the portal area, lay three pedestals.\n\nThe center pedestal serves as a control, more on that later. The side pedestals contain alcoves in which a power source is placed. Through research, we have found the optimum source is a ruby.\n\nTo stabilize the portal, a power source (a ruby) must be placed in each alcove. The button on the controls must then be pressed. A stable portal should then materialize.\n\nCurrently, it only links to our master\'s lair. More research on targeting and coordinate navigation must be conducted.\" The journal provides further uninteresting technical details on the portal.", eDialogPic.TERRAIN, 135, ["OK"])

def CursedMine_1564_MapTrigger_3_29(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["38_9"] == 250:
        return
    StuffDone["38_9"] = 250
    MessageBox("You enter what appears to be some laboratory. An ancient hag, assisted by two large demons, is in the middle of preparing some brew. She is angered by your intrusion and orders her servants to attack.")
    Town.PlaceEncounterGroup(1)

def CursedMine_1565_MapTrigger_9_23(p):
    if StuffDone["39_1"] == 0:
        if StuffDone["39_0"] == 1:
            if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,22)).Num == 145:
                Town.AlterTerrain(Location(9,22), 0, TerrainRecord.UnderlayList[142])
                Town.AlterTerrain(Location(10,22), 0, TerrainRecord.UnderlayList[142])
                return
            return
        return

def CursedMine_1567_MapTrigger_12_23(p):
    ChoiceBox("You discover the witch\'s notebook amongst these shelves. An interesting section reads, \"Who do those Imperial pigs think they are! These caves belong to me. Those fools think they can come in here and mine! They will pay for this! ...\"\n\nThe journal continues, \"...The addition of the ogres has proven effective to chasing away those foolish miners away. In addition to the staged explosions and accidents, it may be sufficient...\n\n...My caves have been abandoned by the Empire. Hopefully, I can now live in solitude. However, they have suffered much damage and they will pay. Perhaps I should look for those notes on that fungus I discovered a while back...\n\n...Success! I have managed to recreate the disease causing fungus in the cave to the north. Its secretions will pollute the waters running into Damasnica. I doubt the effects will kill anyone, but it will make the population very ill.\"\n\nNow it all begins to make sense. The Empire came here to mine, and unbeknownst to them, angered some deranged witch. She employed means to chase away the miners and succeeded.\n\nHowever, she did not stop there. She took revenge upon the people of Damasnica by making them ill by polluting their water. You have to wonder about the sanity of some of these mages...", eDialogPic.TERRAIN, 135, ["OK"])
    StuffDone["40_2"] = 1

def CursedMine_1568_MapTrigger_11_9(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["40_2"] == 1:
        if StuffDone["40_3"] == 1:
            result = ChoiceBox("Ahead lies the source of the disease in Damasnica. Alien fungus upon the stalagtites drips a green slime into the stream leading into the city. It is an ingenious setup by a twisted and vindictive mage.\n\nHowever, the plot may soon come to a close. You have the knowledge and the means to destroy the horrid creation. You could use the \'Explosive Barrel\' to cause a cave in, ending the plight.\n\nThat is, if everything works out as planned. Do you attempt to destroy this place?", eDialogPic.STANDARD, 25, ["Leave", "Destroy"])
            if result == 1:
                SpecialItem.Take("BarrelofExplosives")
                StuffDone["39_1"] = 1
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Party.Reposition(Location(9,26))
                p.CancelAction = True
                Animation_Hold(-1, 005_explosion)
                Wait()
                Animation_Hold(-1, 005_explosion)
                Wait()
                Animation_Hold(-1, 060_smallboom)
                Wait()
                Animation_Hold(-1, 060_smallboom)
                Wait()
                Animation_Hold(-1, 005_explosion)
                Wait()
                Animation_Hold(-1, 060_smallboom)
                Wait()
                Town.AlterTerrain(Location(9,22), 0, TerrainRecord.UnderlayList[145])
                Town.AlterTerrain(Location(10,22), 0, TerrainRecord.UnderlayList[145])
                ChoiceBox("You place the barrel, light the fuse, and run! You reach the witch\'s bunker and brace the doors. Soon after, you hear massive explosions and rocks falling. Hopefully, the evil plan created to make Damasnica\'s people ill has been destroyed.", eDialogPic.STANDARD, 25, ["OK"])
                return
            return
        MessageBox("Well, this is it. Fungus clings to the stalagtites above, dripping a greenish slime into the stream below. The tainted water then flows into the city of Damasnica, making its people sick. The question: How do you stop this?")
        return
    MessageBox("Interesting! The ceiling of the caves is overgrown with some alien fungus. The fungus produces a greenish slime that drips into the stream in large quantities. You wonder what this means.")

def CursedMine_1569_MapTrigger_5_44(p):
    if StuffDone["40_3"] == 1:
        Town.AlterTerrain(Location(8,44), 0, TerrainRecord.UnderlayList[170])
        return

def CursedMine_1570_MapTrigger_8_44(p):
    if StuffDone["40_3"] == 0:
        MessageBox("You find a fair-sized barrel. According to the label, its contents are explosive and you should handle with care. Such barrels were likely the cause of the explosive cave-ins that you saw earlier.\n\nSadly, it is missing a fuse. You will need some item to act as one if you hope to make any use of it.")
        if Party.CountItemClass(24, True) > 0:
            MessageBox("You search your inventory and find a rope. You cut off a reasonable length and insert it into the barrel. If you ever wish to use it, you will just have to light the fuse. Whether or not it works, however, remains to be seen.")
            StuffDone["40_3"] = 1
            SpecialItem.Give("BarrelofExplosives")
            Town.AlterTerrain(Location(8,44), 0, TerrainRecord.UnderlayList[170])
            return
        return

def CursedMine_1571_MapTrigger_8_56(p):
    if StuffDone["39_8"] == 1:
        MessageBox("Suddenly, the portal in the lab fades out of existence! It wasn\'t that stable to begin with, anyway. The point of the matter is, you will have to find a way to reactivate it in order to make use of it.")
        Town.AlterTerrain(Location(4,59), 0, TerrainRecord.UnderlayList[170])
        return
