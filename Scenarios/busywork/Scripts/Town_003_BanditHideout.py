def Generate_Wandering_3_BanditHideout(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Brigand_18"]])
            npcs.append([1,NPCRecord.List["Brigand_18"]])
            npcs.append([1,NPCRecord.List["Brigand_18"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Archer_19"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(4,11)
                elif r2 == 1: l = Location(27,5)
                elif r2 == 2: l = Location(34,20)
                elif r2 == 3: l = Location(35,36)
                
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

def BanditHideout_42_MapTrigger_40_43(p):
    if StuffDone["3_0"] == 250:
        return
    StuffDone["3_0"] = 250
    TownMap.List["BanditHideout_3"].DeactivateTrigger(Location(40,43))
    ChoiceBox("You finally make your way into the Bandit\'s Hideout. It was well concealed ... mounds of brush were heaped in front of the entrance, and dirt was piles onto the brush. You were only able to see it from right outside.\n\nOnce you\'re in, you\'re greeted by a grim, stomach turning sight. The cavern is filled with grisly totems, weapons and bones taken from the merchants killed while trying to leave Mrrnah Hollow. They must be trying to scare off anyone who gets that far.\n\nThey didn\'t count on you, though ...", eDialogPic.TERRAIN, 193, ["OK"])

def BanditHideout_43_MapTrigger_36_24(p):
    if StuffDone["3_1"] == 250:
        return
    StuffDone["3_1"] = 250
    TownMap.List["BanditHideout_3"].DeactivateTrigger(Location(36,24))
    MessageBox("Watching the floor carefully, you can see the signs of many passing feet. The bandits must have been marching in and out of here for months, carrying supplies and building their lair.")

def BanditHideout_44_MapTrigger_35_12(p):
    if Party.HasTrait(Trait.CaveLore):
        if StuffDone["3_2"] == 250:
            return
        StuffDone["3_2"] = 250
        MessageBox("Interesting ... you notice that the signs of people passing stop abruptly here. It doesn\'t look like anyone has walked down this corridor for a while.")
        return

def BanditHideout_45_MapTrigger_41_16(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(34,15)).Num == 9:
        MessageBox("As you search this bunch of stalagmites, one of them moves slightly when your hand brushes against it. You push the loose stalagmite, and find that it moves like a lever.\n\nYou puch it until it stops. When it does, you hear a loud click, followed by a grinding noise from the west.")
        Town.AlterTerrain(Location(34,15), 0, TerrainRecord.UnderlayList[10])
        return

def BanditHideout_47_MapTrigger_23_29(p):
    if StuffDone["3_3"] == 250:
        return
    StuffDone["3_3"] = 250
    TownMap.List["BanditHideout_3"].DeactivateTrigger(Location(23,29))
    MessageBox("This is a storeroom, filled with new, well oiled weapons. You recognize them ... they were clearly made in Cameron\'s smithy back in Cavala. Now you know why he was working so hard.")

def BanditHideout_48_MapTrigger_29_17(p):
    MessageBox("When you move the dried ogre head, you hear a clicking noise.")
    Town.AlterTerrain(Location(26,20), 0, TerrainRecord.UnderlayList[170])

def BanditHideout_49_MapTrigger_26_23(p):
    if StuffDone["3_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["3_4"] = 250
    TownMap.List["BanditHideout_3"].DeactivateTrigger(Location(26,23))
    pc.RunTrap(eTrapType.GAS, 2, 25)

def BanditHideout_50_CreatureDeath30(p):
    ChoiceBox("With a final, decisive blow, Cameron, leader of the bandits and traitor of Cavala, dies. With him dies the bandits\' dominance in Mrrnah Hollow.\n\nWith this victory, your mission here is completed. Thanks to you Cavala will be able to grow and prosper once again.", eDialogPic.CREATURE, 14, ["OK"])
    for pc in Party.EachAlivePC():
        pc.AwardXP(10)
    StuffDone["100_0"] = 1
