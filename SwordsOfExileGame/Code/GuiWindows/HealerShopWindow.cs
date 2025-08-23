using System.Collections.Generic;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class HealerShopWindow : GuiWindow
{
    private ConversationWindow cameFrom;
    private int priceMod;
    private List<PictureButton> pc_buttons = new();
    private List<Label> pc_labels = new();
    private List<PCType> pcs = new();
    private Label goldLabel;

    public HealerShopWindow(ConversationWindow from, int pricemod)
        : base(220, 30, 200, 500, true, true, false, true, false)
    {
        Action.LockActions = eAction.MAGIC_LOCK_ACTIONS;//Don't pause the world, but prevent the player doing anything not inventory related
        cameFrom = from;
        priceMod = pricemod;

        var lbl = AddLabel("Select a party member to heal:", 10, 10, 240, -1, true);
        var y = lbl.Y + lbl.Height + 10;

        var dr = new XnaRect(10, y, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);

        foreach (var pc in Party.PCList)
        {
            var sr = new XnaRect(0, 0, Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT);
            var opt = AddPictureButton(pressPC, sr, pc.PortraitTexture, dr);
            pc_buttons.Add(opt);
            pcs.Add(pc);

            var l = new Label(this, "", Gfx.PCPORTRAITWIDTH + 20, dr.Y, -1, -1, false, -1);
            pc_labels.Add(l);
            controls.Add(l);

            dr.Y += opt.Height + 10;
        }
        y = dr.Y;

        var btn = AddButton(pressFinish, "Finish", 154, y);
        OKKeyControl = btn;
        CancelKeyControl = btn;

        goldLabel = new Label(this, "", 10, y, -1, -1, true, -1);
        controls.Add(goldLabel);
        setLabels();
        Resize(240, y + btn.Height + 30);
        Position(-2, -2);
    }

    private void setLabels()
    {
        for (var n = 0; n < pc_labels.Count; n++)
        {
            var pc = pcs[n];
            var cost = 0;

            if (pc.LifeStatus is eLifeStatus.DEAD or eLifeStatus.DUST)
            {
                cost = (Constants.RESURRECTION_PRICE * Constants.SHOP_PRICE_MULTIPLIER[priceMod]) / 10;
                pc_labels[n].Text = "Resurrect " + pc.Name + ": " + cost + " gold";
            }
            else if (pc.LifeStatus == eLifeStatus.STONE)
            {
                cost = (Constants.DESTONE_PRICE * Constants.SHOP_PRICE_MULTIPLIER[priceMod]) / 10;
                pc_labels[n].Text = "Destone " + pc.Name + ": " + cost + " gold";
            }
            else if (pc.LifeStatus is eLifeStatus.ABSENT or eLifeStatus.SURFACE or eLifeStatus.WON or eLifeStatus.FLED)
            {
                pc_labels[n].Text = pc.Name + " is absent";
                pc_labels[n].Font = Gfx.ItalicFont;
                pc_buttons[n].Enabled = false;
            }
            else if (pc.Health == pc.MaxHealth)
            {
                pc_labels[n].Text = pc.Name + " is at maximum health.";
                pc_labels[n].Font = Gfx.ItalicFont;
                pc_buttons[n].Enabled = false;
            }
            else
            {
                cost = (Constants.HEAL_PRICE * Constants.SHOP_PRICE_MULTIPLIER[priceMod]) / 10;
                pc_labels[n].Text = "Heal & restore " + pc.Name + ": " + cost + " gold";
            }

            if (cost > Party.Gold)
            {
                pc_labels[n].Font = Gfx.ItalicFont;
                pc_buttons[n].Enabled = false;
            }

        }
        goldLabel.Text = "Gold: " + Party.Gold;
    }

    private void pressPC(Control button_pressed)
    {
        for (var n = 0; n < pc_buttons.Count; n++)
        {
            if (button_pressed == pc_buttons[n])
            {
                var pc = pcs[n];
                if (pc.LifeStatus is eLifeStatus.DEAD or eLifeStatus.DUST)
                    Party.Gold -= (Constants.RESURRECTION_PRICE * Constants.SHOP_PRICE_MULTIPLIER[priceMod]) / 10;
                else if (pc.LifeStatus == eLifeStatus.STONE)
                    Party.Gold -= (Constants.DESTONE_PRICE * Constants.SHOP_PRICE_MULTIPLIER[priceMod]) / 10;
                else
                    Party.Gold -= (Constants.HEAL_PRICE * Constants.SHOP_PRICE_MULTIPLIER[priceMod]) / 10;

                pc.LifeStatus = eLifeStatus.ALIVE;
                pc.Health = pc.MaxHealth;
                pc.SP = pc.MaxSP;
                pc.SetStatus(eAffliction.ACID, 0);
                pc.SetStatus(eAffliction.DISEASE, 0);
                pc.SetStatus(eAffliction.DUMB, 0);
                pc.SetStatus(eAffliction.PARALYZED, 0);
                pc.SetStatus(eAffliction.POISON, 0);
                pc.UnequipCursed();

                setLabels();
                return;
            }
        }
    }


    private void pressFinish(Control b)
    {
        KillMe = true;
    }

    public override void Close()
    {
        base.Close();

        if (cameFrom != null)
        {
            cameFrom.Visible = true;
        }
        Action.LockActions = eAction.NONE;
    }


}