
def NortheasternSorcrega_2558_MapTrigger_35_34(p):
    ChoiceBox("Surrounding the Malachite School of Magery are the dormitories for the apprentices. The housing system consists of several areas devoted to residency. This area happens to be one of them.\n\nThere are three kinds of structures contained here, each based on a rigid hierarchy.\n\nThe first kind consists of the Spartan quarters for the standard blue-robed apprentices, the cheapest structures around. The typical room is a small space consisting of a sleeping pad and a shelf to place materials such as textbooks.\n\nThe next kind is step above that is for the full level green-robed mages. Their quarters are actually decent having an actual bed instead of a table, and a few other amenities such as a desk and bookshelves.\n\nThe third variety are the suites reserved for the gray or even purple robed wizards who have duties involving instruction, research, or both. Their rooms are quite luxurious by any normal standards.\n\nWhat you see here is typical. The housing specifications are based upon ancient traditions predating the Empire. One more example of how tradition affects our daily lives.", eDialogPic.CREATURE, 25, ["OK"])
    p.CancelAction = True

def NortheasternSorcrega_2563_MapTrigger_13_39(p):
    result = ChoiceBox("Hidden way up in these hills is a mage tower. Or at least it was a mage tower. The facade of the structure is cracked and has acquired much mold. You can bet that nobody has been here for a while.\n\nYou wonder why anyone would build a mage tower up in these hills. Perhaps if you searched the ruins, you could find out.", eDialogPic.TERRAIN, 197, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["44_1"] == 0:
            StuffDone["44_1"] = 1
            Animation_Hold(-1, 088_slime)
            Wait()
            ChoiceBox("You conduct a search of the ruins. The first thing you notice is the horrible odor that permeates the place. It is very similar to rotten eggs and a mix of sulfur. The fumes make you somewhat nauseous, but you can bare it.\n\nYou figure out where the smell is coming from. Everywhere in the tower is covered by this strange acrid greenish goo. In places of higher concentration, the slime has managed to consume some of the walls.\n\nYou discover a small library, but all of the books have been eaten away by the strange slime. Whatever knowledge may have been contained in them has been lost forever.\n\nFrom there, your search takes you to an area called the laboratory. At least you assume it is the lab, since half-eaten sign outside of the area indicated as such.\n\nAs soon as you open the door, you noses are assaulted by an even heavier concentration of the horrible slime odor. You look inside and notice something very peculiar. These slimes are mobile!\n\nUnfortunately, they begin to move toward you. They are much faster than you might have thought. You are trapped by the slimes and must hack your way through them.", eDialogPic.CREATURE, 107, ["OK"])
            WorldMap.SpawnNPCGroup("Group_5_2_4", p.Target)
            return
        MessageBox("You return to the abandoned tower. A further search reveals nothing new.")
        return
    p.CancelAction = True

def NortheasternSorcrega_2564_MapTrigger_40_44(p):
    result = ChoiceBox("You come to a mage tower, not an unusual sight in this neck of the woods. The area appears to be fairly welcoming, so you decide to take a look inside.\n\nYou discover the typical mage tower setting. One person, the archwizard, directs the towers operations of research and instruction. Under him are lesser wizards and on down the hierarchy to the lowly apprentices.\n\nYou are offered a tour of the tower by one of the wizards. He has a green-robed mage (middle status) lead you around. Like most mage towers, the operation of this place is twofold: magical instruction and research.\n\nThe first area you are shown are the classrooms. They are merely your standard classroom, nothing special. The apprentices live in their small quarters, completely typical. Then you are taken to the research section.\n\nThe main area of research for this tower is the study of flora and fauna in swamps. Within the tower are large rooms containing artificial swamps with all sorts of various plants and creatures. The actual purpose of this research is not told.\n\nFinally, you are led back to the entrance. You are thanked for your cooperation. Before you leave, the mage asks if you would like to purchase some Piercing Crystals that he had made. They would definitely be useful when it comes to magic barriers.", eDialogPic.TERRAIN, 197, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_13_5_2")
        p.CancelAction = True
        return
    p.CancelAction = True

def NortheasternSorcrega_2565_MapTrigger_2_13(p):
    ChoiceBox("This river is rich in fish and the locals have decided to capitalize on that. This is a fair sized village consisting of fisherman. There is little in the way of shops or anything, the villagers rely mostly on sustenance farming, or fishing in this case.\n\nYou notice that many of the fish hanging outside of homes are quite large, larger than you would expect. You decide to ask some of the locals about it.\n\nThey tell you that long ago wizards constructed caverns near the shore to carry on experiments with the river. One of the experiments had the effect of making the fish grow to massive sizes.\n\nThis anomaly has been very beneficial to the locals and has led to a fair profits for the enlarged fish. Whether or not the story is true, you cannot say. You just see the big fishes!", eDialogPic.TERRAIN, 190, ["OK"])
    p.CancelAction = True

def NortheasternSorcrega_2566_MapTrigger_14_15(p):
    if StuffDone["44_2"] == 250:
        return
    StuffDone["44_2"] = 250
    WorldMap.DeactivateTrigger(Location(254,111))
    Animation_Hold(-1, 043_stoning)
    Wait()
    ChoiceBox("Uh oh! You notice several statues of various animals in the vicinity. Your training as Empire soldiers tells you this is a sure sign of basilisk infestation. You decide to pick up your pace and try to avoid a possible confrontation.\n\nUnfortunately, you manage to stumble across the deadly lizards. The group is not all that large, but even one basilisk is deadly.", eDialogPic.CREATURE, 86, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_2_5", p.Target)

def NortheasternSorcrega_2567_MapTrigger_17_16(p):
    if StuffDone["44_3"] == 0:
        if Party.HasTrait(Trait.Woodsman):
            result = ChoiceBox("Your knowledge of woodsman skill reveals a very small patch of Comfrey Root hidden away in this forest. Unfortunately, the patch has not yet matured to the point where it can replenish itself.\n\nMaking a harvest now will surely wipe it out. Generally alchemetical patches take months or even years to mature to a stable point where they can be harvested. You know this patch is nowhere near that point.\n\nDo you make the harvest?", eDialogPic.STANDARD, 20, ["Leave", "Take"])
            if result == 1:
                StuffDone["44_3"] = 1
                MessageBox("You harvest the Comfrey Root. There is really only enough for one helping. Oh well, it looks like this patch won\'t have a chance to get off the ground.")
                Party.GiveNewItem("ComfreyRoot_364")
                return
            return
        return

def NortheasternSorcrega_2568_MapTrigger_23_37(p):
    if StuffDone["44_4"] == 250:
        return
    StuffDone["44_4"] = 250
    WorldMap.DeactivateTrigger(Location(263,133))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("The hills are popular hiding places for all sorts of creatures. Unfortunately, you have just encountered a pack of multiheaded lizards called hydras. Hydras are quite vicious and prey on all but the best equipped patrols.\n\nYou appear to be the next item on their menu!", eDialogPic.CREATURE, 141, ["OK"])
    WorldMap.SpawnNPCGroup("Group_5_2_6", p.Target)

def NortheasternSorcrega_2569_WanderingOnMeet2(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NortheasternSorcrega_2571_SpecialOnWin0(p):
    MessageBox("You manage to wipe out the slimes. You further explore the labs, but a search turns up nothing. Your best guess is that this was some kind of experiment gone wrong. You cannot tell if this is why the tower was abandoned or not.\n\nUnfortunately, anything that may have been of value was consumed by the slimes. They were so corrosive, they even were able to eat away at the thick metal cauldrons! No treasure today. You leave, a bit disappointed.")
    p.CancelAction = True

def NortheasternSorcrega_2572_SpecialOnFlee0(p):
    MessageBox("After running down hallways of caustic fumes, you manage to escape the horrible slimes. You wonder if they were some kind of experiment gone wrong or something. Anyway, if you ever return, you will be sure not to visit the labs.")
    p.CancelAction = True

def NortheasternSorcrega_2573_SpecialOnWin2(p):
    MessageBox("You manage to slay the treacherous Hydras. With some work, you manage to discover a small cave that was the Hydras lair. There you discover lots of bones and all sorts of equipment.\n\nMost of it is quite rusted or chewed up by the Hydras. However, there is a shiny pair of boots that appears to have survived the gnawing of the Hydras. You take it along with the gold coins scattered about.")
    Party.GiveNewItem("MagicBoots_232")
    Party.Gold += 232
