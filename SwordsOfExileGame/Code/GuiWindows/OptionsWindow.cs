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
    class OptionsWindow : GuiWindow
    {
        //static StartMenuWindow instance;
        //Button b_resume, b_startnew, b_quit, b_load;
        ListBox resolutionsList;
        Button okButton, cancelButton, DoKeyRemap;
        Button bWindowed, bFullScreen, bIncVol, bDecVol;
        Label volLabel;
        int tempVol;

        public OptionsWindow()
            : base(20, 20, 400, 310, true, false, true, true, false)
        {
            //AddPictureBox(Gfx.LogoPic, Gfx.LogoPic.Bounds, new XnaRect(0, 10, Gfx.LogoPic.Width, Gfx.LogoPic.Height));

            tempVol = Sound.Volume;

            AddLabel("Available Resolutions", 10, 10, -1, -1, false);

            resolutionsList = new ListBox(null, this, 10,30,200,250,-1);// AddListBox(changeRes, 10, 30, 200, 250,-1,);
            controls.Add(resolutionsList);

            ListBoxItem current = null;
            foreach(DisplayMode mode in Gfx.EachAvailableResolution())
            {
                ListBoxItem i = resolutionsList.AddItem(String.Format("{0} x {1}", mode.Width, mode.Height), Color.White, mode, false);
                if (mode.Width == Gfx.WinW && mode.Height == Gfx.WinH)
                    current = i;
            }
            resolutionsList.SelectedItem = current;
            resolutionsList.RevealItem(current);


            bWindowed = AddOptionButton(pressButton, "Windowed", 0, 0, 0);
            bFullScreen = AddOptionButton(pressButton, "Full Screen", 0, 0, 0);
            LineUpControls(230, 30, 0, bWindowed, bFullScreen);

            if (Gfx.FullScreen) bFullScreen.Pressed = true; else bWindowed.Pressed = true;

            volLabel = AddLabel("Volume:  " + tempVol, 240, 80, -1, -1, false);
            bDecVol = AddPictureButton(pressButton, new XnaRect(117, 0, 18, 18), Gfx.NewGui, new XnaRect(310, 78, 18, 18));
            bIncVol = AddPictureButton(pressButton, new XnaRect(99, 0, 18, 18), Gfx.NewGui, new XnaRect(328, 78, 18, 18));

            if (tempVol == 10) bIncVol.Enabled = false;
            if (tempVol == 0) bDecVol.Enabled = false;

            DoKeyRemap = AddButton(pressButton, "Remap Keys", 230, 120, -1, -1);

            cancelButton = AddButton(pressButton, "Cancel", 0, 0, -1, -1);
            okButton = AddButton(pressButton, "Accept", 0, 0, -1, -1);
            LineUpControlsRight(Width - 30, Height - okButton.Height - 30, 10, cancelButton, okButton);

            Position(-2, -2);
        }

        void pressButton(Control b)
        {
            if (b == okButton)
            {
                Sound.Volume = tempVol;
                var mode = (DisplayMode)resolutionsList.SelectedItem.Tag;
                Game.SaveSettings(mode.Width, mode.Height, bFullScreen.Pressed ? 1 : 0);

                if (mode.Width != Gfx.WinW || mode.Height != Gfx.WinH || bFullScreen.Pressed != Gfx.FullScreen)
                    new MessageWindow(null, "Resolution and Full Screen settings will be applied the next time the game is restarted.", eDialogPic.NONE, -1, "OK");

                KillMe = true;
            }
            else if (b == cancelButton)
            {
                KillMe = true;
            }
            else if (b == bDecVol)
            {
                tempVol = Maths.Max(tempVol - 1, 0);
                if (tempVol == 0) bDecVol.Enabled = false; else bDecVol.Enabled = true;
                volLabel.Text = "Volume:  " + tempVol;
            }
            else if (b == bIncVol)
            {
                tempVol = Maths.Min(tempVol + 1, 10);
                if (tempVol == 10) bIncVol.Enabled = false; else bIncVol.Enabled = true;
                volLabel.Text = "Volume:  " + tempVol;
            }
            else if (b == DoKeyRemap)
            {
                new KeyMappingWindow();
            }
        }

        //void changeRes(bool user_caused, ListBoxItem item)
        //{

        //}

    }

}