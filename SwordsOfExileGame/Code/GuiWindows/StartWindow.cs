using System;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class StartMenuWindow : GuiWindow
{
    private static StartMenuWindow instance;
    private Button b_resume, b_startnew, b_quit, b_load, b_options, b_about;

    public static void Begin()
    {
        StartupMap.Load();
        instance = new StartMenuWindow();
    }

    public StartMenuWindow()
        : base(20, 20, 420, 500, true, false, true, true, false)
    {
        AddPictureBox(Gfx.LogoPic, Gfx.LogoPic.Bounds, new XnaRect(0, 10, Gfx.LogoPic.Width, Gfx.LogoPic.Height));

        b_resume = AddButton(pressButton, "Resume Game", 0, 0, 250, -1);
        OKKeyControl = b_resume;
        if (Game.LastSaveFile == "" || !File.Exists(Path.Combine(Game.RootDirectory, "Saves", Path.ChangeExtension(Game.LastSaveFile, "sav2"))))
            b_resume.Enabled = false;

        b_startnew = AddButton(pressButton, "Start New Game", 0, 0, 250, -1);

        b_load = AddButton(pressButton, "Load Game", 0, 0, 250, -1);
        b_quit = AddButton(pressButton, "Quit", 0, 0, 250, -1);
        b_about = AddButton(pressButton, "About", 0, 0, 250, -1);
        b_options = AddButton(pressButton, "Options", 0, 0, 250, -1);
        CancelKeyControl = b_quit;
        b_startnew.Position(0, 100, 0, -1);

        LineUpControlsDown(b_startnew.X, 210, 10, b_resume, b_startnew, b_load, b_options, b_about, b_quit);

        Resize(Width, b_quit.Height + b_quit.Y + 40);
        Position(-2, -2);
    }

    private void pressButton(Control b)
    {
        if (b == b_resume)
        {
            if (Game.LastSaveFile != "" && File.Exists(Path.Combine(Game.RootDirectory, "Saves", Path.ChangeExtension(Game.LastSaveFile, "sav2"))))
            {
                KillMe = true;
                if (KeyHandler.KeyDown(Keys.Oem8)) Game.DebugLoad = true;
                Game.BeginLoadingThread(false);
            }
        }
        if (b == b_load)
        {
            new LoadGameWindow(true, false, false, doLoad);
            Visible = false;
        }
        else if (b == b_startnew)
        {
            new ScenSelectWindow();
            KillMe = true;
        }  
        else if (b == b_options)
        {
            new OptionsWindow(); 
        }
        else if (b == b_about)
        {
            new MessageWindow(pressAbout, "@bSwords of Exile@e is a ground-up remake of @bBlades of Exile@e by Spiderweb Software.", eDialogPic.SCENARIO, 0, "Ok", "Visit Spiderweb Software", "Visit SoE website");
        }
        else if (b == b_quit)
            Game.Quit = true;
    }

    private void pressAbout(int option)
    {
        if (option == 2)
            System.Diagnostics.Process.Start("https://github.com/max-russell/SwordsOfExile");
        else if (option == 1)
            System.Diagnostics.Process.Start("http://www.spiderwebsoftware.com");
    }

    private void doLoad(int option, string filename)
    {
        if (option == LoadGameWindow.CANCEL)
            Visible = true;
        else
        {
            var i = Game.LoadSaveInfo(filename, false);
            if (i != null)
            {
                Scenario.Filename = Path.GetFileNameWithoutExtension(i.ScenFile);
                Game.ScenarioDirectory = Path.Combine(Game.RootDirectory, "Scenarios", Scenario.Filename);
                Game.LastSaveFile = filename;
                KillMe = true;
                Game.BeginLoadingThread(false);
            }
            else
                Visible = true;
        }
    }

    public override void Draw(SpriteBatch sb, int partial = 0)
    {
        base.Draw(sb, partial);
        sb.DrawString(Gfx.TinyFont, string.Format("v{0}",System.Reflection.Assembly.GetExecutingAssembly().GetName().Version), new Vector2(X + 15,InnerHeight + Y - 1), Color.White);
    }
}