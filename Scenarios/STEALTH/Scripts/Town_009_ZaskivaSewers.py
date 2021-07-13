
def ZaskivaSewers_110_MapTrigger_26_13(p):
    if StuffDone["9_0"] == 250:
        return
    StuffDone["9_0"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(26,13))
    MessageBox("This chest was once filled with suits of leather armor. The harsh atmosphere of the sewers has rotted them all away. Of course, being adventurers, you search through it all anyway, looking for loot.\n\nYour persistence is rewarded. You find a corroded old copper key. With typical Empire attention to detail, some sewer worker has scratched into its side the words \"Sewer Key One.\" You take it with you.")
    SpecialItem.Give("SewerKey1")

def ZaskivaSewers_111_MapTrigger_6_32(p):
    if StuffDone["9_3"] == 250:
        return
    StuffDone["9_3"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(6,32))
    MessageBox("You notice that the bridge over the swampy muck to the south has collapsed. You won\'t be able to get to the passage across the liquid to the southwest. Not on foot, anyway.")

def ZaskivaSewers_112_MapTrigger_2_20(p):
    if StuffDone["9_4"] == 250:
        return
    StuffDone["9_4"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(2,20))
    ChoiceBox("The rebels helped you escape from the aftermath of the destruction of Lord Volpe\'s fortress. Unfortunately, they\'ve dropped you in a situation that doesn\'t seem like much of an improvement. You\'ve been dumped into Zaskiva\'s sewer system.\n\nWhile Zaskiva is a relatively new city, neglect has left its sewer system in a condition which would be thought dreadful anywhere in the Empire. The walkways are crumbling, the ceiling looks likely to cave in, and the ventilation is awful.\n\nIt\'s the last thing that concerns you the most at the moment. Right now, being an adventurer stinks. Literally. The stench assaults your nose, and makes the inside of your mouth feel like it\'s been coated with melted rubber.\n\nAs if all this wasn\'t bad enough, you hear the growls and murmurs of monsters echoing through the passages. Good Heavens! Doesn\'t anyone come down here anymore?", eDialogPic.STANDARD, 4, ["OK"])

def ZaskivaSewers_113_MapTrigger_7_5(p):
    if StuffDone["9_5"] == 250:
        return
    StuffDone["9_5"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(7,5))
    MessageBox("To the west, you see a subterranean dock, with two seaworthy (or perhaps sewerworthy) rowboats docked at it. The dock itself is in terrible condition, crumbling and covered with huge spiderwebs.\n\nIt seems likely that, with all the pressure from the rebels, sewer maintenance simply has a low priority. Not good for you.")

def ZaskivaSewers_114_MapTrigger_28_13(p):
    MessageBox("This is a stairway up to Zaskiva. Unfortunately, it\'s been walled off. The sewer\'s probably been sealed in order to keep the monsters out of the city.")

def ZaskivaSewers_115_MapTrigger_1_37(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(1,38)).Num == 160:
        if SpecialItem.PartyHas("SewerKey1"):
            MessageBox("You are blocked off from the next section of the sewers by an enormous steel door. It\'s rusty, but still plenty strong. Fortunately, the key you found fits in the lock, and, with some effort, you manage to pry the door open.")
            Town.AlterTerrain(Location(1,38), 0, TerrainRecord.UnderlayList[157])
            return
        MessageBox("You are blocked off from the next section of the sewers by an enormous steel door. It\'s rusty, but still plenty strong. It has a large keyhole. None of your keys fit in it.")
        return

def ZaskivaSewers_116_MapTrigger_1_40(p):
    if StuffDone["9_6"] == 250:
        return
    StuffDone["9_6"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(1,40))
    ChoiceBox("Looking ahead, you see that this section of sewer has been overgrown by large, brightly colored fungi. They look harmless.", eDialogPic.CREATURE, 69, ["OK"])

def ZaskivaSewers_117_MapTrigger_21_48(p):
    if StuffDone["9_7"] == 250:
        return
    StuffDone["9_7"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(21,48))
    MessageBox("This trench is currently empty. It\'s still cut pretty deep, and the sides are slick, so climbing inside isn\'t an option. As if you\'d want to.")

def ZaskivaSewers_118_MapTrigger_22_54(p):
    if StuffDone["9_8"] == 250:
        return
    StuffDone["9_8"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(22,54))
    MessageBox("You\'ve reached the south end of the empty trench. You notice that there\'s a huge effluent pipe positioned in the ceiling above the trench. Nothing is pouring out of it right now.")

def ZaskivaSewers_119_MapTrigger_39_11(p):
    if StuffDone["9_9"] == 250:
        return
    StuffDone["9_9"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(39,11))
    MessageBox("The empty trench is blocked off by a crude brick wall. The wall is strong enough to defend itself against your efforts, but fragile enough that if something did pour down the trench, it would fall apart.")

def ZaskivaSewers_120_MapTrigger_28_35(p):
    if StuffDone["111_0"] == 250:
        return
    StuffDone["111_0"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(28,35))
    ChoiceBox("Oh, no! As if this place wasn\'t gross and unpleasant enough, it has an infestation of cockroaches as well. Even worse, they\'re huge! One of the roaches in the cave to the south must be as large as a pony.\n\nYou\'re heard rumors that some places in Valorim have infestations of giant cockroaches. You\'re horrified to find those rumors are true.", eDialogPic.CREATURE, 110, ["OK"])

def ZaskivaSewers_121_MapTrigger_45_12(p):
    if StuffDone["111_1"] == 250:
        return
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["111_1"] == 250:
            return
        StuffDone["111_1"] = 250
        TownMap.List["ZaskivaSewers_9"].AlterTerrain(Location(45,12), 1, None)
        TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(45,12))
        MessageBox("You press the button. It makes a clicking noise, and stays stuck in the wall. A fine, clear spray shoots out of holes in the wall, coating you. It smells nice, and makes you feel much better.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 8))
        Party.HealAll(40)
        return

def ZaskivaSewers_122_MapTrigger_36_1(p):
    if StuffDone["111_2"] == 250:
        return
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["111_2"] == 250:
            return
        StuffDone["111_2"] = 250
        TownMap.List["ZaskivaSewers_9"].AlterTerrain(Location(36,1), 1, None)
        TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(36,1))
        MessageBox("You press the button. It makes a clicking noise, and stays stuck in the wall. A fine, clear spray shoots out of holes in the wall, coating you. It smells nice, and makes you feel much better.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 8))
        Party.HealAll(40)
        return

def ZaskivaSewers_123_MapTrigger_17_29(p):
    if StuffDone["111_3"] == 250:
        return
    StuffDone["111_3"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(17,29))
    MessageBox("This doesn\'t look like Empire construction. Too rough. Looks like some sort of hideout. Your guess is that a bunch of bandits, rebels, or other never-do-wells were hiding here.\n\nUnfortunately, it looks like they came to a bad end. Perhaps they became trapped when the sewers were sealed off. There was certainly some ugly violence taking place here.")

def ZaskivaSewers_124_MapTrigger_26_18(p):
    if StuffDone["111_5"] == 250:
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
    StuffDone["111_5"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(26,18))
    pc.RunTrap(eTrapType.DART, 2, 40)

def ZaskivaSewers_125_MapTrigger_27_20(p):
    if StuffDone["111_6"] == 250:
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
    StuffDone["111_6"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(27,20))
    pc.RunTrap(eTrapType.EXPLOSION, 1, 40)

def ZaskivaSewers_126_MapTrigger_60_28(p):
    if StuffDone["9_1"] == 250:
        return
    StuffDone["9_1"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(60,28))
    MessageBox("Whoever this poor soul was, he died trying to claw his way through this heavy door. He was down here without any sort of protective gear. He does, however, have a copper key in his pocket, labeled \"Sewer Key 2\".")
    SpecialItem.Give("SewerKey2")

def ZaskivaSewers_127_MapTrigger_58_32(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(58,33)).Num == 160:
        if SpecialItem.PartyHas("SewerKey3"):
            MessageBox("You find another massive steel door. Fortunately, \"Sewer Key 3\" fits in the keyhole just fine. After a lot of pulling and prying, the rusty door swings open.")
            Town.AlterTerrain(Location(58,33), 0, TerrainRecord.UnderlayList[157])
            return
        MessageBox("You find another massive steel door. Unfortunately, you don\'t yet have the key to this one.")
        return

def ZaskivaSewers_128_MapTrigger_30_57(p):
    if StuffDone["111_7"] == 250:
        return
    StuffDone["111_7"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(30,57))
    MessageBox("This passage slopes sharps up to the west, to a sort of observation platform.")

def ZaskivaSewers_129_MapTrigger_27_57(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(26,56)).Num == 128:
        if SpecialItem.PartyHas("SewerKey2"):
            MessageBox("This small door glows slightly. It\'s probably magically locked. Fortunately, \"Sewer Key 2\" fits perfectly.")
            Town.AlterTerrain(Location(26,56), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("This small door glows slightly. It\'s probably magically locked. It has a keyhole, but, unfortunately, none of your keys fit.")
        return

def ZaskivaSewers_130_MapTrigger_29_52(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["111_8"] >= 1:
            MessageBox("You pull the lever, and the swamps machinery whirls into brief, intense, and highly irrelevant motion. Nothing interesting happens, and soon it\'s quiet again.")
            return
        ChoiceBox("You pull the lever, and long dormant sewer machinery leaps into action! This lever controls the effluent pipe just outside the control room.\n\nWith a loud, squeal, the cap of the pipe swings open, and thousands of gallons of sticky, foul smelling goo pour out of the pipe and into the empty trench below. From there, with a deafening roar, it rushes down the passage to the north.\n\nSoon, the flow turns from a load roar to a gentle, steady trickle. It seems safe to leave the control room. You can\'t help but wonder what effect all that goop had on the landscape.", eDialogPic.TERRAIN, 217, ["OK"])
        for x in range(23, 25):
            for y in range(33, 59):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
        for x in range(24, 42):
            for y in range(33, 35):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
        for x in range(40, 42):
            for y in range(8, 35):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
        for x in range(42, 43):
            for y in range(12, 14):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
        for x in range(34, 36):
            for y in range(35, 36):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
        Town.AlterTerrain(Location(44,8), 0, TerrainRecord.UnderlayList[84])
        if StuffDone["9_9"] == 250:
            return
        StuffDone["9_9"] = 250
        TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(39,11))
        return

def ZaskivaSewers_131_MapTrigger_52_9(p):
    if StuffDone["111_9"] == 250:
        return
    StuffDone["111_9"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(52,9))
    MessageBox("With typical bureaucratic senselessness, some genius had the idea of putting the administration and planning rooms for the sewers actually in the sewers. Of course, like everything else down here, it\'s been abandoned.\n\nHeaven help anyone who tries to take charge of getting this place under control, if all the plans are stuck down here.")

def ZaskivaSewers_132_MapTrigger_55_1(p):
    MessageBox("Once, the plans and maps for the sewers were on this wall. Unfortunately, the swamp folk have tried to take them down and read them, and the papers crumbled under their acidic touch.")

def ZaskivaSewers_133_MapTrigger_61_5(p):
    if StuffDone["112_0"] == 250:
        return
    StuffDone["112_0"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(61,5))
    MessageBox("On the bright side, the records in this room are intact. On the down side, that means you now have access to hundreds of journals describing in minute detail sewage routes, quantities, and textures. Useless to you.")

def ZaskivaSewers_134_MapTrigger_62_8(p):
    if StuffDone["9_2"] == 250:
        return
    StuffDone["9_2"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(62,8))
    MessageBox("This desk, like the others, is empty, cleaned out by the swamp folk. You do have the fortune to find something under the desk, though: a tarnished copper key. Writing on the side reads \"Sewer Key 3.\"")
    SpecialItem.Give("SewerKey3")

def ZaskivaSewers_135_MapTrigger_53_62(p):
    if StuffDone["112_1"] == 250:
        return
    StuffDone["112_1"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(53,62))
    MessageBox("Suddenly, ahead of you, a thin, insubstantial creature appears. It\'s a ghost! It starts waving its hands. At first, you think it\'s going to attack or cast a spell, but then you realize its trying to get you to approach it.")
    Town.PlaceEncounterGroup(1)

def ZaskivaSewers_136_MapTrigger_41_56(p):
    if StuffDone["112_2"] == 250:
        return
    StuffDone["112_2"] = 250
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(41,56))
    TownMap.List["ZaskivaSewers_9"].DeactivateTrigger(Location(42,56))
    MessageBox("How odd. Someone has placed a lot of lifelike statues down here. Very lifelike statues.")

def ZaskivaSewers_138_MapTrigger_36_62(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("At last! You have finally reached a functioning stairway out of these hellish sewers.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(3,29)
    Party.MoveToMap(TownMap.List["AbandonedOutpost_10"])

def ZaskivaSewers_139_TownTimer_0(p):
    MessageBox("The sewer is finally starting to get to you. The fumes start to make you feel incredibly nauseated.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 1))

def ZaskivaSewers_140_TalkingTrigger0(p):
    if StuffDone["111_4"] >= 1:
        p.TalkingText = "\"The specter! You killed it! I am avenged. I am free. Thanks to you. I will help you pass.\" It waves a spectral hand, and there is a flash of light to the north.\n\n\"It is done. Goodbye.\" The ghost fades away, smiling at the thought of its final rest."
        for x in range(60, 62):
            for y in range(55, 56):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[73])
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Ghost_61": Town.NPCList.Remove(npc)
        return
