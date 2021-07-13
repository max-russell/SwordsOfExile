
def CavernofPoppyShrooms_571_MapTrigger_5_45(p):
    if StuffDone["204_0"] == 250:
        return
    StuffDone["204_0"] = 250
    WorldMap.DeactivateTrigger(Location(5,237))
    WorldMap.DeactivateTrigger(Location(6,237))
    MessageBox("You detect a peculiar smell in the air. It\'s sickly sweet, like slightly old fruit. It makes you feel very happy and pleasant, and somewhat light-headed. The farther north you walk, the stronger the smell gets.")

def CavernofPoppyShrooms_573_MapTrigger_5_42(p):
    if Party.HasTrait(Trait.CaveLore):
        if StuffDone["204_3"] == 250:
            return
        StuffDone["204_3"] = 250
        ChoiceBox("This cavern immediately reminds you of the unicorn cave, far to the south. It\'s a beautiful place, a massive, lovely, underground garden.\n\nThe glow of the fungus overhead reveals a huge forest of soft, white mushrooms. Most of them are only a few inches high, but some are enormous. A few monstrous specimens even come up to your waist.\n\nIt\'s not the mushrooms, however, that makes the cavern lovely. It\'s the smell. The things are putting off this lovely, sweet smell. Even the tiniest whiff of it makes you feel placid and relaxed.\n\nThanks to your knowledge of Cave Lore, however, you aren\'t fooled. You know exactly what these things are: poppy shrooms. Their hypnotic scent has distracted and entrapped many a wandering adventurer before you.\n\nThis is the largest collection of the things you\'ve ever heard of. To get through this cavern will require great force of will.\n\nLooking around, you notice that there is a much higher concentration of mushrooms in the northwest corner of the cavern. Maybe a place to avoid ...", eDialogPic.TERRAIN, 73, ["OK"])
        return
    if StuffDone["204_3"] == 250:
        return
    StuffDone["204_3"] = 250
    ChoiceBox("This cavern immediately reminds you of the unicorn cave, far to the south. It\'s a beautiful place, a massive, lovely, underground garden.\n\nThe glow of the fungus overhead reveals a huge forest of soft, white mushrooms. Most of them are only a few inches high, but some are enormous. A few monstrous specimens even come up to your waist.\n\nIt\'s not the mushrooms, however, that makes the cavern lovely. It\'s the smell. The things are putting off this lovely, sweet smell. Even the tiniest whiff of it makes you feel placid and relaxed.\n\nThe scent makes you feel very happy. You can\'t imagine anything going wrong in here. You can hardly wait to enter.\n\nLooking around, you notice that there is a much higher concentration of mushrooms in the northwest corner of the cavern. Maybe you should go there ...", eDialogPic.TERRAIN, 73, ["OK"])

def CavernofPoppyShrooms_575_MapTrigger_10_11(p):
    if StuffDone["204_2"] == 250:
        return
    StuffDone["204_2"] = 250
    WorldMap.DeactivateTrigger(Location(10,203))
    MessageBox("You walk from a cloud of spores into a cloud of steam. You now know why the mushrooms were so concentrated here. The warmth and moisture pouring out of this caldera makes this area a lovely greenhouse for all manner of hostile fungi.")

def CavernofPoppyShrooms_576_MapTrigger_39_5(p):
    if StuffDone["204_1"] == 250:
        return
    StuffDone["204_1"] = 250
    WorldMap.DeactivateTrigger(Location(39,197))
    WorldMap.DeactivateTrigger(Location(40,197))
    MessageBox("Your head spinning and your eyes watering, you finally stumble out of the mushroom choked cavern. You lean against the wall and suck in cleaner air, relieved you made it through that place at all.")

def CavernofPoppyShrooms_578_MapTrigger_38_39(p):
    if SpecialItem.PartyHas("MushroomTalisman"):
        if StuffDone["204_5"] == 250:
            return
        StuffDone["204_5"] = 250
        MessageBox("As you wade through this exceptionally heavy patch of poppy shrooms, you notice that several of the nearby fungi are much, much larger than usual. In fact, they\'re taller than you.\n\nAs the spores settle harmlessly on you, these enormous fungi suddenly charge you, apparently thinking you will be knocked unconscious. They have a surprise coming ...")
        WorldMap.SpawnEncounter("Group_0_4_4", p.Target)
        return
    if StuffDone["204_5"] == 250:
        return
    StuffDone["204_5"] = 250
    MessageBox("As you wade through this exceptionally heavy patch of poppy shrooms, you notice that several of the nearby fungi are much, much larger than usual. In fact, they\'re taller than you.\n\nAs the spores settle on you, you feel your eyelids droop. As you stumble, the huge fungi suddenly rush to attack you! As the creatures charge, you struggle desperately to stay awake, but you feel so sleepy ...")
    WorldMap.SpawnEncounter("Group_0_4_4", p.Target)
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.ASLEEP, Maths.MinMax(0, 8, pc.Status(eAffliction.ASLEEP) + 8))
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 8))
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 4))

def CavernofPoppyShrooms_581_MapTrigger_42_42(p):
    result = ChoiceBox("Heaped at the bottom of a shallow crevasse, you find the shambler\'s combination compost heap and meat locker. Among the piles of smelly, decomposing goo, you see a wide variety of coinage and even a few weapons (some of which haven\'t rusted).\n\nIt would be a slow, gross job, but you could pick some treasure out of here.", eDialogPic.TERRAIN, 244, ["Take", "Leave"])
    if result == 0:
        Party.GiveNewItem("AssassinsKnife_341")
        Party.Gold += 600
        MessageBox("Most of the weapons turned out to be, upon closer inspection, pitted, rusted, and useless. However, in addition to a bunch of gold, you find a small dagger which looks as new as the day it was made.\n\nUnfortunately, rooting around in filth is not done without penalty. You feel quite ill.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 3))
        return
    return

def CavernofPoppyShrooms_582_MapTrigger_18_3(p):
    if StuffDone["204_7"] == 250:
        return
    result = ChoiceBox("You stumble upon a living testament to the dangers of the poppy shrooms. There is a small group of humans living in this cavern.\n\nSome are naked. The rest are dressed in rags. All of them have the glazed stare of the lost, those whose minds have been lost to the constant ravages of poppy shroom spores.\n\nThey sleep on the bare rock, near piles of mushrooms they have harvested. Some of them have been picked for food, some for spores.\n\nThey barely even seem to notice you when you come near. As you watch them, you notice that one of them is wearing a ring. You doubt she cares about whether she keeps it. You could probably steal it easily.\n\nYou could also try to free these creatures from their horrible bondage. Perhaps if you took them away from here, they could be restored to normality.", eDialogPic.CREATURE, 11, ["Leave", "Free", "Steal"])
    if result == 1:
        StuffDone["204_7"] = 250
        WorldMap.AlterTerrain(Location(18,195), 1, None)
        WorldMap.DeactivateTrigger(Location(18,195))
        MessageBox("Pulling them away doesn\'t work. They shake loose and run back. They don\'t respond when you talk to them, and you don\'t have adequate magic to cure them of the addiction.\n\nAs a last resort, you try taking away their spore supply. That gets a response. They go mad, shrieking and attacking you. Despite their frail appearance, years of exposure to the spores has affected them strangely ...")
        WorldMap.SpawnEncounter("Group_0_4_5", p.Target)
        return
    elif result == 2:
        StuffDone["204_7"] = 250
        WorldMap.AlterTerrain(Location(18,195), 1, None)
        WorldMap.DeactivateTrigger(Location(18,195))
        MessageBox("It\'s shamefully easy. As she eats a large, gray fungus with one hand, you walk up and slide the ring off the other. Then you back away. She doesn\'t even notice.\n\nAs you leave the grove, however, you look back, and see that all of the addicts have slipped away. Your presence must have agitated them.")
        Party.GiveNewItem("BronzeRingofSkill_310")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You leave their grove. They don\'t notice.")

def CavernofPoppyShrooms_583_SpecialOnWin0(p):
    MessageBox("After a long period of hacking, the massive lumps of bark and fungus finally stop moving. You look around, and notice a trail of bone chips and scraps of fur to the southeast. That must be where the creatures dragged their prey ...")

def CavernofPoppyShrooms_584_SpecialOnWin1(p):
    MessageBox("After the battle, you take the ring you saw earlier. Waste not, want not.")
    Party.GiveNewItem("BronzeRingofSkill_310")
