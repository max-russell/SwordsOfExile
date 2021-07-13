def Generate_Wandering_11_OpalCitadel(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Soldier_13"]])
            npcs.append([1,NPCRecord.List["Soldier_13"]])
            npcs.append([1,NPCRecord.List["Soldier_13"]])
            npcs.append([2,NPCRecord.List["Captain_14"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(30,15)
                elif r2 == 1: l = Location(8,10)
                elif r2 == 2: l = Location(6,8)
                elif r2 == 3: l = Location(42,5)
                
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

def OpalCitadel_244_MapTrigger_41_10(p):
    if StuffDone["11_0"] == 250:
        return
    StuffDone["11_0"] = 250
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(41,10))
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(41,9))
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(41,8))
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(41,7))
    MessageBox("Looking through the window, you see what looks like a small shop. Behind the counter is a human, wearing ragged, torn Empire armor, dealing with customers. The customers, interestingly enough, are two wights.\n\nThe human notices you and looks very alarmed. As the wights turn around, the human jumps through a concealed door in the far wall.")

def OpalCitadel_245_MapTrigger_31_10(p):
    MessageBox("This is an enormous, closed portcullis. The bars are far too thick to bend and too close together to slide between.")

def OpalCitadel_246_MapTrigger_26_3(p):
    if StuffDone["11_1"] == 250:
        return
    StuffDone["11_1"] = 250
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(26,3))
    MessageBox("You are at the east end of a narrow bridge over a small pool. Stone ramps are suspended between large stalagmites protruding from the water.\n\nHumans with bows watch you from windows overlooking the bridge. Several of them are taking aim. This fortress is more than ready to defend itself against you.")

def OpalCitadel_247_MapTrigger_10_18(p):
    if StuffDone["11_2"] == 250:
        return
    StuffDone["11_2"] = 250
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(10,18))
    ChoiceBox("There is a large cavern on the other side of the guarded wall. Several crude stone buildings have been constructed inside, some of them barracks, some storerooms.\n\nThere are several guards waiting for you. They\'re dressed like Empire soldiers, but their armor is old and their weapons are dented and slightly rusty. If they are, in fact, from the Empire, they must have been down here for some time.", eDialogPic.CREATURE, 15, ["OK"])

def OpalCitadel_248_MapTrigger_3_23(p):
    MessageBox("The mages here have written their magical notes and thoughts on sheets of treated lizard skin. Unfortunately, their years here seem to have left them somewhat unhinged. The notes descend into demented raving more than once.")

def OpalCitadel_250_MapTrigger_7_32(p):
    ChoiceBox("One of the mages here has been keeping a crude journal, which you find in this desk. It explains, in a rambling, demented way, where this colony came from.\n\nThe people here were a band of elite soldiers during the Empire War with Exile. They were taking boats through the Za-Khazi Run in the hopes of running surprise raids on Exile. Alas, their boats got stuck in the same place yours did.\n\nTrapped here, they made the best of their situation. During their exploration, they found a rich opal deposit. They settled here, mining the stones while waiting for rescue.\n\nWhen no rescue came, they had children and settled down, growing more and more isolated and disturbed.  They never learned of the Empire\'s peace with Exile. Now they are very wealthy, but they\'re also trapped here and unable to take advantage of it.", eDialogPic.TERRAIN, 126, ["OK"])

def OpalCitadel_251_MapTrigger_3_41(p):
    MessageBox("The rune flashes as you pass over it. Your skin feels slightly parboiled.")
    Party.Damage(Maths.Rand(5, 1, 5) + 5, eDamageType.UNBLOCKABLE)
    Wait()

def OpalCitadel_252_MapTrigger_42_46(p):
    if StuffDone["11_3"] == 250:
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
    StuffDone["11_3"] = 250
    TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(42,46))
    pc.RunTrap(eTrapType.GAS, 2, 25)

def OpalCitadel_253_MapTrigger_39_22(p):
    if StuffDone["11_4"] == 250:
        return
    result = ChoiceBox("The altar is a rough block of stone, covered with a sheet of purple cloth. The altar has a gold candlestick on it.", eDialogPic.TERRAIN, 137, ["Take", "Leave"])
    if result == 0:
        StuffDone["11_4"] = 250
        TownMap.List["OpalCitadel_11"].DeactivateTrigger(Location(39,22))
        Party.GiveNewItem("GoldCandlestick_389")
    return

def OpalCitadel_254_MapTrigger_5_24(p):
    result = ChoiceBox("There is a thick spellbook sitting on this pedestal. It\'s cover is dirty and scuffed, and the pages have a dirty, heavily thumbed look. The mages here have clearly been making do with what they had.\n\nOf course, you might be able to get something out of this book as well ...", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 16:
            MessageBox("You try to read the words on the pages, but as you look at them, they seems to dance and squiggle around on the page. You are aware of this sort of script. It is designed to keep the contents secret.\n\nFortunately, you have been trained in determining what words to read when, and you soon decode several spells. Most of them you know, but one is quite interesting. You can now cast Force Barrier.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_force_barrier")
            return
        MessageBox("You try to read the words on the pages, but as you look at them, they seems to dance and squiggle around on the page. You are aware of this sort of script. It is designed to keep the contents secret.\n\nYou need to know what words to read at what times. Unfortunately, you\'ve never learned the techniques for figuring out how to decode such pages. You don\'t get anything out of the book.")
        return

def OpalCitadel_255_MapTrigger_3_31(p):
    result = ChoiceBox("There is a thick spellbook sitting on this pedestal. It\'s cover is dirty and scuffed, and the pages have a dirty, heavily thumbed look. The mages here have clearly been making do with what they had.\n\nOf course, you might be able to get something out of this book as well ...", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        MessageBox("You open the book and try to read the words inside. When you do, the words immediately start shifting around on the page. As you watch, they shift around in hypnotic patterns. Lovely, lovely patterns. You have a hard time looking away.\n\nWhen you do finally manage to close the book and look away, you feel slightly dazed.")
        for pc in Party.EachAlivePC():
            pc.SP-= 25
        return

def OpalCitadel_256_MapTrigger_11_41(p):
    MessageBox("The scrolls on this bookshelf are all ledgers, describing the considerable number of opals pulled from the mines below (along with occasional demented ravings). One listing is of interest:\n\n\"Melora found an amazing specimen today! It\'s the size of a fist and utterly flawless. We must look at it. It is lovely. Lovely. We call it the Melora Opal because after all she found it! It is the most valuable thing we own. Valuable.\"")

def OpalCitadel_260_MapTrigger_20_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(4,1)
    Party.MoveToMap(TownMap.List["OpalMines_12"])
