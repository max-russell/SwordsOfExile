
def SouthwesternAizic_2574_MapTrigger_9_41(p):
    MessageBox("This wall is the Mandahl-Aizic border. A small guardpost separates the two sectors. The guards check your papers and promptly let you through.")

def SouthwesternAizic_2575_MapTrigger_10_17(p):
    ChoiceBox("You have arrived at the gates of the Raymond Naval Base in the Aizic Sector. The function of the navy in these times is more for trade than for defense and this base fulfills that purpose well.\n\nThe ships here carry cargo of passengers, minerals, and other assorted goods between Pralgad and Aizo day and night. The goods arrive (and are sent out) by the use of teleporters to (and from) other parts of Pralgad.\n\nIn conclusion, this base serves a major purpose in global commerce.", eDialogPic.STANDARD, 16, ["OK"])
    p.CancelAction = True

def SouthwesternAizic_2576_MapTrigger_32_5(p):
    ChoiceBox("You arrive at the town of Widesprint to find it in ruins. The walls have been scorched by powerful flames and much has been reduced to ash. You walk inside to find the townspeople, accompanied by soldiers, rebuilding.\n\nFrom your conversations with the townspeople and soldiers you get a fairly good account of what happened here.\n\nIn the past year, the Troglodytes in the area have been causing a great deal of trouble. They would perform raids on farms and attack travelers. Occasionally, they would even go so far as to attack major settlements like these.\n\nAbout a month ago, several Troglodyte Khazis (troglo equivalent to wizards) managed to sneak in the town and set off some quickfire. It spread through the town with great speed and did a vast amount of damage.\n\nMuch property was damaged, but only a few lives were lost in the blaze. The Khazis left a message demanding that this area be abandoned and returned to the Troglodytes or further attacks will persist.\n\nYou also learn that the local authorities are frustrated that the Empire only considers the Troglodytes a \"minor threat\" and refuses to send significant aid. Well, the boring times are getting a bit more exciting.", eDialogPic.STANDARD, 1025, ["OK"])
    p.CancelAction = True

def SouthwesternAizic_2580_MapTrigger_30_22(p):
    if StuffDone["42_4"] == 250:
        return
    StuffDone["42_4"] = 250
    WorldMap.DeactivateTrigger(Location(30,166))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("As you make your way through the forest, you stumble onto a fairly large collection of undead! Unfortunately, undead are very prone to hungering for the life force of the living when not under control by a caster.\n\nDetecting your life forces, they stumble toward you hoping to satisfy their hunger for the energy of the living.", eDialogPic.CREATURE, 55, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_3_4", p.Target)

def SouthwesternAizic_2581_MapTrigger_27_24(p):
    MessageBox("At the end of this forest is the site where the bodies of several corpses are stacked. From clues within the ground, you can tell this place was a cemetery at one time or another.")

def SouthwesternAizic_2582_MapTrigger_37_18(p):
    if StuffDone["42_5"] == 250:
        return
    StuffDone["42_5"] = 250
    WorldMap.DeactivateTrigger(Location(37,162))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("As you make your way through the forest, you stumble onto a fairly large collection of undead! Unfortunately, undead are very prone to hungering for the life force of the living when not under control by a caster.\n\nDetecting your life forces, they stumble toward you hoping to satisfy their hunger for the energy of the living.", eDialogPic.CREATURE, 55, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_3_4", p.Target)

def SouthwesternAizic_2583_MapTrigger_22_32(p):
    if StuffDone["42_6"] == 250:
        return
    StuffDone["42_6"] = 250
    WorldMap.DeactivateTrigger(Location(22,176))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("As you make your way through the forest, you stumble onto a fairly large collection of undead! Unfortunately, undead are very prone to hungering for the life force of the living when not under control by a caster.\n\nDetecting your life forces, they stumble toward you hoping to satisfy their hunger for the energy of the living.", eDialogPic.CREATURE, 55, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_3_4", p.Target)

def SouthwesternAizic_2584_MapTrigger_28_21(p):
    if StuffDone["42_7"] == 0:
        result = ChoiceBox("You enter this tower and discover that it is little more than an enclosed circular temple. The walls and floors have strange markings done in blood. They seem to emit a deep red glow. At the center of the temple is a large basalt altar.\n\nUpon the altar rests a skeletal body. Before it is a woman dressed in deep red robes chanting in some bizarre tongue. Suddenly, there is a red flash! The altar, the woman, and the skeleton glow an eerie red.\n\nThen, the skeleton rises from the altar and begins to pace about mindlessly. The woman at the altar notices you, but does nothing. She seems to be awaiting your move.\n\nYou could attack her and this foul army of undead, or you could approach her and see what happens. Of course, you could also leave. It appears all of those options are open to you at the moment.", eDialogPic.CREATURE, 24, ["Leave", "Attack", "Approach"])
        if result == 1:
            Animation_Hold(-1, 046_growl)
            Wait()
            ChoiceBox("You draw your weapons. The woman begins to chant. Instantly, all of the undead line up in a battle formation and await you to make the next move. You charge the undead and they move forward to meet you.\n\nMeanwhile, the evil priest is preparing a nasty spell.", eDialogPic.CREATURE, 24, ["OK"])
            Animation_Hold(-1, 024_priestspell)
            Wait()
            Message("Cult High Priest casts:")
            Message("  Excommunicate")
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.HASTE_SLOW, Maths.MinMax(-8, 8, pc.Status(eAffliction.HASTE_SLOW) - 6))
            for pc in Party.EachAlivePC():
                pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 6))
            StuffDone["42_7"] = 1
            WorldMap.SpawnNPCGroup("Group_0_3_5", p.Target)
            return
        elif result == 2:
            result = ChoiceBox("You approach the priestess. \"Welcome soldiers, I am Vistia high priestess of the goddess of the underworld. You must forgive my accommodations are not as accommodating as one would like, but they will have to do.\"\n\nShe asks about news around the world and you tell her of some of your travels. \"Indeed, you have the makings of being heroes. Perhaps you would like to enter a proposition.\"\n\nShe takes a deep breath and continues, \"Raising undead is often very labor intensive, requiring a great deal of energy. I would be willing to pay you, say 100 gold, for a small portion of your experience.\n\nIt will drain you somewhat, but you will be able to recover. Will you accept these terms?\"", eDialogPic.CREATURE, 24, ["Leave", "Accept"])
            if result == 1:
                Animation_Hold(-1, 024_priestspell)
                Wait()
                for pc in Party.EachAlivePC():
                    pc.AwardXP(-20)
                Animation_Hold(-1, 067_huh)
                Wait()
                MessageBox("The priestess places her hands on your chests. One at time she chants. As she does, you feel a slight pain as the energy is drained from you. After it is over you feel quite weak and dizzy. She hands you a sack of gold coins.")
                Party.Gold += 100
                Animation_Hold(-1, 015_cash)
                Wait()
                return
            MessageBox("You decide to turn her offer down. \"Thank you for visiting. If you are ever low on cash and change your minds, be sure to come back here!\"")
            return
        p.CancelAction = True
        return
    MessageBox("You return to this tower to find it empty. The undead that used to inhabit this place have crumbled to dust, free from their now deceased owner.")

def SouthwesternAizic_2585_MapTrigger_34_44(p):
    if StuffDone["42_8"] == 250:
        return
    StuffDone["42_8"] = 250
    WorldMap.DeactivateTrigger(Location(34,188))
    Animation_Hold(-1, 018_drawingsword)
    Wait()
    ChoiceBox("You decide to explore this cavern and have a run in with several Troglodytes. It appears they were mining this cave for some mineral or another. Unfortunately, you are surrounded and have to fight.", eDialogPic.CREATURE, 112, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_3_6", p.Target)

def SouthwesternAizic_2586_MapTrigger_43_36(p):
    result = ChoiceBox("You discover a natural spring. The water has an interesting glow to it. Care to take sip?", eDialogPic.STANDARD, 18, ["Leave", "Drink"])
    if result == 1:
        Animation_Hold(-1, 056_swallow)
        Wait()
        Animation_Hold(-1, 004_bless)
        Wait()
        MessageBox("You take a drink. The water invigorates you and restores your health!")
        Party.HealAll(25)
        return
    MessageBox("You think better of that idea and skip this spring.")

def SouthwesternAizic_2587_WanderingOnMeet1(p):
    MessageBox("A small group of people in uniform approaches you. At first you think they are an Empire patrol, but you notice their uniforms have a red spear instead of the Sword and Sun. Unfortunately, they don\'t seem to be friendly.")

def SouthwesternAizic_2588_WanderingOnMeet2(p):
    MessageBox("You have heard this area has been plagued with hostile Troglodytes. A small patrol has decided that you will make easy pickings.")

def SouthwesternAizic_2589_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    Animation_Hold(-1, 004_bless)
    Wait()
    MessageBox("You take a drink. The water invigorates you and restores your health!")
    Party.HealAll(25)

def SouthwesternAizic_2590_SpecialOnWin1(p):
    ChoiceBox("The evil priestess and her army of undead are slain. You decide to conduct a search of the premises. The surrounding alcoves of the temple contain little of value, the priestess must have had little in the way of material possessions.\n\nYou then decide to search the altar. You find a concealed alcove within the altar. Within you find a wickedly sharp knife. You decide to take it as payments for you efforts.", eDialogPic.CREATURE, 24, ["OK"])
    Party.GiveNewItem("RavageKnife_340")

def SouthwesternAizic_2591_SpecialOnFlee1(p):
    StuffDone["42_7"] = 0

def SouthwesternAizic_2592_SpecialOnWin2(p):
    MessageBox("With the Troglodytes vanquished you explore the mine. They had not gotten very far, only managing to extract a little bit of iron. It is not in sufficient quantities to be of value. However, they did find a gemstone that looks valuable.")
    Party.GiveNewItem("Emerald_179")
