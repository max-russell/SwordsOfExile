using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

#region Load Game Window

internal delegate void FileHandler(int option, string filename);

internal class LoadGameWindow : GuiWindow
{
    public const int LOAD = 1, SAVE = 2, CANCEL = -1;

    private PartyType curPartyTemp;

    private ListBox savesList;
    private RichTextBox saveInfoBox;
    private Label saveName, titleLbl;
    private PictureBox[] partyPics;

    private Label[] partyNames = new Label[Constants.PC_LIMIT], 
        partyLvls = new Label[Constants.PC_LIMIT],
        partyStatus = new Label[Constants.PC_LIMIT];

    private PictureBox scenPic;
    private Button btnBack, btnLoad, btnSave, btnDelete;
    private bool allowLoading, allowSaving, partiesOnly;

    private FileHandler Func;

    public LoadGameWindow(bool loading, bool saving, bool parties_only, FileHandler func)
        : base(0, 0, 700, 500, true, false, true, true, false)
    {
        Func = func;

        allowLoading = loading;
        allowSaving = saving;
        partiesOnly = parties_only;

        var txt="";
        if (allowLoading && !allowSaving && !partiesOnly) txt = "Load Game";
        else if (allowLoading && allowSaving && !partiesOnly) txt = "Load/Save Game";
        else if (allowLoading && !allowSaving && partiesOnly) txt = "Load Party";
        else if (!allowLoading && allowSaving && partiesOnly) txt = "Save Party";

        titleLbl = AddLabel(txt, 10, 10, 250, 30, false);
        titleLbl.Font = Gfx.TalkFontBold;

        savesList = AddListBox(changeSave, 10, 50, 250, 410, 0);

        controls.Add(new FrameBox(this, new XnaRect(278, 8, 390, 420), new Color(0, 0, 0, 255), -1));

        saveName = AddLabel("", 292, 22, 352, 32, false);
        saveName.BackColour = Color.Black;
        saveName.Font = Gfx.TalkFontNormal;
        saveName.Padding = 4;

        partyPics = new PictureBox[Constants.PC_LIMIT];
     
        int x = 292, y = 52;
        for (var a = 0; a < Constants.PC_LIMIT; a++)
        {
            if (a % 2 == 0) x = 292; else x = 470;

            partyNames[a] = AddLabel("xxx", x + 74, y + 14, -1, -1, false);
            partyNames[a].Font = Gfx.SmallBoldFont;
            partyLvls[a] = AddLabel("Level 1", x + 74, y + 30, -1, -1, false);
            partyStatus[a] = AddLabel("DEAD", x + 74, y + 46, -1, -1, false);
            partyStatus[a].TextColour = Color.Red;
            partyPics[a] = AddPictureBox(Gfx.NewGui, new XnaRect(134, 147, 32, 32), new XnaRect(x, y, 64, 64));
            if (a % 2 == 1) y += 64;
        }

        scenPic = AddPictureBox(Gfx.ScenarioGfx, new XnaRect(0, 0, 32, 32), new XnaRect(292, 22, 64, 64));
        scenPic.Visible = false;

        saveInfoBox = AddBlankRichTextBox(null, 292, 244, 366, 174);
        saveInfoBox.BackColour = Color.Black;
        saveInfoBox.Padding = 4;
        saveInfoBox.FontNormal = Gfx.TinyFont;
        saveInfoBox.FontBold = Gfx.SmallBoldFont;
        saveInfoBox.FontItalic = Gfx.ItalicFont;

        saveInfoBox.FormatText("");

        btnBack = AddButton(pressButton, "Back", 0, 0, 84, 30);
        btnDelete = AddButton(pressButton, "Delete", 0, 0, 84, 30);

        if (allowLoading && allowSaving)
        {
            btnLoad = AddButton(pressButton, "Load", 0, 0, 84, 30);
            btnSave = AddButton(pressButton, "Save", 0, 0, 84, 30);
            LineUpControls(280, 440, 10, btnBack, btnLoad, btnSave, btnDelete);
        }
        else if (allowLoading)
        {
            btnLoad = AddButton(pressButton, "Load", 0, 0, 178, 30);
            LineUpControls(280, 440, 10, btnBack, btnLoad, btnDelete);
        }
        else if (allowSaving)
        {
            btnSave = AddButton(pressButton, "Save", 0, 0, 178, 30);
            LineUpControls(280, 440, 10, btnBack, btnSave, btnDelete);
        }

        listSaves();

        if (savesList.Items.Count > 0) savesList.SelectedItem = savesList.Items[0];
        else displaySaveInfo(null);

        Position(-2, -2);
    }

    private void pressButton(Control b)
    {
        if (b == btnBack)
        {
            KillMe = true;
            Func.Invoke(CANCEL,null);
        }
        else if (b == btnLoad)
        {

            if (KeyHandler.KeyDown(Keys.Oem8))
                Game.DebugLoad = true;
            var savefile = ((SaveInfo)savesList.SelectedItem.Tag).Filename;
            Func.Invoke(LOAD, savefile);
            KillMe = true;
        }
        else if (b == btnSave)
        {
            if (savesList.SelectedItem.Tag == null)
            {
                //Create new save game
                new InputTextWindow(newSaveGame, "Enter a name for the Save Game", "", false);
            }
            else
            {
                //Overwrite existing save game
                new MessageWindow(confirmOverwrite, "Are you sure you want to overwrite this save game?", eDialogPic.STANDARD, 23, "Yes", "Cancel");
            }
        }
        else if (b == btnDelete)
        {
            //Overwrite existing save game
            new MessageWindow(confirmDelete, "Are you sure you want to delete this save game?", eDialogPic.STANDARD, 23, "Yes", "Cancel");
        }
    }

    private void confirmOverwrite(int n)
    {
        if (n == 0)
        {
            var i = (SaveInfo)savesList.SelectedItem.Tag;

            Func.Invoke(SAVE, i.Filename);
            KillMe = true;
        }
    }

    private void newSaveGame(string n)
    {
        if (n != null && n != "")
        {
            var f = n;

            foreach (var c in Path.GetInvalidFileNameChars())
                if (f.Contains(c)) f = f.Replace(c, '_');

            Func.Invoke(SAVE, f);
            KillMe = true;
        }
    }

    private void confirmDelete(int n)
    {
        if (n == 0)
        {
            var f = Path.Combine(Game.RootDirectory, "Saves", Path.ChangeExtension(((SaveInfo)savesList.SelectedItem.Tag).Filename, "sav2"));
            if (File.Exists(f)) File.Delete(f);

            listSaves();
            if (savesList.Items.Count > 0) savesList.SelectedItem = savesList.Items[0];
            else displaySaveInfo(null);
        }
    }

    private void changeSave(bool user_caused, ListBoxItem item)
    {
        if (item.Tag == null)
        {
            displaySaveInfo(null);
            if (allowLoading) btnLoad.Enabled = false;
            btnDelete.Enabled = false;
        }
        else
        {
            displaySaveInfo((SaveInfo)item.Tag);
            if (allowLoading) btnLoad.Enabled = true;
            btnDelete.Enabled = true;
        }
    }

    private void listSaves()
    {
        savesList.Clear();
        curPartyTemp = Game.CurrentParty; //Keep current party backed up so we don't lose it.

        if (allowSaving)
            savesList.AddItem("(Create New Save)", Color.White, null, true);

        Directory.CreateDirectory(Path.Combine(Game.RootDirectory, "Saves"));
        var savegames = Directory.GetFiles(Path.Combine(Game.RootDirectory, "Saves")).ToList();

        var saves = new List<SaveInfo>();

        //Try to load the info for each directory in the scenario folder. Only adding entry if directory is a valid scenario.
        foreach (var s in savegames)
        {
            var s2 = Path.GetFileNameWithoutExtension(s);
            var i = Game.LoadSaveInfo(s2, partiesOnly);
            if (i != null) saves.Add(i);
        }

        foreach (var i in saves)
        {
            savesList.AddItem(i.SaveName + " (" + i.PartyName + ")", Color.White, i, false);
        }

        if (saves.Count == 0)
            if (partiesOnly) savesList.AddItem("No parties in Saves directory", Color.Gray, null, true);
            else savesList.AddItem("No saved games in Saves directory", Color.Gray, null, true);

        Game.CurrentParty = curPartyTemp;
    }

    private void displaySaveInfo(SaveInfo i)
    {
        if (i == null)
        {
            saveName.Text = "";
            saveInfoBox.FormatText("");
            if (allowLoading) btnLoad.Enabled = false;
            btnDelete.Enabled = false;

            for (var a = 0; a < Constants.PC_LIMIT; a++)
            {
                partyPics[a].Visible = false;
                partyNames[a].Visible = false;
                partyLvls[a].Visible = false;
                partyStatus[a].Visible = false;
            }

        }
        else
        {
            var party = Game.LoadSavedPartyInfo(i.Filename);
            saveName.Text = i.PartyName;
            for (var a = 0; a < Constants.PC_LIMIT; a++)
            {
                if (party.PCList.Count > a && party.PCList[a] != null)
                {

                    partyPics[a].SetPicture(party.PCList[a].PortraitTexture, new XnaRect(0, 0, 32, 32));
                    partyNames[a].Text = party.PCList[a].Name;
                    partyLvls[a].Text = "Level " + party.PCList[a].Level;
                    partyLvls[a].Visible = true;
                    partyPics[a].Visible = true;
                    partyNames[a].Visible = true;
                    if (party.PCList[a].LifeStatus == eLifeStatus.ALIVE) partyStatus[a].Visible = false;
                    else
                    {
                        partyStatus[a].Visible = true;
                        partyStatus[a].Text = party.PCList[a].LifeStatusString;
                    }
                }
                else
                {
                    partyPics[a].SetPicture(Gfx.NewGui, new XnaRect(134, 147, 32, 32));
                    partyNames[a].Text = "-";
                    partyLvls[a].Visible = false;
                    partyStatus[a].Visible = false;
                }
                       

            }

            if (allowLoading) btnLoad.Enabled = true;

            var infotext = new StringBuilder();
            if (partiesOnly)
            {
                infotext.Append(string.Format("This party was saved on {0}", i.LastSavedDate.ToString()));
            }
            else
            {
                var sr = new XnaRect((i.IntroPic % (Gfx.ScenarioGfx.Width / Gfx.SCENGFXWIDTH)) * Gfx.SCENGFXWIDTH, (i.IntroPic / (Gfx.ScenarioGfx.Width / Gfx.SCENGFXHEIGHT)) * Gfx.SCENGFXHEIGHT, Gfx.SCENGFXWIDTH, Gfx.SCENGFXHEIGHT);
                infotext.Append(
                    String.Format("@b{0}@e are currently adventuring in @b{1}@e, where it is day @b{2}@e. Their current location is @b{3}@e. @n@nThis game was saved on {4}.",
                        i.PartyName, i.ScenName, i.Age / Constants.DAY_LENGTH + 1, i.CurrentMapName, i.LastSavedDate.ToString()));
            }
            infotext.Append(string.Format("@n@n@iTotal Damage Dealt: {0}@nTotal Monsters Killed: {1}@nTotal XP gained: {2}@nTotal Damage Taken: {3}", 
                party.total_dam_done, party.total_m_killed, party.total_xp_gained, party.total_dam_taken));

            saveInfoBox.FormatText(infotext.ToString());

            btnDelete.Enabled = true;
        }
    }

    public override void Draw(SpriteBatch sb, int partial = 0)
    {
        base.Draw(sb, partial);
    }

}

#endregion