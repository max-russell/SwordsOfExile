
def SacredGround_85_MapTrigger_23_17(p):
    result = ChoiceBox("The slith horde slowly understands that something is wrong. A few warriors hesitantly move towards you. Then other sliths follow. You must hurry.\n\nStill, you stop to take a quick look at the strange rock. At close quarters you see what made you curious. Small, silvery lines criss-cross the boulder. Close to bottom you find a little hatch. You quickly lift it and peek in. Machinery!\n\nYou hardly know what to think, and do not have much time for it, either. In the middle of the artificial boulder is a small hole. Leaned against it is the curious rod that the slith leader blessed. It seems to fit into the hole.\n\nYou have only a second in which to make mischief for the sliths before they overtake you. The rod seems important. You could push the rod into the hole in the rock, or you could steal it. Or you could forget about it and run for your life.\n\nWhat do you do?", eDialogPic.TERRAIN, 229, ["Leave", "Insert", "Take"])
    if result == 1:
        MessageBox("You grab the strange rod and thrust it into the hole in the rock, just as the first slith spears land among you. The last thing you hear is an ear splitting explosion. The giant bomb goes off just like the priests had intended.\n\nThe bomb takes a supporting pillar with it, and the ceiling caves in, closing the tunnel. All you have succeeded to do is fulfil the first part of the plan for the invasion of Chimney: Sealing its connection to central Exile. And finding a quick death.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
        return
    elif result == 2:
        if StuffDone["4_0"] == 250:
            return
        StuffDone["4_0"] = 250
        MessageBox("You grab the strange rod and run, without looking twice at it. Because just then, the first slith spears swoosh past your ears. You and the other surviving prisoners run as fast as you can, sliths trailing behind you.")
        SpecialItem.Give("Strangerod")
        Party.OutsidePos = Location(119, 24)
        return

def SacredGround_86_OnEntry(p):
    ChoiceBox("The five lone priests that are left look disconsolately at one another. The slith horde watching has withdrawn to a respectful distance. Then they turn towards an altar set in front of a huge and very strange boulder.\n\nYou strain your eyes to get a better look at the rock, but then the priests lift long stone knives from the altar and begin to chant. The ceremony has begun.\n\nYou intend to stop it. Chance has made this showdown less discouraging than you had pictured it. Only the five priests are here to halt your escape.\n\nYou exchange glances, nod to the other prisoners to prepare, and suddenly erupt in furious battle cries.", eDialogPic.TERRAIN, 159, ["OK"])

def SacredGround_87_ExitTown(p):
    if p.Dir.IsNorth or p.Dir.IsWest or p.Dir.IsSouth or p.Dir.IsEast:
        if SpecialItem.PartyHas("Strangerod"):
            ChoiceBox("When the sliths finally give up and turn back to their camp, you are out of Howling Gap! You all laugh, hug and clap one another?s backs for quite some time, catching your breath and enjoying your freedom.\n\nThe ceiling soars up until it is barely visible, the cave walls fall back as the cavern widens out and becomes the fertile Exile province of Chimney.\n\nThe freed prisoners all cheer you, and insist that you should go on to Myldres without them. Several are wounded and all are exhausted. They must travel slowly. Karolynna and Spencer will care for them on their travel to the capital.\n\nOne of the prisoners, a soldier from Lushwater Toll, suggests that you go by that town. Captain Locke of the town garrison should hear your story, the man says. He might help you get to Myldres quickly, so you can reach Commander Groul.\n\nBefore you go, Karolynna asks to see the rod you stole from the sliths. Studying it, she turns pale. \"No wonder the slith priests looked afraid.\" she says. \"It appears Thunder Rock is a powerful bomb. By blowing it, they could have taken the ceiling down.\n\n\"They would have blocked our only route to Exile, isolating us from human help. We have saved more than our own lives today. Take good care of this!\" You leave the others, worry again gnawing at you. This is ambitious planning for simple raiders.", eDialogPic.STANDARD, 30, ["OK"])
            for pc in Party.EachAlivePC():
                pc.AwardXP(30)
            return
        MessageBox("You have no time for souvenirs, you think, and run for your lives. And it actually looks as if you might get away. Then you are thrown to the ground by an earsplitting explosion. The ceremony has been completed without blood sacrifice.\n\nThe artificial rock blows up and tears down the cave ceiling. The whole tunnel collapses, as the slith invaders planned. There is no way for Exile to save its province now. Unfortunately, you are lost in the explosion. Pity, for Chimney needed your help.")
        for pc in Party.EachAlivePC():
            if pc.LifeStatus == eLifeStatus.ALIVE:
                pc.Kill(None, eLifeStatus.DUST, True)
                Wait()
