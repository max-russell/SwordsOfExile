namespace SwordsOfExileGame
{
    class OptionButton : Button
    {
        int optionGroup = 0;
        bool nearlyPressed = false;

        public OptionButton(GuiWindow p, PressControlHandler handler, string c, int xb, int yb, int w, int h, int tno, int optgrp)
            : base(p, handler, c, xb, yb, w, h, tno)
        {
            optionGroup = optgrp;
        }

        public void OptionPress(bool and_invoke)
        {
            Pressed = true;
            //Unpress all other buttons in the option group.
            foreach (Control c in parent.controls)
            {
                if (c is OptionButton)
                {
                    OptionButton ob = (OptionButton)c;
                    if (ob.optionGroup == optionGroup && ob.Pressed && ob != this)
                        ob.Pressed = false;
                }

            }

            if (and_invoke && pressButtonFunc != null)
            {
                pressButtonFunc.Invoke(this);
            }
        }

        public override bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible) return false;

            //Is mouse inside bounds of button?
            int dx = X + xOffset, dy = Y + yOffset;
            if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height)
            {
                //Is button pressed?
                if (Gui.LMBHit) { nearlyPressed = true; Sound.ButtonSound(); }
                else if (!Gui.LMBDown && nearlyPressed)
                {
                    if (!Pressed)
                    {
                        Gui.DragItem = null;
                        parent.controlEvent = this;
                        OptionPress(true);
                    }
                    nearlyPressed = false;
                }
                return true;
            }
            else if (nearlyPressed)
            {
                if (!Gui.LMBDown) nearlyPressed = false;
                return true;
            }
            else nearlyPressed = false;
            return false;
        }

        protected override bool DrawAsPressed { get { return Pressed || nearlyPressed; } }
    }
}