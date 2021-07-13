using System;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{

    class StatsWindow : GuiWindow
    {
        static StatsWindow instance;

        public static void Reveal(PCType pc)
        {
            if (pc == Game.CurrentParty.CurrentPC && instance.Visible == true)
                instance.Visible = false;
            else
            {
                instance.Visible = true;
                Gui.BringToFront(instance);
            }
        }
        public static void Update()
        {
            if (instance == null) return;
            instance.traitsBox.FormatText(instance.makeTraitString());
        }

        public new static void Close()
        {
            if (instance != null) instance.Visible = false;
            instance = null;
        }

        RichTextBox traitsBox;
        Label skillPtsLbl, goldLbl, expLbl, expNextLbl, encumbranceLbl;//, weap1Lbl, weap2Lbl;

        public StatsWindow()
            : base(140, 30, 240, 500, true, true, false, true, true)
        {
            instance = this;
            var c = new Control[19];

            var l = new Label(this, "Skill                       Cost    Gold    Level", 10, 27, -1, -1, false, -1);
            l.Font = Gfx.ItalicFont;
            controls.Add(l);

            for (int n = 0; n <= 18; n++)
            {
                c[n] = new StatControl(this, 10, 10, -1, (eSkill)n, false, false);
                controls.Add(c[n]);
            }

            LineUpControlsDown(10, l.Y + l.Height + 4, 1, c);

            var cn = new StatControl(this, 10, c[18].Y + 26, -1, eSkill.HEALTH, false, false);
            controls.Add(cn);

            cn = new StatControl(this, 10, cn.Y + 19, -1, eSkill.SPELLPTS, false, false);
            controls.Add(cn);

            skillPtsLbl = new Label(this, "Skill Points: ", 10, cn.Y + 24, -1, -1, false, -1);
            skillPtsLbl.Font = Gfx.SmallBoldFont; skillPtsLbl.TextColour = Color.LightGray;
            controls.Add(skillPtsLbl);
            skillPtsLbl.SetStandardToolTip("You earn skill points every time you gain a level. Seek out a trainer to spend them on improving your skills.",200);

            goldLbl = new Label(this, "Gold:", 135, cn.Y + 24, -1, -1, false, -1);
            goldLbl.Font = Gfx.SmallBoldFont; goldLbl.TextColour = Color.LightGray;
            controls.Add(goldLbl);
            goldLbl.SetStandardToolTip("The gold your party has collected. Spend it on items and spells in shops, or to improve your skills with a trainer.", 200);

            expLbl = new Label(this, "Exp: ", 10, goldLbl.Y + 15, -1, -1, false, -1);
            expLbl.Font = Gfx.SmallBoldFont; expLbl.TextColour = Color.LightGray;
            controls.Add(expLbl);
            expLbl.SetStandardToolTip("The amount of experience your character has accrued since they last gained a level.", 200);

            expNextLbl = new Label(this, "To Next:", 100, goldLbl.Y + 15, -1, -1, false, -1);
            expNextLbl.Font = Gfx.SmallBoldFont; expNextLbl.TextColour = Color.LightGray;
            controls.Add(expNextLbl);
            expNextLbl.SetStandardToolTip("The amount of experience your character needs to advance to the next level.", 200);

            encumbranceLbl = new Label(this, "Encumbrance:", 10, expLbl.Y + 15, -1, -1, false, -1);
            encumbranceLbl.SetStandardToolTip("Your encumbrance rating is increased by wearing heavy armour and decreased by the Defence skill. Encumbrance slows you down and makes it harder to hit enemies in combat. Wearing armor with a total encumbrance of more that 1 spoils any mage spell you try to cast in combat. High defense skill sometimes prevents this from happening, but it will only go so far. If any single item has encumb. higher than 2, spells always fail.",200);
            encumbranceLbl.Font = Gfx.SmallBoldFont; 
            encumbranceLbl.TextColour = Color.LightGray;
            controls.Add(encumbranceLbl);

            traitsBox = new RichTextBox(this, null, 10, encumbranceLbl.Y + 18, 226, 80, -1);
            traitsBox.SetFonts(1);
            traitsBox.FormatText(makeTraitString());

            controls.Add(traitsBox);
            InnerHeight = traitsBox.Y + traitsBox.Height + 4;

            Visible = false;
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            if (!Visible) return;
            base.Draw(sb, partial);

            Vector2 wpos = GetClientAreaPos();
            sb.Draw(Gfx.StatAreaGfx, wpos, new XnaRect(0, 116, InnerWidth, 17), Color.White);
            sb.DrawString(Gfx.SmallBoldFont, Party.CurrentPC.Name + " (Level " + Party.CurrentPC.Level + ")", wpos + new Vector2(3, 1), Color.White);

            int y = Y + Gfx.FRAME_HEIGHT;
            int x = X + Gfx.FRAME_WIDTH;

            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.SkillPoints), new Vector2(x + 80, y + skillPtsLbl.Y), Color.White);
            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.Gold), new Vector2(x + 170, y + skillPtsLbl.Y), Color.White);

            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.LevelExperience), new Vector2(x + 40, y + expLbl.Y), Color.White);
            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.ExperienceToNextLevel), new Vector2(x + 150, y + expLbl.Y), Color.White);

            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.TotalEncumbrance), new Vector2(x + 100, y + encumbranceLbl.Y), Color.White);
        }

        string makeTraitString()
        {
            var sb = new StringBuilder();
            sb.Append("@bTRAITS:@e ");
            bool first = true;
            foreach (Trait t in Party.CurrentPC.Traits)
            {
                if (!first) sb.Append(", ");
                first = false;
                sb.Append("@6@[" + t.Description + "@n@n@bExperience Handicap: " + t.Handicap + "%@]");
                sb.Append(t.Name);
                sb.Append("@e");
            }
            return sb.ToString();
        }

        protected override void pressWindowClose(Control button_pressed)
        {
            Visible = false;
        }
    }

}