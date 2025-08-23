using Microsoft.Xna.Framework;

namespace SwordsOfExileGame;

internal class SpecialItemsWindow : GuiWindow
{
    private static SpecialItemsWindow instance;
    private ListBox itemList;
    private RichTextBox descBox;
    private Button useButton;

    public static void Reveal()
    {
        if (instance == null)
            instance = new SpecialItemsWindow();
        else
        {
            instance.Visible = true;
            Refresh();
        }
    }

    public SpecialItemsWindow()
        : base(180, 30, 295, 466, true, true, false, true, true)
    {
        instance = this;

        var l = AddLabel("Special Items", 5, 2, -1, -1, false);
        l.Font = Gfx.TalkFontBold;

        itemList = new ListBox(listChangeHandler, this, 5, 30, 250, 275, -1);
        controls.Add(itemList);

        foreach (var si in SpecialItem.EachHas())
        {
            itemList.AddItem(si.Name, Color.White, si, false);
        }
        if (SpecialItem.NumberHas() == 0)
            itemList.AddItem("No special items owned", Color.White, null, true);

        descBox = new RichTextBox(this, null, "Select a item from the list above", 10, 315, 205, -1, -1);
        controls.Add(descBox);

        useButton = new Button(this, pressUse, "Use", 210, 320, -1, -1, -1);
        controls.Add(useButton);
        useButton.Visible = false;
        Position(-2, -2);
        Gui.BringToFront(this);
    }

    public override void Close()
    {
        base.Close();
        instance = null;
    }

    public static void Refresh()
    {
        if (instance != null && instance.Visible)
            instance.refresh();
    }

    private void refresh()
    {
        var s = (SpecialItem)itemList.SelectedItem?.Tag;
        itemList.Items.Clear();

        foreach (var si in SpecialItem.EachHas())
        {
            itemList.AddItem(si.Name, Color.White, si, false);
            if (s == si) itemList.SelectedItem = itemList.Items[itemList.Items.Count - 1];

        }
        if (SpecialItem.NumberHas() == 0)
            itemList.AddItem("No special items owned", Color.White, null, true);

        listChangeHandler(true, itemList.SelectedItem);
    }

    private void pressUse(Control b)
    {
        var s = (SpecialItem)itemList.SelectedItem.Tag;
        Script.New_UseSpecialItem(s.UseFunc, s);
        KillMe = true;
    }

    private void listChangeHandler(bool user_caused, ListBoxItem item)
    {
        if (!user_caused) return;

        if (item == null || item.Tag == null)
            if (itemList.Items.Count == 0)
                descBox.FormatText("", false);
            else
                descBox.FormatText("Select a item from the list above", false);
        else
        {
            var s = (SpecialItem)item.Tag;
            descBox.FormatText(s.Description);
            useButton.Visible = s.Useable;
        }
    }
}