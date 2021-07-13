def Initialise_Scenario():
    pass

def Intro_Message(p):
    ChoiceBox("Times are tough for adventurers in Valorim, supposedly the wildest and most unsettled of the Empire\'s continents. The monsters have been subdued, the treasure has been claimed, and there\'s little for you to do.\n\nThat\'s why, when you were contacted by an Empire agent and told of jobs for you on a place called Morrow\'s Isle, you jumped at the chance. However, the agent was rather vague about the nature of the problem.\n\nThere are supposedly brigands there, or bandits, or some other sort of evil human determined to cause trouble and mayhem. Your job will be to track down and slay them, or something similar.\n\nAt any rate, it\'s paying work, so you decide to go there and see what\'s going on. Two weeks travel over land and several hours on a boat later, you have been deposited on a dock in Selathni, the largest city on Morrow\'s Isle.\n\nYou have a letter of introduction in your pocket. You\'re supposed to go see a man named Vonnegut, in the Sea Wurm inn, near the dock. He will explain more of what\'s going on, and give you your official orders.\n\nAfter months of scraping out a living, you start to get excited. At last, you can go out, have adventures, and fight evil!", eDialogPic.SCENARIO, 28, ["OK"])

def Town_Pre_Entry(town):
    if town.Num==17:
        return TownMap.List[town.Num + StuffDone["15_1"]]
    return town


def Zaskiva_75_GlobalTalkingTrigger_14(p):
    Town.AlterTerrain(Location(34,12), 0, TerrainRecord.UnderlayList[125])

def On_Using_SI_OakBox_493(p):
    MessageBox("You try everything to get it open: force, lockpicks, even greater force, spells, even hitting it with a hammer. Nothing works. It stays stubbornly closed.")

def On_Using_SI_SmallOakBox_494(p):
    MessageBox("When you reach a place where this item can be used, you will be asked if you want to use it.")

def ScenarioTimer_x_496(p):
    MessageBox("The witches\' curse suddenly falls full force upon your heads. Warts start appearing all over your bodies, and you feel dull witted.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 8))
    for pc in Party.EachAlivePC():
        pc.AwardXP(-50)
