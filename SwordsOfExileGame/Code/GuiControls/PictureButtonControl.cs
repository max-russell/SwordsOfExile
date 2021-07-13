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
    /// <summary>
    /// Picture Button class. Inherits from Text Button because it behaves the same, but we override the Draw method.
    /// </summary>
    class PictureButton : Button
    {
        XnaRect srcRect;
        Texture2D srcImg;

        public PictureButton(GuiWindow p, PressControlHandler handler, XnaRect r, Texture2D img, XnaRect dr, int tno)
            : base(p, handler, null, dr.X, dr.Y, dr.Width, dr.Height, tno)
        {
            srcRect = r;
            srcImg = img;
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;
            if (Pressed) sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, Color.Red);
            else sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, !Enabled ? Color.DarkSlateGray : Color.White);
        }

        public void SetPicture(Texture2D texture, XnaRect r)
        {
            srcImg = texture;
            srcRect = r;
        }
    }
}