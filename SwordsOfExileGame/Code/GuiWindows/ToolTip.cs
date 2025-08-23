using Microsoft.Xna.Framework;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class ToolTipV2 : GuiWindow
{
    private bool onMap = false;
    public XnaRect mZone; //The area the mouse must stay inside for the ToolTip to remain open
    private Vector2 scrollPos = Vector2.Zero;

    public ToolTipV2(bool onmap, XnaRect zone, string txt, int width = -1)//, bool on_map)
        : base(0, 0, 10, 10, true, false, false, true, false)
    {
        if (Gui.DragItem != null) return;

        Gui.ActiveToolTip = this;
        mZone = zone;
        onMap = onmap;
        if (onMap) scrollPos = Gfx.Scroll;

        int w = 0, h = 0;
        var r = new RichTextBox(this, null, txt, 0, 0, width, -1, -1);
        controls.Add(r);
        w = r.Width + ClientX * 2;
        h = r.Height + ClientY * 2;
        PositionNearMouse(w, h);
    }

    public override bool Handle()
    {
        if (Gui.LMBHit || Gui.LMBHitUp || Gui.RMBHit || Gui.RMBHitUp || Gui.MMBHit || Gui.MMBHitUp)
            Gui.ActiveToolTip = null;
        else if (!mZone.Contains(Gui.Ms.X, Gui.Ms.Y))
            Gui.ActiveToolTip = null;

        if (Gui.ActiveToolTip == null) return false;

        PositionNearMouse(Width, Height);
        return false;
    }
}