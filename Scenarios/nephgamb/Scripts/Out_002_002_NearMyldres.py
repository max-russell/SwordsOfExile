
def NearMyldres_569_MapTrigger_37_28(p):
    result = ChoiceBox("A pier stabs out in the river Myld. Tied to it is a heavy barge, carrying goods between the river towns. The bargemen refuse passage to a knot of angry farmers, explaining that they have been commandeered for military service.\n\nWill you approach and demand passage?", eDialogPic.TERRAIN, 49, ["Leave", "Approach"])
    if result == 1:
        if SpecialItem.PartyHas("Commandeerletter"):
            MessageBox("You push through the arguing crowd and present your letter of free passage. The captain on board quickly reads the document, nods at you and orders the crew to set off at once.\n\nThe muttering of the peasants left behind fades away as the barge leaves the shore, pulled by a team of huge lizards on the bank. The voyage passes quickly and pleasantly as you watch the terrain pass by. Eventually, you are pulled ashore.")
            Party.Age += 200
            Party.Reposition(Location(127, 97))
            p.CancelAction = True
            return
        MessageBox("You push through the arguing crowd and try to catch the attention of the captain. You tell him that you are on an important mission and need quick transport. Your voices drown in the throng of people telling him exactly the same thing.\n\nEventually, you give up and prepare for a long hike.")
        return

def NearMyldres_570_MapTrigger_31_1(p):
    result = ChoiceBox("Tuva Isle is a free harbour, a place of rest for the bargemen. The crew and lizard handlers sleep in exhaustion after a long day, while the barge captains and merchants trade, talk shop and exchange rumours of the world.\n\nIt turns out that several of them have heard of you and your exploits in Brattaskar Pass. When you enter a tavern to look for a captain headed south, you attract a small crowd of merchants clamouring to hear your story.\n\nFlushed by your sudden fame, you start to talk. Repeated toasts and offered drinks makes your account ever more dramatic. Your climatic fight with the slith priests and stopping them from sealing the Pass and isolating Chimney gains roars of approval.\n\nYou brandish the rod you stole from Thunder Rock and the merchants applaud. When you mention going south, you get several offers on the spot, without even showing your commandeer letter.\n\nYou leave in the company of an enthusiastic bargeman feeling a bit dizzy. Only afterwards you wonder if you spoke a bit too freely. You are bothered by the memory of a man leaving silently as the others cheered. A nephil.\n\nYou shrug your worries away. Are you certain you want to go south?", eDialogPic.TERRAIN, 239, ["Yes", "No"])
    if result == 0:
        MessageBox("You sleep through most of the journey south, waking to the sight of Myldres crag towering on the horizon. The barge stops just outside town. The captain escorts you ashore, telling you how proud he is to be of help in your adventures.")
        Party.Age += 200
        Party.Reposition(Location(133, 124))
        p.CancelAction = True
        return
    elif result == 1:
        return

def NearMyldres_571_MapTrigger_34_40(p):
    result = ChoiceBox("You approach one of the numerous villages surrounding the capital. There is little prospect of adventure in the settled lands of Central Chimney. But such places tend to be full of rumours from the capital. Do you spend some time looking for information?", eDialogPic.TERRAIN, 239, ["Leave", "Enter"])
    if result == 1:
        ChoiceBox("A servant in the Royal Sector, home of the Mayor of Myldres, is visiting his family in this village. The story he tells in the local inn frightens everyone:\n\n\"They put on a calm facade, but what happened was a real showdown. Groul and Ottar have been restraining anger with one another for a long time. When it was finally let out, there was a fight.\n\n\"Commander Groul and all of his retainers have left the court. He was sent into exile, even though no one dares use the word. Mayor Ottar threw the nephilim out of Myldres!\"\n\nThe villagers react with fear. It appears that Groul has greater support here than among the nobles of Myldres.\n\n\"And now when the sliths are coming, there is nobody to protect us.\" the servant says. \"I wonder where Groul went.\"", eDialogPic.TERRAIN, 239, ["OK"])
        Party.Age += 500
        return

def NearMyldres_572_MapTrigger_35_22(p):
    result = ChoiceBox("You approach one of the numerous villages surrounding the capital. There is little prospect of adventure in the settled lands of Central Chimney. But such places tend to be full of rumours from the capital. Do you spend some time looking for information?", eDialogPic.TERRAIN, 239, ["Leave", "Enter"])
    if result == 1:
        MessageBox("A miner from the tin works north of Milestone stops by the local square. When you ask him about his journey, he tells you that a terrible Drake is ravaging the lands to the east. \"Why don?t the authorities do anything?\" he asks.\n\nYou feel embarrassed, and as you wear the uniforms of the Chimney army, you promise to look into the matter. When you have the time, you add.")
        Party.Age += 500
        return

def NearMyldres_573_MapTrigger_43_38(p):
    result = ChoiceBox("You approach one of the numerous villages surrounding the capital. There is little prospect of adventure in the settled lands of Central Chimney. But such places tend to be full of rumours from the capital. Do you spend some time looking for information?", eDialogPic.TERRAIN, 239, ["Leave", "Enter"])
    if result == 1:
        MessageBox("A trader in alchemical herbs has come in empty handed from the slith border at the Long Stairs. The slith rebel cult has seized the lands below, and the road down from Chimney is under repair. Just as well that the road is impassable, you think.")
        Party.Age += 500
        return

def NearMyldres_574_MapTrigger_44_13(p):
    result = ChoiceBox("You approach one of the numerous villages surrounding the capital. There is little prospect of adventure in the settled lands of Central Chimney. But such places tend to be full of rumours from the capital. Do you spend some time looking for information?", eDialogPic.TERRAIN, 239, ["Leave", "Enter"])
    if result == 1:
        MessageBox("The inhabitants of this village are nearly hysterical. A cave two headed goat has been born at a local farm, and this is only the final warning that the world is coming to an end, a woman tells you. The dead are walking in the ruins of Whitstone.\n\nDuring the period of sleep a few days ago, an endless column of phantom riders rode past the village, headed north. The victims of the disaster in Whitstone are coming back for revenge! You add that the sliths are invading, and the panic heightens.")
        Party.Age += 500
        return
