
def BrattaskarPass_536_MapTrigger_7_34(p):
    if StuffDone["101_0"] == 250:
        return
    result = ChoiceBox("A wide cave opening releasing damp, smelly air attracts your attention. You stop to investigate, and hear a chorus of whining voices inside. Entering would be brave, not to say foolhardy. Still, adventure tugs at you.", eDialogPic.TERRAIN, 242, ["Leave", "Enter"])
    if result == 1:
        StuffDone["101_0"] = 250
        WorldMap.AlterTerrain(Location(55,34), 1, None)
        WorldMap.DeactivateTrigger(Location(55,34))
        MessageBox("Reckless, adventurous spirit wins out, and you enter the smelly pit, blades bared. Adventure is there, waiting for you in the shape of a family of hissing hydras.")
        WorldMap.SpawnNPCGroup("Group_1_0_4", p.Target)
        return

def BrattaskarPass_537_SpecialOnWin0(p):
    result = ChoiceBox("When the last of the hissing multitude of heads is cut off, deadly silence sets in. Humming and talking among yourselves to fend off the oppressive silence, you look for treasure. A metal buckler and a pouch of gold are your reward.", eDialogPic.CREATURE, 143, ["Take", "Leave"])
    if result == 0:
        Party.GiveNewItem("SteelBuckler_142")
        Party.Gold += 100
    return
