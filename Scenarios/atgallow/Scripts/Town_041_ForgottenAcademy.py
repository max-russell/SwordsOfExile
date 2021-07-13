
def ForgottenAcademy_920_MapTrigger_43_28(p):
    if StuffDone["20_2"] == 250:
        return
    StuffDone["20_2"] = 250
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(43,28))
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(43,29))
    MessageBox("As you cross over these runes, they spark and throw you back! However, the runes begin to fizzle out immediately after being triggered. You move in close again and nothing happens! Apparently this device fell to age.")
    Party.Damage(Maths.Rand(1, 1, 10) + 5, eDamageType.MAGIC)
    Wait()

def ForgottenAcademy_922_MapTrigger_43_36(p):
    MessageBox("On this side, near the top of the counter is a large red button. It looks pretty old, but it may still work!")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        MessageBox("You press the button. There is no sound nor any indication that anything has happened. It\'s quite likely the button is broken after so many years, but there is no may to tell.")
        SuspendMapUpdate()
        for x in range(38, 39):
            for y in range(28, 30):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def ForgottenAcademy_923_MapTrigger_58_25(p):
    if StuffDone["21_2"] == 0:
        result = ChoiceBox("This old machine is simply labeled: COMMUNICATOR. Miraculously, the machine seems operational. You don\'t know who or what it was meant to communicate with, but there may be no harm in finding out.\n\nOf course, you may wish to take this machine apart to see if you can find any equipment that may be valuable. What do you do?\n\n1 -- USE MACHINE\n\n2 -- TAKE IT APART AND SCAVENGE FOR VALUABLES", eDialogPic.TERRAIN, 125, ["Leave", "2", "1"])
        if result == 1:
            StuffDone["21_2"] = 1
            MessageBox("You open the machine up. Much of the equipment is in fair condition despite the rust. Unfortunately, the only piece of equipment that is fully intact is a circular plate labeled: TRANSMITTER. You take it just in case.")
            Party.GiveNewItem("TransmitterPlate_243")
            return
        elif result == 2:
            ChoiceBox("The communicator has a circlet which one can place upon his or her head. Following the pictographic instructions, you activate the machine. At first there is only static, you adjust several dials on the panel until you make out a signal.\n\n\"Okay folks, where at the bottom of the seventh; one out, two balls, one strike. Here comes the pitch and...strike! Whoa! That ball sure had some heat behind it. Winding up for another pitch now and...strike three!\n\nWell now, two outs and bases loaded. Here comes the next batter. Okay, the pitch...and ball! That one was sure off. That was an outstanding catch! Next pitch, he swings and a miss...strike one! Another pitch...and ball!?\n\nMy that ump must really be off tonight that\'s got to be the eleventh time tonight he\'s made a call like that. Throwing out another pitch and...ball, for sure this time. All right, two balls, one strike. Here comes...and a hit, but fowl. Strike two!\n\nBases loaded, two strikes, here comes the pitch...ball three! The pressures on both now, three balls, two strikes, only one more out to go. Here comes the pitch and...smack! That one\'s going, going, all the way! Home run!\"\n\nYou move the dials more and find no other signals. You wonder what that person meant by pitches, strikes, balls, and home runs. Who knows...", eDialogPic.STANDARD, 0, ["OK"])
            return
        return

def ForgottenAcademy_924_MapTrigger_44_10(p):
    if StuffDone["20_4"] == 250:
        return
    StuffDone["20_4"] = 250
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(44,10))
    TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(44,10))
    MessageBox("You were wondering why a chair would be sitting in the middle of a circle of runes. You reach out to touch the chair and your hand passes right through it! The chair is only a holographic image and a very realistic one at that.")

def ForgottenAcademy_925_MapTrigger_14_5(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(14,5)).Num == 78:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(51,2))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        MessageBox("You find yourself back in the control room. It appears that you have escaped the illusion.")
        StuffDone["20_5"] += 1
        if StuffDone["20_5"] == 250:
            TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(51,3))
        return

def ForgottenAcademy_926_MapTrigger_51_3(p):
    if StuffDone["20_5"] < 3:
        result = ChoiceBox("You sit down at the control panel to this interesting piece of equipment. The display shows on screen MENTAL HOLOGRAPHIC SURREALITY INFILTRATION SYSTEM. Amazingly, the device appears to be functional after so many years.\n\nUnfortunately, a few of the devices on the panel have rusted away. The only thing that will still work is the large red button that reads ACTIVATE. Do you dare press the button and see what happens?", eDialogPic.TERRAIN, 125, ["Leave", "Push"])
        if result == 1:
            if StuffDone["20_5"] >= 2:
                Party.GiveNewItem("ImagingCrystal_239")
                MessageBox("You push the button again and the machine begins to spark and shorts out! Apparently this machine was just about to die anyway. You open up the control panel to see the entire workings melted away.\n\nThe only thing that survived is a nice looking crystal. It has small flickers of light inside and emits a slight glow. Perhaps it will be valuable to somebody. You take it, leaving this machine dead.")
                StuffDone["20_5"] = 3
                return
            if StuffDone["20_5"] < 1:
                MessageBox("You push the button and all is a blur.  When \'reality\' returns, you find yourself in a fair sized room. Lined up along the wall are quite imposing martial artists! It looks like this is some kind of combat simulation.")
                if Game.Mode == eMode.COMBAT:
                    p.CancelAction = True
                    return
                Animation_Vanish(Party.LeaderPC, True, "010_teleport")
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                Wait()
                Party.Reposition(Location(14,5))
                p.CancelAction = True
                Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                p.CancelAction = True
                Town.PlaceEncounterGroup(1)
                return
            MessageBox("You use the machine again and this time you are placed in a different situation. You see a wizard presenting what appears to be a suit of armor to a bunch of mages. The wizard points to the suit proudly.\n\n\"I have finally done it! You all said it could not be done, but I have after so many years built the world\'s first doomguard!\" All of the mages look over it in awe. One of them asks, \"Yeah! But does it split like you said it will?\"")
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Animation_Vanish(Party.LeaderPC, True, "010_teleport")
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(22,7))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            p.CancelAction = True
            MessageBox("The wizard chuckles, \"Of course! Of course!\" The mage retorts, \"Yeah! Let\'s see it, seeing is believing!\" The wizard gets nervous and takes a swing at the doomguard. It splits in two! All of the magi cheer at the accomplishment.\n\n\"Well it looks like I was wrong about you.  What the...!\" Suddenly, the doomguards are attacking the mages! It does not take long to finish them off. Once they are done, they turn their attention to you!")
            Town.PlaceEncounterGroup(2)
            Timer(Town, 80, False, "ForgottenAcademy_956_TownTimer_26", eTimerType.DELETE)
            return
        return

def ForgottenAcademy_927_MapTrigger_22_5(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(22,5)).Num == 78:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(51,2))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        MessageBox("You find yourself back in the control room. It appears that you have escaped the illusion.")
        StuffDone["20_5"] += 1
        if StuffDone["20_5"] == 250:
            TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(51,3))
        return

def ForgottenAcademy_928_MapTrigger_42_47(p):
    if StuffDone["20_8"] < 1:
        StuffDone["20_8"] = 1
        Town.PlaceEncounterGroup(3)
        ChoiceBox("A wizard emerges from behind what appears to be a control panel on the other side of the bridge. He stares at you blankly and states in a monotone voice, \"Stay where you are. If you continue, you will be destroyed!\"\n\nYou laugh and continue anyway. The wizard returns to the panel and says, \"I warned you!\" He begins to use the controls, the two crystal spires on the panel light up with great intensity.\n\nThe two crystals each fire two laser beams. One for each of the two crystals on the sides of the bridge. Upon contact, your hair begins to stand on end and the platform is getting really hot. You jump back as a storm of lightning covers the bridge!\n\nYou somehow managed to get back unharmed. The wizard emerges once more, \"Now there is no way to get past this forcefield. If you try to cross, you will be toast! Oh, and don\'t think about trying to damage the crystals.\n\nThat would be unwise as the energy release will vaporize anything and everything in proximity. You cannot stop us. Turn back now before we are forced to kill you. Bye, bye!\"\n\nIt looks like you will have to find a way to either get around this forcefield or deactivate it.", eDialogPic.CREATURE, 27, ["OK"])
        Town.AlterTerrain(Location(61,48), 0, TerrainRecord.UnderlayList[171])
        for x in range(43, 47):
            for y in range(45, 51):
                if Maths.Rand(1,0,100) <= 80:
                    Town.PlaceField(Location(x,y), Field.FORCE_WALL)
        Timer(Town, 5, False, "ForgottenAcademy_957_TownTimer_36", eTimerType.DELETE)
        return

def ForgottenAcademy_930_MapTrigger_45_47(p):
    if StuffDone["20_8"] == 1:
        MessageBox("Trying to cross through the powerful electrical field was not a wise idea. Between the massive shocks and intensive heat generated, you are all killed.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        p.CancelAction = True
        return

def ForgottenAcademy_932_MapTrigger_38_47(p):
    if StuffDone["20_8"] == 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(61,48)).Num == 170:
            Town.AlterTerrain(Location(61,48), 0, TerrainRecord.UnderlayList[171])
            for x in range(43, 47):
                for y in range(45, 51):
                    if Maths.Rand(1,0,100) <= 80:
                        Town.PlaceField(Location(x,y), Field.FORCE_WALL)
            Timer(Town, 5, False, "ForgottenAcademy_957_TownTimer_36", eTimerType.DELETE)
            return
        return

def ForgottenAcademy_934_MapTrigger_23_53(p):
    if StuffDone["20_9"] == 250:
        return
    StuffDone["20_9"] = 250
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(23,53))
    TownMap.List["ForgottenAcademy_41"].DeactivateTrigger(Location(23,54))
    TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(23,53))
    TownMap.List["ForgottenAcademy_60"].DeactivateTrigger(Location(23,54))
    Animation_Hold(-1, 058_opendoor)
    Wait()
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 8))
    Animation_Hold(-1, 059_closedoor)
    Wait()
    MessageBox("Yuck! As soon as you open the door, you are assaulted by extremely caustic fumes! You try to proceed, but the fumes make you so feel unbearably nauseous that you have to close the door.\n\nOn the other side is a control room. However, the back wall has been eaten away by corrosive, toxic sludge -- probably waste products that have leaked over the centuries. You doubt you could reach the controls alive.")
    p.CancelAction = True

def ForgottenAcademy_936_MapTrigger_20_50(p):
    if StuffDone["21_0"] == 2:
        MessageBox("Something appears to be going wrong with your robot. For some reason, you cannot seem to go any further. It feels as if the robot has reached its range limit.")
        p.CancelAction = True
        return
    MessageBox("You were right about you not being able to make it to the controls. Despite your best efforts, you are eventually overcome by the caustic fumes.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
    p.CancelAction = True

def ForgottenAcademy_941_MapTrigger_49_41(p):
    MessageBox("There used to be a stairway leading back down to the lower level. However, time has caused this corridor to cave in, blocking off whatever lies below. You will not be able to proceed further this way.")
    p.CancelAction = True

def ForgottenAcademy_943_MapTrigger_39_41(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(56,4)
    Party.MoveToMap(TownMap.List["AncientRuins_40"])

def ForgottenAcademy_946_MapTrigger_12_29(p):
    if StuffDone["21_1"] == 0:
        result = ChoiceBox("This document contains several diagrams and various information on the workings of the robots. The instructions are quite detailed, and had you had the materials and the patience, you could probably build one of your own.\n\nThese robots are very interesting. According to the guide they were used to enter  hazardous locations to clean up failed experiments and such. The robot would be controlled by a person sitting at the controls, with his or her mind!\n\nIf for some reason you wanted to fix these robots up, you could try. Care to make the attempt?", eDialogPic.CREATURE, 120, ["Yes", "No"])
        if result == 0:
            if Party.CountItemClass(25, False) > 0:
                if Party.CountItemClass(27, False) > 0:
                    if Party.CountItemClass(28, False) > 0:
                        if Party.CountItemClass(29, False) > 0:
                            if Party.CountItemClass(25, True) > 0:
                                if Party.CountItemClass(27, True) > 0:
                                    if Party.CountItemClass(28, True) > 0:
                                        if Party.CountItemClass(29, True) > 0:
                                            MessageBox("With all the necessary materials, you begin work on the robot. After several hours of intensive labor, you manage to repair the robot. You follow the activation instructions and the robot turns on! You have succeeded.")
                                            StuffDone["21_1"] = 1
                                            return
                                        return
                                    return
                                return
                            return
                        ChoiceBox("An inspection of the robots reveals that only the one second from the northern wall is suitable to be fixed. The rest are probably too long gone. After sorting through all of the essentials, you discover that you will need four replacements.\n\nThe Imaging Crystal which is used to relay images to the mind has been damaged. Also, the battery on this robot has leaked making it unusable. Third, the transmitter that allows communication with the robot is also defunct.\n\nFinally, there needs to be some replacements of bad wire. You will need to find some cables to do this task. Should you be able to gather these things and repair the robot, you may be able to use it!", eDialogPic.CREATURE, 120, ["OK"])
                        return
                    ChoiceBox("An inspection of the robots reveals that only the one second from the northern wall is suitable to be fixed. The rest are probably too long gone. After sorting through all of the essentials, you discover that you will need four replacements.\n\nThe Imaging Crystal which is used to relay images to the mind has been damaged. Also, the battery on this robot has leaked making it unusable. Third, the transmitter that allows communication with the robot is also defunct.\n\nFinally, there needs to be some replacements of bad wire. You will need to find some cables to do this task. Should you be able to gather these things and repair the robot, you may be able to use it!", eDialogPic.CREATURE, 120, ["OK"])
                    return
                ChoiceBox("An inspection of the robots reveals that only the one second from the northern wall is suitable to be fixed. The rest are probably too long gone. After sorting through all of the essentials, you discover that you will need four replacements.\n\nThe Imaging Crystal which is used to relay images to the mind has been damaged. Also, the battery on this robot has leaked making it unusable. Third, the transmitter that allows communication with the robot is also defunct.\n\nFinally, there needs to be some replacements of bad wire. You will need to find some cables to do this task. Should you be able to gather these things and repair the robot, you may be able to use it!", eDialogPic.CREATURE, 120, ["OK"])
                return
            ChoiceBox("An inspection of the robots reveals that only the one second from the northern wall is suitable to be fixed. The rest are probably too long gone. After sorting through all of the essentials, you discover that you will need four replacements.\n\nThe Imaging Crystal which is used to relay images to the mind has been damaged. Also, the battery on this robot has leaked making it unusable. Third, the transmitter that allows communication with the robot is also defunct.\n\nFinally, there needs to be some replacements of bad wire. You will need to find some cables to do this task. Should you be able to gather these things and repair the robot, you may be able to use it!", eDialogPic.CREATURE, 120, ["OK"])
            return
        elif result == 1:
            return
        return

def ForgottenAcademy_947_MapTrigger_11_23(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["21_0"] == 2:
        Town.PlaceNewNPC(NPCRecord.List["Robot_235"], Location(14,25), False)
        StuffDone["21_0"] = 0
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) - 7))
        if Party.IsSplit:
            Party.Reunite()
            Sound.Play("010_teleport")
        return
    if StuffDone["21_1"] == 1:
        result = ChoiceBox("This control panel will allow you to interface with the robot. Only one of you may partake in this. Do you want to go?", eDialogPic.CREATURE, 120, ["Yes", "No"])
        if result == 0:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Robot_235": Town.NPCList.Remove(npc)
            StuffDone["21_0"] = 1
            pc = SelectPCBox("Select one member of your party?",True)
            if pc == None:
                p.CancelAction = True
                return
            Party.Split(pc, Location(14,25))
            Sound.Play("010_teleport")
            return
        elif result == 1:
            return
        return
    MessageBox("This control panel will allow you to interface with the robots. Unfortunately, none are currently operational.")

def ForgottenAcademy_948_MapTrigger_13_25(p):
    if StuffDone["21_0"] == 1:
        StuffDone["21_0"] = 2
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 7))
        return

def ForgottenAcademy_951_MapTrigger_26_31(p):
    if StuffDone["21_0"] == 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange force seems to hold you back. You try to move the robot forward, but it will not proceed past the runes. Apparently, the designers of this academy have restrictions on the robots!")
        return

def ForgottenAcademy_953_MapTrigger_11_40(p):
    if StuffDone["21_0"] == 2:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("A strange forcefield seems to be holding you back. For some reason, the designers of this academy have wanted to make sure that no one unauthorized person entered the waste area.")

def ForgottenAcademy_955_MapTrigger_18_50(p):
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["20_8"] == 1:
        MessageBox("These are the controls for the forcefield that is impeding your progress. From here, you could easily shut off the power supply, rendering the forcefield inoperative.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            MessageBox("With the push of a button, you can hear the loud forcefield off to the east shutting down! But suddenly, your connection with the robot begins to break. The corrosive chemicals in these sections have eaten away at your robot.\n\nThe image begins to fade off in static as everything blurs back into reality...")
            StuffDone["20_8"] = 2
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(12,23))
            p.CancelAction = True
            StuffDone["21_1"] = 2
            StuffDone["21_0"] = 0
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) - 7))
            if Party.IsSplit:
                Party.Reunite()
                Sound.Play("010_teleport")
            return
        return

def ForgottenAcademy_956_TownTimer_26(p):
    MessageBox("A small glowing portal appears in the center of the room!")
    Town.AlterTerrain(Location(22,5), 0, TerrainRecord.UnderlayList[78])

def ForgottenAcademy_957_TownTimer_36(p):
    if StuffDone["20_8"] == 1:
        for x in range(43, 47):
            for y in range(45, 51):
                if Maths.Rand(1,0,100) <= 80:
                    Town.PlaceField(Location(x,y), Field.FORCE_WALL)
        Timer(Town, 5, False, "ForgottenAcademy_957_TownTimer_36", eTimerType.DELETE)
        return

def ForgottenAcademy_958_OnEntry(p):
    if StuffDone["20_1"] == 250:
        return
    StuffDone["20_1"] = 250
    ChoiceBox("You make your way down the long hallway to be confronted by a large set of stairs. You eagerly climb and emerge in what appears to be some kind of waiting room.\n\nChairs and tables decorate the outside walls of this room. Additionally, is what was probably once the front desk where administrative matters were handled.\n\nOne thing that is immediately apparent is the fact that this level (at least this room of it, anyway) is in MUCH better shape than the one preceding it. The walls are comprised of thick, tough, basalt unlike the cobblestone ones below.\n\nClearly, this level was built to last. If you would not know better, you would say that this place was abandoned yesterday. There is no telling what kind of things can be lurking after so many years. Best be cautious.", eDialogPic.STANDARD, 8, ["OK"])

def ForgottenAcademy_959_CreatureDeath0(p):
    StuffDone["20_6"] += 1
    if StuffDone["20_6"] == 250:
        pass
    if StuffDone["20_6"] >= 8:
        MessageBox("A small glowing portal appears in the center of the room!")
        Town.AlterTerrain(Location(14,5), 0, TerrainRecord.UnderlayList[78])
        return

def ForgottenAcademy_967_CreatureDeath29(p):
    Town.PlaceItem(Item.List["Battery_242"].Copy(), Location(14,29))

def ForgottenAcademy_968_TalkingTrigger3(p):
    StuffDone["17_3"] = 18
    ChoiceBox("\"Odix, that traitor. It is he who is behind all of the disappearances. He has conspired with the order of Watchpoint. They have promised him good payment in order to keep the suspicion off of them by conducting research there.\n\nThey are taking the minds of my fellow magi, and using them as fuel! I know not what their aims are, but the with the treacherous order of Watchpoint involved, it cannot be good I tell you.\n\nIt\'s too late for me, but they must be stopped...Odix must be stopped! Please, do a dying man a wish and halt this horrible crime.\"\n\nPerhaps you should report this to Astervis immediately.", eDialogPic.CREATURE, 27, ["OK"])
