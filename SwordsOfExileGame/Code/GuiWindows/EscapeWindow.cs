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

namespace SwordsOfExileGame
{

    class EscapeMenuWindow : GuiWindow
    {
        Button[] Buttons;// saveBtn, saveAsBtn, loadLastBtn, loadBtn, optionsBtn, helpBtn, startBtn, quitBtn;

        public EscapeMenuWindow()
            : base(0, 0, 200, 353, true, false, true, true, true)
        {
            EscapeKeyCloses = true;

            string[] btntext = { "Quicksave", "Quickload", "Load/Save Game", "View Notes", "Options", "Help", "Start Menu", "Exit Game" };
            Buttons = new Button[btntext.Length];

            for (int n = 0; n < Buttons.Length; n++)
                Buttons[n] = AddButton(pressButton, btntext[n], 0, 0, 160, 30);

            LineUpControlsDown(10, 10, 10, Buttons);

            Position(-2, -2);
        }

        void pressButton(Control b)
        {
            for (int n = 0; n < Buttons.Length; n++)
                if (b == Buttons[n])
                {
                    switch (n)
                    {
                        case 0: //Quicksave
                            //Action.Requested = eAction.QuickSave;
                            new Action(eAction.QuickSave);
                            KillMe = true;
                            break;
                        case 1: //Quickload
                            new Action(eAction.QuickLoad);
                            KillMe = true;
                            break;
                        case 2: //Load/Save Menu
                            new Action(eAction.LoadSaveMenu);
                            KillMe = true;
                            break;
                        case 3: //Notes
                            new NotesWindow();
                            KillMe = true;
                            break;

                        case 4: //Options
                            new OptionsWindow();
                            break;
                        case 5: //Help
                            KillMe = true;
                            break;
                        case 6: //Start Menu
                            new MessageWindow(q => { if (q == 0) Game.Instance.BackToMainMenu(); }, "Any unsaved progress in the current game will be lost. Proceed?", eDialogPic.NONE, 0, "Ok", "Cancel"); 
                            break;
                        case 7: //Exit Game
                            Game.Quit = true;
                            KillMe = true;
                            break;
                    }
                    
                    return;
                }
        }

        public override bool Handle()
        {
            return base.Handle();
        }

    }

}