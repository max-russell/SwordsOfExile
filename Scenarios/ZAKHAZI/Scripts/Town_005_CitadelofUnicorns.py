
def CitadelofUnicorns_125_MapTrigger_31_17(p):
    if StuffDone["5_0"] < 1:
        p.CancelAction = True
        if p.Origin == eCallOrigin.MOVING:
            MessageBox("As you start to walk into this wing of the unicorn\'s dome, the air starts to feel very cold. The farther in you walk, the more uncomfortable you feel. Your skin begins to itch, and you feel like something is watching you.\n\nEventually, you can\'t take it anymore. You walk back out.")
        return

def CitadelofUnicorns_128_OnEntry(p):
    if StuffDone["5_2"] == 250:
        return
    StuffDone["5_2"] = 250
    ChoiceBox("You arrive at a bright, glowing citadel, its elegantly curved walls and delicate spires providing a delightful respite from the unrelenting sameness of these caverns.\n\nThe structure has one central dome with four smaller domes circling it, which are attached to the main structure by tunnels. The walls of the building are white marble. The stone glows slightly.\n\nA stone path leads into the central chamber of the dome. Looking inside, you see patches of grass and other surface plants! For the first time in quite a while, you smell flowers and the the pleasant tang of evergreens.\n\nThis is a beautiful place, and inside the dome you can see one of the beings responsible. It\'s a unicorn, grazing daintily on the grass. It looks up, sees you, and scampers into one of the side domes.", eDialogPic.CREATURE, 149, ["OK"])

def CitadelofUnicorns_129_CreatureDeath0(p):
    MessageBox("As the unicorn falls, you begin to feel ill. Whenever someone slays one of these beautiful, magical creatures, there is a horrible price that must be paid.\n\nEventually, the illness leaves you. However, the weakness it leaves behind doesn\'t go away. Somehow, you suspect it never will.")
    for pc in Party.EachAlivePC():
        pc.SetSkill(eSkill.STRENGTH, pc.GetSkill(eSkill.STRENGTH) - 2)

def CitadelofUnicorns_132_TalkingTrigger26(p):
    if StuffDone["5_0"] == 0:
        p.TalkingText = "\"A unicorn\'s horn contains a good measure of its spirit. To lay one of our number truly to rest, the horn must be present. By taking her horn, the giants have taken some of my love\'s memory from me.\"\n\n\"We could reward you well if the horn was recovered from the giants. Would you accept this mission?\""
        return
        return
    if SpecialItem.PartyHas("UnicornHorn"):
        if StuffDone["5_1"] == 250:
            return
        StuffDone["5_1"] = 250
        p.TalkingText = "You present the horn to Aetherius. Overcome, he touches the tip of his horn to the ground in a sign of respect. He carries the horn in his mouth out of the dome. When he returns, he casts a spell.\n\nThe charm he gave you earlier turns into a small horn, made of amber. \"That is a part of your reward.\""
        SpecialItem.Take("UnicornHorn")
        for pc in Party.EachAlivePC():
            pc.AwardXP(20)
        SpecialItem.Take("HornCharm")
        SpecialItem.Give("UnicornCharm")
        return
    if StuffDone["5_1"] >= 1:
        p.TalkingText = "\"My mate\'s horn has been hidden in a place of great respect. Now my mourning can truly begin. First, however, I want to make sure you have received an adequate reward.\""
        return

def CitadelofUnicorns_133_TalkingTrigger31(p):
    if StuffDone["5_0"] < 1:
        p.TalkingText = "\"Wonderful. I thank you. I can give you something to help you.\" He leaves, and returns with a charm. It is a small, silver horn, on a delicate chain. He gives it to you.\n\n\"When you are in the giant\'s lair, it will let you know when you are near my mate\'s horn. Return it to me, and I will reward you well. Also, we have spare supplies.\""
        StuffDone["5_0"] = 1
        SpecialItem.Give("HornCharm")
        return
    if StuffDone["5_1"] < 1:
        p.TalkingText = "\"The giants have her horn. I have given you a charm to help find it. That is all I can say.\""
        return
