
def SchoolEntry_38_MapTrigger_8_24(p):
    if StuffDone["5_0"] == 250:
        return
    StuffDone["5_0"] = 250
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(8,24))
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(24,8))
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(40,24))
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(24,41))
    ChoiceBox("For the first time, you stand at the entrance to the School of Magery.\n\nYou know practically nothing about it. It\'s a huge structure, and was clearly once quite beautiful. You have no idea how far down it goes, or what wonders and horrors are concealed inside.\n\nIt\'s been abandoned by its former owners. That much is clear. There is dust and trash everywhere, and the massive portcullis just inside is closed to travelers. But why did they leave? And what is inside?\n\nAnd, most importantly, does it have anything to do with the curse that is tearing the Vale apart bit by bit?", eDialogPic.TERRAIN, 104, ["OK"])

def SchoolEntry_42_MapTrigger_34_24(p):
    if StuffDone["5_3"] == 250:
        return
    if SpecialItem.PartyHas("RunedStone"):
        if StuffDone["5_3"] == 250:
            return
        result = ChoiceBox("You stand before a massive iron portcullis. To the right, on the wall, you notice a small circular depression. Interestingly, it looks like Avizo\'s stone would fit snugly inside it.", eDialogPic.TERRAIN, 104, ["Leave", "Insert"])
        if result == 1:
            StuffDone["5_3"] = 250
            TownMap.List["SchoolEntry_5"].AlterTerrain(Location(34,24), 1, None)
            TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(34,24))
            if StuffDone["5_1"] >= 1:
                if StuffDone["5_2"] >= 1:
                    if StuffDone["5_3"] >= 1:
                        if StuffDone["5_4"] >= 1:
                            StuffDone["5_5"] = 1
                            ChoiceBox("With a satisfying click, you place the opening stone into the last of the 4 depressions. At first, you think nothing has happened. There is a long pause, while long dormant machinery grinds back to life.\n\nThen, with a bone-jarring squeal, the old gears begin to grind. As showers of rust flakes rain down upon you, the portcullis opens. Soon, your way unbarred, you stare into the darkness of the abandoned school.\n\nAt first, things are deathly quiet. Then, silently at first, then louder, you begin to hear growling and muttering. While the school\'s owners may have abandoned it, it seems other creatures have somehow taken up residence ...", eDialogPic.TERRAIN, 105, ["OK"])
                            t = Town.TerrainAt(Location(15,24)).TransformTo
                            Town.AlterTerrain(Location(15,24), 0, t)
                            t = Town.TerrainAt(Location(24,15)).TransformTo
                            Town.AlterTerrain(Location(24,15), 0, t)
                            Town.AlterTerrain(Location(24,34), 0, TerrainRecord.UnderlayList[148])
                            Town.AlterTerrain(Location(33,24), 0, TerrainRecord.UnderlayList[148])
                            StuffDone["199_0"] = 1
                            return
                        MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                        return
                    MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                    return
                MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                return
            MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
            return
        return
    ChoiceBox("You walk up to the massive iron portcullis, which is presenting quite an imposing barrier to your entry. The bars are close together, thick and strong, and, you suspect, magically augmented as well.\n\nYou look around for anything that could help you gain entry. The only thing of interest you find is a small circular depression in the wall to the right of the portcullis. Unfortunately, you have nothing that would fit inside it.\n\nDisappointed, you turn back.", eDialogPic.TERRAIN, 104, ["OK"])

def SchoolEntry_43_MapTrigger_24_35(p):
    if StuffDone["5_2"] == 250:
        return
    if SpecialItem.PartyHas("RunedStone"):
        if StuffDone["5_2"] == 250:
            return
        result = ChoiceBox("You stand before a massive iron portcullis. To the right, on the wall, you notice a small circular depression. Interestingly, it looks like Avizo\'s stone would fit snugly inside it.", eDialogPic.TERRAIN, 104, ["Leave", "Insert"])
        if result == 1:
            StuffDone["5_2"] = 250
            TownMap.List["SchoolEntry_5"].AlterTerrain(Location(24,35), 1, None)
            TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(24,35))
            if StuffDone["5_1"] >= 1:
                if StuffDone["5_2"] >= 1:
                    if StuffDone["5_3"] >= 1:
                        if StuffDone["5_4"] >= 1:
                            StuffDone["5_5"] = 1
                            ChoiceBox("With a satisfying click, you place the opening stone into the last of the 4 depressions. At first, you think nothing has happened. There is a long pause, while long dormant machinery grinds back to life.\n\nThen, with a bone-jarring squeal, the old gears begin to grind. As showers of rust flakes rain down upon you, the portcullis opens. Soon, your way unbarred, you stare into the darkness of the abandoned school.\n\nAt first, things are deathly quiet. Then, silently at first, then louder, you begin to hear growling and muttering. While the school\'s owners may have abandoned it, it seems other creatures have somehow taken up residence ...", eDialogPic.TERRAIN, 105, ["OK"])
                            t = Town.TerrainAt(Location(15,24)).TransformTo
                            Town.AlterTerrain(Location(15,24), 0, t)
                            t = Town.TerrainAt(Location(24,15)).TransformTo
                            Town.AlterTerrain(Location(24,15), 0, t)
                            Town.AlterTerrain(Location(24,34), 0, TerrainRecord.UnderlayList[148])
                            Town.AlterTerrain(Location(33,24), 0, TerrainRecord.UnderlayList[148])
                            StuffDone["199_0"] = 1
                            return
                        MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                        return
                    MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                    return
                MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                return
            MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
            return
        return
    ChoiceBox("You walk up to the massive iron portcullis, which is presenting quite an imposing barrier to your entry. The bars are close together, thick and strong, and, you suspect, magically augmented as well.\n\nYou look around for anything that could help you gain entry. The only thing of interest you find is a small circular depression in the wall to the right of the portcullis. Unfortunately, you have nothing that would fit inside it.\n\nDisappointed, you turn back.", eDialogPic.TERRAIN, 104, ["OK"])

def SchoolEntry_44_MapTrigger_14_24(p):
    if StuffDone["5_4"] == 250:
        return
    if SpecialItem.PartyHas("RunedStone"):
        result = ChoiceBox("You stand before a massive iron portcullis. To the right, on the wall, you notice a small circular depression. Interestingly, it looks like Avizo\'s stone would fit snugly inside it.", eDialogPic.TERRAIN, 104, ["Leave", "Insert"])
        if result == 1:
            if StuffDone["5_4"] == 250:
                return
            StuffDone["5_4"] = 250
            TownMap.List["SchoolEntry_5"].AlterTerrain(Location(14,24), 1, None)
            TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(14,24))
            if StuffDone["5_1"] >= 1:
                if StuffDone["5_2"] >= 1:
                    if StuffDone["5_3"] >= 1:
                        if StuffDone["5_4"] >= 1:
                            StuffDone["5_5"] = 1
                            ChoiceBox("With a satisfying click, you place the opening stone into the last of the 4 depressions. At first, you think nothing has happened. There is a long pause, while long dormant machinery grinds back to life.\n\nThen, with a bone-jarring squeal, the old gears begin to grind. As showers of rust flakes rain down upon you, the portcullis opens. Soon, your way unbarred, you stare into the darkness of the abandoned school.\n\nAt first, things are deathly quiet. Then, silently at first, then louder, you begin to hear growling and muttering. While the school\'s owners may have abandoned it, it seems other creatures have somehow taken up residence ...", eDialogPic.TERRAIN, 105, ["OK"])
                            t = Town.TerrainAt(Location(15,24)).TransformTo
                            Town.AlterTerrain(Location(15,24), 0, t)
                            t = Town.TerrainAt(Location(24,15)).TransformTo
                            Town.AlterTerrain(Location(24,15), 0, t)
                            Town.AlterTerrain(Location(24,34), 0, TerrainRecord.UnderlayList[148])
                            Town.AlterTerrain(Location(33,24), 0, TerrainRecord.UnderlayList[148])
                            StuffDone["199_0"] = 1
                            return
                        MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                        return
                    MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                    return
                MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                return
            MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
            return
        return
    ChoiceBox("You walk up to the massive iron portcullis, which is presenting quite an imposing barrier to your entry. The bars are close together, thick and strong, and, you suspect, magically augmented as well.\n\nYou look around for anything that could help you gain entry. The only thing of interest you find is a small circular depression in the wall to the right of the portcullis. Unfortunately, you have nothing that would fit inside it.\n\nDisappointed, you turn back.", eDialogPic.TERRAIN, 104, ["OK"])

def SchoolEntry_45_MapTrigger_24_14(p):
    if StuffDone["5_1"] == 250:
        return
    if SpecialItem.PartyHas("RunedStone"):
        if StuffDone["5_1"] == 250:
            return
        result = ChoiceBox("You stand before a massive iron portcullis. To the right, on the wall, you notice a small circular depression. Interestingly, it looks like Avizo\'s stone would fit snugly inside it.", eDialogPic.TERRAIN, 104, ["Leave", "Insert"])
        if result == 1:
            StuffDone["5_1"] = 250
            TownMap.List["SchoolEntry_5"].AlterTerrain(Location(24,14), 1, None)
            TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(24,14))
            if StuffDone["5_1"] >= 1:
                if StuffDone["5_2"] >= 1:
                    if StuffDone["5_3"] >= 1:
                        if StuffDone["5_4"] >= 1:
                            StuffDone["5_5"] = 1
                            ChoiceBox("With a satisfying click, you place the opening stone into the last of the 4 depressions. At first, you think nothing has happened. There is a long pause, while long dormant machinery grinds back to life.\n\nThen, with a bone-jarring squeal, the old gears begin to grind. As showers of rust flakes rain down upon you, the portcullis opens. Soon, your way unbarred, you stare into the darkness of the abandoned school.\n\nAt first, things are deathly quiet. Then, silently at first, then louder, you begin to hear growling and muttering. While the school\'s owners may have abandoned it, it seems other creatures have somehow taken up residence ...", eDialogPic.TERRAIN, 105, ["OK"])
                            t = Town.TerrainAt(Location(15,24)).TransformTo
                            Town.AlterTerrain(Location(15,24), 0, t)
                            t = Town.TerrainAt(Location(24,15)).TransformTo
                            Town.AlterTerrain(Location(24,15), 0, t)
                            Town.AlterTerrain(Location(24,34), 0, TerrainRecord.UnderlayList[148])
                            Town.AlterTerrain(Location(33,24), 0, TerrainRecord.UnderlayList[148])
                            StuffDone["199_0"] = 1
                            return
                        MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                        return
                    MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                    return
                MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
                return
            MessageBox("You place the stone into the depression. It\'s a perfect match. You wait for several minutes, hoping that something will happen. Nothing does.\n\nDisappointed, you remove the stone from the depression. Only then does something unusual happen. The hole fades away before your eyes, leaving a blank wall. Nothing else happens.")
            return
        return
    ChoiceBox("You walk up to the massive iron portcullis, which is presenting quite an imposing barrier to your entry. The bars are close together, thick and strong, and, you suspect, magically augmented as well.\n\nYou look around for anything that could help you gain entry. The only thing of interest you find is a small circular depression in the wall to the right of the portcullis. Unfortunately, you have nothing that would fit inside it.\n\nDisappointed, you turn back.", eDialogPic.TERRAIN, 104, ["OK"])

def SchoolEntry_46_MapTrigger_30_30(p):
    if StuffDone["5_6"] == 250:
        return
    StuffDone["5_6"] = 250
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(30,30))
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(31,30))
    MessageBox("As you walk down this corridor, you begin to detect a powerful, unpleasant stench, which becomes worse and worse with every passing step. This area is being used as someone\'s dump, and they aren\'t picky about sanitation.")

def SchoolEntry_48_MapTrigger_34_32(p):
    MessageBox("This is interesting - whoever ran the school set up a permanent, magical incinerator here. It is still generating a good deal of heat, even after all these years. Alas, whoever\'s been putting the trash here hasn\'t been bothering to burn it.")

def SchoolEntry_49_MapTrigger_23_26(p):
    if StuffDone["5_7"] == 250:
        return
    StuffDone["5_7"] = 250
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(23,26))
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(24,26))
    TownMap.List["SchoolEntry_5"].DeactivateTrigger(Location(25,26))
    MessageBox("This broad corridor slopes down to the second level of the school. The floor has been worn smooth by the hundreds (if not thousands) of apprentices and teachers that have passed through here.")

def SchoolEntry_52_MapTrigger_23_29(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(25,26)
    Party.MoveToMap(TownMap.List["VisitorsQuarters_6"])

def SchoolEntry_55_OnEntry(p):
    if StuffDone["5_5"] >= 1:
        t = Town.TerrainAt(Location(15,24)).TransformTo
        Town.AlterTerrain(Location(15,24), 0, t)
        t = Town.TerrainAt(Location(24,15)).TransformTo
        Town.AlterTerrain(Location(24,15), 0, t)
        Town.AlterTerrain(Location(24,34), 0, TerrainRecord.UnderlayList[148])
        Town.AlterTerrain(Location(33,24), 0, TerrainRecord.UnderlayList[148])
        StuffDone["199_0"] = 1
        return

def SchoolEntry_56_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(15, 29),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(11, 35),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(15, 39),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(20, 33),WorldMap.SectorAt(Party.OutsidePos))
