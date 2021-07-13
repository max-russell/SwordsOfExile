
def WesternNelon_2436_MapTrigger_30_33(p):
    ChoiceBox("It is no secret that the Nelon Sector is the industrial capital of the world. This large industrial complex does heavy manufacturing of goods like furniture, industrial tools like metallic storage tanks and piping, crates, paper, and much more.\n\nThe size and complexity of the machines is astounding. Iron is smelted in large furnaces into steel and shaped into the various goods. The processes are highly automated, but many parts like assembly require a human touch.\n\nThese industrial machines produce a considerable amount of toxic waste. The nearby lake has become the dumping ground for this industrial sludge. The decades as a dumpsite have turned the lake into a dead, acrid waste.\n\nThe plants and wildlife in the area have been choked to death by the accumulations of sludge. The air has a constant horrible sulfurous rotting smell. You wonder how the people here put up with the horrible stench.\n\nTreatment of the waste is underway, but the expense required causes the process to be quite inadequate at cleaning the factory filth. Unfortunately, there is little you can do to solve this problem.", eDialogPic.TERRAIN, 189, ["OK"])
    p.CancelAction = True

def WesternNelon_2440_MapTrigger_34_25(p):
    ChoiceBox("This tower is responsible for cleaning and purifying the industrial sludge from the lake. Large machines filter, distill, and use various corrosive chemicals on the water to eat away at the waste.\n\nFrom the look of things, the waste is being pumped into the water faster than it is being taken out. The industrial plants in the area are dependent upon pumping in tens of thousands of liters every day to perform various activities.\n\nYour conversation with the tower technicians tells you that every ten years or so, the factories must be shut down for a while to allow the water to be purified so it can be safely used again.\n\nNew methods are currently in development that will hasten this process. However, due to lack of funding, research in these areas has been quite slow. Yet progress is still being made, slow as it may be.", eDialogPic.TERRAIN, 78, ["OK"])
    p.CancelAction = True

def WesternNelon_2441_MapTrigger_26_17(p):
    ChoiceBox("The Nelon Mountains have never really been known for their extreme mineral wealth when it comes to things like gemstones or rare metals. However, the mountains are packed full of useful iron, coal, oil, and high quality granite.\n\nThese materials perfectly suit the industrial nature of the Nelon Sector. The iron is of fair quality in these hills, often requiring much refinement. However, it is suitable for goods where metal purity is not essential.\n\nThe granite has applications to construction. The granite, one of Nelon\'s few raw materials, is shipped throughout the world via ships to be used in various projects. Mostly Nelon is dependent on the rest of the world for its raw materials.\n\nThe coal and oil are the fuel sources that heat the flames of the factories. These materials produce much waste and give the air a kind of smoggy appearance near the larger settlements and factories.", eDialogPic.TERRAIN, 194, ["OK"])
    p.CancelAction = True

def WesternNelon_2442_MapTrigger_34_44(p):
    if StuffDone["52_5"] == 250:
        return
    StuffDone["52_5"] = 250
    WorldMap.AlterTerrain(Location(178,92), 1, None)
    WorldMap.DeactivateTrigger(Location(178,92))
    Animation_Hold(-1, 066_disease)
    Wait()
    ChoiceBox("The factories have done an excellent job of polluting this once pleasant lake. Pools of sludge and toxic goo lie all around the shore. It appears that some of the ooze is not completely dormant.", eDialogPic.CREATURE, 107, ["OK"])
    WorldMap.SpawnNPCGroup("Group_3_1_4", p.Target)

def WesternNelon_2443_MapTrigger_17_11(p):
    if StuffDone["52_6"] == 250:
        return
    StuffDone["52_6"] = 250
    WorldMap.DeactivateTrigger(Location(161,59))
    Animation_Hold(-1, 046_growl)
    Wait()
    ChoiceBox("As you climb up this hill, you come across several lumbering undead. They appear to be walking skeletons, but covered with a strange greenish, glowing ooze. Like all undead, they hunger for the life force of the living.\n\nHence, they begin to chase the nearest living creatures.", eDialogPic.CREATURE, 52, ["OK"])
    WorldMap.SpawnNPCGroup("Group_3_1_5", p.Target)

def WesternNelon_2444_MapTrigger_19_43(p):
    result = ChoiceBox("You come across a fairly isolated mage tower. The place appears very welcoming, so you come inside. The mages inside are more than happy to talk about their projects.\n\nVisiting with the mages reveals that they are performing research on dealing with special toxic industrial wastes. Specifically, they are working on getting rid of a vile byproduct of metallic enhancement chemical reactions.\n\nTheir research leads them to believe that a special compound called Enthrenoline may do the trick. The only problem is the creation of the compound requires reagents that are only found in trace quantities in the horns of gray unicorns.\n\nAlthough gray unicorns are by no means uncommon, the number required is great and the mages are willing to pay a premium rate of 5 gold for any unicorn horns you might have.", eDialogPic.CREATURE, 26, ["Leave", "Give"])
    if result == 1:
        count = Party.CountItemClass(15, True)
        if count == 0:
            MessageBox("You have no unicorn horns to sell!")
            return
        Party.Gold += count * 5
        MessageBox("The mages are glad to take any unicorn horns off your hands. They happily pay the premium rate for the supply. They also welcome you to bring more if you happen to acquire any.")
        return
    p.CancelAction = True

def WesternNelon_2445_MapTrigger_42_11(p):
    if StuffDone["112_1"] == 0:
        result = ChoiceBox("At the top of these hills is a grassy plateau with some lovely flowers. You realize that these flowers are not just ordinary, but ones having applications to alchemy. You have come to a nicely sized patch of Glowing Nettle.", eDialogPic.STANDARD, 20, ["Leave", "Take"])
        if result == 1:
            MessageBox("You harvest some of the Glowing Nettle. There are still many that have not yet reached maturity. You are sure that you will be able to harvest more in a few days.")
            Party.GiveNewItem("GlowingNettle_365")
            RunScript("ScenarioTimer_x_2833", ScriptParameters(eCallOrigin.CUSTOM))
            return
        return
    MessageBox("The patch of Glowing Nettle has not quite grown back to a sufficient quantity yet. You will need to wait another day or so before you can pick more.")

def WesternNelon_2447_WanderingOnMeet3(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
