using System;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal delegate void InputTextHandler(string text);

internal delegate void InputKeyHandler(Keys k);

internal class InputKeyWindow : GuiWindow
{
    private InputKeyHandler Handler;
    private bool keyRemap = false;
    private Label errorLabel;

    public InputKeyWindow(InputKeyHandler handler, string message, bool keyremap) : base(0,0,300,100,true,false,true,true,true)
    {
        Handler = handler;
        var l = AddLabel(message, 10, 20, 260, -1, true);
        Position(-2,-2);
        Resize(300, 100);
        keyRemap = keyremap;
        errorLabel = AddLabel("", 10, 50, 260, 30, false);
    }

    public override bool Handle()
    {
        var interacted = base.Handle();
        var hitkeys = KeyHandler.GetAllKeysHit();
        if (hitkeys != Keys.None)
        {
            if (
                ((hitkeys >= Keys.D0 && hitkeys <= Keys.Z) ||
                 (hitkeys >= Keys.NumPad0 && hitkeys <= Keys.NumPad9)
                 || hitkeys == Keys.Escape)
                || (keyRemap && keycanmap(hitkeys))
            )
            {

                if (!keyRemap || !(hitkeys >= Keys.D1 && hitkeys <= Keys.D6))
                {
                    KeyHandler.FlushHitKey();
                    KillMe = true;
                    Handler.Invoke(hitkeys);
                    return true;
                }
            }

            errorLabel.Text = "That key cannot be mapped to an action.";

        }

        return interacted;
    }

    private bool keycanmap(Keys k)
    {
        switch (k)
        {
            case Keys.F1: 
            case Keys.F2: 
            case Keys.F3: 
            case Keys.F4: 
            case Keys.F5:
            case Keys.F6: 
            case Keys.F7: 
            case Keys.F8:
            case Keys.F9: 
            case Keys.F10: 
            case Keys.F11:
            case Keys.F12:
            case Keys.Space: 
            case Keys.OemMinus: 
            case Keys.OemPlus: 
            case Keys.OemQuestion: 
            case Keys.OemSemicolon: 
            case Keys.PageDown: 
            case Keys.PageUp: 
            case Keys.Home: 
            case Keys.End: 
            case Keys.Insert: 
            case Keys.Delete: 
            case Keys.NumPad0: 
            case Keys.NumPad1: 
            case Keys.NumPad2:
            case Keys.NumPad3: 
            case Keys.NumPad4: 
            case Keys.NumPad5: 
            case Keys.NumPad6: 
            case Keys.NumPad7: 
            case Keys.NumPad8: 
            case Keys.NumPad9:
            case Keys.OemComma: 
            case Keys.OemPeriod: 
            case Keys.OemOpenBrackets: 
            case Keys.OemCloseBrackets: 
            case Keys.Add: 
            case Keys.Subtract: 
            case Keys.Multiply: 
            case Keys.Divide: 
                return true;
        }
        return false;
    }
}

internal class InputTextWindow : GuiWindow
{
    private TextInputBox textBox;
    private InputTextHandler returnText;

    public InputTextWindow(InputTextHandler handler, string message, string def, bool numbers_only, int width = 300)
        : base(0, 0, width, 200, true, false, true, true, true)
    {
        returnText = handler;
        var ypos = 20;
        var l = AddLabel(message, 10, ypos, width-40, -1, true);
        ypos += l.Height + 20;

        textBox = new TextInputBox(this, 10, ypos, width-40, 30, def, numbers_only, -1, -1);//AddTextInputBox(10, ypos, 260, 30, def, numbers_only);
        controls.Add(textBox);

        ypos += textBox.Height + 20;
        var b1 = AddButton(pressDone, "Done", 0, 0);
        OKKeyControl = b1;
        var b2 = AddButton(pressCancel, "Cancel", 0, 0);
        CancelKeyControl = b2;

        LineUpControlsRight(Width - Gfx.FRAME_WIDTH - 18, ypos, 10, b2, b1);

        ypos += b2.Height;
        Resize(width, ypos + 40);
        Position(-2, -2);
    }

    private void pressDone(Control button)
    {
        KillMe = true;
        returnText.Invoke(textBox.Text);
    }

    private void pressCancel(Control button)
    {
        KillMe = true;
        returnText.Invoke(null);
    }

    private class TextInputBox : Control
    {
        private bool numbersOnly;
        public string Text;
        public int MaxChars = 30;
        private int cursorpos = 0;
        private bool cursorFlash, cursorTick;

        private bool textHighlighting; //Whether user is dragging mouse to highlight a selection of text in the box
        private int highlightPos; //Where the text highlight starts - cursorpos is the end.

        public TextInputBox(GuiWindow win, int x, int y, int w, int h, string defaulttext, bool numbers_only, int tabno, int maxchars = 30)
            : base(win, x, y, w, h, tabno)
        {
            MaxChars = maxchars;
            Text = defaulttext;
            highlightPos = Text.Length;
            cursorpos = 0;
            numbersOnly = numbers_only;
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            Gfx.DrawRect(X + xOffset, Y + yOffset, Width, Height, Color.White, true);

            var lh = Maths.Min(cursorpos, highlightPos);
            var rh = Maths.Max(cursorpos, highlightPos);

            if (lh == rh)
                sb.DrawString(Gfx.TalkFontNormal, Text, new Vector2(X + xOffset + 4, Y + yOffset + 2), Color.Black);
            else
            {
                var x = X + xOffset + 4;
                if (lh > 0) //Draw unhighlighted text before the text highlight area
                {
                    sb.DrawString(Gfx.TalkFontNormal, Text.Substring(0, lh), new Vector2(x, Y + yOffset + 2), Color.Black);
                    x += (int)Gfx.TalkFontNormal.MeasureString(Text.Substring(0, lh)).Width;
                }

                Gfx.DrawRect(x, Y + yOffset + 2, (int)Gfx.TalkFontNormal.MeasureString(Text.Substring(lh, rh - lh)).Width, Height - 4, Color.DarkSlateGray, true);
                sb.DrawString(Gfx.TalkFontNormal, Text.Substring(lh, rh - lh), new Vector2(x, Y + yOffset + 2), Color.White);
                x += (int)Gfx.TalkFontNormal.MeasureString(Text.Substring(lh, rh - lh)).Width;
                if (rh < Text.Length)
                    sb.DrawString(Gfx.TalkFontNormal, Text.Substring(rh, Text.Length - rh), new Vector2(x, Y + yOffset + 2), Color.Black);
            }
            var v = Gfx.TalkFontNormal.MeasureString(Text.Substring(0, cursorpos));
            if (cursorFlash)
                Gfx.DrawRect(X + xOffset + 3 + (int)v.Width, Y + yOffset + 2, 3, Height - 4, Color.Black, true);
        }

        public override bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible) return false;

            var tickon = Game.AnimTicks < 2;
            if ((tickon && !cursorTick) || (!tickon && cursorTick)) cursorFlash = !cursorFlash;
            cursorTick = tickon;

            //Is mouse inside bounds of button?

            int dx = X + xOffset, dy = Y + yOffset;
            if (textHighlighting)
            {
                if (Gui.LMBDown)
                {
                    mouseToCursorPos(dx, dy);
                    return true;
                }
                else
                    textHighlighting = false;
            }
            else
            {
                if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height)
                {
                    //Is button pressed?
                    if (Gui.LMBHit)
                    {
                        mouseToCursorPos(dx, dy);
                        highlightPos = cursorpos;
                        textHighlighting = true;
                        return true;
                    }
                }
            }

            var hitkeys = KeyHandler.GetAllKeysHit();
            if (hitkeys != Keys.None)
            {

                var k = hitkeys;
                if (!((k >= Keys.A && k <= Keys.Z) ||
                      (k >= Keys.D0 && k <= Keys.D9) ||
                      (k >= Keys.NumPad0 && k <= Keys.Divide) ||
                      (k >= Keys.OemSemicolon && k <= Keys.OemTilde) ||
                      (k >= Keys.OemOpenBrackets && k <= Keys.Oem8) ||
                      (k == Keys.Back || k == Keys.Delete || k == Keys.Multiply || k == Keys.Add ||
                       k == Keys.Subtract || k == Keys.Decimal || k == Keys.Divide || k == Keys.Space ||
                       k == Keys.Left || k == Keys.Right))) return false;//continue;
                KeyHandler.FlushHitKey();

                var capson = KeyHandler.AnyKeysDown(Keys.LeftShift, Keys.RightShift);//false;
                var alton = KeyHandler.AnyKeysDown(Keys.LeftAlt, Keys.RightAlt);

                var ch = ' ';

                switch (hitkeys)
                {
                    case Keys.Back:
                        if (!deleteHighlight())
                        {
                            if (cursorpos > 0)
                            {
                                Text = Text.Remove((cursorpos--) - 1, 1);
                                highlightPos = cursorpos;
                            }
                        }
                        cursorFlash = true;
                        return true;
                    case Keys.Delete:
                        if (!deleteHighlight())
                        {
                            if (cursorpos < Text.Length) Text = Text.Remove(cursorpos, 1);
                        }
                        cursorFlash = true;
                        return true;
                    case Keys.Left:
                        cursorpos = Math.Max(0, cursorpos - 1); highlightPos = cursorpos; cursorFlash = true; return true;
                    case Keys.Right:
                        cursorpos = Math.Min(cursorpos + 1, Text.Length); highlightPos = cursorpos; cursorFlash = true; return true;
                    default:
                        ch = KeyHandler.GetCharsFromKeys(hitkeys, capson, alton); break;//(char)hitkeys[0]; break;
                }

                if (numbersOnly && !char.IsDigit(ch)) { cursorFlash = true; return true; };
                if (!capson) ch = char.ToLower(ch);

                {
                    //Delete all highlighted text first.
                    deleteHighlight();

                    if (MaxChars == -1 || Text.Length < MaxChars)
                    {
                        Text = Text.Insert(cursorpos++, ch.ToString());
                        highlightPos = cursorpos;
                        cursorFlash = true;
                        return true;
                    }
                }

            }

            return false;
        }

        private bool deleteHighlight()
        {
            if (cursorpos == highlightPos) return false;
            var lh = Maths.Min(cursorpos, highlightPos);
            var rh = Maths.Max(cursorpos, highlightPos);
            Text = Text.Remove(lh, rh - lh);
            cursorpos = lh;
            highlightPos = lh;
            return true;
        }

        private void mouseToCursorPos(int x, int y)
        {
            x = (Gui.Ms.X - x) - 4;
            y = (Gui.Ms.Y - y) - 2;

            for (var n = 1; n <= Text.Length; n++)
            {
                var l = (int)Gfx.TalkFontNormal.MeasureString(Text.Substring(0, n)).Width;
                if (x < l) { cursorpos = n - 1; return; }
            }
            cursorpos = Text.Length;
        }
    }
}