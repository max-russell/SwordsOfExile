
def GuardianCave_1147_MapTrigger_14_11(p):
    if StuffDone["25_3"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Crossing over this line of complicated runes proves quite difficult. No matter how hard you try, you cannot seem to move your bodies any further.")
        return

def GuardianCave_1152_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(7, 19),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(7, 23),WorldMap.SectorAt(Party.OutsidePos))

def GuardianCave_1153_TalkingTrigger12(p):
    if StuffDone["24_1"] == 1:
        p.TalkingText = "You inquire about deactivating. She sighs. \"Indeed you have proven yourself worthy to our people by saving countless lives. We will deactivate the runes for you. Alas, we cannot help you with the chasm or the door.\""
        StuffDone["25_3"] = 1
        return
