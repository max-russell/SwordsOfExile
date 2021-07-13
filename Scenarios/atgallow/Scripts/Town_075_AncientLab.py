
def AncientLab_1852_MapTrigger_1_1(p):
    if StuffDone["64_7"] >= 1:
        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[78])
        if StuffDone["64_8"] == 250:
            return
        StuffDone["64_8"] = 250
        Animation_Hold(-1, 005_explosion)
        Wait()
        ChoiceBox("It worked! With the pentagram as the power source and the gems to focus and activate the portal, you manage to open the portal. It should lead you into the underground chambers.\n\nHowever, it has been many centuries since the portal has been used. It could be risky.", eDialogPic.STANDARD, 22, ["OK"])
        return

def AncientLab_1853_MapTrigger_30_22(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(30,22)).Num == 78:
        result = ChoiceBox("This portal will (hopefully) take you to the underground chambers. From there, you will possibly be able to access the central structure. It looks safe. Of course, entering ancient portals is quite risky.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            Animation_Hold(-1, 010_teleport)
            Wait()
            if StuffDone["64_7"] >= 3:
                if StuffDone["64_7"] < 4:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(30,28), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(32,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(31,31), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(29,31), True):
                                        if i.SpecialClass == 26:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("Prismitite_388")
                                    itemthere = False
                                    if Game.Mode != eMode.OUTSIDE:
                                        for i in Town.EachItemThere(Location(28,29), True):
                                            if i.SpecialClass == 30:
                                                itemthere = True
                                                break
                                    if itemthere == True:
                                        Party.GiveNewItem("DreamQuartz_389")
                                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                            p.CancelAction = True
                                            return
                                        Animation_FadeDown()
                                        Wait()
                                        Party.Pos = Location(30,49)
                                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                        return
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(30,49)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(28,29), True):
                                        if i.SpecialClass == 30:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("DreamQuartz_389")
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(30,49)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(29,31), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(28,29), True):
                                        if i.SpecialClass == 30:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("DreamQuartz_389")
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(30,49)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(31,31), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(29,31), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(28,29), True):
                                        if i.SpecialClass == 30:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("DreamQuartz_389")
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(30,49)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(30,49)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(32,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(31,31), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(29,31), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(28,29), True):
                                        if i.SpecialClass == 30:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("DreamQuartz_389")
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(30,49)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(30,49)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(31,31), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(30,49)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(30,49)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(30,49)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(30,49)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(30,49)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(30,49)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(30,28), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(32,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(31,31), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(29,31), True):
                                    if i.SpecialClass == 31:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("VulcanAmber_390")
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(28,29), True):
                                        if i.SpecialClass == 31:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("VulcanAmber_390")
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(56,12)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(56,12)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 31:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("VulcanAmber_390")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(56,12)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 31:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("VulcanAmber_390")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(56,12)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(31,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 31:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("VulcanAmber_390")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(56,12)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(56,12)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(32,29), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(31,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 31:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("VulcanAmber_390")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(56,12)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(56,12)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(31,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 31:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("VulcanAmber_390")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(56,12)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(56,12)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(56,12)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(56,12)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(28,29), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(56,12)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(56,12)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            if StuffDone["64_7"] < 2:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(30,28), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(32,29), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(31,31), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(29,31), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                itemthere = False
                                if Game.Mode != eMode.OUTSIDE:
                                    for i in Town.EachItemThere(Location(28,29), True):
                                        if i.SpecialClass == 26:
                                            itemthere = True
                                            break
                                if itemthere == True:
                                    Party.GiveNewItem("Prismitite_388")
                                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                        p.CancelAction = True
                                        return
                                    Animation_FadeDown()
                                    Wait()
                                    Party.Pos = Location(18,23)
                                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                    return
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(18,23)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(18,23)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(18,23)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(31,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(18,23)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,23)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(32,29), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(31,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 26:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("Prismitite_388")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(18,23)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,23)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(31,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,23)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,23)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("DreamQuartz_389")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,23)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,23)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(28,29), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,23)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(18,23)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(30,28), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                Party.GiveNewItem("DreamQuartz_389")
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(32,29), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("DreamQuartz_389")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(31,31), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("VulcanAmber_390")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(29,31), True):
                                if i.SpecialClass == 26:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("Prismitite_388")
                            itemthere = False
                            if Game.Mode != eMode.OUTSIDE:
                                for i in Town.EachItemThere(Location(28,29), True):
                                    if i.SpecialClass == 30:
                                        itemthere = True
                                        break
                            if itemthere == True:
                                Party.GiveNewItem("DreamQuartz_389")
                                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                    p.CancelAction = True
                                    return
                                Animation_FadeDown()
                                Wait()
                                Party.Pos = Location(18,53)
                                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                                return
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,53)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,53)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,53)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(31,31), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,53)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(28,29), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("DreamQuartz_389")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(18,53)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(32,29), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                Party.GiveNewItem("DreamQuartz_389")
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(31,31), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("VulcanAmber_390")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(29,31), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("Prismitite_388")
                        itemthere = False
                        if Game.Mode != eMode.OUTSIDE:
                            for i in Town.EachItemThere(Location(28,29), True):
                                if i.SpecialClass == 30:
                                    itemthere = True
                                    break
                        if itemthere == True:
                            Party.GiveNewItem("DreamQuartz_389")
                            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                                p.CancelAction = True
                                return
                            Animation_FadeDown()
                            Wait()
                            Party.Pos = Location(18,53)
                            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                            return
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(28,29), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("DreamQuartz_389")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(18,53)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(31,31), True):
                    if i.SpecialClass == 31:
                        itemthere = True
                        break
            if itemthere == True:
                Party.GiveNewItem("VulcanAmber_390")
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("Prismitite_388")
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        Party.GiveNewItem("DreamQuartz_389")
                        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                            p.CancelAction = True
                            return
                        Animation_FadeDown()
                        Wait()
                        Party.Pos = Location(18,53)
                        Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                        return
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(28,29), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("DreamQuartz_389")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(18,53)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(29,31), True):
                    if i.SpecialClass == 26:
                        itemthere = True
                        break
            if itemthere == True:
                Party.GiveNewItem("Prismitite_388")
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(28,29), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    Party.GiveNewItem("DreamQuartz_389")
                    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                        p.CancelAction = True
                        return
                    Animation_FadeDown()
                    Wait()
                    Party.Pos = Location(18,53)
                    Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                    return
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(18,53)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(28,29), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                Party.GiveNewItem("DreamQuartz_389")
                if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                    p.CancelAction = True
                    return
                Animation_FadeDown()
                Wait()
                Party.Pos = Location(18,53)
                Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
                return
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(18,53)
            Party.MoveToMap(TownMap.List["UndergroundLabs_78"])
            return
        p.CancelAction = True
        return

def AncientLab_1854_MapTrigger_30_25(p):
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(30,28), True):
            if i.SpecialClass == 31:
                itemthere = True
                break
    if itemthere == True:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(32,29), True):
                if i.SpecialClass == 26:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(31,31), True):
                    if i.SpecialClass == 26:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 30:
                            itemthere = True
                            break
                if itemthere == True:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 26:
                                itemthere = True
                                break
                    if itemthere == True:
                        StuffDone["64_7"] = 1
                        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[78])
                        if StuffDone["64_8"] == 250:
                            return
                        StuffDone["64_8"] = 250
                        Animation_Hold(-1, 005_explosion)
                        Wait()
                        ChoiceBox("It worked! With the pentagram as the power source and the gems to focus and activate the portal, you manage to open the portal. It should lead you into the underground chambers.\n\nHowever, it has been many centuries since the portal has been used. It could be risky.", eDialogPic.STANDARD, 22, ["OK"])
                        return
                    StuffDone["64_7"] = 0
                    Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                    return
                StuffDone["64_7"] = 0
                Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                return
            StuffDone["64_7"] = 0
            Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
            return
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(32,29), True):
                if i.SpecialClass == 31:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(31,31), True):
                    if i.SpecialClass == 26:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 31:
                            itemthere = True
                            break
                if itemthere == True:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 31:
                                itemthere = True
                                break
                    if itemthere == True:
                        StuffDone["64_7"] = 4
                        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[78])
                        if StuffDone["64_8"] == 250:
                            return
                        StuffDone["64_8"] = 250
                        Animation_Hold(-1, 005_explosion)
                        Wait()
                        ChoiceBox("It worked! With the pentagram as the power source and the gems to focus and activate the portal, you manage to open the portal. It should lead you into the underground chambers.\n\nHowever, it has been many centuries since the portal has been used. It could be risky.", eDialogPic.STANDARD, 22, ["OK"])
                        return
                    StuffDone["64_7"] = 0
                    Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                    return
                StuffDone["64_7"] = 0
                Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                return
            StuffDone["64_7"] = 0
            Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
            return
        StuffDone["64_7"] = 0
        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(30,28), True):
            if i.SpecialClass == 30:
                itemthere = True
                break
    if itemthere == True:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(32,29), True):
                if i.SpecialClass == 30:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(31,31), True):
                    if i.SpecialClass == 31:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        StuffDone["64_7"] = 2
                        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[78])
                        if StuffDone["64_8"] == 250:
                            return
                        StuffDone["64_8"] = 250
                        Animation_Hold(-1, 005_explosion)
                        Wait()
                        ChoiceBox("It worked! With the pentagram as the power source and the gems to focus and activate the portal, you manage to open the portal. It should lead you into the underground chambers.\n\nHowever, it has been many centuries since the portal has been used. It could be risky.", eDialogPic.STANDARD, 22, ["OK"])
                        return
                    StuffDone["64_7"] = 0
                    Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                    return
                StuffDone["64_7"] = 0
                Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                return
            StuffDone["64_7"] = 0
            Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
            return
        StuffDone["64_7"] = 0
        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
        return
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(30,28), True):
            if i.SpecialClass == 26:
                itemthere = True
                break
    if itemthere == True:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(32,29), True):
                if i.SpecialClass == 31:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(31,31), True):
                    if i.SpecialClass == 30:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(29,31), True):
                        if i.SpecialClass == 26:
                            itemthere = True
                            break
                if itemthere == True:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(28,29), True):
                            if i.SpecialClass == 30:
                                itemthere = True
                                break
                    if itemthere == True:
                        StuffDone["64_7"] = 3
                        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[78])
                        if StuffDone["64_8"] == 250:
                            return
                        StuffDone["64_8"] = 250
                        Animation_Hold(-1, 005_explosion)
                        Wait()
                        ChoiceBox("It worked! With the pentagram as the power source and the gems to focus and activate the portal, you manage to open the portal. It should lead you into the underground chambers.\n\nHowever, it has been many centuries since the portal has been used. It could be risky.", eDialogPic.STANDARD, 22, ["OK"])
                        return
                    StuffDone["64_7"] = 0
                    Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                    return
                StuffDone["64_7"] = 0
                Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
                return
            StuffDone["64_7"] = 0
            Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
            return
        StuffDone["64_7"] = 0
        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])
        return
    StuffDone["64_7"] = 0
    Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[173])

def AncientLab_1855_MapTrigger_12_35(p):
    if StuffDone["64_9"] == 250:
        return
    StuffDone["64_9"] = 250
    TownMap.List["AncientLab_75"].DeactivateTrigger(Location(12,35))
    TownMap.List["AncientLab_75"].DeactivateTrigger(Location(13,35))
    TownMap.List["AncientLab_75"].DeactivateTrigger(Location(14,35))
    ChoiceBox("During the centuries of neglect, a large vein of water erupted and flooded this room. The pressure had to give out somewhere and it just happened to be this wall. Good thing too, for now you may enter this lab.", eDialogPic.TERRAIN, 107, ["OK"])

def AncientLab_1859_OnEntry(p):
    if StuffDone["64_7"] >= 1:
        Town.AlterTerrain(Location(30,22), 0, TerrainRecord.UnderlayList[78])
        if StuffDone["64_8"] == 250:
            return
        StuffDone["64_8"] = 250
        Animation_Hold(-1, 005_explosion)
        Wait()
        ChoiceBox("It worked! With the pentagram as the power source and the gems to focus and activate the portal, you manage to open the portal. It should lead you into the underground chambers.\n\nHowever, it has been many centuries since the portal has been used. It could be risky.", eDialogPic.STANDARD, 22, ["OK"])
        return
