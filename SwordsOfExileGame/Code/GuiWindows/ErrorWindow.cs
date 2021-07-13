namespace SwordsOfExileGame
{
    class ErrorWindow : GuiWindow
    {
        public ErrorWindow(string txt1, string txt2): base(0, 0, 400, 200, true, false, true, true, false)
        {
            Label l = AddLabel(txt1, 10, 10, -1, -1, false);
            l.Font = Gfx.TalkFontNormal;
            AddRichTextBox(txt2, null, 10, 40, InnerWidth - 20);
            Position(-2, -2);
            Button b = AddButton(pressButton, "OK", 0, 0, -1, -1);
            b.Position(-10, -10, 1, 1);
            OKKeyControl = b;
            CancelKeyControl = b;
        }

        void pressButton(Control b)
        {
            KillMe = true;
            Game.Quit = true;
        }
    }
}