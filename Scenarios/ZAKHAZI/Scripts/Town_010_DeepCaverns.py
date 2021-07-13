
def DeepCaverns_227_MapTrigger_6_38(p):
    if StuffDone["10_0"] == 250:
        return
    StuffDone["10_0"] = 250
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(6,38))
    ChoiceBox("This far away from the portal that brought you here, these caverns are completely, absolutely dark. The darkness is like a living thing, converging and smothering event the slightest bit of illumination.\n\nYou are in caverns, but they\'re completely unlike any of the caves of Exile. The stone is harder, and there\'s none of the fungus or mold. It\'s icy cold, as if you\'re so far down that none of the heat from the sun ever reaches here.\n\nThere is less flora, but there must be some fauna. You hear the sounds of scratching, rasping, and occasional noisy eating. You also hear the screams of whatever\'s being eaten.", eDialogPic.STANDARD, 8, ["OK"])

def DeepCaverns_228_MapTrigger_5_42(p):
    if SpecialItem.PartyHas("MorogsShrooms"):
        result = ChoiceBox("The portal is dim and weak, not surprising considering how far you are below Morog\'s Castle. Fortunately, it does look stable enough to carry you back to the Za-Khazi Run.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            MessageBox("You feel the now-familiar wrenching sensation, as you are roughly flung from the deepest parts of the underworld back to Exile. You return safely to Morog\'s Castle.")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(46,42)
            Party.MoveToMap(TownMap.List["MorogsCastle_9"])
            return
        return
    ChoiceBox("The portal is dim and weak, not surprising considering how far you are below Morog\'s Castle. Fortunately, it does look stable enough to carry you back to the Za-Khazi Run.\n\nWhen you step near it, however, you feel a force pushing you away. You try to move closer, but the force pushes back even harder. The portal doesn\'t want to let you return yet.", eDialogPic.STANDARD, 22, ["OK"])

def DeepCaverns_229_MapTrigger_15_20(p):
    if StuffDone["10_1"] == 250:
        return
    StuffDone["10_1"] = 250
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(15,20))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(36,37))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(36,35))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(16,10))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(14,20))
    ChoiceBox("As you maneuver through the caverns, you suddenly sense that something is different. Something feels strange in your mind. At first, you think it\'s the effect of being this deep, below this much stone.\n\nThen you realize that it\'s not just that. Someone it trying to touch your mind. It\'s as if someone has detected an intruder, and is searching for you. After a moment, the feeling passes.\n\nYou can\'t tell whether it\'s because you were noticed or because the searcher decided you look elsewhere.", eDialogPic.STANDARD, 13, ["OK"])

def DeepCaverns_233_MapTrigger_37_22(p):
    if StuffDone["10_2"] == 250:
        return
    StuffDone["10_2"] = 250
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(37,22))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(37,12))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(19,17))
    TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(25,12))
    ChoiceBox("You step into a massive throne room. It\'s very incongruous, considering how remote and alien the surroundings are. Then you see what\'s sitting on the throne.\n\nIt\'s not your ordinary, garden variety demon. It\'s about twelve feet tall, with enormous claws and a protective nimbus of energy. You recognize this creature - it\'s a Haakai.\n\nYou\'ve heard legends of these beasts. They\'re the barons of Hell, evil incarnate. That it\'s here must mean that it has been exiled or imprisoned from the nether realms. It certainly doesn\'t plan to talk to you so you can find out why.", eDialogPic.STANDARD, 13, ["OK"])
    Town.PlaceEncounterGroup(1)

def DeepCaverns_237_MapTrigger_29_7(p):
    result = ChoiceBox("This portal is not linked to anything at Morog\'s Castle. This is something very different. It\'s fourteen feet high, fiery red, and searingly hot. It hurts to stand near it.\n\nYou try to look through the portal and see what\'s on the other side. You think that you can make out flames, and maybe the occasional creature dancing around, but you aren\'t sure.\n\nAlthough it\'s red hot, if you ran towards it you might be able to pass through safely.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        MessageBox("Indeed, running towards the portal gets you safely to it, and then through. Unfortunately, the problem is not so much portal as what\'s on the other side.\n\nYou land in a lake of lava, where imps and other demonic creatures fall upon you. In your last moments, you look around and see a nearly infinite caldera of sulphur and fire. Nasty place.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def DeepCaverns_238_MapTrigger_28_11(p):
    MessageBox("You open the box and see a large pile of gold, as well as several scrolls and potion. Alas, as you look at it, it dissolves before your eyes. Soon, you\'re standing in an empty cubicle.")
    Town.AlterTerrain(Location(28,11), 0, TerrainRecord.UnderlayList[0])

def DeepCaverns_239_MapTrigger_30_11(p):
    MessageBox("You open the box and see a heap of jewelry and silver ingots, as well a steel greatsword and two rings. Alas, as you look at it, it dissolves before your eyes. Soon, you\'re standing in an empty cubicle.")
    Town.AlterTerrain(Location(30,11), 0, TerrainRecord.UnderlayList[0])

def DeepCaverns_240_MapTrigger_43_2(p):
    if StuffDone["10_3"] == 250:
        return
    result = ChoiceBox("This has been the only place in the deep caverns you\'ve seen mushrooms growing, so you inspect them closely. Sure enough, you find that a few of them have the small red spots Morog told you about.\n\nPluck them, and you\'re almost done.", eDialogPic.TERRAIN, 73, ["Take", "Leave"])
    if result == 0:
        StuffDone["10_3"] = 250
        TownMap.List["DeepCaverns_10"].AlterTerrain(Location(43,2), 1, None)
        TownMap.List["DeepCaverns_10"].DeactivateTrigger(Location(43,2))
        SpecialItem.Give("MorogsShrooms")
    return

def DeepCaverns_241_MapTrigger_31_24(p):
    if StuffDone["10_4"] == 250:
        return
    result = ChoiceBox("This chamber is dominated by a massive altar, six feet high, ten feet wide, made of black basalt and dripping with dried gore.  Evil blows off it it like a wind, strong, industrial strength evil that feels like its warping your mind by just being nearby.\n\nAnything you do near an artifact of this power is bound to be extremely dangerous. This thing may be out of your league.", eDialogPic.TERRAIN, 159, ["Leave", "Destroy", "Pray"])
    if result == 1:
        MessageBox("You approach the thing, trying to figure out how to destroy it. The stone looks into your mind and sees your intent. A warning blast of fire throws you back. This may be the wrong thing to do.")
        Party.Damage(Maths.Rand(10, 1, 10) + 20, eDamageType.FIRE)
        Wait()
        return
    elif result == 2:
        MessageBox("The moment your knees hit the stone, the altar scours your minds clean and takes control of them. After it tires of having you serve it, it sends you out to be willingly devoured by the creatures outside.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def DeepCaverns_242_SanctifyTrigger_31_23(p):
    if p.Spell.ID != "p_sanctify":
        return
    MessageBox("The moment you begin to cast the spell, the altar begins to fight back. You immediately begin to see that you don\'t even have the power to affect it. You end the spell and try to get away, but the altar has been infuriated by your actions.\n\nBy the time the bolts of fire stop coming, there\'s nothing left of you but dust.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def DeepCaverns_524_StairwayDestination53(p):
    return
