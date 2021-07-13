
def BrattaskarEntrance_538_MapTrigger_23_23(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You crawl back towards Howling Gap, trying to find a way past the slith army. It turns out that evading the patrols is hopeless, even for adventurers of your calibre.")
    WorldMap.SpawnNPCGroup("Group_2_0_4", p.Target)
