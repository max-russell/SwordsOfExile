
def MajorWasteRepository_185_MapTrigger_41_36(p):
    if StuffDone["10_2"] == 250:
        return
    StuffDone["10_2"] = 250
    TownMap.List["MajorWasteRepository_10"].DeactivateTrigger(Location(41,36))
    ChoiceBox("From here, at last, you can see the true causes of the curse on the Vale. They\'re right in front of you. You see boxes and barrels, dozens of them, many of them leaking.\n\nOn the floor around the containers are all manner of alchemical and magical tools. You see beakers and flasks, vials and tubes, each of them covered with the residue of magical experiments.\n\nThis structure contains the debris and poisonous detritus of a thousand failed experiments, badly mixed potions, and spells gone wrong. Nothing is more dangerous than the result of a miscast spell, and all of those leavings were just put into barrels.\n\nAnd left here. Left without proper protection, without anything that would effectively keep the refuse from poisoning the water of the Vale. Cold fury grows inside you. How could anyone be so careless?\n\nAnd how are you to take care of it? There\'s so much residue, so much waste here, you can\'t imagine how you will be able to get rid of it all. The cause is here. The solution is still far distant.", eDialogPic.TERRAIN, 76, ["OK"])
    MessageBox("You take note of all of this. The officials of the Vale are sure to be interested.")
    StuffDone["199_1"] = 1

def MajorWasteRepository_186_MapTrigger_14_15(p):
    if StuffDone["10_3"] == 250:
        return
    StuffDone["10_3"] = 250
    TownMap.List["MajorWasteRepository_10"].DeactivateTrigger(Location(14,15))
    MessageBox("This room must be where the barrels started to leak. It looks like there was a cave-in here. The barrels broke and the goo spilled out, eating away at the other containers from the outside.\n\nNow the stuff is working its ways to the other chambers, breaking open more containers as it goes. Soon every bit of waste here will be turned loose, unless you do something.")

def MajorWasteRepository_187_MapTrigger_13_17(p):
    if StuffDone["10_4"] == 250:
        return
    StuffDone["10_4"] = 250
    TownMap.List["MajorWasteRepository_10"].DeactivateTrigger(Location(13,17))
    ChoiceBox("Suddenly, things start climbing out of the acidic muck! You watch, stunned, amazed that anything could survive in that stuff. One thing sure can, though - demons.\n\nThe hellish imps were having a pleasant, leisurely swim in the goop before you arrived. Now, annoyed that you want to end their fun, they decide to kill you ...", eDialogPic.CREATURE, 71, ["OK"])
    Town.PlaceEncounterGroup(9)

def MajorWasteRepository_188_MapTrigger_23_23(p):
    result = ChoiceBox("You have finally managed to reach the control panel for the Primary Waste Storage facility. Perhaps here, you can find a way to contain the stuff. Or you could also make the problem much worse.\n\nSit down ... if you dare.", eDialogPic.TERRAIN, 125, ["Leave", "Sit"])
    if result == 1:
        if StuffDone["10_9"] >= 1:
            result = ChoiceBox("You sit down and look the controls over. At first, you think your trip to the Main Control Room was in vain. Everything looks pretty dark and uninteresting.\n\nThen you notice that one of the displays isn\'t dark after all. It\'s flickering very dimly. You bend down to read it. It says \"Activate Purification Process. Danger - Safety Off\" Next to the light is a tiny switch.\n\nYou could push the switch. However, you\'re a tiny bit nervous about the whole Safety thing.", eDialogPic.TERRAIN, 125, ["Leave", "Push"])
            if result == 1:
                if SpecialItem.PartyHas("CrystalofPower"):
                    result = ChoiceBox("You push the switch. A little hole opens up on the panel, and the words \"Insert Crystal\" appear next to it, written in letters of mist. It looks like the crystal the Vahnatai gave you would fit perfectly.\n\nThis would appear to be it. Do you insert the crystal?", eDialogPic.TERRAIN, 125, ["Leave", "Insert"])
                    if result == 1:
                        ChoiceBox("You insert the crystal. There is a flash of light and heat, and it disintegrates. You aren\'t allowed time to ponder what this means. At last, the powerful machinery of the School of Magery has been unleashed, as it should have been long before.\n\nQuickfire is the most thorough, devastating, rapacious magical effect known. It can and will devour anything and everything it can reach. You hear the roar of its unending flame roaring through the Storage areas, devouring the waste.\n\nFor whatever reason, the waste destruction mechanisms weren\'t used when the School was closed. At last, they have been activated.\n\nUnfortunately, the doors and gates that would keep the quickfire from reaching you are no longer working. You watch rusted shutters pathetically attempt to close over the windows surrounding you. They aren\'t working. The fire will soon reach you.\n\nPerhaps you should run ...", eDialogPic.TERRAIN, 125, ["OK"])
                        StuffDone["1_9"] = 1
                        Town.PlaceField(Location(24,18), Field.QUICKFIRE)
                        Town.PlaceField(Location(27,24), Field.QUICKFIRE)
                        Town.PlaceField(Location(22,29), Field.QUICKFIRE)
                        return
                    p.CancelAction = True
                    if p.Origin == eCallOrigin.MOVING:
                        MessageBox("For all you know, you\'re about to bring a river of deadly goo pouring in on you. You back away, and the hole disappears.")
                    return
                p.CancelAction = True
                if p.Origin == eCallOrigin.MOVING:
                    MessageBox("You push the switch. A little hole opens up on the panel, and the words \"Insert Crystal\" appear next to it, written in letters of mist. Alas, you have no crystal, or anything similar.\n\nDisappointed, you back away. The hole closes up as you do.")
                return
            p.CancelAction = True
            if p.Origin == eCallOrigin.MOVING:
                MessageBox("Probably a wise move. This isn\'t a suicide mission.")
            return
            return
        ChoiceBox("It\'s rather anticlimactic, after all. You sit down, examine the panel, and realize all the levers are locked down, the displays are dark, and the buttons have been removed entirely.\n\nThere\'s nothing you can do here now. There may be somewhere you can go to activate this control panel, but you aren\'t optimistic.", eDialogPic.TERRAIN, 125, ["OK"])
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You back away. Probably a sensible idea.")

def MajorWasteRepository_189_MapTrigger_34_6(p):
    if StuffDone["10_5"] == 250:
        return
    result = ChoiceBox("That\'s odd. One of these boxes of waste is shaking. Do you open it?", eDialogPic.TERRAIN, 138, ["Leave", "Open"])
    if result == 1:
        StuffDone["10_5"] = 250
        TownMap.List["MajorWasteRepository_10"].AlterTerrain(Location(34,6), 1, None)
        TownMap.List["MajorWasteRepository_10"].DeactivateTrigger(Location(34,6))
        MessageBox("Oops. It would appear that not all of the waste placed here was inert.")
        Town.PlaceEncounterGroup(8)
        return

def MajorWasteRepository_190_MapTrigger_29_2(p):
    if StuffDone["10_6"] == 250:
        return
    StuffDone["10_6"] = 250
    TownMap.List["MajorWasteRepository_10"].DeactivateTrigger(Location(29,2))
    MessageBox("This chamber was where fresh, virulent waste was teleported in for storage. For extra safety, magic barriers were placed around the arrival portal. Most of the barriers have faded away on their own at this point.")

def MajorWasteRepository_191_MapTrigger_27_9(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Not even adventurers as foolhardy as you would step into a portal this weak and unstable, leading to who knows where. You back away carefully.")

def MajorWasteRepository_192_MapTrigger_26_23(p):
    if StuffDone["1_9"] >= 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        ChoiceBox("The quickfire advanced too fast. You didn\'t have a chance. You were trapped. The searing heat, which will burn away all the waste in the repository, will turn you to ash as well. You grow resigned. You have no hope.\n\nThen, suddenly, all is blackness. You are no longer in the School! You have been transported to an area of total darkness, where you float suspended in nothingness. Is this the end? Have you died?\n\nThen you hear a voice. You recognize it! It\'s Baia-Tel, the leader of the Vahnatai! He says \"Gratitude and honor are thing we Vahnatai always much valuing. Your goodness to us is getting reward now. Saving you is but the least we can do.\"\n\n\"Thanking to you, and good luck.\"\n\nThen you are somewhere else ...", eDialogPic.CREATURE, 83, ["OK"])
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(34,34)
        Party.MoveToMap(TownMap.List["Sweetgrove_1"])
        return

def MajorWasteRepository_193_TownTimer_0(p):
    MessageBox("You\'ve spent too long in this incredibly poisonous atmosphere. It\'s starting to get to you ...")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 2))

def MajorWasteRepository_194_OnEntry(p):
    if StuffDone["10_1"] == 250:
        return
    StuffDone["10_1"] = 250
    ChoiceBox("You stand at the entrance to the Primary Waste Disposal. While the builders of the School of Magery obviously built this to be a massive and nearly impregnable structure, it has not proved to be impervious to the ravages of time.\n\nThe massive basalt front of the structure has been cracked and eaten away by the foul ooze seeping out of it. Even as you watch, bits of the wall crumble away and dissolve, making the holes even wider and allowing more poison out.\n\nThis must be the true cause of the \"curse\" that afflicts the valley. More information is sure to be available inside.", eDialogPic.TERRAIN, 76, ["OK"])
