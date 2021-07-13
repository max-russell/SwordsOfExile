
def FelineFrontier_412_MapTrigger_8_51(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(8,36)
    Party.MoveToMap(TownMap.List["YvosstaiCamp_15"])

def FelineFrontier_413_MapTrigger_11_53(p):
    MessageBox("No matter how much force you put into opening the door, you cannot budge it. It might be magically protected.")

def FelineFrontier_414_MapTrigger_16_58(p):
    if StuffDone["15_5"] >= 1:
        if StuffDone["17_1"] == 250:
            return
        StuffDone["17_1"] = 250
        MessageBox("You pass through an invisible crack in the cave wall. Now that you know where it is, you feel certain you can find it again.")
        return
    if StuffDone["17_0"] >= 1:
        if StuffDone["17_1"] == 250:
            return
        StuffDone["17_1"] = 250
        MessageBox("You pass through an invisible crack in the cave wall. Now that you know where it is, you feel certain you can find it again.")
        return
    p.CancelAction = True

def FelineFrontier_415_MapTrigger_42_50(p):
    if StuffDone["17_2"] == 250:
        return
    StuffDone["17_2"] = 250
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(42,50))
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(42,51))
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(42,49))
    MessageBox("The inn is nearly deserted. The mood is one of expatriates clinging together to protect their identity from all foreign influence. When you (who are clearly of human culture) enter, you get approving nods and smiles from the patrons and innkeep.")

def FelineFrontier_418_MapTrigger_50_17(p):
    if StuffDone["17_3"] == 250:
        return
    StuffDone["17_3"] = 250
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(50,17))
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(51,17))
    MessageBox("The air in this small, crowded cave is stuffy and smells of sweat and filth. It is crammed full of nephilim. Most are skinny and weak. They have few or no possessions and many are diseased. The sight of these fugitives makes it hard to see them as enemies")

def FelineFrontier_420_MapTrigger_16_12(p):
    if StuffDone["17_4"] == 250:
        return
    StuffDone["17_4"] = 250
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(16,12))
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(16,11))
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(16,13))
    MessageBox("This must be where the Cat Paw shamans practice throwing fireballs. You notice that the target dummies are shaped as humans and sliths.")

def FelineFrontier_423_MapTrigger_12_43(p):
    if StuffDone["17_5"] == 250:
        return
    StuffDone["17_5"] = 250
    TownMap.List["FelineFrontier_17"].DeactivateTrigger(Location(12,43))
    MessageBox("Carefully closing the revolving bookshelf behind you, you descend a set of narrow stairs into darkness. You try to be as quiet as possible as you stumble down. Being found in here would not be good for your reputation.")

def FelineFrontier_424_MapTrigger_15_54(p):
    if StuffDone["15_4"] >= 1:
        if StuffDone["17_9"] == 250:
            return
        StuffDone["17_9"] = 250
        ChoiceBox("The table is laden with clothes and robes. Your hands are trembling with apprehension as you look through the clothes. If your sense of direction isn?t completely befuddled, this is an antechamber to the portal into the slith lands.\n\nThe portal used by the Masked Aide when he visits his servant, Sss-Chross of the Yvoss-tai.\n\nYou recognize the robe at once when you uncover it. The robe of the man posing as Zahr, God of True Warriors. Commander Groul.\n\nYour heads spin as you take in this new information and try to understand. Groul, Commander of Chimney, is the true leader of the slith rebels. He must have suggested that the Yvoss-tai attack Chimney. Sss-Chross would never have thought of it himself.\n\n\"Why?\" you ask one another. Why would he attack his own country? You are beginning to understand that Groul is not the generous protector of Chimney he appears to be. But there is still much you do not know.\n\nZahr?s robe is important evidence against Groul if you ever choose to oppose him. You put it in your packs, storaging it for the right moment.", eDialogPic.STANDARD, 1024, ["OK"])
        if StuffDone["214_0"] == 250:
            return
        StuffDone["214_0"] = 250
        SpecialItem.Give("ZahrsRobe")
        for pc in Party.EachAlivePC():
            pc.AwardXP(20)
        StuffDone["213_1"] += 1
        if StuffDone["213_1"] == 250:
            pass
        RunScript("GlobalCall_BelowWhitstone_601", ScriptParameters(eCallOrigin.CUSTOM))
        if StuffDone["17_1"] == 250:
            return
        StuffDone["17_1"] = 250
        MessageBox("You pass through an invisible crack in the cave wall. Now that you know where it is, you feel certain you can find it again.")
        return
    MessageBox("Various pieces of clothing are stacked neatly on the table. You sort through them, expecting something highly magical or valuable in a place like this. You are disappointed.")

def FelineFrontier_425_MapTrigger_42_33(p):
    if SpecialItem.PartyHas("Archivekey"):
        t = Town.TerrainAt(Location(43,33))
        if t.InGroup("Unlockable"):
            t = Town.TerrainAt(Location(43,33)).TransformTo
            Town.AlterTerrain(Location(43,33), 0, t)
        if StuffDone["17_6"] == 250:
            return
        StuffDone["17_6"] = 250
        MessageBox("The librarian?s key opens the archive, releasing dusty air. The public records lie open before you.")
        return

def FelineFrontier_426_MapTrigger_48_30(p):
    MessageBox("Road maintenance. Chicken import taxes. Lizard sickness vaccine costs. Public servant salaries. Town square fountain permits. Last year?s sheep count. Bridge toll income. Everything has been carefully recorded and for some reason brought here.")

def FelineFrontier_437_MapTrigger_50_34(p):
    if StuffDone["11_0"] >= 1:
        if StuffDone["67_0"] == 250:
            return
        StuffDone["67_0"] = 250
        ChoiceBox("Two of you guard the door while the rest look through the endless rows of public records. You probably are more alert than anyone who has read the records in a long time. If your suspicions are right, you are in great danger here.\n\nFew know what is hidden here. The Keeper of Records knew, and the knowledge killed him. You reach the accounts for the last year, and find just what you were looking for.\n\nA bill of sale. There had to be some record of such a substantial transaction. And when you heard that the records in Myldres had been moved, your suspicions grew. You were right.\n\nVerundis got 10.000 gold pieces for the Thunder Rock, delivery included. The bill describes how he is to leave the artifact on a spot in Howling Gap, where the Yvoss-tai can find it. The document is signed by Verundis and Commander Groul.\n\nGroul gave the invaders the means to close Brattaskar Pass! Why? Why would he want to deliver you into the hands of the enemy?\n\nYou are more confused than ever. You put the bill of sale in a safe place in your packs before you leave. This may prove very important some day.", eDialogPic.STANDARD, 1024, ["OK"])
        if StuffDone["213_0"] == 250:
            return
        StuffDone["213_0"] = 250
        SpecialItem.Give("BillofSale")
        for pc in Party.EachAlivePC():
            pc.AwardXP(20)
        StuffDone["213_1"] += 1
        if StuffDone["213_1"] == 250:
            pass
        RunScript("GlobalCall_BelowWhitstone_601", ScriptParameters(eCallOrigin.CUSTOM))
        if StuffDone["17_1"] == 250:
            return
        StuffDone["17_1"] = 250
        MessageBox("You pass through an invisible crack in the cave wall. Now that you know where it is, you feel certain you can find it again.")
        return
    MessageBox("Road maintenance. Chicken import taxes. Lizard sickness vaccine costs. Public servant salaries. Town square fountain permits. Last year?s sheep count. Bridge toll income. Everything has been carefully recorded and for some reason brought here.")

def FelineFrontier_438_MapTrigger_44_30(p):
    MessageBox("An old spell book has been misfiled among clerical birth records from Myldres. You don?t mind. Instead, you set about reading the spell formula. You learn the mage spell `Venom Arrows?.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_venom_arrows")

def FelineFrontier_439_MapTrigger_46_36(p):
    MessageBox("A prayer book has been left on this shelf. With eager hands, your priest spell casters grab the book and start learning the mantras to trigger the spell `Bless Party?.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_bless_party")

def FelineFrontier_440_SanctifyTrigger_55_26(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["17_8"] == 250:
        return
    StuffDone["17_8"] = 250
    MessageBox("You cast the exhausting Ritual of Sanctification on the sick nephil. His body starts shaking, and his arms and legs wave in the air. His mouth opens and a gray mist seeps out. \"Hah!\" the shaman cries, and blows at the smoke, dispersing it.\n\n\"Thank you,\" the shaman says. \"I hope you learn from this that helping and cooperation is always better than force.\" In return for your help, he teaches you a priest spell, `Mass Sanctuary?.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_mass_sanctuary")

def FelineFrontier_441_MapTrigger_13_30(p):
    if StuffDone["201_0"] >= 1:
        if StuffDone["67_1"] == 250:
            return
        StuffDone["67_1"] = 250
        ChoiceBox("You enter the chamber of Commander Groul. The nephil leader was apparently waiting for you, for when you enter, he springs to his feet to lead you to the long council table.\n\n\"The army of Chimney has been beaten! The humans are driven back towards Lushwater Toll with great losses. My sources tell me that Sss-Chross is preparing for the final campaign to take Chimney and the bronze works.\n\n\"I had intended to stay out of this war, and to let Mayor Ottar try out his own military tactics. But I cannot stand aside and watch the lizard men ruin all I have built. Which is why I thought of you.\n\n\"If half the stories people tell of you are true, you should be up to this task as well. Sss-Chross is planning the invasion with his captains in the Yvoss-tai camp below the Dividing Wall. If we strike at him there, his army will be crippled.\n\n\"It may not halt the invasion, but it is the best we can do at the moment. After you have killed Sss-Chross, find the slith corridor that leads into Howling Gap. It is their supply route, and should open into our lands near the remains of the human army.\n\n\"Join them there, and I will do what I can in the mean time. For this mission, I have created a magic portal that will take you into the slith camp. A secret passage follows the edge of the chasm to the south into the portal cave. Hurry, and good luck!\"", eDialogPic.CREATURE, 1024, ["OK"])
        StuffDone["17_0"] = 1
        ChoiceBox("PART 3: Nephil?s Gambit", eDialogPic.STANDARD, 6, ["OK"])
        return

def FelineFrontier_443_MapTrigger_8_32(p):
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
    pc.RunTrap(eTrapType.EXPLOSION, 2, 40)

def FelineFrontier_444_ExitTown(p):
    if p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(13, 10),WorldMap.SectorAt(Party.OutsidePos))
    if p.Dir.IsEast:
        MessageBox("What makes this fortress impregnable is its route of access. The road follows a narrow, winding track with several blind ends. You are entirely dependent upon your nephil guides to find your way in or out.\n\nYou ask them very nicely to remember your faces. Without the help of the guides you cannot enter the fortress. They assure you with a smirk that of course they remember you.")
        StuffDone["17_7"] = 1

def Talking_17_5(p):
    if Party.Gold >= 10:
        Party.Gold -= 10
        p.TalkingText = "You order, and savour the memories of Home. The inn keeper goes on telling you his opinion of the \"foreigners\", meaning the nephilim. \"And there are so few of us. After the librarian left, there?s almost only me left of the proper people.\""
    else:
        p.TalkingText = "\"Oh, I forgot to mention, my prices are high. But it?s worth it, I assure you. A real taste of Home!\""
