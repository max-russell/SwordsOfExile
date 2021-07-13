
def BelowWillow_25_MapTrigger_7_14(p):
    if StuffDone["2_0"] == 250:
        return
    StuffDone["2_0"] = 250
    TownMap.List["BelowWillow_2"].DeactivateTrigger(Location(7,14))
    MessageBox("You reach the questioning chamber. It\'s an eerie room, bare except for dim, flickering torches on the walls, and a gilt throne in the center of the room. It\'s empty, and you suspect you may be supposed to be sitting in it.")

def BelowWillow_26_MapTrigger_10_14(p):
    result = ChoiceBox("The throne is large, and you could sit in it comfortably. There\'s even a small velvet cushion. What happens after you sit, that may be another story ...", eDialogPic.TERRAIN, 144, ["Leave", "Sit"])
    if result == 1:
        if StuffDone["101_7"] >= 1:
            ChoiceBox("You sit in the throne, the room darkens, and the calm voice asks \"Well? Have they agreed to take you to Stalker?\" You say what happened under Buzzard.\n\nThe voice definitely sounds enthusiastic. \"Excellent! At last, we have them! At last, we can seize and slay this foul creature in our midst!\"\n\n\"Follow the instructions given to you under Buzzard as soon as possible, find out where Stalker\'s lair is, and report to us as soon as possible. Your rewards will be lavish.\" The room brightens up again. End of session.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["101_8"] = 1
            return
        if StuffDone["101_3"] >= 1:
            if StuffDone["100_9"] >= 1:
                ChoiceBox("The room darkens, and you hear a single word: \"Report.\" You tell of the meeting under Buzzard, and of the mission to kill the Empire soldiers.\n\nThere is a pause, and the voice says \"This is as we suspected. After the last atrocity, it was only natural you would be asked to raise the stakes. Since they gave you this mission, they must have a great deal of trust for you.\"\n\n\"You must not perform this mission. Slaying Empire soldiers will not be tolerated. Do not do it, at any cost. Instead, you are to return to Buzzard.\"\n\n\"Tell them that you will do this mission, but only if you can meet Stalker first. Tell them this is the only condition. Considering the trust they have shown you, they will surely agree, and once you report his location back to us, we will have him!\"\n\n\"That is all.\" The room brightens.", eDialogPic.TERRAIN, 144, ["OK"])
                StuffDone["101_4"] = 1
                return
            ChoiceBox("You sit in the throne, and the lights darken. The voice begins to speak, but it is cold and grim.\n\n\"Did we not say that you must consult with us before doing any missions? Did we not say everything must be cleared? Now we see the results of your willful ignorance. Lord Volpe is dead, and you are responsible.\"\n\n\"We have considered forgiving you for your crime. Alas, it would not present a good picture to others working for us. Your failure must be a glorious example, teaching others the importance of following orders.\"\n\n\"We suggest running. There will be no succor for you here. Only death. Thank you for your help. Good luck.\" The room brightens again.\n\nThat didn\'t bode well.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["101_1"] = 1
            return
        if StuffDone["101_0"] >= 1:
            if StuffDone["100_9"] >= 1:
                ChoiceBox("You sit, and the voice returns. It sounds grim. \"Well, Stalker got us there. You were not the agents for blowing up Lord Volpe\'s mansion, but you unwittingly made it possible. Now Volpe is dead.\"\n\n\"There is only one silver lining in this incredible disaster. Now, the Hill Runners will trust you for sure. Have they given you any orders?\" You say how you were told to contact Luna, in Buzzard.\n\n\"Excellent. This is our chance. We will make them pay double for what they have done to us. Go there immediately, and be sure to report to us what they tell you to do. We may be getting close to reaching them.\"\n\n\"That is all.\" The room brightens.", eDialogPic.TERRAIN, 144, ["OK"])
                StuffDone["101_2"] = 1
                return
            ChoiceBox("You sit in the throne, and the lights darken. The voice begins to speak, but it is cold and grim.\n\n\"Did we not say that you must consult with us before doing any missions? Did we not say everything must be cleared? Now we see the results of your willful ignorance. Lord Volpe is dead, and you are responsible.\"\n\n\"We have considered forgiving you for your crime. Alas, it would not present a good picture to others working for us. Your failure must be a glorious example, teaching others the importance of following orders.\"\n\n\"We suggest running. There will be no succor for you here. Only death. Thank you for your help. Good luck.\" The room brightens again.\n\nThat didn\'t bode well.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["101_1"] = 1
            return
        if StuffDone["100_8"] >= 1:
            if StuffDone["100_7"] >= 1:
                ChoiceBox("You settle in the throne again, and the light dims. \"Things are progressing well. You have done one mission for them, and given them nothing. Now, they are giving you some sort of simple courier task.\"\n\n\"By all means, recover the box and take it where they say. The path to Zaskiva will be clear to you. Once this is done, they will again have gained little, and they will trust you more.\"\n\n\"Soon, they will tell you the path to Stalker, and we will have them! Go. Go now.\" The light returns.", eDialogPic.TERRAIN, 144, ["OK"])
                StuffDone["100_9"] = 1
                return
            MessageBox("You sit in the throne. It shocks you! You jump up again. The voice says \"You returned the papers to the Hill Runners without clearing it with us. That was not right.\"\n\n\"You should not eat, not think, not even breathe without returning to consult with us. Now wipe those hurt puppy dog expressions off your faces and sit down.\"")
            ChoiceBox("You settle in the throne again, and the light dims. \"Things are progressing well. You have done one mission for them, and given them nothing. Now, they are giving you some sort of simple courier task.\"\n\n\"By all means, recover the box and take it where they say. The path to Zaskiva will be clear to you. Once this is done, they will again have gained little, and they will trust you more.\"\n\n\"Soon, they will tell you the path to Stalker, and we will have them! Go. Go now.\" The light returns.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["100_9"] = 1
            return
        if StuffDone["8_0"] >= 1:
            if StuffDone["100_6"] >= 1:
                MessageBox("The voice appears, and asks \"Have the papers been returned?\" You answer in the affirmative, and tell of how O\'Grady is your next contact. \"Excellent. Go see her. This next contact will surely give us more information.\"\n\n\"Alas, Canizares disappeared after he gave you your next contact. We will be unable to arrest him. Go now. Hopefully, the next step will turn out better.\"")
                return
            if StuffDone["100_5"] >= 1:
                ChoiceBox("You sit in the throne again. The torches flicker, and darken. The voice says \"You have the papers. We have investigated, and found that there is nothing in them that can possibly help the Hill Runners.\"\n\n\"Go ahead and follow the instructions. Return the papers, and then go see what other missions they give you. Return, and clear those missions with us. We may be making headway. Jaen sends his compliments.\"\n\n\"That is all.\" The light returns.", eDialogPic.TERRAIN, 144, ["OK"])
                StuffDone["100_7"] = 1
                return
            MessageBox("You sit in the throne, and it shocks you! When you jump up, the voice says \"You fools! We told you to return here and clear any rebel missions before performing them, and yet you got the papers on your own.\"\n\n\"Had the papers been in any way useful, you could have done great harm. Do this again, and you will be severely punished. Now sit.\"")
            ChoiceBox("You sit in the throne again. The torches flicker, and darken. The voice says \"You have the papers. We have investigated, and found that there is nothing in them that can possibly help the Hill Runners.\"\n\n\"Go ahead and follow the instructions. Return the papers, and then go see what other missions they give you. Return, and clear those missions with us. We may be making headway. Jaen sends his compliments.\"\n\n\"That is all.\" The light returns.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["100_7"] = 1
            return
        if StuffDone["100_4"] >= 1:
            ChoiceBox("The lights in the room darken. A deep, grim voice sounds out in the air around you. \"Welcome. Have the Hill Runners contacted you? Have they asked you to do anything for them?\"\n\nYou say what happened. The voice responds, \"Good. They see you as good potential members, and they have given you a mission. Through you, we may find our way in, and find out where they are based.\"\n\n\"We know of that abandoned base. We also know that nothing of value was left there, of course. We are not fools. Go there, and recover the papers they wish.\"\n\n\"However, as always, return to us before taking any additional steps, such as returning the paper. Take no steps before consulting with us.\"\n\n\"That is all.\" The lights rise, and you stand.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["100_5"] = 1
            return
        ChoiceBox("You sit down in the throne, and wait for something to happen. It doesn\'t take long. The torches dim. Then, you hear a voice. It\'s slightly masculine, very flat, strong and deep. If seems to come from the walls around you.\n\n\"Welcome to Morrow\'s Isle. Hopefully, by now, you have heard of the cruel, violent rebels who are ravaging this island. You have been brought here to infiltrate them. No doubt, they will soon contact you. Have they?\"\n\nYou mention the note you found in your pocket. The voice says \"Excellent. Listen carefully. You are alone in this place. I am not a human, but a magical being, programmed to hear what you say and give directions. I also send your words elsewhere.\"\n\n\"Your mission is to help us find Stalker, leader of the Hill Runners. You will perform missions, winning their trust, until they tell you where he can be found. The work will be dangerous, but your reward at the end will be generous.\"\n\n\"In addition, of course, you will save many, many lives. These are lives that would have been lost to rebel attacks.\"", eDialogPic.TERRAIN, 144, ["OK"])
        if StuffDone["100_1"] >= 1:
            ChoiceBox("\"Now go, go and meet this Canizares mentioned in the note. And remember, there is one rule you must follow above all others. The rebels are crafty, and will try to manipulate you to do us great harm.\"\n\n\"Whatever you do, always report back to us before doing anything that might aid them. Take no steps without our permission. Otherwise, they will use you, and use you well. To get permission, return and sit in this chair.\"\n\n\"Failure to follow this direction will result in your severe punishment. Now go,and meet this Canizares. Good luck.\" The voice fades away, and the light returns.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["100_3"] = 1
            return
        result = ChoiceBox("\"This is the task before you. Great are the risks, great are the rewards, and great is the heroism you may perform. You will be fighting shrewd and lethal killers, killers of men, women, and children, who fight not only with blades, but with terror.\"\n\n\"Will you join us? Will you help in this noble fight?\"", eDialogPic.TERRAIN, 144, ["No", "Yes"])
        if result == 0:
            MessageBox("The voice is cold and soft. \"Fine. You reject our task, we reject you. Should you think better of it, return here. Otherwise, you can leave at the dock in Selathni. A boat will return you to the mainland.\"\n\n\"No thanks to you. You may go now.\" The lights return. The audience is over.")
            return
        elif result == 1:
            StuffDone["100_1"] = 1
            ChoiceBox("\"Now go, go and meet this Canizares mentioned in the note. And remember, there is one rule you must follow above all others. The rebels are crafty, and will try to manipulate you to do us great harm.\"\n\n\"Whatever you do, always report back to us before doing anything that might aid them. Take no steps without our permission. Otherwise, they will use you, and use you well. To get permission, return and sit in this chair.\"\n\n\"Failure to follow this direction will result in your severe punishment. Now go,and meet this Canizares. Good luck.\" The voice fades away, and the light returns.", eDialogPic.TERRAIN, 144, ["OK"])
            StuffDone["100_3"] = 1
            return
        return

def BelowWillow_27_MapTrigger_10_5(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(2,8)).Num == 131:
        if StuffDone["1_1"] >= 1:
            if StuffDone["2_0"] == 0:
                MessageBox("You find a note on the door. It reads \"We saw your approach. We know you have helped the rebels, without permission. We suggest you leave now. Continuing further will result in your doom.\"")
                Town.AlterTerrain(Location(2,8), 0, TerrainRecord.UnderlayList[130])
                return
            return
        return

def BelowWillow_28_MapTrigger_12_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(6,30)
    Party.MoveToMap(TownMap.List["Willow_0"])

def BelowWillow_29_MapTrigger_9_5(p):
    if StuffDone["101_1"] >= 1:
        Town.AlterTerrain(Location(2,8), 0, TerrainRecord.UnderlayList[130])
        return
