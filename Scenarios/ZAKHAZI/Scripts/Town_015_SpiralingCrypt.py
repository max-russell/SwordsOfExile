
def SpiralingCrypt_339_MapTrigger_5_5(p):
    MessageBox("You hear a soft, gentle voice. It sounds like someone is whispering into your ear, even though there\'s nobody there.\n\nThe voice says \"The four darks are to go up.\"")

def SpiralingCrypt_340_MapTrigger_25_5(p):
    MessageBox("You hear a soft, gentle voice. It sounds like someone is whispering into your ear, even though there\'s nobody there.\n\nThe voice says, \"The colors are the key to move on.\"")

def SpiralingCrypt_341_MapTrigger_25_25(p):
    MessageBox("You hear a soft, gentle voice. It sounds like someone is whispering into your ear, even though there\'s nobody there.\n\nThe voice says, \"The four light colors for the docks.\"")

def SpiralingCrypt_342_MapTrigger_5_25(p):
    MessageBox("You hear a soft, gentle voice. It sounds like someone is whispering into your ear, even though there\'s nobody there.\n\nIt says, \"First the colors, then the checking rune.\"")

def SpiralingCrypt_343_MapTrigger_23_19(p):
    if StuffDone["130_0"] >= 1:
        if StuffDone["130_1"] >= 1:
            if StuffDone["130_2"] >= 1:
                if StuffDone["130_3"] >= 1:
                    MessageBox("The rune glows when you step on it, and the  red, green, orange, and yellow sparkles following you begin to shake and swirl around you. A whispering voice says \"The way to the docks is now clear.\" Then the rune stops glowing, and motes calm down.")
                    StuffDone["15_0"] = 1
                    return
                if StuffDone["130_4"] >= 1:
                    if StuffDone["130_5"] >= 1:
                        if StuffDone["130_6"] >= 1:
                            if StuffDone["130_7"] >= 1:
                                MessageBox("The rune turns black when you step on it, and the dark motes surrounding you all turn dead black. A cold, hostile voice whispers in your ear \"Search the pillar by the slime, and you can come before me.\" Then the rune and motes return to \"normal\".")
                                return
                            MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                            return
                        MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                        return
                    MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                    return
                MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                return
            if StuffDone["130_4"] >= 1:
                if StuffDone["130_5"] >= 1:
                    if StuffDone["130_6"] >= 1:
                        if StuffDone["130_7"] >= 1:
                            MessageBox("The rune turns black when you step on it, and the dark motes surrounding you all turn dead black. A cold, hostile voice whispers in your ear \"Search the pillar by the slime, and you can come before me.\" Then the rune and motes return to \"normal\".")
                            return
                        MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                        return
                    MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                    return
                MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                return
            MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
            return
        if StuffDone["130_4"] >= 1:
            if StuffDone["130_5"] >= 1:
                if StuffDone["130_6"] >= 1:
                    if StuffDone["130_7"] >= 1:
                        MessageBox("The rune turns black when you step on it, and the dark motes surrounding you all turn dead black. A cold, hostile voice whispers in your ear \"Search the pillar by the slime, and you can come before me.\" Then the rune and motes return to \"normal\".")
                        return
                    MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                    return
                MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                return
            MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
            return
        MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
        return
    if StuffDone["130_4"] >= 1:
        if StuffDone["130_5"] >= 1:
            if StuffDone["130_6"] >= 1:
                if StuffDone["130_7"] >= 1:
                    MessageBox("The rune turns black when you step on it, and the dark motes surrounding you all turn dead black. A cold, hostile voice whispers in your ear \"Search the pillar by the slime, and you can come before me.\" Then the rune and motes return to \"normal\".")
                    return
                MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
                return
            MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
            return
        MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")
        return
    MessageBox("You step on the rune. The bright motes surrounding you flash and shake slightly and then return to normal. A voice whispers in your ear \"Your colors are not proper.\"")

def SpiralingCrypt_347_MapTrigger_15_23(p):
    StuffDone["130_0"] = 0
    StuffDone["130_1"] = 0
    StuffDone["130_2"] = 0
    StuffDone["130_3"] = 0
    StuffDone["130_4"] = 0
    StuffDone["130_5"] = 0
    StuffDone["130_6"] = 0
    StuffDone["130_7"] = 0
    StuffDone["130_8"] = 0
    StuffDone["130_9"] = 0
    MessageBox("When you step on the rune, bright white light pours out of it. The light seems to bleach the sparkling motes following you clean. The light disappears, and the motes shine with pure, untarnished white light.")

def SpiralingCrypt_351_MapTrigger_27_15(p):
    MessageBox("When you step on the rune, it begins to glow a dull, dark brown. The dark light changes several of the motes of light following you. Some of them remain brown. The rune turns dark again.")
    StuffDone["130_7"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_370_TownTimer_22", eTimerType.DELETE)

def SpiralingCrypt_352_MapTrigger_27_19(p):
    MessageBox("When you step on the rune, it begins to glow a dull, dark blue. The dark light changes several of the motes of light following you. Some of them remain blue. The rune turns dark again.")
    StuffDone["130_6"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_371_TownTimer_25", eTimerType.DELETE)

def SpiralingCrypt_353_MapTrigger_11_27(p):
    MessageBox("When you step on the rune, it begins to glow a dull, dark gray. The dark light changes several of the motes of light following you. Some of them remain gray. The rune turns dark again.")
    StuffDone["130_5"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_372_TownTimer_28", eTimerType.DELETE)

def SpiralingCrypt_354_MapTrigger_3_15(p):
    MessageBox("When you step on the rune, it begins to glow a dull, dark black. The dark light changes several of the motes of light following you. Some of them remain black. The rune turns dark again.")
    StuffDone["130_4"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_373_TownTimer_31", eTimerType.DELETE)

def SpiralingCrypt_355_MapTrigger_15_27(p):
    MessageBox("When you step on the rune, it begins to glow a bright, cheery red. The light changes several of the motes of light following you. Some of them remain red. The rune turns dark again.")
    StuffDone["130_0"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_374_TownTimer_34", eTimerType.DELETE)

def SpiralingCrypt_356_MapTrigger_3_11(p):
    MessageBox("When you step on the rune, it begins to glow a bright, cheery green. The light changes several of the motes of light following you. Some of them remain green. The rune turns dark again.")
    StuffDone["130_1"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_375_TownTimer_37", eTimerType.DELETE)

def SpiralingCrypt_357_MapTrigger_15_3(p):
    MessageBox("When you step on the rune, it begins to glow a bright, cheery orange. The light changes several of the motes of light following you. Some of them remain orange. The rune turns dark again.")
    StuffDone["130_2"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_376_TownTimer_40", eTimerType.DELETE)

def SpiralingCrypt_358_MapTrigger_19_3(p):
    MessageBox("When you step on the rune, it begins to glow a bright, cheery yellow. The light changes several of the motes of light following you. Some of them remain yellow. The rune turns dark again.")
    StuffDone["130_3"] = 1
    Timer(Town, 65, False, "SpiralingCrypt_377_TownTimer_43", eTimerType.DELETE)

def SpiralingCrypt_359_MapTrigger_19_23(p):
    if StuffDone["15_2"] == 250:
        return
    StuffDone["15_2"] = 250
    TownMap.List["SpiralingCrypt_15"].DeactivateTrigger(Location(19,23))
    MessageBox("The rune flashes when you step on it, and the white motes following you turn red and angry. Then they return to their previous state, and several creatures appear to attack you. Clearly, the tower still intends to harm you.")
    Town.PlaceEncounterGroup(1)

def SpiralingCrypt_360_MapTrigger_23_11(p):
    if StuffDone["15_3"] == 250:
        return
    StuffDone["15_3"] = 250
    TownMap.List["SpiralingCrypt_15"].DeactivateTrigger(Location(23,11))
    MessageBox("The rune flashes when you step on it, and the white motes following you turn red and angry. Then they return to their previous state, and several creatures appear to attack you. Clearly, the tower still intends to harm you.")
    Town.PlaceEncounterGroup(2)

def SpiralingCrypt_361_MapTrigger_11_7(p):
    if StuffDone["15_4"] == 250:
        return
    StuffDone["15_4"] = 250
    TownMap.List["SpiralingCrypt_15"].DeactivateTrigger(Location(11,7))
    MessageBox("The rune flashes when you step on it, and the white motes following you turn red and angry. Then they return to their previous state, and several creatures appear to attack you. Clearly, the tower still intends to harm you.")
    Town.PlaceEncounterGroup(3)

def SpiralingCrypt_362_MapTrigger_7_19(p):
    if StuffDone["15_5"] == 250:
        return
    StuffDone["15_5"] = 250
    TownMap.List["SpiralingCrypt_15"].DeactivateTrigger(Location(7,19))
    MessageBox("The rune flashes when you step on it, and the white motes following you turn red and angry. Then they return to their previous state, and several creatures appear to attack you. Clearly, the tower still intends to harm you.")
    Town.PlaceEncounterGroup(4)

def SpiralingCrypt_363_MapTrigger_2_20(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(4,26)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_14"])

def SpiralingCrypt_364_MapTrigger_10_2(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,7)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_14"])

def SpiralingCrypt_365_MapTrigger_28_10(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,7)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_14"])

def SpiralingCrypt_366_MapTrigger_20_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,27)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_14"])

def SpiralingCrypt_367_MapTrigger_13_15(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(12,21)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_16"])

def SpiralingCrypt_368_MapTrigger_20_10(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(25,6)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_16"])

def SpiralingCrypt_369_MapTrigger_10_20(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,25)
    Party.MoveToMap(TownMap.List["SpiralingCrypt_16"])

def SpiralingCrypt_370_TownTimer_22(p):
    if StuffDone["130_7"] >= 1:
        MessageBox("The brown motes turn white again.")
        StuffDone["130_7"] = 0
        return

def SpiralingCrypt_371_TownTimer_25(p):
    if StuffDone["130_6"] >= 1:
        MessageBox("The dark blue motes turn white again.")
        StuffDone["130_6"] = 0
        return

def SpiralingCrypt_372_TownTimer_28(p):
    if StuffDone["130_5"] >= 1:
        MessageBox("The gray motes turn white again.")
        StuffDone["130_5"] = 0
        return

def SpiralingCrypt_373_TownTimer_31(p):
    if StuffDone["130_4"] >= 1:
        MessageBox("The black motes turn white again.")
        StuffDone["130_4"] = 0
        return

def SpiralingCrypt_374_TownTimer_34(p):
    if StuffDone["130_0"] >= 1:
        MessageBox("The red motes turn white again.")
        StuffDone["130_0"] = 0
        return

def SpiralingCrypt_375_TownTimer_37(p):
    if StuffDone["130_1"] >= 1:
        MessageBox("The green motes turn white again.")
        StuffDone["130_1"] = 0
        return

def SpiralingCrypt_376_TownTimer_40(p):
    if StuffDone["130_2"] >= 1:
        MessageBox("The orange motes turn white again.")
        StuffDone["130_2"] = 0
        return

def SpiralingCrypt_377_TownTimer_43(p):
    if StuffDone["130_3"] >= 1:
        MessageBox("The yellow motes turn white again.")
        StuffDone["130_3"] = 0
        return

def SpiralingCrypt_378_OnEntry(p):
    if StuffDone["14_5"] >= 1:
        Town.AlterTerrain(Location(18,15), 0, TerrainRecord.UnderlayList[217])
        StuffDone["130_0"] = 1
        StuffDone["130_1"] = 1
        StuffDone["130_2"] = 1
        StuffDone["130_3"] = 1
        StuffDone["130_4"] = 1
        StuffDone["130_5"] = 1
        StuffDone["130_6"] = 1
        StuffDone["130_7"] = 1
        StuffDone["130_8"] = 1
        StuffDone["130_9"] = 1
        if StuffDone["15_1"] == 250:
            return
        StuffDone["15_1"] = 250
        MessageBox("You climb the stairs to the second level of this strange tower. When you reach the top, you notice two things. First, the architecture on this floor is noticeably Vahnatai.\n\nSecond, you see that the air around you is filled with brief, tiny flashes of light. The motes are too dim to see by but are constantly visible. All of them are white, and the effect is quite pretty.")
        return
    StuffDone["130_0"] = 1
    StuffDone["130_1"] = 1
    StuffDone["130_2"] = 1
    StuffDone["130_3"] = 1
    StuffDone["130_4"] = 1
    StuffDone["130_5"] = 1
    StuffDone["130_6"] = 1
    StuffDone["130_7"] = 1
    StuffDone["130_8"] = 1
    StuffDone["130_9"] = 1
    if StuffDone["15_1"] == 250:
        return
    StuffDone["15_1"] = 250
    MessageBox("You climb the stairs to the second level of this strange tower. When you reach the top, you notice two things. First, the architecture on this floor is noticeably Vahnatai.\n\nSecond, you see that the air around you is filled with brief, tiny flashes of light. The motes are too dim to see by but are constantly visible. All of them are white, and the effect is quite pretty.")
