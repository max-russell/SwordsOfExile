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
    delegate void MessageWindowHandler(int button_index);

    class MessageWindow : GuiWindow
    {
        List<Button> mainButtons = new List<Button>();
        MessageWindowHandler Handler;
        Button recordButton;
        RichTextBox messageArea;
        string rawMessage;
        //Texture2D customPic;

        public MessageWindow(MessageWindowHandler handler, string message, eDialogPic pictype, int pictureindex, params string[] buttons)
            : base(0, 0, 400, 400, true, false, true, true, false)
        {

            Handler = handler;

            int ypos = 20, xpos = 10;
            PictureBox p = null;
            Texture2D pictex; XnaRect picrect;

            int sheet = (pictureindex & 0x7C00) >> 10;
            int no = (pictureindex & 0x03FF);

            switch (pictype)
            {
                case eDialogPic.CREATURE:
                case eDialogPic.CREATURE2x1:
                case eDialogPic.CREATURE1x2:
                case eDialogPic.CREATURE2x2:
                    var npc = new NPCRecord(pictureindex,
                        (pictype == eDialogPic.CREATURE2x1 || pictype == eDialogPic.CREATURE2x2) ? 2 : 1,
                        (pictype == eDialogPic.CREATURE1x2 || pictype == eDialogPic.CREATURE2x2) ? 2 : 1
                        );
                    picrect = npc.GetGraphic(true, false, out pictex);
                    p = new PictureBox(this, picrect, pictex, new XnaRect(10, ypos, picrect.Width, picrect.Height), -1);
                    break;
                case eDialogPic.FACE:
                    if (Gfx.FacesGfx[sheet] == null) break;

                    XnaRect sr = new XnaRect((no % Gfx.FacesGfxSlotsAcross[sheet]) * Gfx.FACEGFXWIDTH, (no / Gfx.FacesGfxSlotsAcross[sheet]) * Gfx.FACEGFXHEIGHT, 
                                                Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT);
                    p = new PictureBox(this, sr, Gfx.FacesGfx[sheet], new XnaRect(10, ypos, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT), -1);
                    break;
                case eDialogPic.SCENARIO:
                    sr = new XnaRect((pictureindex % (Gfx.ScenarioGfx.Width / Gfx.SCENGFXWIDTH)) * Gfx.SCENGFXWIDTH, (pictureindex / (Gfx.ScenarioGfx.Width / Gfx.SCENGFXHEIGHT)) * Gfx.SCENGFXHEIGHT, Gfx.SCENGFXWIDTH, Gfx.SCENGFXHEIGHT);
                    p = new PictureBox(this, sr, Gfx.ScenarioGfx, new XnaRect(10, ypos, Gfx.SCENGFXWIDTH, Gfx.SCENGFXHEIGHT), -1);
                    break;
                case eDialogPic.STANDARD:
                    if (Gfx.DialogGfx[sheet] == null) break;
                    sr = new XnaRect((no % Gfx.DialogGfxSlotsAcross[sheet]) * Gfx.MISCGFXWIDTH, (no / Gfx.DialogGfxSlotsAcross[sheet]) * Gfx.MISCGFXHEIGHT, Gfx.MISCGFXWIDTH, Gfx.MISCGFXHEIGHT);
                    p = new PictureBox(this, sr, Gfx.DialogGfx[sheet], new XnaRect(10, ypos, Gfx.MISCGFXWIDTH, Gfx.MISCGFXHEIGHT), -1);
                    break;
                case eDialogPic.TERRAIN:
                    if ((pictureindex & 0x10000) != 0)
                    {
                        if (Gfx.AnimTerrainGfx[sheet] == null) break;
                        sr = new XnaRect((no % Gfx.AnimTerrainGfxSlotsAcross[sheet]) * Gfx.SRCTILEWIDTH * 4, pictureindex / Gfx.AnimTerrainGfxSlotsAcross[sheet] * Gfx.SRCTILEHEIGHT, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
                        p = new PictureBox(this, sr, Gfx.AnimTerrainGfx[sheet], new XnaRect(10, ypos, Gfx.TILEWIDTH, Gfx.SRCTILEHEIGHT), -1);
                    }
                    else
                    {
                        if (Gfx.TerrainGfx[sheet] == null) break;
                        sr = new XnaRect((no % Gfx.TerrainGfxSlotsAcross[sheet]) * Gfx.SRCTILEWIDTH, pictureindex / Gfx.TerrainGfxSlotsAcross[sheet] * Gfx.SRCTILEHEIGHT, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
                        p = new PictureBox(this, sr, Gfx.TerrainGfx[sheet], new XnaRect(10, ypos, Gfx.TILEWIDTH, Gfx.SRCTILEHEIGHT), -1);
                    }
                    break;
                //case eDialogPic.CUSTOM_SQUARE: 
                //case eDialogPic.CUSTOM_TILE:
                //    customPic = Gfx.MakeKludgyCustomDialogPic(pictureindex, pictype);
                //    int w = pictype == eDialogPic.CUSTOM_SQUARE ? Gfx.CUSTOMGFXHEIGHT : Gfx.CUSTOMGFXWIDTH;
                //    sr = new XnaRect(0, 0, w, Gfx.CUSTOMGFXHEIGHT);
                //    p = new PictureBox(this, sr, customPic, new XnaRect(10, ypos, w, Gfx.CUSTOMGFXHEIGHT), -1);
                //    break;
                ////case eDialogPic.CREATURE_CUSTOM:
                ////case eDialogPic.TERRAIN_CUSTOM:
                ////    Gfx.MakeKludgyCustomDialogPic(pictureindex, pictype == eDialogPic.DIALOG_CUSTOM);

                ////    int w = pictype == eDialogPic.DIALOG_CUSTOM ? Gfx.CUSTOMGFXHEIGHT : Gfx.CUSTOMGFXWIDTH;
                ////    sr = new XnaRect(0, 0, w, Gfx.CUSTOMGFXHEIGHT);
                ////    p = new PictureBox(this, sr, Gfx.CustomDialogPicKludge, new XnaRect(10, ypos, w, Gfx.CUSTOMGFXHEIGHT), -1);
                ////    break;
            }
            if (p != null)
            {
                controls.Add(p);
                xpos = 20 + p.Width;
            }

            rawMessage = message;
            messageArea = AddRichTextBox(message, null, xpos, ypos, 360);
            ypos += messageArea.Height + 20;

            bool first = true;

            foreach (string s in buttons)
            {
                Button b = AddButton(pressMainButton, s, 0, ypos);
                mainButtons.Add(b);
                if (first) OKKeyControl = b;
                first = false;
            }

            int winpos = ypos + mainButtons[0].Height + 30;
            Resize(390 + xpos, winpos);
            LineUpControlsRight(InnerWidth - 10, ypos, 10, mainButtons.ToArray<Control>());
            Position(-2, -2);

            recordButton = AddButton(pressMainButton, "Record", 0, 0, 48, 15);
            recordButton.Position(10, -10, -1, 1);
            if (Game.InMainMenu) recordButton.Visible = false;
        }

        void pressMainButton(Control button)
        {  
            int n = 0;
            foreach (Button b in mainButtons)
            {
                if (b == button)
                {
                    if (Handler != null) Handler.Invoke(n);
                    KillMe = true;
                    return;
                }
                n++;
            }

            if (button == recordButton)
            {
                Game.AddMessage("Saved to Notes.");
                Scenario.MakeNote(Game.CurrentMap.Name + " - Day " + Party.Day, rawMessage);
                recordButton.Enabled = false;
            }
        }

    }

    //class CustomMessageWindow : GuiWindow
    //{

    //    public static short[] available_dlog_buttons = {0,63,64,65,1,4,5,8, 
    //                            128,
    //                            9,
    //                            10, // 10
    //                            11,12,13,
    //                            14,15,16,17,29, 51,
    //                            60,61,62, // 20
    //                            66,69,70, 71,72,73,74,79,
    //                            80,83,86,87,88, 91,92,93,99,100,
    //                            101,102,104, 129,130,131,132,133,134,135,136,137};
    //    public static string[] button_strs = {"Done ","Ask"," "," ","Keep", "Cancel","+","-","Buy","Leave",
    //                    "Get","1","2","3","4","5","6","Cast"," "," ",
    //                    " "," "," ","Buy","Sell","Other Spells","Buy x10"," "," ","Save",
    //                    "Race","Train","Items","Spells","Heal Party","1","2","3","4","5",
    //                    "6","7","8","9","10","11","12","13","14","15",
    //            /*50*/  "16","Take","Create","Delete","Race/Special","Skill","Name","Graphic","Bash Door","Pick Lock",
    //                    "Leave","Steal","Attack","OK","Yes","No","Step In"," ","Record","Climb",
    //                    "Flee","Onward","Answer","Drink","Approach","Mage Spells","Priest Spells","Advantages","New Game","Land",
    //                    "Under","Restore","Restart","Quit","Save First","Just Quit","Rest","Read","Pull","Alchemy",
    //                    "17","Push","Pray","Wait","","","Delete","Graphic","Create","Give",
    //            /*100*/		"Destroy","Pay","Free","Next Tip","Touch", "Select Icon","Create/Edit","Clear Special","Edit Abilities","Choose",
    //                    "Go Back","Create New","General","One Shots","Affect PCs","If-Thens","Town Specs","Out Specs","Advanced","Weapon Abil",
    //                    "General Abil.","NonSpell Use","Spell Usable","Reagents","Missiles","Abilities","Pick Picture","Animated","Enter","Burn",
    //                    "Insert","Remove","Accept","Refuse","Open","Close","Sit","Stand","","",
    //                    "18","19","20","Invisible!","","","","","",""};


    //    List<Label> labels = new List<Label>();
    //    Button doneButton, recordButton;
    //    List<Button> mainButtons = new List<Button>();
    //    List<SpecialNode> buttonNodes;
    //    bool firstButtonCancels = false;

    //    public CustomMessageWindow(string[] texts, int pictureindex, List<int> buttons, List<SpecialNode>bnodes, bool first_button_cancels)
    //        : base(0, 0, 400, 400, true, false, true, true, false)
    //    {
    //        int ypos = 10;

    //        //ToDO: Draw the correct picture in the window according to pictureindex

    //        foreach(string t in texts)
    //        {
    //            if (t == null || t.Length == 0) break;

    //            Label l = AddLabel(t, 10, ypos,-1,-1,true);
    //            l.Resize(360, -1);
    //            ypos += l.Height + 10;
    //        }

    //        ypos += 30;

    //        if (buttons != null)
    //        {
    //            int xpos = 380;
    //            bool first = true;

    //            foreach (int s in buttons)
    //            {
    //                Button b = AddButton(pressMainButton, button_strs[available_dlog_buttons[s]], 0, ypos);
    //                mainButtons.Add(b);
    //                b.X = xpos - b.Width;
    //                xpos = b.X - 10;
    //                if (first && first_button_cancels) b.KeyShortcut = Keys.Enter;

    //                first = false;
    //            }
    //            buttonNodes = bnodes;
    //            firstButtonCancels = first_button_cancels;
    //        }
    //        recordButton = AddButton(null, "Record", 20, ypos);
    //        Resize(400, ypos + recordButton.Height + 20);

    //        if (buttons == null)
    //        {
    //            doneButton = AddButton(pressDone, "Done", 340, ypos);
    //            doneButton.Position(-10, -10, 1, 1);
    //            doneButton.KeyShortcut = Keys.Enter;
    //        }

    //        recordButton.Position(10, -10, -1, 1);
    //        Position(-2, -2);
    //    }

    //    void pressDone(Button button_pressed)
    //    {
    //        KillMe = true;
    //    }

    //    void pressMainButton(Button button_pressed)
    //    {
    //        for (int n = 0; n < mainButtons.Count; n++)
    //        {
    //            if (button_pressed == mainButtons[n])
    //            {
    //                SpecialNode.SendDialogOutcomeToSpecials(n == 0 && firstButtonCancels ? true : false, buttonNodes[n]);
    //                KillMe = true;
    //                break;
    //            }
    //        }
    //    }

    //}

}