using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    class LockpickWindow : GuiWindow
    {
        Location doorPos;
        List<OptionPictureButton> pc_buttons = new List<OptionPictureButton>();
        List<PCType> pcs = new List<PCType>();
        OptionButton bashButton, pickButton;
        Button okButton, cancelButton;
        Label chanceLabel, additionalLabel;
        List<PictureBox> hasLockpicks = new List<PictureBox>();

        public LockpickWindow(Location pos)
            : base(0, 0, 270, 270, true, false, true, true, true)
        {
            doorPos = pos;
            //WorldFreeze = true;
            Position(-2, -2);
            AddLabel("This door is locked. What do you do?", 20, 10, -1, -1, false);

            AddLabel("Choose one of your party:", 20, 30, -1, -1, false);

            XnaRect dr = new XnaRect(20, 50, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);

            XnaRect sr = new XnaRect(0, 0, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);
            foreach (PCType pc in Party.EachAlivePC())
            {
                pc_buttons.Add(AddOptionPictureButton(pressPC, sr, pc.PortraitTexture, dr, 0));
                pcs.Add(pc);
                if (pc.HasItemEquippedWithAbility(eItemAbil.LOCKPICKS)!=null)
                {
                    hasLockpicks.Add(AddPictureBox(Gfx.NewGui, new XnaRect(157, 182, 24, 24), new XnaRect(dr.X, dr.Y + Gfx.PCPORTRAITHEIGHT-6, 18,18)));   
                    hasLockpicks[hasLockpicks.Count - 1].SetStandardToolTip(pc.Name + " has\nlockpicks equipped.");
                }
                dr.X += Gfx.PCPORTRAITWIDTH + 2;
            }

            AddLabel("Choose the action to perform:", 20, 50 + Gfx.CHARGFXHEIGHT + 10, -1, -1, false);

            pickButton = AddOptionButton(pressTactic, "(P)ick the lock.", 20, Gfx.CHARGFXHEIGHT + 80, 1);
            bashButton = AddOptionButton(pressTactic, "(B)ash it down.", 30 + pickButton.Width, Gfx.CHARGFXHEIGHT + 80, 1);
            if (pcs[0].BashDoorChance(doorPos) > pcs[0].PickLockChance(doorPos) || pcs[0].HasItemEquippedWithAbility(eItemAbil.LOCKPICKS) == null)
                bashButton.Pressed = true;
            else pickButton.Pressed = true;

            chanceLabel = AddLabel("", 20, Gfx.CHARGFXHEIGHT + 90 + bashButton.Height, -1, -1, false);
            additionalLabel = AddLabel("", 20, Gfx.CHARGFXHEIGHT + 110 + bashButton.Height, -1, -1, false);
            setChanceInfo();

            cancelButton = AddButton(pressCancel, "Cancel", 200, 0);
            CancelKeyControl = cancelButton;

            okButton = AddButton(pressDoIt, "Do it!", 150, 0);
            OKKeyControl = okButton;

            LineUpControlsRight(InnerWidth - 10, Gfx.CHARGFXHEIGHT + 130 + bashButton.Height, 10, cancelButton, okButton);

            pc_buttons[Party.CurrentPC.Slot].OptionPress(true);
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            base.Draw(sb, partial);
        }


        void setChanceInfo()
        {
            PCType pc = pcs[0];

            for (int n = 0; n < pc_buttons.Count; n++)
                if (pc_buttons[n].Pressed) { pc = pcs[n]; break; }

            int chance = 0;
            if (pickButton.Pressed) 
                chance = pc.PickLockChance(doorPos);
            else 
                chance = pc.BashDoorChance(doorPos);

            chanceLabel.Text = String.Format("Chance of success: {0}%", Math.Max(0, chance));

            if (chance == -1)
                additionalLabel.Text = String.Format("({0} has no lockpicks equipped)", pc.Name);
            else if (chance == -2)
                additionalLabel.Text = "(That is not a door!)";
            else if (chance == -3)
                additionalLabel.Text = "(Impossible to open without the key!)";
            else
                additionalLabel.Text = "";
        }

        void pressCancel(Control button_pressed) { KillMe = true; }

        void pressDoIt(Control button_pressed)
        {
            PCType pc = pcs[0];
            for (int n = 0; n < pc_buttons.Count; n++)
                if (pc_buttons[n].Pressed) { pc = pcs[n]; break; }
            if (bashButton.Pressed)
                pc.BashDoor(doorPos);
            else
                pc.PickLock(doorPos);
            KillMe = true;
        }

        void pressTactic(Control button_pressed)
        {
            setChanceInfo();
        }

        void pressPC(Control button_pressed)
        {
            for (int n = 0; n < pc_buttons.Count; n++)
            {
                if (button_pressed == pc_buttons[n])
                {
                    //Automatically select the option that has the best chance for the PC
                    if (pcs[n].BashDoorChance(doorPos) > pcs[n].PickLockChance(doorPos) || pcs[n].HasItemEquippedWithAbility(eItemAbil.LOCKPICKS) == null)
                    { bashButton.Pressed = true; pickButton.Pressed = false; }
                    else
                    { bashButton.Pressed = false; pickButton.Pressed = true; }

                    setChanceInfo();
                    return;
                }
            }
        }

        public override bool Handle()
        {
            bool interacted = base.Handle();

            var list = KeyHandler.GetAllKeysHit();

            if (list == Keys.None) return interacted;

            if (list >= Keys.D1 && list <= Keys.D6)
                pc_buttons[(int)(list - Keys.D1)].OptionPress(true);
            else if (list == Keys.P)
                pickButton.OptionPress(true);
            else if (list == Keys.B)
                bashButton.OptionPress(true);
            else
                return interacted;
            KeyHandler.FlushHitKey();

            return true;

        }

    }

}