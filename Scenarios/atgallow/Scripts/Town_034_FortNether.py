
def FortNether_706_MapTrigger_32_31(p):
    result = ChoiceBox("This portal glows ominously. You have no idea where it will take you. Care to find out?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        ChoiceBox("You step into the portal and pulled into a large room. Your attention is immediately drawn to the other end of the room. Dominating this area is a large black circular hole in space.\n\nIt emits a low ominous hum and occasional flashes of electricity spark within. That must be the awesome Nethergate! Beside it stands a malevolent figure in black robes. Although you cannot make out his/her face, you do not believe you\'ve met.\n\nIt is almost as if the Nethergate is beckoning you to come closer.", eDialogPic.STANDARD, 22, ["OK"])
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(31,15)
        Party.MoveToMap(TownMap.List["FortNether_35"])
        return
    p.CancelAction = True

def FortNether_707_MapTrigger_45_54(p):
    if StuffDone["14_6"] == 250:
        return
    StuffDone["14_6"] = 250
    TownMap.List["FortNether_34"].DeactivateTrigger(Location(45,54))
    TownMap.List["FortNether_34"].DeactivateTrigger(Location(45,55))
    TownMap.List["FortNether_34"].DeactivateTrigger(Location(58,50))
    TownMap.List["FortNether_34"].DeactivateTrigger(Location(59,50))
    MessageBox("This pen is filled with those horrible Mutant Giants that you saw being created back on Mount Bleak. You bet they are \"manufacturing\" them here as well.")

def FortNether_711_MapTrigger_18_54(p):
    if StuffDone["14_8"] >= 2:
        Town.AlterTerrain(Location(13,43), 0, TerrainRecord.UnderlayList[84])
        return
    if StuffDone["14_7"] == 250:
        return
    StuffDone["14_7"] = 250
    MessageBox("Just when you thought you were done with Wyverns, you encounter a pen full of them. Several part eaten human bodies are strewn about in the pens. The mages are probably breeding and training them here.")
    Timer(Town, 3, False, "FortNether_741_TownTimer_12", eTimerType.DELETE)

def FortNether_713_MapTrigger_13_50(p):
    if StuffDone["14_8"] == 0:
        Animation_Hold(-1, 005_explosion)
        Wait()
        MessageBox("There is an explosion from behind the wall just to the north. The blast knocks some of the stones away. You wonder what is going on.")
        StuffDone["14_8"] = 1
        return

def FortNether_715_MapTrigger_13_44(p):
    if StuffDone["14_8"] == 1:
        Town.AlterTerrain(Location(13,43), 0, TerrainRecord.UnderlayList[84])
        Animation_Explosion(Location(13,43), 0, "005_explosion")
        Animation_Hold()
        Wait()
        MessageBox("Suddenly another explosion blasts apart a small section of the wall. You are assaulted by a rain of stones. You can now get a glimpse of the room beyond.\n\nInside is a young woman with many tattoos wearing the traditional prisoner uniform of the Empire. She holds a kind of wand. They must be using prisoners for labor and she has just tried to escape!")
        Party.Damage(Maths.Rand(4, 1, 5) + 10, eDamageType.WEAPON)
        Wait()
        StuffDone["14_8"] = 2
        return

def FortNether_716_MapTrigger_2_42(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("The controls operate the nearby portculli.")
        SuspendMapUpdate()
        for x in range(5, 7):
            for y in range(43, 44):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def FortNether_717_MapTrigger_5_23(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["14_9"] == 250:
        return
    StuffDone["14_9"] = 250
    MessageBox("A massive gallery lies before you. All sorts of treasure are scattered about in a seemingly random configuration. Then, several creatures, look like masses of eyes, swoop down from the ceiling to defend their trove.")

def FortNether_719_MapTrigger_10_27(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["15_0"] == 250:
        return
    StuffDone["15_0"] = 250
    MessageBox("This room is unnaturally cool and damp. A quick survey reveals that this is the home of some giant insects. The creatures are about as tall as you and have razor sharp claws. Unfortunately, they look hungry.")

def FortNether_720_MapTrigger_18_17(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["15_1"] == 250:
        return
    StuffDone["15_1"] = 250
    MessageBox("How thoughtful of the creators of this fortress! They have even put in a special yard with green grass and even some flowers. It sure perks up the esthetic value of this grim place.")

def FortNether_722_MapTrigger_36_25(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["15_2"] == 250:
        return
    StuffDone["15_2"] = 250
    ChoiceBox("At first you think this room is filled with humans dressed in gray robes meditating on cots. But then you realize that they are not so. Their faces are a deathly pale greenish gray color and their bodies extremely thin.\n\nUpon your disturbance, all of them rise. They begin to converse in a series of whispers. You cannot make out what they are saying, or even if it is your language. You could swear somebody is peeking inside of your minds.\n\nWhatever they were discussing, you can get a fairly good idea. They all turn to halt your progress through the fortress. True, they look pretty frail, but looks can be deceiving.", eDialogPic.CREATURE, 57, ["OK"])

def FortNether_724_MapTrigger_47_21(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["15_3"] == 250:
        return
    StuffDone["15_3"] = 250
    MessageBox("You encounter another new species. This one is short, under a meter tall. Its skin appears to be like wax. Most interesting is its behavior. The species has been randomly creating narrow corridors to live in.")

def FortNether_726_MapTrigger_50_16(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["15_4"] == 250:
        return
    StuffDone["15_4"] = 250
    MessageBox("And what assortment of bizarre creatures would be complete without some kind of large hulking daemon? Not this one for sure! These denizens look overjoyed at having someone to play with.")

def FortNether_728_MapTrigger_58_12(p):
    if StuffDone["15_5"] == 250:
        return
    StuffDone["15_5"] = 250
    TownMap.List["FortNether_34"].DeactivateTrigger(Location(58,12))
    TownMap.List["FortNether_34"].DeactivateTrigger(Location(59,12))
    MessageBox("This room contains thugs and mutant giants hard at work building what look like huge pens for some kind of creature. You have no idea what it is or even if you want to know of what kind of horrors will occupy those pens.")

def FortNether_730_MapTrigger_61_49(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("The controls operate the nearby portculli.")
        SuspendMapUpdate()
        for x in range(58, 60):
            for y in range(50, 51):
                t = Town.TerrainAt(Location(x,y)).TransformTo
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def FortNether_731_MapTrigger_39_36(p):
    result = ChoiceBox("Some kind of tome has been placed on this pedestal for reading. Care to find out what it\'s about?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        MessageBox("This appears to be some kind of Gloomor holy book. You cannot make out the language or anything else for that matter.")
        return

def FortNether_732_MapTrigger_37_36(p):
    result = ChoiceBox("Some kind of tome has been placed on this pedestal for reading. Care to find out what it\'s about?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("This tome contains information on pentagrams. You decide to read: \"The pentagram is one of the most ancient and powerful runes. Necessary in most important rituals, understanding of the pentagram is integral to spell casting.\n\nThe pentagram is a star drawn like so: [drawing of a star]. As you can see, it has five points. Each point represents a different element which has its own color.\n\nThe top point represents spirit which is white or black and must always face north. Going in clockwise order, the next point is water (blue), fire (red), earth (green or brown), and air (yellow).\"", eDialogPic.TERRAIN, 247, ["OK"])
        return

def FortNether_733_MapTrigger_43_34(p):
    MessageBox("This altar is unusual. It is perfect! It shows no marks of stone use or fire burns. It must have been formed naturally or could have been shaped by the acid of the Gloomor.")

def FortNether_734_MapTrigger_32_21(p):
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for i in Town.EachItemThere(Location(32,15), True):
            if i.SpecialClass == 22:
                itemthere = True
                break
    if itemthere == True:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(34,16), True):
                if i.SpecialClass == 19:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(33,18), True):
                    if i.SpecialClass == 21:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(31,18), True):
                        if i.SpecialClass == 20:
                            itemthere = True
                            break
                if itemthere == True:
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(30,16), True):
                            if i.SpecialClass == 23:
                                itemthere = True
                                break
                    if itemthere == True:
                        MessageBox("It seems you have completed some kind of circuit. The portal at the other end of the room has grown in brightness. It appears you have activated it. Now, do you dare to use it?")
                        StuffDone["15_6"] = 1
                        return
                    return
                return
            return
        return

def FortNether_735_MapTrigger_31_29(p):
    if StuffDone["15_6"] >= 1:
        result = ChoiceBox("This portal glows ominously. You have no idea where it will take you. Care to find out?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            Animation_Hold(-1, 010_teleport)
            Wait()
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(32,33)
            Party.MoveToMap(TownMap.List["FortNether_35"])
            return
        p.CancelAction = True
        return
    MessageBox("This portal is too insubstantial to use. If only you had some way to power it up.")
    p.CancelAction = True

def FortNether_736_MapTrigger_34_22(p):
    result = ChoiceBox("Some kind of tome has been placed on this pedestal for reading. Care to find out what it\'s about?", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("This book is really a journal of all the races summoned to this fortress. Much of it is worthless anatomy, but the introductions to each race are of interest.\n\nGloomors - A strange race of humanoids destroyed during the Empire purges. They have frail bodies, unusually corrosive saliva. They have strong religious ties to their gods and insist on wearing dull gray garments along with other customs.\n\nWyverns - Another extinct race of reptiles. Large, vicious, stealthy, and breathe fire. They lack any real weakness and will provide excellent assistance during invasions. A bit ornery, but not too difficult to train.\n\nMantis - An extremely prolific race of carnivorous insectoids. They are very agile and spit a sticky goo, which slows down prey. Binding of these beasts must be done through magic.\n\nMorplings - A strange race summoned by accident. Have a peculiar habit of building hive like corridors for homes. They are semi intelligent. However, most interesting is their ability to split into separate entities when damaged.\n\nGrawlers - A kind of daemon. Large, nasty, not too bright, and easy to control. Has wickedly sharp claws for goring things. Like many of their kind, they are attracted to fire.", eDialogPic.STANDARD, 24, ["OK"])
        return

def FortNether_737_MapTrigger_51_22(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 15:
        MessageBox("Among the various administrative scrolls, a lone scroll describing a prayer was lost. You manage to recover it and can now cast \'Summon Guardian\'!")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_summon_guardian")
        return
    MessageBox("Among all these administrative records, a scroll teaching a prayer was lost. Well, at least that\'s what you think it is. You will need more Mage Lore to understand it fully.")

def FortNether_738_MapTrigger_25_47(p):
    result = ChoiceBox("This portal glows ominously. You have no idea where it will take you. Care to find out?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        Animation_Hold(-1, 010_teleport)
        Wait()
        if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
            p.CancelAction = True
            return
        Animation_FadeDown()
        Wait()
        Party.Pos = Location(33,22)
        Party.MoveToMap(TownMap.List["FortNether_35"])
        return
    p.CancelAction = True

def FortNether_739_MapTrigger_37_47(p):
    result = ChoiceBox("This portal glows ominously. You have no idea where it will take you. Care to find out?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(25,48))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        return
    p.CancelAction = True

def FortNether_740_MapTrigger_27_46(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        if StuffDone["16_9"] == 0: StuffDone["16_9"] = 1
        else: StuffDone["16_9"] = 0
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(32,38)).Num == 147:
            MessageBox("You pull the lever and the massive portculli on the face of the fortress slide open!")
            SuspendMapUpdate()
            for x in range(31, 34):
                for y in range(38, 39):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("You pull the levers and the portculli slam shut.")
        SuspendMapUpdate()
        for x in range(31, 34):
            for y in range(38, 39):
                t = Town.TerrainAt(Location(x,y))
                t = t.GetLocked()
                Town.AlterTerrain(Location(x,y), 0, t)
        ResumeMapUpdate()
        return

def FortNether_741_TownTimer_12(p):
    Animation_Hold(-1, 005_explosion)
    Wait()
    MessageBox("You hear an explosion coming from the north. You can only guess, but it did not sound like too far away.")

def FortNether_742_OnEntry(p):
    if StuffDone["16_9"] == 0:
        if StuffDone["14_3"] == 250:
            return
        StuffDone["14_3"] = 250
        ChoiceBox("You reach the end of the tunnel and find nothing. Knowing that the entrance to Fort Nether must be here somewhere, you look around. After a short search, you discover a small section of the cliff is an illusion.\n\nYou walk straight through and find yourself in a massive cavernous courtyard. The first thing you notice is the ceiling is covered with some kind of strange fluorescent mold that bathes the cavern in light.\n\nAround you is the foreboding basalt facade of Fort Nether. Your goal lies somewhere within.", eDialogPic.STANDARD, 22, ["OK"])
        return
    SuspendMapUpdate()
    for x in range(31, 34):
        for y in range(38, 39):
            t = Town.TerrainAt(Location(x,y))
            t = t.GetUnlocked()
            Town.AlterTerrain(Location(x,y), 0, t)
    ResumeMapUpdate()

def FortNether_743_CreatureDeath48(p):
    MessageBox("Well, it looks like that escape attempt failed. You look around and you can see the bodies of two guards, horribly burned to death. Anyway, her attempt to get out had the unexpected effect of getting you in!")
