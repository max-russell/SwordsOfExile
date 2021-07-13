def Generate_Wandering_3_BloodGleeClan(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["CaveGiant_155"]])
            npcs.append([1,NPCRecord.List["CaveGiant_155"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(21,35)
                elif r2 == 1: l = Location(51,19)
                elif r2 == 2: l = Location(30,33)
                elif r2 == 3: l = Location(11,33)
                
                if Town.InActArea(l):
                    for pc in Party.EachIndependentPC():
                        if l.VDistanceTo(pc.Pos) < 10: l = Location.Zero
                else:
                    l = Location.Zero
                    
            if l != Location.Zero:
                for n in npcs:
                    for m in range(n[0]):
                       if m == 0 or Maths.Rand(1,0,1) == 1:
                           p_loc = Location(l.X + Maths.Rand(1,0,4) - 2, l.Y + Maths.Rand(1,0,4) - 2)
                           Town.PlaceNewNPC(n[1], p_loc, False)

def BloodGleeClan_53_MapTrigger_52_27(p):
    if StuffDone["3_0"] == 250:
        return
    StuffDone["3_0"] = 250
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(52,27))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(53,27))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(45,19))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(45,18))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(53,15))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(54,16))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(55,16))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(53,16))
    MessageBox("At first, you think that these heaps of rotting vegetations, rigor stricken bodies, and moldy, unidentifiable dead things are compost piles or trash dumps.\n\nThen you see a giant picking something horrible out of a mound and munching on it, and you realize that this is the giant\'s larder. The creatures must take delight in eating as awful food as they can get.")
    Town.PlaceEncounterGroup(1)

def BloodGleeClan_59_MapTrigger_11_7(p):
    if StuffDone["3_1"] == 250:
        return
    StuffDone["3_1"] = 250
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(11,7))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(12,7))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(16,22))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(16,23))
    MessageBox("Like many humanoid species in Exile, these giants revere their dead to a creepy extent, and keep their most valued corpses safely buried in cairns close to home.\n\nThere is a subtle, unpleasant, sickly sweet smell. You suspect that not all of the dead giants were buried as well as they could have been.")

def BloodGleeClan_65_MapTrigger_29_14(p):
    MessageBox("This chamber is very out of place. It\'s beautiful, elegant, and very carefully made. Considering the scale everything is built to, it must have been made by the giants. Why these barbarians felt a need to have this pleasant, peaceful room escapes you.")

def BloodGleeClan_66_MapTrigger_25_20(p):
    MessageBox("This is a mural of a very young giant. He is being savagely beaten by his friends. He seems to be enjoying it. All of the giants have major scars.")

def BloodGleeClan_67_MapTrigger_27_20(p):
    MessageBox("This is a mural of a young giant. He is shown going through several stages of some sort of highly painful, violent, terrifying ritual of passage. He seems to be enjoying it.")

def BloodGleeClan_68_MapTrigger_29_20(p):
    MessageBox("This is a mural of an adult giant. He is eating a gigantic, raw, fanged worm. He is also bleeding from several fresh, severe bites. He seems to be very, very happy. Large kegs of ale surround him.")

def BloodGleeClan_69_MapTrigger_31_20(p):
    MessageBox("This is a mural of a very old giant. He is being savagely beaten by his friends, perhaps fatally. He seems to be enjoying it.")

def BloodGleeClan_70_MapTrigger_20_15(p):
    ChoiceBox("The altar is covered with fangs. They\'re each a foot long, and look like they\'ve been ripped out of some creature\'s mouth. There must be at least a hundred of them.\n\nYou don\'t feel any sort of malevolent magic radiating from the altar. It seems to just be here as a place to put torn out fangs. This clan of giants is very odd.", eDialogPic.TERRAIN, 154, ["OK"])

def BloodGleeClan_71_MapTrigger_42_30(p):
    if StuffDone["3_2"] == 250:
        return
    StuffDone["3_2"] = 250
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(42,30))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(42,29))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(28,36))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(28,35))
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(28,34))
    MessageBox("The giant clan\'s lair has a huge cavern in the middle. In the center of the cave, you see a massive pit. Harsh, alien growls rise from the inky depths.\n\nYour continuous prayers for indigenous lifeforms who don\'t instantly want to devour you have not yet been answered in the affirmative.")

def BloodGleeClan_76_MapTrigger_5_32(p):
    if SpecialItem.PartyHas("HornCharm"):
        if StuffDone["3_3"] == 250:
            return
        StuffDone["3_3"] = 250
        MessageBox("Suddenly, the charm the unicorns gave you starts to glow and vibrate. You remove it from around your neck and examine it. Interesting ... no matter how you hold it, it struggles to point downward.\n\nMaybe the thing you\'re looking for is below you somewhere. Whether it is or not, after a moment the charm stops glowing and twitching.")
        return

def BloodGleeClan_81_MapTrigger_20_12(p):
    if StuffDone["3_4"] == 250:
        return
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("The giant chieftain\'s chest has several runes etched onto the lock. Maybe the tribal shamans have placed a trap.", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("The giant chieftain\'s chest has several runes etched onto the lock. Maybe the tribal shamans have placed a trap.")
        if pc == None:
            p.CancelAction = True
            return
    StuffDone["3_4"] = 250
    TownMap.List["BloodGleeClan_3"].DeactivateTrigger(Location(20,12))
    pc.RunTrap(eTrapType.DART, 3, 75)

def BloodGleeClan_82_MapTrigger_37_15(p):
    MessageBox("The shamans of the tribe have, with no doubt considerable effort, gathered together a variety of spell books and stored them here.\n\nUnfortunately, very few of them could be of any use to you, and the crude treatment they\'ve received at the hands of the giants have made them basically unreadable. Tough luck.")

def BloodGleeClan_84_MapTrigger_15_50(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(17,44)).Num == 163:
        MessageBox("Suddenly, the portcullises behind you slam shut! You don\'t see any giants behind them ... the closing must be automatic. Looks like you\'re stuck in here.")
        Town.AlterTerrain(Location(17,44), 0, TerrainRecord.UnderlayList[162])
        Town.AlterTerrain(Location(18,44), 0, TerrainRecord.UnderlayList[162])
        return

def BloodGleeClan_86_MapTrigger_10_55(p):
    result = ChoiceBox("A lever has been built into the wall here. A small sign by it reads, succinctly, \"Pull.\" From the pit behind you, you hear creatures roaring.", eDialogPic.STANDARD, 9, ["Leave", "Pull"])
    if result == 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(19,55)).Num == 162:
            MessageBox("When you pull the lever, a bell tolls in the pit behind you. The growling noises intensify. The portcullises at the east end of the cave open. However, at the same time, a huge, pale, wriggling worm climbs up out of the pit to see what the noise was.")
            Town.AlterTerrain(Location(19,56), 0, TerrainRecord.UnderlayList[163])
            Town.AlterTerrain(Location(19,55), 0, TerrainRecord.UnderlayList[163])
            Town.PlaceNewNPC(NPCRecord.List["MeatWorm_188"], Location(15,56), True)
            return
        MessageBox("You hear the loud clanging noise again. Another worm crawls up out of the pit, intent on mayhem.")
        Town.PlaceNewNPC(NPCRecord.List["MeatWorm_188"], Location(15,56), True)
        return

def BloodGleeClan_87_MapTrigger_58_36(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(40,30)
    Party.MoveToMap(TownMap.List["WormCaves_4"])

def BloodGleeClan_88_MapTrigger_28_55(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(29,55)).Num == 162:
        MessageBox("When you get close to the portcullises, they open.")
        Town.AlterTerrain(Location(29,55), 0, TerrainRecord.UnderlayList[163])
        return
        return

def BloodGleeClan_91_MapTrigger_36_57(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(41,55)).Num == 162:
        Town.AlterTerrain(Location(41,55), 0, TerrainRecord.UnderlayList[163])
        Town.AlterTerrain(Location(41,56), 0, TerrainRecord.UnderlayList[163])
        MessageBox("You find several tight rows of totems, each topped with the dried head of a young giant. These must be the giants who died while passing through these tests.\n\nOne of the totems looks a bit loose. you touch it, and it shifts slightly. When you do, the portcullises to the east slide open. Unfortunately, the chamber also grows very cold.")
        for x in range(32, 41):
            for y in range(53, 61):
                Town.PlaceField(Location(x,y), Field.ICE_WALL)
        return

def BloodGleeClan_92_MapTrigger_38_57(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(41,55)).Num == 163:
        MessageBox("Suddenly, blades begin circling through the air around you. To giants, they would just be very annoying. To you, they\'re a bit worse.")
        for x in range(32, 41):
            for y in range(53, 61):
                Town.PlaceField(Location(x,y), Field.BLADE_WALL)
        return

def BloodGleeClan_100_MapTrigger_52_57(p):
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(55,50)).Num == 162:
        result = ChoiceBox("You find two platforms. One has a lit brazier on it. The other is bare. The brazier is iron, and has two hand grips so that it can be easily picked up and moved from one platform to the other.\n\nEasily, except for the fact that the metal of the grips is red hot, and moving the brazier would be agonizingly painful. Also, it is built for giants to lift, so you would have to pull it slowly, inch by inch, across the floor.\n\nStill, no pain, no gain, you suppose, and the portcullises to the north are still closed. Does one of you pull it?", eDialogPic.TERRAIN, 160, ["Leave", "Push"])
        if result == 1:
            pc = SelectPCBox("Select a member of your party:",True)
            if pc == None:
                return
            MessageBox("The metal of the brazier sears your flesh. As a peculiar, burnt meat smell fills the room, you drag the cursed thing across to the other platform. Sure enough, when it\'s there, the portcullises to the north open, freeing you from the test.\n\nYour hands are in dire need of some salve.")
            pc.Damage()
            Wait()
            for x in range(55, 57):
                for y in range(50, 51):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[163])
            Town.AlterTerrain(Location(51,58), 0, TerrainRecord.UnderlayList[210])
            Town.AlterTerrain(Location(53,58), 0, TerrainRecord.UnderlayList[214])
            return
        return
    MessageBox("The brazier is still here, waiting to be carried. Since the portcullises are open, you decide to leave it be. You\'ve suffered more than enough pain in these caves.")

def BloodGleeClan_101_MapTrigger_4_7(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("The passageway you're walking down slopes sharply downward here.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(2,9)
    Party.MoveToMap(TownMap.List["WormCaves_4"])

def BloodGleeClan_103_ExitTown(p):
    if p.Dir.IsWest:
        Party.OutsidePos = WorldMap.ToGlobal(Location(41, 25),WorldMap.SectorAt(Party.OutsidePos))
    elif p.Dir.IsEast:
        Party.OutsidePos = WorldMap.ToGlobal(Location(43, 25),WorldMap.SectorAt(Party.OutsidePos))

def BloodGleeClan_104_CreatureDeath9(p):
    MessageBox("The giant chieftain ran to battle you with childlike glee and boundless joy. When he takes his death blow, it dims his enthusiasm a bit. He lands heavily on the ground.\n\nLooking at his body, you see that he had taken incredible amounts of punishment during his long life, in the process of becoming the leader of this tribe of joyful giant masochists. He will undoubtedly be buried with the highest honors.")
