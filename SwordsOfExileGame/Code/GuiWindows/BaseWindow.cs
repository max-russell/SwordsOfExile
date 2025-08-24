using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

/*****************************************************************************************************
 * WINDOW CLASS
 *****************************************************************************************************/
internal class GuiWindow
{
    protected PartyType Party => Game.CurrentParty;
    protected TownMap Town => Game.CurrentMap as TownMap;

    public bool Border = true; //False if instance handles drawing its own window borders
    private bool visible = false;
    public virtual bool Visible
    {
        get => visible;
        set
        {
            visible = value; if (Modal) Gui.WorldModalPaused = value;
        }
    }

    public bool EscapeKeyCloses = false; //Don't set if CancelKeyControl is set to something.
    public bool Modal = false; //True if the window freezes all windows beneath it until it closes 
    public bool KillMe = false; //Set to true to end the window at the next opportunity
    public bool OnTop = false; //Set to true for tooltips and popupmenus to always appear above other windows
    private bool moveable = true;      //The window can be repositioned by the user
    private bool closeable = true;     //The window has a little cross button in the corner which the user can use to close it

    private bool resizeable = false;   //The window can be resized by the user (but only its Height)
    private int minHeight = 0, defHeight = 0, maxHeight = int.MaxValue;  //Smallest and largest values window can be resized to.

    private Color backCol = new(255, 255, 255, 200);
    public int X, Y, Width, Height;
    public int ClientX = 0, ClientY = 0;
    public int InnerWidth
    {
        get => Width - ClientX * 2;
        set => Move(0, 0, value + ClientX * 2, Height);
    }
    public int InnerHeight
    {
        get => Height - ClientY * 2;
        set => Move(0, 0, Width, value + ClientY * 2);
    }

    private readonly int frameWidth, frameHeight;

    public TabButton[] Tabs;
    public int currentTab; //The currently selected tab
    public Control controlEvent; //Set to the control that the user has just interacted with

    public Control OKKeyControl, CancelKeyControl;

    private PictureButton closeButton, expandButton; //The button that closes the form

    public List<Control> controls = new(); //All the controls on the window

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
        }

        if (!(this is ToolTipV2))
        {
            Gui.GuiWindows.Add(this);
            Gui.ActiveToolTip = null;
        }
    }

    public int Opacity { set => backCol = new Color(255, 255, 255, value);
        get => backCol.A;
    }

    public void SetTabs(params string[] tabnames)
    {
        Tabs = new TabButton[tabnames.Count()];
        var xpos = 6;

        for (var i = 0; i < tabnames.Length; i++)
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
        var l = new Label(this, c, x, y, w, h, wrapping_on, tabno);
        controls.Add(l);
        return l;
    }

    protected RichTextBox AddBlankRichTextBox(LinkClickHandler handler, int x, int y, int w, int h, int tabno = -1)
    {
        var l = new RichTextBox(this, handler, x, y, w, h, tabno);
        controls.Add(l);
        return l;
    }

    protected RichTextBox AddRichTextBox(string msg, LinkClickHandler handler, int x, int y, int width, int tabno = -1)
    {
        var l = new RichTextBox(this, handler, msg, x, y, width, -1, tabno);
        controls.Add(l);
        return l;
    }

    protected Button AddButton(PressControlHandler press_handler, string c, int x, int y, int w = -1, int h = -1, int tabno = -1)
    {
        Vector2 ssize = Gfx.GuiFont1.MeasureString(c);
        if (x == -1) x = (InnerWidth - (int)ssize.X + 16) / 2;
        var b = new Button(this, press_handler, c, x, y, w, h, tabno);
        controls.Add(b);
        return b;
    }

    protected PictureButton AddPictureButton(PressControlHandler press_handler, XnaRect sr, Texture2D img, XnaRect dr, int tabno = -1)
    {
        var b = new PictureButton(this, press_handler, sr, img, dr, tabno);
        controls.Add(b);
        return b;
    }

    protected PictureBox AddPictureBox(Texture2D img, XnaRect sr, XnaRect dr, int tabno = -1)
    {
        var p = new PictureBox(this, sr, img, dr, tabno);
        controls.Add(p);
        return p;
    }

    protected OptionButton AddOptionButton(PressControlHandler press_handler, string c, int x, int y, int optgrp, int tabno = -1)
    {
        Vector2 ssize = Gfx.GuiFont1.MeasureString(c);
        if (x == -1) x = (InnerWidth - (int)ssize.X + 16) / 2;
        var b = new OptionButton(this, press_handler, c, x, y, (int)ssize.X + 16, (int)ssize.Y + 16, tabno, optgrp);
        controls.Add(b);
        return b;
    }

    protected OptionPictureButton AddOptionPictureButton(PressControlHandler press_handler, XnaRect sr, Texture2D img, XnaRect dr, int optgrp, int tabno = -1)
    {
        var b = new OptionPictureButton(this, press_handler, sr, img, dr, tabno, optgrp);
        controls.Add(b);
        return b;
    }

    protected InventoryBox AddInventoryBox(IInventory c, XnaRect r, bool use_shortcuts = false, int tabno = -1)
    {
        var i = new InventoryBox(this, c, r, tabno, use_shortcuts);
        controls.Add(i);
        return i;
    }

    protected EquipmentSlot AddEquipmentSlot(int x, int y, PCType pc, string txt, eEquipSlot kind, int tabno = -1)
    {
        var e = new EquipmentSlot(this, x, y, pc, txt, kind);
        controls.Add(e);
        return e;
    }

    protected ListBox AddListBox(ChangeSelectedHandler handler, int x, int y, int w, int h, int tab, params ListBoxItem[] list)
    {
        var l = new ListBox(handler, this, x, y, w, h, tab, list);
        controls.Add(l);
        return l;
    }

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
            foreach (var c in controls)
                if (currentTab == c.TabNo || c.TabNo == -1)
                    c.Draw(sb, X + ClientX, Y + ClientY);

    }

    public virtual bool Handle()
    {
        if (!Visible) return false;

        var interacted = false;
        controlEvent = null;

        if (EscapeKeyCloses && KeyHandler.KeyHit(Keys.Escape)) 
        { 
            KillMe = true; return true; 
        }

        foreach (var b in controls)
            if (currentTab == b.TabNo || b.TabNo == -1)
                interacted |= b.Handle(X + ClientX, Y + ClientY);

        if (interacted)
        {
            return true;
        }
        else
            //If mouse wasn't near a control, try to start moving window.

        if (Gui.Ms.X >= X && Gui.Ms.X < X + Width)
        {
            if (Gui.Ms.Y >= Y && Gui.Ms.Y < Y + frameHeight)
            {
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

    private void pressExpand(Control b)
    {

        if (Height >= Maths.Min(maxHeight, Gfx.WinH - Y))
            Resize(Width, defHeight);
        else
            Resize(Width, Maths.Min(maxHeight, Gfx.WinH - Y));
    }

    private void pressWindowTab(Control button_pressed)
    {
        for (var i = 0; i < Tabs.Count(); i++)
            if (button_pressed == Tabs[i]) { currentTab = i; break; }
    }

    public bool MouseIsInside()
    {
        return Gui.Ms.X >= X && Gui.Ms.Y >= Y && Gui.Ms.X < X + Width && Gui.Ms.Y < Y + Height;
    }

    private bool MouseIsOnTopFrame()
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

        foreach (var c in controls)
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

        foreach (var c in controls.Reverse())
        {
            c.X = x - c.Width;
            c.Y = y;
            x -= c.Width + gap;
        }
    }

    public void LineUpControlsDown(int x, int y, int gap, params Control[] controls)
    {

        foreach (var c in controls)
        {
            c.X = x;
            c.Y = y;
            y += c.Height + gap;
        }
    }

    public virtual void Close()
    {
        Gui.GuiWindows.Remove(this);
    }
}