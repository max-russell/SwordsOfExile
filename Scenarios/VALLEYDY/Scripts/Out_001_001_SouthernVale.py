
def SouthernVale_410_MapTrigger_45_40(p):
    if StuffDone["204_1"] >= 1:
        MessageBox("You return to the spot where you met the drake. He still hasn\'t returned. Nothing is left to mark his presence but a few tracks and some carelessly shedded scales.")
        return
    if StuffDone["204_0"] >= 1:
        MessageBox("The drake is still here, and still dead. There is still nothing of value for you.")
        return
    if SpecialItem.PartyHas("DrakeFang"):
        if StuffDone["204_2"] >= 1:
            ChoiceBox("When you approach, Zorvas sniffs the air eagerly. Whatever he smells, it pleases him. He runs up to you. \"You are having the fang? Yes?\" You pull it out and show it to him.\n\n\"Wondrous!\" he responds. \"I knew I was smelling it! Be giving it? Yes?\" You hand it over. \"Excellent. Now for your reward. Be listening!\"\n\nHe begins to say a series of magical instructions in his thick, reptilian accent. You listen carefully, picking up as much of it as you can. You now know the spells Ice Bolt and Slow Group.\n\nThen, his debt discharged, Zorvas bends down and eats the Drake fang. It takes a while, and involves a bit of gnawing. Then, this done, he flies off without a word. You are alone.", eDialogPic.CREATURE2x1, 1, ["OK"])
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_slow_group")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_ice_bolt")
            StuffDone["204_1"] = 1
            return
        result = ChoiceBox("You are getting close to the end of this long, winding valley. When you look ahead, however, you see what could be trouble. It\'s a drake, a full forty feet from head to tail, and it\'s looking right at you!\n\nDrakes are vicious, blood-thirsty creatures. However, oddly, this one doesn\'t seem to want to attack you. It\'s just watching you. You can\'t help but wonder why.", eDialogPic.CREATURE2x1, 1, ["Leave", "Attack", "Approach"])
        if result == 1:
            MessageBox("You decide that it\'s best to play it safe and charge to attack. The drake was peaceful at first, but there\'s no way it\'s going to ignore this affront.")
            StuffDone["204_0"] = 1
            WorldMap.SpawnNPCGroup("Group_1_1_4", p.Target)
            return
            return
        elif result == 2:
            p.CancelAction = True
            ChoiceBox("You walk up to the drake. When you do, it surprises you by bowing its head in greeting. \"I am Zorvas,\" it says in a peculiar accent. \"I am here in the hopes of finding help, and my luck is here in you.\" It\'s hard to understand him.\n\n\"I am here to be striving for completing the tests to be a great Drake Lord, but there is one thing I am never finding in 30 years of looking. I need the tooth of a Drake Lord. I cannot this find.\"\n\n\"If you can be bringing this, I will reward you well and give you no harm. This a Drake\'s Oath I swear.\" He then spreads his wings and flies off. As he goes, he shouts \"Return here when it you are having. Luck to you!\" Then he is gone.", eDialogPic.CREATURE2x1, 1, ["OK"])
            StuffDone["204_2"] = 1
            return
        p.CancelAction = False
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You back away. Best to play it safe.")
        return
        return
    if StuffDone["204_2"] >= 1:
        MessageBox("Zorvas is still here, waiting patiently for the fang. When you arrive, he somehow seems to know you don\'t have it. He turns away from you without a single word.")
        return
    result = ChoiceBox("You are getting close to the end of this long, winding valley. When you look ahead, however, you see what could be trouble. It\'s a drake, a full forty feet from head to tail, and it\'s looking right at you!\n\nDrakes are vicious, blood-thirsty creatures. However, oddly, this one doesn\'t seem to want to attack you. It\'s just watching you. You can\'t help but wonder why.", eDialogPic.CREATURE2x1, 1, ["Leave", "Attack", "Approach"])
    if result == 1:
        MessageBox("You decide that it\'s best to play it safe and charge to attack. The drake was peaceful at first, but there\'s no way it\'s going to ignore this affront.")
        StuffDone["204_0"] = 1
        WorldMap.SpawnNPCGroup("Group_1_1_4", p.Target)
        return
        return
    elif result == 2:
        p.CancelAction = True
        ChoiceBox("You walk up to the drake. When you do, it surprises you by bowing its head in greeting. \"I am Zorvas,\" it says in a peculiar accent. \"I am here in the hopes of finding help, and my luck is here in you.\" It\'s hard to understand him.\n\n\"I am here to be striving for completing the tests to be a great Drake Lord, but there is one thing I am never finding in 30 years of looking. I need the tooth of a Drake Lord. I cannot this find.\"\n\n\"If you can be bringing this, I will reward you well and give you no harm. This a Drake\'s Oath I swear.\" He then spreads his wings and flies off. As he goes, he shouts \"Return here when it you are having. Luck to you!\" Then he is gone.", eDialogPic.CREATURE2x1, 1, ["OK"])
        StuffDone["204_2"] = 1
        return
    p.CancelAction = False
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You back away. Best to play it safe.")
    return

def SouthernVale_411_MapTrigger_20_13(p):
    ChoiceBox("This town can\'t have been ruins for long. You doubt it\'s been abandoned for more than five years or so. The giant lizards did fast work, however - they moved through, ate some things, tore everything else up, and left.\n\nBandits picked apart the rest.\n\nThere\'s nothing left here now, except for a grim warning of what the Vale will look like if the curse is left unchecked.", eDialogPic.TERRAIN, 85, ["OK"])

def SouthernVale_412_SpecialOnWin0(p):
    MessageBox("Now that the Drake is dead, you search eagerly for treasure. Unfortunately, you find nothing but gnawed bones and shedded scales. You\'re out of luck.")
