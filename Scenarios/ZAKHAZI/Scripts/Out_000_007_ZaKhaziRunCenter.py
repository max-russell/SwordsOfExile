
def ZaKhaziRunCenter_605_MapTrigger_36_2(p):
    result = ChoiceBox("As you make your way down this winding path, you notice a glitter from the ground nearby. Looking closer, you find a small, round, iridescent gemstone.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        Party.GiveNewItem("Opal_388")
    return

def ZaKhaziRunCenter_606_MapTrigger_43_21(p):
    if StuffDone["207_1"] == 250:
        return
    StuffDone["207_1"] = 250
    WorldMap.DeactivateTrigger(Location(43,357))
    MessageBox("The cave path slopes sharply upward to the north. The ground is unusually rocky and uneven, even for these tunnels. It will take a while to reach the end.")

def ZaKhaziRunCenter_607_MapTrigger_18_22(p):
    result = ChoiceBox("You have made your way to the top of a large cliff. The stone surface is sheer, with very few footholds. A hundred feet below you, you can see a wide gallery, which looks somewhat familiar.\n\nAfter a while, you come to the conclusion that you could probably climb down the cliff safely. However, you doubt you would be able to make it back up.", eDialogPic.STANDARD, 31, ["Leave", "Climb"])
    if result == 1:
        MessageBox("It takes a few hours, but by making makeshift ropes and working your way down extremely carefully, you finally manage to arrive safely at the bottom of the cliff.")
        Party.Reposition(Location(15, 358))
        p.CancelAction = True
        Party.Age += 800
        return

def ZaKhaziRunCenter_608_MapTrigger_38_19(p):
    result = ChoiceBox("You have made your way to the top of a large cliff. The stone surface is sheer, with very few footholds. A hundred feet below you, you can see a wide gallery, which looks somewhat familiar.\n\nAfter a while, you come to the conclusion that you could probably climb down the cliff safely. However, you doubt you would be able to make it back up.", eDialogPic.STANDARD, 31, ["Leave", "Climb"])
    if result == 1:
        MessageBox("It takes a few hours, but by making makeshift ropes and working your way down extremely carefully, you finally manage to arrive safely at the bottom of the cliff.")
        Party.Reposition(Location(38, 358))
        p.CancelAction = True
        Party.Age += 800
        return

def ZaKhaziRunCenter_609_MapTrigger_43_13(p):
    if StuffDone["207_2"] == 250:
        return
    result = ChoiceBox("Panting and wheezing, you finally reach the top of this long, rubble strewn gallery. Looking back, you don\'t relish the thought of climbing back down.\n\nThe last few hundred feet of the journey were the worst, not only because of fatigue but because all of the boulders were covered with a thin layer of frost. Once you reach the top, you look around to try and figure out why it\'s so cold here.\n\nAfter a short search, you find a large cave entrance. The frost is thickest here, and icicles hang from the stone above your heads.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        StuffDone["207_2"] = 250
        WorldMap.AlterTerrain(Location(43,349), 1, None)
        WorldMap.DeactivateTrigger(Location(43,349))
        ChoiceBox("Being careful not to slip on the ice, you make your way into the tunnel. It goes for about a hundred feet and then opens into a large, beautiful, frozen cavern.\n\nThe walls, floor, and ceiling are covered with sheets of ice. It reflects you, and reflects your reflections, showing your group back to you from an infinite variety of angles.\n\nSoon, however, the reflections of other forms mingle with yours. The ice on what at first appeared to be boulders cracks, revealing large, blue lizards. They were sleeping, until your arrival disturbed them. Now awake, they are very hungry.", eDialogPic.CREATURE2x1, 2, ["OK"])
        WorldMap.SpawnEncounter("Group_0_7_4", p.Target)
        return

def ZaKhaziRunCenter_610_MapTrigger_6_40(p):
    if StuffDone["207_3"] == 250:
        return
    StuffDone["207_3"] = 250
    WorldMap.DeactivateTrigger(Location(6,376))
    WorldMap.DeactivateTrigger(Location(7,376))
    WorldMap.DeactivateTrigger(Location(8,376))
    WorldMap.DeactivateTrigger(Location(9,376))
    MessageBox("You have passed from beauty into darkness. The loveliness of the unicorn\'s caverns are only a memory. Now, you look out over a desolate landscape of stagnant pools, scattered bones, and sharp rubble.\n\nThis enormous cavern is cold and dim, and you can make out stooped, shambling shapes making their way through the grim landscape.")

def ZaKhaziRunCenter_614_MapTrigger_6_34(p):
    if StuffDone["207_4"] == 250:
        return
    StuffDone["207_4"] = 250
    WorldMap.DeactivateTrigger(Location(6,370))
    WorldMap.DeactivateTrigger(Location(8,370))
    WorldMap.DeactivateTrigger(Location(10,370))
    ChoiceBox("As you walk among these algae-choked pools, you notice that the mist suspended above them has started to move towards you. Soon, it takes a more solid form. Insubstantial creatures hover around you. You shiver inside your armor.\n\nThe creatures whisper amongst themselves, seemingly unsure what to do with you. The whispers are so faint and fleeting that you can neither tell what they are saying nor even tell who is speaking.\n\nFinally, one of them says, in a flat, hostile voice, \"What is the word of safe passage?\"", eDialogPic.CREATURE, 58, ["OK"])
    response = InputTextBox("Enter something:", "")
    response = response[0:6].upper()
    if response == "CALAMI":
        MessageBox("When you say the word, the beings flinch back, as if struck. Then, disappointed, they float back out over the pools, and again take on the appearance of harmless mist.")
        return
    MessageBox("One at a time, they all whisper \"Wrong.\" They then charge you, hoping to feed to feed on your still living flesh.")
    WorldMap.SpawnEncounter("Group_0_7_5", p.Target)

def ZaKhaziRunCenter_618_SpecialOnWin0(p):
    MessageBox("The drakes had a good deal of treasure, although it takes a while to chip it out of the ice. There\'s a lot of gold, and a frozen giant lizard or two for food. While you aren\'t able to recover a few scrolls, there\'s also a nice wand.\n\nFinally, below all of the gold and other loot, you eventually dig down to a large, bronze key. The handle end is worked into the shape of a dragon\'s head.")
    Party.GiveNewItem("PrismaticWand_209")
    Party.Gold += 500
    Party.Food += 150
    SpecialItem.Give("DrakeKey")
