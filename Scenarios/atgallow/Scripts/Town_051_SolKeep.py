
def SolKeep_1182_MapTrigger_17_12(p):
    if StuffDone["27_5"] >= 2:
        SpecialItem.Give("Sunstone")
        MessageBox("You return to discover a fully functional sunstone! You grab the sphere, now very bright, from the alcove. It is so bright, like a miniature sun, that you have to conceal it. You now have your weapon to use against Morbane!")
        StuffDone["27_5"] = 0
        return
    if StuffDone["27_5"] < 1:
        if SpecialItem.PartyHas("Moonstone"):
            result = ChoiceBox("The sunlight shines extremely bright over this area. You have heard of this place. Here the sun always shines, day and night, cloudy and sunny. You look to the ceiling, at the source, and are blinded by the brightness.\n\nYou don\'t know how this strange effect occurs, but you guess that somehow the rocks store the sunlight and radiate it down.\n\nYou take out your moonstone. If you are going to convert it into a sunstone, you would need constant sunlight for several days. This is probably the only place in the world you could accomplish this. There is am alcove here where you could insert it.\n\nOf course, you notice the warmth of the sunlight and could meditate here for a while first.", eDialogPic.STANDARD, 28, ["Leave", "Insert", "Pray"])
            if result == 1:
                StuffDone["27_5"] = 1
                MessageBox("You insert the moonstone in the alcove, taking care that the sunlight will be exposed to all of it. It will probably take several days for this transformation to occur.")
                SpecialItem.Take("Moonstone")
                RunScript("GlobalCall_SolKeep_2844", ScriptParameters(eCallOrigin.CUSTOM))
                return
                return
            elif result == 2:
                Party.HealAll(250)
                MessageBox("You spend several hours basking in the warm glow of the sunlight. The effect is much better than you could have dreamed of. It feels as if you have become one with the world itself. You emerge fully restored!")
                for pc in Party.EachAlivePC():
                    pc.SP+= 150
                if StuffDone["27_7"] == 250:
                    return
                StuffDone["27_7"] = 250
                MessageBox("You also notice that your mind is much clearer. In fact, you\'ve never felt quite so good in your life. You seem to know things that you never did before as if the sunlight literally enlightened you!")
                for pc in Party.EachAlivePC():
                    pc.SetSkill(eSkill.INTELLIGENCE, pc.GetSkill(eSkill.INTELLIGENCE) + 1)
                return
            return
        result = ChoiceBox("The sunlight shines extremely bright over this area. You have heard of this place. Here the sun always shines, day or night, cloudy or sunny. You look to the ceiling, at the source, and are blinded by the brightness.\n\nYou don\'t know how this strange effect occurs, but you guess that somehow the rocks store the sunlight and radiate it down. It is said that meditating within the warmth of the sunlight improves ones health.\n\nCare to meditate and appreciate the full beauty of this sanctuary?", eDialogPic.STANDARD, 28, ["Leave", "Pray"])
        if result == 1:
            Party.HealAll(250)
            MessageBox("You spend several hours basking in the warm glow of the sunlight. The effect is much better than you could have dreamed of. It feels as if you have become one with the world itself. You emerge fully restored!")
            for pc in Party.EachAlivePC():
                pc.SP+= 150
            if StuffDone["27_7"] == 250:
                return
            StuffDone["27_7"] = 250
            MessageBox("You also notice that your mind is much clearer. In fact, you\'ve never felt quite so good in your life. You seem to know things that you never did before as if the sunlight literally enlightened you!")
            for pc in Party.EachAlivePC():
                pc.SetSkill(eSkill.INTELLIGENCE, pc.GetSkill(eSkill.INTELLIGENCE) + 1)
            return
        p.CancelAction = True
        return
    MessageBox("The moonstone is still here. It seems brighter than before, but it still has not begun to radiate sunlight on its own. These things take time.")
