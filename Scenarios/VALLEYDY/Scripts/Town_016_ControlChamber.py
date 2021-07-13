
def ControlChamber_321_MapTrigger_19_24(p):
    if StuffDone["16_0"] == 250:
        return
    StuffDone["16_0"] = 250
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(19,24))
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(19,25))
    ChoiceBox("You step into the clean, warm halls of the Main Control Center of the School of Magery. To be honest, you still have little idea what a \"Main Control Center\" is supposed to be.\n\nThe air is dry, and a constant, low hum fills the air. The floor is still impeccably clean and polished, and no mold or sign of decay has successfully intruded on this place. Light is no problem. The walls themselves glow with the energy of the place.", eDialogPic.TERRAIN, 229, ["OK"])

def ControlChamber_323_MapTrigger_19_18(p):
    if StuffDone["16_1"] == 250:
        return
    StuffDone["16_1"] = 250
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(19,18))
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(20,18))
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(19,31))
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(20,31))
    ChoiceBox("There can be no more doubt. The School of Magery was not just a teaching institution - some remarkable research was going on here as well. The strange devices in front of you are evidence enough of that.\n\nThis room is filled with strange walls. Or panels. Or devices. You aren\'t sure. They\'re metal, and glow slightly, and emit a constant, soothing hum. Some have flashing lights on them, some buttons. None of them have a clear purpose.\n\nThey\'re truly amazing devices. What they do and if it\'s possible for you to control them, however, remains an open question.", eDialogPic.TERRAIN, 229, ["OK"])

def ControlChamber_327_MapTrigger_25_39(p):
    if StuffDone["16_2"] == 250:
        return
    result = ChoiceBox("The panel here has what looks like some sort of controls. There are several rows of buttons, each of which has a label, none of which you can read.\n\nYou have no idea what to do with any of this. Of course, that doesn\'t stop you from trying.", eDialogPic.TERRAIN, 229, ["Leave", "Push", "Destroy"])
    if result == 1:
        StuffDone["16_2"] = 250
        TownMap.List["ControlChamber_16"].AlterTerrain(Location(25,39), 1, None)
        TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(25,39))
        MessageBox("Unfortunately, you don\'t get far before a security spell gets wind of your interference. The buttons go dark, and you hear a brief alarm.")
        Town.PlaceEncounterGroup(1)
        return
    elif result == 2:
        StuffDone["16_2"] = 250
        TownMap.List["ControlChamber_16"].AlterTerrain(Location(25,39), 1, None)
        TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(25,39))
        MessageBox("Unfortunately, you don\'t get far before a security spell gets wind of your interference. The buttons go dark, and you hear a brief alarm.")
        Town.PlaceEncounterGroup(1)
        return

def ControlChamber_328_MapTrigger_26_5(p):
    if StuffDone["16_3"] == 250:
        return
    result = ChoiceBox("The panel here has a large, friendly button, placed at about waist height. A sign above it reads \"In Case of Injury.\"", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        StuffDone["16_3"] = 250
        TownMap.List["ControlChamber_16"].AlterTerrain(Location(26,5), 1, None)
        TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(26,5))
        MessageBox("The moment you press the button, a sparkling green field appears, surrounding you. You feel it rapidly rejuvenate you, relaxing your muscles and erasing your wounds.\n\nUnfortunately, the green field abruptly disappears. Sparks and a cloud of smoke fly out of the panel. Looks like this device needs constant maintenance to function.")
        Party.HealAll(50)
        return

def ControlChamber_329_MapTrigger_36_37(p):
    if StuffDone["16_5"] == 250:
        return
    result = ChoiceBox("The panel here has a large, friendly button, placed at about waist height. A sign above it reads \"In Case of Injury.\"", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        StuffDone["16_5"] = 250
        TownMap.List["ControlChamber_16"].AlterTerrain(Location(36,37), 1, None)
        TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(36,37))
        MessageBox("The moment you press the button, a sparkling green field appears, surrounding you. You feel it rapidly rejuvenate you, relaxing your muscles and erasing your wounds.\n\nUnfortunately, the green field abruptly disappears. Sparks and a cloud of smoke fly out of the panel. Looks like this device needs constant maintenance to function.")
        Party.HealAll(50)
        return

def ControlChamber_330_MapTrigger_38_10(p):
    if StuffDone["16_4"] == 250:
        return
    result = ChoiceBox("The panel in this little niche has a rectangle of glass set into it, about 1 foot by 1 foot. Peering through the glass, you can see words floating by in the darkness beyond. They\'re dim, but you can just make them out, if you try.", eDialogPic.TERRAIN, 229, ["Leave", "Read", "Destroy"])
    if result == 1:
        StuffDone["16_4"] = 250
        TownMap.List["ControlChamber_16"].AlterTerrain(Location(38,10), 1, None)
        TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(38,10))
        MessageBox("You bent down and peer through the glass, reading the words as they pass by. You read arcane rituals, bits of history, ancient stories, theorems of mathematics, and all manner of other knowledge, carefully assembled and displayed here.\n\nMaybe you watch for an hour, maybe more. Eventually the words displayed begin to repeat themselves, and you walk away, feeling very enlightened.")
        for pc in Party.EachAlivePC():
            pc.SetSkill(eSkill.INTELLIGENCE, pc.GetSkill(eSkill.INTELLIGENCE) + 1)
        return
    elif result == 2:
        StuffDone["16_4"] = 250
        TownMap.List["ControlChamber_16"].AlterTerrain(Location(38,10), 1, None)
        TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(38,10))
        MessageBox("A single blow from your weapon shatters the glass. One less sinister device in the School of Magery.")
        return

def ControlChamber_331_MapTrigger_29_24(p):
    result = ChoiceBox("Here, deep inside the control chambers, you find an ornate, carved stone throne. Strangely, it has been set facing a bare wall. As experience has taught you, when you find something odd and inexplicable, magic must be involved.", eDialogPic.TERRAIN, 161, ["Leave", "Sit"])
    if result == 1:
        MessageBox("When you sit in the throne, words seem to try to form on the wall you\'re facing, coalescing out of thin air in letters of mist. However, before the words manage to come together, the mist dissipates, and they fade again.\n\nYou stand up, confused. Perhaps you aren\'t authorized to use the chair, or perhaps the system is no longer functional.")
        return

def ControlChamber_333_MapTrigger_34_20(p):
    if StuffDone["16_6"] == 250:
        return
    result = ChoiceBox("Here, deep inside the control chambers, you find an ornate, carved stone throne. Strangely, it has been set facing a bare wall. As experience has taught you, when you find something odd and inexplicable, magic must be involved.", eDialogPic.TERRAIN, 161, ["Leave", "Sit"])
    if result == 1:
        if SpecialItem.PartyHas("InstructionsScrolls"):
            ChoiceBox("The moment you sit down, words spring up on the wall before you, written in midair in letters of white mist. The words are in your tongue, but don\'t make sense to you. Phrases like \"Directory Structure\" and \"Flow Control\" are beyond your understanding.\n\nFortunately, you do have the scrolls of instructions you bought from Pangle, and while they didn\'t make any sense before, they do now. From here, you can magically control gates and machinery all throughout the School of Magery.\n\nCommands are issued by pointing at the appropriate words of mist. Searching the instructions, you find the area describing waste disposal. Soon, you are able to bring up the command to reactivate the waste destruction system.\n\nCrossing your fingers, you point at the command. There is a pause, and a short chiming noise. The words \"Power to Waste Cleanup System System Reactivated. Waste Cleanup Panel can now be used.\"\n\nThe letters of mist disappear, and the room goes dark. Hmm. Now where is the Waste Cleanup Panel?", eDialogPic.TERRAIN, 161, ["OK"])
            StuffDone["10_9"] = 1
            if StuffDone["16_6"] == 250:
                return
            StuffDone["16_6"] = 250
            TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(34,20))
            return
        MessageBox("The moment you sit down, words spring up on the wall the chair faces, written in midair in letters of white mist. The words are in your tongue, but don\'t make sense to you. Phrases like \"Directory Structure\" and \"Flow Control\" are beyond you.\n\nWhatever this thing is, you have no idea how to operate it. You stand up before you break it, or kill yourself, or do something similarly unpleasant.")
        return

def ControlChamber_334_MapTrigger_15_4(p):
    if StuffDone["16_7"] == 250:
        return
    StuffDone["16_7"] = 250
    TownMap.List["ControlChamber_16"].DeactivateTrigger(Location(15,4))
    MessageBox("Many years ago, four mages were brought into this cavern and murdered. Their multiply stabbed bodies are arrayed before you. Whoever closed the School of Magery, they wanted to close it for good.")
