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
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{

    class AlchemyWindow : GuiWindow
    {
        static AlchemyWindow Instance;

        ListBox recipeListBox;
        Button OKButton, makeButton;

        Label selRecipeTitle;
        RichTextBox selRecipeDesc;

        PictureBox pcPic;
        RichTextBox pcInfo;

        PCType Alchemist;

        Recipe selectedRecipe;

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

        //public override void Draw(SpriteBatch sb, int partial = 0)
        //{
        //    base.Draw(sb, partial);
        //}

        void changedSelected(bool user_caused, ListBoxItem item)
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

            string ingredients = "";
            foreach (var t in selectedRecipe.Ingredients)
            {
                int has = 0;
                foreach (Item i in Alchemist.EachItemHeld())
                    if (i.AlchemyID == t.Item1) has += i.Charges;
                ingredients += String.Format("  @i{0} ({1}{2}{3}/{4})@e@n", 
                    Recipe.GetIngredientName(t.Item1), 
                    has >= t.Item2 ? "@b" : "", 
                    has, 
                    has >= t.Item2 ? "@i" : "", 
                    t.Item2);
            }

            string cannotcast = "";
            int cancast = Alchemist.CanConcoct(selectedRecipe);
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

            selRecipeDesc.FormatText(String.Format("@bSKILL REQUIRED: {0}@e@n@bINGREDIENTS: @e@n{1}{2}@n@n@i{3}",
                selectedRecipe.Skill,
                ingredients,
                selectedRecipe.Description,
                cannotcast
                ));
        }


        void pressButton(Control b)
        {
            if (b == OKButton)
                KillMe = true;
            else if (b == makeButton)
            {
                //First subtract the alchemical ingredients required
                foreach (var ing in selectedRecipe.Ingredients)
                {
                    int count = ing.Item2;

                    foreach (Item i in Alchemist.EachItemHeld())
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
            int m = caster.GetSkill(eSkill.ALCHEMY);
            if (m == 0)
                q = "@iNo alchemical ability.@e";
            else
                q = "@iLevel " + m + " Alchemist@e";
       
            pcInfo.FormatText("@b" + Alchemist.Name + "@e@n" + q);

            updateSpellList();
        }

        void updateSpellList()
        {
            Recipe old = recipeListBox.SelectedItem != null ? (Recipe)recipeListBox.SelectedItem.Tag : null;
            recipeListBox.Clear();

            foreach (Recipe ms in Party.KnownRecipes.Values)
            {
                if (ms == null) continue;

                if (Alchemist.CanConcoct(ms) > 0)
                    recipeListBox.AddItem(String.Format("{0} ({1})", ms.Name, ms.Skill), Color.Gold, ms, false);
                else
                    recipeListBox.AddItem(String.Format("{0} ({1})", ms.Name, ms.Skill), Color.DarkGray, ms, true);

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

}