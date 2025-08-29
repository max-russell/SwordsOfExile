using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal delegate void MessageWindowHandler(int button_index);

internal class MessageWindow : GuiWindow
{
    private List<Button> mainButtons = new();
    private MessageWindowHandler Handler;
    private Button recordButton;
    private RichTextBox messageArea;
    private string rawMessage;

    public MessageWindow(MessageWindowHandler handler, string message, eDialogPic pictype, int pictureindex, params string[] buttons)
        : base(0, 0, 400, 400, true, false, true, true, false)
    {

        Handler = handler;

        int ypos = 20, xpos = 10;
        PictureBox p = null;
        Texture2D pictex; XnaRect picrect;

        var sheet = (pictureindex & 0x7C00) >> 10;
        var no = (pictureindex & 0x03FF);

        switch (pictype)
        {
            case eDialogPic.CREATURE:
            case eDialogPic.CREATURE2x1:
            case eDialogPic.CREATURE1x2:
            case eDialogPic.CREATURE2x2:
                var npc = new NPCRecord(pictureindex,
                    pictype is eDialogPic.CREATURE2x1 or eDialogPic.CREATURE2x2 ? 2 : 1,
                    pictype is eDialogPic.CREATURE1x2 or eDialogPic.CREATURE2x2 ? 2 : 1
                );
                picrect = npc.GetGraphic(true, false, out pictex);
                p = new PictureBox(this, picrect, pictex, new XnaRect(10, ypos, picrect.Width, picrect.Height), -1);
                break;
            case eDialogPic.FACE:
                if (Gfx.FacesGfx[sheet] == null) break;

                var sr = new XnaRect((no % Gfx.FacesGfxSlotsAcross[sheet]) * Gfx.FACEGFXWIDTH, (no / Gfx.FacesGfxSlotsAcross[sheet]) * Gfx.FACEGFXHEIGHT, 
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
        }
        if (p != null)
        {
            controls.Add(p);
            xpos = 20 + p.Width;
        }

        rawMessage = message;
        messageArea = AddRichTextBox(message, null, xpos, ypos, 360);
        ypos += messageArea.Height + 20;

        var first = true;

        foreach (var s in buttons)
        {
            var b = AddButton(pressMainButton, s, 0, ypos);
            mainButtons.Add(b);
            if (first) OKKeyControl = b;
            first = false;
        }

        var winpos = ypos + mainButtons[0].Height + 30;
        base.Resize(390 + xpos, winpos);
        LineUpControlsRight(InnerWidth - 10, ypos, 10, mainButtons.ToArray<Control>());
        Position(-2, -2);

        recordButton = AddButton(pressMainButton, "Record", 0, 0, 48, 15);
        recordButton.Position(10, -10, -1, 1);
        if (Game.InMainMenu) recordButton.Visible = false;
    }

    private void pressMainButton(Control button)
    {  
        var n = 0;
        foreach (var b in mainButtons)
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