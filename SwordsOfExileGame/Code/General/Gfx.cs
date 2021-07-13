using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.IO;
//using System.Drawing;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using Color = Microsoft.Xna.Framework.Color;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using XnaPoint = Microsoft.Xna.Framework.Point;

using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    static class Gfx
    {
        public const int SRCTILEWIDTH = 48, SRCTILEHEIGHT = 48;
        public const int TILEWIDTH = 48, TILEHEIGHT = 48;
        public const int CHARGFXWIDTH = 28, CHARGFXHEIGHT = 36;
        public const int CUSTOMGFXWIDTH = 28, CUSTOMGFXHEIGHT = 36;
        public const int ITEMGFXWIDTH = 28, ITEMGFXHEIGHT = 36;
        public const int FACEGFXWIDTH = 32, FACEGFXHEIGHT = 32,
                         PCPORTRAITWIDTH = 32, PCPORTRAITHEIGHT = 32;
        public const int SCENGFXWIDTH = 32, SCENGFXHEIGHT = 32,
                         MISCGFXWIDTH = 36, MISCGFXHEIGHT = 36;
        public const int MISSILE_GFX_WIDTH = 16, MISSILE_GFX_HEIGHT = 16;

        public const int HIGHLIGHT_SIZE = 4;//Thickness of the outline when a character is highlighted

        public static Texture2D DarkEdges, NewGui;
        public static Texture2D Dot, Bar;
        public static BitmapFont GuiFont1, SmallBoldFont, BoldFont, ItalicFont, TinyFont, TalkFontNormal, TalkFontBold, TalkFontItalic;

        //Multiple sheet textures
        public static Texture2D[] TerrainGfx = new Texture2D[32],
                                  AnimTerrainGfx = new Texture2D[32],
                                  NPCGfx1x1 = new Texture2D[32],
                                  NPCGfx2x1 = new Texture2D[32],
                                  NPCGfx1x2 = new Texture2D[32],
                                  NPCGfx2x2 = new Texture2D[32],
                                  ItemGfx = new Texture2D[32],
                                  FacesGfx = new Texture2D[32],
                                  MissilesGfx = new Texture2D[32],
                                  DialogGfx = new Texture2D[32];

        public static Texture2D FieldsGfx, ScenarioGfx, StatAreaGfx, MixedGfx,
                                ButtonsGfx, TextBarGfx, PCHighlightGfx, PCCombatHighlightGfx,
                                LogoPic, CursorsGfx;

        //public static Texture2D TerrainGfx;// = new Texture2D[6];
        //public static Texture2D NPCGfx1x1, NPCGfx2x1, NPCGfx1x2, NPCGfx2x2,
        //                        AnimTerrainGfx, ItemGfx/*, BigItemGfx*/, FieldsGfx, //RoadsGfx,
        //                        CustomGfx, FacesGfx, MissilesGfx, ScenarioGfx, DialogGfx,
        //                        StatAreaGfx, MixedGfx, ButtonsGfx, TextBarGfx,
        //                        PCHighlightGfx, PCCombatHighlightGfx, NPCHighlightGfx,
        //                        CustomNPCGfx2x1, CustomNPCGfx1x2, CustomNPCGfx2x2, LogoPic,
        //                        CursorsGfx; 
                                //CustomDialogPicKludge; //This is a dodgy bit to handle custom 'dialog' graphics from BoE, that are cut in two in the bitmap
        public static int[] ItemGfxSlotsAcross = new int[32],
                            TerrainGfxSlotsAcross = new int[32],
                            AnimTerrainGfxSlotsAcross = new int[32],
                            NPCGfx1x1SlotsAcross = new int[32],
                            NPCGfx2x1SlotsAcross = new int[32],
                            NPCGfx1x2SlotsAcross = new int[32],
                            NPCGfx2x2SlotsAcross = new int[32],
                            FacesGfxSlotsAcross = new int[32],
                            MissilesGfxSlotsAcross = new int[32],
                            DialogGfxSlotsAcross = new int[32];

        //These are only needed during party creation. After that the chosen graphics are copied out to new textures stored in each PCType
        public static Texture2D PCGfx, PCPortraitGfx;

        static Effect ColourFlashEffect;
        public static Effect SpriteWhite;

        public static GraphicsDevice Device;
        public static RasterizerState RasterizerWotsit = new RasterizerState { ScissorTestEnable = true };
        static GraphicsDeviceManager DeviceManager;
        static ContentManager Content;
        static SpriteBatch spriteBatch;
        //public static RenderTarget2D renderTarget1, renderTarget2, renderTarget3;
        static TextureLoader textureLoader;

        public static int WinW=-1, WinH=-1;
        public static bool FullScreen = false;
        static SurfaceFormat defaultDisplayFormat;
        static float defaultAspect;

        //public const int SQUAREWIDTH = 36, SQUAREHEIGHT = 36; //Default size in pixels of each map square
        public const float CHARWIDTH = (float)CHARGFXWIDTH / (float)CHARGFXHEIGHT; //Character's width in proportion to full width of square
        public const int DEFAULTZOOM = 36;

        public static int ZoomSizeW = 36/*TILEWIDTH*/, ZoomSizeH = 36/*TILEHEIGHT*/; //Current size in pixels of map square.

        static List<int> ZoomStages;
        static int ZoomStage, DefaultZoomStage;
        static int ZoomStart, ZoomDest;
        static bool ZoomingMap;
        static int ZoomTime, ZoomDuration;

        //static float zoom = 1f;
        //public static float Zoom { get { return zoom; } set { zoom = value; ZoomW = (int)(Gfx.TILEWIDTH * zoom); ZoomH = (int)(Gfx.TILEHEIGHT * zoom); } }
        //public static int ZoomW = (int)(TILEWIDTH * zoom);
        //public static int ZoomH = (int)(TILEHEIGHT * zoom);

        public const int ZOOMMAX = 88, ZOOMMIN = 8;
        public const int ZOOMSIMPLETHRESHOLD = 24; //Below this zoom level don't bother drawing items or map frills.

        public static Vector2 Scroll; //Square that is currently centred in the viewport.
        public static Vector2 ScrollDest, ScrollStart;
        public static int ScrollTime, ScrollDuration;//float ScrollTime, ScrollRate = 0.2f;
        public static bool ScrollingMap = false;

        public static int FadeMode; //0: No fade, 1: Fading to black, 2: Black 3: Fading from black
        //public static int FadeTime, FadeDuration;
        public static Color FadeColor = Color.Black;

        //Graphics Options
        public static bool DrawHealthBars = true;

        class CursorGraphic
        {
            public int XCorner, YCorner;
            public int XHotspot, YHotspot;
        }
        //SWORD, NW, N, NE, TALK, USE, W, WAIT, E, BOOT, TARGET, SW, S, SE

        static CursorGraphic[] Cursors = new CursorGraphic[] { 
            new CursorGraphic { XCorner = 32, YCorner = 0, XHotspot = 0x7, YHotspot = 0x9 },
            new CursorGraphic { XCorner = 64, YCorner = 0, XHotspot = 0xF, YHotspot = 0xF },
            new CursorGraphic { XCorner = 96, YCorner = 0, XHotspot = 0x11, YHotspot = 0xF },
            new CursorGraphic { XCorner = 128, YCorner = 0, XHotspot = 0x10, YHotspot = 0x11 },
            new CursorGraphic { XCorner = 0, YCorner = 32, XHotspot = 0xD, YHotspot = 0xC },
            new CursorGraphic { XCorner = 32, YCorner = 32, XHotspot = 0x17, YHotspot = 0x7 },
            new CursorGraphic { XCorner = 64, YCorner = 32, XHotspot = 0x10, YHotspot = 0x10 },
            new CursorGraphic { XCorner = 96, YCorner = 32, XHotspot = 0xA, YHotspot = 0x12 },
            new CursorGraphic { XCorner = 128, YCorner = 32, XHotspot = 0x10, YHotspot = 0x10 },
            new CursorGraphic { XCorner = 0, YCorner = 64, XHotspot = 0x10, YHotspot = 0x10 },
            new CursorGraphic { XCorner = 32, YCorner = 64, XHotspot = 0x10, YHotspot = 0xE },
            new CursorGraphic { XCorner = 64, YCorner = 64, XHotspot = 0x10, YHotspot = 0x10 },
            new CursorGraphic { XCorner = 96, YCorner = 64, XHotspot = 0x10, YHotspot = 0xE },
            new CursorGraphic { XCorner = 128, YCorner = 64, XHotspot = 0x10, YHotspot = 0x10 },
            new CursorGraphic { XCorner = 0, YCorner = 0, XHotspot = 0x10, YHotspot = 0x10 }
        };

        static CursorGraphic currentCursor = Cursors[0];

        public static void SetCursor(eCursor c)
        {
            currentCursor = Cursors[(int) c];
        }

        //public static ICharacter combat_posing_monster;

        public static void Initialise(Game g)
        {
            DeviceManager = new GraphicsDeviceManager(g);
            //Device = g.GraphicsDevice;
            Content = g.Content;
            Content.RootDirectory = "Content";

            ZoomStages = new List<int>();
            ZoomStage = 0;

            double z = DEFAULTZOOM;// ZoomSizeW;//TILEWIDTH;

            while (z <= ZOOMMAX)
            {
                ZoomStages.Add((int)z);
                z /= 0.75f;// *= 1.25f;
            }
            z = /*TILEWIDTH*/ DEFAULTZOOM * 0.75f; // / 1.25f;
            while (z >= ZOOMMIN)
            {
                ZoomStages.Insert(0, (int)z);
                ZoomStage++;
                z *= 0.75f;// /= 1.25f;
            }
            DefaultZoomStage = ZoomStage;
        }

        public static void Load(GraphicsDevice gd, bool just_base)//GraphicsDevice gd, ContentManager cm)
        {
            if (just_base)
            {
                Directory.SetCurrentDirectory(Path.Combine(Game.BaseDirectory, "Images"));
                Device = gd;
                textureLoader = new TextureLoader(gd);
                spriteBatch = new SpriteBatch(Device);
                //spriteBatch = new MonoGame.Extended.Graphics.Batcher2D(Device);

            }
            else
            {
                if (!Directory.Exists(Path.Combine(Game.ScenarioDirectory, "Images"))) return;
                Directory.SetCurrentDirectory(Path.Combine(Game.ScenarioDirectory, "Images"));
            }

            for (int n = 0; n < 32; n++)
            {
                textureLoader.FromFile(String.Format("Terrains_{0:D2}.png", n), ref TerrainGfx[n]); //textureLoader.FromFile("Terrains.png", ref TerrainGfx);
                if (TerrainGfx[n] != null) TerrainGfxSlotsAcross[n] = TerrainGfx[n].Width / SRCTILEWIDTH;

                textureLoader.FromFile(String.Format("TerrainsAnim_{0:D2}.png", n), ref AnimTerrainGfx[n]);
                if (AnimTerrainGfx[n] != null) AnimTerrainGfxSlotsAcross[n] = AnimTerrainGfx[n].Width / (SRCTILEWIDTH * 4);

                textureLoader.FromFile(String.Format("Npcs1x1_{0:D2}.png", n), ref NPCGfx1x1[n]);
                if (NPCGfx1x1[n] != null) NPCGfx1x1SlotsAcross[n] = NPCGfx1x1[n].Width / (CHARGFXWIDTH * 4);

                textureLoader.FromFile(String.Format("Npcs1x2_{0:D2}.png", n), ref NPCGfx1x2[n]);
                if (NPCGfx1x2[n] != null) NPCGfx1x2SlotsAcross[n] = NPCGfx1x2[n].Width / (CHARGFXWIDTH * 4);

                textureLoader.FromFile(String.Format("Npcs2x1_{0:D2}.png", n), ref NPCGfx2x1[n]);
                if (NPCGfx2x1[n] != null) NPCGfx2x1SlotsAcross[n] = NPCGfx2x1[n].Width / (CHARGFXWIDTH * 8);

                textureLoader.FromFile(String.Format("Npcs2x2_{0:D2}.png", n), ref NPCGfx2x2[n]);
                if (NPCGfx2x2[n] != null) NPCGfx2x2SlotsAcross[n] = NPCGfx2x2[n].Width / (CHARGFXWIDTH * 8);

                textureLoader.FromFile(String.Format("Items_{0:D2}.png", n), ref ItemGfx[n]);
                if (ItemGfx[n] != null) ItemGfxSlotsAcross[n] = ItemGfx[n].Width / ITEMGFXWIDTH;

                textureLoader.FromFile(String.Format("TalkPortraits_{0:D2}.png", n), ref FacesGfx[n]);
                if (FacesGfx[n] != null) FacesGfxSlotsAcross[n] = FacesGfx[n].Width / Gfx.FACEGFXWIDTH;

                textureLoader.FromFile(String.Format("Missiles_{0:D2}.png", n), ref MissilesGfx[n]);
                if (MissilesGfx[n] != null) MissilesGfxSlotsAcross[n] = MissilesGfx[n].Width / (Gfx.MISSILE_GFX_WIDTH * 8);

                textureLoader.FromFile(String.Format("DialogPics_{0:D2}.png", n), ref DialogGfx[n]);
                if (DialogGfx[n] != null) DialogGfxSlotsAcross[n] = DialogGfx[n].Width / Gfx.MISCGFXWIDTH;
            }

            textureLoader.FromFile("mixed.png", ref MixedGfx);
            textureLoader.FromFile("Fields.png", ref FieldsGfx);
            textureLoader.FromFile("statarea.png", ref StatAreaGfx);
            textureLoader.FromFile("buttons.png", ref ButtonsGfx);
            textureLoader.FromFile("textbar.png", ref TextBarGfx);

            textureLoader.FromFile("ScenarioPics.png", ref ScenarioGfx);
            textureLoader.FromFile("cursors.png", ref CursorsGfx);

            if (!just_base) return;

            LogoPic = Texture2D.FromFile(gd, "SwordsofExileLogo half.png"); //'Content.Load<Texture2D>("SwordsOfExileLogo");
            
            ColourFlashEffect = Content.Load<Effect>("ColourFlash");

            //Make Dot texture used for drawing lines and rectangles
            Dot = new Texture2D(gd, 1, 1, false, SurfaceFormat.Color);
            Dot.SetData<Color>(0, new XnaRect(0, 0, 1, 1), new Color[] { Color.White }, 0, 1);

            Bar = new Texture2D(gd, 16, 8, false, SurfaceFormat.Color);
            Color[] arr = new Color[16*8];
            for(int n = 0; n < arr.Length; n++) arr[n] = Color.White;
            Bar.SetData<Color>(arr);
            
            //GuiBits = Content.Load<Texture2D>("guibits" );
            DarkEdges = Texture2D.FromFile(gd, "darkedges.png");//Content.Load<Texture2D>("darkedges");
            NewGui = Texture2D.FromFile(gd, "gui new.png");

            //GuiFont1 = Content.Load<BitmapFont>("guifont1");
            SmallBoldFont = Content.Load<BitmapFont>("NewSmallBoldFont");
            ItalicFont = Content.Load<BitmapFont>("NewItalicFont");
            BoldFont = Content.Load<BitmapFont>("NewBoldFont");
            TinyFont = Content.Load<BitmapFont>("NewTinyFont");
            //TinyFont = Content.Load<BitmapFont>("NewTinyFont");

            SpriteWhite = Content.Load<Effect>("SpriteWhite");

            TalkFontNormal = Content.Load<BitmapFont>("NewTalkFontNormal");
            TalkFontBold = Content.Load<BitmapFont>("NewTalkFontBold");
            TalkFontItalic = Content.Load<BitmapFont>("NewTalkFontItalic");
            
            GuiFont1 = TinyFont;

            defaultDisplayFormat = GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.Format;
            defaultAspect = GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.AspectRatio;

            if (WinW == -1 || WinH == -1 || !SupportedRes(WinW, WinH))
            {
                //Graphics settings have not been initialised. Find a good starting resolution for the current system.
                WinW = GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.Width;
                WinH = GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.Height;
                FullScreen = true;
                Game.SaveSettings();

                //if (GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.Height < 1024)
                //{
                //    WinW = 1024;
                //    WinH = 700;
                //}
                //else
                //{
                //    WinW = 1600;
                //    WinH = 1024;
                //}
            }

            InitGraphicsMode(WinW, WinH, FullScreen);
            //SetViewArea(Device, WinW, WinH);
        }

        public static IEnumerable<DisplayMode> EachAvailableResolution()
        {
            var modes = GraphicsAdapter.DefaultAdapter.SupportedDisplayModes.ToList<DisplayMode>();

            modes.RemoveAll(n => n.Format != defaultDisplayFormat);
            modes.RemoveAll(n => n.Height < 600);
            modes = modes.OrderBy(n => n.Height).ToList<DisplayMode>();
            
            foreach (DisplayMode mode in modes) yield return mode;
        }

        static bool SupportedRes(int width, int height)
        {
            try
            { GraphicsAdapter.DefaultAdapter.SupportedDisplayModes.First(n => n.Width == width && n.Height == height); }
            catch
            {
                return false;
            }
            return true;
        }

        public static void LoadPCGraphicsOptions()
        {
            textureLoader.FromFile(Path.Combine(Game.BaseDirectory, "Images", "pcs.png"), ref PCGfx);
            textureLoader.FromFile(Path.Combine(Game.BaseDirectory, "Images", "PCPortraits.png"), ref PCPortraitGfx);
        }

        public static bool LoadCustom(string fn, ref Texture2D pic)
        {
            if (File.Exists(Path.ChangeExtension(fn, "png")))
            {
                textureLoader.FromFile(Path.ChangeExtension(fn, "png"), ref pic); //Path.Combine(Game.BaseDirectory, "scenarios", Path.ChangeExtension(fn, "png")));
                return true;
            }
            //else if (File.Exists(Path.ChangeExtension(fn, "bmp")))
            //{
            //    throw new Exception("Change that BMP to a PNG, NOW!");
            //    //Message telling the player to convert the bmp to a png.
            //    //return false;
            //}
            return false;
        }

        //public static XnaRect GetCustomRect(int no)
        //{
        //    return new XnaRect((no % 10) * CUSTOMGFXWIDTH, (no / 10) * CUSTOMGFXHEIGHT, CUSTOMGFXWIDTH, CUSTOMGFXHEIGHT);
        //}

        public static void Draw()
        {
            Device.Clear(Color.Black);

            if (Game.InMainMenu)
                StartupMap.Draw(spriteBatch);
            else

            if (!Game.ErrorFlagged && !Game.Loading && Game.CurrentMap != null)
                Game.CurrentMap.Draw(spriteBatch);

            //spriteBatch.Begin();
            //////spriteBatch.Draw(GuiBits, new Vector2(ViewW / 2 - 8, ViewH/2 - 8),new XnaRect(0,0,16,16),Color.Red);
            //spriteBatch.DrawString(BoldFont, String.Format("{0}", Gfx.ZoomSizeW), new Vector2(WinW - 120, 20), Color.White); 

            //if (Gui.ActiveToolTip != null)
            //    spriteBatch.DrawString(BoldFont, String.Format("x:{0} y:{1} w:{2} h:{3}", Gui.ActiveToolTip.mZone.X, Gui.ActiveToolTip.mZone.Y, Gui.ActiveToolTip.mZone.Width, Gui.ActiveToolTip.mZone.Height), new Vector2(WinW - 120, 50), Color.White); 

            //spriteBatch.End();

            Gui.Draw(spriteBatch);
            
        }

        public static void DrawCursor(MouseState ms)
        {
            spriteBatch.Draw(CursorsGfx, new Vector2(ms.X - currentCursor.XHotspot, ms.Y - currentCursor.YHotspot), new XnaRect(currentCursor.XCorner, currentCursor.YCorner, 32, 32), Color.White);
        }

        public static void DrawRect(int x, int y, int w, int h, Color col, bool filled = true, int thickness = 1)
        {
            if (filled)
                spriteBatch.Draw(Dot, new XnaRect(x, y, w, h), col);
            else
            {
                spriteBatch.Draw(Dot, new XnaRect(x, y, w, thickness), col);
                spriteBatch.Draw(Dot, new XnaRect(x, y, thickness, h), col);
                spriteBatch.Draw(Dot, new XnaRect(x + w - thickness, y, thickness, h), col);
                spriteBatch.Draw(Dot, new XnaRect(x, y + h - thickness, w, thickness), col);
            }
        }

        public const int frame_l_src = 163, frame_t_src = 0, frame_r_src = 247, frame_b_src = 84,
                    frame_hside_l = 175, frame_hside_width = 72,
                    frame_vside_t = 12, frame_vside_height = 72;
        public const int FRAME_WIDTH = 12, FRAME_HEIGHT = 12;

        public static void DrawFrame(int X, int Y, int Width, int Height, Color inner_tint)
        {
            var tex = Gfx.NewGui;

            //Draw Corners
            spriteBatch.Draw(tex, new Vector2(X, Y), new XnaRect(frame_l_src, frame_t_src, FRAME_WIDTH, FRAME_HEIGHT), Color.White);
            spriteBatch.Draw(tex, new Vector2(X + Width - FRAME_WIDTH, Y), new XnaRect(frame_r_src, frame_t_src, FRAME_WIDTH, FRAME_HEIGHT), Color.White);
            spriteBatch.Draw(tex, new Vector2(X, Y + Height - FRAME_HEIGHT), new XnaRect(frame_l_src, frame_b_src, FRAME_WIDTH, FRAME_HEIGHT), Color.White);
            spriteBatch.Draw(tex, new Vector2(X + Width - FRAME_WIDTH, Y + Height - FRAME_HEIGHT), new XnaRect(frame_r_src, frame_b_src, FRAME_WIDTH, FRAME_HEIGHT), Color.White);

            //Top/bottom sides
            int w = Width - FRAME_WIDTH * 2;
            int hsidetimes = w / frame_hside_width, hsiderem = w % frame_hside_width; //How many complete times to draw the source, and how many pixels left over
            //int h = Height - frame_height * 2;
            //int vsidetimes = h / frame_vside_height, vsiderem = h % frame_vside_height;
            int x2 = X + FRAME_WIDTH;
            for (int x = 0; x < hsidetimes; x++) //Draw complete lengths of the horizontal frame sides
            {
                spriteBatch.Draw(tex, new Vector2(x2, Y), new XnaRect(frame_hside_l, frame_t_src, frame_hside_width, FRAME_HEIGHT), Color.White);
                spriteBatch.Draw(tex, new Vector2(x2, Y + Height - FRAME_HEIGHT), new XnaRect(frame_hside_l, frame_b_src, frame_hside_width, FRAME_HEIGHT), Color.White);
                x2 += frame_hside_width;
            }
            if (hsiderem != 0) //Draw partial bit of frame side
            {
                spriteBatch.Draw(tex, new Vector2(x2, Y), new XnaRect(frame_hside_l, frame_t_src, hsiderem, FRAME_HEIGHT), Color.White);
                spriteBatch.Draw(tex, new Vector2(x2, Y + Height - FRAME_HEIGHT), new XnaRect(frame_hside_l, frame_b_src, hsiderem, FRAME_HEIGHT), Color.White);
            }

            //left / right sides
            int h = Height - FRAME_HEIGHT * 2;
            int vsidetimes = h / frame_vside_height, vsiderem = h % frame_vside_height;
            int y2 = Y + FRAME_HEIGHT;
            for (int y = 0; y < vsidetimes; y++) //Draw complete lengths of the horizontal frame sides
            {
                spriteBatch.Draw(tex, new Vector2(X, y2), new XnaRect(frame_l_src, frame_vside_t, FRAME_WIDTH, frame_vside_height), Color.White);
                spriteBatch.Draw(tex, new Vector2(X + Width - FRAME_WIDTH, y2), new XnaRect(frame_r_src, frame_vside_t, FRAME_WIDTH, frame_vside_height), Color.White);
                y2 += frame_vside_height;
            }
            if (vsiderem != 0) //Draw partial bit of frame side
            {
                spriteBatch.Draw(tex, new Vector2(X, y2), new XnaRect(frame_l_src, frame_vside_t, FRAME_WIDTH, vsiderem), Color.White);
                spriteBatch.Draw(tex, new Vector2(X + Width - FRAME_WIDTH, y2), new XnaRect(frame_r_src, frame_vside_t, FRAME_WIDTH, vsiderem), Color.White);
            }

            //Fill in
            spriteBatch.Draw(tex, new XnaRect(X + FRAME_WIDTH, Y + FRAME_HEIGHT, Width - (FRAME_WIDTH * 2), Height - (FRAME_HEIGHT * 2)), new XnaRect(frame_hside_l, frame_vside_t, frame_hside_width, frame_vside_height), inner_tint);//backCol);//new Color(255, 255, 255, 127));

        }

        //public static void DrawPortrait(XnaRect dst, int num, Color col)
        //{
        //    spriteBatch.Draw(Gfx.FacesGfx, dst, new XnaRect((num % 10) * 32, (num / 10) * 32, 32, 32), col);
        //}

        /// <summary>
        /// Set up a scroll so that the target square ends up in the centre of the screen.
        /// </summary>
        /// <param name="l"></param>
        /// <param name="instant">Doesn't gradually scroll there, goes instantly.</param>
        public static void CentreView(Location l, bool instant) {

            //Scroll.X = l.x + 0.5f;
            //Scroll.Y = l.y + 0.5f;
            Vector2 s = new Vector2(l.X + 0.5f, l.Y + 0.5f);
                //-(ViewW / 2) + ((l.x + 0.5f) * TILEWIDTH * Zoom),
                   //-(ViewH / 2) + ((l.y + 0.5f) * TILEHEIGHT * Zoom));
            
            if (instant) {
                ScrollingMap = false;
                ScrollDest = s;
                Scroll = s;
            } else {
                ScrollStart = Scroll;
                ScrollDest = s;
                ScrollingMap = true;
                ScrollTime = 0;
                ScrollDuration = 250;
            }
        }

        /// <summary>
        /// Set up a scroll so that the target square is somewhere inside the middle section of the screen if its not already.
        /// </summary>
        /// <param name="l"></param>
        public static void ScrollTo(Location l)
        {
            //Scroll.X = l.x + 0.5f;
            //Scroll.Y = l.y + 0.5f;

            float VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
            float VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
            float vhmargin = VW / 4f, vvmargin = VH / 4;

            float lx = (l.X + 0.5f);// *Gfx.ZoomSizeW;
            float ly = (l.Y + 0.5f);// *Gfx.ZoomSizeH;

            if (lx > Scroll.X + vhmargin)
                ScrollDest.X = lx - vhmargin;
            else if (lx < Scroll.X - vhmargin)
                ScrollDest.X = lx + vhmargin;

            if (ly > Scroll.Y + vvmargin)
                ScrollDest.Y = ly - vvmargin;
            else if (ly < Scroll.Y - vvmargin)
                ScrollDest.Y = ly + vvmargin;

            if (ScrollDest != Scroll)
            {
                ScrollStart = Scroll;
                ScrollingMap = true;
                ScrollTime = 0;
                ScrollDuration = 250;
            }


        }

        public static void StartZoom(bool zoomout, int duration) {

            ZoomStage = zoomout ? ZoomStage - 1 : ZoomStage + 1;
            ZoomStage = Maths.MinMax(0, ZoomStages.Count - 1, ZoomStage);

            if (duration == 0)
            {
                ZoomingMap = false;
                ZoomSizeW = ZoomSizeH = ZoomStages[ZoomStage];
            }
            else
            {
                ZoomingMap = true;
                ZoomStart = ZoomSizeW;
                ZoomDest = ZoomStages[ZoomStage];
                ZoomTime = 0;
                ZoomDuration = duration;
            }

            //ZoomSizeW = ZoomSizeH = ZoomStages[ZoomStage];


            //if (zoomout) ZoomSizeH=--ZoomSizeW; else ZoomSizeH=++ZoomSizeW;
            //ZoomSizeW = ZoomSizeH = Maths.MinMax(ZOOMMIN, ZOOMMAX, ZoomSizeW);

            //float zoomrate = zoomout ? 1 / ZOOMRATE : ZOOMRATE;

            //float z = Zoom * zoomrate;

            //if ((zoomout && z >= ZOOMMIN) || (!zoomout && z <= ZOOMMAX)) {
            //    Zoom = z;
            //    //ScrollStart = Scroll;
            //    //ScrollDest = new Vector2((ViewW / 2 + Scroll.X) * zoomrate - ViewW / 2, (ViewH / 2 + Scroll.Y) * zoomrate - ViewH / 2);
            //    //ScrollingMap = true;
            //    //ScrollTime = 0;

            //    Scroll.X = (ViewW / 2f + Scroll.X) * zoomrate - ViewW / 2f;
            //    Scroll.Y = (ViewH / 2f + Scroll.Y) * zoomrate - ViewH / 2f;
            //    //Scroll.X = (ZoomW / 2 + Scroll.X) * zoomrate - ZoomW / 2;
            //    //Scroll.Y = (ZoomH / 2 + Scroll.Y) * zoomrate - ZoomH / 2;
                
            //}
        }

        public static void MapZoom()
        {
            if (ZoomingMap) return;

            if (ZoomStage >= DefaultZoomStage - 2) 
                ZoomStage = 0;
            else 
                ZoomStage = DefaultZoomStage;

            ZoomStart = ZoomSizeW;
            ZoomDest = ZoomStages[ZoomStage];
            ZoomingMap = true;
            ZoomTime = 0;
            ZoomDuration = 150;

            //ZoomSizeW = ZoomSizeH = ZoomStages[ZoomStage];
        }

        public static void DoMapScroll(int ms_passed)
        {
            if (ScrollingMap)
            {
                ScrollTime += ms_passed;//+= ScrollRate;

                float f = (float)ScrollTime / (float)ScrollDuration;
                Scroll = Vector2.SmoothStep(ScrollStart, ScrollDest, f);
                if (f >= 0.95f) //>= 1f)
                {
                    ScrollingMap = false;
                    Scroll = ScrollDest;
                }
                //if (ToolTip.OnMap) ToolTip.ResetWait();
            }
        }

        public static void DoMapZoom(int ms_passed)
        {
            if (ZoomingMap)
            {
                ZoomTime += ms_passed;

                float f = (float)ZoomTime / (float)ZoomDuration;
                ZoomSizeW = ZoomSizeH = (int)((float)(ZoomDest - ZoomStart) * f) + ZoomStart;

                if (f >= 0.95f) //>= 1f)
                {
                    ZoomingMap = false;
                    ZoomSizeW = ZoomSizeH = ZoomDest;
                    //ToolTip.ResetWait();
                }

                //if (ZoomDest > ZoomSizeW) ZoomSizeH = ++ZoomSizeW;
                //else if (ZoomDest < ZoomSizeW) ZoomSizeH = --ZoomSizeW;
                //else ZoomingMap = false;
            }

        }

        //public static void DoFade(int ms_passed)
        //{
        //    if (FadeMode == 1) //Fading to black
        //    {
        //        if (Game.DrawCalled)
        //            FadeTime += ms_passed;
        //        if (FadeTime >= FadeDuration)
        //        {
        //            FadeMode = 2; //Black
        //            FadeColor = Color.Black;
        //        }
        //        else 
        //            FadeColor.A = (byte)(((float)FadeTime / (float)FadeDuration) * 255f);
        //        return;
        //    }
        //    else if (FadeMode == 3) //Fading from black
        //    {
        //        if (Game.DrawCalled)
        //            FadeTime += ms_passed;
        //        if (FadeTime >= FadeDuration)
        //        {
        //            FadeMode = 0;
        //            FadeColor = new Color(0,0,0,0);
        //            Action.Requested = eAction.NONE; //Flush any action
        //        }
        //        else 
        //            FadeColor.A = (byte)(255f - ((float)FadeTime / (float)FadeDuration) * 255f);
        //    }
        //}

        //public static void StartFade(int duration, bool from_black)
        //{
        //    //Gui.WorldModalPaused = true;
        //    FadeDuration = duration;
        //    FadeTime = 0;

        //    if (!from_black)
        //    {
        //        FadeMode = 1;
        //        FadeColor = new Color(0, 0, 0, 0);
        //    }
        //    else
        //    {
        //        FadeMode = 3;
        //        FadeColor = Color.Black;
        //    }
        //}

        public static void ApplyFlashShader(Color col, float amt)
        {
            ColourFlashEffect.Parameters["ColR"].SetValue(col.R / 255f);
            ColourFlashEffect.Parameters["ColG"].SetValue(col.G / 255f);
            ColourFlashEffect.Parameters["ColB"].SetValue(col.B / 255f);
            ColourFlashEffect.Parameters["ColLevel"].SetValue(amt);
            ColourFlashEffect.CurrentTechnique.Passes[0].Apply();
        }

        public static Location GetTileAtMouse(MouseState ms)
        {
            float VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
            float VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
            int offx = (int)(((Gfx.Scroll.X - VW / 2f) - (int)(Gfx.Scroll.X - VW / 2f)) * Gfx.ZoomSizeW);
            int offy = (int)(((Gfx.Scroll.Y - VH / 2f) - (int)(Gfx.Scroll.Y - VH / 2f)) * Gfx.ZoomSizeH);
            int sx = (int)(Gfx.Scroll.X - VW / 2f);
            int sy = (int)(Gfx.Scroll.Y - VH / 2f);

            int posx = (int)((ms.X + offx) / Gfx.ZoomSizeW + sx);
            int posy = (int)((ms.Y + offy) / Gfx.ZoomSizeH + sy);

            return new Location(posx, posy);
        }
        public static XnaRect GetMapMouseRect()
        {
            float VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
            float VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
            int offx = (int)(((Gfx.Scroll.X - VW / 2f) - (int)(Gfx.Scroll.X - VW / 2f)) * Gfx.ZoomSizeW);
            int offy = (int)(((Gfx.Scroll.Y - VH / 2f) - (int)(Gfx.Scroll.Y - VH / 2f)) * Gfx.ZoomSizeH);
            int posx = (int)((Gui.Ms.X+offx) / Gfx.ZoomSizeW) * Gfx.ZoomSizeW - offx;
            int posy = (int)((Gui.Ms.Y+offy) / Gfx.ZoomSizeH) * Gfx.ZoomSizeH - offy;
            return new XnaRect(posx, posy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
        }



        static bool InitGraphicsMode(int iWidth, int iHeight, bool bFullScreen)
        {
            // If we aren't using a full screen mode, the height and width of the window can
            // be set to anything equal to or smaller than the actual screen size.
            if (bFullScreen == false)
            {
                if ((iWidth <= GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.Width)
                    && (iHeight <= GraphicsAdapter.DefaultAdapter.CurrentDisplayMode.Height))
                {
                    DeviceManager.PreferredBackBufferWidth = iWidth;
                    DeviceManager.PreferredBackBufferHeight = iHeight;
                    DeviceManager.IsFullScreen = bFullScreen;
                    DeviceManager.ApplyChanges();
                    return true;
                }
            }
            else
            {
                // If we are using full screen mode, we should check to make sure that the display
                // adapter can handle the video mode we are trying to set.  To do this, we will
                // iterate thorugh the display modes supported by the adapter and check them against
                // the mode we want to set.
                foreach (DisplayMode dm in GraphicsAdapter.DefaultAdapter.SupportedDisplayModes)
                {
                    // Check the width and height of each mode against the passed values
                    if ((dm.Width == iWidth) && (dm.Height == iHeight))
                    {
                        // The mode is supported, so set the buffer formats, apply changes and return
                        DeviceManager.PreferredBackBufferWidth = iWidth;
                        DeviceManager.PreferredBackBufferHeight = iHeight;
                        DeviceManager.IsFullScreen = bFullScreen;
                        DeviceManager.ApplyChanges();
                        return true;
                    }
                }
            }
            return false;
        }

        static public void MakePCGraphics(int n, int p, out Texture2D pctex, out Texture2D portraittex)
        {
            Color[] coldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT * 4];
            XnaRect srcrct = new XnaRect(0, n * CHARGFXHEIGHT, CHARGFXWIDTH * 4, CHARGFXHEIGHT);
            Gfx.PCGfx.GetData<Color>(0, srcrct, coldata, 0, CHARGFXWIDTH * CHARGFXHEIGHT * 4);
            pctex = new Texture2D(Device, CHARGFXWIDTH * 4, CHARGFXHEIGHT);
            pctex.SetData<Color>(coldata);

            coldata = new Color[PCPORTRAITWIDTH * PCPORTRAITHEIGHT];
            srcrct = new XnaRect((p % 10) * PCPORTRAITWIDTH, (p / 10) * PCPORTRAITHEIGHT, PCPORTRAITWIDTH, PCPORTRAITHEIGHT);
            Gfx.PCPortraitGfx.GetData<Color>(0, srcrct, coldata, 0, PCPORTRAITWIDTH * PCPORTRAITHEIGHT);
            portraittex = new Texture2D(Device, PCPORTRAITWIDTH, PCPORTRAITHEIGHT);
            portraittex.SetData<Color>(coldata);
        }
        static public void SavePCGraphics(BinaryWriter file, Texture2D pcg, Texture2D pcp)
        {
            //Save graphics
            Color[] coldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT * 4];
            pcg.GetData<Color>(coldata);
            foreach (Color c in coldata) file.Write(c.PackedValue);

            coldata = new Color[PCPORTRAITWIDTH * PCPORTRAITHEIGHT];
            pcp.GetData<Color>(coldata);
            foreach (Color c in coldata) file.Write(c.PackedValue);
        }

        static public void LoadPCGraphics(BinaryReader file, out Texture2D pcg, out Texture2D pcp)
        {
            Color[] coldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT * 4];
            for (int a = 0; a < coldata.Length; a++)
                coldata[a] = new Color { PackedValue = file.ReadUInt32() };
            pcg = new Texture2D(Device, CHARGFXWIDTH * 4, CHARGFXHEIGHT);
            pcg.SetData<Color>(coldata);
            
            coldata = new Color[PCPORTRAITWIDTH * PCPORTRAITHEIGHT];
            for (int a = 0; a < coldata.Length; a++)
                coldata[a] = new Color { PackedValue = file.ReadUInt32() };
            pcp = new Texture2D(Device, PCPORTRAITWIDTH, PCPORTRAITHEIGHT);
            pcp.SetData<Color>(coldata);
        }

        static public void MakeCharacterHighlight(PCType pc)
        {
            Texture2D srctx;

            XnaRect srcrct = new XnaRect();

            //Get the graphic texture and rectangle for this character
            //if (ch is PCType) {
                //PCType pc = (PCType)ch;
                srctx = pc.PCTexture;
                srcrct = pc.GetGraphicRect(true);
            //} else {
            //    srctx = NPCGfx1x1;//CreatureGfx;
            //    srcrct = new XnaRect();
            //}

            //Put it into a new texture.
            //if (ch is PCType)
            //{
                PCHighlightGfx = generateHighlight(srctx, srcrct);
                srcrct.X += CHARGFXWIDTH * 2;
                PCCombatHighlightGfx = generateHighlight(srctx, srcrct);
            //}
            //else
            //{
            //    NPCHighlightGfx = generateHighlight(srctx, srcrct);
            //}

        
        }
        static Texture2D generateHighlight(Texture2D srctx, XnaRect srcrct)
        {

            //Get pixel data from the graphic
            Color[] origcoldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT];
            srctx.GetData<Color>(0, srcrct, origcoldata, 0, CHARGFXWIDTH * CHARGFXHEIGHT);

            //Port it over to a bigger size array so there's room for the whole outline in the graphic
            int sw = CHARGFXWIDTH + 2 * HIGHLIGHT_SIZE;
            int sh = CHARGFXHEIGHT + 2 * HIGHLIGHT_SIZE;
            Color[] newcoldata = new Color[sw * sh];

            int n = 0;
            
            for (int y = 0; y < CHARGFXHEIGHT; y++) {

                int m = sw * HIGHLIGHT_SIZE + sw * y + HIGHLIGHT_SIZE;

                for (int x = 0; x < CHARGFXWIDTH; x++) {
                    newcoldata[m++] = origcoldata[n++];
                }
            }

            //0: 255    0/3 * 200 = 0        255-0 = 255
            //1:        1/3 * 200 = 66.66    255-66.66 = 188
            //2: 50     2/3 * 200 = 133.33   255-133  = 122


            //Manipulate the data to add the outline.
            for (int q = 0; q < HIGHLIGHT_SIZE; q++)
            {
                Color col = Color.FromNonPremultiplied(255, 255, 255, 255 - (int)(((float)q / (float)HIGHLIGHT_SIZE) * 200f));

                Color[] coldata = newcoldata;
                newcoldata = (Color[])coldata.Clone();

                n = 0;
                for (int y = 0; y < sh; y++)
                {
                    for (int x = 0; x < sw; x++) {

                        if  (coldata[n].A == 0 && 
                            ((x > 0 && coldata[n-1].A > 0) ||
                             (x < sw - 1 && coldata[n+1].A > 0) ||
                             (y > 0 && coldata[n - sw].A > 0) ||
                             (y < sh - 1 && coldata[n+sw].A > 0)))
                        {
                            newcoldata[n] = col;// Color.White;
                        }
                        n++;
                    }
                }
            }

            Texture2D dsttxt = new Texture2D(Device, sw, sh);
            dsttxt.SetData<Color>(newcoldata);
            return dsttxt;

        }

        //public static void GenerateBigNPCGfx()
        //{
        //    var l2x1 = new List<int>();
        //    var l1x2 = new List<int>();
        //    var l2x2 = new List<int>();

        //    ////Find the plus-sized pre-fabricated monsters
        //    //for(int n = 0; n< NPCRecord.m_pic_index.Length; n++)
        //    //{
        //    //    if (NPCRecord.m_pic_index[n] == 0) break;
        //    //    if (NPCRecord.m_pic_index_x[n] == 2 && NPCRecord.m_pic_index_y[n] == 1)
        //    //    { 
        //    //        l2x1.Add(NPCRecord.m_pic_index[n]);
        //    //        NPCRecord.m_pic_index[n] = (byte)(l2x1.Count - 1);
        //    //    }
        //    //    else if (NPCRecord.m_pic_index_x[n] == 1 && NPCRecord.m_pic_index_y[n] == 2)
        //    //    {
        //    //        l1x2.Add(NPCRecord.m_pic_index[n]);
        //    //        NPCRecord.m_pic_index[n] = (byte)(l1x2.Count - 1);
        //    //    }
        //    //    else if (NPCRecord.m_pic_index_x[n] == 2 && NPCRecord.m_pic_index_y[n] == 2)
        //    //    {
        //    //        l2x2.Add(NPCRecord.m_pic_index[n]);
        //    //        NPCRecord.m_pic_index[n] = (byte)(l2x2.Count - 1);
        //    //    }
        //    //}

        //    //0000 - standard 1x1
        //    //1000 - standard 2x1
        //    //2000 - standard 1x2
        //    //3000 - standard 2x2
        //    //4000 - custom 1x1
        //    //5000 - custom 2x1
        //    //6000 - custom 1x2
        //    //7000 - custom 2x2

        //    //Find the plus-sized monsters in the custom graphics
        //    foreach (NPCRecord nr in NPCRecord.List)
        //    {
        //        if (nr.Picture >= 10000)
        //        {
        //            if (nr.Width == 2 && nr.Height == 2)
        //            {
        //                if (!l2x2.Contains(nr.Picture))
        //                {
        //                    l2x2.Add(nr.Picture);
        //                    nr.Picture = 10000 + l2x2.Count - 1;
        //                }
        //                else
        //                {
        //                    nr.Picture = 10000 + l2x2.IndexOf(nr.Picture);
        //                }
        //            }
        //            else if (nr.Width == 2 && nr.Height == 1)
        //            {
        //                if (!l2x1.Contains(nr.Picture))
        //                {
        //                    l2x1.Add(nr.Picture);
        //                    nr.Picture = 10000 + l2x1.Count - 1;
        //                }
        //                else
        //                {
        //                    nr.Picture = 10000 + l2x1.IndexOf(nr.Picture);
        //                }
        //            }
        //            else if (nr.Width == 1 && nr.Height == 2)
        //            {
        //                if (!l1x2.Contains(nr.Picture))
        //                {
        //                    l1x2.Add(nr.Picture);
        //                    nr.Picture = 10000 + l1x2.Count - 1;
        //                }
        //                else
        //                {
        //                    nr.Picture = 10000 + l1x2.IndexOf(nr.Picture);
        //                }
        //            }
        //        }


        //        //if (nr.Picture >= 7000) { if (!l2x2.Contains(nr.Picture)) { l2x2.Add(nr.Picture); nr.Picture = 7000 + l2x2.Count - 1; } }
        //        //else if (nr.Picture >= 6000) { if (!l1x2.Contains(nr.Picture)) { l1x2.Add(nr.Picture-5000); nr.Picture = 6000 + l1x2.Count - 1; } }
        //        //else if (nr.Picture >= 5000) { if (!l2x1.Contains(nr.Picture)) { l2x1.Add(nr.Picture-4000); nr.Picture = 5000 + l2x1.Count - 1; } }
        //    }

        //    if (l2x1.Count > 0)
        //    {
        //        CustomNPCGfx2x1 = new Texture2D(Device, 8 * CHARGFXWIDTH, l2x1.Count * CHARGFXHEIGHT);
        //        Color[] destcol = new Color[CustomNPCGfx2x1.Width * CustomNPCGfx2x1.Height];
        //        int slotx = 0, sloty = 0, slotsacross = 8;

        //        foreach (int n in l2x1)
        //        {
        //            //if (n < 1000)
        //            //{
        //            //    copyNPCGfxColourData(n, destcol, slotx++, sloty, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx++, sloty, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n, destcol, slotx++, sloty, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx++, sloty, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n, destcol, slotx++, sloty, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx++, sloty, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n, destcol, slotx++, sloty, slotsacross, true, true);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx, sloty, slotsacross, true, true);
        //            //    sloty++; slotx = 0;
        //            //}
        //            //else
        //            //{
        //                copyNPCGfxColourData(n, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 1, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 2, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 3, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 4, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 5, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 6, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 7, destcol, slotx, sloty, slotsacross);
        //                sloty++; slotx = 0;
        //            //}
        //        }
        //        CustomNPCGfx2x1.SetData<Color>(destcol);
        //    }

        //    if (l1x2.Count > 0)
        //    {
        //        CustomNPCGfx1x2 = new Texture2D(Device, 4 * CHARGFXWIDTH, l1x2.Count * 2 * CHARGFXHEIGHT);
        //        Color[] destcol = new Color[CustomNPCGfx1x2.Width * CustomNPCGfx1x2.Height];
        //        int slotx = 0, sloty = 0, slotsacross = 4;

        //        foreach (int n in l1x2)
        //        {
        //            //if (n < 1000)
        //            //{
        //            //    copyNPCGfxColourData(n, destcol, slotx, sloty++, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n+1, destcol, slotx++, sloty--, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n, destcol, slotx, sloty++, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx++, sloty--, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n, destcol, slotx, sloty++, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx++, sloty--, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n, destcol, slotx, sloty++, slotsacross, true, true);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx, sloty++, slotsacross, true, true);
        //            //    slotx = 0;
        //            //}
        //            //else
        //            //{
        //                copyNPCGfxColourData(n+0, destcol, slotx, sloty++, slotsacross);
        //                copyNPCGfxColourData(n+1, destcol, slotx++, sloty--, slotsacross);
        //                copyNPCGfxColourData(n + 2, destcol, slotx, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 3, destcol, slotx++, sloty--, slotsacross);
        //                copyNPCGfxColourData(n + 4, destcol, slotx, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 5, destcol, slotx++, sloty--, slotsacross);
        //                copyNPCGfxColourData(n + 6, destcol, slotx, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 7, destcol, slotx, sloty++, slotsacross);
        //                slotx = 0;
        //            //}
        //        }
        //        CustomNPCGfx1x2.SetData<Color>(destcol);
        //    }

        //    if (l2x2.Count > 0)
        //    {
        //        CustomNPCGfx2x2 = new Texture2D(Device, 8 * CHARGFXWIDTH, l2x2.Count * 2 * CHARGFXHEIGHT);
        //        Color[] destcol = new Color[CustomNPCGfx2x2.Width * CustomNPCGfx2x2.Height];
        //        int slotx = 0, sloty = 0, slotsacross = 8;

        //        foreach (int n in l2x2)
        //        {
        //            //if (n < 1000)
        //            //{
        //            //    copyNPCGfxColourData(n + 0, destcol, slotx++, sloty, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx--, sloty++, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n + 2, destcol, slotx++, sloty, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n + 3, destcol, slotx++, sloty--, slotsacross, false, false);
        //            //    copyNPCGfxColourData(n + 0, destcol, slotx++, sloty, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx--, sloty++, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n + 2, destcol, slotx++, sloty, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n + 3, destcol, slotx++, sloty--, slotsacross, true, false);
        //            //    copyNPCGfxColourData(n + 0, destcol, slotx++, sloty, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx--, sloty++, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n + 2, destcol, slotx++, sloty, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n + 3, destcol, slotx++, sloty--, slotsacross, false, true);
        //            //    copyNPCGfxColourData(n + 0, destcol, slotx++, sloty, slotsacross, true, true);
        //            //    copyNPCGfxColourData(n + 1, destcol, slotx--, sloty++, slotsacross, true, true);
        //            //    copyNPCGfxColourData(n + 2, destcol, slotx++, sloty, slotsacross, true, true);
        //            //    copyNPCGfxColourData(n + 3, destcol, slotx, sloty, slotsacross, true, true);
        //            //    sloty++; slotx = 0;
        //            //}
        //            //else
        //            //{
        //                copyNPCGfxColourData(n + 0, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 1, destcol, slotx--, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 2, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 3, destcol, slotx++, sloty--, slotsacross);
        //                copyNPCGfxColourData(n + 4, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 5, destcol, slotx--, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 6, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 7, destcol, slotx++, sloty--, slotsacross);
        //                copyNPCGfxColourData(n + 8, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 9, destcol, slotx--, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 10, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 11, destcol, slotx++, sloty--, slotsacross);
        //                copyNPCGfxColourData(n + 12, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 13, destcol, slotx--, sloty++, slotsacross);
        //                copyNPCGfxColourData(n + 14, destcol, slotx++, sloty, slotsacross);
        //                copyNPCGfxColourData(n + 15, destcol, slotx, sloty, slotsacross);
        //                sloty++; slotx = 0;
        //            //}
        //        }
        //        CustomNPCGfx2x2.SetData<Color>(destcol);
        //    }

        //}

        //static void copyNPCGfxColourData(int index, Color[] dstcol, int dstindexX, int dstindexY, int slotsacross, bool leftwards=false, bool actionpose=false )
        //{
        //    Texture2D stex;
        //    XnaPoint sp = XnaPoint.Zero;
        //    Color[] srccol;

        //    index -= 10000;
        //    stex = CustomGfx;
        //    srccol = new Color[stex.Width * stex.Height];
        //    stex.GetData<Color>(srccol);
        //    sp = new XnaPoint((index % 10) * CHARGFXWIDTH, (index / 10) * CHARGFXHEIGHT);

        //    int dp = (dstindexY * slotsacross * CHARGFXWIDTH * CHARGFXHEIGHT) + (dstindexX * CHARGFXWIDTH);
        //    for (int y = sp.Y; y < sp.Y + CHARGFXHEIGHT; y++)
        //    {
        //        for (int x = sp.X; x < sp.X + CHARGFXWIDTH; x++)
        //        {
        //            dstcol[dp] = srccol[y * stex.Width + x];
        //            dp++;
        //        }
        //        dp += (slotsacross * CHARGFXWIDTH) - CHARGFXWIDTH;
        //    }
            
        //}

        //public static Texture2D MakeKludgyCustomDialogPic(int index, eDialogPic picsize)
        //{
        //    //In a scenario's custom graphics sheet, custom Dialog Pics are stored in two adjacent 28x36 slots. Half of the 36x36 dialog graphic in each slot.
        //    //This subroutine, extracts the graphic from the slots, glues it together and sticks it in a temporary Texture2D, which is then used by the 
        //    //CustomDialogWindow to display the right graphic in the PictureBox.

        //    int height = picsize == eDialogPic.CUSTOM_FACE ? FACEGFXHEIGHT : CUSTOMGFXHEIGHT;
        //    int width; 
            
        //    if (picsize == eDialogPic.CUSTOM_FACE) width = FACEGFXWIDTH;
        //    else if (picsize == eDialogPic.CUSTOM_SQUARE) width = CUSTOMGFXHEIGHT;
        //    else width = CUSTOMGFXWIDTH;

        //    Texture2D pic = new Texture2D(Device, width, height);

        //    var dstcol = new Color[width * height];

        //    var srccol = new Color[CustomGfx.Width * CustomGfx.Height];
        //    CustomGfx.GetData<Color>(srccol);

        //    if (picsize == eDialogPic.CUSTOM_FACE || picsize == eDialogPic.CUSTOM_SQUARE)
        //    {
        //        //First left half in custom graphic slot 'index'
        //        var sp = new XnaPoint((index % 10) * CUSTOMGFXWIDTH, (index / 10) * CUSTOMGFXHEIGHT);
        //        int dp = 0;
        //        for (int y = sp.Y; y < sp.Y + height; y++)
        //        {
        //            for (int x = sp.X; x < sp.X + (width >> 1); x++)
        //            {
        //                dstcol[dp] = srccol[y * CustomGfx.Width + x];
        //                dp++;
        //            }
        //            dp += width >> 1;
        //        }

        //        //Then right half in custom graphic slot 'index'+1
        //        sp = new XnaPoint(((index + 1) % 10) * CUSTOMGFXWIDTH, ((index + 1) / 10) * CUSTOMGFXHEIGHT);
        //        dp = width >> 1;
        //        for (int y = sp.Y; y < sp.Y + height; y++)
        //        {
        //            for (int x = sp.X; x < sp.X + (width >> 1); x++)
        //            {
        //                dstcol[dp] = srccol[y * CustomGfx.Width + x];
        //                dp++;
        //            }
        //            dp += width >> 1;
        //        }
        //    }
        //    else
        //    {
        //        var sp = new XnaPoint((index % 10) * CUSTOMGFXWIDTH, (index / 10) * CUSTOMGFXHEIGHT);
        //        int dp = 0;
        //        for (int y = sp.Y; y < sp.Y + height; y++)
        //        {
        //            for (int x = sp.X; x < sp.X + width; x++)
        //            {
        //                dstcol[dp] = srccol[y * CustomGfx.Width + x];
        //                dp++;
        //            }
        //        }
        //    }

        //    pic.SetData<Color>(dstcol);
        //    return pic;
        //}

        /// <summary>
        /// Based on http://jakepoz.com/jake_poznanski__background_load_xna.html 
        /// </summary>
        public class TextureLoader
        {
            static TextureLoader()
            {
                BlendColorBlendState = new BlendState
                {
                    ColorDestinationBlend = Blend.Zero,
                    ColorWriteChannels = ColorWriteChannels.Red | ColorWriteChannels.Green | ColorWriteChannels.Blue,
                    AlphaDestinationBlend = Blend.Zero,
                    AlphaSourceBlend = Blend.SourceAlpha,
                    ColorSourceBlend = Blend.SourceAlpha
                };

                BlendAlphaBlendState = new BlendState
                {
                    ColorWriteChannels = ColorWriteChannels.Alpha,
                    AlphaDestinationBlend = Blend.Zero,
                    ColorDestinationBlend = Blend.Zero,
                    AlphaSourceBlend = Blend.One,
                    ColorSourceBlend = Blend.One
                };
            }

            public TextureLoader(GraphicsDevice graphicsDevice, bool needsBmp = false)
            {
                _graphicsDevice = graphicsDevice;
                _needsBmp = needsBmp;
                _spriteBatch = new SpriteBatch(_graphicsDevice);
            }

            public void FromFile(string path, ref Texture2D tex, bool preMultiplyAlpha = true)
            {
                if (!File.Exists(path)) return;

                using (Stream fileStream = File.OpenRead(path))
                    tex = FromStream(fileStream, preMultiplyAlpha);//return FromStream(fileStream, preMultiplyAlpha);
            }


            public Texture2D FromStream(Stream stream, bool preMultiplyAlpha = true)
            {
                Texture2D texture;

                if (_needsBmp)
                {
                    // Load image using GDI because Texture2D.FromStream doesn't support BMP
                    using (System.Drawing.Image image = System.Drawing.Image.FromStream(stream))
                    {
                        // Now create a MemoryStream which will be passed to Texture2D after converting to PNG internally
                        using (MemoryStream ms = new MemoryStream())
                        {
                            image.Save(ms, System.Drawing.Imaging.ImageFormat.Png);
                            ms.Seek(0, SeekOrigin.Begin);
                            texture = Texture2D.FromStream(_graphicsDevice, ms);
                        }
                    }
                }
                else
                {
                    texture = Texture2D.FromStream(_graphicsDevice, stream);
                }

                if (preMultiplyAlpha)
                {
                    // Setup a render target to hold our final texture which will have premulitplied alpha values
                    using (RenderTarget2D renderTarget = new RenderTarget2D(_graphicsDevice, texture.Width, texture.Height))
                    {
                        Viewport viewportBackup = _graphicsDevice.Viewport;
                        _graphicsDevice.SetRenderTarget(renderTarget);
                        _graphicsDevice.Clear(Color.Black);

                        // Multiply each color by the source alpha, and write in just the color values into the final texture
                        _spriteBatch.Begin(SpriteSortMode.Deferred, BlendColorBlendState);
                        _spriteBatch.Draw(texture, texture.Bounds, Color.White);
                        _spriteBatch.End();

                        // Now copy over the alpha values from the source texture to the final one, without multiplying them
                        _spriteBatch.Begin(SpriteSortMode.Deferred, BlendAlphaBlendState);
                        _spriteBatch.Draw(texture, texture.Bounds, Color.White);
                        _spriteBatch.End();

                        // Release the GPU back to drawing to the screen
                        _graphicsDevice.SetRenderTarget(null);
                        _graphicsDevice.Viewport = viewportBackup;

                        // Store data from render target because the RenderTarget2D is volatile
                        Color[] data = new Color[texture.Width * texture.Height];
                        renderTarget.GetData(data);

                        // Unset texture from graphic device and set modified data back to it
                        _graphicsDevice.Textures[0] = null;
                        texture.SetData(data);
                    }

                }

                return texture;
            }

            private static readonly BlendState BlendColorBlendState;
            private static readonly BlendState BlendAlphaBlendState;

            private readonly GraphicsDevice _graphicsDevice;
            private readonly SpriteBatch _spriteBatch;
            private readonly bool _needsBmp;
        }

    }


}
