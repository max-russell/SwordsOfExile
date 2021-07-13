
def ZenithKeep_577_MapTrigger_31_57(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(32,8)
    Party.MoveToMap(TownMap.List["Zenith_28"])

def ZenithKeep_580_MapTrigger_50_19(p):
    if StuffDone["17_2"] == 250:
        return
    StuffDone["17_2"] = 250
    TownMap.List["ZenithKeep_30"].DeactivateTrigger(Location(50,19))
    StuffDone["100_0"] = 4
    Animation_Hold(-1, 075_cold)
    Wait()
    ChoiceBox("CHAPTER IV -- THE HARVEST", eDialogPic.STANDARD, 29, ["OK"])

def ZenithKeep_581_MapTrigger_25_21(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,23)
    Party.MoveToMap(TownMap.List["BeneathZenithKeep_48"])

def ZenithKeep_596_TalkingTrigger1(p):
    ChoiceBox("\"Our findings indicate that Auspire, her daughter Cylene, and her son Sirius, are all missing. We presume they perished in the fall of Fort Nether, but that cannot be proven.\n\nSince this time, there has been much dispute as to who will be the next ruler of the order of Odin. It appears the Stolgradian authority will survive, much to my dislike, but will be weaker.\n\nWe are simply here making sure that an all out war doesn\'t break out between the multiple factions vying for the throne. Thus far, we have been successful at keeping the peace.\n\nBy and large, you will find the Stolgradian system working much as it did earlier. The fall of Auspire does not fundamentally change policy, much to my dislike. The peasants are still treated harshly in the labor camps.\n\nIt\'s business as usual here in Stolgrad, or as much as it can be in the wake of the power shift. Anyway, I thought I would give you the heads up on what\'s going on.\"", eDialogPic.STANDARD, 17, ["OK"])
