
def NorthernStolgrad_2323_MapTrigger_8_40(p):
    ChoiceBox("This institution is the training facility for the Stolgradian army. Stolgrad, unlike other sectors of Pralgad, is still under control of a line of nobility. Such lines have always had the authority to build and maintain their own military.\n\nThese forces are completely separate from the Imperial forces which you belong. Their allegiance is not really to the Emperor but to the ruler of Stolgrad, Auspire in this day.\n\nYou have heard that the forces of Stolgrad are generally better trained than most of the Empire\'s, a fact that Stolgrad commonly boasts. They claim that rigorous discipline, with strict punishments, and lucrative rewards pays off.\n\nRecruits are treated worse than the peasants and forced to live in unbearable conditions until they prove themselves. At which point, they gain considerable authority over the people.\n\nThey can behave how they choose, as there is no oversight of their powers. They can be cruel and ruthless. Additionally, only the soldiers and the authority has access to alcohol. Possession or consumption of such beverages by peasants is prohibited.\n\nStolgrad sure has their own way of doing things. You are glad you were not part of it.", eDialogPic.CREATURE, 13, ["OK"])
    p.CancelAction = True

def NorthernStolgrad_2324_MapTrigger_13_34(p):
    ChoiceBox("This is a Stolgradian military outpost. They are in control of maintaining security around the city as well as overseeing the mines. The city itself has its own soldiers assigned to patrol it.", eDialogPic.CREATURE, 20, ["OK"])
    p.CancelAction = True

def NorthernStolgrad_2326_MapTrigger_40_39(p):
    MessageBox("This is a residential area where many of the peasants of Stolgrad are housed. Conditions are cramped and there is literally a soldier on every street corner. There is a certain fear in the air here.")

def NorthernStolgrad_2328_MapTrigger_39_39(p):
    MessageBox("This is a residential area where many of the peasants of Stolgrad are housed. You manage to wander into a temple and have a chat with the priest. He offers to perform healing on you cheaply. You decide to look at his offer.")
    OpenHealingShop(0)
    p.CancelAction = True

def NorthernStolgrad_2329_MapTrigger_40_40(p):
    if StuffDone["46_8"] == 0:
        MessageBox("This is a residential are where many of the peasants of Stolgrad are housed. During your explorations, a merchant asks you to have a look at some hot merchandise, you decide to take a look.")
        result = ChoiceBox("You are pulled into a concealed back room. Here there is the set up of a moonshine distillery. The merchant grins. You notice that several of his teeth are missing.\n\n\"You\'re not from around here so you cannot appreciate this setup. You see, here in Stolgrad, it is illegal to possess or make any kind of alcohol. That is, unless you are a Stolgradian soldier or high up.\n\nDid you know that it is even illegal for you to possess alcohol? Even Empire soldiers are not exempt from this without special permission. This stuff is the highest quality that I make.\n\nI will sell you some of this contraband for only 20 gold! It\'s the only whiskey you are going to get for kilometers!\" Do you take him up on his offer? Sounds like you could get in trouble if you are caught.", eDialogPic.CREATURE, 1, ["Buy", "Refuse"])
        if result == 0:
            StuffDone["46_8"] = 1
            Animation_Hold(-1, 040_thankyou)
            Wait()
            Animation_Hold(-1, 018_drawingsword)
            Wait()
            ChoiceBox("As soon as you hand the gold to the merchant and are handed the bottles of moonshine, soldiers burst into the room. It was a set up all along! They were trying to entrap you, the dogs.\n\nThe captain approaches you. \"I\'m afraid you\'re under arrest for violated our laws about the possession and sale of contraband. This offense is punishable by death, please come with us.\"\n\nYou decide not to allow yourself to be arrested and fight back!", eDialogPic.CREATURE, 14, ["OK"])
            WorldMap.SpawnNPCGroup("Group_1_0_4", p.Target)
            return
        elif result == 1:
            MessageBox("You decide to turn down the offer. The merchant frowns. \"Ah well, there is always somebody else with some good taste.\"")
            return
        return
    MessageBox("This is a residential area where many of the peasants of Stolgrad are housed. Conditions are cramped and there is literally a soldier on every street corner. There is a certain fear in the air here.")

def NorthernStolgrad_2330_MapTrigger_40_33(p):
    ChoiceBox("This is a Stolgrad labor camp. The peasants are forced to arrive early every morning and work extensive hours with grueling tasks with little breaks and meager meals. They only get to leave late in the evening for a short rest before repeating the cycle.\n\nThese methods are rarely used by the Empire today. The only other place that really employs this harsh system is on Vantanas where peasants are forced to work the mines there.\n\nBehind these walls is where a lot of manufacturing is carried out. Stolgrad is second in manufacturing next to the neighboring Nelon Sector. All sorts of goods are assembled here ranging from furniture to weapons to clothing.\n\nYou have heard the ruling authority makes a killing by exporting these goods. Only the rejects, or ones of low quality, actually goes to the peasants.", eDialogPic.CREATURE, 2, ["OK"])
    p.CancelAction = True

def NorthernStolgrad_2331_MapTrigger_18_21(p):
    ChoiceBox("Stolgrad is also into the mining industry. Although the degree of productivity pales to that of the Mandahl Sector and Vantanas, Stolgrad still makes a fair amount of profits from the operations.\n\nThe chief products of this are marble and granite which are used heavily in construction. Also, there is a fairly rich supply of high quality iron ore. And, most notable, are the veins of rare metals with magical and industrial applications.\n\nOf course, the peasants work the mines tediously day and night. Working conditions are generally bad in the Stolgrad sector, but the mines are the absolute worst. Peasants typically work close to sixteen hours per day.\n\nNo wonder why the mines are so profitable. Cheap labor equals high profits for the Stolgradian authority.", eDialogPic.TERRAIN, 194, ["OK"])
    p.CancelAction = True

def NorthernStolgrad_2335_MapTrigger_7_24(p):
    if StuffDone["46_9"] == 250:
        return
    StuffDone["46_9"] = 250
    WorldMap.DeactivateTrigger(Location(55,24))
    Animation_Hold(-1, 043_stoning)
    Wait()
    ChoiceBox("You do not mind lizards all that much. Sure they can be pesky from time to time, but they are usually easy to deal with. However, there is one kind of lizard you absolutely hate to deal with.\n\nUnfortunately, you have to face this occasion at this moment. You are confronted by several deadly basilisks who do not like you intruding onto their lair.", eDialogPic.CREATURE, 86, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_0_5", p.Target)

def NorthernStolgrad_2336_MapTrigger_34_15(p):
    if StuffDone["47_0"] == 250:
        return
    StuffDone["47_0"] = 250
    WorldMap.DeactivateTrigger(Location(82,15))
    Animation_Hold(-1, 014_missile)
    Wait()
    ChoiceBox("Desolate areas such as the rocky mountains in northern Stolgrad make excellent hiding places for some of the more hunted races. One of them are the Hill Giants who are largely considered pests because of their continued hostility to the Empire.\n\nA group of these arrogant giants has decided to start flinging rocks at you. You manage to dodge the first volley and the giants move in closer for a better shot.", eDialogPic.CREATURE1x2, 0, ["OK"])
    WorldMap.SpawnNPCGroup("Group_1_0_6", p.Target)

def NorthernStolgrad_2337_MapTrigger_8_13(p):
    if StuffDone["47_1"] == 0:
        result = ChoiceBox("At the edge of this mountain you encounter some interesting rocks. You would swear some of them emit a slight glow. The metal lumps are very heavy and feel unusually cool. They could be valuable.", eDialogPic.STANDARD, 30, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("Uraniumbar_333")
            StuffDone["47_1"] = 1
            return
        return

def NorthernStolgrad_2338_WanderingOnMeet1(p):
    if StuffDone["9_0"] >= 7:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    if StuffDone["9_0"] < 3:
        RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
        return
        return
    if Maths.Rand(1,0,100) < 35:
        MessageBox("You encounter a Stolgradian patrol. They stop you, ask questions, and check your papers. Unfortunately, one of them realizes that you are wanted by the authorities. You decide not to go peacefully.")
        return
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NorthernStolgrad_2341_SpecialOnWin0(p):
    MessageBox("You manage to kill off the Stolgradian soldiers. You have just committed another crime that is punishable by death. Two in one day, not a good record. You wonder how anyone survives the law out here. Just hope nobody finds out about this.")

def NorthernStolgrad_2342_SpecialOnFlee0(p):
    MessageBox("You manage to elude the authorities. Just hope they do not come looking for you.")
