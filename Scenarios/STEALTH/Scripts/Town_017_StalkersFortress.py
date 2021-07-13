
def StalkersFortress_230_MapTrigger_62_61(p):
    if StuffDone["17_0"] == 250:
        return
    StuffDone["17_0"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(62,61))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(61,60))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(61,61))
    ChoiceBox("Time breaks up for you for a while. You aren\'t sure what happened. You entered the fort. Rebels surrounded you and beat you senseless. The last thing you remember is a man in leather armor standing over you, debating over whether to kill you or not.\n\nHe decided not to. You woke up in this cell, beaten and bruised. Several days have passed. The time was spent recuperating, eating the wormy (but edible) food they brought you, and listening to their taunts.\n\nYour cell is amazingly secure. There is not even a door, just a massive slab of rock with a narrow slit. Most strangely, you were left with your supplies, though they aren\'t doing you any good.\n\nAccording to your guards, your future involves intense torture, agonizing death, and delivery of your body parts to Selathni as a warning to all who would betray the Hill Runners. You sit and ponder this fate, and try (in vain) to devise an escape plan.\n\nEventually, you have recovered from your wounds. You haven\'t been tortured yet. Odd. You wonder what they\'re waiting for.", eDialogPic.CREATURE, 1024, ["OK"])
    Party.HealAll(200)
    for pc in Party.EachAlivePC():
        pc.SP+= 100
    Timer(Town, 10, False, "StalkersFortress_277_TownTimer_3", eTimerType.DELETE)

def StalkersFortress_233_MapTrigger_53_62(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear the grinding, sliding noise of one of the slabs of stone serving as cell doors.")
        t = Town.TerrainAt(Location(59,53))
        if t == TerrainRecord.UnderlayList[139]: Town.AlterTerrain(Location(59,53), 0, TerrainRecord.UnderlayList[170])
        elif t == TerrainRecord.UnderlayList[170]: Town.AlterTerrain(Location(59,53), 0, TerrainRecord.UnderlayList[139])
        return

def StalkersFortress_234_MapTrigger_54_62(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear the grinding, sliding noise of one of the slabs of stone serving as cell doors.")
        t = Town.TerrainAt(Location(59,57))
        if t == TerrainRecord.UnderlayList[139]: Town.AlterTerrain(Location(59,57), 0, TerrainRecord.UnderlayList[170])
        elif t == TerrainRecord.UnderlayList[170]: Town.AlterTerrain(Location(59,57), 0, TerrainRecord.UnderlayList[139])
        return

def StalkersFortress_235_MapTrigger_55_62(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever, and hear the grinding, sliding noise of one of the slabs of stone serving as cell doors.")
        t = Town.TerrainAt(Location(59,61))
        if t == TerrainRecord.UnderlayList[139]: Town.AlterTerrain(Location(59,61), 0, TerrainRecord.UnderlayList[170])
        elif t == TerrainRecord.UnderlayList[170]: Town.AlterTerrain(Location(59,61), 0, TerrainRecord.UnderlayList[139])
        return

def StalkersFortress_236_MapTrigger_57_51(p):
    if StuffDone["17_1"] == 250:
        return
    StuffDone["17_1"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(57,51))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(58,51))
    ChoiceBox("You reach the guardpost for this section of cells. Strangely, none of the guards are here. Looking closely, you see the seats have small specks of blood on them. You can take a guess what happened to the guards.", eDialogPic.TERRAIN, 141, ["OK"])

def StalkersFortress_238_MapTrigger_62_43(p):
    MessageBox("You peer over the edge of the pit. Normally prisoners would be kept in this pit to stew and listen to the screams of the tormented. Now, it has several bodies in it, freshly killed. Now you know where the guards and torturers went.")

def StalkersFortress_239_MapTrigger_50_57(p):
    if StuffDone["17_4"] == 250:
        return
    StuffDone["17_4"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(50,57))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(50,59))
    ChoiceBox("You reach the front door of the interrogation section, and peek out. A band of massive rebel soldiers are marching towards the door! You start to get ready for a big, ugly battle. Fortunately, they are distracted.\n\nThe whole complex is rocked by a powerful explosion. You hear screams, both of alarm and pain. One of the approaching rebels shouts \"They\'re attacking!\" and the band runs back down the corridor.\n\nFrom far away, you hear the sounds of combat. The Empire forces must be attacking the fortress. Unfortunately, considering the powerful defenses of these mountains, you doubt that Jaen managed to get many troops up here.\n\nThe attack at the entrance must be a diversion. This may well be the chance you need to escape or to slay Stalker. Whatever you do, you\'ll need to do it quickly. Once Stalker\'s men finish off the attackers, they\'ll come for you, and things will get ugly.\n\nYou\'d better hurry.\n\n(You have only a limited amount of time to finish this dungeon. You may want to save the game now.)", eDialogPic.CREATURE, 17, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Agent_35": Town.NPCList.Remove(npc)
    Timer(Town, 300, False, "StalkersFortress_278_TownTimer_16", eTimerType.DELETE)
    Timer(Town, 500, False, "StalkersFortress_279_TownTimer_18", eTimerType.DELETE)
    Timer(Town, 650, False, "StalkersFortress_280_TownTimer_20", eTimerType.DELETE)

def StalkersFortress_242_MapTrigger_45_53(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The Hill Runners were called away to help defend this fortress. Unfortunately, a large crowd of them are being held in reserve. You can see the auxiliaries hanging back to the north, waiting to attack.\n\nYou back away before they see you. You might be able to beat them in a fight. But you doubt it.")

def StalkersFortress_246_MapTrigger_42_57(p):
    if StuffDone["17_5"] == 250:
        return
    StuffDone["17_5"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(42,57))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(42,59))
    MessageBox("Unfortunately, not all of the Hill Runners reported for duty when the distracting attack started. Maybe they were ordered to hang back. Maybe they\'re cowards. Either way, they\'re very unhappy to see you.")

def StalkersFortress_248_MapTrigger_23_62(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(24,62)).Num == 170:
        MessageBox("Suddenly, a slab of stone drops out of the ceiling behind you! Looks like the Hill Runners have placed at least one trap near their payroll.")
        Town.AlterTerrain(Location(24,62), 0, TerrainRecord.UnderlayList[122])
        return

def StalkersFortress_250_MapTrigger_24_53(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(26,54)).Num == 122:
        MessageBox("Oh dear. Looks like you\'ve stumbled upon another Hill Runner trap. A small panel opens in a nearby wall. Flames pour out.")
        Town.AlterTerrain(Location(26,54), 0, TerrainRecord.UnderlayList[170])
        return

def StalkersFortress_251_MapTrigger_44_37(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You peer carefully out the doorway, hoping to see that the coast is clear. It isn\'t. You see at least a hundred burly, well armed Hill Runners standing around nearby in reserve, itching to be called to help defend their fortress.\n\nFortunately, they\'re all nervously looking in the direction of the front gates, waiting for orders. You\'re able to pull your head back unnoticed.")

def StalkersFortress_252_MapTrigger_38_37(p):
    if StuffDone["17_6"] == 250:
        return
    StuffDone["17_6"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(38,37))
    Animation_Hold(-1, 005_explosion)
    Wait()
    ChoiceBox("There is another explosion, very close by. It sounds like one of the Hill Runner\'s explosive boxes, but it\'s gone off in the room just ahead of you.\n\nTwo possibilities. Either the Hill Runners are trying to blow up their own complex, or you aren\'t the only saboteurs sneaking around in here.", eDialogPic.TERRAIN, 95, ["OK"])

def StalkersFortress_253_MapTrigger_40_34(p):
    if StuffDone["17_7"] == 250:
        return
    StuffDone["17_7"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(40,34))
    MessageBox("This room is still hot and smoking, and smoke hangs in the air. Charred rubble is strewn everywhere. You can see what the place was before it was trashed: a magical laboratory, and a good one too.\n\nSeveral of the rebel bombs must have just gone off. Whether they did it by themselves, or had help, you aren\'t sure.")

def StalkersFortress_263_MapTrigger_43_22(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(61,33))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def StalkersFortress_264_MapTrigger_61_34(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(42,22))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def StalkersFortress_265_MapTrigger_25_12(p):
    if StuffDone["17_8"] == 250:
        return
    StuffDone["17_8"] = 250
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(25,12))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(25,14))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(14,19))
    TownMap.List["StalkersFortress_17"].DeactivateTrigger(Location(12,19))
    ChoiceBox("The sounds of battle fading to the south, you rush through the doorway, hoping to find some way out of this death trap. Instead of an escape route, you find yourself face to face with Stalker.\n\nHe is sitting with his most valued lieutenants, planning the defense of the fortress. You see Canizares near him, and Luna as well. Guards are everywhere. They\'re all looking at you.\n\nStalker stands and laughs. For the first time, you get a good look at him. He\'s an average looking man. Simple. Nondescript. There\'s little about him that would make you think that this is the man who has held the Empire at bay for several years.\n\nTo his credit, he does not taunt you. He does not demand your surrender. He doesn\'t waste words. He simply stands, bows, and draws his blade. It is time for the final battle.", eDialogPic.CREATURE, 1024, ["OK"])
    Town.PlaceEncounterGroup(1)
    if SpecialItem.PartyHas("SmallOakBox"):
        result = ChoiceBox("As the Hill Runners stand and draw their blades, you realize that you still have one of their explosive devices, the box you found in the slime research facility. You could try using it. It could do great harm, maybe to them, maybe to you.\n\nDo you throw it?", eDialogPic.CREATURE, 1024, ["No", "Yes"])
        if result == 0:
            Town.PlaceEncounterGroup(2)
            return
        elif result == 1:
            ChoiceBox("You pull the rope, and fling the box. The timing on the device could not be better - it arcs through the air, and explodes on impact. Unfortunately, it was too heavy to throw far. It doesn\'t quite reach Stalker.\n\nInstead, it lands in front of Luna. The explosion flings her against the far wall like a rag doll, shattering her ribcage. She wasn\'t the only foe to be killed by the bomb, either. Not a great advantage, but it\'s a start.", eDialogPic.CREATURE, 20, ["OK"])
            return
        return
    Town.PlaceEncounterGroup(2)

def StalkersFortress_269_MapTrigger_11_2(p):
    MessageBox("The box is empty.")

def StalkersFortress_270_MapTrigger_18_2(p):
    MessageBox("You approach the altar, and feel very uncomfortable. You back away before it hurts you.")

def StalkersFortress_271_SanctifyTrigger_17_2(p):
    if p.Spell.ID != "p_sanctify":
        return
    MessageBox("Nothing happens. It\'s not powerfully enchanted enough to be affected by this spell.")

def StalkersFortress_272_MapTrigger_21_2(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 13:
        MessageBox("The rebels have liberated a huge prayer book from the Empire. You would love to spend several hours learning from it, but have to settle for a quick browse of one of the simpler prayers.\n\nIt\'s a simple prayer, but quite powerful. You can now cast Revive All.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_revive_all")
        return
    MessageBox("The rebels have liberated a huge prayer book from the Empire. You would love to spend several hours learning from it, but have to settle for a quick browse of one of the simpler prayers.\n\nAlas, your knowledge of magic is not enough to absorb anything from such a quick skim. Oh well.")

def StalkersFortress_273_MapTrigger_23_2(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 15:
        MessageBox("The rebels have liberated a huge prayer book from the Empire. You would love to spend several hours learning from it, but have to settle for a quick browse of one of the simpler prayers.\n\nFortunately, you are able to absorb one of the prayers, a brief incantation possessing  great power. You now know the spell Major Cleansing.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_major_cleansing")
        return
    MessageBox("The rebels have liberated a huge prayer book from the Empire. You would love to spend several hours learning from it, but have to settle for a quick browse of one of the simpler prayers.\n\nAlas, your knowledge of magic is not enough to absorb anything from such a quick skim. Oh well.")

def StalkersFortress_274_MapTrigger_9_2(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(8,1)).Num == 128:
        if SpecialItem.PartyHas("DockKey"):
            MessageBox("The door to the docks has been locked with a massive, complicated padlock. Fortunately, Stalker\'s key works on it. You open it as quickly as possible.")
            Town.AlterTerrain(Location(8,1), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("The door to the docks has been locked with a massive, complicated padlock. You try each of your keys as quickly as possible, trying desperately to get it open. None work. There\'s no way you\'ll be able to get the thing open in the time available.\n\nYou\'ll have to find the key to this door. You wonder who in this fortress would be important enough to have one ...")
        return

def StalkersFortress_276_MapTrigger_7_3(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,29)
    Party.MoveToMap(TownMap.List["ConcealedDocks_19"])

def StalkersFortress_277_TownTimer_3(p):
    MessageBox("As you pace the cell, wondering what to do, the stone slab locking you in slides away! You snap to attention, ready for a chance to fight your way out. However, there are no guards outside.\n\nInstead, you see a small, bearded man. He looks rather nervous, and is motioning for you to come out of the cell. Could this be a chance to escape? Or just a sinister Hill Runner trick?")
    Town.AlterTerrain(Location(59,61), 0, TerrainRecord.UnderlayList[170])

def StalkersFortress_278_TownTimer_16(p):
    MessageBox("The sounds of battle coming from the entrance to Stalker\'s fortress have changed. There\'s less clanking of weapons, and more screaming of the dying. One side is starting to lose. You may be running short on time.")

def StalkersFortress_279_TownTimer_18(p):
    MessageBox("The battle sounds like it\'s almost finished. You hear rebels shouting in triumph nearby. You have the feeling that your diversion is about to end. You\'d better hurry.")

def StalkersFortress_280_TownTimer_20(p):
    if StuffDone["17_3"] < 1:
        ChoiceBox("Time\'s up. The survivors of the battle at the front sweep through the fortress, looking for surviving Empire soldiers to butcher. When they find you, there is no question of imprisoning you again. They attack.\n\nFortunately, you are able to kill quite as few of them. Unfortunately, you don\'t quite kill enough. They eventually overwhelm you.", eDialogPic.CREATURE, 17, ["OK"])
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return
    MessageBox("You were able to kill Stalker, but you couldn\'t get away quite fast enough. The battle at the entrance ends, and Hill Runners sweep through the complex, looking for stragglers. They find you easily.\n\nYou could handle a few of them, but not hundreds. Their punishment for your slaying  their leader is far too horrifying to describe.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def StalkersFortress_281_CreatureDeath1(p):
    ChoiceBox("For a brief, horrible moment, Stalker seemed to actually be a threat to the Empire\'s rule. He had been the only person who had figured out how to hold its might at bay.\n\nNo longer. With a final, desperate blow, you strike him down. You may have had doubts about whether it was the right thing to do, but circumstances forced your hand. What\'s done is done. Stalker falls.\n\nHe lands on his back, life draining from him as you watch. Combat pauses, as all turn to see his final moments. Staring at the ceiling, he mutters one finally benediction to his rebels: \"Remember what I have taught you.\" Then he is gone.\n\nAround his neck, you see a small silver key hanging from a chain. You run and grab it. It may be your path out of here. You may have killed their leader, but there are still hundreds of Hill Runners nearby, and they won\'t appreciate what you\'ve done.\n\nTime to leave.", eDialogPic.CREATURE, 1024, ["OK"])
    StuffDone["17_3"] = 1
    for pc in Party.EachAlivePC():
        pc.AwardXP(100)
    SpecialItem.Give("DockKey")
