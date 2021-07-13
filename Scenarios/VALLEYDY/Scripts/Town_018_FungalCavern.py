def Generate_Wandering_18_FungalCavern(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Bat_82"]])
            npcs.append([1,NPCRecord.List["Bat_82"]])
            npcs.append([1,NPCRecord.List["Bat_82"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Serpent_99"]])
            npcs.append([1,NPCRecord.List["Serpent_99"]])
            npcs.append([1,NPCRecord.List["Serpent_99"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Skeleton_58"]])
            npcs.append([1,NPCRecord.List["Skeleton_58"]])
            npcs.append([1,NPCRecord.List["Skeleton_58"]])
            npcs.append([2,NPCRecord.List["Skeleton_58"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["SporeBeast_134"]])
            npcs.append([1,NPCRecord.List["SporeBeast_134"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(24,16)
                elif r2 == 1: l = Location(41,4)
                elif r2 == 2: l = Location(8,36)
                elif r2 == 3: l = Location(19,30)
                
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

def FungalCavern_346_MapTrigger_7_40(p):
    if StuffDone["18_0"] == 250:
        return
    StuffDone["18_0"] = 250
    TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(7,40))
    ChoiceBox("You have stumbled upon a strange, hidden underground wonderland! The air is cool and damp, the perfect atmosphere for the variety of fungi growing down here!\n\nMolds, mosses, mushrooms and toadstools form a wild, undisturbed fairyland, which you are now free to frolic about in! It\'s actually quite lovely, and you can\'t imagine anything down here trying to hurt you.", eDialogPic.TERRAIN, 73, ["OK"])

def FungalCavern_347_MapTrigger_30_28(p):
    if StuffDone["18_1"] == 250:
        return
    StuffDone["18_1"] = 250
    TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(30,28))
    ChoiceBox("While this fungus infested series of caverns seemed completely undisturbed, it\'s quite clear that someone has been here before. You find the walls of some sort of stone structure.\n\nThe dark stone is covered with thin cracks, as well as many thick patches of mold and lichen. Whatever it is, it\'s been here for quite some time.", eDialogPic.TERRAIN, 106, ["OK"])

def FungalCavern_348_MapTrigger_32_27(p):
    if StuffDone["18_2"] == 250:
        return
    StuffDone["18_2"] = 250
    TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(32,27))
    TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(32,28))
    TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(32,29))
    ChoiceBox("You find your way inside the structure, which is definitely a crypt. Bones crunch underfoot. However, they aren\'t the bones of those buried here, but of those unfortunate enough to stumble upon this place.\n\nThere has been no shortage of spelunkers and adventurers slain here by the undead residents of this crypt. These lost souls are even now rising up, hoping to have you join them in their eternal, moldy slumber.", eDialogPic.CREATURE, 53, ["OK"])
    Town.PlaceEncounterGroup(1)

def FungalCavern_351_MapTrigger_39_25(p):
    if StuffDone["18_4"] == 250:
        return
    StuffDone["18_4"] = 250
    TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(39,25))
    MessageBox("You find a small gemstone hidden behind the brazier!")
    Party.GiveNewItem("ShieldingCrystal_186")

def FungalCavern_352_MapTrigger_39_28(p):
    if StuffDone["18_3"] == 250:
        return
    result = ChoiceBox("Walking back behind the bier, you notice a small niche in its back, near the floor. You bend down and peer inside, and can make out a long, slender blade! There\'s also a number of small jewels. Looks like quite a haul.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["18_3"] = 250
        TownMap.List["FungalCavern_18"].DeactivateTrigger(Location(39,28))
        Party.GiveNewItem("SteelRapier_70")
        Party.Gold += 400
        MessageBox("Unfortunately, you seem to have triggered some sort of a curse. The fate for graverobbers in this crypt is pretty unpleasant. Wracking stomach cramps double you over, and it feels like acid is coursing its way around your veins instead of blood.")
        for pc in Party.EachAlivePC():
            pc.Poison(8)
        return
    return

def FungalCavern_353_TownTimer_0(p):
    MessageBox("The moist atmosphere of these tunnels is starting to make you feel chilly.")
