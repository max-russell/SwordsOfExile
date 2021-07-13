
def KimzahnsCaldera_284_MapTrigger_19_10(p):
    if StuffDone["13_2"] == 250:
        return
    StuffDone["13_2"] = 250
    TownMap.List["KimzahnsCaldera_13"].DeactivateTrigger(Location(19,10))
    TownMap.List["KimzahnsCaldera_13"].DeactivateTrigger(Location(19,11))
    MessageBox("You enter Kimzahn\'s home. It\'s a dome, built with a high ceiling to fit the massive efreet. The air is thick with incense. There is a large, lit brazier in the center of the room, surrounded by thick rugs and pillows for lounging.")

def KimzahnsCaldera_286_OnEntry(p):
    if StuffDone["13_3"] == 250:
        return
    StuffDone["13_3"] = 250
    MessageBox("After what you\'ve seen so far, seeing that someone has built a forge by this lake of lava is less than a surprise. What is unusual is the creature repairing an axe on one of the anvils. It\'s a humanoid, about ten feet tall, with gleaming red skin.\n\nAs you watch the creature work, you notice that it\'s on fire. Tiny flames constantly erupt from his skin, flicker for a few moments, and go out. You think you know what it is: an efreet, a massive, magical creature from, well, from you aren\'t sure where.")

def KimzahnsCaldera_287_CreatureDeath11(p):
    MessageBox("With his dying breath, Kimzahn shouts out \"Please, my brethren! Avenge me!\" As he passes away, many other efreeti appear to get revenge.")
    Town.PlaceEncounterGroup(1)
