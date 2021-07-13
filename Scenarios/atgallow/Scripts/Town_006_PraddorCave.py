
def PraddorCave_56_MapTrigger_25_36(p):
    if StuffDone["1_1"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return;
        Animation_Hold(-1, 028_waterfall)
        Wait()
        if StuffDone["1_2"] == 0:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(48,28))
            p.CancelAction = True
            ChoiceBox("You had noticed the floor ahead looked a little suspicious. As soon as you step on it, the floor slides away revealing a trap door! You slide down several meters until you splash into icy cold, rapidly moving water.\n\nThe current sweeps you down as you struggle to get to shore. You get lucky and manage to grab ahold of a rock and pull each other to shore before you are all swept away. It\'s a near miracle that you all got out of that one alive!\n\nYou start to dry yourselves as you notice the shore is overgrown with fungus! Could this be the mold colony you\'re looking for? Suddenly, you hear some noises. You notice some of the fungi start moving toward you.", eDialogPic.TERRAIN, 244, ["OK"])
            StuffDone["1_2"] = 1
            return
        MessageBox("It looks like this trap is still active! You slide down into the fast moving current. However, this time you aren\'t so lucky and cannot get ahold of the rocks and are swept away!\n\nThe river carries you off into some rocky rapids. Your bodies are battered against them. None of you come out alive.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def PraddorCave_58_MapTrigger_48_30(p):
    if SpecialItem.PartyHas("BarrelofExplosives"):
        MessageBox("There is nowhere you can place the Barrel of Explosives here to knock down the wall. If you try, you will just get them wet, rendering them useless. You will have to find another spot.")
        return
    MessageBox("This is an interesting setup. Someone has built a large basalt wall to stop the water flow and divert it all into the passage flowing east. You wonder why it was built and what is behind this wall.")

def PraddorCave_59_MapTrigger_38_13(p):
    result = ChoiceBox("This moldy stairway leads up. You notice this passage is quite unstable, but it should be safe. The lack of footprints in the mold reveals that nobody has been down here for a while. Going up?", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(32,22))
        p.CancelAction = True
        return

def PraddorCave_60_MapTrigger_29_17(p):
    ChoiceBox("This desk is extremely cluttered. You don\'t know how its owner can locate anything. You search it for anything of use. Searching through a stack of papers, you discover an interesting memo dated last week.\n\n\"Zaine -- The mold spores will reach maturity in about a month. Afterward, we can unleash them into Lake Praddor where they will proliferate and wipe out a great portion of the crops by the next harvest.\n\nIt is important we do not unleash them too soon, for before maturity, the mold cannot handle the water and would perish. Thus, making our efforts a failure. -- Armedus.\"\n\nYou know that the mold colony is not yet ready to be released into the water systems of Agran yet. Now if only you could think of some way to use this to your advantage.", eDialogPic.STANDARD, 20, ["OK"])
    StuffDone["1_3"] = 1
    if StuffDone["1_3"] == 1:
        if StuffDone["1_4"] == 1:
            StuffDone["1_5"] = 1
            ChoiceBox("You ponder for a moment and get an idea. If you could somehow bring down the wall in the mold cavern, you could wash away the mold before it was ready, thus killing it. The question is how.", eDialogPic.STANDARD, 7, ["OK"])
            return
        return

def PraddorCave_61_MapTrigger_50_34(p):
    if StuffDone["1_5"] >= 2:
        MessageBox("The Barrel of Explosives could go off at any minute. You better hurry as you may not have much time to get to safety!")
        return
    if SpecialItem.PartyHas("BarrelofExplosives"):
        result = ChoiceBox("With your Barrel of Explosives in hand, you return to the wall. All you have to do is light the fuse and run! You\'re not sure how much time you exactly have, but it probably is not too long. Place the barrel?", eDialogPic.STANDARD, 6, ["No", "Yes"])
        if result == 0:
            return
        elif result == 1:
            SpecialItem.Take("BarrelofExplosives")
            StuffDone["1_5"] = 2
            MessageBox("You place the barrel and light the fuse. Suddenly, you hear several footsteps and shouts! The cultists have amassed a counterattack against you at the exact wrong moment.\n\nIt is too late to stop the barrel. You must hurry and get to the stairway before the barrel explodes!")
            Town.PlaceEncounterGroup(1)
            Timer(Town, 70, False, "PraddorCave_74_TownTimer_44", eTimerType.DELETE)
            return
        return
    ChoiceBox("You have reached the other side of the mysterious wall you saw in the northern fungal cave. For some reason, the cultists must have built this to halt the water flow to their mold colony.\n\nYou wonder why it was constructed and if you can use this to your advantage. If only you knew more about how to destroy the mold.", eDialogPic.TERRAIN, 100, ["OK"])
    StuffDone["1_4"] = 1
    if StuffDone["1_3"] == 1:
        if StuffDone["1_4"] == 1:
            StuffDone["1_5"] = 1
            ChoiceBox("You ponder for a moment and get an idea. If you could somehow bring down the wall in the mold cavern, you could wash away the mold before it was ready, thus killing it. The question is how.", eDialogPic.STANDARD, 7, ["OK"])
            return
        return

def PraddorCave_62_MapTrigger_40_34(p):
    if StuffDone["1_5"] == 1:
        if SpecialItem.PartyHas("BarrelofExplosives"):
            return
        result = ChoiceBox("This storeroom has several barrels labeled \'Explosives\' inside. These are typical of those used to hollow out mine shafts. Perhaps you could use this to bring down the wall north of the mold colony.\n\nIt would be heavy and bulky, but you could manage to carry it.", eDialogPic.STANDARD, 25, ["Leave", "Take"])
        if result == 1:
            SpecialItem.Give("BarrelofExplosives")
            return
        return
    MessageBox("This is a storage room for tools. You notice several barrels in the corner marked \'Explosives\'. These are typical of the types used to hollow out mine shafts.")

def PraddorCave_63_MapTrigger_39_45(p):
    result = ChoiceBox("This stairway leads up.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
    if result == 1:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(9,46))
        p.CancelAction = True
        if StuffDone["1_5"] == 2:
            StuffDone["0_2"] = 6
            Animation_Hold(-1, 005_explosion)
            Wait()
            Animation_Hold(-1, 028_waterfall)
            Wait()
            ChoiceBox("Just as you reach the top of the stairs, the explosives set off. You hear the sudden rush of water and the screams of the cultists swept away in the current. You feel kind of remorseful of the way they went.\n\nYou pause for a moment to reflect. You have saved the crops of the Agran Sector and probably many lives of the Empire that would have starved without them. Also, Bladesman Kelli promised you a promotion.\n\nHowever, you have to wonder, whatever happened to Zaine? Did the mighty prophet abandon his fanatics or is he waiting for vengeance? That is something you may never find out.", eDialogPic.STANDARD, 25, ["OK"])
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            return
        return

def PraddorCave_65_MapTrigger_8_47(p):
    if StuffDone["1_5"] < 2:
        result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
        if result == 1:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(39,46))
            p.CancelAction = True
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Below is the lab and the mold cavern. All of which are submerged in water. You can\'t go here now.")

def PraddorCave_67_MapTrigger_33_22(p):
    if StuffDone["1_5"] < 2:
        result = ChoiceBox("This stairway leads down.", eDialogPic.STANDARD, 19, ["Leave", "Climb"])
        if result == 1:
            if Game.Mode == eMode.COMBAT:
                p.CancelAction = True
                return
            Party.Reposition(Location(39,13))
            p.CancelAction = True
            return
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("This passageway was not stable to begin with. The recent explosion you set off has collapsed this passage. It is impossible to get back down.")

def PraddorCave_68_MapTrigger_13_41(p):
    if StuffDone["1_5"] == 2:
        if StuffDone["1_6"] == 0:
            StuffDone["1_6"] = 1
            Town.PlaceEncounterGroup(3)
            Animation_Explosion(Location(16,41), 0, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("Your questions are soon answered. You confront an angry looking Zaine. \"Well, it appears you have defeated us. No matter, the great Morbane has much more in store for your Empire. It is only a minor defeat to us.\"\n\nZaine makes a hand motion and a massive hulking Golem steps forward! \"I was away building this. It appears I had arrived too late to stop you with my new weapon. Nevertheless, it may still be of some use. Golem, attack!!\"\n\nThe Golem moves forward to crush you. Meanwhile, Zaine vanishes in a puff of smoke leaving you to fight his Golem.", eDialogPic.CREATURE, 26, ["OK"])
            Town.PlaceEncounterGroup(2)
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Zaine_208": Town.NPCList.Remove(npc)
            Animation_Explosion(Location(16,41), 0, "005_explosion")
            Animation_Hold()
            Wait()
            return
        return

def PraddorCave_71_MapTrigger_29_36(p):
    if ChoiceBox("There is a stout wooden lever protruding from the ground here. Pull it?", eDialogPic.STANDARD, 9, ["Yes", "No"]) == 0:
        t = Town.TerrainAt(p.Target).TransformTo
        Town.AlterTerrain(p.Target, 0, t)
        MessageBox("You hear a small click. You don\'t know if anything significant happened or not.")
        if StuffDone["1_1"] == 0: StuffDone["1_1"] = 1
        else: StuffDone["1_1"] = 0
        return

def PraddorCave_72_MapTrigger_41_50(p):
    if Game.Mode == eMode.COMBAT:
        return;
    ChoiceBox("This is a very ancient book describing the creation of the \'Lotus Mold\' which is very prolific and extremely destructive to many kinds of plants. You can bet this is the crop destroying mold.\n\nThe methods are extremely complex involving ingredients that you had not even heard of. Their product is very exotic. Should they succeed in releasing it, the Empire would have a difficult time fixing the problem.\n\nYou wonder where the cultists got their hands on such an ancient and powerful alchemetical resource.", eDialogPic.STANDARD, 24, ["OK"])

def PraddorCave_73_MapTrigger_6_33(p):
    result = ChoiceBox("This is a large and hidden book of arcane prayers. Perhaps you could learn useful magics from this text.", eDialogPic.STANDARD, 24, ["Leave", "Read"])
    if result == 1:
        if Party.GetSkillTotal(eSkill.MAGE_LORE) > 8:
            MessageBox("This book is reveals the secrets of many dark prayers and sacrificial rituals. The rituals are not too difficult to comprehend, but are of little or no use to you.\n\nThere is one healing ritual involving curing your party of poison. You learn the prayer \'Cure Poison\'.")
            for pc in Party.EachAlivePC():
                pc.LearnSpell("p_cure_all_poison")
            return
        MessageBox("This book is reveals the secrets of many dark prayers and sacrificial rituals. The rituals are not too difficult to comprehend, but are of little or no use to you.\n\nThere are a few rituals that sound somewhat useful, but they are slightly beyond your level. You will need more \'Mage Lore\'.")
        return

def PraddorCave_74_TownTimer_44(p):
    if StuffDone["0_2"] < 6:
        Animation_Hold(-1, 005_explosion)
        Wait()
        Animation_Hold(-1, 028_waterfall)
        Wait()
        MessageBox("It appears you were a bit too slow in getting to the stairwell. The barrel explodes and water instantly rushes in sweeping everybody and everything away. You quickly drown. At least you saved the crops!")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def PraddorCave_75_OnEntry(p):
    if not Town.Abandoned:
        if StuffDone["0_2"] >= 6:
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if  npc.IsABaddie: Town.NPCList.Remove(npc)
            return

def PraddorCave_76_CreatureDeath4(p):
    ChoiceBox("After several mighty strikes, the Golem falls to the floor and shatters into three pieces. The living stone ceases its movement. You have beaten Zaine\'s Golem!\n\nUnfortunately, Zaine escaped. There is little doubt that he will continue to be a menace to the Empire. You can only wonder what he is planning next. Oh well, that is not your concern.\n\nYou have done a great deed for the Empire today. You have pretty much wiped out the \'Followers\' and they will threaten the Agran Sector no more. You will undoubted receive your well deserved promotions for this.", eDialogPic.CREATURE, 119, ["OK"])
