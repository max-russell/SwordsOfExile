
def SpiralingCrypt_387_MapTrigger_11_18(p):
    if StuffDone["16_4"] >= 1:
        if StuffDone["16_2"] == 250:
            return
        StuffDone["16_2"] = 250
        MessageBox("You\'ve spent a little bit too much time around this creature. He makes a last, futile effort to exert his will and keep from attacking you. He fails. His servants shamble forward, and they attack.")
        return
    if StuffDone["16_4"] == 250:
        return
    result = ChoiceBox("In the center of the highest level of the tower, you find a crypt. It\'s not a small, personal, private sepulcher or a grim charnel house. It\'s a brightly lit, airy chamber, decorated in the odd, chaotic style the Vahnatai prefer.\n\nA closer inspection, however, gives hints to the constant presence of madness. Everything is damaged, as if it\'s been repeatedly smashed and thrown around. The funeral bier is surrounded by crystals on pedestals. Each has been repeatedly cracked.\n\nYou aren\'t alone in the chamber. Dark, warped shapes move around in the shadows of the chamber, watching you. The being the crypt was built for lies on a bier in the corner. It\'s a small, withered, Vahnatai body, dressed in a simple shroud.\n\nAs you watch, the small, fragile being stands and faces you. It looks small and weak, but a strange, dark energy radiates from it. It says \"You have interrupted my solitude.\"\n\n\"My people have not given me my proper respect. My rage knows no limits. I tell you that you should leave now, or I shall not be able to resist destroying you.\" Do you leave?", eDialogPic.CREATURE, 74, ["Leave", "Approach"])
    if result == 1:
        StuffDone["16_4"] = 250
        TownMap.List["SpiralingCrypt_16"].DeactivateTrigger(Location(11,18))
        TownMap.List["SpiralingCrypt_16"].DeactivateTrigger(Location(10,18))
        if StuffDone["16_2"] == 250:
            return
        StuffDone["16_2"] = 250
        MessageBox("You\'ve spent a little bit too much time around this creature. He makes a last, futile effort to exert his will and keep from attacking you. He fails. His servants shamble forward, and they attack.")
        return
    p.CancelAction = True

def SpiralingCrypt_389_MapTrigger_12_10(p):
    if StuffDone["16_5"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("This cabinet is covered with protective runes. Strong ones. Considering the strength of the crypt\'s owner, you suspect this would be a very nasty trap to mess with.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("This cabinet is covered with protective runes. Strong ones. Considering the strength of the crypt\'s owner, you suspect this would be a very nasty trap to mess with.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["16_5"] = 250
    TownMap.List["SpiralingCrypt_16"].DeactivateTrigger(Location(12,10))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 80)

def SpiralingCrypt_390_MapTrigger_12_20(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(14,15)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_391_MapTrigger_5_26(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(10,19)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_392_MapTrigger_25_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(20,11)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_15"])

def SpiralingCrypt_393_MapTrigger_5_5(p):
    if StuffDone["16_0"] == 250:
        return
    StuffDone["16_0"] = 250
    TownMap.List["SpiralingCrypt_16"].DeactivateTrigger(Location(5,5))
    MessageBox("You open the box and see only one thing inside: a glyph painted on the bottom in gold paint. You try to close the box but aren\'t quite fast enough. The box explodes.")
    Party.Damage(Maths.Rand(7, 1, 12) + 5, eDamageType.FIRE)
    Wait()

def SpiralingCrypt_394_MapTrigger_25_26(p):
    if StuffDone["16_1"] == 250:
        return
    StuffDone["16_1"] = 250
    TownMap.List["SpiralingCrypt_16"].DeactivateTrigger(Location(25,26))
    MessageBox("You open the box and see only one thing inside: a glyph painted on the bottom in gold paint. You try to close the box but aren\'t quite fast enough. The box explodes.")
    Party.Damage(Maths.Rand(7, 1, 12) + 8, eDamageType.FIRE)
    Wait()

def SpiralingCrypt_395_CreatureDeath0(p):
    MessageBox("There was great power in the creature\'s small form. Yet, once again, your strength has proved the greater. As its life force departs. it casts a last, longing glance at the broken crystals nearby. Then it dies.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(10)
