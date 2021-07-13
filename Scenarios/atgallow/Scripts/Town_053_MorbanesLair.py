
def MorbanesLair_1220_MapTrigger_28_46(p):
    if StuffDone["31_3"] == 250:
        return
    StuffDone["31_3"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(28,46))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(28,47))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(24,39))
    MessageBox("This is quite an elegant sight. Marvelous statues of Nephilim surround a glowing pool. Typically things this advanced are not what you would expect to find in a Nephil temple. The ancient Nephil engineers must have been quite advanced.")

def MorbanesLair_1223_MapTrigger_18_32(p):
    if StuffDone["31_4"] == 250:
        return
    StuffDone["31_4"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(18,32))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(18,24))
    MessageBox("You enter this room, discovering a major summoning ritual just at completion. A massive blue flame forms in the center of the pentagram, it takes a daemonic shape. Your heart sinks as you realize that you now encounter a Haakai!")
    Town.PlaceEncounterGroup(2)

def MorbanesLair_1225_MapTrigger_22_16(p):
    MessageBox("This portal is extremely dim, almost to the point of fading away completely. It seems this portal is not charged up to the point of being able to take you anywhere.")
    p.CancelAction = True

def MorbanesLair_1227_MapTrigger_7_7(p):
    if StuffDone["30_9"] == 250:
        return
    StuffDone["30_9"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(7,7))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(7,5))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(7,4))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(7,2))
    Town.PlaceEncounterGroup(3)
    Animation_Explosion(Location(9,4), 1, "005_explosion")
    Animation_Hold()
    Wait()
    ChoiceBox("Suddenly, you see a bright flash and a familiar figure emerges. You remember him from the story scene as the villainous Raven, assassin to Emperor Sol III and Morbane\'s father.\n\nYou hear Morbane\'s voice, \"Once I was able to escape this prison, I managed to conjure the soul of the murderer of my parents. I managed to conquer his will and is now under my control. I shall now have him kill you as he killed my parents.\"\n\nThe voice disappears and Raven begins to move toward you. His eyes appear struggled, as if he is trying to pull back, but his body will not allow it. You see the retribution. Morbane is forcing his old foe to serve him.\n\nUnfortunately, that service is not to your benefit at all.", eDialogPic.CREATURE, 33, ["OK"])

def MorbanesLair_1231_MapTrigger_14_9(p):
    if StuffDone["31_1"] == 0:
        MessageBox("Sparks fly out from the floor, forcing you back!")
        Party.Damage(Maths.Rand(5, 1, 5) + 25, eDamageType.MAGIC)
        Wait()
        p.CancelAction = True
        return

def MorbanesLair_1237_MapTrigger_14_11(p):
    if StuffDone["31_1"] == 0:
        MessageBox("Blades rain from the ceiling and fling back and forth between the pillars. Ouch!")
        for x in range(14, 19):
            for y in range(10, 16):
                Town.PlaceField(Location(x,y), Field.BLADE_WALL)
        return

def MorbanesLair_1243_MapTrigger_17_10(p):
    if StuffDone["31_1"] == 0:
        MessageBox("The floor seems to suck the life force right out of you!")
        Party.HealAll(-100)
        return

def MorbanesLair_1245_MapTrigger_32_6(p):
    if StuffDone["31_1"] == 0:
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Animation_Vanish(Party.LeaderPC, True, "010_teleport")
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        Wait()
        Party.Reposition(Location(32,8))
        p.CancelAction = True
        Animation_Vanish(Party.LeaderPC, False, "010_teleport");
        for n in range(9):
            Animation_Explosion(Maths.Rand(Party.LeaderPC.Pos.X - 2, Party.LeaderPC.Pos.X + 2), Maths.Rand(Party.LeaderPC.Pos.Y - 2, Party.LeaderPC.Pos.Y + 2), 2, None)
            Animation_Pause(50)
        p.CancelAction = True
        ChoiceBox("When you approach the door, there is a flash of light and you find yourselves teleported into Morbane\'s throne room. His skeletal body sits as imposing as ever. Dark energy swirls around him and permeates the entire room.\n\n\"At last, you have made it, come forward and face your destiny!\" he beckons. The door behind you is sealed tight. It looks like you have passed the point of no return. There is no turning back now!", eDialogPic.CREATURE, 60, ["OK"])
        return

def MorbanesLair_1246_MapTrigger_32_10(p):
    if StuffDone["31_1"] == 0:
        ChoiceBox("Morbane stares deep into your soul as his skeletal rises from its throne. \"Now you know the truth of your Empire. By law and my heritage, I am the rightful ruler of the Empire. I am your Emperor.\n\nI know you may not excuse what I have done, but I find my actions perfectly acceptable. I am not the fiend you believe me for I have compassion for the people of my nation. I regret having to take the lives of several magi.\n\nHowever, the time here had made me weak, too weak to effectively rule. Their life forces were the necessary sacrifice to make way for my rise. I truly apologize for the damage I was forced to inflict, but such is the way for any Emperor.\n\nThe war I would have waged through Auspire was the best way. I wanted to strike with such force that the current powers would know that the fight was hopeless and surrender to me. It was the way with the least loss of life.\n\nMy compassion not only extends to humans but also the Nephilim, Slithzerikai, Troglodytes, and any other sentient and civilized race. Once I take control I shall ensure equality and proportional representation for all cultures and races.\n\nThe aeons locked in this place have given me great wisdom and power. My influence will spread to every corner of the world. We shall enter a new era without secrets, without the need for violence, without injustice.", eDialogPic.CREATURE, 60, ["OK"])
        ChoiceBox("\"I envision a world where everyone has access to the resources and needs that everyone requires. Everyone will live and work in comfort to build a new productive society. It shall be the dreamed of Utopia!\"\n\nYou ask, \"What about the people that will not conform to your rulership.\" Morbane emits what you might consider to be a chuckle. It is quite hard to tell with that outerworldly voice of his.\n\n\"Immediately after my takeover, life shall become better for all. I understand that there would be those who may resist. However, the masses will come to accept the better life and reject the ideals of those outsiders.\n\nI have powers that no Emperor before has had, not even the great Odin I, the only Emperor who was also an archmage. I shall be able to see everywhere around the world at once, I shall see injustices, I shall see everything.\n\nMy influence will solve all ills. All diseases will be cured. There shall never be a shortage of resources through my planning. There will be no need for armies or weapons for I shall be the final adjudicator and administrator of justice.\n\nMost importantly, I am eternal. Once I take control, this prosperity will not end with my death. It shall be as everlasting as the mountains. Join me, friends, and you can be a part of the revolution to make the world a better place!\"", eDialogPic.CREATURE, 60, ["OK"])
        ChoiceBox("\"Our mind is already made up. Our loyalty is to OUR Empire, not YOUR vision of what the Empire should be. Get over yourself Morbane. We, the citizens of the Empire, are capable of doing things for ourselves!\n\nWe don\'t require you looking over our shoulders, deciding everything for us. For what is the point of living if there are no challenges or struggles. Your intent does not forgive your crimes, Morbane. We will do whatever it takes to stop you!\"\n\nMorbane becomes very black upon your harsh refusal. He causes a gust of wind that knocks you to the floor. \"Do you really think you are capable of stopping me, puny soldiers? Your foolishness surprises me considering you have already witnessed my power.\n\nThis time we are deep inside of a mountain, far from the sunlight which can harm me. There will be no accidental victory for you this time, I\'m afraid. I give you one final chance to reconsider or I shall crush you like the insects you are!\"\n\nYou stand and draw your weapons. Morbane levitates his body from the ground as he charges his powers. \"Very well then fools. Prepare to meet your final destiny!\"", eDialogPic.CREATURE, 60, ["OK"])
        if SpecialItem.PartyHas("Sunstone"):
            ChoiceBox("Morbane instantly discharges massive amounts of dark energy that pin you against the back wall. You hear his horrific cackle as your life force is forced out of you. It appears that this is the end.\n\nBut then, you withdraw the sunstone and shine it directly at Morbane!", eDialogPic.CREATURE, 60, ["OK"])
            Animation_Explosion(Location(32,12), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Animation_Explosion(Location(32,12), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Animation_Explosion(Location(32,12), 0, "005_explosion")
            Animation_Hold()
            Wait()
            Town.NPCList.Clear()
            StuffDone["31_1"] = 1
            if Maths.Rand(1,0,100) <= 100:
                Town.PlaceField(Location(32,12), Field.CRATER)
            Town.AlterTerrain(Location(32,7), 0, TerrainRecord.UnderlayList[142])
            Animation_Explosion(Location(32,12), 1, "005_explosion")
            Animation_Hold()
            Wait()
            ChoiceBox("As soon as the sunlight strikes Morbane, the tables turn. He howls out in great agony as the sunlight literally begins to burn him away. At first there is a thick black smoke, then several small fires, and finally a succession of explosions!\n\nDespite his best efforts, he is unable to recover and counterattack. You show him no mercy as the searing beams of sunlight tear him apart. There is a final booming scream, louder and more pained then you had ever heard before.\n\nThen, there is a brilliant flash of light and all that is left of Morbane is a pile of ash. You hear a distant fading whisper ring out. You are not sure if it is just your imagination or real.\n\n\"My burden...finally gone. Strife is...over. Finally...at long...last...I am...free!\"\n\nThe final word echoes through your mind. You wonder about those last words. Perhaps all Morbane truly wanted was to be relieved of all the suffering and bitter thoughts of what the world could have been had Ironclad failed so long ago.\n\nHowever, that is simply speculation. The only thing for sure is that it is over, at least for now anyway.", eDialogPic.CREATURE, 60, ["OK"])
            StuffDone["100_1"] = 1
            return
        Party.HealAll(-250)
        Party.Damage(Maths.Rand(20, 1, 20) + 100, eDamageType.UNBLOCKABLE)
        Wait()
        Party.Damage(Maths.Rand(20, 1, 20) + 100, eDamageType.UNBLOCKABLE)
        Wait()
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        ChoiceBox("You charge Morbane, but he instantly discharges his dark energies. You are smashed against the back wall, by the intense waves of pure shadow. They penetrate you, causing immense pain. You feel your life force being pushed out of you.\n\nNo matter how hard you try, you are incapable of rising up against Morbane. It is not too long that you are reduced to a pile of dust. If only you had had some kind of weapon to have used against him.\n\nTHE END", eDialogPic.CREATURE, 60, ["OK"])
        Scenario.End()
        return

def MorbanesLair_1255_MapTrigger_27_3(p):
    if StuffDone["31_5"] == 250:
        return
    StuffDone["31_5"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(27,3))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(27,4))
    MessageBox("You emerge into an extremely elegant temple. This must be the main shrine. There is large iron door to the south of the main altar. For some reason, you feel drawn to that door.")

def MorbanesLair_1257_MapTrigger_37_3(p):
    if StuffDone["31_1"] == 0:
        MessageBox("You just cannot go further. The urge to see what is behind that door overcomes you. You have to see what is beyond that door!")
        p.CancelAction = True
        return

def MorbanesLair_1259_MapTrigger_47_28(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["31_6"] == 250:
        return
    StuffDone["31_6"] = 250
    ChoiceBox("You enter this room and are awestruck by what you see ahead. Decorated in alien style, this room houses what you can best describe only as a machine.\n\nThe machine is, or at least is covered by, a glowing basalt dome decorated with several runes. At the top of the dome, protrudes a large flawless bright blue crystal. Around that crystal are several smaller, but equally flawless crystals.\n\nAt the face of the dome is what you believe to be a control panel. The only mechanism there is another shimmering crystal, very similar to the other ones but a bit brighter. The entire mechanism emits a soft hum.\n\nYou\'ve never quite seen anything like this before. You are betting it has something to do with that mysterious purple robed mage, that Apieron character that you saw in Morbane\'s story sequence. Either way, you have severe misgivings about this device.\n\nPerhaps this merits a closer look.", eDialogPic.STANDARD, 1026, ["OK"])

def MorbanesLair_1261_MapTrigger_47_23(p):
    result = ChoiceBox("A closer look reveals little else about this machine. You have very little idea of what it does or how it works. The panel imbedded the face leads you to believe that it is the control mechanism.\n\nYou sit and inspect the control panel. There are no other buttons besides that sparkling crystal. As you examine it more closely, the crystal seems to reach out and touch your mind, as if it wants you to interface with it.\n\nYou bet that if you touch the crystal, you would be able to somehow interface with this strange machine and perhaps learn a thing or two about it.\n\nHowever, interfacing with alien machines can be very dangerous. You don\'t like this machine at all. It permeates some intangible malevolent field, something that you cannot quite get a grip of. All you know is that it is no good.\n\nSo perhaps you should try to smash this machine and halt the plans of that Apieron. However, it is unlikely he/she/it left the machine without adequate defenses, so that would be risky.\n\nOf course, the best and sure action, along with the safest, is to simply leave this thing alone.", eDialogPic.STANDARD, 1026, ["Leave", "Destroy", "Touch"])
    if result == 1:
        MessageBox("You attempt to smash the machine. You were correct in suspecting the machine had defenses. In fact whoever designed this really wanted to keep it safe.\n\nAs soon as you strike the machine, it emits an extremely powerful shot of electrical energy. In fact it gets so hot, it vaporizes all of you. Unfortunately, the machine remains undamaged.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return
    elif result == 2:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        ChoiceBox("One of you grabs hold of the crystal. Immediately, it begins to interact with your mind. Your brain is literally flooded with options and maintenance terms. It is all so fast that you cannot sort it out or have the will to control it.\n\nYou pull your hands away from the crystal and grab your throbbing head. Your brain feels as if it is ready to explode from the overflow.\n\nAfter a few moments, you mostly recover your senses. Although you were flooded with information, you lacked the mechanisms or the knowledge to interpret or understand any of it.\n\nThe only thing that stays in your mind is the phrase \"Dark Metal\". You have no idea what this Dark Metal stuff is or what it means. Perhaps there may be someone who might.\n\nPerhaps your quest is not nearly as over as you had thought!", eDialogPic.STANDARD, 1026, ["OK"])
        pc.SetStatus(eAffliction.DUMB, Maths.MinMax(0, 7, pc.Status(eAffliction.DUMB) + 7))
        if StuffDone["32_0"] == 0:
            StuffDone["32_0"] = 1
            StuffDone["100_1"] = 1
            return
        return

def MorbanesLair_1263_MapTrigger_56_6(p):
    if StuffDone["71_1"] == 250:
        return
    StuffDone["71_1"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(56,6))
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(57,6))
    ChoiceBox("You enter a small library. You browse several of the titles and know all of them are WAY over your head. This is an ancient collection of extremely complicated books on all sorts of magic.\n\nThe writing in these books is quite bizarre and twisted. You don\'t even understand what appears to be the most \"remedial\" of the books. Whoever would read these books would probably be driven insane.\n\nYou could spend decades, probably centuries, in this library trying to learn from these books and still not understand much of it.\n\nThis library must have been where Morbane spent most of the 1,200 years imprisoned here and where he learned his ancient magics. You do not have THAT much time to spend on these works, trying to comprehend them.\n\nIt is probably best you leave this library alone.", eDialogPic.TERRAIN, 135, ["OK"])

def MorbanesLair_1265_MapTrigger_58_11(p):
    result = ChoiceBox("This chair is bathed in soft blue light emitted from the surrounding crystals. It is labeled: CHAIR OF KNOWLEDGE. Morbane probably constructed this chair to recharge his energies and aide in his learning of magic.\n\nThere is no telling what kind of benefits it could bestow onto you. Does one of you sit in the chair?", eDialogPic.TERRAIN, 171, ["Leave", "Sit"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            p.CancelAction = True
            return
        MessageBox("You sit in the chair for a while and notice little effect. You feel no new secret and ancient knowledge pouring into your mind as you had hoped. After about ten minutes, you rise feeling a bit drained of knowledge!\n\nApparently Morbane either constructed this chair so it would only serve him. Or the fact that he was undead and you are living could have had something to do with it.")
        pc.AwardXP(-30)
        return
    p.CancelAction = True

def MorbanesLair_1266_MapTrigger_59_15(p):
    if StuffDone["31_8"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["31_8"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(59,15))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 100)

def MorbanesLair_1267_MapTrigger_59_16(p):
    if StuffDone["31_9"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["31_9"] = 250
    TownMap.List["MorbanesLair_53"].DeactivateTrigger(Location(59,16))
    pc.RunTrap(eTrapType.EXPLOSION, 3, 100)

def MorbanesLair_1268_MapTrigger_50_13(p):
    RunScript("GlobalCall_MorbanesLair_2845", ScriptParameters(eCallOrigin.CUSTOM))

def MorbanesLair_1269_OnEntry(p):
    if StuffDone["31_2"] == 250:
        return
    StuffDone["31_2"] = 250
    ChoiceBox("Passing through the portal, you emerge in the same room at the beginning of the Nephilim Temple, at least you think it\'s the same room. The only difference is that the portal you went through is now gone.\n\nYou wonder why Morbane went through the trouble of showing you what is essentially his life story. Does he want you to understand his actions? Does he want you to forgive the crimes he has committed?\n\nYou have a feeling the answer lies somewhere deep within this temple. Now for the matter of getting there.", eDialogPic.STANDARD, 4, ["OK"])
