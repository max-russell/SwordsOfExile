
def Sanctuary_1309_MapTrigger_43_1(p):
    MessageBox("This stairway winds upward into the Archelder\'s chambers. You had better hurry, he could be back with reinforcements at any moment.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(21,18))
    p.CancelAction = True

def Sanctuary_1310_MapTrigger_60_62(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This stairway would take you back into the library. Leaving without conducting a search for anything interesting would not be advisable considering the amount of trouble it took to get in the Sanctuary.")

def Sanctuary_1311_MapTrigger_33_5(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(16,26)
    Party.MoveToMap(TownMap.List["Aerie_56"])

def Sanctuary_1312_MapTrigger_47_57(p):
    ChoiceBox("This way takes you into a room filled with all sorts of Gynites performing various tasks. For instance some are seated at learning crystals which interact directly with the mind, others are listening to a lecture by an elder, and so on.\n\nYou would say there would be around fifty Gynites ahead. You probably want to stay out of sight as much as possible. Going into this area would drastically increase your chances of getting caught.\n\nIt would be better not to go through this area unless you really have to.", eDialogPic.CREATURE, 1028, ["OK"])
    p.CancelAction = True

def Sanctuary_1313_MapTrigger_51_49(p):
    if StuffDone["50_9"] == 250:
        return
    StuffDone["50_9"] = 250
    TownMap.List["Sanctuary_55"].DeactivateTrigger(Location(51,49))
    ChoiceBox("These doors lead into a kind of discussion room. An elder, is having a discussion with several soldiers. Upon your entry, the Gynites look to see who has just entered. They all go back to their discussion.\n\nBut then one of the soldiers takes a closer look at you. \"Wait a minute, I remember you! You were the guests I let into the city earlier today. You\'re not supposed to be in here. I\'m afraid you are under arrest!\"\n\nThe other Gynites decide to assist the soldier in this. It looks like you have already encountered trouble.", eDialogPic.CREATURE, 1027, ["OK"])
    Town.PlaceEncounterGroup(1)

def Sanctuary_1314_MapTrigger_20_18(p):
    MessageBox("The stairway leads back down into the Archelder\'s lab.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(43,2))
    p.CancelAction = True

def Sanctuary_1315_MapTrigger_52_6(p):
    if StuffDone["51_5"] == 250:
        return
    StuffDone["51_5"] = 250
    TownMap.List["Sanctuary_55"].DeactivateTrigger(Location(52,6))
    TownMap.List["Sanctuary_55"].DeactivateTrigger(Location(53,6))
    Town.PlaceEncounterGroup(2)
    Animation_Explosion(Location(52,1), 2, "005_explosion")
    Animation_Hold()
    Wait()
    SuspendMapUpdate()
    for x in range(49, 57):
        for y in range(1, 7):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[224]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[222])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[222]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[224])
    ResumeMapUpdate()
    ChoiceBox("Inside this room is a man in the robes of a Gynite elder. However, he seems much more decorated than any of the others you have seen. This man may be the Archelder that people keep referring to.\n\nThe man turns around, surprised to see you. \"Who dares intrude into my chambers? Do you not know that access to these areas is strictly forbidden? Wait, I sense that you...are not from around here.\"\n\nYou sense him probing your mind. \"You are from the Empire! How dare you trespass onto these chambers. For this you will be strictly punished. Now you shall be one of the few outsiders to witness our true powers.\"\n\nHe waves his hand and the crystals around him begin to emit an eerie glow. It\'s almost as if they are coming to life!", eDialogPic.CREATURE, 1027, ["OK"])
    Animation_Explosion(Location(51,4), 2, "005_explosion")
    Animation_Hold()
    Wait()
    Animation_Explosion(Location(54,4), 2, "005_explosion")
    Animation_Hold()
    Wait()
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Elder_245": Town.NPCList.Remove(npc)
    Animation_Explosion(Location(52,3), 1, "005_explosion")
    Animation_Hold()
    Wait()

def Sanctuary_1318_MapTrigger_45_43(p):
    ChoiceBox("You sit down at this learning crystal and peer deep into it. The crystal seems to interact directly with your mind, much like the crystal on the strange machine in Morbane\'s Lair. Yet, this one seems much less alien and much easier to direct.\n\nYou discover information on pentagrams: Pentagrams are one of the oldest and most powerful tools used in spellcasting. The purpose of the pentagram is to invoke and banish elementals. Which elemental is determined by the way it is drawn.\n\nThe pentagram has five points, each corresponding to an element. Clockwise starting at the top, they are: spirit, water, fire, earth, and wind. To invoke elementals, one must start at an opposite point and immediately proceed to the invoking point.\n\nFor instance, to invoke earth and fire one must first start at the spirit point and then move to the invoked element point and then complete the rune ending at spirit. Ex. invoke earth is: spirit to earth, to water, to wind, to fire, and back to spirit.\n\nInvoking wind and water starts on the opposite point. For instance, to invoke water one begins on wind, goes to water, and completes the rune ending with wind. Banishing is important as only one elemental can be invoked at a time.\n\nTo banish, one begins at the point of the element one wishes to banish and draws the rune in reverse of the invoke path. Ex. banish earth is: earth to spirit, to fire, to wind, to water, and back to earth.", eDialogPic.TERRAIN, 247, ["OK"])

def Sanctuary_1319_MapTrigger_50_39(p):
    MessageBox("This stairway leads upward. You find yourself in a semi-spherical room. The floor slopes downward and meets at a basin. A large pentagram is inscribed at the basin of the spherical room.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(36,32))
    p.CancelAction = True

def Sanctuary_1320_MapTrigger_7_49(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(7,48)).Num == 145:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for n in range(Town.ItemList.Count - 1, -1, -1):
                i = Town.ItemList[n]
                if i.Pos == Location(8,53) and i.SpecialClass == 40:
                    Town.ItemList.Remove(i)
                    itemthere = True
                    break
        if itemthere == True:
            Animation_Hold(-1, 009_lockpick)
            Wait()
            MessageBox("You hear the doors click open as you approach. You turn around and look to find the offering table empty. It appears you have pleased the ancients.")
            SuspendMapUpdate()
            for x in range(7, 9):
                for y in range(48, 49):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        return

def Sanctuary_1321_MapTrigger_37_32(p):
    MessageBox("This stairway takes you back down to the area you entered the Sanctuary from.")
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(50,40))
    p.CancelAction = True

def Sanctuary_1323_MapTrigger_32_30(p):
    Animation_Hold(-1, 061_summoning)
    Wait()
    RunScript("GlobalCall_Sanctuary_2846", ScriptParameters(eCallOrigin.CUSTOM))

def Sanctuary_1324_MapTrigger_34_31(p):
    Animation_Hold(-1, 008_bubbles)
    Wait()
    RunScript("GlobalCall_Sanctuary_2847", ScriptParameters(eCallOrigin.CUSTOM))

def Sanctuary_1325_MapTrigger_33_33(p):
    Animation_Hold(-1, 073_fireimpact)
    Wait()
    RunScript("GlobalCall_Sanctuary_2848", ScriptParameters(eCallOrigin.CUSTOM))

def Sanctuary_1326_MapTrigger_31_33(p):
    Animation_Hold(-1, 060_smallboom)
    Wait()
    RunScript("GlobalCall_Sanctuary_2849", ScriptParameters(eCallOrigin.CUSTOM))

def Sanctuary_1327_MapTrigger_30_31(p):
    Animation_Hold(-1, 019_swordswish)
    Wait()
    RunScript("GlobalCall_Sanctuary_2850", ScriptParameters(eCallOrigin.CUSTOM))

def Sanctuary_1328_MapTrigger_25_33(p):
    Animation_Hold(-1, 068_identify)
    Wait()
    StuffDone["51_1"] = 0

def Sanctuary_1330_MapTrigger_40_29(p):
    Animation_Hold(-1, 008_bubbles)
    Wait()
    if StuffDone["51_0"] == 2:
        return
    p.CancelAction = True

def Sanctuary_1331_MapTrigger_10_18(p):
    if StuffDone["51_7"] == 0:
        StuffDone["51_7"] = 1
        Timer(Town, 3, False, "Sanctuary_1359_TownTimer_86", eTimerType.DELETE)
        if StuffDone["51_8"] == 250:
            return
        StuffDone["51_8"] = 250
        ChoiceBox("You enter this room and receive a view of that odd blue glow that you saw back at the reactor. This time it is coming from a small hole in the ceiling. From this hole, little bits of glowing dust fall to the floor.\n\nYou notice that there is a platform on the floor specifically for the glowing dust. In fact, a fairly large amount has been accumulated. This must be where the reactor dumps its waste products after the internal process is finished.\n\nYou swear that your skin begins to tingle and you are developing a headache from this dust in the air. It would probably be best not to breathe this air for long.", eDialogPic.STANDARD, 4, ["OK"])
        return

def Sanctuary_1332_MapTrigger_38_39(p):
    Animation_Hold(-1, 073_fireimpact)
    Wait()
    if StuffDone["51_0"] == 4:
        return
    p.CancelAction = True

def Sanctuary_1333_MapTrigger_26_39(p):
    Animation_Hold(-1, 060_smallboom)
    Wait()
    if StuffDone["51_0"] == 1:
        return
    p.CancelAction = True

def Sanctuary_1335_MapTrigger_7_27(p):
    if StuffDone["51_9"] == 250:
        return
    StuffDone["51_9"] = 250
    TownMap.List["Sanctuary_55"].DeactivateTrigger(Location(7,27))
    MessageBox("You open this cabinet only to find more of that glowing dust. Also contained are a few other metallic objects. It seems like this is some kind of an experiment of sort.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 3))

def Sanctuary_1336_MapTrigger_24_29(p):
    Animation_Hold(-1, 019_swordswish)
    Wait()
    if StuffDone["51_0"] == 3:
        return
    p.CancelAction = True

def Sanctuary_1337_MapTrigger_16_41(p):
    ChoiceBox("This crystal contains a supply of the engineering knowledge of Gynai. It details magical methods for growing stone and the creation of all sorts of interesting things. You do not understand most of it.\n\nThen you come across a reference to the enigmatic Dark Metal. It appears the Elders back at the city hall did know something about it, and not as much as they wanted to admit.\n\nGynai uses dark metal to power their entire city. Figures are given showing the relatively small amounts that are required to power the city. You would have thought there would be more.\n\nThe Engineering Elder told you the truth, mostly. The Gynai process the metal through a machine, a reactor, built thousands of years ago with the help of an alien race. They have theories about how the reactor works, but they are unsure.\n\nApparently the speeding of the inherent decay is the best guess they have come up with. How the machine does this producing energy is still beyond them. They dare not disassemble the machine fearing they would be unable to reassemble it.\n\nHowever, they have mastered the science of operating the machine. The details are highly technical and a bit advanced, but you manage to come off with enough of the details so that you might be able to do simple operations.", eDialogPic.TERRAIN, 168, ["OK"])
    StuffDone["51_2"] = 1

def Sanctuary_1338_MapTrigger_27_49(p):
    ChoiceBox("This crystal contains information on materials has a listing of important metals with a simplistic listing of special properties.\n\nMagnetic Metal - This group contains metals that have magnetic properties. This group contains lodestone and \'common gray\', or iron, which is highly attractive to magnets and is commonly used in all sorts of applications.\n\nNonmagnetic Metal - This group contains metals like silver which has applications in engineering as a non-magnetic substance. Also, many electrochemical reactions (whatever they are) involve silver.\n\nYellow Metal - This group is gold. Gold is highly malleable, yet very dense, and is often used while enchanting. It seems to have many magical properties. It also comments on practical uses as a trading good with the rest of the world.\n\nDark Metal - This group contains metals that decay or are radioactive. It contains metals like uranium, thorium, and a few other abstract ones. The decay is harmful to life, but can be used to cure diseases and the production of energy.\n\nHoly Metal - This is platinum, the most valuable metal to the Gynites. It\'s applications are countless in wiring to chemical reaction chambers. It also has great spiritual value for the Gynites, often being used in ceremony.", eDialogPic.TERRAIN, 168, ["OK"])

def Sanctuary_1339_MapTrigger_39_47(p):
    if StuffDone["51_4"] == 250:
        return
    StuffDone["51_4"] = 250
    TownMap.List["Sanctuary_55"].DeactivateTrigger(Location(39,47))
    ChoiceBox("You are in awe at the moment you enter this room. The ceiling here is quite high in the typical domed shaped room. This high ceiling is made to accommodate the piece of machinery in the center.\n\nYou have never seen anything quite like this before. This device is unbelievably complex. It can best be described as a massive well armored chamber with several rods leading from the ceiling. The machine emits an eerie blue glow.\n\nThe glow is unlike anything you have ever seen before. It is oddly pleasing to your senses. The air of this room crackles with electric energy much like magical labs, but this is definitely more powerful.\n\nAt the base of the device are alcoves where it seems something is made to be inserted. You wonder exactly what this machine is for.", eDialogPic.CREATURE, 88, ["OK"])

def Sanctuary_1340_MapTrigger_34_48(p):
    if StuffDone["51_2"] == 0:
        MessageBox("These are the controls to operate this enigmatic machine. You have no idea how to work these controls, let alone the processes involved with the machine. It would be best to leave these alone.")
        return
    if StuffDone["51_3"] == 0:
        result = ChoiceBox("These are the controls to the reactor you read about. It contains an assortment of dials, levers, buttons, and switches. Although it is a bit more complicated than you expected, you should still be able to use the controls safely.\n\nSitting at the panel, you give the controls a thorough examination. You are able to find all of the basic things mentioned in the instructions. You also notice that one of the reaction chambers, Chamber Epsilon, is currently inactive.\n\nRemembering the instructions, you check the safety system. It reveals that the chamber is ready to use, if you wanted to activate it for some reason. Unfortunately, you are unable to shut down the power while the reactions are in progress.\n\nSo if you start it, you will not be able to shut it off until the fuel has been consumed. This process can take several days. Also, you cannot shut any of the other reaction chambers down either.\n\nDo you want to activate the inactive chamber?", eDialogPic.STANDARD, 9, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for n in range(Town.ItemList.Count - 1, -1, -1):
                    i = Town.ItemList[n]
                    if i.Pos == Location(36,53) and i.SpecialClass == 39:
                        Town.ItemList.Remove(i)
                        itemthere = True
                        break
            if itemthere == True:
                Town.AlterTerrain(Location(36,53), 0, TerrainRecord.UnderlayList[139])
                StuffDone["51_3"] = 1
                Animation_Hold(-1, 053_magic3)
                Wait()
                ChoiceBox("Following the instructions you found in the learning crystal, you manage to run through the sequence successfully. When you are complete, a light comes on indicating the chamber is active.\n\nYou will now be able to use any device that required Chamber Epsilon to be active!", eDialogPic.TERRAIN, 168, ["OK"])
                return
            MessageBox("You do not get very far. About on the third step, the part where the fuel is injected, the machine beeps at you. You touch the mind crystal to learn that the appropriate reaction chamber requires fuel.")
            return
        return
    MessageBox("All of the chambers are currently active. There is no way at this point to shut them down. You could adjust the outputs, inputs, or some other minor settings, but there is little to do here right now.")

def Sanctuary_1341_MapTrigger_13_40(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 20:
        MessageBox("This crystal is packed full of all sorts of advanced magical knowledge. Just about all of it is far out of your grasp. However, you manage to decode a prayer that makes one an Avatar of the gods for a short time.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_avatar")
        return
    MessageBox("This crystal contains a hefty amount of complicated magical knowledge. You are having a very difficult time understanding any of this. Perhaps if you had more knowledge in this sort of thing?")

def Sanctuary_1342_MapTrigger_45_40(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(53,35)).Num == 90:
        result = ChoiceBox("These controls effect the water system of Gynai. An examination of them reveals they are pretty straight forward. There are more advanced settings such as gauge pressure and such, but the on/off switches are quite easy to use.\n\nAll except one of the water switches are active. The inactive one is for the flow in a series of streams within the Sanctuary called the Ceremony Tunnels. You have no idea what they are for, but you could fill them up from here.\n\nIt would be unwise to tinker with any of the other water switches. If you were to turn something off accidentally, that would definitely attract immediate attention. And attention is not something you want here.\n\nDo you pull the switch to activate the water flow to the Ceremony Tunnels?", eDialogPic.STANDARD, 18, ["Leave", "Pull"])
        if result == 1:
            if StuffDone["51_3"] >= 1:
                SuspendMapUpdate()
                for x in range(1, 64):
                    for y in range(1, 64):
                        if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
                        elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[90]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
                ResumeMapUpdate()
                SuspendMapUpdate()
                for x in range(36, 48):
                    for y in range(28, 39):
                        if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
                        elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[90]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
                ResumeMapUpdate()
                MessageBox("You pull the lever and hear the sounds of rushing water behind the walls. Apparently, these controls have activated the ceremony tunnels. Perhaps you should give them a search.")
                SuspendMapUpdate()
                for x in range(44, 63):
                    for y in range(46, 63):
                        if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[71]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
                        elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[90]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
                ResumeMapUpdate()
                return
            MessageBox("You pull the switch, but nothing happens. The board which shows the activated areas stays dark. You wait wondering if it is broken. You then notice a glowing mind crystal. Touching reveals that Power Chamber Epsilon is inactive.")
            return
        return
    MessageBox("It would be unwise to tinker with any of the other water switches. If you were to turn something off accidentally, that would definitely attract immediate attention. And attention is not something you want here.")

def Sanctuary_1343_MapTrigger_60_42(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(14,61))
    p.CancelAction = True

def Sanctuary_1344_MapTrigger_57_28(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(2,3))
    p.CancelAction = True

def Sanctuary_1345_MapTrigger_2_2(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(56,28))
    p.CancelAction = True

def Sanctuary_1347_MapTrigger_32_22(p):
    MessageBox("You step on this rune and it seems to scry you. After a few seconds the sensation stops. There is no apparent change in status.")

def Sanctuary_1348_MapTrigger_48_27(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(43,59))
    p.CancelAction = True

def Sanctuary_1349_MapTrigger_44_59(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(48,28))
    p.CancelAction = True

def Sanctuary_1352_MapTrigger_15_61(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(60,41))
    p.CancelAction = True

def Sanctuary_1353_MapTrigger_14_26(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. There is no sound or any indication that anything has happened.")
        t = Town.TerrainAt(Location(4,13))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(4,13), 0, TerrainRecord.UnderlayList[249])
        elif t == TerrainRecord.UnderlayList[249]: Town.AlterTerrain(Location(4,13), 0, TerrainRecord.UnderlayList[147])
        return

def Sanctuary_1354_MapTrigger_4_13(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(2,15))
    p.CancelAction = True

def Sanctuary_1355_MapTrigger_2_14(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(4,12))
    p.CancelAction = True
    StuffDone["51_7"] = 0

def Sanctuary_1356_MapTrigger_28_23(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. There is no sound or any indication that anything has happened.")
        t = Town.TerrainAt(Location(48,27))
        if t == TerrainRecord.UnderlayList[147]: Town.AlterTerrain(Location(48,27), 0, TerrainRecord.UnderlayList[249])
        elif t == TerrainRecord.UnderlayList[249]: Town.AlterTerrain(Location(48,27), 0, TerrainRecord.UnderlayList[147])
        return

def Sanctuary_1357_MapTrigger_18_57(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(38,24))
    p.CancelAction = True

def Sanctuary_1358_MapTrigger_37_24(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(19,57))
    p.CancelAction = True

def Sanctuary_1359_TownTimer_86(p):
    if StuffDone["51_7"] == 1:
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 1))
        Timer(Town, 3, False, "Sanctuary_1359_TownTimer_86", eTimerType.DELETE)
        if StuffDone["51_8"] == 250:
            return
        StuffDone["51_8"] = 250
        ChoiceBox("You enter this room and receive a view of that odd blue glow that you saw back at the reactor. This time it is coming from a small hole in the ceiling. From this hole, little bits of glowing dust fall to the floor.\n\nYou notice that there is a platform on the floor specifically for the glowing dust. In fact, a fairly large amount has been accumulated. This must be where the reactor dumps its waste products after the internal process is finished.\n\nYou swear that your skin begins to tingle and you are developing a headache from this dust in the air. It would probably be best not to breathe this air for long.", eDialogPic.STANDARD, 4, ["OK"])
        return

def Sanctuary_1360_CreatureDeath22(p):
    StuffDone["51_6"] += 1
    if StuffDone["51_6"] == 250:
        pass
    if StuffDone["51_6"] >= 4:
        Town.AlterTerrain(Location(48,4), 0, TerrainRecord.UnderlayList[142])
        ChoiceBox("Whew! Those Crystals sure were powerful. Although you have seen some pretty powerful enchantments, you have never seen inanimate objects cast spells like that. This furthers the possibility of that rumored omniscient living crystal.\n\nIf you wish to find out if those rumors are true, you better hurry. You doubt it will be long before the Archelder returns with overwhelming force. You only hope you can learn what is needed and escape before they organize.", eDialogPic.CREATURE, 88, ["OK"])
        return
