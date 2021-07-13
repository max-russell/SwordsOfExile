
def UnderBuzzard_161_MapTrigger_24_21(p):
    if StuffDone["13_0"] == 250:
        return
    StuffDone["13_0"] = 250
    TownMap.List["UnderBuzzard_13"].DeactivateTrigger(Location(24,21))
    MessageBox("Back when the rebels were still underground, this was where a good number of them hid out. To the south, you see pallets on the floor. To the north are a number of storage boxes.\n\nNow that it isn\'t needed, these chambers are cold, dark, and empty, with one exception. You see a dim red glow down the passage to the northwest.")

def UnderBuzzard_162_MapTrigger_21_14(p):
    if StuffDone["101_0"] >= 1:
        Town.AlterTerrain(Location(14,10), 0, TerrainRecord.UnderlayList[148])
        return

def UnderBuzzard_163_MapTrigger_11_10(p):
    result = ChoiceBox("All of this seems rather familiar. Eerily familiar, in fact. It\'s a dim underground room, with a large throne set in the middle of it, facing a wall.", eDialogPic.TERRAIN, 161, ["Leave", "Sit"])
    if result == 1:
        if StuffDone["101_3"] >= 1:
            if StuffDone["101_5"] >= 1:
                ChoiceBox("The lights dim, and the voice speaks. \"You have done well. While we suspected you were working for the Empire, our suspicions have been alleviated. With the outpost you attacked gone, our operations can expand to the south.\"\n\n\"I wish to meet you personally, to speak with you and reward you. Come to me. Leave Buzzard, and follow the mountain path to the east (or north). You will arrive at my fortress before long.\"\n\n\"I eagerly await your presence. That is all.\" The lights return.", eDialogPic.TERRAIN, 161, ["OK"])
                StuffDone["101_9"] = 1
                return
            if StuffDone["101_7"] >= 1:
                ChoiceBox("You sit, and the voice says \"As you do not wish to assault the outpost to the southeast, as we said before, we will grant you an audience with Stalker. First, leave these mountains.\"\n\n\"Go to the southeast side of the mountains, and follow the path up along the sea. From there, the path to Stalker will be made clear.\"", eDialogPic.TERRAIN, 161, ["OK"])
                return
            if StuffDone["101_4"] >= 1:
                result = ChoiceBox("You sit, and the lights dim. The voice says \"You have returned. You have not yet gone to the Empire outpost burrowed into the outside of our mountain chain to the southeast. You have not killed their commander.\"\n\n\"Are you having difficulties? Do you have any questions?\" Your Empire superiors told you that you should insist on being taken to meet Stalker first. Do you?", eDialogPic.TERRAIN, 161, ["No", "Yes"])
                if result == 0:
                    MessageBox("You say you have no questions. The voice says \"Fine then. Time is always short. Go now, and complete your mission.\" You stand, and the lights rise.")
                    return
                elif result == 1:
                    StuffDone["101_7"] = 1
                    ChoiceBox("You say \"We will do what you ask, but only if we can be sure you are who you say you are. We\'ll only do it if we can meet Stalker first.\"\n\nThere is a long pause. You sit nervously in the shadow, waiting. Finally, the voice speaks.\n\n\"Very well. This is unusual, but, considering the exceptionality of your aid so far, it can be allowed. There is a back entrance to Stalker\'s Fortress. We will direct you there.\"\n\n\"Leave this mountain range. Go to the east, to where the mountains meet the sea, and walk north along the path between mountains and sea. From there, the way to Stalker will be made clear to you.\"\n\n\"Remember - a great trust is being placed upon you. In the name of justice, to not betray it. That is all.\" The lights go up again.", eDialogPic.TERRAIN, 161, ["OK"])
                    return
                return
            ChoiceBox("When you sit in the throne, the light from the braziers dims, and a voice speaks. The voice is softer and more natural than the voice in the chamber under Willow, but still has a disjointed, recorded quality.\n\n\"Hello, adventurers. I am Stalker, leader of the Hill Runners, planner of our just war against the Empire. You have done great good for us so far. One more test, and we will truly let you into our inner circle.\"\n\n\"In the south side of these mountains, to the southeast, there is a hidden Empire fort. It is well defended, and we have had trouble infiltrating it. We believe that you can succeed.\"\n\n\"Go there, break in, and kill the Empire commander there, and we will be convinced of your loyalty to our cause. We will bring you in, and give you power in our organization.\"\n\n\"When you have completed this mission, or should you have other questions, return here. That is all.\" The speech ends, and the lights rise.", eDialogPic.TERRAIN, 161, ["OK"])
            TownMap.List["EmpireOutpost_15"].Hidden = False
            return
        StuffDone["101_3"] = 1
        ChoiceBox("When you sit in the throne, the light from the braziers dims, and a voice speaks. The voice is softer and more natural than the voice in the chamber under Willow, but still has a disjointed, recorded quality.\n\n\"Hello, adventurers. I am Stalker, leader of the Hill Runners, planner of our just war against the Empire. You have done great good for us so far. One more test, and we will truly let you into our inner circle.\"\n\n\"In the south side of these mountains, to the southeast, there is a hidden Empire fort. It is well defended, and we have had trouble infiltrating it. We believe that you can succeed.\"\n\n\"Go there, break in, and kill the Empire commander there, and we will be convinced of your loyalty to our cause. We will bring you in, and give you power in our organization.\"\n\n\"When you have completed this mission, or should you have other questions, return here. That is all.\" The speech ends, and the lights rise.", eDialogPic.TERRAIN, 161, ["OK"])
        TownMap.List["EmpireOutpost_15"].Hidden = False
        return

def UnderBuzzard_164_MapTrigger_27_27(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(27,21)
    Party.MoveToMap(TownMap.List["Buzzard_12"])
