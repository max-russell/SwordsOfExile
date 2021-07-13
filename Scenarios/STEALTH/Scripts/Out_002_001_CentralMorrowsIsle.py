
def CentralMorrowsIsle_419_MapTrigger_44_46(p):
    if StuffDone["210_1"] >= 1:
        if Game.Mode == eMode.OUTSIDE and WorldMap.TerrainAt(Location(140,93)).Num == 112:
            if Party.HasTrait(Trait.Woodsman):
                MessageBox("If it wasn\'t for your sharp Woodsman\'s senses, you never would have noticed it. There\'s a large path heading north into the woods, surprisingly well concealed considering its size.")
                WorldMap.AlterTerrain(Location(140,93), 0, TerrainRecord.UnderlayList[114])
                return
            return
        return

def CentralMorrowsIsle_420_MapTrigger_46_43(p):
    if StuffDone["206_0"] == 250:
        return
    StuffDone["206_0"] = 250
    WorldMap.DeactivateTrigger(Location(142,91))
    ChoiceBox("For creatures as large and lumbering as hill giants, this band has grown surprisingly adept at hiding its tracks. You\'re right on top of them before you realize you\'re at their camp.\n\nWhen you arrive, they lose no time attacking you. They don\'t want you getting back and sending a horde of Empire soldiers after them.", eDialogPic.CREATURE1x2, 0, ["OK"])
    WorldMap.SpawnEncounter("Group_2_1_4", p.Target)

def CentralMorrowsIsle_421_MapTrigger_17_28(p):
    if StuffDone["206_1"] == 250:
        return
    StuffDone["206_1"] = 250
    WorldMap.DeactivateTrigger(Location(113,76))
    MessageBox("The bridge is heavily worn, and has had two ruts worn into it by the passage of many sleds. To the east, you see a thick forest. Wide swaths of wood have been cut from it, and dragged to the south to build the cities there.\n\nThe guardpost by the bridge is empty, and nobody is traveling the roads. This area is the No Man\'s Land between the rebels to the northeast and the Empire cities to the south.")

def CentralMorrowsIsle_422_MapTrigger_25_28(p):
    if StuffDone["206_2"] == 250:
        return
    StuffDone["206_2"] = 250
    WorldMap.DeactivateTrigger(Location(121,76))
    WorldMap.DeactivateTrigger(Location(124,77))
    WorldMap.DeactivateTrigger(Location(126,81))
    WorldMap.DeactivateTrigger(Location(123,83))
    WorldMap.DeactivateTrigger(Location(121,82))
    WorldMap.DeactivateTrigger(Location(119,80))
    WorldMap.DeactivateTrigger(Location(119,79))
    ChoiceBox("You stand at the edge of the huge swath of cleared land the city of Fahl cleared out of this forest. You see stumps and trampled undergrowth for miles around, the trees cleared away to build the cities of Morrow\'s Isle.\n\nEven from here, you can see that all is not well in the city of Fahl. You see that two massive holes have been torn into its walls, and nobody is moving around the town.", eDialogPic.TERRAIN, 189, ["OK"])

def CentralMorrowsIsle_429_MapTrigger_31_45(p):
    if StuffDone["206_3"] == 250:
        return
    StuffDone["206_3"] = 250
    WorldMap.AlterTerrain(Location(127,93), 1, None)
    WorldMap.DeactivateTrigger(Location(127,93))
    MessageBox("With all their heads, hydras have the keenest sense of smell of any creature in these woods. Thus, these hydras knew you were coming from a mile away. They move to greet you ...")
    WorldMap.SpawnEncounter("Group_2_1_5", p.Target)

def CentralMorrowsIsle_430_MapTrigger_45_22(p):
    if StuffDone["204_3"] >= 1:
        MessageBox("You notice that one of the stones on the path is a slightly different color than the others. On a hunch, you turn it over, and find the words \"Stone 3\" carved on the underside. How odd.")
        StuffDone["206_4"] = 1
        return

def CentralMorrowsIsle_431_MapTrigger_29_19(p):
    if StuffDone["206_5"] == 250:
        return
    StuffDone["206_5"] = 250
    WorldMap.DeactivateTrigger(Location(125,67))
    WorldMap.DeactivateTrigger(Location(126,67))
    MessageBox("You climb up the steep road into the mountains, which, or so you\'ve heard, are filled with Hill Runners and other rebels. You certainly haven\'t seen any.\n\nHowever, as you climb farther up, you start to suspect you are being closely watched. It\'s not surprising - you doubt anyone moves into these mountains without being instantly spotted.")

def CentralMorrowsIsle_433_MapTrigger_31_17(p):
    if StuffDone["101_0"] < 1:
        result = ChoiceBox("You have definitely been watched as you climbed. A band of rebels show themselves well above you on the hills above the path. Many have bows and arrows, others crossbows. Some stand ready to roll rocks down onto you.\n\nOne of them shouts \"We don\'t know if you\'re friend or foe, but you aren\'t welcome here. Turn back, adventurers.\"", eDialogPic.CREATURE, 18, ["Leave", "Climb"])
        if result == 1:
            MessageBox("The rebels weren\'t joking. They let their arrows fly. After taking a fair amount of damage, you realize that the approach is futile, and turn back.")
            Party.Damage(Maths.Rand(9, 1, 9) + 1, eDamageType.WEAPON)
            Wait()
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("Rebuffed, you turn back. The rebels may have welcomed you here, but they don\'t trust you enough to let you near their stronghold.")
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Rebuffed, you turn back. The rebels may have welcomed you here, but they don\'t trust you enough to let you near their stronghold.")
        return

def CentralMorrowsIsle_435_MapTrigger_32_13(p):
    if StuffDone["206_6"] == 250:
        return
    StuffDone["206_6"] = 250
    WorldMap.AlterTerrain(Location(128,61), 1, None)
    WorldMap.DeactivateTrigger(Location(128,61))
    ChoiceBox("After an hour of searching, you finally find a gate through this huge wall. Both the wall and gate are well guarded by rebels with crossbows and halberds, and between the guards and the terrain, you can see why the Empire troops don\'t go up here.\n\nAt the gate, grim, scarred veterans let you through immediately, giving you only mild disapproving looks. You enter the lands of the Hill Runners for the first time.", eDialogPic.TERRAIN, 198, ["OK"])

def CentralMorrowsIsle_437_SpecialOnWin0(p):
    StuffDone["210_2"] = 1
    MessageBox("You defeated the giants! Unfortunately, now that their bodies lie before you, you see that they were a rather pitiful band, ill fed and clothed. You only find a few hundred gold worth of trinkets and small change in their camp.\n\nYou can\'t pity them too much, though. At least now they won\'t be raiding the much weaker farmers to the south.")
    Party.Gold += 250

def CentralMorrowsIsle_438_SpecialOnFlee0(p):
    MessageBox("You beat feet. As you run, you hear the giants run off in the other direction. Now that they\'ve been discovered, you can bet they\'ll be much, much better at hiding the next time.")

def CentralMorrowsIsle_439_SpecialOnWin1(p):
    MessageBox("After a bit of searching, you find the hydra\'s nest. There\'s a number of gold coins, rusted weapons, and a freshly killed deer. In addition, you find a strange blade. It\'s razor sharp, made of good metal, and curved in a strange wavy pattern.")
    Party.GiveNewItem("IronWaveBlade_93")
    Party.Gold += 300
    Party.Food += 50
