
def LongStairs_268_MapTrigger_43_8(p):
    if StuffDone["17_0"] >= 1:
        return
    if StuffDone["12_0"] >= 1:
        if StuffDone["12_3"] >= 1:
            return
        result = ChoiceBox("A portion of the road has slid out at this point, leaving a six meter gap. It is too far to jump, so you can see no way of crossing. Looking down, you can see the ledge of the level below, about twenty meters down.\n\nDo you fasten your rope and send a member of your party down to investigate?", eDialogPic.CREATURE, 14, ["Leave", "Climb"])
        if result == 1:
            MessageBox("Your friends tie the rope around your waist, wish you luck, and you slide off the ledge. From below the path, you instantly notice the way the shelf sags. The mountain side is riddled with mole-like holes, breaking up the rock in several places.\n\nYou look into a hole as you descend, but see only darkness. Then, as you look down to prepare for your landing, there is a quick movement near the hole. Your rope has been cut off! Luckily, you are nearly down on the ledge, your drop is short.")
            pc = SelectPCBox("Getting back on your feet, you see nothing near the hole. Whatever was there has withdrawn. There is no way back up, so now you have only one option for joining your friends: Reaching the winch spot and connecting the line.",True)
            if pc == None:
                p.CancelAction = True
                return
            Party.Split(pc, Location(53,24))
            return
        return
    MessageBox("A portion of the road has slid out at this point, leaving a six meter gap. It is too far to jump, so you can see no way of crossing. Looking down, you can see the ledge of the level below, about twenty meters down.")

def LongStairs_269_MapTrigger_37_23(p):
    if StuffDone["12_1"] == 250:
        return
    StuffDone["12_1"] = 250
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(37,23))
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(37,22))
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(37,24))
    MessageBox("There is another mole hole ahead. As you approach, you think you hear a sharp whispering voice. Maybe your solitude and nerves are playing tricks on you. On the other hand ...")

def LongStairs_272_MapTrigger_32_21(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You try to force your way into the hole, but you can get only your head inside. You are too big.")

def LongStairs_275_MapTrigger_25_24(p):
    if StuffDone["12_2"] == 250:
        return
    StuffDone["12_2"] = 250
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(25,24))
    MessageBox("Rounding a corner, you glimpse something green, almost metallic, diving into a mole hole. Pebbles drop from overhead. You feel uncomfortable. Your heart is beating rapidly as you approach the ledge directly under Fort Outlook.")

def LongStairs_276_MapTrigger_12_26(p):
    if StuffDone["12_3"] >= 1:
        if StuffDone["12_4"] == 250:
            return
        StuffDone["12_4"] = 250
        TownMap.List["LongStairs_12"].DeactivateTrigger(Location(5,27))
        MessageBox("No more insects appear, and the winch line is descending. You catch the line and hammer the hook into the rock, securing the elevator. Your spectators cheer and lower a cage full of soldiers right away.\n\nThey congratulate you on your work, but you are grim. You are only a quarter part of the way down the Long Stairs, and from here you can all see the myriad of chitrach holes riddling the cliff. The winch is operable, you report as you are brought up.")
        Town.PlaceEncounterGroup(2)
        Timer(Town, 1, False, "LongStairs_285_TownTimer_25", eTimerType.DELETE)
        if Party.IsSplit:
            Party.Reunite()
        return
    MessageBox("You gasp in relief as you reach the winch site without encounter. The fort lies more than a hundred meters above you, and the heads that look down at you look very distant. You shout and wave your arms for them to drop the connecting line.\n\nThey shout and wave back. At first you take it for excitement. Then you hear their cries of warning. One of the hole diggers has finally chosen to reveal itself.")
    Town.PlaceEncounterGroup(1)

def LongStairs_277_MapTrigger_5_27(p):
    if StuffDone["12_4"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The road twists around and doubles back on itself at this point. You do not want to descend further without your party. Returning to the winch site and helping the soldiers lower the line is your best hope.")
        return

def LongStairs_278_MapTrigger_5_32(p):
    MessageBox("The long ramp is especially steep where it doubles back. Pebbles littering the road make your descent even more uncontrolled. Suddenly, a section of the ledge gives away under you, dumping you on the path several meters below, rocks raining around you.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(7,45))
    p.CancelAction = True
    Party.Damage(Maths.Rand(2, 1, 6) + -1, eDamageType.UNBLOCKABLE)
    Wait()

def LongStairs_280_MapTrigger_53_40(p):
    if StuffDone["12_5"] == 250:
        return
    StuffDone["12_5"] = 250
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(53,40))
    MessageBox("A pile of boulders has been hastily raised as defence against the chitrachs. Apparently to no avail. This small squad from Fort Outlook was overcome, even as they were raising a barricade to strengthen the mountain side.")

def LongStairs_281_MapTrigger_59_36(p):
    result = ChoiceBox("This passage is very narrow, but it is certainly the broadest hole you have seen the insects make so far. It descends further, and you think you can see daylight at the bottom. Perhaps this passage will take you to the ledge below.", eDialogPic.TERRAIN, 244, ["Leave", "Climb"])
    if result == 1:
        MessageBox("You emerge onto the ledge and find you have come a long way down the Long Stairs. The subterranean palms of the slith jungle are less than a hundred meters below you. However, the wall is riddled with holes, and you hear an incessant chirping.")
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(57,52))
        p.CancelAction = True
        return

def LongStairs_282_MapTrigger_38_55(p):
    if StuffDone["12_6"] == 250:
        return
    StuffDone["12_6"] = 250
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(38,55))
    TownMap.List["LongStairs_12"].DeactivateTrigger(Location(41,55))
    MessageBox("You have no other option, the ledge has been undermined and has fallen away. Blades drawn, you enter what appears to be the nest of the vermin. The smell is awful, but if this is what it takes to get away from this place, you are ready.")

def LongStairs_284_MapTrigger_10_59(p):
    Party.HealAll(40)
    for pc in Party.EachAlivePC():
        pc.SP+= 40
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(41,41)
    Party.MoveToMap(TownMap.List["YvosstaiCamp_15"])

def LongStairs_285_TownTimer_25(p):
    MessageBox("You return to the Fort. The captain hoists you all down in the winch cage and wishes you luck on your trip down the Long Stairs.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(12,26))
    p.CancelAction = True

def LongStairs_286_OnEntry(p):
    if not Town.Abandoned:
        ChoiceBox("At this point the Chimney ledge lies five hundred meters above the slith jungles. High up on the Wall, as the lizards see it. The chasm is almost vertical, straight down.\n\nThe only known point of connection is a long ramp zig-zaging down the half-kilometre drop. Sliths and humans built it together, chiselling out a narrow strip in the face of the mountain.\n\nThe work went on for many years, but the result is the lifeline of Chimney and the main route of trade with the slith nation.\n\nYou approach the top of the Long Stairs and Fort Outlook guarding it. Unconsciously, you shift your weight as far back as you can, afraid of the seemingly bottomless pit.", eDialogPic.TERRAIN, 1024, ["OK"])

def LongStairs_287_CreatureDeath14(p):
    MessageBox("The great Chitrach Queen tumbles to the ground. With her gone, the soldiers should be able to wipe out the rest. Your business, however, is elsewhere. The giant insects just had the poor fortune of being in your way.")
def Talking_12_0(p):
    Town.NPCList.Remove(p.NPCTarget)
    if p.NPCTarget.Start.LifeVariable != "":
        StuffDone[p.NPCTarget.Start.LifeVariable] = 1
    p.TalkingText = "\"Main camp iss some hours from Wall. We must go. Come down to ground with me!\" The slith turns and leads on down the final slope of the Long Stairs, beckoning you to follow."
