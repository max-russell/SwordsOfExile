
def BelowWhitstone_365_MapTrigger_30_12(p):
    if SpecialItem.PartyHas("Minekey"):
        t = Town.TerrainAt(Location(30,13))
        if t.InGroup("Unlockable"):
            t = Town.TerrainAt(Location(30,13)).TransformTo
            Town.AlterTerrain(Location(30,13), 0, t)
        if StuffDone["16_0"] == 250:
            return
        StuffDone["16_0"] = 250
        MessageBox("You stand before the results of a life?s effort. A sealed tomb. Thinking of the broken old man in Myldres, you enter his key in the lock and turn it, dreading what lies within.")
        return

def BelowWhitstone_366_MapTrigger_27_20(p):
    if SpecialItem.PartyHas("Frayamulet"):
        MessageBox("As you approach this nondescript wall, one of you senses a throbbing on your chest. Reaching under your cloak, you find that Lady Fray?s amulet is glowing. You discover that the one wearing the amulet can pass through the wall, leading the others.")
        Town.AlterTerrain(Location(26,20), 0, TerrainRecord.UnderlayList[10])
        return

def BelowWhitstone_367_MapTrigger_17_25(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(51,37))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_368_MapTrigger_8_17(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(14,8))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_369_MapTrigger_55_35(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(14,8))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_370_MapTrigger_4_8(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(51,37))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_371_MapTrigger_22_9(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(32,36))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_372_MapTrigger_36_38(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(13,21))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_373_MapTrigger_26_37(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(52,49))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def BelowWhitstone_374_MapTrigger_41_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(15,44))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return
    if StuffDone["16_1"] == 250:
        return
    StuffDone["16_1"] = 250
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(14,44))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(14,45))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(16,45))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(16,44))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(14,43))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(16,43))
    MessageBox("This room has a very different feeling to it than the little, imp infested chambers you have been passing through. A huge throne decorated with skulls and tormented faces overlooks a grand hall. You are startled to hear a human voice calling your names.")

def BelowWhitstone_375_MapTrigger_9_45(p):
    if StuffDone["16_3"] >= 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
            Animation_Vanish(Party.LeaderPC, True, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(13,30))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("A demonic force flings you back from this gate, barring your entrance.")

def BelowWhitstone_376_MapTrigger_13_29(p):
    if Party.CountItemClass(1, False) > 0:
        if StuffDone["16_4"] >= 1:
            MessageBox("You return to a sinister scene. Rashtarra has returned, his portal is glowing fiercely again. And the demon lord is in no mood to play games of torment on Karolynna. She is hanging by her fingers from her little island, struggling not to fall. Your turn.")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
                Animation_Vanish(Party.LeaderPC, True, "010_teleport");
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                Wait()
                Party.Reposition(Location(9,51))
                p.CancelAction = True
                Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                return
            return
        MessageBox("You return just as the huge portal is recharging. Rashtarra has not yet stepped into your world. \"Well done!\" Karolynna cries, \"Bring the lamp into the gate!\" A demonic foot emerges from the portal.")
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
            Animation_Vanish(Party.LeaderPC, True, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(9,51))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            return
        return
    if StuffDone["215_0"] >= 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
            Animation_Vanish(Party.LeaderPC, True, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(9,51))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You haven?t found what you came here for yet!")

def BelowWhitstone_377_MapTrigger_15_48(p):
    MessageBox("This portal is different from the other portals you have just passed through. It is taller, for one thing, and looks almost majestic. Hot gases stream through it, apparently coming from a different atmosphere than yours.")

def BelowWhitstone_378_MapTrigger_15_50(p):
    if Party.CountItemClass(1, False) > 0:
        if StuffDone["16_5"] == 250:
            return
        StuffDone["16_5"] = 250
        MessageBox("The gaunt shape of the haakai emerges, his sharp teeth grinning at you in scorn. Until he sees the prison lamp. \"NO!\" he cries, \"THIS CANNOT BE! NOT AGAIN!\" You hear a swoosh, and the giant haakai is sucked into your little lamp.")
        ChoiceBox("\"Marvellous. Marvellous.\" Karolynna purrs. She is back on firm ground next to you, somehow. \"You have done a good day?s work today, friends!\"\n\nRashtarra himself was quite a threat to Chimney and Exile, she explains, but as a captive he will testify against another unscrupulous plotter. \"Do you want to know who his master is?\" she asks. Rhetorically, for she is already rubbing the lamp.\n\nMist gathers once again into Rashtarra, this time in his haakai shape. But timid, this time, humble in the way only a captive spirit can be.\n\n\"Tell us,\" Karolynna commands \"who was your master? Who let you out of the lamp and made you destroy Whitstone?\"", eDialogPic.CREATURE, 132, ["OK"])
        ChoiceBox("\"It was Groul. Commander Groul of the Cat Paws.\" The haakai bows meekly.\n\n\"He found my lamp as a young nephil, many years ago. He made me help him in gathering his mercenary tribe. When he entered human politics, I helped him. When his army attacked Flickering Keep, I led the battle in the shape of a Drake Lord.\n\n\"That was when I captured Lord Fray, as he fell towards his death off the cliff. In return for my last service, Groul allowed me to live in these catacombs. For that he made me destroy Whitstone, the one military power that could resist him.\"\n\nThe voice of the demon is plaintive, almost regretful now. Quite unlike what you have heard before he was captured.\n\n\"Groul is a ruthless warlord, bent on restoring his people and himself to power at any cost. He killed an entire human town in cold blood!\" Having said this, the demon returns into his prison.\n\n\"Keep this lamp for later. It might prove very important.\" Karolynna points to the western wall. \"There is a secret exit in the wall. But before you go, feel free to loot Rashtarra?s chamber. I will remain here for some time. Go on to Myldres!\"", eDialogPic.CREATURE1x2, 4, ["OK"])
        if Party.CountItemClass(1, True) > 0:
            if StuffDone["215_0"] == 250:
                return
            StuffDone["215_0"] = 250
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,30))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,31))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,32))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,33))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,34))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,35))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,36))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,30))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,31))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,32))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,33))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,34))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,35))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,36))
            TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(5,44))
            SpecialItem.Give("RashtarrasLamp")
            for pc in Party.EachAlivePC():
                pc.AwardXP(15)
            RunScript("GlobalCall_BelowWhitstone_601", ScriptParameters(eCallOrigin.CUSTOM))
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
                Animation_Vanish(Party.LeaderPC, True, "010_teleport");
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                Wait()
                Party.Reposition(Location(51,37))
                p.CancelAction = True
                Animation_Vanish(Party.LeaderPC, False, "010_teleport");
                for n in range(9):
                    Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                    Animation_Pause(50)
                return
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Entering this portal strikes even the more adventurous members of your party as an extraordinarily bad idea. You step back.")

def BelowWhitstone_379_MapTrigger_14_44(p):
    if StuffDone["16_1"] == 250:
        return
    StuffDone["16_1"] = 250
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(14,44))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(14,45))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(16,45))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(16,44))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(14,43))
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(16,43))
    MessageBox("This room has a very different feeling to it than the little, imp infested chambers you have been passing through. A huge throne decorated with skulls and tormented faces overlooks a grand hall. You are startled to hear a human voice calling your names.")

def BelowWhitstone_385_MapTrigger_10_51(p):
    if StuffDone["16_2"] == 250:
        return
    StuffDone["16_2"] = 250
    TownMap.List["BelowWhitstone_16"].AlterTerrain(Location(10,51), 1, None)
    TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,51))
    ChoiceBox("Following the familiar voice calling you, you stop at the edge of a bottomless pit covering a part of the throne room. Trapped on a small island floating in the void, you finally find your friend Karolynna.\n\nShe looks exhausted and  in poor shape after her long captivity, but you have yet to see her broken by anything. \"Thank you for coming. It appears you must rescue me once more!\" she smiles.\n\n\"The demon lord Rashtarra holds me captive. He enjoys playing with us, like in the dream you were exposed to in Flickering Keep. That may give us an opportunity to escape, even to turn my captivity to our advantage! But we must hurry.\n\n\"When Rashtarra comes to torment me, he always comes in the guise of our old acquaintance, Lord Fray. Try to stall him when he comes through the gate. He is not allowed to attack unless certain rules are broken, so try not to anger him.\n\n\"But talk! Distract him while I prepare my spell. Make him relax until I strike, put him off guard. Try to keep him close to the gate. I will try to disrupt the portal and wound him. He should be weakened enough for you to finish him off.\n\n\"After that, time is essential. You will be able to enter the northern gate, into his material prison, where you will find a lamp. Bring this back before he has time to bring in another incarnation, then I shall be able to capture him.\"", eDialogPic.CREATURE, 132, ["OK"])
    MessageBox("You feel the ground tremble, as the grand southern gate flashes into activity. Nodding briskly to Karolynna, you rehearse her instructions. The demon posing as Lord Fray is on his way.")
    Timer(Town, 3, False, "BelowWhitstone_405_TownTimer_19", eTimerType.DELETE)

def BelowWhitstone_386_MapTrigger_10_30(p):
    if StuffDone["215_0"] >= 1:
        return
    if StuffDone["16_4"] == 250:
        return
    StuffDone["16_4"] = 250
    MessageBox("The temptation is too great for greedy adventurers. Just one quick peek can?t take too long, you tell yourselves. You will soon regret that.")
    Town.PlaceEncounterGroup(1)

def BelowWhitstone_400_MapTrigger_59_7(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(6,23)
    Party.MoveToMap(TownMap.List["_RuinsofWhitstone_14"])

def BelowWhitstone_402_MapTrigger_5_44(p):
    if StuffDone["215_0"] >= 1:
        return
    p.CancelAction = True

def BelowWhitstone_403_MapTrigger_8_36(p):
    MessageBox("You find a magical treaty explaining in great detail how to cast the spell `Wall of Ice?. The author cannot understand why anyone would cast such a brutal spell, yet you think you can come up with a reason or two.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_wall_of_ice")

def BelowWhitstone_404_MapTrigger_9_30(p):
    MessageBox("The mages of the party insist that the others wait while they very slowly attain the skills necessary for casting `Summoning?, as described in this book.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_summoning")

def BelowWhitstone_405_TownTimer_19(p):
    Town.PlaceEncounterGroup(2)
    Animation_Hold(-1, 005_explosion)
    Wait()

def BelowWhitstone_406_TownTimer_21(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if not npc.IsABaddie: Town.NPCList.Remove(npc)
    MessageBox("\"Stand back!\" Karolynna cries. The portal flashes, expending all its energy in a moment. Rashtarra staggers as the electrical charge settles as a halo over his head. He leans heavily on his staff, and you seize his moment of weakness to attack.")
    Town.PlaceEncounterGroup(3)
    Animation_Explosion(Location(15,50), 2, "005_explosion")
    Animation_Hold()
    Wait()

def BelowWhitstone_407_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(33, 8),WorldMap.SectorAt(Party.OutsidePos))

def BelowWhitstone_408_CreatureDeath25(p):
    if StuffDone["16_5"] == 250:
        return
    StuffDone["16_5"] = 250
    MessageBox("You batter the demon lord with fierce blows, but they have little effect. He raises himself to full size, sharp teeth glittering. Then Karolynna strikes. \"NO!\" Rashtarra cries. But there is no help for him. He dissolves and is sucked into your lamp.")
    ChoiceBox("\"Marvellous. Marvellous.\" Karolynna purrs. She is back on firm ground next to you, somehow. \"You have done a good day?s work today, friends!\"\n\nRashtarra himself was quite a threat to Chimney and Exile, she explains, but as a captive he will testify against another unscrupulous plotter. \"Do you want to know who his master is?\" she asks. Rhetorically, for she is already rubbing the lamp.\n\nMist gathers once again into Rashtarra, this time in his haakai shape. But timid, this time, humble in the way only a captive spirit can be.\n\n\"Tell us,\" Karolynna commands \"who was your master? Who let you out of the lamp and made you destroy Whitstone?\"", eDialogPic.CREATURE, 132, ["OK"])
    ChoiceBox("\"It was Groul. Commander Groul of the Cat Paws.\" The haakai bows meekly.\n\n\"He found my lamp as a young nephil, many years ago. He made me help him in gathering his mercenary tribe. When he entered human politics, I helped him. When his army attacked Flickering Keep, I led the battle in the shape of a Drake Lord.\n\n\"That was when I captured Lord Fray, as he fell towards his death off the cliff. In return for my last service, Groul allowed me to live in these catacombs. For that he made me destroy Whitstone, the one military power that could resist him.\"\n\nThe voice of the demon is plaintive, almost regretful now. Quite unlike what you have heard before he was captured.\n\n\"Groul is a ruthless warlord, bent on restoring his people and himself to power at any cost. He killed an entire human town in cold blood!\" Having said this, the demon returns into his prison.\n\n\"Keep this lamp for later. It might prove very important.\" Karolynna points to the western wall. \"There is a secret exit in the wall. But before you go, feel free to loot Rashtarra?s chamber. I will remain here for some time. Go on to Myldres!\"", eDialogPic.CREATURE1x2, 4, ["OK"])
    if Party.CountItemClass(1, True) > 0:
        if StuffDone["215_0"] == 250:
            return
        StuffDone["215_0"] = 250
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,30))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,31))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,32))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,33))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,34))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,35))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(10,36))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,30))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,31))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,32))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,33))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,34))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,35))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(17,36))
        TownMap.List["BelowWhitstone_16"].DeactivateTrigger(Location(5,44))
        SpecialItem.Give("RashtarrasLamp")
        for pc in Party.EachAlivePC():
            pc.AwardXP(15)
        RunScript("GlobalCall_BelowWhitstone_601", ScriptParameters(eCallOrigin.CUSTOM))
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
            Animation_Vanish(Party.LeaderPC, True, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            Wait()
            Party.Reposition(Location(51,37))
            p.CancelAction = True
            Animation_Vanish(Party.LeaderPC, False, "010_teleport");
            for n in range(9):
                Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
                Animation_Pause(50)
            return
        return

def BelowWhitstone_409_TalkingTrigger3(p):
    Timer(Town, 3, False, "BelowWhitstone_406_TownTimer_21", eTimerType.DELETE)
def Talking_16_5(p):
    p.NPCTarget.Attitude = eAttitude.HOSTILE_A
    p.TalkingText = "The demon shouts with glee. \"Hah, you asked me a forbidden question! My master allows me to attack anyone who tries to discover his identity! Now you die.\" You hope Karolynna has her trap ready soon."
