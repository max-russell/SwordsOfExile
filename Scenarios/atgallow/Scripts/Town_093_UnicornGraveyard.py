
def UnicornGraveyard_2174_TownTimer_0(p):
    if Maths.Rand(1,0,100) < 30:
        Animation_Hold(-1, 084_neigh)
        Wait()
        RunScript("Generate_Wandering_93_UnicornGraveyard", ScriptParameters(eCallOrigin.CUSTOM))
        RunScript("Generate_Wandering_93_UnicornGraveyard", ScriptParameters(eCallOrigin.CUSTOM))
        return

def UnicornGraveyard_2175_TownTimer_1(p):
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(7,20), True):
            if i.SpecialClass == 34:
                itemthere = True
                break
    if itemthere == True:
        if StuffDone["70_4"] == 250:
            return
        StuffDone["70_4"] = 250
        Animation_Hold(-1, 005_explosion)
        Wait()
        Town.PlaceEncounterGroup(1)
        ChoiceBox("Several ghostly unicorns rise up to avenge you desecrating their holy shrine!", eDialogPic.CREATURE, 128, ["OK"])
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 8))
        return

def UnicornGraveyard_2176_TownTimer_2(p):
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 2))

def UnicornGraveyard_2177_TownTimer_3(p):
    if StuffDone["70_5"] == 0:
        if Maths.Rand(1,0,100) < 10:
            StuffDone["70_5"] = 1
            if Maths.Rand(1,0,100) < 50:
                if Maths.Rand(1,0,100) < 50:
                    Town.PlaceNewNPC(NPCRecord.List["Unicorn_183"], Location(28,11), False)
                    return
                Town.PlaceNewNPC(NPCRecord.List["Unicorn_183"], Location(37,16), False)
                return
            if Maths.Rand(1,0,100) < 50:
                Town.PlaceNewNPC(NPCRecord.List["Unicorn_183"], Location(14,31), False)
                return
            Town.PlaceNewNPC(NPCRecord.List["Unicorn_183"], Location(6,42), False)
            return
        return

def UnicornGraveyard_2178_TownTimer_4(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Unicorn_183": Town.NPCList.Remove(npc)

def UnicornGraveyard_2179_ExitTown(p):
    if p.Dir.IsNorth or p.Dir.IsWest or p.Dir.IsSouth or p.Dir.IsEast:
        StuffDone["70_5"] = 0
