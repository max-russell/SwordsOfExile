
def MrrnahHollow_62_MapTrigger_22_42(p):
    p.CancelAction = True
    result = ChoiceBox("The road to the south leads up and out of Mrrnah Hollow. If you\'ve completed your investigation to your satisfaction, you can leave now. Are you done here?", eDialogPic.STANDARD, 30, ["No", "Yes"])
    if result == 0:
        return
    elif result == 1:
        if StuffDone["100_0"] >= 1:
            ChoiceBox("You leave the valley triumphantly and return to Krizsan, where the commander is very happy to see you. Your mission was a complete success: the bandits are dead, and citizens are already returning to Cavala.\n\nThe commander gives you your well-earned reward: a thousand gold pieces and a beautifully made short sword. After receiving a few more accolades, you move on. There are more adventures to be had!\n\nSure, you didn\'t save the world, but there\'s still plenty of satisfaction in a small job done quickly and well. You may not have had the scale, but you had the craftsmanship.\n\nTHE END", eDialogPic.CREATURE, 17, ["OK"])
            Party.GiveNewItem("MagicShortSword_78")
            Party.Gold += 1000
            for pc in Party.EachAlivePC():
                pc.AwardXP(20)
            Scenario.End()
            return
        MessageBox("You return to Krizsan and tell the commander there of your failure to complete your mission. Needless to say, you receive no reward. The commander dismisses you curtly, and sets to work finding a new group of adventurers to send.\n\nOh well. Sometimes, failing an adventure means the end of the world . This time, it just means someone else will finish it. Not a problem. You ride off, looking for new things to try.\nThe end.")
        Scenario.End()
        return

def MrrnahHollow_65_MapTrigger_15_8(p):
    if StuffDone["200_0"] == 250:
        return
    result = ChoiceBox("You stumble upon a small, well hidden supply cache! You can\'t be sure whether it was left here by the bandits ... a careful search reveals no sign of who left these supplies here.\n\nThere are several bags of food and a small bottle. The bottle is labeled \'Hrras Juice\'. Hrras Juice is the Hollow\'s lead export - a sour drink with mild healing properties.\n\nAll of the stuff is fresh. The cache is probably fairly new. It may well have been left by the bandits.", eDialogPic.TERRAIN, 81, ["Take", "Leave"])
    if result == 0:
        StuffDone["200_0"] = 250
        WorldMap.DeactivateTrigger(Location(15,104))
        WorldMap.DeactivateTrigger(Location(14,104))
        Party.GiveNewItem("HrrasJuice_383")
        Party.Food += 40
    return

def MrrnahHollow_67_MapTrigger_37_20(p):
    if StuffDone["200_2"] == 250:
        return
    StuffDone["200_2"] = 250
    WorldMap.DeactivateTrigger(Location(37,116))
    MessageBox("Hiking up into these hills, you hear the distant howling of wolves.")

def MrrnahHollow_68_MapTrigger_42_15(p):
    if StuffDone["200_1"] == 250:
        return
    StuffDone["200_1"] = 250
    WorldMap.AlterTerrain(Location(42,111), 1, None)
    WorldMap.DeactivateTrigger(Location(42,111))
    MessageBox("Wolves start appearing on the crags above you. They watch you intently as you march. Then they run off. You don\'t worry. Wolves aren\'t uncommon in the wilds, and they almost never actually attack humans.\n\nThese wolves are different, however. The whole pack is waiting for you as you turn to march back down. They aren\'t the least bit nervous about humans. They attack.")
    WorldMap.SpawnEncounter("Group_0_2_4", p.Target)

def MrrnahHollow_69_MapTrigger_22_1(p):
    result = ChoiceBox("In the middle of this small copse of trees, you see what looks like the site of a recent combat.", eDialogPic.TERRAIN, 81, ["Leave", "Approach"])
    if result == 1:
        MessageBox("You were right. There was a fight here recently. Blood stains are still visible on the ground. The tracks lead you to guess that a caravan was attacked here recently. They were camped here when they were ambushed.\n\nMost of the tracks leading away have faded by now, and everything of value was stripped away. Unfortunately, you don\'t find any signs of who the bandits were or where they came from.")
        return

def MrrnahHollow_70_SpecialOnWin0(p):
    MessageBox("You find the wolves lair nearby and soon figure out why they were so aggresive. The lair is filled with humanoid bones, all well gnawed. These wolves have feasted wel on the bandits\' leavings.\n\nUnfortunately, there is no treasure among the grisly remains.")
