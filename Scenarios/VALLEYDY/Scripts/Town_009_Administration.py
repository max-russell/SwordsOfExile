
def Administration_154_MapTrigger_10_48(p):
    Party.OutsidePos = Location(12, 99)
    if StuffDone["7_5"] >= 1:
        if StuffDone["9_0"] == 250:
            return
        StuffDone["9_0"] = 250
        MessageBox("It looks like a force of nature has smashed its way through this chamber. The exit to the south was blocked by a massive barrier, no doubt placed by the wizards of the school to keep intruders from penetrating farther into the school.\n\nThe wizards did not reckon, however, on the wall having to deflect the attacks of an enraged dragon. Pythras tore this wall down and passed through, having the fortunate incidental effect of enabling you to pass as well.")
        return
    if StuffDone["9_1"] == 250:
        return
    StuffDone["9_1"] = 250
    MessageBox("You start to experience a familiar, unpleasant sinking feeling. Your explorations of the School of Magery have suddenly been sharply limited. The wizards of the School erected a serious barrier to your progress.\n\nThe south exit from the room is blocked by a massive black wall, magically shaped from the living rock of the caverns. As if a five foot thick sheet of solid rock wasn\'t enough, it\'s also covered with a multitude of protective runes. This is a problem.")

def Administration_156_MapTrigger_2_1(p):
    Party.OutsidePos = Location(111, 29)
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(24,45)
    Party.MoveToMap(TownMap.List["StorageLevel_8"])

def Administration_158_MapTrigger_15_1(p):
    Party.OutsidePos = Location(111, 29)
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(14,43)
    Party.MoveToMap(TownMap.List["HoldingCells_7"])

def Administration_159_MapTrigger_4_45(p):
    if StuffDone["9_2"] == 250:
        return
    result = ChoiceBox("The destruction of this level miraculously left this small shrine somewhat intact. In particular, the altar managed to survive, its aura of holiness protecting it from the evil and horror all around you.\n\nIf you want, you can take advantage of it ...", eDialogPic.TERRAIN, 137, ["Leave", "Pray"])
    if result == 1:
        StuffDone["9_5"] += 1
        if StuffDone["9_5"] == 250:
            pass
        MessageBox("You kneel in front of the altar and offer sincere thanks and prayer to, well, whoever the altar was built to. This indiscriminate homage has a positive effect. You feel much better.")
        Party.HealAll(10)
        if StuffDone["9_5"] >= 5:
            MessageBox("Unfortunately, you seem to have exhausted its holy energy. The positive energy in the temple has faded away. Oh well.")
            if StuffDone["9_2"] == 250:
                return
            StuffDone["9_2"] = 250
            TownMap.List["Administration_9"].AlterTerrain(Location(4,45), 1, None)
            TownMap.List["Administration_9"].DeactivateTrigger(Location(4,45))
            return
        return

def Administration_160_MapTrigger_2_4(p):
    if StuffDone["9_6"] == 250:
        return
    StuffDone["9_6"] = 250
    TownMap.List["Administration_9"].DeactivateTrigger(Location(2,4))
    TownMap.List["Administration_9"].DeactivateTrigger(Location(3,4))
    TownMap.List["Administration_9"].DeactivateTrigger(Location(15,4))
    TownMap.List["Administration_9"].DeactivateTrigger(Location(16,4))
    ChoiceBox("Considering the amount of time it\'s been closed up, the good condition of the School has been quite a surprise. The rooms, furniture, and (unfortunately) denizens have been amazingly intact.\n\nAt first, it seems that you\'ve found areas that have been struck by the inevitable decay. This floor is in an advanced state of disrepair. The walls have collapsed, the ceiling has caved in in places, and rubble and debris are everywhere.\n\nLooking closer, however, you realize that the decay was not natural. The walls and rubble have been scorched by fire, and the structures look less like they\'ve fallen apart and more like they were torn apart.\n\nBefore the school was closed, someone went to an awful lot of effort to make sure that this level was blown to pieces. Curiouser and curiouser ...", eDialogPic.TERRAIN, 95, ["OK"])

def Administration_165_MapTrigger_19_40(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 10:
        MessageBox("You find a spellbook which managed to escape the destruction of this floor. It\'s tricky, but you manage to decode it. You can now cast the spell Venom Arrows.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_venom_arrows")
        return
    MessageBox("This spellbook managed to escape the destruction of this floor. Unfortunately, you can\'t understand a word of it. Maybe if you studied the magical arts more ...")

def Administration_166_MapTrigger_15_38(p):
    MessageBox("The desk is filled with ashes and bits of charred paper. Someone didn\'t even bother to take all the papers out before burning them.")

def Administration_168_MapTrigger_26_35(p):
    if StuffDone["9_7"] == 250:
        return
    StuffDone["9_7"] = 250
    TownMap.List["Administration_9"].DeactivateTrigger(Location(26,35))
    TownMap.List["Administration_9"].DeactivateTrigger(Location(27,35))
    ChoiceBox("You hear voices ahead. Adrenaline rushes through your veins. Whoever\'s ahead, you will be able to ambush them! You stalk forward in as stealthy a manner as possible.\n\nAs you get closer, however, you notice that something isn\'t right about the voices. They\'re not gruff and guttural, like goblin voices. They\'re high pitched, chirpy, and friendly, like ... like ...\n\nOh no. You\'ve heard of these creatures. They\'re some of the rarest and most feared denizens of the dungeons of the world: the legendary Giant Intelligent Friendly Talking Spiders.\n\nYou see them ahead, skittering about on the arachnid legs, making webs, chatting happily, and keeping busy. Some monsters are more dangerous. But few are more irritating ...", eDialogPic.CREATURE, 97, ["OK"])

def Administration_170_MapTrigger_55_31(p):
    if StuffDone["9_8"] == 250:
        return
    StuffDone["9_8"] = 250
    TownMap.List["Administration_9"].DeactivateTrigger(Location(55,31))
    TownMap.List["Administration_9"].DeactivateTrigger(Location(56,30))
    MessageBox("You leave the spiders\' caves and enter a new area. Instead of spiders bothering you, you are now surrounded by flying gnats. Like the spiders, these gnats are much larger than usual. In fact, each is about the size of your hand.\n\nThey\'re pretty big and annoying. At least they don\'t talk.")

def Administration_172_MapTrigger_59_4(p):
    if StuffDone["9_9"] == 250:
        return
    result = ChoiceBox("Just under the surface of the stagnant water, you see dozens of clutches of gnat eggs, each promising a multitude of nasty, annoying flying creatures. One of the clusters of eggs is just close enough for you to grab it.", eDialogPic.TERRAIN, 76, ["Take", "Leave"])
    if result == 0:
        StuffDone["9_9"] = 250
        TownMap.List["Administration_9"].AlterTerrain(Location(59,4), 1, None)
        TownMap.List["Administration_9"].DeactivateTrigger(Location(59,4))
        SpecialItem.Give("GnatEggs")
    return

def Administration_173_MapTrigger_62_9(p):
    if StuffDone["100_1"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?", True)
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["100_1"] = 250
    TownMap.List["Administration_9"].DeactivateTrigger(Location(62,9))
    pc.RunTrap(eTrapType.RANDOM, 1, 10)

def Administration_174_MapTrigger_32_9(p):
    if StuffDone["100_2"] == 250:
        return
    StuffDone["100_2"] = 250
    TownMap.List["Administration_9"].DeactivateTrigger(Location(32,9))
    MessageBox("Interesting ... you wouldn\'t have thought that gnats would act like pack rats. Mindless as they may be, they\'ve happily gathered all manner of junk in this room. You see broken scroll tubes, scraps of paper, pottery, and all manner of junk.\n\nThere might even be something useful buried in there. Alas, you don\'t have the months it would take to sort through it all.")

def Administration_175_MapTrigger_25_3(p):
    if StuffDone["9_3"] >= 1:
        if StuffDone["9_4"] == 250:
            return
        result = ChoiceBox("You\'re in luck! If the spiders hadn\'t told you about it, you wouldn\'t have even known to look. You find a small, round black stone, carefully polished, not unlike the stone you used to get inside the School.\n\nIt\'s very smooth, as if many people had rubbed it in the past. You can only hope that it\'s useful.", eDialogPic.TERRAIN, 228, ["Take", "Leave"])
        if result == 0:
            StuffDone["9_4"] = 250
            SpecialItem.Give("OpeningStone")
        return
        return

def Administration_176_MapTrigger_46_19(p):
    if StuffDone["100_3"] == 250:
        return
    StuffDone["100_3"] = 250
    TownMap.List["Administration_9"].DeactivateTrigger(Location(46,19))
    TownMap.List["Administration_9"].DeactivateTrigger(Location(42,9))
    ChoiceBox("There are two things that are interesting about this cave. First, of course, is the fountain in the center.\n\nIt somehow survived and continued to function despite the explosion that destroyed this floor. Magical pumps bring water up from below, and spray it in high, elegant arcs through the air.\n\nThe second interesting thing is the nature of the water. It has the same oily sheen and bitter, acrid smell as the water on the surface. For some reason, the curse is present inside the school too.\n\nAfter the water is pumped up from below, it drains back down again through large grates. You wonder where it goes ...", eDialogPic.STANDARD, 18, ["OK"])

def Administration_178_MapTrigger_51_35(p):
    MessageBox("You find a bunch of rotten, unreadable books. Disappointing.")

def Administration_180_MapTrigger_51_33(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 8:
        MessageBox("You find an ancient, fragile spellbook in the bookshelf. Carefully inspecting it, you find it\'s written in an old, but still decipherable script. Studying carefully, you learn the spell Slow Group.\n\nYou return the book to its shelf ... it\'s far too fragile to carry with you,")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_slow_group")
        return
    MessageBox("You find yet another magical book. You grab it eagerly, flipping through the delicate pages for useful information. Unfortunately, you can\'t understand any of it.\n\nYou return the book to its shelf ... it\'s far too fragile to carry with you,")

def Administration_181_MapTrigger_23_53(p):
    if StuffDone["9_3"] >= 1:
        MessageBox("The spiders have placed the gnat eggs you provided in the piles of refuse here. They are already starting to hatch, and will soon provide many, many tasty spider snacks.")
        return

def Administration_182_OnEntry(p):
    if StuffDone["7_5"] >= 1:
        for x in range(8, 11):
            for y in range(55, 56):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
        return

def Administration_183_TalkingTrigger6(p):
    if StuffDone["9_3"] >= 1:
        p.TalkingText = "\"Yeah, we can help you! Thanks for the happy eggs, by the way. Don\'t forget ... a gnat took the stone. It was small and shiny and black, and it\'s sure to be hidden in the gnat caves somewhere or other.\""
        return
    if StuffDone["100_5"] >= 1:
        if SpecialItem.PartyHas("GnatEggs"):
            p.TalkingText = "You give the chief spider the gnat eggs. It does a happy little dance. \"Thank you! Now we can raise our own yummy gnats and not hunt them! In return, I will help you and stuff!\"\n\n\"We had a pretty magic stone, but a gnat grabbed it and flew it to the north. If you search the gnat\'s caves you\'re sure to find it!\" (You take note of this.)"
            SpecialItem.Take("GnatEggs")
            StuffDone["9_3"] = 1
            return
        return
    StuffDone["100_5"] = 1
    return
def Talking_9_9(p):
    Town.NPCList.Remove(p.NPCTarget)
    if p.NPCTarget.Start.LifeVariable != "":
        StuffDone[p.NPCTarget.Start.LifeVariable] = 1
    p.TalkingText = "\"Yeah, that\'s the password! You can go by.\" It skitters away."
