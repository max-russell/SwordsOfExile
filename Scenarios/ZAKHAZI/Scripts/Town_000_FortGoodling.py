
def FortGoodling_0_MapTrigger_14_28(p):
    result = ChoiceBox("The chambers you\'ve been provided are quite comfortable, and the beds are empty and waiting for you. You can spend a few of your precious hours resting, if you want.", eDialogPic.TERRAIN, 143, ["Leave", "Rest"])
    if result == 1:
        Party.Age += 600
        MessageBox("You sleep for several hours and wake up again, feeling refreshed.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += -1
            Party.HealAll(100)
            Party.RestoreSP(100)
        return

def FortGoodling_1_MapTrigger_39_29(p):
    if StuffDone["0_0"] == 250:
        return
    StuffDone["0_0"] = 250
    TownMap.List["FortGoodling_0"].DeactivateTrigger(Location(39,29))
    MessageBox("This supply room contains a variety of useful goods, arranged in neat rows. A note on the wall reads \"Supplies reserved for Fort Cavalier rescue team.\" You think that\'s you.\n\nThere is an odd chill in the air.")

def FortGoodling_2_MapTrigger_22_43(p):
    result = ChoiceBox("You return to the gates of Fort Goodling. Looking through them, you can see the Exile countryside beyond. It would be easy for you to leave, rejecting this mission in favor of safer adventures elsewhere. Do you go?", eDialogPic.TERRAIN, 93, ["No", "Yes"])
    if result == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You boldly stride back into Fort Goodling, ready to boldly face the challenges that await you.")
        return
    elif result == 1:
        MessageBox("You leave Fort Goodling. This mission will just have to be done by someone else.")
        if SpecialItem.PartyHas("BundleofWands"):
            MessageBox("Of course, before you leave, the soldiers relieve you of the bundle of wands.")
            Scenario.End()
            return
        Scenario.End()
        return

def FortGoodling_4_MapTrigger_16_14(p):
    if SpecialItem.PartyHas("BundleofWands"):
        if StuffDone["0_5"] == 250:
            return
        StuffDone["0_5"] = 250
        ChoiceBox("These are the Fort Goodling docks. Two long, low rowboats are moored here, ready for you to take one of them north to Fort Cavalier.\n\nGuards stand at the river, watching the water carefully. Slithzerikai can attack forts by surprise by approaching underwater - guards need to be placed anywhere wet.", eDialogPic.STANDARD, 31, ["OK"])
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You try to go to the fort docks, where two long rowboats are moored. As you try to enter, a guard stops you. \"Sorry, friends,\" he explains. \"We can\'t let you in until you have the goods for Fort Cavalier.\"")

def FortGoodling_5_MapTrigger_32_28(p):
    ChoiceBox("You find an interesting book, titled \"The History of Exile Following the Return.\" A summary:\n\nExile was formed when the Empire, deciding to rid itself of the annoying people on its surface, sent them through a one-way teleporter into the caves far below the surface of the world.\n\nAfter Exile made peace with the Empire, all of its citizens who cared to return to the surface were given land in southeast Valorim. Many of the Exiles decided to return. Surprisingly, many decided to stay in the caves instead.\n\nThe Exiles who had made comfortable lives below ground or who were unable to trust or obey the Empire stayed in their caves, where they continued to tame the underworld and build ever grander subterranean cities.\n\nThe Exiles have been successful, and, to some extent, even prosperous. Massive teleporters carry materials from the underworld to the surface, and the goods necessary for survival in the cave are sent down in return.\n\nAlthough the perils of being an Exile are as great as ever, the future of these strange, pale people has never been brighter.", eDialogPic.TERRAIN, 130, ["OK"])

def FortGoodling_6_MapTrigger_34_34(p):
    ChoiceBox("You find an interesting book, titled \"A Summary of the Second Slith War So Far.\" A summary:\n\nExile contains cities of both friendly, civilized Slithzerikai and evil, barbarian Slithzerikai (also called sliths, a pejorative term). Exile has fought one war with barbarian sliths already, which ended with the assassination of their king, Sss-Thsss.\n\nThe evil sliths, following their defeat, fled to lower caverns as yet unreached by Exiles, where they united, trained, reproduced, and built themselves up into a united, fearsome army. There, they waited with uncharacteristic patience.\n\nWhen half of the Exile population returned to the surface, the slith\'s opportunity presented itself. They attacked through the waterways. They moved swiftly and with the advantage of surprise, butchering many Exile settlers.\n\nNow the Sliths stand poised to destroy the last forts separating them from the Great Cave and the capital of Exile. Fortunately, we still have several options to explore to defeat them.\n\n(The rest of the book has been censored. The pages have been torn out of the book.)", eDialogPic.TERRAIN, 130, ["OK"])

def FortGoodling_13_TalkingTrigger43(p):
    if StuffDone["0_2"] >= 1:
        if SpecialItem.PartyHas("BundleofWands"):
            return
        if StuffDone["0_4"] == 250:
            return
        StuffDone["0_4"] = 250
        p.TalkingText = "Seletine hands you a bundle of what feels like 12 sticks, wrapped in canvas, and sealed shut with a leather band with gold runes. \"These are the wands.\"\n\n\"To help you resist the temptation to open the bundle early, the magical bands will keep the bundle from being opened until you reach Fort Cavalier.\""
        SpecialItem.Give("BundleofWands")
        return
    p.TalkingText = "\"Before I can give you the wands, you should speak with Commander Yale.\""
def Talking_0_33(p):
    Town.NPCList.Remove(p.NPCTarget)
    if p.NPCTarget.Start.LifeVariable != "":
        StuffDone[p.NPCTarget.Start.LifeVariable] = 1
    p.TalkingText = "\"You may enter the citadel of Morog without fear. He wishes, in his might and wisdom, to deal with you. That is all.\" The shade abruptly disappears."
