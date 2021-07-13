
def ChasmofFire_134_MapTrigger_28_15(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("The lava river becomes far too hot for you to make your way farther up it, magical protected or not.")

def ChasmofFire_137_OnEntry(p):
    if StuffDone["6_0"] == 250:
        return
    StuffDone["6_0"] = 250
    ChoiceBox("Your further progress is blocked by a river of fire. It\'s a slow moving flow of magma, coming from a tunnel to the east and dropping into a chasm to the west.\n\nThe heat has attracted a family of pyrohydras, who have taken this cavern as their own personal health spa. They lurk at the edges of the huge cavern, but they\'ll probably hunt you down if they get the chance.", eDialogPic.CREATURE, 140, ["OK"])

def ChasmofFire_138_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(30, 23),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(30, 25),WorldMap.SectorAt(Party.OutsidePos))
