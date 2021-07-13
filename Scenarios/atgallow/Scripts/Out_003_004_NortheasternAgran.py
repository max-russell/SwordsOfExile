
def NortheasternAgran_2691_MapTrigger_9_19(p):
    result = ChoiceBox("You come to one of the many small farming villages in the Agran sector. Care to look around?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        MessageBox("You enter the village and try to start conversations with the farmers. However, none of them really has anything all that interesting to say.")
        return
    p.CancelAction = True

def NortheasternAgran_2692_MapTrigger_23_17(p):
    result = ChoiceBox("You find a small hut in this concealed scenic grove. A large rune is carved in the stone above the door. Care to see if anybody is home?", eDialogPic.TERRAIN, 190, ["Leave", "Yes"])
    if result == 1:
        result = ChoiceBox("A young mage comes to the door. He checks you over. \"Welcome, Empire soldiers. I am Analex. What brings you to my grove?\" You reply that you are on patrol. He smiles and says, \"Good, why don\'t you come in.\"\n\nYou enter and he speaks, \"Lately I\'ve been seeing many suspicious people in the forest. Many of them wearing dark colored red robes. I leave them alone, and they do the same for me. Otherwise I\'d blast \'em! Perhaps that may interest you.\n\nIt\'s not often that I receive visitors here and I\'m in need of money. I know a spell called \'Poison\' and would love to teach it to you for say, 250 gold. Do we have a deal?\"", eDialogPic.CREATURE, 26, ["Leave", "Accept"])
        if result == 1:
            if Party.Gold >= 250:
                Party.Gold -= 250
                MessageBox("He takes your gold and he begins to teach you the \'Poison\' spell. \"You will now be able to use magic to inject your opponents with a fairly strong toxin! Use it well.\"")
                for pc in Party.EachAlivePC():
                    pc.LearnSpell("m_poison")
                return
            MessageBox("He sighs. \"I see, the Empire really doesn\'t pay its soldiers much. If you manage to acquire the funds and are still interested, I\'d be more than happy to teach you.\"")
            p.CancelAction = True
            return
        MessageBox("\"Well if you change your mind, I\'ll be right here.\"")
        p.CancelAction = True
        return
    p.CancelAction = True

def NortheasternAgran_2693_MapTrigger_36_30(p):
    result = ChoiceBox("A small ruined hut lies on the shore. It looks like nobody has lived here for months. Care to look inside?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["16_3"] < 1:
            StuffDone["16_3"] = 1
            MessageBox("You look around the hut, but anything of value has been taken. Then you hear a high pitched voice, \"You\'re mine now! Hee, hee, hee!\" You turn around to see a small demon! He looks hungry.")
            WorldMap.SpawnNPCGroup("Group_3_4_4", p.Target)
            return
        MessageBox("This hut is still in the same shape as you left it. Nobody has dropped any treasure while you were gone.")
        return
    p.CancelAction = True

def NortheasternAgran_2695_MapTrigger_4_38(p):
    if StuffDone["16_4"] == 250:
        return
    StuffDone["16_4"] = 250
    WorldMap.AlterTerrain(Location(148,230), 1, None)
    WorldMap.DeactivateTrigger(Location(148,230))
    MessageBox("You come across some goblins hanging out by the lake. Unfortunately, they are looking to cause some trouble.")
    WorldMap.SpawnNPCGroup("Group_3_4_5", p.Target)

def NortheasternAgran_2696_MapTrigger_12_10(p):
    if StuffDone["100_0"] < 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You have reached the border of the Agran and the Imperial sectors. Unfortunately, this is where your jurisdiction ends. The guards at the border will not let you pass without appropriate authorization.")
        return
    MessageBox("This is the Agran-Imperial border. The guards at the bridge check your papers and allow you to proceed.")

def NortheasternAgran_2697_MapTrigger_12_5(p):
    if StuffDone["54_0"] == 250:
        return
    StuffDone["54_0"] = 250
    WorldMap.DeactivateTrigger(Location(156,197))
    ChoiceBox("You arrive at the Imperial Sector, the center of the Empire and the entire world. It is within this Sector that tens of thousands of decisions are made each day about public policy by various officials and bureaucrats.\n\nIt is here where most of Pralgad\'s soldiers (including you) are trained. Armies are housed within the sector to help maintain security and order. The protection of the capital of the Empire, Solaria, is paramount.\n\nThe Imperial Sector is probably the most densely populated sector in the world. Census figures say that about five million people live and work within the sector with jobs ranging from administration to clerical to maintenance.\n\nThe size will soon become apparent as you will see the many residential areas that dot the landscape. Each has its own name, but largely these dwellings are insignificant.\n\nThe Imperial Sector is also the largest consumers of resources. The upper class residents here tend to be the wealthiest in the world. The chief product of the Imperial Sector is policy, and little else also making it the most dependent.\n\nWelcome to the heart of the Empire!", eDialogPic.CREATURE, 130, ["OK"])

def NortheasternAgran_2698_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
