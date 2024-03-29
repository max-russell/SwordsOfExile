﻿using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace SwordsOfExileGame
{
    static class Gui
    {
        static PartyType Party { get { return Game.CurrentParty; } }
        public static List<GuiWindow> GuiWindows = new List<GuiWindow>();

        public static MouseState Ms;
        public static bool LMBStop, RMBStop, MMBStop, LMBDown, RMBDown, MMBDown, LMBHit, RMBHit, MMBHit,
            LMBHitUp, RMBHitUp, MMBHitUp;
        public static bool NeedMouseRelease; //Set this if we want the user to release the mouse buttons before the GUI will respond to anything else
        static bool mouseScrolling;
        static int mouseScrollX, mouseScrollY;

        static GuiWindow moveWindow, resizeWindow;
        static int moveWinOrgX, moveWinOrgY, resizeWinOrgY;

        static GuiWindow bringFrontWin; //Set to a window that has been requested to be brought to the front at the start of the next Gui update.

        public static Item DragItem, SplitDragItem;
        public static IInventory DragItemFrom, SplitDragFrom;
        public static Shop ShopIsOpen = null; //Shop whose window is open
        public static Control ServiceBoxOpen = null; //Identify/Enchanting box on window that is currently open
        public static MagicShopWindow MagicShopIsOpen = null;

        static bool worldModalPaused = false;
        public static bool WorldModalPaused { get { return worldModalPaused; } set { worldModalPaused = value; KeyHandler.ScrollWheel = Ms.ScrollWheelValue; } }// = false;
        public static int TooltipDelay = 5;

        public static ToolTipV2 ActiveToolTip = null;

        static MapPath PathPreview = new MapPath();

        public static void StartMovingWindow(GuiWindow w)
        {
            moveWindow = w;
            moveWinOrgX = Ms.X;
            moveWinOrgY = Ms.Y;
        }
        public static void StartResizingWindow(GuiWindow w)
        {
            resizeWindow = w;
            resizeWinOrgY = Ms.Y;
        }


        public static void BringToFront(GuiWindow win)
        {
            bringFrontWin = win;
        }

        static void bringToFront(GuiWindow win)
        {
            //Bring window to the front, except if there is a visible modal window in front of it
            int pos = GuiWindows.IndexOf(win);
            bool dontdoit = false;
            for (int n = pos + 1; n < GuiWindows.Count; n++)
            {
                if (GuiWindows[n].Modal && GuiWindows[n].Visible) { dontdoit = true; break; }
            }
            if (!dontdoit)
            {

                GuiWindows.Remove(win);
                if (win.OnTop || GuiWindows.Count == 0 || GuiWindows.FindIndex(n => n.OnTop) == -1)
                    GuiWindows.Add(win);
                else
                    GuiWindows.Insert(GuiWindows.FindIndex(n => n.OnTop), win);
            }
        }

        public static void HandleToolTip()
        {
            if (ActiveToolTip != null) ActiveToolTip.Handle();
        }

        public static void Handle()
        {
            if (!Game.Instance.IsActive) return;

            LMBStop = LMBDown;
            RMBStop = RMBDown;
            MMBStop = MMBDown;
            Ms = Mouse.GetState();
            LMBDown = Ms.LeftButton == ButtonState.Pressed;
            RMBDown = Ms.RightButton == ButtonState.Pressed;
            MMBDown = Ms.MiddleButton == ButtonState.Pressed;
            LMBHit = LMBDown && !LMBStop;
            RMBHit = RMBDown && !RMBStop;
            MMBHit = MMBDown && !MMBStop;
            LMBHitUp = !LMBDown && LMBStop;
            RMBHitUp = !RMBDown && RMBStop;
            MMBHitUp = !MMBDown && MMBStop;

            if (RMBHit && DragItem != null)
            {
                DragItem = null; //Right click always cancels item drag.
                return;
            }

            //Sometimes we want the GUI to stop until the user lets go of the mouse button. Eg, when the user clicks outside a popupmenu to close it
            if (NeedMouseRelease)
                if (!LMBDown && !RMBDown && !MMBDown)
                    NeedMouseRelease = false;
                else
                    return;

            //Don't let the user interact with windows until finished map scrolling.
            if (mouseScrolling)
                if (!MMBDown) mouseScrolling = false;
                else {
                    Gfx.Scroll.X -=  (float)(Ms.X - mouseScrollX) / (float)Gfx.ZoomSizeW;
                    Gfx.Scroll.Y -=  (float)(Ms.Y - mouseScrollY) / (float)Gfx.ZoomSizeH;
                    mouseScrollX = Ms.X;
                    mouseScrollY = Ms.Y;
                    return;
                }

            if (bringFrontWin != null)
            {
                bringToFront(bringFrontWin);
                bringFrontWin = null;
            }

            bool interacted = false;
            bool mouseoverwindow = false;

            if (doMoveWindow()) return;
            if (doResizingWindow()) return;

            //Check for interaction with window or control on it
            foreach (GuiWindow win in GuiWindows.Reverse<GuiWindow>()) 
            {
                mouseoverwindow |= win.Visible && win.MouseIsInside();
                interacted = win.Handle();
                if (win.KillMe)
                {
                    win.Close();

                    //See if there are any modal windows still visible. If not, we can unpause the world. 
                    if (win.Modal)
                    {
                        if (!GuiWindows.Any(n => (n.Modal && n.Visible)))
                            WorldModalPaused = false;
                    }
                }
                else
                {
                    //If the window is modal, don't update the world or any windows beneath this one.
                    if (win.Modal && win.Visible) { WorldModalPaused = true; interacted = true; }

                    if (interacted)
                    {
                        bringToFront(win);
                        break; //Don't handle any windows below the modal window
                    }
                }
            }

            if (mouseoverwindow) Gfx.SetCursor(eCursor.SWORD);

            if (!mouseoverwindow && Game.CurrentMap != null && Gfx.FadeMode == 0) //!interacted
            {
                //User hasn't gone near a window, so check the map
                if (!WorldModalPaused && MMBHit) {

                    if (!mouseScrolling) {
                        mouseScrolling = true;
                        mouseScrollX = Ms.X;
                        mouseScrollY = Ms.Y;
                    }

                }

                Location mloc = Gfx.GetTileAtMouse(Ms);

                IMap map = Game.CurrentMap;

                string tt = map.GetToolTipMessage(mloc);

                if (tt != null && tt != "" && ActiveToolTip == null)//GetWindowOfType(typeof(PopUpMenu)) == null)
                {
                    new ToolTipV2(true, Gfx.GetMapMouseRect(), tt, -1);
                }

                if (Game.PlayerTargeting)
                {
                    switch (Action.TargetWhat)
                    {
                        case eAction.TargetSearch:
                            Gfx.SetCursor(eCursor.LOOK); break;
                        case eAction.TargetTalk:
                            Gfx.SetCursor(eCursor.TALK); break;
                        case eAction.TargetUse:
                            Gfx.SetCursor(eCursor.USE); break;
                        default:
                            Gfx.SetCursor(eCursor.TARGET); break;
                    }
                }
                else if (Game.Turn == eTurn.PLAYER && Party.ActivePC != null)
                {
                    var dir = new Direction(Party.ActivePC.Pos, mloc);
                    Gfx.SetCursor(dir.ToCursor());
                }   
                else
                    Gfx.SetCursor(eCursor.SWORD);


                if (!WorldModalPaused)
                {
                    if (LMBHitUp)
                    {
                        if (Game.PlayerTargeting)
                        {
                            new Action(eAction.MapClick) { Loc = mloc };
                        }
                        else
                        {
                            //Clicked on map to move current PC/Party. Need to know which direction to move

                            if (Party.ActivePC != null)
                            {
                                var dir = new Direction(Party.ActivePC.Pos, mloc);
                                new Action(dir.ToAction());
                            }

                        }
                    }
                    else if (RMBHitUp)
                    {
                        if (!Game.PlayerTargeting)
                        {
                            var options = Game.CurrentMap.GetPopUpMenuOptions(mloc, Party.Pos);
                            if (options != null)
                                new PopUpMenu(Game.CurrentMap.HandleMapPopUp, options);
                        }
                        else
                        {
                            new Action(eAction.Cancel);
                        }
                    }
                }
            }

        }

        static bool doMoveWindow()
        {
            if (moveWindow == null) return false;//Not moving a window

            if (LMBDown)
            {
                moveWindow.Move(Ms.X - moveWinOrgX, Ms.Y - moveWinOrgY);
                moveWinOrgX = Ms.X;
                moveWinOrgY = Ms.Y;
            }
            else moveWindow = null;
            return true;
        }
        static bool doResizingWindow()
        {
            if (resizeWindow == null) return false;

            if (LMBDown)
            {
                resizeWindow.Resize(resizeWindow.Width, resizeWindow.Height + Ms.Y - resizeWinOrgY);
                resizeWinOrgY = Ms.Y;
            }
            else
                resizeWindow = null;
            return true;
        }


        public static void Draw(SpriteBatch sb)
        {
            Ms = Mouse.GetState();

            sb.Begin(SpriteSortMode.Immediate, BlendState.NonPremultiplied, null, null, Gfx.RasterizerWotsit);

            foreach (GuiWindow win in GuiWindows) win.Draw(sb);

            if (ActiveToolTip != null) ActiveToolTip.Draw(sb);

            NewsLine.DrawAll(sb);

            //Draw mouse pointer
            if (Game.ErrorFlagged || Gfx.FadeMode == 0  || Gui.WorldModalPaused)
            {
                if (DragItem != null) 
                    DragItem.DrawOffMapSimple(sb, new Vector2(Ms.X, Ms.Y), Color.White);
                else
                    Gfx.DrawCursor(Ms);
            }
            sb.End();
        }

        public static GuiWindow GetWindowOfType(Type typeofwindow)
        {
            try
            {
                return GuiWindows.First(n => n.GetType() == typeofwindow);
            }
            catch (InvalidOperationException) //Couldn't find the window we wanted.
            {
                return null;
            }
        }

        public static bool errorReporting = false;
        public static void ErrorReport(string msg1, string msg2)
        {
            if (!errorReporting)
            {
                errorReporting = true;
                Gui.WorldModalPaused = true;
                Gui.GuiWindows.Clear();
                new ErrorWindow(msg1, msg2);
            }
        }
    }
}
