def Generate_Wandering_7_HoldingCells(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["GiantLizard_72"]])
            npcs.append([1,NPCRecord.List["GiantLizard_72"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["Goblin_38"]])
            npcs.append([1,NPCRecord.List["GoblinFlinger_40"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["GoblinFighter_39"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(9,19)
                elif r2 == 1: l = Location(36,15)
                elif r2 == 2: l = Location(37,28)
                elif r2 == 3: l = Location(15,29)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def HoldingCells_87_MapTrigger_2_7(p):
    if StuffDone["7_0"] == 250:
        return
    result = ChoiceBox("When the School of Magery was abandoned, this strange skeletal creature was left in this cell. You aren\'t sure what it looked like when it was still functioning, or whether it was good or evil.\n\nThe only thing you do know is that the years and years of being trapped in here were too much for it. It cut itself to pieces with its sword, only stopping when its pieces were spread all over the room.\n\nWhat was it, why was it left here, and why was it left with a weapon? You can only guess. At least the sword is still here, if you want it.", eDialogPic.CREATURE, 51, ["Take", "Leave"])
    if result == 0:
        StuffDone["7_0"] = 250
        TownMap.List["HoldingCells_7"].AlterTerrain(Location(2,7), 1, None)
        TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(2,7))
        Party.GiveNewItem("FlamingSword_345")
    return

def HoldingCells_88_MapTrigger_2_14(p):
    MessageBox("This book still contains the list of creatures held in these cells, creatures, who were supposed to have long lifespans and who could be left here for some time.\n\nThe last entries indicate that two of the cells were left occupied when the School was abandoned. The prisoners: \'Vazalco\' and \'Seemingly sentient skeletal creature, with stubbornly held weapon.\'")

def HoldingCells_89_MapTrigger_33_30(p):
    if StuffDone["7_1"] == 250:
        return
    StuffDone["7_1"] = 250
    TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(33,30))
    MessageBox("When the School had a specimen they wanted to put on display, this arena was used. Rings of seats surround an open central area, where creatures could be put out on display.\n\nNow that this level is controlled by goblins, however, this arena seems to be more for their amusement. Several undead creatures have been sealed up in the middle, no doubt to be taunted by the nasty little humanoids.")

def HoldingCells_90_MapTrigger_36_1(p):
    MessageBox("While this desk was left behind for you to find, everything inside it was removed. Nice desk, anyway.")

def HoldingCells_92_MapTrigger_32_1(p):
    MessageBox("The only thing in this desk is a brief memo: \"Velad - A Power Crystal is missing. And an opening stone, and documentation as well. If you can\'t keep things straight, you will be replaced. - Vinnia\"")

def HoldingCells_93_MapTrigger_44_1(p):
    result = ChoiceBox("Not all of the moldy books on these shelves seem worthless. One of them, titled \"Alchemical Arcana,\" looks quite interesting.", eDialogPic.TERRAIN, 135, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 5:
            MessageBox("It\'s a book of Alchemical Recipes. Most of them are pretty dull: cleansing solutions, beverages, and the like. One, however, is for a \'Potion of Greater Alacrity.\'\n\nIt\'s the recipe for a Potion of Weak Speed, which requires comfrey root and wormgrass. You take note of it for future potion making.")
            Party.LearnRecipe("weak_speed")
            return
        MessageBox("Well, it seemed interesting, but your knowledge of Mage Lore is insufficient to make any sense of it. Disappointed, you return it to the shelf.")
        return

def HoldingCells_94_MapTrigger_40_7(p):
    if StuffDone["7_3"] == 250:
        return
    StuffDone["7_3"] = 250
    TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(40,7))
    MessageBox("Like most goblin tribes, the small tribe on this level needed a place to reverentially put their dead. They adopted this room for that sacred purpose. The bones actually aren\'t that interesting.")

def HoldingCells_95_MapTrigger_44_7(p):
    if StuffDone["7_4"] == 250:
        return
    StuffDone["7_4"] = 250
    TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(44,7))
    MessageBox("The sign on the door said, unnervingly enough, \"Dissection Room.\" Despite that, this room seems mundane enough. All the room contains are two tables, and a ring of runes on the floor by the south wall.")

def HoldingCells_96_MapTrigger_44_11(p):
    MessageBox("Oh, no! When you step into the ring of runes, invisible knives begin to, with careful, precise strokes, slash you open. You jump back fast enough to save your life, but not your good health.")
    Party.Damage(Maths.Rand(10, 1, 10) + 0, eDamageType.WEAPON)
    Wait()
    p.CancelAction = False

def HoldingCells_97_MapTrigger_39_24(p):
    MessageBox("You sit down in the nice, padded seat and start examining the controls. Unfortunately, it doesn\'t take long to figure out that they\'re completely dead. Pressing the unresponsive buttons gets boring pretty quickly.")

def HoldingCells_100_MapTrigger_41_23(p):
    result = ChoiceBox("This control panel has three buttons on it, labeled \"Holding 1\", \"Holding 2\", and \"Holding 3.\" The first two are stuck in the down position. The third isn\'t.", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        MessageBox("You push the button. It makes a satisfying click. Nothing else happens (that you can tell).")
        t = Town.TerrainAt(Location(1,17))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(1,17), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(1,17), 0, TerrainRecord.UnderlayList[130])
        return

def HoldingCells_101_MapTrigger_39_18(p):
    if StuffDone["7_5"] >= 1:
        MessageBox("This control panel is still dark.")
        return
    result = ChoiceBox("The top of this pedestal is smooth, flat, and featureless, and glows slightly. When you get close, you hear a soft, gentle voice. It says \"Please approach and sit to operate.\"", eDialogPic.TERRAIN, 125, ["Leave", "Sit"])
    if result == 1:
        ChoiceBox("When you sit in front of the pedestal, the voice says \"What is your command?\" It seems to be waiting for you to say something.", eDialogPic.TERRAIN, 125, ["OK"])
        response = InputTextBox("Enter something:", "")
        response = response[0:5].upper()
        if response == "QUARK":
            StuffDone["7_5"] = 1
            ChoiceBox("You say \"Quark,\" and the voice responds \"Command accepted.\" You wait. At first, it seems like nothing has happened. Then several things happen all at once. First, the floor and walls begin to shake slightly.\n\nThen the vibrations come in sharp pulses, as if mighty blows are being struck somewhere. The vibrations come faster and faster, and then suddenly cease. Then you hear, off in the distance, a mighty roar, followed by an impact, followed by silence.\n\nYou look back at the pedestal for some clue of what has happened, but it has gone dark. Nothing else happens.", eDialogPic.TERRAIN, 125, ["OK"])
            StuffDone["Event_2"] = Party.Day
            return
        MessageBox("You respond, and wait for something to happen. After a moment, the voice says \"I am not aware of any meaning inherent in your response. I apologize for my inadequacy.\"")
        return

def HoldingCells_102_MapTrigger_12_39(p):
    MessageBox("When you step on the rune, blue and red lights start to play over you. You feel them lightly searing your flesh, cleansing away any nasty afflictions you may have picked up in the holding cells. It kind of hurts.")
    Party.Damage(Maths.Rand(1, 1, 1) + 0, eDamageType.UNBLOCKABLE)
    Wait()
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 8))

def HoldingCells_103_MapTrigger_11_27(p):
    if StuffDone["7_6"] == 250:
        return
    StuffDone["7_6"] = 250
    TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(11,27))
    TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(11,26))
    TownMap.List["HoldingCells_7"].DeactivateTrigger(Location(11,25))
    MessageBox("This platform was where the creatures that resided in these holding cells were teleported in. Now that the School is abandoned, the goblins are using this chamber as a garbage dump.")

def HoldingCells_106_MapTrigger_1_42(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(35,11)
    Party.MoveToMap(TownMap.List["VisitorsQuarters_6"])

def HoldingCells_111_MapTrigger_38_42(p):
    return

def HoldingCells_112_MapTrigger_14_42(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(16,2)
    Party.MoveToMap(TownMap.List["Administration_9"])
