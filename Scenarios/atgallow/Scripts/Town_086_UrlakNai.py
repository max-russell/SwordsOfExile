
def UrlakNai_2101_MapTrigger_3_35(p):
    if StuffDone["7_2"] == 0:
        StuffDone["7_2"] = 1
        MessageBox("You step over the rune and a strange tingle runs through your body. You feel as if you\'ve been marked in some way.")
        Town.MakeTownHostile()
        return

def UrlakNai_2102_MapTrigger_3_37(p):
    if StuffDone["7_3"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["7_3"] = 250
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(3,37))
    pc.RunTrap(eTrapType.BLADE, 2, 50)

def UrlakNai_2103_MapTrigger_12_6(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["7_4"] == 250:
        return
    StuffDone["7_4"] = 250
    MessageBox("You open the secret door and emerge in some magical library. Several mages are busy at work preparing some large arcane ritual. You don\'t know what it\'s purpose, but they don\'t want you to find out.")
    Town.PlaceEncounterGroup(1)

def UrlakNai_2104_MapTrigger_56_10(p):
    if StuffDone["7_5"] == 250:
        return
    StuffDone["7_5"] = 250
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(56,10))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(57,10))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(58,10))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(59,11))
    MessageBox("The priests of this monastary placed some punishments upon those who would defile their graves. Several of the corpses rise from beneath intending to take you back with them.")
    Town.PlaceEncounterGroup(2)

def UrlakNai_2108_MapTrigger_53_5(p):
    if StuffDone["7_6"] == 250:
        return
    StuffDone["7_6"] = 250
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(53,5))
    TownMap.List["UrlakNai_86"].DeactivateTrigger(Location(53,4))
    Town.PlaceEncounterGroup(3)

def UrlakNai_2110_MapTrigger_12_43(p):
    result = ChoiceBox("This altar is a finely crafted piece of work. It has several intricate carvings of some arcane god you do not recognize. Blood stains upon the altar show it was recently used for sacrifice.\n\nThe altar seems to welcome you. You get the urge to kneel and pray.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["8_0"] == 0:
            StuffDone["8_0"] = 1
            MessageBox("You kneel before the altar. The spirits within immediately engage your mind. They flow within you. Your entire body tingles and you feel light-headed. Then it is over. You don\'t feel any different than before.")
            StuffDone["7_7"] += 1
            if StuffDone["7_7"] == 250:
                pass
            return
        MessageBox("You kneel before the altar expecting a similar sensation. However, nothing happens. You wait around to see if the affect is delayed. Still nothing happens. You give up.")
        return

def UrlakNai_2111_MapTrigger_6_21(p):
    result = ChoiceBox("This altar is a finely crafted piece of work. It has several intricate carvings of some arcane god you do not recognize. Blood stains upon the altar show it was recently used for sacrifice.\n\nThe altar seems to welcome you. You get the urge to kneel and pray.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["8_1"] == 0:
            StuffDone["8_1"] = 1
            MessageBox("You kneel before the altar. The spirits within immediately engage your mind. They flow within you. Your entire body tingles and you feel light-headed. Then it is over. You don\'t feel any different than before.")
            StuffDone["7_7"] += 1
            if StuffDone["7_7"] == 250:
                pass
            return
        MessageBox("You kneel before the altar expecting a similar sensation. However, nothing happens. You wait around to see if the affect is delayed. Still nothing happens. You give up.")
        return

def UrlakNai_2112_MapTrigger_38_25(p):
    result = ChoiceBox("This altar is a finely crafted piece of work. It has several intricate carvings of some arcane god you do not recognize. Blood stains upon the altar show it was recently used for sacrifice.\n\nThe altar seems to welcome you. You get the urge to kneel and pray.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["8_2"] == 0:
            StuffDone["8_2"] = 1
            MessageBox("You kneel before the altar. The spirits within immediately engage your mind. They flow within you. Your entire body tingles and you feel light-headed. Then it is over. You don\'t feel any different than before.")
            StuffDone["7_7"] += 1
            if StuffDone["7_7"] == 250:
                pass
            return
        MessageBox("You kneel before the altar expecting a similar sensation. However, nothing happens. You wait around to see if the affect is delayed. Still nothing happens. You give up.")
        return

def UrlakNai_2113_MapTrigger_26_42(p):
    result = ChoiceBox("This altar is a finely crafted piece of work. It has several intricate carvings of some arcane god you do not recognize. Blood stains upon the altar show it was recently used for sacrifice.\n\nThe altar seems to welcome you. You get the urge to kneel and pray.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["8_3"] == 0:
            StuffDone["8_3"] = 1
            MessageBox("You kneel before the altar. The spirits within immediately engage your mind. They flow within you. Your entire body tingles and you feel light-headed. Then it is over. You don\'t feel any different than before.")
            StuffDone["7_7"] += 1
            if StuffDone["7_7"] == 250:
                pass
            return
        MessageBox("You kneel before the altar expecting a similar sensation. However, nothing happens. You wait around to see if the affect is delayed. Still nothing happens. You give up.")
        return

def UrlakNai_2114_MapTrigger_50_3(p):
    result = ChoiceBox("This altar is a finely crafted piece of work. It has several intricate carvings of some arcane god you do not recognize. Blood stains upon the altar show it was recently used for sacrifice.\n\nThe altar seems to welcome you. You get the urge to kneel and pray.", eDialogPic.TERRAIN, 154, ["Leave", "Pray"])
    if result == 1:
        if StuffDone["8_4"] == 0:
            StuffDone["8_4"] = 1
            MessageBox("You kneel before the altar. The spirits within immediately engage your mind. They flow within you. Your entire body tingles and you feel light-headed. Then it is over. You don\'t feel any different than before.")
            StuffDone["7_7"] += 1
            if StuffDone["7_7"] == 250:
                pass
            return
        MessageBox("You kneel before the altar expecting a similar sensation. However, nothing happens. You wait around to see if the affect is delayed. Still nothing happens. You give up.")
        return

def UrlakNai_2115_MapTrigger_10_36(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(10,35)).Num == 147:
        if StuffDone["7_7"] >= 5:
            MessageBox("As you approach the gates a mysterious force scrys you. After a few seconds, the sensation ceases. A whisper sounds in your heads, \"You are worthy to pass.\" The gates slide open for you.")
            SuspendMapUpdate()
            for x in range(10, 12):
                for y in range(35, 36):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("As you approach the gates a mysterious force scrys you. After a few seconds, it ceases. A whisper sounds within your head. \"You are not ready yet. You have not said ALL your prayers today.\" The gate remains closed.")
        return

def UrlakNai_2119_MapTrigger_25_6(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(25,5)).Num == 147:
        if StuffDone["7_7"] >= 5:
            MessageBox("As you approach the gates a mysterious force scrys you. After a few seconds, the sensation ceases. A whisper sounds in your heads, \"You are worthy to pass.\" The gates slide open for you.")
            SuspendMapUpdate()
            for x in range(25, 27):
                for y in range(5, 6):
                    t = Town.TerrainAt(Location(x,y))
                    t = t.GetUnlocked()
                    Town.AlterTerrain(Location(x,y), 0, t)
            ResumeMapUpdate()
            return
        MessageBox("As you approach the gates a mysterious force scrys you. After a few seconds, it ceases. A whisper sounds within your head. \"You are not ready yet. You have not said ALL your prayers today.\" The gate remains closed.")
        return

def UrlakNai_2123_MapTrigger_6_7(p):
    if StuffDone["7_1"] == 0:
        MessageBox("This very ancient tome is a journal of some mage named Linda. It depicts some very arcane ritual. It is way over your head. However, you can tell it has something to do with serious demon summoning.")
        return

def UrlakNai_2124_MapTrigger_10_11(p):
    if StuffDone["7_1"] == 0:
        StuffDone["7_1"] = 1
        ChoiceBox("You search the desk and find a the leader of these mage\'s journal. You flip thorough it and figure out what they were doing here and why this cult was so intent upon hiding them.\n\nThe group of rebel mages was approached by the masters of this monastary and struck a pact. The mages agreed to summon a powerful demon -- a Haakai chieftain called Adze in exchange for treasure and power.\n\nThe monastary used their powers to steal several tomes on demonology that were recently discovered and on their way to the Imperial Library. The tomes depict many rituals and a journal of an ancient mage named Linda.\n\nYou have obviously stopped a major crime. You gather up the dark works. The Imperial Library would be very interested in these tomes.", eDialogPic.STANDARD, 13, ["OK"])
        SpecialItem.Give("MithralMaiden")
        return

def UrlakNai_2125_OnEntry(p):
    if StuffDone["7_2"] == 1:
        Town.MakeTownHostile()
        return
    ChoiceBox("You have entered the monastary of Urlak-Nai. It is somewhat of a forboding place. The dark basalt walls clearly do not welcome visitors. Several priests are camped around a fire, probably acting as guards. They look you over impassively.\n\nFrom your knowledge of history you know that Urlak-Nai was an ancient monastary dedicated to training priests and monks to serve the Empire. However, today it has become somewhat of a cult-like worship with bizarre tenants.\n\nYou know that no one, not even the high officials of the Empire, is allowed to view the sacred interior. You doubt you are going to be able to look around much.", eDialogPic.CREATURE, 24, ["OK"])
