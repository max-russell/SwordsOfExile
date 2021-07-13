
def FortReflection_291_MapTrigger_46_31(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["2_1"] == 0:
        StuffDone["2_1"] = 1
        Timer(Town, 5, False, "FortReflection_318_TownTimer_5", eTimerType.DELETE)
        return

def FortReflection_295_MapTrigger_44_31(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["2_1"] = 0

def FortReflection_299_MapTrigger_28_24(p):
    if StuffDone["4_5"] == 250:
        return
    StuffDone["4_5"] = 250
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(28,24))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(29,24))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(30,24))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(30,25))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(30,26))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(29,26))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(28,26))
    TownMap.List["FortReflection_16"].DeactivateTrigger(Location(28,25))
    ChoiceBox("You return to find the lab in shambles! Bloodstains, ash, and pieces of Golems are strewn about on the floor. You wonder what happened and if everybody is all right. Your questions are soon answered when Sidor enters.\n\n\"You have returned! As you can see, we were attacked in the time you were gone. About sixty Troglodytes blasted their way through the northern wall. We were able to dispatch all of them, but not before suffering casualties.\n\nWe lost several soldiers in the attack. Worse, two of our Golems were destroyed! Unfortunately, this will hold off our assault for a few days. Probably the most damaging, however, was the destruction of our portal.\n\nFortunately, we will recover from this blow. Oh, and how was your mission?\"", eDialogPic.CREATURE, 28, ["OK"])
    Town.PlaceEncounterGroup(1)
    if StuffDone["2_6"] == 0:
        MessageBox("You convey that you failed to destroy the Golem. Sidor does not look happy. \"Well, at least you escaped. I\'m going to bet this failure will come back to haunt us in the future.\"\n\n\"Dervish Montcalm sent me to tell you to see him in his office. He has a new mission set up for you.\"")
        return
    MessageBox("You tell him that you have successfully obliterated the Golem beyond use. Sidor smiles, \"Well at least something good came out of the past two hours! I have a feeling that your success has aided us greatly.\"\n\n\"Dervish Montcalm sent me to tell you to see him in his office. He has a new mission set up for you.\"")

def FortReflection_307_MapTrigger_31_57(p):
    Town.PlaceEncounterGroup(1)

def FortReflection_310_MapTrigger_32_36(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["2_9"] == 250:
        return
    StuffDone["2_9"] = 250
    if StuffDone["2_6"] == 1:
        MessageBox("\"Welcome back! Congratulations on the destruction of our Golem. Now Halloth will not have that foreknowledge to aid him. Your reward is on the table over there.\n\nAs Sidor has told you, we have suffered a recent attack with heavy damage. As we repair the damage, I would like you to go on another mission.\"")
        Town.PlaceItem(Item.List["GoldRingofProt_294"].Copy(), Location(30,33))
        return
    MessageBox("\"There is no need to explain. Unfortunately, we are unable to send in anyone else because of the destruction of our portal. It is just a setback that we will have to compromise.\n\nAs Sidor has told you, we have suffered a recent attack with heavy damage. As we repair the damage, I would like you to go on another mission.\"")

def FortReflection_311_MapTrigger_31_52(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,53)).Num == 147:
        MessageBox("The guard recognizes you and quickly opens the gate.")
        SuspendMapUpdate()
        for x in range(31, 34):
            for y in range(53, 54):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetUnlocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def FortReflection_317_MapTrigger_48_42(p):
    result = ChoiceBox("These beds are currently unused. You are sure that the Dervish will not mind if you borrow them for a night\'s sleep.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        Animation_Hold(-1, 020_yawn)
        Wait()
        Party.Age += 1000
        Party.HealAll(100)
        MessageBox("Your slumber was very refreshing. When you awaken, you feel very much restored.")
        for pc in Party.EachAlivePC():
            pc.SP+= 60
        return

def FortReflection_318_TownTimer_5(p):
    if StuffDone["2_1"] == 1:
        Animation_Hold(-1, 074_fireball)
        Wait()
        Animation_Explosion(Location(51,25), 0, "005_explosion")
        Animation_Hold()
        Wait()
        for ch in Town.EachCharacterInRange(Location(51,25), 1):
            ch.Damage(None, 15, 0, eDamageType.FIRE)
        Timer(Town, 5, False, "FortReflection_318_TownTimer_5", eTimerType.DELETE)
        return

def FortReflection_319_TalkingTrigger1(p):
    StuffDone["2_0"] = 4
    ChoiceBox("\"The reason the Troglodytes are such a threat is their knowledge of teleportation. Specifically, the Troglodytes have a short range portal which can send out large numbers of troops quite efficiently.\n\nNow we hadn\'t worried about this, but we are now within the range of that portal. The Troglos won\'t be able to penetrate our anti-teleportation field anytime soon, but they can just teleport large platoons at the edge of the field and attack by foot!\n\nThis is what happened while you were gone. We were taken off guard because we didn\'t think they had such capabilities. However, it is empirically shown that they now do. More attacks could seriously delay our assault further.\n\nFortunately, the portal is short range and is built on the edge of their territory. So getting there shouldn\'t be a problem! To reach it, you will need to travel south and enter the mountains. At the plateau, head down the western tunnel.\n\nYou shouldn\'t have any trouble locating it. On behalf of the Emperor, I am going to ask you to infiltrate the Portal Fortress and destroy the portal. If you can disable it, the Troglos will have a much harder time reaching here.\"\n\nWith that, Dervish Montcalm continues with his plans for the assault.", eDialogPic.STANDARD, 22, ["OK"])
    TownMap.List["PortalFortress_13"].Hidden = False
