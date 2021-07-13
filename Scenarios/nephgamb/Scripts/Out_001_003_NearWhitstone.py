
def NearWhitstone_583_MapTrigger_37_8(p):
    result = ChoiceBox("On the shore of the shallow Marble Lake, you come across a team of burly men, hauling boulders from the water. They seem peaceful, so you approach them. They tell you that they salvage marble from the ruins of the drowned city Whitstone.\n\nOne of the men points over the dark lake to a grand collection of houses, sunk into the ice cold water. \"Whitstone is haunted. They say lord White himself walks over the water, lamenting his city. Nobody goes there.\"\n\nYou ask the man what happened to the town, but he shakes his head. \"It?s bad luck to speak of it. And I don?t think of curses or anything. The Cat Commander has declared Whitstone a forbidden area. Nobody is to go there or even talk about it.\n\n\"We don?t have to go there to pick up the marble, however. The current in the river tears the buildings apart and push rocks ever so slowly this way. After ten years, quite a few slabs of marble have crossed the lake.\"\n\nYou ask if he could take you to Whitstone, but he refuses blankly. You tell him that you act on behalf of Mayor Ottar and he jerks a thumb over his shoulder. \"If you?re really interested in going there, talk to our master Chilke over there. I?d never go.\"", eDialogPic.CREATURE, 3, ["Leave", "Approach"])
    if result == 1:
        result = ChoiceBox("A small, wrinkly man is leading the salvage. You ask him if he could take you into Whitstone, and he considers you shrewdly. \"This is important to you?\" he asks. You nod reluctantly.\n\n\"Hah!\" he chuckles, \"A lesson in economics! The value of an object lies in the price the customer is willing to pay, not in the cost of manufacture. It would cost me very little to have one of my men row you across. But it is worth a lot to you, yes?\"\n\n\"My advantage! I am the only provider, and you must have urgent business in that place, otherwise you would never have come here. I name the price!\" He rubs his hands, enjoying himself.\n\n\"MY price is ... four hundred gold! Take it or leave it!\"", eDialogPic.CREATURE, 59, ["Leave", "Buy"])
        if result == 1:
            if Party.Gold >= 400:
                Party.Gold -= 400
                MessageBox("Master Chilke takes your money and waves for one of his workers to row you across. \"I?m sure we can agree on a price to bring you back as well!\" he shouts as you pull away from the shore. Ten minutes later, you land outside the town.")
                Party.Reposition(Location(82, 149))
                p.CancelAction = True
                return
            return
        return

def NearWhitstone_584_MapTrigger_34_5(p):
    result = ChoiceBox("Master Chilke?s boat hovers just off shore. \"My estimated value for carrying you back is 200 gold!\" the businessman shouts.", eDialogPic.CREATURE, 59, ["Leave", "Buy"])
    if result == 1:
        if Party.Gold >= 200:
            Party.Gold -= 200
            MessageBox("You are taken back on land. Glad to leave Whitstone.")
            Party.Reposition(Location(85, 152))
            p.CancelAction = True
            return
        return
