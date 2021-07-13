
def Arrphyr_1076_MapTrigger_34_37(p):
    if StuffDone["24_3"] == 250:
        return
    StuffDone["24_3"] = 250
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(34,37))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(34,38))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(34,41))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(36,41))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(37,41))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(40,40))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(40,41))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(40,36))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(38,35))
    TownMap.List["Arrphyr_46"].DeactivateTrigger(Location(37,35))
    MessageBox("This appears to have once been some kind of shrine. It was destroyed by a very powerful explosion. There is not much left, but the altar did survive. You can bet this occurred as a direct result of a Nephil conflict.")

def Arrphyr_1086_MapTrigger_35_12(p):
    if StuffDone["24_4"] == 1:
        if StuffDone["24_5"] == 250:
            return
        StuffDone["24_5"] = 250
        ChoiceBox("You return to Arrphyr and present the Mithral Maiden to the chieftain. His eyes narrow and he asks. \"Where did you get this!?\" You respond by telling him it was found in the trader\'s fortress, Cyrpus.\n\n\"I find this difficult to believe. The traders are our brothers and allies and have always been. I do not believe that they would start a war just to profit. However, I\'m sorry but...\" The chief mutters a few words. You feel sharp pains in your head.\n\n\"Now I must ask you again, exactly where did you find the Mithral Maiden?\" Your response is difficult because of the magic but essentially the same. You are forced to give a detailed description of your adventure.\n\nThe chief wears a grave expression. \"I am sorry that I had to resort to truth spells, but it was necessary. This is grim news to have been used by the traders. And all this time, they convinced us it was Gwas! We believed them!\"\n\nHe shakes his head. \"No longer. A few things are for certain. This conflict is over, no longer shall the traders benefit from this war. No longer shall we have any dealings with them. Never again...\"\n\nSuddenly, a Nephil Soldier bursts past you. \"Your honor! The Tribe of Gwas is attacking! We need your guidance!\"", eDialogPic.CREATURE, 41, ["OK"])
        SpecialItem.Take("MithralMaiden")
        Animation_Hold(-1, 023_startoutdoorcombat)
        Wait()
        ChoiceBox("The chief orders his men to surrender and calls a truce and meets with the chieftain of Gwas. He tells the story to the other chieftain. They seem to come to an agreement. It appears this tribal conflict that has plagued this area.\n\nThe chief returns to you. \"This war is over. To think that our own brothers would betray us. To convince us to fight just to sell their goods. What corruption has become of our people.\"\n\nHe sighs. \"However, now we must come together and rebuild! You have done a great service to us and you have our blessings. I suppose I should reward you, but I fear our tribe cannot spare the resources.\"", eDialogPic.CREATURE, 41, ["OK"])
        StuffDone["24_1"] = 1
        for pc in Party.EachAlivePC():
            pc.AwardXP(40)
        return
