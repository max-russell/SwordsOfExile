using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{

    class GameOverWindow : GuiWindow
    {
        public GameOverWindow()
            : base(000, 000, 310, 400, true, false, true, true, false)
        {
            Game.CurrentMap = null;
            Gfx.FadeMode = 0;

            var p = AddPictureBox(Gfx.DialogGfx[0], new XnaRect(0, 288, 72, 72), new XnaRect(150, 10, 72, 72));
            p.Position(0, 20, 0, -1);

            var l = AddRichTextBox(
                Scenario.DeathMessage
                , null, 10, p.Y + p.Height + 20, 270);
            var b = AddButton(pressButton, "Main Menu", 0, l.Y + l.Height + 20, -1, -1);
            Resize(310, b.Y + b.Height + 30);
            b.Position(0, -10, 0, 1);
            
            Position(-2, -2);
        }

        void pressButton(Control c)
        {
            Game.Instance.BackToMainMenu();
        }
    }
}