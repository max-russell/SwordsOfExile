
def LushwaterToll_88_MapTrigger_29_24(p):
    MessageBox("A winding path strikes out from the central square and climbs a steep hill bordering the town. The path circles the hill and reaches the idyllic castle nestling on the top, overlooking the bridge.")

def LushwaterToll_89_MapTrigger_25_16(p):
    if StuffDone["5_0"] == 250:
        return
    StuffDone["5_0"] = 250
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(25,16))
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(24,16))
    MessageBox("The path slopes sharply upwards. You already have a good view of the town, clutching the hill fortress for protection.")

def LushwaterToll_91_MapTrigger_14_5(p):
    if StuffDone["5_1"] == 250:
        return
    StuffDone["5_1"] = 250
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(14,5))
    MessageBox("The river laps at the crag, slowly gnawing away at the rock sixty feet below. A hundred years more of lapping and gnawing, and the path will slide into the hungry river. You try not to think about it as you follow the narrow ledge.")

def LushwaterToll_92_MapTrigger_4_9(p):
    if StuffDone["5_2"] == 250:
        return
    StuffDone["5_2"] = 250
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(4,9))
    MessageBox("You finally reach the top, and the ledge widens a bit. After climbing the path, you understand why the robbers were never ousted from their lair. You would not have liked fighting your way up here with people dropping boulders and fire on you.")

def LushwaterToll_93_MapTrigger_5_14(p):
    if StuffDone["5_3"] == 250:
        return
    StuffDone["5_3"] = 250
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(5,14))
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(5,15))
    ChoiceBox("Harfloot Castle was built not to be grand, but to shelter a band of vicious outlaws preying on merchants and travellers. It is quite small as castles go, and rather cramped, but probably easy to defend.\n\nThe original bandit?s son was rather more civilized than his father. His grandson, the current Lord Harfloot, appears almost meek. Though he enjoys the wild reputation of the Harfloots, it seems the fighting spirit of the clan has been tamed.\n\nLord Harfloot is also practically without political influence in Chimney. After the military reign in Myldres seized power, it installed a garrison commander that answers directly to Commander Groul.", eDialogPic.TERRAIN, 1024, ["OK"])

def LushwaterToll_95_MapTrigger_9_21(p):
    if StuffDone["5_4"] == 250:
        return
    StuffDone["5_4"] = 250
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(9,21))
    MessageBox("The entire castle is cramped and gives the impression of being crammed full of too many possessions. This room, however, is extreme. Big, stately furniture, meant for large rooms, are packed into this chamber, little more than a cabinet.")

def LushwaterToll_96_MapTrigger_14_24(p):
    if StuffDone["5_8"] >= 1:
        return
    pc = SelectPCBox("Select a member of your party:",True)
    if pc == None:
        p.CancelAction = True
        return
    MessageBox("From out of nowhere, a chair is flung in your direction. You dive for cover, but react too late. Sinister laughter floats through the room, coming from nowhere in particular. This is a warning.")
    pc.Damage()
    Wait()

def LushwaterToll_97_MapTrigger_39_19(p):
    if StuffDone["5_5"] == 250:
        return
    StuffDone["5_5"] = 250
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(39,19))
    TownMap.List["LushwaterToll_5"].DeactivateTrigger(Location(39,18))
    ChoiceBox("You enter the office of Captain Locke. He is a tall, austere man and the de facto ruler of Lushwater. Word of your arrival must have reached him already, for when you enter, he stands from his desk to salute you.\n\nIn short terms you introduce yourselves and relate the story of what has befallen you and the inhabitants of the Brattaskar Pass. You describe the invaders in as much detail as you can provide, guessing at their strength and positions.\n\nDuring your ten minute flood of words, he says nothing, nor does his eyes leave you. When you finally conclude, he remains silent for a long time, pondering your report.\n\nWhen he speaks, it is with a voice full of concern. \"You are brave soldiers of outstanding resources and exemplary determination. Your deeds honour Chimney and the Commander, and give all of us hope before the coming trial.\n\n\"Still, your report confirms and even deepens my fears. The sliths haven?t dared to attack us at Lushwater, but patrols sent to investigate reported of slith marauders. Your story of massacres proves that a conquering army threatens us.\n\n\"Groul knows of the raids already, but your report adds new urgency to the affair. I will arrange that you are brought speedily to the capital.\" Locke sits at his desk to draft orders.", eDialogPic.CREATURE, 16, ["OK"])
    ChoiceBox("PART 2: Raising the Mask", eDialogPic.STANDARD, 6, ["OK"])

def LushwaterToll_99_MapTrigger_17_25(p):
    if StuffDone["5_8"] >= 1:
        return
    MessageBox("A fistful of sharp knives are thrown towards your group. Somebody is getting serious.")
    Party.Damage(Maths.Rand(2, 1, 5) + 5, eDamageType.WEAPON)
    Wait()

def LushwaterToll_100_MapTrigger_16_26(p):
    if StuffDone["5_8"] >= 1:
        return
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 3))

def LushwaterToll_101_MapTrigger_19_26(p):
    if StuffDone["5_8"] >= 1:
        return
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.BLESS_CURSE, Maths.MinMax(-8, 8, pc.Status(eAffliction.BLESS_CURSE) - 2))

def LushwaterToll_102_MapTrigger_19_25(p):
    if StuffDone["5_8"] >= 1:
        return
    pc = SelectPCBox("Select a member of your party:",True)
    if pc == None:
        p.CancelAction = True
        return
    MessageBox("An invisible hand stabs a needle into your behind. You yell, and almost immediately feel worse.")
    pc.Poison(6)

def LushwaterToll_104_MapTrigger_20_25(p):
    if StuffDone["5_8"] >= 1:
        return
    for x in range(15, 22):
        for y in range(23, 29):
            if Maths.Rand(1,0,100) <= 80:
                Town.PlaceField(Location(x,y), Field.BLADE_WALL)

def LushwaterToll_105_MapTrigger_18_24(p):
    if StuffDone["5_8"] >= 1:
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("Electric force builds up on the throne. You back away before it is unleashed on you.")

def LushwaterToll_111_MapTrigger_18_27(p):
    if StuffDone["5_9"] >= 1:
        if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(18,28)).Num == 173:
            return
        MessageBox("While most of you doubtfully guard the room, your chosen scribe nervously bends to draw the complicated seal. You finish, and everyone checks to see if it looks like the one Pandora showed you. Then you are done.")
        Town.AlterTerrain(Location(18,28), 0, TerrainRecord.UnderlayList[173])
        return

def LushwaterToll_114_MapTrigger_18_28(p):
    if StuffDone["5_8"] >= 1:
        return
    if Game.Mode != eMode.OUTSIDE and Town.TerrainAt(Location(18,28)).Num == 173:
        itemthere = False
        if Game.Mode != eMode.OUTSIDE:
            for i in Town.EachItemThere(Location(16,24), True):
                if i.SpecialClass == 3:
                    itemthere = True
                    break
        if itemthere == True:
            itemthere = False
            if Game.Mode != eMode.OUTSIDE:
                for i in Town.EachItemThere(Location(20,25), True):
                    if i.SpecialClass == 3:
                        itemthere = True
                        break
            if itemthere == True:
                itemthere = False
                if Game.Mode != eMode.OUTSIDE:
                    for i in Town.EachItemThere(Location(18,26), True):
                        if i.SpecialClass == 3:
                            itemthere = True
                            break
                if itemthere == True:
                    if StuffDone["55_0"] == 250:
                        return
                    StuffDone["55_0"] = 250
                    MessageBox("You carefully light the black candles and distribute them on top of the blood stains. Then you stand inside your protective seal and start chanting your ritual. You feel a gust of wind, then hear a screeching noise. Then there is a fierce explosion.\n\nThe demonic seal shelters you from the spiritual blast, and you watch calmly as a shape materializes on the throne.")
                    Town.PlaceEncounterGroup(1)
                    return
                MessageBox("You place yourselves cautiously within your demonic seal and start chanting your ritual. But something is missing. The poltergeist laughs with scorn, and suddenly an anvil appears above your heads! It drops on you before you have time to evade the weight.")
                Party.Damage(Maths.Rand(3, 1, 8) + 15, eDamageType.UNBLOCKABLE)
                Wait()
                return
            MessageBox("You place yourselves cautiously within your demonic seal and start chanting your ritual. But something is missing. The poltergeist laughs with scorn, and suddenly an anvil appears above your heads! It drops on you before you have time to evade the weight.")
            Party.Damage(Maths.Rand(3, 1, 8) + 15, eDamageType.UNBLOCKABLE)
            Wait()
            return
        MessageBox("You place yourselves cautiously within your demonic seal and start chanting your ritual. But something is missing. The poltergeist laughs with scorn, and suddenly an anvil appears above your heads! It drops on you before you have time to evade the weight.")
        Party.Damage(Maths.Rand(3, 1, 8) + 15, eDamageType.UNBLOCKABLE)
        Wait()
        return

def LushwaterToll_117_OnEntry(p):
    if not Town.Abandoned:
        if StuffDone["5_7"] == 250:
            return
        StuffDone["5_7"] = 250
        ChoiceBox("The story of Lushwater Toll is in many ways the essential story of Exile.\n\nIt was founded (or initiated, for he never intended anything grand) by a runaway from the Empire. Not a political fugitive or a free-thinker, but the leader of a small band of cutthroats, looking for fresh territories and liberal law.\n\nIn the time just after the disastrous First Expedition, when plans for profitable colonization were discarded and nobody knew just what to do with the caverns, the brigand chief Harfloot thought them the perfect hide-out.\n\nHe settled about as far away from the Empire as he could come, and quickly found easy plunder in the lands of the nephilim. When trade routes between humans and sliths were established, Harfloot and his band made a fat living from highway robbery.\n\nThe merchants soon got used to pay taxes for free passage. When Harfloot grew old and died and his son took over, he inherited an enterprise of ritual threats and payments. Young Harfloot was less of a robber and more of a businessman.\n\nHe built a good road and a strong bridge, and soon received toll from the travellers to protect them from bandits. A trade post grew into a medium sized town, ruled by the grandson of the original Harfloot, considered a kind and polite gentleman.", eDialogPic.TERRAIN, 187, ["OK"])

def LushwaterToll_118_CreatureDeath12(p):
    MessageBox("You deal a final blow to the golem, and it collapses. The banishing ritual completed and its material incarnation destroyed, the poltergeist howls in agony and disappears. You feel the tension in the room lighten at once. Lord Harfloot should be grateful.")
    StuffDone["5_8"] = 1

def LushwaterToll_119_TalkingTrigger8(p):
    if StuffDone["5_6"] == 250:
        return
    StuffDone["5_6"] = 250
    SpecialItem.Give("Commandeerletter")

def LushwaterToll_120_TalkingTrigger36(p):
    if StuffDone["55_1"] == 250:
        return
    StuffDone["55_1"] = 250
    Party.GiveNewItem("PiercingCrystal_182")

def Talking_5_16(p):
    if Party.Gold < 10:
        p.TalkingText = "Melinny smiles, no less friendly. \"You must have been robbed already.\""
    else:
        Party.Gold -= 10
        Party.Pos = Location(43, 36)
        Town.UpdateVisible()
        Party.HealAll(60, True)
        Party.RestoreSP(50)
        p.TalkingText = "Melinny leads you to a comfortable room with a view of the town square. You would not mind if it had rats or foul smell in it. Your first night in a proper bed after what seems an eternity is luxury in itself."
        CentreView(Party.Pos, False)

def Talking_5_28(p):
    if Party.Gold >= 5:
        Party.Gold -= 5
        p.TalkingText = "\"Alright. But not more than one, now! It?s still early.\" Melinny watches you through your drink, making you less comfortable drinking it than you might have been."
    else:
        p.TalkingText = "\"Have you spent all your money already?\""
