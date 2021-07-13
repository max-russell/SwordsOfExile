def PlaceRubbleCave(currentmap, pos, ter):
    currentmap.AlterTerrain(pos, ter)

    if ter.ID == "Rubble_85":
       currentmap.AlterTerrain(Location(pos.X+1, pos.Y), TerrainRecord.List["Rubble_86"])
    if ter.ID == "Rubble_86":
       currentmap.AlterTerrain(Location(pos.X-1, pos.Y), TerrainRecord.List["Rubble_85"])
    AdjustTerrain(currentmap, pos)

def PlaceRubbleGrass(currentmap, pos, ter):
    currentmap.AlterTerrain(pos, ter)

    if ter.ID == "Rubble_88":
       currentmap.AlterTerrain(Location(pos.X+1, pos.Y), TerrainRecord.List["Rubble_89"])
    if ter.ID == "Rubble_89":
       currentmap.AlterTerrain(Location(pos.X-1, pos.Y), TerrainRecord.List["Rubble_88"])
    AdjustTerrain(currentmap, pos)

def PlaceMountain(currentmap, pos, ter):
    currentmap.AlterTerrain(pos, ter)

    for x in range(pos.X-1, pos.X+2):
        for y in range(pos.Y-1, pos.Y+2):
            pos2 = Location(x, y)
            t2 = currentmap.TerrainAt(ter.Layer, pos2)
            if t2 is None:
               continue
            if (t2.Num >= 22 and t2.Num <= 35) or (t2.Picture >= 18 and t2.Picture <= 31) or (t2.Picture >= 192 and t2.Picture <= 195):
               continue
            currentmap.AlterTerrain(pos2, "Hills_36")
    AdjustTerrain(currentmap, pos)

def PlaceGeneral(currentmap, pos, ter):
    currentmap.AlterTerrain(pos, ter)
    if ter.Layer == 0:
        AdjustTerrain(currentmap, pos)
    elif ter.Layer == 1:
        AdjustOverlays(currentmap, pos)

def PaintGeneral(currentmap, pos, ter, pattern):
    if ter.Layer == 0:
        for l in pattern.EachPatternSpot(pos):
            currentmap.AlterTerrain(l, ter)
            AdjustTerrain(currentmap, l)
    else:
        for l in pattern.EachPatternSpot(pos):
            currentmap.AlterTerrain(l, ter)
            AdjustOverlays(currentmap, l)


def EraseGeneral(currentmap, pos, ter):
    currentmap.AlterTerrain(pos, TerrainRecord.NoOverlay)
    AdjustOverlays(currentmap, pos)

def SprayGeneral(currentmap, pos, ter, pattern):
    if ter.Layer == 0:
        for l in pattern.EachPatternSpot(pos):
            if Maths.Rand(1,1,7) == 1:
                currentmap.AlterTerrain(l, ter)
                AdjustTerrain(currentmap, l)
    else:
        for l in pattern.EachPatternSpot(pos):
            if Maths.Rand(1,1,7) == 1:
                currentmap.AlterTerrain(l, ter)
                AdjustOverlays(currentmap, l)

rect_topleft = Location(0,0)

def PlaceRect1(currentmap, pos, ter):
    global rect_topleft
    rect_topleft = pos

def PlaceRect2(currentmap, pos, ter):
    if pos.X >= rect_topleft.X and pos.Y >= rect_topleft.Y:
        if ter.Layer == 0:
            for y in range(rect_topleft.Y, pos.Y+1):
                for x in range(rect_topleft.X, pos.X + 1):
                    l = Location(x,y)
                    currentmap.AlterTerrain(l, ter)
                    AdjustTerrain(currentmap, l)
        else:
            for y in range(rect_topleft.Y, pos.Y+1):
                for x in range(rect_topleft.X, pos.X + 1):
                    l = Location(x,y)
                    currentmap.AlterTerrain(l, ter)
                    AdjustOverlays(currentmap, l)

cmap = None

def AdjustTerrain(currentmap, pos):
    global cmap
    cmap = currentmap

    AdjustSpace(pos)
    AdjustSpace(Location(pos.X-1, pos.Y))
    AdjustSpace(Location(pos.X+1, pos.Y))
    AdjustSpace(Location(pos.X, pos.Y-1))
    AdjustSpace(Location(pos.X, pos.Y+1))
    
def AdjustSpace(pos):
    needed_change = False
    if FixRubble(pos): needed_change = True
    if FixCave(pos): needed_change = True
    if FixMountain(pos): needed_change = True
    if FixHill(pos): needed_change = True
    if FixWater(pos): needed_change = True
    if needed_change:
        AdjustSpace(Location(pos.X-1, pos.Y))
        AdjustSpace(Location(pos.X+1, pos.Y))
        AdjustSpace(Location(pos.X, pos.Y-1))
        AdjustSpace(Location(pos.X, pos.Y+1))

def FixRubble(pos):
    t = cmap.TerrainAt(0, pos)
    if t == TerrainRecord.List["Rubble_85"] and cmap.TerrainAt(0, Location(pos.X+1, pos.Y)) != TerrainRecord.List["Rubble_86"]:
        cmap.AlterTerrain(pos, "CaveFloor_0")
        return True
    if t == TerrainRecord.List["Rubble_86"] and cmap.TerrainAt(0, Location(pos.X-1, pos.Y)) != TerrainRecord.List["Rubble_85"]:
        cmap.AlterTerrain(pos, "CaveFloor_0")
        return True
    if t == TerrainRecord.List["Rubble_88"] and cmap.TerrainAt(0, Location(pos.X+1, pos.Y)) != TerrainRecord.List["Rubble_89"]:
        cmap.AlterTerrain(pos, "Grass_2")
        return True
    if t == TerrainRecord.List["Rubble_89"] and cmap.TerrainAt(0, Location(pos.X-1, pos.Y)) != TerrainRecord.List["Rubble_88"]:
        cmap.AlterTerrain(pos, "Grass_2")
        return True
    return False

def FixCave(pos):
    store_ter = cmap.TerrainAt(0, pos)
    if store_ter is None: return False
    if IsCorrectableWall(pos):
        if not IsWall(Location(pos.X-1, pos.Y)):
            if not IsWall(Location(pos.X, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["CaveWall_14"]
            elif not IsWall(Location(pos.X, pos.Y + 1)):
                ter_to_fix = TerrainRecord.List["CaveWall_17"]
            else:
                ter_to_fix = TerrainRecord.List["CaveWall_15"]
        else:
            if not IsWall(Location(pos.X+1, pos.Y)):
                if not IsWall(Location(pos.X, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_11"]
                elif not IsWall(Location(pos.X, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_8"]
                else:
                    ter_to_fix = TerrainRecord.List["CaveWall_9"]
            else:
                if not IsWall(Location(pos.X, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_12"]
                elif not IsWall(Location(pos.X, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_6"]
                elif not IsWall(Location(pos.X-1, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_19"]
                elif not IsWall(Location(pos.X-1, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_18"]
                elif not IsWall(Location(pos.X+1, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_20"]
                elif not IsWall(Location(pos.X+1, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["CaveWall_21"]
                else:
                    ter_to_fix = TerrainRecord.List["CaveWall_5"]
        cmap.AlterTerrain(pos, ter_to_fix)
    return not(store_ter == cmap.TerrainAt(0, pos))

def FixMountain(pos):
    store_ter = cmap.TerrainAt(0, pos)
    if store_ter is None: return False
    if store_ter.Num >= 22 and store_ter.Num <= 35 and store_ter.Num != 23:
        if not IsMountain(Location(pos.X-1, pos.Y)):
            if not IsMountain(Location(pos.X, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Mountains_29"]
            elif not IsMountain(Location(pos.X, pos.Y+1)):
                ter_to_fix = TerrainRecord.List["Mountains_31"]
            else:
                ter_to_fix = TerrainRecord.List["Mountains_30"]
        elif not IsMountain(Location(pos.X+1, pos.Y)):
            if not IsMountain(Location(pos.X, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Mountains_27"]
            elif not IsMountain(Location(pos.X, pos.Y+1)):
                ter_to_fix = TerrainRecord.List["Mountains_25"]
            else:
                ter_to_fix = TerrainRecord.List["Mountains_26"]
        else:
            if not IsMountain(Location(pos.X, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Mountains_28"]
            elif not IsMountain(Location(pos.X, pos.Y+1)):
                ter_to_fix = TerrainRecord.List["Mountains_24"]
            elif not IsMountain(Location(pos.X-1, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Mountains_33"]
            elif not IsMountain(Location(pos.X-1, pos.Y+1)):
                ter_to_fix = TerrainRecord.List["Mountains_32"]
            elif not IsMountain(Location(pos.X+1, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Mountains_34"]
            elif not IsMountain(Location(pos.X+1, pos.Y+1)):
                ter_to_fix = TerrainRecord.List["Mountains_35"]
            else:
                ter_to_fix = TerrainRecord.List["Mountains_22"]
        cmap.AlterTerrain(pos, ter_to_fix)
    return not (store_ter == cmap.TerrainAt(0, pos))

def FixHill(pos):
    store_ter = cmap.TerrainAt(0, pos)
    if store_ter is None: return False
    if store_ter.Num >= 36 and store_ter.Num <= 49:
        if not IsHillOrMountain(Location(pos.X-1, pos.Y)):
            if not IsHillOrMountain(Location(pos.X, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Hills_43"]
            elif not IsHillOrMountain(Location(pos.X, pos.Y+1)):
                ter_to_fix = TerrainRecord.List["Hills_45"]
            else:
                ter_to_fix = TerrainRecord.List["Hills_44"]
        else:
            if not IsHillOrMountain(Location(pos.X+1, pos.Y)):
                if not IsHillOrMountain(Location(pos.X, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Hills_41"]
                elif not IsHillOrMountain(Location(pos.X, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Hills_39"]
                else:
                    ter_to_fix = TerrainRecord.List["Hills_40"]
            else:
                if not IsHillOrMountain(Location(pos.X, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Hills_42"]
                elif not IsHillOrMountain(Location(pos.X, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Hills_38"]
                elif not IsHillOrMountain(Location(pos.X-1, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Hills_47"]
                elif not IsHillOrMountain(Location(pos.X-1, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Hills_46"]
                elif not IsHillOrMountain(Location(pos.X+1, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Hills_48"]
                elif not IsHillOrMountain(Location(pos.X+1, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Hills_49"]
                else:
                    ter_to_fix = TerrainRecord.List["Hills_36"]

        if store_ter.ID != "Hills_37" or ter_to_fix.ID != "Hills_36":
           cmap.AlterTerrain(pos, ter_to_fix)

    return not (store_ter == cmap.TerrainAt(0, pos))

def FixWater(pos):
    store_ter = cmap.TerrainAt(0, pos)
    if store_ter is None: return False

    if IsCorrectableWater(pos):
        if not IsWater(Location(pos.X-1, pos.Y)):
            if not IsWater(Location(pos.X, pos.Y-1)):
                ter_to_fix = TerrainRecord.List["Water_56"]
            elif not IsWater(Location(pos.X, pos.Y+1)):
                 ter_to_fix = TerrainRecord.List["Water_58"]
            else:
                 ter_to_fix = TerrainRecord.List["Water_57"]
        else:
            if not IsWater(Location(pos.X+1, pos.Y)):
                if not IsWater(Location(pos.X, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Water_54"]
                elif not IsWater(Location(pos.X, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Water_52"]
                else:
                    ter_to_fix = TerrainRecord.List["Water_53"]
            else:
                if not IsWater(Location(pos.X, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Water_55"]
                elif not IsWater(Location(pos.X, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Water_51"]
                elif not IsWater(Location(pos.X-1, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Water_60"]
                elif not IsWater(Location(pos.X-1, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Water_59"]
                elif not IsWater(Location(pos.X+1, pos.Y-1)):
                    ter_to_fix = TerrainRecord.List["Water_61"]
                elif not IsWater(Location(pos.X+1, pos.Y+1)):
                    ter_to_fix = TerrainRecord.List["Water_62"]
                else:
                    ter_to_fix = TerrainRecord.List["Water_50"]
        cmap.AlterTerrain(pos, ter_to_fix)
    return not (store_ter == cmap.TerrainAt(0, pos))

def IsWall(pos):
    t = cmap.TerrainAt(0, pos)
    if t is None: return True
    if t.Num < 22 and t.Num > 4: return True
    if t.Picture >= 5 and t.Picture <= 17: return True
    if t.Picture >= 88 and t.Picture <= 120: return True
    if t.Picture >= 240 and t.Picture <= 243: return True
    if t.Picture == 65536 + 5: return True
    return False

def IsCorrectableWall(pos):
    walls = [5,6,8,9,11,12,14,15,17,18,19,20,21]
    t = cmap.TerrainAt(0, pos)
    if t is None: return False
    for k in range(len(walls)):
        if t.Num == walls[k]:
            return True
    return False

def IsMountain(pos):
    t = cmap.TerrainAt(0, pos)
    if t is None: return True
    if t.Num >= 22 and t.Num <= 35: return True
    if t.Picture >= 18 and t.Picture <= 31: return True
    if t.Picture >= 192 and t.Picture <= 195: return True
    return False

def IsHillOrMountain(pos):
    t = cmap.TerrainAt(0, pos)
    if t is None: return True

    # Hill
    if t.Num >= 36 and t.Num <= 49: return True
    if t.Picture >= 32 and t.Picture <= 45: return True
    if t.Picture == 204 or t.Picture == 212: return True

    #Mountain
    if t.Num >= 22 and t.Num <= 35: return True
    if t.Picture >= 18 and t.Picture <= 31: return True
    if t.Picture >= 192 and t.Picture <= 195: return True

    return False
    
def IsCorrectableWater(pos):
    t = cmap.TerrainAt(0, pos)
    if t is None: return False
    return t.Num >= 50 and t.Num <= 62

def IsWater(pos):
    t = cmap.TerrainAt(0, pos)
    if t is None: return True
    return t.Picture >= 46 and t.Picture <= 66

def AdjustOverlays(currentmap, pos):
    global cmap
    cmap = currentmap

    AdjustOverlay(pos)
    AdjustOverlay(Location(pos.X-1, pos.Y))
    AdjustOverlay(Location(pos.X+1, pos.Y))
    AdjustOverlay(Location(pos.X, pos.Y-1))
    AdjustOverlay(Location(pos.X, pos.Y+1))

def AdjustOverlay(pos):
    FixWalkway(pos)
    FixRoad(pos)

def FixWalkway(pos):
    t = cmap.TerrainAt(1, pos)
    if t is None: return
    if not IsWalkway(pos): return
    w = 21
    above = IsWalkwayOrWall(Location(pos.X, pos.Y - 1))
    below = IsWalkwayOrWall(Location(pos.X, pos.Y + 1))
    left = IsWalkwayOrWall(Location(pos.X - 1, pos.Y))
    right = IsWalkwayOrWall(Location(pos.X + 1, pos.Y))

    if above and left and not right and not below: w = 20
    elif above and right and not left and not below: w = 17
    elif below and left and not right and not above: w = 19
    elif below and right and not left and not above: w = 18

    cmap.AlterTerrain(pos, TerrainRecord.OverlayList[w])


def FixRoad(pos):
    t = cmap.TerrainAt(1, pos)
    if t is None: return
    if not IsRoad(pos): return

    r = 0
    if IsRoad(Location(pos.X, pos.Y - 1)):
       r += 1
    if IsRoad(Location(pos.X + 1, pos.Y)):
       r += 2
    if IsRoad(Location(pos.X, pos.Y + 1)):
       r += 4
    if IsRoad(Location(pos.X - 1, pos.Y)):
       r += 8
    if r == 0: r = 1
    cmap.AlterTerrain(pos, TerrainRecord.OverlayList[r])
    
def IsRoad(pos):
    t = cmap.TerrainAt(1, pos)
    if t is None: return True
    if t.Num >= 1 and t.Num <= 15: return True
    return False

def IsWalkway(pos):
    t = cmap.TerrainAt(1, pos)
    if t is None: return True
    if t.Num >= 17 and t.Num <= 21: return True
    return False
    
def IsWalkwayOrWall(pos):
    t = cmap.TerrainAt(1, pos)
    if t is None: return True
    if t.Num >= 17 and t.Num <= 21: return True

    t = cmap.TerrainAt(0, pos)
    if t.Picture >= 88 and t.Picture <= 120: return True
    return False
