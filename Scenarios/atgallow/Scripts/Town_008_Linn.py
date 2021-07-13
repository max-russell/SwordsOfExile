
def Linn_80_ExitTown(p):
    if p.Dir.IsNorth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(11, 17),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(11, 17),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsSouth:
        Party.OutsidePos = WorldMap.ToGlobal(Location(12, 18),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(12, 17),WorldMap.SectorAt(Party.OutsidePos))

def Linn_81_TalkingTrigger6(p):
    if StuffDone["32_5"] >= 2:
        return
    if StuffDone["32_5"] < 1:
        p.TalkingText = "\"It should not be a problem for trained Imperial men like us. But with so many of them and so few of us, my situation is difficult. We could defeat them, but I would suffer losses I cannot afford.\n\nWe even know where their base is. But we can\'t do anything about it.\""
        return
    p.TalkingText = "You tell her about the slaying of the mage in control of the Goblins. She smiles, \"Thank you for your services. The main reason we did not attack was because of him. We just couldn\'t stand up to him in our condition.\"\n\nShe presents you with a sword. \"Take this blade as compensation. Your help is appreciated.\""
    StuffDone["32_5"] = 2
    Party.GiveNewItem("IronBroadsword_58")

def Linn_82_TalkingTrigger23(p):
    if StuffDone["0_2"] < 6:
        p.TalkingText = "\"A local, no names, mentioned that he was a member of that renegade group called the Followers. Anyway, he talked about the leader, a Zaine. He said he used magic to give him fighting abilities.\n\nHe showed them off. They were pretty impressive martial arts. If he could do that for HIM, I wonder what that Zaine could do for me!\""
        return

def Talking_8_7(p):
    if Party.Gold >= 0:
        if TownMap.List["GoblinFarms_84"].Hidden == True:
            Party.Gold -= 0
            TownMap.List["GoblinFarms_84"].Hidden = False
        p.TalkingText = "\"You want to help? Well, I suppose it can\'t hurt to let you. They reside in a small farming community which is south of here. The farmers were killed by the Goblins and they took it over. Just be careful around there.\""
    else:
        p.TalkingText = ""

def Talking_8_11(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "He grabs a mug from under the counter and fills it with nice, cold beer. \"Enjoy folks!\" You drink it down, it is very refreshing."
    else:
        p.TalkingText = "\"Sorry everybody pays. Rules of the house.\""

def Talking_8_12(p):
    if Party.Gold >= 12:
        Party.Gold -= 12
        p.TalkingText = "\"Feelin\' a bit more luxurious are we?\" He pours some wine in some glasses. It tastes fairly good. He turns to you and smiles. \"Say would you like to here the latest news.\""
    else:
        p.TalkingText = "\"Sorry everybody pays. Rules of the house.\""

def Talking_8_14(p):
    if Party.Gold < 20:
        p.TalkingText = "\"Sorry but we need to make a profit. Can\'t let anyone stay for free. Rules of the house.\""
    else:
        Party.Gold -= 20
        Party.Pos = Location(9, 38)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "Baley calls for an assistant. A young man comes and leads you to your lodgings. Just as you are leaving, Baley wishes you a good night and you do."
        CentreView(Party.Pos, False)

def Talking_8_20(p):
    if Party.Gold >= 2500:
        if TownMap.List["ForgottenAcademy_41"].Hidden == True:
            Party.Gold -= 2500
            TownMap.List["ForgottenAcademy_41"].Hidden = False
        p.TalkingText = "You hand him the gold. He smiles. \"It\'s in a cave just north of Lake Praddor. You will need a boat to reach it. Be careful, I received my illness from one of the traps within. You don\'t want to end up like me.\""
    else:
        p.TalkingText = "\"My search was extensive and took years. Come back when you have enough gold.\""
