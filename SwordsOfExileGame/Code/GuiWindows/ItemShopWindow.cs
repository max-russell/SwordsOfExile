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
    class ItemShopWindow : GuiWindow
    {
        ConversationWindow calledFromTalk;
        public Shop thisShop;
        Label lblPrice, lblWillBuy;
        InventoryBox inventoryBox;
        Button btnDone;

        public ItemShopWindow(Shop shop, ConversationWindow calledfromtalk)//, string shopname)
            : base(0, 0, 302, 350, true, true, false, true, true)
        {
            Gui.ShopIsOpen = shop;
            thisShop = shop;
            Action.LockActions = eAction.INVENTORY_LOCKED_ACTIONS;////true; //Don't pause the world, but prevent the player doing anything not inventory related
            Position(-2, -2);
            calledFromTalk = calledfromtalk;

            AddLabel(shop.Name, 5, 5, -1, -1, false);
            lblPrice = AddLabel("The prices here are " + thisShop.PriceWord, 5, 276, -1, -1, false);
            lblWillBuy = AddLabel("This shop will buy: " + shop.SellToShopDescription(), 5, 290, -1, -1, false);

            inventoryBox = AddInventoryBox(thisShop, new XnaRect(5, 20, 256, 252));
            btnDone = AddButton(pressDone, "Done", 223, 280);
            OKKeyControl = btnDone; //b.KeyShortcut = Keys.Enter;
            //Gui.KeyFocusWindow = this;
            AllowResizing(Height, Height, Gfx.WinH);

            InventoryWindow.Reveal(Party.CurrentPC);
        }

        public override void Resize(int w, int h)
        {
            base.Resize(w, h);
            inventoryBox.Resize(inventoryBox.Width, Height - 98);
            lblPrice.Y = Height - 74;
            lblWillBuy.Y = Height - 60;
            btnDone.Y = Height - 70;
        }

        public override void Close()
        {
            Gui.ShopIsOpen = null;
            base.Close();
            Gui.DragItem = null;
            if (calledFromTalk != null)
            {
                calledFromTalk.Visible = true;
                //Gui.KeyFocusWindow = calledFromTalk;
            }
            Action.LockActions = eAction.NONE;//false;
        }

        void pressDone(Control b)
        {
            //Close();
            KillMe = true;
        }

    }
}