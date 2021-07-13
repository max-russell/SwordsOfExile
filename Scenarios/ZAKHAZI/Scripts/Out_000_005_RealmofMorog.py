
def RealmofMorog_585_MapTrigger_43_17(p):
    if StuffDone["205_0"] == 250:
        return
    StuffDone["205_0"] = 250
    WorldMap.DeactivateTrigger(Location(43,257))
    WorldMap.DeactivateTrigger(Location(43,256))
    WorldMap.DeactivateTrigger(Location(43,255))
    WorldMap.DeactivateTrigger(Location(43,254))
    WorldMap.DeactivateTrigger(Location(44,254))
    ChoiceBox("The entrance to this narrow valley is marked by a long row of very grisly trophies. They\'re dead humans. Some wear the uniforms of the Exile armor. Some are dressed like travelers. All have been hanging here for some time.\n\nA sign under one of the bodies gives you an idea of who is responsible for this crime. It reads \"Death to all Exiles\", and has the family seal of Emperor Hawthorne.\n\nHawthorne was a foe of Exile before he was assassinated. That would mean that some of these totems were made decades ago. However, some of them are clearly much newer than that. Very odd.", eDialogPic.TERRAIN, 185, ["OK"])

def RealmofMorog_590_MapTrigger_44_39(p):
    result = ChoiceBox("The path to the south is steep. Very steep. It slopes downward at a 45 degree angle, and then grows even steeper. Sliding down it would be no problem. However, without climbing equipment, which you lack, getting back up would be a problem.\n\nAt the top of the slope, you find an abandoned campsite, and you can see another at the bottom. The campsite at the top is fresh ... someone lives near here. At least that tells you that there\'s probably a way to get out, should you climb down.", eDialogPic.STANDARD, 8, ["Leave", "Climb"])
    if result == 1:
        MessageBox("Sure enough, you manage to get to the bottom safely. Nothing is harmed, apart from the scratches in the seat of your armor from where you needed to slide down.")
        Party.Reposition(Location(44, 282))
        p.CancelAction = True
        return
    p.CancelAction = True

def RealmofMorog_591_MapTrigger_44_41(p):
    MessageBox("You try to climb back up the slope. However, without any sort of climbing equipment, there\'s no way you can make it back up the smooth, sheer path.")
    p.CancelAction = True

def RealmofMorog_592_MapTrigger_24_17(p):
    if StuffDone["205_1"] == 250:
        return
    StuffDone["205_1"] = 250
    WorldMap.DeactivateTrigger(Location(24,257))
    WorldMap.DeactivateTrigger(Location(25,257))
    MessageBox("You are at the south end of a steep path up to the top of a plateau. Whoever was at the top of the plateau would have a panoramic view of the whole cavern to the south. Of course, why anyone would walk to look at that mess is beyond you.")

def RealmofMorog_594_MapTrigger_5_35(p):
    StuffDone["205_2"] = 1

def RealmofMorog_595_MapTrigger_4_32(p):
    if StuffDone["205_2"] >= 1:
        if StuffDone["205_3"] == 250:
            return
        result = ChoiceBox("As you walk out of this tunnel, you notice that someone has etched into the side of a boulder the words \"Look up.\"\n\nYou look up, and see several red creatures floating about you. You look around, and see another boulder farther down, which reads \"Leave money.\" It would appear that, if you left some gold, they would leave you alone. Maybe.", eDialogPic.CREATURE, 85, ["Leave", "Pay", "Attack"])
        if result == 1:
            StuffDone["205_3"] = 250
            MessageBox("You put a pile of cash on the ground and back away. The creatures swoop down, pass over the treasure, rise back up, and fly away. You\'re a bit poorer, but still alive.")
            Party.Gold -= 500
            return
        elif result == 2:
            StuffDone["205_3"] = 250
            MessageBox("You refuse to submit to the creatures\' extortion. Angered by your defiance, they swoop down and attack you.")
            WorldMap.SpawnEncounter("Group_0_5_4", p.Target)
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You back away. Maybe there\'s another way out of this.")
        return

def RealmofMorog_596_MapTrigger_3_39(p):
    if StuffDone["205_4"] == 250:
        return
    result = ChoiceBox("On this small, remote ledge, you find a tunnel leading into the rock wall. It\'s very quiet, and there\'s no sign of anything walking in or out.", eDialogPic.TERRAIN, 241, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["205_4"] == 250:
            return
        result = ChoiceBox("You come across the lair of some sort of vicious, carnivorous creatures. Fortunately, the owners are currently absent. There\'s some gold around, and you see a nice helmet as well.", eDialogPic.TERRAIN, 241, ["Take", "Leave"])
        if result == 0:
            StuffDone["205_4"] = 250
            WorldMap.AlterTerrain(Location(3,279), 1, None)
            WorldMap.DeactivateTrigger(Location(3,279))
            Party.GiveNewItem("RunedHelm_221")
            Party.Gold += 700
            MessageBox("You quickly collect the treasure and leave the lair. You managed to get away without running into the owners.")
            return
        return
        return

def RealmofMorog_597_MapTrigger_6_3(p):
    if StuffDone["205_5"] == 250:
        return
    StuffDone["205_5"] = 250
    WorldMap.DeactivateTrigger(Location(6,243))
    WorldMap.DeactivateTrigger(Location(7,243))
    MessageBox("You finally leave the grim, undead filled cavern, with its rubble, bones, and stench. It\'s as if a constant, heavy weight has been lifted from your shoulders.")
