
def Restock_Shop_Alchemy_Outside_1_3_3(shop):
    shop.Clear()
    shop.AddRecipe("weak_curing")
    shop.AddRecipe("weak_healing")
    shop.AddRecipe("weak_poison")
    shop.AddRecipe("weak_speed")
    shop.AddRecipe("medium_poison")
    shop.AddRecipe("medium_healing_potion")
    shop.AddRecipe("strong_curing_potion")
    shop.AddRecipe("medium_speed")
    shop.AddRecipe("graymold_salve")

def Restock_Shop_Items_2_7(shop):
    shop.Clear()

def Restock_Shop_Items_5_3(shop):
    shop.Clear()
    shop.AddItem(Item.List["RootBread_387"].Copy(True,1), False)
    shop.AddItem(Item.List["RootBread_387"].Copy(True,10), False)
    shop.AddItem(Item.List["RootBread_387"].Copy(True,50), False)

def Restock_Jumble_Shop_0(shop):
    shop.Clear()
    loot_index = [1,1,1,1,2,2,2,3,3,4]
    for a in range(10):
        item = Item.GetTreasure(loot_index[a])
        if item.Variety != eVariety.None and item.Variety != eVariety.Food and item.Variety != eVariety.Gold:
            item.Identified = True
            shop.AddItem(item, False)

def Restock_Shop_Items_5_19(shop):
    shop.Clear()
    shop.AddItem(Item.List["BronzeStuddedArmor_122"].Copy(True), False)
    shop.AddItem(Item.List["BronzeChainMail_123"].Copy(True), False)
    shop.AddItem(Item.List["BronzeBreastplate_124"].Copy(True), False)
    shop.AddItem(Item.List["BronzePlate_125"].Copy(True), False)
    shop.AddItem(Item.List["IronStuddedArmor_126"].Copy(True), False)
    shop.AddItem(Item.List["IronChainMail_127"].Copy(True), False)
    shop.AddItem(Item.List["IronBreastplate_128"].Copy(True), False)
    shop.AddItem(Item.List["IronPlate_129"].Copy(True), False)
    shop.AddItem(Item.List["SteelStuddedArmor_130"].Copy(True), False)
    shop.AddItem(Item.List["SteelChainMail_131"].Copy(True), False)
    shop.AddItem(Item.List["SteelBreastplate_132"].Copy(True), False)
    shop.AddItem(Item.List["SteelPlate_133"].Copy(True), False)

def Restock_Shop_Items_5_26(shop):
    shop.Clear()

def Restock_Shop_Items_6_13(shop):
    shop.Clear()
    shop.AddItem(Item.List["Boots_169"].Copy(True), False)
    shop.AddItem(Item.List["SteelToedBoots_170"].Copy(True), False)

def Restock_Shop_Items_6_17(shop):
    shop.Clear()
    shop.AddItem(Item.List["Pants_4"].Copy(True), False)
    shop.AddItem(Item.List["Pants_5"].Copy(True), False)
    shop.AddItem(Item.List["Shirt_6"].Copy(True), False)
    shop.AddItem(Item.List["Shirt_7"].Copy(True), False)
    shop.AddItem(Item.List["Robes_8"].Copy(True), False)

def Restock_Shop_Items_6_18(shop):
    shop.Clear()
    shop.AddItem(Item.List["VahnataiRobes_30"].Copy(True), False)

def Restock_Shop_Items_6_20(shop):
    shop.Clear()
    shop.AddItem(Item.List["SaltFish_383"].Copy(True,1), False)
    shop.AddItem(Item.List["SaltFish_383"].Copy(True,10), False)
    shop.AddItem(Item.List["SaltFish_383"].Copy(True,50), False)
    shop.AddItem(Item.List["LizardMeat_384"].Copy(True,1), False)
    shop.AddItem(Item.List["LizardMeat_384"].Copy(True,10), False)
    shop.AddItem(Item.List["LizardMeat_384"].Copy(True,50), False)
    shop.AddItem(Item.List["DrakeEgg_385"].Copy(True,1), False)
    shop.AddItem(Item.List["DrakeEgg_385"].Copy(True,10), False)
    shop.AddItem(Item.List["DrakeEgg_385"].Copy(True,50), False)

def Restock_Shop_Items_6_32(shop):
    shop.Clear()
    shop.AddItem(Item.List["IronKnife_51"].Copy(True), False)
    shop.AddItem(Item.List["IronShortSword_52"].Copy(True), False)
    shop.AddItem(Item.List["IronMace_53"].Copy(True), False)
    shop.AddItem(Item.List["IronAxe_54"].Copy(True), False)
    shop.AddItem(Item.List["IronSpear_55"].Copy(True), False)
    shop.AddItem(Item.List["IronHammer_56"].Copy(True), False)
    shop.AddItem(Item.List["IronRapier_57"].Copy(True), False)
    shop.AddItem(Item.List["IronBroadsword_58"].Copy(True), False)
    shop.AddItem(Item.List["IronFlail_59"].Copy(True), False)
    shop.AddItem(Item.List["IronBardiche_60"].Copy(True), False)
    shop.AddItem(Item.List["IronHalberd_61"].Copy(True), False)
    shop.AddItem(Item.List["IronGreatsword_62"].Copy(True), False)
    shop.AddItem(Item.List["IronGreatMace_63"].Copy(True), False)
    shop.AddItem(Item.List["SteelKnife_64"].Copy(True), False)
    shop.AddItem(Item.List["SteelShortSword_65"].Copy(True), False)
    shop.AddItem(Item.List["SteelMace_66"].Copy(True), False)
    shop.AddItem(Item.List["SteelAxe_67"].Copy(True), False)
    shop.AddItem(Item.List["SteelSpear_68"].Copy(True), False)
    shop.AddItem(Item.List["SteelHammer_69"].Copy(True), False)
    shop.AddItem(Item.List["SteelRapier_70"].Copy(True), False)
    shop.AddItem(Item.List["SteelBroadsword_71"].Copy(True), False)
    shop.AddItem(Item.List["SteelFlail_72"].Copy(True), False)
    shop.AddItem(Item.List["SteelBardiche_73"].Copy(True), False)
    shop.AddItem(Item.List["SteelHalberd_74"].Copy(True), False)
    shop.AddItem(Item.List["SteelGreatsword_75"].Copy(True), False)
    shop.AddItem(Item.List["SteelGreatMace_76"].Copy(True), False)

def Restock_Shop_Priest_6_35(shop):
    shop.Clear()
    shop.AddSpell("p_dispel_undead")
    shop.AddSpell("p_remove_curse")
    shop.AddSpell("p_sticks_to_snakes")
    shop.AddSpell("p_martyrs_shield")
    shop.AddSpell("p_cleanse")
    shop.AddSpell("p_firewalk")

def Restock_Shop_Items_6_51(shop):
    shop.Clear()
    shop.AddItem(Item.List["ThrowingKnives_101"].Copy(True), False)
    shop.AddItem(Item.List["IronThrowingKnives_102"].Copy(True), False)
    shop.AddItem(Item.List["Arrows_103"].Copy(True), False)
    shop.AddItem(Item.List["IronArrows_104"].Copy(True), False)

def Restock_Shop_Mage_8_15(shop):
    shop.Clear()
    shop.AddSpell("m_poison")
    shop.AddSpell("m_ice_bolt")
    shop.AddSpell("m_slow_group")
    shop.AddSpell("m_magic_map")

def Restock_Shop_Items_11_5(shop):
    shop.Clear()
    shop.AddItem(Item.List["IronWaveBlade_93"].Copy(True), False)
    shop.AddItem(Item.List["SteelWaveBlade_94"].Copy(True), False)
    shop.AddItem(Item.List["MagicWaveBlade_95"].Copy(True), False)
    shop.AddItem(Item.List["IronRazordisks_96"].Copy(True), False)
    shop.AddItem(Item.List["SteelRazordisks_97"].Copy(True), False)

def Restock_Shop_Mage_11_6(shop):
    shop.Clear()
    shop.AddSpell("m_capture_soul")
    shop.AddSpell("m_simulacrum")

def Restock_Jumble_Shop_1(shop):
    shop.Clear()
    loot_index = [1,1,1,1,2,2,2,3,3,4]
    for a in range(10):
        item = Item.GetTreasure(loot_index[a])
        if item.Variety != eVariety.None and item.Variety != eVariety.Food and item.Variety != eVariety.Gold:
            item.Identified = True
            shop.AddItem(item, False)
