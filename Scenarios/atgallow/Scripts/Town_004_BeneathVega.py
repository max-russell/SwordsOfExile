
def BeneathVega_27_MapTrigger_50_55(p):
    if StuffDone["0_6"] == 0:
        result = ChoiceBox("You enter a large room with several members of the cultists sitting at tables, drinking away. One of the red robed men waves you over. \"Aye comrades! Come and drink with us. To victory!\"\n\nYou are offered mugs of beer. However, you notice the red robed man is watching you very carefully. Your instincts tell you to refuse at the risk of offending the cultists. Do you drink with the cultists?", eDialogPic.CREATURE, 23, ["Drink", "Refuse"])
        if result == 0:
            MessageBox("You drink the beer. Within minutes, you begin to feel very tired. You realize that the beer was spiked with poison! However, it\'s too late. You fall asleep and they tear you apart. At least you don\'t feel anything.")
            for pc in Party.EachAlivePC():
                if pc.LifeStatus == eLifeStatus.ALIVE:
                    pc.Kill(None, eLifeStatus.DUST, True)
                    Wait()
            return
        elif result == 1:
            MessageBox("You reluctantly refuse. The robed man replies, \"Ah! So we have intelligent spies thinking they could infiltrate our lair. Kill them!\" It\'s a trap! They\'ve known all along. It looks like you\'ll have to fight.")
            StuffDone["0_6"] = 1
            TownMap.List["BeneathVega_4"].Hidden = False
            Town.MakeTownHostile()
            Party.OutsidePos = Location(163, 211)
            return
        return

def BeneathVega_30_MapTrigger_53_57(p):
    if StuffDone["0_6"] == 1:
        Town.MakeTownHostile()
        Party.OutsidePos = Location(163, 211)
        return

def BeneathVega_31_MapTrigger_58_57(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading up.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(8,17)
    Party.MoveToMap(TownMap.List["Vega_3"])

def BeneathVega_32_MapTrigger_4_27(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(57,32)
    Party.MoveToMap(TownMap.List["OldEmpireOutpost_5"])
