﻿using System;
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

namespace SwordsOfExileGame
{
    class TabButton : Button
    {
        public TabButton(GuiWindow p, PressControlHandler handler, string c, int xb, int yb, int w, int h)
            : base(p, handler, c, xb, yb, w, h, -1) { }

        public override bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible) return false;

            //Is mouse inside bounds of button?
            int dx = X + xOffset, dy = Y + yOffset;
            if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height)
                //Is button pressed?
                if (Gui.LMBDown)
                {
                    Press();
                    parent.controlEvent = this;
                    if (pressButtonFunc != null) pressButtonFunc.Invoke(this);
                    return true;
                }
            return false;
        }

        public void Press()
        {
            Pressed = true;
            foreach (TabButton b in parent.Tabs)
                if (b != this)
                    b.Pressed = false;
        }
    }
}