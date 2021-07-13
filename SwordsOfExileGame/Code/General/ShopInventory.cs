using System;
using System.IO;
using System.Collections.Generic;
using System.Text;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    public class Shop : IListEntity, IInventory
    {
        public static ExileList<Shop> List = new ExileList<Shop>();

        public string ID { get { return id; } set { id = value; } }
        string id;

        public eShop ShopType;
        int restockTime;
        string FuncOnRestock;
        public string Name;
        uint willBuy;
        int costLevel;

        List<Item> itemList;
        List<int> slotList;
        List<MagicSpell> spellList;
        List<Recipe> recipeList;

        eItemFilter _Filter;
        public eItemFilter Filter
        {
            get { return _Filter; }
            set
            {
                _Filter = value;
                //Remake slot list according to the new filter.
                slotList.Clear();

                int n = 0;
                foreach (Item i in itemList)
                {
                    if (i.Filter(_Filter))
                        slotList.Add(n++);
                    else
                        slotList.Add(-1);
                }
            }
        }

        public Shop() { }

        public void Load(BinaryReader In)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            ShopType = (eShop)In.ReadByte();

            restockTime = In.ReadInt32();
            FuncOnRestock = In.ReadString();
            costLevel = In.ReadInt16();
            Name = In.ReadString();

            if (ShopType == eShop.ITEM)
            {
                willBuy = In.ReadUInt32();
                itemList = new List<Item>();
                slotList = new List<int>();
            }
            else if (ShopType == eShop.MAGIC)
            {
                spellList = new List<MagicSpell>();
                In.ReadUInt32();
            }
            else if (ShopType == eShop.ALCHEMY)
            {
                recipeList = new List<Recipe>();
                In.ReadUInt32();
            }

            List.Add(this);
        }

        public static void RestockAll(int time = -1)
        {
            foreach (Shop shop in List)
            {
                if (time == -1 || (shop.restockTime != -1 && time % shop.restockTime == 0))
                {
                    Script.RunShopRestock(shop.FuncOnRestock, shop);
                }
            }
        }

        public void LoadGame(BinaryReader file)
        {

            if (ShopType == eShop.ITEM)
            {
                itemList.Clear();
                slotList.Clear();
                int count = file.ReadInt32();
                for (int n = 0; n < count; n++)
                {
                    Item i = new Item();
                    i.LoadInstance(file);
                    itemList.Add(i);
                    slotList.Add(file.ReadInt32());
                }
            }
            else if (ShopType == eShop.MAGIC)
            {
                spellList.Clear();
                int count = file.ReadInt32();
                for (int n = 0; n < count; n++)
                    spellList.Add(MagicSpell.List[file.ReadInt32()]);
            }
            else if (ShopType == eShop.ALCHEMY)
            {
                recipeList.Clear();
                int count = file.ReadInt32();
                for (int n = 0; n < count; n++)
                    recipeList.Add(Recipe.List[file.ReadInt32()]);
            }
        }

        public void SaveGame(BinaryWriter file)
        {
            if (ShopType == eShop.ITEM)
            {

                file.Write(itemList.Count);
                for (int n = 0; n < itemList.Count; n++)
                {
                    Item i = itemList[n];
                    i.SaveGame(file);
                    file.Write(slotList[n]);
                }
            }
            else if (ShopType == eShop.MAGIC)
            {
                file.Write(spellList.Count);
                for (int n = 0; n < spellList.Count; n++)
                {
                    file.Write(MagicSpell.List.IndexOf(spellList[n]));
                }
            }
            else if (ShopType == eShop.ALCHEMY)
            {
                file.Write(recipeList.Count);
                for (int n = 0; n < recipeList.Count; n++)
                {
                    file.Write(Recipe.List.IndexOf(recipeList[n]));
                }
            }
        }

        public void Clear()
        {
            if (ShopType == eShop.ITEM)
            {
                itemList.Clear();
                slotList.Clear();
            }
            else if (ShopType == eShop.MAGIC)
                spellList.Clear();
            else if (ShopType == eShop.ALCHEMY)
                recipeList.Clear();
        }

        public bool Run()
        {
            new ItemShopWindow(this, null);
            return true;
        }

        public bool SellTo(Item i)
        {
            if (WillBuy(i))
            {
                Sound.Play("039_coinsjingle");
                Game.AddMessage("You sell it.");
                Game.CurrentParty.Gold += i.Value;
                return true;
            }
            else
            {
                Game.AddMessage("This shop doesn't buy that item.");
                return false;
            }
        }

        public string SellToShopDescription()
        {
            StringBuilder sb = new StringBuilder();
            List<string> things = new List<string>();

            //         RN B  Cr Tr No Po Nk          Gl He                                  2  1                              
            //         No ol sb sr nU is lc Ri Bo    ov lm Ar Sh Fo To Wa Sc Po Th Ar Bo Go Hn Hn -                                                         
            //         Am ts ow s  se on    ng ot    es    mr ld od ol nd rl tn rn rw w  ld dd dd                                                  
            //   27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9  8  7  6  5  4  3  2  1  0

            //   0  0  1  1  1  1  1  1  1  1  1  0  1  1  1  1  1  1  1  1  1  1  1  1  0  1  1  0 all items      0x03FEFFF6
            //   0  0  1  1  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  1  0  1  1  0 all weapons    0x03800056
            //   0  0  0  0  0  1  0  0  0  0  1  1  1  1  1  1  0  0  0  0  0  0  0  0  0  0  0  0 all armour     0x0021F800
            //   0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  0 Melee Weapons  0x00000006
            //   0  0  1  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  1  0  0  0  0 Ranged weapons 0x02800050
            //   0  0  0  0  0  1  0  0  0  0  1  0  1  1  1  0  0  0  0  0  0  0  0  0  0  0  0  0 Clothing       0x0042E000
            //   0  0  0  0  0  0  0  0  1  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 Jewelery       0x000C0000
            //   0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  1  0  0  0  0  0 Projects       0x01000060

            uint w = willBuy;

            if ((w & 0x03FEFFF6) == 0) things.Add("Nothing");
            else
            {
                if ((w & 0x03FEFFF6) == 0x03FEFFF6) { things.Add("All Items"); w -= 0x03FEFFF6; }
                if ((w & 0x03800056) == 0x03800056) { things.Add("All Weapons"); w -= 0x03800056; }
                if ((w & 0x0021F800) == 0x0021F800) { things.Add("All Armour"); w -= 0x0021F800; }
                if ((w & 0x00000006) == 0x00000006) { things.Add("Melee Weapons"); w -= 0x00000006; }
                if ((w & 0x02800050) == 0x02800050) { things.Add("Ranged Weapons"); w -= 0x02800050; }
                if ((w & 0x0042E000) == 0x0042E000) { things.Add("Clothing"); w -= 0x0042E000; }
                if ((w & 0x000C0000) == 0x000C0000) { things.Add("Jewellry"); w -= 0x000C0000; }
                if ((w & 0x01000060) == 0x01000060) { things.Add("Projectiles"); w -= 0x01000060; }

                for (int n = 1; n < 26; n++)
                    if ((w & (int)Math.Pow(2, n)) != 0)
                        switch ((eVariety)n)
                        {
                            case eVariety.Armour: sb.Append("Armour"); break;
                            case eVariety.Arrows: sb.Append("Arrows"); break;
                            case eVariety.Bolts: sb.Append("Bolts"); break;
                            case eVariety.Boots: sb.Append("Boots"); break;
                            case eVariety.Bow: sb.Append("Bows"); break;
                            case eVariety.Crossbow: sb.Append("Crossbows"); break;
                            case eVariety.Food: sb.Append("Food"); break;
                            case eVariety.Gloves: sb.Append("Gloves"); break;
                            case eVariety.Helm: sb.Append("Helms"); break;
                            case eVariety.Necklace: sb.Append("Necklaces"); break;
                            case eVariety.NonUse: sb.Append("Sundry"); break;
                            case eVariety.OneHanded: sb.Append("One-Handed Weapons"); break;
                            case eVariety.Poison: sb.Append("Poisons"); break;
                            case eVariety.Potion: sb.Append("Potions"); break;
                            case eVariety.RangedNoAmmo: sb.Append("Slings"); break;
                            case eVariety.Ring: sb.Append("Rings"); break;
                            case eVariety.Scroll: sb.Append("Scrolls"); break;
                            case eVariety.Shield: sb.Append("Shields"); break;
                            case eVariety.Thrown: sb.Append("Thrown Weapons"); break;
                            case eVariety.Tool: sb.Append("Tools"); break;
                            case eVariety.Trousers: sb.Append("Trousers"); break;
                            case eVariety.TwoHanded: sb.Append("Two-Handed Weapons"); break;
                            case eVariety.Wand: sb.Append("Wands"); break;
                        }
            }
            for (int n = 0; n < things.Count; n++)
            {
                if (n > 0 && n < things.Count - 1) sb.Append(", ");
                else if (n > 0 && n == things.Count - 1) sb.Append(" & ");
                sb.Append(things[n]);
            }

            return sb.ToString();
        }

        public Location Pos { get; set; }
        public IEnumerable<Tuple<Item, int>> EachItem()
        {
            if (ShopType != eShop.ITEM) yield break;
            for (int n = 0; n < itemList.Count; n++)
            {
                if (itemList[n].Filter(_Filter)) yield return new Tuple<Item, int>(itemList[n], slotList[n]);
            }
        }
        public IEnumerable<MagicSpell> EachSpell()
        {
            if (ShopType != eShop.MAGIC) yield break;
            foreach (MagicSpell m in spellList) yield return m;
        }
        public IEnumerable<Recipe> EachRecipe()
        {
            if (ShopType != eShop.ALCHEMY) yield break;
            foreach (Recipe r in recipeList) yield return r;
        }

        public Item PlaceItem(Item item, int slotno) { return null; }

        public bool AddItem(Item item, bool stack)
        {
            if (ShopType != eShop.ITEM) return false;
            if (item == null) return true;

            if (stack)
                //Stack an item if it's combinable with one already held.
                foreach (Item i in itemList)
                    if (item != i && item.CombinableWith(i))
                    {
                        i.Charges += item.Charges;
                        if (i.Charges > Constants.ITEM_STACK_LIMIT) { item.Charges = i.Charges - Constants.ITEM_STACK_LIMIT; i.Charges = Constants.ITEM_STACK_LIMIT; continue; } //Can only stack to 999
                        return true;
                    }

            int n = 0;
            bool slotfree = false;
            while (!slotfree)
            {
                int m = 0;
                slotfree = true;
                foreach (Item i in itemList)
                {
                    if (slotList[m++] == n) { n++; slotfree = false; break; }
                }
            };

            slotList.Add(n);
            itemList.Add(item);
            return true;
        }

        public bool RemoveItem(Item item)
        {
            return true;
        }

        public void ArrangeItems() { } //No need for this in shops.

        public Item GetSlot(int slotno)
        {
            if (ShopType != eShop.ITEM) return null;
            int n = 0;
            foreach (int i in slotList)
            {
                if (i == slotno /*&& i != Gui.MoveItem*/) return itemList[n];
                n++;
            }
            return null;
        }

        public bool InventorysClose(IInventory other) { return true; }
        public void MakeInventoryPopUpWindow(Item c)
        {
            var popupoptions = new List<PopUpMenuData>();

            if (c != null)
            {
                Gui.DragItem = null;
                popupoptions.Add(new PopUpMenuData("Buy for " + BuyCost(c.Value) + " gold", c, null, PopUpMenuData.BUY));
                new PopUpMenu(handlePopUp, popupoptions);
            }
        }

        void handlePopUp(object o, object o2, int data)
        {
            Item c = (Item)o;
            PCType pc = Game.CurrentParty.CurrentPC;
            switch (data)
            {
                case PopUpMenuData.BUY:
                    var a = new Action(eAction.BuyItem) { PC = Game.CurrentParty.CurrentPC, Item = c, InventoryFrom = this, InventoryTo = Game.CurrentParty.CurrentPC, Loc = new Location(-1, -1) };
                    a.PlaceDraggedItem(eAction.PlaceInInventory);
                    new Action(eAction.NONE);
                    break;
            }
        }

        public int BuyCost(int i)
        {
            return i * Constants.SHOP_PRICE_MULTIPLIER[costLevel] / 10;
        }

        public bool WillBuy(Item i)
        {
            if (ShopType != eShop.ITEM) return false;
            if (!i.Identified) return false;
            if ((willBuy & (uint)Math.Pow(2, (int)i.Variety)) == 0) return false;
            return true;
        }

        public void AddSpell(MagicSpell s)
        {
            if (ShopType != eShop.MAGIC) return;
            if (!spellList.Contains(s)) spellList.Add(s);
        }
        public void AddSpell(string s)
        {
            if (ShopType != eShop.MAGIC) return;
            if (MagicSpell.List.Contains(s)) AddSpell(MagicSpell.List[s]);
        }
        public void AddRecipe(Recipe r)
        {
            if (ShopType != eShop.ALCHEMY) return;
            if (!recipeList.Contains(r)) recipeList.Add(r);
        }
        public void AddRecipe(string s)
        {
            if (ShopType != eShop.ALCHEMY) return;
            if (Recipe.List.Contains(s)) AddRecipe(Recipe.List[s]);
        }
        public void RemoveSpell(MagicSpell s)
        {
            if (ShopType != eShop.MAGIC) return;
            if (spellList.Contains(s)) spellList.Remove(s);
        }
        public void RemoveSpell(string s)
        {
            if (ShopType != eShop.MAGIC) return;
            if (MagicSpell.List.Contains(s)) RemoveSpell(MagicSpell.List[s]);
        }
        public void RemoveRecipe(Recipe r)
        {
            if (ShopType != eShop.ALCHEMY) return;
            if (recipeList.Contains(r)) recipeList.Remove(r);
        }
        public void RemoveRecipe(string s)
        {
            if (ShopType != eShop.ALCHEMY) return;
            if (Recipe.List.Contains(s)) RemoveRecipe(Recipe.List[s]);
        }
        
        public void MakeItemToolTip(Item i, XnaRect r)
        {
            if (i != null)
            {
                string txt = i.TooltipInfo() + "@n@e@7" + "Cost: " + BuyCost(i.Value) + " gold";
                new ToolTipV2(false, r, txt, -1);
            }
        }

        public string PriceWord
        {
            get
            {
                string[] w = {"extremely cheap",
			                "very reasonable",
			                "pretty average",
			                "somewhat pricey",
			                "expensive",
			                "exorbitant",
			                "utterly ridiculous"};
                return w[Maths.MinMax(0, 6, costLevel)];
            }
        }
    }
}