
def RoyalSector_173_MapTrigger_24_9(p):
    MessageBox("\"Do not approach the Mayor. You should kneel in the presence of your ruler.\" The words come from one of the guards and are accompanied by a jolt.")

def RoyalSector_177_MapTrigger_24_43(p):
    if Game.Mode != eMode.TOWN or p.Origin != eCallOrigin.MOVING:
        p.CancelAction = True
        return
    if ChoiceBox("You find a stairway heading down.", eDialogPic.STANDARD, 19, ["Climb", "Leave"]) == 1:
        p.CancelAction = True
        return
    Animation_FadeDown()
    Wait()
    Party.Pos = Location(29,51)
    Party.MoveToMap(TownMap.List["Myldres_6"])

def RoyalSector_179_MapTrigger_24_17(p):
    if StuffDone["8_2"] == 250:
        return
    StuffDone["8_2"] = 250
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(24,17))
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(25,17))
    MessageBox("You approach the gates and identify yourselves to the guards. One enters the throne room of the mayor. After a few minutes, he returns with a brief smile. \"You are in luck. The Mayor will see you right away. Please enter.\"")

def RoyalSector_181_MapTrigger_18_24(p):
    MessageBox("Your thorough search pays off. Towards the end of a rather dull treatise on the architecture of the royal sector, you find a floor plan. There is another room next to the library! The plan refers to a secret button on the western wall of the library.")
    StuffDone["8_1"] = -1

def RoyalSector_182_MapTrigger_9_28(p):
    if StuffDone["8_1"] >= 1:
        Town.AlterTerrain(Location(9,28), 0, TerrainRecord.UnderlayList[146])
        if StuffDone["58_0"] == 250:
            return
        StuffDone["58_0"] = 250
        MessageBox("You never would have found this button if you hadn?t known what to look for. But then, that is why they call it a secret button.")
        return

def RoyalSector_183_MapTrigger_34_17(p):
    if StuffDone["8_3"] == 250:
        return
    StuffDone["8_3"] = 250
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(34,17))
    MessageBox("Tucked under the tablecloth of the altar, you find a small steel key. You nonchalantly slip it in your pocket.")
    SpecialItem.Give("Magekey")

def RoyalSector_184_MapTrigger_42_24(p):
    if Game.Mode == eMode.COMBAT:
        if ChoiceBox("You've found a trap. Do you want to try to disarm it?", eDialogPic.NONE, 0, ["Disarm", "Leave"]) == 1:
            p.CancelAction = True
            return
        pc = p.PC
    else:
        pc = SelectPCBox("You've found a trap. Do you want to try to disarm it?")
        if pc == None:
            p.CancelAction = True
            return
    pc.RunTrap(eTrapType.GAS, 2, 50)

def RoyalSector_185_MapTrigger_37_20(p):
    if SpecialItem.PartyHas("Magekey"):
        MessageBox("You try your steel key in the imposing steel-bound door. It turns, and the lock snaps open. Still, you wonder if going inside really is a good idea. You can still leave.")
        Town.AlterTerrain(Location(38,20), 0, TerrainRecord.UnderlayList[142])
        return
        return
    MessageBox("This door is bound with criss-crossing steel bonds. The way it is done gives you the feeling that the door is built as much to keep things from breaking out as to keep you from coming in. Nevertheless, you give up forcing the door without even trying.")

def RoyalSector_186_MapTrigger_40_18(p):
    result = ChoiceBox("The air in the laboratory is thick with smoke, making your eyes water. Toppled braziers and torn-up diagrams are illuminated by a pulsing blob on the floor.\n\nAs you approach, you feel heat radiating from the thing. You stop at a respectful distance. Now you can see that it is a slimy, greenish mass, wobbling slowly as sulfur bubbles force their way to the surface.\n\nFrankly, you would prefer to leave. Still, adventurous instincts rebel against cautious nature, daring you to experiment. Do you pick up a fistful of the stuff?", eDialogPic.TERRAIN, 226, ["Leave", "Take"])
    if result == 1:
        pc = SelectPCBox("Select a member of your party:",True)
        if pc == None:
            return
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 4))
        result = ChoiceBox("You draw lots, and the unfortunate loser plunges his hands into the glowing slime. Gritting his teeth, he pulls out a handful of the stuff, passing it between his hands to keep the poison from entering his veins too deeply.\n\nNow what?", eDialogPic.TERRAIN, 226, ["Drink", "Cast"])
        if result == 0:
            MessageBox("Your poor volunteer forces down a mouthful of the stuff. Bravely done, but very, very foolish. The slime burns down his throat, enters his stomach and kills him in ten seconds. You now understand why the wizard locks his door.")
            pc.Kill(None, eLifeStatus.DUST, True)
            Wait()
            return
        elif result == 1:
            MessageBox("Mostly to get rid of the awful stuff, you thrust it at the wall, splashing it against the stone. There is an explosion, throwing you off your feet and soaking you with slime. When you get to your feet, a part of the wall is gone. There is even more smoke.")
            for x in range(40, 41):
                for y in range(14, 17):
                    if Maths.Rand(1,0,100) <= 100:
                        Town.AlterTerrain(Location(x,y), 0, TerrainRecord.UnderlayList[84])
            Timer(Town, 4, False, "RoyalSector_211_TownTimer_19", eTimerType.DELETE)
            Animation_Hold(-1, 074_fireball)
            Wait()
            return
        return

def RoyalSector_187_MapTrigger_38_11(p):
    if StuffDone["8_4"] == 250:
        return
    StuffDone["8_4"] = 250
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(38,11))
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(38,12))
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(38,10))
    MessageBox("Oh, no! It is the top-of-the-line home protector model! You?d better hurry...")

def RoyalSector_190_MapTrigger_41_13(p):
    MessageBox("The Mayor?s desk is filled with documents in imposing piles. One letter lies open on the desk. It is signed Sss-Varbas, the slith ambassador, and reassures Ottar that the Yvoss-tai are of no importance and poses absolutely no threat to Chimney.")

def RoyalSector_191_MapTrigger_40_10(p):
    MessageBox("Perhaps hoping to loot the treasury of the capital, you throw the chest open. No such luck. The chest is filled with documents. But then again, the treasury probably is loaded full of deadly traps, and this chest is not. So perhaps you were lucky?")

def RoyalSector_193_MapTrigger_40_5(p):
    if StuffDone["8_7"] == 250:
        return
    result = ChoiceBox("This table holds a collection of Ottar?s trophies. Among them lies the biggest ruby you have ever seen. It is beautifully cut and set in a shining mithral diadem. If Ottar ever finds out you have stolen it, you will be hung within the hour, heroes or no.", eDialogPic.TERRAIN, 137, ["Leave", "Steal"])
    if result == 1:
        StuffDone["8_7"] = 250
        TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(40,5))
        if StuffDone["8_6"] == 250:
            return
        StuffDone["8_6"] = 250
        MessageBox("The diadem is tied to the table with a small lock. You nervously tug at it, and the loose mithral chain comes off, leaving you with the bare ruby. You pocket it.")
        SpecialItem.Give("MotraxEye")
        return

def RoyalSector_194_MapTrigger_38_5(p):
    if StuffDone["8_8"] == 250:
        return
    StuffDone["8_8"] = 250
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(38,5))
    MessageBox("You are in a hurry. Being caught in here would look very bad on your record. Still, you can?t resist the temptation bred into every adventurer: Rob every important-looking bookshelf you come across.\n\nYou do find a promising magical tome, but then rationality regains control. Instead of reading it here and now, you tuck it under your arm to enjoy it later.")
    SpecialItem.Give("Magictome")

def RoyalSector_195_MapTrigger_6_20(p):
    MessageBox("You find a pile of letters, bound in a velvet ribbon. Seeing that Mina is deeply concentrating about her book, you break the first rule of gentility and read her private letters.\n\nThey are romantic letters from Stanza, your comrade at Brattaskar Fort. It?s a small world. Looking over your shoulder, you envy Stanza for a short moment. Then you remember how his life ended, and change your mind.")

def RoyalSector_196_MapTrigger_11_36(p):
    result = ChoiceBox("The master of arms is here, waiting for you with new orders from the Mayor. You are to remain here in the barracks, talking to no one and doing nothing to influence the political situation. You shake your heads in disbelief.", eDialogPic.CREATURE, 17, ["Accept", "Refuse"])
    if result == 0:
        result = ChoiceBox("Accepting these orders means giving up, allowing the great lords to decide your fate and that of your country. Even if they are mistaken. Are you sure you want to resign to this?", eDialogPic.CREATURE, 17, ["Accept", "Refuse"])
        if result == 0:
            RunScript("GlobalCall_RoyalSector_599", ScriptParameters(eCallOrigin.CUSTOM))
            Timer(Town, 4, False, "RoyalSector_211_TownTimer_19", eTimerType.DELETE)
            Animation_Hold(-1, 074_fireball)
            Wait()
            return
        elif result == 1:
            MessageBox("No, you tell yourselves, you cannot allow the misguided Mayor to ruin his country. Something very wrong is afoot, and you must continue to play your part in averting it. You turn your back on the master at arms.")
            return
        return
    elif result == 1:
        MessageBox("No, you tell yourselves, you cannot allow the misguided Mayor to ruin his country. Something very wrong is afoot, and you must continue to play your part in averting it. You turn your back on the master at arms.")
        return

def RoyalSector_197_MapTrigger_30_36(p):
    if StuffDone["58_1"] == 250:
        return
    StuffDone["58_1"] = 250
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(30,36))
    MessageBox("The nephil barracks are nearly empty. A lone warrior shuffles over to talk to you. \"Mayorr Ottar sent them away\" he mutters, \"the Commanderr and most of the Cat Paws are gone.\" `Why?? you ask, and the nephil shrugs.\n\n\"Ottar won?t let anyone disagree with him. The Commander wanted to strike against the slith invaderrs. Ottar did not. Groul was dismissed.\" `Where did they go?? you ask, and get another shrug. \"North. Into the caves, where nephilim belong.\"")

def RoyalSector_198_MapTrigger_10_24(p):
    MessageBox("Row upon row of public documents line the room. Upon closer inspection you discover that there ought to be even more. Whole shelves of records are missing!")

def RoyalSector_206_MapTrigger_6_27(p):
    MessageBox("You find a note: \"Something is wrong in the records, and now they come to take them away to hide the fault. I cannot allow such manipulation of public documents. I go after them to find out.  -The Keeper of Records.")

def RoyalSector_207_MapTrigger_6_25(p):
    MessageBox("Tucked in among the public records, you find a small prayer book. You eagerly open it and read. After a strenuous session of prayers, you learn the Priest Spell `Curse All?.")
    for pc in Party.EachAlivePC():
        pc.LearnSpell("p_curse_all")

def RoyalSector_208_MapTrigger_16_26(p):
    ChoiceBox("You find a long row of volumes. Picking one, you decide to refresh your knowledge of recent history by reading the Chronicles of Chimney, part VI:\n\n\"At this time, the nephilim entered history in a new sense. Not as raiders or robbers, but as politically versed mercenaries. One band, the Cat Paws, overturned the status quo between the city states of Chimney.\n\n\"Their leader, the now famous Groul, made a pact with a fraction of minor nobles of Myldres, and with their backing he led a stunning series of conquests. The proud Lushwater Toll was ashamed to be the first to fall, to a sudden, wild attack by nephilim.\n\n\"The new rulers of Myldres threatened Milestone, the miner town, with a trade blockade. No traders from that town were allowed across the river Myld. Milestone, ruled more by businessmen than its lord, surrendered without a blow.\n\n\"The nephilim then marched south, stockpiled with supplies from the mines. They laid siege to Flickering Keep in the Shadowlands, and eventually stormed the castle by climbing along the side of the abyss at its back. Lord Fray was killed.\n\n\"After this, the enemies gathered in Whitstone, the last free city. A  battle was brewing when the cave ceiling over the town fell in. Half the inhabitants were killed, along with its lord. So ended the war, leaving Myldres the ruler of all of Chimney.\"", eDialogPic.TERRAIN, 135, ["OK"])

def RoyalSector_209_MapTrigger_39_29(p):
    ChoiceBox("You find a handwritten manuscript abandoned on the desk. Picking it up, you find that it is written by Commander Groul! Its heading says \"Alliance Politics in the Vahnatai War, an Analysis:\n\n\"The Vahnatai, waking up from their hibernation to find their territories invaded, quickly and correctly identified the Empire as their chief adversary. They saw that the minor races were too busy with internal conflicts to significantly affect the war.\n\n\"They concerned themselves instead with the disordered nation Exile. Seeing that the political struggle would be put aside if faced with a powerful alien aggressor, the Vahnatai introduced themselves as an ally in Exile?s struggle against the Empire.\n\n\"The Vahnatai left it to the humans to wear themselves out in the war. Only when the exiles had realized that they by themselves were losing, did fresh Vahnatai troops turn the tide of the war, making Exile victory wholly dependent upon their support.\n\n\"The Vahnatai must have been tempted to turn on their ally and secure full control of the cavern realms. Instead they held, perhaps wisely, that no complete victory could be won until their main opponent, the Empire, had been defeated.\n\n\"The strategy might have worked, except for the often discussed defection of Exile. Their unexpected alliance with their old rival made Exile -definitely the weakest party of the three- the only overall victor, gaining territories and prestige.\"", eDialogPic.STANDARD, 4, ["OK"])

def RoyalSector_210_MapTrigger_12_29(p):
    if StuffDone["58_2"] == 250:
        return
    StuffDone["58_2"] = 250
    TownMap.List["RoyalSector_8"].DeactivateTrigger(Location(12,29))
    MessageBox("Looking at the section on home security, you find a Scroll of Stealth, used as evidence in a trial against a professional burglar years ago. Using scrolls like this, he terrorized the local nobles, entering and leaving their houses unseen.")
    Party.GiveNewItem("ScrollStealth_199")

def RoyalSector_211_TownTimer_19(p):
    MessageBox("The slime has worked its way through your clothes, making you all understand why the volunteer felt so bad about it.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.DISEASE, Maths.MinMax(0, 8, pc.Status(eAffliction.DISEASE) + 2))

def RoyalSector_212_TownTimer_37(p):
    MessageBox("You leave the presence of Mayor Ottar in extreme agitation. He seems uninterested in your version of events! He suppresses your story and smothers the efforts of Locke and Karolynna and yourselves to save your realm from invasion!\n\nCan it be simple pride? Does it bother him to see you and Groul being hailed as heroes? Or has he been bought by the sliths? You have the feeling he is making a dreadful mistake. You wonder where Commander Groul has gone.")

def RoyalSector_213_OnEntry(p):
    MessageBox("Towns in Exile are governed by mayors, not lords. Still, even though Ottar took the title mayor when he conquered Chimney, the Royal Sector retains its name. And your surroundings make you think of nobles, rather than mayors.")
    if StuffDone["7_0"] >= 1:
        Town.PlaceEncounterGroup(1)
        return

def RoyalSector_214_TalkingTrigger14(p):
    ChoiceBox("You show Zarander your rod from Howling Gap and tell him how you got it. He takes it and examines it well.\n\n\"It?s not a slith artifact, I can tell you that right away.\" he mutters while he squints at the runes. \"It?s Vahnatai! Yes, I?m sure it is. Now let?s see...\" Zarander picks a book from his shelf and quickly finds the right passage.\n\n\"The Thunder Rock,\" he finally translates, \"provided by Verundis.\"\n\n\"Verundis? Never heard of him. The name is Vahnatai, and I don?t know many of those. Strange people. Well, somebody who knows more than I of the goings-on in Chimney might tell you who he is.\"\n\nHe hands you the rod back. \"Anything else?\"\n\nYou repeat the name. Verundis, the man who helped the sliths in their invasion, who wanted them to isolate Chimney from the rest of humankind. Who is he? What is his game? You must find this Vahnatai, and put him through serious questioning.", eDialogPic.CREATURE, 28, ["OK"])
    if StuffDone["8_5"] == 250:
        return
    StuffDone["8_5"] = 250
    SpecialItem.Take("Strangerod")
    SpecialItem.Give("Vahnatairod")

def RoyalSector_215_TalkingTrigger21(p):
    if SpecialItem.PartyHas("MotraxEye"):
        if StuffDone["8_9"] == 250:
            return
        StuffDone["8_9"] = 250
        ChoiceBox("Mina gasps when you pull out Motrax? eye. Light is caught and returned manifold from the glowing ruby. Even Oterel rises to get a good look at the red gem.\n\n\"You really did rob a haakai for its treasure, didn?t you?\" You cross your fingers behind your back. They do not recognize Motrax? eye without its diadem chain. You tell an outrageous story of how you stole the ruby in a savage nephil temple on Myld Isle.\n\nMina swallows the bait first, gripping the wonderful jewel from your hands, placing it on her forehead. It looks perfect under her red curls. As she stands purring in front of a mirror, Oterel thanks you.\n\n\"You made her very happy. My regard for you as mercenaries keeps improving. Maybe I?ll give you a steady job in my lifeguard when I get to be mayor! Here is a token of my gratitude.\" He pulls a ring off his finger and gives it to you.\n\nYou suppress a wild smile as you leave the two aristocrats. Any moment now, Mayor Ottar will discover that his proudest trophy has been stolen. The vain Mina won?t wait long to show off her new piece of jewelry, and the trap snaps shut.\n\nTossing Oterel?s ring on your palm, you leave the room. You guess you are even with them now.", eDialogPic.CREATURE, 31, ["OK"])
        SpecialItem.Take("MotraxEye")
        Party.GiveNewItem("SilverRingofSkill_303")
        return

def RoyalSector_216_TalkingTrigger26(p):
    Timer(Town, 3, False, "RoyalSector_212_TownTimer_37", eTimerType.DELETE)
