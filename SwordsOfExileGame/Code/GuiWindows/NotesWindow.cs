using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace SwordsOfExileGame
{

    class NotesWindow : GuiWindow
    {
        ListBox notesListBox;
        RichTextBox notesMessage;
        Button okButton, deleteButton;

        public NotesWindow() : base(0,0, 600,600,true,false,true,true,true)
        {
            Position(-2, -2);

            notesListBox = AddListBox(changedSelected, 0, 25, 200, InnerHeight - 30, -1);
            notesListBox.Position(5, 25, -1, -1);

            AddLabel("Notes", 5, 5, -1, -1, false);

            notesMessage = AddBlankRichTextBox(null, 0, 0, 340 - Gfx.FRAME_WIDTH*2, InnerHeight - 60 - Gfx.FRAME_HEIGHT*2);
            notesMessage.Position(230 + Gfx.FRAME_WIDTH, 5 + Gfx.FRAME_HEIGHT, -1, -1);
            notesMessage.BackColour = Color.Black;
            notesMessage.Padding = 4;
            notesMessage.FontNormal = Gfx.TinyFont;
            notesMessage.FontBold = Gfx.SmallBoldFont;
            notesMessage.FontItalic = Gfx.ItalicFont;

            okButton = AddButton(pressButton, "Close", 0, 0, -1, -1);
            deleteButton = AddButton(pressButton, "Delete Note", 0, 0, -1, -1);
            deleteButton.Enabled = false;

            LineUpControlsRight(InnerWidth - 7, InnerHeight - 47, 10, deleteButton, okButton);

            listNotes();
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            base.Draw(sb, partial);
            Gfx.DrawFrame(X + Gfx.FRAME_WIDTH + 230, Y + Gfx.FRAME_HEIGHT + 5, 340, InnerHeight-60, new Color(0, 0, 0, 0));
        }

        void listNotes()
        {
            int n = 0;

            int selected = notesListBox.SelectedItem == null ? -1 : (int)notesListBox.SelectedItem.Tag;

            notesListBox.Clear();
            foreach (string t in Scenario.ListNotes())
            {
                notesListBox.AddItem(t, Color.White, n, false);
                if (n == selected) notesListBox.SelectedItem = notesListBox.Items[n];
                n++;
            }

            if (n == 0)
            {
                notesListBox.AddItem("No notes stored", Color.White, -1, true);
                changedSelected(true, null);
            }
        }

        void changedSelected(bool user_caused, ListBoxItem item)
        {
            if (item == null || (int)item.Tag == -1)
            {
                notesMessage.FormatText("");
                deleteButton.Enabled = false;
            }
            else
            {
                int n = (int)item.Tag;
                notesMessage.FormatText(Scenario.GetNoteMessage(n));
                deleteButton.Enabled = true;
            }
        }

        void pressButton(Control c)
        {
            if (c == okButton)
                KillMe = true;

            if (c == deleteButton)
            {
                Scenario.DeleteNote((int)notesListBox.SelectedItem.Tag);
                listNotes();
            }
        }

    }
}