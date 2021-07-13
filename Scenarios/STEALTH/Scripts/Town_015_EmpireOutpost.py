
def EmpireOutpost_175_MapTrigger_9_36(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,37)).Num == 131:
        if StuffDone["15_1"] < 1:
            if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,30)).Num == 130:
                MessageBox("Suddenly, two rather unsettling things happen simultaneously. First, the portcullis behind you slams shut. Second, the room starts to grow warmer. The lava bubbles faster. You\'re starting to suspect you\'ve stumbled into a trap.")
                Town.AlterTerrain(Location(9,37), 0, TerrainRecord.UnderlayList[130])
                return
            return
        return

def EmpireOutpost_176_MapTrigger_9_31(p):
    if StuffDone["15_1"] < 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(9,30)).Num == 130:
            Town.AlterTerrain(Location(9,30), 0, TerrainRecord.UnderlayList[131])
            MessageBox("The room starts to cool down, and the portcullises at the north and south ends of the room open. Someone\'s decided not to kill you. That\'s refreshing.")
            Town.AlterTerrain(Location(9,37), 0, TerrainRecord.UnderlayList[131])
            return
        return

def EmpireOutpost_177_MapTrigger_9_27(p):
    if StuffDone["15_2"] == 250:
        return
    result = ChoiceBox("When you get close to the door, the watchful soldier says \"Sorry, but you can\'t go in there. It\'s secret.\" His words aren\'t too threatening by themselves, but as he speaks, he pulls his sword slightly out of its sheathe.\n\nThe message is clear. Keep going, and be ready to fight.", eDialogPic.TERRAIN, 90, ["Leave", "Approach"])
    if result == 1:
        StuffDone["15_2"] = 250
        TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(9,27))
        ChoiceBox("Dylan shouts an alarm. Soon after, a loud, piercing noise echoes through the outpost. Behind you, you hear a gate slamming shut. Now you\'ve done it.", eDialogPic.CREATURE, 13, ["OK"])
        Town.AlterTerrain(Location(9,37), 0, TerrainRecord.UnderlayList[130])
        Town.MakeTownHostile()
        if StuffDone["15_2"] == 250:
            return
        StuffDone["15_2"] = 250
        TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(9,27))
        StuffDone["101_1"] = 1
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Deciding not to cause trouble, you back away.")

def EmpireOutpost_178_MapTrigger_13_28(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(13,32)).Num == 122:
        Town.AlterTerrain(Location(13,32), 0, TerrainRecord.UnderlayList[138])
        MessageBox("Walking inside the guard room, you see that there are two windows looking in on the room you were briefly trapped in. They weren\'t visible from that side ... must be magic.")
        Town.AlterTerrain(Location(13,35), 0, TerrainRecord.UnderlayList[138])
        return

def EmpireOutpost_179_MapTrigger_16_36(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear the soothing clatter of a distant portcullis opening. Maybe you can escape this dangerous place at last.")
        t = Town.TerrainAt(Location(9,37))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(9,37), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(9,37), 0, TerrainRecord.UnderlayList[130])
        StuffDone["101_5"] = 1
        return

def EmpireOutpost_180_MapTrigger_31_35(p):
    ChoiceBox("You approach the polished white marble altar, hoping to receive some sort of blessing or holy reward. Unfortunately, you can sense no positive energy, magical or otherwise, coming from the stone.\n\nThis area hasn\'t been sanctified. The altar is here for psychological and aesthetic reasons, more than anything else.", eDialogPic.TERRAIN, 158, ["OK"])

def EmpireOutpost_181_MapTrigger_35_33(p):
    MessageBox("Your traditional excitement at seeing shelves full of books is short lived. These books are provided for the amusement and education of the soldiers, to pass the time during their long stays underground.\n\nSome of it is interesting, sure, and some of it is VERY interesting. But nothing magical or useful.")

def EmpireOutpost_182_MapTrigger_34_18(p):
    if StuffDone["15_4"] == 250:
        return
    StuffDone["15_4"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(34,18))
    ChoiceBox("You open the door, and the twin smells of ozone and alchemical ingredients hit you. You\'ve stumbled into a hidden, underground magical laboratory.\n\nThis room is a holding cell for experiments. There is a platform in the center of the room, mostly circled by magical fields, where dangerous spells can be tested safely. Several mages stand around it, waiting for you.", eDialogPic.CREATURE, 26, ["OK"])

def EmpireOutpost_183_MapTrigger_39_4(p):
    MessageBox("This book is a lab journal. You browse through it briefly. The mages here were looking for a way to safely contain quickfire in some sort of a bomb, so that it could be easily transported into rebel lands.\n\nLooks like the war between the Empire and the Rebels is about to heat up. Literally.")

def EmpireOutpost_184_MapTrigger_26_12(p):
    if StuffDone["15_5"] < 1:
        MessageBox("When you get close to the door, you hear a loud clicking noise. Someone has locked it from the other side. It\'s a very solid door, with a complex lock. It will take a while to open it.\n\nAs you stare at the door, trying to figure out what to do, a panel slides away in the wall behind you ...")
        Town.AlterTerrain(Location(29,10), 0, TerrainRecord.UnderlayList[170])
        StuffDone["15_5"] = 1
        Town.AlterTerrain(Location(30,14), 0, TerrainRecord.UnderlayList[128])
        return

def EmpireOutpost_185_MapTrigger_26_18(p):
    if StuffDone["15_6"] == 250:
        return
    if StuffDone["15_5"] >= 1:
        if StuffDone["15_6"] == 250:
            return
        StuffDone["15_6"] = 250
        TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(26,18))
        for x in range(26, 30):
            for y in range(9, 17):
                Town.DispelFields(Location(x,y), 2)
        MessageBox("Miraculously, you managed to find a concealed nook with a small door, which protects you as the quickfire rages outside. This hole must have been placed here to protect soldiers in case of a quickfire accident.\n\nSweating, you wait it out. Soon, you hear chanting outside, and the heat fades away. The quickfire must have been dispelled. Then you hear a door opening. Someone is coming in to look for your bodies. They\'re going to be surprised.")
        Town.AlterTerrain(Location(25,11), 0, TerrainRecord.UnderlayList[129])
        Town.PlaceEncounterGroup(1)
        Town.AlterTerrain(Location(30,14), 0, TerrainRecord.UnderlayList[129])
        return

def EmpireOutpost_188_MapTrigger_23_9(p):
    if StuffDone["15_7"] == 250:
        return
    StuffDone["15_7"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(23,9))
    ChoiceBox("You hear a spell being completed. You look to the northwest, and see the door there start to glow slightly. Considering the caliber of the mages here, you\'re willing to guess that the door has received a much stronger than average locking spell.", eDialogPic.TERRAIN, 90, ["OK"])

def EmpireOutpost_189_MapTrigger_10_22(p):
    if StuffDone["15_8"] == 250:
        return
    StuffDone["15_8"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(10,22))
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(11,22))
    MessageBox("Suddenly, there is an explosion ahead! It\'s not a large one, and it\'s near the ceiling, so you don\'t suffer any more damage than a few rocks striking against your armor.\n\nHowever, when the smoke clears, you see that the northern passage has been blocked. Falling rock from the ceiling has effectively blocked the corridor. You\'ll have to head east.")
    Town.AlterTerrain(Location(10,19), 0, TerrainRecord.UnderlayList[97])
    Town.AlterTerrain(Location(11,19), 0, TerrainRecord.UnderlayList[97])

def EmpireOutpost_191_MapTrigger_27_1(p):
    if StuffDone["15_9"] == 250:
        return
    StuffDone["15_9"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(27,1))
    MessageBox("You open the iron box, hoping to find a key, or crowbar, or something that would help you open the locked door. Instead, you see a polished oak box. You immediately recognize it. It\'s one of the rebel\'s bombs.\n\nAs you look at it, it vibrates slightly. It\'s about to explode, and destroy everything nearby with it!")
    Timer(Town, 3, False, "EmpireOutpost_197_TownTimer_42", eTimerType.DELETE)

def EmpireOutpost_192_MapTrigger_10_6(p):
    if StuffDone["120_0"] == 250:
        return
    StuffDone["120_0"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(10,6))
    MessageBox("You see the door ahead start to glow. Here we go again.")

def EmpireOutpost_193_MapTrigger_5_1(p):
    if StuffDone["120_1"] == 250:
        return
    StuffDone["120_1"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(5,1))
    MessageBox("You reach the lever, only to find that it\'s a fake. It doesn\'t even move. You hear clicking from the walls around you. The lever may be fake, but the panel that just opened up in the wall to the south is very real.")
    Town.AlterTerrain(Location(5,4), 0, TerrainRecord.UnderlayList[170])
    Town.AlterTerrain(Location(6,3), 0, TerrainRecord.UnderlayList[122])
    Town.AlterTerrain(Location(1,4), 0, TerrainRecord.UnderlayList[123])
    Town.AlterTerrain(Location(7,7), 0, TerrainRecord.UnderlayList[129])

def EmpireOutpost_194_MapTrigger_19_11(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You pull the lever. Click.")
        t = Town.TerrainAt(Location(16,35))
        if t == TerrainRecord.UnderlayList[130]: Town.AlterTerrain(Location(16,35), 0, TerrainRecord.UnderlayList[131])
        elif t == TerrainRecord.UnderlayList[131]: Town.AlterTerrain(Location(16,35), 0, TerrainRecord.UnderlayList[130])
        return

def EmpireOutpost_195_MapTrigger_6_10(p):
    if StuffDone["120_2"] == 250:
        return
    StuffDone["120_2"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(6,10))
    ChoiceBox("At last, you have reached the final stand of the outpost\'s commander. He is an Empire Dervish, seven feet and 300 pounds of pure mean. He swings his greatsword like a twig, and is more than ready for a real fight.\n\nOf course, the mages, priests, and soldiers around him seem to be spoiling for a fight as well. This could be messy.", eDialogPic.CREATURE, 17, ["OK"])

def EmpireOutpost_196_MapTrigger_18_22(p):
    StuffDone["101_1"] = 1

def EmpireOutpost_197_TownTimer_42(p):
    MessageBox("The box explodes. Rocks fall from the ceiling, and flames shoot out in all directions. The ground shimmies, and the walls crack. Hope you weren\'t too close ...")
    Animation_Explosion(Location(27,1), 0, "005_explosion")
    Animation_Hold()
    Wait()
    for ch in Town.EachCharacterInRange(Location(27,1), 2):
        ch.Damage(None, 1000, 0, eDamageType.FIRE)
    for ch in Town.EachCharacterInRange(Location(27,1), 4):
        ch.Damage(None, 40, 0, eDamageType.FIRE)
    Town.AlterTerrain(Location(27,1), 0, TerrainRecord.UnderlayList[0])
    Town.AlterTerrain(Location(20,6), 0, TerrainRecord.UnderlayList[84])
    for ch in Town.EachCharacterInRange(Location(27,1), 0):
        ch.Damage(None, 1000, 0, eDamageType.FIRE)

def EmpireOutpost_198_OnEntry(p):
    if Town.Abandoned:
        MessageBox("You return to the concealed Empire outpost. Following your successful raid, the place is abandoned.")
    else:
        if StuffDone["15_0"] == 250:
            return
        StuffDone["15_0"] = 250
        ChoiceBox("If the Hill Runners hadn\'t told you that this outpost would be here, you would never have known to look for it. Now that you know, however, the narrow path and soldier\'s tracks are readily apparent.\n\nThe tracks led up to this mountain wall. There\'s no door or passage visible ... it\'s probably magically concealed.", eDialogPic.TERRAIN, 194, ["OK"])

def EmpireOutpost_199_CreatureDeath1(p):
    Town.AlterTerrain(Location(9,37), 0, TerrainRecord.UnderlayList[130])
    Town.MakeTownHostile()
    if StuffDone["15_2"] == 250:
        return
    StuffDone["15_2"] = 250
    TownMap.List["EmpireOutpost_15"].DeactivateTrigger(Location(9,27))
    StuffDone["101_1"] = 1

def EmpireOutpost_200_CreatureDeath6(p):
    ChoiceBox("The Dervish falls to a well timed blow. His enormous body hits the floor with a resounding crash. Your third mission for the rebels is complete.\n\nAs you look at his body lying there, you experience a strange, sinking feeling. You have passed the point of no return. Jaen and his lackeys might have been able to forgive some things, but slaying Empire soldiers is beyond the pale.\n\nLike it or not, you\'re stuck with the rebels now. They\'re the only ones who would possibly have you.", eDialogPic.CREATURE, 17, ["OK"])
    StuffDone["101_1"] = 1
    StuffDone["101_5"] = 1
    for pc in Party.EachAlivePC():
        pc.AwardXP(20)
    StuffDone["15_1"] = 1
