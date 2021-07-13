
def ValorArms_1791_MapTrigger_23_38(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["55_7"] == 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange force holds these doors shut. It appears you are trapped!")
        return
    if StuffDone["55_8"] == 250:
        return
    StuffDone["55_8"] = 250
    ChoiceBox("You enter the inn to find an almost deserted room. Several tables occupy the large tavern area. Upon many of the tables rests several drinks, unattended. The only sign of life is the innkeeper at the counter.\n\nPerhaps he can tell you more.", eDialogPic.STANDARD, 3, ["OK"])

def ValorArms_1793_MapTrigger_29_26(p):
    if StuffDone["55_7"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A sign above this door says that this area is for guests and personnel only. You will probably need to acquire a room before you can pass these doors.")
        return

def ValorArms_1795_MapTrigger_14_29(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["55_7"] == 0:
        StuffDone["55_7"] = 1
        ChoiceBox("You emerge from your room completely refreshed from the excellent rest. Upon opening the door, you swear you see the glint of a fleeting insubstantial humanoid figure.\n\nOf course, it could just be your imagination.", eDialogPic.CREATURE, 43, ["OK"])
        Town.PlaceEncounterGroup(1)
        for x in range(23, 25):
            for y in range(38, 39):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[125])
        return

def ValorArms_1797_MapTrigger_37_26(p):
    if StuffDone["55_9"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("A strange force holds this door shut. It seems to be held shut by a hot force, one that gives you the impression of rage.")
        return

def ValorArms_1798_MapTrigger_10_36(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        return;
    if StuffDone["55_7"] == 1:
        if StuffDone["56_2"] >= 4:
            if Party.CountItemClass(18, False) > 0:
                result = ChoiceBox("Marilyn has already set up the altar for the appropriate ritual 250 years ago, so everything is set. She will assist you with the casting when you are ready.", eDialogPic.STANDARD, 15, ["Leave", "Cast"])
                if result == 1:
                    Animation_Hold(-1, 024_priestspell)
                    Wait()
                    itemthere = False
                    if Game.Mode != eMode.OUTSIDE:
                        for i in Town.EachItemThere(Location(10,37), True):
                            if i.SpecialClass == 42:
                                itemthere = True
                                break
                    if itemthere == True:
                        Town.PlaceEncounterGroup(4)
                        Animation_Explosion(Location(9,35), 2, "005_explosion")
                        Animation_Hold()
                        Wait()
                        ChoiceBox("Suddenly, the figure of a man appears in a flash of light behind you. The ritual was a success! Vandole looks around to comprehend his new surroundings as Maggie floats closer to him.\n\n\"Vandole? Is that you?\" Vandole turns to Maggie and looks her over. \"Maggie?\" Maggie nods with tears in her eyes. \"Yes, I\'m so sorry for what I did. I thought you had completely forgotten about me!\"\n\n\"But the note?\" asks Vandole. \"I never saw the note until just recently. You see, it was burned and the ring was thrown out in the trash. I wish I had known, I\'m so sorry I caused you and...and...her to suffer.\"\n\n\"You mean Lily? What is this place and who are these people?\" Maggie looks surprised. \"Don\'t you know? This is the inn! We are all trapped here thanks to that Lily and her curse!\"\n\nVandole looks surprised as well. \"A curse? I never knew Lily laid a curse on you. Does this mean I am trapped here too?\"", eDialogPic.CREATURE, 4, ["OK"])
                        Town.PlaceEncounterGroup(5)
                        Animation_Explosion(Location(8,34), 2, "005_explosion")
                        Animation_Hold()
                        Wait()
                        ChoiceBox("Suddenly there is a flash of light. The figure of a strikingly beautiful young woman appears. \"No Vandole, YOU are not trapped here. You are coming with me. This time I will make sure no one can interfere again!\"\n\nVandole turns to Lily. \"No Lily. Please, let them go. You were the one who made this curse, please let them go.\" She responds, \"Don\'t you remember those filthy caves we had to live in? All thanks to her!\" She points at Maggie.\n\nMaggie approaches Lily. \"I guess saying that I am sorry is not good enough, Lily. I was bitter back then, so angry at you and Vandole. I did not understand, but I am sorry. I know that is not enough, but it is all I can do. At least let the others go.\"\n\nVandole turns to Lily. \"Were you the one to destroy the note and hide my ring?\" Lily looks down at the floor. \"I...I was. I just did not want to think you still loved her, I did not want her to think...\"\n\nVandole interrupts. \"Please Lily, it is for the best. Remove this curse so the spirits trapped here can depart. Please Lily.\" The young witch nods and begins to chant.", eDialogPic.CREATURE, 30, ["OK"])
                        Animation_Hold(-1, 024_priestspell)
                        Wait()
                        Town.NPCList.Clear()
                        Animation_Hold(-1, 053_magic3)
                        Wait()
                        ChoiceBox("After the chanting ceases, Lily turns to Maggie. They both look at each other, seemingly with a new understanding. Lily breaks the silence. \"The curse is broken. You, and all others trapped here, are free to leave.\"\n\nVandole approaches Maggie. \"Please, come with us. There is much I would like to speak with you about.\" Maggie nods. \"You go ahead, first I must thank those who made this possible.\" Lily and Vandole vanish.\n\nMaggie turns to you. \"Thank you. I thought for sure that we would be trapped forever here. I really have no way to repay you other than with thanks. May I wish you luck on your travels. Farewell.\"\n\nMaggie fades away, presumably following the other two. You suspect the other spirits are leaving as well now they are free. Perhaps you should be leaving too.", eDialogPic.STANDARD, 15, ["OK"])
                        StuffDone["55_7"] = 2
                        Town.NPCList.Clear()
                        return
                    MessageBox("Unfortunately, the ritual failed. Marilyn says, \"It appears you are too weak to summon him. However, it may be possible to improve our chances if you could place an object close to the person on the altar. Articles of clothing work best.\"")
                    return
                return
            MessageBox("You will require the prayer book in order to cast the ritual for it is too lengthy to memorize.")
            return
        if StuffDone["56_2"] < 2:
            MessageBox("This polished slab of rock appears to be kind of a makeshift altar. It has a similar setup to many altars that are used for conjuring. From the layers of dust, it seems this was not used in some time.")
            return
        if Party.CountItemClass(18, False) > 0:
            result = ChoiceBox("Marilyn has already set up the altar for the appropriate ritual 250 years ago, so everything is set. She will assist you with the casting when you are ready.", eDialogPic.STANDARD, 15, ["Leave", "Cast"])
            if result == 1:
                Animation_Hold(-1, 024_priestspell)
                Wait()
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(10,37), True):
                        if i.SpecialClass == 42:
                            itemthere = True
                            break
                if itemthere == True:
                    MessageBox("Even with the assistance of Vandole\'s boots, the ritual is still a failure. However, it did feel closer than before. Marilyn speaks, \"Often having someone who was close to the person increases the chance of success. Why not tell Maggie about our ritual?\"")
                    StuffDone["56_2"] = 3
                    return
                MessageBox("Unfortunately, the ritual failed. Marilyn says, \"It appears you are too weak to summon him. However, it may be possible to improve our chances if you could place an object close to the person on the altar. Articles of clothing work best.\"")
                return
            return
        MessageBox("You will require the prayer book in order to cast the ritual for it is too lengthy to memorize.")
        return

def ValorArms_1799_OnEntry(p):
    if StuffDone["55_7"] == 2:
        Town.NPCList.Clear()
        return

def ValorArms_1800_TalkingTrigger10(p):
    if StuffDone["56_0"] >= 2:
        p.TalkingText = "\"I am so sorry that I thought he did not care. I am so sorry that I did the things I did to him. I was so bitter, I wish there were a way to tell him.\""
        StuffDone["56_0"] = 2
        return
    if StuffDone["56_0"] < 1:
        StuffDone["55_9"] = 1
        return
    if StuffDone["55_9"] == 0:
        StuffDone["55_9"] = 1
        return
    if Party.CountItemClass(45, False) > 0:
        if Party.CountItemClass(43, True) > 0:
            if Party.CountItemClass(45, True) > 0:
                ChoiceBox("You show Maggie Vandole\'s letter and give her the ring you recovered. She reads the letter and looks at the ring closely. She turns to you, almost in tears.\n\n\"I have never seen this before and want not to believe, yet this ring has an inscription that Vandole used to say. I know that you did not manufacture this, and this is the truth.\n\nI just wish there were some way I could make it up to Vandole. I thought he truly did not care anymore! I am so sorry...\" She begins to cry.", eDialogPic.STANDARD, 21, ["OK"])
                p.TalkingText = "\"I am so sorry that I thought he did not care. I am so sorry that I did the things I did to him. I was so bitter, I wish there were a way to tell him.\""
                StuffDone["56_0"] = 2
                return
            return
        p.TalkingText = "You show her the note. She looks at it and hands it back to you. \"I refuse to believe this. You wrote it! My it does not even look like his handwriting and where is this ring?\" She turns away in anger. If only you could prove its validity."
        return

def ValorArms_1801_TalkingTrigger21(p):
    if Party.CountItemClass(44, False) > 0:
        p.TalkingText = "You show him the charred paper and ask him if he can help. \"It\'s been a while since I\'ve done this. I guess I can do it for a bit of entertainment and old times sake. Now, do you want me to restore the paper?\""
        return

def ValorArms_1802_TalkingTrigger23(p):
    if Party.CountItemClass(44, True) > 0:
        Sound.Play(068_identify)
        Party.GiveNewItem("VandolesLetter_393")
        ChoiceBox("You set the paper down on the table and the mage casts a something similar to an identify spell. Before your eyes, the paper begins to restore itself. You pick up the paper and find it to be a letter.\n\n\"Dear Maggie, I know that you are angry and hurt by what I have done. I also know there is nothing I can truly do to restore what we had. However, when I met her, I realized that what we wanted could never be.\n\nAs much as I care for you, I know that our differences would make us incompatible. For this I am truly sorry, but we must live with reality. Know that it is a reality that I am not happy or pleased with, but it is what stands.\n\nYou cannot imagine the guilt I feel for having to leave you. I suppose I cannot also imagine the pain you are in. I just wish there were a better way, a way that we could all be happy.\n\nI guess this is not much, but I will offer you this ring as a token of remembrance. I know that it is not enough to satisfy your pain, but it is the best I can do. Yours always, Vandole.\"", eDialogPic.STANDARD, 21, ["OK"])
        p.TalkingText = "You pocket the letter in the hope that it may be of use."
        StuffDone["56_0"] = 1
        return

def ValorArms_1803_TalkingTrigger31(p):
    if StuffDone["56_1"] == 0:
        if Party.CountItemClass(45, False) > 0:
            p.TalkingText = "You show Miles Vandole\'s letter and offer a few arguments. He sighs. \"I suppose if you think the ring belongs to her, I guess you can borrow it. I seriously doubt it will get us out of here as you think, however.\""
            Party.GiveNewItem("GoldRing_359")
            StuffDone["56_1"] = 1
            return
        return
    p.TalkingText = "You already have it."

def ValorArms_1804_TalkingTrigger35(p):
    if StuffDone["56_2"] >= 2:
        return
    if StuffDone["56_2"] < 1:
        if Party.CountItemClass(18, False) > 0:
            p.TalkingText = "You bring her prayer book. \"The curse is far too strong to dispel through ritual means. The only way is to destroy the witch\'s spirit, or to convince her to lift the curse. However, as you can see, we need the name of someone to summon.\""
            return
        p.TalkingText = "\"You look capable, but I doubt you have what it takes to perform any ritual. Not even I, in my prime, could not summon a powerful spirit like the witch\'s without knowing her name. Besides, you have no resources.\""
        return
    p.TalkingText = "You agree to help. \"Well then, we will need a place. I suppose the same altar I used to summon the witch will do. When you are ready, go to the room down the hall to the south. I shall be waiting.\""
    StuffDone["56_2"] = 2
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Priest_22": Town.NPCList.Remove(npc)
    Town.PlaceEncounterGroup(2)

def ValorArms_1805_TalkingTrigger37(p):
    if StuffDone["56_2"] == 0:
        StuffDone["56_2"] = 1
        return

def ValorArms_1806_TalkingTrigger38(p):
    if StuffDone["56_2"] >= 3:
        if StuffDone["56_0"] >= 2:
            p.TalkingText = "You tell her about the ritual. \"You mean that I will get a chance to see him again, and maybe get out of here?\" You affirm this. \"I suppose I can assist you as best I am able.\""
            StuffDone["56_2"] = 4
            for n in range(Town.NPCList.Count-1, -1, -1):
                npc = Town.NPCList[n]
                if npc.Record.ID == "Townsperson_6": Town.NPCList.Remove(npc)
            Town.PlaceEncounterGroup(3)
            return
        return
    p.TalkingText = "She scowls."

def Talking_71_0(p):
    if Party.Gold < 15:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 15
        Party.Pos = Location(9, 32)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "Your gold is pocketed and you are led by the passive innkeeper to your rooms. On your way there, you notice the inn is actually quite large by regular standards. Anyway, the room is very spacious and extremely comfortable."
        CentreView(Party.Pos, False)
