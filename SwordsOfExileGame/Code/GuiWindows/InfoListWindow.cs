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

    class InfoListWindow : GuiWindow
    {
        static InfoListWindow instance;
        List<string> messageList = new List<string>();
        int messageLimit = 50;
        int messagePos = 0;
        int messagesHeight = 0;
        int messageExtend = 136;

        const int SCROLL_CHANGE = 12;

        enum eButton { NONE, UP, DOWN, BAR };
        eButton pressedButton = eButton.NONE;

        XnaRect gfxSrcRect = new XnaRect(0, 260, 271, 138);

        public InfoListWindow()
            : base(0, 260, 271 + Gfx.FRAME_WIDTH * 2, 138 + Gfx.FRAME_HEIGHT * 2, true, true, false, true, false)
        {
            instance = this;
            Position(0, -1);
            AllowResizing(24, Height, Gfx.WinH);
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            Vector2 wpos = GetClientAreaPos();
            base.Draw(sb);
            //sb.Draw(Gfx.StatAreaGfx, wpos, gfxSrcRect, Color.White);

            int pos = InnerHeight + messagePos; //gfxSrcRect.Height + messagePos;


            XnaRect currentRect = sb.GraphicsDevice.ScissorRectangle;
            sb.GraphicsDevice.ScissorRectangle = new XnaRect((int)wpos.X, (int)wpos.Y, InnerWidth - 16, Maths.Min(InnerHeight,Gfx.WinH - (int)wpos.Y));

            for (int n = 0; n < messageList.Count; n++)
            {
                string message = messageList[n];
                pos -= (int)Gfx.TinyFont.MeasureString(message).Height;
                if (pos >= InnerHeight) continue;
                sb.DrawString(Gfx.TinyFont, message, new Vector2(4, pos) + wpos, Color.LightGray);
                if (pos < 0) break;
            }

            sb.GraphicsDevice.ScissorRectangle = currentRect;

            if (InnerHeight >= 32)
            {
                Color col;
                if (messagesHeight <= messagePos + messageExtend) col = Color.DarkGray; else if (pressedButton == eButton.UP) col = Color.Red; else col = Color.White;
                sb.Draw(Gfx.NewGui, new XnaRect((int)wpos.X + gfxSrcRect.Width - 16, (int)wpos.Y, 16, 16), new XnaRect(156, 209, 16, 16), col);
                if (messagePos <= 0) col = Color.DarkGray; else if (pressedButton == eButton.DOWN) col = Color.Red; else col = Color.White;
                sb.Draw(Gfx.NewGui, new XnaRect((int)wpos.X + gfxSrcRect.Width - 16, (int)wpos.Y + InnerHeight - 16, 16, 16), new XnaRect(156, 225, 16, 16), col);
                Gfx.DrawRect((int)wpos.X + gfxSrcRect.Width - 16, (int)wpos.Y + 16, 16, InnerHeight - 32, Color.Black);

                float barh = InnerHeight - 32;
                float g1 = messagesHeight < messageExtend ? 0 : ((float)messagePos / (float)messagesHeight) * barh;
                float g2 = messagesHeight < messageExtend ? barh : ((float)messageExtend / (float)messagesHeight) * barh;
                if (g2 > barh) g2 = barh;
                g1 = barh - g2 - g1;


                //g1 = barh - g2;

                Gfx.DrawRect((int)wpos.X + gfxSrcRect.Width - 16, (int)wpos.Y + 16 + (int)g1, 16, (int)g2/*(int)(g2 > barh ? barh : g2)*/, Color.DarkGray);
            }
        }

        public override bool Handle()
        {
            if (!Visible) return false;
            bool interacted = base.Handle();

            Vector2 wpos = GetClientAreaPos();
            int dx = (int)wpos.X + InnerWidth - 16;
            int dy = (int)wpos.Y;

            if (Gui.Ms.X >= dx && Gui.Ms.X < dx + 16 && Gui.Ms.Y >= dy && Gui.Ms.Y < dy + InnerHeight)
            {
                if (Gui.Ms.Y < dy + 16) //'up' button
                {
                    if (Gui.LMBHit)
                    {
                        pressedButton = eButton.UP;
                        interacted = true;
                    }
                    else if (!Gui.LMBDown && pressedButton == eButton.UP)
                    {
                        //if (--pos < min) pos = min;
                        if (messagePos + messageExtend < messagesHeight)
                            messagePos = Maths.Min(messagePos + SCROLL_CHANGE, messagesHeight - messageExtend);//+= 8;
                        interacted = true;
                        pressedButton = eButton.NONE;
                    }
                }
                else if (Gui.Ms.Y >= dy + InnerHeight - 16) //'down' button
                {
                    if (Gui.LMBHit)
                    {
                        pressedButton = eButton.DOWN;
                        interacted = true;
                    }
                    else if (!Gui.LMBDown && pressedButton == eButton.DOWN)
                    {
                        if (messagePos > 0) messagePos = Maths.Max(0, messagePos - SCROLL_CHANGE);
                        interacted = true;
                        pressedButton = eButton.NONE;
                    }
                }
                else //The bar
                {
                    if (Gui.LMBDown)
                    {
                        if (messagesHeight > messageExtend)
                        {

                            pressedButton = eButton.BAR;

                            //Get mouse position in the bar from 0 (top) to 1 (bottom)
                            float mpos = 1 - ((float)(Gui.Ms.Y - dy - 16) / (float)(InnerHeight - 32));
                            //Game.TestMessage = mpos.ToString();


                            messagePos = (int)((float)(messagesHeight - messageExtend) * mpos);
                            if (messagePos < 0) messagePos = 0;
                            if (messagePos > messagesHeight - messageExtend) messagePos = messagesHeight - messageExtend;

                            //if (extend > max - min)
                            //{
                            //    extend = max - min;
                            //    Visible = false;
                            //}
                            //else Visible = true;
                            //if (pos < min) pos = min;
                            //if (pos + extend > max) pos = max - extend;

                            interacted = true;
                        }
                    }
                }
            }
            else
            {
                if (Gui.LMBDown && pressedButton == eButton.BAR)
                {
                    float mpos = 1 - ((float)(Gui.Ms.Y - dy - 16) / (float)(InnerHeight - 32));
                    //ChangeValues((int)((float)(max - min) * mpos) + min - extend / 2, extend, min, max);

                    messagePos = (int)((float)(messagesHeight - messageExtend) * mpos);
                    if (messagePos < 0) messagePos = 0;
                    if (messagePos > messagesHeight - messageExtend) messagePos = messagesHeight - messageExtend;


                    //float mpos = (float)(Gui.Ms.Y - dy - 16) / (float)(Height - 32);
                    //if (mpos < 0) mpos = 0; if (mpos > 1) mpos = 1;
                    //ChangeValues((int)((float)(max - min) * mpos) + min - extend / 2, extend, min, max);
                    interacted = true;

                }
                else
                    pressedButton = eButton.NONE;
            }

            return interacted;

        }

        public override void Resize(int w, int h)
        {
            base.Resize(w, h);
            messageExtend = InnerHeight - 2;
        }

        public void AddMessage(String message)
        {
            var all_lines = message.Split(new char[]{'\n'}, StringSplitOptions.None).ToList<string>();
            //all_lines.Reverse();
            int insertpos = 0;

            foreach (string text in all_lines)
            {
                List<string> msgs = new List<string>();

                var sb = new System.Text.StringBuilder();
                int linestartpos = 0;
                int pos = 0;
                bool string_ended = false;

                do
                {
                    string_ended = false;
                    int wordstartpos = pos;

                    do
                    {
                        if (pos >= text.Length) { string_ended = true; break; }
                        if (char.IsWhiteSpace(text[pos])) pos++;
                        else
                            break;
                    } while (true);

                    if (string_ended)
                    {
                        msgs.Add(sb.ToString());
                        break;
                    }

                    do
                    {
                        if (pos >= text.Length)
                        { string_ended = true; break; }
                        if (!char.IsWhiteSpace(text[pos])) pos++; else break;
                    }
                    while (true);

                    if (Gfx.TinyFont.MeasureString(text.Substring(linestartpos, pos - linestartpos)).Width > InnerWidth - 16)
                    {
                        msgs.Add(sb.ToString());
                        linestartpos = wordstartpos;
                        sb.Clear();
                        sb.Append(text.Substring(wordstartpos, pos - wordstartpos).TrimStart(' '));
                    }
                    else
                    {
                        sb.Append(text.Substring(wordstartpos, pos - wordstartpos));
                    }

                    if (string_ended) msgs.Add(sb.ToString());
                }
                while (!string_ended);

                foreach (string m in msgs)
                {
                    messageList.Insert(insertpos, m);
                    messagesHeight += (int)Gfx.TinyFont.MeasureString(m).Height;
                }
                messagePos = 0;
            }

            while (messageList.Count > messageLimit)
            {
                messagesHeight -= (int)Gfx.TinyFont.MeasureString(messageList[messageList.Count - 1]).Height;
                messageList.RemoveAt(messageLimit);
            }

        }

    }

}