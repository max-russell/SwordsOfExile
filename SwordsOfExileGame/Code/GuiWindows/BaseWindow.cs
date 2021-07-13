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
    /*****************************************************************************************************
     * WINDOW CLASS
     *****************************************************************************************************/
    class GuiWindow
    {
        protected PartyType Party { get { return Game.CurrentParty; } }
        protected TownMap Town { get { return Game.CurrentMap as TownMap; } }

        public bool Border = true; //False if instance handles drawing its own window borders
        bool visible = false;
        public virtual bool Visible
        {
            get { return visible; }
            set
            {
                visible = value; if (Modal /*|| 
                WorldFreeze*/) Gui.WorldModalPaused = value;
            }
        }

        public bool EscapeKeyCloses = false; //Don't set if CancelKeyControl is set to something.
        public bool Modal = false; //True if the window freezes all windows beneath it until it closes 
        //public bool WorldFreeze = false;//True if the window pauses all game actions
        public bool KillMe = false; //Set to true to end the window at the next opportunity
        public bool OnTop = false; //Set to true for tooltips and popupmenus to always appear above other windows
        bool moveable = true;      //The window can be repositioned by the user
        bool closeable = true;     //The window has a little cross button in the corner which the user can use to close it

        bool resizeable = false;   //The window can be resized by the user (but only its Height)
        int minHeight = 0, defHeight = 0, maxHeight = int.MaxValue;  //Smallest and largest values window can be resized to.

        Color backCol = new Color(255, 255, 255, 200);
        public int X, Y, Width, Height;
        public int ClientX = 0, ClientY = 0;
        //protected string Title;
        public int InnerWidth
        {
            get { return Width - ClientX * 2; }
            set { Move(0, 0, value + ClientX * 2, Height); }
        }
        public int InnerHeight
        {
            get { return Height - ClientY * 2; }
            set { Move(0, 0, Width, value + ClientY * 2); }
        }
        readonly int frameWidth, frameHeight;

        public TabButton[] Tabs;
        public int currentTab; //The currently selected tab
        public Control controlEvent; //Set to the control that the user has just interacted with

        public Control OKKeyControl, CancelKeyControl;

        PictureButton closeButton, expandButton; //The button that closes the form
        //protected bool CloseButtonHides = false; //Whether the close button kills the window or just hides it.

        public List<Control> controls = new List<Control>(); //All the controls on the window

        public GuiWindow(int x, int y, int w, int h, bool vis, bool move, bool mod, bool drawborders, bool close)
        {
            Border = drawborders;
            frameWidth = Gfx.FRAME_WIDTH;
            frameHeight = Gfx.FRAME_HEIGHT;

            if (Border) { ClientX = frameWidth; ClientY = frameHeight; }
            closeable = close;
            Visible = vis;
            moveable = move;
            Modal = mod;
            //Title = t;
            if (w < 17) Width = 17; else Width = w;
            if (h < 17) Height = 17; else Height = h;
            if (x == -1) X = (Gfx.WinW - Width) / 2; else X = x;
            if (y == -1) Y = (Gfx.WinH - Height) / 2; else Y = y;

            if (closeable && Border)
            {
                closeButton = AddPictureButton(pressWindowClose, new XnaRect(191, 209, 16, 16), Gfx.NewGui, new XnaRect(InnerWidth, -4 - ClientY, 16, 16));
                //closeButton = (PictureButton) controls[controls.Count - 1];
            }

            if (!(this is ToolTipV2))
            {
                Gui.GuiWindows.Add(this);
                Gui.ActiveToolTip = null;
            }

            //if (Modal) Gui.KeyFocusWindow = this; //Newly created windows automatically gain the key focus
        }

        public int Opacity { set { backCol = new Color(255, 255, 255, value); } get { return backCol.A; } }

        public void SetTabs(params string[] tabnames)
        {
            Tabs = new TabButton[tabnames.Count()];

            //tabNames = tabnames;
            //Title = null; //Windows with tabs have no title
            int xpos = 6;

            for (int i = 0; i < tabnames.Length; i++)
            {
                Vector2 ssize = Gfx.GuiFont1.MeasureString(tabnames[i]);
                Tabs[i] = new TabButton(this, pressWindowTab, tabnames[i], xpos, 4, (int)ssize.X + 16, (int)ssize.Y + 16);
                if (i == 0) currentTab = i;
                controls.Add(Tabs[i]);
                xpos += (int)ssize.X + 16;
            }
            Tabs[currentTab].Press();
        }

        protected void AllowResizing(int min, int def, int max)
        {
            resizeable = true;
            minHeight = min;
            defHeight = def;
            maxHeight = max;
            expandButton = AddPictureButton(pressExpand, new XnaRect(208, 209, 16, 16), Gfx.NewGui, new XnaRect(InnerWidth - 16, -4 - ClientY, 16, 16));
        }

        protected Label AddLabel(string c, int x, int y, int w, int h, bool wrapping_on, int tabno = -1)
        {
            Label l = new Label(this, c, x, y, w, h, wrapping_on, tabno);
            controls.Add(l);
            return l;
        }

        protected RichTextBox AddBlankRichTextBox(LinkClickHandler handler, int x, int y, int w, int h, int tabno = -1)
        {
            RichTextBox l = new RichTextBox(this, handler, x, y, w, h, tabno);
            controls.Add(l);
            return l;
        }

        protected RichTextBox AddRichTextBox(string msg, LinkClickHandler handler, int x, int y, int width, int tabno = -1)
        {
            RichTextBox l = new RichTextBox(this, handler, msg, x, y, width, -1, tabno);
            controls.Add(l);
            return l;
        }

        //protected TextInputBox AddTextInputBox(int x, int y, int w, int h, string default_text, bool numbers_only = false, int tabno = -1)
        //{
        //    TextInputBox tx = new TextInputBox(this, x, y, w, h, default_text, numbers_only, tabno);
        //    controls.Add(tx);
        //    return tx;
        //}

        protected Button AddButton(PressControlHandler press_handler, string c, int x, int y, int w = -1, int h = -1, int tabno = -1)
        {
            Vector2 ssize = Gfx.GuiFont1.MeasureString(c);
            if (x == -1) x = (InnerWidth - (int)ssize.X + 16) / 2;
            Button b = new Button(this, press_handler, c, x, y, w, h, tabno);
            controls.Add(b);
            return b;
        }

        protected PictureButton AddPictureButton(PressControlHandler press_handler, XnaRect sr, Texture2D img, XnaRect dr, int tabno = -1)
        {
            PictureButton b = new PictureButton(this, press_handler, sr, img, dr, tabno);
            controls.Add(b);
            return b;
        }

        protected PictureBox AddPictureBox(Texture2D img, XnaRect sr, XnaRect dr, int tabno = -1)
        {
            PictureBox p = new PictureBox(this, sr, img, dr, tabno);
            controls.Add(p);
            return p;
        }

        protected OptionButton AddOptionButton(PressControlHandler press_handler, string c, int x, int y, int optgrp, int tabno = -1)
        {
            Vector2 ssize = Gfx.GuiFont1.MeasureString(c);
            if (x == -1) x = (InnerWidth - (int)ssize.X + 16) / 2;
            OptionButton b = new OptionButton(this, press_handler, c, x, y, (int)ssize.X + 16, (int)ssize.Y + 16, tabno, optgrp);
            controls.Add(b);
            return b;
        }

        protected OptionPictureButton AddOptionPictureButton(PressControlHandler press_handler, XnaRect sr, Texture2D img, XnaRect dr, int optgrp, int tabno = -1)
        {
            OptionPictureButton b = new OptionPictureButton(this, press_handler, sr, img, dr, tabno, optgrp);
            controls.Add(b);
            return b;
        }

        protected InventoryBox AddInventoryBox(IInventory c, XnaRect r, bool use_shortcuts = false, int tabno = -1)
        {
            //if (!(c is Container || c is Character)) throw new Exception("Inventory must belong to a Character or a Container!");
            InventoryBox i = new InventoryBox(this, c, r, tabno, use_shortcuts);//PictureButton(r, x, y, r.Width, r.Height);
            controls.Add(i);
            return i;
        }

        protected EquipmentSlot AddEquipmentSlot(int x, int y, PCType pc, String txt, eEquipSlot kind, int tabno = -1)
        {
            //if (!(c is Container || c is Character)) throw new Exception("Inventory must belong to a Character or a Container!");
            EquipmentSlot e = new EquipmentSlot(this, x, y, pc, txt, kind);//PictureButton(r, x, y, r.Width, r.Height);
            controls.Add(e);
            return e;
        }

        //protected IdentifyBox AddIdentifyBox(XnaRect r, int price, int tabno = -1)
        //{
        //    IdentifyBox i = new IdentifyBox(this, r, price, tabno);
        //    controls.Add(i);
        //    return i;
        //}
        //protected EnchantingBox AddEnchantingBox(XnaRect r, eEnchantShop type, int tabno = -1)
        //{
        //    EnchantingBox i = new EnchantingBox(this, r, type, tabno);
        //    controls.Add(i);
        //    return i;
        //}


        protected ListBox AddListBox(ChangeSelectedHandler handler, int x, int y, int w, int h, int tab, params ListBoxItem[] list)
        {
            ListBox l = new ListBox(handler, this, x, y, w, h, tab, list);
            controls.Add(l);
            return l;
        }
        //protected Slider AddSlider(int x, int y, int w, int tab)
        //{
        //    Slider s = new Slider(this, x, y, w, tab);
        //    controls.Add(s);
        //    return s;
        //}

        protected Vector2 GetClientAreaPos()
        {
            return new Vector2(X + ClientX, Y + ClientY);
        }
        protected Vector2 GetWindowPos()
        {
            return new Vector2(X, Y);
        }

        protected void PositionNearMouse(int w, int h)
        {
            //Work out position based on mouse pointer. If it will fit on screen, it should appear below-right,
            //otherwise, try somewhere else.
            int x, y;
            if (Gui.Ms.X + 5 + w < Gfx.WinW)
                x = Gui.Ms.X + 5;
            else
                x = Gui.Ms.X - w - 5;
            if (Gui.Ms.Y + 5 + h < Gfx.WinH)
                y = Gui.Ms.Y + 5;
            else
                y = Gui.Ms.Y - h - 5;

            X = 0; Y = 0;
            //Reposition and resize the menu accordingly
            Move(x, y, w, h);
        }

        /// <summary>
        /// Draws the window
        /// </summary>
        /// <param name="sb"></param>
        /// <param name="partial">0: Draw everything  1: draw only the border  2: draw only the controls</param>
        public virtual void Draw(SpriteBatch sb, int partial = 0)
        {
            if (!Visible) return;

            if (partial != 2)
            {

                if (Border)
                {
                    Gfx.DrawFrame(X, Y, Width, Height, Color.White);
                }
            }

            if (partial != 1)
                foreach (Control c in controls)
                    if (currentTab == c.TabNo || c.TabNo == -1)
                        c.Draw(sb, X + ClientX, Y + ClientY);

        }

        public virtual bool Handle()
        {
            if (!Visible) return false;

            bool interacted = false;
            controlEvent = null;

            if (EscapeKeyCloses && KeyHandler.KeyHit(Keys.Escape)) 
            { 
                KillMe = true; return true; 
            }

            foreach (Control b in controls)
                if (currentTab == b.TabNo || b.TabNo == -1)
                    interacted |= b.Handle(X + ClientX, Y + ClientY);

            if (interacted)
            {
                //Automatically handle the close window picture button.
                //if (closeButton != null && controlEvent == closeButton) { KillMe = true; return true; }

                //Switch tabs if there are any
                //if (controlEvent is TabButton)
                //{
                //    for (int i = 0; i < Tabs.Count(); i++)
                //        if (controlEvent == Tabs[i]) { currentTab = i; break; }
                //}
                return true;
            }
            else
                //If mouse wasn't near a control, try to start moving window.

                if (Gui.Ms.X >= X && Gui.Ms.X < X + Width)//MouseIsOnTopFrame())
                {
                    if (Gui.Ms.Y >= Y && Gui.Ms.Y < Y + frameHeight)
                    {
                        //if (moveable && Gui.moveCarryable == null)
                        if (Gui.LMBHit && moveable)
                        {
                            Gui.StartMovingWindow(this);
                            return true;
                        }
                    }
                    else if (Gui.Ms.Y >= Y + Height - frameHeight && Gui.Ms.Y < Y + Height)
                    {
                        if (Gui.LMBHit && resizeable)
                        {
                            Gui.StartResizingWindow(this);
                            return true;
                        }

                    }


                }
            return false;
        }

        protected virtual void pressWindowClose(Control button_pressed) { KillMe = true; }

        void pressExpand(Control b)
        {

            if (Height >= Maths.Min(maxHeight, Gfx.WinH - Y))
                Resize(Width, defHeight);
            else
                Resize(Width, Maths.Min(maxHeight, Gfx.WinH - Y));

            //Height - h

            //int h = (maxHeight - minHeight) / 2 + minHeight;

            //if (Height > h) 
            //    Resize(Width, minHeight);
            //else 
            //    Resize(Width, Maths.Min(maxHeight, Gfx.WinH - Y));

        }

        void pressWindowTab(Control button_pressed)
        {
            for (int i = 0; i < Tabs.Count(); i++)
                if (button_pressed == Tabs[i]) { currentTab = i; break; }
        }

        public bool MouseIsInside()
        {
            return Gui.Ms.X >= X && Gui.Ms.Y >= Y && Gui.Ms.X < X + Width && Gui.Ms.Y < Y + Height;
        }
        bool MouseIsOnTopFrame()
        {
            return (Gui.Ms.X >= X && Gui.Ms.Y >= Y && Gui.Ms.X < X + Width && Gui.Ms.Y < Y + Height)
                    && !(Gui.Ms.X >= X + frameWidth && Gui.Ms.Y >= Y + frameHeight && Gui.Ms.X < X + Width - frameWidth && Gui.Ms.Y < Y + Height - frameHeight);
        }


        public void Move(int xmod, int ymod, int newwidth = -1, int newheight = -1)
        {
            if (newwidth != -1) Width = newwidth;
            if (newheight != -1) Height = newheight;
            X += xmod;
            Y += ymod;
            if (X < 0) X = 0;
            if (Y < 0) Y = 0;
            if (X >= Gfx.WinW - Width) X = (int)Gfx.WinW - Width;
            if (Y >= Gfx.WinH - Height) Y = (int)Gfx.WinH - Height;
        }

        public virtual void Resize(int w, int h)
        {
            Width = w;
            Height = Maths.MinMax(minHeight, maxHeight, h);
        }

        /// <summary>
        /// Re-position the window
        /// </summary>
        /// <param name="x">If >= 0, give absolute coordinate, if -1, right edge. If -2 centred</param>
        /// <param name="y">If >= 0, give absolute coordinate, if -1, bottom edge. If -2 centred</param>
        public void Position(int x, int y, int modx = 0, int mody = 0)
        {
            if (x >= 0)
            {
                X = x + modx;
                if (X >= Gfx.WinW - Width) X = (int)Gfx.WinW - Width;
            }
            else if (x == -1) X = (int)Gfx.WinW - Width + modx;
            else if (x == -2) X = (int)(Gfx.WinW / 2 - Width / 2) + modx;

            if (y >= 0)
            {
                Y = y + mody;
                if (Y >= Gfx.WinH - Height) Y = (int)Gfx.WinH - Height;
            }
            else if (y == -1) Y = (int)Gfx.WinH - Height + mody;
            else if (y == -2) Y = (int)(Gfx.WinH / 2 - Height / 2) + mody;
        }

        /// <summary>
        /// Lines up a series of controls in a row, with a number of pixels between each one 
        /// </summary>
        /// <param name="x">Start x position</param>
        /// <param name="y">y position</param>
        /// <param name="gap">Gap to leave between each control</param>
        /// <param name="controls">All the controls to line up</param>
        public void LineUpControls(int x, int y, int gap, params Control[] controls)
        {

            foreach (Control c in controls)
            {
                c.X = x;
                c.Y = y;
                x += c.Width + gap;
            }
        }

        /// <summary>
        /// Lines up a series of controls in a right-justified row, with a number of pixels between each one 
        /// </summary>
        /// <param name="x">rightmost x position</param>
        /// <param name="y">y position</param>
        /// <param name="gap">Gap to leave between each control</param>
        /// <param name="controls">All the controls to line up</param>
        public void LineUpControlsRight(int x, int y, int gap, params Control[] controls)
        {

            foreach (Control c in controls.Reverse())
            {
                c.X = x - c.Width;
                c.Y = y;
                x -= c.Width + gap;
            }
        }

        public void LineUpControlsDown(int x, int y, int gap, params Control[] controls)
        {

            foreach (Control c in controls)
            {
                c.X = x;
                c.Y = y;
                y += c.Height + gap;
            }
        }

        public virtual void Close()
        {
            //If KillMe is flagged the Gui Handle routine will automatically do this.
            //if (!KillMe)
            Gui.GuiWindows.Remove(this);
        }

        //public virtual void makeInventoryPopUpWindow(int slot) {
        //}
    }

}