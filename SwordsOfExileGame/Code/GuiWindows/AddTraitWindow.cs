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
    delegate void VoidFunc();

    class AddTraitWindow : GuiWindow
    {

        PCType PC;
        VoidFunc FuncOnClose;
        ListBox traitsList;
        Button addTrait, Cancel;
        RichTextBox descBox;

        public AddTraitWindow(PCType pc, VoidFunc d)
            : base(0, 0, 300, 480, true, false, true, true, false)
        {
            PC = pc;
            FuncOnClose = d;

            List<ListBoxItem> list = new List<ListBoxItem>();

            for (int n = 0; n < Trait.Index.Length; n++)
                if (!Trait.Index[n].Race && !pc.Traits.Contains(Trait.Index[n]))
                {
                    var l = new ListBoxItem();
                    l.Text = Trait.Index[n].Name;
                    l.Tag = Trait.Index[n];
                    list.Add(l);
                }

            addTrait = AddButton(pressButton, "Add Selected", 0, 0);
            Cancel = AddButton(pressButton, "Cancel", 0, 0);
            LineUpControlsRight(InnerWidth - 10, InnerHeight - 50, 10, addTrait, Cancel);

            traitsList = AddListBox(changeTrait, 10, 10, InnerWidth - 30, InnerHeight - 155, 0, list.ToArray());

            descBox = AddBlankRichTextBox(null, 10, traitsList.Y + traitsList.Height + 8, InnerWidth - 20, 80);
            descBox.FontNormal = Gfx.GuiFont1;
            descBox.FontBold = Gfx.BoldFont;
            descBox.FontItalic = Gfx.ItalicFont;

            if (traitsList.Items.Count > 0) traitsList.SelectedItem = traitsList.Items[0];
            else
                addTrait.Enabled = false;

            Position(-2, -2);
        }

        void pressButton(Control b)
        {
            if (b == addTrait)
                PC.Traits.Add((Trait)traitsList.SelectedItem.Tag);
            KillMe = true;
        }

        void changeTrait(bool user_caused, ListBoxItem item)
        {
            Trait t = (Trait)item.Tag;
            descBox.FormatText("@b" + t.Name + ":@e " + t.Description + "@n@iExperience Handicap: " + t.Handicap + "%");
        }

        public override void Close()
        {
            FuncOnClose.Invoke();
            base.Close();
        }


    }

}