
def AncientLab_1860_MapTrigger_25_15(p):
    MessageBox("This lever has rotted away long ago. You wonder how the spores operate the mechanism.")

def AncientLab_1861_MapTrigger_1_1(p):
    if StuffDone["63_4"] == 250:
        return
    StuffDone["63_4"] = 250
    TownMap.List["AncientLab_76"].DeactivateTrigger(Location(1,1))
    ChoiceBox("How peculiar! This ancient structure is surrounded by a vast field of various kinds of fungus. Spores fill the air to the point where it creates a strange haze.\n\nAlthough the structure is ancient, probably a millennium old, the walls are in extremely good condition. Judging by the barren landscape, there probably have not been too many disturbances such as erosion.\n\nThe thickness of the walls and the engineering definitely helped. Old Imperial structures were usually built to last.", eDialogPic.TERRAIN, 73, ["OK"])

def AncientLab_1862_MapTrigger_25_39(p):
    if StuffDone["63_5"] == 250:
        return
    StuffDone["63_5"] = 250
    TownMap.List["AncientLab_76"].DeactivateTrigger(Location(25,39))
    Animation_Hold(-1, 035_spiderhi)
    Wait()
    ChoiceBox("Although the exterior was pretty much flawless, the interior is just the opposite. The front of the other room is in utter ruin. The floor is overgrown with spores, mold, and has been mostly eaten away.\n\nAt the other end of the room, you see a giant living spore gliding about. Generally these creatures are dumb and eat anything they can. However, this one seems to take no interest in you, not yet at least.\n\nDid someone just say \"Hi\"?", eDialogPic.CREATURE, 69, ["OK"])

def AncientLab_1863_MapTrigger_33_34(p):
    if StuffDone["63_3"] >= 4:
        for n in range(Town.NPCList.Count-1, -1, -1):
            npc = Town.NPCList[n]
            if npc.Record.ID == "VahnataiWarrior_92": Town.NPCList.Remove(npc)
        Town.PlaceEncounterGroup(1)
        return

def AncientLab_1865_MapTrigger_28_14(p):
    if StuffDone["63_3"] < 4:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange force holds this door closed.")
        return
    if StuffDone["63_6"] == 250:
        return
    StuffDone["63_6"] = 250
    MessageBox("You open this door and enter a cramped record hall. You notice the immediate change in atmosphere: from damp to bone dry. This is a common practice to help preserve records. Most of these appear to be worthless unfortunately.")

def AncientLab_1867_MapTrigger_27_15(p):
    MessageBox("This bookshelf contains administrative records of the day to day activities of this place. It provides little in the way of clues about this place.")

def AncientLab_1877_MapTrigger_31_16(p):
    ChoiceBox("You discover a journal describing the purpose of this isle. The dates are back in the fourth Imperial century, a time when the Empire still had credible opposition to global domination.\n\nThis island was established to perform research on weapons on several fronts. This lab was specifically established to create improved biological entities to assist in battle campaigns.\n\nIt makes note of the prolific semi-intelligent fungus that can grow so fast as to overcome any hostile fortress. Apparently the spores evolved much since that time, gaining psychic abilities.\n\nAlthough it does not detail it much, it does give a description of the main research in the central building. The mages wondered if it would be possible to implant certain destructive properties of certain materials into the land.\n\nThe poisoning would last several decades and was designed to be used on large hostile nations to wipe them out economically. When the effect subsides, the Empire would move in and conquer.\n\nHowever, this island became heavily contaminated through this research and had to be abandoned as per the final entries. You wonder if the Vahnatai are using the left over mechanisms to accomplish their goals -- scary thought indeed.", eDialogPic.TERRAIN, 135, ["OK"])

def AncientLab_1878_MapTrigger_27_17(p):
    ChoiceBox("You find a book mentioning a system of underground tunnels that were going to connect the central structure of the four labs. These tunnels would largely be used for storage and more dangerous weapon testing.\n\nIt appears that construction never completed before the island had to be abandoned. Although mostly complete, only two of the structures were hooked up via the \'latest in teleportation research\'.\n\nThese two are the central and the western structures. At the time, the craze in teleportation involved the use of gemstones and pentagrams to establish and link portals.\n\nThese set ups required five rare gems using three major kinds that you have had some experience with: Prismitite, Dream Quartz, and Vulcan Amber. It appears that all forms of parallel structure have been cleared up by new mechanisms.\n\nAnyway, there were many sequences to be made. The only ones noted are those that allow you to access the underground structure from the central and western lab. You may access them through the west lab by the combination:\n\nAmber, Prismitite, Prismitite, Quartz, Prismitite going clockwise starting at the north point. If you place these gemstones on a pentagram in this order, a portal will be activated.", eDialogPic.TERRAIN, 135, ["OK"])

def AncientLab_1879_OnEntry(p):
    if StuffDone["63_4"] == 250:
        return
    StuffDone["63_4"] = 250
    TownMap.List["AncientLab_76"].DeactivateTrigger(Location(1,1))
    ChoiceBox("How peculiar! This ancient structure is surrounded by a vast field of various kinds of fungus. Spores fill the air to the point where it creates a strange haze.\n\nAlthough the structure is ancient, probably a millennium old, the walls are in extremely good condition. Judging by the barren landscape, there probably have not been too many disturbances such as erosion.\n\nThe thickness of the walls and the engineering definitely helped. Old Imperial structures were usually built to last.", eDialogPic.TERRAIN, 73, ["OK"])

def AncientLab_1880_TalkingTrigger11(p):
    if StuffDone["63_3"] >= 2:
        if StuffDone["63_3"] >= 4:
            p.TalkingText = "\"Prisoner been released as promised.\""
            return
        p.TalkingText = "You tell of Aroal\'s terms to share the secret to accessing the Vahnatai bunker in exchange for his freedom. Spore thinks. \"Tell him he share knowledge and we not eat. When spores are free, so shall he.\""
        return
    if StuffDone["63_3"] < 1:
        return
    p.TalkingText = "You tell of Aroal\'s terms to share the secret to accessing the Vahnatai bunker in exchange for his freedom. Spore thinks. \"Tell him he share knowledge and we not eat. When spores are free, so shall he.\""
    StuffDone["63_3"] = 2

def AncientLab_1881_TalkingTrigger15(p):
    if StuffDone["63_3"] >= 2:
        p.TalkingText = "He looks disappointed at the news. \"I guess some hope is better than none. I will do my part. In the northern lab you shall find a Vahnatai statue. Touch the statue on the forehead and say \'dhev\'. Please Imperials, succeed so I may live.\""
        StuffDone["63_3"] = 3
        return
    if StuffDone["63_3"] < 2:
        StuffDone["63_3"] = 1
        return
