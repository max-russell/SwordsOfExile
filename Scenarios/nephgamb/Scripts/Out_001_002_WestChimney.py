
def WestChimney_568_MapTrigger_31_39(p):
    result = ChoiceBox("At the edge of a fertile grass meadow, you find a cosy cabin. A herd of cave sheep are grazing by the house, but scatter in fear when you arrive. Moreover, two or three scaly lizards are snoozing in front of the cabin.\n\nDo you approach and knock on the door?", eDialogPic.TERRAIN, 239, ["Leave", "Approach"])
    if result == 1:
        result = ChoiceBox("You push a lizard away from the door with your boot and knock. The lizards wheeze, but show little concern at your intrusion. The door is opened by a man with the same phlegmatic facial expression as his lizards.\n\nHe invites you in and offers you to have dinner with him. He asks about you and your lives, but seems uninterested in the threat of war. \"Wars and rulers come and go,\" he says. \"I moved here to get away from them. I hope they won?t follow.\"\n\nHe tells you that he used to make a living by selling boots in Myldres. When his daughter was old enough to run the shop, he moved here to pursue his interest in leather and scale footwear.\n\nAt first you find his account rather dull. But when you realize that his creations serve excellently as armour, your interest grows. \"Adventurers come here at times to by my greaves. I give them for free, provided they bring their own material.\n\n\"Different kinds of skins and scales may be used, everything that is tough and resistant. Let me know if you want me to make you a piece. I do it free for promotion. If you are pleased, let your colleagues know!\"", eDialogPic.CREATURE, 2, ["Leave", "Accept"])
        if result == 1:
            if Party.CountItemClass(2, True) > 0:
                MessageBox("You show him the material that you took so crudely from its previous owner. The man looks it over and approves. He takes you into his workshop, where he skilfully fastens the armour onto a set of leather pants. You now have a set of leg greaves.")
                Party.GiveNewItem("Greaves_395")
                return
            MessageBox("\"I?m afraid I must insist that you bring your own materials. They are hard to come by for an old man.\" You promise to return if you find any, thank him for his hospitality and leave. The lizards are still dozing outside")
            return
        return
