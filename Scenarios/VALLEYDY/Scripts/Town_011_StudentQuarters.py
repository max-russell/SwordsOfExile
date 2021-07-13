def Generate_Wandering_11_StudentQuarters(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Gremlin_188"]])
            npcs.append([1,NPCRecord.List["Gremlin_189"]])
            npcs.append([1,NPCRecord.List["Gremlin_190"]])
        elif r1 == 1:
            npcs.append([2,NPCRecord.List["Gremlin_120"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(36,23)
                elif r2 == 1: l = Location(27,25)
                elif r2 == 2: l = Location(28,11)
                elif r2 == 3: l = Location(24,11)
                
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

def StudentQuarters_195_MapTrigger_25_7(p):
    if StuffDone["11_1"] == 250:
        return
    StuffDone["11_1"] = 250
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(25,7))
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(27,7))
    ChoiceBox("You step through the open gates into the lower section of the School of Magery, where all the serious learning and research took place. The air is fresher here (if dustier) and it\'s a relief to leave the airborne poisons of the earlier caves behind.\n\nAlthough this area has been abandoned by its former owners, it is nowhere near unoccupied. You hear shrill, demonic screeches of laugher to the south, which don\'t bode well for your travels.\n\nRefuse is everywhere, and what were once lovely frescoes on the walls have been scratched into unrecognizability. The current residents of the School don\'t seem to feel like keeping things neat.\n\nIt has seemed that any long-lived creature which doesn\'t need to eat much has thrived while in the magical atmosphere of the school. It will probably be tough going from here on in ...", eDialogPic.TERRAIN, 93, ["OK"])

def StudentQuarters_197_MapTrigger_38_28(p):
    if StuffDone["11_2"] == 250:
        return
    StuffDone["11_2"] = 250
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(38,28))
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(37,28))
    MessageBox("Here is yet another area that was blown up before the School was abandoned. You haven\'t a clue what these rooms were used for. The destroyers were thorough.")

def StudentQuarters_198_MapTrigger_33_29(p):
    MessageBox("The books on these shelves were burned to bits by several well placed Flame spells.")

def StudentQuarters_199_MapTrigger_33_16(p):
    MessageBox("Although the desk is empty, you notice that there\'s a small piece of paper crumpled underneath it. It reads: \"Don\'t forget. Caretaker key left with Provost. Healing Scepter still with Apothecary. Be sure to recover.\"\n\n\"If only we were given more time. Vinnia will have my head if they\'re left. Be sure not to forget.\"")

def StudentQuarters_200_MapTrigger_39_11(p):
    if StuffDone["11_3"] == 250:
        return
    StuffDone["11_3"] = 250
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(39,11))
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(39,13))
    MessageBox("Beyond these heavy gates, the worldly possessions of the students here were stored, kept from them so that they could concentrate on their studies. It looks like a few items still remain.")

def StudentQuarters_201_MapTrigger_12_6(p):
    if StuffDone["11_4"] == 250:
        return
    result = ChoiceBox("On a polished marble pedestal, you find a small scepter, resting on a pillow of velvet.\n\nIt\'s not an impressive object, merely a piece of polished and varnished driftwood with a piece of rose quartz set in one end. Despite its unassuming appearance, you can\'t help but believe an object so well hidden must have at least a small value.", eDialogPic.TERRAIN, 125, ["Take", "Leave"])
    if result == 0:
        StuffDone["11_4"] = 250
        TownMap.List["StudentQuarters_11"].AlterTerrain(Location(12,6), 1, None)
        TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(12,6))
        SpecialItem.Give("HealingScepter")
        MessageBox("The sceptre is slightly warm to the touch and feels solid and reassuring in your hand. Whatever it is, it\'s now yours.")
        return
    return

def StudentQuarters_202_MapTrigger_15_9(p):
    if StuffDone["11_5"] == 250:
        return
    StuffDone["11_5"] = 250
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(15,9))
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(14,8))
    MessageBox("This book contains records of the students let into the infirmary, and the cause of the injuries that placed them there. The number placed here because of magical accidents is quite telling.\n\nThe gremlins didn\'t tear this book up, although it shows signs that they flipped through it frequently. This is probably because they\'ve found reading it to be very amusing.")

def StudentQuarters_204_MapTrigger_16_23(p):
    if StuffDone["11_6"] == 250:
        return
    StuffDone["11_6"] = 250
    TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(16,23))
    MessageBox("This areas contains the cells where the third year apprentices spent their traditional year of silence, privation, and quiet thought. This area looks far too enclosed and boring for the gremlins to live  here.")

def StudentQuarters_205_MapTrigger_16_37(p):
    result = ChoiceBox("One of the books on this bookshelf looks useful (the rest being moldy, esoteric, or pieces of amusing fiction). It\'s a book of magic, probably left here by a careless student. You can\'t understand the title.", eDialogPic.TERRAIN, 135, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 8:
            MessageBox("It takes an hour of careful concentration, but you manage to decipher the runes inside. It is indeed a spellbook, teaching the words and subtle motions necessary to cast the Poison spell. You learn it well.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_poison")
            return
        MessageBox("Alas, you can\'t understand the magical script inside. Maybe, if you had taken a few classes here, it would have made more sense ...")
        return

def StudentQuarters_206_MapTrigger_14_37(p):
    MessageBox("The bookshelves in this room don\'t contain the spellbooks and dry magical tomes you\'ve come to expect. Instead, they seem to contain fiction and other works of a lighter nature.\n\nAccess to this room was probably a reward for third year students, or a brief respite from the ceaseless privations of being an apprentice here.")

def StudentQuarters_208_MapTrigger_1_42(p):
    MessageBox("This desk is empty.")

def StudentQuarters_212_MapTrigger_1_46(p):
    if StuffDone["11_8"] == 250:
        return
    result = ChoiceBox("Most of the books, journals, and scrolls on these shelves have rotted away. The few that remain readable are useless to you, mainly forms and records.\n\nAs you pull one book out, however, a shiny item falls to the floor with a metallic ring. You bend down to inspect it. It\'s a small silver key.", eDialogPic.TERRAIN, 135, ["Take", "Leave"])
    if result == 0:
        StuffDone["11_8"] = 250
        TownMap.List["StudentQuarters_11"].DeactivateTrigger(Location(1,46))
        SpecialItem.Give("SilverKey")
    return

def StudentQuarters_213_MapTrigger_24_46(p):
    MessageBox("At one time, the transcripts and student records in this chamber needed to be well hidden and guarded. Nobody cares anymore, of course, but hidden they remain.")

def StudentQuarters_214_MapTrigger_28_43(p):
    Town.AlterTerrain(Location(32,37), 0, TerrainRecord.UnderlayList[125])

def StudentQuarters_216_MapTrigger_27_46(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(1,2)
    Party.MoveToMap(TownMap.List["LectureHalls_12"])

def StudentQuarters_220_MapTrigger_20_35(p):
    MessageBox("Someone has cast quite a spell on these doors. The walls to either side of them melted, and the stone flowed like water over their edges, solidifying in bars of rock, 5 inches thick.\n\nThese doors are sealed. You\'ll have to find another way through.")

def StudentQuarters_224_MapTrigger_33_37(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,37)).Num == 128:
        if SpecialItem.PartyHas("SilverKey"):
            MessageBox("You find a locked door with a silver keyhole. You try the silver key you found nearby in the lock, and it fits. The door is now unlocked.")
            Town.AlterTerrain(Location(32,37), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("This door is locked. There is a silver keyhole, but you have no key that fits. Considering the power of the mages who sealed this portal, you aren\'t optimistic about your ability to open it.")
        return

def StudentQuarters_227_MapTrigger_30_46(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(1,34)
    Party.MoveToMap(TownMap.List["Libraries_13"])
