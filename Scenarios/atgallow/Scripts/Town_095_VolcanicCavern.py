def Generate_Wandering_95_VolcanicCavern(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([2,NPCRecord.List["Salamander_127"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([2,NPCRecord.List["Salamander_127"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([2,NPCRecord.List["Salamander_127"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["Drake_83"]])
            npcs.append([2,NPCRecord.List["Salamander_127"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(9,30)
                elif r2 == 1: l = Location(36,29)
                elif r2 == 2: l = Location(14,9)
                elif r2 == 3: l = Location(23,44)
                
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

def VolcanicCavern_2214_MapTrigger_15_22(p):
    if StuffDone["59_9"] == 250:
        return
    StuffDone["59_9"] = 250
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(15,22))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(16,22))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(23,20))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(24,20))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(28,29))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(28,30))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(16,28))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(19,31))
    TownMap.List["VolcanicCavern_95"].DeactivateTrigger(Location(22,28))
    ChoiceBox("This must be the chamber you read about in Khross\' journal. You peer through the windows and see several pieces of glowing metal floating on top of the bubbling molten rock.\n\nYou bet that metal is to be transformed into rare adamantite by Khross once the volcano erupts. The metal is probably quite valuable, but the walls are enhanced by magic and the windows protected by barrier.\n\nYou cannot take the metal at this point.", eDialogPic.STANDARD, 25, ["OK"])

def VolcanicCavern_2223_MapTrigger_22_42(p):
    if StuffDone["60_0"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Very interesting, you discover a basalt structure hidden in the volcano. You found no reference to this in Khross\' notes. The doors and wall were clearly made to resist the heat. But the level of magma prohibits you from safely opening these doors.")
        return
    if StuffDone["60_2"] == 250:
        return
    StuffDone["60_2"] = 250
    ChoiceBox("With the lava drained, you are able to open this door. The interior of this room sheds some light on this situation. Your attention is immediately grabbed by the massive drill at the end of this room.\n\nBeneath the drill is a large (and presumably deep) hole. Your questions as to the origin of this machinery is quickly answered. On the back wall on both sides of the drill are banners with the Sword and Sun insignia.\n\nThis was definitely built by the Empire. How long ago, you cannot be certain.", eDialogPic.STANDARD, 8, ["OK"])

def VolcanicCavern_2225_MapTrigger_43_43(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The cavern narrows considerably here. It is far too dangerous to try and go further, for you might get stuck.")

def VolcanicCavern_2226_MapTrigger_37_42(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(38,42)).Num == 151:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(38,43)).Num == 151:
            MessageBox("This wall is quite ancient and the constant battering by the molten rock has worn away at it. You doubt if this wall has too much longer to stand.")
            return
        return

def VolcanicCavern_2228_MapTrigger_38_45(p):
    if StuffDone["60_0"] == 0:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(38,42)).Num == 0:
            MessageBox("Using move mountains on that wall was a very good idea. The stagnated magma quickly begins to pour down into the newly opened cavern, causing the magma level to decrease significantly.")
            StuffDone["60_0"] = 1
            SuspendMapUpdate()
            for x in range(38, 48):
                for y in range(42, 45):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
            ResumeMapUpdate()
            StuffDone["61_0"] = 1
            return
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(38,43)).Num == 0:
            MessageBox("Using move mountains on that wall was a very good idea. The stagnated magma quickly begins to pour down into the newly opened cavern, causing the magma level to decrease significantly.")
            StuffDone["60_0"] = 1
            SuspendMapUpdate()
            for x in range(38, 48):
                for y in range(42, 45):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
            ResumeMapUpdate()
            StuffDone["61_0"] = 1
            return
        return

def VolcanicCavern_2229_MapTrigger_35_39(p):
    if StuffDone["60_0"] == 1:
        if StuffDone["61_0"] == 0:
            for x in range(38, 39):
                for y in range(42, 44):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            SuspendMapUpdate()
            for x in range(38, 48):
                for y in range(42, 45):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[0]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[75]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[0])
            ResumeMapUpdate()
            StuffDone["61_0"] = 1
            return
        return
    if StuffDone["60_1"] == 250:
        return
    StuffDone["60_1"] = 250
    MessageBox("You notice that this area has become a basin for the magma. It flows from the north and seems to stagnate here.")

def VolcanicCavern_2233_MapTrigger_28_40(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["60_3"] == 250:
        return
    StuffDone["60_3"] = 250
    MessageBox("This area at one time led to the mines. However, the recent stream of volcanic activity has caused this area to be inundated with hot magma. You bet that at one time there was a stairway leading deeper, no longer.")

def VolcanicCavern_2234_MapTrigger_18_39(p):
    ChoiceBox("You can always depend on the Imperial bureaucrats to leave sufficient paperwork to figure this place out.\n\nFour centuries ago during a campaign to enhance Imperial wealthy, this area was a proposed mining site. Although volcanic, this series of caverns was found to be rich in diamonds.\n\nThe problem with all out mining here is the safety concerns of mining in an active volcano. The mages constructed a drill to assist in harvesting the mine\'s wealth. Standard procedures were deemed too dangerous.\n\nThe drill is powered by three devices called steam turbines. Basically, a pump takes water from the nearby river and diverts it into three channels. The water is vaporized and the pressurized gas spins a turbine causing energy to be produced.\n\nThis mine, including all other mines in the region, was abandoned because of changes in resource allocation, namely a war.", eDialogPic.TERRAIN, 126, ["OK"])

def VolcanicCavern_2235_MapTrigger_29_23(p):
    if StuffDone["60_4"] == 0:
        MessageBox("This appears to be some kind of control panel. There is a status display, but it is dark. The machine seems to be currently off. There is a button allowing you to turn it on.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            MessageBox("You press the button. Instantly, the ancient machine turns on. You hear the sounds of steam and clanking below you. The display begins to show statistics. You are guessing that it is working.")
            StuffDone["60_4"] = 1
            return
        return
    MessageBox("The machine is currently running. The status display shows a steady 738 flarons, whatever that means. You may push the button to turn it off if you wanted.")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        MessageBox("You press the button and the machine shuts down.")
        StuffDone["60_4"] = 0
        return

def VolcanicCavern_2236_MapTrigger_31_23(p):
    result = ChoiceBox("There is a hatch that leads downward to where you can view the machinery close up. Looking down, you realize there is not much room in the compartment. Only one of you will be able to fit down there.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        if StuffDone["60_4"] == 1:
            MessageBox("Going down here while the machinery was operating was not a good idea. You realize that the machine produces steam, very hot steam. The metal ladder is extremely hot, you burn yourself and fall into the lava below.")
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
            return
        MessageBox("You observe the machinery. The device is suspended above a hot pool of water. A pipe connects the tank at the bottom. You believe this to be the heating tank. Four pipes lead up from the tank to another chamber containing a turbine.\n\nYou have heard that such devices are used to produce energy for experiments or various other projects. The system seems fine and there is little you can do here. You decide to climb back up.")
        return

def VolcanicCavern_2237_MapTrigger_8_36(p):
    if StuffDone["60_5"] == 0:
        MessageBox("This appears to be some kind of control panel. There is a status display, but it is dark. The machine seems to be currently off. There is a button allowing you to turn it on.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            MessageBox("You press the button. Instantly, the ancient machine turns on. You hear the sounds of steam and clanking below you. The display begins to show statistics. You are guessing that it is working.")
            StuffDone["60_5"] = 1
            return
        return
    MessageBox("The machine is currently running. The status display shows a steady 703 flarons, whatever that means. You may push the button to turn it off if you wanted.")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        MessageBox("You press the button and the machine shuts down.")
        StuffDone["60_5"] = 0
        return

def VolcanicCavern_2238_MapTrigger_8_38(p):
    result = ChoiceBox("There is a hatch that leads downward to where you can view the machinery close up. Looking down, you realize there is not much room in the compartment. Only one of you will be able to fit down there.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        if StuffDone["60_5"] == 1:
            MessageBox("Going down here while the machinery was operating was not a good idea. You realize that the machine produces steam, very hot steam. The metal ladder is extremely hot, you burn yourself and fall into the lava below.")
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
            return
        MessageBox("You observe the machinery. The device is suspended above a hot pool of water. A pipe connects the tank at the bottom. You believe this to be the heating tank. Four pipes lead up from the tank to another chamber containing a turbine.\n\nYou have heard that such devices are used to produce energy for experiments or various other projects. The system seems fine and there is little you can do here. You decide to climb back up.")
        return

def VolcanicCavern_2239_MapTrigger_9_19(p):
    if StuffDone["60_6"] >= 2:
        MessageBox("The machine is currently running. The status display shows a steady 682 flarons, whatever that means. You may push the button to turn it off if you wanted.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            StuffDone["60_6"] = 0
            return
        return
    if StuffDone["60_6"] < 1:
        MessageBox("This appears to be some kind of control panel. There is a status display, but it is dark. The machine seems to be currently off. There is a button allowing you to turn it on.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            if StuffDone["60_7"] == 0:
                MessageBox("You press the button. Instantly, the ancient machine turns on. You hear the sounds of steam and clanking below you. The display begins to show statistics. You are guessing that it is working.")
                StuffDone["60_6"] = 1
                return
            MessageBox("You press the button. Instantly, the ancient machine turns on. You hear the sounds of steam and clanking below you. The display begins to show statistics. You are guessing that it is working.")
            StuffDone["60_6"] = 2
            return
        return
    MessageBox("The machine is currently running. The status display shows a steady 352 flarons, whatever that means. You may push the button to turn it off if you wanted.")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        StuffDone["60_6"] = 0
        return

def VolcanicCavern_2240_MapTrigger_9_21(p):
    result = ChoiceBox("There is a hatch that leads downward to where you can view the machinery close up. Looking down, you realize there is not much room in the compartment. Only one of you will be able to fit down there.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        if StuffDone["60_6"] >= 1:
            MessageBox("Going down here while the machinery was operating was not a good idea. You realize that the machine produces steam, very hot steam. The metal ladder is extremely hot, you burn yourself and fall into the lava below.")
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
            return
        if StuffDone["60_7"] == 0:
            MessageBox("You observe the machinery. The device is suspended above a hot pool of water. A pipe connects the tank at the bottom. You believe this to be the heating tank. Four pipes lead up from the tank to another chamber containing a turbine.\n\nYou inspect the pipes and find a small crack in one of the four. This could mean less energy is being delivered. If you could seal the crack with, say some metal, you could perhaps improve the energy level to the drill.")
            if Party.CountItemClass(47, True) > 0:
                MessageBox("You return temporarily and inspect your inventory. The iron bar you are carrying around just may provide the needed sealant. You return into the pit and heat one end of the bar using the lava until it is almost liquid.\n\nCareful to cover your hand with thick cloth to keep from burning your skin, you place the molten area on the pipe. Using a weapon as a hammer, you manage to seal the crack. It appears the pipe is repaired.")
                StuffDone["60_7"] = 1
                return
            return
        MessageBox("You observe the machinery. The device is suspended above a hot pool of water. A pipe connects the tank at the bottom. You believe this to be the heating tank. Four pipes lead up from the tank to another chamber containing a turbine.\n\nYou have heard that such devices are used to produce energy for experiments or various other projects. The system seems fine and there is little you can do here. You decide to climb back up.")
        return

def VolcanicCavern_2241_MapTrigger_24_38(p):
    if StuffDone["60_8"] == 0:
        result = ChoiceBox("This control panel operates this massive drill. Considering the instability of these caverns, it may not be wise to disturb the geologic features of these caverns. The drill controls are quite sophisticated allowing you to rotate and move about.\n\nIt would take some time to familiarize oneself with the controls completely. However, you will not be able to drill anything until you push the power button.", eDialogPic.TERRAIN, 125, ["Leave", "Push"])
        if result == 1:
            if StuffDone["60_4"] == 1:
                if StuffDone["60_5"] == 1:
                    if StuffDone["60_6"] >= 2:
                        ChoiceBox("You push the button and the drill turns on. It begins to spin, ready to bore into the rock. The spin is fast, it appears that your repairs have succeeded. You bet that you will be able to make some sufficient holes with that.\n\nYou lower it into the pit for a while. Eventually you feel that you have stuck solid rock. You instantly begin to bore deeper. The process is slow and produces the sensation of burning metal.\n\nYou are not sure exactly what you are going to do with this. Even if you could reveal some diamonds, you have no idea how you are going to excavate them. But, this sure is fun.\n\nThen suddenly, you break through into an open area!", eDialogPic.TERRAIN, 125, ["OK"])
                        Animation_Hold(-1, 060_smallboom)
                        Wait()
                        Animation_Hold(-1, 060_smallboom)
                        Wait()
                        Animation_Hold(-1, 005_explosion)
                        Wait()
                        Animation_Hold(-1, 060_smallboom)
                        Wait()
                        StuffDone["60_8"] = 1
                        ChoiceBox("Uh oh! You seem to have caused a major shift in the geologic features. You listen trying to deduce what happened. You then realize that the noises of crumbling, lava bubbling, and explosions are growing louder.\n\nThe sounds are not local either, they seem to be coming from all over the cavern. It seems you may have sparked a volcanic eruption. If that is the case, you should probably get out of here immediately!", eDialogPic.STANDARD, 25, ["OK"])
                        Timer(Town, 200, False, "VolcanicCavern_2265_TownTimer_73", eTimerType.DELETE)
                        Timer(Town, 10, False, "VolcanicCavern_2266_TownTimer_77", eTimerType.DELETE)
                        Timer(Town, 8, False, "VolcanicCavern_2268_TownTimer_82", eTimerType.DELETE)
                        return
                    if StuffDone["60_6"] < 1:
                        MessageBox("You press the button but nothing seems to happen. Either the device is broken, or it lacks the power to operate.")
                        return
                    MessageBox("You push the button and the drill turns on. It begins to spin, ready to bore into the rock. However, the spin is quite slow. You doubt that it will be able to do anything. You search the controls and find a speed control dial.\n\nYou turn it up to the maximum, but it does not improve the situation too much. But really, what can you expect from such ancient machinery?")
                    return
                MessageBox("You press the button but nothing seems to happen. Either the device is broken, or it lacks the power to operate.")
                return
            MessageBox("You press the button but nothing seems to happen. Either the device is broken, or it lacks the power to operate.")
            return
        return

def VolcanicCavern_2242_MapTrigger_24_6(p):
    if StuffDone["60_8"] == 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("It would be wise not to return here. The volcano is still quite violent. Going any further is sure to bring death.")
        return

def VolcanicCavern_2243_MapTrigger_24_25(p):
    if Maths.Rand(1,0,100) < 30:
        Animation_Hold(-1, 005_explosion)
        Wait()
        if Party.HasTrait(Trait.CaveLore):
            if Maths.Rand(1,0,100) < 60:
                MessageBox("Your knowledge of Cave Lore assisted you in avoiding a little accident. You realized in advance that the lava was about ready to bubble and stayed back until the coast was clear. That sure was a close call though!")
                return
            MessageBox("Volcanos are inherently dangerous places. You step on this space just as it bursts, spewing lava all over you. The burns are only minor, but it sure hurt a lot.")
            Party.Damage(Maths.Rand(5, 1, 4) + 5, eDamageType.FIRE)
            Wait()
            return
        MessageBox("Volcanos are inherently dangerous places. You step on this space just as it bursts, spewing lava all over you. The burns are only minor, but it sure hurt a lot.")
        Party.Damage(Maths.Rand(5, 1, 4) + 5, eDamageType.FIRE)
        Wait()
        return

def VolcanicCavern_2263_MapTrigger_39_38(p):
    MessageBox("These controls operated a lava flow gate. You are guessing that is the thing you just shattered. These controls are now worthless.")

def VolcanicCavern_2265_TownTimer_73(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    Animation_Hold(-1, 005_explosion)
    Wait()
    MessageBox("You were a bit too slow in escaping from the mine. The eruption appears to now be in full swing. The entire cavern is flooded with a violent surge of lava. You have not the magic to protect you and you are reduced to ash.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def VolcanicCavern_2266_TownTimer_77(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    Party.Damage(Maths.Rand(6, 1, 5) + 10, eDamageType.FIRE)
    Wait()
    Timer(Town, 15, False, "VolcanicCavern_2266_TownTimer_77", eTimerType.DELETE)
    if StuffDone["60_9"] == 250:
        return
    StuffDone["60_9"] = 250
    MessageBox("Suddenly lava splashes up in front of you, searing your skin. The explosions and the sounds are getting louder and louder. It would be best to hurry.")

def VolcanicCavern_2268_TownTimer_82(p):
    Animation_Hold(-1, 060_smallboom)
    Wait()
    Timer(Town, 8, False, "VolcanicCavern_2268_TownTimer_82", eTimerType.DELETE)

def VolcanicCavern_2269_ExitTown(p):
    if p.Dir.IsNorth:
        StuffDone["61_0"] = 0
