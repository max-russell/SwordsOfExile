
def NelonMountains_2363_MapTrigger_4_11(p):
    if StuffDone["27_4"] == 250:
        return
    StuffDone["27_4"] = 250
    WorldMap.DeactivateTrigger(Location(196,11))
    WorldMap.DeactivateTrigger(Location(197,11))
    MessageBox("Moving hard against the current, you find yourself in a large freshwater lake. This is truly one of the most amazing sites you\'ve ever seen in your life. You\'ve heard people speak of this place, but no words can truly describe the splendor.\n\nAll around you are glaciers melting to form many of the rivers of Pralgad. You can imagine how much ice must melt to keep the rivers flowing. Truly amazing.")

def NelonMountains_2365_MapTrigger_26_29(p):
    if StuffDone["53_3"] == 0:
        ChoiceBox("As you try to row forward, several spirits rise from the river. They speak in a unisoned haunting voice, \"Arvarrin demands tribute! Head east mortals and pay your respects to the goddess of these mountains.\"\n\nNo matter how hard you try to row to the north, you seem to be making zero progress. It appears you will have to appease the demands of this Arvarrin.", eDialogPic.CREATURE, 54, ["OK"])
        p.CancelAction = True
        return

def NelonMountains_2367_MapTrigger_16_19(p):
    p.CancelAction = True
    if StuffDone["53_4"] == 0:
        result = ChoiceBox("You come to a small isolated tower occupied by a lone elderly Slith mage. The Slith is wrinkled and seems to have scales of a pale grayish green. He welcomes you to his tower and you tell him about some of your adventures and it seems to amuse him.\n\nEventually, the conversation shifts to these rocky rivers. He mentions that he knows a way to navigate through the rocks. He indicates it took him a while to scry a passage through and had many close calls.\n\nYou indicate that you would like to have this knowledge. He thinks for a while. \"I will tell you what soldiers. There is this divine wine called an \'Ambrosia\'. It brings instant healing and rejuvenation to the drinker.\n\nMy illness has made me quite weak and I believe such a brew may cure it. If you could bring me an \'Ambrosia\', I would be willing to share the secret of these rivers with you.\"", eDialogPic.CREATURE, 49, ["Leave", "Give"])
        if result == 1:
            if Party.CountItemClass(35, True) > 0:
                MessageBox("You give him the Ambrosia. He immediately drinks it. Right before your eyes, his skin begins to brighten and he becomes healthier by the moment. He explains that the way to proceed is to head north and then continue west.\n\nThere is no way to navigate the rocks directly west. He then explains the procedure of making your way through the sharp rocks. It is kind of complicated, so you take notes.")
                StuffDone["53_4"] = 1
                return
            MessageBox("Second thought, you do not have any Ambrosia. The Slith looks disappointed that you got his hopes up.")
            return
        MessageBox("You decline his offer for now, saying that you will return if you find some Ambrosia. The Slith nods and welcomes you back in advance.")
        return
    MessageBox("You return to the Slith mage. His skin has regained the bright green vibrance. The Ambrosia really has done wonders for him. He welcomes you back and explains how to get through the rocks in the northern fork once more.")

def NelonMountains_2368_MapTrigger_28_13(p):
    result = ChoiceBox("This stone hut is owned by a massive and hulking Slithzerikai. His entire body is covered with muscles, quite a fearsome sight. As soon as you enter the home, you notice the incredible heat.\n\nYou have heard that reptiles, and Sliths in particular, love warm temperatures. The hut is built on a small patch of lava. The Nelon Mountains are semi active geologically. The Slith welcomes you.\n\n\"It is not often that soldiers come to these lands, it is good to have visitors. I am Sslavk, a weaponsmith. I trade my personally made weapons to my brother Sliths who live in these areas.\" You notice the walls are lined with two-pronged spears.\n\nThe conversation shifts to the dangers of these mountains. \"Yes, there are many wild creatures who dwell here. However, the volcanic activity makes excellent dwellings for us. The remote location provides us refuge.\n\nSliths are still not a well accepted race you see. Many of us would prefer to live apart from other races anyway. Many Sliths will not respect your authority as Empire soldiers and would rather hunt you. I would be careful if I were you.\n\nI suppose I should offer to sell you some of my fine work. The prices are quite reasonable.\"", eDialogPic.CREATURE, 47, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_17_4_0")
        p.CancelAction = True
        return
    p.CancelAction = True

def NelonMountains_2369_MapTrigger_17_7(p):
    if StuffDone["53_4"] >= 1:
        WorldMap.AlterTerrain(Location(208,8), 0, TerrainRecord.UnderlayList[51])
        WorldMap.AlterTerrain(Location(208,7), 0, TerrainRecord.UnderlayList[55])
        if StuffDone["53_5"] == 250:
            return
        StuffDone["53_5"] = 250
        MessageBox("Using the instructions you received from the old Slith, you manage to navigate your way through the rocks. It was kind of tricky in some spots, but not too difficult. You just don\'t want to go through this too often.")
        return

def NelonMountains_2373_MapTrigger_20_25(p):
    result = ChoiceBox("At the corner of this fiery valley, you discover a ledge. Upon it rests a massive anvil, much larger than any of the traditional kind. At its side lay massive tools for shaping. It reminds you of a Giant\'s forge, but larger still.\n\nYou wonder exactly what gets made here. Then there is a bubbling from within the lava. Suddenly, a torch of flame rises from the fiery pit. You realize the torch has arms and begins to take a quasi-humanoid shape.\n\nIt barks at you in a booming voice. The sound echoes between the walls of the chasm. \"Welcome, I am Callisto and this is my forge. I see you are afraid, but you need not be. I mean you no harm, unless you attempt to harm me.\n\nI am what is called an Efreet, a race of fire beings brought to life. Our existence predates that of all other races on this world, we are the oldest and the wisest. Once we ruled the world, but those were times where we were immature.\n\nNow we merely watch and learn. The activities of your Empire bring us much amusement. Perhaps you would like to amuse us more by purchasing some of my brilliant stock of weapons.\n\nI assure you that there is no equivalent anywhere in the world. Unless, you find another Efreet of course. But, I doubt you shall.\"", eDialogPic.TERRAIN, 156, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_20_4_0")
        p.CancelAction = True
        return
    MessageBox("You decline the offer of the mighty Efreet. He lets out a booming laugh that stirs the entire cauldron. \"If you wise up and change your minds, come back here. I am a patient creature, like all of our kind.\"")
    p.CancelAction = True

def NelonMountains_2374_MapTrigger_39_38(p):
    if StuffDone["53_6"] == 250:
        return
    StuffDone["53_6"] = 250
    WorldMap.AlterTerrain(Location(231,38), 1, None)
    WorldMap.DeactivateTrigger(Location(231,38))
    Animation_Hold(-1, 075_cold)
    Wait()
    ChoiceBox("This passage slopes downward slightly. You notice that the air suddenly has become unusually cold. When you reach the end of the passage, you notice several small (and a couple large) caves.\n\nYou hear the sounds of motion in the hills. Curious, you decide to take a closer look. You reach the entrance to one of the small caves and find a pack of about three ice lizards.\n\nYou think easy prey, but then you notice that these ice lizards are actually a small part of a much larger population, a much larger and hungry population!", eDialogPic.CREATURE, 65, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_0_5", p.Target)

def NelonMountains_2375_MapTrigger_20_29(p):
    if StuffDone["53_7"] == 250:
        return
    StuffDone["53_7"] = 250
    WorldMap.DeactivateTrigger(Location(212,29))
    Animation_Hold(-1, 014_missile)
    Wait()
    ChoiceBox("Suddenly a spear lands near you, nearly missing. You look forward and see the figures of several muscular Slithzerikai. You have heard tales that these lizard creatures enjoy consuming the flesh of Humans, Nephilim, and even enemy Sliths!\n\nUnfortunately, the law is meaningless up in the Nelon Mountains. You are on their turf and their newly selected prey.", eDialogPic.CREATURE, 46, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_0_4", p.Target)

def NelonMountains_2376_MapTrigger_25_6(p):
    if StuffDone["53_8"] == 250:
        return
    StuffDone["53_8"] = 250
    WorldMap.DeactivateTrigger(Location(217,6))
    Animation_Hold(-1, 014_missile)
    Wait()
    ChoiceBox("Suddenly a spear lands near you, nearly missing. You look forward and see the figures of several muscular Slithzerikai. You have heard tales that these lizard creatures enjoy consuming the flesh of Humans, Nephilim, and even enemy Sliths!\n\nUnfortunately, the law is meaningless up in the Nelon Mountains. You are on their turf and their newly selected prey.", eDialogPic.CREATURE, 46, ["OK"])
    WorldMap.SpawnNPCGroup("Group_4_0_4", p.Target)

def NelonMountains_2377_MapTrigger_5_38(p):
    if StuffDone["53_9"] == 0:
        result = ChoiceBox("At the end of this passage lies a large wand, seemingly abandoned. There is no indication of any kind about who or what may have left the object. You could take it if you want it.", eDialogPic.STANDARD, 30, ["Leave", "Take"])
        if result == 1:
            Party.GiveNewItem("WandofParalysis_356")
            MessageBox("You take the wand. It kind of has a numbing feeling when you touch it.")
            StuffDone["53_9"] = 1
            return
        return

def NelonMountains_2378_SpecialOnWin1(p):
    ChoiceBox("With the Ice Drakes slain, you decide to search the large cave (also the dwelling of the drakes). You turn up the frozen bodies of several Slithzerikai. It is quite a gruesome sight, considering that they are half eaten.\n\nApparently these creatures prefer their meals cold. There is not much left of the bodies in the way of treasure except for one shiny ring that may be of interest. It kind of feels warm to the touch.", eDialogPic.STANDARD, 2, ["OK"])
    Party.GiveNewItem("RingofWarmth_314")
