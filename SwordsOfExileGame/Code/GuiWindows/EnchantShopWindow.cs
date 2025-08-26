using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal class EnchantingWindow : GuiWindow
{
    private ConversationWindow calledFromTalk;

    public EnchantingWindow(ConversationWindow calledfromtalk, string msg, eEnchantShop type)
        : base(0, 0, 272, 200, true, true, false, true, true)
    {
        Action.LockActions = eAction.INVENTORY_LOCKED_ACTIONS;//Don't pause the world, but prevent the player doing anything not inventory related
        Position(-2, -2);
        calledFromTalk = calledfromtalk;

        var y = 5;
        var l = AddLabel(msg, 5, y, 240, -1, true);
        y += l.Height + 10;
        var i = new EnchantingBox(this, new XnaRect(5, y, 240, 100), type, -1);
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

    private void pressDone(Control b)
    {
        KillMe = true;
    }

    public class EnchantingBox : Control
    {
        private Item lastEnchanted = null;
        public eEnchantShop Enchantment;
        private string Msg;

        public EnchantingBox(GuiWindow p, XnaRect r, eEnchantShop type, int tno)
            : base(p, r.X, r.Y, r.Width, r.Height, tno)
        {
            Enchantment = type;
            setInstructionMsg();
        }

        private void setInstructionMsg()
        {
            switch (Enchantment)
            {
                case eEnchantShop.PLUS_1:
                    Msg = "Drag a weapon here to purchase\na +1 enchantment";
                    break;
                case eEnchantShop.PLUS_2:
                    Msg = "Drag a weapon here to purchase\na +2 enchantment";
                    break;
                case eEnchantShop.PLUS_3:
                    Msg = "Drag a weapon here to purchase\na +3 enchantment";
                    break;
                case eEnchantShop.BLESSED:
                    Msg = "Drag a weapon here to purchase\na blessing enchantment";
                    break;
                case eEnchantShop.FLAMING:
                    Msg = "Drag a weapon here to purchase\na flaming enchantment";
                    break;
                case eEnchantShop.PLUS_5:
                    Msg = "Drag a weapon here to purchase\na +5 enchantment";
                    break;
                case eEnchantShop.SHOOT_FLAMES:
                    Msg = "Drag a weapon here to purchase\na Fire enchantment";
                    break;
            }
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
                    if (Gui.DragItem == lastEnchanted)
                    {
                        Msg = Gui.DragItem.ShortName + " is now '" + Gui.DragItem.Name + "'";
                        return false;
                    }
                    else
                    {
                        if (!Gui.DragItem.Identified) { Msg = "Item must be identified"; return false; }
                        if (!Gui.DragItem.IsWeapon()) { Msg = "Can only enchant weapons"; return false; }
                        if (Gui.DragItem.Ability != eItemAbil.NO_ABILITY) { Msg = "Item must not already have an ability"; return false; }
                        if (Gui.DragItem.Magic) { Msg = "Can only enchant non-magic items"; return false; }

                        var cost = EnchantCost(Gui.DragItem);
                        if (Game.CurrentParty.Gold < cost) { Msg = "You need " + cost + " gold\nto enchant that"; return false; }

                        if (Gui.LMBHitUp)
                        {
                            Gui.DragItem.Enchant(Enchantment, cost);
                            Msg = Gui.DragItem.ShortName + " is now '" + Gui.DragItem.Name + "'";
                            lastEnchanted = Gui.DragItem;
                            return true;
                        }
                        else
                        {
                            Msg = "Enchant for " + cost + " gold?";
                            return false;
                        }
                    }
            }
            setInstructionMsg();
            return false;
        }

        public int EnchantCost(Item item)
        {
            short[] aug_cost = { 4, 7, 10, 8, 15, 15, 10, 0, 0, 0 };

            if (item.BaseValue <= 1400)
                return Maths.Max(aug_cost[(int)Enchantment] * 100, item.BaseValue * (5 + aug_cost[(int)Enchantment]));//original
            else
                return 1400 * (5 + aug_cost[(int)Enchantment]) + (30000 - 1400 * (5 + aug_cost[(int)Enchantment])) * (item.BaseValue - 1400) / 8600;//really smoothen the price curve
        }
    }
}