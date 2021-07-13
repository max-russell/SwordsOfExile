
def SoutheasternAizic_2593_MapTrigger_36_37(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This way leads into Troglodyte territory and sure conflict. You do not want to go this way.")

def SoutheasternAizic_2594_MapTrigger_38_39(p):
    MessageBox("This was the encampment of wizards you had arrived at originally. Now, it is empty except for a note saying, \"Excellently done! Proceed northward to the Citadel, we shall meet there. -- Dervish Montcalm\"")

def SoutheasternAizic_2595_MapTrigger_9_24(p):
    if StuffDone["3_5"] >= 6:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("In the wake of the Portal Fortress\'s destruction, a massive landslide has occurred obstructing your passage.")
        return

def SoutheasternAizic_2596_MapTrigger_21_24(p):
    if StuffDone["16_5"] == 0:
        if Party.HasTrait(Trait.Woodsman):
            result = ChoiceBox("Your knowledge of woodsman skill reveals many hiding places in the hills to your side. It is very likely that you will be walking into an ambush if you continue. One thing on your side is that you will be ready.", eDialogPic.CREATURE, 113, ["Onward", "Flee"])
            if result == 0:
                StuffDone["16_5"] = 1
                MessageBox("You walk forward very carefully. When rocks begin to fly, you fall back undamaged. The Troglodytes charge from their hiding spaces. You\'re now on better footing than you would have been without knowing about it ahead of time.")
                WorldMap.SpawnNPCGroup("Group_1_3_4", p.Target)
                return
            elif result == 1:
                p.CancelAction = True
                return
            return
        StuffDone["16_5"] = 1
        Party.Damage(Maths.Rand(3, 1, 5) + 10, eDamageType.WEAPON)
        Wait()
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 4))
        for pc in Party.EachAlivePC():
            pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 4))
        ChoiceBox("You\'ve just stumbled into a massive ambush! Rocks fly out from the hills as shamans assault you with spells. The Troglodytes charge to finish you off. Not good.", eDialogPic.CREATURE, 113, ["OK"])
        WorldMap.SpawnNPCGroup("Group_1_3_4", p.Target)
        return

def SoutheasternAizic_2597_MapTrigger_13_31(p):
    if StuffDone["16_6"] == 250:
        return
    StuffDone["16_6"] = 250
    WorldMap.DeactivateTrigger(Location(61,175))
    MessageBox("You have just stumbled into a Troglodyte patrol. They don\'t take to friendly to Empire soldiers trespassing onto their territory.")
    WorldMap.SpawnNPCGroup("Group_1_3_5", p.Target)

def SoutheasternAizic_2598_MapTrigger_9_27(p):
    if StuffDone["16_7"] == 250:
        return
    StuffDone["16_7"] = 250
    WorldMap.DeactivateTrigger(Location(57,171))
    MessageBox("You have just stumbled into a Troglodyte patrol. They don\'t take to friendly to Empire soldiers trespassing onto their territory.")
    WorldMap.SpawnNPCGroup("Group_1_3_5", p.Target)

def SoutheasternAizic_2599_MapTrigger_28_36(p):
    if StuffDone["16_8"] == 250:
        return
    StuffDone["16_8"] = 250
    WorldMap.DeactivateTrigger(Location(76,180))
    MessageBox("You have just stumbled into a Troglodyte patrol. They don\'t take to friendly to Empire soldiers trespassing onto their territory.")
    WorldMap.SpawnNPCGroup("Group_1_3_5", p.Target)

def SoutheasternAizic_2600_MapTrigger_20_42(p):
    ChoiceBox("Ahead you see a wall fortress packed with Troglodytes. As you near, Troglodytes begin to throw spears at you. You back off unharmed. You could take tens of Troglodytes but not hundreds of them.\n\nA full scale fighting force would have no problem handling this, but you would be crushed quickly. You will not be able to proceed this way.", eDialogPic.CREATURE, 113, ["OK"])
    p.CancelAction = True

def SoutheasternAizic_2602_MapTrigger_45_12(p):
    MessageBox("This small guardpost sections the Imperial Sector and the Aizic Sector. The attendants check your papers and allow you to pass.")
    if StuffDone["54_0"] == 250:
        return
    StuffDone["54_0"] = 250
    WorldMap.DeactivateTrigger(Location(156,197))
    ChoiceBox("You arrive at the Imperial Sector, the center of the Empire and the entire world. It is within this Sector that tens of thousands of decisions are made each day about public policy by various officials and bureaucrats.\n\nIt is here where most of Pralgad\'s soldiers (including you) are trained. Armies are housed within the sector to help maintain security and order. The protection of the capital of the Empire, Solaria, is paramount.\n\nThe Imperial Sector is probably the most densely populated sector in the world. Census figures say that about five million people live and work within the sector with jobs ranging from administration to clerical to maintenance.\n\nThe size will soon become apparent as you will see the many residential areas that dot the landscape. Each has its own name, but largely these dwellings are insignificant.\n\nThe Imperial Sector is also the largest consumers of resources. The upper class residents here tend to be the wealthiest in the world. The chief product of the Imperial Sector is policy, and little else also making it the most dependent.\n\nWelcome to the heart of the Empire!", eDialogPic.CREATURE, 130, ["OK"])

def SoutheasternAizic_2603_MapTrigger_15_10(p):
    ChoiceBox("You come to the town of Andron to find it in ruins. The entire place looks like it suffered some massive pillaging. For the most part, the town is abandoned except for a few soldiers who are stationed here.\n\nThere is some rebuilding being done, but it is very slow. This is probably due to the frequent raids by the Troglodytes. The one building that has been completely rebuilt is the barracks. You decide to pay a visit.\n\nSeveral soldiers are resting in beds and others are playing dice at a table. Suddenly, a burly soldier welcomes you. \"Good day! I\'m Bladesman Simmons. You look like you are lost or something.\" You explain you are just on patrol.\n\nHe nods. \"Well, as you can see Andron has suffered greatly from the Troglodytes. We were holding them off pretty good until they figured out that damned teleportation! Just a few weeks ago, they started teleporting troops inside the town!\n\nThis really made the situation difficult. I went to speak with Dervish Montcalm of Fort Reflection about having an anti-teleportation shield put into place and he agreed. Unfortunately, the day before it was installed, they did another attack.\n\nUsually they would only teleport in four or five and we could deal with them easily. This time, they sent in close to twenty and we were totally unprepared! They managed to pillage the town, many of the townspeople perished in the assault.\"", eDialogPic.TERRAIN, 189, ["OK"])
    ChoiceBox("\"We were able to get everything under control, but the town was a total loss. We had the remaining civilians take refuge in the other towns. We stayed behind as a post to help keep the Troglos in back in the hills.\n\nFor the most part, we have been successful at that. However, about once every few days we get an assault of twenty or so. We usually manage to hold them off without too many casualties.\n\nFortunately, Fort Reflection has adequately supplemented our forces to the point where we can defend this place. I just hope this conflict can be resolved soon. My men really need a vacation from this fighting.\"", eDialogPic.CREATURE, 15, ["OK"])
    p.CancelAction = True

def SoutheasternAizic_2604_MapTrigger_9_37(p):
    result = ChoiceBox("You have come to a peaceful hut up in the Troglodyte occupied Mandahl Mountains. The outside has a nicely tended garden of all sorts of plants. You hear the sounds of birds chirping.\n\nIt seems the fighting has decided to leave this place alone. Care to see if anyone is home?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        result = ChoiceBox("You open the door and are faced with a Troglodyte Khazi. Due to previous experience you reach for your weapons. The Khazi replies in a raspy voice, \"No, no, that won\'t be necessary. I mean you know harm, unless you mean me harm.\"\n\nYou decide to put away your weapons. \"Now that\'s much better. I am named Ghorzika and you have come to my home out here in the mountains. I prefer to stay away from all the fighting of my people. I do not by all that hate talk by the rulers.\n\nI\'ve always considered fighting to be a crude thing. I believe that there are better ways to solve the differences with the Empire. Even Vulcaroc, Nycraogos, and Octavus would agree, but all they really want is power.\n\nThat and they follow that risen dead Halloth like he is some kind of god or something. Anyway, do you have any news about the world. I don\'t hear much up here. I just make potions in my spare time.\"\n\nYou tell her of your adventures, she seems amused. \"It\'s been so nice to have visitors. The only visitors I get are other Troglodytes and they tell me news about the war, not that I really care all that much.\n\nI usually sell them potions and with the money I go deeper into the lands to buy up supplies. I guess I should make the same offer to you. Reasonable prices here, of course!\"", eDialogPic.CREATURE, 115, ["Leave", "Buy"])
        if result == 1:
            OpenShop("Shop_Items_Outside_26_1_3")
            p.CancelAction = True
            return
        p.CancelAction = True
        return
    p.CancelAction = True

def SoutheasternAizic_2605_WanderingOnMeet0(p):
    MessageBox("You have heard this area is home to many renegade Troglodytes and is the \'front line\' of their assaults. These rumors are confirmed as you have just encountered a hostile Troglodyte patrol.")

def SoutheasternAizic_2608_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
