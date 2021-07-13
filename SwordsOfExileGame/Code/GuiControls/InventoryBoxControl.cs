using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    class InventoryBox : Control, IScrollBarOwner
    {
        enum eView {GRID, LIST};
        
        eView View = eView.LIST;
        eItemFilter Filter { get {return owner.Filter;} set {owner.Filter = value;}} 

        int pressedSlot; bool pressedButton;
        int tooltipSlot;

        int itemWidth, itemHeight;

        public const int ICONVIEWITEMWIDTH = Gfx.ITEMGFXWIDTH, ICONVIEWITEMHEIGHT = Gfx.ITEMGFXHEIGHT,
                         BIGVIEWITEMWIDTH = (int)(Gfx.ITEMGFXWIDTH * 9), BIGVIEWITEMHEIGHT = Gfx.ITEMGFXHEIGHT,
                         MENUBARHEIGHT = 24;

        int rows;

        const int BORDER_WIDTH = 0, BORDER_HEIGHT = 0;

        IInventory owner;
        VScrollBar vScroll;
        Button viewButton, arrangeButton, filterButton;
        bool useShortcuts = false;

        int itemsAcross { get { return Width / itemWidth; } }
        int itemsDown { get { return (Height - MENUBARHEIGHT) / itemHeight; } }
        Vector2 getItemPosinBox(int slot)
        {
            return new Vector2((slot % itemsAcross) * itemWidth, (slot / itemsAcross) * itemHeight - scrollViewPos);
        }

        int scrollViewPos;
        int scrollFullHeight;

        const string viewTooltip = "Toggle the inventory view";
        const string arrangeTooltip = "Automatically sorts and stacks items in the inventory.";
        const string filterTooltip = "Filter items in the inventory by type";



        public InventoryBox(GuiWindow p, IInventory owns, XnaRect r, int tno, bool use_shortcuts)
            : base(p, r.X, r.Y, r.Width, r.Height, tno)
        {   
            owner = owns;
            useShortcuts = use_shortcuts;

            vScroll = new VScrollBar(this, parent, MENUBARHEIGHT, Height - MENUBARHEIGHT, 0, 1, 0, 1, itemHeight);

            parent.controls.Add(viewButton = new Button(parent, pressButton, "List View", X, Y, 70, MENUBARHEIGHT,-1));
            parent.controls.Add(arrangeButton = new Button(parent, pressButton, "Arrange", X + viewButton.Width, Y, 60, MENUBARHEIGHT, -1));
            parent.controls.Add(filterButton = new Button(parent, pressButton, "Show: All Items", X + viewButton.Width + arrangeButton.Width, Y, 140, MENUBARHEIGHT, -1));

            viewButton.SetStandardToolTip(viewTooltip,200);
            arrangeButton.SetStandardToolTip(arrangeTooltip,200);
            filterButton.SetStandardToolTip(filterTooltip,200);

            setView(eView.LIST);
            pressedSlot = -1;
            scrollViewPos = 0;
            scrollFullHeight = Height;
        }

        public override void Resize(int w, int h)
        {
            base.Resize(w, h);
            vScroll.Height = Height - MENUBARHEIGHT;
            updateView();
        }

        void setView(eView view)
        {
            View = view;
            if (View == eView.GRID)
            {
                itemWidth = ICONVIEWITEMWIDTH;
                itemHeight = ICONVIEWITEMHEIGHT;
                viewButton.Caption = "Grid View";
            }
            else
            {
                itemWidth = BIGVIEWITEMWIDTH;
                itemHeight = BIGVIEWITEMHEIGHT;
                viewButton.Caption = "List View";
            }

        }

        static readonly string[] filterLabels = { "All Items", "Weapons", "Armour/Accessories", "Potions/Poisons", "Useable Items", "Other" };

        void pressButton(Control b)
        {
            if (b == viewButton)
            {
                if (View == eView.LIST)
                    setView(eView.GRID);
                else
                    setView(eView.LIST);
            }
            else if (b == arrangeButton)
            {
                owner.ArrangeItems();
                scrollViewPos = 0;
                updateView();
            }
            else if (b == filterButton)
            {
                var l = new List<PopUpMenuData>();
                for (int n = (int)eItemFilter.ALL; n <= (int)eItemFilter.OTHER; n++)
                    l.Add(new PopUpMenuData(filterLabels[n], null, null, n));
                new PopUpMenu(changeFilter, l);
            }
        }

        void changeFilter(Object o, Object o2, int option)
        {
            Filter = (eItemFilter)option;
            scrollViewPos = 0;
            filterButton.Caption = "Show: " + filterLabels[(int)Filter];
            updateView();
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            if (!Visible) return;
            if (TabNo != -1 && TabNo != parent.currentTab) return;

            int dx = X + xOffset + BORDER_WIDTH, dy = Y + yOffset + BORDER_HEIGHT;

            //Copy the current scissor rect so we can restore it after
            XnaRect currentRect = sb.GraphicsDevice.ScissorRectangle;

            sb.GraphicsDevice.ScissorRectangle = new XnaRect(dx, dy + MENUBARHEIGHT, Width - 2 * BORDER_WIDTH, Maths.Min(Gfx.WinH - (dy + MENUBARHEIGHT), Height - (2 * BORDER_HEIGHT) - MENUBARHEIGHT));

            if (View == eView.LIST)
            {
                sb.Draw(Gfx.NewGui, new XnaRect(dx, dy + MENUBARHEIGHT, Width, Height - MENUBARHEIGHT), new XnaRect(Gfx.frame_hside_l, Gfx.frame_vside_t, Gfx.frame_hside_width, Gfx.frame_vside_height), Color.SlateGray);//backCol);//new Color(255, 255, 255, 127));
            }

            //Draw background
             for (int bx = 0; bx <= Width - 24; bx += itemWidth)
                for (int by = 0 - (scrollViewPos % itemHeight); by < (Height-MENUBARHEIGHT); by += itemHeight)
                    sb.Draw(Gfx.NewGui, new XnaRect(dx + bx, dy + by + MENUBARHEIGHT, Gfx.ITEMGFXWIDTH, Gfx.ITEMGFXHEIGHT), new XnaRect(184, 182, 24, 24), new Color(255, 255, 255, 100));

            //Draw each carryable

            foreach (Tuple<Item, int> c in owner.EachItem())
            {
                Vector2 v = getItemPosinBox(c.Item2);

                if (v.Y >= -itemHeight && v.Y < scrollViewPos + (Height-MENUBARHEIGHT))
                {
                    v.Y += MENUBARHEIGHT;
                    v.X += xOffset + X;
                    v.Y += yOffset + Y;
                    c.Item1.DrawOffMap(sb, v, Color.White);

                    if (View == eView.LIST)
                    {
                        v.X += Gfx.ITEMGFXWIDTH + 4;
                        v.Y += 4;
                        sb.DrawString(Gfx.SmallBoldFont, c.Item1.KnownName, v, Color.White);
                        v.Y += 12;
                        c.Item1.DrawBigViewInfo(sb, v);

                        if (useShortcuts)
                        {
                            if (owner is LootSpot)
                            {
                                char key = (owner as LootSpot).GetShortcutFromItem(c.Item1);
                                if (key != 0)
                                {
                                    v.X += itemWidth - Gfx.ITEMGFXWIDTH - 40;
                                    v.Y -= 8;
                                    sb.DrawString(Gfx.SmallBoldFont, "Ctrl+" + key, v, Color.Orange);
                                }

                            }
                        }

                    }
                }
            }

            //Restore old scissor rectangle.
            sb.GraphicsDevice.ScissorRectangle = currentRect;
        }

        public void ScrollBarUpdate(int pos)
        {
            //Invoked by the VScroll control when the player messes wi' it.
            scrollViewPos = pos;
            updateView();
        }

        void updateView()
        {
            //Calculate the number of rows there are
            int lastslot = -1;

            foreach (Tuple<Item, int>i in owner.EachItem())
                lastslot = Maths.Max(lastslot, i.Item2);

            rows = (int)Math.Ceiling(((double)(lastslot + 1) / (double)itemsAcross)) + 1;
            if (rows < itemsDown) rows = itemsDown;
            int lastrow = rows - itemsDown;
            scrollFullHeight = rows * itemHeight;
            scrollViewPos = vScroll.ChangeValues(scrollViewPos, Height - MENUBARHEIGHT, 0, scrollFullHeight, itemHeight);
        }

        public override bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible) return false;

            updateView();

            if (Action.LockActions >= eAction.MAGIC_LOCK_ACTIONS) return false;

            if (useShortcuts && owner is LootSpot)
            {
                if (KeyHandler.AnyKeysDown(Keys.LeftControl, Keys.RightControl))
                {
                    Keys k = KeyHandler.GetAllKeysHit();
                    if (k >= Keys.A && k <= Keys.Z) KeyHandler.FlushHitKey();

                    Item i = (owner as LootSpot).GetItemFromShortcut(k);
                    if (i != null)
                    {
                        new Action(eAction.TakeItem) { PC = Game.Mode == eMode.COMBAT ? Game.CurrentParty.ActivePC : Game.CurrentParty.CurrentPC, Item = i, InventoryFrom = owner };
                        return true;
                    }
                }
                else
                {
                    if (Game.Mode == eMode.COMBAT && KeyHandler.KeyHit(Keys.F))
                    {
                        KeyHandler.FlushHitKey();
                        parent.KillMe = true;
                        new Action(eAction.EndCombat);
                    }
                }
            }


            int dx = X + xOffset, dy = Y + yOffset;
            if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy + MENUBARHEIGHT && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height) //Mouse within bounds of box?
            {
                //Is button pressed?
                if (Gui.LMBHit || Gui.RMBHit)
                {
                    pressedSlot = getSlotAtMouse(xOffset, yOffset);
                    pressedButton = Gui.LMBDown;
                    return true;
                }
                else if (!Gui.LMBDown && !Gui.RMBDown)
                {
                    int slotatmouse = getSlotAtMouse(xOffset, yOffset);
                    if (pressedSlot == -1)
                    {
                        //Button not pressed and hasn't just been released.
                        if (slotatmouse == tooltipSlot)
                            owner.MakeItemToolTip(owner.GetSlot(tooltipSlot), getSlotRectangle(tooltipSlot, xOffset, yOffset));
                        else
                            tooltipSlot = slotatmouse;
                        return false;
                    }
                    else
                    { 
                        if (pressedSlot == slotatmouse)
                        {
                            if (Game.Mode == eMode.COMBAT && owner != Game.CurrentParty.ActivePC)
                            {
                                Game.AddMessage("During combat, only the active character may access their inventory.");
                            }
                            else if (owner is PCType && ((PCType)owner).LifeStatus == eLifeStatus.ABSENT)
                            {
                                Game.AddMessage("Cannot access an absent character's inventory");
                            }
                            else
                            {
                                if (pressedButton) //Left mouse button was pressed - Do the default action for this inventory.
                                {
                                    if (Gui.DragItem != null) //Dragging an item to here
                                    {
                                        new Action(eAction.PlaceInInventory) { Item = Gui.DragItem, InventoryTo = owner, InventoryFrom = Gui.DragItemFrom, Loc = new Location(pressedSlot, 0) };
                                    }
                                    else
                                    {
                                        bool split = KeyHandler.AnyKeysDown(Keys.LeftShift, Keys.RightShift);
                                        Game.StartItemDrag(owner.GetSlot(pressedSlot), owner, split);
                                    }
                                }
                                else
                                { //Right button - bring up menu for object
                                    if (owner.GetSlot(pressedSlot) != null)
                                        owner.MakeInventoryPopUpWindow(owner.GetSlot(pressedSlot));
                                }
                            }

                            pressedSlot = -1;
                            tooltipSlot = -1;
                            return true;
                        }
                    }
                }
            }
            tooltipSlot = -1;
            return false;
        }

        public void ChangeOwner(IInventory inv)
        {
            owner = inv;
        }

        int getSlotAtMouse(int xOffset, int yOffset)
        {

            int sx = Gui.Ms.X - X - xOffset;
            int sy = Gui.Ms.Y - Y - yOffset - MENUBARHEIGHT + scrollViewPos;

            if (sx < Width - 16)
            {
                return (sx / itemWidth) + ((sy / itemHeight) * itemsAcross);
            }
            return -1;
        }

        XnaRect getSlotRectangle(int slot, int xOffset, int yOffset)
        {
            int tx = (slot % itemsAcross) * itemWidth;
            int ty = (slot / itemsAcross) * itemHeight - scrollViewPos;

            int dy = 0;

            if (ty < 0) { dy = 0 - ty; ty = 0; }
            if (ty >= Height - MENUBARHEIGHT) { dy = ty - (Height - MENUBARHEIGHT); ty = (Height - MENUBARHEIGHT) - 1; }

            tx += X + xOffset;
            ty += Y + yOffset + MENUBARHEIGHT;

            return new XnaRect(tx, ty, itemWidth, itemHeight - dy);
        }

        XnaRect getRectAtMouse(int xOffset, int yOffset)
        {
            int sx = Gui.Ms.X - X - xOffset;
            int sy = Gui.Ms.Y - Y - yOffset + scrollViewPos;
            return new XnaRect((sx / itemWidth) * itemWidth, (sy / itemHeight) * itemHeight, itemWidth, itemHeight);
        }

    }

}