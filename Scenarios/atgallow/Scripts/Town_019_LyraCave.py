
def LyraCave_356_MapTrigger_55_12(p):
    if StuffDone["5_7"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["5_7"] = 250
    TownMap.List["LyraCave_19"].DeactivateTrigger(Location(55,12))
    pc.RunTrap(eTrapType.BLADE, 3, 60)

def LyraCave_357_MapTrigger_55_11(p):
    if StuffDone["5_8"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["5_8"] = 250
    TownMap.List["LyraCave_19"].DeactivateTrigger(Location(55,11))
    pc.RunTrap(eTrapType.GAS, 3, 60)

def LyraCave_358_MapTrigger_55_10(p):
    if StuffDone["5_9"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["5_9"] = 250
    TownMap.List["LyraCave_19"].DeactivateTrigger(Location(55,10))
    pc.RunTrap(eTrapType.EXPLOSION, 2, 60)

def LyraCave_359_MapTrigger_51_7(p):
    if StuffDone["6_1"] == 250:
        return
    StuffDone["6_1"] = 250
    TownMap.List["LyraCave_19"].DeactivateTrigger(Location(51,7))
    TownMap.List["LyraCave_19"].DeactivateTrigger(Location(51,8))
    TownMap.List["LyraCave_19"].DeactivateTrigger(Location(51,9))
    ChoiceBox("This room has a large dais in the center. Upon it, rests a ball of gas. You draw closer and the ball takes a humanoid shape. It floats away from you and several other spirits materialize within the room.\n\nThey all stare at you awaiting your next move. You draw one step closer and they begin to attack!", eDialogPic.CREATURE, 54, ["OK"])
    Town.PlaceEncounterGroup(1)

def LyraCave_362_MapTrigger_29_41(p):
    if Party.HasTrait(Trait.CaveLore):
        if StuffDone["6_2"] == 250:
            return
        StuffDone["6_2"] = 250
        MessageBox("Your knowledge of \'Cave Lore\' tells you that the passage ahead is quite unstable due to the moisture. Walking there could be dangerous.")
        return

def LyraCave_364_MapTrigger_30_38(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(30,37)).Num == 0:
        for x in range(29, 31):
            for y in range(37, 38):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[97])
        MessageBox("This passage was unstable to begin with. Your passing through has caused a rockslide! Not only do you receive a painful shower of stones, but the passage ahead is now blocked!")
        Party.Damage(Maths.Rand(4, 1, 5) + 10, eDamageType.WEAPON)
        Wait()
        return

def LyraCave_368_TownTimer_8(p):
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "GuardianSpirit_216": Town.NPCList.Remove(npc)
    Town.PlaceItem(Item.List["Lyra_183"].Copy(), Location(47,10))
    Animation_Explosion(Location(47,10), 2, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("Suddenly, the spirit erupts in a blinding flash of light! You open your eyes to see a radiant Greatsword floating gently onto the dais. You are guessing this must be the legendary sword Lyra!", eDialogPic.CREATURE, 1024, ["OK"])

def LyraCave_369_CreatureDeath0(p):
    Town.PlaceEncounterGroup(2)
    ChoiceBox("Suddenly, the spirit halts its attack. It waves its ghostly arms and all of the hostile spirits fade away. The spirit returns to the center dais and watches you closely. It makes no move to attack.", eDialogPic.CREATURE, 1024, ["OK"])
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if  npc.IsABaddie: Town.NPCList.Remove(npc)
    Timer(Town, 4, False, "LyraCave_368_TownTimer_8", eTimerType.DELETE)

def Talking_19_2(p):
    if Party.Gold >= 0:
        if TownMap.List["MandahlAscent_70"].Hidden == True:
            Party.Gold -= 0
            TownMap.List["MandahlAscent_70"].Hidden = False
        p.TalkingText = "\"Half the battle is finding a way to get up the Mountains. There is a nice ascenting point in the hills northeast of this city. You will need to search for small passages in the mountains to get there. I would be careful, those beasts are sure hefty.\""
    else:
        p.TalkingText = ""
