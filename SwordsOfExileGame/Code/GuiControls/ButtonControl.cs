using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal delegate void PressControlHandler(Control control_pressed);//string option);

/// <summary>
/// Text button class.
/// </summary>
internal class Button : Control
{
    private int Style = 0;
    protected PressControlHandler pressButtonFunc;
    public bool Pressed;
    private bool mousePressed, keyPressed;
    private string caption;
    public string Caption { get => caption;
        set { caption = value; Resize(Width, Height); } }

    private Vector2 textPos = Vector2.Zero;
    private BitmapFont Font = Gfx.GuiFont1;

    private const int edge_width = 6, edge_height = 6,
        src_corner_tl_x = 81, src_corner_tl_y = 56,
        src_corner_br_x = 151, src_corner_br_y = 126,
        src_hside_x = 87, src_vside_y = 62,
        src_side_width = 64, src_side_height = 64;

    public int Padding { get; set; } = 8;

    public Button(GuiWindow p, PressControlHandler handler, string c, int xb, int yb, int w, int h, int tno)
        : base(p, xb, yb, w, h, tno)
    {
        caption = c;
        Resize(w, h);
        pressButtonFunc = handler;
    }

    public void SetStyle(int n)
    {
        Style = n;
        Resize(Width, Height);
    }

    public void SetFont(BitmapFont f, bool resize)
    {
        Font = f;
        if (resize) Resize(-1, -1);
        else Resize(Width, Height);
    }

    public override void Resize(int w, int h)
    {
        Width = w;
        Height = h;
        if (caption != null)
        {
            Vector2 ssize = Font.MeasureString(caption);

            if (Style == 0)
            {
                if (w == -1) Width = (int)(ssize.X + 2 * edge_width + 2 * Padding);//(innerWidth - (int)ssize.X + 16) / 2;
                if (h == -1) Height = (int)(ssize.Y + 2 * edge_height + 2 * Padding);
                textPos = new Vector2((Width - (int)ssize.X) / 2, (Height - (int)ssize.Y) / 2);
            }
            else
            {
                if (w == -1) Width = (int)(ssize.X + 2 * Padding);//(innerWidth - (int)ssize.X + 16) / 2;
                if (h == -1) Height = (int)(ssize.Y + 2 * Padding);
                textPos = new Vector2(4, (Height - (int)ssize.Y) / 2);
            }
        }
    }

    public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
    {
        if (!Visible) return;

        int dx = X + xOffset, dy = Y + yOffset;
        var tex = Gfx.NewGui;

        var shade = Enabled ? Color.White : Color.DimGray;

        if (Style == 0)
        {

            int tlx = src_corner_tl_x, tly = src_corner_tl_y, brx = src_corner_br_x, bry = src_corner_br_y;

            if (DrawAsPressed) //shift = 8; else shift = 0;
            {
                tlx = src_corner_tl_x - edge_width;
                tly = src_corner_tl_y - edge_height;
                brx = src_corner_br_x + edge_width;
                bry = src_corner_br_y + edge_height;
            }

            //Draw button border
            sb.Draw(tex, new XnaRect(dx, dy, edge_width, edge_height), new XnaRect(tlx, tly, edge_width, edge_height), shade); //TL
            sb.Draw(tex, new XnaRect(dx + Width - edge_width, dy, edge_width, edge_height), new XnaRect(brx, tly, edge_width, edge_height), shade); //TR
            sb.Draw(tex, new XnaRect(dx, dy + Height - edge_height, edge_width, edge_height), new XnaRect(tlx, bry, edge_width, edge_height), shade); //BL
            sb.Draw(tex, new XnaRect(dx + Width - edge_width, dy + Height - edge_height, edge_width, edge_height), new XnaRect(brx, bry, edge_width, edge_height), shade); //BR

            //Top/bottom sides
            var w = Width - edge_width * 2;
            int hsidetimes = w / src_side_width, hsiderem = w % src_side_width; //How many complete times to draw the source, and how many pixels left over
            var x2 = dx + edge_width;
            for (var x = 0; x < hsidetimes; x++) //Draw complete lengths of the horizontal frame sides
            {
                sb.Draw(tex, new Vector2(x2, dy), new XnaRect(src_hside_x, tly, src_side_width, edge_height), shade); //Top side
                sb.Draw(tex, new Vector2(x2, dy + Height - edge_height), new XnaRect(src_hside_x, bry, src_side_width, edge_height), shade); //Bottom side
                x2 += src_side_width;
            }
            if (hsiderem != 0) //Draw partial bit of frame side
            {
                sb.Draw(tex, new Vector2(x2, dy), new XnaRect(src_hside_x, tly, hsiderem, edge_height), shade);
                sb.Draw(tex, new Vector2(x2, dy + Height - edge_height), new XnaRect(src_hside_x, bry, hsiderem, edge_height), shade);
            }

            //left / right sides
            var h = Height - edge_height * 2;
            int vsidetimes = h / src_side_height, vsiderem = h % src_side_height;
            var y2 = dy + edge_height;
            for (var y = 0; y < vsidetimes; y++) //Draw complete lengths of the horizontal frame sides
            {
                sb.Draw(tex, new Vector2(dx, y2), new XnaRect(tlx, src_vside_y, edge_width, src_side_height), shade);
                sb.Draw(tex, new Vector2(dx + Width - edge_width, y2), new XnaRect(brx, src_vside_y, edge_width, src_side_height), shade);
                y2 += src_side_height;
            }
            if (vsiderem != 0) //Draw partial bit of frame side
            {
                sb.Draw(tex, new Vector2(dx, y2), new XnaRect(tlx, src_vside_y, edge_width, vsiderem), shade);
                sb.Draw(tex, new Vector2(dx + Width - edge_width, y2), new XnaRect(brx, src_vside_y, edge_width, vsiderem), shade);
            }

            //Fill In
            y2 = dy + edge_height;
            for (var y = 0; y < vsidetimes; y++) //Draw complete lengths of the horizontal frame sides
            {
                x2 = dx + edge_width;
                for (var x = 0; x < hsidetimes; x++) //Draw complete lengths of the horizontal frame sides
                {
                    sb.Draw(tex, new Vector2(x2, y2), new XnaRect(src_hside_x, src_vside_y, src_side_width, src_side_height), shade);
                    x2 += src_side_width;
                }
                if (hsiderem != 0) //Draw partial bit of frame side
                    sb.Draw(tex, new Vector2(x2, y2), new XnaRect(src_hside_x, src_vside_y, hsiderem, src_side_height), shade);
                y2 += src_side_height;
            }
            if (vsiderem != 0) //Draw partial bit of frame side
            {
                x2 = dx + edge_width;
                for (var x = 0; x < hsidetimes; x++) //Draw complete lengths of the horizontal frame sides
                {
                    sb.Draw(tex, new Vector2(x2, y2), new XnaRect(src_hside_x, src_vside_y, src_side_width, vsiderem), shade);
                    x2 += src_side_width;
                }
                if (hsiderem != 0) //Draw partial bit of frame side
                    sb.Draw(tex, new Vector2(x2, y2), new XnaRect(src_hside_x, src_vside_y, hsiderem, vsiderem), shade);
            }

            if (!DrawAsPressed)
                sb.DrawString(Font, caption, new Vector2(dx + textPos.X, dy + textPos.Y), shade);
            else
                sb.DrawString(Font, caption, new Vector2(dx + textPos.X + 2, dy + textPos.Y + 2), shade);
        }
        else if (Style == 1)
        {
            Gfx.DrawRect(dx, dy, Width, Height, shade, false, 2);
            sb.DrawString(Font, caption, new Vector2(dx + textPos.X, dy + textPos.Y), shade);
        }

    }

    public override bool Handle(int xOffset, int yOffset)
    {
        if (!Enabled || !Visible) return false;
            
        base.Handle(xOffset, yOffset);

        if (!Game.PlayerTargeting)
        {
            if (ShortcutKeyHit()) 
                keyPressed = true;
            else if (!ShortcutKeyDown() && keyPressed)
            {
                keyPressed = false;
                Gui.DragItem = null;
                parent.controlEvent = this;
                Sound.ButtonSound();
                pressButtonFunc.Invoke(this);
                Pressed = keyPressed | mousePressed;
                return true;
            }
        }
        else
            keyPressed = false;

        //Is mouse inside bounds of button?
        int dx = X + xOffset, dy = Y + yOffset;
        if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height)
        {
            //Is button pressed?
            if (Gui.LMBHit)
            {
                mousePressed = true;
                Sound.ButtonSound();
            }
            else if (!Gui.LMBDown && mousePressed)
            {
                //Button has just been released while mouse is still over it, so
                //activate the button by setting the Gui.Event variable.
                mousePressed = false;

                parent.controlEvent = this;
                if (pressButtonFunc != null)
                {
                    pressButtonFunc.Invoke(this);
                }
                Pressed = keyPressed | mousePressed;
                return true;
            }
            Pressed = keyPressed | mousePressed;
            return false;
        }
        else if (mousePressed)
        {
            if (!Gui.LMBDown) { mousePressed = false; }
            Pressed = keyPressed | mousePressed;
            return true;
        }

        Pressed = keyPressed | mousePressed;
        return false;
    }

    protected virtual bool DrawAsPressed => Pressed;
}