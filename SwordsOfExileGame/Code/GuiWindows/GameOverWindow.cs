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

    class GameOverWindow : GuiWindow
    {

        //public static bool IsRunning = false;

        public GameOverWindow()
            : base(000, 000, 310, 400, true, false, true, true, false)
        {
            Game.CurrentMap = null;
            Gfx.FadeMode = 0;
            //Game.GameOver = false;
            //IsRunning = true;

            var p = AddPictureBox(Gfx.DialogGfx[0], new XnaRect(0, 288, 72, 72), new XnaRect(150, 10, 72, 72));
            p.Position(0, 20, 0, -1);

            var l = AddRichTextBox(
                //"Being an adventurer is unpredictable work. Sometimes, you becomes heroes, wealthy as Croesus and famous beyond words. " +
                //          "And, sometimes your gnawed bones are left to dry out in some shadowy, forgotten hole.@n@n" +
                //          "Unfortunately, the latter fate is the one that just befell you. Easy come, easy go. Care to make another attempt?"
                Scenario.DeathMessage
                , null, 10, p.Y + p.Height + 20, 270);
            var b = AddButton(pressButton, "Main Menu", 0, l.Y + l.Height + 20, -1, -1);
            Resize(310, b.Y + b.Height + 30);
            b.Position(0, -10, 0, 1);
            
            Position(-2, -2);
        }

        void pressButton(Control c)
        {
            Game.Instance.BackToMainMenu();
        }


        //public override void Close()
        //{
        //    base.Close();
        //    IsRunning = false;
        //}



    }
}