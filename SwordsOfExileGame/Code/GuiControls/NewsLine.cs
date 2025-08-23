﻿using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class NewsLine
{
    private static List<NewsLine> List = new();
    private string text;
    private bool big;
    private int width, height;
    private int Duration;
    private BitmapFont BigFont = Gfx.TalkFontBold;
    private BitmapFont SmallFont = Gfx.ItalicFont;

    public static void DrawAll(SpriteBatch sb)
    {
        //Update durations and remove if finished
        if (List.Count > 0)
        {
            //int i;
            for (var i = List.Count-1; i >= 0; i--)
                if (List[i].Duration >= 0)
                    if (--List[i].Duration <= 0) 
                        List.RemoveAt(i);

            //Draw news that is still there
            var pos = 5;
            foreach (var nl in List)
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

    private void Draw(SpriteBatch sb, int pos)
    {
        sb.DrawString(big ? BigFont : SmallFont, text, new Vector2((Gfx.WinW - width) / 2, pos), Color.White);
    }
}