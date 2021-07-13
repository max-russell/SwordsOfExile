
def EasternNelon_2461_MapTrigger_13_26(p):
    MessageBox("This place is a residential suburb of Evergold. A majority of the industrial workers live outside the city in these areas. The standard of living here is not excellent, but better than many other places in the Empire.")

def EasternNelon_2466_MapTrigger_14_27(p):
    MessageBox("This is one the suburbs of the industrial city of Evergold. Although the area is mostly residential, there are a few shops. The fletcher appears to have some interesting goods.")
    OpenShop("Shop_Items_Outside_3_5_1")
    p.CancelAction = True

def EasternNelon_2467_MapTrigger_13_27(p):
    MessageBox("This is a suburb of the industrial city of Evergold. Among the homes is a temple which offers cheap healing services.")
    OpenHealingShop(0)
    p.CancelAction = True

def EasternNelon_2468_MapTrigger_18_36(p):
    MessageBox("This is a residential suburb of the industrial city, Evergold. Among the homes are several shops. Most of them offer mundane goods, but there is one that sells some interesting crystals.")
    OpenShop("Shop_Items_Outside_7_5_1")
    p.CancelAction = True

def EasternNelon_2469_MapTrigger_16_40(p):
    if StuffDone["53_1"] == 250:
        return
    StuffDone["53_1"] = 250
    WorldMap.AlterTerrain(Location(256,88), 1, None)
    WorldMap.DeactivateTrigger(Location(256,88))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("You come across a patrol of Empire soldiers battling a collection of Golems. The soldiers appear to be outclassed by the living pieces of stone. As the battle rages on, you are sighted by a Dervish who motions you to join in.\n\nYou are pulled into the fray.", eDialogPic.CREATURE, 122, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_1_4", p.Target)

def EasternNelon_2470_MapTrigger_11_20(p):
    if StuffDone["53_2"] == 0:
        result = ChoiceBox("The shallow ocean allows you to merely walk to this small island. There is not much here, a sandy beach and a few trees. However, you notice a glint just off the northern beach.\n\nYou walk over to it and find an oddly curved sword washed up on the beach. It is quite unlike any conventional sword you have seen. You wonder who would make such a blade.\n\nIt is yours if you really want it.", eDialogPic.TERRAIN, 59, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("SteelWaveBlade_94")
            StuffDone["53_2"] = 1
            return
        return

def EasternNelon_2471_MapTrigger_36_36(p):
    ChoiceBox("Alas, even the people of Evergold must eat. Although they receive much of their food via teleporter from back in good old Agran, they do grow a handful of crops here to make up for any shortages.", eDialogPic.TERRAIN, 181, ["OK"])
    p.CancelAction = True

def EasternNelon_2472_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def EasternNelon_2473_SpecialOnWin0(p):
    ChoiceBox("With the Golems reduced to piles of rubble, the Dervish comes over to thank you personally. He informs you to be on the lookout for renegade Golems. For some reason, Golems have been going berserk at an unusual rate these days.\n\nThey suspect that there are renegades disrupting the Golem\'s circuits causing them to roam and attack travelers. The process is not overly difficult to do and can really cause a lot of damage.\n\nAfter the patrol is rested and bandaged, they head back to the city. Before they leave, the Dervish hands you a wand telling you that it will help repel any other golems you may meet.", eDialogPic.CREATURE, 17, ["OK"])
    Party.GiveNewItem("WandofDeath_288")

def EasternNelon_2474_SpecialOnFlee0(p):
    MessageBox("Like cowards you flee the battlefield, leaving the patrol to fend for themselves. After your retreat, the soldiers have little chance and flee as well. This will not bode well for your reputation.")
    for pc in Party.EachAlivePC():
        pc.AwardXP(-20)
