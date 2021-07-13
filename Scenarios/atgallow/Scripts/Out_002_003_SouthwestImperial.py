
def SouthwestImperial_2609_MapTrigger_38_9(p):
    ChoiceBox("This place is the Imperial Hall of Justice. It is, essentially, the highest court in the world. All high profile cases involving crimes such as treason and smuggling are tried in these chambers.\n\nAdditionally, this court serves as an appeals for the decision of higher courts. However, most appeals are rejected by the courts and not even given a review.\n\nThere is only one sentence in this court, death. Executions are carried out in the small bunker in the adjacent structure.", eDialogPic.STANDARD, 26, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2610_MapTrigger_34_9(p):
    ChoiceBox("The small tower ahead is the Imperial Gallows where many of the world\'s executions are carried out. The condemned have several choices to die (assuming one is not assigned by the courts), none of them truly painless.\n\nThe most common choice is through ingesting a powerful toxin that brings death within several minutes. Then there is the more immediate, but much more painful, through a well placed kill spell. Quick, but quite painful.\n\nThen there is the classic beheading. Another choice given, but rarely taken, is the option of being slain before a unit of eight skilled Imperial Archers. Usually the true revolutionaries choose this death as a symbol of martyrdom.\n\nThe rarest form is reserved for only the most treacherous traitors or the most vile fiends. It is the classic execution of being tied to a post and being hacked apart by soldiers. It is clearly the most painful and violent way to die.\n\nThere is a grim place before you. Perhaps you should not visit.", eDialogPic.STANDARD, 1024, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2611_MapTrigger_20_17(p):
    ChoiceBox("This is one of the Empire\'s major army bases. Within these walls dwell tens of thousands of Empire soldiers, ready to be deployed anywhere on the continent at a moment\'s notice.\n\nThe truth is, they have not been deployed en masse in centuries, yet the Empire always leaves the military option to deploy a large number of troops on the continent open just in case.", eDialogPic.CREATURE, 14, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2613_MapTrigger_37_32(p):
    ChoiceBox("This is the Fourth Imperial Archive. Also, it is the active one. Just as you reach the gates, a cart full of records passes through. You assume they are to be archived and probably never seen again.\n\nThere were three archives before this one. All are still around, but considered inactive. They contain old records that are really only used by historians and scholars.\n\nThis one, is the only one that can be said to have a practical use. Bureaucrats constantly pour over the records searching for information to assist them in policy making.\n\nYou have heard this archive houses records from the mid-tenth century to the current date (the mid-thirteenth century). Also, this archive is running out of space and is likely by the next generation to be inactive.\n\nBut never fear, the Empire has already provided a remedy. Construction on a Fifth Imperial Archive is already underway. You wonder if they will ever dispose of the earlier records in say the First Archive and just reuse that.", eDialogPic.CREATURE, 31, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2614_MapTrigger_37_25(p):
    ChoiceBox("This is one section of the Empire\'s primary universities. Not all training that the Empire offers is magical, military, or bureaucratic. There are many other areas of profession that are taught like History, Arts, Law, Literature, Mathematics, etc.\n\nThis institution is probably the largest in the Empire training tens of thousands of students in the various professional fields. In addition to being the largest, it is also the most selective. Only the best are selected for apprenticeship here.\n\nUnfortunately, you will not be able to get in because you were not accepted. You chose a different path.", eDialogPic.CREATURE, 21, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2619_MapTrigger_22_8(p):
    ChoiceBox("This is where the Empire conducts some of its magical research. This is not a major institution of research, but one of the minor ones that dot the world. The heavy research is carried out east in the Sorcrega Sector.", eDialogPic.CREATURE, 27, ["OK"])
    p.CancelAction = True

def SouthwestImperial_2620_WanderingOnMeet0(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return
