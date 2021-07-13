
def OgreFarms_165_MapTrigger_35_8(p):
    ChoiceBox("You\'ve seen a lot of odd things, but you\'ve never seen anything like this. Ogres are hunters, vicious carnivores. The last thing you\'d ever expect to see them doing is raising any sort of crop.\n\nYet, here they are, in their strange, glazed daze, carefully tending to long rows of bright green plants. The plants aren\'t food, though. They have a strong smell, which burns your nose slightly.\n\nSomething odd is going on here.", eDialogPic.TERRAIN, 181, ["OK"])

def OgreFarms_166_MapTrigger_8_28(p):
    if StuffDone["14_2"] == 250:
        return
    StuffDone["14_2"] = 250
    TownMap.List["OgreFarms_14"].DeactivateTrigger(Location(8,28))
    TownMap.List["OgreFarms_14"].DeactivateTrigger(Location(10,25))
    TownMap.List["OgreFarms_14"].DeactivateTrigger(Location(20,28))
    if Party.HasTrait(Trait.Woodsman):
        MessageBox("This room is filled with the overpowering stench of leaves being cut, boiled, and treated. The strong, bitter smell makes your eyes water. The leaves being grown outside are being processed into a thick, strong brew.\n\nNow that you\'ve seen this, your Woodsman skills tell you what the plants are: Skribbane herb. When boiled and drunk, it saps the will and makes the drinker dazed and pliable. The ogres here are victims of powerful mind control.")
        return
    MessageBox("This room is filled with the overpowering stench of leaves being cut, boiled, and treated. The strong, bitter smell makes your eyes water. The leaves being grown outside are being processed into a thick, strong brew.\n\nYou still aren\'t sure what the brew is for. The ogres must just like it.")

def OgreFarms_169_MapTrigger_20_39(p):
    if StuffDone["14_3"] == 250:
        return
    StuffDone["14_3"] = 250
    TownMap.List["OgreFarms_14"].DeactivateTrigger(Location(20,39))
    ChoiceBox("You enter this huge, fiery chamber, and come face to face with a giant, scaled monstrosity, straight out of your worst nightmares. It\'s a huge demon, sitting in its throne waiting for you.\n\n\"At last,\" it laughs. \"You\'ve gotten through my defenses. I had long expected you humans would come here. I am not worried! My ogre slaves will soon be replaced, and my strength will continue to grow.\"\n\n\"First, though, I must kill you.\" It stands, flexing its claws. \"No hard feelings.\"", eDialogPic.CREATURE, 72, ["OK"])

def OgreFarms_170_MapTrigger_2_10(p):
    MessageBox("Thick ogre fingers have pored over parts of this alchemy text to the point of unreadability. Most of the recipes you can read are useless. The one you can\'t read involves something called \"Will Destroying Brew.\"")

def OgreFarms_171_MapTrigger_4_10(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 13:
        MessageBox("You find an ogre mage\'s spell book. It\'s a hastily scrawled mess, and the notation is very non-standard. Fortunately, you\'re able to make some sense of it.\n\nYou now know the spells Major Blessing and Major Cleansing.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_major_blessing")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_major_cleansing")
        return
    MessageBox("You find an ogre mage\'s spellbook. Unfortunately, the ogre\'s magical notation is unreadable. You try for a little while, but you can\'t make any sense of it.")

def OgreFarms_172_OnEntry(p):
    if StuffDone["14_0"] >= 1:
        MessageBox("The ogre\'s lair is a lot quieter now that the demon is gone and his slaves have fled. You still hear grunts and howls from deep inside, and they still sound dangerous. Just not as much.")
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "Ogre_45": Town.NPCList.Remove(npc)
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "OgreWarrior_47": Town.NPCList.Remove(npc)
        return
    if StuffDone["14_1"] == 250:
        return
    StuffDone["14_1"] = 250
    ChoiceBox("You approach this small settlement, and immediately come face to face with a huge, armed ogre. You reach for your weapons and brace yourselves, getting ready for the attack.\n\nAfter a moment, however, you realize the ogre isn\'t quite all right. It seems to be in a daze, moving around and doing its work mechanically. It seldom blinks, and drool trickles out of its mouth. It almost looks drugged.\n\nYou relax, thinking that you aren\'t going to be in a fight after all. Then, suddenly, the ogre catches your scent. Without thinking, it grabs its club and charges to attack!", eDialogPic.CREATURE, 112, ["OK"])

def OgreFarms_173_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(33, 31),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(34, 34),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(32, 30),WorldMap.SectorAt(Party.OutsidePos))

def OgreFarms_174_CreatureDeath32(p):
    MessageBox("The death blow delivered, the demon collapses. The last look on his scaly face is one of surprise.\n\nThe hold over their minds loosened, you hear the ogres outside howling with relief. The ogre slaves flee the fortress, leaving their leaders alone. This operation is pretty much shut down.")
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Ogre_45": Town.NPCList.Remove(npc)
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "OgreWarrior_47": Town.NPCList.Remove(npc)
