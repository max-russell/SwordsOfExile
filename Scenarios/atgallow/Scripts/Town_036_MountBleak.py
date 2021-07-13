
def MountBleak_778_MapTrigger_7_13(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(49,46)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_780_MapTrigger_2_50(p):
    if StuffDone["9_6"] == 250:
        return
    StuffDone["9_6"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(2,50))
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(3,50))
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(6,50))
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(7,50))
    MessageBox("You see a middle aged woman in the cave ahead. She spots you and pulls out a knife. \"Who goes there!\" She looks you over. \"Empire soldiers finally come to arrest us? Well, you\'ll never take us alive!\"\n\nYou assure her that you are not here to arrest her or whoever else lives here. She puts away the knife. \"Sorry. Cain and I had some pretty bad experiences with your kind. Anyway, we welcome you visitors.\"")

def MountBleak_784_MapTrigger_6_29(p):
    result = ChoiceBox("This room is dusty, but looks comfortable.  It is not being used so the owners will not mind if you use it to rest and recover. Take a rest?", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        MessageBox("The bed is very comfortable and you get an excellent rest.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += 1000
            Party.HealAll(75)
            Party.RestoreSP(75)
        return

def MountBleak_785_MapTrigger_3_60(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(44,30)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_787_MapTrigger_2_18(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(59,22)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_789_MapTrigger_26_4(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["9_8"] = 0
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(20,39)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_792_MapTrigger_46_14(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(9,8)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_794_MapTrigger_26_11(p):
    if StuffDone["9_9"] < 1:
        result = ChoiceBox("Before you lies a massive cavern. The ceilings are really high, perfect for its inhabitants. Giants are everywhere ahead! As you intrude into their village, they grab their weapons and watch you carefully.\n\nThen, one giant steps forward. He is dressed in much more regal (but not very impressive) attire than the others. That must be the leader.\n\nHe shouts out in a booming voice that echoes through the entire cavern, \"Humans! I am Hav\'klar, leader of my peoples. We have no quarrel with your kind. Leave now and we shall not kill you.\"\n\nShould you try to proceed, you would be up against close to a hundred Giants. You doubt you can take them all.", eDialogPic.CREATURE1x2, 2, ["Flee", "Onward"])
        if result == 0:
            p.CancelAction = True
            return
        elif result == 1:
            MessageBox("You decide to spit at the giants mandate and proceed anyway. You could have handled a group of say eight or ten, but not ten times that many! It doesn\'t take long for you to die.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        return

def MountBleak_797_MapTrigger_26_36(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(6,15)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_800_MapTrigger_60_32(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,52)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_802_MapTrigger_44_24(p):
    if StuffDone["10_1"] == 0:
        StuffDone["10_1"] = 1
        Town.PlaceEncounterGroup(1)
        ChoiceBox("The cavern leads into a large alcove. The area is lit by a blazing fire. Several Giants are huddled around it, telling stories. You hide behind some rocks and listen in.\n\n\"Graa, I saw more of them humans again couple days back.\" The other replies, \"Them pesky maggots. Have to wonder what they want way up here. Always think them humans like it down below.\"\n\nThe other continues, \"I was chasin\' em, you see. Suddenly, they duck into this hidden small passage, have to squeeze to get through. They get to the end, I think I have \'em. But they used some kind of crystal on the wall!\n\nA hole appeared and they escaped!\" All the Giants yell out in fury. Suddenly, you hear a noise behind you. You turn to see a Hill Giant facing you, and he looks ready to kill you.", eDialogPic.CREATURE1x2, 0, ["OK"])
        return

def MountBleak_804_MapTrigger_18_60(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(18,28)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_806_MapTrigger_36_41(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("This lever controls the gates of the cell just to your west.")
        t = Town.TerrainAt(Location(34,42)).TransformTo
        Town.AlterTerrain(Location(34,42), 0, t)
        return

def MountBleak_807_MapTrigger_51_40(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 016_townentry)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,49)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_808_MapTrigger_43_60(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,57)
    Party.MoveToMap(TownMap.List["MountBleak_31"])

def MountBleak_810_MapTrigger_4_3(p):
    result = ChoiceBox("This portal will take you back to the bunker if you wish to go.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(42,53)
        Party.MoveToMap(TownMap.List["MountBleak_31"])
        return

def MountBleak_811_MapTrigger_8_5(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear the sound of metal rubbing against stone.")
        t = Town.TerrainAt(Location(4,6)).TransformTo
        Town.AlterTerrain(Location(4,6), 0, t)
        return

def MountBleak_812_MapTrigger_15_34(p):
    Party.Damage(Maths.Rand(4, 1, 5) + 10, eDamageType.FIRE)
    Wait()

def MountBleak_814_MapTrigger_18_35(p):
    if StuffDone["10_2"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The Giants may not be the brightest creatures in the world, but they were smart enough to put in traps to dissuade thieves. Care to take a stab at this one?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The Giants may not be the brightest creatures in the world, but they were smart enough to put in traps to dissuade thieves. Care to take a stab at this one?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["10_2"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(18,35))
    pc.RunTrap(eTrapType.BLADE, 2, 60)

def MountBleak_815_MapTrigger_20_35(p):
    if StuffDone["10_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The Giants may not be the brightest creatures in the world, but they were smart enough to put in traps to dissuade thieves. Care to take a stab at this one?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The Giants may not be the brightest creatures in the world, but they were smart enough to put in traps to dissuade thieves. Care to take a stab at this one?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["10_3"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(20,35))
    pc.RunTrap(eTrapType.BLADE, 2, 60)

def MountBleak_816_MapTrigger_58_2(p):
    if StuffDone["10_4"] == 250:
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
    StuffDone["10_4"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(58,2))
    pc.RunTrap(eTrapType.EXPLOSION, 1, 90)

def MountBleak_817_MapTrigger_51_8(p):
    if StuffDone["10_5"] == 250:
        return
    StuffDone["10_5"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(51,8))
    MessageBox("You burst into this house and see the grim figure of a Troglodyte Khazi. You immediately draw your weapons. But the Khazi speaks in a raspy voice, \"Put them away, I mean you no harm. Unless, you merit it that is.\"\n\nYou do as she requests. \"It has been long since humans have visited here on Mount Bleak. Have a look around if you like.\"")

def MountBleak_818_MapTrigger_34_59(p):
    if StuffDone["10_6"] == 250:
        return
    StuffDone["10_6"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(34,59))
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(35,59))
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(36,59))
    MessageBox("You gaze about this large room and see a horrifying site. On the tables, lie appendages and organs of what were once parts of human beings! These Giants have barbaric ritualistic practices.")

def MountBleak_821_MapTrigger_34_42(p):
    if StuffDone["10_7"] == 250:
        return
    StuffDone["10_7"] = 250
    TownMap.List["MountBleak_36"].DeactivateTrigger(Location(34,42))
    MessageBox("These were once soldiers of the army of Stolgrad. It looks like they were beaten severely and left to die. For some reason, the Giants have not harvested their equipment.")

def MountBleak_822_MapTrigger_51_52(p):
    for x in range(49, 55):
        for y in range(52, 54):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
    if StuffDone["10_8"] == 250:
        return
    StuffDone["10_8"] = 250
    ChoiceBox("Your recent adventures have shown you some pretty appalling things. Nothing yet matches this. In a room off to your right, you see a large creature. It looks like it was once a Giant, but something was done to it.\n\nIts skin looks like it has been warped and twisted into a thick armor-like hide. Its facial features are frozen in an expression of pain. The creature emits a high pitched pained howl. You feel an odd sympathy for these creatures.\n\nYou have read in history that Empire mages have done some pretty cruel things to other creatures to make them subjects, but those days are long over. Apparently,  Auspire\'s army has decided to revive those cruel practices.\n\nPerhaps its time you closed down shop.", eDialogPic.CREATURE1x2, 3, ["OK"])

def MountBleak_826_MapTrigger_35_19(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
        MessageBox("The Giant Shamans have amassed a collection of magical and non-magical writings. You have no idea exactly how they managed to assemble this collection, but it may be worth it to look through.\n\nMost of the books are fairly mundane. One book does talk about conjuring. It\'s only a beginners to intermediate book, so there isn\'t anything too complex. You manage to learn the spell \'Summon\'.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_summoning")
        return
    MessageBox("The Giant Shamans have amassed a collection of magical and non-magical writings. You have no idea exactly how they managed to assemble this collection, but it may be worth it to look through.\n\nMost of the books are fairly mundane. However, you find a book on conjuring. Most of the spells are either too easy or a bit beyond you. You will need more \'Mage Lore\' to access this knowledge.")

def Talking_36_13(p):
    if SpecialItem.PartyHas("TroglodyteMap"):
        p.TalkingText = "You already have that."
    else:
        if Party.Gold >= 10:
            Party.Gold -= 10
            SpecialItem.Give("TroglodyteMap")
            p.TalkingText = "She hands you a vellum scroll showing the map to the Troglodyte lair. \"Now why not create some trouble!\""
        else:
            p.TalkingText = ""
