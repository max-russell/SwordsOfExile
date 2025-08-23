using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class Label : Control
{
    protected PressControlHandler pressFunc;
    private string text, wrapped_text;
    public string Text { set { text = value; if (wrapping) wrapText(); } get => text;
    }
    public bool Wrapping { set { Wrapping = value; if (value) wrapText(); } get => Wrapping;
    }

    private bool wrapping = false;
    private BitmapFont font = Gfx.GuiFont1;
    public BitmapFont Font
    {
        get => font;
        set
        {
            font = value;
            if (wrapping)
            {
                wrapText();
                Vector2 sz = font.MeasureString(wrapped_text);
                Height = (int)sz.Y + 2 * padding;
            }
        }
    }
    public Color BackColour;
    public Color TextColour = Color.White;
    public int padding = 0;
    public int Padding { get => padding;
        set { padding = value; if (wrapping) wrapText(); } }

    public Label(GuiWindow p, string c, int x, int y, int w, int h, bool wrapping_on, int tno)
        : base(p, x, y, 0, 0, tno)
    {
        BackColour = Color.Transparent;
        text = wrapped_text = c;
        Vector2 sz = Gfx.GuiFont1.MeasureString(c);
        if (w == -1) Width = (int)sz.X + 2 * padding; else Width = w;

        if (wrapping_on)
        {
            wrapping = true;
            wrapText();
        }

        sz = Gfx.GuiFont1.MeasureString(wrapped_text);
        if (h == -1) Height = (int)sz.Y + 2 * padding;
        else Height = h;
    }
    public void SetHandler(PressControlHandler handler) { pressFunc = handler; }

    public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
    {
        if (Visible)
        {
            if (BackColour != Color.Transparent)
                Gfx.DrawRect(X + xOffset, Y + yOffset, Width, Height, BackColour, true);

            sb.DrawString(Font, wrapping ? wrapped_text : text, new Vector2(X + xOffset + padding, Y + yOffset + padding), TextColour);
        }
    }

    public override void Resize(int w, int h)
    {
        if (w == -1)
            Width = (int)Font.MeasureString(text).Width + 2 * padding;
        else
        {
            Width = w;

            if (wrapping) wrapText();
        }

        if (h == -1)
            Height = (int)Font.MeasureString(wrapping ? wrapped_text : text).Height + 2 * padding;
        else
            Height = h;
    }

    public override bool Handle(int xOffset, int yOffset)
    {
        if (!Enabled || !Visible) return false;
            
        base.Handle(xOffset, yOffset);

        int dx = X + xOffset, dy = Y + yOffset;

        if (pressFunc != null && Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height && Gui.LMBHit)
        {
            Gui.DragItem = null;
            pressFunc.Invoke(this);
            return true;
        }
        return false;
    }

    private void wrapText()
    {
        //Wrap the text so it fits in the area.
        if (text.Length == 0) return;
        var sb = new System.Text.StringBuilder();
        var linestartpos = 0;
        var pos = 0;
        var string_ended = false;

        do
        {
            string_ended = false;
            var wordstartpos = pos;

            do
            {
                if (pos >= text.Length) { string_ended = true; break; }
                if (char.IsWhiteSpace(text[pos])) pos++; else break;
            } while (true);

            if (string_ended)
            {
                wrapped_text = sb.ToString();
                return;
            }

            do
            {
                if (pos >= text.Length)
                { string_ended = true; break; }
                if (!char.IsWhiteSpace(text[pos])) pos++; else break;
            }
            while (true);

            if (Font.MeasureString(text.Substring(linestartpos, pos - linestartpos)).Width > Width - 2 * padding)
            {
                sb.Append("\n");
                linestartpos = wordstartpos;
                sb.Append(text.Substring(wordstartpos, pos - wordstartpos).TrimStart(' '));
            }
            else
            {
                sb.Append(text.Substring(wordstartpos, pos - wordstartpos));
            }

        }
        while (!string_ended);

        wrapped_text = sb.ToString();
    }
}