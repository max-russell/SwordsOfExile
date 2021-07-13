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
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    class NewPartyMainWindow : GuiWindow
    {
        Button bPartyName, bAccept, bBack, bSave;
        RichTextBox helpBox;
        int helpPage = 0;

        string[] helpText = {"Here is where you edit your party before beginning the game. You start with 6 prefabricated characters. " +
                             "To replace them with characters of your own, hit the @bDelete@e button and then click the @bAdd New@e button.@n@n" +
                             "Press a character's name to rename her and her picture to pick a new graphic. When you press @bEdit@e, that " +
                             "character's starting skills will appear in the window on the right for you to edit.@n@n" +
                             "You should also give your party a name, by clicking in the box below. This has no effect in the game " +
                             "but it may help keep track of your most successful adventurers as you can save your party after " +
                             "completing a scenario. @n@n" +
                             "@lClick here for the next page >@e",

                             "You start with a set number of @bSkill Points@e to distribute amongst the skills. If you have enough spare skill points, " +
                             "press @b+@e next to a skill to increase that skill, or @b-@e to decrease it and reclaim the skill points to spend " +
                             "elsewhere. Each skill costs a certain number of skill points to upgrade, which is listed next to the skill. Move the mouse " +
                             "over a skill to learn more about it.@n@n" +
                             "@l< Click here for the previous page@e    @lClick here for the next page >@e",
                             
                             "Your character can also have any number of @bTraits@e that affect your character for better of worse. Generally, the more " +
                             "beneficial trait, the greater your @bExperience Modifier@e, which increases how much experience you need to earn " +
                             "before you gain a level. Negative traits have the opposite effect, allowing you to gain levels at a higher rate!@n@n" +
                             "The first trait is always your character's " +
                             "@bRace@e, and must be one of either @bHuman@e, @bNephilim@e, or @bSlithzerikai@e. Click on the race trait in the list " +
                             "to change your race, and click the other traits in the list to remove them. Click @b(Add New)@e to choose a new trait " +
                             "to give your character. Move the mouse over a trait to learn more about it.@n@n" +
                             "@l< Click here for the previous page@e"};

        static NewPartyStatsWindow statsWin;
        static NewPartyWindow partyWin;
        static NewPartyMainWindow mainWin;

        public static PCType DummyPC = new PCType(true,0);

        public NewPartyMainWindow()
            : base(0, 0, 445 + 270 + 1, 327 + 253 + 10, true, false, false, true, false)
        {
            Position(-2, -2);
            Resize(445, 327);

            helpBox = new RichTextBox(this, pressHelp, helpText[0], 10, 10, InnerWidth - 20, 215, -1);
            controls.Add(helpBox);

            if (Party == null) Game.CurrentParty = new PartyType();
            var l = AddLabel("From henceforth your\nadventurers shall be known as:", 10, 225, -1, -1, false);
            bPartyName = AddButton(pressButton, Party.Name, l.X + l.Width + 10, l.Y - 2, 235, 30);
            bPartyName.SetStyle(1);
            bPartyName.SetFont(Gfx.TalkFontNormal, false);

            bAccept = AddButton(pressButton, "Accept Party & Begin Adventuring", 0, 0, -1, 30);
            OKKeyControl = bAccept;
            bBack = AddButton(pressButton, "Back", 0, 0, -1, 30);
            CancelKeyControl = bBack;
            bSave = AddButton(pressButton, "Save Party", 0, 0, -1, 30);
            LineUpControlsRight(InnerWidth - 10, bPartyName.Y + 40, 10, bBack, bSave, bAccept);

            Gfx.LoadPCGraphicsOptions();

            statsWin = new NewPartyStatsWindow(X + 445 + 10, Y);
            partyWin = new NewPartyWindow(X, Y + 327 + 10);
            mainWin = this;


        }

        void pressHelp(int n)
        {
            if (helpPage == 0) helpPage++;
            else if (helpPage == helpText.Length - 1) helpPage--;
            else
                if (n == 0) helpPage--;
                else helpPage++;

            helpBox.FormatText(helpText[helpPage]);
        }

        void pressButton(Control b)
        {
            if (b == bAccept)
            {
                //Get rid of any spaces in the party.
                for (int n = 5; n >= 0; n--)
                {
                    if (Party.PCList[n] == null) Party.PCList.RemoveAt(n);
                }

                ////Pull out graphics for PCs and save them in their own textures

                foreach (PCType pc in Party.PCList)
                    pc.MakePCGraphics();

                Gfx.MakeCharacterHighlight(Party.ActivePC);
                Gfx.PCPortraitGfx = null;
                Gfx.PCGfx = null;

                Game.BeginLoadingThread(true);
                KillMe = true;
            }
            else if (b == bSave)
            {
                foreach (PCType pc in Party.PCList)
                    pc.MakePCGraphics();
                new LoadGameWindow(false, true, true, doSaveParty);
            }
            else if (b == bBack)
            {
                KillMe = true;
                Gfx.PCPortraitGfx = null;
                Gfx.PCGfx = null;
                partyWin.Close();
                statsWin.Close();
                new ScenSelectWindow();
            }
            else if (b == bPartyName)
            {
                new InputTextWindow(nameChange, "Enter new name:", Party.Name, false);
            }
        }

        void doSaveParty(int option, string filename)
        {
            if (option == LoadGameWindow.SAVE)
            {
                Game.SaveGame(filename, true);
            }
        }

        void nameChange(string new_name)
        {
            if (new_name == null || new_name == "") return;
            Party.Name = new_name;
            bPartyName.Caption = Party.Name;
            Refresh();
        }

        public static void Refresh()
        {
            if (Game.CurrentParty.CurrentPC == null || Game.CurrentParty.CurrentPC == DummyPC) Game.CurrentParty.CurrentPC = Game.CurrentParty.LeaderPC;
            if (Game.CurrentParty.CurrentPC == null) Game.CurrentParty.CurrentPC = DummyPC;

            bool nopcs = true;
            foreach (PCType pc in Game.CurrentParty.PCList)
            {
                if (pc != null) { nopcs = false; break; }
            }
            mainWin.bAccept.Enabled = mainWin.bSave.Enabled = !nopcs;

            partyWin.Refresh();
            statsWin.Refresh();
        }
    }

    class NewPartyStatsWindow : GuiWindow
    {
        RichTextBox traitsBox;
        Label skillPtsLbl, expModLbl;

        Trait traitTemp;


        public NewPartyStatsWindow(int x, int y)
            : base(x, y, 270, 590, true, false, false, true, false)
        {

            int rside = 10;

            var c = new Control[19];

            Label l = new Label(this, "Skill                       Cost               Level", rside, 22, -1, -1, false, -1);
            l.Font = Gfx.ItalicFont;
            controls.Add(l);

            for (int n = 0; n <= 18; n++)
            {
                c[n] = new StatControl(this, 0, 0, -1, (eSkill)n, true, true);
                controls.Add(c[n]);
            }

            LineUpControlsDown(rside, l.Y + l.Height + 2, 1, c);/*controls[0], controls[1], controls[2], controls[3],
                                           controls[4], controls[5], controls[6], controls[7],
                                           controls[8], controls[9], controls[10], controls[11],
                                           controls[12], controls[13], controls[14], controls[15],
                                           controls[16], controls[17], controls[18]*/

            var cn = new StatControl(this, rside, c[18].Y + 19, -1, eSkill.HEALTH, true, true);
            controls.Add(cn);

            cn = new StatControl(this, rside, cn.Y + 19, -1, eSkill.SPELLPTS, true, true);
            controls.Add(cn);

            skillPtsLbl = new Label(this, "Skill Points Remaining: ", rside, cn.Y + 24, -1, -1, false, -1);
            skillPtsLbl.Font = Gfx.SmallBoldFont; skillPtsLbl.TextColour = Color.LightGray;
            controls.Add(skillPtsLbl);

            expModLbl = new Label(this, "Experience Modifier:", rside, skillPtsLbl.Y + 18, -1, -1, false, -1);
            expModLbl.Font = Gfx.SmallBoldFont; expModLbl.TextColour = Color.LightGray;
            controls.Add(expModLbl);

            //expLbl = new Label(this, "Exp: ", 10, goldLbl.Y + 15, -1, -1, false, -1);
            //expLbl.Font = Gfx.SmallBoldFont; expLbl.TextColour = Color.LightGray;
            //controls.Add(expLbl);

            //expNextLbl = new Label(this, "To Next:", 100, goldLbl.Y + 15, -1, -1, false, -1);
            //expNextLbl.Font = Gfx.SmallBoldFont; expNextLbl.TextColour = Color.LightGray;
            //controls.Add(expNextLbl);

            traitsBox = new RichTextBox(this, pressTrait, rside, expModLbl.Y + 18, 246, 35, -1);
            traitsBox.SetFonts(1);
            traitsBox.FormatText(makeTraitString());
            controls.Add(traitsBox);
        }

        void pressTrait(int n)
        {
            if (n == 0)
            {
                //Clicked on the Race link, which allows you to change the race of the character.
                new MessageWindow(changeRace, "@bSelect your character's species:@e\n\n" +
                                        "@bHUMAN:@e " + Trait.Human.Description + "@n@iExperience handicap 0%@e\n\n" +
                                        "@bNEPHILIM:@e " + Trait.Nephilim.Description + "@n@iExperience handicap 12%@e\n\n" +
                                        "@bSLITHERZAKAI:@e " + Trait.Slitherzakai.Description + "@n@iExperience handicap 20%@e",
                                        eDialogPic.NONE, 0, "Human", "Nephilim", "Slithzerikai");
            }

            else if (n == Party.CurrentPC.Traits.Count)
                new AddTraitWindow(Party.CurrentPC, NewPartyMainWindow.Refresh);
            else
            {
                new MessageWindow(removeTrait, "Do you want to remove the trait '" + Party.CurrentPC.Traits[n].Name + "' from this character?", eDialogPic.NONE, 0, "Yes", "No");
                traitTemp = Party.CurrentPC.Traits[n];
            }
        }

        void removeTrait(int n)
        {
            if (n == 1) return;
            Party.CurrentPC.Traits.Remove(traitTemp);
            NewPartyMainWindow.Refresh();
        }

        void changeRace(int n)
        {
            if (n == 0)
                Party.CurrentPC.Traits[0] = Trait.Human;
            else if (n == 1)
                Party.CurrentPC.Traits[0] = Trait.Nephilim;
            else if (n == 2)
                Party.CurrentPC.Traits[0] = Trait.Slitherzakai;
            NewPartyMainWindow.Refresh();
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
                sb.Append("@l@6@[" + t.Description + "@n@n@bExperience Handicap: " + t.Handicap + "%@]");
                sb.Append(t.Name);
                sb.Append("@e");
            }

            if (Party.CurrentPC.Traits.Count < Trait.MaxCanHave)
                sb.Append(", @l(Add New)@e");

            return sb.ToString();
        }

        public void Refresh()
        {
            traitsBox.FormatText(Party.CurrentPC == null ? "" : makeTraitString());
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            if (!Visible) return;
            base.Draw(sb, partial);

            Vector2 wpos = GetClientAreaPos();
            sb.Draw(Gfx.StatAreaGfx, wpos, new XnaRect(0, 116, 250, 17), Color.White);

            if (Party.CurrentPC != null)
            {
                sb.DrawString(Gfx.SmallBoldFont, "Editing " + Party.CurrentPC.Name + ":", wpos + new Vector2(3, 1), Color.White);
                int y = Y + Gfx.FRAME_HEIGHT;// +skillPtsLbl.Y;
                int x = X + Gfx.FRAME_WIDTH;
                sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.SkillPoints), new Vector2(x + 150, y + skillPtsLbl.Y), Color.White);
                sb.DrawString(Gfx.SmallBoldFont, Party.CurrentPC.GetExperienceModifier() + "%", new Vector2(x + 150, y + expModLbl.Y), Color.White);
            }
            //sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.Gold), new Vector2(x + 170, y + skillPtsLbl.Y), Color.White);
        }

    }

    class NewPartyWindow : GuiWindow
    {
        PictureButton[] portraitPic;
        PictureButton[] fullPic;
        OptionButton[] editPCButton;
        Button[] pcName, deletePCButton, addPCButton;

        PCType pcTemp;

        public NewPartyWindow(int x, int y)
            : base(x, y, 445/*523*/, 253, true, false, false, true, false)
        {
            portraitPic = new PictureButton[6];
            pcName = new Button[6];
            fullPic = new PictureButton[6];
            editPCButton = new OptionButton[6];
            deletePCButton = new Button[6];
            addPCButton = new Button[6];
            for (int n = 0; n < 6; n++)
            {
                PCType pc = Game.CurrentParty.PCList[n];
                portraitPic[n] = AddPictureButton(pressPortrait, 
                    getPortraitRect(pc), 
                    Gfx.PCPortraitGfx, 
                    new XnaRect(0, 0, 64, 64));
                fullPic[n] = AddPictureButton(pressPic, 
                    getGraphicRect(pc),
                    Gfx.PCGfx, 
                    new XnaRect(0, 0, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT));
                pcName[n] = AddButton(pressName, pc.Name, 84, 0, 120, 20);
                pcName[n].SetStyle(1);
                editPCButton[n] = AddOptionButton(pressEditPC, "Edit", 170, 0, 0);
                deletePCButton[n] = AddButton(pressDeletePC, "Delete", 120, 0);
                addPCButton[n] = AddButton(pressAddPC, "Create New Character", 0, 0, 120);
            }
            LineUpControlsDown(10, 10, 10, portraitPic[0], portraitPic[1], portraitPic[2]);
            LineUpControlsDown(220, 10, 10, portraitPic[3], portraitPic[4], portraitPic[5]);

            for (int n = 0; n < 6; n++)
            {
                //pcName[n].Y = portraitPic[n].Y;
                pcName[n].Position(portraitPic[n].X + 74, portraitPic[n].Y, -1, -1);
                //addPCButton[n].Y = pcName[n].Y + 6;
                addPCButton[n].Position(portraitPic[n].X + 74, portraitPic[n].Y, -1, -1);

                //fullPic[n].Y = pcName[n].Y + pcName[n].Height+6;
                //fullPic[n].X = pcName[n].X;
                fullPic[n].Position(pcName[n].X, pcName[n].Y + pcName[n].Height + 6, -1, -1);

                //editPCButton[n].Y = deletePCButton[n].Y = fullPic[n].Y + 4;
                editPCButton[n].Position(portraitPic[n].X + 160, fullPic[n].Y + 4, -1, -1);

                deletePCButton[n].Resize(editPCButton[n].Width + 10, editPCButton[n].Height);
                //deletePCButton[n].X = editPCButton[n].X - deletePCButton[n].Width - 5;
                deletePCButton[n].Position(editPCButton[n].X - deletePCButton[n].Width - 5, fullPic[n].Y + 4, -1, -1);

                addPCButton[n].Visible = false;
            }
            editPCButton[0].Pressed = true;

            //var l = AddLabel("Your adventurers are known as:", 10, portraitPic[5].Y + 74, -1, -1, false);
            //partyName = AddButton(pressPartyName, Party.Name, 10, l.Y + 20, 200, 20);
            //partyName.SetStyle(1);

            //Accept = AddButton(pressButton, "Finish", 10, partyName.Y + 30);
            //Back = AddButton(pressButton, "Back", 0, 0);
            //LineUpControls(10, partyName.Y + 30, 10, Back, Accept);

            //int rside = 250;

            //var c = new Control[19];

            //l = new Label(this, "Skill                       Cost               Level", rside, 22, -1, -1, false, -1);
            //l.Font = Gfx.ItalicFont;
            //controls.Add(l);

            //for (int n = 0; n <= 18; n++)
            //{
            //    c[n] = new StatControl(this, 0, 0, -1, (eSkill)n, true, true);
            //    controls.Add(c[n]);
            //}

            //LineUpControlsDown(rside, l.Y + l.Height + 2, 1, c);/*controls[0], controls[1], controls[2], controls[3],
            //                               controls[4], controls[5], controls[6], controls[7],
            //                               controls[8], controls[9], controls[10], controls[11],
            //                               controls[12], controls[13], controls[14], controls[15],
            //                               controls[16], controls[17], controls[18]*/

            //var cn = new StatControl(this, rside, c[18].Y + 19, -1, eSkill.HEALTH, true, true);
            //controls.Add(cn);

            //cn = new StatControl(this, rside, cn.Y + 19, -1, eSkill.SPELLPTS, true, true);
            //controls.Add(cn);

            //skillPtsLbl = new Label(this, "Skill Points Remaining: ", rside, cn.Y + 24, -1, -1, false, -1);
            //skillPtsLbl.Font = Gfx.SmallBoldFont; skillPtsLbl.TextColour = Color.LightGray;
            //controls.Add(skillPtsLbl);

            //expModLbl = new Label(this, "Experience Modifier:", rside, skillPtsLbl.Y + 18, -1, -1, false, -1);
            //expModLbl.Font = Gfx.SmallBoldFont; expModLbl.TextColour = Color.LightGray;
            //controls.Add(expModLbl);

            //traitsBox = new RichTextBox(this, pressTrait, rside, expModLbl.Y + 18, 246, 35, -1);
            //traitsBox.SetFonts(1);
            //traitsBox.FormatText(makeTraitString());
            //controls.Add(traitsBox);


            //Position(-2, -2);
        }

        //void pressButton(Button b)
        //{
        //    if (b == Accept)
        //    {
        //        //Get rid of any spaces in the party.
        //        for (int n = 5; n >= 0; n--)
        //        {
        //            if (Party.PCList[n] == null) Party.PCList.RemoveAt(n);
        //        }
        //        Game.BeginLoadingThread();
        //        KillMe = true;
        //    }
        //    else if (b == Back)
        //    {
        //        KillMe = true;
        //        new ScenSelectWindow();
        //    }

        //}

        //void pressPartyName(Button b)
        //{
        //    pcTemp = null;
        //    new InputTextWindow(nameChange, "Enter new name:", Party.Name, false);
        //}

        void pressPortrait(Control b)
        {
            for (int n = 0; n < 6; n++)
                if (b == portraitPic[n])
                {
                    if (Party.PCList[n] == null) return;
                    pcTemp = Party.PCList[n];

                    new ChoosePictureWindow(EachPortraitGraphic, Gfx.PCPortraitGfx, Party.PCList[n].Portrait, changePortrait);
                    //(Gfx.FacesGfx, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT, Party.PCList[n].Portrait, changePortrait);
                }
        }

        IEnumerable<XnaRect> EachPortraitGraphic()
        {
            int h = Gfx.PCPortraitGfx.Height / Gfx.PCPORTRAITHEIGHT, w = Gfx.PCPortraitGfx.Width / Gfx.PCPORTRAITHEIGHT;
            for (int y = 0; y < h; y++)
                for (int x = 0; x < w; x++)
                {
                    yield return new XnaRect(x * Gfx.PCPORTRAITWIDTH, y * Gfx.PCPORTRAITHEIGHT, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);
                }
        }


        void pressName(Control b)
        {
            for (int n = 0; n < 6; n++)
                if (b == pcName[n])
                {
                    pcTemp = Party.PCList[n];
                    new InputTextWindow(nameChange, "Enter new name:", pcTemp.Name, false);
                    break;
                }
        }
        void pressPic(Control b)
        {
            for (int n = 0; n < 6; n++)
                if (b == fullPic[n])
                {
                    if (Party.PCList[n] == null) return;
                    pcTemp = Party.PCList[n];

                    new ChoosePictureWindow(EachPCGraphic, Gfx.PCGfx, Party.PCList[n].which_graphic, changePicture);
                    //(Gfx.FacesGfx, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT, Party.PCList[n].Portrait, changePortrait);
                }
        }
        IEnumerable<XnaRect> EachPCGraphic()
        {
            int y = 0;
            while (y < Gfx.PCGfx.Height)
            {
                yield return new XnaRect(0, y, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
                y += Gfx.CHARGFXHEIGHT;
            }

            //for (int a = 0; a < 36; a++)
            //    yield return new XnaRect(//(a / 8) * Gfx.CHARGFXWIDTH * 2,
            //                 (a % 8) * Gfx.CHARGFXHEIGHT,
            //                 Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
        }


        void pressEditPC(Control b)
        {
            for (int n = 0; n < 6; n++)
                if (b == editPCButton[n])
                {
                    Game.CurrentParty.CurrentPC = Game.CurrentParty.PCList[n];
                    NewPartyMainWindow.Refresh();
                    break;
                }
        }
        void pressDeletePC(Control b)
        {
            for (int n = 0; n < 6; n++)
                if (b == deletePCButton[n])
                {
                    pcTemp = Party.PCList[n];
                    new MessageWindow(confirmDelete, "Are you sure you want to delete " + pcTemp.Name + "?", eDialogPic.FACE, pcTemp.Portrait, "Yes", "No");
                    break;
                }
        }
        void pressAddPC(Control b)
        {
            for (int n = 0; n < 6; n++)
                if (b == addPCButton[n])
                {
                    Party.PCList[n] = new PCType(false,n);
                    Party.CurrentPC = Party.PCList[n];
                    NewPartyMainWindow.Refresh();
                    break;
                }
        }

        //void pressTrait(int n)
        //{
        //    if (n == 0)
        //    {
        //        //Clicked on the Race link, which allows you to change the race of the character.
        //        new MessageWindow(changeRace, "@bSelect your character's species:@e\n\n" +
        //                                "@bHUMAN:@e " + Trait.Human.Description + "@n@iExperience handicap 0%@e\n\n" +
        //                                "@bNEPHILIM:@e " + Trait.Nephilim.Description + "@n@iExperience handicap 12%@e\n\n" +
        //                                "@bSLITHZERIKAI:@e " + Trait.Slitherzakai.Description + "@n@iExperience handicap 20%@e",
        //                                eDialogPic.NONE, 0, "Human", "Nephilim", "Slithzerikai");
        //    }

        //    else if (n == Party.CurrentPC.Traits.Count)
        //        new AddTraitWindow(Party.CurrentPC, refreshPartyDisplay);
        //    else
        //    {
        //        new MessageWindow(removeTrait, "Do you want to remove the trait '" + Party.CurrentPC.Traits[n].Name + "' from this character?", eDialogPic.NONE, 0, "Yes", "No");
        //        traitTemp = Party.CurrentPC.Traits[n];
        //    }
        //}

        //void removeTrait(int n)
        //{
        //    if (n == 1) return;
        //    Party.CurrentPC.Traits.Remove(traitTemp);
        //    refreshPartyDisplay();
        //}

        void changePortrait(int n)
        {
            pcTemp.Portrait = n;
            NewPartyMainWindow.Refresh();
        }
        void changePicture(int n)
        {
            pcTemp.which_graphic = n;
            NewPartyMainWindow.Refresh();
        }

        //void changeRace(int n)
        //{
        //    if (n == 0)
        //        Party.CurrentPC.Traits[0] = Trait.Human;
        //    else if (n == 1)
        //        Party.CurrentPC.Traits[0] = Trait.Nephilim;
        //    else if (n == 2)
        //        Party.CurrentPC.Traits[0] = Trait.Slitherzakai;
        //    refreshPartyDisplay();
        //}

        void nameChange(string new_name)
        {
            if (new_name == null || new_name == "") return;

            //if (pcTemp == null)
            //    Party.Name = new_name;
            //else
            pcTemp.Name = new_name;

            NewPartyMainWindow.Refresh();
        }

        void confirmDelete(int option)
        {
            if (option == 0)
            {
                if (Party.PCList[pcTemp.Slot] == Party.CurrentPC)
                    Party.CurrentPC = null;
                Party.PCList[pcTemp.Slot] = null;

                NewPartyMainWindow.Refresh();
            }
        }

        public void Refresh()
        {
            if (Party.CurrentPC != null && Party.CurrentPC != NewPartyMainWindow.DummyPC)
                editPCButton[Party.CurrentPC.Slot].OptionPress(false);

            for (int n = 0; n < 6; n++)
            {
                if (Party.PCList[n] == null)
                {
                    pcName[n].Visible = false;
                    editPCButton[n].Visible = false;
                    deletePCButton[n].Visible = false;
                    fullPic[n].Visible = false;
                    addPCButton[n].Visible = true;
                    portraitPic[n].SetPicture(Gfx.NewGui, new XnaRect(134, 147, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT));
                }
                else
                {
                    pcName[n].Visible = true;
                    editPCButton[n].Visible = true;
                    deletePCButton[n].Visible = true;
                    fullPic[n].Visible = true;
                    addPCButton[n].Visible = false;
                    PCType pc = Party.PCList[n];
                    pcName[n].Caption = pc.Name;
                    portraitPic[n].SetPicture(Gfx.PCPortraitGfx, getPortraitRect(pc));
                    fullPic[n].SetPicture(Gfx.PCGfx, getGraphicRect(pc));
                }
            }

            //partyName.Caption = Party.Name;
            //traitsBox.FormatText(Party.CurrentPC == null ? "" : makeTraitString());

        }

        XnaRect getGraphicRect(PCType pc)
        {
            return new XnaRect(0, pc.which_graphic * Gfx.CHARGFXHEIGHT, Gfx.CHARGFXWIDTH, Gfx.CHARGFXHEIGHT);
        }

        XnaRect getPortraitRect(PCType pc)
        {
            return new XnaRect((pc.Portrait % 10) * 32, (pc.Portrait / 10) * 32, 32, 32);
        }


        //string makeTraitString()
        //{
        //    var sb = new StringBuilder();
        //    sb.Append("@bTRAITS:@e ");
        //    bool first = true;
        //    foreach (Trait t in Party.CurrentPC.Traits)
        //    {
        //        if (!first) sb.Append(", ");
        //        first = false;
        //        sb.Append("@l@6[" + t.Description + "@n@n@bExperience Handicap: " + t.Handicap + "%]");
        //        sb.Append(t.Name);
        //        sb.Append("@e");
        //    }

        //    if (Party.CurrentPC.Traits.Count < Trait.MAX_TRAITS)
        //        sb.Append(", @l(Add New)@e");

        //    return sb.ToString();
        //}

        //public override void Draw(SpriteBatch sb, int partial = 0)
        //{
        //    if (!Visible) return;
        //    base.Draw(sb, partial);

        //    Vector2 wpos = GetClientAreaPos();
        //    sb.Draw(Gfx.StatAreaGfx, wpos + new Vector2(250,0), new XnaRect(0, 116, 250, 17), Color.White);

        //    if (Party.CurrentPC != null)
        //    {
        //        sb.DrawString(Gfx.SmallBoldFont, "Editing " + Party.CurrentPC.Name + ":", wpos + new Vector2(253, 1), Color.White);
        //        int y = Y + Gfx.FRAME_HEIGHT;// +skillPtsLbl.Y;
        //        int x = X + Gfx.FRAME_WIDTH;
        //        sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.CurrentPC.SkillPoints), new Vector2(x + 400, y + skillPtsLbl.Y), Color.White);
        //        sb.DrawString(Gfx.SmallBoldFont, Party.CurrentPC.GetExperienceModifier() + "%", new Vector2(x + 400, y + expModLbl.Y), Color.White);
        //    }
        //    //sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(Party.Gold), new Vector2(x + 170, y + skillPtsLbl.Y), Color.White);
        //}

    }

}