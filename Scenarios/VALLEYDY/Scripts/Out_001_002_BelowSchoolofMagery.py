
def BelowSchoolofMagery_435_MapTrigger_16_5(p):
    if StuffDone["207_0"] == 250:
        return
    StuffDone["207_0"] = 250
    WorldMap.DeactivateTrigger(Location(64,101))
    ChoiceBox("You step out of the School of Magery into a long, subterranean, natural gallery. A wide stone path leads to the south, stretching far beyond sight.\n\nThe bits of bone, claw marks, and blood stains that dot the path at regular intervals clearly tell you that all is not calm and peaceful down here. The creatures that escaped the School had to go somewhere.\n\nAs you walk out, you see several of the creatures that made this area their home. They look similar to wolves, but have six legs, shaggy fur, and vicious, jagged teeth, and seem far, far fiercer.\n\nThe small pack that has sighted you leaps to its feet and charges toward you with long, even strides. Sadly, you have little doubt that these caves are inhabited by many more creatures just like these ...", eDialogPic.CREATURE, 126, ["OK"])
    WorldMap.SpawnEncounter("Group_1_2_4", p.Target)

def BelowSchoolofMagery_436_MapTrigger_19_17(p):
    if StuffDone["207_1"] == 250:
        return
    StuffDone["207_1"] = 250
    WorldMap.DeactivateTrigger(Location(67,113))
    WorldMap.DeactivateTrigger(Location(68,113))
    MessageBox("As you continue south, you hear the distant, raspy howls of the alien beasts. Somehow, they have sensed the presence of new, tasty morsels, and are preparing for your advance.")

def BelowSchoolofMagery_438_MapTrigger_6_28(p):
    if StuffDone["207_2"] == 250:
        return
    StuffDone["207_2"] = 250
    WorldMap.DeactivateTrigger(Location(54,124))
    WorldMap.DeactivateTrigger(Location(56,124))
    WorldMap.SpawnWanderingGroup()

def BelowSchoolofMagery_440_MapTrigger_21_40(p):
    if StuffDone["207_3"] == 250:
        return
    result = ChoiceBox("You find a small natural spring. That sort of thing isn\'t unusual underground. What\'s odd about this fountain is that the water is glowing slightly. Whether that\'s because of rare mineral deposits, or some strange magical effect, you aren\'t sure.\n\nBeing adventurers, of course, you\'re strongly tempted to drink the stuff. It doesn\'t smell polluted, at any rate.", eDialogPic.STANDARD, 18, ["Leave", "Drink"])
    if result == 1:
        StuffDone["207_3"] = 250
        WorldMap.AlterTerrain(Location(69,136), 1, None)
        WorldMap.DeactivateTrigger(Location(69,136))
        MessageBox("The water is amazingly fresh and invigorating. Drinking it makes you feel ready to take on a thousand alien beasts! You bend down to drink more, but are saddened to find that the glow is faded.\n\nYou\'ve drained the magic for now. You\'ll have to find future healing elsewhere.")
        Party.HealAll(30)
        return

def BelowSchoolofMagery_441_MapTrigger_44_26(p):
    if StuffDone["207_4"] == 250:
        return
    result = ChoiceBox("You find a small natural spring. That sort of thing isn\'t unusual underground. What\'s odd about this fountain is that the water is glowing slightly. Whether that\'s because of unusual mineral deposits, or some strange magical effect, you aren\'t sure.\n\nThe light has an odd, sickly green tinge to it. It isn\'t very reassuring or appetizing, but, being adventurers, you\'re still tempted to drink some of it.", eDialogPic.STANDARD, 18, ["Leave", "Drink"])
    if result == 1:
        StuffDone["207_4"] = 250
        WorldMap.AlterTerrain(Location(92,122), 1, None)
        WorldMap.DeactivateTrigger(Location(92,122))
        MessageBox("The water is amazingly fresh and invigorating. Drinking it makes you feel ready to take on a thousand alien beasts! You bend down to drink more, but are saddened to find that the glow is faded.\n\nYou\'ve drained the magic for now. You\'ll have to find future healing elsewhere.")
        Party.HealAll(30)
        return

def BelowSchoolofMagery_442_MapTrigger_36_21(p):
    if StuffDone["207_5"] == 250:
        return
    StuffDone["207_5"] = 250
    WorldMap.DeactivateTrigger(Location(84,117))
    MessageBox("Out of curiosity, you toss a pebble over the edge of this natural bridge to see how long it takes to hit the ground. You wait, and wait, and wait. Then you back away from the edge. It\'s obviously quite a drop.")

def BelowSchoolofMagery_443_MapTrigger_9_16(p):
    if StuffDone["207_6"] == 250:
        return
    StuffDone["207_6"] = 250
    WorldMap.DeactivateTrigger(Location(57,112))
    WorldMap.DeactivateTrigger(Location(56,112))
    MessageBox("You stumble upon a pack of the strange beasts, drinking deep from this icy cavern pool. It doesn\'t take them long to decide that they\'d like some meat to go with their drink.")
    WorldMap.SpawnEncounter("Group_1_2_4", p.Target)

def BelowSchoolofMagery_445_SpecialOnWin0(p):
    MessageBox("The alien beasts are dead, but you\'re afraid there\'s plenty more waiting for you. You have a long, hard march ahead of you.")
