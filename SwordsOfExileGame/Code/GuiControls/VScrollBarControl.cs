using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    public interface IScrollBarOwner
    {
        void ScrollBarUpdate(int pos);
    }

    class VScrollBar : Control
    {
        Control Owner;

        int pos, extend, min, max, Change;
        int YOffset;

        enum eButton { NONE, UP, DOWN, BAR };

        eButton pressedButton = eButton.NONE;

        /// <summary>
        /// Make a new scroll bar.
        /// </summary>
        /// <param name="owner">The control to which the scroll bar is attached and interacts with. It always sticks to the right hand side of this control</param>
        /// <param name="window">The window the control (and parent) is on.</param>
        /// <param name="_pos">The starting value in the scroll bar</param>
        /// <param name="_extend">The size of the moveable bar section. If this is more than (max - min) the scroll bar disappears.</param>
        /// <param name="_min">The minimum value</param>
        /// <param name="_max">The maximum value</param>
        public VScrollBar(IScrollBarOwner owner, GuiWindow window, int yoffset, int height, int _pos, int _extend, int _min, int _max, int change)
            : base(window, 0, 0, 0, 0, -1)
        {
            Owner = (Control)owner;
            X = Owner.X + Owner.Width;
            YOffset = yoffset;
            Y = Owner.Y + YOffset;
            Width = 16;
            Height = height;
            ChangeValues(_pos, _extend, _min, _max, change);
            window.controls.Add(this);
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;

            int dx = X + xOffset, dy = Y + yOffset;

            Color col;

            //Up bottom
            if (!Enabled || pos <= min) col = Color.DarkGray; else if (pressedButton == eButton.UP) col = Color.Red; else col = Color.White;
            sb.Draw(Gfx.NewGui, new XnaRect(dx, dy, 16, 16), new XnaRect(156, 209, 16, 16), col);

            //Bottom button
            if (!Enabled || pos + extend >= max) col = Color.DarkGray;
            else if (pressedButton == eButton.DOWN) col = Color.Red; else col = Color.White;
            sb.Draw(Gfx.NewGui, new XnaRect(dx, dy + Height - 16, 16, 16), new XnaRect(156, 225, 16, 16), col);

            //Bar background
            Gfx.DrawRect(dx, dy + 16, 16, Height - 32, Color.Black);

            //Bar
            if (Enabled)
            {
                float barh = Height - 32;
                float g1 = ((float)pos / (float)max) * barh;
                float g2 = ((float)extend / (float)max) * barh;
                Gfx.DrawRect(dx, (int)(dy + 16 + g1), 16, (int)g2, Color.DarkGray);
            }
        }

        public override bool Handle(int xOffset, int yOffset)
        {

            if (!Visible || !Enabled) return false;
            X = Owner.X + Owner.Width;
            Y = Owner.Y + YOffset;

            int dx = X + xOffset, dy = Y + yOffset;
            bool interacted = false;

            if (Gui.Ms.X >= dx && Gui.Ms.X < dx + 16 && Gui.Ms.Y >= dy && Gui.Ms.Y < dy + Height)
            {
                if (Gui.Ms.Y < dy + 16) //Up button
                {
                    if (Gui.LMBHit)
                    {
                        pressedButton = eButton.UP;
                        interacted = true;
                    }
                    else if (!Gui.LMBDown && pressedButton == eButton.UP)
                    {
                        Sound.ButtonSound();
                        pos = Maths.Max(pos - Change, min);
                        interacted = true;
                        pressedButton = eButton.NONE;
                    }
                }
                else if (Gui.Ms.Y >= dy + Height - 16) //Down button
                {
                    if (Gui.LMBHit)
                    {
                        pressedButton = eButton.DOWN;
                        interacted = true;
                    }
                    else if (!Gui.LMBDown && pressedButton == eButton.DOWN)
                    {
                        Sound.ButtonSound();
                        pos = Maths.Min(pos + Change, max - extend);
                        interacted = true;
                        pressedButton = eButton.NONE;
                    }
                }
                else //Bar
                {
                    if (Gui.LMBDown)
                    {
                        pressedButton = eButton.BAR;
                        float mpos = (float)(Gui.Ms.Y - dy - 16) / (float)(Height - 32);
                        ChangeValues((int)((float)(max - min) * mpos) + min - extend / 2, extend, min, max, Change);
                        interacted = true;
                    }
                }
            }
            else
            {
                if (Gui.LMBDown && pressedButton == eButton.BAR)
                {
                    float mpos = (float)(Gui.Ms.Y - dy - 16) / (float)(Height - 32);
                    if (mpos < 0) mpos = 0; if (mpos > 1) mpos = 1;
                    ChangeValues((int)((float)(max - min) * mpos) + min - extend / 2, extend, min, max, Change);
                    interacted = true;
                }
                else
                    pressedButton = eButton.NONE;
            }

            ((IScrollBarOwner)Owner).ScrollBarUpdate(pos);
            return interacted;
        }

        public int ChangeValues(int _pos, int _extend, int _min, int _max, int change)
        {
            pos = _pos; extend = _extend; min = _min; max = _max;

            if (extend >= max - min)
            {
                extend = max - min;
                Enabled = false;
            }
            else 
                Enabled = true;
            if (pos < min) pos = min;
            if (pos + extend > max) pos = max - extend;
            Change = change;
            return pos;
        }

    }
}