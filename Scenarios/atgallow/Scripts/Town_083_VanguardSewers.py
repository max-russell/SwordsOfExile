def Generate_Wandering_83_VanguardSewers(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["MungRoach_146"]])
            npcs.append([1,NPCRecord.List["LargeRoach_144"]])
            npcs.append([1,NPCRecord.List["Cockroach_143"]])
            npcs.append([2,NPCRecord.List["Cockroach_143"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["MungRoach_146"]])
            npcs.append([1,NPCRecord.List["LargeRoach_144"]])
            npcs.append([1,NPCRecord.List["Cockroach_143"]])
            npcs.append([2,NPCRecord.List["Cockroach_143"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["MungRoach_146"]])
            npcs.append([1,NPCRecord.List["LargeRoach_144"]])
            npcs.append([1,NPCRecord.List["Cockroach_143"]])
            npcs.append([2,NPCRecord.List["Cockroach_143"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["MungRoach_146"]])
            npcs.append([1,NPCRecord.List["LargeRoach_144"]])
            npcs.append([1,NPCRecord.List["Cockroach_143"]])
            npcs.append([2,NPCRecord.List["Cockroach_143"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(18,34)
                elif r2 == 1: l = Location(35,34)
                elif r2 == 2: l = Location(2,7)
                elif r2 == 3: l = Location(20,53)
                
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

def VanguardSewers_2063_MapTrigger_60_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(52,54)
    Party.MoveToMap(TownMap.List["Vanguard_9"])

def VanguardSewers_2064_MapTrigger_56_59(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["43_1"] == 250:
        return
    StuffDone["43_1"] = 250
    MessageBox("You\'re not sure if coming down here was a good idea. The smell of decaying waste is awful. No wonder why the Empire hasn\'t found the rebels yet. No soldier would dare come down here; let alone conduct an extensive search.\n\nYou only hope that you can find the rebels soon, very soon.")

def VanguardSewers_2066_MapTrigger_40_48(p):
    if StuffDone["43_2"] == 250:
        return
    StuffDone["43_2"] = 250
    TownMap.List["VanguardSewers_83"].DeactivateTrigger(Location(40,48))
    TownMap.List["VanguardSewers_83"].DeactivateTrigger(Location(41,48))
    MessageBox("You\'re in a slimy, monster-filled sewer! That\'s bad enough, but some very intelligent people just decided to leave no boats at the docks for you. Looks like you have another obstacle in front of you.\n\nHowever, these are the \'southern\' docks. Hopefully there is another set of docks. But with the way things are going, you don\'t count on there being \'northern\' or \'western\' docks.")

def VanguardSewers_2068_MapTrigger_5_55(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        t = Town.TerrainAt(Location(32,46))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(32,46), 0, TerrainRecord.UnderlayList[73])
        elif t == TerrainRecord.UnderlayList[73]: Town.AlterTerrain(Location(32,46), 0, TerrainRecord.UnderlayList[71])
        MessageBox("You pull the lever. You hear creaky gears turning.")
        t = Town.TerrainAt(Location(32,52))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(32,52), 0, TerrainRecord.UnderlayList[73])
        elif t == TerrainRecord.UnderlayList[73]: Town.AlterTerrain(Location(32,52), 0, TerrainRecord.UnderlayList[71])
        return

def VanguardSewers_2069_MapTrigger_22_28(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        t = Town.TerrainAt(Location(9,27))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(9,27), 0, TerrainRecord.UnderlayList[73])
        elif t == TerrainRecord.UnderlayList[73]: Town.AlterTerrain(Location(9,27), 0, TerrainRecord.UnderlayList[71])
        MessageBox("You pull the lever. You hear creaky gears turning.")
        t = Town.TerrainAt(Location(25,29))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(25,29), 0, TerrainRecord.UnderlayList[130])
        elif t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(25,29), 0, TerrainRecord.UnderlayList[71])
        return

def VanguardSewers_2070_MapTrigger_23_35(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. You hear creaky gears turning.")
        t = Town.TerrainAt(Location(25,35))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(25,35), 0, TerrainRecord.UnderlayList[130])
        elif t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(25,35), 0, TerrainRecord.UnderlayList[71])
        return

def VanguardSewers_2071_MapTrigger_29_31(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever and hear machinery creaking. However, it stops. The machine is stuck! Another frustrating moment in your adventuring career.")
        return

def VanguardSewers_2072_MapTrigger_28_24(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. You hear creaky gears turning.")
        t = Town.TerrainAt(Location(32,23))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(32,23), 0, TerrainRecord.UnderlayList[130])
        elif t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(32,23), 0, TerrainRecord.UnderlayList[71])
        return

def VanguardSewers_2074_MapTrigger_12_4(p):
    if StuffDone["43_3"] == 250:
        return
    StuffDone["43_3"] = 250
    TownMap.List["VanguardSewers_83"].DeactivateTrigger(Location(12,4))
    MessageBox("A bittersweet sight faces you. On the bright side, there is one boat for your use. On the dimmer side, the boat is on dry land! Somehow you\'re going to have to provide a stream.")

def VanguardSewers_2075_MapTrigger_43_6(p):
    if StuffDone["43_4"] == 0:
        MessageBox("You find the decaying body of a middle-aged man in a sewer worker uniform. He was clearly murdered by the many dagger wounds. You search his body and find a small key in his pocket.")
        StuffDone["43_4"] = 1
        return

def VanguardSewers_2076_MapTrigger_21_20(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(21,19)).Num == 128:
        if StuffDone["43_4"] == 1:
            MessageBox("This door has a large padlock latched upon it. You use the key you found on the dead sewer worker\'s body. It opens the padlock. You may continue.")
            t = Town.TerrainAt(Location(21,19))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(21,19)).TransformTo
                Town.AlterTerrain(Location(21,19), 0, t)
            return
        MessageBox("This door has a large padlock latched upon it. You won\'t be able to pass until you have the proper key; which you do not.")
        return

def VanguardSewers_2078_MapTrigger_18_17(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. You hear creaky gears turning.")
        t = Town.TerrainAt(Location(15,19))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(15,19), 0, TerrainRecord.UnderlayList[130])
        elif t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(15,19), 0, TerrainRecord.UnderlayList[71])
        if StuffDone["43_5"] == 250:
            return
        StuffDone["43_5"] = 250
        MessageBox("You look out the window and see a massive wave of water rushing into the dry trench below.")
        SuspendMapUpdate()
        for x in range(13, 18):
            for y in range(6, 19):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[90]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
        ResumeMapUpdate()
        return

def VanguardSewers_2079_MapTrigger_43_23(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. You hear creaky gears turning.")
        t = Town.TerrainAt(Location(44,26))
        if t == TerrainRecord.UnderlayList[71]: Town.AlterTerrain(Location(44,26), 0, TerrainRecord.UnderlayList[130])
        elif t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(44,26), 0, TerrainRecord.UnderlayList[71])
        return

def VanguardSewers_2080_MapTrigger_60_28(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["43_6"] == 250:
        return
    StuffDone["43_6"] = 250
    MessageBox("It appears your search is over. You have found the rebel\'s base. You notice that the stench is nonexistent here, thankfully. Some magical force must lie here. Now it is time to fight.")

def VanguardSewers_2081_MapTrigger_25_36(p):
    MessageBox("Not a wise move. You get caught in the current and are pulled down into the cleansing pool. The magical machinery grinds you into a pulp and dissolves you with acids. Not a good way to go.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def VanguardSewers_2082_MapTrigger_56_16(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(55,16)).Num == 128:
        if StuffDone["43_7"] == 1:
            MessageBox("This door has a large padlock latched upon it. You try the key you found on the Dervish\'s body. The padlock opens! You may continue.")
            t = Town.TerrainAt(Location(55,16))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(55,16)).TransformTo
                Town.AlterTerrain(Location(55,16), 0, t)
            return
        MessageBox("This door has a large padlock latched upon it. You won\'t be able to pass until you have the proper key; which you do not.")
        return

def VanguardSewers_2084_MapTrigger_53_12(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(36,13)
    Party.MoveToMap(TownMap.List["Vanguard_9"])

def VanguardSewers_2085_OnEntry(p):
    if StuffDone["43_5"] >= 1:
        SuspendMapUpdate()
        for x in range(13, 18):
            for y in range(6, 19):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[90]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
        ResumeMapUpdate()
        return

def VanguardSewers_2086_CreatureDeath12(p):
    MessageBox("The person you have just killed was an Imperial Dervish, a traitor. Dervish Saab will be very pleased to have him out of the way. A search of his body reveals a key.")
    StuffDone["43_8"] = 1
