using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    class IdentifyWindow : GuiWindow
    {
        ConversationWindow calledFromTalk;

        public IdentifyWindow(ConversationWindow calledfromtalk, string msg, int price)
            : base(0, 0, 272, 200, true, true, false, true, true)
        {
            Action.LockActions = eAction.INVENTORY_LOCKED_ACTIONS; //Don't pause the world, but prevent the player doing anything not inventory related
            Position(-2, -2);
            calledFromTalk = calledfromtalk;

            int y = 5;
            Label l = AddLabel(msg, 5, y, 240, -1, true);
            y += l.Height + 10;
            IdentifyBox i = new IdentifyBox(this, new XnaRect(5, y, 240, 100), price, -1);
            controls.Add(i);
            Gui.ServiceBoxOpen = i;
            y += i.Height + 10;
            var b = AddButton(pressDone, "Done", 193, y);
            y += b.Height + 5;
            Resize(272, y + Gfx.FRAME_HEIGHT * 2);

            OKKeyControl = b;

            InventoryWindow.Reveal(Party.CurrentPC);

        }

        public override void Close()
        {
            base.Close();
            Gui.ServiceBoxOpen = null;
            Gui.DragItem = null;
            if (calledFromTalk != null)
            {
                calledFromTalk.Visible = true;
            }
            Action.LockActions = eAction.NONE;
        }

        void pressDone(Control b)
        {
            KillMe = true;
        }

        public class IdentifyBox : Control
        {
            string Msg;
            string defMsg;
            Item lastIdentified = null;
            public int Price = 0;


            public IdentifyBox(GuiWindow p, XnaRect r, int price, int tno)
                : base(p, r.X, r.Y, r.Width, r.Height, tno)
            {
                Price = price;
                Msg = defMsg = "Drag an item here to\nidentify it for " + price + " gold";
            }

            public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
            {
                if (!Visible) return;
                if (TabNo != -1 && TabNo != parent.currentTab) return;

                int dx = X + xOffset, dy = Y + yOffset;

                Gfx.DrawFrame(dx, dy, Width, Height, Color.DarkSlateGray);

                if (Msg.Length > 0)
                {
                    var v = Gfx.SmallBoldFont.MeasureString(Msg);
                    v.Width = Maths.Floor(((Width - v.Width) / 2) + dx);
                    v.Height = Maths.Floor(((Height - v.Height) / 2) + dy);
                    sb.DrawString(Gfx.SmallBoldFont, Msg, v, Color.White);
                }
            }

            public override bool Handle(int xOffset, int yOffset)
            {
                if (!Enabled || !Visible) return false;

                int dx = X + xOffset, dy = Y + yOffset;

                if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height) //Mouse within bounds of box?
                {
                    if (Gui.DragItem != null)
                        if (Gui.DragItem == lastIdentified)
                        {
                            Msg = Gui.DragItem.ShortName + " identified as\n'" + Gui.DragItem.Name + "'";
                            return false;
                        }
                        else
                        {
                            {
                                if (Gui.DragItem.Identified) { Msg = "Item is already identified"; return false; }
                                if (Game.CurrentParty.Gold < Price) { Msg = "You don't have " + Price + " gold"; return false; }

                                if (Gui.LMBHitUp)
                                {
                                    Gui.DragItem.Identify(Price);
                                    Msg = Gui.DragItem.ShortName + " identified as\n'" + Gui.DragItem.Name + "'";
                                    lastIdentified = Gui.DragItem;
                                    return true;
                                }
                            }
                        }
                }
                Msg = defMsg;
                return false;
            }
        }

    }
}