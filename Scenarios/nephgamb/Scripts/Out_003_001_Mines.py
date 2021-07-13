
def Mines_557_MapTrigger_19_27(p):
    result = ChoiceBox("One of the mine shafts that riddle northern Chimney opens out into the tunnel in front of you. From where you stand, you get no clues as to whether or not the mine is in use.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        MessageBox("These parts of the cave contain rich copper ore. Because Chimney was so recently settled, metals can still be found close to the cave floor. The mines are shallow and rich. They and the tin found further east, are the spine of Chimney?s economy.\n\nYou enter the mine and chat with some of the workers for a while. But the conversation holds little interest for either party, so you leave after a short while. People in there are friendly, but dull.")
        return

def Mines_559_MapTrigger_37_12(p):
    result = ChoiceBox("One of the mine shafts that riddle northern Chimney opens out into the tunnel in front of you. From where you stand, you get no clues as to whether or not the mine is in use.", eDialogPic.TERRAIN, 240, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["57_2"] >= 1:
            if StuffDone["131_0"] == 250:
                return
            StuffDone["131_0"] = 250
            ChoiceBox("Darkness is complete inside the mine. As you stand in the entrance, you hear an unfriendly voice say \"Sstay out, or we sshoot!\" You recoil in surprise, but then you hear another voice.\n\n\"No, let them in! They are friends.\" Wondering what is going on, you see a spark light up, and soon a torch lights the old mine shaft. Eight sliths stand in a circle around you, watching you with distrust.\n\nYou recognize one. \"Sss-Varbas! You survived the attack of the rebels!\" The ambassador bows. \"Yes, thanks to you, I and my Ssara-tai brothers escaped the traitor Bass-Sslatun. I left a body in my chamber, and he thinks me dead!\"\n\nYou stay and have a ritual meal of lizard meat with the slith noble. \"We hide here until the rebels are beaten. From what I hear of them, they cannot last long. For your sake I hope they do not crush Chimney before they are are defeated.\"\n\nYou tell him what you know of the events outside the mine shaft. As you prepare to leave, Sss-Varbas presents you with a strange amulet. \"I owe you my life, and when my possessions are restored to me, I will reward you properly.\n\n\"For now, this is a token of my respect. This is a relic to us, of a kind ordinarily worn only by a priest. It will increase the potency of any poison used by your entire party. Guard it well, and good bye!\" You leave, studying the amulet.", eDialogPic.CREATURE, 50, ["OK"])
            Party.GiveNewItem("PoisonRelic_399")
            return
        MessageBox("As you enter the cave mouth, you hear an unfriendly voice: \"Sstay out, or we sshoot!\" You take no chances against an unseen enemy and pull out. But you recognize the accent. It was definitely not human.")
        return
