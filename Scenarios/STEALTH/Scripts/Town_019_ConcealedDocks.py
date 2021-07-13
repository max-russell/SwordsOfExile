
def ConcealedDocks_310_MapTrigger_19_21(p):
    MessageBox("The chest contains all sorts of paperwork. Most of it is simple letters and correspondence. One slender volume, however, contains alchemical recipes.\n\nYou take it with you for later study. You can now make the potions Medium Speed and Graymold Salve.")
    Party.LearnRecipe("medium_speed")
    Party.LearnRecipe("graymold_salve")

def ConcealedDocks_311_MapTrigger_14_20(p):
    if StuffDone["19_0"] == 250:
        return
    StuffDone["19_0"] = 250
    TownMap.List["ConcealedDocks_19"].DeactivateTrigger(Location(14,20))
    TownMap.List["ConcealedDocks_19"].DeactivateTrigger(Location(15,20))
    TownMap.List["ConcealedDocks_19"].DeactivateTrigger(Location(16,20))
    MessageBox("You have finally reached the Hill Runner\'s secret dock, build with great care and effort in a secluded lagoon on the north side of the island.\n\nAt the end of the dock, you see a large boat, empty and ready for use. It looks like it\'s your only safe way off Morrow\'s Isle.")

def ConcealedDocks_314_MapTrigger_17_21(p):
    if StuffDone["17_3"] >= 1:
        if StuffDone["19_1"] == 250:
            return
        result = ChoiceBox("You open the chest, and find Jaen\'s parting gift for you for your services: a beautiful suit of armor, covered with small gemstones and protective runes. It\'s a truly remarkable reward.\n\nThere is also a small sack of gold, which can\'t hurt.", eDialogPic.TERRAIN, 138, ["Take", "Leave"])
        if result == 0:
            StuffDone["19_1"] = 250
            Party.GiveNewItem("PrismaticArmor_387")
            Party.Gold += 1000
        return
        return

def ConcealedDocks_315_MapTrigger_26_30(p):
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You climb the stairs, only to find that someone has locked the door at the top. Your key no longer works. Odd.")

def ConcealedDocks_316_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(40, 10),WorldMap.SectorAt(Party.OutsidePos))

def ConcealedDocks_317_CreatureDeath0(p):
    ChoiceBox("Jaen concealed himself magically to hide here, but revealed himself in order to speak with you. That was his final, critical mistake. Now, the rebels and the Empire are on even ground again. For now.\n\nOf course, the Hill Runners, having just lost their leader, won\'t be thankful, and the Empire forces will soon figure out what you\'ve done. You have no friends here anymore.\n\nYou have to leave. You\'ve undone everything you\'ve done here. Everyone is back to square one. Perhaps that\'s for the best.", eDialogPic.CREATURE, 1025, ["OK"])
