using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class InventoryWindow : GuiWindow
{
    private static InventoryWindow instance;
    private PictureButton[] pcButtons = new PictureButton[6];
    private PictureButton specialItems;
    private InventoryBox inventoryBox;
    private List<EquipmentSlot> equipBoxes = new();
    private XnaRect gfxSrcRectTop = new(0, 99, 269, 34);

    public static void Reveal(PCType pc, bool toggle=false)
    {
        if (toggle && (pc == Game.CurrentParty.CurrentPC && instance.Visible == true))
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
        instance.inventoryBox.ChangeOwner(Game.CurrentParty.CurrentPC);
        foreach (var eq in instance.equipBoxes) eq.ChangeOwner(Game.CurrentParty.CurrentPC);
    }
    public new static void Close()
    {
        if (instance != null) instance.Visible = false;
        instance = null;
    }

    public InventoryWindow()
        : base(140, 30, 291, Gfx.WinH - 200, true, true, false, true, true)
    {
        instance = this;
        inventoryBox = AddInventoryBox(Party.CurrentPC, new XnaRect(0, 187, 253, Height - 246));

        int[] pc_button_pos = { 11, 40, 69, 98, 127, 156 };

        var n = 0;
        foreach (var pc in Party.PCList)
        {
            pcButtons[n] = AddPictureButton(pressButtons, pc.GetGraphicRect(true), pc.PCTexture, new XnaRect(pc_button_pos[n], inventoryBox.Height + 187, 18, 18));
            n++;
        }

        //1 Main hand     1-handed weapon / 2 handed weapon
        //2 Off-hand      Shield / 2 handed-weapon
        //3 Ranged Weapon Bow / crossbow / discs
        //4 Ammo          Arrows / Bolts
        //5 Head          Helmet
        //6 Hands         Gloves
        //7 Feet          Boots
        //8 Ring1
        //9 Ring2
        //10 Necklace
        //11 Legs          Trousers

        equipBoxes.Add(AddEquipmentSlot(5, 22, Party.CurrentPC, "Main Hand", eEquipSlot.MainHand));
        equipBoxes.Add(AddEquipmentSlot(95, 22, Party.CurrentPC, "Off Hand", eEquipSlot.OffHand));
        equipBoxes.Add(AddEquipmentSlot(185, 22, Party.CurrentPC, "Ranged", eEquipSlot.Ranged));
        equipBoxes.Add(AddEquipmentSlot(5, 63, Party.CurrentPC, "Ammo", eEquipSlot.Ammo));
        equipBoxes.Add(AddEquipmentSlot(95, 63, Party.CurrentPC, "Head", eEquipSlot.Head));
        equipBoxes.Add(AddEquipmentSlot(185, 63, Party.CurrentPC, "Hands", eEquipSlot.Hands));
        equipBoxes.Add(AddEquipmentSlot(5, 104, Party.CurrentPC, "Feet", eEquipSlot.Feet));
        equipBoxes.Add(AddEquipmentSlot(95, 104, Party.CurrentPC, "Legs", eEquipSlot.Legs));
        equipBoxes.Add(AddEquipmentSlot(170, 104, Party.CurrentPC, "", eEquipSlot.Ring1));
        equipBoxes.Add(AddEquipmentSlot(200, 104, Party.CurrentPC, "Rings", eEquipSlot.Ring2));
        equipBoxes.Add(AddEquipmentSlot(95, 145, Party.CurrentPC, "Necklace", eEquipSlot.Necklace));
        equipBoxes.Add(AddEquipmentSlot(185, 145, Party.CurrentPC, "Torso", eEquipSlot.Torso));
        equipBoxes.Add(AddEquipmentSlot(5, 145, Party.CurrentPC, "Tool", eEquipSlot.Tool));

        specialItems = new PictureButton(this, pressButtons, new XnaRect(176, 242, 35, 15), Gfx.StatAreaGfx, new XnaRect(176, 190 + inventoryBox.Height, 35, 15), -1);
        controls.Add(specialItems);
        specialItems.SetStandardToolTip("Display a window listing the Special Items your party has acquired in this scenario.",200);
        Visible = false;

        AllowResizing(300, Height, Gfx.WinH);
    }

    public override void Resize(int w, int h)
    {
        base.Resize(w, h);

        inventoryBox.Resize(inventoryBox.Width, Height - 246);

        foreach (var b in pcButtons)
            b.Y = inventoryBox.Height + 187;
        specialItems.Y = inventoryBox.Height + 190;
    }

    private void pressButtons(Control button_pressed)
    {
        var pcb = -1;

        if (button_pressed == pcButtons[0]) pcb = 0;
        else if (button_pressed == pcButtons[1]) pcb = 1;
        else if (button_pressed == pcButtons[2]) pcb = 2;
        else if (button_pressed == pcButtons[3]) pcb = 3;
        else if (button_pressed == pcButtons[4]) pcb = 4;
        else if (button_pressed == pcButtons[5]) pcb = 5;
        else if (button_pressed == specialItems)
        {
            SpecialItemsWindow.Reveal();
            return;
        }

        if (pcb != -1)
        {
            var pc = Party.PCList[pcb];
            Party.CurrentPC = pc;
        }
    }

    protected override void pressWindowClose(Control button_pressed)
    {
        Visible = false;
    }

    public override void Draw(SpriteBatch sb, int partial = 0)
    {
        if (!Visible || Party.CurrentPC == null) return;

        base.Draw(sb, 1);
        var winpos = GetClientAreaPos();
        var wpos = winpos;
        sb.Draw(Gfx.StatAreaGfx, wpos, new XnaRect(0, 116, 269, 17), Color.White);
        sb.DrawString(Gfx.SmallBoldFont, Party.CurrentPC.Name + " inventory:", wpos + new Vector2(3, 1), Color.White);

        wpos.Y += 186 + inventoryBox.Height;

        sb.Draw(Gfx.StatAreaGfx, wpos, new XnaRect(0, 239, 269, 21), Color.White);
        wpos.Y += 21;
        sb.Draw(Gfx.StatAreaGfx, wpos, new XnaRect(0, 99, 269, 17), Color.White);

        wpos.X += 37; wpos.Y++;
        sb.DrawString(Gfx.BoldFont, Party.Food.ToString(), wpos, Color.White);

        wpos.X += 71;
        sb.DrawString(Gfx.BoldFont, Party.Gold.ToString(), wpos, Color.White);

        wpos.X += 69;
        sb.DrawString(Gfx.BoldFont, Party.Day.ToString(), wpos, Color.White);

        base.Draw(sb, 2);

        if ((Game.Mode == eMode.COMBAT && Party.CurrentPC != Party.ActivePC)
            || Party.CurrentPC.LifeStatus == eLifeStatus.ABSENT)
            sb.Draw(Gfx.NewGui, new XnaRect((int)winpos.X, (int)winpos.Y, InnerWidth, InnerHeight), new XnaRect(20,20,1,1), Color.FromNonPremultiplied(255, 255, 255, 125));

    }

}