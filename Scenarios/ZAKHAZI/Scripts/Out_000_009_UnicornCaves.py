
def UnicornCaves_627_MapTrigger_41_41(p):
    if StuffDone["209_0"] == 250:
        return
    StuffDone["209_0"] = 250
    WorldMap.DeactivateTrigger(Location(41,473))
    WorldMap.DeactivateTrigger(Location(40,473))
    WorldMap.DeactivateTrigger(Location(39,473))
    ChoiceBox("When you walk into this huge cavern, you have to look twice to make sure your eyes aren\'t misleading you. So far, the caves of the Za-Khazi run have been your ordinary Exile caverns - rough, wild, filled with fungi and rubble.\n\nThis cavern, on the other hand, has been carefully cultivated. It lacks the rubble and rough ground, instead being filled with carefully arranges groves of twisted trees and tall, creamy white toadstools.\n\nThe ceiling fungi in this cavern glow brighter than normal, giving you a good view of the lovely cavescape. You aren\'t sure who made it like this, but it is undeniably beautiful.\n\nAs you look, you think you catch a glimpse of something white moving in a nearby copse. Then it is gone.", eDialogPic.STANDARD, 8, ["OK"])

def UnicornCaves_630_MapTrigger_11_19(p):
    if StuffDone["209_1"] == 250:
        return
    result = ChoiceBox("Among the mushrooms, you find a small patch of strange, beautiful yellow flowers. Perhaps nobody would mind if you picked a few of them.", eDialogPic.TERRAIN, 73, ["Take", "Leave"])
    if result == 0:
        StuffDone["209_1"] = 250
        WorldMap.AlterTerrain(Location(11,451), 1, None)
        WorldMap.DeactivateTrigger(Location(11,451))
        Party.GiveNewItem("EmberFlowers_369")
    return

def UnicornCaves_631_MapTrigger_34_5(p):
    if StuffDone["209_2"] == 250:
        return
    result = ChoiceBox("The cave wall here is studded with small, red, glittering crystals. One of them protrudes a bit, and would be easy to break off and take with you.", eDialogPic.STANDARD, 2, ["Take", "Leave"])
    if result == 0:
        StuffDone["209_2"] = 250
        WorldMap.DeactivateTrigger(Location(34,437))
        WorldMap.DeactivateTrigger(Location(32,437))
        Party.GiveNewItem("Crystal_222")
    return

def UnicornCaves_632_MapTrigger_32_5(p):
    StuffDone["209_2"] = 0
