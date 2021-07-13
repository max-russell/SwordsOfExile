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