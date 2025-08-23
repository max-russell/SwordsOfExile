using System.Collections.Generic;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal delegate void SelectPCWindowHandler(PCType pc);

internal class SelectPCWindow : GuiWindow
{
    private SelectPCWindowHandler Handler;
    private List<PictureButton> pc_buttons = new();
    private List<PCType> pcs = new();

    public SelectPCWindow(SelectPCWindowHandler handler, string msg, bool only_living)
        : base(0, 0, 270, 240, true, false, true, true, true)
    {
        Handler = handler;

        var lbl = AddLabel(msg, 10, 10, 240, -1, true);
        var y = lbl.Y + lbl.Height + 10;
        lbl = AddLabel("Choose one of your party:", 10, y, 240, -1, true);
        y += lbl.Height + 10;

        var dr = new XnaRect(10, y, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);

        foreach (var pc in Party.PCList)
        {
            var sr = new XnaRect(0, 0, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);//pc.GetGraphicRect(true);
            var opt = AddPictureButton(pressPC, sr, pc.PortraitTexture, dr);
            if ((only_living && pc.LifeStatus != eLifeStatus.ALIVE) || (!only_living && pc.IsGone()))
                opt.Enabled = false;
            pc_buttons.Add(opt);
            pc_buttons[pc_buttons.Count - 1].KeyShortcut = pc.Slot + Keys.D1;

            pcs.Add(pc);
            dr.X += Gfx.PCPORTRAITWIDTH + 10;
        }

        y += pc_buttons[0].Height + 10;

        var btn = AddButton(pressCancel, "Cancel", 200, y);
        CancelKeyControl = btn;
        Position(-2, -2);
        Resize(280, y + btn.Height + 30);
        btn.X = Width - btn.Width - 30;

    }

    private void pressPC(Control button_pressed)
    {
        for (var n = 0; n < pc_buttons.Count; n++)
        {
            if (button_pressed == pc_buttons[n])
            {
                Handler.Invoke(pcs[n]);
                KillMe = true;
            }
        }
    }

    private void pressCancel(Control button_pressed) { KillMe = true; Handler.Invoke(null); }
}