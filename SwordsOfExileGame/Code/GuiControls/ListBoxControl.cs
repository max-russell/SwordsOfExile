using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal delegate void ChangeSelectedHandler(bool user_caused, ListBoxItem item);

internal class ListBoxItem
{
    public string Text;
    public bool Italic;
    public object Tag;
    public Color Colour = Color.White;
}

internal class ListBox : Control, IScrollBarOwner
{
    private ChangeSelectedHandler changedHandler;
    public List<ListBoxItem> Items = new();
    private int itemsel;
    private int scrollViewPos; //Amount of pixels control is currently scroll down from top of list area.
    private int scrollFullHeight; //Height of entire list area in pixels
    private int scrollViewHeight; //Height of list area that can fit in the view in pixels
    private BitmapFont listFont = Gfx.SmallBoldFont, listFontItalic = Gfx.ItalicFont;

    private readonly int BORDER_WIDTH, BORDER_HEIGHT;

    private readonly int itemHeight;
    private int visibleitems;
    private VScrollBar vScroll;

    public ListBox(ChangeSelectedHandler handler, GuiWindow p, int xb, int yb, int w, int h, int tno, params ListBoxItem[] list)
        : base(p, xb, yb, w, h, tno)
    {
        BORDER_WIDTH = Gfx.FRAME_WIDTH;
        BORDER_HEIGHT = Gfx.FRAME_HEIGHT;

        changedHandler = handler;

        if (list != null) Items.AddRange(list);
        itemsel = -1;
        itemHeight = (int)listFont.MeasureString("blah!").Height + 6;
        visibleitems = Height / itemHeight;

        scrollFullHeight = itemHeight * Items.Count;
        scrollViewHeight = Height - 2 * BORDER_HEIGHT;
        scrollViewPos = 0;

        vScroll = new VScrollBar(this, parent, 0, Height, scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);//0, visibleitems, 0, Items.Count);

    }

    public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
    {
        if (!Visible) return;
        int dx = X + xOffset, dy = Y + yOffset;

        Gfx.DrawFrame(dx, dy, Width, Height, Color.DarkSlateGray);

        //Copy the current scissor rect so we can restore it after
        var currentRect = sb.GraphicsDevice.ScissorRectangle;
        sb.GraphicsDevice.ScissorRectangle = new XnaRect(dx += BORDER_WIDTH, dy += BORDER_HEIGHT, Width - 2 * BORDER_WIDTH, Height - 2 * BORDER_HEIGHT);

        //Draw each item in the list
        var i = 0;
        var scale = 1f;
        foreach (var item in Items)
        {
            var ypos = i * itemHeight - scrollViewPos;

            if (ypos >= -itemHeight && ypos < scrollViewHeight)
            {

                if (i == itemsel)
                {
                    Gfx.DrawRect(dx, dy + ypos, Width - BORDER_WIDTH * 2, itemHeight, Color.White, true);
                    sb.DrawString(item.Italic ? listFontItalic : listFont, item.Text, new Vector2(dx, dy + ypos), Color.Black, 0f, Vector2.Zero, scale, SpriteEffects.None, 0f);
                }
                else
                    sb.DrawString(item.Italic ? listFontItalic : listFont, item.Text, new Vector2(dx, dy + ypos), item.Colour, 0f, Vector2.Zero, scale, SpriteEffects.None, 0f);

            }
            i++;
        }

        sb.GraphicsDevice.ScissorRectangle = currentRect;



    }

    public override bool Handle(int xOffset, int yOffset)
    {
        if (!Enabled || !Visible) return false;

        int dx = X + xOffset + BORDER_WIDTH, dy = Y + yOffset + BORDER_HEIGHT;

        if (Gui.LMBHit)
        {
            if (Gui.Ms.X >= dx && Gui.Ms.Y >= dy && Gui.Ms.X < dx + Width - 2 * BORDER_WIDTH && Gui.Ms.Y < dy + Height - 2 * BORDER_HEIGHT)
            {
                var sel = (Gui.Ms.Y - dy + scrollViewPos) / itemHeight;
                if (sel < Items.Count)
                {
                    itemsel = sel;
                    if (changedHandler != null) changedHandler.Invoke(true, Items[sel]);
                    return true;
                }  
            }
        }
        return false;
    }

    public override void Position(int x, int y, int xalign, int yalign)
    {
        base.Position(x, y, xalign, yalign);

        vScroll.X = X + Width;
        vScroll.Y = Y;
    }

    public override void Resize(int w, int h)
    {
        base.Resize(w, h);

        scrollViewHeight = Height - 2 * BORDER_HEIGHT;
        scrollViewPos = 0;

        vScroll.X = X + w;
        vScroll.Resize(vScroll.Width, h);
        vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
    }

    public ListBoxItem SelectedItem
    {
        get => itemsel == -1 ? null : Items[itemsel];
        set
        {
            if (value == null)
            {
                itemsel = -1;
                if (changedHandler != null) changedHandler.Invoke(false, null);
            }
            else
            {
                itemsel = Items.IndexOf(value); 
                if (changedHandler != null) changedHandler.Invoke(false, itemsel == -1 ? null : value);
            }
        }
    }

    public void RevealItem(ListBoxItem lb)
    {
        if (lb == null) { vScroll.ChangeValues(scrollViewPos = 0, scrollViewHeight, 0, scrollFullHeight, itemHeight); }
        else
        {
            var i = Items.IndexOf(lb) * itemHeight;

            if (i > scrollViewPos + scrollViewHeight - itemHeight || i < scrollViewPos)
            {
                scrollViewPos = Maths.Min(i, scrollFullHeight - scrollViewHeight);
                vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
            }
        }
    }

    public void ScrollBarUpdate(int pos)
    {
        scrollViewPos = pos;
    }

    public void Clear()
    {
        Items.Clear();
        scrollViewPos = 0;
        scrollFullHeight = 0;
        vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
    }

    public void InsertItem(int pos, string txt, Color colour, object data, bool italic)
    {
        Items.Insert(pos, new ListBoxItem { Text = txt, Colour = colour, Tag = data, Italic = italic });
        scrollFullHeight += itemHeight;
        vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
    }

    public ListBoxItem AddItem(string txt, Color colour, object data, bool italic)
    {
        var i = new ListBoxItem { Text = txt, Colour = colour, Tag = data, Italic = italic };
        Items.Add(i);
        scrollFullHeight += itemHeight;
        vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
        return i;
    }

}