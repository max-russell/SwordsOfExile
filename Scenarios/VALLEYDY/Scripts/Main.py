def Initialise_Scenario():
    pass

def Intro_Message(p):
    ChoiceBox("Adventuring! You are on the road at last, vagabonds, travelers, looking for missions to complete, people to help, adventures to have! Soon you will be heroes, if you have anything to say about it.\n\nEven better, the Empire hired you immediately, giving you a special mission. You are to go to Skylark Vale, and investigate a minor plague or disaster or some other sort of affliction.\n\nSure, the Empire considers it seriously low priority. Otherwise they wouldn\'t send you. It\'ll probably be wrapped up in a week. Still, it\'s your first job, no doubt the first of many!\n\nYou have just arrived at Fort Talrus, an Empire outpost on the lip of Skylark Vale. Your orders are to speak with Commander Terrance, descend into the Vale to find out what the problem is, and deal with it.\n\nYou\'ve just stayed the night in your room at the fort, and have had a good night\'s sleep and a good meal. Time to go out and be heroes!", eDialogPic.SCENARIO, 5, ["OK"])


def Blinlock_26_GlobalTalkingTrigger_20(p):
    if StuffDone["2_5"] == 1:
        p.TalkingText = "\"Yeah, that tablet you brought was a huge help. It\'s all about acid use in processing certain types of ores.\" She goes on about the details for a while. Your eyes glaze."
        return
    if SpecialItem.PartyHas("StoneTablets_4"):
        p.TalkingText = "She grabs the stone tablet eagerly. She doesn\'t stay enthusiastic for long. \"What is this? It\'s on woodcarving. Why would I want this?\"\n\nDisgusted, she returns it."
        return
    if SpecialItem.PartyHas("StoneTablets"):
        p.TalkingText = "She takes the tablet you found and looks at it. Her eyes light up. \"This is perfect! Thank you so much!\" Then, after you drop a few hints, she decides to reward you.\n\nShe gives you a large pouch of gold coins, a pretty decent reward for a seemingly worthless slab of stone."
        SpecialItem.Take("StoneTablets")
        Party.Gold += 400
        return

def On_Using_SI_OpeningStone_454(p):
    if Game.Mode == eMode.OUTSIDE:
        return;
    MessageBox("You rub the stone, and it makes a strong humming sound. The sound lasts for several seconds, and stops.")
    SuspendMapUpdate()
    for x in range(0, 64):
        for y in range(0, 64):
            if Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[252]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[253])
            elif Town.TerrainAt(Location(x,y)) == TerrainRecord.UnderlayList[253]:
                Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[252])
    ResumeMapUpdate()

def On_Using_SI_HealingScepter_455(p):
    MessageBox("You wave the scepter, and a warm light emerges from its tip. As the light washes over you, you feel a pleasant, tingling sensation.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) - 1))

def On_Death_Of_Gremlord_456(p):
    MessageBox("You have slain the ferocious, peculiar gremlord. That\'s another mess left behind by the masters of the School of Magery that you\'ve had to clean up.")
