using System.Collections.Generic;

namespace SwordsOfExileGame;

internal delegate void VoidFunc();

internal class AddTraitWindow : GuiWindow
{
    private PCType PC;
    private VoidFunc FuncOnClose;
    private ListBox traitsList;
    private Button addTrait, Cancel;
    private RichTextBox descBox;

    public AddTraitWindow(PCType pc, VoidFunc d)
        : base(0, 0, 300, 480, true, false, true, true, false)
    {
        PC = pc;
        FuncOnClose = d;

        var list = new List<ListBoxItem>();

        for (var n = 0; n < Trait.Index.Length; n++)
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

    private void pressButton(Control b)
    {
        if (b == addTrait)
            PC.Traits.Add((Trait)traitsList.SelectedItem.Tag);
        KillMe = true;
    }

    private void changeTrait(bool user_caused, ListBoxItem item)
    {
        var t = (Trait)item.Tag;
        descBox.FormatText("@b" + t.Name + ":@e " + t.Description + "@n@iExperience Handicap: " + t.Handicap + "%");
    }

    public override void Close()
    {
        FuncOnClose.Invoke();
        base.Close();
    }


}