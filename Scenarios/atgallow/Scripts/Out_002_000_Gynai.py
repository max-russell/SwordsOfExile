
def Gynai_2343_MapTrigger_20_14(p):
    if StuffDone["100_0"] == 7:
        if StuffDone["52_1"] == 250:
            return
        StuffDone["52_1"] = 250
        Animation_Hold(-1, 043_stoning)
        Wait()
        ChoiceBox("CHAPTER VII -- THE SEARCH FOR ANSWERS", eDialogPic.STANDARD, 31, ["OK"])
        StuffDone["100_1"] = 1
        return

def Gynai_2344_MapTrigger_26_26(p):
    result = ChoiceBox("This area appears to be some sort of shrine. In the center of a circle of tall crystalline spires is a circular pool of clear water. Around the pool are several pedestals for kneeling and meditation.\n\nThis is certainly a lovely place of wonderful architecture unlike any you have seen before. Perhaps you could meditate here and enjoy the serenity.", eDialogPic.TERRAIN, 1024, ["Leave", "Pray"])
    if result == 1:
        MessageBox("You meditate before the crystal pool. You find the time you spend to be most relaxing, but you do not feel at all benefited by doing this.")
        return

def Gynai_2345_MapTrigger_13_13(p):
    ChoiceBox("You have heard that Gynai produces some of the most tasteful foods in the world. Now you get a glimpse of the secrets. This place has a number of plant farms, yet they are unlike any farms you have ever seen.\n\nAll of the plants are grown in large basalt domes. Around the circumference of the structure at eye level are several green-tinted windows allowing you to look inside to see the neatly tended rows of crops.\n\nYou also notice that the entire structure is completely self contained. Filtered air is pumped in (and out) through a series of vents. Irrigation is provided from special valves in the ceiling.\n\nYou are also guessing factors like temperature, humidity, and soil content are kept strictly controlled as well. These rigorous controls must have taken a long time to develop to yield an optimum crop.\n\nThe system is much more inefficient than the \'standard\' ways you saw back in Agran, only providing a fraction of the crop there. However, Gynai has fewer mouths to feed and can afford this complicated and inefficient system to produce excellent food.", eDialogPic.TERRAIN, 181, ["OK"])
    p.CancelAction = True

def Gynai_2348_MapTrigger_16_13(p):
    ChoiceBox("You have heard that Gynai produces some of the most tasteful foods in the world. Now you get a glimpse at some of their secrets. This place has a number of animal farms, yet they are unlike any farms you have ever seen.\n\nThe animals are raised in an extremely contained and controlled environment. The structures are quite massive and have an odd bubble shape to them. Several windows allow you to peer into the activities.\n\nEach structure is for a different type of livestock. One for cows, one for sheep, one for chickens, and so forth. Although the methods used are very complex and different for each of them, you notice all of them are almost completely automated.\n\nThe only tasks for the workers is to apply the proper foods and ensure that the entire system is working properly. This is much easier than the difficult sunrise to sunset in the field days that the farmers in Agran had to withstand.\n\nAnother peculiarity is the intelligence of the animals. All of them appear to be already instinctively trained to eat foods at a certain time. The cows willingly line up in single file to be milked by strange tentacled machines.\n\nYou bet that the farmers around the Empire wished they had animals with such obedience and intelligence. Quite an interesting system the Gynites have set here. You wonder how long it took to develop.", eDialogPic.CREATURE, 93, ["OK"])
    p.CancelAction = True

def Gynai_2352_MapTrigger_36_28(p):
    result = ChoiceBox("This is one of the Gynai farming areas. You notice all of the crops are grown in contained basalt domes. However, there is something peculiar about one of the domes.\n\nYou notice one is wide open. It appears the stone has actually been grown apart, and not opened by some mechanical means, quite peculiar. From talking to the distressed farmers around the open machine, you learn what went on.\n\nApparently the mechanical farming system that Gynai has is not fool proof. On average, the machinery on one of the farming domes fails each year. This basically \'ruins\' the crop inside.\n\nThis crop was some interesting spotted mushrooms. The mushrooms are quite overgrown, much larger than you have ever seen before. Whatever treatments the Gynites applied to them sure worked better than any others.\n\nThe farmers are concerned that the taste of their crop is ruined because of the malfunction. One of them offers you a taste. You take a bite expecting the usual earthy taste of mushroom, but are greeted by an indescribable pleasant taste.\n\nThis has got to be the best mushroom you have ever had! If they consider this ruined, you would love to see what high quality is. The farmers say they would be willing to sell some of the ruined crop at a discount.", eDialogPic.TERRAIN, 73, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_10_2_0")
        p.CancelAction = True
        return
    p.CancelAction = True

def Gynai_2353_MapTrigger_15_33(p):
    result = ChoiceBox("This somewhat hidden group of farms is responsible for the growth of alchemy herbs. Typical of Gynai, the dome chambers are very automated and the factors are strictly controlled.\n\nYou have heard the mages in Nelon have long ago developed similar contained houses to grow herbs. However, the herb houses there need constant personal attention. These are completely automated.\n\nThe alchemists in charge of maintaining these herbs boast that their herbs are the most potent in the world. They have mastered growing all the major alchemy herbs including graymold, ember flowers, and even mandrake.\n\nYou are amazed by the mechanical setup, especially the ones which grow ember flowers and mandrake. The systems of maintenance for these are extremely complicated and not even the Empire has managed to develop their own.\n\nHerbs are constantly being harvested to fit the demands of the engineers in Gynai. They offer to sell some of their available product to you, at a special higher guest rate of course.", eDialogPic.STANDARD, 20, ["Leave", "Buy"])
    if result == 1:
        OpenShop("Shop_Items_Outside_13_2_0")
        p.CancelAction = True
        return
    p.CancelAction = True

def Gynai_2354_MapTrigger_36_13(p):
    ChoiceBox("Gynai is completely self contained, having its own system of mines. You do not get very far before you are stopped at the entrance office. You notice on the wall there is a map of the mine.\n\nThe mine runs far deeper than any one you have ever heard of before. Although the units are unfamiliar to you, \'blms\' (whatever that means), you can tell by the complexity of the mine that it is far larger than any other shaft.\n\nIn fact, the miners here are happy to attest to that fact. The mine has three major products, crystals, gems, and metals. You hear that the two former are actually grown in the mines in special chambers where they are harvested.\n\nThe metals are a bit more difficult, but you hear talk about special devices called magical transmutaters installed into the mine. By looking at the map, you find the locations of the massive machines.\n\nYou hear that the process of rearranging the rock into special metals is an extremely slow process, often taking generations to produce a suitable amount to excavate. However, by sheer numbers of machines, there is always a rich supply.\n\nSo this explains how Gynai stayed self contained and separate from the world for so long. They literally have developed the perfect system of mining that could potentially satisfy all their needs forever.", eDialogPic.STANDARD, 8, ["OK"])
    p.CancelAction = True

def Gynai_2355_MapTrigger_15_10(p):
    ChoiceBox("This large facility is the Gynai Fishery. The Gynai have a very mechanical and different way of raising their food. The way they raise their fish is no exception. The fish are grown in a large tank of water.\n\nThe water is filtered in from the ocean where special additives are mixed in. These additives allow the fish to grow to amazing sizes and develop the fine taste that is typical of Gynai food.\n\nAlthough you do not get to see much of the procedure, you notice that the environment for the fish is strictly regulated. Factors such as temperature, salinity, acidity, and current flow are kept under control.\n\nThe engineers claim that these secrets give the best possible yield. Judging by the complexity of the operation, you would not doubt it.", eDialogPic.STANDARD, 16, ["OK"])
    p.CancelAction = True
