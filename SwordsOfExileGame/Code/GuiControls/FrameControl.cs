using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    class FrameBox : Control
    {
        Color colour;

        public FrameBox(GuiWindow p, XnaRect r, Color fill, int tno)
            : base(p, r.X, r.Y, r.Width, r.Height, tno)
        {
            colour = fill;
        }
        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;
            Gfx.DrawFrame(X + xOffset, Y + yOffset, Width, Height, colour);
        }
    }

}