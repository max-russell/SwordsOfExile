using Microsoft.Xna.Framework.Input;

//CUSTOMIZABLE KEYS

//L:    Look
//T:    Talk
//G:    Loot
//U:    Use
//M:    Cast Mage Spell
//P:    Cast Priest Spell
//S:    Fire Ranged
//Y:    Alchemy
//C:    Camp
//F:    Start Combat
//F:    End Combat
//W:    Wait
//Num 5: Stand Ready
//D:    Defend
//K:    Toggle Single Character
//Num 7: Move NW
//Num 8: Move N
//Num 9: Move NE
//Num 4: Move W
//Num 6: Move E
//Num 1: Move SW
//Num 2: Move S
//Num 3: Move SE
//F5:   Quicksave
//F9:   Quickload
//A:    Map View
//+:    Zoom in map
//-:    Zoom out map

namespace SwordsOfExileGame;

internal class KeyMappingWindow : GuiWindow
{
    private Label[] Labels = new Label[30];
    private Button[] remapButton = new Button[30];
    private Button okButton, cancelButton;
    private Button bDefault1, bDefault2;

    private Keys[] backupMap = new Keys[30];

    private int actionToRemap;

    public KeyMappingWindow()
        : base(20, 20, 605, 530, true, false, true, true, false)
    {
        var y = 20;
        var x = 20;
        for (var n = 0; n < 30; n++)
        {
            backupMap[n] = KeyHandler.KeyMap[n];
            if (n == 15) { x = 230; y = 20; }
            Labels[n] = AddLabel(KeyHandler.KeyMapNames[n], x, y, 0, 0, false);
            remapButton[n] = AddButton(pressButton, KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[n]), Labels[n].X + 100, Labels[n].Y - 10, 80, 30);
            y += 32;
        }
        Labels[14].Y -= 10;
        Labels[28].Y -= 10;
        Labels[29].Y -= 10;

        AddLabel("Use the buttons to customise the key mappings. Or use the buttons below for the default configurations.", Labels[15].X + 200, 20, 150, -1, true);
        bDefault1 = AddButton(pressButton, "Standard", Labels[15].X + 200, 100, 140, 30);
        bDefault2 = AddButton(pressButton, "No NumPad", Labels[15].X + 200, 132, 140, 30);

        cancelButton = AddButton(pressButton, "Cancel", 0, 0, -1, -1);
        okButton = AddButton(pressButton, "Accept", 0, 0, -1, -1);
        LineUpControlsRight(Width - 30, Height - okButton.Height - 30, 10, cancelButton, okButton);

        Position(-2, -2);
    }

    private void pressButton(Control b)
    {
        if (b == okButton)
        {
            var w = Gui.GetWindowOfType(typeof(MenuBarWindow));
            if (w != null)
                ((MenuBarWindow)w).SetKeyShortcuts();
            Game.SetPortraitWindowKeys();
            KillMe = true;
        }
        else if (b == cancelButton)
        {
            for (var n = 0; n < 30; n++)
                KeyHandler.KeyMap[n] = backupMap[n];
            KillMe = true;
        }
        else if (b == bDefault1)
        {
            for (var n = 0; n < 30; n++)
            {
                actionToRemap = n;
                remapKey(KeyHandler.Default1KeyMap[n]);
            }
        }
        else if (b == bDefault2)
        {
            for (var n = 0; n < 30; n++)
            {
                actionToRemap = n;
                remapKey(KeyHandler.Default2KeyMap[n]);
            }
        }
        else
        {
            for (var n = 0; n < 30; n++)
            {
                if (b == remapButton[n])
                {
                    actionToRemap = n;
                    new InputKeyWindow(remapKey, "Press a key (Escape to cancel)", true);
                    break;
                }
            }
        }
    }

    private void remapKey(Keys k)
    {
        if (k != Keys.Escape)
        {
            remapButton[actionToRemap].Caption = KeyHandler.GetStringFromKeys(k);
            KeyHandler.KeyMap[actionToRemap] = k;
        }
    }

}