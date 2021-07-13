using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace SwordsOfExileGame
{
    class AlchemyShopWindow : GuiWindow
    {
        ConversationWindow calledFromTalk = null;

        Shop _Shop;
        //string ShopName = null;
        //List<Recipe> SpellsForSale = null;
        //int costAdjust;

        ListBox spellListBox;
        Button cancelButton, buyButton;

        Recipe selectedSpell;

        Label selSpellTitle, goldLabel;
        RichTextBox selSpellDesc;

        public AlchemyShopWindow(Shop shop, ConversationWindow shopcaller)//, List<Recipe> spelllist, int costadjust, string shopname)
            : base(0, 0, 500, 480, true, false, true, true, true)
        {
            _Shop = shop;

            calledFromTalk = shopcaller;

            Position(-2, -2);
            spellListBox = AddListBox(changedSelected, 0, 130, 200, InnerHeight - 10, -1);
            spellListBox.Position(10, 10, -1, -1);
            cancelButton = AddButton(pressCancel, "Finish Shopping", 238, InnerHeight - 30, 230, 30);

            buyButton = AddButton(pressBuy, "Buy", 238, InnerHeight - 60, 230, 30);

            Label l = AddLabel(_Shop.Name, 238, 10, 230, -1, true);
            l.Font = Gfx.TalkFontNormal;

            Label l2 = AddLabel("Prices here are " + _Shop.PriceWord, 238, 30, 230, -1, true);

            goldLabel = AddLabel("You have " + Party.Gold + " gold", 238, 50, 230, -1, true);

            selSpellTitle = AddLabel("Yo!", 238, 200, 230, 30, false);
            selSpellTitle.BackColour = Color.Black;
            selSpellTitle.Font = Gfx.TalkFontNormal;
            selSpellTitle.Padding = 4;

            selSpellDesc = AddBlankRichTextBox(null, 238, 230, 230, 160);
            selSpellDesc.BackColour = Color.Black;
            selSpellDesc.Padding = 4;
            selSpellDesc.FontNormal = Gfx.TinyFont;
            selSpellDesc.FontBold = Gfx.SmallBoldFont;
            selSpellDesc.FontItalic = Gfx.ItalicFont;

            LineUpControlsDown(238, 10, 0, l, l2, goldLabel, selSpellTitle, selSpellDesc, buyButton, cancelButton);

            Resize(500, cancelButton.Y + cancelButton.Height + 10 + Gfx.FRAME_HEIGHT * 2);
            spellListBox.Resize(200, InnerHeight - 20);

            UpdateSpellList();
        }

        void changedSelected(bool user_caused, ListBoxItem item)
        {
            if (item == null)
            {
                selSpellTitle.Text = _Shop.Name;
                selSpellDesc.FormatText("Choose the recipe to purchase from the list to the left.");
                buyButton.Enabled = false;
                return;
            }

            selectedSpell = item.Tag as Recipe;
            selSpellTitle.Text = selectedSpell.Name;

            string ingredients = "";
            foreach (var t in selectedSpell.Ingredients)
            {
                int has = 0;
                foreach (PCType pc in Party.PCList)
                {
                    foreach (Item i in pc.EachItemHeld())
                        if (i.AlchemyID == t.Item1) has += i.Charges;
                }

                ingredients += String.Format("  @i{0} ({1}{2}{3}/{4})@e@n",
                    Recipe.GetIngredientName(t.Item1),
                    has >= t.Item2 ? "@b" : "",
                    has,
                    has >= t.Item2 ? "@i" : "",
                    t.Item2);
            }

            string cannotcast = "";

            buyButton.Enabled = false;

            if (Party.KnownRecipes.ContainsValue(selectedSpell))
                cannotcast = "You already have this recipe";
            else if (Party.Gold < _Shop.BuyCost(selectedSpell.Price)) cannotcast = "You don't have enough gold to purchase this recipe";
            else
                buyButton.Enabled = true;


            selSpellDesc.FormatText(String.Format("@bPRICE: {0}@e@n@bSKILL REQUIRED: {1}@e@n@bINGREDIENTS: @e@n{2}@n{3}@n@n@i{4}",
                _Shop.BuyCost(selectedSpell.Price),
                selectedSpell.Skill,
                ingredients,
                selectedSpell.Description,
                cannotcast
                ));
        }

        //int spellPrice(Recipe spell)
        //{
        //    return (spell.Price * Constants.SHOP_PRICE_MULTIPLIER[costAdjust]) / 10;//for now.
        //}

        void pressCancel(Control b)
        {
            KillMe = true;
        }

        void pressBuy(Control b)
        {
            Party.Gold -= _Shop.BuyCost(selectedSpell.Price);
            Party.KnownRecipes.Add(selectedSpell.ID, selectedSpell);
            Recipe s = selectedSpell;
            UpdateSpellList();
            selSpellTitle.Text = "Recipe Purchased";
            selSpellDesc.FormatText("Your party learns the recipe for '" + s.Name + "'");
            Sound.Play("038_coinsoncounter");
        }

        public void UpdateSpellList()
        {
            var litem = spellListBox.SelectedItem == null ? null : spellListBox.SelectedItem.Tag;
            spellListBox.Clear();

            foreach (Recipe ms in _Shop.EachRecipe())
            {
                if (Party.KnownRecipes.ContainsValue(ms))
                    spellListBox.AddItem(ms.Name, Color.DarkGray, ms, true);
                else if (Party.Gold < _Shop.BuyCost(ms.Price))
                    spellListBox.AddItem(String.Format("{0} ({1})", ms.Name, _Shop.BuyCost(ms.Price)), Color.LightGray, ms, true);
                else
                    spellListBox.AddItem(String.Format("{0} ({1})", ms.Name, _Shop.BuyCost(ms.Price)), Color.Gold, ms, false);
            }

            spellListBox.SelectedItem = spellListBox.Items.Count > 0 ? spellListBox.Items[0] : null;
            foreach (ListBoxItem l in spellListBox.Items)
                if (l.Tag == litem)
                {
                    spellListBox.SelectedItem = l;
                    break;
                }

            if (spellListBox.SelectedItem != null) spellListBox.RevealItem(spellListBox.SelectedItem);
            changedSelected(false, spellListBox.SelectedItem);
            goldLabel.Text = "You have " + Party.Gold + " gold";

            buyButton.Caption = "Buy";

        }

        public override void Close()
        {
            base.Close();
            if (calledFromTalk != null)
            {
                calledFromTalk.Visible = true;
                //Gui.KeyFocusWindow = calledFromTalk;
            }
        }


    }



}