
def Assikvas_35_MapTrigger_23_17(p):
    if StuffDone["2_0"] == 0:
        result = ChoiceBox("When you approach this corridor, a slith warrior steps up to block your way. It brandishes a massive two-tined spear, the traditional weapon of the slith warrior.\n\nIt says nothing, but its confrontation stance makes its meaning perfectly clear. To get by it, you will have to attack.", eDialogPic.CREATURE, 47, ["Leave", "Attack"])
        if result == 1:
            MessageBox("You draw your weapons. The creature calls out an alarm. In moments, Assikvas is like an angry bee hive, humming with hostile intent.")
            Town.MakeTownHostile()
            StuffDone["2_0"] = 1
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You back away. The slith, looking relieved that you decided not to attack, backs away and lowers its weapon.")
        return
    return

def Assikvas_38_MapTrigger_14_17(p):
    if StuffDone["2_0"] == 0:
        MessageBox("A Slithzerikai guard spots you. Alas, he is fully aware that you aren\'t supposed to be here. He shouts out an alarm, and in moments you hear the angry hisses of the alerted lizard people.")
        Town.MakeTownHostile()
        StuffDone["2_0"] = 1
        return

def Assikvas_40_MapTrigger_15_6(p):
    if StuffDone["2_0"] == 0:
        if StuffDone["2_1"] == 250:
            return
        StuffDone["2_1"] = 250
        MessageBox("You have found a secret back entrance into the Slithzerikai lair. You\'d best avoid the guards. If they see you back here, their reaction will probably be swift and violent.")
        return

def Assikvas_41_MapTrigger_8_20(p):
    if StuffDone["2_2"] == 250:
        return
    StuffDone["2_2"] = 250
    TownMap.List["Assikvas_2"].DeactivateTrigger(Location(8,20))
    MessageBox("You enter the Slithzerikai chieftain\'s chambers. Fortunately, they\'re currently empty. It\'s very hot in here. The sliths, being cold-blooded, keep their warrens as hot as possible.")

def Assikvas_42_MapTrigger_11_26(p):
    MessageBox("You notice that the book on the pedestal is very sparse, only 10 sheets of thick leather with crude maps painted on it. Walking over to investigate, you see that the pages contain charts of nearby bodies of water.\n\nIn particular, you find a diagram of the placement of dangerously sharp stones in a river to the northwest. You take note of this information - you can now pass any dangerous areas the sliths have created in nearby rivers.")
    StuffDone["211_0"] = 1

def Assikvas_43_MapTrigger_10_31(p):
    if StuffDone["2_3"] == 250:
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
    StuffDone["2_3"] = 250
    TownMap.List["Assikvas_2"].DeactivateTrigger(Location(10,31))
    pc.RunTrap(eTrapType.RANDOM, 3, 25)

def Assikvas_44_MapTrigger_1_25(p):
    Town.AlterTerrain(Location(4,23), 0, TerrainRecord.UnderlayList[10])

def Assikvas_45_MapTrigger_8_28(p):
    if StuffDone["2_4"] == 250:
        return
    StuffDone["2_4"] = 250
    TownMap.List["Assikvas_2"].DeactivateTrigger(Location(8,28))
    MessageBox("Suddenly, the floor opens up underneath you! You slide down a chute, and find yourself in a different cavern.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(3,31))
    p.CancelAction = True

def Assikvas_46_MapTrigger_8_29(p):
    if StuffDone["2_0"] == 0:
        StuffDone["2_0"] = 1
        MessageBox("Suddenly, an alarm rings out! The battle roars of alerted sliths roar down the corridors, and you hear the distant sounds of weapons being drawn.")
        Town.MakeTownHostile()
        return

def Assikvas_47_MapTrigger_8_27(p):
    if StuffDone["2_5"] == 250:
        return
    StuffDone["2_5"] = 250
    TownMap.List["Assikvas_2"].DeactivateTrigger(Location(8,27))
    MessageBox("You see several chests in the room to the south. Looks like you\'ve found the treasure room.")

def Assikvas_48_MapTrigger_38_7(p):
    ChoiceBox("The altar is covered with hundreds of small, carefully carved figurines. Each represents some obscure Slithzerikai god or hero from centuries past.\n\nThey\'re nice carvings, but not nice enough to be valuable. They are made of mundane types of stone, not anything you could sell for the materials.\n\nA sociologist could learn all sorts of things by looking at this. Being adventurers, currently in the process of butchering everyone here, you aren\'t too interested.", eDialogPic.TERRAIN, 158, ["OK"])

def Assikvas_49_MapTrigger_8_9(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
        MessageBox("This is a nice, thick spell book. It\'s written in Slithzerikai spell notation, but, fortunately, you\'ve learned some of it. Reading the parts you can understand, you learn how to cast the spell Protection.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_protection")
        return
    MessageBox("The good news is that this is a nice, thick spell book. The bad news is that it is written in Slithzerikai magical notation. Not understanding it, the book does you no good.")

def Assikvas_50_OnEntry(p):
    if Town.Abandoned:
        MessageBox("The Slithzerikai warrens are eerily silent. The few survivors of your earlier rampages have fled, rather than face your wrath again.")
    else:
        if StuffDone["2_0"] >= 1:
            MessageBox("The Slithzerikai here remember about you, and they have not forgiven you for your actions the last time you were here.")
            Town.MakeTownHostile()
            return

def Assikvas_51_TalkingTrigger3(p):
    if StuffDone["211_0"] < 1:
        result = ChoiceBox("Masskriss says \"Our toll to pass is large for humansss, who are unwelcome in our land. But we are generous. We letsss you pass for but 1200 gold piecesss. Will you pay us our fair toll?\"\n\n\"If you haven\'t the gold, you can sell things to Sssah.\" He points at the priest sitting next to him.", eDialogPic.CREATURE, 47, ["No", "Yes"])
        if result == 0:
            p.TalkingText = "He snorts. \"Fine, then. You can wait forever with no pass.\""
            return
        elif result == 1:
            if Party.Gold >= 1200:
                Party.Gold -= 1200
                p.TalkingText = "You pay the gold, and the slith warrior explains in great detail the route to row your boat along to pass the jagged rocks in the river to the northwest safely.\n\nYou take note of the information. The extortion money paid, you are free to continue."
                StuffDone["211_0"] = 1
                return
            p.TalkingText = "He shakes its head, annoyed. \"But no gold you has! Not enough! No pass for you!\""
            return
        return

def Assikvas_52_TalkingTrigger4(p):
    if StuffDone["211_0"] < 1:
        if SpecialItem.PartyHas("SlithStatuette"):
            result = ChoiceBox("The slith asks \"What itemsss might you have which has holy or great slith value to us?\" You pull out the small statue you found in the crypt.\n\nThe slith\'s eyes widen. \"It is a figurine! It is of Sss-Thsss, great and power slith leader of old. Great lord! Great artifact! Will you give it to us for your passage?\"", eDialogPic.CREATURE, 47, ["Leave", "Give"])
            if result == 1:
                p.TalkingText = "You hand over the figurine, and Masskriss explains in great detail the route to row your boat to successfully navigate the treacherous waters to the northwest. You take note of the information. You can move on now."
                StuffDone["211_0"] = 1
                SpecialItem.Take("SlithStatuette")
                return
            p.TalkingText = "\"Hmm. Fine then. I not tell you how to pass.\""
            return
        p.TalkingText = "The slith asks \"What itemsss might you have which has holy or great slith value to us?\" Unfortunately, you don\'t have any items which you think the Slithzerikai might find holy."
        return
