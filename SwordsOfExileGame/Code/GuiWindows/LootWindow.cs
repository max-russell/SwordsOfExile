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

    class LootWindow : GuiWindow
    {
        public static bool IsOpen = false;
        public LootSpot Inventory;
        InventoryBox inventoryBox;
        Button okButton, takeAllButton;

        public LootWindow(LootSpot loot)
            : base(0, 0, 300, 350, true, true, false, true, true)
        {
            IsOpen = true;
            Action.LockActions = eAction.INVENTORY_LOCKED_ACTIONS;//true; //Don't pause the world, but prevent the player doing anything not inventory related
            Inventory = loot;
            Position(-1, 0, -50, 50);

            string desc = "";
            if (!loot.Gathering)
            {
                if (Game.CurrentTown.FieldThere(loot.Pos, Field.CRATE))
                    desc = "Looking in the crate:";
                else if (Game.CurrentTown.FieldThere(loot.Pos, Field.BARREL))
                    desc = "Looking in the barrel:";
                else
                    desc = "Looking in " + Game.CurrentTown.TerrainAt(loot.Pos).Name + ":";
            }
            else
                desc = "Nearby items found:";

            AddLabel(desc, 5, 0, -1, -1, false);

            //Title = loot.Gathering ? "Gathering" : "Searching";
            inventoryBox = AddInventoryBox(Inventory, new XnaRect(5, 20, Gfx.ITEMGFXWIDTH * 9/* 240*/, 252), true);
            takeAllButton = AddButton(pressTakeAll, "Take all", 5, 280);
             
            okButton = AddButton(pressDone, "Done", 221, 280);
            OKKeyControl = okButton; //b.KeyShortcut = Keys.Enter;
            CancelKeyControl = okButton;

            AllowResizing(300,Height, Gfx.WinH);

            //Gui.KeyFocusWindow = this;

            InventoryWindow.Reveal(Party.CurrentPC);
        }

        public override void Resize(int w, int h)
        {
            base.Resize(w, h);
            inventoryBox.Resize(inventoryBox.Width, Height - 98);
            okButton.Y = Height - 70;
            takeAllButton.Y = Height - 70;
        }

        public override void Close()
        {
            base.Close();
            //Put all the items in the inventory back where they belong.
            IsOpen = false;
            Gui.DragItem = null;
            Inventory.Finish();
            Action.LockActions = eAction.NONE;// false;
        }

        void pressTakeAll(Control button_pressed)
        {
            ////TODO: Take All in loot window 
            //Action.Requested = eAction.TakeAllItems;
            //Action.InventoryFrom = Inventory;
            //if (Game.Mode == eMode.COMBAT)
            //    Action.PC = Game.CurrentParty.ActivePC;
            //else
            //    Action.PC = Game.CurrentParty.CurrentPC;

            new Action(eAction.TakeAllItems)
            {
                InventoryFrom = Inventory,
                PC = Game.Mode == eMode.COMBAT ? Game.CurrentParty.ActivePC : Game.CurrentParty.CurrentPC
            };

        }

        void pressDone(Control b)
        {
            //Close();
            KillMe = true;
        }

    }

}