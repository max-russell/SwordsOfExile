
def Libraries_243_MapTrigger_4_2(p):
    result = ChoiceBox("You walk up to this strange machine. It\'s about 12 feet high, is made of shiny bronze and iron, and beeps and buzzes. You spend a few minutes looking for controls, instructions, or some hint of what it does.\n\nEventually, you find a small, magical, glowing display. It reads: \"School Tome Dispenser. Please Select. Available: 1 - Mining Arts, 2 - Woodcarving Arts. Please Make A Selection.\"\n\nBelow the display are two buttons, labeled \'1\' and \'2\'. Do you press one of them, or leave?", eDialogPic.TERRAIN, 229, ["Leave", "1", "2"])
    if result == 1:
        if StuffDone["13_0"] == 250:
            return
        StuffDone["13_0"] = 250
        MessageBox("You press the buttons. The machine squeals and beeps, and a small tablet of stone slides out into a nearby hopper. Unfortunately, some smoke and sparks come out with it. The machine display goes dark. You get the tablet.")
        SpecialItem.Give("StoneTablets")
        return
    elif result == 2:
        if StuffDone["13_0"] == 250:
            return
        StuffDone["13_0"] = 250
        MessageBox("You press the buttons. The machine squeals and beeps, and a small tablet of stone slides out into a nearby hopper. Unfortunately, some smoke and sparks come out with it. The machine display goes dark. You get the tablet.")
        SpecialItem.Give("StoneTablets_4")
        return

def Libraries_244_MapTrigger_12_1(p):
    ChoiceBox("This chamber is where all of the school\'s rarest and most valuable spell books were stored. They\'re gone now. There\'s nothing but several rows of bare pedestals and this official looking proclamation, pinned to the wall:\n\n\"BY THE ORDER OF EMPEROR STEWART, MOST HIGH RULER OF THE EMPIRE.\n\nIt is now officially decreed that the School of Magery, located in Skylark Vale, cease operations immediately. The deadline for ceasing of operations is one week from receipt of this proclamation.\n\nThe school is to be sealed, and all magical texts returned to Empire custody or destroyed. The School is to be permanently sealed, and all students and faculty are to return to Empire custody.\n\nAnyone interfering with the carrying out of this order will be disciplined in the most severe way. A similar fate will await those entering the School later than one week from now. That is all.\"\n\nThe proclamation is dated 130 years ago. Emperor Stewart has been dead for a century.", eDialogPic.TERRAIN, 106, ["OK"])

def Libraries_245_MapTrigger_35_6(p):
    MessageBox("The index card and files for the library were in this room. Well, they still are, but someone has gone through, dumped them out, and mixed them up. In this state of disarray, they\'ll be useless for finding your way around the library.")

def Libraries_246_MapTrigger_11_33(p):
    MessageBox("You find the body of a murdered mage. She was barricaded up here behind several force barriers, and left to starve. Ugly business.")

def Libraries_247_MapTrigger_1_33(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(30,45)
    Party.MoveToMap(TownMap.List["StudentQuarters_11"])

def Libraries_249_MapTrigger_3_23(p):
    if StuffDone["13_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?", True)
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["13_1"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(3,23))
    pc.RunTrap(eTrapType.BLADE, 2, 40)

def Libraries_250_MapTrigger_8_30(p):
    if StuffDone["13_2"] == 250:
        return
    StuffDone["13_2"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(8,30))
    MessageBox("When you step inside this small chamber, a cloud of blue mist appears in the northwest corner. It soon fades, and a big, nasty lizard is left in its place. Looks like someone\'s left a nice magical trap behind for you.")
    Town.PlaceEncounterGroup(2)

def Libraries_251_MapTrigger_18_27(p):
    MessageBox("You find an interesting, thin book on something called a Piercing Crystal. It\'s a magical item which can dispel any magical barrier it\'s thrown at. Useful thing to have around.")

def Libraries_252_MapTrigger_36_13(p):
    MessageBox("You find a book on \"library sprites.\" They\'re magical creature created in many libraries (such as this one) to keep things clean and looked after automatically.\n\nThe book makes a note that library sprites shouldn\'t be left unguided for too long. They are, in a limited way, sentient, and will become very unstable when left alone.")

def Libraries_253_MapTrigger_40_30(p):
    MessageBox("You find a book describing the spell Move Mountains. You can already cast this spell, so the tome isn\'t very interesting to you. All it really does is go on at great length on what use this spell can be to destroy weak walls.")

def Libraries_254_MapTrigger_38_13(p):
    if StuffDone["13_3"] == 250:
        return
    StuffDone["13_3"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(38,13))
    MessageBox("You open an interesting looking book. The first page has a large, painted rune inside the front cover. You recognize what it is too late. The book explodes, burning you badly ...")
    Party.Damage(Maths.Rand(6, 1, 7) + 1, eDamageType.FIRE)
    Wait()

def Libraries_255_MapTrigger_13_26(p):
    if StuffDone["13_4"] == 250:
        return
    StuffDone["13_4"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(13,26))
    MessageBox("Suddenly, a shower of books rains down from above onto your heads. Bruised, you look up, but you can\'t figure out what caused the books to fall.")
    Party.Damage(Maths.Rand(2, 1, 2) + 2, eDamageType.WEAPON)
    Wait()

def Libraries_256_MapTrigger_34_24(p):
    if StuffDone["13_5"] == 250:
        return
    StuffDone["13_5"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(34,24))
    MessageBox("Suddenly, a shower of books rains down from above onto your heads. Bruised, you look up, but you can\'t figure out what caused the books to fall.")
    Party.Damage(Maths.Rand(2, 1, 2) + 2, eDamageType.WEAPON)
    Wait()

def Libraries_257_MapTrigger_30_16(p):
    if StuffDone["13_6"] == 250:
        return
    StuffDone["13_6"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(30,16))
    MessageBox("Suddenly, a shower of books rains down from above onto your heads. Bruised, you look up, but you can\'t figure out what caused the books to fall.")
    Party.Damage(Maths.Rand(2, 1, 2) + 2, eDamageType.WEAPON)
    Wait()

def Libraries_258_MapTrigger_5_10(p):
    if StuffDone["13_7"] == 250:
        return
    StuffDone["13_7"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(5,10))
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(5,18))
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(15,18))
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(15,10))
    MessageBox("You find another room which was destroyed before the School was closed. You have little doubt that plenty of invaluable magical texts were destroyed.")

def Libraries_262_MapTrigger_23_31(p):
    if StuffDone["13_8"] == 250:
        return
    StuffDone["13_8"] = 250
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(23,31))
    TownMap.List["Libraries_13"].DeactivateTrigger(Location(24,31))
    ChoiceBox("You step into the library of the School of Magery. The air is cool, musty, and still, and the smell of books and leather bindings fill the air.\n\nDown the hallways, you see many shelves of books and scrolls, thick and thin, bound in paper and leather. Strangely, there is a visible lack of dust and decay. Things seem to have been kept in good order. Someone\'s been looking after the place.", eDialogPic.TERRAIN, 135, ["OK"])

def Libraries_264_MapTrigger_32_22(p):
    if Maths.Rand(1,0,100) < 8:
        MessageBox("Out of the corner of your eye, you\'d swear you see two of the books on a nearby shelf switch places. You look closer but see nobody there. Must have been your imagination.")
        return

def Libraries_269_MapTrigger_43_6(p):
    if StuffDone["13_9"] >= 1:
        return
    MessageBox("You stand at the entrance to a small room with a lone pedestal, which has nothing resting on it. As you look at it, you hear a voice whispering in your ear. \"On the pedestal. The green book. We miss the green book.\"\n\nYou turn quickly, but nobody is there. It\'s still and quiet.")

def Libraries_270_MapTrigger_20_8(p):
    if StuffDone["13_9"] >= 1:
        return
    if Maths.Rand(1,0,100) < 25:
        MessageBox("You hear a whispered message in your ear. \"Green books. We miss the green books. Stolen. Want. Want. Back here to us.\" You turn to see who spoke to you, but there\'s nobody there.")
        return

def Libraries_274_MapTrigger_42_10(p):
    if StuffDone["13_9"] >= 1:
        return
    if Maths.Rand(1,0,100) < 25:
        MessageBox("You hear a soft voice whispering in your ear. It says \"The pedestal. To the pedestal. On the pedestal.\" You turn to see who spoke, but there\'s nobody there.")
        return

def Libraries_278_MapTrigger_3_26(p):
    result = ChoiceBox("You find a thick tome, bound in thick, green dyed leather. Strange runes and symbols are etched in the cover.", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 11:
            MessageBox("It\'s a book of alchemical recipes! While instructions for making hair restoratives and magically augmented laxatives aren\'t interesting to you, you find a good recipe for a powerful poison.\n\nIt requires wormgrass to make, but isn\'t very difficult and doesn\'t require much Alchemy skill.")
            Party.LearnRecipe("medium_poison")
            return
        MessageBox("You peruse the book, but just can\'t make any sense of the words inside. The magical dialect is just too complicated for you. Maybe if you studied more Mage Lore ...")
        return

def Libraries_279_MapTrigger_5_26(p):
    result = ChoiceBox("You find a thick tome, bound in thick, black leather. Strange runes and symbols are etched in the cover, and strips of onyx are set into the spine. It\'s cold to the touch.", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
            MessageBox("It\'s a book on necromancy and the dark arts, describing rituals so dark and horrifying they chill your soul, and yet so eerily compelling that you can\'t stop reading.\n\nWhen you can finally stumble away, you feel numb. Your brain feels dull and lost.")
            for pc in Party.EachAlivePC():
                pc.AwardXP(-10)
            return
        MessageBox("You peruse the book, but just can\'t make any sense of the words inside. The magical dialect is just too complicated for you. Maybe if you studied more Mage Lore ...")
        return

def Libraries_280_MapTrigger_7_26(p):
    result = ChoiceBox("You find a thick tome, bound in thick, red dyed leather. Strange runes and symbols are etched in the cover. The cover is soft and warm to the touch.", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 10:
            MessageBox("This is a book on the healing arts. While the recipes for acne treatment, extreme chafing and hangnail removal don\'t interest you (well, maybe the chafing one), the recipe for a healing potion does.\n\nThe recipe calls for Glowing Nettle, an alchemical ingredient. With it, you could make all the healing potions you wanted.")
            Party.LearnRecipe("medium_healing_potion")
            return
        MessageBox("You peruse the book, but just can\'t make any sense of the words inside. The magical dialect is just too complicated for you. Maybe if you studied more Mage Lore ...")
        return

def Libraries_281_MapTrigger_43_34(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a tunnel leading out of the School. It looks recently dug, as if someone burrowed into here recently. The tunnel slopes sharply downward. It\'s steep, but you should be able to climb it.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(5,40)
    Party.MoveToMap(TownMap.List["VahnataiCaverns_15"])

def Libraries_283_MapTrigger_45_46(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(45,2)
    Party.MoveToMap(TownMap.List["ExperimentHalls_14"])

def Libraries_285_TownTimer_0(p):
    if StuffDone["13_9"] >= 1:
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(43,2), True):
            if i.SpecialClass == 1:
                itemthere = True
                break
    if itemthere == True:
        StuffDone["13_9"] = 1
        MessageBox("The air around you is suddenly filled with whispering voices: \"Thank you. Book. Thank ... Book. Thank you. Reward. Book. Thank you.\" You feel a strange tugging around your pocket.\n\nYou look in your pocket and find that, somehow, a large brass key has ended up there. Interesting.")
        SpecialItem.Give("BrassKey")
        return
