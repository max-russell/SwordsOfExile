using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal delegate void PopUpHandler(object o, object o2, int data);

public class PopUpMenuData
{
    public const int EQUIP = 1, UNEQUIP = 2, DROP = 3, TAKE = 4, INFO = 5, USE = 6, TAKE_ALL = 7, TALK_TO = 8, SEARCH = 9, GIVE = 10,
        MOVEUPORDER = 11, MOVEDOWNORDER = 12, BUY = 13, SELL = 14, IDENTIFY = 15, ENCHANT = 16, INVENTORY = 17, STATS = 18;

    public string Name;
    public object Object, Object2;
    public int Data;

    public PopUpMenuData(string name, object obj, object obj2, int data)
    {
        Name = name;
        Object = obj;
        Object2 = obj2;
        Data = data;
    }
}

internal class PopUpMenu : GuiWindow
{
    private PopUpMenuOption[] menuButtons;
    private PopUpHandler popupHandler;
    private List<PopUpMenuData> optionList;

    public PopUpMenu(PopUpHandler handler, List<PopUpMenuData> options)
        : base(0, 0, 10, 10, true, false, true, true, false)
    {
        OnTop = true;
        int w = 0, h = 0, x, y;
        popupHandler = handler;
        //Work out size of pop-up menu from option texts
        optionList = options;
        foreach (var op in optionList)
        {
            Vector2 sz = Gfx.GuiFont1.MeasureString(op.Name);
            h += (int)sz.Y;
            if (sz.X > w) w = (int)sz.X;
        }
        w += ClientX * 2; h += ClientY * 2; //Add borders
        //Work out position based on mouse pointer. If it will fit on screen, menu should appear below-right,
        //otherwise, try somewhere else.
        if (Gui.Ms.X + w < Gfx.WinW) x = Gui.Ms.X;
        else x = Gui.Ms.X - w;
        if (Gui.Ms.Y + h < Gfx.WinH) y = Gui.Ms.Y;
        else y = Gui.Ms.Y - h;

        //Reposition and resize the menu accordingly
        base.Move(x, y, w, h);

        //Add the menu buttons
        menuButtons = new PopUpMenuOption[options.Count];
        var c = 0; y = 0; w -= ClientX * 2;
        foreach (var o in optionList)
        {
            Vector2 sz = Gfx.GuiFont1.MeasureString(o.Name);
            menuButtons[c] = new PopUpMenuOption(this, null, o.Name, y, w, (int)sz.Y);
            controls.Add(menuButtons[c]);
            y += (int)sz.Y;
            c++;
        }
    }

    public override bool Handle()
    {
        var interacted = base.Handle();

        //If user clicks outside menu, close it down
        if (!MouseIsInside() && (Gui.LMBDown || Gui.RMBDown))
        {
            Gui.NeedMouseRelease = true;
            KillMe = true;
            return true;
        }
        if (interacted)
        {
            for (var n = 0; n < menuButtons.Length; n++)
                if (controlEvent == menuButtons[n])
                {
                    KillMe = true;
                    popupHandler.Invoke(optionList[n].Object, optionList[n].Object2, optionList[n].Data);
                    return true;
                }
        }
        return false;

    }
}

internal class PopUpMenuOption : Button
{
    public PopUpMenuOption(PopUpMenu pum, PressControlHandler handler, string txt, int y, int w, int h) : base(pum, handler, txt, 0, y, w, h, 0) { }
    public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
    {
        int dx = X + xOffset, dy = Y + yOffset;
        if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height)
        {
            sb.Draw(Gfx.Dot, new XnaRect(dx, dy, Width, Height), new XnaRect(0, 0, 1, 1), Color.White);
            sb.DrawString(Gfx.GuiFont1, Caption, new Vector2(dx, dy), Color.Black);
        }
        else
            sb.DrawString(Gfx.GuiFont1, Caption, new Vector2(dx, dy), Color.White);
    }

}