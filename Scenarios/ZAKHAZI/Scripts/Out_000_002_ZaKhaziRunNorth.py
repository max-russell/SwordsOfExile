
def ZaKhaziRunNorth_554_MapTrigger_43_23(p):
    if StuffDone["202_0"] == 250:
        return
    result = ChoiceBox("At the end of this passage, you find the wall is covered with massive clumps of lichen. You almost give it up as a dead end and turn back, until you notice a peculiar design on one exposed section of wall.\n\nLooking closer, you see that there\'s more here than just wall and lichen. There\'s a door! It\'s mostly concealed by lichen, but it\'s a door nonetheless. The design you saw was a carving of a dragon. The door is covered with them.", eDialogPic.TERRAIN, 102, ["Leave", "Open"])
    if result == 1:
        if SpecialItem.PartyHas("DrakeKey"):
            if StuffDone["202_0"] == 250:
                return
            result = ChoiceBox("The door is locked. Just on a hunch, you try your keys. The key you recovered from the ice drakes unlocks the door!\n\nYou open the door and find a small treasure cache. It\'s mostly silver and copper coins, many of them very old. There\'s also a flask and a beautiful old spear. While stealing a dragon\'s horde is a risky proposition, it\'s also awfully tempting ...", eDialogPic.TERRAIN, 102, ["Take", "Leave"])
            if result == 0:
                StuffDone["202_0"] = 250
                WorldMap.AlterTerrain(Location(43,119), 1, None)
                WorldMap.DeactivateTrigger(Location(43,119))
                Party.GiveNewItem("MagicSpear_81")
                Party.Gold += 1000
                Party.GiveNewItem("StrongEnergyP_248")
                return
            return
            return
        MessageBox("You try to open the door, but it\'s locked. You find a handle and a keyhole, choked with lichen. Unfortunately, you don\'t have the key. Your best efforts don\'t budge the door. You leave.")
        return

def ZaKhaziRunNorth_555_MapTrigger_31_36(p):
    if Party.HasTrait(Trait.CaveLore):
        MessageBox("Your keen eye and knowledge of Cave Lore tips you off that the ceiling in this area is very unstable. You pass through carefully, and avoid harm.")
        return
    MessageBox("The ceiling in this passage is very loose and unstable. As you pass, a few chunks of it obligingly fall on you. You try to spot signs of other loose rocks, but you don\'t know what to look for.")
    Party.Damage(Maths.Rand(8, 1, 8) + 0, eDamageType.WEAPON)
    Wait()

def ZaKhaziRunNorth_561_MapTrigger_7_18(p):
    if StuffDone["202_1"] == 250:
        return
    StuffDone["202_1"] = 250
    WorldMap.DeactivateTrigger(Location(7,114))
    MessageBox("When you reach the end of this cavern, a small cavequake hits! As stone starts flying and stone dust covers you, you hit the ground. When it passes, you are unharmed. However, the tunnel you came down to get here has caved in.\n\nAt first, you think you\'re doomed. Then, upon inspection, you see that it wasn\'t as bad as it looks. You eventually dig your way out. However, it costs you over twelve hours of precious time.")
    Party.Age += 2000
    WorldMap.AlterTerrain(Location(6,114), 0, TerrainRecord.UnderlayList[84])
