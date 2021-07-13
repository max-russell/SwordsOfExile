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

    delegate void ChoosePictureHandler(int n);

    class ChoosePictureWindow : GuiWindow
    {
        List<OptionPictureButton> Pictures;
        Button OK, Cancel;
        ChoosePictureHandler Handler;

        const int MAXCOLUMNS = 12;

        public ChoosePictureWindow(Func<IEnumerable<XnaRect>> collate, Texture2D texture, int def, ChoosePictureHandler handler)
             : base(0, 0, 400, 400, true, false, true, true, false)
        {
            Handler = handler;
            Pictures = new List<OptionPictureButton>();

            int x = 0, y = 0, rightmost = 0;
            foreach (XnaRect r in collate.Invoke())
            {
                OptionPictureButton o = new OptionPictureButton(this, null, r, texture, new XnaRect(10 + x * (r.Width + 4), 10 + y * (r.Height + 4), r.Width, r.Height), 0, 0);

                rightmost = Maths.Max(rightmost, 10 + x * (r.Width + 4) + r.Width);

                controls.Add(o);
                Pictures.Add(o);
                if (++x == MAXCOLUMNS) { y++; x = 0;}
            }

            Pictures[def].OptionPress(false);

            InnerWidth = rightmost + 10;
            InnerHeight = Pictures[Pictures.Count - 1].Y + Pictures[Pictures.Count - 1].Height + 60;

            //Resize(30 + rightmost, 60 + 60 +  + 10 * 2);
            Position(-2, -2);

            OK = AddButton(pressButton, "OK", 0, 0);
            Cancel = AddButton(pressButton, "Cancel", 0, 0);

            LineUpControlsRight(InnerWidth - 10, InnerHeight - 50, 10, OK, Cancel);
        }


        //public ChoosePictureWindow(Texture2D texture, int w, int h, int def, ChoosePictureHandler handler, Func<int, int, XnaRect> predicate)
        //    : base(0, 0, 400, 400, true, false, true, true, false)
        //{
        //    Handler = handler;
        //    Pictures = new List<OptionPictureButton>();

        //    Func<int, int, XnaRect> f = (x, y) => new XnaRect(x * w, y * h, w, h);

        //    for(int y = 0; y < texture.Height / h; y++)
        //        for (int x = 0; x < texture.Width / w; x++)
        //        {
        //            OptionPictureButton o = new OptionPictureButton(this, null, /*new XnaRect(x * w, y * h, w, h)*/predicate(x,y), texture, new XnaRect(10 + x * (w + 4), 10 + y * (h + 4), w, h), 0, 0);
        //            controls.Add(o);
        //            Pictures.Add(o);
        //        }

        //    Pictures[def].OptionPress(false);

        //    Resize(20 + texture.Width + w*2, 60 + texture.Height + h*2);
        //    Position(-2, -2);

        //    OK = AddButton(pressButton, "OK", 0, 0);
        //    Cancel = AddButton(pressButton, "Cancel", 0, 0);

        //    LineUpControlsRight(InnerWidth - 10, InnerHeight - 50, 10, OK, Cancel);
        //}

        void pressButton(Control b)
        {
            if (b == OK)
            {
                if (Handler != null)
                    for (int n = 0; n < Pictures.Count; n++)
                    {
                        if (Pictures[n].Pressed) { Handler.Invoke(n); break; }
                    }
            }
            KillMe = true;   
        }
    }

}