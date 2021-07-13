
def Myldres_121_MapTrigger_28_51(p):
    if StuffDone["6_0"] >= 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("The perimeter walkway slopes upwards, rising above town level at this point. Two guards salute you, making it clear that you are allowed into the royal levels further up the spiralling walkway.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(24,43)
        Party.MoveToMap(TownMap.List["RoyalSector_8"])
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The guards on both sides of the stairway drop their halberds to block your passage. Access to this level is granted only to those especially invited.")

def Myldres_123_MapTrigger_37_28(p):
    if StuffDone["6_0"] >= 1:
        Town.PlaceEncounterGroup(1)
        if StuffDone["6_1"] == 250:
            return
        StuffDone["6_1"] = 250
        ChoiceBox("When you enter the central square, you find it buzzing with excitement. Crowds are gathering around a few people bringing shocking news. You can guess. The rumours of the slith cult in Brattaskar have finally reached the capital.\n\nFrightened people discuss the attack and its meaning, when somebody notices you and raises a shout. \"The heroes of Brattaskar!\" Suddenly, everyone surges towards you, wanting to touch you, congratulate you or to talk to you.\n\nBlushing from embarrassment in the middle of the crowd, you realize that you might have to get used to being a celebrity from now on, as everyone hears the story of how you disarmed Thunder Rock and saved Chimney from isolation.\n\nYou notice Spencer, the landlord of the Anguished Maiden, struggling to reach through to you. You wave to him, and an opening appears. The prisoners from Brattaskar have arrived! They got in this morning, and brought the news of your feat with them.\n\n\"We?ve moved in with the Hands of the Watcher. Come see us when this has settled down!\" is all Spencer manages to say over the crowd. For then a messenger appears, asking you to visit Mayor Ottar up in the royal sector.\n\n(Certain people may be more friendly towards you from now on.)", eDialogPic.CREATURE, 1, ["OK"])
        return

def Myldres_124_MapTrigger_14_9(p):
    MessageBox("You enter the busy temple of the Hands of the Watcher. No mass is going on at the moment, so the main room is used as work space and administration centre for a dozen novices and guests coming and going. The high priestess is trying to control the bustle.")

def Myldres_133_MapTrigger_43_6(p):
    if StuffDone["6_0"] >= 1:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        if ChoiceBox("The slith guards salute you and show by gestures that you are allowed to descend into the slith warren to speak to the slith leader.", eDialogPic.STANDARD, 0, ["Yes", "No"]) == 1:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(35,16)
        Party.MoveToMap(TownMap.List["SlithEmbassy_7"])
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The guards on both sides of the stairway drop their halberds to block your passage. Access to this level is granted only to those especially invited.")

def Myldres_134_MapTrigger_22_14(p):
    if StuffDone["6_0"] >= 1:
        if StuffDone["200_0"] >= 1:
            if StuffDone["6_6"] == 250:
                return
            StuffDone["6_6"] = 250
            ChoiceBox("You enter the quarters of the Brattaskar prisoners and once again are greeted warmly. At the moment, however they must manage without the healing powers of Karolynna. She has gone south, Spencer tells you soberly.\n\nHe hands you a letter. Seeing Karolynna?s seal, you tear it open and read:\n\n\"Dear friends! Something is very wrong in Flickering Keep. I cannot tell you now what is amiss, but if my suspicions are right, this may be very important to the outcome of this war.\n\n\"I go there at once to speak to Lady Fray, mistress of Flickering Keep. I might need help in this matter, I?m not sure what I?ll find there. So please follow me, join me at Flickering Keep!    -Karolynna.\"\n\nThe people of the Shadowlands, around Flickering Keep in southern Chimney, are considered very odd. It is a remote place, even by the standards of Chimney, and the people have little in common with the rest of the human lands.\n\nIf Karolynna is on her own there, you owe her all your help.", eDialogPic.CREATURE, 132, ["OK"])
            return
        if StuffDone["6_5"] == 250:
            return
        StuffDone["6_5"] = 250
        MessageBox("Karolynna and the others from Howling Gap have arrived! Cheers and warm embraces abound, restoring your confidence and sense of purpose. The prisoners are recovering well under the care of Karolynna.")
        return

def Myldres_136_MapTrigger_26_35(p):
    if StuffDone["7_0"] >= 1:
        if StuffDone["6_2"] == 250:
            return
        StuffDone["6_2"] = 250
        ChoiceBox("The Town Square is once again humming with rumours. You keep your heads down and try not to get caught up in the crowd, for you can guess what is happening. You make your way over the bridge into the Cliff, hoping to find Oterel.\n\nThe table is empty. The maitre d? comes over, his smile more friendly now that you are an acquaintance of the Mayor?s son. \"Sir Oterel had to go, but he left this letter for you, my lords.\"\n\nYou grimly tear the seal open and read:\n\n\"My compliments, dear friends, for the way you helped the slith revolution. Lodark and I placed a bet on your fate. He thought you would die in the slith gutter. A double victory for me! The new ambassador might look kindly to me for this assistance.\n\n\"A word of warning: It might be wise not to tell anyone of your involvement in this affair. You might lose your general standing as public heroes!\n\n\"I promised you a reward, and I am true to my word. You shall have a grand prize for your efforts. Ask Sultara the shoe seller about `credit?, and you shall see. Yours sincerely, Oterel.\"", eDialogPic.CREATURE, 31, ["OK"])
        return
        return

def Myldres_140_MapTrigger_16_54(p):
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
    pc.RunTrap(eTrapType.DART, 1, 30)

def Myldres_142_OnEntry(p):
    if StuffDone["6_0"] >= 1:
        return
    Timer(None, 500, False,  "ScenarioTimer_x_598")

def Myldres_143_TalkingTrigger12(p):
    if StuffDone["6_4"] == 250:
        return
    StuffDone["6_4"] = 250
    SpecialItem.Give("Minekey")

def Myldres_144_TalkingTrigger19(p):
    if StuffDone["6_3"] == 250:
        return
    StuffDone["6_3"] = 250
    Party.GiveNewItem("BootsofSpeed_235")

def Myldres_145_TalkingTrigger48(p):
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_cure_all_poison")

def Talking_6_40(p):
    if Party.Gold < 0:
        p.TalkingText = ""
    else:
        Party.Gold -= 0
        Party.Pos = Location(11, 21)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "She leads you down the hall and opens a large room. She explains that the common room is full, so she lets you have her own. You protest, but she fends you off. \"You said you needed the rest. Make the best use of it.\""
        CentreView(Party.Pos, False)
