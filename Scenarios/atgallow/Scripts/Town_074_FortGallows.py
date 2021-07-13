
def FortGallows_1838_MapTrigger_25_25(p):
    if StuffDone["62_7"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("The guard stops your advance through these doors. You are informed that you must first sign in at the desk. It sure does not take long for the Imperial bureaucracy to spring up.")
        return

def FortGallows_1840_MapTrigger_14_11(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(14,16)).Num == 128:
        if StuffDone["62_8"] == 1:
            Town.AlterTerrain(Location(14,16), 0, TerrainRecord.UnderlayList[125])
            return
        return

def FortGallows_1843_MapTrigger_14_16(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["62_9"] == 250:
        return
    StuffDone["62_9"] = 250
    MessageBox("You open the door to speak with the barrier expert. You are pleasantly surprised to find out that the barrier expert is none other than Astervis! At this moment he is analyzing a barrier set up between several runes.\n\nHe turns to you and smiles. \"Well, it appears that we will be getting to work together again. Come in! I\'ll tell you about the situation we are facing.\"")

def FortGallows_1844_MapTrigger_18_11(p):
    if StuffDone["62_8"] == 0:
        MessageBox("This is no time for rest! You must see the Dervish first.")
        return
    result = ChoiceBox("These beds have specially been set aside for you. You are free to kick back and relax whenever you like.", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        Party.HealAll(250)
        for pc in Party.EachAlivePC():
            pc.SP+= 150
        MessageBox("You rest in the barracks. You have an extremely comfortable resting period.")
        Party.Age += 1000
        return

def FortGallows_1845_MapTrigger_23_5(p):
    if StuffDone["62_8"] == 0:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("You should not leave the fortress before you speak with the commanding Dervish.")
        return

def FortGallows_1848_OnEntry(p):
    if StuffDone["62_6"] == 250:
        return
    StuffDone["62_6"] = 250
    ChoiceBox("Accepting your fate, you board the cargo ship. The accommodations are far from comfortable, but at an acceptable level. Beginning your voyage in the afternoon, it takes you overnight to get there.\n\nYou manage to get a decent rest while aboard the vessel. One of you awakens during the night and sees an ominous glow in the sea to the north. It is very faint, but it seems like an early dawn from the north.\n\nNo wonder why ships have stayed away from here. You just hope that you will be all right by going there. You near the island in the morning, getting a good view. It is not that impressive really.\n\nIt is just a massive, barren rock. You notice slight flickers of glow throughout the island. In the center is a hill with a large ominous fortress giving off green light from the bubulous openings. You feel the end may lie there.\n\nAt last you arrive at the small settlement. The construction looks shoddy, but it is as complete as it is going to be. You must admit this is quite impressive on such a short notice.\n\nAt last you arrive at a large dock and disembark. There is no turning back now...", eDialogPic.STANDARD, 1024, ["OK"])
    Party.HealAll(250)
    for pc in Party.EachAlivePC():
        pc.SP+= 150
    Party.OutsidePos = Location(265, 40)
    Party.Age += 4000

def FortGallows_1849_TalkingTrigger0(p):
    StuffDone["62_7"] = 1
    ChoiceBox("You give him your names and he looks in the registry. \"Ah! We were wondering how long it would take for you to get here. We have heard lots about you and your numerous deeds.\n\nI\'ll just need to check you off.\" He grabs his pen and draws check marks next to your names. \"You are to report to Dervish Lin immediately. She is the one in charge of this whole blasted place.\n\nAnyway, you may use storage room \'A\' to house any of your supplies. Whatever you leave in there will not be touched. If you leave anything anywhere else, I\'m afraid you may lose it.\n\nOh and on a personal note, I sure hope that you get whatever needs to get done fast. This place really gives me the creeps.\"", eDialogPic.STANDARD, 24, ["OK"])

def FortGallows_1850_TalkingTrigger3(p):
    StuffDone["62_8"] = 1
    ChoiceBox("\"We\'ve been waiting for your arrival. Let me first inform you of the dilemma. You see, we believe the Vahnatai base is in the fortress at the center of the island. The problem is, we cannot get there.\n\nThere is an invisible barrier in between us and Gallows Keep. It is completely unlike anything our mages have seen before. In fact, we called in a barrier expert who arrived a couple days ago. Even he has no idea how to bring the barrier down yet.\n\nYou should speak with him, his lab is to the south. Penetrating this barrier will be essential if we are to succeed in our mission. That shall be your first order of business.\n\nOnce you accomplish that objective, you are to infiltrate the fortress and take any means necessary to halt Altrus. We are hoping that this will not prove too difficult once you are within the confines of the keep.\n\nWe have set aside some beds in the adjacent barracks for your exclusive use. I suggest you not tarry for time is short. We cannot allow Altrus to complete his experiment. What is the experiment you ask?\n\nWe are not totally sure, but we believe it is similar to this island. You saw this island! If Altrus is not stopped, the rest of the world may become a rocky waste just like this. The Vahnatai cannot achieve their revenge.", eDialogPic.CREATURE, 17, ["OK"])
    ChoiceBox("\"Our scouts have had many encounters with the Vahnatai. They are extremely skillful warriors and mages so care must be taken. It may be best to avoid them. We have lost several patrols to them already.\n\nAnyway, the layout of this isle is quite barren. The only features of note are Gallows Keep at the center and three ancient labs at the edges of the island. Our scouts have not yet explored the interior of the labs.\n\nWhether or not a solution to the barrier problem lies in the labs is unknown. Also, there have been reports of strange mobile fungi walking about. They seem to avoid our patrols, but they may be a threat.\"", eDialogPic.CREATURE, 17, ["OK"])

def FortGallows_1851_TalkingTrigger6(p):
    ChoiceBox("\"The barrier appeared soon after the first cargo ship arrived on these desolate shores. No one has seen anything like it before. The mages on the first voyage were utterly stumped. Somehow, I got recommended for this position.\n\nI too am perplexed by this barrier. It can only be described in one word, perfection. The barrier matrix is literally flawless. Usually barriers can be brought down because of inherent flaws in its creation.\n\nI suppose you remember Odix\'s quest to find the \'perfect barrier\' for Morbane. I believe that I have finally discovered it. To make matters worse, the matrix is utterly alien to me. I do not have any way to perform a direct assault on the barrier.\n\nIt has no weakness and it is far beyond my understanding. The Vahnatai sure are an advanced magical race. I do not know what could possibly put up and maintain a barrier of that magnitude.\n\nWe have also been unable to peer magically past the barrier so we do not know how close they are to completing their tasks. However, the environment remains unchanged so they could not have done anything appreciable yet.\n\nI do have a theory. I believe this barrier is being maintained by some powerful object within the field. It may be possible to disrupt this source. However, we must find an area called a focal point.", eDialogPic.TERRAIN, 231, ["OK"])
    ChoiceBox("Every barrier has a focal point. It is the miniscule point at the barrier\'s origin, or the point where the caster focused to create the barrier. Usually this point is insignificant because of its size.\n\nNo object could fit through this point. I believe that this barrier must have one, and that point needs to be accessible. It may be possible to cast a spell through the focal point to assault the device creating the barrier.\n\nIt may be possible to disrupt or destroy the barrier by doing this. Of course, I would need to find the focal point. My analysis of the barrier reveals none surrounding the fortress. Yet, there is probably one beneath the surface.\n\nAlthough scrys of this island are difficult because of the curse, I detect the area beneath the keep to be hollow and containing facilities. I suspect that we may be able to access these.\n\nAnyway, I\'m coming with you. I don\'t think you could do this alone.\"", eDialogPic.TERRAIN, 231, ["OK"])
    StuffDone["63_0"] = 1
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Astervis_204": Town.NPCList.Remove(npc)
    Message("Astervis joins the party!")
    SpecialItem.Give("AstervisNPC")
