
def Willow_0_MapTrigger_11_8(p):
    MessageBox("This bookshelf is filled with ledgers and notebooks, detailing the success of the crops in Willow. You notice that they\'re mostly shipped off to Selathni for export.")

def Willow_1_MapTrigger_12_8(p):
    MessageBox("Among the books of records on these shelves, you find an intriguing journal: \"Discipline Records.\" It describes the many serfs who have done time in the \"Discipline Cells,\" and the crimes that landed them there.\n\nThe most common crimes are poaching, hoarding food, and \"Being difficult.\" The stays tend to be 3 to 5 days long.")

def Willow_2_MapTrigger_6_37(p):
    if StuffDone["0_1"] == 250:
        return
    result = ChoiceBox("This book is quite thick and impressive. Each page is thick, high quality vellum, carefully and skillfully illuminated.", eDialogPic.TERRAIN, 130, ["Leave", "Read"])
    if result == 1:
        StuffDone["0_1"] = 250
        TownMap.List["Willow_0"].DeactivateTrigger(Location(6,37))
        MessageBox("Oh dear. You must have done something wrong. The moment you touch one of the pages, the book explodes. You are engulfed in a cloud of flame and burnt vellum.")
        Party.Damage(Maths.Rand(10, 1, 10) + 0, eDamageType.FIRE)
        Wait()
        return

def Willow_3_MapTrigger_41_30(p):
    if StuffDone["0_2"] == 250:
        return
    StuffDone["0_2"] = 250
    TownMap.List["Willow_0"].DeactivateTrigger(Location(41,30))
    MessageBox("As you enter Welde\'s bedroom, you have the unmistakable feeling that you\'re being watched.")

def Willow_4_MapTrigger_35_16(p):
    if StuffDone["0_3"] == 250:
        return
    StuffDone["0_3"] = 250
    TownMap.List["Willow_0"].DeactivateTrigger(Location(35,16))
    TownMap.List["Willow_0"].DeactivateTrigger(Location(35,14))
    MessageBox("As you enter the serfs\' barracks, you are assaulted by the twin sour smells of sweat and fatigue. Most families laboring under a lord are at least afforded a hut to call their own.\n\nMost of the workers of Willow are instead billeted in these cramped barracks. You can only hope they are given better accomodations soon.")

def Willow_6_MapTrigger_31_29(p):
    if StuffDone["0_4"] == 250:
        return
    StuffDone["0_4"] = 250
    TownMap.List["Willow_0"].DeactivateTrigger(Location(31,29))
    MessageBox("Willow\'s only silo, meant for the storage of grain, corn, and other bounties of the farm, is eerily empty and dusty. Nobody has kept much of anything here for a while.")

def Willow_7_MapTrigger_6_31(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(11,5)
    Party.MoveToMap(TownMap.List["BelowWillow_2"])

def Willow_8_OnEntry(p):
    if StuffDone["101_1"] >= 1:
        MessageBox("Unfortunately, news of your notoriety and criminal acts have reached the normally sleepy town of Willow. With a lusty shout, the guards raise the alarm.")
        Town.MakeTownHostile()
        return
    if StuffDone["0_0"] == 250:
        return
    StuffDone["0_0"] = 250
    MessageBox("You arrive at the sleepy farming village of Willow. Actually, sleepy isn\'t the right way to put it. Exhausted seems a much better word. Tired serfs mechanically farm rows of rich crops, as guards watch them carefully.\n\nAfter the richness of Selathni, Willow comes as a bit of a shock.")

def Willow_9_TalkingTrigger33(p):
    if StuffDone["0_5"] == 0:
        if StuffDone["0_5"] == 250:
            return
        StuffDone["0_5"] = 250
        p.TalkingText = "She removes a thick sheaf of papers from her leather jerkin. They\'re wrapped in leather, tied with twine, and sealed with wax. You won\'t need to be too careful about taking care of them.\n\n\"Take these papers to Zulli in Zaskiva. I\'m sure he\'ll give you a reward.\" She gives you a quick hug. \"And thank you!\""
        SpecialItem.Give("LetterforZulli")
        return
    if StuffDone["0_6"] == 0:
        p.TalkingText = "\"Have you delivered my letters yet?\" You answer in the negative. \"Please try! It is so important I get a message to him before something terrible happens with the rebels.\""
        return
