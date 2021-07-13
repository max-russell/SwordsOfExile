
def HugeRiverCavern_421_MapTrigger_13_8(p):
    if StuffDone["206_0"] == 250:
        return
    StuffDone["206_0"] = 250
    WorldMap.DeactivateTrigger(Location(13,104))
    ChoiceBox("You walk into an enormous cavern, and immediately run back out. The air inside is so bad, so viciously polluted, that it\'s a struggle merely to breathe. Your skin itches. Your eyes water and burn. You stagger out and spend a while gagging and choking.\n\nAfter preparing yourselves, you walk back in and look around. Spots of light on the ceiling, created, no doubt, by the School\'s wizards, illuminate the cavern. It\'s about two miles by two miles, and dominated by the huge river winding through it.\n\nYou examine the cave carefully, trying to figure out what\'s befouling the air. You soon figure it out. To the southeast, there is a thin stream of gray green fluid, slowly trickling into the river.\n\nUpriver from the stream, the river is lined with pallid mushrooms and sickly trees. Downriver from the stream, there is diseased swamp and rubble. It\'s pretty compelling evidence.\n\nOn the good side, you may be close to discovering the cause of the curse. On the bad side, it seems to be a problem of a far greater scale than anyone had imagined.", eDialogPic.TERRAIN, 76, ["OK"])
    TownMap.List["SmallCave_19"].Hidden = False

def HugeRiverCavern_422_MapTrigger_37_34(p):
    if StuffDone["206_1"] == 250:
        return
    StuffDone["206_1"] = 250
    WorldMap.DeactivateTrigger(Location(37,130))
    WorldMap.DeactivateTrigger(Location(38,130))
    WorldMap.DeactivateTrigger(Location(39,130))
    WorldMap.DeactivateTrigger(Location(40,130))
    ChoiceBox("Just to the north, you see a massive structure built into the cavern wall. You can\'t make out much detail with your bloodshot, burning eyes, but it looks like the stream of filth is trickling out of there.", eDialogPic.TERRAIN, 240, ["OK"])

def HugeRiverCavern_426_MapTrigger_23_31(p):
    if StuffDone["206_2"] == 250:
        return
    StuffDone["206_2"] = 250
    WorldMap.DeactivateTrigger(Location(23,127))
    ChoiceBox("From this vantage point, you can see a bit more of what is going on. The stream of poison (or filth, or demonic ichor, or whatever it is) moves very slowly and is only a few inches deep. The material is very viscous, and doesn\'t flow so much as ooze.\n\nAlthough the stream is shallow, it\'s cut quite a trench out of the rock to flow down. So far, it\'s burned 5 feet down into the solid rock, and will probably eat its way much farther down. In addition to being smelly, it\'s very acidic.\n\nThe stream flows from the southeast. To find out where it comes from, that would be the place to go.", eDialogPic.TERRAIN, 76, ["OK"])

def HugeRiverCavern_427_MapTrigger_23_32(p):
    MessageBox("As you cross the bridge, spray from the river below coats you with a thin layer of burning water. The poisonous atmosphere of the cavern finally catches up with you.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 1))

def HugeRiverCavern_428_MapTrigger_39_15(p):
    if StuffDone["206_3"] == 250:
        return
    StuffDone["206_3"] = 250
    WorldMap.DeactivateTrigger(Location(39,111))
    MessageBox("From here, you think you can see movement in the mushroom grove to the west. You\'ll have to get closer to find out more.")

def HugeRiverCavern_429_MapTrigger_36_15(p):
    if StuffDone["206_4"] == 250:
        return
    result = ChoiceBox("Now you know where the occasional undead creature wandering this cavern comes from. From a hiding place on the outside of this glade, you can see a macabre dance of death going on inside.\n\nDozens of skeletons and zombies dance tirelessly around a bonfire, as a lone pale figure watches and joylessly claps his hands. There is a pile of bodies of all sorts nearby, probably waiting for reanimation.\n\nNone of the undead have noticed you. They seem to be following some sort of programmed motions. Maybe they\'ll have treasure. Or maybe they would speak with you. Or maybe they should just be left alone ...", eDialogPic.CREATURE, 59, ["Leave", "Attack"])
    if result == 1:
        StuffDone["206_4"] = 250
        WorldMap.DeactivateTrigger(Location(36,111))
        MessageBox("Fortunately, you manage to take them by something resembling surprise. As you rush into the circle, weapons in the air, the pale leader of the dance jumps up gleefully. You must be doing a lot to relieve the tedium.")
        WorldMap.SpawnNPCGroup("Group_0_2_4", p.Target)
        return

def HugeRiverCavern_430_MapTrigger_35_24(p):
    if StuffDone["206_5"] == 250:
        return
    StuffDone["206_5"] = 250
    WorldMap.DeactivateTrigger(Location(35,120))
    WorldMap.DeactivateTrigger(Location(37,118))
    WorldMap.DeactivateTrigger(Location(40,118))
    MessageBox("Empire Wizards long ago figured out how to make forms of plants that could survive in caverns (many of which ended up being raised in Exile). These trees must be specimens of that sort of magic.\n\nThis subterranean forest has managed to survive the poisonous gases, but only barely. The forest is sickly and twisted, and you see many little lizard skeletons.")

def HugeRiverCavern_433_MapTrigger_36_44(p):
    if StuffDone["206_6"] == 250:
        return
    result = ChoiceBox("As if this cavern isn\'t unsettling enough, someone left several dead mages back here. There are four bodies. All of them were stabbed to death, and all wear the robes of apprentices (now rotted away).\n\nThe poisonous air of the cavern has eaten away at most of their possessions. One thing remains - one of them still wears a silver ring.", eDialogPic.TERRAIN, 179, ["Take", "Leave"])
    if result == 0:
        StuffDone["206_6"] = 250
        WorldMap.AlterTerrain(Location(36,140), 1, None)
        WorldMap.DeactivateTrigger(Location(36,140))
        Party.GiveNewItem("SilverRingofSkill_303")
        MessageBox("You feel kind of bad robbing the dead, but oh well. It\'s not like he was getting any use out of it.")
        return
    return

def HugeRiverCavern_434_SpecialOnWin0(p):
    if StuffDone["206_7"] == 250:
        return
    StuffDone["206_7"] = 250
    MessageBox("Your victory was a miracle, and the spoils are glorious. You won\'t have to worry about meeting too many undead in this cavern anymore. In addition, you find some loot.\n\nUnder the vampire\'s chair, you find a bunch of old meat (which you leave) and gold (which you take). In addition, you get a long, slender ivory wand.")
    Party.GiveNewItem("WandofCharming_289")
    Party.Gold += 800
