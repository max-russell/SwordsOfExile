using System;
using Microsoft.Xna.Framework;

namespace SwordsOfExileGame
{
    class MagicShopWindow : GuiWindow
    {
        ConversationWindow calledFromTalk = null;

        Shop _Shop;

        ListBox spellListBox;
        Button cancelButton, buyButton;

        MagicSpell selectedSpell;

        Label selSpellTitle, goldLabel;
        RichTextBox selSpellDesc;

        public MagicShopWindow(Shop shop, ConversationWindow shopcaller)
            : base(0, 0, 500, 480, true, true, false, true, true)
        {
            Action.LockActions = eAction.MAGIC_LOCK_ACTIONS;
            Gui.MagicShopIsOpen = this;
            calledFromTalk = shopcaller;
            _Shop = shop;

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
                selSpellDesc.FormatText("Choose the party member to purchase the spell, and the spell to learn from the list to the left.");
                buyButton.Enabled = false;
                return;
            }

            selectedSpell = item.Tag as MagicSpell;
            selSpellTitle.Text = selectedSpell.Name;

            string where = selectedSpell.GetWhereString();

            string cannotcast = "";

            buyButton.Enabled = false;

            if (Party.CurrentPC.KnownSpells.ContainsValue(selectedSpell))
                cannotcast = Party.CurrentPC.Name + " already knows this spell";
            else if (Party.Gold < _Shop.BuyCost(selectedSpell.Cost)) cannotcast = "You don't have enough gold to purchase this spell";
            else
                buyButton.Enabled = true;

            selSpellDesc.FormatText(String.Format("@bLEVEL {0} {1} SPELL@e@n@bCOST: {2} SP@n{5}WHERE: {6}@e@n@bPRICE: {7} gold@e@n@n{3}@n@n@i{4}",
                selectedSpell.Level,
                selectedSpell.Mage ? "MAGE" : "PRIEST",
                selectedSpell.Cost,
                selectedSpell.Description,
                cannotcast,
                selectedSpell.Range == 0 ? "" : "RANGE: " + selectedSpell.Range + "@n",
                where,
                _Shop.BuyCost(selectedSpell.Cost)));
        }

        void pressCancel(Control b)
        {
            KillMe = true;
        }

        void pressBuy(Control b)
        {
            Party.Gold -= _Shop.BuyCost(selectedSpell.Cost);
            Party.CurrentPC.KnownSpells.Add(selectedSpell.ID, selectedSpell);
            MagicSpell s = selectedSpell;
            UpdateSpellList();
            selSpellTitle.Text = "Spell Purchased";
            selSpellDesc.FormatText(Party.CurrentPC.Name + " learns the spell '" + s.Name + "'");
            Sound.Play("038_coinsoncounter");
        }

        public void UpdateSpellList()
        {
            var litem = spellListBox.SelectedItem == null ? null : spellListBox.SelectedItem.Tag;
            spellListBox.Clear();

            foreach (MagicSpell ms in _Shop.EachSpell())
            {
                if (Party.CurrentPC.KnownSpells.ContainsValue(ms))
                    spellListBox.AddItem(ms.Name, Color.DarkGray, ms, true);
                else if (Party.Gold < _Shop.BuyCost(ms.Cost))
                    spellListBox.AddItem(String.Format("{0} ({1})", ms.Name, _Shop.BuyCost(ms.Cost)), Color.LightGray, ms, true);
                else
                    spellListBox.AddItem(String.Format("{0} ({1})", ms.Name, _Shop.BuyCost(ms.Cost)), ms.Mage ? Color.Fuchsia : Color.LightSkyBlue, ms, false);
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

            buyButton.Caption = "Buy (" + Party.CurrentPC.Name + ")";

        }

        public override void Close()
        {
            base.Close();
            if (calledFromTalk != null)
            {
                calledFromTalk.Visible = true;
            }
            Action.LockActions = eAction.NONE;
            Gui.MagicShopIsOpen = null;
        }
    }


}