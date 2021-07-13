def Generate_Wandering_0_ArmsDepot(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([2,NPCRecord.List["Goblin_38"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Ogre_45"]])
            npcs.append([1,NPCRecord.List["Ogre_45"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
            npcs.append([1,NPCRecord.List["Ogre_45"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(100,0)
                elif r2 == 1: l = Location(100,0)
                elif r2 == 2: l = Location(100,0)
                elif r2 == 3: l = Location(100,0)
                
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

def ArmsDepot_0_MapTrigger_27_20(p):
    if StuffDone["0_0"] == 250:
        return
    StuffDone["0_0"] = 250
    TownMap.List["ArmsDepot_0"].AlterTerrain(Location(27,20), 1, None)
    TownMap.List["ArmsDepot_0"].DeactivateTrigger(Location(27,20))
    MessageBox("Your last hopes for row upon row of fine suits of armour and gleaming weapons are shattered. Someone has broken in and looted the arms shed, only useless garbage remains.")

def ArmsDepot_1_MapTrigger_25_19(p):
    if StuffDone["0_1"] == 250:
        return
    result = ChoiceBox("Those who looted this room evidently did not understand the value of this scroll. It was left rotting with the garbage.", eDialogPic.TERRAIN, 228, ["Take", "Leave"])
    if result == 0:
        StuffDone["0_1"] = 250
        TownMap.List["ArmsDepot_0"].DeactivateTrigger(Location(25,19))
        Party.GiveNewItem("ScrollFirestorm_203")
    return

def ArmsDepot_2_MapTrigger_31_33(p):
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
    pc.RunTrap(eTrapType.BLADE, 1, 20)
    if StuffDone["0_2"] == 250:
        return
    StuffDone["0_2"] = 250
    MessageBox("You finally uncover some weapons and equipment of the fort depot.")

def ArmsDepot_5_MapTrigger_20_38(p):
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
    pc.RunTrap(eTrapType.DART, 2, 10)

def ArmsDepot_6_MapTrigger_24_24(p):
    if StuffDone["0_3"] == 250:
        return
    StuffDone["0_3"] = 250
    TownMap.List["ArmsDepot_0"].DeactivateTrigger(Location(24,24))
    MessageBox("It appears that humanoids are responsible for looting this place. Perhaps, if their hide-out is not too distant, you can still salvage some of your equipment.")

def ArmsDepot_8_MapTrigger_23_16(p):
    if StuffDone["0_4"] == 250:
        return
    StuffDone["0_4"] = 250
    TownMap.List["ArmsDepot_0"].DeactivateTrigger(Location(23,16))
    TownMap.List["ArmsDepot_0"].DeactivateTrigger(Location(22,16))
    ChoiceBox("The arms depot is placed in the side of a hill. Even from a distance, you can see that the walls sag and crumble from neglect. You hope that the goods inside is still intact, but worry gnaws at you.\n\nYou approach the portcullis and shake the bars. Locked. During the terrifying hours since the attack on your fort, you have put every effort into getting to the depot.\n\nNow that you are here, it occurs you that you have no idea of how to get inside. You certainly will not be able to squeeze through the grate. Still, considering the state of the walls, you hope you can find a second way of entry.", eDialogPic.TERRAIN, 242, ["OK"])

def ArmsDepot_10_MapTrigger_34_15(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The ceiling of this short corridor has fallen in, effectively blocking it. Blackened rock and marks from picks make you wonder if the cave-in was accidental. For whatever reason, this way is permanently blocked.")

def ArmsDepot_11_MapTrigger_38_21(p):
    if StuffDone["0_5"] == 250:
        return
    StuffDone["0_5"] = 250
    TownMap.List["ArmsDepot_0"].DeactivateTrigger(Location(38,21))
    MessageBox("The soft light that you have come to think of as daylight in the caves, shines faintly ahead (It is not daylight in the sense that it tells the time of day, but at least it allows you to discern the small living caves from big, \"outdoor caves\".).")

def ArmsDepot_12_MapTrigger_38_14(p):
    if StuffDone["0_6"] >= 1:
        return
    if SpecialItem.PartyHas("Ironcone"):
        result = ChoiceBox("Somebody has made an earnest attempt at opening these battered bars. Ashes on the floor hint that a spell caster tired of unlocking spells and tried a fireball in pure frustration. Given the tempting contents, you sympathize.\n\nYou wonder dispiritedly if you can do any better. Then you notice a slot in the wall next to the bars. It is a small opening that makes you think of something.\n\nYou suddenly remember, and pull out the strange iron cone you found in Mathias? office. You hold it up next to the hole. It matches exactly. Do you put it in?", eDialogPic.TERRAIN, 92, ["Leave", "Insert"])
        if result == 1:
            MessageBox("You insert the strange key and give it a good push. The portcullis groans and rumbles, and finally rises. The cone gets stuck in the lock, though.")
            t = Town.TerrainAt(Location(39,14))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(39,14)).TransformTo
                Town.AlterTerrain(Location(39,14), 0, t)
            SpecialItem.Take("Ironcone")
            StuffDone["0_6"] = 1
            return
        return
    MessageBox("Somebody has made an earnest attempt at opening these battered bars. Ashes on the floor hint that a spell caster tired of unlocking spells and tried a fireball in pure frustration. Given the tempting contents, you sympathize.\n\nYou wonder dispiritedly if you can do any better. After a few shoves, you decide to give up, and turn away with a wistful look over your shoulder.")
