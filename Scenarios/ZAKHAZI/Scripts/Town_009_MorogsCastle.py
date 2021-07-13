
def MorogsCastle_185_MapTrigger_52_36(p):
    result = ChoiceBox("At first, this looks like a completely ordinary chair. Then you look closer, and see that it is covered with a network of tiny runes, etched all over its surface. It also has straps, designed to hold a reluctant person down.\n\nFinally, you find traces of blood. Someone didn\'t wipe the chair down as well at they could have.", eDialogPic.TERRAIN, 140, ["Leave", "Sit"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        MessageBox("When you sit in the transmuting chair, the runes that cover every inch of its surface begin to glow. The powerful magic of the chair begins to transmute you into a sheep. Unfortunately, there are still a few bugs in the system.\n\nYou are spared a humiliating life as a sheep. The chair only hunches you over a bit, and makes tufts of wool spring on on your skin. The shock of the change also, incidentally, kills you.")
        pc.Kill(None, eLifeStatus.DUST, True)
        Wait()
        return

def MorogsCastle_186_MapTrigger_56_16(p):
    if StuffDone["8_1"] == 250:
        return
    StuffDone["8_1"] = 250
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(56,16))
    MessageBox("Suddenly, huge, red creatures appear all around you!")
    Town.PlaceEncounterGroup(1)

def MorogsCastle_187_MapTrigger_50_9(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Bolts of lightning arc across the passage in front of you! You jump back before you get baked.")

def MorogsCastle_188_MapTrigger_49_20(p):
    Town.AlterTerrain(Location(48,19), 0, TerrainRecord.UnderlayList[139])
    Town.AlterTerrain(Location(51,22), 0, TerrainRecord.UnderlayList[140])

def MorogsCastle_189_MapTrigger_47_14(p):
    if StuffDone["8_2"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(47,18))
        p.CancelAction = True
        return

def MorogsCastle_190_MapTrigger_58_25(p):
    Message("Click.")
    StuffDone["8_2"] = 1

def MorogsCastle_191_MapTrigger_51_20(p):
    Town.AlterTerrain(Location(52,24), 0, TerrainRecord.UnderlayList[148])

def MorogsCastle_192_MapTrigger_52_23(p):
    Town.AlterTerrain(Location(52,24), 0, TerrainRecord.UnderlayList[147])

def MorogsCastle_193_MapTrigger_48_28(p):
    if StuffDone["8_3"] >= 1:
        MessageBox("What a disappointment. You\'ve come all this way, only to finally reach an empty case.")
        return
    if StuffDone["8_4"] == 250:
        return
    result = ChoiceBox("The case only contains one item. It\'s an ancient scroll, over ten long. It is covered with faint, fine writing, painted on thin leather. Rolled up, it\'s almost six inches in diameter.\n\nYou unroll it slightly to look at it. It\'s not magical. It\'s more a work of history. It contains many small portraits of dragons, with pieces of biographical information.\n\nIt doesn\'t look too interesting to you. Someone, however, might find it very valuable. The key question is how much the lich Morog will mind your stealing it from her.", eDialogPic.TERRAIN, 169, ["Take", "Leave"])
    if result == 0:
        StuffDone["8_4"] = 250
        SpecialItem.Give("ScrollofDragons")
        MessageBox("When you take the scroll, you hear a distant rumbling. The ground vibrates slightly under your feet. Someone isn\'t reacting well to your theft.")
        StuffDone["8_0"] = 1
        Town.MakeTownHostile()
        return
    return

def MorogsCastle_194_MapTrigger_41_9(p):
    if StuffDone["8_6"] == 250:
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
    StuffDone["8_6"] = 250
    TownMap.List["WurmPit_8"].DeactivateTrigger(Location(10,11))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(41,9))
    pc.RunTrap(eTrapType.ALERT, 0, 60)

def MorogsCastle_195_MapTrigger_37_14(p):
    result = ChoiceBox("The pedestal bears a massive spell book. It\'s a monster - over eight inches thick, with a cover of dragon skin and spells painted on the pages with gold paint. It\'s an incredible piece of work.\n\nThis spell book must be Morog\'s. Only a creature as powerful and magical as a lich could own a magical tome this formidable.", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("Bolts of lightning arc across the passage in front of you! You jump back before you get baked.")
            return
        MessageBox("The moment you touch the book, icy numbness races up your arm, spreads across your torso, and flows down your legs. You try to pull yourself away, only to find your hand stuck to the page!\n\nFinally, with a last desperate bit of strength, you manage to throw yourself away from the book. You collapse to the ground, your skin frigid from head to toe.")
        pc.SetSkill(eSkill.INTELLIGENCE, pc.GetSkill(eSkill.INTELLIGENCE) - 3)
        return

def MorogsCastle_196_MapTrigger_36_6(p):
    MessageBox("You find a slender tome with a very simple alchemical recipe inside. You now know how to make Resurrection Balm.")
    Party.LearnRecipe("resurrection_balm")

def MorogsCastle_197_MapTrigger_36_5(p):
    MessageBox("This concealed bookshelf contains Morog\'s more esoteric and obscure magical tomes. Very few of them are of use to you, being dedicated to the more bizarre areas of magic.\n\nOne spell book, however, proves itself worth a quick browse. The spell inside is demanding, but not difficult to learn. You can now cast the spell Word of Recall.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_word_of_recall")

def MorogsCastle_198_MapTrigger_40_29(p):
    MessageBox("This is the body of a Slithzerikai, recently killed and bled. The corpse is lying here, ready to provide a tasty meal for Morog.")

def MorogsCastle_199_MapTrigger_26_28(p):
    if StuffDone["8_7"] == 250:
        return
    StuffDone["8_7"] = 250
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(26,28))
    MessageBox("Morog\'s Castle is more accomodating than you thought. This section contains a small town! This is a huge chamber, with a ceiling 40 feet high. Built inside it are several small shops, all of which are open for business.\n\nMorog must keep this here to service the magical travelers who pass through the run, and the beings who come to her to deal or to buy assistance.")

def MorogsCastle_200_MapTrigger_42_37(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(37,27))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_201_MapTrigger_42_47(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(48,7))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_202_MapTrigger_42_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(47,37))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_203_MapTrigger_23_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(6,56))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_204_MapTrigger_23_47(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(6,27))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_205_MapTrigger_23_37(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(27,28))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_206_MapTrigger_6_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(24,57))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_207_MapTrigger_6_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(24,47))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_208_MapTrigger_28_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(24,37))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_209_MapTrigger_37_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(41,37))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_210_MapTrigger_57_28(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(48,13))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_211_MapTrigger_48_12(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(56,28))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_212_MapTrigger_48_6(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(41,47))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_213_MapTrigger_46_37(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("There is a glowing teleporter here. Do you step through?", eDialogPic.STANDARD, 22, ["Enter", "Leave"]) == 0:
        Animation_Vanish(Party.LeaderPC, True, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(41,57))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        return

def MorogsCastle_214_MapTrigger_10_5(p):
    if StuffDone["8_8"] == 250:
        return
    StuffDone["8_8"] = 250
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(10,5))
    MessageBox("This room is filled with dozens of small piles of bones. They are the mortal remains of all manner of creatures, some humanoids, some animals. All of the bones show signs of sharp teeth gnawing on them.")

def MorogsCastle_215_MapTrigger_32_30(p):
    if StuffDone["8_9"] == 250:
        return
    StuffDone["8_9"] = 250
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(32,30))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(33,30))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(41,33))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(41,32))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(25,34))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(25,33))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(25,32))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(25,31))
    ChoiceBox("You stand at the entrance to Morog\'s throne room. She has constructed a magnificent palace, with this enormous, gleaming marble hall as its centerpiece.\n\nThe throne room was constructed over a natural caldera. Bubbling pits of hot mud keep the room intensely hot, and the sulphurous steam makes you faint. The ceiling glows, keeping the chamber well lit.\n\nTo the south, you see a massive throne. A small, hunched over, skeletal shape sits in it. Even though it looks ridiculously small sitting in the huge chair, you can feel the creature\'s power from here.\n\nThe being is a lich, one of the most powerful and feared beings in existence. Fortunately, it doesn\'t seem inclined to attack you. Yet.", eDialogPic.CREATURE, 60, ["OK"])

def MorogsCastle_223_MapTrigger_46_41(p):
    if StuffDone["110_0"] >= 1:
        MessageBox("The portal is dim now. It\'s gotten much weaker. You\'re sure it\'s not strong enough to take you back down to the deep caverns. There\'s nothing else to do here.")
        return
    if SpecialItem.PartyHas("MorogsShrooms"):
        MessageBox("The portal is dim now. It\'s gotten much weaker. You\'re sure it\'s not strong enough to take you back down to the deep caverns. There\'s nothing else to do here.")
        return
    result = ChoiceBox("This magical portal is different from the others scattered around this castle. It\'s larger and hotter, and has more power running through it. It looks more likely to send you far away from the Za-Khazi Run than across the building.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        MessageBox("At first, you think you\'ve made a critical mistake. The moment you step into the portal, you feel agonizing pain, as if you\'re being savagely ripped apart and the pieces are being carelessly tossed away.\n\nInstead, you fall out of another portal, into a pitch black cavern. It\'s icy cold, and you feel as if the air is pressing in upon you. It feels as if you\'ve been sent far, far away, possibly straight down.")
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(5,41)
        Party.MoveToMap(TownMap.List["DeepCaverns_10"])
        RunScript("DeepCaverns_524_StairwayDestination53", ScriptParameters(eCallOrigin.CUSTOM))
        return

def MorogsCastle_224_OnEntry(p):
    if StuffDone["8_5"] >= 1:
        Town.MakeTownHostile()
        return
    if StuffDone["8_0"] >= 1:
        MessageBox("Morog is a graceful host to her guests, but her hospitality has limits. Your theft of the history scroll was one of them. The moment you enter, the alarm is raised.")
        Town.MakeTownHostile()
        return

def MorogsCastle_225_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(25, 30),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(26, 30),WorldMap.SectorAt(Party.OutsidePos))

def MorogsCastle_226_CreatureDeath12(p):
    MessageBox("You have achieved the near-impossible - you have slain a lich. Morog literally falls apart. The magical force holding her bones together gone, they fall apart, and quickly molder into dust.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(20)
