
def CentralMorrowsIsle_405_MapTrigger_40_3(p):
    if StuffDone["205_0"] == 250:
        return
    result = ChoiceBox("As you start to climb down into a small valley, on your way through this rocky area, you suddenly get a strange feeling. Maybe things are a little too quiet, or a little too enclosed, but there\'s something about this place that makes you uncomfortable.", eDialogPic.TERRAIN, 85, ["Leave", "Enter"])
    if result == 1:
        StuffDone["205_0"] = 250
        WorldMap.AlterTerrain(Location(88,51), 1, None)
        WorldMap.DeactivateTrigger(Location(88,51))
        ChoiceBox("As you walk down the valley, things get quieter. As you watch the rocks above you, you become more and more sure that you\'re being watched.\n\nThen, suddenly, people start standing up above you. They\'re dressed in light armors, like leather and chain, and definitely don\'t have Empire uniforms. They\'re heavily armed.\n\nYou draw your weapons, but then realize that the people above you aren\'t preparing to attack. Instead, one of them gives you a sharp salute. Then, in mere moments, they\'re all gone.\n\nYou can\'t be sure, but you suspect you were just found by a group of rebels. Fortunately, they knew who you were. You proceed unmolested.", eDialogPic.CREATURE, 18, ["OK"])
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You back away from the valley. It was just too suspicious.")

def CentralMorrowsIsle_406_MapTrigger_22_4(p):
    if StuffDone["100_8"] >= 1:
        ChoiceBox("As you cross the bridge, you see that a large contingent of Empire soldiers, clad in plate and wielding massive weapons, have set up a guard post in the middle.\n\nAs you approach, they favor you with snide smiles, and ask you to identify yourselves. Much to their surprise, however, when they look at their lists, they find your names.\n\nWith a dismissive jerk of his thumb, the lead Empire Dervish says \"OK. You can pass.\"", eDialogPic.CREATURE, 17, ["OK"])
        return
    ChoiceBox("As you cross the bridge, you see that a large contingent of Empire soldiers, clad in plate and wielding massive weapons, have set up a guard post in the middle.\n\nWhen you approach, they stop you and ask you to identify yourselves. They listen to you dubiously, look at some papers, laugh at you, and tell you \"The northwest corner of the island is closed off. You aren\'t cleared to pass.\"\n\nYou\'re forced to turn back, the derisive laughter of the Empire Dervishes following you.", eDialogPic.CREATURE, 17, ["OK"])
    p.CancelAction = True

def CentralMorrowsIsle_407_MapTrigger_20_17(p):
    if StuffDone["205_1"] == 250:
        return
    StuffDone["205_1"] = 250
    WorldMap.DeactivateTrigger(Location(68,65))
    MessageBox("Funny how you can always tell when you\'re entering humanoid territory. Hard to tell whether it\'s the shards of bones, the piles of rotting trash, or the mind numbing stench that tips you off first.\n\nBest be wary ... there are monsters ahead.")

def CentralMorrowsIsle_408_MapTrigger_19_24(p):
    if StuffDone["205_2"] == 250:
        return
    p.CancelAction = True
    result = ChoiceBox("You hear harsh laughter ahead. Looking up the hill walls, you see a large band of ogres, standing atop piles of massive, rounded boulders. Some of them are holding long sticks, no doubt to act as levers to roll rocks down on you.\n\nYou could keep going, but you seem to be in a vulnerable spot.", eDialogPic.CREATURE, 42, ["Leave", "Onward"])
    if result == 1:
        MessageBox("Sure enough, the ogres start rolling rocks down the hill towards you. There\'s a long way to climb, and they have a lot of rocks. After getting smashed up enough, you decide to retreat.")
        Party.Damage(Maths.Rand(8, 1, 10) + 1, eDamageType.WEAPON)
        Wait()
        return
    MessageBox("You back away. As you do, the ogres laugh and call you certain highly objectionable names.")

def CentralMorrowsIsle_409_MapTrigger_15_24(p):
    if StuffDone["205_2"] == 250:
        return
    StuffDone["205_2"] = 250
    WorldMap.DeactivateTrigger(Location(67,72))
    WorldMap.DeactivateTrigger(Location(63,72))

def CentralMorrowsIsle_410_MapTrigger_11_27(p):
    if StuffDone["205_3"] == 250:
        return
    StuffDone["205_3"] = 250
    WorldMap.AlterTerrain(Location(59,75), 1, None)
    WorldMap.DeactivateTrigger(Location(59,75))
    MessageBox("The ogres have piled lots of smelly trash and rancid meat here. Unpleasant, feral creatures have taken up residence, living it up on their debris. Monster etiquette, of course, demands that they attack you.")
    WorldMap.SpawnEncounter("Group_1_1_4", p.Target)

def CentralMorrowsIsle_411_MapTrigger_18_25(p):
    if StuffDone["205_4"] == 250:
        return
    StuffDone["205_4"] = 250
    WorldMap.DeactivateTrigger(Location(66,73))
    MessageBox("A lot of ogres are up here, ready to throw rocks on people coming up the path below. The are quite put out to find that you\'ve flanked them. They rush to attack.")
    WorldMap.SpawnEncounter("Group_1_1_5", p.Target)

def CentralMorrowsIsle_412_MapTrigger_22_22(p):
    if StuffDone["205_5"] == 250:
        return
    result = ChoiceBox("You reach the ogre\'s main lair. Not surprisingly, they knew you were coming. There are quite a few of them, and they\'re mean looking. Really mean looking.\n\nOddly, they haven\'t attacked yet. Their chief seems to he holding them back. Perhaps, for once, some monsters are showing respect for your abilities. If you want, you can attack them. Or, you could just leave.", eDialogPic.CREATURE, 152, ["Leave", "Attack"])
    if result == 1:
        StuffDone["205_5"] = 250
        WorldMap.AlterTerrain(Location(70,70), 1, None)
        WorldMap.DeactivateTrigger(Location(70,70))
        MessageBox("Oops. That\'s why they were waiting. They wanted to buy some time, so their mages could cast spells while you charged. The world begins to speed up around you. Then the ogres attack.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 8))
        WorldMap.SpawnEncounter("Group_1_1_6", p.Target)
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("As you walk away, one of the ogres shouts an insult at you. Fortunately, it\'s in ogrish, so you can\'t understand it.")

def CentralMorrowsIsle_413_MapTrigger_19_30(p):
    if StuffDone["205_6"] == 250:
        return
    StuffDone["205_6"] = 250
    WorldMap.AlterTerrain(Location(67,78), 1, None)
    WorldMap.DeactivateTrigger(Location(67,78))
    MessageBox("The ogres keep their pets in caves down here. They must feed them by sending prisoners to walk up this path. At least, that\'s what all the gnawed bones suggest to you.")
    WorldMap.SpawnEncounter("Group_1_1_7", p.Target)

def CentralMorrowsIsle_414_MapTrigger_13_15(p):
    if StuffDone["205_7"] == 250:
        return
    result = ChoiceBox("How nice! Some alchemical herbs are growing on the riverbank, just waiting to be taken!", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["205_7"] = 250
        WorldMap.AlterTerrain(Location(61,63), 1, None)
        WorldMap.DeactivateTrigger(Location(61,63))
        Party.GiveNewItem("GlowingNettle_365")
    return

def CentralMorrowsIsle_415_SpecialOnWin0(p):
    MessageBox("There might be undiscovered treasure under all this gunk. Unfortunately, the goo is gross beyond all human understanding. It will just have to stay undiscovered.")

def CentralMorrowsIsle_416_SpecialOnWin2(p):
    MessageBox("The ogre tribe destroyed, their loot is laid out for the taking. You leave the questionable meat behind, instead filling your packs with all manner of gold and trade goods.\n\nIn addition, you find a potion, a necklace, and a scroll tube. Not a bad day\'s work, overall.")
    Party.GiveNewItem("ScrollFirestorm_203")
    Party.Gold += 1000
    Party.GiveNewItem("StrongEnergyP_248")
    Party.GiveNewItem("OnyxCharm_322")

def CentralMorrowsIsle_417_SpecialOnFlee2(p):
    MessageBox("At least you managed to get away. Considering how tough this tribe was, it\'s a small miracle.")

def CentralMorrowsIsle_418_SpecialOnWin3(p):
    MessageBox("The ogres must love their pet bears very much. Each one wears a collar, and each collar has a semi-precious stone set into it. This expedition suddenly became very profitable.")
    Party.Gold += 500
