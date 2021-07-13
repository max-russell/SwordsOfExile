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
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    class NewsLine
    {
        static List<NewsLine> List = new List<NewsLine>();
        string text;
        bool big;
        int width, height;
        int Duration;
        BitmapFont BigFont = Gfx.TalkFontBold;
        BitmapFont SmallFont = Gfx.ItalicFont;

        public static void DrawAll(SpriteBatch sb)
        {
            //Update durations and remove if finished
            if (List.Count > 0)
            {
                //int i;
                for (int i = List.Count-1; i >= 0; i--)
                    if (List[i].Duration >= 0)
                        if (--List[i].Duration <= 0) 
                            List.RemoveAt(i);

                //Draw news that is still there
                int pos = 5;
                foreach (NewsLine nl in List)//(i = List.Count <= 10 ? 0 : List.Count - 10; i < List.Count; i++)
                {
                    nl.Draw(sb, pos);
                    pos += nl.height + 2;
                }
            }
        }
        public static void Clear()
        {
            List.Clear();
        }

        public NewsLine(string t, bool large, int duration = -1)
        {
            //Stop anything that might spam the same message too much
            if (List.Count > 0 && List[List.Count - 1].text == t) return;

            Duration = duration;
            text = t;
            big = large;
            Vector2 v = big ? BigFont.MeasureString(text) : SmallFont.MeasureString(text);
            width = (int)v.X;
            height = (int)v.Y;
            List.Add(this);
        }

        void Draw(SpriteBatch sb, int pos)
        {
            sb.DrawString(big ? BigFont : SmallFont, text, new Vector2((Gfx.WinW - width) / 2, pos), Color.White);
        }
    }
}