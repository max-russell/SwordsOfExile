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
    delegate void ChangeSelectedHandler(bool user_caused, ListBoxItem item);

    class ListBoxItem
    {
        public string Text;
        public bool Italic;
        public object Tag;
        public Color Colour = Color.White;
    }

    class ListBox : Control, IScrollBarOwner
    {
        ChangeSelectedHandler changedHandler;
        public List<ListBoxItem> Items = new List<ListBoxItem>();
        int itemsel;
        int scrollViewPos; //Amount of pixels control is currently scroll down from top of list area.
        int scrollFullHeight; //Height of entire list area in pixels
        int scrollViewHeight; //Height of list area that can fit in the view in pixels
        BitmapFont listFont = Gfx.SmallBoldFont, listFontItalic = Gfx.ItalicFont;

        readonly int BORDER_WIDTH, BORDER_HEIGHT;

        readonly int itemHeight;
        int visibleitems;
        VScrollBar vScroll;

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

            //Draw border
            //sb.Draw(Gfx.GuiBits, new XnaRect(dx, dy, Width - 2, 2), new XnaRect(8,24, 1, 1), Color.White);
            //sb.Draw(Gfx.GuiBits, new XnaRect(dx + Width - 2, dy, 2, Height - 2), new XnaRect(8, 24, 1, 1), Color.White);
            //sb.Draw(Gfx.GuiBits, new XnaRect(dx, dy + 2, 2, Height - 2), new XnaRect(8, 24, 1, 1), Color.White);
            //sb.Draw(Gfx.GuiBits, new XnaRect(dx + 2, dy + Height - 2, Width - 2, 2), new XnaRect(8, 24, 1, 1), Color.White);

            Gfx.DrawFrame(dx, dy, Width, Height, Color.DarkSlateGray);

            //Copy the current scissor rect so we can restore it after
            XnaRect currentRect = sb.GraphicsDevice.ScissorRectangle;
            sb.GraphicsDevice.ScissorRectangle = new XnaRect(dx += BORDER_WIDTH, dy += BORDER_HEIGHT, Width - 2 * BORDER_WIDTH, Height - 2 * BORDER_HEIGHT);



            //If selected item is visible, draw bar behind it

            //Draw each item in the list
            int i = 0;
            float scale = 1f;
            foreach (ListBoxItem item in Items)
            {
                int ypos = i * itemHeight - scrollViewPos;

                if (ypos >= -itemHeight && ypos < scrollViewHeight)//itemtop)
                {
                    //Vector2 ssize = Gfx.GuiFont1.MeasureString(item);
                    //int ypos = (int)((i - itemtop) * itemHeight + 4);
                    //if (ypos + ssize.Y > Height) break; //Stop if no space for more items in box

                    //if (ssize.X > Width - 8)
                    //    scale = (Width - 8) / ssize.X;
                    //else
                    //    scale = 1f;

                    if (i == itemsel)
                    {
                        Gfx.DrawRect(dx, dy + ypos, Width - BORDER_WIDTH * 2, itemHeight, Color.White, true);
                        //sb.Draw(Gfx.GuiBits, new XnaRect(dx, dy + ypos, Width - BORDER_WIDTH * 2, itemHeight), new XnaRect(8, 24, 1, 1), Color.White);
                        sb.DrawString(item.Italic ? listFontItalic : listFont, item.Text, new Vector2(dx, dy + ypos), Color.Black, 0f, Vector2.Zero, scale, SpriteEffects.None, 0f);
                    }
                    else
                        sb.DrawString(item.Italic ? listFontItalic : listFont, item.Text, new Vector2(dx /*+ 4*/, dy + ypos), item.Colour, 0f, Vector2.Zero, scale, SpriteEffects.None, 0f);

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

                    //if (Items.Count <= visibleitems || Gui.Ms.X < dx + Width - 16) //user selects an item in the list
                    //{
                    int sel = (Gui.Ms.Y - dy + scrollViewPos) / itemHeight;
                    if (sel < Items.Count)
                    {
                        itemsel = sel;
                        if (changedHandler != null) changedHandler.Invoke(true, Items[sel]);
                        return true;
                    }
                    //}    
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
            get { return itemsel == -1 ? null : Items[itemsel]; }
            set
            {
                if (value == null)
                {
                    itemsel = -1;
                    if (changedHandler != null) changedHandler.Invoke(false, null);
                }
                else
                {
                    itemsel = Items.IndexOf(value);// FindIndex(n => n == value); 
                    if (changedHandler != null) changedHandler.Invoke(false, itemsel == -1 ? null : value);
                }
            }
        }

        public void RevealItem(ListBoxItem lb)
        {
            if (lb == null) { vScroll.ChangeValues(scrollViewPos = 0, scrollViewHeight, 0, scrollFullHeight, itemHeight); }
            else
            {
                int i = Items.IndexOf(lb) * itemHeight;

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

        public void InsertItem(int pos, String txt, Color colour, object data, bool italic)
        {
            Items.Insert(pos, new ListBoxItem { Text = txt, Colour = colour, Tag = data, Italic = italic });
            scrollFullHeight += itemHeight;
            vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
        }

        public ListBoxItem AddItem(String txt, Color colour, object data, bool italic)
        {
            ListBoxItem i = new ListBoxItem { Text = txt, Colour = colour, Tag = data, Italic = italic };
            Items.Add(i);
            scrollFullHeight += itemHeight;
            vScroll.ChangeValues(scrollViewPos, scrollViewHeight, 0, scrollFullHeight, itemHeight);
            return i;
        }

    }
}