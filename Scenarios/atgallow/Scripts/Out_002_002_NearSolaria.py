
def NearSolaria_2507_MapTrigger_21_27(p):
    MessageBox("This is one of the forts charged with the protection of the capital city, Solaria. This one protects from attacks from the north. Although there has not really been an aggressor in centuries, the Empire still maintains these fortresses with elite staffing\n\nIn the Empire\'s infancy, these forts were integral in maintaining the solid defense of the capital. Today their function, like most of the military, has become mostly symbolic.")
    p.CancelAction = True

def NearSolaria_2508_MapTrigger_22_45(p):
    ChoiceBox("This is the center of the agency termed Imperial Unspecified Services. The main function of Unspecified Services is to act as the Empire\'s eyes and ears, gathering intelligence through both overt and covert methods.\n\nThe overt methods are done primarily through the bureaucratic channels. Representatives from Unspecified Services gather intelligence reports and monitor ongoing activities throughout the world with the aid of the bureaucracy.\n\nHowever, there are times the bureaucratic channels are ineffective at ascertaining truthful intelligence reports. So the agency uses covert tactics involving agents infiltrating agencies to discover activities.\n\nOften the covert agents of Unspecified Services are used to monitor specific people suspected of security risks by assuming false identities. Many rebels have been taken down with the assistance of such agents.\n\nToday, most of the efforts are focused on the overt bureaucratic side. However, the agency still maintains a large and well-trained network of agents throughout the world.", eDialogPic.STANDARD, 6, ["OK"])
    p.CancelAction = True

def NearSolaria_2509_MapTrigger_44_44(p):
    ChoiceBox("This ancient structure is the first of the Empire\'s Hall of Archives. Contained within is much of the important bureaucratic paperwork and records from the first four centuries of the Empire\'s existence.\n\nToday, these documents serve primarily as references for historians and are of little significance for today\'s Imperial politics. Despite this fact, the Empire maintains a fair number of lower level bureaucrats and guards to maintain and defend them.\n\nFrom what you have heard, these documents are largely intact. One of the greatest innovations of the Aizonic Empire has been the discovery of paper and later methods to magically preserve paper.\n\nThese specially crafted preserved sheets are known to last indefinitely unless subjected to extreme conditions. The paper is highly resistant to chemicals, heat, and tearing. Writing on these sheets requires a special, and expensive, magical ink.\n\nEven with all of this, each archive building is surrounded by a kind of moat of coolant which keeps the temperature of the archive at a constant five degrees Celsius which helps further preserve the paper from aging.\n\nUnfortunately, you cannot access these archives. To do so would require special permission from the bureaucracy which have a slew of forms requesting specific information to be obtained from the search. Not worth your time.", eDialogPic.CREATURE, 31, ["OK"])
    p.CancelAction = True

def NearSolaria_2510_MapTrigger_41_32(p):
    result = ChoiceBox("You have just arrived at the Imperial Treasury. This series of structures is the most well-guarded in the world. There is even more security here than in the Imperial Palace itself, which is probably the second.\n\nBeyond these walls is a great amount of the world\'s wealth. Coins are manufactured here and distributed throughout the Empire only to be returned eventually after taxation.\n\nAlso inside, are some of the world\'s priceless magical artifacts collected throughout the ages.\n\nThere are tours of the treasury being offered for only 50 gold. Do you take the tour?", eDialogPic.STANDARD, 2, ["Leave", "Take"])
    if result == 1:
        if Party.Gold >= 50:
            Party.Gold -= 50
            ChoiceBox("You decide to take the tour. The first thing you are told about is the elite security system, probably to discourage attempts at theft. Each hallway and room is protected by elite guards.\n\nAdditionally, the entire structure is kept under constant magical surveillance as to further boost security. When you get a first hand look, you see the depth of security. There are literally guards watching guards!\n\nThe surveillance system is well hidden within the walls and you cannot find it. The first step of the tour takes you to the ore house, or at least a view of it from a corridor with magically enhanced glass. Here, ore is melted down and processed into bars\n\nThese bars are stored in massive underground storerooms with magically reinforced walls to protect against magical assaults. The second part of the tour takes you to the mint where the bars are melted down and processed into coins.\n\nThe process is very mechanical and automated consisting of large machines and conveyor belts. At the end of the line, hundreds of coins per minute are poured into large bins. This is a definite feat of magical engineering.\n\nThe next area is a room of huge teleporters connecting various points of the world. Not just on the continent, but the world! The energy requirements for such must be immense. Of course, there is only one portal per continent.", eDialogPic.STANDARD, 2, ["OK"])
            ChoiceBox("The gold arrives at a substation on each continent where it is distributed locally through another system of smaller teleporters. This way is much more efficient and much safer than if portals teleported directly from here.\n\nThe tour continues into the offices. Here vast numbers of bureaucrats deliver detailed paperwork on economic conditions throughout the world, each one in charge of only a small area. This includes tracking all sorts of factors such as:\n\nPopulation, growth rate, government programs, industries, special problems, exports, imports, and a multitude of others. The purpose of this is to determine how the supply of treasure should be allocated to maximize the economy.\n\nThese offices are termed the \'Heart of World\', for it is responsible for pumping the gold like blood to all areas of the Empire. Even the slightest failure can lead to severe consequences such as failing businesses, famines, or even rebellion.\n\nThe final part of the tour takes you to the cache of magical artifacts. Priceless objects are on display much in the sense of a museum. Stored here are renowned objects such as the legendary sword Demonslayer and the holy armor, Prachtar\'s Plate.\n\nThe objects here range from the mundane to the exotic. It is not even clear what all of these do. With that, you are led into a gift shop (which you pass) and proceed back to the gates.", eDialogPic.STANDARD, 2, ["OK"])
            p.CancelAction = True
            return
        MessageBox("Unfortunately, you do not have the necessary gold to pay for the tour.")
        p.CancelAction = True
        return
    p.CancelAction = True

def NearSolaria_2511_WanderingOnMeet0(p):
    RunScript("GlobalCall_NorthwesternStolgrad_2853", ScriptParameters(eCallOrigin.CUSTOM))
    return