
def DisposalSite_2275_MapTrigger_20_37(p):
    if StuffDone["67_8"] == 250:
        return
    StuffDone["67_8"] = 250
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(20,37))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(21,37))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(22,37))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(23,37))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(25,37))
    ChoiceBox("The amount of concentrated goo here is truly astounding. You have heard that many forms of industrial sludge produced from magical reactions actually grows and reproduces if left uncontained.\n\nYou are guessing this is that variety. The sludge is so strong that it literally ate through this reinforced wall and the gates. With this last line of defense, the living varieties of the sludge are free to roam.\n\nJust remember this is not the normal kind of sludge, but the highly noxious kind which requires special treatment.", eDialogPic.TERRAIN, 76, ["OK"])

def DisposalSite_2280_MapTrigger_34_40(p):
    if StuffDone["67_9"] == 250:
        return
    StuffDone["67_9"] = 250
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(34,40))
    MessageBox("This corpse is little more than a skeleton. His or her skin was eaten away by the acidic sludge that he or she drowned in. This is definitely not the way you would want to go.")

def DisposalSite_2281_MapTrigger_40_11(p):
    MessageBox("This door leads to the quickfire room, your goal, but it has a large padlock upon it. Apparently the workers here were not able to secure the key to unlock it in time.")

def DisposalSite_2282_MapTrigger_36_7(p):
    if StuffDone["70_0"] == 250:
        return
    StuffDone["70_0"] = 250
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(36,7))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(36,8))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(36,9))
    MessageBox("It appears you will not have to struggle too much to get into the quickfire chamber. Although the door is still intact, the side walls have given way to the intense goo in this room. You just hope the controls are still functional.")

def DisposalSite_2285_MapTrigger_30_21(p):
    if StuffDone["70_1"] == 250:
        return
    StuffDone["70_1"] = 250
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(30,21))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(30,22))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(28,13))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(27,13))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(23,13))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(22,13))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(21,13))
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(20,13))
    ChoiceBox("From this point, you can figure out what happened. It appears the north incinerator that is used to destroy the waste ruptured. The violent explosion shattered the north wall and presumably some of the containers.\n\nOnce the dangerous goo was released, it must have spread very quickly. It seems that the workers here were inadequately trained to handle such a disaster.", eDialogPic.STANDARD, 25, ["OK"])

def DisposalSite_2293_MapTrigger_6_24(p):
    if StuffDone["70_2"] == 250:
        return
    StuffDone["70_2"] = 250
    TownMap.List["DisposalSite_97"].DeactivateTrigger(Location(6,24))
    MessageBox("The control room seems to be the only chamber that has escaped the influence of the disaster. The powerful runes have managed to repel all of the waste.")

def DisposalSite_2294_MapTrigger_4_23(p):
    MessageBox("This control panel regulates the settings of the incinerators. Unless you want to gather up every piece of sludge in this place, you doubt this will have any use to you.")

def DisposalSite_2295_MapTrigger_42_38(p):
    MessageBox("You find a small memo that is still intact. \"In case of disaster follow protocols: (1) Simultaneously have one worker proceed to Quickfire release and second to deactivate safety in control room.\n\n(2) After all workers are accounted for, activate trigger and evacuate site. Note that saving the facility from disaster is the first priority! If workers cannot be found, assume perished!")

def DisposalSite_2296_MapTrigger_32_39(p):
    MessageBox("The contents of this dresser have been thoroughly eaten away by the caustic sludge.")

def DisposalSite_2298_MapTrigger_10_41(p):
    MessageBox("These controls have been corroded away by the chemicals. It seems this mechanism controlled the teleporter used to transport waste here. Needless to say, it is now inoperative.")

def DisposalSite_2299_MapTrigger_3_23(p):
    if StuffDone["70_3"] == 0:
        MessageBox("These controls are responsible for the safety settings here such as the gates and alarms. A key item of interest is the switch which disables (or enables) the safety for the quickfire release. It is currently turned on.")
        if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
            if StuffDone["70_3"] == 0: StuffDone["70_3"] = 1
            else: StuffDone["70_3"] = 0
            Animation_Hold(-1, 034_button1)
            Wait()
            return
        return
    MessageBox("These controls are responsible for the safety settings here such as the gates and alarms. A key item of interest is the switch which disables (or enables) the safety for the quickfire release. It is currently turned off.")
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["70_3"] == 0: StuffDone["70_3"] = 1
        else: StuffDone["70_3"] = 0
        Animation_Hold(-1, 034_button1)
        Wait()
        return

def DisposalSite_2300_MapTrigger_40_7(p):
    if StuffDone["67_4"] == 0:
        result = ChoiceBox("This control panel has a single lever with the following notice: DANGER! QUICKFIRE RELEASE -- USE ONLY IN EMERGENCY. This is what you came for. Do you pull the lever?", eDialogPic.STANDARD, 9, ["Leave", "Pull"])
        if result == 1:
            if StuffDone["70_3"] == 0:
                MessageBox("You pull the lever, but you find it locked into place. After shouting several expletives, you realize that some safety mechanism is holding it in place. You will need to turn it off before you can use it.")
                return
            StuffDone["67_4"] = 1
            Town.AlterTerrain(Location(40,5), 0, TerrainRecord.UnderlayList[90])
            Animation_Explosion(Location(40,5), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Town.AlterTerrain(Location(40,5), 0, TerrainRecord.UnderlayList[75])
            Town.AlterTerrain(Location(40,4), 0, TerrainRecord.UnderlayList[90])
            Animation_Explosion(Location(40,4), 0, "005_explosion")
            Animation_Hold()
            Wait()
            for x in range(40, 41):
                for y in range(3, 5):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[75])
            for x in range(40, 41):
                for y in range(3, 6):
                    Town.PlaceField(Location(x,y), Field.QUICKFIRE)
            Animation_Explosion(Location(40,3), 0, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("You pull the lever and hear the satisfying sounds of explosions as the wall between the two substances collapses. As the chemicals come into contact with one another, there occurs a violent reaction.\n\nThe result is the formation of quickfire, one of the most devastating weapons known! As pretty as the reaction is, you really should get out of here now!", eDialogPic.STANDARD, 25, ["OK"])
            return
        return

def DisposalSite_2301_TownTimer_0(p):
    if StuffDone["67_4"] == 0:
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 1))
        return

def DisposalSite_2302_OnEntry(p):
    if StuffDone["67_4"] == 1:
        SuspendMapUpdate()
        for x in range(1, 48):
            for y in range(1, 48):
                if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[96]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
                elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[84]:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[96])
        ResumeMapUpdate()
        for x in range(37, 44):
            for y in range(3, 5):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[90])
        Town.NPCList.Clear()
        return
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 2))
    if StuffDone["67_7"] == 250:
        return
    StuffDone["67_7"] = 250
    ChoiceBox("You journey down a long winding tunnel filled with toxic sludge. The fumes given off are quite noxious starting to make you feel ill. It seems you have reached the main facility.\n\nUnfortunately, the sludge is also much more concentrated here and spending too much time here will be hazardous to your health. Just hope you can find the quickfire controls as soon as possible.", eDialogPic.TERRAIN, 76, ["OK"])
