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
    class ScenSelectWindow : GuiWindow
    {
        ListBox scenList;
        RichTextBox scenInfoBox;
        Label scenTitle;
        PictureBox scenPic;
        Button btnBack, btnNewParty, btnLoadParty;


        public ScenSelectWindow()
            : base(0, 0, 700, 500, true, false, true, true, false)
        {
            scenList = AddListBox(changeScenario, 10, 10, 250, 460, 0);

            scenTitle = AddLabel("", 356, 22, 302, 64, false);
            scenTitle.BackColour = Color.Black;
            scenTitle.Font = Gfx.TalkFontNormal;
            scenTitle.Padding = 4;

            scenPic = AddPictureBox(Gfx.ScenarioGfx, new XnaRect(0, 0, 32, 32), new XnaRect(292, 22, 64, 64));

            scenInfoBox = AddBlankRichTextBox(null, 292, 86, 366, 332);
            scenInfoBox.BackColour = Color.Black;
            scenInfoBox.Padding = 4;
            scenInfoBox.FontNormal = Gfx.TinyFont;
            scenInfoBox.FontBold = Gfx.SmallBoldFont;
            scenInfoBox.FontItalic = Gfx.ItalicFont;

            scenInfoBox.FormatText("");

            btnBack = AddButton(pressButton, "Main Menu", 0, 0, 123, 30);
            CancelKeyControl = btnBack;
            btnNewParty = AddButton(pressButton, "Start with New Party", 0, 0, 123, 30);
            OKKeyControl = btnNewParty;
            btnLoadParty = AddButton(pressButton, "Start with Stored Party", 0, 0, 123, 30);
            LineUpControls(280, 440, 10, btnBack, btnNewParty, btnLoadParty);

            listScenarios();

            if (scenList.Items.Count > 0)
            {
                scenList.SelectedItem = scenList.Items[0];
                foreach (ListBoxItem l in scenList.Items)
                {
                    if (Scenario.Filename == ((ScenarioInfo)l.Tag).Filename)
                        scenList.SelectedItem = l;
                }
            }
            else
            {
                scenList.AddItem("No scenarios in Scenarios directory", Color.Gray, null, true); 
                displayScenarioInfo(null);
            }

            Position(-2, -2);
        }

        public override void Draw(SpriteBatch sb, int partial = 0)
        {
            base.Draw(sb, partial);

            Gfx.DrawFrame(X + 290, Y + 20, 390, 420, new Color(0, 0, 0, 0));
        }

        void pressButton(Control b)
        {
            if (b == btnBack)
            {
                KillMe = true;
                StartMenuWindow.Begin();
                return;
            }

            if (scenList.SelectedItem == null)
            {
                new MessageWindow(null, "Choose a scenario first.", eDialogPic.STANDARD, 0, "Ok");
                return;
            }

            if (b == btnNewParty)
            {
                Scenario.Filename = Path.GetFileNameWithoutExtension(((ScenarioInfo)scenList.SelectedItem.Tag).Filename);
                //Game.ScenarioDirectory = Path.Combine(Game.RootDirectory, "Scenarios", Scenario.Filename);
                KillMe = true;
                new NewPartyMainWindow();
            }
            else if (b == btnLoadParty)
            {
                Scenario.Filename = Path.GetFileNameWithoutExtension(((ScenarioInfo)scenList.SelectedItem.Tag).Filename);
                new LoadGameWindow(true, false, true, doLoadParty);
                //KillMe = true;
                Visible = false;
            }
        }

        void doLoadParty(int option, string filename)
        {
            if (option == LoadGameWindow.CANCEL)
                Visible = true;
            else
            {
                SaveInfo i = Game.LoadSaveInfo(filename, true);
                if (i != null)
                {
                    //foreach (PCType pc in Party.PCList)
                    //    pc.MakePCGraphics();

                    Gfx.MakeCharacterHighlight(Party.ActivePC);
                    //Gfx.PCPortraitGfx = null;
                    //Gfx.PCGfx = null;

                    Game.BeginLoadingThread(true);
                    KillMe = true;
                }
                else Visible = true;
            }
        }

        void changeScenario(bool user_caused, ListBoxItem item)
        {
            displayScenarioInfo((ScenarioInfo)item.Tag);
        }

        void listScenarios()
        {
            scenList.Clear();

            if (!Directory.Exists(Path.Combine(Game.RootDirectory, "Scenarios"))) { Game.FlagError("Directory missing", "Scenarios directory not found."); return; }

            List<string> scens_to_try = Directory.GetDirectories(Path.Combine(Game.RootDirectory, "Scenarios")).ToList();
            List<ScenarioInfo> scens = new List<ScenarioInfo>();

            //Try to load the info for each directory in the scenario folder. Only adding entry if directory is a valid scenario.
            foreach (string s in scens_to_try)
            {
                ScenarioInfo si = ScenarioInfo.LoadScenarioInfo(s);
                if (si != null) scens.Add(si);
            }

            foreach (ScenarioInfo si in scens)
            {
                scenList.AddItem(si.Name, Color.White, si, false);
            }
        }

        void displayScenarioInfo(ScenarioInfo si)
        {
            if (si == null)
            {
                scenPic.Visible = false;
                scenTitle.Visible = false;
                scenInfoBox.Visible = false;
                return;
            }

            scenPic.Visible = true;
            scenTitle.Visible = true;
            scenInfoBox.Visible = true;

            string[] diff = { "Low Level (1-8)", "Medium Level (9-18)", "High Level (19-30)", "Very High Level (30+)" };
            string[] rating = { "G", "PG", "R", "NC-17" };

            var sr = new XnaRect((si.IntroPic % (Gfx.ScenarioGfx.Width / Gfx.SCENGFXWIDTH)) * Gfx.SCENGFXWIDTH, (si.IntroPic / (Gfx.ScenarioGfx.Width / Gfx.SCENGFXHEIGHT)) * Gfx.SCENGFXHEIGHT, Gfx.SCENGFXWIDTH, Gfx.SCENGFXHEIGHT);

            var scenpicfile = Path.Combine(Game.RootDirectory, "Scenarios", si.Filename, "Images", "ScenarioPics.png");
            Texture2D pic = null;
            if (Gfx.LoadCustom(scenpicfile, ref pic))
                scenPic.SetPicture(pic, sr);
            else
                scenPic.SetPicture(Gfx.ScenarioGfx, sr);

            scenTitle.Text = si.Name;
            scenInfoBox.FormatText(String.Format("{0}@n@n@b{1}@e@n@n{2}@n@n@iVersion: {3}.{4}.{5}@nRating: {6}@nDifficulty: {7}", si.Description, si.Credits1, si.Credits2, si.Version[0], si.Version[1], si.Version[2], rating[Maths.MinMax(0, 3, si.Rating)], diff[Maths.MinMax(0, 3, si.Difficulty)]));
        }
    }
}