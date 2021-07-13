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
    class OptionPictureButton : OptionButton
    {
        XnaRect srcRect;
        Texture2D srcImg;

        public OptionPictureButton(GuiWindow p, PressControlHandler handler, XnaRect r, Texture2D img, XnaRect dr, int tno, int optgrp)
            : base(p, handler, null, dr.X, dr.Y, dr.Width, dr.Height, tno, optgrp)
        {
            srcRect = r;
            srcImg = img;
        }
        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;
            if (!Enabled)
                if (Pressed)
                {
                    sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, Color.DimGray);
                    Gfx.DrawRect(X + xOffset, Y + yOffset, Width, Height, Color.DimGray, false, 3);
                }
                else
                    sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, Color.DimGray);
            else
                if (Pressed)
                {
                    sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, Color.White);
                    Gfx.DrawRect(X + xOffset, Y + yOffset, Width, Height, Color.White, false, 3);
                }
                else
                    sb.Draw(srcImg, new XnaRect(X + xOffset, Y + yOffset, Width, Height), srcRect, Color.White);
        }
    }
}