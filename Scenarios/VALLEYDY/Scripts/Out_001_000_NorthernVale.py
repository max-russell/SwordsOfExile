
def NorthernVale_379_MapTrigger_13_36(p):
    if StuffDone["201_0"] == 250:
        return
    StuffDone["201_0"] = 250
    WorldMap.DeactivateTrigger(Location(61,36))
    MessageBox("This small bridge spans a river flowing from the large hill to the northeast. Interestingly, you notice that the water from this river lacks the bitter reek of the water to the southwest.")

def NorthernVale_380_MapTrigger_6_38(p):
    if StuffDone["201_1"] == 250:
        return
    StuffDone["201_1"] = 250
    WorldMap.DeactivateTrigger(Location(54,38))
    result = ChoiceBox("Exploring the small island, you notice a small stone circle on a promontory on the west end. It looks very old and harmless, so you go to investigate.\n\nStepping inside, you find a small, polished altar. Although the stone pillars are clearly ancient and crumbled, the altar looks brand new. There is a kneeling stone in front of it - one of you can pray if you wish.", eDialogPic.TERRAIN, 137, ["Leave", "Pray"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            MessageBox("Soon, you walk back out of the shrine. After a few minutes, you look back, and see that it\'s disappeared! You feel relaxed, knowing you\'ve once again avoided serious danger.")
            return
        MessageBox("As you kneel, a serene feeling sweeps over you. As you stare into the polished stone of the altar, your mind is filled with an incredible sense of clarity. Distractions are lost, and your thoughts float freely.\n\nThe feeling soon fades, but that brief moment of pure mental clarity made you realize many useful things. You feel more experienced.")
        pc.AwardXP(50)
        MessageBox("Soon, you walk back out of the shrine. After a few minutes, you look back, and see that it\'s disappeared! You feel relaxed, knowing you\'ve once again avoided serious danger.")
        return
    MessageBox("Soon, you walk back out of the shrine. After a few minutes, you look back, and see that it\'s disappeared! You feel relaxed, knowing you\'ve once again avoided serious danger.")

def NorthernVale_381_MapTrigger_2_38(p):
    if StuffDone["201_3"] == 250:
        return
    StuffDone["201_3"] = 250
    WorldMap.AlterTerrain(Location(50,38), 1, None)
    WorldMap.DeactivateTrigger(Location(50,38))
    ChoiceBox("This foul, stagnant fen has attracted several horrid beasts, who have set up a cozy lair here. They regard you as a fortunate source of tasty meat and rush you, tendrils wiggling.", eDialogPic.CREATURE, 69, ["OK"])
    WorldMap.SpawnEncounter("Group_1_0_4", p.Target)

def NorthernVale_382_MapTrigger_20_21(p):
    if StuffDone["201_2"] == 250:
        return
    result = ChoiceBox("The long valley ends at a wide, dark cave entrance. Between the many claw marks on the ground and the thousands of shedded scales, you have no trouble figuring out what creatures lurk here.\n\nOne of the lizards inside walks to the entrance, sees you, and runs back inside, startled. Maybe there aren\'t too many of them here, and you can wipe the nest out with little trouble.", eDialogPic.CREATURE, 63, ["Leave", "Enter"])
    if result == 1:
        StuffDone["201_2"] = 250
        WorldMap.AlterTerrain(Location(68,21), 1, None)
        WorldMap.DeactivateTrigger(Location(68,21))
        WorldMap.SpawnEncounter("Group_1_0_5", p.Target)
        return

def NorthernVale_383_MapTrigger_38_7(p):
    if StuffDone["201_4"] == 250:
        return
    result = ChoiceBox("You reach an isolated clearing, far up the jagged northern wall of Skylark Vale. It\'s more interesting than you suspected. As you enter, you are startled by the massive skeleton which dominates the open area.\n\nIt was a Drake Lord, one of the massive and powerful lords of lizardkind. Fortunately, it is no longer a threat to you. It has been dead for many years, as the dry and bleached bones mutely testify.\n\nAs you look over the skeleton, you notice one interesting detail. One of the creature\'s massive fangs remains in its skull. Drake fangs are reputed to have interesting magical uses. Do you take this one with you?", eDialogPic.CREATURE2x2, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["201_4"] = 250
        WorldMap.AlterTerrain(Location(86,7), 1, None)
        WorldMap.DeactivateTrigger(Location(86,7))
        SpecialItem.Give("DrakeFang")
        MessageBox("With difficulty, you rip the tooth out of the creature\'s skull. Hopefully no curse will befall you because of the callous act.")
        return
    return

def NorthernVale_384_MapTrigger_26_9(p):
    if StuffDone["201_5"] == 250:
        return
    StuffDone["201_5"] = 250
    WorldMap.AlterTerrain(Location(74,9), 1, None)
    WorldMap.DeactivateTrigger(Location(74,9))
    MessageBox("As you enter this valley, several large lizards emerge from the rocks to trap you inside. You\'re in danger of becoming something\'s meal.")
    WorldMap.SpawnEncounter("Group_1_0_6", p.Target)

def NorthernVale_385_SpecialOnWin0(p):
    MessageBox("Searching their lair, you find that these creatures have had some success waylaying travelers. Most of the victim\'s goods have rotted or rusted away. However, one ring managed to survive.")
    Party.GiveNewItem("BronzeRingofProt_308")

def NorthernVale_386_SpecialOnMeet1(p):
    MessageBox("This lair was more heavily populated than you suspected. A large extended family of giant lizards comes out to greet you.")

def NorthernVale_387_SpecialOnWin1(p):
    MessageBox("You\'ve done quite a good deed for the Vale. Now that these lizards are gone, traveling nearby will hopefully be much safer. You search the lizards\' lair, hoping for a reward for your good deeds.\n\nAlas, your pickings are meager. You find some coins, some tasty lizard meat, and a small flask. Little else is still useful.")
    Party.GiveNewItem("StrongEnergyP_248")
    Party.Gold += 30
    Party.Food += 45
