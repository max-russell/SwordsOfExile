
def StalkersFortress_286_MapTrigger_7_51(p):
    if StuffDone["18_0"] == 250:
        return
    StuffDone["18_0"] = 250
    TownMap.List["StalkersFortress_18"].DeactivateTrigger(Location(7,51))
    TownMap.List["StalkersFortress_18"].DeactivateTrigger(Location(7,52))
    ChoiceBox("You step inside Stalker\'s Fortress. It\'s not so much a castle as a warren, one incredibly well guarded gate, followed by a long, natural gallery with buildings burrowed into the wall along it.\n\nThe guards are a motley bunch, wearing a wide variety of armor (some stolen from Empire troops), and wielding all manner of wicked blades, pole arms, and spiked clubs. They watch you with profound mistrust, but at least these guards don\'t attack you.\n\nAs you enter, one of the guards says \"Stalker wants to see you. He\'s to the north. Go see him. Don\'t go anywhere else. You aren\'t allowed.\" The other guards nod at the last bit. Friendly lot.", eDialogPic.CREATURE, 13, ["OK"])

def StalkersFortress_288_MapTrigger_40_34(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You walk in on several wizards, performing delicate and dangerous experiments on explosive materials. When they see you, they stop what they\'re doing long enough to call for guards. They come and pull you away, telling you not to come back.")

def StalkersFortress_291_MapTrigger_49_59(p):
    MessageBox("These are the doors to the fortresses interrogation chambers. Behind the doors, you can dimly hear the sounds of people in pain.\n\nFortunately, the doors are massive and heavily locked, so you\'re unable to go in there and see what\'s going on. It\'ll do a lot for your peace of mind.")

def StalkersFortress_295_MapTrigger_25_12(p):
    if StuffDone["20_0"] >= 1:
        if StuffDone["18_5"] == 250:
            return
        StuffDone["18_5"] = 250
        ChoiceBox("You return to Stalker\'s throne room in triumph, having managed to miraculously slay his greatest enemy. You walk in proudly, eager to bask in admiration and adulation.\n\nYou are disappointed. For some reason, despite what you have done, the guards barely seem to even notice you. The rebel warriors seem to be taking great care not to admire your deed. Stalker seems to be, if anything, displeased to see you.\n\nThis was unexpected. Looking into the rebel leader\'s eyes, you would swear you see envy and fear. It\'s as if he is afraid that you will take his place. This is going to be awkward.", eDialogPic.CREATURE, 1024, ["OK"])
        return
    if StuffDone["18_1"] == 250:
        return
    StuffDone["18_1"] = 250
    ChoiceBox("You enter Stalker\'s throne room. It\'s a massive chamber, clearly built with the intention of impressing all who are brought here, willingly or unwillingly. Huge, granite pillars tower above you on all sides, like a monumental stone forest.\n\nIn the center of the chamber is a massive oak table, fifty feet long, where the leaders of the Hill Runners meet to plan tactics. At the far end sit Stalker and Canizares. They look up from their plans when you enter, and Stalker motions you forward.\n\nAfter hearing so much about him, you find his appearance somehow disappointing. There\'s nothing about his nondescript look and bearing that indicates the ruthlessness and genius that have made him the scourge of the Empire.", eDialogPic.CREATURE, 1024, ["OK"])
    TownMap.List["JaensHeadquarters_20"].Hidden = False

def StalkersFortress_299_MapTrigger_21_2(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 10:
        MessageBox("The rebels have liberated a huge prayer book from the Empire. You spend some time looking at it. Most of the rituals are either uninteresting or already known to you. Fortunately, one spell seems useful.\n\nYou can now cast the spell Major Cleansing.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_major_cleansing")
        return
    MessageBox("The rebels have liberated a huge prayer book from the Empire. You spend some time looking at it. Most of the rituals are either uninteresting or already known to you. Alas, one spell seems useful, but you can\'t quite make sense of it.")

def StalkersFortress_300_MapTrigger_23_2(p):
    if Party.GetSkillTotal(eSkill.MAGE_LORE) > 10:
        MessageBox("The rebels have liberated a huge prayer book from the Empire. You spend some time looking at it. Most of the rituals are either uninteresting or already known to you. Fortunately, one spell seems useful.\n\nYou can now cast the spell Revive All.")
        for pc in Party.EachAlivePC():
            pc.LearnSpell("p_revive_all")
        return
    MessageBox("The rebels have liberated a huge prayer book from the Empire. You spend some time looking at it. Most of the rituals are either uninteresting or already known to you. Alas, one spell seems useful, but you can\'t quite make sense of it.")

def StalkersFortress_301_MapTrigger_18_2(p):
    MessageBox("You step in front of the altar, and feel a pleasant, soothing feeling. You feel much better when you walk away.")
    Party.HealAll(50)

def StalkersFortress_302_MapTrigger_11_2(p):
    if StuffDone["20_0"] >= 1:
        if StuffDone["18_3"] == 250:
            return
        result = ChoiceBox("The box contains a broadsword, a sack of gold, a silver key, and a note: \"Thank you for your assistance. We wish you the best of luck in your further adventures, which, we hope, will take place elsewhere.\"\n\n\"This key will let you down to the docks, where a boat has been left to leave our isle. With our regards. Stalker.\"\n\nYou aren\'t sure why Stalker wants you away from here, but the message is clear. Despite your services, you are no longer welcome. Maybe he\'s afraid you will be more popular than him. No matter. It\'s time to go.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
        if result == 0:
            StuffDone["18_3"] = 250
            SpecialItem.Give("DockKey")
            Party.GiveNewItem("Korthrax_386")
            Party.Gold += 500
        return
        return
    MessageBox("The box is empty.")

def StalkersFortress_303_MapTrigger_5_51(p):
    if StuffDone["18_4"] >= 1:
        MessageBox("The small army outside here has heard of Stalker\'s death and is waiting for revenge. They overpower you effortlessly and inflict unbelievable horrors upon you.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return

def StalkersFortress_305_MapTrigger_9_2(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(8,1)).Num == 128:
        if SpecialItem.PartyHas("DockKey"):
            MessageBox("You find the door to the docks. It was locked, but your silver key fits. You may finally be able to escape Morrow\'s Isle.")
            Town.AlterTerrain(Location(8,1), 0, TerrainRecord.UnderlayList[125])
            return
        MessageBox("This door leads to the docks behind Stalker\'s fortress. Unfortunately, the door is locked, and you don\'t have the key. Pity ... this dock may be your only route off this island.")
        return

def StalkersFortress_306_MapTrigger_7_1(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(8,1)).Num == 128:
        MessageBox("You find that the door has been locked behind you, and your silver key no longer works. You are no longer welcome here.")
        return

def StalkersFortress_307_MapTrigger_7_3(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(26,29)
    Party.MoveToMap(TownMap.List["ConcealedDocks_19"])

def StalkersFortress_308_CreatureDeath47(p):
    MessageBox("You have killed Stalker. He has a silver key around his neck. You grab it. Perhaps you should leave the island. It would appear you\'re out of friends here.")
    SpecialItem.Give("DockKey")
    StuffDone["18_4"] = 1

def StalkersFortress_309_TalkingTrigger8(p):
    if StuffDone["20_0"] == 0:
        ChoiceBox("Stalker leans back and begins to speak, with the tired patience of one used to repeating things again and again, and the confidence of one who knows his words must be obeyed, like it or not.\n\n\"There is only one person on this island who has the skill and strength to defeat me. His name is Jaen.\n\n\"As long as he lives, we will not be able to take Morrow\'s Isle. If we do take the Isle, though, we may be able to hold it against the Empire for years. It is not hard to defend an island.\"\n\n\"We have finally convinced an Empire prisoner to tell us where Jaen is. We have people there. All we need is someone good enough to get in and kill Jaen. That someone will be you.\"\n\n\"To get there, stand just north of the town of Liam, and walk due north. You will be contacted from there. Good luck to you. You will be doing the Hill Runners a great service.\"", eDialogPic.CREATURE, 1024, ["OK"])
        p.TalkingText = "\"Be sure to go get supplies before leaving.\"\n\n\"Of course, you will receive a good reward for completing this mission. And this reward is, alas, one you can\'t live without.\""
        TownMap.List["JaensHeadquarters_20"].Hidden = False
        return
