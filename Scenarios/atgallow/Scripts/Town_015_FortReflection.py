
def FortReflection_270_MapTrigger_46_31(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    if StuffDone["2_1"] == 0:
        StuffDone["2_1"] = 1
        Timer(Town, 5, False, "FortReflection_286_TownTimer_5", eTimerType.DELETE)
        return

def FortReflection_274_MapTrigger_44_31(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if Game.Mode == eMode.COMBAT:
        p.CancelAction = True
        return;
    StuffDone["2_1"] = 0

def FortReflection_278_MapTrigger_31_57(p):
    if StuffDone["2_0"] == 2:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Although nobody will stop you from leaving, it would be very dishonorable to do so. You have agreed to help Dervish Montcalm. Not doing so could cost many lives. You decide to stay here.")
        return

def FortReflection_281_MapTrigger_22_27(p):
    if StuffDone["2_0"] >= 2:
        for x in range(23, 24):
            for y in range(25, 27):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[142])
        return

def FortReflection_285_MapTrigger_36_24(p):
    if StuffDone["2_3"] == 1:
        result = ChoiceBox("The shimmering portal awaits to take you to the Fort Khazar. Are you ready?", eDialogPic.STANDARD, 22, ["Leave", "Enter"])
        if result == 1:
            Animation_Hold(-1, 010_teleport)
            Wait()
            MessageBox("You take a collective deep breath and step into the portal knowing to expect a turbulent ride. You\'ve used them before in training, and didn\'t like them at all. After a painful moment, you find yourselves at your destination...")
            if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
                p.CancelAction = True
                return
            Animation_FadeDown()
            Wait()
            Party.Pos = Location(31,33)
            Party.MoveToMap(TownMap.List["FortKhazar_12"])
            return
        p.CancelAction = True
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Dervish Montcalm told you to speak with Sidor before going to Fort Khazar. You decide that it would be foolish to go on without talking to him first.")

def FortReflection_286_TownTimer_5(p):
    if StuffDone["2_1"] == 1:
        Animation_Hold(-1, 074_fireball)
        Wait()
        Animation_Explosion(Location(51,25), 0, "005_explosion")
        Animation_Hold()
        Wait()
        for ch in Town.EachCharacterInRange(Location(51,25), 1):
            ch.Damage(None, 15, 0, eDamageType.FIRE)
        Timer(Town, 5, False, "FortReflection_286_TownTimer_5", eTimerType.DELETE)
        return

def FortReflection_287_TalkingTrigger0(p):
    if StuffDone["2_0"] >= 1:
        p.TalkingText = "\"I am only allowed to open them for people on the list.\" You tell him your names and he flips through the registry. He then turns the wheel to open the gate.\n\n\"Welcome to Fort Reflection, Imperial Guardians. Dervish Montcalm wishes to see you immediately.\""
        for x in range(31, 34):
            for y in range(53, 54):
                if Maths.Rand(1,0,100) <= 100:
                    Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[148])
        return

def FortReflection_288_TalkingTrigger4(p):
    StuffDone["2_0"] = 2
    ChoiceBox("\"As you may remember, I had mentioned we are building golems to help us on the attack of Halloth\'s Citadel. The Citadel is protected by constructs called Spectral Knights. Our golems are specifically designed to fight them.\n\nUntil now, the golems have been known only to the mages in this fortress. Our mages usually take all precautions, and they did this time, when they test the golems outside. However, they got into a skirmish with some troglodytes.\n\nWe couldn\'t have anything worse happen. The patrol was sizable and our mages unprepared. The attack resulted in the Golem being captured. This occurred about four hours ago.\n\nWe have finally tracked the Golem to Fort Khazar, a Troglo research outpost deep in their territory. The Troglodytes are skilled in teleportation so getting it to that outpost was fairly easy for them.\n\nUndoubtedly, the Khazis (the Troglodyte Wizards) are studying the Golem right now. We cannot let them learn of the weaknesses of the golem lest Halloth may have an easy time taking out the Golems. In which case, their purpose is lost.\n\nWe have a portal in this fortress. I need you to use the portal, infiltrate the fort, destroy the golem, and escape. Be sure to speak with Sidor in the lab near the portal. Good luck Imperial Guardians!\"", eDialogPic.CREATURE, 118, ["OK"])

def FortReflection_289_TalkingTrigger7(p):
    ChoiceBox("\"Use the portal in the room just to the east. It will take you to Fort Khazar which is deep within their territory. We haven\'t had much time to perfect the portal targeting to the Golem\'s location, but you will be near where you need to be.\n\nOnce inside, find your way to the lab (it\'s in the northwest) and destroy the Golem. It will attack you, but there\'s not much we can do about that. Once it is destroyed you will need an escape. This is where it gets tricky.\n\nYou are too deep in Troglodyte territory to get out alive. However, the fortress is equipped with its own portal on the northeastern wing. You will need to figure out how to use it to get back here.\"\n\nSidor explains the process of setting the portal coordinates. \"The final part will allow you to penetrate the antiteleportation shield around this fortress. Don\'t forget that, or you\'ll be bounced waaaayy off course!\n\nAlso, once you\'re spotted, I\'m sure the Troglos will call for reinforcements from nearby forts so you better hurry. In addition, I\'ve prepared some potions for the raid. You can find them in the chest over there. Good luck!\"", eDialogPic.STANDARD, 22, ["OK"])
    StuffDone["2_3"] = 1
