
def CentralNelon_2448_MapTrigger_11_29(p):
    WorldMap.AlterTerrain(Location(203,77), 0, TerrainRecord.UnderlayList[87])
    if StuffDone["52_7"] == 250:
        return
    StuffDone["52_7"] = 250
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("In the center of this patch of rubble is a small tower. You decide to approach and explore. However, no sooner to you get near the structure, it vanishes! The entire tower was some kind of illusion.\n\nSuddenly, you hear psychic growls. You look around to see yourself surrounded by several hungry eye creatures. You have heard that these menacing foes often use deceptive tactics like these to lure travelers to their deaths.\n\nUnfortunately, you have just fallen into such a fate.", eDialogPic.CREATURE, 85, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_1_4", p.Target)

def CentralNelon_2449_MapTrigger_36_12(p):
    if StuffDone["52_8"] >= 2:
        MessageBox("This tower has been completely trashed. There is nothing of value left.")
        return
    if StuffDone["52_8"] < 1:
        StuffDone["52_8"] = 1
        Animation_Hold(-1, 005_explosion)
        Wait()
        result = ChoiceBox("As you near this tower, you hear a loud explosion from within. You hurry to check out what is going on inside. This tower apparently does research on Golems. However, one of the experiments seems to have gotten out of hand.\n\nThe Golems here have gone berserk and are trashing the labs. A lone wizard tries to destroy the Golems. There are sure a lot of them and you doubt that he will be able to handle it alone. Even with your help, it will prove difficult. Give him a hand?", eDialogPic.CREATURE, 121, ["No", "Yes"])
        if result == 0:
            MessageBox("You decide that it would be better not to get involved with this conflict. Besides the mages should have been more careful.")
            StuffDone["52_8"] = 2
            p.CancelAction = True
            return
        elif result == 1:
            Animation_Hold(-1, 018_drawingsword)
            Wait()
            WorldMap.SpawnNPCGroup("Group_4_1_5", p.Target)
            return
        return
    MessageBox("You return to the tower to still find it mostly in shambles. The repair effort, however, is underway and proceeding slowly. Several mages and other people are working hard to restore the tower after the little accident.")

def CentralNelon_2450_MapTrigger_22_10(p):
    if StuffDone["52_9"] == 250:
        return
    StuffDone["52_9"] = 250
    WorldMap.DeactivateTrigger(Location(214,58))
    Animation_Hold(-1, 043_stoning)
    Wait()
    ChoiceBox("The Nelon Mountains are not exactly friendly territory. It is vastly wild and only traveled by brave souls. It is not uncommon for some threats to seek refuge in these unpatrolled areas of the empire.\n\nThis rocky island has become home to a small pack of dangerous Basilisks. You have just had an unfortunate run in with the deadly lizards.", eDialogPic.CREATURE, 86, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_1_7", p.Target)

def CentralNelon_2451_MapTrigger_26_16(p):
    if StuffDone["53_0"] == 250:
        return
    StuffDone["53_0"] = 250
    WorldMap.DeactivateTrigger(Location(218,64))
    WorldMap.DeactivateTrigger(Location(218,63))
    WorldMap.DeactivateTrigger(Location(220,60))
    WorldMap.DeactivateTrigger(Location(221,60))
    ChoiceBox("This river will lead you into the Nelon Mountains. These mountains are one of the most dangerous places on the continent. The terrain is rough, desolate, and full of winding rivers with many forks and dead ends.\n\nMany adventurers have gone down these rivers and disappeared without a trace. Needless to say, the rough terrain makes this area uninhabited and hence unpatrolled, making it home to all sorts of dangerous creatures.\n\nOnly those who are seeking danger should continue upstream into the mountains.", eDialogPic.TERRAIN, 19, ["OK"])

def CentralNelon_2455_MapTrigger_9_18(p):
    result = ChoiceBox("At the edge of these mountains is a small hut. The isolated home is occupied by a starkly beautiful young druid. She says she has come out here to experience the solitude of wilderness and practice her skills.\n\nShe offers to sell you some of her potions to assist with the journey into the mountains if you plan to go there.", eDialogPic.CREATURE, 30, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_23_4_1")
        p.CancelAction = True
        return
    p.CancelAction = True

def CentralNelon_2456_MapTrigger_16_39(p):
    ChoiceBox("Although the Nelon Sector is not known for its fertile soil, the towns do keep a fair supply of crops growing close by. Having spent a while in an agricultural section of the continent, you understand the plight of these farmers.\n\nYou learn that the crops they raise are used directly by the residents of the two nearby towns, Glade and Coraeon. However, their supplies alone are not enough to feed everyone.\n\nThe Nelon Sector, like much of the continent, is dependent on shipments of crops from Agran via the teleportation network. However, to keep costs lower (teleporters are expensive to maintain) many areas grow some of their own.\n\nThat is the purpose of this specific farm. You would hate to wonder what would have happened to this region if Zaine and his buddies would have succeeded in releasing that fungus you wiped out. You are sure this area would be hungry.", eDialogPic.CREATURE, 2, ["OK"])
    p.CancelAction = True

def CentralNelon_2457_MapTrigger_33_38(p):
    ChoiceBox("This structure is a massive mill. Grain is imported from Agran and the local countryside and is ground into flour. The large grinding wheels are run by harnessing the current of the nearby river.\n\nSome of the flour is shipped out and some of it is processed into bread and other consumer products. The system is quite the assembly line. Each person is responsible for one small task.\n\nHowever, with hundreds of people, this translates into lots of loaves of bread. You are guessing that thousands of loaves are produced here every day and shipped out to the local areas and even other parts of the continent.", eDialogPic.STANDARD, 16, ["OK"])
    p.CancelAction = True

def CentralNelon_2458_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def CentralNelon_2459_SpecialOnWin1(p):
    ChoiceBox("With the berserk Golem\'s shattered, you come to the wizard\'s aid. It appears that he is going to be all right. The wizard tells you that they were doing an experiment on improving the mental capacity of Golems.\n\nThe experiment was a failure and managed to scatter the minds of the Golems and cause them to destroy everything in sight. The tower was a complete loss and will need to be rebuilt.\n\nIn response to your good deed the wizard decides to break a few laws and teach you an advanced spell called \'Shockwave\'. The spell will create a minor disturbance within the earth causing damage for a short radius.", eDialogPic.CREATURE, 27, ["OK"])
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_shockwave")

def CentralNelon_2460_SpecialOnFlee1(p):
    MessageBox("You decide that it would be better not to get involved with this conflict. Besides the mages should have been more careful.")
    StuffDone["52_8"] = 2
    p.CancelAction = True
