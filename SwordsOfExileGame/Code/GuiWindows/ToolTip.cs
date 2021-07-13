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
    class ToolTipV2 : GuiWindow
    {
        //Control Caller; //If null - it's the map
        bool onMap = false;
        public XnaRect mZone; //The area the mouse must stay inside for the ToolTip to remain open
        Vector2 scrollPos = Vector2.Zero;

        public ToolTipV2(bool onmap, XnaRect zone, string txt, int width = -1)//, bool on_map)
            : base(0, 0, 10, 10, true, false, false, true, false)
        {
            if (Gui.DragItem != null) return;

            Gui.ActiveToolTip = this;
            //OnMap = on_map;
            //if (OnMap)
            //{
            //    scrollPos = Gfx.Scroll;
            //}
            //OnTop = true;
            //msPos = new Point(Gui.Ms.X, Gui.Ms.Y);
            mZone = zone;
            onMap = onmap;
            //Caller = caller;
            if (onMap) scrollPos = Gfx.Scroll;

            int w = 0, h = 0;
            RichTextBox r = new RichTextBox(this, null, txt, 0, 0, width, -1, -1);//AddRichTextBox(txt, 0, 0, true);
            controls.Add(r);
            w = r.Width + ClientX * 2;
            h = r.Height + ClientY * 2;
            PositionNearMouse(w, h);
            
            //active = true;
        }

        public override bool Handle()
        {
            if (Gui.LMBHit || Gui.LMBHitUp || Gui.RMBHit || Gui.RMBHitUp || Gui.MMBHit || Gui.MMBHitUp)
                Gui.ActiveToolTip = null;
            else if (!mZone.Contains(Gui.Ms.X, Gui.Ms.Y))
                Gui.ActiveToolTip = null;
            //else if (Caller != null)
            //{
            //    if (!Caller.Visible) Gui.ActiveToolTip = null;
            //}
            //else if (onMap && Gfx.Scroll != scrollPos)
            //    Gui.ActiveToolTip = null;

            if (Gui.ActiveToolTip == null) return false;

            PositionNearMouse(Width, Height);
            return false;
        }
    }

    //class ToolTip : GuiWindow
    //{
    //    //This stores the mouse position when the tooltip first appears. If the mouse moves a few pixel from this,
    //    //the tooltip automatically closes.
    //    static Point msPos;

    //    const int TOOLTIPSTRAYDISTANCE = 8;
    //    static int tooltipWait;
    //    static bool active = false;


    //    public static int GetWait() {return Gui.TooltipDelay - tooltipWait;}

    //    public static bool OnMap = false;
    //    Vector2 scrollPos = Vector2.Zero;

    //    public static bool WaitForToolTip() {
    //        if (!active) {

    //            if (Math.Abs(Gui.Ms.X - msPos.X) + Math.Abs(Gui.Ms.Y - msPos.Y) > TOOLTIPSTRAYDISTANCE)
    //            {
    //                tooltipWait = 0;
    //                msPos = new Point(Gui.Ms.X, Gui.Ms.Y);
    //                return false;
    //            }

    //            tooltipWait++;
    //            if (tooltipWait >= Gui.TooltipDelay) {
    //                tooltipWait = 0;
    //                return true;
    //            }
    //        }
    //        return false;
    //    }

    //    public static void New(string txt, int width = -1, bool on_map=false)
    //    {
    //        if (txt == null) return;
    //        else new ToolTip(txt, width, on_map);
    //    }

    //    public static void ResetWait() {
    //        tooltipWait = 0;
    //    }

    //    public ToolTip(string txt, int width, bool on_map)
    //        : base(0, 0, 10, 10, true, false, false, true, false)
    //    {
    //        OnMap = on_map;
    //        if (OnMap)
    //        {
    //            scrollPos = Gfx.Scroll;
    //        }
    //        OnTop = true;
    //        msPos = new Point(Gui.Ms.X, Gui.Ms.Y);
    //        int w = 0, h = 0;
    //        RichTextBox r = new RichTextBox(this, null, txt, 0, 0, width,-1, -1);//AddRichTextBox(txt, 0, 0, true);
    //        controls.Add(r);
    //        w = r.Width + ClientX * 2;
    //        h = r.Height + ClientY * 2;
    //        PositionNearMouse(w, h);
    //        active = true;
    //    }

    //    //public ToolTip(ITooltipable tt) : base(null,0,0,10,10,true,false,false,true,false)
    //    //{
    //    //    msPos = new Point(Gui.Ms.X, Gui.Ms.Y);
    //    //    int w = 0, h = 0;
    //    //    string txt = tt.TooltipInfo();
    //    //    Vector2 sz = Gfx.GuiFont1.MeasureString(txt);
    //    //    w = (int)sz.X + 16;
    //    //    h = (int)sz.Y + 16;
    //    //    PositionNearMouse(w, h);
    //    //    AddLabel(txt,8,8);
    //    //    active = true;
    //    //}

    //    public override bool Handle() {
    //        if (Gui.LMBDown || Gui.RMBDown) { 
    //            KillMe = true; active = false; }
    //        if (Math.Abs(Gui.Ms.X - msPos.X) + Math.Abs(Gui.Ms.Y - msPos.Y) > TOOLTIPSTRAYDISTANCE) { KillMe = true; active = false; }
    //        if (OnMap && Gfx.Scroll != scrollPos) { KillMe = true; active = false; }
    //        return false;
    //    }

    //}

}