using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class PictureBox : Control
{
    private XnaRect srcRect;
    private Texture2D srcImg;
    private Color colour;

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