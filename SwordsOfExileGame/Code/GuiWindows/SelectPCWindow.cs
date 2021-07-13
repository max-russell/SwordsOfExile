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
    delegate void SelectPCWindowHandler(PCType pc);

    class SelectPCWindow : GuiWindow
    {
        SelectPCWindowHandler Handler;
        List<PictureButton> pc_buttons = new List<PictureButton>();
        List<PCType> pcs = new List<PCType>();

        public SelectPCWindow(SelectPCWindowHandler handler, string msg, bool only_living)
            : base(0, 0, 270, 240, true, false, true, true, true)
        {
            Handler = handler;

            Label lbl = AddLabel(msg, 10, 10, 240, -1, true);
            int y = lbl.Y + lbl.Height + 10;
            lbl = AddLabel("Choose one of your party:", 10, y, 240, -1, true);
            y += lbl.Height + 10;

            XnaRect dr = new XnaRect(10, y, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);

            foreach (PCType pc in Party.PCList)
            {
                XnaRect sr = new XnaRect(0, 0, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);//pc.GetGraphicRect(true);
                var opt = AddPictureButton(pressPC, sr, pc.PortraitTexture, dr);
                if ((only_living && pc.LifeStatus != eLifeStatus.ALIVE) || (!only_living && pc.IsGone()))
                    opt.Enabled = false;
                pc_buttons.Add(opt);
                pc_buttons[pc_buttons.Count - 1].KeyShortcut = pc.Slot + Keys.D1;

                pcs.Add(pc);
                dr.X += Gfx.PCPORTRAITWIDTH + 10;
            }

            y += pc_buttons[0].Height + 10;

            Button btn = AddButton(pressCancel, "Cancel", 200, y);
            CancelKeyControl = btn;
            Position(-2, -2);
            Resize(280, y + btn.Height + 30);
            btn.X = Width - btn.Width - 30;

        }

        void pressPC(Control button_pressed)
        {
            for (int n = 0; n < pc_buttons.Count; n++)
            {
                if (button_pressed == pc_buttons[n])
                {
                    Handler.Invoke(pcs[n]);
                    KillMe = true;
                }
            }
        }

        void pressCancel(Control button_pressed) { KillMe = true; Handler.Invoke(null); }
    }

}