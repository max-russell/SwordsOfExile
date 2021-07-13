
def MilestoneCasino_246_MapTrigger_22_40(p):
    if StuffDone["10_0"] == 250:
        return
    StuffDone["10_0"] = 250
    TownMap.List["MilestoneCasino_10"].DeactivateTrigger(Location(22,40))
    TownMap.List["MilestoneCasino_10"].DeactivateTrigger(Location(23,40))
    TownMap.List["MilestoneCasino_10"].DeactivateTrigger(Location(24,40))
    TownMap.List["MilestoneCasino_10"].DeactivateTrigger(Location(25,40))
    ChoiceBox("The towering shape of Milestone Casino covers a small hill and dominates the modest mining town below.\n\nThis place holds enormous attraction to the local miners, being the only site of diversion in their rather dreary lives. It is run by the owners of the tin and copper mines and insures that a great deal of the salary expenses return directly to them.\n\nDrawing on plentiful experience with infuriated miners who have lost their monthly wages, the owners have hired a band of troglodytes to maintain control.\n\nThe stocky monsters pat their weapons and grin, as if to encourage you to start a fight. You remind yourselves to behave very nicely.\n\nWarm air and music drifts from the main room of the casino, filled with eager miners and other visitors. A low wall to the northwest gives the restaurant a weak shelter from the noisy main room.\n\nTwo burly fighters guard a thick door into what you guess must be the infamous fighting arena.", eDialogPic.CREATURE, 113, ["OK"])

def MilestoneCasino_250_MapTrigger_23_22(p):
    MessageBox("These stairs lead from the noisy main room of the casino to a row private rooms on the first floor.")

def MilestoneCasino_252_MapTrigger_27_15(p):
    if StuffDone["10_1"] >= 1:
        MessageBox("There is a general surge towards the fighting pit as the head cashier himself descends to supervise a dramatic showdown in the arena. \"The battle commences in five minutes. Call out your bets now!\" the cashier announces.")
        Town.PlaceEncounterGroup(5)
        Timer(Town, 10, False, "MilestoneCasino_257_TownTimer_20", eTimerType.DELETE)
        return
    result = ChoiceBox("A big troglodyte keeps score in the fighting arena, doing his best to negotiate bets and remember the stakes put by eager gamblers. He occasionally seems to forget a stake or a debt, but nobody cares to argue with three hundred pounds of muscle.\n\nA new round of fighting is about to begin. The price for one bet is 400 gold pieces. Do you approach the troglodyte to offer a bet?", eDialogPic.CREATURE, 117, ["Leave", "Approach"])
    if result == 1:
        if Party.Gold >= 400:
            result = ChoiceBox("\"Rules easy. You guess right monster wins, you get two times money back. Your monster die, you lose.\" The troglo grins.\n\n\"This time, bet 400 gold. First monster, big bug. Second monster, bad bones. You choose.\"", eDialogPic.CREATURE, 117, ["Leave", "2", "1"])
            if result == 1:
                StuffDone["10_3"] = 1
                MessageBox("You place your bet. The grates covering the fighter cells rise, and an expectant hush settles as the spectators stretch to see. The two contestants seem hesitant to leave their cells at first. Suddenly they clash.")
                Party.Gold -= 400
                if StuffDone["10_1"] == 250:
                    return
                StuffDone["10_1"] = 250
                TownMap.List["MilestoneCasino_10"].AlterTerrain(Location(27,15), 1, None)
                TownMap.List["MilestoneCasino_10"].DeactivateTrigger(Location(27,15))
                Town.PlaceEncounterGroup(4)
                t = Town.TerrainAt(Location(37,19))
                if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
                elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
                t = Town.TerrainAt(Location(30,12))
                if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
                elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])
                return
            elif result == 2:
                StuffDone["10_2"] = 1
                MessageBox("You place your bet. The grates covering the fighter cells rise, and an expectant hush settles as the spectators stretch to see. The two contestants seem hesitant to leave their cells at first. Suddenly they clash.")
                Party.Gold -= 400
                if StuffDone["10_1"] == 250:
                    return
                StuffDone["10_1"] = 250
                TownMap.List["MilestoneCasino_10"].AlterTerrain(Location(27,15), 1, None)
                TownMap.List["MilestoneCasino_10"].DeactivateTrigger(Location(27,15))
                Town.PlaceEncounterGroup(4)
                t = Town.TerrainAt(Location(37,19))
                if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
                elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
                t = Town.TerrainAt(Location(30,12))
                if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
                elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])
                return
            return
        MessageBox("The troglo growls at you. \"You poor. Go away, or I eat!\"")
        return

def MilestoneCasino_253_MapTrigger_22_11(p):
    if StuffDone["10_7"] >= 1:
        if StuffDone["10_9"] == 250:
            return
        StuffDone["10_9"] = 250
        MessageBox("As you push the wall and uncover a secret panel, you hear a quick intake of breath and an ominous rumbling. \"You?ll never take me alive!\" a man cries. You get a quick look at the haunted face of the gambler before you draw your swords.")
        Town.PlaceEncounterGroup(6)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Out of curiosity, you tap the walls and uncover a secret panel. You peek in, and see a small chamber and an angry wizard. \"Leave me alone!\" he shouts, and sends a fireball roaring over your head. Having no interest in the man, you decide to obey.")

def MilestoneCasino_254_MapTrigger_20_8(p):
    MessageBox("A faint blur obscures the corner. Perhaps the mage was trying to conjure a way out of the casino without passing the guards. Your intrusion has stopped him from outrunning his debts.")

def MilestoneCasino_255_MapTrigger_14_13(p):
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
    pc.RunTrap(eTrapType.GAS, 1, 40)

def MilestoneCasino_256_TownTimer_18(p):
    MessageBox("There is a general surge towards the fighting pit as the head cashier himself descends to supervise a dramatic showdown in the arena. \"The battle commences in five minutes. Call out your bets now!\" the cashier announces.")
    Town.PlaceEncounterGroup(5)
    Timer(Town, 10, False, "MilestoneCasino_257_TownTimer_20", eTimerType.DELETE)

def MilestoneCasino_257_TownTimer_20(p):
    Animation_Hold(-1, 023_startoutdoorcombat)
    Wait()
    MessageBox("\"No more bets!\" the Head Cashier Voznu roars, and places the now full gold chest under heavy guard. \"Let the gates open! To insure a fair fight, we have taken a small precaution. I?m sure you understand.\" You feel drained of magical energy.")
    for pc in Party.EachAlivePC():
        pc.SP-= 100
    t = Town.TerrainAt(Location(37,19))
    if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
    elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
    t = Town.TerrainAt(Location(30,12))
    if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
    elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])

def MilestoneCasino_258_CreatureDeath14(p):
    MessageBox("The unfortunate gambler sinks to the floor with a last, frightened moan. Knowing what is expected from you, you reluctantly cut his head off as proof. You promise yourself never to get involved with gambling. Or with running a casino, for that matter.")
    StuffDone["10_8"] = 1

def MilestoneCasino_259_CreatureDeath26(p):
    if StuffDone["10_3"] >= 1:
        MessageBox("A furious fight erupts, cheered on by the spectators. Some throw bottles and small rocks to infuriate the opponents. They all yell, howl and curse.\n\nFinally, the battle ends, and your champion is the one left standing. You hurry to collect your winnings from the muttering troglodyte.")
        Party.Gold += 800
        MessageBox("The arena wardens clean the pit after the fight, and usher the surviving monster back into its cell. The troglodyte pit master announces a major fighting event coming up in a few minutes.")
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Vahnavoi_71": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Chitrach_130": Town.NPCList.Remove(npc)
        Timer(Town, 20, False, "MilestoneCasino_256_TownTimer_18", eTimerType.DELETE)
        t = Town.TerrainAt(Location(37,19))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
        t = Town.TerrainAt(Location(30,12))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])
        return
    MessageBox("A furious fight erupts, cheered on by the spectators. Some throw bottles and small rocks to infuriate the opponents. They all yell, howl and curse.\n\nUnfortunately, your champion is beaten soundly by its opponent. It finally collapses in a bloody pile, to the joy of some, and the chagrin of others. You bitterly renounce gambling.")
    MessageBox("The arena wardens clean the pit after the fight, and usher the surviving monster back into its cell. The troglodyte pit master announces a major fighting event coming up in a few minutes.")
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Vahnavoi_71": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Chitrach_130": Town.NPCList.Remove(npc)
    Timer(Town, 20, False, "MilestoneCasino_256_TownTimer_18", eTimerType.DELETE)
    t = Town.TerrainAt(Location(37,19))
    if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
    elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
    t = Town.TerrainAt(Location(30,12))
    if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
    elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])

def MilestoneCasino_260_CreatureDeath29(p):
    if StuffDone["10_2"] >= 1:
        MessageBox("A furious fight erupts, cheered on by the spectators. Some throw bottles and small rocks to infuriate the opponents. They all yell, howl and curse.\n\nFinally, the battle ends, and your champion is the one left standing. You hurry to collect your winnings from the muttering troglodyte.")
        Party.Gold += 800
        MessageBox("The arena wardens clean the pit after the fight, and usher the surviving monster back into its cell. The troglodyte pit master announces a major fighting event coming up in a few minutes.")
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Vahnavoi_71": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Chitrach_130": Town.NPCList.Remove(npc)
        Timer(Town, 20, False, "MilestoneCasino_256_TownTimer_18", eTimerType.DELETE)
        t = Town.TerrainAt(Location(37,19))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
        t = Town.TerrainAt(Location(30,12))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])
        return
    MessageBox("A furious fight erupts, cheered on by the spectators. Some throw bottles and small rocks to infuriate the opponents. They all yell, howl and curse.\n\nUnfortunately, your champion is beaten soundly by its opponent. It finally collapses in a bloody pile, to the joy of some, and the chagrin of others. You bitterly renounce gambling.")
    MessageBox("The arena wardens clean the pit after the fight, and usher the surviving monster back into its cell. The troglodyte pit master announces a major fighting event coming up in a few minutes.")
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Vahnavoi_71": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Chitrach_130": Town.NPCList.Remove(npc)
    Timer(Town, 20, False, "MilestoneCasino_256_TownTimer_18", eTimerType.DELETE)
    t = Town.TerrainAt(Location(37,19))
    if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[148])
    elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(37,19), 0, TerrainRecord.UnderlayList[147])
    t = Town.TerrainAt(Location(30,12))
    if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[148])
    elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(30,12), 0, TerrainRecord.UnderlayList[147])

def MilestoneCasino_261_CreatureDeath30(p):
    if StuffDone["10_5"] >= 1:
        MessageBox("The battle is truly titanic, perhaps beyond any you have taken part in. You are glad you are yards away when the two behemoths bash at one another. Suddenly, one misjudges a blow. The other monster seizes the moment of imbalance and thrusts.\n\nStartled, the defeated adversary blinks, and topples to the ground. The crowd is hysterical, but no more than you. You joyfully gather handful by handful of coin from the grudging cashier, ignoring the envious stares from the losers.")
        Party.Gold += 2000
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "RingfighterGiant_202": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "CaptiveUnicorn_203": Town.NPCList.Remove(npc)
        MessageBox("You feel your magical powers seeping back into you.")
        for pc in Party.EachAlivePC():
            pc.SP+= 100
        return
    MessageBox("The battle is truly titanic, perhaps beyond any you have taken part in. You are glad you are yards away when the two behemoths bash at one another. Suddenly, one misjudges a blow. The other monster seizes the moment of imbalance and thrusts.\n\nStartled, its adversary blinks, and topples to the ground. The crowd is hysterical. You can restrain your joy. There is no money for you in this victory. You consider the cruelty of man in exploiting the suffering of others. No more gambling for you.")
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "RingfighterGiant_202": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "CaptiveUnicorn_203": Town.NPCList.Remove(npc)
    MessageBox("You feel your magical powers seeping back into you.")
    for pc in Party.EachAlivePC():
        pc.SP+= 100

def MilestoneCasino_262_CreatureDeath33(p):
    if StuffDone["10_4"] >= 1:
        MessageBox("The battle is truly titanic, perhaps beyond any you have taken part in. You are glad you are yards away when the two behemoths bash at one another. Suddenly, one misjudges a blow. The other monster seizes the moment of imbalance and thrusts.\n\nStartled, the defeated adversary blinks, and topples to the ground. The crowd is hysterical, but no more than you. You joyfully gather handful by handful of coin from the grudging cashier, ignoring the envious stares from the losers.")
        Party.Gold += 2000
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "RingfighterGiant_202": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "CaptiveUnicorn_203": Town.NPCList.Remove(npc)
        MessageBox("You feel your magical powers seeping back into you.")
        for pc in Party.EachAlivePC():
            pc.SP+= 100
        return
    MessageBox("The battle is truly titanic, perhaps beyond any you have taken part in. You are glad you are yards away when the two behemoths bash at one another. Suddenly, one misjudges a blow. The other monster seizes the moment of imbalance and thrusts.\n\nStartled, its adversary blinks, and topples to the ground. The crowd is hysterical. You can restrain your joy. There is no money for you in this victory. You consider the cruelty of man in exploiting the suffering of others. No more gambling for you.")
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "RingfighterGiant_202": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "CaptiveUnicorn_203": Town.NPCList.Remove(npc)
    MessageBox("You feel your magical powers seeping back into you.")
    for pc in Party.EachAlivePC():
        pc.SP+= 100

def MilestoneCasino_263_TalkingTrigger7(p):
    if StuffDone["10_6"] == 250:
        return
    StuffDone["10_6"] = 250
    SpecialItem.Give("Vampirebox")

def MilestoneCasino_264_TalkingTrigger8(p):
    if StuffDone["141_0"] >= 1:
        p.TalkingText = "\"Ah, you brought me my pet vampire! Thank you very much indeed. I?ll just have it resurrected, and my arena has a new champion. Here is your reward!\" He tosses you a large pouch of coins."
        if StuffDone["60_0"] == 250:
            return
        StuffDone["60_0"] = 250
        SpecialItem.Take("Fullvampirebox")
        Party.Gold += 700
        return

def MilestoneCasino_265_TalkingTrigger15(p):
    if StuffDone["10_8"] >= 1:
        p.TalkingText = "You drop the head of the gambler on the counter in disgust, and Rodovan Zerr laughs. \"Your reputation does you no justice! You truly are marvellous mercenaries!\n\n\"The Vahnatai is an arms dealer, offering his services to a very select and wealthy group of customers. He has set up shop in a cave in eastern Chimney.\" He gives you directions to a secret cave."
        TownMap.List["VahnataiCave_11"].Hidden = False
        return

def Talking_10_1(p):
    if Party.Gold >= 1000:
        Party.Gold -= 1000
        StuffDone["10_4"] = 1
        p.TalkingText = "\"One thousand gold on the mighty Giant Gorgh!\" you cry, and the crowd sighs in excitement. The Cashier bows to you and accepts your stake. \"Let the challenge commence!\" he booms."
    else:
        p.TalkingText = "You make a bold bid, but to your embarrassment, you cannot provide the gold requested."

def Talking_10_2(p):
    if Party.Gold >= 1000:
        Party.Gold -= 1000
        StuffDone["10_5"] = 1
        p.TalkingText = "\"We back the charms of the pure unicorn Alanna\" you cry, and the crowd sighs in excitement. The Cashier bows to you and accepts your stake. \"The challenge commences!\" he booms."
    else:
        p.TalkingText = "You make a bold bid, but to your embarrassment, you cannot provide the gold requested."
