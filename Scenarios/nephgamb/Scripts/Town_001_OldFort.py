
def OldFort_13_MapTrigger_10_16(p):
    if StuffDone["1_8"] == 250:
        return
    StuffDone["1_8"] = 250
    TownMap.List["OldFort_1"].AlterTerrain(Location(10,16), 1, None)
    TownMap.List["OldFort_1"].DeactivateTrigger(Location(10,16))
    MessageBox("The garrison quarters are spotless after the morning inspection. To save work, you usually just throw the garbage through the window onto the trash pit.\n\n")

def OldFort_14_MapTrigger_23_7(p):
    if StuffDone["1_0"] == 250:
        return
    StuffDone["1_0"] = 250
    TownMap.List["OldFort_1"].DeactivateTrigger(Location(23,7))
    TownMap.List["OldFort_1"].DeactivateTrigger(Location(26,5))
    MessageBox("Somebody has left his weapon behind. Finders keepers.")
    Party.GiveNewItem("BronzeBroadsword_45")

def OldFort_15_MapTrigger_10_7(p):
    if p.Origin == eCallOrigin.SEARCHING: return
    if StuffDone["1_3"] == 250:
        return
    StuffDone["1_3"] = 250
    ChoiceBox("This fort has seen better days. Up until a few years ago, your country was harassed by bandits and bands of alien races attacking the towns and trade caravans. Several guard posts were put up to protect the trade route through Brattaskar into Exile.\n\nThen, a new reign in Myldres gathered the towns to repulse the invaders. After a short, bloody period of war, peace settled in Chimney.\n\nWhich in turn made the Brattaskar Posts a dull place.\n\nThe small garrison of this post has given up on maintaining the fort. The walls are falling apart and empty barracks are gathering dust. Last month, a section of the perimeter wall fell in, and you have not had time to repair it yet.\n\nYou can see the two soldiers who were supposed to rebuild the wall lounging in front of the kitchen hall. To the north you see Mathias, the Captain of the garrison, conferring with a visitor.", eDialogPic.TERRAIN, 232, ["OK"])

def OldFort_16_MapTrigger_21_9(p):
    MessageBox("Stairs lead up to the lookout tower over the front gate")

def OldFort_17_MapTrigger_5_6(p):
    MessageBox("These shelves are the archives of the fort. Thick books containing troop orders and patrol reports give the impression of hectic activity. Closer inspection, however, reveals that the books all date a few years back and have a thin coat of dust on them.")

def OldFort_18_MapTrigger_5_7(p):
    result = ChoiceBox("Captain Mathias evidently has plenty of time for reading. His personal bookshelves contain a variety of literature and several scientific texts. If you have nothing better to do, many of the titles look tempting.", eDialogPic.TERRAIN, 135, ["Leave", "Read"])
    if result == 1:
        ChoiceBox("You pick a book that turns out to be a textbook on cave geography. You read a page at random.\n\n\"The lands of Chimney give an interesting lesson on meteorology. The human settlements are actually placed on a ledge high up on the wall of the slithzerikai caverns.\n\n\"These caves provide just the warm, damp environment that cold blooded lizards enjoy, considerably warmer than the caves of central Exile, high above.\n\n\"At a point in the cave ceiling above the Chimney ledge, there is a wide opening. This tunnel connects to the caves above, forming a vertical chute, two thousand meters high.\n\n\"The warm air that rises from the slith jungles is sucked into the chute, causing a continuous breeze through the human lands. The draft functions like a pipe, thus giving Chimney its name.\n\n\"Moreover, when the damp airstream encounters the cold air of Exile, it often releases its watery content, producing a peculiar effect: Indoor rain. This makes the soil of Cimney very fertile.\"", eDialogPic.TERRAIN, 135, ["OK"])
        return

def OldFort_20_MapTrigger_26_12(p):
    if StuffDone["1_6"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Leaving your post without permission from your commanding officer is strictly forbidden.")
        return

def OldFort_25_MapTrigger_24_8(p):
    if StuffDone["1_9"] == 250:
        return
    StuffDone["1_9"] = 250
    TownMap.List["OldFort_1"].AlterTerrain(Location(24,8), 1, None)
    TownMap.List["OldFort_1"].DeactivateTrigger(Location(24,8))
    MessageBox("Thes room has been out of use for some time. Various objects lie scattered about, some of which may be useful.")

def OldFort_26_MapTrigger_8_5(p):
    if StuffDone["1_7"] == 250:
        return
    StuffDone["1_7"] = 250
    TownMap.List["OldFort_1"].DeactivateTrigger(Location(8,5))
    MessageBox("Papers and rubble fill the desk. One item catches your eye, however. It is a small cone made of iron, attached to a leather strap. On a hunch, you pocket it.")
    SpecialItem.Give("Ironcone")

def OldFort_31_MapTrigger_25_11(p):
    if StuffDone["1_2"] >= 1:
        return
    result = ChoiceBox("For a moment you thought you could hear whispering and the sound of steps in the gravel from the hole in the east wall. You strain your ears, but the conversation of the other soldiers drown the sounds.\n\nDo you feel ready for adventure, or do you return to your friends for some more cosy relaxation?", eDialogPic.TERRAIN, 95, ["Leave", "Approach"])
    if result == 1:
        if StuffDone["1_1"] == 250:
            return
        StuffDone["1_1"] = 250
        MessageBox("You move towards the gap, but do not get far. Sensing that they have been discovered, the whisperers decide to reveal themselves.\n\nA shout rises from the lookout as a small band of sliths climb through the hole in the east wall. Surprise turns to horror when the lizard men gurgle their battle cries and attack. You recoil and prepare to meet their charge.")
        if StuffDone["1_2"] == 250:
            return
        StuffDone["1_2"] = 250
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(25,11))
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(24,11))
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(24,12))
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(24,13))
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(24,14))
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(24,15))
        TownMap.List["OldFort_1"].DeactivateTrigger(Location(25,15))
        Town.PlaceEncounterGroup(1)
        if Game.Mode == eMode.COMBAT:
            p.CancelAction = True
            return
        Party.Reposition(Location(19,13))
        p.CancelAction = True
        return
    p.CancelAction = True

def OldFort_41_TownTimer_12(p):
    MessageBox("The battle seems hopeless. Pace by pace, your side is forced back. Suddenly it is decided: A slith spear strikes Captain Mathias in the chest, throwing him to his knees.\n\n\"Retreat!\" the Captain cries, \"retreat, boys! Run away, get help! Tell the Commander in Myldres of this!\" These are his last words. As your leader collapses, you eye the hole in the east wall. If only you could get out in time...")
    StuffDone["1_6"] = 1
    for n in range(Town.NPCList.Count-1, -1, -1):
        npc = Town.NPCList[n]
        if npc.Record.ID == "Captain_14": Town.NPCList.Remove(npc)

def OldFort_42_ExitTown(p):
    if p.Dir.IsNorth or p.Dir.IsWest or p.Dir.IsSouth or p.Dir.IsEast:
        ChoiceBox("You throw yourselves desperately through the gap in the wall and run away blindly from the anguished screams of those who were less lucky. The sliths do not bother to follow. They put all their effort into butchering the rest of the garrison.\n\nYou drop exhausted to the ground on the top of a small hill, half a mile away from the fort. It appears that nobody else made it out. Tears fill your eyes as you watch the sacking of your home.\n\nA thin line of smoke rises from the barracks. It grows, as the buildings one by one are engulfed by flames. Sliths swarm around, trying to rob the fort of its loot before the fire claims it.\n\nScattered over the court you see the bodies of your friends. Brave Mathias, Thomes and the one-armed Wilbur. All are lost in this sudden, inexplicable raid.\n\nWho are these ferocious sliths? The slithzerikai are a peaceful people, they have been friends of Chimney for as long as you can remember. Why this sudden attack?\n\nPeople died to help you get away. Now it is time to honour their sacrifice. You must obey Mathias? last command and bring news of this tragedy to the famous Commander Groul in Myldres.", eDialogPic.CREATURE, 48, ["OK"])
        MessageBox("You turn away from the disheartening sight, but its impression never quite leaves you. For the rest of your lives you will be taunted by this memory. Your friends dying, your home burning and your own searing sense of impotence and shame.\n\nIn the coming days, you encounter many trials and hard choices. You are tempted by great rewards, but always, and behind everything you do lies the force of your obligation to your lost comrades.")
        ChoiceBox("PART 1: The Grim Messengers", eDialogPic.STANDARD, 6, ["OK"])

def OldFort_43_CreatureDeath6(p):
    if StuffDone["1_4"] == 250:
        return
    StuffDone["1_4"] = 250
    MessageBox("The slith leader, a huge lizard wielding his traditional battle spear with terrifying grace, falls bleeding to the ground. With his last breath he mutters a silent prayer, clutching a scale necklace to his chest.\n\nDeath relaxes his muscles, and he drops the holy ornament to the ground. You take a deep breath of relief as you pick up the necklace. But it turns out that your problems have only just begun. A sound makes you whirl...")
    SpecialItem.Give("SlithCharm")
    if StuffDone["1_5"] == 250:
        return
    StuffDone["1_5"] = 250
    MessageBox("A new wave of attackers floods through the open front gates. This is definitely not going your way.")
    Town.PlaceEncounterGroup(2)
    Timer(Town, 2, False, "OldFort_41_TownTimer_12", eTimerType.DELETE)
