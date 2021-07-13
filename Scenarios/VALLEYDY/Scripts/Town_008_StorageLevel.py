
def StorageLevel_114_MapTrigger_22_45(p):
    MessageBox("The words \"Sign in before seeing specimen.\" are carved into the pedestal. The sign-in book, however, is long absent.")

def StorageLevel_115_MapTrigger_23_19(p):
    if StuffDone["8_0"] == 250:
        return
    StuffDone["8_0"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(23,19))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(24,19))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(23,30))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(24,30))
    MessageBox("The floor of the corridor ahead is covered with strange weblike husks, each about 3 feet long. When you get closer, you see what they are: the bodies of goblins, each wrapped in webs and sucked dry.")

def StorageLevel_119_MapTrigger_26_24(p):
    if StuffDone["8_1"] == 250:
        return
    StuffDone["8_1"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(26,24))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(39,24))
    MessageBox("Some sort of magic keeps this chamber freezing cold, and, remarkably, the spell is still functioning many years after the school closed. You see many chunks of frozen, old meat.")

def StorageLevel_120_MapTrigger_46_2(p):
    MessageBox("The School of Magery is filled with all manner of fascinating, long-lasting magical devices, and this thing is no exception. It\'s a machine for making chickens. Looking through a small window, you see rows of eggs waiting to hatch.\n\nYou can\'t be sure where the eggs came from. The chickens hatched from the machine probably provide them - the machine has a pair of ominous mechanical arms, which probably occasionally grab a passing fowl.")

def StorageLevel_122_MapTrigger_26_37(p):
    if StuffDone["8_2"] == 250:
        return
    StuffDone["8_2"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(26,37))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(26,38))
    MessageBox("Any Empire organization generates an awful lot of paperwork, and the School was clearly no exception. Looking through this opening, you see room after room filled with bookshelves, no doubt for storing all manner of forms and bureaucratic mumbo-jumbo.\n\nStrangely, considering all the creatures that roam loose in the School, these chambers have been left completely undisturbed.")

def StorageLevel_124_MapTrigger_23_34(p):
    if StuffDone["8_3"] == 250:
        return
    StuffDone["8_3"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(23,34))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(24,34))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(24,41))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(25,41))
    ChoiceBox("As you walk down the corridor, your minds are suddenly attacked. One moment, nothing unusual is happening, The next, you feel a weighty presence floating in and out of your minds.\n\nAs you struggle to concentrate and repel the presence, it suddenly decides to withdraw. As you feel it go, it leaves you a message, written neatly in among your memories. It says, simply:\n\n\"I am Pythras. I am imprisoned nearby. Come to me. I will help you.\"\n\nPythras also left an image of herself in your minds. You recognize what she is immediately. She\'s a dragon.", eDialogPic.CREATURE2x2, 2, ["OK"])

def StorageLevel_128_MapTrigger_19_33(p):
    if StuffDone["8_4"] == 250:
        return
    result = ChoiceBox("You are walking down a wide passage circling a massive basalt dome. Whatever the School liked to store inside here, they were determined to make sure it didn\'t escape. The floor just ahead has two runes of warding etched inside it.\n\nThey are glowing brightly, and putting off a fair amount of heat as well. Heavy duty magic. They\'re definitely here to keep something in. The only question is whether they\'ll keep you out as well. Do you approach?", eDialogPic.TERRAIN, 124, ["Leave", "Approach"])
    if result == 1:
        StuffDone["8_4"] = 250
        TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(19,33))
        TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(20,33))
        TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(20,40))
        TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(19,40))
        MessageBox("You walk over the runes. They make you quite warm, but don\'t hurt you in any way. Lucky break.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Being a valiant adventurer does not include, in your opinion, being baked alive by some sort of bizarre magical trap. You back away.")

def StorageLevel_132_MapTrigger_13_34(p):
    if StuffDone["8_5"] == 250:
        return
    StuffDone["8_5"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(13,34))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(14,34))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(15,34))
    MessageBox("At first, you aren\'t sure what this machinery does. Then, when you approach, it makes a chirpy, humming sound, and spits out several pieces of greenish, moldy meat.\n\nThis must be how the dragon gets fed. You try to get it to spit out meat again, but it doesn\'t. The machine must not like you very much. It also doesn\'t like Pythras, if this meat is the only thing it ever feeds her.")
    Town.PlaceItem(Item.List["VeryOldMeat_386"].Copy(), Location(15,34))

def StorageLevel_135_MapTrigger_43_33(p):
    if StuffDone["8_6"] == 250:
        return
    StuffDone["8_6"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(43,33))
    MessageBox("This is very interesting. This room must have contained a number of spell books. Before the School was abandoned, however, someone came here, and, with a few well placed fireballs, burned them all.\n\nConsidering the amount of ash and charred paper here, it must have been quite a library. You look over the wreckage, stunned by the sheer waste of it, and can only wonder who would do such a thing.")

def StorageLevel_136_MapTrigger_28_27(p):
    MessageBox("What luck! Among the endless rows of meaningless, rotting paperwork, you find a spell book, which must have been misfiled. You flip through it for a bit. It\'s very well written - you don\'t have any trouble understanding it.\n\nSoon, you\'ve committed the arcane instructions to memory. You now know the spell Wall of Ice.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("m_wall_of_ice")

def StorageLevel_137_MapTrigger_43_46(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(43,46)).Num == 191:
        MessageBox("When you examine this bookshelf, you notice that it\'s leaning away from the wall slightly. Curious, you pull on it, and find that it swings away from the wall.")
        Town.AlterTerrain(Location(43,46), 0, TerrainRecord.UnderlayList[170])
        return

def StorageLevel_138_MapTrigger_35_46(p):
    result = ChoiceBox("Bookworms have had their way with the books on this shelf. Most of them crumble at your touch. One book, however, remains in good condition. It\'s a heavy tome, bound in black leather and brass fittings.\n\nYou reach out to get it, hoping to examine it, and find it\'s icy cold to the touch. If you were careful, you could read it without freezing your fingers, but only if you wanted to ...", eDialogPic.TERRAIN, 135, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 7:
            MessageBox("The book contains various spells for the creation and manipulation of cold. You try to etch the runes into your memory. Most of the rituals are beyond your ability, but one isn\'t. You can now cast Ice Bolt.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("m_ice_bolt")
            return
        MessageBox("You flip through the pages of the frigid book, only to find that the magical script inside is far beyond your understanding. In fact, even attempting to read it warps and twists your minds.\n\nYou quickly close the book and put it back before it does you too much harm.")
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 1))
        return

def StorageLevel_139_MapTrigger_30_45(p):
    MessageBox("Wedged between to moldering tomes, you find a note, which seems to have never reached its addressee: \"Pergaltho - Vinnia plans something. I know not what. She means us no good, though.\"\n\n\"Desperate times, my friend. I have done my best in Master Control to make sure disaster can avoided. We can only hope someone makes it down there, before disaster strikes. - Palhatis.\"")

def StorageLevel_140_MapTrigger_37_38(p):
    if StuffDone["7_7"] == 250:
        return
    StuffDone["7_7"] = 250
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(37,38))
    TownMap.List["StorageLevel_8"].DeactivateTrigger(Location(37,34))
    MessageBox("The mystery of who has been protecting the bookshelves has been solved. Several insubstantial beings with very substantial claws have flowed out of the walls. One is in front of you. The rest are behind.\n\nAlas, you don\'t think they want to be friends.")
    Town.PlaceEncounterGroup(1)

def StorageLevel_142_MapTrigger_23_1(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply upward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(25,22)
    Party.MoveToMap(TownMap.List["VisitorsQuarters_6"])

def StorageLevel_143_MapTrigger_22_42(p):
    ChoiceBox("You find a detailed fresco set into the wall, providing a crude map of this level. It\'s divided into four quarters, each devoted to storing a different thing.\n\nThe northwest corner is for dry goods. The northeast corner is for \"live meat products.\" The southeast is dedicated to books and paperwork. Finally, the southwest corner is left intriguingly, ominously blank.", eDialogPic.TERRAIN, 94, ["OK"])

def StorageLevel_147_MapTrigger_1_26(p):
    MessageBox("Once, these pedestals bore books containing detailed catalogs of all the items stored in this area. Unfortunately, the books are gone. Chitrachs ate them.")

def StorageLevel_150_MapTrigger_21_36(p):
    if StuffDone["7_5"] >= 1:
        MessageBox("This enormous holding area has grown cold and quiet since you were last here. Pythras obviously lost no time in escaping. She certainly didn\'t stay behind to give you any thanks.")
        return

def StorageLevel_152_MapTrigger_24_46(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(3,2)
    Party.MoveToMap(TownMap.List["Administration_9"])
