
def Marralis_28_MapTrigger_12_14(p):
    if StuffDone["3_0"] == 250:
        return
    StuffDone["3_0"] = 250
    TownMap.List["Marralis_3"].DeactivateTrigger(Location(12,14))
    TownMap.List["Marralis_3"].DeactivateTrigger(Location(22,18))
    TownMap.List["Marralis_3"].DeactivateTrigger(Location(32,18))
    MessageBox("By any measure, this town\'s crops are a disaster. They get plenty of sun and plenty of water from the nearby river, and yet they are dying by the bushel. The dead plant matter then rots, coating the ground with a thick, viscous mass.\n\nYou can\'t blame people for abandoning the Vale, if this is all their life\'s work amounts to.")

def Marralis_31_TalkingTrigger27(p):
    if StuffDone["3_2"] >= 1:
        p.TalkingText = "\"Much to our relief, the scepter you returned has shown signs of alleviating the afflictions of the curse. Alas, it only helps, not cures. Still, you may take satisfaction in your endeavors. You have performed a great and kind act.\"\n\n\"By the way, have you found the other artifact from the school?\""
        return
    if StuffDone["3_1"] >= 1:
        if SpecialItem.PartyHas("HealingScepter"):
            p.TalkingText = "Broder\'s jaw drops. He takes the scepter reverently. \"I have heard of this blessed object, but had not dreamed that we could find it.\" He removes from a pouch a slender wand. \"Here is a reward. Thank you again for your invaluable help!\"\n\n\"He thinks. That reminds me. I know someone else who owns an artifact from the school.\""
            SpecialItem.Take("HealingScepter")
            Party.GiveNewItem("WandofFireballs_284")
            StuffDone["3_2"] = 1
            return
        return
    StuffDone["3_1"] = 1
