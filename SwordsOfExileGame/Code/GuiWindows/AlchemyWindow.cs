using System;
using Microsoft.Xna.Framework;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class AlchemyWindow : GuiWindow
{
    private static AlchemyWindow Instance;

    private ListBox recipeListBox;
    private Button OKButton, makeButton;

    private Label selRecipeTitle;
    private RichTextBox selRecipeDesc;

    private PictureBox pcPic;
    private RichTextBox pcInfo;

    private PCType Alchemist;

    private Recipe selectedRecipe;

    public AlchemyWindow()
        : base(0, 0, 500, 400, true, true, false, true, true)
    {
        Action.LockActions = eAction.MAGIC_LOCK_ACTIONS;
        Instance = this;

        Position(-2, -2);
        recipeListBox = AddListBox(changedSelected, 0, 130, 200, InnerHeight - 20, -1);
        recipeListBox.Position(10, 10, -1, -1);

        controls.Add(new FrameBox(this, new XnaRect(238, 60, 230, 270), new Color(0, 0, 0, 0), -1));

        OKButton = AddButton(pressButton, "Finish", 358, InnerHeight - 30, 110, 30);
        makeButton = AddButton(pressButton, "Make", 238, InnerHeight - 30, 110, 30);
        CancelKeyControl = OKButton;
        OKKeyControl = makeButton;

        selRecipeTitle = AddLabel("Yo!", 250, 68, 206, 35, true);
        selRecipeTitle.BackColour = Color.Black;
        selRecipeTitle.Font = Gfx.TalkFontNormal;
        selRecipeTitle.Padding = 4;

        selRecipeDesc = AddBlankRichTextBox(null, 250, 95, 206, 230);
        selRecipeDesc.BackColour = Color.Black;
        selRecipeDesc.Padding = 4;
        selRecipeDesc.FontNormal = Gfx.TinyFont;
        selRecipeDesc.FontBold = Gfx.SmallBoldFont;
        selRecipeDesc.FontItalic = Gfx.ItalicFont;

        pcPic = AddPictureBox(Gfx.Dot, XnaRect.Empty, new XnaRect(258, 5, 48, 48));
        pcInfo = AddRichTextBox("", null, 310, 5, 160);

        UpdateCaster(Party.CurrentPC);
    }

    private void changedSelected(bool user_caused, ListBoxItem item)
    {
        if (item == null || item.Tag == null)
        {
            selRecipeTitle.Text = "Select Recipe";
            selRecipeTitle.SetStandardToolTip(null);
            selRecipeTitle.Height = 35;
            selRecipeDesc.FormatText("Choose the party member to do the alchemy, and the recipe to follow from the list to the left.");
            makeButton.Enabled = false;
            return;
        }

        selectedRecipe = item.Tag as Recipe;
        selRecipeTitle.Text = selectedRecipe.Name;
        selRecipeTitle.Height = 50;

        var ingredients = "";
        foreach (var t in selectedRecipe.Ingredients)
        {
            var has = 0;
            foreach (var i in Alchemist.EachItemHeld())
                if (i.AlchemyID == t.Item1) has += i.Charges;
            ingredients += string.Format("  @i{0} ({1}{2}{3}/{4})@e@n", 
                Recipe.GetIngredientName(t.Item1), 
                has >= t.Item2 ? "@b" : "", 
                has, 
                has >= t.Item2 ? "@i" : "", 
                t.Item2);
        }

        var cannotcast = "";
        var cancast = Alchemist.CanConcoct(selectedRecipe);
        switch (cancast)
        {
            case -1: cannotcast = "Can't make: Insufficient Ingredients"; break;
            case -2: cannotcast = "Can't make: Alchemy skill too low."; break;
            case -3: cannotcast = "Can't make: Dumbfounded!"; break;
            case -4: cannotcast = "Can't cast: Paralyzed!"; break;
            case -5: cannotcast = "Can't cast: Asleep!"; break;
        }

        if (cancast < 0)
            makeButton.Enabled = false;
        else
            makeButton.Enabled = true;

        selRecipeDesc.FormatText(string.Format("@bSKILL REQUIRED: {0}@e@n@bINGREDIENTS: @e@n{1}{2}@n@n@i{3}",
            selectedRecipe.Skill,
            ingredients,
            selectedRecipe.Description,
            cannotcast
        ));
    }


    private void pressButton(Control b)
    {
        if (b == OKButton)
            KillMe = true;
        else if (b == makeButton)
        {
            //First subtract the alchemical ingredients required
            foreach (var ing in selectedRecipe.Ingredients)
            {
                var count = ing.Item2;

                foreach (var i in Alchemist.EachItemHeld())
                {
                    if (i.AlchemyID == ing.Item1)
                    {
                        Alchemist.UseItemCharge(i);
                        count--;
                        if (count == 0) break;
                    }
                }
            }
            Script.RunAlchemy(Alchemist, selectedRecipe);
            UpdateCaster(Alchemist);
        }
    }

    public static void Update(PCType pc)
    {
        if (Instance != null)
            Instance.UpdateCaster(pc);
    }

    public void UpdateCaster(PCType caster)
    {
        Alchemist = caster;
        pcPic.SetPicture(caster.PortraitTexture, new XnaRect(0, 0, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT));

        string q;
        var m = caster.GetSkill(eSkill.ALCHEMY);
        if (m == 0)
            q = "@iNo alchemical ability.@e";
        else
            q = "@iLevel " + m + " Alchemist@e";
       
        pcInfo.FormatText("@b" + Alchemist.Name + "@e@n" + q);

        updateSpellList();
    }

    private void updateSpellList()
    {
        var old = (Recipe)recipeListBox.SelectedItem?.Tag;
        recipeListBox.Clear();

        foreach (var ms in Party.KnownRecipes.Values)
        {
            if (ms == null) continue;

            if (Alchemist.CanConcoct(ms) > 0)
                recipeListBox.AddItem(string.Format("{0} ({1})", ms.Name, ms.Skill), Color.Gold, ms, false);
            else
                recipeListBox.AddItem(string.Format("{0} ({1})", ms.Name, ms.Skill), Color.DarkGray, ms, true);

            if (ms == old)
                recipeListBox.SelectedItem = recipeListBox.Items[recipeListBox.Items.Count - 1];
        }

        if (recipeListBox.SelectedItem == null) changedSelected(false, null);

        if (recipeListBox.Items.Count == 0)
            recipeListBox.AddItem("No recipes known", Color.DarkGray, null, true);
    }

    public override void Close()
    {
        base.Close();
        Action.LockActions = eAction.NONE;
        Instance = null;
    }

}