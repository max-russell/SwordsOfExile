using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

namespace SwordsOfExileGame
{
    class LoadingWindow : GuiWindow
    {
        static LoadingWindow Instance;

        public LoadingWindow()
            : base(0, 0, 200, 100, true, false, true, true, false)
        {
            Instance = this;
            var l = AddLabel("Loading...", 0, 0, -1, -1, false);
            l.Position(0, -10, 0, 0);
            Position(-2, -2);
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            base.Draw(sb, partial);

            int dx = X + (Width / 2 - 20);

            if (Game.AnimTicks >= 0)
                Gfx.DrawRect(dx, Y + 60, 5, 5, Color.White, true);
            if (Game.AnimTicks >= 1)
                Gfx.DrawRect(dx + 10, Y + 60, 5, 5, Color.White, true);
            if (Game.AnimTicks >= 2)
                Gfx.DrawRect(dx + 20, Y + 60, 5, 5, Color.White, true);
            if (Game.AnimTicks >= 3)
                Gfx.DrawRect(dx + 30, Y + 60, 5, 5, Color.White, true);

        }

        public static void Terminate()
        {
            Instance.KillMe = true;
        }

    }

}