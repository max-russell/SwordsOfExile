
def ZaKhaziRunSouth_645_MapTrigger_10_15(p):
    if StuffDone["211_0"] >= 1:
        MessageBox("You reach the massive jumble of sharp rocks. Looking just under the surface of the water, you can see them all there, threatening to rip the bottom out of your boat.\n\nFortunately, you\'ve learned the route to pass them safely. Moving your boat carefully, you thread your way past the hazardous stones, and pass the blockage.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("As you being to pilot your boat into this narrow river, you begin to notice that there are jagged rocks just below the surface of the water.\n\nLooking closer, you realize that this stream is a deathtrap - someone has placed sharpened stalagmites all along the river floor. Trying to pass here without knowing the safe way through would be suicide. You back away.")

def ZaKhaziRunSouth_646_MapTrigger_38_45(p):
    result = ChoiceBox("The tunnel becomes very narrow. You don\'t hear or smell monsters, so you peek around inside. It was a good idea ... you realize that the walls are glittering. It\'s gold ore!\n\nWithout proper tools, it would take a while to dig the stuff out. However, you could still make a good bit of money with only a day or so of digging. Do you?", eDialogPic.TERRAIN, 241, ["No", "Yes"])
    if result == 0:
        MessageBox("Regretfully, you leave the gold behind. It would be a great deal, but only if you had more time.")
        return
    elif result == 1:
        if StuffDone["211_1"] >= 1:
            MessageBox("Unfortunately, you\'ve already dug out all the easy gold ore. You can\'t get any more out without more time and better tools.")
            return
        StuffDone["211_1"] = 1
        Party.Age += 2500
        MessageBox("You spend the better part of the day striking the rock with clubs and broken stalagmites, and picking out the nicer bits. Before long, you have a large sack of high quality gold ore, suitable for barter.")
        Party.Gold += 600
        return

def ZaKhaziRunSouth_647_MapTrigger_43_43(p):
    result = ChoiceBox("The tunnel becomes very narrow. You don\'t hear or smell monsters, so you peek around inside. It was a good idea ... you realize that the walls are glittering. It\'s gold ore!\n\nWithout proper tools, it would take a while to dig the stuff out. However, you could still make a good bit of money with only a day or so of digging. Do you?", eDialogPic.TERRAIN, 240, ["No", "Yes"])
    if result == 0:
        MessageBox("Regretfully, you leave the gold behind. It would be a great deal, but only if you had more time.")
        return
    elif result == 1:
        if StuffDone["211_2"] >= 1:
            MessageBox("Unfortunately, you\'ve already dug out all the easy gold ore. You can\'t get any more out without more time and better tools.")
            return
        StuffDone["211_2"] = 1
        Party.Age += 2500
        MessageBox("You spend the better part of the day striking the rock with clubs and broken stalagmites, and picking out the nicer bits. Before long, you have a large sack of high quality gold ore, suitable for barter.")
        Party.Gold += 600
        return

def ZaKhaziRunSouth_648_MapTrigger_22_7(p):
    if StuffDone["211_3"] == 250:
        return
    StuffDone["211_3"] = 250
    WorldMap.DeactivateTrigger(Location(22,535))
    ChoiceBox("Ugh. You\'ve detected a rank, unpleasant smell. You look around the corner into a large cavern and see small herds of pests. They mill around the cave, grazing on mushrooms and making unpleasant bleating noises.\n\nThe cave is filled with the ruinous pests of the surface world: unicorns. They\'re nasty critters, about four feet tall, tough and irritable, and with a nasty, sharp horn. The Empire must have teleported a bunch of them down here, knowingly or not.\n\nThe things are often cowardly, but they have been known to attack humans. You may want to tread carefully.", eDialogPic.CREATURE, 128, ["OK"])

def ZaKhaziRunSouth_649_MapTrigger_25_4(p):
    if StuffDone["211_6"] == 250:
        return
    StuffDone["211_6"] = 250
    WorldMap.DeactivateTrigger(Location(25,532))
    WorldMap.DeactivateTrigger(Location(30,533))
    WorldMap.DeactivateTrigger(Location(34,536))
    MessageBox("A group of unicorns have built up their courage and started stalking you. You try to lose them, but they start trotting after you. You have no choice but to fight them.")
    WorldMap.SpawnEncounter("Group_0_11_4", p.Target)

def ZaKhaziRunSouth_652_MapTrigger_31_43(p):
    if StuffDone["211_7"] == 250:
        return
    StuffDone["211_7"] = 250
    WorldMap.DeactivateTrigger(Location(31,571))
    WorldMap.DeactivateTrigger(Location(32,571))
    ChoiceBox("You sail out onto a large, subterranean lake. The green fungus light is unusually bright here, revealing large schools of pale cave fish swimming under the surface. Some of them boldly move close to look at you with eyes on tentacles, and swim away again.\n\nLooking around, you see the light of small fires to the northwest. Peering intently through the mist, you see a large island with a huge stone spire on it. Lights have been lit in windows in the spire. Someone must be living there!", eDialogPic.STANDARD, 31, ["OK"])
