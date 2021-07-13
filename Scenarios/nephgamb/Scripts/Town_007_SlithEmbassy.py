
def SlithEmbassy_146_MapTrigger_7_31(p):
    if StuffDone["7_8"] == 250:
        return
    StuffDone["7_8"] = 250
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(7,31))
    MessageBox("A draft carries the smell of tar and rotten fish down this corridor.")

def SlithEmbassy_147_MapTrigger_9_36(p):
    if StuffDone["7_1"] == 250:
        return
    StuffDone["7_1"] = 250
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(9,36))
    MessageBox("The smell grows ever worse, and you try not to breath when you enter this small, dark room, filled with rotten trash.")

def SlithEmbassy_148_MapTrigger_26_36(p):
    if StuffDone["7_2"] == 250:
        return
    StuffDone["7_2"] = 250
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(26,36))
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(27,36))
    MessageBox("Sss-Varbas? personal caves are kept clean, even by human standards. There is no moss on the walls, no fungus or poisonous vegetation. The cave grass is lovingly cut and tended.")

def SlithEmbassy_150_MapTrigger_32_7(p):
    if StuffDone["7_0"] >= 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Slith spears glint in the dark corridor. The defenders have set up an ambush in the vulnerable passage. You decide to leave it to the Yvoss-tai to spring the trap.")
        return

def SlithEmbassy_151_MapTrigger_33_12(p):
    if StuffDone["57_0"] == 250:
        return
    StuffDone["57_0"] = 250
    TownMap.List["SlithEmbassy_7"].AlterTerrain(Location(33,12), 1, None)
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(33,12))
    MessageBox("You find a narrow side passage and climb quietly into it. Hidden by darkness, it takes a few seconds before Bass-Sslatun misses you. Then you hear him whispering hoarsely: \"Damn it, where are you? This is no time for games! Come out!\"")

def SlithEmbassy_152_MapTrigger_26_9(p):
    if StuffDone["7_7"] == 250:
        return
    StuffDone["7_7"] = 250
    TownMap.List["SlithEmbassy_7"].AlterTerrain(Location(26,9), 1, None)
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(26,9))
    MessageBox("Bass-Sslatun leads you down the narrow corridor with sure steps. His confidence seems like a thin coat over a shaky nerves. \"There will be an attempt on the ambassador?s life very soon.\" he whispers. \"We must hurry if we are to stop it.\"")

def SlithEmbassy_153_MapTrigger_33_7(p):
    if StuffDone["7_9"] == 250:
        return
    StuffDone["7_9"] = 250
    TownMap.List["SlithEmbassy_7"].AlterTerrain(Location(33,7), 1, None)
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(33,7))
    MessageBox("Bass-Sslatun stands at the entrance of a large cave. He curses silently and looks over his shoulder. \"I didn?t know there was a portculliss. See if you can find a way to open it. But hurry!\" He takes a few steps back into the corridor to listen.")

def SlithEmbassy_154_MapTrigger_15_19(p):
    if StuffDone["57_5"] == 250:
        return
    StuffDone["57_5"] = 250
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(15,19))
    MessageBox("This bridge has evidently been set up for the convenience of visiting humans. Sliths dive into the stream and swim, a much quicker way of transport in this terrain.")

def SlithEmbassy_155_MapTrigger_6_7(p):
    result = ChoiceBox("This pool of sparkling water evidently holds some ritual importance for the sliths. The three pools form the centrepiece for the shrine. A slith statue overlooks the pool, regarding you sternly. What do you do?", eDialogPic.TERRAIN, 186, ["Leave", "Touch", "Drink"])
    if result == 1:
        MessageBox("You dip your hand into the sparkling water.")
        StuffDone["7_3"] = 1
        if StuffDone["7_3"] >= 1:
            if StuffDone["7_4"] >= 1:
                if StuffDone["7_5"] >= 1:
                    if StuffDone["7_6"] < 1:
                        MessageBox("A voice sounds in your heads. \"You have great knowledge and resspect for our culture. We rejoice. As a reward you will learn more.\" The voice goes silent, and you look around you in astonishment. (Your poison skill has been adjusted.)\n\nThe three pools, that a moment ago were unspecified, poisonous liquid, now appear to you as distinct flavours, marked by minute differences. Is this how the sliths perceive the world? Intrigued by this insight into slith culture, you leave the shrine.")
                        for pc in Party.EachAlivePC():
                            pc.SetSkill(eSkill.POISON, pc.GetSkill(eSkill.POISON) + 2)
                        StuffDone["7_6"] = 1
                        return
                    return
                return
            return
        return
    elif result == 2:
        MessageBox("You cup your hands and drink deeply. Then you cough and vomit, trying to rid your system of the poisonous water. If the sliths drink this, they are even stranger than you thought.")
        for pc in Party.EachAlivePC():
            pc.Poison(3)
        return

def SlithEmbassy_156_MapTrigger_8_7(p):
    result = ChoiceBox("This pool of sparkling water evidently holds some ritual importance for the sliths. The three pools form the centrepiece for the shrine. A slith statue overlooks the pool, regarding you sternly. What do you do?", eDialogPic.TERRAIN, 186, ["Leave", "Touch", "Drink"])
    if result == 1:
        MessageBox("You dip your hand into the sparkling water.")
        StuffDone["7_4"] = 1
        if StuffDone["7_3"] >= 1:
            if StuffDone["7_4"] >= 1:
                if StuffDone["7_5"] >= 1:
                    if StuffDone["7_6"] < 1:
                        MessageBox("A voice sounds in your heads. \"You have great knowledge and resspect for our culture. We rejoice. As a reward you will learn more.\" The voice goes silent, and you look around you in astonishment. (Your poison skill has been adjusted.)\n\nThe three pools, that a moment ago were unspecified, poisonous liquid, now appear to you as distinct flavours, marked by minute differences. Is this how the sliths perceive the world? Intrigued by this insight into slith culture, you leave the shrine.")
                        for pc in Party.EachAlivePC():
                            pc.SetSkill(eSkill.POISON, pc.GetSkill(eSkill.POISON) + 2)
                        StuffDone["7_6"] = 1
                        return
                    return
                return
            return
        return
    elif result == 2:
        MessageBox("You cup your hands and drink deeply. Then you cough and vomit, trying to rid your system of the poisonous water. If the sliths drink this, they are even stranger than you thought.")
        for pc in Party.EachAlivePC():
            pc.Poison(3)
        return

def SlithEmbassy_157_MapTrigger_21_12(p):
    MessageBox("Dozens of slith hatchlings swarm this humid cave. Sliths are born with gills and poor lungs, and so spend more time under water than over during their first years. A slith nurse tries in vain to keep the hatchlings from splashing water on the bonfire.\n\nDuring the first years, it also becomes evident which social class the adult slith will sort under. Nurses separate the warriors from the craftsman class as well as the dimwitted workers.")

def SlithEmbassy_158_MapTrigger_22_20(p):
    if StuffDone["57_6"] == 250:
        return
    StuffDone["57_6"] = 250
    TownMap.List["SlithEmbassy_7"].AlterTerrain(Location(22,20), 1, None)
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(22,20))
    MessageBox("Somebody has dropped his spear down into this narrow crack. You pick it up and hope nobody will claim it.")
    Party.GiveNewItem("IronSlithSpear_90")

def SlithEmbassy_159_MapTrigger_35_16(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(43,6)
    Party.MoveToMap(TownMap.List["Myldres_6"])

def SlithEmbassy_160_MapTrigger_39_10(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(Location(45,3))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(45,3), 0, TerrainRecord.UnderlayList[148])
        elif t == TerrainRecord.UnderlayList[148]: Town.AlterTerrain(Location(45,3), 0, TerrainRecord.UnderlayList[147])
        if StuffDone["7_0"] >= 1:
            return
        ChoiceBox("You push hard and hear the sound of a portcullis rising. You turn around and are startled to see cowled shapes streaming through the open portal, whispering thanks for letting them in.\n\nWhen they are all in, they drop their cloaks, revealing slith warriors and mages. It takes a moment for you to recognize them, but then you freeze from shock. They wear the bronze charms of the Yvoss-tai. You have let the enemy in!\n\nYou reach for your weapons, but then Bass-Sslatun bursts into the cave. \"Ah, I see you have already met.\" The bronze-toucher grins. \"I?m sorry we led you into this, but we needed your help in the fight. The ambassador?s men have found us!\"", eDialogPic.CREATURE, 48, ["OK"])
        Town.PlaceEncounterGroup(3)
        StuffDone["222_0"] = 1
        StuffDone["7_0"] = 1
        Timer(Town, 2, False, "SlithEmbassy_168_TownTimer_36", eTimerType.DELETE)
        return

def SlithEmbassy_161_MapTrigger_40_16(p):
    if StuffDone["57_1"] == 250:
        return
    StuffDone["57_1"] = 250
    TownMap.List["SlithEmbassy_7"].AlterTerrain(Location(40,16), 1, None)
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(40,16))
    MessageBox("Bass-Sslatun chances a shout in the corridor behind you: \"The ambassador is in danger! Return now, or all will be losst! Please, humanss, where have you gone?\" The brave slith sounds like he is on the edge of panic.")

def SlithEmbassy_162_MapTrigger_39_28(p):
    if StuffDone["57_2"] == 250:
        return
    StuffDone["57_2"] = 250
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(39,28))
    TownMap.List["SlithEmbassy_7"].DeactivateTrigger(Location(38,28))
    ChoiceBox("Your nagging suspicions are confirmed when this winding passage enters the quarters of the ambassador.\n\nThe ambassador himself jumps to his feet when you barge in on him, demanding to know why you startle him. It is clear that he knows nothing of the expected assassination. Why would Bass-Sslatun tell you about it, but not the target?\n\nYou quickly let the ambassador know what is happening, and for a moment you think you spy fear in his eyes. \"That Bass-Sslatun, the arrogant craftssman! He is behind this!\" the ambassador roars.\n\n\"It was good of you to see through his plan. You must never trust a bronze-toucher!\"\n\nSss-Varbas is already moving, picking up weapons and calling for his warriors. \"You must return to the traitor, allow him to spring his trap. You have given me warning. That is all you can do. Now, play along with him.\"\n\nAs the slith ambassador leaves the cave, he stops and bows to you. \"You may have saved my life. I am in debt to you.\" This is rare, coming from a slith noble.", eDialogPic.CREATURE, 50, ["OK"])

def SlithEmbassy_163_MapTrigger_32_32(p):
    if StuffDone["57_3"] >= 1:
        if StuffDone["57_4"] == 250:
            return
        StuffDone["57_4"] = 250
        MessageBox("You leave the ambassador deep in thought. So there are good sliths and bad sliths. Or are there? Which side is which? Well, there are two kinds of sliths, anyway. And the ambassador sounded like his warriors were coming after the rebels.\n\nWill they turn Chimney into a battleground over nursing rights? And if one of them wins, what will they do to Chimney? You are not reassured by this conversation.")
        return

def SlithEmbassy_164_MapTrigger_10_7(p):
    result = ChoiceBox("This pool of sparkling water evidently holds some ritual importance for the sliths. The three pools form the centrepiece for the shrine. A slith statue overlooks the pool, regarding you sternly. What do you do?", eDialogPic.TERRAIN, 186, ["Leave", "Touch", "Drink"])
    if result == 1:
        MessageBox("You dip your hand into the sparkling water.")
        StuffDone["7_5"] = 1
        if StuffDone["7_3"] >= 1:
            if StuffDone["7_4"] >= 1:
                if StuffDone["7_5"] >= 1:
                    if StuffDone["7_6"] < 1:
                        MessageBox("A voice sounds in your heads. \"You have great knowledge and resspect for our culture. We rejoice. As a reward you will learn more.\" The voice goes silent, and you look around you in astonishment. (Your poison skill has been adjusted.)\n\nThe three pools, that a moment ago were unspecified, poisonous liquid, now appear to you as distinct flavours, marked by minute differences. Is this how the sliths perceive the world? Intrigued by this insight into slith culture, you leave the shrine.")
                        for pc in Party.EachAlivePC():
                            pc.SetSkill(eSkill.POISON, pc.GetSkill(eSkill.POISON) + 2)
                        StuffDone["7_6"] = 1
                        return
                    return
                return
            return
        return
    elif result == 2:
        MessageBox("You cup your hands and drink deeply. Then you cough and vomit, trying to rid your system of the poisonous water. If the sliths drink this, they are even stranger than you thought.")
        for pc in Party.EachAlivePC():
            pc.Poison(3)
        return

def SlithEmbassy_165_MapTrigger_32_40(p):
    MessageBox("The stream widens at this point and enters the river Myld. Your boat is made for the calm indoor lakes of the sliths, not for the wild streams of a large river, so you decide against venturing out.")

def SlithEmbassy_168_TownTimer_36(p):
    ChoiceBox("The sliths hiss in alarm, and without warning a second group bursts into the room. Lizard faces regard each other in silent contempt, and you repeat Bass-Sslatun?s alien curses as the subtleness of the Yvoss-tai trap dawns on you.\n\nBass-Sslatun didn?t bring you here to push a button for him. The cold looks of the ambassador?s soldiers say it all. Your presence in this room makes you a rebel and an accomplice. You are just as dead as the others if the Yvoss-tai lose this battle.\n\n\"You get the point?\" Bass-Sslatun leers. \"This time you fight for us, Brattaskar Heroes. And fight well, we?ll need your help!\"\n\nYou grit your teeth and look from side to side, begging for a way out of this dilemma. No such luck. You have been framed, and must suffer the consequences. A fireball sizzles, and lizard yells start the battle.\n\nAfter a moment, all you can do is defend yourselves. But, you think, you must survive this. If only to hunt Oterel out and smash his slick face...", eDialogPic.CREATURE, 49, ["OK"])
    Town.PlaceEncounterGroup(2)

def SlithEmbassy_169_OnEntry(p):
    if not Town.Abandoned:
        MessageBox("This set of stairs separates two worlds. Above are the human streets of the capital. Below, you step into a humid, warm cave smelling of fungus and sweet herbs. Sounds of splashing water and lizards hissing echo through this genuinely subterranean world.\n\nBonfires heat the closed-in air, making you sweat and attracting swarms of stinging insects. Pools reflect the light of the flames, making flickering shadows in the ceiling. You remind yourselves of how different the sliths really are.")
        if StuffDone["7_0"] >= 1:
            MessageBox("The battle is over, there is a new ambassador, an Yvoss-tai. You look for changes, but see no great difference. The guards at the stairways are the same, you think. There are less people about, the mood is perhaps more subdued.")
            Town.AlterTerrain(Location(37,31), 0, TerrainRecord.UnderlayList[102])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "SlithChief_53": Town.NPCList.Remove(npc)
            Town.PlaceEncounterGroup(3)
            return

def SlithEmbassy_170_ExitTown(p):
    if p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(30, 27),WorldMap.SectorAt(Party.OutsidePos))

def SlithEmbassy_171_TalkingTrigger2(p):
    Town.AlterTerrain(Location(22,6), 0, TerrainRecord.UnderlayList[0])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "SlithWarrior_48": Town.NPCList.Remove(npc)
    Town.AlterTerrain(Location(16,10), 0, TerrainRecord.UnderlayList[109])
