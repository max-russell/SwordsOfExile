
def GiantsCaverns_633_MapTrigger_15_34(p):
    result = ChoiceBox("You find a natural steam vent. It\'s a steep depression in the cave floor, with cracks belching sulphurous steam at the base. The air is rank and thick with choking mists.\n\nWhile it hurts to breathe, the mist isn\'t so thick that you couldn\'t climb down into the vent, if you wanted to investigate.", eDialogPic.TERRAIN, 244, ["Leave", "Climb"])
    if result == 1:
        if StuffDone["210_1"] >= 1:
            MessageBox("You work your way down to the base of the vent. You find that the drake Aleel left discarded scales and some spoor behind, but nothing else. You climb back out.")
            return
        if StuffDone["212_4"] >= 1:
            if SpecialItem.PartyHas("GrayStones"):
                ChoiceBox("You return to the steamy pit, bearing the stones Aleel requested. Aleel is there, and approaches you. You show him the stones. He sniffs them, tastes them with a long, forked tongue, and says \"These are the correct stones.\"\n\n\"I have no treasure for you, but I do have knowledge. I will teach you a valuable spell.\" He explains to you how to cast the spell Avatar.\n\nHe then picks up the stones and puts them in his mouth, and, without a word of thanks, flies away.", eDialogPic.CREATURE2x1, 1, ["OK"])
                StuffDone["210_1"] = 1
                for pc in Party.EachAlivePC():
                    pc.LearnSpell("p_avatar")
                SpecialItem.Take("GrayStones")
                return
            ChoiceBox("As you start to climb down into the pit, you meet Aleel. The drake sniffs you, and says \"You haven\'t done what I asked. Do not return again without the stones, or I may forget my generous offer to not eat you.\"\n\nHe climbs back down into the pit. You leave.", eDialogPic.CREATURE2x1, 1, ["OK"])
            return
        ChoiceBox("The rocks are slippery, but you manage to make your way down to the bottom of the vent. You look around, and see shedded lizard scales. Large scales, as if they came from a massive creature.\n\nSuspecting a trap, you turn back, only to see an enormous drake perched on a pile of boulders about you. It looks down at you curiously. It doesn\'t seem inclined to attack, so you wait and see what it has to say.\n\n\"Hello, visitors,\" it chuckles. \"I am Aleel, elder of Drakekind. Welcome to my temporary home. As tempting as it is to devour you, I am in need of assistance from your kind.\"\n\n\"I have come down to these cold caverns to find a valuable reagent for my magical work. I left it down here once, marked with a stone I shaped with my own, fiery breath.\"\n\nHe describes the stones he needs to you. They are chalky and have a gray tinge. \"Return these to me, and I give you a Drake\'s oath that I will reward you for them and let you go safely as well. Now go. That is all.\"\n\nRelieved, you climb out of the pit.", eDialogPic.CREATURE2x1, 1, ["OK"])
        StuffDone["212_4"] = 1
        return

def GiantsCaverns_634_MapTrigger_8_25(p):
    if StuffDone["210_2"] == 250:
        return
    StuffDone["210_2"] = 250
    WorldMap.DeactivateTrigger(Location(8,505))
    WorldMap.DeactivateTrigger(Location(7,505))
    ChoiceBox("Looking to the northwest and northeast, you realize that the seafaring portion of your journey is about to come to an unwilling end.\n\nThe river in both directions turns from the placid path you have been following to fast, wood crushing rapids, filled with sharp rocks and massive boulders. You have to continue on foot.", eDialogPic.STANDARD, 31, ["OK"])

def GiantsCaverns_636_MapTrigger_36_15(p):
    if StuffDone["210_0"] == 250:
        return
    result = ChoiceBox("The river is spanned by an enormous bridge, made of massive boulders and cavewood timbers, strong enough to support the giants who no doubt constructed it.\n\nA large war party of those giants is currently standing guard on the bridge. There are several of them, roasting giant lizards on a chunk of the bridge they decided to set on fire.\n\nWhen they see you, they stand and grab their weapons. They don\'t move to attack. Instead, they stay put and defend their post. The only way you\'ll pass this bridge is with a fight.", eDialogPic.CREATURE1x2, 0, ["Leave", "Attack"])
    if result == 1:
        StuffDone["210_0"] = 250
        WorldMap.DeactivateTrigger(Location(36,495))
        WorldMap.DeactivateTrigger(Location(36,494))
        WorldMap.DeactivateTrigger(Location(36,493))
        MessageBox("You charge to attack. When you get close, you see that the giants are covered with scars, and many have the twisted and bent limbs that come with poorly set broken  bones.\n\nWhen they see you want to fight them, the giants are overwhelmed with childlike glee, as if there was nothing they would rather happen. Laughing and jumping around, they grab their weapons.")
        WorldMap.SpawnEncounter("Group_0_10_4", p.Target)
        return
    p.CancelAction = True

def GiantsCaverns_639_MapTrigger_37_22(p):
    if StuffDone["210_3"] == 250:
        return
    StuffDone["210_3"] = 250
    WorldMap.DeactivateTrigger(Location(37,502))
    WorldMap.DeactivateTrigger(Location(38,502))
    MessageBox("You run into a giant hunting party. That is to say, not a hunting party with a lot of people in it, but a hunting party composed of giants. They decide to hunt you.")
    WorldMap.SpawnEncounter("Group_0_10_5", p.Target)

def GiantsCaverns_640_MapTrigger_22_2(p):
    if StuffDone["210_4"] == 250:
        return
    StuffDone["210_4"] = 250
    WorldMap.AlterTerrain(Location(22,482), 1, None)
    WorldMap.DeactivateTrigger(Location(22,482))
    result = ChoiceBox("You stumble upon yet another scene of horrible violence. Several giants have trapped a unicorn in a corner. It is one of the white unicorns, the legendary, good, magical kind.\n\nThe unicorn is not radiating tranquility, however. The giants are moving in on it with violence on their minds. Do you help it?", eDialogPic.CREATURE, 149, ["Leave", "Attack"])
    if result == 1:
        MessageBox("You run up and chip in. The unicorn seems relieved to get some help.")
        WorldMap.SpawnEncounter("Group_0_10_6", p.Target)
        return
    MessageBox("Giants are nasty, and unicorns should be more than able to help themselves. You back away.")

def GiantsCaverns_642_SpecialOnWin0(p):
    MessageBox("Gasping and trembling, you stare out over the carnage. Massive bodies are strewn about like fallen trees. Streams of blood trickle through the cracks into the river below, attracting hungry cave fish.\n\nSearching the bodies, you find a good deal of gold. In addition, the tasty lizard they were roasting is still there.")
    Party.Gold += 1000
    Party.Food += 200

def GiantsCaverns_643_SpecialOnFlee0(p):
    MessageBox("You escape the giants. They laugh at you and go back to their roasting lizard.")
    StuffDone["210_0"] = 0

def GiantsCaverns_644_SpecialOnWin2(p):
    ChoiceBox("The unicorn, bleeding slightly but still OK, prances over to you and touches his horn to the floor. Must be a sign of respect.\n\nIt says \"I am Handi, a wandering unicorn. To the north are several of my kind, living in a lovely glade. Mention my name to them, and they will render you assistance in thanks for your deed.\"\n\n\"Now, alas, I prefer my solitude, and the company of even those as noble as you is difficult for me to take. Good luck to you.\" Then, with remarkable speed and agility, it scampers off.", eDialogPic.CREATURE, 149, ["OK"])
