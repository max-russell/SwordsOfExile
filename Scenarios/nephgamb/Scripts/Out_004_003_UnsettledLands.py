
def UnsettledLands_589_MapTrigger_39_6(p):
    MessageBox("This passage appears to be in use. In some places you can even spot what must be tracks from cart wheels. Why they are here, you have no idea.")

def UnsettledLands_590_MapTrigger_33_11(p):
    if StuffDone["143_0"] >= 1:
        return
    result = ChoiceBox("In the middle of a particularly rough terrain you smell smoke. Following the trail of the smoke, you look down into a wide  crevice and see a brigand camp. A number of troglodytes seem to be doing well as highway robbers in the area.\n\nYou apparently come across them as they are celebrating a victory, for they pay more attention to the hog roasting over the fire than to you. Do you seize the moment and attack them unawares?", eDialogPic.CREATURE, 113, ["Leave", "Attack"])
    if result == 1:
        MessageBox("Hoping for a share in their booty, you sneak up on the humanoids. At the last moment, someone hears you and shouts a warning. You attack before the drunken guards have time to react.")
        WorldMap.SpawnNPCGroup("Group_4_3_4", p.Target)
        return

def UnsettledLands_591_SpecialOnWin0(p):
    if StuffDone["143_0"] == 250:
        return
    StuffDone["143_0"] = 250
    WorldMap.AlterTerrain(Location(225,155), 1, None)
    WorldMap.DeactivateTrigger(Location(225,155))
    MessageBox("Leaning on your weapons and heaving for breath, you look for more enemies. Nothing moves. As soldiers of Chimney you thought it your duty to rid the roads of these brigands. Now that they are dead, you should also confiscate all their ill-gotten goods.")
    Party.GiveNewItem("IronGreatsword_62")
    Party.Gold += 400
