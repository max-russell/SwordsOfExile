
def ScenicVista_2274_TalkingTrigger0(p):
    ChoiceBox("Who I am is not important, but who you are is.\n\nPivotal time this is, beginning of reason I came so far. Have seen you long before, but cannot say too much for now is not the time. Great purpose you shall serve: The beginning of a new era, the beginning of the brightest star...\n\n...Remember victory cannot always be achieved, but defeat is always attainable. So long as you try your hardest, take no sorrow. Fate does not always travel on a path we may wish...", eDialogPic.STANDARD, 1030, ["OK"])
    StuffDone["63_2"] = 1
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "EnigmaticMan_251": Town.NPCList.Remove(npc)
