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
    class PictureBox : Control
    {
        XnaRect srcRect;
        Texture2D srcImg;
        Color colour;

        public PictureBox(GuiWindow p, XnaRect r, Texture2D img, XnaRect dr, int tno)
            : base(p, dr.X, dr.Y, dr.Width, dr.Height, tno)
        {
            colour = Color.White;
            srcRect = r;
            srcImg = img;
        }
        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;
            sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, colour);
        }

        public void SetPicture(Texture2D texture, XnaRect r)
        {
            srcImg = texture;
            srcRect = r;
        }
        public void SetColour(Color col)
        {
            colour = col;
        }
    }

}