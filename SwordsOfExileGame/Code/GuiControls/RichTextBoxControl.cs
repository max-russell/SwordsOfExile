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
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    delegate void LinkClickHandler(int index);

    class RichTextBox : Control
    {
        static float stringWidthModifier = 1.1f;

        BitmapFont fontNormal = Gfx.TalkFontNormal, fontItalic = Gfx.TalkFontItalic, fontBold = Gfx.TalkFontBold;
        public BitmapFont FontNormal { get { return fontNormal; } set { fontNormal = value; FormatText(rawText); } }
        public BitmapFont FontItalic { get { return fontItalic; } set { fontItalic = value; FormatText(rawText); } }
        public BitmapFont FontBold { get { return fontBold; } set { fontBold = value; FormatText(rawText); } }

        bool hasHypertext;
        LinkClickHandler linkHandler;
        string rawText = ""; //Raw Text string including all formatting marks
        public string GetRawText() { return rawText; }

        public Color BackColour = Color.Transparent;
        public int padding = 0;
        public int Padding { get { return padding; } set { padding = value; FormatText(rawText); } }

        static Color[] presetColour = { Color.Black, Color.Blue, Color.Red, Color.Magenta, Color.LightGreen, Color.Cyan, Color.Yellow, Color.White, Color.Gray, Color.LightGray };
        static Color linkColour = Color.Green;

        enum eFormat { Normal, Bold, Italic, Link };
        struct TextZone
        {
            public XnaRect Rect;// = XnaRect.Empty;
            public eFormat Style;// = eFormat.Normal;
            public Color Colour;
            public string Text;
            public string ToolTipText;
            public int LinkIndex;
        }
        List<TextZone> zoneList = new List<TextZone>();

        bool mousePressed = false;

        //Constructor specifically for Conversation Box
        public RichTextBox(GuiWindow p, LinkClickHandler handler, int x, int y, int w, int h, int tno)
            : base(p, x, y, w, h, tno)
        {
            hasHypertext = handler != null;
            linkHandler = handler;
        }

        //Constructor generally for Rich Text controls
        public RichTextBox(GuiWindow p, LinkClickHandler handler, string txt, int x, int y, int width, int h, int tno)
            : base(p, x, y, 0, 0, tno)
        {
            hasHypertext = handler != null;
            linkHandler = handler;
            SetFonts(1);

            XnaRect r;
            if (width == -1)
            {
                r = FormatText(txt, true);
                Width = r.Width;
            }
            else
            {
                Width = width;
                r = FormatText(txt, false);
            }

            if (h == -1) Height = r.Height;
            else Height = h;
        }

        //public RichTextBox(GuiWindow p, string txt, string[] tooltips, int x, int y, int tno)
        //    : base(p, x, y, 0, 0, tno)
        //{
        //    hasHypertext = true;
        //    SetFonts(1);
        //    XnaRect r = FormatText(txt, true, tooltips);
        //    Width = r.Width;
        //    Height = r.Height;
        //}


        public void SetFonts(int s)
        {
            if (s == 0)
            {
                fontNormal = Gfx.TalkFontNormal;
                fontItalic = Gfx.TalkFontItalic;
                fontBold = Gfx.TalkFontBold;
            }
            else
            {
                fontNormal = Gfx.TinyFont;
                fontItalic = Gfx.ItalicFont;
                fontBold = Gfx.SmallBoldFont;
            }
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (Visible)
            {
                int dx = X + xOffset, dy = Y + yOffset;

                if (BackColour != Color.Transparent)
                    Gfx.DrawRect(dx, dy, Width, Height, BackColour, true);

                dx += padding; dy += padding;

                foreach (TextZone z in zoneList)
                {
                    BitmapFont font = fontNormal;
                    Color col = z.Colour;

                    switch (z.Style)
                    {
                        case eFormat.Bold: font = fontBold; break;
                        case eFormat.Italic: font = fontItalic; break;
                        case eFormat.Link: col = linkColour; break;
                    }

                    sb.DrawString(font, z.Text, new Vector2(dx + z.Rect.X, dy + z.Rect.Y), col);
                }
                //Gfx.DrawRect(X + xOffset, Y + yOffset, Width, Height, Color.Red, false, 1);
            }
        }

        public override bool Handle(int xOffset, int yOffset)
        {
            bool interacted = base.Handle(xOffset, yOffset);

            if (!Enabled || !Visible) return false;

            //Is mouse inside bounds of word link?

            //if (!hasHypertext) return interacted;

            int dx = Gui.Ms.X - X - xOffset - padding, dy = Gui.Ms.Y - Y - yOffset - padding;
            int index = 0;

            foreach (TextZone z in zoneList)
            {
                if (dx >= z.Rect.Left && dx < z.Rect.Left + z.Rect.Width &&
                    dy >= z.Rect.Top && dy < z.Rect.Top + z.Rect.Height)
                {
                    if (Gui.LMBDown && z.Style == eFormat.Link)
                        mousePressed = true;
                    else if (mousePressed)
                    {
                        mousePressed = false;
                        if (z.Style == eFormat.Link)
                        {
                            if (linkHandler != null)
                            {
                                Sound.ButtonSound();
                                linkHandler.Invoke(z.LinkIndex); 
                            }
                            return true;
                        }
                    }
                    else
                    {
                        if (z.ToolTipText != "")
                            new ToolTipV2(false, new XnaRect(z.Rect.X + X + xOffset, z.Rect.Y + Y + yOffset, z.Rect.Width, z.Rect.Height), z.ToolTipText, 200);
                        //if (ToolTip.WaitForToolTip())
                        //{
                        //    ToolTip.New(z.ToolTipText, 200);
                        //}
                    }
                }
                //else
                //    mousePressed = false;
                if (z.Style == eFormat.Link) index++;
            }
            return interacted;
        }

        /// <summary>
        /// Changes the text in the Hypertext control and sets up the link areas so that the user can click parts of the text to trigger actions.
        /// Formatting codes recognized are:
        /// @n : New line
        /// @b : Bold
        /// @i : Italic
        /// @l : Link
        /// @[tooltip text] : Start tooltip
        /// @e : End bold/italic/link/tooltip
        /// @0..9: Text in one of the 10 preset colours (Ignored if this is a link, which is always link colour)
        /// @@ : Single @
        /// </summary>
        public XnaRect FormatText(string txt, bool width_not_set = false)
        {
            const char DENOTE_CHAR = '±';

            zoneList.Clear();// = new List<TextZone>();
            BitmapFont curfont = fontNormal;
            txt = txt.Replace("\n", "@n");
            rawText = txt;
            if (txt.Length == 0) return XnaRect.Empty;
            var sb = new System.Text.StringBuilder();
            int linestartpos = 0;
            int pos = 0;
            bool string_ended = false;
            int boxwidth = !width_not_set ? Width - padding * 2 : int.MaxValue;
            float linelength = 0;
            List<string> lines = new List<string>();

            do
            {
                string_ended = false;

                do
                {
                    if (pos >= rawText.Length) { string_ended = true; break; }
                    if (char.IsWhiteSpace(rawText[pos]))
                    {
                        sb.Append(rawText[pos]);
                        linelength += curfont.MeasureString(rawText.Substring(pos, 1)).Width * stringWidthModifier;
                        pos++;
                    }
                    else
                        break;
                } while (true);

                int wordstartpos = pos;
                if (!string_ended)
                {

                    var word = new System.Text.StringBuilder();
                    float wordlength = 0f;
                    bool newline = false;

                    if (linelength < boxwidth)
                    {
                        do
                        {
                            if (pos >= rawText.Length) { string_ended = true; break; }

                            //if (rawText[pos] == '[')
                            //{
                            //    word.Append('[');
                            //    do
                            //    {
                            //        pos++;
                            //        if (pos >= rawText.Length) { throw new Exception("Can't format Rich text: No matching ']'"); }
                            //        word.Append(rawText[pos]);
                            //    } while (rawText[pos] != ']');
                            //    pos++;
                            //}
                            
                            if (rawText[pos] == '@')
                            {
                                pos++;
                                if (pos >= rawText.Length) { string_ended = true; break; }

                                if (rawText[pos] == 'n')
                                {
                                    newline = true;
                                    pos++;
                                    break;
                                }

                                if (char.IsDigit(rawText[pos])) //Check for colour code
                                {
                                    word.Append(DENOTE_CHAR/*'@'*/); word.Append(rawText[pos]);
                                }
                                else if (rawText[pos] == 'b')
                                {
                                    curfont = fontBold; word.Append(DENOTE_CHAR /*'@'*/); word.Append(rawText[pos]);
                                }
                                else if (rawText[pos] == 'i')
                                {
                                    curfont = fontItalic; word.Append(DENOTE_CHAR /*'@'*/); word.Append(rawText[pos]);
                                }
                                else if (rawText[pos] == 'e')
                                {
                                    curfont = fontNormal; word.Append(DENOTE_CHAR /*'@'*/); word.Append(rawText[pos]);
                                }
                                else if (rawText[pos] == 'l')
                                {
                                    curfont = fontNormal; word.Append(DENOTE_CHAR /*'@'*/); word.Append(rawText[pos]);
                                }

                                else if (rawText[pos] == '[')
                                {
                                    word.Append(DENOTE_CHAR);
                                    word.Append('[');
                                    do
                                    {
                                        do
                                        {
                                            pos++;
                                            if (pos >= rawText.Length) 
                                            { Game.FlagError("Text Formatting Error", "Can't format Rich text: No matching ']'"); return new XnaRect(0, 0, 10, 10); }
                                            word.Append(rawText[pos]);
                                        } while (rawText[pos] != '@');
                                        if (pos + 1 >= rawText.Length) 
                                        { Game.FlagError("Text Formatting Error", "Can't format Rich text: No matching ']'"); return new XnaRect(0,0,10,10); }
                                    } while (rawText[pos + 1] != ']');
                                    word.Remove(word.Length - 1, 1);
                                    word.Append(DENOTE_CHAR /*'@'*/);
                                    pos++;
                                }

                                else if (rawText[pos] == '@')
                                {
                                     word.Append(rawText[pos]);
                                }
                                pos++;
                                if (pos >= rawText.Length) string_ended = true;
                                //break;
                            }
                            else if (!char.IsWhiteSpace(rawText[pos]))
                            {
                                word.Append(rawText[pos]);
                                wordlength += curfont.MeasureString(rawText.Substring(pos, 1)).Width * stringWidthModifier;
                                pos++;
                            }
                            else
                                break;
                        }
                        while (true);

                        linelength += wordlength;
                    }

                    if (linelength >= boxwidth)//Gfx.GuiFont1.MeasureString(rawText.Substring(linestartpos, pos - linestartpos)).X > Width)
                    {
                        lines.Add(sb.ToString());
                        sb.Clear();
                        linestartpos = wordstartpos;
                        //sb.Append(word);
                        linelength = wordlength;
                        //sb.Append(rawText.Substring(wordstartpos, pos - wordstartpos).TrimStart(' '));
                    }
                    /*else*/
                    if (newline)
                    {
                        sb.Append(word);
                        lines.Add(sb.ToString());
                        sb.Clear();
                        linestartpos = pos;// wordstartpos;
                        linelength = 0;
                    }
                    else
                    {
                        sb.Append(word);//(rawText.Substring(wordstartpos, pos - wordstartpos));
                    }
                }

            }
            while (!string_ended);

            lines.Add(sb.ToString());

            zoneList = new List<TextZone>();
            TextZone curzone = new TextZone();
            int ypos = 0;
            curfont = fontNormal;
            string curtooltip = "";
            eFormat curstyle = curzone.Style = eFormat.Normal;
            Color curcolour = curzone.Colour = Color.White;
            int curlinkindex = 0;
            sb.Clear();
            int maxwidth = 0;
            int linkcount = 0;

            //Now all the text has been wrapped to separate lines, we can make the text zones in the right places

            foreach (string l in lines)
            {
                bool needstyle = false;
                XnaRect txtr = new XnaRect(0, ypos, 0, fontNormal.LineHeight);

                if (l.Length > 0)
                {
                    for (int n = 0; n < l.Length; n++)
                    {
                        if (needstyle && l[n] == 'b')
                        {
                            curzone.Style = curstyle = eFormat.Bold;
                            curfont = fontBold;
                            needstyle = false;
                        }
                        else if (needstyle && l[n] == 'i')
                        {
                            curzone.Style = curstyle = eFormat.Italic;
                            curfont = fontItalic;
                            needstyle = false;
                        }
                        else if (needstyle && l[n] == 'e')
                        {
                            curzone.Style = curstyle = eFormat.Normal;
                            curtooltip = "";
                            curfont = fontNormal;
                            needstyle = false;
                        }
                        else if (needstyle && l[n] == 'l')
                        {
                            curzone.Style = curstyle = eFormat.Link;
                            curfont = fontNormal;
                            curzone.LinkIndex = curlinkindex = linkcount++;
                            needstyle = false;
                        }
                        else if (needstyle && char.IsDigit(l[n]))
                        {
                            curzone.Colour = curcolour = presetColour[Convert.ToInt32(l.Substring(n, 1))];
                            needstyle = false;
                        }
                        else if (needstyle && l[n] == '[')
                        {
                            curtooltip = "";
                            n++;
                            while (l[n] != DENOTE_CHAR)
                                curtooltip += l[n++];
                            needstyle = false;
                        }
                        else if (l[n] == DENOTE_CHAR)
                        {
                            if (sb.Length > 0)
                            {
                                curzone.Text = sb.ToString();
                                curzone.Style = curstyle;
                                curzone.Colour = curcolour;
                                curzone.Rect = txtr;
                                curzone.ToolTipText = curtooltip;
                                zoneList.Add(curzone);
                                if (maxwidth < curzone.Rect.X + curzone.Rect.Width) maxwidth = curzone.Rect.X + curzone.Rect.Width;
                                sb.Clear();
                            }
                            curzone = new TextZone();
                            curzone.Style = curstyle;
                            curzone.Colour = curcolour;
                            curzone.LinkIndex = curlinkindex;
                            txtr.X = txtr.X + txtr.Width;
                            txtr.Width = 0;
                            needstyle = true;
                        }
                        else
                        {
                            sb.Append(l[n]);
                            txtr.Width = (int)(curfont.MeasureString(sb).Width );
                        }
                    }
                    if (sb.Length > 0)
                    {
                        curzone.Text = sb.ToString();
                        curzone.Rect = txtr;
                        curzone.ToolTipText = curtooltip;
                        zoneList.Add(curzone);
                        if (maxwidth < curzone.Rect.X + curzone.Rect.Width) maxwidth = curzone.Rect.X + curzone.Rect.Width;
                        sb.Clear();
                    }
                }
                ypos += fontNormal.LineHeight;

            }
            return new XnaRect(X, Y, maxwidth, ypos);
        }
    }

}