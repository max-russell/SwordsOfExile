
def UpperTower_441_MapTrigger_16_16(p):
    if StuffDone["8_3"] == 250:
        return
    StuffDone["8_3"] = 250
    TownMap.List["UpperTower_22"].AlterTerrain(Location(16,16), 1, None)
    TownMap.List["UpperTower_22"].DeactivateTrigger(Location(16,16))
    Town.PlaceEncounterGroup(1)
    t = Town.TerrainAt(Location(16,24))
    if t.InGroup("Lockable"):
        t = Town.TerrainAt(Location(16,24)).TransformTo
        Town.AlterTerrain(Location(16,24), 0, t)
    ChoiceBox("You look around and see no signs of life (or unlife in this case). Could it be that the great Halloth has fled! In which case this entire assault would be in vain. You then hear several bat screeches above you.\n\nYou look up and see a storm of about twenty bats hovering near the top of the dome shaped roof. They are not ordinary bats, but larger nastier Vamprye Bats. They seem to fly aimlessly for a while. Then the bats form a circle around you!\n\nEven if Halloth has fled, he left his pets to take care of you.", eDialogPic.CREATURE, 70, ["OK"])

def UpperTower_442_MapTrigger_15_29(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["8_4"] == 0:
        result = ChoiceBox("This stairway leads back down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
        if result == 1:
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(32,33)
            Party.MoveToMap(TownMap.List["HallothsCitadel_21"])
            return
        return
    if Party.CountItemClass(2, True) > 0:
        Party.GiveNewItem("Lyra_183")
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(33,33)
        Party.MoveToMap(TownMap.List["FortReflection_17"])
        return
    Party.OutsidePos = Location(70, 124)
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(33,33)
    Party.MoveToMap(TownMap.List["FortReflection_17"])

def UpperTower_445_TownTimer_11(p):
    if StuffDone["8_4"] == 0:
        if Maths.Rand(1,0,100) < 50:
            if Maths.Rand(1,0,100) < 50:
                Message("Halloth Casts:")
                Message("  Excommunicate")
                Animation_Hold(-1, 024_priestspell)
                Wait()
                for pc in Party.EachAlivePC():
                    pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 3))
                for pc in Party.EachAlivePC():
                    pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 3))
                Timer(Town, 4, False, "UpperTower_445_TownTimer_11", eTimerType.DELETE)
                return
            Message("Halloth Casts:")
            Message("  Mass Paralysis")
            Animation_Hold(-1, 025_magespell)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.PARALYZED, Maths.MinMax(0, 5000, pc.Status(eAffliction.PARALYZED) + 5))
            Timer(Town, 4, False, "UpperTower_445_TownTimer_11", eTimerType.DELETE)
            return
        if Maths.Rand(1,0,100) < 50:
            Message("Halloth Casts:")
            Message("  Psychic Pulse")
            Animation_Hold(-1, 053_magic3)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 2))
            Timer(Town, 4, False, "UpperTower_445_TownTimer_11", eTimerType.DELETE)
            return
        Message("Halloth Casts:")
        Message("  Arctic Fury")
        Animation_Hold(-1, 025_magespell)
        Wait()
        Party.Damage(Maths.Rand(4, 1, 5) + 10, eDamageType.COLD)
        Wait()
        Timer(Town, 4, False, "UpperTower_445_TownTimer_11", eTimerType.DELETE)
        return

def UpperTower_446_CreatureDeath0(p):
    ChoiceBox("After a long and drawn out battle, you have finally inflicted enough damage to cause Halloth to \'die\'. \"Nooooo! It cannot be. Beaten by mortals again...\" Halloth\'s body  disintegrates as he screams in fury.\n\nYou can also hear the sounds of the other undead below screeching out in terror as they too are pulled away from this physical plane along with their master. You have slain Halloth and saved many many lives from his clutches.\n\nDervish Montcalm and the rest of the Empire will be pleased.", eDialogPic.STANDARD, 1025, ["OK"])
    Town.NPCList.Clear()
    for pc in Party.EachAlivePC():
        pc.AwardXP(25)
    StuffDone["6_4"] = 4
    StuffDone["2_0"] = 7
    StuffDone["8_6"] = 1
    t = Town.TerrainAt(Location(16,24))
    if t.InGroup("Unlockable"):
        t = Town.TerrainAt(Location(16,24)).TransformTo
        Town.AlterTerrain(Location(16,24), 0, t)
    StuffDone["100_1"] = 1
    if Party.CountItemClass(2, True) > 0:
        Party.GiveNewItem("Lyra_183")
        return

def UpperTower_447_CreatureDeath1(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if  npc.IsABaddie: Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(2)
    Animation_Hold(-1, 004_bless)
    Wait()
    ChoiceBox("This bat does not die like the others. When you slay it, this bat flashes out of existence! Instantly, the other Vampyre Bats scatter away seeming to no longer take interest in you. There must have been something special about that bat.\n\nSuddenly you hear a grim laughter. You look to the throne and you see the same bat floating down. It transmutes into a large humanoid figure. The figure is massive standing seven feet tall! It glares at you with fiery red eyes.\n\nYou are now face to face with the master of this Citadel, the bane of the Aizic Sector, the mighty Halloth! The creature begins to speak in a booming voice seeming to come from everywhere in the room.\n\n\"Ah foolish mortals! Well met. I am not amused by your intrusion into my Citadel and the damage you have done to my plans. I can sense fear in you. You should be afraid, for now you will have the honor to perish at my hands!\"", eDialogPic.STANDARD, 1025, ["OK"])
    if Party.CountItemClass(1, True) > 0:
        Party.GiveNewItem("Lyra_184")
        Animation_Hold(-1, 053_magic3)
        Wait()
        ChoiceBox("Suddenly, Lyra begins to vibrate. The entire blade starts to glow green. Halloth looks at the sword and for the first time, his expression shows fear. He speaks, \"So you have the sword. No matter, you are still no match for me!\"\n\nLyra has awakened and her spirit is ready to help you slay Halloth!", eDialogPic.STANDARD, 0, ["OK"])
        Timer(Town, 4, False, "UpperTower_445_TownTimer_11", eTimerType.DELETE)
        return
    Timer(Town, 4, False, "UpperTower_445_TownTimer_11", eTimerType.DELETE)
