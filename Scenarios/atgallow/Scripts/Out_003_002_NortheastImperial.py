
def NortheastImperial_2515_MapTrigger_38_19(p):
    if StuffDone["12_4"] >= 2:
        StuffDone["12_2"] = 3
        if StuffDone["13_3"] == 250:
            return
        StuffDone["13_3"] = 250
        ChoiceBox("You step outside of the Spire and look back on the destruction you have caused. The once awesome structure is now a pile of smoldering rubble. Trapped within are the over 6,000 members of the Urlak-Nai.\n\nMost are probably dead, but some may still be alive in the wreck. Most likely, those survivors will also perish. You cannot help but to feel guilt for what you have done. What if you had not taken the Onyx Scepter you now possess?\n\nCould an alternate solution have been devised and lives spared? You will probably never know for sure. You will just have to come to grips with what you have done. You have killed many before, but those were hostile. These were innocent civilians.\n\nThe only thing you can take comfort in is now you have a chance against that Nethergate. If that portal were allowed to be completed, there is no telling what destruction Auspire could bring forth.\n\nYou must go onward to Fort Nether!", eDialogPic.STANDARD, 13, ["OK"])
        ChoiceBox("Not so fast! Although Tyrann may have \"forgiven\" you, many of his followers do not. In the wake of the destruction of their home and religion, several survivors have arrived to avenge their cause.\n\nThere is no hope at reasoning with them; they only have a thirst for blood -- and that blood be yours!", eDialogPic.CREATURE, 24, ["OK"])
        WorldMap.SpawnNPCGroup("Group_3_2_4", p.Target)
        return

def NortheastImperial_2516_MapTrigger_5_18(p):
    MessageBox("This structure is the second Imperial Hall of Archives. It stores records and important historical documents from about the late fourth century to the end of the seventh. This is one big house of paper!")
    p.CancelAction = True

def NortheastImperial_2517_MapTrigger_6_24(p):
    MessageBox("This section of shops sells all sorts of interesting foods, exotic to mundane. They have clearly been exported from around the world and are, of course, quite expensive.")
    OpenShop("Shop_Items_Outside_9_3_2")
    p.CancelAction = True

def NortheastImperial_2518_MapTrigger_10_26(p):
    MessageBox("Most of these shops sell worthless items, at least to you. There is one for pets, another for plants, and the sort. However, the one with alchemetical supplies may be of use to you.")
    OpenShop("Shop_Items_Outside_11_3_2")
    p.CancelAction = True

def NortheastImperial_2519_MapTrigger_7_27(p):
    MessageBox("This section of shops consists of things like toys, furniture, and antique shops. The only place of real use to you is a mage peddling Piercing Crystals. He charges a hefty price, but his product is of value.")
    OpenShop("Shop_Items_Outside_13_3_2")
    p.CancelAction = True

def NortheastImperial_2520_MapTrigger_7_23(p):
    MessageBox("Among the shops you come to an alchemist. Unfortunately, his selection of brews contain little for the adventuring type and more for the practical user. Such items are laxatives, and cough syrups. But he does have a collection of poisons.")
    OpenShop("Shop_Items_Outside_15_3_2")
    p.CancelAction = True

def NortheastImperial_2521_MapTrigger_27_9(p):
    MessageBox("This fortress bridges the border of the Imperial Sector and the Nelon Sector. You present your papers and are allowed passage.")
    Party.Reposition(Location(171, 100))
    p.CancelAction = True

def NortheastImperial_2522_MapTrigger_27_5(p):
    MessageBox("This fortress bridges the border of the Imperial Sector and the Nelon Sector. You present your papers and are allowed passage.")
    Party.Reposition(Location(171, 106))
    p.CancelAction = True
    if StuffDone["54_0"] == 250:
        return
    StuffDone["54_0"] = 250
    WorldMap.DeactivateTrigger(Location(156,197))
    ChoiceBox("You arrive at the Imperial Sector, the center of the Empire and the entire world. It is within this Sector that tens of thousands of decisions are made each day about public policy by various officials and bureaucrats.\n\nIt is here where most of Pralgad\'s soldiers (including you) are trained. Armies are housed within the sector to help maintain security and order. The protection of the capital of the Empire, Solaria, is paramount.\n\nThe Imperial Sector is probably the most densely populated sector in the world. Census figures say that about five million people live and work within the sector with jobs ranging from administration to clerical to maintenance.\n\nThe size will soon become apparent as you will see the many residential areas that dot the landscape. Each has its own name, but largely these dwellings are insignificant.\n\nThe Imperial Sector is also the largest consumers of resources. The upper class residents here tend to be the wealthiest in the world. The chief product of the Imperial Sector is policy, and little else also making it the most dependent.\n\nWelcome to the heart of the Empire!", eDialogPic.CREATURE, 130, ["OK"])

def NortheastImperial_2523_MapTrigger_19_20(p):
    if StuffDone["41_5"] == 250:
        return
    StuffDone["41_5"] = 250
    WorldMap.DeactivateTrigger(Location(163,116))
    MessageBox("This place is the Cemetery of Legends. Here the ashes of heroic figures throughout history are stored in monuments that dot the gardens. The structure to the north is the Tomb of Emperors.")

def NortheastImperial_2524_MapTrigger_19_16(p):
    MessageBox("This tower is the Tomb of Emperors. The ashes of most of the Imperial monarchs have been laid to rest for eternity within this tower. The place is only open on two occasions. One is the first day on the month of Empire every year.\n\nThat day is the death of the first Emperor, Sol I. The other is on the days of funerals for the Emperors where visitors may pay their last respects. Otherwise, like today, the place is magically sealed.")
    p.CancelAction = True

def NortheastImperial_2525_MapTrigger_17_28(p):
    ChoiceBox("You know this place all too well. You return to the place where you spent the first year of your career as soldiers before being transferred to the Agran Sector. That time was not good memories.\n\nYou remember having to get up at odd hours to perform grueling exercises and training scenarios. The barracks were less than adequate and the meals were downright awful.\n\nThe training course is basically the Ermarian equivalent to the Abyss. Filled with thick forests, swamps, steep hills, and rough terrain, the place is not one you wish to return to anytime soon. You were glad to finally be free of it.\n\nThe same goes for the rest of this place. You decide to leave this place to the past where it belongs.", eDialogPic.CREATURE, 13, ["OK"])
    p.CancelAction = True

def NortheastImperial_2526_MapTrigger_26_26(p):
    ChoiceBox("This is, or shall be, the Fifth Imperial Hall of Archives. The construction was started a few years ago and shall continue into the next decade. Progress is slow, and funding for the project is low. However, there is no need to hurry.\n\nFrom what you have heard, the fourth Archive Hall still is expected to suffice for another thirty years or so. After which, it, like its three predecessors, will be filled with millions of worthless historical documents stored for eternity.\n\nYou sometimes wonder why the Empire goes to such effort to maintain these Archive Halls. Many of them contain information that is centuries old. Most of it has not been viewed since the day it was placed in the archives.\n\nYet, the Empire continues to house the information on the off chance that at one point in the future, some bureaucrat or scholar will actually require it. As unlikely as such cases may be, that is the Empire\'s justification for using its resources here.\n\nThrough its twelve hundred year history, the Empire has used literally billions of pieces of paper. Most of it is destroyed after some time, but the fraction that is deemed \'important\' is preserved and uses space.\n\nYou wonder how long it will be before the Empire will build the Sixth Imperial Hall of Archives.", eDialogPic.CREATURE, 31, ["OK"])

def NortheastImperial_2527_MapTrigger_30_36(p):
    ChoiceBox("This place is called the Imperial Bureaucratic Institution. It is nicknamed several things, but two that come to mind are the humorous term \'Paper Palace\' and the more serious one, the \'Second Empire\'.\n\nThis place serves several purposes. One is as the recruiting corps for the imperial bureaucracy. The world\'s career bureaucrats are trained within these walls in all the practices and rituals set in place by other bureaucrats a long time ago.\n\nThe humorous nickname of the \'Paper Palace\' refers to the output of this place. Tens of thousands of pieces of paper are consumed here and transferred into various Imperial decrees and such by the beehive of bureaucrats.\n\nThe other term of the \'Second Empire\' describes its function. The chief export, aside from paper, of this place is law. Major policy decisions are made by the Throne and its ministers.\n\nHowever, minor policy decisions such as the logistics of carrying out major policies are made here. The bureaucracy has a lot of power in decision making in the real world, one that has not escaped the minds of politicians everywhere.\n\nFor there is a saying that to alienate a bureaucrat is to commit political suicide. Indeed this place is where the government busywork commences with all its departments of interior, agriculture, commerce, etc.", eDialogPic.CREATURE, 31, ["OK"])
    p.CancelAction = True

def NortheastImperial_2528_MapTrigger_5_33(p):
    MessageBox("This place houses the embassies where functionaries from various sections of the world come to lobby their needs. Footing in the Imperial Sector is critical to maintaining ones interest in the world.")
    p.CancelAction = True

def NortheastImperial_2529_MapTrigger_7_45(p):
    ChoiceBox("This place is the Imperial Center of Defense. The high up Dervishes of the Imperial Army and Navy live within this place. Inside they carry out discussions to decide the activities of the Imperial Armed Forces throughout the world.\n\nThis structure is the apex of martial authority and is critical in the shaping of Imperial policy. No major decision is made without the consultation of the military. That is how much power rests here.\n\nDespite this power, the structure of the Empire has remained for a long time. The reasoning lies in two things. The first is that the armed forces keeps the people in line. The second is that the tradition of the Empire keeps the military in line.\n\nAll attempts at sheer military takeover have resulted in rebellion resulting in the reinstatement of the old system. It is the legitimacy and the tradition that keep the Emperor and his Ministers safe from the blades of power hungry Dervishes.\n\nHowever, in recent centuries the power of the military has dwindled. Although it is still a powerful faction in Imperial politics, it lacks the force to seriously disable policies made by Solaria.", eDialogPic.CREATURE, 17, ["OK"])
    p.CancelAction = True

def NortheastImperial_2530_MapTrigger_9_23(p):
    MessageBox("Among all the various stores, you encounter a wizard. He is selling an assortment of rings, and the enchanted kind! You decide to have a look.")
    OpenShop("Shop_Items_Outside_26_3_2")
    p.CancelAction = True

def NortheastImperial_2531_MapTrigger_10_24(p):
    MessageBox("Most of these stores are useless to you. However, you discover a wand shop with some interesting looking goods.")
    OpenShop("Shop_Items_Outside_28_3_2")
    p.CancelAction = True

def NortheastImperial_2532_MapTrigger_9_27(p):
    MessageBox("Among all of the various stores, you encounter a priest of some religion or another. He offers to teach you a certain prayer, intrigued, you ask for more information.")
    OpenShop("Shop_Priest_Outside_30_3_2")
    p.CancelAction = True

def NortheastImperial_2533_WanderingOnMeet0(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return

def NortheastImperial_2537_SpecialOnWin0(p):
    MessageBox("Once again, blood has only resulted in more blood. You leave this gruesome site behind. Enough blood has been spilled today.")
