
def MountBleak_597_MapTrigger_49_45(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(7,12)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_598_MapTrigger_44_29(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    return

def MountBleak_599_MapTrigger_59_23(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(2,19)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_600_MapTrigger_38_22(p):
    if StuffDone["9_7"] == 250:
        return
    StuffDone["9_7"] = 250
    TownMap.List["MountBleak_31"].DeactivateTrigger(Location(38,22))
    TownMap.List["MountBleak_31"].DeactivateTrigger(Location(38,21))
    Animation_Hold(-1, 023_startoutdoorcombat)
    Wait()
    ChoiceBox("As you near the plateau, you hear a loud battle cry! Two armies converge on the plateau -- one of Troglodytes, the other of Hill Giants. They immediately engage in a bloody combat.\n\nYou have heard tales of the rivalry between these two races dating back to before the Empire\'s foundation. It looks like this rivalry continues today. One thing is certain: Neither race likes Empire soldiers.", eDialogPic.STANDARD, 1027, ["OK"])
    Town.PlaceEncounterGroup(1)

def MountBleak_602_MapTrigger_20_40(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["9_8"] = 1
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,5)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_603_MapTrigger_9_7(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(47,13)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_604_MapTrigger_6_14(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,35)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_605_MapTrigger_10_19(p):
    if StuffDone["10_0"] == 250:
        return
    StuffDone["10_0"] = 250
    TownMap.List["MountBleak_31"].DeactivateTrigger(Location(10,19))
    TownMap.List["MountBleak_31"].DeactivateTrigger(Location(10,20))
    Party.Damage(Maths.Rand(5, 1, 5) + 10, eDamageType.WEAPON)
    Wait()
    Town.PlaceEncounterGroup(2)
    Animation_Hold(-1, 023_startoutdoorcombat)
    Wait()
    ChoiceBox("Suddenly rocks start raining down upon you! You look up to see several Hill Giants hiding up in the rocks. You\'ve been ambushed! One of them speaks, \"Humans! You dare trespass upon the land of H\'Nloka! Prepare to die.\"\n\nThe giants jump down from their hiding places and ready their clubs. You are surrounded.", eDialogPic.CREATURE1x2, 0, ["OK"])

def MountBleak_607_MapTrigger_26_51(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(60,31)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_608_MapTrigger_18_27(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(18,59)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_609_MapTrigger_32_58(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(43,59)
    Party.MoveToMap(TownMap.List["MountBleak_36"])

def MountBleak_611_MapTrigger_5_49(p):
    if StuffDone["10_1"] == 1:
        if Party.CountItemClass(12, False) > 0:
            MessageBox("The insignia of Stolgrad is etched into the face of this rock. Remembering the clues you had learned earlier, you place the crystal you found off of the dead mage\'s body into a small alcove.\n\nThe entire surface begins to glow. An opening has now appeared!")
            Town.AlterTerrain(Location(5,50), 0, TerrainRecord.UnderlayList[237])
            return
        MessageBox("The insignia of the Stolgrad Sector is carved into the stone. You wonder what it means.")
        return
    MessageBox("The insignia of the Stolgrad Sector is carved into the stone. You wonder what it means.")

def MountBleak_612_MapTrigger_5_50(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(5,50)).Num == 237:
        Animation_Hold(-1, 095_enterdungeon)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(51,41)
        Party.MoveToMap(TownMap.List["MountBleak_36"])
        return

def MountBleak_613_MapTrigger_38_47(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a soft click.")
        t = Town.TerrainAt(Location(39,49))
        if t == TerrainRecord.UnderlayList[145]: Town.AlterTerrain(Location(39,49), 0, TerrainRecord.UnderlayList[142])
        elif t == TerrainRecord.UnderlayList[142]: Town.AlterTerrain(Location(39,49), 0, TerrainRecord.UnderlayList[145])
        return

def MountBleak_614_MapTrigger_39_49(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(39,49)).Num == 142:
        if StuffDone["9_0"] < 4:
            StuffDone["9_0"] = 4
            ChoiceBox("You enter the cell and see a wizard quietly reading a book. He sets it down and looks up at you. \"I have not seen you here before. I wonder if it had something to do with all that ruckus outside. Who are you?\" You identify yourself.\n\nThe wizard nods. \"Indeed, I am who you seek.\" He gathers up his things, taking a few books off the shelf. \"A little entertainment.\" He chuckles. \"I have to admit, it will be a pity to leave. The guards here treated me well.\"\n\nHe takes one last look around and turns to you. \"Shall we?\"", eDialogPic.CREATURE, 27, ["OK"])
            SpecialItem.Give("RaidenNPC")
            Message("Raiden joins the party!")
            return
        return

def MountBleak_615_MapTrigger_41_53(p):
    result = ChoiceBox("A glowing portal is here. It is probably used for fast transportation from the top to the bottom of the mountain.", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(4,4)
        Party.MoveToMap(TownMap.List["MountBleak_36"])
        return

def MountBleak_616_MapTrigger_37_51(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 12:
        MessageBox("It must be pretty boring for these soldiers to be stuck up here on this mountain, away from civilization. To entertain themselves, they brought along a sizable collection of books.\n\nOne book of interest is titled \'1,001 Useless Spells & Rituals\'. However, the writing describes this entertaining spell called \'Spray Fields\' and thoroughly rips on the person who came up with that idea for a spell.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_spray_fields")
        return
    MessageBox("It must be pretty boring for these soldiers to be stuck up here on this mountain, away from civilization. To entertain themselves, they brought along a sizable collection of books.\n\nOne book is entitled \'1,001 Useless Spells & Rituals\'. The book is very entertaining, but you will need more Mage Lore to determine if the spells are really \'useless\'.")

def MountBleak_617_MapTrigger_35_51(p):
    MessageBox("It must be pretty boring for these soldiers to be stuck up here on this mountain, away from civilization. To entertain themselves, they brought along a sizable collection of books.")

def MountBleak_620_MapTrigger_52_8(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    Animation_Hold(-1, 095_enterdungeon)
    Wait()
    if StuffDone["9_9"] == 0:
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(59,58)
        Party.MoveToMap(TownMap.List["TroglodyteLair_69"])
        return
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(59,26)
    Party.MoveToMap(TownMap.List["TroglodyteLair_69"])

def MountBleak_621_MapTrigger_52_9(p):
    if StuffDone["48_6"] >= 1:
        Town.AlterTerrain(Location(52,8), 0, TerrainRecord.UnderlayList[240])
        return
