
def HowlingGap_48_MapTrigger_44_42(p):
    if StuffDone["3_0"] == 250:
        return
    StuffDone["3_0"] = 250
    TownMap.List["HowlingGap_3"].AlterTerrain(Location(44,42), 1, None)
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(44,42))
    MessageBox("You find a narrow, winding track, circling an enormous stalagmite")

def HowlingGap_49_MapTrigger_39_29(p):
    if StuffDone["3_1"] == 250:
        return
    StuffDone["3_1"] = 250
    TownMap.List["HowlingGap_3"].AlterTerrain(Location(39,29), 1, None)
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(39,29))
    MessageBox("You nervously feel your way along the side of the towering stalagmite. Halfway up, you already have quite a view of the broken caves. Echoing slith voices make it clear to you that you are far from alone.\n\nYou hunch down and hope that no one will see you in this very vulnerable position.")

def HowlingGap_50_MapTrigger_39_47(p):
    if StuffDone["53_4"] == 250:
        return
    StuffDone["53_4"] = 250
    TownMap.List["HowlingGap_3"].AlterTerrain(Location(39,47), 1, None)
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(39,47))
    MessageBox("Echoing down this crack, you hear the faint and very human sound of weeping.")

def HowlingGap_51_MapTrigger_33_24(p):
    MessageBox("Your mountain track returns to a point just above the Brattaskar Road. You take a quick look, and are glad you turned away from the main road. Heavily armed sliths are patrolling the road. Progress there is almost impossible.")

def HowlingGap_52_MapTrigger_42_15(p):
    if StuffDone["3_4"] == 250:
        return
    StuffDone["3_4"] = 250
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(42,15))
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(51,24))
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(51,23))
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(50,24))
    MessageBox("You come across a small team of sliths holding large lizards by bronze chains. The lizards seem to be some kind of trackers, running with their noses to the ground. When you arrive, they raise their heads and wheeze, and their keepers let them loose.")

def HowlingGap_53_MapTrigger_10_16(p):
    MessageBox("The road seems to be under control of the sliths. You wonder if it is safe to continue this way.")

def HowlingGap_55_MapTrigger_26_21(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Peeking carefully around a bend in the road, you spot another group of sliths coming your way. You pull back hurriedly from the sight of steel spears and the silk robes of a mage.")

def HowlingGap_56_MapTrigger_40_34(p):
    ChoiceBox("From the top of the giant stalagmite you are rewarded with a terrific view of Howling Gap. Rock towers of all sizes litter the ground, stretching towards the drops from the low ceiling, just above your head. Most are dwarfed by this column.\n\nWhat draws your eye at this time, however, is not the view. You look carefully through the maze and see many slith patrols prowling through the jumble. Most stay near the main road, where you can see a small stone building.\n\nTo the south the cave opens up into a wide, but low cave. This is apparently where the slith campaign has made its headquarters. At the shores of a small lake, and even on floating platforms in the lake, hundreds of canvas tents have been erected.\n\nSeveral big, gaudily painted pavilions in the middle of the camp signify that some of the leaders of the army must be present. Huge bonfires are spread all over the cave. The cold outside the slith jungles must be getting to the lizards.\n\nSouth of the main camp is an open area. Under the direction of priests in shining robes, a crowd of worker sliths are dragging an apparently very heavy object covered by a canvas carpet. It takes ten sliths pulling ropes to move it.\n\nThe camp fires make the cave very bright, making it appear nearly impossible to sneak through the cave unseen.", eDialogPic.STANDARD, 29, ["OK"])

def HowlingGap_57_MapTrigger_59_29(p):
    if StuffDone["3_5"] == 250:
        return
    StuffDone["3_5"] = 250
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(59,29))
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(60,36))
    MessageBox("You squeeze through a narrow crack in the rock and down a steep slope. At the bottom you find a small, dark natural chamber. Its occupant reassures you that some of the tormented wailing that the wind carries actually comes from tormented souls.")

def HowlingGap_62_MapTrigger_52_7(p):
    if StuffDone["3_3"] == 250:
        return
    StuffDone["3_3"] = 250
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(52,7))
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(55,12))
    MessageBox("You stumble across a slith guard post. The cold-blooded lizards are shivering in the low temperature of the cave. As they leap up from their campfires, the sliths look just as unhappy with this encounter as you are.")

def HowlingGap_63_MapTrigger_60_4(p):
    if StuffDone["3_6"] >= 1:
        MessageBox("Your ears are still ringing with the loud sound of the gong. You are not about to sound it again.")
        return
    result = ChoiceBox("A large brass gong hangs from a pole next to the fire. It looks like some kind of alarm device. The guards did not strike it when you arrived, but perhaps they thought you weren?t trouble big enough to sound a general alarm.\n\nThey were wrong, it appears. Do you want to do their job for them?", eDialogPic.CREATURE, 49, ["Yes", "No"])
    if result == 0:
        MessageBox("You strike the gong with the brass club lying next to it and get an impressive, resounding boom from the disk. You now understand why the guards were hesitant to use the gong, as several stone stalactites are shattered by the sound and drop to the ground.\n\nThe sound still echoes through the maze, causing small rock slides, and, by the sounds of it, great anxiety from the slith patrols. You?d better be careful now.")
        StuffDone["3_6"] = 1
        for x in range(54, 60):
            for y in range(3, 6):
                if Maths.Rand(1,0,100) <= 70:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[97])
        return
        return
    elif result == 1:
        return

def HowlingGap_64_MapTrigger_35_41(p):
    if StuffDone["3_6"] >= 1:
        Timer(Town, 20, False, "HowlingGap_82_TownTimer_14", eTimerType.DELETE)
        MessageBox("The general alarm that you sounded has drawn several of the patrols into the corridors. If you hurry, you think you might nip across the road without being seen. Better be quick, though.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Peeking carefully around a bend in the road, you spot another group of sliths coming your way. You pull back hurriedly from the sight of steel spears and the silk robes of a mage.")

def HowlingGap_65_MapTrigger_23_43(p):
    StuffDone["3_7"] = 1
    if StuffDone["3_8"] == 250:
        return
    StuffDone["3_8"] = 250
    ChoiceBox("You dive through the door to get out of sight of the road. Only when you have slammed it shut behind you, you have time to take in the scene in front of you. It is another surprise.\n\nYou have been on your own among enemies for so long that the sight of humans is quite a shock. Especially when you stumble dramatically into a quiet, ordinary inn, full of calm, peaceful people.\n\nThey all startle and look up when you burst into the room, and the innkeeper by the bar takes a surprised step back. You suddenly feel silly for making such a fuss when entering. How can two so different realities be separated only by a door?\n\nThen you notice that everything is not well in here, either. Several of the people are wounded and bleeding. One man is unconscious, slumped over the table. Another was crying silently when you entered. He is now looking at you with hopeful eyes.\n\nYou suddenly notice that everyone is bound by heavy, bronze shackles. You enter the room warily. It is a gloomy place, with large windows overlooking the tunnels.\n\nEveryone is watching you expectantly, waiting for you to make the first move. Then the inn keeper waves at you to come over and talk.", eDialogPic.TERRAIN, 153, ["OK"])

def HowlingGap_69_MapTrigger_16_46(p):
    MessageBox("The atmosphere of the place is greatly heightened by this dramatic statue. It portrays a beautiful, young woman wringing her hands and crying. Soundlessly.")

def HowlingGap_71_MapTrigger_12_8(p):
    if StuffDone["3_9"] == 250:
        return
    StuffDone["3_9"] = 250
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(12,8))
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(12,7))
    MessageBox("A winding corridor with some signs of use burrows between giant stalagmites, away from the main road.")

def HowlingGap_73_MapTrigger_53_53(p):
    if StuffDone["53_0"] == 250:
        return
    StuffDone["53_0"] = 250
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(53,53))
    MessageBox("This cave lies lower than the other caverns, and pieces of rubble have drifted down here to clutter the room. The rubble has been arranged in tidy rows and piles, like some sentient being cleaning its lair and lovingly displaying its treasures.")

def HowlingGap_74_MapTrigger_30_10(p):
    MessageBox("It appears that the south wall of the corridor has caved in at this point, filling the cave with rocks, sharp points and rubble. You hope you can make it through. The stone twists into bizarre shapes, but you have no eye for art right now.")

def HowlingGap_76_MapTrigger_34_17(p):
    if StuffDone["53_1"] == 250:
        return
    result = ChoiceBox("You enter a small chamber inside a stalagmite. It is furnished to serve as a base for several people, but you find no traces to indicate for whom. The decoration is unfamiliar to you, but you cannot imagine it to be of human origin.\n\nWas the cave-in in the corridor outside meant to conceal this place? Or was it an attack? You might never find out. However, it has evidently been deserted for some time. As the occupants have left, they surely will not mind it if you borrow their chamber\n\nThe place is so well hidden that you feel certain that you could rest here for a period without being found. Care to try out these strange beds?", eDialogPic.TERRAIN, 165, ["Leave", "Rest"])
    if result == 1:
        StuffDone["53_1"] = 250
        TownMap.List["HowlingGap_3"].AlterTerrain(Location(34,17), 1, None)
        TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(34,17))
        MessageBox("You settle into the frail beds, trying to find comfortable positions without breaking them. Sleep is comfortable and quiet, but you eventually force yourselves to continue your mission.")
        Party.HealAll(50)
        for pc in Party.EachAlivePC():
            pc.SP+= 50
        return

def HowlingGap_77_MapTrigger_11_43(p):
    if StuffDone["53_2"] >= 1:
        result = ChoiceBox("You talk to the brave priestess for a while. She looks at your weapons and battle-worn confidence, then draws her breath to summon courage to speak.\n\n\"Listen,\" she says, \"your presence has given me hope. I now believe that we have a chance of saving these people,\" she nods at the frightened prisoners \"and get you out of Howling Gap at the same time.\n\n\"The sacrificial ceremony will be held at the field just south of the slith camp, where the tunnel widens out into the Chimney caves. If you were to join us, and hide among the other prisoners...\"\n\nHer voice fades off in embarrassment. She clearly is not used to making demands of others, and it dawns upon you what she asks: You must surrender to the sliths and face death at the ceremonial knives of the priests.\n\nYou flinch, but Karolynna meets your eye. You know that whatever you decide, she will meet the ceremonial death without blinking. And she is right: It is a chance for you to escape the maze of boulders.", eDialogPic.CREATURE, 132, ["Accept", "Refuse"])
        if result == 0:
            ChoiceBox("You agree with the priest?s desperate plan and stay with the prisoners, hiding among their numbers. As you sit down, fatigue overwhelms you, and you can barely move for aching muscles. You bury in warm animal skins and fall asleep.\n\nWhen you wake up, the slith guards have returned. They look into the prison, but do not count their prisoners or check on their manacles. You pull the skins over you to conceal your weapons, and are not noticed.\n\nYou spend some time dozing and talking to the other prisoners. They repeat the same story of a sudden attack by merciless sliths. Spencer brings you a meal of delicious mushrooms and you fall asleep again.\n\nKarolynna and Spencer shake you awake and whisper excitedly that something is happening outside. The sacrificial ceremony is about to begin.", eDialogPic.TERRAIN, 182, ["OK"])
            if Game.Mode != eMode.COMBAT:
                Party.Age += 500
                Party.HealAll(50)
                Party.RestoreSP(50)
            ChoiceBox("The front door slams open, and a small group of slith warriors enter. They usher you into the main room to face the dignitaries. Five or six priests eye you haughtily.\n\nAmong them is the biggest slith you have ever seen, fully two meters tall, with heavy muscles and almost glowing, green skin. He is clad in the ceremonial robes of a clan chieftain and wears a bronze sceptre shaped like a spear.\n\nEven in these stately circumstances, he is every bit the warrior, with suspicious eyes guarding the room. He carefully considers the prisoners, one by one. When he reaches you, he halts, and for a dreadful moment you think he has recognized you.\n\nThen he beckons for the guards to lead you all out. The prisoners move in a tight cluster in order to hide you, who wear no chains, but plenty of noisy weapons. You are led through the slith camp.\n\nHundreds of sliths line your path, leering and gloating. But when you arrive at the sacred ground south of the camp, only the priests and the chieftain escort you. The chieftain says a few words, then pulls out a silvery rod from his robes.\n\nHe hands this over to one of the priests, salutes them and leaves, along with the two high priests. This surprises you. Why should the dignitaries leave the ceremony, leaving it to common priests?", eDialogPic.CREATURE, 1025, ["OK"])
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(16,16)
            Party.MoveToMap(TownMap.List["SacredGround_4"])
            return
        elif result == 1:
            MessageBox("You awkwardly explain that you have other, important business to complete. She nods once in acceptance, never once showing that it is her own death sentence she is receiving. You feel her eyes in your back as you leave.")
            return
        return

def HowlingGap_79_MapTrigger_10_43(p):
    if StuffDone["53_3"] == 250:
        return
    StuffDone["53_3"] = 250
    TownMap.List["HowlingGap_3"].AlterTerrain(Location(10,43), 1, None)
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(10,43))
    MessageBox("This small, dark room is packed full of people. About twenty prisoners sit shackled along the walls. Some are dressed like merchants or travellers, others wear soldiers? tunics. Most are bruised, and several are unconscious.\n\nA woman is moving freely among the prisoners, offering water and laying bandages. She sighs as you enter, expecting more wounds to care for.")

def HowlingGap_81_MapTrigger_43_36(p):
    if StuffDone["3_2"] == 250:
        return
    StuffDone["3_2"] = 250
    TownMap.List["HowlingGap_3"].DeactivateTrigger(Location(43,36))
    MessageBox("You reach the highest point of the giant stalagmite, a place with excellent view of the area. Unfortunately, you are not the only ones to climb the rock and get an overview.\n\nA small group of sliths have watched you climb the path, and are waiting for you at the lookout post.")

def HowlingGap_82_TownTimer_14(p):
    if StuffDone["3_7"] >= 1:
        return
    MessageBox("You have been discovered! The slith patrol asks no questions, it simply charges.")
    Town.PlaceEncounterGroup(1)

def HowlingGap_83_OnEntry(p):
    if StuffDone["53_5"] == 250:
        return
    StuffDone["53_5"] = 250
    ChoiceBox("You are drawing near to a very scenic area, renowned through Exile and loved by poets for its haunting beauty. Under the present circumstances it is simply frightening.\n\nDue to differences in temperature in the neighbouring slith caves, air masses over Chimney are very turbulent. There is nearly always wind. Soft jungle breezes from the south are relieved by whipping wind from the upper caves or the occasional storm.\n\nThe place known as Howling Gap makes the wind almost visible. The ceiling hangs very low, in places stalactites touch the ground. Stalagmites stab angrily back at the ceiling in a jumble of boulders, rocky towers and fallen stone spears.\n\nAnd everywhere is the wind. Groping for a way through the stone maze, it tears at the rock columns, throws itself with full force at barely balancing boulders, causes rock slides and twists around at a junction to meet and wrestle with itself.\n\nThe struggling wind whistles through gaps, moans and sighs at narrow cracks. At times it rises to a roar, at other times it is just a faint whisper in the shadows behind you. It gives the impression of a maddened crowd, each voice calling for your help.\n\nYou pull your cloaks tightly around you as you enter this living landscape. Not really because of the cold. But because you already feel watched. A thousand small, moving stones and twigs could hide a slith assassin. Still, through you must.", eDialogPic.TERRAIN, 83, ["OK"])
