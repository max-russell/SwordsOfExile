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
    /// <summary>
    /// Base class for all Window controls. Stores things common to all controls like its position.
    /// </summary>
    abstract class Control
    {
        //static int idcount = 0;
        //public int ID = 0;
        public int TabNo = -1; //Which tab the control is on (-1 for always show regardless of tab)
        public bool Enabled = true;
        public bool Visible = true;
        public int X, Y, Width, Height;
        protected GuiWindow parent;
        public Keys KeyShortcut = Keys.None;
        string tooltipMessage = null; //If not null, the control automatically displays this tool tip when the mouse is over it.
        int tooltipWidth = -1;

        public Control(GuiWindow p, int xb, int yb, int w, int h, int tno)
        {
            parent = p;
            X = xb;
            Y = yb;
            Width = w;
            Height = h;
            TabNo = tno;
            //ID = idno;// idcount;
            //idcount++;
        }

        public virtual void Draw(SpriteBatch sb, int xOffset, int yOffset) { }
        public virtual bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible) return false;
            if (tooltipMessage != null)
            {
                int dx = X + xOffset, dy = Y + yOffset;
                if (Gui.Ms.X >= dx && Gui.Ms.X < dx + Width && Gui.Ms.Y >= dy && Gui.Ms.Y < dy + Height)
                    new ToolTipV2(false, new XnaRect(dx,dy, Width, Height), tooltipMessage, tooltipWidth);
            }
            return false;
        }
        public virtual void Resize(int w, int h) { Width = w; Height = h; }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="x">Amount to offset from alignment</param>
        /// <param name="y">ditto for y</param>
        /// <param name="xalign">-1: from left, 0: from centre, 1: from right</param>
        /// <param name="yalign">-1: from top, 0: from centre, 1: from bottom</param>
        public virtual void Position(int x, int y, int xalign, int yalign)
        {
            switch (xalign)
            {
                case -1:
                    X = 0 + x; break;
                case 0:
                    X = (parent.InnerWidth - Width) / 2 + x; break;
                case 1:
                    X = (parent.InnerWidth - Width) + x; break;
            }

            switch (yalign)
            {
                case -1:
                    Y = 0 + y; break;
                case 0:
                    Y = (parent.InnerHeight - Height) / 2 + y; break;
                case 1:
                    Y = (parent.InnerHeight - Height) + y; break;
            }
        }

        public bool ShortcutKeyHit()
        {
            return (parent.OKKeyControl == this && KeyHandler.KeyHit(Keys.Enter))
                 || (parent.CancelKeyControl == this && KeyHandler.KeyHit(Keys.Escape))
                 || KeyHandler.KeyHit(KeyShortcut);
        }

        public bool ShortcutKeyDown()
        {
            return (parent.OKKeyControl == this && KeyHandler.KeyDown(Keys.Enter))
                 || (parent.CancelKeyControl == this && KeyHandler.KeyDown(Keys.Escape))
                 || KeyHandler.KeyDown(KeyShortcut);
        }

        public void SetStandardToolTip(string s, int width=-1)
        {
            tooltipMessage = s;
            tooltipWidth = width;
        }
    }

}