using System;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class MenuBarWindow : GuiWindow
{
    private static MenuBarWindow instance;

    private PictureButton btnCastMage, btnCastPriest, btnLook, btnCamp, btnDefend, btnTalk, btnMap, btnLoot, btnGather,
        btnSave, btnLoad, btnWait, btnEnd, btnAct, btnCombat, btnRanged, btnMapSml, btnUse, btnAlchemy;

    public MenuBarWindow()
        : base(0, 0, 279, 58, true, true, false, false, false)
    {
        instance = this;
        //Centre horizontally on bottom of screen
        Position(-2, -1);
        btnCastMage = AddPictureButton(pressMagic, new XnaRect(0, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(0, 21, 37, 37));
        btnCastPriest = AddPictureButton(pressMagic, new XnaRect(37, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(37, 21, 37, 37));
        btnLook = AddPictureButton(pressLook, new XnaRect(74, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(74, 21, 37, 37));
        btnCamp = AddPictureButton(pressRest, new XnaRect(111, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(111, 21, 37, 37));
        btnDefend = AddPictureButton(pressDefend, new XnaRect(111, 37, 37, 37), Gfx.ButtonsGfx, new XnaRect(111, 21, 37, 37));
        btnTalk = AddPictureButton(pressTalk, new XnaRect(111, 74, 37, 37), Gfx.ButtonsGfx, new XnaRect(111, 21, 37, 37));
        btnMap = AddPictureButton(pressMap, new XnaRect(148, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(148, 21, 37, 37));
        btnLoot = AddPictureButton(pressGather, new XnaRect(148, 37, 37, 37), Gfx.ButtonsGfx, new XnaRect(148, 21, 37, 37));
        btnGather = AddPictureButton(pressGather, new XnaRect(148, 74, 37, 37), Gfx.ButtonsGfx, new XnaRect(148, 21, 37, 37));
        btnSave = AddPictureButton(pressSave, new XnaRect(185, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(185, 21, 37, 37));
        btnLoad = AddPictureButton(pressLoad, new XnaRect(222, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(222, 21, 37, 37));
        btnWait = AddPictureButton(pressWait, new XnaRect(185, 37, 37, 18), Gfx.ButtonsGfx, new XnaRect(185, 21, 37, 18));
        btnEnd = AddPictureButton(pressEndCombat, new XnaRect(222, 37, 37, 18), Gfx.ButtonsGfx, new XnaRect(222, 21, 37, 18));
        btnRanged = AddPictureButton(pressRanged, new XnaRect(185, 56, 37, 18), Gfx.ButtonsGfx, new XnaRect(185, 40, 37, 18));
        btnAct = AddPictureButton(pressAct, new XnaRect(222, 56, 37, 18), Gfx.ButtonsGfx, new XnaRect(222, 40, 37, 18));
        btnUse = AddPictureButton(pressUse, new XnaRect(185, 74, 37, 18), Gfx.ButtonsGfx, new XnaRect(185, 21, 37, 18));
        btnMapSml = AddPictureButton(pressMap, new XnaRect(185, 93, 37, 18), Gfx.ButtonsGfx, new XnaRect(185, 40, 37, 18));
        btnCombat = AddPictureButton(pressStartCombat, new XnaRect(222, 74, 37, 37), Gfx.ButtonsGfx, new XnaRect(222, 21, 37, 37));
        btnAlchemy = AddPictureButton(pressAlchemy, new XnaRect(258,74,36,36), Gfx.ButtonsGfx, new XnaRect(258,21,36,36));
        SetKeyShortcuts();
        Update();
    }

    public void SetKeyShortcuts()
    {
        btnCastMage.KeyShortcut = KeyHandler.KeyMap[4];
        btnCastMage.SetStandardToolTip("Cast Mage Spell@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[4]), -1);

        btnCastPriest.KeyShortcut = KeyHandler.KeyMap[5];
        btnCastPriest.SetStandardToolTip("Cast Priest Spell@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[5]), -1);

        btnLook.KeyShortcut = KeyHandler.KeyMap[0];
        btnLook.SetStandardToolTip("Inspect Terrain@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[0]), -1);

        btnCamp.SetStandardToolTip("Set up Camp@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[8]), -1);
        btnCamp.KeyShortcut = KeyHandler.KeyMap[8];

        btnDefend.SetStandardToolTip("Defend@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[13]), -1);
        btnDefend.KeyShortcut = KeyHandler.KeyMap[13];

        btnTalk.KeyShortcut = KeyHandler.KeyMap[1];
        btnTalk.SetStandardToolTip("Talk@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[1]), -1);

        btnMap.KeyShortcut = KeyHandler.KeyMap[25];
        btnMap.SetStandardToolTip("Map View@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[25]), -1);

        btnLoot.KeyShortcut = KeyHandler.KeyMap[2];
        btnLoot.SetStandardToolTip("Gather Loot@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[2]), -1);

        btnGather.KeyShortcut = KeyHandler.KeyMap[2];
        btnGather.SetStandardToolTip("Gather Loot@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[2]), -1);

        btnSave.SetStandardToolTip("Quick Save@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[23]), -1);

        btnLoad.SetStandardToolTip("Quick Load@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[24]), -1);

        btnWait.KeyShortcut = KeyHandler.KeyMap[11];
        btnWait.SetStandardToolTip("Wait (Delay acting this turn)@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[11]), -1);

        btnEnd.KeyShortcut = KeyHandler.KeyMap[10];
        btnEnd.SetStandardToolTip("End Combat@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[10]), -1);

        btnRanged.KeyShortcut = KeyHandler.KeyMap[6];
        btnRanged.SetStandardToolTip("Fire Ranged Weapon@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[6]), -1);

        btnAct.SetStandardToolTip("Toggle Single Character Mode@nOnly current party member will@nact each turn.@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[14]), -1);
        btnAct.KeyShortcut = KeyHandler.KeyMap[14];

        btnUse.KeyShortcut = KeyHandler.KeyMap[3];
        btnUse.SetStandardToolTip("Use Terrain@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[3]), -1);

        btnMapSml.KeyShortcut = KeyHandler.KeyMap[25];
        btnMapSml.SetStandardToolTip("Map View@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[25]), -1);

        btnCombat.KeyShortcut = KeyHandler.KeyMap[9];
        btnCombat.SetStandardToolTip("Begin Combat@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[9]), -1);

        btnAlchemy.KeyShortcut = KeyHandler.KeyMap[7];
        btnAlchemy.SetStandardToolTip("Do Alchemy@n@iKey Shortcut: @b" + KeyHandler.GetStringFromKeys(KeyHandler.KeyMap[7]), -1);
    }

    public override bool Handle()
    {
        if (Action.LockActions > eAction.NONE || Game.PlayerTargeting)
            return false;
        return base.Handle();
    }

    public static bool CombatEnabled { get => instance.btnCombat.Enabled;
        set => instance.btnCombat.Enabled = value;
    }

    public override void Draw(SpriteBatch sb, int partial = 0)
    {
        var wpos = GetWindowPos();
        sb.Draw(Gfx.TextBarGfx, wpos, Color.White);
        base.Draw(sb);

        var txt = "";

        //Draw textbar text
        if (Game.Mode == eMode.COMBAT)
        {
            //Players or monster's turn?
            if (Party.ActivePC != null)
                txt = String.Format("{0} (ap:{1})", Party.ActivePC.Name, Party.ActivePC.AP);
        }
        else
        {
            //Draw info rect string if pc/party is in one.
            txt = Game.CurrentMap.GetInfoRectString(Party.Pos);
            if (txt == null) txt = Game.CurrentMap.Name; //Otherwise just the map name
        }
        sb.DrawString(Gfx.TinyFont, txt, new Vector2(4, 4) + wpos, Color.White);
    }

    private void pressAct(Control b) { new Action(eAction.Act); }
    private void pressDefend(Control b) { new Action(eAction.Parry); }
    private void pressRest(Control b) { new Action(eAction.StartRest); }
    private void pressWait(Control b) { new Action(eAction.Wait); }
    private void pressUse(Control b) { new Action(eAction.TargetUse); }
    private void pressSave(Control b) { new Action(eAction.QuickSave); }
    private void pressLoad(Control b) { new Action(eAction.QuickLoad); }

    private void pressMagic(Control b)
    {
        if (b == btnCastMage)
            new Action(eAction.ChooseMagicM);
        else
            new Action(eAction.ChooseMagicP);
    }

    private void pressAlchemy(Control b)
    {
        new Action(eAction.DoAlchemy);
    }

    private void pressMap(Control b) { Gfx.MapZoom(); }
    private void pressLook(Control b) { new Action(eAction.TargetSearch); }
    private void pressStartCombat(Control button_pressed) { new Action(eAction.StartCombat); }
    private void pressEndCombat(Control button_pressed) { new Action(eAction.EndCombat); }
    private void pressTalk(Control button_pressed) { new Action(eAction.TargetTalk) { PC = Party.ActivePC }; }

    private void pressGather(Control button_pressed)
    {
        new Action(eAction.GatherLoot);
    }

    private void pressRanged(Control b)
    {
        new Action(eAction.TargetFireRanged);
    }

    public void Update()
    {
        //This should be run when the mode changes and every time something happens that might disable a button.
        //Not having a ranged weapon or matching ammo equipped disables ranged attack button
        //Not having spell levels disables magic buttons

        switch (Game.Mode)
        {
            case eMode.OUTSIDE:
                btnCamp.Visible = true; btnDefend.Visible = false; btnTalk.Visible = false;
                btnMap.Visible = true; btnLoot.Visible = false; btnGather.Visible = false;
                btnSave.Visible = true; btnWait.Visible = false; btnRanged.Visible = false; btnUse.Visible = false; btnMapSml.Visible = false;
                btnLoad.Visible = true; btnEnd.Visible = false; btnAct.Visible = false; btnCombat.Visible = false;
                btnAlchemy.Visible = true;
                break;
            case eMode.COMBAT:
                btnCamp.Visible = false; btnDefend.Visible = true; btnTalk.Visible = false;
                btnMap.Visible = false; btnLoot.Visible = true; btnGather.Visible = false;
                btnSave.Visible = false; btnWait.Visible = true; btnRanged.Visible = true; btnUse.Visible = false; 
                btnLoad.Visible = false; btnEnd.Visible = true; btnAct.Visible = true; btnCombat.Visible = false;
                btnMapSml.Visible = true; btnMapSml.Position(Gfx.WinW, Gfx.WinH,-1,-1); //Kludge. Put it just off screen so it can be pressed via key shortcut
                btnAlchemy.Visible = false;
                break;
            case eMode.TOWN:
                btnCamp.Visible = false; btnDefend.Visible = false; btnTalk.Visible = true;
                btnMap.Visible = false; btnLoot.Visible = false; btnGather.Visible = true;
                btnSave.Visible = false; btnWait.Visible = false; btnRanged.Visible = false; btnUse.Visible = true; 
                btnMapSml.Visible = true; btnMapSml.Position(185, 40,-1,-1);
                btnLoad.Visible = false; btnEnd.Visible = false; btnAct.Visible = false; btnCombat.Visible = true;
                btnAlchemy.Visible = true;
                break;
        }
    }

}