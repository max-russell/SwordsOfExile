
def NortheasternAizic_2493_MapTrigger_10_38(p):
    if StuffDone["41_8"] == 250:
        return
    StuffDone["41_8"] = 250
    WorldMap.DeactivateTrigger(Location(58,134))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("This is a small farming community that produces crops for the area in the fertile plains of the Aizic Sector. When you arrive, there is some kind of rally going on. You decide to take a closer look.\n\nSeveral people are huddled around a central stage at the center of the town. On the stage is a man in shiny armor with a red spear painted upon its crest. He is speaking of the atrocities of the Empire and how it needs to be, in his words, \'defrocked\'.\n\nWith him on the stage are several archers. You notice that one of them spots you and points you out to the speaker. He grins for a moment and continues to speak. Then he points you out to the crowd. Everyone turns to look at you.\n\n\"I see those Imperials have arrived! They have come to break up our demonstration. Think of how they treat farmers. They are underpaid, overworked, and under appreciated by the Empire. These soldiers represent all of that!\"\n\nA stream of boos run through the crowd. They begin to chant, \"Down with the Empire! Down with the Empire!\" Then one of them attacks you, you have no choice but to fight back. Your assault leaves him on the ground, with the wind knocked out of him.\n\nThe speaker shouts, \"Look at the example of the Empire\'s cruelty. This only further verifies what I have told you. The Empire must be stopped!\" With those words many of the crowd begin to riot against you. The speaker and his guards also join in.", eDialogPic.CREATURE, 15, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_2_4", p.Target)

def NortheasternAizic_2494_MapTrigger_31_18(p):
    if StuffDone["42_0"] == 0:
        result = ChoiceBox("Several Troglodytes are encamped in the middle of this swamp. You bet you have stumbled on to one of their hiding places. They are probably going to stage an assault on the nearby fort.\n\nHowever, you have the opportunity to preempt such an attack. The Troglos have about twenty or so people encamped here. A raid would be a challenge, but probably not out of the scope of your abilities.\n\nThe other thing you have is the element of surprise on your side. As far as you know, they do not know of your presence yet. Considering this fact, you could also leave this campsite undetected.", eDialogPic.CREATURE, 114, ["Leave", "Attack"])
        if result == 1:
            StuffDone["42_0"] = 1
            Animation_Hold(-1, 018_drawingsword)
            Wait()
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) + 2))
            ChoiceBox("You decide to charge the camp. They are totally unprepared for your attack which definitely gives you an advantage. You should probably work as fast as you can before they manage to regroup.", eDialogPic.CREATURE, 112, ["OK"])
            WorldMap.SpawnNPCGroup("Group_1_2_5", p.Target)
            return
        MessageBox("You decide the Troglodytes are a bit too much for you to handle at the moment. Perhaps someone else can deal with them more effectively.")
        p.CancelAction = True
        return
    MessageBox("There is the left over of a campsite here.")

def NortheasternAizic_2495_MapTrigger_40_19(p):
    if StuffDone["42_1"] == 0:
        result = ChoiceBox("There is a human skeleton lying on the ground. The skeleton is garbed in tattered and worn mage robes. You cannot tell if this person was male or female. One thing you notice is one of the leg bones were broken.\n\nHe or she must have had a nasty fall in these hills and met an unpleasant end by dying of thirst. Beneath the body is a satchel containing a few scrolls and on the person\'s belt is a wand. Do you take them?", eDialogPic.TERRAIN, 179, ["Leave", "Take"])
        if result == 1:
            StuffDone["42_1"] = 1
            Party.GiveNewItem("ScrollFlame_196")
            Party.GiveNewItem("ScrollSlow_197")
            Party.GiveNewItem("ScrollCharm_206")
            Party.GiveNewItem("WandofIce_286")
            return
        return

def NortheasternAizic_2496_MapTrigger_26_38(p):
    if StuffDone["42_2"] == 250:
        return
    StuffDone["42_2"] = 250
    WorldMap.AlterTerrain(Location(74,134), 1, None)
    WorldMap.DeactivateTrigger(Location(74,134))
    Animation_Hold(-1, 023_startoutdoorcombat)
    Wait()
    ChoiceBox("You come across a fairly large battle. Several Empire soldiers are fending off a much larger pack of Troglodytes. The situation does not look very good for the Empire soldiers here.\n\nOne of them sees you and calls for your help. Then several of the Troglodytes begin to attack you! It looks like you are trapped and have no choice but to enter the fray.", eDialogPic.STANDARD, 1027, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_2_7", p.Target)

def NortheasternAizic_2497_MapTrigger_18_3(p):
    if StuffDone["42_3"] == 250:
        return
    StuffDone["42_3"] = 250
    WorldMap.AlterTerrain(Location(66,99), 1, None)
    WorldMap.DeactivateTrigger(Location(66,99))
    MessageBox("A person jumps from the top of the wall. He is a young man in his mid-twenties. He shouts, \"At last I am free!\" He looks over and is shocked to see you. He gets on his knees and begs. \"Oh, please do not take me back!\"\n\nYou inquire about the escape. \"I escaped from Stolgrad, a horrible place. They treat the subjects there worse than dogs. I\'d do anything not to go back there, please!\" You decide not to take him prisoner and he runs off.")

def NortheasternAizic_2498_WanderingOnMeet0(p):
    MessageBox("The Aizic Sector has been having problems lately with some renegade Troglodytes. Unfortunately, you have just managed to stumble across one of their patrols.")

def NortheasternAizic_2499_WanderingOnMeet1(p):
    MessageBox("You are approached by a group of armed people. You immediately recognize them as wearing uniforms displaying a red spear. As soon as they see you, they move in to attack!")

def NortheasternAizic_2500_WanderingOnMeet2(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NortheasternAizic_2502_SpecialOnWin0(p):
    ChoiceBox("During the fray, you tried your best not to kill or mame any of the townspeople. Most of them decided to flee when the riot broke out. Most of them are injured, but will recover. Only two of the ten who attacked are seriously wounded.\n\nThe only people that you had to kill were the speaker and his archers. They would have stopped at nothing to lynch some Empire soldiers, making an example out of you. Now they are dead and the crowds have dispersed.\n\nA few of the more higher minded townspeople come up to you and thank you for breaking up the rally. They tell you that the Red Spear is trying to insight local disturbances to destabilize the Empire.\n\nThey have had good success with the former, but have only had a minimal impact of the latter, which was their ultimate goal. They hope that the Red Spear will not return for quite some time.", eDialogPic.CREATURE, 2, ["OK"])

def NortheasternAizic_2503_SpecialOnWin1(p):
    ChoiceBox("Your raid was a success! You have managed to kill off several of the Troglodytes. A few of them managed to escape, but you cannot expect to get everyone. You have disrupted whatever operations that had planned in this swamp.\n\nNow that the camp is empty, you decide to take a look around. These Troglodytes were fairly successful. You manage to gather between the tents several hundred gold pieces. Also you find some nice shiny chain mail with the Sword and Sun.\n\nYou bet that was taken from a fallen soldier during one of their raids. Oh well, it is yours now.", eDialogPic.CREATURE, 116, ["OK"])
    Party.Gold += 341
    Party.GiveNewItem("SteelChainMail_131")

def NortheasternAizic_2504_SpecialOnFlee1(p):
    MessageBox("The Troglos were too much for you to handle. Not wanted to risk another attack, the Troglos flee their campsite.")

def NortheasternAizic_2505_SpecialOnWin3(p):
    ChoiceBox("The Troglodytes have been slain and your fellow Empire soldiers have been saved. The leader of the troops, a mage captain comes up to you to thank you personally.\n\n\"Thanks soldiers! We could not have won without you. I don\'t seem to recognize you, are you from around here?\" You tell him that you are Imperial Guardians originally stationed in the Agran Sector.\n\n\"I see, so that is why you were so skilled on the battlefield.\" He grins. \"I am Captain Leavy. My boys and I were stationed up at Fort Reflection when we stumbled onto a sizable force of Troglodytes.\n\nWe were doing all right until another Troglodyte patrol decided to join in the combat. It\'s a good thing you came along or we would have been toast!\" He grabs a wand that was secured on his belt.\n\n\"Here take this!\" He hands you the wand. \"It\'s a wand of fireballs. It\'s mostly used up, but it\'s the only payment I can think of. I hope it is of help to you on your travels.\"", eDialogPic.CREATURE, 26, ["OK"])
    Party.GiveNewItem("WandofFireballs_284")

def NortheasternAizic_2506_SpecialOnFlee3(p):
    MessageBox("You manage to flee the battlefield. Too bad for the Empire soldiers. With your help, they could have actually won the thing. However, the Troglos manage to tear them apart. Too bad.")
