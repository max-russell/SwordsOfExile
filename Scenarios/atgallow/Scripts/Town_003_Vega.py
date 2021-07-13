
def Vega_18_MapTrigger_8_16(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(57,57)
    Party.MoveToMap(TownMap.List["BeneathVega_4"])

def Vega_19_MapTrigger_8_18(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(8,19)).Num == 128:
        MessageBox("Uh oh! It looks like someone locked your escape door also. You will just have to go forward and hope you can come out alive.")
        return

def Vega_20_MapTrigger_14_47(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(13,47)).Num == 128:
        if StuffDone["32_2"] == 1:
            t = Town.TerrainAt(Location(13,47))
            if t.InGroup("Unlockable"):
                t = Town.TerrainAt(Location(13,47)).TransformTo
                Town.AlterTerrain(Location(13,47), 0, t)
            if StuffDone["32_3"] == 250:
                return
            StuffDone["32_3"] = 250
            MessageBox("As instructed by the local innkeeper, you knock on the door and say \'spearhead\'. After a few seconds, you hear a lock click and the door is opened by a monk of the Followers looking surprised to see Empire soldiers.\n\nHe shouts, \"Quick comrades! We have been discovered by those imperialists. Draw your weapons. Let us make our god proud!\"")
            Town.PlaceEncounterGroup(1)
            return
        return

def Vega_21_MapTrigger_12_40(p):
    if StuffDone["32_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("It appears the Followers have trapped their loot. It does not look too complicated nor deadly.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("It appears the Followers have trapped their loot. It does not look too complicated nor deadly.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["32_4"] = 250
    TownMap.List["Vega_3"].DeactivateTrigger(Location(12,40))
    pc.RunTrap(eTrapType.BLADE, 0, 15)

def Vega_22_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 28),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 34),WorldMap.SectorAt(Party.OutsidePos))

def Vega_23_TalkingTrigger6(p):
    if StuffDone["0_5"] < 1:
        if Party.Gold >= 200:
            Party.Gold -= 200
            p.TalkingText = "You hand over the coins. Alda carefully counts them.\n\n\"All right, you\'ll need some instructions to get into our sanctuary.\""
            StuffDone["0_5"] = 1
            return
        return
    p.TalkingText = "\"All right, you\'ll need some instructions to get into our sanctuary.\""

def Vega_24_TalkingTrigger10(p):
    Sound.Play(009_lockpick)
    p.TalkingText = "He nods at the saying of the password. He unlocks a room on the other side of the building and returns. \"Aye comrades!\""
    Town.AlterTerrain(Location(8,19), 0, TerrainRecord.UnderlayList[125])

def Vega_25_TalkingTrigger45(p):
    if StuffDone["33_0"] >= 2:
        p.TalkingText = "\"Now that Emitar is no more, we see the Followers rapidly disintegrating. The original members who are trying to restore the order are failing. Soon, this madness will be over! All thanks to you, of course.\""
        return
    if StuffDone["33_0"] < 1:
        return
    p.TalkingText = "You return with news that you have slain Emitar. She smiles. \"That is excellent news! Now the Followers will be completely defunct. Let\'s see what I can do.\" She removes a sack of gold.\n\n\"Here\'s a bonus to supplement your standard pay. You deserve it!\""
    StuffDone["33_0"] = 2
    Party.Gold += 400

def Vega_26_TalkingTrigger50(p):
    if StuffDone["0_2"] >= 6:
        if StuffDone["33_0"] < 2:
            p.TalkingText = "\"Now that you have taken care of Zaine, several of his lieutenants have risen up. One is named Emitar who is a major threat to us. The Mayor mentioned to refer any adventurers or soldiers who inquired.\n\nI\'m mostly dealing with disposing of any other hostile Followers.\""
            return
        return
    if StuffDone["0_2"] < 4:
        p.TalkingText = "\"I\'m working in conjunction with your immediate commander, Bladesman Kelli. He has informed me that he has sent you to infiltrate some bunker. Unfortunately, we don\'t know where it is.\n\nHowever, I\'m sure if you ask around, somebody should know.\""
        return
    p.TalkingText = "\"So I hear that they have threatened to lay a curse on our crops. I personally think that\'s a lot of hot air, but one can never be sure. Right now, we\'re cleaning out that old fort. Imagine, we didn\'t even know about it!\n\nI wonder how they came to find out about those things.\""

def Talking_3_32(p):
    if Party.Gold < 20:
        p.TalkingText = ""
    else:
        Party.Gold -= 20
        Party.Pos = Location(22, 40)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "He collects your money and leads you to your room. \"Have a good night!\""
        CentreView(Party.Pos, False)

def Talking_3_33(p):
    if Party.Gold >= 4:
        Party.Gold -= 4
        p.TalkingText = "He serves up some drinks. They are cold and taste very good. \"Home grown barley, best in the world you know! Hey, want to know a little secret.\""
    else:
        p.TalkingText = ""
