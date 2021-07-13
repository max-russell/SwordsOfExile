
def ArgadonsLab_1596_MapTrigger_45_21(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("There is, or was, a stairway here. However, a large pile of rocks has caved in blocking the passage. It appears you will not be going this way.")

def ArgadonsLab_1598_MapTrigger_38_17(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["57_4"] == 0:
        MessageBox("Upon opening this door, you confront a statue with fiery red eyes. It fires a large beam which quickly reduces you to dust. It all happened so fast that you did not have a chance.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        p.CancelAction = True
        return
    Town.AlterTerrain(Location(38,14), 0, TerrainRecord.UnderlayList[217])
    if Maths.Rand(1,0,100) <= 100:
        Town.PlaceField(Location(38,14), Field.ROCKS)

def ArgadonsLab_1599_MapTrigger_14_41(p):
    if StuffDone["57_7"] == 250:
        return
    StuffDone["57_7"] = 250
    TownMap.List["ArgadonsLab_66"].DeactivateTrigger(Location(14,41))
    MessageBox("This narrow passage slopes steeply upward for a while.")

def ArgadonsLab_1600_MapTrigger_18_3(p):
    if StuffDone["57_5"] >= 3:
        MessageBox("The battery is still inside firmly. In fact, you doubt you could get it out even if you wanted to.")
        return
    if StuffDone["57_5"] < 1:
        MessageBox("There is a circular hole in the wall which extends back for a bit. It seems that you could fit some cylindrical object in here.")
        return
    result = ChoiceBox("The battery needs to be inserted in this socket to power the machine. It appears the cylindrical battery will just fit perfectly in the hole. You note that the negative side needs to be inserted first.", eDialogPic.TERRAIN, 100, ["Leave", "Insert"])
    if result == 1:
        if StuffDone["57_6"] == 0:
            MessageBox("Or maybe it will not fit perfectly. Despite your best attempts to squeeze the battery in, the hole is ever so slightly too small. You would think the designers of this place would have been more intelligent. So much for that idea!")
            StuffDone["57_5"] = 2
            return
        SpecialItem.Take("Battery")
        MessageBox("Although it is a tight squeeze, you manage to push the battery in. The heat must have slightly expanded the opening. You close the hatch on the opening to complete the circuit. Hopefully, you can now use the teleporter.")
        StuffDone["57_5"] = 3
        Town.AlterTerrain(Location(6,60), 0, TerrainRecord.UnderlayList[170])
        return

def ArgadonsLab_1601_MapTrigger_19_49(p):
    if StuffDone["57_9"] == 250:
        return
    StuffDone["57_9"] = 250
    TownMap.List["ArgadonsLab_66"].DeactivateTrigger(Location(19,49))
    MessageBox("This smooth passage slopes downward steeply. You are guessing that the liquid from the nearby tank travels through this passage once the gate is opened.")

def ArgadonsLab_1602_MapTrigger_12_49(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(11,49)).Num == 139:
        MessageBox("The corridor veers sharply to the south here where it continues downward to who knows where. This wall has taken quite a beating over the years of experimentation. A sizable force could punch through it.")
        return

def ArgadonsLab_1603_MapTrigger_20_48(p):
    if StuffDone["57_8"] >= 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(11,49)).Num == 139:
            Town.AlterTerrain(Location(11,49), 0, TerrainRecord.UnderlayList[166])
            for x in range(7, 11):
                for y in range(48, 51):
                    if Maths.Rand(1,0,100) <= 25:
                        Town.PlaceField(Location(x,y), Field.SMALL_SLIME)
            for x in range(7, 11):
                for y in range(48, 51):
                    if Maths.Rand(1,0,100) <= 20:
                        Town.PlaceField(Location(x,y), Field.LARGE_SLIME)
            if StuffDone["57_5"] >= 3:
                Town.AlterTerrain(Location(6,60), 0, TerrainRecord.UnderlayList[170])
                return
            return
        return

def ArgadonsLab_1604_MapTrigger_30_47(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["57_8"] == 0:
            if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(25,47)).Num == 71:
                Animation_Hold(-1, 028_waterfall)
                Wait()
                MessageBox("You pull the lever and hear the sound of water draining from the pool and roaring down the passageway. When it is finished, you hear the tank refilling.")
                for x in range(25, 28):
                    for y in range(47, 50):
                        if Maths.Rand(1,0,100) <= 100:
                            Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
                Timer(Town, 100, False, "ArgadonsLab_1639_TownTimer_19", eTimerType.DELETE)
                foundit = False
                if Game.Mode != eMode.OUTSIDE:
                    for x in range(Town.Width):
                        for y in range(Town.Height):
                            if Town.FieldThere(Location(x,y), Field.BARREL):
                                foundit = True
                                break
                        if foundit == True: break
                if foundit == True:
                    return
                Animation_Hold(-1, 060_smallboom)
                Wait()
                MessageBox("Soon afterward, the roar of water becomes more like a tumbling of rocks. You hear it slam into a wall and the distinct sound of something shattering. It appears that extra stuff had a neat effect on the water.")
                StuffDone["57_8"] = 1
                Town.AlterTerrain(Location(11,49), 0, TerrainRecord.UnderlayList[166])
                for x in range(7, 11):
                    for y in range(48, 51):
                        if Maths.Rand(1,0,100) <= 25:
                            Town.PlaceField(Location(x,y), Field.SMALL_SLIME)
                for x in range(7, 11):
                    for y in range(48, 51):
                        if Maths.Rand(1,0,100) <= 20:
                            Town.PlaceField(Location(x,y), Field.LARGE_SLIME)
                if StuffDone["57_5"] >= 3:
                    Town.AlterTerrain(Location(6,60), 0, TerrainRecord.UnderlayList[170])
                    return
                return
            MessageBox("You pull the lever, but nothing seems to happen.")
            return
        MessageBox("You pull the lever, but nothing seems to happen.")
        return

def ArgadonsLab_1605_MapTrigger_28_32(p):
    MessageBox("This desk contains information on a discovery of a special kind of fluid. The green fluid in the nearby barrel is like a normal liquid except that when force is applied to it becomes hard and solid.")

def ArgadonsLab_1606_MapTrigger_5_47(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This door has rusted shut and will not budge despite your best attempts.")

def ArgadonsLab_1607_MapTrigger_6_60(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(6,60)).Num == 247:
        result = ChoiceBox("On this table lies several gray metallic cylinders. One side is marked with a plus sign and the other is marked with a minus sign. If you really wanted to lug one of these heavy things around you could.", eDialogPic.TERRAIN, 251, ["Leave", "Take"])
        if result == 1:
            if StuffDone["57_5"] == 0:
                StuffDone["57_5"] = 1
                MessageBox("You take the large cylinder. It is quite heavy and bulky, but you can manage.")
                SpecialItem.Give("Battery")
                return
            MessageBox("Seeing little point in carrying two bulky batteries around, you decide to put the other one back before you take the new one.")
            return
        return

def ArgadonsLab_1608_MapTrigger_7_8(p):
    if StuffDone["57_6"] == 0:
        MessageBox("These are the controls to some kind of thermal experiment. That part you do not really understand. However, you also notice these controls will allow you to affect the temperature by running heated liquid through the walls. The device is currently off.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            MessageBox("You press the button. The changes you have enacted immediately begin to take effect.")
            if StuffDone["57_6"] == 0: StuffDone["57_6"] = 1
            else: StuffDone["57_6"] = 0
            return
        return
    MessageBox("These are the controls to some kind of thermal experiment. That part you do not really understand. However, you also notice these controls will allow you to affect the temperature by running heated liquid through the walls. The device is currently on.")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        MessageBox("You press the button. The changes you have enacted immediately begin to take effect.")
        if StuffDone["57_6"] == 0: StuffDone["57_6"] = 1
        else: StuffDone["57_6"] = 0
        return

def ArgadonsLab_1609_MapTrigger_11_9(p):
    if StuffDone["57_6"] == 1:
        if StuffDone["58_0"] == 250:
            return
        StuffDone["58_0"] = 250
        MessageBox("You notice that this room has already heated up by several degrees. You presume the same effect can be observed throughout the rest of the lab. The machinery here is old but effective.")
        return

def ArgadonsLab_1611_MapTrigger_33_39(p):
    MessageBox("You find a note that describes something called the Telepathic Chair. By sitting in the chair, a person is shown random images of the surrounding area and can partially interact with them. The designers note little practical application to this.")

def ArgadonsLab_1612_MapTrigger_37_46(p):
    if Game.Mode == eMode.COMBAT:
        return;
    result = ChoiceBox("My what an interesting chair! The seat is covered with an assortment of runes. It seems to radiate a strange mental energy. One of you could dare to sit in the chair.", eDialogPic.TERRAIN, 171, ["Leave", "Sit"])
    if result == 1:
        pc = SelectPCBox("Select one member of your party?",True)
        if pc == None:
            p.CancelAction = True
            return
        Party.Split(pc, Location(7,58))
        Sound.Play("010_teleport")
        return

def ArgadonsLab_1613_MapTrigger_6_58(p):
    if StuffDone["58_1"] == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(30,58))
        p.CancelAction = True
        return

def ArgadonsLab_1616_MapTrigger_29_58(p):
    if StuffDone["58_1"] == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(41,12))
        p.CancelAction = True
        return

def ArgadonsLab_1618_MapTrigger_40_12(p):
    if StuffDone["58_1"] == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(5,16))
        p.CancelAction = True
        return

def ArgadonsLab_1622_MapTrigger_4_16(p):
    if Party.IsSplit:
        Party.Reunite()
        Sound.Play("010_teleport")

def ArgadonsLab_1625_MapTrigger_37_41(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["58_1"] = 1

def ArgadonsLab_1626_MapTrigger_32_35(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["58_1"] = 0

def ArgadonsLab_1628_MapTrigger_24_6(p):
    MessageBox("These controls allow you to set coordinates. It appears you must input four digits to set the coordinates for the snare.")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        response = InputTextBox("Enter something:", "")
        response = response[0:4].upper()
        if response == "3814":
            MessageBox("You input the coordinates. There is no indication whether or not they will be effective.")
            StuffDone["58_2"] = 1
            return
        MessageBox("You input the coordinates. There is no indication whether or not they will be effective.")
        StuffDone["58_2"] = 0
        return

def ArgadonsLab_1629_MapTrigger_24_8(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["57_5"] >= 3:
            Animation_Explosion(Location(27,7), 1, "005_explosion")
            Animation_Hold()
            Wait()
            if StuffDone["58_2"] >= 1:
                if StuffDone["57_4"] == 0:
                    MessageBox("There is a brilliant flash of light and emerging are pieces of an alien statue. Immediately they fall to the floor. It appears that the snare failed to take the entire statue, but a good portion of it.")
                    StuffDone["57_4"] = 1
                    if Maths.Rand(1,0,100) <= 100:
                        Town.PlaceField(Location(27,7), Field.ROCKS)
                    return
                MessageBox("There is a brilliant flash of light on the rune. However, nothing else appears to have occurred.")
                return
            MessageBox("There is a brilliant flash of light on the rune. However, nothing else appears to have occurred.")
            return
        MessageBox("Nothing happens.")
        return

def ArgadonsLab_1630_MapTrigger_40_8(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(41,8)).Num == 169:
        if SpecialItem.PartyHas("BlessedAtheme"):
            MessageBox("The Blessed Atheme cuts right through the waxy magic seal like a knife cutting through butter. As soon as you make the first slice, the entire seal begins to melt away. You may now proceed.")
            for x in range(41, 42):
                for y in range(8, 10):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[224])
            return
        ChoiceBox("You encounter a strange kind of barrier you have never seen before. Although it is clearly a magical construct, it is not made from magical energy. This barrier has a material, and wax-like form.\n\nThe wax looks very easy to slice through, but your weapons just slide right off and your spells are deflected. No matter how hard you try, you cannot slice through this barrier.\n\nPerhaps you should consult an expert in these matters.", eDialogPic.TERRAIN, 231, ["OK"])
        StuffDone["54_2"] = 1
        return

def ArgadonsLab_1632_MapTrigger_43_8(p):
    if StuffDone["58_3"] == 250:
        return
    StuffDone["58_3"] = 250
    TownMap.List["ArgadonsLab_66"].DeactivateTrigger(Location(43,8))
    TownMap.List["ArgadonsLab_66"].DeactivateTrigger(Location(43,9))
    MessageBox("Altrus sure went to the trouble of defending his lab. First he employed the work of a deadly statue, next a magical seal, and now he has enlisted the help of a few hungry undead.")
    Town.PlaceEncounterGroup(1)

def ArgadonsLab_1634_MapTrigger_54_15(p):
    ChoiceBox("You have discovered another one of those machines that Altrus constructed. It looks very similar to the one you found back at Morbane\'s Crypt. You touch the crystal, hoping to learn a little bit more.\n\nThis time you are more prepared for the mental rush. You see many of the same references to Dark Metal, mentions about energy nodes, and an assortment of other alien terms.\n\nFinally, you must withdraw. You pull away none the smarter. It looks like this lead has ended cold so far. However, there may be other information lying around.", eDialogPic.STANDARD, 1026, ["OK"])
    StuffDone["55_1"] = 1

def ArgadonsLab_1636_MapTrigger_56_3(p):
    ChoiceBox("You peer into this learning crystal. It seems to be some kind of alien spell book. The concepts contained within are quite foreign to you. Completely different symbols and practices makes understanding the rituals quite difficult.\n\nHowever, you manage to latch on to one of the simpler spells. It takes a while, but you manage to learn how to cast \'Simulacrum\'. This spell allows the user to summon creatures that were \'captured\' through the spell, \'Capture Soul\'.\n\nUnfortunately, the reference does not contain such information on that spell for whatever reason. Additionally, in order to cast either spell, one would require a \'Soul Crystal\'. You have no idea where you can find that either.", eDialogPic.TERRAIN, 168, ["OK"])
    StuffDone["121_1"] = 1
    if StuffDone["121_2"] == 1:
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_simulacrum")
        return

def ArgadonsLab_1637_MapTrigger_54_3(p):
    MessageBox("You peer into this crystal. It contains a lot of information. Unfortunately, you are unable to use any of it because you lack the capability to understand it.")

def ArgadonsLab_1638_MapTrigger_40_3(p):
    if StuffDone["58_5"] == 0:
        result = ChoiceBox("You open this cabinet and discover one object, a crystal. However, this crystal is unlike any other crystal you have seen. It radiates a kind of mental energy that touches your minds.\n\nIt is almost as if the crystal is trying to teach you something. It also almost feels that the crystal has a kind of life within it, although not sentient. This could be very interesting to use or some mage may wish to study it.", eDialogPic.TERRAIN, 169, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("LearningCrystal_343")
            MessageBox("You take the crystal, it seems to radiate knowledge upon coming into contact with it.")
            StuffDone["58_5"] = 1
            return
        return

def ArgadonsLab_1639_TownTimer_19(p):
    for x in range(25, 28):
        for y in range(47, 50):
            if Maths.Rand(1,0,100) <= 100:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[71])
