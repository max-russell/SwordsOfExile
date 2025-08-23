using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Color = Microsoft.Xna.Framework.Color;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

internal static class Gfx
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

    private static Effect ColourFlashEffect;
    public static Effect SpriteWhite;

    public static GraphicsDevice Device;
    public static RasterizerState RasterizerWotsit = new() { ScissorTestEnable = true };
    private static GraphicsDeviceManager DeviceManager;
    private static ContentManager Content;
    private static SpriteBatch spriteBatch;
    private static TextureLoader textureLoader;

    public static int WinW=-1, WinH=-1;
    public static bool FullScreen = false;
    private static SurfaceFormat defaultDisplayFormat;
    private static float defaultAspect;

    public const float CHARWIDTH = (float)CHARGFXWIDTH / (float)CHARGFXHEIGHT; //Character's width in proportion to full width of square
    public const int DEFAULTZOOM = 36;

    public static int ZoomSizeW = 36, ZoomSizeH = 36; //Current size in pixels of map square.

    private static List<int> ZoomStages;
    private static int ZoomStage, DefaultZoomStage;
    private static int ZoomStart, ZoomDest;
    private static bool ZoomingMap;
    private static int ZoomTime, ZoomDuration;

    public const int ZOOMMAX = 88, ZOOMMIN = 8;
    public const int ZOOMSIMPLETHRESHOLD = 24; //Below this zoom level don't bother drawing items or map frills.

    public static Vector2 Scroll; //Square that is currently centred in the viewport.
    public static Vector2 ScrollDest, ScrollStart;
    public static int ScrollTime, ScrollDuration;
    public static bool ScrollingMap = false;

    public static int FadeMode; //0: No fade, 1: Fading to black, 2: Black 3: Fading from black
    public static Color FadeColor = Color.Black;

    //Graphics Options
    public static bool DrawHealthBars = true;

    private class CursorGraphic
    {
        public int XCorner, YCorner;
        public int XHotspot, YHotspot;
    }
    //SWORD, NW, N, NE, TALK, USE, W, WAIT, E, BOOT, TARGET, SW, S, SE

    private static CursorGraphic[] Cursors = new CursorGraphic[] { 
        new() { XCorner = 32, YCorner = 0, XHotspot = 0x7, YHotspot = 0x9 },
        new() { XCorner = 64, YCorner = 0, XHotspot = 0xF, YHotspot = 0xF },
        new() { XCorner = 96, YCorner = 0, XHotspot = 0x11, YHotspot = 0xF },
        new() { XCorner = 128, YCorner = 0, XHotspot = 0x10, YHotspot = 0x11 },
        new() { XCorner = 0, YCorner = 32, XHotspot = 0xD, YHotspot = 0xC },
        new() { XCorner = 32, YCorner = 32, XHotspot = 0x17, YHotspot = 0x7 },
        new() { XCorner = 64, YCorner = 32, XHotspot = 0x10, YHotspot = 0x10 },
        new() { XCorner = 96, YCorner = 32, XHotspot = 0xA, YHotspot = 0x12 },
        new() { XCorner = 128, YCorner = 32, XHotspot = 0x10, YHotspot = 0x10 },
        new() { XCorner = 0, YCorner = 64, XHotspot = 0x10, YHotspot = 0x10 },
        new() { XCorner = 32, YCorner = 64, XHotspot = 0x10, YHotspot = 0xE },
        new() { XCorner = 64, YCorner = 64, XHotspot = 0x10, YHotspot = 0x10 },
        new() { XCorner = 96, YCorner = 64, XHotspot = 0x10, YHotspot = 0xE },
        new() { XCorner = 128, YCorner = 64, XHotspot = 0x10, YHotspot = 0x10 },
        new() { XCorner = 0, YCorner = 0, XHotspot = 0x10, YHotspot = 0x10 }
    };

    private static CursorGraphic currentCursor = Cursors[0];

    public static void SetCursor(eCursor c)
    {
        currentCursor = Cursors[(int) c];
    }

    public static void Initialise(Game g)
    {
        DeviceManager = new GraphicsDeviceManager(g);
        Content = g.Content;
        Content.RootDirectory = "Content";

        ZoomStages = new List<int>();
        ZoomStage = 0;

        double z = DEFAULTZOOM;

        while (z <= ZOOMMAX)
        {
            ZoomStages.Add((int)z);
            z /= 0.75f;
        }
        z = DEFAULTZOOM * 0.75f; 
        while (z >= ZOOMMIN)
        {
            ZoomStages.Insert(0, (int)z);
            ZoomStage++;
            z *= 0.75f;
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
        }
        else
        {
            if (!Directory.Exists(Path.Combine(Game.ScenarioDirectory, "Images"))) return;
            Directory.SetCurrentDirectory(Path.Combine(Game.ScenarioDirectory, "Images"));
        }

        for (var n = 0; n < 32; n++)
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
        var arr = new Color[16*8];
        for(var n = 0; n < arr.Length; n++) arr[n] = Color.White;
        Bar.SetData<Color>(arr);
            
        DarkEdges = Texture2D.FromFile(gd, "darkedges.png");//Content.Load<Texture2D>("darkedges");
        NewGui = Texture2D.FromFile(gd, "gui new.png");

        SmallBoldFont = Content.Load<BitmapFont>("NewSmallBoldFont");
        ItalicFont = Content.Load<BitmapFont>("NewItalicFont");
        BoldFont = Content.Load<BitmapFont>("NewBoldFont");
        TinyFont = Content.Load<BitmapFont>("NewTinyFont");

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
        }

        InitGraphicsMode(WinW, WinH, FullScreen);
    }

    public static IEnumerable<DisplayMode> EachAvailableResolution()
    {
        var modes = GraphicsAdapter.DefaultAdapter.SupportedDisplayModes.ToList<DisplayMode>();

        modes.RemoveAll(n => n.Format != defaultDisplayFormat);
        modes.RemoveAll(n => n.Height < 600);
        modes = modes.OrderBy(n => n.Height).ToList<DisplayMode>();
            
        foreach (var mode in modes) yield return mode;
    }

    private static bool SupportedRes(int width, int height)
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
        return false;
    }

    public static void Draw()
    {
        Device.Clear(Color.Black);

        if (Game.InMainMenu)
            StartupMap.Draw(spriteBatch);
        else

        if (!Game.ErrorFlagged && !Game.Loading && Game.CurrentMap != null)
            Game.CurrentMap.Draw(spriteBatch);

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
        var w = Width - FRAME_WIDTH * 2;
        int hsidetimes = w / frame_hside_width, hsiderem = w % frame_hside_width; //How many complete times to draw the source, and how many pixels left over
        var x2 = X + FRAME_WIDTH;
        for (var x = 0; x < hsidetimes; x++) //Draw complete lengths of the horizontal frame sides
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
        var h = Height - FRAME_HEIGHT * 2;
        int vsidetimes = h / frame_vside_height, vsiderem = h % frame_vside_height;
        var y2 = Y + FRAME_HEIGHT;
        for (var y = 0; y < vsidetimes; y++) //Draw complete lengths of the horizontal frame sides
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

    /// <summary>
    /// Set up a scroll so that the target square ends up in the centre of the screen.
    /// </summary>
    /// <param name="l"></param>
    /// <param name="instant">Doesn't gradually scroll there, goes instantly.</param>
    public static void CentreView(Location l, bool instant) {

        var s = new Vector2(l.X + 0.5f, l.Y + 0.5f);
            
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
        var VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
        var VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
        float vhmargin = VW / 4f, vvmargin = VH / 4;

        var lx = (l.X + 0.5f);
        var ly = (l.Y + 0.5f);

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
    }

    public static void DoMapScroll(int ms_passed)
    {
        if (ScrollingMap)
        {
            ScrollTime += ms_passed;

            var f = (float)ScrollTime / (float)ScrollDuration;
            Scroll = Vector2.SmoothStep(ScrollStart, ScrollDest, f);
            if (f >= 0.95f) 
            {
                ScrollingMap = false;
                Scroll = ScrollDest;
            }
        }
    }

    public static void DoMapZoom(int ms_passed)
    {
        if (ZoomingMap)
        {
            ZoomTime += ms_passed;

            var f = (float)ZoomTime / (float)ZoomDuration;
            ZoomSizeW = ZoomSizeH = (int)((float)(ZoomDest - ZoomStart) * f) + ZoomStart;

            if (f >= 0.95f) 
            {
                ZoomingMap = false;
                ZoomSizeW = ZoomSizeH = ZoomDest;
            }
        }

    }

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
        var VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
        var VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
        var offx = (int)(((Gfx.Scroll.X - VW / 2f) - (int)(Gfx.Scroll.X - VW / 2f)) * Gfx.ZoomSizeW);
        var offy = (int)(((Gfx.Scroll.Y - VH / 2f) - (int)(Gfx.Scroll.Y - VH / 2f)) * Gfx.ZoomSizeH);
        var sx = (int)(Gfx.Scroll.X - VW / 2f);
        var sy = (int)(Gfx.Scroll.Y - VH / 2f);

        var posx = (int)((ms.X + offx) / Gfx.ZoomSizeW + sx);
        var posy = (int)((ms.Y + offy) / Gfx.ZoomSizeH + sy);

        return new Location(posx, posy);
    }
    public static XnaRect GetMapMouseRect()
    {
        var VW = (float)Gfx.WinW / Gfx.ZoomSizeW;
        var VH = (float)Gfx.WinH / Gfx.ZoomSizeH;
        var offx = (int)(((Gfx.Scroll.X - VW / 2f) - (int)(Gfx.Scroll.X - VW / 2f)) * Gfx.ZoomSizeW);
        var offy = (int)(((Gfx.Scroll.Y - VH / 2f) - (int)(Gfx.Scroll.Y - VH / 2f)) * Gfx.ZoomSizeH);
        var posx = (int)((Gui.Ms.X+offx) / Gfx.ZoomSizeW) * Gfx.ZoomSizeW - offx;
        var posy = (int)((Gui.Ms.Y+offy) / Gfx.ZoomSizeH) * Gfx.ZoomSizeH - offy;
        return new XnaRect(posx, posy, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
    }

    private static bool InitGraphicsMode(int iWidth, int iHeight, bool bFullScreen)
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
            foreach (var dm in GraphicsAdapter.DefaultAdapter.SupportedDisplayModes)
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
        var coldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT * 4];
        var srcrct = new XnaRect(0, n * CHARGFXHEIGHT, CHARGFXWIDTH * 4, CHARGFXHEIGHT);
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
        var coldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT * 4];
        pcg.GetData<Color>(coldata);
        foreach (var c in coldata) file.Write(c.PackedValue);

        coldata = new Color[PCPORTRAITWIDTH * PCPORTRAITHEIGHT];
        pcp.GetData<Color>(coldata);
        foreach (var c in coldata) file.Write(c.PackedValue);
    }

    static public void LoadPCGraphics(BinaryReader file, out Texture2D pcg, out Texture2D pcp)
    {
        var coldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT * 4];
        for (var a = 0; a < coldata.Length; a++)
            coldata[a] = new Color { PackedValue = file.ReadUInt32() };
        pcg = new Texture2D(Device, CHARGFXWIDTH * 4, CHARGFXHEIGHT);
        pcg.SetData<Color>(coldata);
            
        coldata = new Color[PCPORTRAITWIDTH * PCPORTRAITHEIGHT];
        for (var a = 0; a < coldata.Length; a++)
            coldata[a] = new Color { PackedValue = file.ReadUInt32() };
        pcp = new Texture2D(Device, PCPORTRAITWIDTH, PCPORTRAITHEIGHT);
        pcp.SetData<Color>(coldata);
    }

    static public void MakeCharacterHighlight(PCType pc)
    {
        Texture2D srctx;
        var srcrct = new XnaRect();
        srctx = pc.PCTexture;
        srcrct = pc.GetGraphicRect(true);

        //Put it into a new texture.
        PCHighlightGfx = generateHighlight(srctx, srcrct);
        srcrct.X += CHARGFXWIDTH * 2;
        PCCombatHighlightGfx = generateHighlight(srctx, srcrct);
    }

    private static Texture2D generateHighlight(Texture2D srctx, XnaRect srcrct)
    {
        //Get pixel data from the graphic
        var origcoldata = new Color[CHARGFXWIDTH * CHARGFXHEIGHT];
        srctx.GetData<Color>(0, srcrct, origcoldata, 0, CHARGFXWIDTH * CHARGFXHEIGHT);

        //Port it over to a bigger size array so there's room for the whole outline in the graphic
        var sw = CHARGFXWIDTH + 2 * HIGHLIGHT_SIZE;
        var sh = CHARGFXHEIGHT + 2 * HIGHLIGHT_SIZE;
        var newcoldata = new Color[sw * sh];

        var n = 0;
            
        for (var y = 0; y < CHARGFXHEIGHT; y++) {

            var m = sw * HIGHLIGHT_SIZE + sw * y + HIGHLIGHT_SIZE;

            for (var x = 0; x < CHARGFXWIDTH; x++) {
                newcoldata[m++] = origcoldata[n++];
            }
        }

        //0: 255    0/3 * 200 = 0        255-0 = 255
        //1:        1/3 * 200 = 66.66    255-66.66 = 188
        //2: 50     2/3 * 200 = 133.33   255-133  = 122

        //Manipulate the data to add the outline.
        for (var q = 0; q < HIGHLIGHT_SIZE; q++)
        {
            var col = Color.FromNonPremultiplied(255, 255, 255, 255 - (int)(((float)q / (float)HIGHLIGHT_SIZE) * 200f));

            var coldata = newcoldata;
            newcoldata = (Color[])coldata.Clone();

            n = 0;
            for (var y = 0; y < sh; y++)
            {
                for (var x = 0; x < sw; x++) {

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

        var dsttxt = new Texture2D(Device, sw, sh);
        dsttxt.SetData<Color>(newcoldata);
        return dsttxt;

    }

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
                using (var image = System.Drawing.Image.FromStream(stream))
                {
                    // Now create a MemoryStream which will be passed to Texture2D after converting to PNG internally
                    using (var ms = new MemoryStream())
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
                using (var renderTarget = new RenderTarget2D(_graphicsDevice, texture.Width, texture.Height))
                {
                    var viewportBackup = _graphicsDevice.Viewport;
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
                    var data = new Color[texture.Width * texture.Height];
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