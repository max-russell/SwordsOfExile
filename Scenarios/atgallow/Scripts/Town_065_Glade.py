
def Glade_1592_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(31, 30),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(29, 32),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(31, 34),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(33, 32),WorldMap.SectorAt(Party.OutsidePos))

def Glade_1593_TalkingTrigger14(p):
    if StuffDone["52_3"] < 5:
        if Party.Gold >= 3000:
            Party.Gold -= 3000
            Party.GiveNewItem("GoldUnicornHorn_327")
            p.TalkingText = "You purchase a gold unicorn horn. \"Make good use of it, friends. It\'s not often that you come by these.\""
            StuffDone["52_3"] += 1
            if StuffDone["52_3"] == 250:
                pass
            return
        p.TalkingText = "You cannot afford it."
        return

def Glade_1594_TalkingTrigger18(p):
    count = Party.CountItemClass(32, True)
    Party.Gold += count * 3
    p.TalkingText = "Arno pays three gold pieces for each of your standard books."

def Glade_1595_TalkingTrigger22(p):
    if StuffDone["52_4"] >= 3:
        return
    if StuffDone["52_4"] < 2:
        StuffDone["52_4"] = 1
        p.TalkingText = "\"You would?\" He checks his bookshelves and digs it out and hands it to you. It is a rolled up vellum scroll. \"If you find someone who would be willing to translate it, it would be much appreciated.\""
        SpecialItem.Give("NephilimManuscript")
        return
    StuffDone["52_4"] = 3
    SpecialItem.Take("NephilimManuscript")
    ChoiceBox("You return the translated manuscript to him. He looks it over and quickly reads the first part. Satisfied he puts it down on the table and grabs a book of prayers. As he flips through it he says, \"Now to find that reward. Ah, here it is!\"\n\nHe rises and begins to chant in some strange tongue, an ancient and lost prayer. As he proceeds with the chants, he becomes louder and louder as if he was building up to a grand crescendo.\n\nOn the last verse, he lets out a great cry. You swear that your skin tingles slightly. He puts the book away and speaks to you. \"That is an ancient Nephilim blessing that is said to bring good fortune to doers of good.\"\n\nHe clears his throat and takes his seat again. \"I felt it appropriate to give you that for I have little in the way of physical possessions. May you find the blessing most helpful on your travels.\"", eDialogPic.STANDARD, 21, ["OK"])
    for pc in Party.EachAlivePC():
        pc.SetSkill(eSkill.LUCK, pc.GetSkill(eSkill.LUCK) + 2)

def Talking_65_2(p):
    if Party.Gold >= 500:
        boat_ids = ["Boat_3"]
        boat_sold = False
        for s in boat_ids:
            if Vehicle.List[s].PartyOwns == False:
                Vehicle.List[s].PartyOwns = True
                Party.Gold -= 500
                boat_sold = True
                break
        if boat_sold == False:
            p.TalkingText = "There are no boats left."
        else:
            p.TalkingText = "Reluctantly, you fork over the gold and the official hands you a permit. \"The boat is to the docks, which are just to the south. Be careful, you break it, you buy it!\""
    else:
        p.TalkingText = "\"Sorry, but everyone must pay. Unless they have direct orders from the Emperor, of course.\""

def Talking_65_5(p):
    if Party.Gold >= 6:
        Party.Gold -= 6
        p.TalkingText = "You pay the fee and are served a round of refreshing drinks. They seem to have the processed taste you remember back in training. This stuff is a whole lot better than the the stuff you were served as recruits though."
    else:
        p.TalkingText = "You cannot afford it."

def Talking_65_6(p):
    if Party.Gold < 30:
        p.TalkingText = "You cannot afford it."
    else:
        Party.Gold -= 30
        Party.Pos = Location(6, 5)
        Town.UpdateVisible()
        Party.HealAll(90, True)
        Party.RestoreSP(75)
        p.TalkingText = "\"Looks like we\'ve filled one room for tonight!\" He leads you outside across a bridge to your room. It has a nice comfortable feel to it. You manage to get an excellent rest."
        CentreView(Party.Pos, False)

def Talking_65_16(p):
    if Party.Gold >= 4000:
        if TownMap.List["UnicornGraveyard_93"].Hidden == True:
            Party.Gold -= 4000
            TownMap.List["UnicornGraveyard_93"].Hidden = False
        p.TalkingText = "\"When you sail up the river into the mountains. Take the westernmost passage. At the second fork, head south and disembark at the end. Continue west into the mountains from there.\""
    else:
        p.TalkingText = "You cannot afford it."
