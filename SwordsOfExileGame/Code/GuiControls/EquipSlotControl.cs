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
    class EquipmentSlot : Control
    {
        bool pressed = false, pressedLMB = false;
        eEquipSlot SlotType;
        PCType Owner;
        String Text;

        Item getEquippedItem() { return Owner.GetEquipped(SlotType); }

        public EquipmentSlot(GuiWindow p, int x, int y, PCType owner, String txt, eEquipSlot kind, int tabno = -1)
            : base(p, x, y, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT, tabno)
        {
            Owner = owner;
            SlotType = kind;
            Text = txt;
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;
            if (TabNo != -1 && TabNo != parent.currentTab) return;
            int dx = X + xOffset, dy = Y + yOffset;

            sb.Draw(Gfx.NewGui, new XnaRect(dx, dy, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT), new XnaRect(184, 182, 24, 24), new Color(255, 255, 255, 100));

            Vector2 sz = Gfx.GuiFont1.MeasureString(Text);

            sb.DrawString(Gfx.GuiFont1, Text, new Vector2(dx + Gfx.ITEMGFXWIDTH + 5, dy + (Gfx.ITEMGFXHEIGHT - sz.Y) / 2), Color.White);

            Item item = getEquippedItem();

            if (Gui.DragItem != null && Gui.DragItem.CompatibleSlot(SlotType))
                Gfx.DrawRect(dx, dy, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT, Color.Green, false, 2);

            if (item != null)// && item != Gui.DragItem)
            {
                item.DrawOffMap(sb, new Vector2(dx, dy), Color.White);
            }
            else
            {
                //In off-hand slot, if a two handed weapon is equipped in the main hand, draw a faint picture of that weapon.
                if (SlotType == eEquipSlot.OffHand)
                {
                    Item i = Owner.GetEquipped(eEquipSlot.MainHand);
                    if (i != null && i.Variety == eVariety.TwoHanded /*&& Gui.DragItem != i*/)
                    {
                        i.DrawOffMap(sb, new Vector2(dx, dy), Color.FromNonPremultiplied(255, 255, 255, 100));
                    }
                }
            }
        }

        public override bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible) return false;
            if (Action.LockActions >= eAction.MAGIC_LOCK_ACTIONS) return false;

            int dx = X + xOffset, dy = Y + yOffset;
            if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height) //Mouse within bounds of box?
            {
                //Is button pressed?
                if (Gui.LMBHit || Gui.RMBHit)
                {
                    pressed = true;
                    pressedLMB = Gui.LMBDown;
                    return true;
                }
                else if (!Gui.LMBDown && !Gui.RMBDown)
                {
                    //Has button just been released?
                    if (pressed)
                    {

                        pressed = false;

                        if (Game.Mode == eMode.COMBAT && Owner != Game.CurrentParty.ActivePC)
                        {
                            Game.AddMessage("During combat, only the active character may access their inventory.");
                        }
                        else if (Owner is PCType && ((PCType)Owner).LifeStatus == eLifeStatus.ABSENT)
                        {
                            Game.AddMessage("Cannot access an absent character's inventory");
                        }
                        else if (pressedLMB)
                        {
                            if (getEquippedItem() != null && getEquippedItem().Cursed)
                            {
                                Game.AddMessage("Can't remove cursed item!");
                            }
                            else
                            {
                                if (Gui.DragItem != null)
                                {
                                    //Action.Requested = eAction.PlaceInEquipSlot;
                                    //Action.Item = Gui.DragItem;
                                    //Action.InventoryTo = Owner;
                                    //Action.PC = Owner;
                                    //Action.InventoryFrom = Gui.DragItemFrom;
                                    //Action.EquipSlot = SlotType;
                                    new Action(eAction.PlaceInEquipSlot) { Item = Gui.DragItem, InventoryTo = Owner, PC = Owner, InventoryFrom = Gui.DragItemFrom, EquipSlot = SlotType };
                                }
                                else
                                {
                                    bool split = KeyHandler.AnyKeysDown(Keys.LeftShift, Keys.RightShift);
                                    Game.StartItemDrag(getEquippedItem(), Owner, split);
                                }
                            }
                        }
                        else
                        {
                            //Pressed the right mouse button - bring up the menu
                            if (getEquippedItem() != null)
                                Owner.MakeInventoryPopUpWindow(getEquippedItem());
                        }
                        return true;
                    }
                    else
                    {
                        Item i = getEquippedItem();

                        if (i != null)
                            Owner.MakeItemToolTip(i, new XnaRect(dx, dy, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT));
                    }
                }
            }
            return false;
        }

        public void ChangeOwner(PCType pc)
        {
            Owner = pc;
        }

    }
}