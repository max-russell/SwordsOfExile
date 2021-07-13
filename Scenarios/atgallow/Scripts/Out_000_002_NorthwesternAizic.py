
def NorthwesternAizic_2475_MapTrigger_11_28(p):
    ChoiceBox("This pier was placed as a memorial to the first settlers of Pralgad from the Aizonic Empire. Simply called \"Landing Point\", this is the place the first explorers from Aizo landed on the shores of Pralgad.\n\nWhen they arrived they discovered a wild land of all sorts of dangers. There were barbaric tribes of Humans (historians argue how the native humans arrived on Pralgad) and Nephilim. The continent was home to all kinds of wild creatures.\n\nThe most advanced civilization at the time were the Troglodytes who ruled this section of the continent. They welcomed the settlers with open arms, a mistake they would later regret after the Empire waged campaigns against them.\n\nSettlement of this new land by the Aizonic Empire was slow at first. The rulers at the time did not want to take the risks of settling a new bizarre land. However, as valuable minerals were discovered, settlement began to pick up.\n\nCenturies later, the Aizonic Empire began to weaken. Poor decisions and corrupt rulers led to massive revolts that led to the downfall of the Empire. Pralgad became a safe haven for all the conflict on Aizo and prospered further.\n\nHowever, states and factions began to form (somewhat representative of today\'s sectors) and wars broke out on Pralgad also. That was until the rise of Sol I, who was able to unite the states into the sapling of the Empire of today.", eDialogPic.STANDARD, 16, ["OK"])

def NorthwesternAizic_2476_MapTrigger_15_16(p):
    if StuffDone["41_6"] == 250:
        return
    StuffDone["41_6"] = 250
    WorldMap.DeactivateTrigger(Location(15,112))
    ChoiceBox("Several dead bodies with severe battle wounds rest on the ground here. They are quite decayed and emit a horrid stench. Your guess is they are weeks old.\n\nEven though they look like soldiers, they are clearly not of the Empire. They are all wearing armor with a red spear painted on them, unlike the Empire\'s Sword and Sun Emblem. You wonder who these men were.\n\nLooking around, you see broken arrows, craters from fireball spells, a shattered shield, and all the other signs of battle. There was obviously a battle here, but who these men were and why the battle took place remain a mystery.", eDialogPic.STANDARD, 1027, ["OK"])

def NorthwesternAizic_2477_MapTrigger_18_11(p):
    result = ChoiceBox("This cavern entrance has a red spear emblem painted above it. You look around and listen for any signs of activity, but find none. First the battle and now this lair. Things are kind of eerie.\n\nPerhaps you should take the next step and take a look inside this lair to find out what is going on.", eDialogPic.TERRAIN, 194, ["Leave", "Enter"])
    if result == 1:
        if StuffDone["41_7"] == 0:
            result = ChoiceBox("You proceed into the cavern. It slopes sharply upward. The first thing you find is a kind of guardpost. The bodies of several guards are lying on the ground. The structure has been shattered by explosives, so passing is no problem.\n\nWhat is beyond is a horrific sight. There is a kind of small town built within this cavern. There are bodies lying everywhere slain by all sorts of methods typical of combat. All of them are wearing that red spear insignia.\n\nA search of the buildings turns up little. Dressers and containers have been opened and looted. Whoever was here did a very thorough job of this.\n\nHowever, it seems they had missed one chest. It remains closed for some reason. Perhaps it was looted as well and then closed, maybe they couldn\'t get it open, or perhaps it was forgotten about.\n\nNow that you are here, you can try to open the chest and take what is inside.", eDialogPic.TERRAIN, 138, ["Leave", "Open"])
            if result == 1:
                Animation_Hold(-1, 005_explosion)
                Wait()
                Animation_Hold(-1, 060_smallboom)
                Wait()
                Animation_Hold(-1, 060_smallboom)
                Wait()
                Party.Damage(Maths.Rand(6, 1, 5) + 15, eDamageType.UNBLOCKABLE)
                Wait()
                MessageBox("Oops! There was a reason they left this chest untampered. They must have known that it was trapped. Too bad you did not have that same foresight. You open the chest and it explodes. You are almost buried by the cave in! Fortunately, you make it out alive.")
                StuffDone["41_7"] = 1
                p.CancelAction = True
                return
            p.CancelAction = True
            return
        MessageBox("Returning to this base is only a waste of time. Little has changed since your last debacle here. The only thing different is the bodies are a bit more decayed than last time and the smell is a whole lot worse.")
        p.CancelAction = True
        return
    p.CancelAction = True

def NorthwesternAizic_2478_MapTrigger_23_39(p):
    MessageBox("This is a small farming community of about fifty people that grow the crops providing for much of Vanguard\'s food needs.")
    p.CancelAction = True

def NorthwesternAizic_2480_MapTrigger_30_40(p):
    MessageBox("This small town is called Pleasant Field. It is a suburb of Vanguard and mostly residential. There is little of interest here.")

def NorthwesternAizic_2482_MapTrigger_31_40(p):
    MessageBox("This small town is called Pleasant Field. It is a suburb of Vanguard and mostly residential. However, there is a fletcher here with some very interesting supplies.")
    OpenShop("Shop_Items_Outside_16_0_2")
    p.CancelAction = True

def NorthwesternAizic_2483_MapTrigger_30_41(p):
    MessageBox("This small town is called Pleasant Field. It is a suburb of Vanguard and mostly residential. Every town has at least one area to purchase food. You are currently in a farmer\'s market and decide to take a look around.")
    OpenShop("Shop_Items_Outside_18_0_2")
    p.CancelAction = True

def NorthwesternAizic_2484_MapTrigger_9_39(p):
    result = ChoiceBox("You approach a small tower. The exterior is decorated with small gardens growing all sorts of herbs and flowers. It is quite a nice place. You near the door and it swings open for you! Some mage must live here.\n\nYou step inside and find yourself in a small antechamber. Ahead is another door which remains closed. To your right is an alcove in the wall with a table to set items on. To your left are some nice paintings.\n\nSuddenly there is a voice. \"By decree of the owner, there are no weapons allowed past this point! Place any weapons you have inside the alcove. They shall be kept safe there.\"\n\nDo you place your weapons in the alcove. It could be some kind of trap.", eDialogPic.TERRAIN, 197, ["Accept", "Refuse"])
    if result == 0:
        ChoiceBox("You do as instructed and place your weapons on the table in the alcove. The voice chimes, \"Thank you! The owner welcomes you to her home.\" The next door opens as the first door slams shut.\n\nYou look at your weapons and they are gone! Have you been tricked? The only way to find out is to proceed. You enter another larger room and encounter a woman in her fifties in the archmage\'s purple robes. You notice she has a red spear sewn in to them.\n\n\"Welcome soldiers! It is good to see that you were willing to comply with my rules. Most of your kind refuse to surrender their weapons. You must understand, that because of my affiliation I must be careful.\"\n\nShe points to the red spear on her robes upon saying the last sentence. You ask about it. \"Ah! I see, you\'re not from around here. Then I shall explain. The Red Spear is a resistance organization against the cruel practices of the Empire.\n\nThe spear is Red to represent all of the blood and injustice done by the Empire throughout the ages. We believe in the the ancient theories called democracy where the people get to choose their rulers.\" Such a concept is foreign to you.\n\n\"I know it sounds strange. We are so used to being ruled by his eminence high atop Solaria, that we cannot comprehend any other way. Most in the Red Spear have received some kind of mistreatment by the Empire in one way or another.\"", eDialogPic.CREATURE, 28, ["OK"])
        ChoiceBox("\"I myself spoke out against the corruption of the establishment in Sorcrega about fifteen years ago. Needless to say, I lost my lucrative teaching position and was blacklisted by the Empire. The Empire turned the other cheek against corrupt officials.\n\nSo I decided to move out here, far away from those pinheads at Sorcrega. I periodically offer instruction in magic, make potions, scrolls, and wands and sell them in the city. I do odd jobs and such to make a living.\n\nWhen the Red Spear rose up about a year ago, I was one of the first to join. I taught many of their members the arts of magic and such. However, my affiliation has scaled back ever since they began to partake in violence.\n\nI do not support the beliefs of Dervish Lennon, a former Empire Dervish and leader of the Red Spear. He believes that violence is necessary to achieve a more peaceful world. I am more of a pacifist, so my support has become minimal.\n\nYet, I still remain a member as I support the ideology of the group. Of course, that makes me guilty of treason. However, most people don\'t care because I haven\'t really harmed anyone directly.\n\nAnyways, I have some project that I\'m working on and I\'m falling behind. It was nice talking to you. Your weapons will be where you left them. Thanks!\" With that abrupt goodbye, you leave. Of course, you remember to take your weapons.", eDialogPic.CREATURE, 28, ["OK"])
        p.CancelAction = True
        return
    elif result == 1:
        MessageBox("You decide that it would be best to keep your items. The voice asks again about thirty seconds later and every subsequent thirty second interval. You do not obey and the next door remains locked.")
        p.CancelAction = True
        return

def NorthwesternAizic_2485_MapTrigger_33_7(p):
    result = ChoiceBox("You approach a small hut. There are several stacks of chopped wood of fairly high quality just beside the wall of the hut. The sign above the door says, \"WELCOME! FRANK\'S FINE WOODWORKING\"\n\nCare to go inside?", eDialogPic.TERRAIN, 190, ["Leave", "Enter"])
    if result == 1:
        ChoiceBox("You walk inside and meet, presumably, Frank. He is sitting at his desk, carving a wooden figure. It appears to be some kind of small animal, a squirrel perhaps. He smiles as you approach.\n\n\"Good afternoon, I am Frank. What brings you to my fine store, soldiers.\" You just tell him you were on patrol. He smiles. \"That\'s good. I\'m glad to see there are more patrols out these days in the wake of the rebels.\"\n\nYou inquire about the rebels. \"Ah! They\'re a small band, nothing serious. I think they call themselves the Red Spear if I remember right. Some of them came by the other week and asked if I was interested in joining.\n\nTold them I wasn\'t interested. I didn\'t want to take part in their activities. Don\'t really see how they hope to accomplish anything. They are more a group of idealists than anything else.\n\nIt is a pity that they had to turn violent. Last time I was in Vanguard I overheard some soldiers talking. They said they just came back from a raid of a hidden lair up in the hills. Killed a whole bunch of them.\n\nIt\'s too bad too. Most of them are just kids in their early twenties, idealist types you know. But I guess they have to learn that no one fights the almighty Empire. Anyway, are you here to buy anything.\" You decline the offer and hearing enough, depart.", eDialogPic.CREATURE, 3, ["OK"])
        p.CancelAction = True
        return
    p.CancelAction = True

def NorthwesternAizic_2486_MapTrigger_44_19(p):
    MessageBox("There is a finely sculpted statue out here in the middle of this large plain. It looks kind of old and worn by the weather. You wonder why it\'s here.")

def NorthwesternAizic_2487_MapTrigger_37_30(p):
    if StuffDone["41_9"] == 250:
        return
    StuffDone["41_9"] = 250
    WorldMap.DeactivateTrigger(Location(37,126))
    ChoiceBox("Along this road are about ten carts backed up from both directions on their way to and from the city. You move to the center to see what is going on. You find several young people sitting in the road obstructing traffic.\n\nThey are chanting, \"Down with Imperial corruption! Down with business!\" over and over. You approach them and demand that they clear the road. They all laugh at you and continue chanting.\n\nAnother three or so carts arrive and the merchants are getting quite angry. One of merchants shouts, \"Damned traitors!\" as he hacks at one of the young men sitting in the road with a shovel.\n\nHe hits him and knocks him out. The others rise up, but you immediately rush to the scene and quell the situation. Another two carts arrive. You wonder where the other patrols are! You really don\'t want to slaughter many people over this.\n\nThis is definitely a stressful situation. You have carts full of goods arriving every minute and complaining merchants. If you try to move them with force, that could lead to a riot. You hope soldiers show up soon so peaceful action can be carried out.\n\nThere are now about ten carts full of goods on each side and no patrols in sight.", eDialogPic.CREATURE, 2, ["OK"])
    Animation_Hold(-1, 012_longbow)
    Wait()
    Animation_Hold(-1, 098_missilehit)
    Wait()
    Animation_Hold(-1, 029_monsterdeath2)
    Wait()
    ChoiceBox("Suddenly you hear a scream! One of the merchants falls to the ground, slain by an arrow piercing his heart. Suddenly, arrows begin to fly through the entire scene as archers appear from behind the trees.\n\nFrom a distance, you can barely make out the red spear on their uniforms. Then you notice the young people in the road have risen and are ready to fight, many of them brandishing weapons. It appears this was a staged event by rebels.\n\nThey wanted to lure as many merchants as possible into one area, slay them, and take their loot to add to their coffers. Things are happening very fast, you draw your weapons and prepare to defend the merchants.", eDialogPic.CREATURE, 20, ["OK"])
    WorldMap.SpawnNPCGroup("Group_0_2_4", p.Target)

def NorthwesternAizic_2488_WanderingOnMeet0(p):
    MessageBox("You are approached by a sizable group of people in uniform. You immediately notice  they lack the the Sword and Sun insignia instead having a red spear. They shout some obscenities and then attack!")

def NorthwesternAizic_2490_WanderingOnMeet2(p):
    MessageBox("You have heard there has been an outbreak in hostile Troglodyte activity in this area lately. However, it is unusual to spot patrols this close to the city. Nevertheless, they take on what they consider an \'easy target\', deciding to challenge you.")

def NorthwesternAizic_2491_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NorthwesternAizic_2492_SpecialOnWin0(p):
    MessageBox("Unfortunately this event turned into a massacre. Thankfully you were here to save the lives of many of the merchants. You receive much thanks as they tend to their wounds and move off.\n\nFinally, a patrol of soldiers arrives. You tell them what happened. You leave it to them to clean up this mess.")
