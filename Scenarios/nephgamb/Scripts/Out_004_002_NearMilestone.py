
def NearMilestone_578_MapTrigger_15_12(p):
    ChoiceBox("While Milestone is an important town in Chimney, it is also a dull one.\n\nIt is important as the centre of the bronze industry of Chimney. Tin bars from the mines to the north are carried here, as is copper ore from the mines to the north west. Alloying the two into bronze demands extremely high temperatures.\n\nMilestone makes use of its natural lava resources to keep the temperature in the forges at 3000 degrees celsius. From here, bronze tools and utensils stream to the markets in Myldres and Lushwater.\n\nThe slithzerikai taboo that prohibits worker sliths from even touching iron or steel ensures an eager market for the Chimney bronze.\n\nMilestone is also a dull place, in the sense that most people in Milestone are deeply involved in the bronze business, and care little for the events of the world. Several members of your party have traumatic memories of childhoods in mining towns.\n\nYou walk the streets for some time, looking for adventure or hints to help you in your mission. You soon give up. The famous Milestone Casino on top of the hill looks much more interesting.", eDialogPic.TERRAIN, 187, ["OK"])

def NearMilestone_579_MapTrigger_39_8(p):
    MessageBox("The path narrows at this point, and you have to proceed in single file, making your way slowly among the boulders. You feel very exposed.")

def NearMilestone_580_MapTrigger_36_5(p):
    WorldMap.SpawnNPCGroup("Group_4_2_4", p.Target)

def NearMilestone_581_MapTrigger_29_4(p):
    if StuffDone["142_0"] == 250:
        return
    StuffDone["142_0"] = 250
    WorldMap.AlterTerrain(Location(221,100), 1, None)
    WorldMap.DeactivateTrigger(Location(221,100))
    MessageBox("You find the lair of the cave giants, and after some more climbing, you enter it. Their possessions are mainly rocks. You are starting to think you were the first victims ever to enter their trap when you find a pouch containing coins and a jewel.")
    Party.GiveNewItem("Sapphire_177")
    Party.Gold += 300

def NearMilestone_582_SpecialOnMeet0(p):
    MessageBox("As you climb over a boulder inconveniently placed across the corridor, you hear sliding noises from above. Boulders crash down at you, to the joyous shouts of a band of cave giants. Once the rocks have softened you up, they attack.")
    Party.Damage(Maths.Rand(3, 1, 5) + -1, eDamageType.WEAPON)
    Wait()
