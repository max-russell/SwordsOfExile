
def VahnataiCaverns_315_MapTrigger_21_39(p):
    if StuffDone["15_0"] == 250:
        return
    result = ChoiceBox("You see that someone has etched several glyphs in the cave floor just ahead. There\'s no dust or moss on them, and they\'re still pretty clean. If you didn\'t know better, you\'d think they were etched here very recently.\n\nThey look magical, and maybe a little dangerous.", eDialogPic.TERRAIN, 170, ["Leave", "Approach"])
    if result == 1:
        StuffDone["15_0"] = 250
        TownMap.List["VahnataiCaverns_15"].AlterTerrain(Location(21,39), 1, None)
        TownMap.List["VahnataiCaverns_15"].DeactivateTrigger(Location(21,39))
        MessageBox("When you try to walk over the runes, there\'s a small explosion. You\'re lightly toasted. Fortunately, it was more a trap to keep away pests than something deadly serious.")
        Party.Damage(Maths.Rand(2, 1, 6) + 2, eDamageType.FIRE)
        Wait()
        return
    p.CancelAction = True

def VahnataiCaverns_316_MapTrigger_25_22(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You follow this passage for an hour, and it winds farther and farther down into the ground. After a while it splits, and then splits again.\n\nYou try to mark your path, but you soon realize that there\'s nothing down here of interest. You carefully make your way back.")

def VahnataiCaverns_317_MapTrigger_4_39(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The tunnel leads back up into the School of Magery.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(42,34)
    Party.MoveToMap(TownMap.List["Libraries_13"])

def VahnataiCaverns_319_MapTrigger_30_36(p):
    if StuffDone["15_2"] == 250:
        return
    StuffDone["15_2"] = 250
    TownMap.List["VahnataiCaverns_15"].DeactivateTrigger(Location(30,36))
    ChoiceBox("When you see the bizarre creature staring at you at the other end of the cavern, you reflexively draw your weapons. Your experience has taught you that something this alien is sure to immediately attack you.\n\nAs you bare your blades, it does nothing. It simply sits and watches. You get a chance to look it over. It\'s about seven feet tall and humanoid. Its limbs are long, incredibly thin, triple jointed, and covered with tight, dry, gray skin.\n\nIts head is large and round, and its bug eyes glow slightly. Its sole garment also glows. It\'s a sheer, translucent poncho, brightly colored. It\'s a very strange creature, highly alien in appearance.\n\nAs you gawk at it, you realize it is sizing you up in a similar way. A minute passes in silence. Then it raises a spindly arm, and waves for you to approach.", eDialogPic.CREATURE, 61, ["OK"])

def VahnataiCaverns_320_TalkingTrigger27(p):
    if StuffDone["15_3"] == 0:
        if StuffDone["15_3"] == 250:
            return
        StuffDone["15_3"] = 250
        p.TalkingText = "She looks over to Baia-Tel, who nods. She then reaches under her sleeping pad, removes a long, slender crystal, and hands it to you. \"Careful,\" she says. \"it\'s hot.\" She\'s right. It\'s hot enough to burn flesh.\n\n\"We found this nearby. It is part of the controls of the School. We know not what it is used for. Perhaps you can find out.\""
        SpecialItem.Give("CrystalofPower")
        return
