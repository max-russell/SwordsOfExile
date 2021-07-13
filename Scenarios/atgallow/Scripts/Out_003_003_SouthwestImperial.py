
def SouthwestImperial_2624_MapTrigger_8_11(p):
    ChoiceBox("This enclosed area is home to several of the Empire\'s VIPs. Most of them are relatives of the Emperor or the homes of distinguished ministers such as the Prime Director and his top advisors.\n\nThe area contains several luxurious mansions surrounded by elegant courtyards and gardens. Also, the VIPs have easy access to the other more scenic parts of the Imperial Sector -- the Imperial Theater, the Imperial Zoo, and a forest for hunting.\n\nIt is fair to say that this is the life!", eDialogPic.CREATURE, 130, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2625_MapTrigger_8_9(p):
    ChoiceBox("The structure to the north is the Imperial Theater. The theater is an exclusive by invitation only club for the VIPs of the Empire. Needless to say, you are not on the guest list.\n\nAside from the theater where talented actors put on epic plays nightly, there are also extravagant art displays. The theater houses some of the most valuable sculptures and paintings done through the ages.\n\nAll you can do is appreciate it all from the outside. But that is not too bad for the structure is a small elegant castle with well maintained gardens with exotic statues. Perhaps one day if you get famous, you can visit the interior.", eDialogPic.STANDARD, 16, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2626_MapTrigger_8_22(p):
    ChoiceBox("This series of structures is the Imperial Zoo which houses some of the world\'s most exotic animals. Since the public can access it for free, you decide to take the tour.\n\nYou see an assortment of creatures in all habitats, magically simulated of course. For instance, you see the giant scorpions and fauna of the world\'s deserts. There is a whole assortment of forest and swamp creatures.\n\nThere is even a simulated jungle which brings to Pralgad many of the wonders of the continent Vantanas. You are impressed by nature\'s beauty. Unfortunately, the tour has to come to an end.", eDialogPic.CREATURE, 149, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2627_MapTrigger_20_11(p):
    ChoiceBox("This place is called the Sanctuary of the Gods. It is here that many of the world\'s priests are trained in the teachings of the gods before they are released to spread those words.\n\nIn the center of the sanctuary is a massive cathedral decorated with statues and plants galore. The cathedral is quite impressive and very old. Records do not indicate its time of construction. Some say that it was created with the world.\n\nHowever, most scholars believe that it was built during a very ancient time. The quandary is the level of sophistication of the structure. Such techniques are not believed to have been known about at the time.\n\nYet, the structure was somehow built and it is a mystery. Some have speculated that there was an advanced ancient civilization who built the cathedral, but those are just speculations at best.\n\nToday this place serves not only to train the private priests, but many of the Empire\'s as well. Although not trained as soldiers here, the Empire recruits them after their formal training here. In fact, most of the Imperial priests have graduated here.", eDialogPic.CREATURE, 22, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2629_MapTrigger_42_17(p):
    ChoiceBox("This is the Third Imperial Archive Hall. It contains records ranging from the early eighth century into the tenth. Currently, like the two before it, this archive is considered to be inactive.\n\nIt\'s shelves are full and as such no new records are stored here. The only real purpose this place serves is as reference for historians and scholars.\n\nYou believe the current active archive is the next one built, the fourth. However, you have heard that the shelves of that are already filling up and construction on a fifth is well underway.\n\nThis is the Empire\'s bureaucracy at its best!", eDialogPic.CREATURE, 31, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2630_MapTrigger_22_26(p):
    ChoiceBox("Although most of the magical learning on Pralgad happens in the Sorcrega Sector, to the east of here, there are several other institutions that perform such tasks. This happens to be one of them.\n\nThis mage academy, unlike Sorcrega, is specifically for the military. Although the training is excellent, it lacks the prestige of the learning in Sorcrega, a fact that the alumni of this institution resent.\n\nThe truth is most of the Imperial mages are not trained here but in Sorcrega. Although recruitment into the military is optional, many graduates decide to pursue that option as it gives good opportunities.", eDialogPic.CREATURE, 25, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2631_MapTrigger_13_36(p):
    ChoiceBox("This is one of the Empire\'s major army bases. In fact, it is one of the two stationed within the Imperial Sector. This place houses tens of thousands of soldiers who loyally serve the Empire.\n\nTheir immediate concern is the defense of the Solaria, the Imperial capital. However, there has not been a serious challenger to that in centuries. Otherwise, they serve as enforcement of laws within the Sector.\n\nOccasionally, the soldiers are called to other portions of the continent, and even to other continents, to assist with matters of concern. However, like most of the military today, this place is mostly symbolic.", eDialogPic.CREATURE, 13, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2632_MapTrigger_36_22(p):
    ChoiceBox("If the army has a base in the Imperial Sector, then the navy must have one as well. This place is the navy\'s stronghold within the Imperial Sector. This base is considered to be a minor naval base these days.\n\nBut at one time, this base was the center of naval activity around the world. That time was long ago, when the Empire still had serious contenders against it. However, since the world has been assimilated, there has been little need for maintaining this.\n\nMuch of the facility was disbanded after the use for the navy waned. Today, this area serves as a port of the Imperial Sector. The navy is largely responsible for the carrying of trade goods around the world these days.\n\nIn fact, you can see several ships leaving and arriving at the moment. The ships generally head south where the river meets the ocean and their cargo is carried to other continents.\n\nThis is business as usual in the Empire.", eDialogPic.STANDARD, 16, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2633_WanderingOnMeet0(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
