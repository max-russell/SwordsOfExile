
def Sweetgrove_8_MapTrigger_58_56(p):
    MessageBox("This old silo has been abandoned by everyone except the rats.")

def Sweetgrove_9_MapTrigger_6_37(p):
    MessageBox("You try to take one of the books on the shelf. When you do, sparks leap out and burn your fingers. Irritated, you back away. At least there could be a warning sign!")
    Party.Damage(Maths.Rand(1, 1, 1) + 0, eDamageType.UNBLOCKABLE)
    Wait()

def Sweetgrove_10_MapTrigger_18_5(p):
    if StuffDone["1_3"] == 250:
        return
    StuffDone["1_3"] = 250
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(18,5))
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(15,19))
    MessageBox("This home was clearly abandoned in some haste. Some of the owner\'s possessions are scattered about, left behind in a frenzied effort to escape the Vale.")

def Sweetgrove_11_MapTrigger_16_8(p):
    if StuffDone["1_4"] == 250:
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
    StuffDone["1_4"] = 250
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(16,8))
    pc.RunTrap(eTrapType.DART, 1, 20)

def Sweetgrove_13_MapTrigger_36_27(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(36,27))
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(37,27))
    MessageBox("You find the pitiful debris of another person\'s dreams. Before it was abandoned, this was clearly a very handsome shop. Now it\'s just another empty building, filled with dust.\n\nSomething is different about this shop, however. There\'s a strange energy in the air, and your hair stands on end a little. There\'s something peculiar going on here.")

def Sweetgrove_15_MapTrigger_32_22(p):
    if StuffDone["1_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The runes on the floor are glowing gently. It must be a magical trap. These are intensely difficult to disarm ... you can only hope it\'s not too powerful.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The runes on the floor are glowing gently. It must be a magical trap. These are intensely difficult to disarm ... you can only hope it\'s not too powerful.", True)
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["1_1"] = 250
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(32,22))
    TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(41,22))
    pc.RunTrap(eTrapType.EXPLOSION, 0, 80)

def Sweetgrove_17_MapTrigger_35_21(p):
    if StuffDone["1_2"] == 250:
        return
    result = ChoiceBox("On a hunch, you dig a little in the dry, cracked dirt in the pot. Your efforts are soon rewarded. You unearth a small sphere. It\'s polished black stone, about four inches in diameter.\n\nAs you hold it, your hand begins to tingle. Whatever this thing is, it\'s quite a powerful little magic item. Of course, it could be incredibly dangerous, but that hardly seems a reason not to take it with you ...", eDialogPic.TERRAIN, 132, ["Take", "Leave"])
    if result == 0:
        StuffDone["1_2"] = 250
        TownMap.List["Sweetgrove_1"].DeactivateTrigger(Location(35,21))
        SpecialItem.Give("RunedStone")
        MessageBox("You pocket the stone sphere. You can only hope that it makes itself useful eventually ...")
        return
    return

def Sweetgrove_18_OnEntry(p):
    if StuffDone["1_9"] >= 1:
        ChoiceBox("You find yourself back in Sweetgrove, standing in front of Mayor Crouch! She is surprised, to say the least, at your appearance. She asks you what happened, and why you\'ve just appeared here.\n\nYou tell her of your adventure in the school, the leaky waste barrels, and of their destruction. Her reaction surprises you. You thought she would be thrilled, but she only grows more grim as you explain the situation.\n\nFinally, she says, \"It is as I feared. You have done a great good deed. But we will not be the beneficiaries. Our masters, the Empire, have poisoned our Vale, and it will be many years before the poisons are leached away.\"\n\n\"The poison in the water and the dirt will stay there for some time. The only hope for us, here, today, is to leave before it kills us all.\"", eDialogPic.CREATURE, 31, ["OK"])
        ChoiceBox("\"Please do not think me ungrateful.\" She sends for an aide, and you are given a large sack of gold coins. \"Simply letting us know the dimensions of the problem was an incredible service. Now we can escape with our lives.\"\n\n\"In addition, you saved many more lives, I am sure, by removing the problem\'s source. The Vale\'s woes will not now spread to other locales. For this we are infinitely grateful.\"\n\n\"Thank you again for your help.\" She returns to his desk. \"Now the work of survival begins.\"", eDialogPic.CREATURE, 31, ["OK"])
        Party.Gold += 2500
        ChoiceBox("In the weeks that followed, the Vale was evacuated. The Empire, uncharacteristically, tried to give some compensation, but nothing could make up for what these people have lost.\n\nYou are rewarded, of course, with the gold you have received, plenty of hard experience, and the promise of jobs to come. It\'s a bittersweet victory.\n\nAs you leave the Vale for the last time, you look back. It remains a grim place, lacking green plants and birdsong. You console yourselves with the fact that while animals and fish will still die here, humans will not.\n\nIn the next few years, things turn out to be not as bad as they seemed. The magic which created the sickness also serves, with great difficulty, to cure it as well. Empire wizards purge the soil of its poisons, and destroy the school and its contents.\n\nThe Vale never again regains its legendary richness and beauty, but it does become safe and productive again. And finally, one day, the people of Skylark Vale return to reclaim their home.\n\nTHE END", eDialogPic.STANDARD, 4, ["OK"])
        for pc in Party.EachAlivePC():
            pc.AwardXP(100)
        Scenario.End()
        return
    if StuffDone["1_5"] == 250:
        return
    StuffDone["1_5"] = 250
    ChoiceBox("You arrive at the city of Sweetgrove, largest settlement in Skylark Vale. On the surface, it\'s a beautiful place - several large adobe domes, poking out among stands of oak and alder.\n\nWhen you get closer, however, you see that the beauty is only on the surface. The streets are almost empty, and the few people walking along them shuffle along weakly, as if ill. The trees are dying.\n\nThe curse on Skylark Vale has hit this city very hard.", eDialogPic.TERRAIN, 189, ["OK"])

def Sweetgrove_19_TalkingTrigger17(p):
    if StuffDone["199_1"] >= 1:
        p.TalkingText = "You tell Mayor Crouch of the barrels of poison leaking underground. Shocked, she falls back into her chair, speechless. She shakes her head for several long minutes.\n\nThen she says, \"Thank you. I beg you, do what you can to remove the poison. I don\'t know how, but I\'m sure you can find a way.\""
        return
    if StuffDone["199_0"] >= 1:
        p.TalkingText = "When you tell Mayor Crouch how you managed to enter the old School of Magery, she looks disturbed. \"Why are you going there? There is a crisis! There is no time for tourism!\"\n\n\"Please, return when you have good news to report.\""
        return

def Talking_1_1(p):
    if Party.Gold < 5:
        p.TalkingText = "He shakes his head. \"Times are hard. If you have no gold, you can\'t stay.\""
    else:
        Party.Gold -= 5
        Party.Pos = Location(48, 44)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "He shows you to a dusty room. It clearly hasn\'t been used for a few weeks. You sleep poorly."
        CentreView(Party.Pos, False)

def Talking_1_3(p):
    if Party.Gold >= 2:
        Party.Gold -= 2
        p.TalkingText = "He fills some tankards and hands them to you. The beer tastes like the inside of a well-used boot. Your mouth burns, and your eyes water. McKean looks at you with sympathy. \"Yeah, that\'s been a serious problem.\""
    else:
        p.TalkingText = "\"Times are tough. No gold, no beer.\""
