
def WormCaves_105_MapTrigger_6_35(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(5,37)).Num == 9:
        if SpecialItem.PartyHas("HornCharm"):
            MessageBox("The unicorn charm suddenly starts humming and flashing! You remove it from around your neck and hold it out. It points at the cavern wall to the southwest.\n\nYou go examine the wall. It feels solid. After a bit of searching, however, you find a button, so well concealed that you never would have found it if it wasn\'t pointed out. You push it, and the wall shimmers.")
            Town.AlterTerrain(Location(5,37), 0, TerrainRecord.UnderlayList[10])
            Town.AlterTerrain(Location(5,38), 0, TerrainRecord.UnderlayList[10])
            return
        return

def WormCaves_106_MapTrigger_7_46(p):
    if StuffDone["4_0"] == 250:
        return
    result = ChoiceBox("The chest contains a large, velvet pad, spotted with dirt and filth. The horn of a unicorn rests on it. The giants haven\'t cleaned their grisly trophy very well, but the horn still glows slightly. The unicorn\'s magic still hasn\'t left it.\n\nThis is definitely what the unicorns wanted.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
    if result == 0:
        StuffDone["4_0"] = 250
        TownMap.List["WormCaves_4"].DeactivateTrigger(Location(7,46))
        SpecialItem.Give("UnicornHorn")
    return

def WormCaves_107_MapTrigger_3_46(p):
    if StuffDone["4_1"] == 250:
        return
    StuffDone["4_1"] = 250
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(3,46))
    MessageBox("You open the giant\'s chest. One of the clan\'s most valued treasures is inside. Unfortunately, it isn\'t an object but a thing. It\'s a specter, which the big, clumsy dopes managed to trap somehow. And you just set it free.")
    Town.PlaceEncounterGroup(1)

def WormCaves_108_MapTrigger_1_46(p):
    if StuffDone["4_2"] == 250:
        return
    StuffDone["4_2"] = 250
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(1,46))
    MessageBox("This suit of plate armor still has the blood of its previous owner on it.")

def WormCaves_110_MapTrigger_16_22(p):
    if StuffDone["4_3"] == 250:
        return
    StuffDone["4_3"] = 250
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(16,22))
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(16,23))
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(21,17))
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(22,17))
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(21,28))
    TownMap.List["WormCaves_4"].DeactivateTrigger(Location(22,28))
    ChoiceBox("The floor of this cavern is covered with a thick layer of gore. Shards of bone, dried (and not so dried) blood, and meat worm excretions have mixed to form large deposits of stuff you want to get nowhere near.\n\nThe ceiling of this cave has a shaft extending upward, down which the giants have no doubt thrown hundreds if not thousands of hapless creatures to be eaten by the worms.\n\nThese caverns must be the giant\'s combination meat locker and playground. They keep the worms alive to eat and to hunt for sport. It\'s a living.", eDialogPic.CREATURE2x1, 5, ["OK"])

def WormCaves_116_MapTrigger_11_3(p):
    if SpecialItem.PartyHas("HornCharm"):
        if StuffDone["4_4"] == 250:
            return
        StuffDone["4_4"] = 250
        MessageBox("You walk into the dank, musty tunnels under the clan\'s fortress. As you do, the unicorn charm begins to hum and glow again. You notice that it seems to want to point to the southwest.")
        return

def WormCaves_120_MapTrigger_2_10(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,6)
    Party.MoveToMap(TownMap.List["BloodGleeClan_3"])

def WormCaves_122_MapTrigger_40_31(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(57,36)
    Party.MoveToMap(TownMap.List["BloodGleeClan_3"])

def WormCaves_124_MapTrigger_46_9(p):
    if StuffDone["4_5"] == 250:
        return
    result = ChoiceBox("You find the massive, rather smelly corpse of a giant. It\'s been here for at least a few weeks. It looks like she was chewed up by giant worms pretty bad, and crawled here to die.\n\nHer club and armor are far too large to use. However, she was wearing a human sized shield on a chain around her neck. It would be usable after a serious cleaning.", eDialogPic.TERRAIN, 179, ["Take", "Leave"])
    if result == 0:
        StuffDone["4_5"] = 250
        TownMap.List["WormCaves_4"].AlterTerrain(Location(46,9), 1, None)
        TownMap.List["WormCaves_4"].DeactivateTrigger(Location(46,9))
        Party.GiveNewItem("CrystalShield_237")
    return
