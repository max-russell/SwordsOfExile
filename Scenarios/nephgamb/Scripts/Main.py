def Initialise_Scenario():
    pass

def Intro_Message(p):
    ChoiceBox("The lands of Chimney know well the advantages of being remote: The great events that stagger the rest of the world, -Wars, discoveries and diplomatic intrigue- pass Chimney gently by.\n\nDeep down in the lower caves, on the very rim of the slithzerikai realms, far away from the Empire and even from the central Exile government, Chimney is largely unknown to the world. And of those who do know, most people do not care.\n\nChimney lives by mining and selling metal to the the slithzerikai, in exchange for herbs from the lizard jungles. This sustains a modest trade with Formello, the nearest Exile town.\n\nYour own place in the world is just as modest. As new soldiers guarding an old fort on the Formello trade route, you quickly fall into the daily routine.\n\nShort patrols, dice games and endless conversations with the other soldiers in the garrison are only rarely interrupted by a visiting trader.\n\nOn this morning your lives and the destiny of all Chimney are about to change forever. For better or for worse? That remains to be seen.", eDialogPic.SCENARIO, 20, ["OK"])


def On_Using_SI_Magictome_595(p):
    MessageBox("You open the book and start reading. As you do, the gold letters start to disappear! You only get one chance to learn what is in this book, for the text disappears once you have read it. You concentrate deeply and repeat the lines among yourselves.\n\nBy the time the pages of the book are all empty, you have learned the complicated spell Major Haste.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_major_haste")
    SpecialItem.Take("Magictome")

def ScenarioTimer_x_596(p):
    if StuffDone["201_1"] == 250:
        return
    StuffDone["201_1"] = 250
    ChoiceBox("Once again, you all receive a mental message. Images flood your minds as you behold a scene north of Lushwater Toll, where the army of Chimney has arrived from Myldres. Captain Locke is leading the column towards Howling Gap.\n\nThe countryside is deadly quiet as the army struggles over the broken terrain. Only the clinking of metal and snorts from horses and  freight lizards can be heard. You sense that something is wrong.\n\nThe rocks, you suddenly realize, the towering boulders that are piled on the hills bordering the road! From your birds eye perspective you see that they are artificially stacked on top of one another so that they almost topple down on the road.\n\nYou cry out in warning, but no one hears your spirit voices, no one sees the lizard men scuttling behind the ridges.\n\nYou cry, but in vain. Without warning, boulders crash into the caravan, crushing, separating, confusing the human soldiers. Then the hills are lined with sliths, raining fire and bronze spears into the disordered column.\n\n\"The human army is beaten. We are open to invasion,\" a voice booms over the battle. \"Chimney is in desperate need of help. Come see me at my fortress.\" You recognize the voice. Commander Groul has decided to enter the game over Chimney.", eDialogPic.CREATURE, 1024, ["OK"])
    StuffDone["17_7"] = 1
    StuffDone["220_0"] = 1
    StuffDone["201_0"] = 1

def ScenarioTimer_x_597(p):
    if StuffDone["200_1"] == 250:
        return
    StuffDone["200_1"] = 250
    ChoiceBox("Without warning, you all find yourselves thinking about Karolynna, the brave priestess you met in Howling Gap. Is she well? You all get an urge to go to Myldres and see her.\n\nWhen you find out that you all share the same impulse, you understand that you have been given a telepathic message. You start discussing how you can get to Myldres as soon as possible.", eDialogPic.CREATURE, 132, ["OK"])
    StuffDone["221_0"] = 1
    StuffDone["200_0"] = 1

def ScenarioTimer_x_598(p):
    StuffDone["6_0"] = 1
    if Game.Mode != eMode.OUTSIDE and Town.Num == 6:
        if StuffDone["6_7"] == 250:
            return
        StuffDone["6_7"] = 250
        MessageBox("Echoing down the streets of Myldres, you hear the sound of commotion in the city square. You wonder what is going on and decide to investigate at first opportunity.")
        return

def GlobalCall_RoyalSector_599(p):
    MessageBox("SURVIVAL!                                             You survived the war over Chimney. But you failed to make your way into the circle of powerful rulers of the country. After a brief period as celebrities you return to life as ordinary citizens.\n\nAs Groul might have said: Fate can offer you the opportunity to succeed. But that inevitably comes to nothing if you do not also have the skill and courage to seize the opportunity and force the world to do your bidding.               -THE END")
    Scenario.End()

def GlobalCall_BelowWhitstone_601(p):
    if StuffDone["213_1"] >= 2:
        if StuffDone["215_0"] >= 1:
            Timer(None, 50, False,  "ScenarioTimer_x_596")
            return
        Timer(None, 50, False,  "ScenarioTimer_x_597")
        return
