def Generate_Wandering_8_WurmPit(p):
    if p.Origin != eCallOrigin.TIMER or Maths.Rand(1,1,10) == 1: # Change to frequency of wandering monster generation
        if Town.NPCList.Count > 50 or Town.KillCount >= Town.CreatureKillLimit: return
        r1 = Maths.Rand(1,0,3)
        npcs = []
        if r1 == 0:
            npcs.append([1,NPCRecord.List["OozingSerpent_190"]])
            npcs.append([1,NPCRecord.List["OozingSerpent_190"]])
            npcs.append([1,NPCRecord.List["OozingSerpent_190"]])
        elif r1 == 1:
            npcs.append([1,NPCRecord.List["OozingSerpent_190"]])
            npcs.append([1,NPCRecord.List["OozingSerpent_190"]])
        if len(npcs) > 0:
            l = Location.Zero
            num_tries = 0
            
            while l == Location.Zero and num_tries < 100:
                num_tries += 1
                r2 = Maths.Rand(1,0,3)
                if r2 == 0: l = Location(39,24)
                elif r2 == 1: l = Location(29,22)
                elif r2 == 2: l = Location(19,28)
                elif r2 == 3: l = Location(6,22)
                
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

def WurmPit_155_MapTrigger_23_16(p):
    if StuffDone["9_2"] == 250:
        return
    StuffDone["9_2"] = 250
    TownMap.List["WurmPit_8"].DeactivateTrigger(Location(23,16))
    MessageBox("As you begin to walk down this passage, a strange feeling of dread overwhelms you. You pause. Fortunately, it passes soon enough, and you are able to continue.")

def WurmPit_156_MapTrigger_19_19(p):
    if StuffDone["9_4"] >= 1:
        if SpecialItem.PartyHas("MalachiteStatue"):
            result = ChoiceBox("You return to the skull totems. The stone platform you found the statue on is still here and still bare. You suddenly feel a strange, nearly overwhelming compulsion to replace the statue. Do you?", eDialogPic.TERRAIN, 185, ["No", "Yes"])
            if result == 0:
                MessageBox("You turn away, again taking the statue farther from the totems. The grim objects curse you again.")
                for pc in Party.EachAlivePC():
                    pc.Poison(4)
                return
            elif result == 1:
                MessageBox("You replace the statue. You suddenly feel much better. A strange weight has been lifted from your shoulders. You feel rejuvenated.")
                SpecialItem.Take("MalachiteStatue")
                Party.HealAll(25)
                StuffDone["9_4"] = 0
                return
            return
        MessageBox("You return to the totems. Now that the statue is far away, they seem to have lost their power. This place is cold, empty, and harmless.")
        return
    result = ChoiceBox("Although this cavern seems natural, populated only by mindless creatures and missing the touch of intelligent beings, it clearly has not always been that way. This small alcove contains some sort of sinister shrine.\n\nThere are eight totems, arranged in a circle. They\'re quite old, hundreds of years, and yet mold and decay have barely affected the carved cavewood. At the top of each is the skull of a humanoid. You aren\'t sure of the species, though they had fangs.\n\nIn the middle of the circle is a stone pedestal. Sitting on the pedestal is an intricate, carved statuette. It is of a strange, tentacled monster, carved of malachite and about nine inches high.\n\nAlthough it\'s not exactly pretty, it is a fascinating artifact. Someone somewhere would be sure to pay good money for it.", eDialogPic.TERRAIN, 185, ["Take", "Leave"])
    if result == 0:
        SpecialItem.Give("MalachiteStatue")
        MessageBox("You carefully pick up the statue and put it into your pack. When you do, the feeling of dread which afflicted you when you approached this tunnel returns in full force.\n\nSuddenly, it seems as if the skulls are staring at you, and you feel ill and shaky. Cramps shoot across your abdomens, and sweat breaks out on your foreheads. You can still move, but with difficulty. You leave the circle.")
        StuffDone["9_4"] = 1
        for pc in Party.EachAlivePC():
            pc.Poison(6)
        return
    return

def WurmPit_157_MapTrigger_12_27(p):
    result = ChoiceBox("This cavern contains a small, tranquil pool, fed by a slow, natural spring. The water looks clear, inviting, and relatively algae free.", eDialogPic.TERRAIN, 75, ["Leave", "Drink"])
    if result == 1:
        MessageBox("You drink the water. It fills you with a gentle, pleasant, relaxed feeling.")
        StuffDone["9_0"] = 1
        Timer(Town, 80, False, "WurmPit_182_TownTimer_21", eTimerType.DELETE)
        return

def WurmPit_158_MapTrigger_39_39(p):
    if StuffDone["9_0"] >= 1:
        MessageBox("You reach a circle of grim totems, covered with skulls, bones, and grisly trophies of the slain. The poles are covered with mold and have clearly been here for quite some time. Strangely, being near them makes you feel very uncomfortable.\n\nHowever, the tranquil feeling you got from the drinking from the cave pool is still with you, and you are able to walk among the totems with only mild discomfort.")
        return
    p.CancelAction = True
    if p.Origin == eCallOrigin.MOVING:
        MessageBox("You reach a circle of grim totems, covered with skulls, bones, and grisly trophies of the slain. The poles are covered with mold and have clearly been here for quite some time. Strangely, being near them makes you feel very uncomfortable.\n\nThe closer you get to the totems, the worse they make you feel. It\'s as if the skulls were staring at you, and, for a moment, you think they\'re whispering to you as well. You back away.")

def WurmPit_159_MapTrigger_6_22(p):
    if SpecialItem.PartyHas("MalachiteStatue"):
        if StuffDone["9_5"] >= 1:
            return
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("Suddenly, the statue starts to feel extremely heavy in your pack. You look out the tunnel into the larger cave beyond and start to feel extremely agoraphobic. You turn back. As you do, you feel ill.\n\nAs the waves of nausea overcome you, you would swear you hear someone whisper \"Take the idol back.\"")
        for pc in Party.EachAlivePC():
            pc.Poison(3)
        return

def WurmPit_169_MapTrigger_41_39(p):
    if SpecialItem.PartyHas("MalachiteStatue"):
        StuffDone["9_5"] = 1
        return

def WurmPit_170_MapTrigger_8_24(p):
    if SpecialItem.PartyHas("MalachiteStatue"):
        StuffDone["9_5"] = 0
        return

def WurmPit_179_MapTrigger_10_11(p):
    if StuffDone["8_6"] == 250:
        return
    StuffDone["8_6"] = 250
    TownMap.List["WurmPit_8"].DeactivateTrigger(Location(10,11))
    TownMap.List["MorogsCastle_9"].DeactivateTrigger(Location(41,9))
    MessageBox("This cavern is filled with a thick colony of large, creamy, white mushrooms.")

def WurmPit_180_MapTrigger_7_11(p):
    if Party.HasTrait(Trait.CaveLore):
        if StuffDone["9_7"] == 250:
            return
        result = ChoiceBox("Your knowledge of cave lore pays off. You recognize several of the mushrooms in this alcove. They\'re a very rare variety which is reputed to have great healing properties. Several of them are ripe and ready for plucking.", eDialogPic.TERRAIN, 73, ["Take", "Leave"])
        if result == 0:
            StuffDone["9_7"] = 250
            Party.GiveNewItem("HealingShrooms_391")
        return
        return

def WurmPit_181_TownTimer_0(p):
    if SpecialItem.PartyHas("MalachiteStatue"):
        MessageBox("The statue in your pack suddenly grows very heavy. As you stumble, you begin to sweat, and a familiar unpleasant feeling rises in your stomach.\n\nAs the waves of nausea overcame you, you would swear you heard someone whisper \"Take the idol back.\"")
        for pc in Party.EachAlivePC():
            pc.Poison(3)
        return

def WurmPit_182_TownTimer_21(p):
    MessageBox("The feeling of tranquility passes. You feel agitated again.")
    StuffDone["9_0"] = 0

def Talking_8_38(p):
    if Party.Gold < 30:
        p.TalkingText = "\"I\'m afraid that you don\'t have the gold. Oh, and I wish I could tear your throat out with my fangs.\""
    else:
        Party.Gold -= 30
        Party.Pos = Location(25, 7)
        Town.UpdateVisible()
        Party.HealAll(30, True)
        Party.RestoreSP(25)
        p.TalkingText = "It takes your gold and shows you to your room. As it leaves, it says \"I hope I can keep from killing you in your sleep.\" Then it leaves. Understandably, you don\'t sleep well."
        CentreView(Party.Pos, False)
