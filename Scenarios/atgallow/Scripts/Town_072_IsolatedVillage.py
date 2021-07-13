
def IsolatedVillage_1807_MapTrigger_18_20(p):
    if StuffDone["56_4"] == 1:
        Town.AlterTerrain(Location(18,18), 0, TerrainRecord.UnderlayList[247])
        return

def IsolatedVillage_1808_MapTrigger_18_18(p):
    if StuffDone["56_4"] == 1:
        result = ChoiceBox("At last, some comfortable beds! You examine the beds finding them a bit dusty. You are about to relax when you notice a little spark from the dresser. Probably just your imagination.\n\nThe air in this room seems to be making you very tired. Do you want to lay down and rest, or do you want to wait a bit longer.", eDialogPic.TERRAIN, 230, ["Wait", "Rest"])
        if result == 0:
            return
        elif result == 1:
            Animation_Hold(-1, 019_swordswish)
            Wait()
            MessageBox("You decide to lay down and rest. You quickly fall into a deep sleep, so deep that you do not feel a thing when you are mauled to death in your sleep.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        return

def IsolatedVillage_1809_MapTrigger_18_16(p):
    if StuffDone["56_4"] == 1:
        StuffDone["56_4"] = 2
        ChoiceBox("You begin to conduct a search of the dresser, pulling out drawers. You discover them empty, but as you start to fool around more, the dresser begins to spark more! Eventually it begins to start to fade revealing a humanoid form.\n\nUh oh! This appears to be some kind of trap.", eDialogPic.TERRAIN, 145, ["OK"])
        Town.AlterTerrain(Location(18,16), 0, TerrainRecord.UnderlayList[170])
        Town.AlterTerrain(Location(18,18), 0, TerrainRecord.UnderlayList[170])
        Town.PlaceEncounterGroup(1)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Townsperson_2": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Townsperson_4": Town.NPCList.Remove(npc)
        return

def IsolatedVillage_1810_MapTrigger_27_14(p):
    MessageBox("As you kill the Rakshasa, the creature disintegrates. You notice that he was wearing a wickedly sharp claw around his neck. Looks very intriguing.")
    Town.PlaceItem(Item.List["RakshasaClaw_394"].Copy(), Location(25,16))

def IsolatedVillage_1811_MapTrigger_50_32(p):
    if StuffDone["56_6"] == 0:
        result = ChoiceBox("This is a statue of a large humanoid Tiger. You believe this race is called Rakshasa and is supposedly extinct. On its forehead, you notice a large shiny black claw sitting in an alcove ready to take.", eDialogPic.TERRAIN, 133, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("RakshasaClaw_394")
            StuffDone["56_6"] = 1
            MessageBox("You have to pry the claw loose from the alcove, but it does not prove too difficult. However, this act is not without punishment. You turn to see the trees reformed into several creatures, some of them Rakshasi!")
            Town.PlaceEncounterGroup(2)
            SuspendMapUpdate()
            for x in range(47, 54):
                for y in range(29, 36):
                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[113]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[3])
                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[3]:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[113])
            ResumeMapUpdate()
            return
        return

def IsolatedVillage_1812_MapTrigger_16_32(p):
    if StuffDone["56_7"] < 2:
        foundit = False
        if Game.Mode != eMode.OUTSIDE:
            for x in range(Town.Width):
                for y in range(Town.Height):
                    if Town.FieldThere(Location(x,y), Field.BARREL):
                        foundit = True
                        break
                if foundit == True: break
        if foundit == True:
            ChoiceBox("You sit and open the tome, and it begins to speak. \"Greetings! I am Frankie and welcome to my abode. Now listen carefully, there is a barrel in the other room that I need dumped into the fountain.\n\nIf you can help me with my evil plans, I will give you the rewards in that chest over there!\" You look behind you to see a chest materialize. \"Imagine the treasure that could be inside. You would be rich!\"\n\nThere is a pause. \"Of course, you will need to get the barrel to the fountain, but that should not be too much trouble I presume. Excellent, everything is going according to my evil plans! Mwa, ha, ha, ha, ha, ha, ha!\"\n\nThe book continues to laugh uncontrollably for some time before quieting down. Is it any wonder that they chose to lock this tome away?", eDialogPic.TERRAIN, 130, ["OK"])
            StuffDone["56_7"] = 1
            Town.AlterTerrain(Location(18,31), 0, TerrainRecord.UnderlayList[194])
            return
        StuffDone["56_7"] = 2
        Town.AlterTerrain(Location(18,31), 0, TerrainRecord.UnderlayList[170])
        Town.PlaceEncounterGroup(3)
        MessageBox("You return to the tome. \"Excellent! Everything is going according to my evil plans. Now, for your reward. Mwa, ha, ha!\" There is a burst of light, the chest transmutes into a Rakshasa! \"At last I am free from that stupid book. Now for your final reward!\"")
        Animation_Explosion(Location(18,31), 2, "005_explosion")
        Animation_Hold()
        Wait()
        return

def IsolatedVillage_1813_MapTrigger_18_31(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(18,31)).Num == 194:
        MessageBox("The chest is sealed tightly by a strange force. You cannot get it open.")
        return

def IsolatedVillage_1814_MapTrigger_16_41(p):
    MessageBox("As you kill the Rakshasa, the creature disintegrates. You notice that he was wearing a wickedly sharp claw around his neck. Looks very intriguing.")
    Town.PlaceItem(Item.List["RakshasaClaw_394"].Copy(), Location(18,31))

def IsolatedVillage_1815_MapTrigger_16_34(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(15,34)).Num == 186:
        result = ChoiceBox("You sit at the tome and it begins to speak. \"Hi there kids! I\'m Chuckles. My what a fine day this is! Do you know what time it is? Why it\'s riddle time of course! Tell me, do you want to try and solve my riddles?\"", eDialogPic.TERRAIN, 130, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            MessageBox("A pen suddenly appears! \"You must write your answers in this book to all the question I ask. The only rule is that there are no numbers allowed! Okay?\" Now, shall we get started.\n\nNow here\'s the first one: What is four plus six? Ten or tin?")
            response = InputTextBox("Enter something:", "")
            response = response[0:3].upper()
            if response == "TEN":
                MessageBox("\"All right, that was too easy. Now, what whole number comes after nine, tin or ten?\"")
                response = InputTextBox("Enter something:", "")
                response = response[0:3].upper()
                if response == "TEN":
                    MessageBox("\"I see you know that then. Well then what is five times two? Is it tin or is it ten?\"")
                    response = InputTextBox("Enter something:", "")
                    response = response[0:3].upper()
                    if response == "TEN":
                        MessageBox("\"All right then, what is an aluminum can made out of?\"")
                        response = InputTextBox("Enter something:", "")
                        response = response[0:5].upper()
                        if response == "ALUMI":
                            MessageBox("\"Okay, now decipher this message.\" A stream of text appears on the page: SIHT EGASSEM LLIW FLES TCURTSED NI EVIF SDNOCES. HAVE A NICE DAY!")
                            Town.AlterTerrain(Location(15,34), 0, TerrainRecord.UnderlayList[170])
                            Animation_Explosion(Location(15,34), 0, "005_explosion")
                            Animation_Hold()
                            Wait()
                            Party.Damage(Maths.Rand(5, 1, 6) + 15, eDamageType.FIRE)
                            Wait()
                            StuffDone["56_9"] = 1
                            SuspendMapUpdate()
                            for x in range(13, 16):
                                for y in range(33, 36):
                                    if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[122]:
                                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[166])
                                    elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[166]:
                                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[122])
                            ResumeMapUpdate()
                            return
                        MessageBox("\"Gets \'em all the time! Suckers!\" You feel some of your life force be sucked out of you. \"Care to try again?\"")
                        for pc in Party.EachAlivePC():
                            pc.AwardXP(-25)
                        return
                    MessageBox("\"Gets \'em all the time! Suckers!\" You feel some of your life force be sucked out of you. \"Care to try again?\"")
                    for pc in Party.EachAlivePC():
                        pc.AwardXP(-25)
                    return
                MessageBox("\"Gets \'em all the time! Suckers!\" You feel some of your life force be sucked out of you. \"Care to try again?\"")
                for pc in Party.EachAlivePC():
                    pc.AwardXP(-25)
                return
            MessageBox("\"Gets \'em all the time! Suckers!\" You feel some of your life force be sucked out of you. \"Care to try again?\"")
            for pc in Party.EachAlivePC():
                pc.AwardXP(-25)
            return
        return

def IsolatedVillage_1816_MapTrigger_33_28(p):
    if StuffDone["57_0"] < 5:
        result = ChoiceBox("These runes depict the five fingered hand of a some kind of feline, perhaps a Nephilim. However, at each of the five fingertips are small alcoves that resemble claws. You wonder if something belongs in its place.\n\nCare to attempt and put things there?", eDialogPic.TERRAIN, 106, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            if Party.CountItemClass(46, False) > 0:
                if StuffDone["57_0"] < 5:
                    if Party.CountItemClass(46, True) > 0:
                        StuffDone["57_0"] += 1
                        if StuffDone["57_0"] == 250:
                            TownMap.List["IsolatedVillage_72"].DeactivateTrigger(Location(33,28))
                        RunScript("Loopback_55_1", p)
                        return
                    MessageBox("You fill in some of the alcoves with the claws you discovered. However, there is still at least one unoccupied alcove.")
                    return
                MessageBox("You place a claw in each of the alcoves. Immediately after placing the last one, openings appear in the walls to the sides of the claw diagram allowing you access.")
                SuspendMapUpdate()
                for x in range(32, 35):
                    for y in range(28, 29):
                        if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[139]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
                        elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[170]:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[139])
                ResumeMapUpdate()
                if StuffDone["57_1"] >= 1:
                    Town.AlterTerrain(Location(33,38), 0, TerrainRecord.UnderlayList[142])
                    return
                return
            MessageBox("Alas, you have nothing to place in the alcoves.")
            return
        return
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,28)).Num == 139:
        MessageBox("You place a claw in each of the alcoves. Immediately after placing the last one, openings appear in the walls to the sides of the claw diagram allowing you access.")
        SuspendMapUpdate()
        for x in range(32, 35):
            for y in range(28, 29):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[139]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[170]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[139])
        ResumeMapUpdate()
        if StuffDone["57_1"] >= 1:
            Town.AlterTerrain(Location(33,38), 0, TerrainRecord.UnderlayList[142])
            return
        return

def IsolatedVillage_1817_SanctifyTrigger_33_34(p):
    if p.Spell.ID != "p_sanctify":
        return
    if StuffDone["57_1"] == 0:
        Town.AlterTerrain(Location(33,34), 0, TerrainRecord.UnderlayList[166])
        Animation_Explosion(Location(33,34), 0, "005_explosion")
        Animation_Hold()
        Wait()
        Animation_Hold(-1, 023_startoutdoorcombat)
        Wait()
        Town.PlaceEncounterGroup(4)
        MessageBox("You cast the ritual of sanctification on the Rakshasi altar. As far as altars go, it was not that difficult to tackle. Upon completion of the ritual, the basalt slab explodes leaving a pile of rubble! Unfortunately, you have trouble on your hands.\n\nThe Rakshasi are outnumber and overpower you by many times. Then you notice a door behind you. You could have sworn that was not there before. Better head for it before you are toast.")
        StuffDone["57_1"] = 1
        Town.AlterTerrain(Location(33,38), 0, TerrainRecord.UnderlayList[142])
        return

def IsolatedVillage_1818_MapTrigger_33_38(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(33,38)).Num == 142:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(32,43))
        p.CancelAction = True
        return

def IsolatedVillage_1819_MapTrigger_32_42(p):
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return
    Party.Reposition(Location(33,37))
    p.CancelAction = True

def IsolatedVillage_1821_MapTrigger_32_49(p):
    if StuffDone["57_2"] == 250:
        return
    StuffDone["57_2"] = 250
    TownMap.List["IsolatedVillage_72"].DeactivateTrigger(Location(32,49))
    TownMap.List["IsolatedVillage_72"].DeactivateTrigger(Location(33,49))
    Town.PlaceEncounterGroup(5)
    Animation_Explosion(Location(1,1), 2, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("The Rakshasi are in hot pursuit of you, looking to take revenge for invading their village and desecrating their shrine. Then the runes on the floor along the side of the hallway begin to glow a dull crimson color.\n\nAll the action stops. You and the Rakshasi are frozen into place for several seconds. It feels as if some magical force is scrying you, trying to determine your identity. Suddenly, you realize you can move again!\n\nYou look to see your foes only to find that they have vanished! This is getting very suspicious. You wonder why you remain and what the heck is down here.", eDialogPic.CREATURE, 104, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Rakshasa_135": Town.NPCList.Remove(npc)
    Animation_Hold(-1, 068_identify)
    Wait()

def IsolatedVillage_1823_MapTrigger_31_19(p):
    if StuffDone["56_4"] >= 2:
        Town.PlaceEncounterGroup(1)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Townsperson_2": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Townsperson_4": Town.NPCList.Remove(npc)
        return

def IsolatedVillage_1825_MapTrigger_32_50(p):
    Town.PlaceEncounterGroup(6)
    if StuffDone["57_3"] == 250:
        return
    StuffDone["57_3"] = 250
    ChoiceBox("How very interesting! Beyond the runed hallway is a large hollowed out room of strange alien decor. In the center of the rune is a large pillar inscribed with runic markings.\n\nAt first you think the purpose of the pillar is to hold the dome up, but you realize that cannot be the case. The pillar is a twisted mesh of stones, bubbles, and glowing markings. It radiates flickers of light all about.\n\nIt is quite an alien site to see this strange pillar. You have no idea yet what this is for, yet you can almost sense that it has a certain intelligence to it.\n\nThe amazement of this gallery does not end there. At the other end is a complicated configuration of focusing crystals and runic markings. It resembles that used for mass teleportation, but is quite unlike any you have ever seen.\n\nYou wonder who built this place and why you, and not the Rakshasi, were allowed to see it. It is not likely that they constructed this then, but then who did? Perhaps further exploration can answer some questions.", eDialogPic.TERRAIN, 106, ["OK"])

def IsolatedVillage_1827_MapTrigger_7_50(p):
    if SpecialItem.PartyHas("BlessedAtheme"):
        MessageBox("The crystal contains information on the Blessed Atheme. You have already read all of the important parts.")
        return
    result = ChoiceBox("You peer into this crystal and find notes about the discovery of a special kind of object, a knife. The builders of this place were very intrigued by the material which the blade is forged with.\n\nIt seems the knife was discovered about four years ago by the Rakshasi (or the specimens, as they are referred to). The creators of this place were intrigued and decided to take the knife to study it.\n\nIt has a metal unlike any they have ever seen. The molecular matrix of the metal is astoundingly complex and the creators have not really managed to study it in depth due to \"more urgent matters\". It does not elaborate on that.\n\nYou notice that the knife sits on the dais to the the side. Upon closer look, you see the blade has a kind of brilliant white glow about it. Etched into the blade is a black pentagram. The blade itself looks wickedly sharp.\n\nYou believe this artifact is called the \'Blessed Atheme\', a legendary knife that can cut through anything. You may take it if you wish.", eDialogPic.STANDARD, 2, ["Leave", "Take"])
    if result == 1:
        SpecialItem.Give("BlessedAtheme")
        return
    StuffDone["54_2"] = 2

def IsolatedVillage_1828_MapTrigger_53_55(p):
    ChoiceBox("This crystal contains the basic information on why this bunker is here. It was created by a group of mages working on something called Applied Theoretics in Political Science (ATPS), a mathematical method of predicting political events.\n\nYou gather the mages were from a place called a parallel universe, an alternate reality. Apparently travel between \'parallel universes\' is very difficult and risky (32% failure rate), however, information can be sent with high success.\n\nThe device in the central chamber is the \'transmitter\' which allows the flow of information between the two. It appears that these mages wish to test their theories, but cannot do so in the confines of one universe to do so.\n\nIn fact, the mages are trying to duplicate, as close as possible, the features of their universe to test their theories. This reality was chosen because of its geological and biological resemblance. However, a few races are missing e.g. Rakshasi.\n\nThis bunker is used to engineer the race, yet they are having some problems. This place was built about 25 years ago, their time. However, time flows differently in different realities. The conversion factor is their 1 year equals 72.63 of ours.\n\nThat must mean this place is older than the Empire! Could it be that this experiment was responsible for the formation of your nation? It mentions that knowledge had to be restricted. You wonder how much influence they have really had.", eDialogPic.STANDARD, 16, ["OK"])

def IsolatedVillage_1829_MapTrigger_49_55(p):
    ChoiceBox("This crystal gives information on the Rakshasi. It appears this bunker was created for the purpose of engineering the Rakshasi race to \"further match conditions of our reality\", whatever that means.\n\nTheir first attempt was about eight years ago, their time (\"footnote: conversion factor os 1:72.63 years\"). Although they had perfectly duplicated the Rakshasi long ago, they did not count on slight differences in the environment.\n\nThe Rakshasi have an unusually complicated and sensitive cellular matrix that allows for the absorption of energy. The problem is our atmosphere has a slightly different composition to theirs, which slowly destabilizes the matrix.\n\nIt appears that the first effects are observed at third or fourth generation which include shortened life and limited mental capabilities. The problem worsens exponentially with each generation until complete sterility.\n\nTo perform their experiments properly, they must adjust the matrix to allow complete stability as \"Rakshasi play an integral role in our politics.\" It appears their first attempt was scrapped about four of their years ago.\n\nThis would explain the mysterious disappearance of all Rakshasi about three centuries ago. Apparently, progress is being made and they believe they are on the \"verge of a breakthrough\".", eDialogPic.CREATURE, 104, ["OK"])

def IsolatedVillage_1830_MapTrigger_51_55(p):
    MessageBox("This crystal runs an interesting sequence. It displays a complex pattern of lines, circles, and polygons and shortly after it breaks apart. Afterward, it begins the cycle with a slightly different pattern. You wonder what this means.")

def IsolatedVillage_1831_MapTrigger_51_51(p):
    MessageBox("Beyond this stage is the body of a Rakshasa. It does not appear to be cognizant in any way. The crystals fire beams on the creature seeming to carefully analyze it. Perhaps the people here are studying the Rakshasi.")

def IsolatedVillage_1832_MapTrigger_11_50(p):
    MessageBox("This crystal appears to be concentrating on geography. It displays two images: a map of the area, and a more focused area. The focused area is streaming through very quickly, too fast for your eyes. This crystal is tracking all the Rakshasi!")

def IsolatedVillage_1833_MapTrigger_11_59(p):
    MessageBox("This crystal contains information on other races. It mentions that to \"equalize conditions\" seventeen races had to be either eliminated or minimized. It seems they did this using the Imperial purges.\n\nHowever, five races had to be engineered. These are the Rakshasi (the only one you know of), the Colidon, the Mantcore, the Undine, and the Lyron. Apparently, the Rakshasi has been the most difficult to engineer of the five.")

def IsolatedVillage_1834_MapTrigger_7_59(p):
    MessageBox("This crystal is running through a lot of numbers and symbols much faster than you can read. It is fair to say that you will learn no useful information from this crystal.")

def IsolatedVillage_1837_TalkingTrigger1(p):
    StuffDone["56_4"] = 1

def Loopback_55_1(p):
    if StuffDone["57_0"] < 5:
        if Party.CountItemClass(46, True) > 0:
            StuffDone["57_0"] += 1
            if StuffDone["57_0"] == 250:
                TownMap.List["IsolatedVillage_72"].DeactivateTrigger(Location(33,28))
            RunScript("Loopback_55_1", p)
            return
        MessageBox("You fill in some of the alcoves with the claws you discovered. However, there is still at least one unoccupied alcove.")
        return
    MessageBox("You place a claw in each of the alcoves. Immediately after placing the last one, openings appear in the walls to the sides of the claw diagram allowing you access.")
    SuspendMapUpdate()
    for x in range(32, 35):
        for y in range(28, 29):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[139]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[170])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[170]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[139])
    ResumeMapUpdate()
    if StuffDone["57_1"] >= 1:
        Town.AlterTerrain(Location(33,38), 0, TerrainRecord.UnderlayList[142])
        return
