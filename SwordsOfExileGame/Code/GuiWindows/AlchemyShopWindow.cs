using System;
using Microsoft.Xna.Framework;

namespace SwordsOfExileGame;

internal class AlchemyShopWindow : GuiWindow
{
    private ConversationWindow calledFromTalk = null;

    private Shop _Shop;

    private ListBox spellListBox;
    private Button cancelButton, buyButton;

    private Recipe selectedSpell;

    private Label selSpellTitle, goldLabel;
    private RichTextBox selSpellDesc;

    public AlchemyShopWindow(Shop shop, ConversationWindow shopcaller)
        : base(0, 0, 500, 480, true, false, true, true, true)
    {
        _Shop = shop;

        calledFromTalk = shopcaller;

        Position(-2, -2);
        spellListBox = AddListBox(changedSelected, 0, 130, 200, InnerHeight - 10, -1);
        spellListBox.Position(10, 10, -1, -1);
        cancelButton = AddButton(pressCancel, "Finish Shopping", 238, InnerHeight - 30, 230, 30);

        buyButton = AddButton(pressBuy, "Buy", 238, InnerHeight - 60, 230, 30);

        var l = AddLabel(_Shop.Name, 238, 10, 230, -1, true);
        l.Font = Gfx.TalkFontNormal;

        var l2 = AddLabel("Prices here are " + _Shop.PriceWord, 238, 30, 230, -1, true);

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

    private void changedSelected(bool user_caused, ListBoxItem item)
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

        var ingredients = "";
        foreach (var t in selectedSpell.Ingredients)
        {
            var has = 0;
            foreach (var pc in Party.PCList)
            {
                foreach (var i in pc.EachItemHeld())
                    if (i.AlchemyID == t.Item1) has += i.Charges;
            }

            ingredients += string.Format("  @i{0} ({1}{2}{3}/{4})@e@n",
                Recipe.GetIngredientName(t.Item1),
                has >= t.Item2 ? "@b" : "",
                has,
                has >= t.Item2 ? "@i" : "",
                t.Item2);
        }

        var cannotcast = "";

        buyButton.Enabled = false;

        if (Party.KnownRecipes.ContainsValue(selectedSpell))
            cannotcast = "You already have this recipe";
        else if (Party.Gold < _Shop.BuyCost(selectedSpell.Price)) cannotcast = "You don't have enough gold to purchase this recipe";
        else
            buyButton.Enabled = true;


        selSpellDesc.FormatText(string.Format("@bPRICE: {0}@e@n@bSKILL REQUIRED: {1}@e@n@bINGREDIENTS: @e@n{2}@n{3}@n@n@i{4}",
            _Shop.BuyCost(selectedSpell.Price),
            selectedSpell.Skill,
            ingredients,
            selectedSpell.Description,
            cannotcast
        ));
    }

    private void pressCancel(Control b)
    {
        KillMe = true;
    }

    private void pressBuy(Control b)
    {
        Party.Gold -= _Shop.BuyCost(selectedSpell.Price);
        Party.KnownRecipes.Add(selectedSpell.ID, selectedSpell);
        var s = selectedSpell;
        UpdateSpellList();
        selSpellTitle.Text = "Recipe Purchased";
        selSpellDesc.FormatText("Your party learns the recipe for '" + s.Name + "'");
        Sound.Play("038_coinsoncounter");
    }

    public void UpdateSpellList()
    {
        var litem = spellListBox.SelectedItem?.Tag;
        spellListBox.Clear();

        foreach (var ms in _Shop.EachRecipe())
        {
            if (Party.KnownRecipes.ContainsValue(ms))
                spellListBox.AddItem(ms.Name, Color.DarkGray, ms, true);
            else if (Party.Gold < _Shop.BuyCost(ms.Price))
                spellListBox.AddItem(string.Format("{0} ({1})", ms.Name, _Shop.BuyCost(ms.Price)), Color.LightGray, ms, true);
            else
                spellListBox.AddItem(string.Format("{0} ({1})", ms.Name, _Shop.BuyCost(ms.Price)), Color.Gold, ms, false);
        }

        spellListBox.SelectedItem = spellListBox.Items.Count > 0 ? spellListBox.Items[0] : null;
        foreach (var l in spellListBox.Items)
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
        }
    }


}