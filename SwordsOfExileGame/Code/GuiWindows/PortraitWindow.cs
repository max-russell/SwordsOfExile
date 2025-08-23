using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class PortraitWindow : GuiWindow
{
    private PictureBox[] afflictBoxes = new PictureBox[14];

    public const int HEIGHT = 90;
    private PictureButton inventoryButton, statsButton;
    public PCType PC;
    private bool pressed, pressedLMB;

    public PortraitWindow(PCType pc, int num)
        : base(10, num * HEIGHT + 10, 64 + Gfx.FRAME_WIDTH + 24, 64 + Gfx.FRAME_HEIGHT * 2, true, false, false, false, false)
    {
        PC = pc;
        inventoryButton = AddPictureButton(pressInventory, new XnaRect(63, 0, 18, 18), Gfx.NewGui, new XnaRect(82, 13, 18, 18));
        statsButton = AddPictureButton(pressStats, new XnaRect(81, 0, 18, 18), Gfx.NewGui, new XnaRect(82, 31, 18, 18));

        inventoryButton.SetStandardToolTip("Show/Hide Inventory@nfor " + PC.Name);
        statsButton.SetStandardToolTip("Show/Hide Skills & Stats@nfor " + PC.Name);

        int x = 0, y = 0;
        for (var n = 0; n < 14; n++)
        {
            afflictBoxes[n] = AddPictureBox(Gfx.MixedGfx, XnaRect.Empty, new XnaRect(x + 14, y + 13, 12, 12));
            afflictBoxes[n].Visible = false;
            x += 12;
            if (x >= 5 * 12) { x = 0; y += 12; }
        }

    }

    public override void Draw(SpriteBatch sb, int partial = 0)
    {
        var wpos = GetWindowPos();
        var r = new XnaRect(5, 145, 94, 92);
        sb.Draw(Gfx.NewGui, wpos, r, PC == Party.ActivePC && Game.Mode == eMode.COMBAT ? Color.Red: Color.White);


        sb.Draw(PC.PortraitTexture, new XnaRect((int)wpos.X + 16, (int)wpos.Y + 14, 64, 64),PC.LifeStatus == eLifeStatus.ALIVE ? Color.White : Color.DarkGray);// new XnaRect((num % 10) * 32, (num / 10) * 32, 32, 32), col);

        if (PC.IsAlive())
        {
            if (PC.Health < PC.MaxHealth)
            {
                var h = 64 - (int)(((float)PC.Health / (float)PC.MaxHealth) * 64f);
                Gfx.DrawRect((int)wpos.X + 16, (int)wpos.Y + 14 + (64 - h), 64, h, new Color(255, 0, 0, 128), true);
            }
            if ((PC.GetSkill(eSkill.MAGE_SPELLS) > 0 || PC.GetSkill(eSkill.PRIEST_SPELLS) > 0))
            {
                sb.Draw(Gfx.NewGui, wpos + new Vector2(16 + 56, 14), new XnaRect(115, 148, 8, 64), Color.White);
                var h = (int)(((float)PC.SP / (float)PC.MaxSP) * 64);
                sb.Draw(Gfx.NewGui, wpos + new Vector2(16 + 56, 14 + 64 - h), new XnaRect(103, 148, 8, h), Color.White);
            }

        }

        if (MagicWindow.Instance == null)
        {
            if (Party.CurrentPC == PC)
                Gfx.DrawRect((int)wpos.X, (int)wpos.Y, 94, 92, Color.Red, false, 2);
        }
        else
        if (MagicWindow.Instance.Caster == PC)
            Gfx.DrawRect((int)wpos.X, (int)wpos.Y, 94, 92, Color.Teal, false, 2);

        base.Draw(sb);

        if (PC.IsAlive())
        {
            if (Game.Mode == eMode.COMBAT)
                sb.DrawString(Party.ActivePC == PC ? Gfx.BoldFont : Gfx.ItalicFont, "AP: " + PC.AP, new Vector2(wpos.X + 32, wpos.Y + 75), Color.White);

        }
        else
        {
            if (PC.LifeStatus != eLifeStatus.ALIVE)
                sb.DrawString(Gfx.BoldFont, PC.LifeStatusString, new Vector2(wpos.X + 18, wpos.Y + 16), Color.White);   
        }

    }

    public override bool Handle()
    {
        var interacted = base.Handle();

        var cbox = 0;
        int[] xp = { 12, 24, 0, 0, 24, 0, 12, 24, 0, 12, 24, 0, 12, 24 };
        int[] yp = { 67, 55, 55, 79, 67, 91, 91, 91, 103, 103, 103, 115, 115, 115 };

        foreach (var pb in afflictBoxes) pb.Visible = false;

        for (var a = 0; a < 14; a++)
        {
            var s = PC.Status((eAffliction)a);

            if (s > 0)
            {
                afflictBoxes[cbox].Visible = true;

                var tooltip = String.Format("@b{0}@e@n@i{1}", PCType.StatusMsg(PC, (eAffliction)a), PC.AfflictionHlp[a]);

                afflictBoxes[cbox].SetStandardToolTip(tooltip, 150);
                if ((eAffliction)a == eAffliction.POISON && s >= 4)
                {
                    afflictBoxes[cbox].SetPicture(Gfx.MixedGfx, new XnaRect(12, 55, 12, 12));
                    cbox++;
                }
                else
                {
                    afflictBoxes[cbox].SetPicture(Gfx.MixedGfx, new XnaRect(xp[a], yp[a], 12, 12));
                    cbox++;
                }
            }
            else if (((eAffliction)a == eAffliction.HASTE_SLOW || (eAffliction)a == eAffliction.BLESS_CURSE) && s < 0)
            {
                afflictBoxes[cbox].Visible = true;
                var tooltip = String.Format("@b{0}@e@n@i{1}", PCType.StatusMsg(PC, (eAffliction)a), PC.AfflictionHlp[a]);
                afflictBoxes[cbox].SetStandardToolTip(tooltip, 150);

                if ((eAffliction)a == eAffliction.HASTE_SLOW)
                    afflictBoxes[cbox].SetPicture(Gfx.MixedGfx, new XnaRect(24, 79, 12, 12));
                else
                    afflictBoxes[cbox].SetPicture(Gfx.MixedGfx, new XnaRect(0, 67, 12, 12));
                cbox++;
            }
        }

        int dx = X + 13, dy = Y + 11;
        if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + 64 && Gui.Ms.Y < dy + 64) //Mouse within bounds of face box?
        {
            if (Gui.LMBHit || Gui.RMBHit)
            {
                pressed = true;
                pressedLMB = Gui.LMBDown;
                return true;
            }
            else if (!Gui.LMBDown && !Gui.RMBDown)
            {
                if (pressed)
                {
                    pressed = false;

                    if (!pressedLMB)
                    {
                        if ((Game.Mode != eMode.COMBAT && MagicWindow.Instance != null) || MagicWindow.Instance == null)
                        {
                            var options = new List<PopUpMenuData>();
                            options.Add(new PopUpMenuData("Inventory", PC, null, PopUpMenuData.INVENTORY));
                            options.Add(new PopUpMenuData("Character", PC, null, PopUpMenuData.STATS));

                            if (Action.LockActions == eAction.NONE)
                            {
                                if (PC.Slot > 0) options.Add(new PopUpMenuData("Move up in party order", PC, null, PopUpMenuData.MOVEUPORDER));
                                if (PC.Slot < Constants.PC_LIMIT - 1) options.Add(new PopUpMenuData("Move down in party order", PC, null, PopUpMenuData.MOVEDOWNORDER));
                            }
                            if (options.Count > 0)
                            {
                                new PopUpMenu(popupMenuHandler, options);
                            }
                        }
                    }
                    else
                    {
                        if (Gui.DragItem != null && PC != Gui.DragItemFrom)
                        {
                            if (!PC.InventorysClose(Gui.DragItemFrom))
                            {
                                Game.AddMessage("Item move: Too far away.");
                                return true;
                            }

                            if (Gui.DragItemFrom is PCType && PC.HasEquipped(Gui.DragItem) != eEquipSlot.None)
                                if (((PCType)Gui.DragItemFrom).Unequip(Gui.DragItem) == null)
                                    return true;
                            if (!Gui.DragItemFrom.RemoveItem(Gui.DragItem))
                                return true;
                            PC.AddItem(Gui.DragItem, true);
                            Gui.DragItem = null;
                        }
                        else
                        {
                            new Action(eAction.ChangeCurrentPC) { PC = PC };
                        }
                    }
                    return true;

                }
                else
                {
                    foreach (var pb in afflictBoxes)
                    {
                        if (pb.Visible && (Gui.Ms.X >= X + pb.X && Gui.Ms.Y >= Y + pb.Y && Gui.Ms.X < X + pb.X + pb.Width && Gui.Ms.Y < Y + pb.Y + pb.Height))
                            return interacted;
                    }

                    new ToolTipV2(false, new XnaRect(dx, dy, 64, 64), PC.TooltipInfo(false), -1);
                }
            }
        }

        return interacted;

    }

    private void pressInventory(Control b)
    {
        new Action(eAction.ShowInventoryWin) { PC = PC };
    }

    private void pressStats(Control b)
    {
        new Action(eAction.ShowCharacterWin) { PC = PC };
    }

    private void popupMenuHandler(object o_pc, object nuttin, int what)
    { 
        switch (what)
        {
            case PopUpMenuData.MOVEUPORDER:
            case PopUpMenuData.MOVEDOWNORDER:
                Party.ReorderPC((PCType)o_pc, what);
                break;
            case PopUpMenuData.INVENTORY:
                new Action(eAction.ShowInventoryWin) { PC = PC };
                break;
            case PopUpMenuData.STATS:
                new Action(eAction.ShowCharacterWin) { PC = PC };
                break;
        }
    }

    public void SetShortcuts(bool turn_on)
    {
        inventoryButton.KeyShortcut = turn_on ? KeyHandler.KeyMap[28] : Keys.None;
        statsButton.KeyShortcut = turn_on ? KeyHandler.KeyMap[29] : Keys.None;
    }
}