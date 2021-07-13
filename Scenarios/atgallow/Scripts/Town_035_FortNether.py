
def FortNether_745_MapTrigger_30_5(p):
    if StuffDone["14_4"] == 250:
        return
    StuffDone["14_4"] = 250
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(30,5))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(31,5))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(32,5))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(33,5))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(34,3))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(34,4))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(29,3))
    TownMap.List["FortNether_35"].DeactivateTrigger(Location(29,4))
    ChoiceBox("You near the Nethergate and the sorcerer. You say, \"Balkis, I presume.\" He grins, \"Indeed your presumption is correct. However, it is not healthy to presume. Just because you\'re here, doesn\'t mean you will win. I could easily smash all of you!\n\nHowever, I want to finish my test of you first. You have proven to be a great stumbling block for our operations. But no longer. You are no match for me. I doubt your weapons and spells are even strong enough to harm me. Pity.\n\nI must admit that I am impressed. You managed to defeat my capable apprentice, and escape the death sentence he had inflicted on you. Oh, and you can give me credit for that poison. I gave him the idea.\n\nI purposely left a way for you to get here. I was amused to watch your frustration. But, against all odds you made it. I swear that you were chosen by some divine power or something. No ordinary band of soldiers could have done as much as yours.\"\n\nHe turns to the Nethergate. He casts a spell and it seems to expand. \"Ah my lovely creation! It enabled me to bring forth those creatures you fought earlier. But this is only the beginning! Soon I shall have thousands at my command!\n\nNow, there is this new creature called an Alien Slime that I am considering. I see no better test for it than on you.\" The portal begins to crackle and an immense tentacled shadow emerges. Balkis looks at you with amusement.", eDialogPic.STANDARD, 22, ["OK"])
    Town.PlaceEncounterGroup(1)

def FortNether_753_MapTrigger_32_3(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["14_5"] >= 2:
        if StuffDone["14_5"] < 3:
            if SpecialItem.PartyHas("OnyxScepter"):
                ChoiceBox("You approach the Nethergate and remove the Onyx Scepter. Immediately, the scepter emits a high pitched keening sound and glows a dazzling white. You hold it up to the Nethergate and the two forces begin to conflict.\n\nHowever, as strong as the Nethergate is, the spacial restoring effects of the Onyx Scepter are stronger. The Nethergate begins to shrink and degenerate. In not too much time, the gate is gone. You have accomplished your mission!\n\nSuddenly, you see a flash behind you...", eDialogPic.STANDARD, 22, ["OK"])
                for x in range(31, 33):
                    for y in range(1, 3):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
                Town.PlaceEncounterGroup(3)
                Animation_Explosion(Location(31,5), 1, "005_explosion")
                Animation_Hold()
                Wait()
                ChoiceBox("You turn to see Auspire materialize. You get a jolt of pleasure as you watch her smug complexion turn to one of horror and shock. \"What have you done to my beautiful Nethergate!? All my years of planning and hoping, gone!\"\n\nShe calms down considerably. \"You Imperial pigs. Do you not know that the Order of Odin are the true claimants to the throne. We were merely trying to take back what was ours so long ago.\n\nBut now our hopes and dreams are shattered. Just like Zenith Keep. As we speak, Empire soldiers are making their way through my palace. However, they shall not find me. If it is any consolation, I shall deal with you before I leave the continent.\"\n\nShe begins to build up power. You draw your weapons in preparation for the fight. \"Now behold our true power!\"", eDialogPic.CREATURE, 1025, ["OK"])
                Town.PlaceEncounterGroup(4)
                Animation_Explosion(Location(32,5), 1, "005_explosion")
                Animation_Hold()
                Wait()
                ChoiceBox("Cylene materializes beside Auspire. She shouts out, \"Mother stop!\" She continues to build power. \"No Cylene, I must have revenge against them. Years and years of planning, all gone because of them. I must defend the Order.\"\n\n\"To hell with the Order! That\'s what Raiden said.\" Auspire replies, \"Raiden was a fool. We shall see he gets what he deserves. Nobody crosses the Order of Odin and gets away with it. I decided to ignore your treachery, do not force me to harm you!\"\n\n\"Mother, why can\'t you see that your bloodlust only causes more suffering. Nothing good will come.\" Auspire says nothing. Cylene begins to cry, \"Mother, what happened to you? You used to have compassion. You used to have a soul.\"\n\nAuspire turns to her daughter with a grim expression. Suddenly, a voice echoes from out of nowhere and seemingly from everywhere. It is a chilling voice, that strikes fear into your soul.\n\n\"You are correct young one. She has no soul anymore because I have taken it, along with much of the Order of Odin. They have been excellent pawns in my plans. Your soul is strong, but soon it shall be mine as well.\"\n\nCylene pleas, \"Who are you?\"", eDialogPic.CREATURE, 132, ["OK"])
                Town.PlaceEncounterGroup(5)
                Animation_Explosion(Location(32,6), 2, "005_explosion")
                Animation_Hold()
                Wait()
                ChoiceBox("The most fearsome sight appears. A skeleton surrounded by immense dark energy floats before you. Its eyes glow a deep red. Evil seems to pour from the foul being. You are standing before a Lich!\n\nIt begins to speak. The voice continues to come from beyond. The mouth of its skeletal body does not move as it speaks. \"I am Morbane, the almighty! Bow down and worship me, puny mortals!\"\n\nAt last! You know the true identity of Morbane, a Lich. He directs his thoughts at you. \"You have come far my warriors, too far. Now I shall personally destroy you!\" Cylene shouts out, \"No! Take that!\" She fires a bolt of light, Morbane absorbs it.\n\nHe turns to Cylene, \"Mwa, ha, ha! You really think your powers can harm me? Oh don\'t lie to yourself.\" He fires a bolt of darkness back at her. She is thrown back as she screams with pain. \"Now, victory will be mine!\"\n\nYou are assaulted with waves of darkness. It is extremely painful and you stand no chance. But then, Auspire unleashes her powers on Morbane. Cylene stands and Mother and Daughter confront the Lich. You get up to help.\n\n\"Now you shall all perish!\" He begins an earthquake! Auspire yells out to you, \"You, Cylene escape while there is still time, I shall hold them off.\" Cylene refuses to leave and yells, \"No, I\'m staying with Mother. Get out of here!\"", eDialogPic.CREATURE, 60, ["OK"])
                StuffDone["14_5"] = 3
                return
            MessageBox("You approach the Nethergate and realize that you have no idea how to destroy it. Suddenly, you see a flash of light behind you.")
            Town.PlaceEncounterGroup(3)
            Animation_Explosion(Location(31,5), 1, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("Auspire, the ruler of the Stolgrad Sector has arrived. Surprisingly, she is not accompanied by any kind of guards. She looks at you with utter hatred and contempt.\n\n\"Well, it looks like your nation found me out. As we speak, the forces of the Empire are cutting their way through Zenith Keep. Too bad I managed to escape. I see that you managed to take care of Balkis.\n\nI can succeed without him. But first I shall deal with you.\" She casts a spell and opens the Nethergate. You try to resist, but she hits you with a bolt of energy and you are swept into the darkness.", eDialogPic.STANDARD, 22, ["OK"])
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        return
    if StuffDone["14_5"] < 1:
        return
    if SpecialItem.PartyHas("NullityCrystal"):
        MessageBox("You decide that this would be an excellent time to use that crystal that Dervish Montcalm gave you. You smash it on the ground. Balkis looks at the event inquisitively.\n\n\"I don\'t know what you were trying to do, but whatever does not appear to have done anything of significance.\" You keep trying to resist and suddenly...")
        SpecialItem.Take("NullityCrystal")
        Town.PlaceEncounterGroup(2)
        Animation_Explosion(Location(33,4), 1, "005_explosion")
        Animation_Hold()
        Wait()
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(32,5))
        p.CancelAction = True
        ChoiceBox("Dervish Montcalm materializes! Balkis immediately shifts his attention away from the gate and onto the wizard, allowing you to escape the pull of the Nethergate. Both magi stare at each other for seeming eternity.\n\nThen Balkis speaks. \"We have met before. You have that aura. But I cannot place...ah ha! Montcalm, my old friend from the magery academy!\" He looks him over. \"Impressive, you made it to the rank of Dervish. Didn\'t think you had it.\"\n\nMontcalm speaks, \"Well you would be surprised. Just as I have another surprise for you.\" Balkis retorts. \"Ah, you think you could defeat me? Well, you were no match for me back at the academy and certainly none for me now!\"\n\nWith that, the two magi enter some kind of mental duel. You try to assist your ally, but Balkis sends out a bolt to throw you back. You will just have to wait and see the outcome.\n\nIt appears the Dervish is losing. \"Give up now, old friend. Do not force me to kill you!\" Montcalm replies, \"Never! See how you like this!\" Montcalm suddenly reopens the Nethergate with maximum force!\n\nBalkis, swept off guard is pulled into the void. Unfortunately, he manages to hook Montcalm with him. Both magi vanish into the darkness. The gate closes and Balkis is gone, as is your friend. Now to take care of the gate.", eDialogPic.CREATURE, 27, ["OK"])
        StuffDone["14_5"] = 2
        Town.NPCList.Clear()
        return
    MessageBox("The pull of the Nethergate is too strong and you are sucked into the void. The last thing you see before everything goes totally black is the smiling face of Balkis.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def FortNether_757_MapTrigger_31_16(p):
    if StuffDone["14_5"] < 3:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange force keeps this door closed. You cannot escape.")
        return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["13_5"] = 2
    StuffDone["17_0"] = 1
    StuffDone["9_0"] = 7
    StuffDone["17_1"] = 1
    StuffDone["43_0"] = 1
    Animation_Hold(-1, 005_explosion)
    Wait()
    Animation_Hold(-1, 010_teleport)
    Wait()
    Party.OutsidePos = Location(77, 36)
    ChoiceBox("You quickly flee the chamber and find a way out of the crumbling fortress. When you are clear, you turn around to see the entire face of the mountain passage cave in. Nobody will ever be getting in there anymore.\n\nYou start to walk back and are encountered by a fairly large band of Empire soldiers led by an Empire Dervish. You approach. You do not recognize the Dervish, but his face is very grim. \"Good day Guardians. I am Dervish Accolade.\"\n\nSuddenly other soldiers in the group surround you. \"I\'m afraid that you will have to surrender your equipment to us. By order of the Empire, I am hereby ordered to place you under arrest.\"\n\nYou are shocked by hearing this. You demand, \"Explain this, sir!\" He replies, \"The nature of the charge is the murder of the Order of Urlak-Nai. Please, do not make us use force.\" You are overwhelmed in strength, you have no choice.\n\nYou are escorted back through the guarded mountains. As you pass the guard towers, you see several archers atop them. However, they are ones loyal to the Empire. You reach another fortress in Stolgrad to find it occupied by Empire soldiers also.\n\nYour escort back ends at Zenith Keep. As you had suspected, the Empire has taken complete control away from the ruling Order of Odin. The Dervish speaks, \"I must confine you to quarters we have set up for you.\"", eDialogPic.CREATURE, 17, ["OK"])
    ChoiceBox("There is little else you can do but wait. In the morning an official comes to you. The same official that spoke out against you at the hearing in Auspire earlier. \"I suppose you want an explanation.\n\nYour actions led to the unauthorized release of the Haakai lord Skol-Trok and the utter obliteration of the Order of Urlak-Nai. The sectors of the Empire saw this covert action as a threat to their internal sovereignty and demanded recourse.\"\n\nYou ask, \"But how does it threaten them?\" He responds, \"All image and precedence. If we, the Empire, take action against a sector (although this time Urlak-Nai) without provocation, it appears that we could do it whenever we wanted to.\n\nThis makes the other sectors feel threatened and subsequently applied pressure on us. They demanded that you and your commanding officer Vale be executed as a sign to show that this was an intolerable independent act.\n\nThe fact that you were actually preserving the Empire and stopping the encroachment of the Stolgrad sector managed to quell them somewhat. The good news, is you will not be tried for this.\n\nHowever, I\'m afraid Vale was executed promptly last night. It was the only way to show that Imperial commanders cannot overstep their bounds. Anyway, the Prime Director wishes to speak with you soon. You are free to go!\"", eDialogPic.CREATURE, 31, ["OK"])
    ChoiceBox("The official leaves. You are stuck by the pain of guilt. If the deed back at Urlak-Nai wasn\'t bad enough, things are now worse. Another life has been lost because of your actions.\n\nSure, you were just following orders. But that still does little to wash away the guilt. You will never know for sure if there would have been another way to duplicate the effects of the Onyx Scepter.\n\nUnfortunately, there is nothing you can do about that. You must take pride in saving the Empire from years of bloody battle, even if no appreciation has been shown to you.\n\nBut now, the Prime Director awaits back at the Palace!", eDialogPic.STANDARD, 4, ["OK"])
    StuffDone["100_1"] = 1
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(53,19)
    Party.MoveToMap(TownMap.List["ZenithKeep_30"])

def FortNether_759_MapTrigger_53_57(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(56,54), 0, TerrainRecord.UnderlayList[139])
        Town.AlterTerrain(Location(30,51), 0, TerrainRecord.UnderlayList[170])
        return

def FortNether_760_MapTrigger_10_54(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(56,54), 0, TerrainRecord.UnderlayList[139])
        Town.AlterTerrain(Location(8,38), 0, TerrainRecord.UnderlayList[170])
        Town.AlterTerrain(Location(30,51), 0, TerrainRecord.UnderlayList[139])
        return

def FortNether_761_MapTrigger_5_24(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(56,54), 0, TerrainRecord.UnderlayList[170])
        Town.AlterTerrain(Location(30,51), 0, TerrainRecord.UnderlayList[139])
        return

def FortNether_762_MapTrigger_16_22(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(4,38), 0, TerrainRecord.UnderlayList[170])
        Town.AlterTerrain(Location(8,38), 0, TerrainRecord.UnderlayList[139])
        Town.AlterTerrain(Location(30,51), 0, TerrainRecord.UnderlayList[170])
        return

def FortNether_763_MapTrigger_6_42(p):
    Town.AlterTerrain(Location(4,38), 0, TerrainRecord.UnderlayList[139])

def FortNether_764_MapTrigger_59_39(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(50,38), 0, TerrainRecord.UnderlayList[170])
        Town.AlterTerrain(Location(32,36), 0, TerrainRecord.UnderlayList[139])
        return

def FortNether_765_MapTrigger_54_29(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(56,29)).Num == 71:
            MessageBox("Suddenly, all of the water drains out!")
            SuspendMapUpdate()
            for x in range(54, 61):
                for y in range(28, 38):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[96])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[96]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
            ResumeMapUpdate()
            return
        MessageBox("Nothing happens.")
        return

def FortNether_766_MapTrigger_55_37(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(36,32), 0, TerrainRecord.UnderlayList[170])
        return

def FortNether_767_MapTrigger_48_13(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(28,32), 0, TerrainRecord.UnderlayList[170])
        return

def FortNether_768_MapTrigger_51_2(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(13,19), 0, TerrainRecord.UnderlayList[170])
        return

def FortNether_769_MapTrigger_5_4(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(23,25), 0, TerrainRecord.UnderlayList[139])
        Town.AlterTerrain(Location(32,28), 0, TerrainRecord.UnderlayList[170])
        Timer(Town, 20, False, "FortNether_775_TownTimer_69", eTimerType.DELETE)
        return

def FortNether_770_MapTrigger_29_22(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        Town.AlterTerrain(Location(32,28), 0, TerrainRecord.UnderlayList[170])
        return

def FortNether_771_MapTrigger_34_22(p):
    result = ChoiceBox("You come across a glowing portal. Care to find out where it goes?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(38,47)
        Party.MoveToMap(TownMap.List["FortNether_34"])
        return
    p.CancelAction = True

def FortNether_772_MapTrigger_32_32(p):
    result = ChoiceBox("You come across a glowing portal. Care to find out where it goes?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(31,28)
        Party.MoveToMap(TownMap.List["FortNether_34"])
        return
    p.CancelAction = True

def FortNether_773_MapTrigger_11_61(p):
    ChoiceBox("You find a well used piece of paper. There is a note at the beginning, \"Damn that Balkis! This has got to be the most illogical fortress in the history of the Empire. He says these measures are necessary to ward off an invasion.\n\nHe sure did a damn good job of that. Not even we can remember how to make their way through this insane place. He says that we all need to commit the fortress to memory. Yeah right!\n\nI wonder who\'s idea it was to hire that eccentric. Anyway, in case we get lost, I decided to write down what some of the buttons do. Just don\'t let Balkis find out about this.\" The note is unsigned. You read further:\n\n5,23 Op. 56,54 Cl. 30,51 -- 10,55 Op. 8,38 Cl. 56,54 30,51 -- 16,23 Op. 4,38 30,51 Cl. 8,38 -- 29,23 Op. 32,28 -- 53,58 Op. 30,51 Cl. 56,54 -- 5,3 Op. 32,28 Cl. 23,25 -- 48,12 Op. 28,32 -- 58,3 Op. 32,28 Cl. 28,32 -- 58,39 Op. 50,38 Cl. 32,36\n\nYikes! Balkis sure must be paranoid to design something this horribly complicated. The worst part is, you are the ones who have to figure it out!", eDialogPic.TERRAIN, 135, ["OK"])

def FortNether_774_MapTrigger_42_51(p):
    MessageBox("There is a note buried in the stacks. \"The passageway to the Nethergate area only stays open for a short time. The distance between the switch and it makes it so that one person would have to push the switch while another goes through.\n\nAlthough that is the plan, I suppose it is possible to make it through alone with the aid of haste spells and a lot of running. Haven\'t tried it though.\"")

def FortNether_775_TownTimer_69(p):
    Town.AlterTerrain(Location(32,28), 0, TerrainRecord.UnderlayList[139])
    Animation_Hold(-1, 010_teleport)
    Wait()

def FortNether_776_CreatureDeath1(p):
    Town.NPCList.Clear()
    Town.PlaceEncounterGroup(6)
    ChoiceBox("You strike a final blow to the massive Alien Slime. It begins to wrack in pain as it emits a horrid screech. Within a minute, the creature has degenerated to little more than a large pool of jelly.\n\nBalkis claps his hands. \"Well done! But this creature is only the beginning! Soon I shall have armies of these and creatures thrice as powerful. Oh, it shall be wonderful. Pity that you won\'t be around to witness it!\"\n\nHe laughs as he casts another spell on the gate. The gate becomes an even deeper black as it becomes like a vacuum! It pulls the pool of jelly back into the gate. It vanishes in the blackness. Balkis laughs as he increases the intensity.\n\nAll the other monsters around you struggle but are ultimately pulled inside. You manage to grip some of the pillars and resist the pull. \"Not only can the Nethergate dish it out, but it can take it in as well! Come, the void awaits!\"", eDialogPic.STANDARD, 22, ["OK"])
    StuffDone["14_5"] = 1
