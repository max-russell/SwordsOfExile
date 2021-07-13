
def WarZone_539_MapTrigger_20_39(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("There is no way back. You are drawing close to the end of this affair, and have no choice but to do your part.")

def WarZone_540_MapTrigger_35_6(p):
    if StuffDone["111_0"] == 250:
        return
    StuffDone["111_0"] = 250
    WorldMap.DeactivateTrigger(Location(83,54))
    MessageBox("The slith corridor opens up into the Chimney cave near Howling Gap! You remember well the last time you were here, fleeing the slith Sacred Ground and Thunder Rock to the north. These memories mix with the vision Groul sent you as you take in the scene.\n\nTrees have been burned and thrown to the ground. Rocks and stalagmites have been blown up or used as weapons in a series of battles. Corpses, both human and slith, line the roads. A crude wall has been erected to the south, where you see a camp.")

def WarZone_541_MapTrigger_37_3(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The Yvoss-tai still hold Howling Gap. Entering their main camp on your own is a very bad idea.")

def WarZone_542_MapTrigger_37_14(p):
    if StuffDone["18_8"] >= 1:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("A group of Chimney soldiers are hastily raising a defensive wall. They are glad to see you and ask for news of the Yvoss-tai. They suggest you go see Captain Locke in his outpost camp to the north.")
