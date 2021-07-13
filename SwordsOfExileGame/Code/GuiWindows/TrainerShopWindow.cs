using System;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    class TrainerWindow : GuiWindow
    {
        static TrainerWindow instance;

        Label skillPtsLbl, goldLbl, expLbl, expNextLbl;
        ConversationWindow cameFrom;

        public TrainerWindow(ConversationWindow from)
            : base(220, 30, 268, 500, true, true, false, true, true)
        {
            Action.LockActions = eAction.MAGIC_LOCK_ACTIONS; //Don't pause the world, but prevent the player doing anything not inventory related
            instance = this;
            cameFrom = from;
            var c = new Control[19];

            var l = new Label(this, "Skill                       Cost    Gold    Level", 10, 27, -1, -1, false, -1);
            l.Font = Gfx.ItalicFont;
            controls.Add(l);

            for (int n = 0; n <= 18; n++)
            {
                c[n] = new StatControl(this, 10, 10, -1, (eSkill)n, true, false);
                controls.Add(c[n]);
            }

            LineUpControlsDown(10, l.Y + l.Height + 4, 1, c);

            var cn = new StatControl(this, 10, c[18].Y + 26, -1, eSkill.HEALTH, true, false);
            controls.Add(cn);

            cn = new StatControl(this, 10, cn.Y + 19, -1, eSkill.SPELLPTS, true, false);
            controls.Add(cn);

            skillPtsLbl = new Label(this, "Skill Points: ", 10, cn.Y + 24, -1, -1, false, -1);
            skillPtsLbl.Font = Gfx.SmallBoldFont; skillPtsLbl.TextColour = Color.LightGray;
            controls.Add(skillPtsLbl);

            goldLbl = new Label(this, "Gold:", 135, cn.Y + 24, -1, -1, false, -1);
            goldLbl.Font = Gfx.SmallBoldFont; goldLbl.TextColour = Color.LightGray;
            controls.Add(goldLbl);

            expLbl = new Label(this, "Exp: ", 10, goldLbl.Y + 15, -1, -1, false, -1);
            expLbl.Font = Gfx.SmallBoldFont; expLbl.TextColour = Color.LightGray;
            controls.Add(expLbl);

            expNextLbl = new Label(this, "To Next:", 100, goldLbl.Y + 15, -1, -1, false, -1);
            expNextLbl.Font = Gfx.SmallBoldFont; expNextLbl.TextColour = Color.LightGray;
            controls.Add(expNextLbl);

            var b = new Button(this, pressFinish, "Finish Training", 0, 0, -1, -1, -1);
            b.Position(-10, 10, 1, 1);
            b.Y = expNextLbl.Y + expNextLbl.Height + 10;
            controls.Add(b);
            OKKeyControl = b;
            CancelKeyControl = b;

            InnerHeight = b.Y + b.Height + 4;
            Position(-2, -2);
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            if (!Visible) return;
            base.Draw(sb, partial);

            Vector2 wpos = GetClientAreaPos();
            sb.Draw(Gfx.StatAreaGfx, wpos, new XnaRect(0, 116, InnerWidth, 17), Color.White);
            sb.DrawString(Gfx.SmallBoldFont, "Training: " + Party.CurrentPC.Name + " (Level " + Party.CurrentPC.Level + ")", wpos + new Vector2(3, 1), Color.White);

            int y = Y + Gfx.FRAME_HEIGHT;
            int x = X + Gfx.FRAME_WIDTH;

            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.SkillPoints), new Vector2(x + 80, y + skillPtsLbl.Y), Color.White);
            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.Gold), new Vector2(x + 170, y + skillPtsLbl.Y), Color.White);

            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.LevelExperience), new Vector2(x + 40, y + expLbl.Y), Color.White);
            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.ExperienceToNextLevel), new Vector2(x + 150, y + expLbl.Y), Color.White);

        }

        void pressFinish(Control b)
        {
            KillMe = true;
        }

        public override void Close()
        {
            base.Close();
            if (cameFrom != null)
            {
                cameFrom.Visible = true;
            }
            Action.LockActions = eAction.NONE;
        }
    }

}