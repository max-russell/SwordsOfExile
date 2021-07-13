
def AbandonedShack_24_MapTrigger_14_15(p):
    result = ChoiceBox("Sure, the bed in this shack is old and moldy, and the blankets are filthy. It\'s still much, much better (and more secure) than sleeping outside on the ground. Do you rest for a while?", eDialogPic.TERRAIN, 230, ["Leave", "Rest"])
    if result == 1:
        MessageBox("Sure, it\'s filthy, smelly, and cold, but, for now, it\'s home. You manage to sleep for a little while and recover some of your energy.")
        if Game.Mode != eMode.COMBAT:
            Party.Age += 500
            Party.HealAll(50)
            Party.RestoreSP(50)
        return

def AbandonedShack_25_MapTrigger_16_19(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["AbandonedShack_1"].DeactivateTrigger(Location(16,19))
    MessageBox("You aren\'t sure who left this abandoned home, but, as you leave, you mutter a silent thanks to your unknown benefactors. It was, after all, infinitely preferable to sleeping out in the rain.")
