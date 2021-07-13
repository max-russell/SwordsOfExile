
def Selathni_10_MapTrigger_14_53(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["Selathni_1"].DeactivateTrigger(Location(14,53))
    ChoiceBox("You walk up the dock into the city of Selathni. Looking around, it\'s hard to believe there\'s any trouble here. The people look happy and well fed, and the buildings and streets are clean and well taken care of.\n\nTo the northeast, you see a large inn with a long green sea serpent painted along its wall. Perhaps that\'s where you\'re supposed to meet Vonnegut and find out what\'s going on.", eDialogPic.TERRAIN, 189, ["OK"])

def Selathni_11_MapTrigger_11_49(p):
    if SpecialItem.PartyHas("EmpirePapers"):
        result = ChoiceBox("You notice, at the base of the counter, the gap in the floor Canizares told you about. It\'s a crack, about a foot long, in the floor at the base of the counter. The Empire papers would just barely fit inside it.\n\nDo you drop the papers down the crack?", eDialogPic.TERRAIN, 150, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            MessageBox("You drop the papers into the crack, and they disappear from sight. You can only hope they get to whoever wants them.")
            SpecialItem.Take("EmpirePapers")
            StuffDone["1_1"] = 1
            StuffDone["1_8"] = 1
            return
        return
    MessageBox("You notice a large crack in the floor.")

def Selathni_12_MapTrigger_34_43(p):
    if StuffDone["1_2"] == 250:
        return
    StuffDone["1_2"] = 250
    TownMap.List["Selathni_1"].DeactivateTrigger(Location(34,43))
    MessageBox("This hotel room has two reading stands set up in it. Each has a chair set up in front of it, so that you can read in comfort.")

def Selathni_13_MapTrigger_35_44(p):
    ChoiceBox("The book is titled \"History of Morrow\'s Isle.\" A summary:\n\nMorrow\'s Isle was first settled by humans about 200 years before. Valorim was a wild and unsettled continent, and the settlers had a very hard time of it.\n\nEventually, a tormented band of them made it to this Isle, and, when they found rich grasslands, ore-filled hills, and a minimal number of hostile creatures, they knew they had reached their final destination.\n\nOnce the few Nephilim living there were butchered, they were home at last. The settlers lived independently there for a hundred years, until the Empire finally noticed the Isle. Seeing the need for order, the Empire established a feudal state there.\n\nDespite a few minor difficulties which were easily dealt with, the transition of the island\'s population from settlers to serfs went smoothly, and, with hard work, the wealth of the island was harvested.\n\nToday, with many rich fields, productive mines, and happy citizens, Morrow\'s Isle is a virtual paradise to live and work in, thanks to the benevolent rule of the Empire and the hard work of the settlers.", eDialogPic.TERRAIN, 130, ["OK"])

def Selathni_14_MapTrigger_37_44(p):
    ChoiceBox("The leather bound tome is titled \"A Report On Unrest In Morrow\'s Isle.\" A brief summary of the uncensored parts:\n\nThere has been some unrest on Morrow\'s Isle for the past century, ever since the settlers there were brought under the control of a feudal lord. Until recently, the minor rebellions were easily dealt with.\n\nNow, however, there is a new, vicious force on the Isle. Known as the Hill Runners, and led by a person known only as Stalker, the rebels have has a good deal of success against the government.\n\nThey have completely seized control of the northeastern mountains of Morrow\'s Isle, and, playing on and building up a small amount of mild discontent in the citizenry, they have done a good deal of harm to the Empire\'s control in this area.\n\nPart of their success can be attributed to their vicious tactics. Nobody, neither soldiers nor civilians, men nor women, is exempted from the Hill Runner\'s violence. Aiding an Empire soldier invites murder as surely as being one.\n\nSomething should be done about this menace as quickly as possible. Otherwise, it is possible that malcontents in other areas will feel these tactics can succeed, and adopt them.", eDialogPic.TERRAIN, 130, ["OK"])

def Selathni_15_MapTrigger_51_17(p):
    if StuffDone["1_3"] == 250:
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
    StuffDone["1_3"] = 250
    TownMap.List["Selathni_1"].DeactivateTrigger(Location(51,17))
    pc.RunTrap(eTrapType.RANDOM, 2, 0)

def Selathni_16_MapTrigger_43_17(p):
    if StuffDone["1_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("Uh oh. It looks like someone has set an alarm in this dresser.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("Uh oh. It looks like someone has set an alarm in this dresser.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["1_4"] = 250
    TownMap.List["Selathni_1"].DeactivateTrigger(Location(43,17))
    pc.RunTrap(eTrapType.ALERT, 0, 20)

def Selathni_17_MapTrigger_39_21(p):
    result = ChoiceBox("The shrine\'s donation box is here. It\'s empty right now. A small sign hung on the front of the box says \"Suggested, life-affirming donation: 100 gold.\"", eDialogPic.TERRAIN, 138, ["Leave", "Pay"])
    if result == 1:
        if Party.Gold >= 100:
            Party.Gold -= 100
            MessageBox("You put the money in the box. As you watch, it slowly disappears! You have a warm, pleasant feeling.")
            StuffDone["1_5"] = 1
            Party.Gold -= 100
            return
        MessageBox("Unfortunately, you don\'t have 100 gold.")
        return

def Selathni_18_MapTrigger_42_24(p):
    result = ChoiceBox("The shrine, as usual, is dominated by a large, gleaming altar. Even being near it fills you with a warm, comforting feeling. There are kneeling pads set in front, no doubt so you can pay your respects, get blessings, etc.", eDialogPic.TERRAIN, 158, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["1_5"] >= 1:
            MessageBox("When you kneel, the altar begins to glow warmly, bathing you in a healing white light. When the glow fades, you feel reinvigorated. Good shrine!")
            StuffDone["1_5"] = 0
            Party.HealAll(100)
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) - 7))
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 8))
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.PARALYZED, Maths.MinMax(0, 5000, pc.Status(eAffliction.PARALYZED) - 5000))
            return
        MessageBox("Kneeling in front of the altar does, indeed, give you a warm, pleasant feeling. And that\'s all.")
        return

def Selathni_19_MapTrigger_37_6(p):
    if StuffDone["100_8"] >= 1:
        if StuffDone["1_6"] == 250:
            return
        StuffDone["1_6"] = 250
        MessageBox("Remembering O\'Grady\'s instructions, you pull the dresser away from the wall. Sure enough, in a gap in the wall, you find a heavy, polished mahogany box. It\'s about a foot by eight inches by six inches.\n\nIt\'s pretty bulky, but you manage to fit it into your pack. Looks like it\'s time to go to Zaskiva.")
        SpecialItem.Give("OakBox")
        return

def Selathni_20_MapTrigger_21_38(p):
    if StuffDone["1_7"] == 250:
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
    StuffDone["1_7"] = 250
    TownMap.List["Selathni_1"].DeactivateTrigger(Location(21,38))
    pc.RunTrap(eTrapType.BLADE, 2, 40)

def Selathni_21_MapTrigger_8_54(p):
    MessageBox("The Selathni harbor has a high stone wall built around it, sheltering it from rough waves and storms. You are on a narrow path, running along this section of the wall.")

def Selathni_22_MapTrigger_26_52(p):
    if StuffDone["101_1"] >= 1:
        MessageBox("You reach the end of the dock, only to find no boat waiting for you. Looks like, now that you\'re criminals, getting off the island will not be as easy as it once was.")
        return
    result = ChoiceBox("You find a boat at the end of the dock, waiting to take passengers away from Morrow\'s Isle. If you want, you can leave this confusing, violent place now.", eDialogPic.TERRAIN, 64, ["No", "Yes"])
    if result == 0:
        p.CancelAction = True
        return
    elif result == 1:
        ChoiceBox("With heavy heart, you board the boat to leave Morrow\'s Isle. You came here with the dream of slaying evil, of fighting the good fight, of courage and nobility.\n\nInstead, you found corruption. You were only given a chance to be in the middle of a battle between selfish politicians and vicious rebels. Not what you had in mind.\n\nMaybe there was a way out of this, a way to, despite the mess, make things better. Probably not. You got away with your lives,  without making things any worse. It\'s not much of a reward, but hey, at least you\'ll be able to sleep at night.\n\nTHE END", eDialogPic.TERRAIN, 64, ["OK"])
        Scenario.End()
        return

def Selathni_23_OnEntry(p):
    if StuffDone["101_1"] >= 1:
        MessageBox("As soon as the guards see you, they recognize you. Someone calls an alarm out. More guards come running. You obviously aren\'t welcome here anymore. Now what?")
        Town.MakeTownHostile()
        return

def Selathni_24_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(21, 12),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 12),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(21, 12),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(22, 12),WorldMap.SectorAt(Party.OutsidePos))

def Talking_1_1(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "You get a few mugs of the Inn\'s beer. As expected, it\'s noxious stuff. As you choke it down, Klivans says \"You look new here. Have you heard the Isle\'s been dangerous lately?\""
    else:
        p.TalkingText = "\"Sorry. It costs 5 gold.\""

def Talking_1_3(p):
    if Party.Gold < 6:
        p.TalkingText = "\"Sorry. It costs 6 gold.\""
    else:
        Party.Gold -= 6
        Party.Pos = Location(37, 40)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "You are shown to a cramped room, containing 3 lumpy beds, an armada of bed bugs, and not much else. You\'ve spent a hellish night."
        CentreView(Party.Pos, False)

def Talking_1_23(p):
    if Party.Gold < 14:
        p.TalkingText = "She shakes her head. \"Sorry, friend. No quality without money.\""
    else:
        Party.Gold -= 14
        Party.Pos = Location(20, 10)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "You pay the hefty price and are shown to a neat, private room with a very comfortable bed. Your sleep is deep and restful."
        CentreView(Party.Pos, False)

def Talking_1_24(p):
    if Party.Gold >= 12:
        Party.Gold -= 12
        p.TalkingText = "She brings you a bottle of delicious, carefully aged wine. As you sip, she mentions conspiratorially, \"By the way, adventurers, are you interested in rumors? I\'m heard interesting things about the Empire, and about some monsters.\""
    else:
        p.TalkingText = "She frowns. \"You don\'t expect wine for free, now, do you?\""

def Talking_1_39(p):
    if Party.Day <= 25:
        p.TalkingText = "\"She\'s coming here soon to look into things. The closer investigators get to me, the worse things are. That\'s why I\'m glad for a chance to hand off the chest!\""
    else:
        p.TalkingText = "\"She\'s here now. She\'s always wandering the streets, poking into things! The closer investigators get to me, the worse things are. That\'s why I\'m glad for a chance to hand off the chest!\""

def Talking_1_58(p):
    if Party.Gold >= 400:
        horse_ids = ["Horse_0", "Horse_1"]
        horse_sold = False
        for s in horse_ids:
            if Vehicle.List[s].PartyOwns == False:
                Vehicle.List[s].PartyOwns = True
                Party.Gold -= 400
                horse_sold = True
                break
        if horse_sold == False:
            p.TalkingText = "There are no horses left."
        else:
            p.TalkingText = "He takes your gold and, with some difficulty, counts it. \"Great! The horses are in the stables, some of them will go with you now.\" He orders beer in celebration of his good fortune."
    else:
        p.TalkingText = "He belches angrily. It\'s an ugly sound. \"You want to rob a destitute man? My horses are 400 gold!\""
