
def FortKhazar_135_MapTrigger_30_33(p):
    if StuffDone["2_4"] == 250:
        return
    StuffDone["2_4"] = 250
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(30,33))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(30,32))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(31,32))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(32,32))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(32,33))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(32,34))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(31,34))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(30,34))
    ChoiceBox("It doesn\'t take long to recover from the effects of portal use. You look around and survey your surroundings.\n\nIt\'s obvious that you are within a cavern; Troglodytes are known to be a race that prefers caves. Right now, you are in the courtyard of Fort Khazar. The courtyard is pretty much empty, so you haven\'t been seen yet.\n\nTo your south is the entrance that presumably leads into Troglo territory, or sure death for you. You doubt that you will be going that way. The rest of the fort is composed of two other structures. One to your north and the other east.\n\nIt won\'t be long before you\'re spotted; you had better find the Golem and get out quickly. Considering its location, you can bet that the fortress will be overrun with units if you do not hurry.\n\n(This dungeon has a time limit, I suggest backing up a save file here!)", eDialogPic.CREATURE, 115, ["OK"])
    Timer(Town, 400, False, "FortKhazar_159_TownTimer_1", eTimerType.DELETE)

def FortKhazar_143_MapTrigger_10_15(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["2_7"] == 250:
        return
    StuffDone["2_7"] = 250
    MessageBox("You discover a concealed laboratory. Inside is one of the Golems at Fort Reflection. A Khazi is busy at work studying the components of the Golem. You can bet this is what you are here to destroy.")
    Town.PlaceEncounterGroup(1)

def FortKhazar_144_MapTrigger_15_12(p):
    MessageBox("This is a journal being kept on the Golem. Apparently, they had not learned much yet. You doubt this brief, general description will be of any use.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(25)

def FortKhazar_145_MapTrigger_54_7(p):
    if StuffDone["2_8"] == 250:
        return
    StuffDone["2_8"] = 250
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(54,7))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(54,8))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(54,9))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(54,10))
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(54,11))
    Town.AlterTerrain(Location(52,9), 0, TerrainRecord.UnderlayList[173])
    MessageBox("Uh oh! The portal has deteriorated for some reason. You will have to reactivate it or find another way out. Whatever you do, you don\'t have much time.")
    Animation_Explosion(Location(52,9), 2, "005_explosion")
    Animation_Hold()
    Wait()

def FortKhazar_150_MapTrigger_44_15(p):
    ChoiceBox("This tome describes the Troglodyte\'s portal. There is a short section on activation instructions.\n\n\"Activation of the portal requires two focusing devices. The best devices are gemstones, specifically rubies which are fairly common in this area. To activate the portal, place the devices on the north and south pedestal.\n\nThen set your coordinates on the central pedestal. Finally, press the red button on the central pedestal to charge the portal.\"", eDialogPic.STANDARD, 22, ["OK"])

def FortKhazar_151_MapTrigger_35_54(p):
    if StuffDone["2_5"] == 0:
        result = ChoiceBox("These controls operate the gates to Fort Khazar. You could destroy them, disabling their use for a while.", eDialogPic.STANDARD, 9, ["Leave", "Destroy", "Pull"])
        if result == 1:
            if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,55)).Num == 130:
                MessageBox("You smash the controls. The gates will remain closed until the controls are repaired. Perhaps this may buy you a little extra time to escape.")
                StuffDone["2_5"] = 1
                return
            MessageBox("You smash the controls. The gates will remain open until the controls are repaired.")
            StuffDone["2_5"] = 2
            return
        elif result == 2:
            MessageBox("The controls are in fine working order! They easily close or open the gates.")
            SuspendMapUpdate()
            for x in range(31, 34):
                for y in range(55, 56):
                    t = Town.TerrainAt(Location(x,y)).TransformTo
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        return
    MessageBox("The controls are smashed. You cannot open nor close the gates.")

def FortKhazar_152_MapTrigger_49_9(p):
    result = ChoiceBox("These appear to be the controls for the portal. Perhaps you can reactivate the portal and get out of here.", eDialogPic.STANDARD, 11, ["Leave", "Push"])
    if result == 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(52,9)).Num == 173:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(49,7), True):
                    if i.SpecialClass == 3:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(49,11), True):
                        if i.SpecialClass == 3:
                            itemthere = True
                            break
                if itemthere == True:
                    Town.AlterTerrain(Location(52,9), 0, TerrainRecord.UnderlayList[78])
                    MessageBox("It worked! The portal has reactivated. Time to get out of this place.")
                    Animation_Explosion(Location(52,9), 2, "005_explosion")
                    Animation_Hold()
                    Wait()
                    return
                MessageBox("Nothing happens!")
                return
            MessageBox("Nothing happens!")
            return
        MessageBox("Nothing happens!")
        return

def FortKhazar_153_MapTrigger_52_9(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(52,9)).Num == 78:
        result = ChoiceBox("This portal will hopefully take you back to Fort Reflection, assuming you\'ve done everything correctly. Do you enter?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            Animation_Hold(-1, 010_teleport)
            Wait()
            MessageBox("The Troglodyte\'s portal is no better than the one at Fort Reflection. This time, you feel yourselves pass through a kind of wall on your trip. It must have been the anti-teleportation field Sidor told you about.\n\nYou end up in the lab, but something is wrong!")
            StuffDone["2_0"] = 3
            StuffDone["2_2"] = 1
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(29,25)
            Party.MoveToMap(TownMap.List["FortReflection_16"])
            return
        p.CancelAction = True
        return

def FortKhazar_154_MapTrigger_31_59(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This way is no exit for you. Leaving here would lead you into an army of Troglos, meaning a quick and painful death.")

def FortKhazar_157_MapTrigger_29_16(p):
    result = ChoiceBox("This is a Troglodyte spellbook. Care to take a look through it?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 8:
            MessageBox("You flip through the spellbook. Although the Troglodytes speak the same general language as you, there are many differences that show throughout the book making much not understandable.\n\nHowever, there are a few rituals not obscured by the foreign dialect. You now know how to cast \'Venom Arrows\'!")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_venom_arrows")
            return
        MessageBox("You flip through the spellbook. Although the Troglodytes speak the same general language as you, there are many differences that show throughout the book making much not understandable.\n\nUnfortunately, you do not have enough knowledge about magic to know how to go about learning most of these spells.")
        return

def FortKhazar_158_MapTrigger_8_28(p):
    if StuffDone["3_0"] == 250:
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
    StuffDone["3_0"] = 250
    TownMap.List["FortKhazar_12"].DeactivateTrigger(Location(8,28))
    pc.RunTrap(eTrapType.EXPLOSION, 0, 40)

def FortKhazar_159_TownTimer_1(p):
    MessageBox("No reinforcements have yet come. You can bet the Troglos have called for assistance and it will probably arrive soon. Once it arrives, you will be overwhelmed. You had better find an escape soon.")
    Timer(Town, 200, False, "FortKhazar_160_TownTimer_2", eTimerType.DELETE)

def FortKhazar_160_TownTimer_2(p):
    if StuffDone["2_5"] == 1:
        MessageBox("You can hear shouts from the southern sections of the fortress. Fortunately, you have disabled the gate, buying more time. However, you don\'t have much more time to spare!")
        Timer(Town, 100, False, "FortKhazar_161_TownTimer_4", eTimerType.DELETE)
        return
    MessageBox("Time has run out for you. The reinforcements Sidor told you about have arrived! You put up a valiant fight, but you are overcome by sheer numbers. It looks like this wasn\'t your day.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def FortKhazar_161_TownTimer_4(p):
    MessageBox("Well, it appears your extra time wasn\'t enough. The Troglodytes break through the gates and you are overcome by their great numbers.")
    for pc in Party.EachAlivePC():
        if pc.LifeStatus == eLifeStatus.ALIVE:
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()

def FortKhazar_162_CreatureDeath0(p):
    MessageBox("You have destroyed the Golem! You make sure you do a thorough job of it as well. By the time you are finished, you are certain the Khazis won\'t learn anything more from it. Now, it\'s time to escape!")
