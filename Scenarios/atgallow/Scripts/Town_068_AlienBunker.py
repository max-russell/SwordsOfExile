def Generate_Wandering_68_AlienBunker(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["Vahnavoi_71"]])
            npcs.append([1,NPCRecord.List["Hraithe_70"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["Vahnavoi_71"]])
            npcs.append([1,NPCRecord.List["Hraithe_70"]])
        elif r1 == 2:
            npcs.append([1,NPCRecord.List["Vahnavoi_71"]])
            npcs.append([1,NPCRecord.List["Hraithe_70"]])
        elif r1 == 3:
            npcs.append([1,NPCRecord.List["Vahnavoi_71"]])
            npcs.append([1,NPCRecord.List["Hraithe_70"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(32,52)
                elif r2 == 1: l = Location(49,9)
                elif r2 == 2: l = Location(13,34)
                elif r2 == 3: l = Location(32,34)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def AlienBunker_1690_MapTrigger_9_28(p):
    if StuffDone["61_4"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A powerful field obstructs this passage. Your muscles simply refuse to move against it. You will not be able to proceed this way.")
        return

def AlienBunker_1693_MapTrigger_32_22(p):
    if StuffDone["61_5"] == 0:
        if Party.CountItemClass(49, False) > 0:
            result = ChoiceBox("This obelisk appears to be some sort of projection device. You notice there is an empty alcove at the tip. You may wish to insert an object in there.\n\nYou check your inventory and find that one of your crystals will fit nicely into the slot.", eDialogPic.TERRAIN, 184, ["Leave", "Insert"])
            if result == 1:
                MessageBox("You place the crystal in the alcove. Nothing appears to happen. Perhaps you should turn the machine on.")
                StuffDone["61_5"] = 3
                if Party.CountItemClass(49, True) > 0:
                    return
                return
            return
        if Party.CountItemClass(50, False) > 0:
            result = ChoiceBox("This obelisk appears to be some sort of projection device. You notice there is an empty alcove at the tip. You may wish to insert an object in there.\n\nYou check your inventory and find that one of your crystals will fit nicely into the slot.", eDialogPic.TERRAIN, 184, ["Leave", "Insert"])
            if result == 1:
                MessageBox("You place the crystal in the alcove. Nothing appears to happen. Perhaps you should turn the machine on.")
                StuffDone["61_5"] = 1
                if Party.CountItemClass(50, True) > 0:
                    return
                return
            return
        if Party.CountItemClass(48, False) > 0:
            result = ChoiceBox("This obelisk appears to be some sort of projection device. You notice there is an empty alcove at the tip. You may wish to insert an object in there.\n\nYou check your inventory and find that one of your crystals will fit nicely into the slot.", eDialogPic.TERRAIN, 184, ["Leave", "Insert"])
            if result == 1:
                MessageBox("You place the crystal in the alcove. Nothing appears to happen. Perhaps you should turn the machine on.")
                StuffDone["61_5"] = 2
                if Party.CountItemClass(48, True) > 0:
                    return
                return
            return
        MessageBox("This obelisk appears to be some sort of projection device. You notice there is an empty alcove at the tip. You may wish to insert an object in there.")
        return
    result = ChoiceBox("The crystal remains positioned in the alcove where you left it. If you wanted to try a different crystal, you will have to remove this one first.", eDialogPic.TERRAIN, 184, ["Leave", "Remove"])
    if result == 1:
        if StuffDone["61_5"] >= 3:
            Party.GiveNewItem("Crystal_395")
            StuffDone["61_5"] = 0
            return
        if StuffDone["61_5"] < 2:
            Party.GiveNewItem("Crystal_396")
            StuffDone["61_5"] = 0
            return
        Party.GiveNewItem("CrackedCrystal_241")
        StuffDone["61_5"] = 0
        return

def AlienBunker_1694_MapTrigger_32_24(p):
    if ChoiceBox("There is a large button here, waiting to be pressed. Do you?", eDialogPic.STANDARD, 11, ["Yes", "No"]) == 0:
        if StuffDone["61_5"] >= 2:
            if StuffDone["61_5"] < 3:
                MessageBox("You push the button. The obelisk glows and the lights dim. The crystal you inserted into the obelisk becomes very bright. However, nothing else seems to happen. After about ten seconds, the lights return.")
                return
            ChoiceBox("You push the button. The obelisk glows and the lights dim. The crystal you inserted into the obelisk becomes very bright. Small beams shoot out at the runes and an balls of light appear over the runes.\n\nThe balls are made of three different colors: red, green, and blue. From left to right they are: blue, red, green, red, green. After about thirty seconds, the balls of light vanish and the room becomes light again.", eDialogPic.TERRAIN, 170, ["OK"])
            return
        if StuffDone["61_5"] < 1:
            MessageBox("You press the button. The obelisk glows slightly and the lights dim. After about ten seconds, everything returns to normal. You are unsure if anything useful has occurred.")
            return
        ChoiceBox("You push the button. The obelisk glows and the lights dim. The crystal you inserted into the obelisk becomes very bright. Small beams shoot out at the runes and an image forms overhead.\n\nYou see a silent projection of a wild landscape filled with lush forests, clean mountains, and beautiful streams. The image pans on several primitive civilizations of both Humans and Nephilim.\n\nYou watch the scenes for several minutes. There is very little action, but more and more of the same. Eventually, the image dissipates and the room returns to its previous condition.", eDialogPic.STANDARD, 28, ["OK"])
        return

def AlienBunker_1695_MapTrigger_57_4(p):
    Party.HealAll(5)
    if StuffDone["61_6"] == 250:
        return
    StuffDone["61_6"] = 250
    MessageBox("Stepping on this rune has beneficial effects on your health. It seems to radiate energy which replenishes your body.")

def AlienBunker_1696_MapTrigger_8_41(p):
    if StuffDone["62_0"] >= 2:
        result = ChoiceBox("This crystal is glowing an unusually bright green. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from green to blue.")
            StuffDone["62_0"] = 0
            return
        return
    if StuffDone["62_0"] < 1:
        result = ChoiceBox("This crystal is glowing an unusually bright blue. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from blue to red.")
            StuffDone["62_0"] = 1
            return
        return
    result = ChoiceBox("This crystal is glowing an unusually bright red. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
    if result == 1:
        MessageBox("You touch the crystal and it changes from red to green.")
        StuffDone["62_0"] = 2
        return

def AlienBunker_1697_MapTrigger_13_22(p):
    if StuffDone["62_1"] >= 2:
        result = ChoiceBox("This crystal is glowing an unusually bright green. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from green to blue.")
            StuffDone["62_1"] = 0
            return
        return
    if StuffDone["62_1"] < 1:
        result = ChoiceBox("This crystal is glowing an unusually bright blue. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from blue to red.")
            StuffDone["62_1"] = 1
            return
        return
    result = ChoiceBox("This crystal is glowing an unusually bright red. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
    if result == 1:
        MessageBox("You touch the crystal and it changes from red to green.")
        StuffDone["62_1"] = 2
        return

def AlienBunker_1698_MapTrigger_32_3(p):
    if StuffDone["62_2"] >= 2:
        result = ChoiceBox("This crystal is glowing an unusually bright green. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from green to blue.")
            StuffDone["62_2"] = 0
            return
        return
    if StuffDone["62_2"] < 1:
        result = ChoiceBox("This crystal is glowing an unusually bright blue. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from blue to red.")
            StuffDone["62_2"] = 1
            return
        return
    result = ChoiceBox("This crystal is glowing an unusually bright red. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
    if result == 1:
        MessageBox("You touch the crystal and it changes from red to green.")
        StuffDone["62_2"] = 2
        return

def AlienBunker_1699_MapTrigger_52_17(p):
    if StuffDone["62_3"] >= 2:
        if StuffDone["62_3"] == 250:
            return
        result = ChoiceBox("This crystal is glowing an unusually bright green. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            StuffDone["62_3"] = 250
            TownMap.List["AlienBunker_68"].DeactivateTrigger(Location(52,17))
            MessageBox("You touch the crystal and it changes from green to blue.")
            StuffDone["62_3"] = 0
            return
        return
    if StuffDone["62_3"] < 1:
        result = ChoiceBox("This crystal is glowing an unusually bright blue. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from blue to red.")
            StuffDone["62_3"] = 1
            return
        return
    result = ChoiceBox("This crystal is glowing an unusually bright red. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
    if result == 1:
        MessageBox("You touch the crystal and it changes from red to green.")
        StuffDone["62_3"] = 2
        return

def AlienBunker_1700_MapTrigger_54_42(p):
    if StuffDone["62_4"] >= 2:
        result = ChoiceBox("This crystal is glowing an unusually bright green. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from green to blue.")
            StuffDone["62_4"] = 0
            return
        return
    if StuffDone["62_4"] < 1:
        result = ChoiceBox("This crystal is glowing an unusually bright blue. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            MessageBox("You touch the crystal and it changes from blue to red.")
            StuffDone["62_4"] = 1
            return
        return
    result = ChoiceBox("This crystal is glowing an unusually bright red. You get the sudden urge to touch this crystal.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
    if result == 1:
        MessageBox("You touch the crystal and it changes from red to green.")
        StuffDone["62_4"] = 2
        return

def AlienBunker_1701_MapTrigger_31_39(p):
    if StuffDone["61_4"] == 0:
        result = ChoiceBox("You sit before this crystal and stare into it. It seems these are the controls to the ancient chambers. You can control an assortment of functions, most utterly meaningless to you.\n\nHowever, the controls do allow you to access the forcefields which are currently active. You could touch the crystal to disable them.", eDialogPic.TERRAIN, 168, ["Leave", "Touch"])
        if result == 1:
            if StuffDone["62_0"] == 0:
                if StuffDone["62_1"] == 1:
                    if StuffDone["62_2"] == 2:
                        if StuffDone["62_3"] == 1:
                            if StuffDone["62_4"] == 2:
                                MessageBox("You use the controls to turn off the forcefields. You will now be able to access previously obstructed areas.")
                                StuffDone["61_4"] = 1
                                return
                            MessageBox("You touch the crystal expecting the status of the forcefields to change. Unfortunately they are still active. The crystal indicates that the \'security color sequence is incorrect\'. You will need to remedy this to deactivate the forcefields.")
                            return
                        MessageBox("You touch the crystal expecting the status of the forcefields to change. Unfortunately they are still active. The crystal indicates that the \'security color sequence is incorrect\'. You will need to remedy this to deactivate the forcefields.")
                        return
                    MessageBox("You touch the crystal expecting the status of the forcefields to change. Unfortunately they are still active. The crystal indicates that the \'security color sequence is incorrect\'. You will need to remedy this to deactivate the forcefields.")
                    return
                MessageBox("You touch the crystal expecting the status of the forcefields to change. Unfortunately they are still active. The crystal indicates that the \'security color sequence is incorrect\'. You will need to remedy this to deactivate the forcefields.")
                return
            MessageBox("You touch the crystal expecting the status of the forcefields to change. Unfortunately they are still active. The crystal indicates that the \'security color sequence is incorrect\'. You will need to remedy this to deactivate the forcefields.")
            return
        return
    MessageBox("You sit before this crystal and stare into it. It seems these are the controls to the ancient chambers. You can control an assortment of functions, most utterly meaningless to you.")

def AlienBunker_1702_MapTrigger_33_39(p):
    MessageBox("You sit before this crystal and stare into it. It seems these are the controls to the ancient chambers. You can control an assortment of functions, most utterly meaningless to you.")

def AlienBunker_1703_MapTrigger_4_21(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(4,20)).Num == 169:
        if SpecialItem.PartyHas("BlessedAtheme"):
            MessageBox("The Blessed Atheme cuts right through the waxy magic seal like a knife cutting through butter. As soon as you make the first slice, the entire seal begins to melt away. You may now proceed.")
            for x in range(4, 6):
                for y in range(20, 21):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[224])
            return
        ChoiceBox("You encounter a strange kind of barrier you have never seen before. Although it is clearly a magical construct, it is not made from magical energy. This barrier has a material, and wax-like form.\n\nThe wax looks very easy to slice through, but your weapons just slide right off and your spells are deflected. No matter how hard you try, you cannot slice through this barrier.\n\nPerhaps you should consult an expert in these matters.", eDialogPic.TERRAIN, 231, ["OK"])
        StuffDone["54_2"] = 1
        return

def AlienBunker_1705_MapTrigger_3_14(p):
    ChoiceBox("You have discovered another one of those machines that Altrus constructed. It looks very similar to the one you found back at Morbane\'s Crypt. You touch the crystal, hoping to learn a little bit more.\n\nThis time you are more prepared for the mental rush. You see many of the same references to Dark Metal, mentions about energy nodes, and an assortment of other alien terms.\n\nFinally, you must withdraw. You pull away none the smarter. It looks like this lead has ended cold so far. However, there may be other information lying around.", eDialogPic.STANDARD, 1026, ["OK"])

def AlienBunker_1707_MapTrigger_4_4(p):
    if StuffDone["61_7"] == 0:
        StuffDone["61_7"] = 1
        ChoiceBox("This crystal flickers differently than the other crystals you have seen. It is almost as if it is somewhat alive. As you try nearer, you can feel it touch you psychically. Then it begins to speak.\n\n\"I detect you wondering what I am. First I shall tell you I am not a crystal soul, I am merely an animated crystal created to perform designated tasks. What tasks you ask? I am the recorder of information here.\"\n\nWhat luck! This crystal may have some information. You ask it about the crystal machine. \"Indeed, I know of these machines and the one who constructed them.\" You ask to tell all that you know.\n\n\"I am sorry, but he has commanded me not to tell anyone about matters pertaining to the crystal machine.\" You ask again and he repeats the same response. Once more you ask in an interrogating voice.\n\n\"I wish to obey, but I have previously been ordered...\" You tell it to disregard those orders and divulge the location of Altrus\' base. \"I cannot tell you.\" The flickers of light are becoming more and more chaotic, it may be working.\n\nYou press further as the flickers grow even more random and violent. \"I cannot obey. My orders...I must obey, but who? Cannot handle this! The base is...at...the...gallows...\" The crystal grows dark forever. You have overloaded it.", eDialogPic.TERRAIN, 168, ["OK"])
        return

def AlienBunker_1708_MapTrigger_4_8(p):
    if StuffDone["61_7"] == 1:
        if StuffDone["61_8"] == 250:
            return
        StuffDone["61_8"] = 250
        ChoiceBox("You consider the information you have just learned. Unfortunately, you were not able to get too much. The only thing was a simple phrase, \"At the Gallows.\" You have no idea what this means.\n\nCould Gallows be a place? Is it literally referring to a gallows? Is Altrus literally facing execution? Right now more questions have been raised than answered. However, this one clue may provide a lead to Altrus.\n\nYou should definitely report this to the Prime Director.", eDialogPic.STANDARD, 1028, ["OK"])
        StuffDone["100_0"] = 8
        StuffDone["100_1"] = 1
        Animation_Hold(-1, 053_magic3)
        Wait()
        ChoiceBox("CHAPTER VIII -- AT THE GALLOWS", eDialogPic.STANDARD, 1024, ["OK"])
        return

def AlienBunker_1709_MapTrigger_20_40(p):
    ChoiceBox("This crystal is a kind of alien spell book. The concepts of the powerful alien magic are a bit beyond you. However, there is one simpler ritual that you successfully learn. It is called \'Capture Soul\'.\n\nThis spell will allow the user to capture the essence of a creature inside a device called a \'Soul Crystal\' which can later be summoned by the spell called \'Simulacrum\'\n\nUnfortunately, the reference makes no indication of where you might find either of the two.", eDialogPic.TERRAIN, 168, ["OK"])
    StuffDone["121_0"] = 1
    if SpecialItem.PartyHas("SoulCrystal"):
        for pc in Party.EachAlivePC():
            pc.LearnSpell("m_capture_soul")
        return

def AlienBunker_1710_MapTrigger_22_40(p):
    MessageBox("This crystal is a kind of alien spell book. The concepts of the powerful alien magic are a bit beyond you. You doubt any level of normal magical learning will allow you to comprehend these alien concepts.")

def AlienBunker_1711_TownTimer_0(p):
    itemthere = False
    if Game.Mode != eMode.OUTSIDE:
        for n in range(Town.ItemList.Count - 1, -1, -1):
            i = Town.ItemList[n]
            if i.Pos == Location(57,4) and i.SpecialClass == 48:
                Town.ItemList.Remove(i)
                itemthere = True
                break
    if itemthere == True:
        Town.PlaceItem(Item.List["Crystal_395"].Copy(), Location(57,4))
        return
