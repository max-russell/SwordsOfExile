
def UnicornGate_139_MapTrigger_22_22(p):
    if StuffDone["7_0"] == 250:
        return
    StuffDone["7_0"] = 250
    TownMap.List["UnicornGate_7"].DeactivateTrigger(Location(22,22))
    TownMap.List["UnicornGate_7"].DeactivateTrigger(Location(21,22))
    TownMap.List["UnicornGate_7"].DeactivateTrigger(Location(22,9))
    TownMap.List["UnicornGate_7"].DeactivateTrigger(Location(21,9))
    MessageBox("The air in here is clean and fresh, and the walls glow with their own soft luminescence. Although it is a lovely place, this gate house is still rather effectively blocking your progress down this passage.")

def UnicornGate_143_MapTrigger_20_18(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(21,17)).Num == 147:
        if SpecialItem.PartyHas("UnicornCharm"):
            MessageBox("The gates in the walls are also glowing. However, the glow has a slightly more red, harsher tone. When you get close, the amber charm the unicorns gave you begins to glow. The gates open smoothly, allowing you to pass.")
            Town.AlterTerrain(Location(21,14), 0, TerrainRecord.UnderlayList[148])
            Town.AlterTerrain(Location(22,14), 0, TerrainRecord.UnderlayList[148])
            Town.AlterTerrain(Location(21,17), 0, TerrainRecord.UnderlayList[148])
            Town.AlterTerrain(Location(22,17), 0, TerrainRecord.UnderlayList[148])
            return
        MessageBox("The gates in the walls are also glowing. However, the glow has a slightly more red, harsher tone. You touch the bars ... they\'re hot. They\'ll probably be difficult to open, if not impossible.")
        return

def UnicornGate_151_MapTrigger_18_16(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(17,15)).Num == 147:
        MessageBox("The amber charm begins to glow again. The gates open.")
        Town.AlterTerrain(Location(17,15), 0, TerrainRecord.UnderlayList[148])
        Town.AlterTerrain(Location(17,16), 0, TerrainRecord.UnderlayList[148])
        return

def UnicornGate_153_MapTrigger_6_18(p):
    result = ChoiceBox("The unicorns have created a beautiful garden inside this dome. An artificial, magical sun floats above you, shining cheerily down onto the grass and trees. How the unicorns got the seeds, you can\'t guess, but what they\'ve done with them is remarkable.\n\nThe air is so invigorating and the grove is so pleasant that resting here would be a lot calmer and healthier that resting outside.", eDialogPic.TERRAIN, 79, ["Leave", "Rest"])
    if result == 1:
        MessageBox("You lie down on the grass and sleep very well. When you wake up, for a few moments, you believe that you\'re on the surface again. Then you remember where you are, and your spirits fall again.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += 250
            Party.HealAll(200)
            Party.RestoreSP(200)
        return

def UnicornGate_154_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(7, 28),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(7, 30),WorldMap.SectorAt(Party.OutsidePos))
