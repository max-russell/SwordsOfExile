using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework.Input;

namespace SwordsOfExileGame
{
    public static class KeyHandler
    {
        //Keyboard Routines
        static KeyboardState testKeys, oldKeys;
        static int keyRepeatTime;
        static Keys keyRepeat;

        public static int ScrollWheel = 0;

        static Keys hitKey;


        public static bool KeyHit(Keys k)
        {

            if (k != Keys.None && hitKey == k)
            {
                hitKey = Keys.None; 
                return true;
            }
            return false;
        }

        public static bool AnyKeysHit(params Keys[] ka) { foreach (Keys k in ka) if (KeyHit(k)) return true; return false; }
        public static bool KeyDown(Keys k) { return testKeys.IsKeyDown(k); }
        public static bool AnyKeysDown(params Keys[] ka) { foreach (Keys k in ka) if (testKeys.IsKeyDown(k)) return true; return false; }
        public static void GetKeysHit(int elapsedtime)
        {
            keyRepeatTime = Math.Max(keyRepeatTime - elapsedtime, 0);
            oldKeys = testKeys;
            testKeys = Keyboard.GetState();

            Keys[] nk = testKeys.GetPressedKeys();
            Keys[] ok = oldKeys.GetPressedKeys();

            hitKey = Keys.None;

            if (!Game.Instance.IsActive) return;

            var allHitKeys = new List<Keys>();

            if (nk.Length > 0)
            {
                allHitKeys = nk.Except(ok).ToList<Keys>();

                if (allHitKeys.Count > 0)
                {
                    hitKey = allHitKeys[0];

                    keyRepeat = hitKey;
                    keyRepeatTime = Constants.KEY_REPEAT_DURATION_1ST;
                }
                else if (KeyDown(keyRepeat) && keyRepeatTime == 0)
                {
                    keyRepeatTime = Constants.KEY_REPEAT_DURATION_SUBSEQUENT;
                    hitKey = keyRepeat;
                }

            }

        }

        public static void GetActionKeys()
        {
            //Handle map zooming with mouse scroll wheel
            MouseState ms = Mouse.GetState();
            if (ScrollWheel < ms.ScrollWheelValue)
            {
                Gfx.StartZoom(false, Constants.ZOOM_SPEED);
                ScrollWheel = ms.ScrollWheelValue;
            }
            else if (ScrollWheel > ms.ScrollWheelValue)
            {
                Gfx.StartZoom(true, Constants.ZOOM_SPEED);
                ScrollWheel = ms.ScrollWheelValue;
            }

            if (hitKey != Keys.None)
            {
                if (hitKey == Keys.Up) Gfx.Scroll.Y -= 1;
                else if (hitKey == Keys.Down) Gfx.Scroll.Y += 1;
                else if (hitKey == Keys.Left) Gfx.Scroll.X -= 1;
                else if (hitKey == Keys.Right) Gfx.Scroll.X += 1;
                else if (hitKey == KeyHandler.KeyMap[26]) Gfx.StartZoom(false, Constants.ZOOM_SPEED);
                else if (hitKey == KeyHandler.KeyMap[27]) Gfx.StartZoom(true, Constants.ZOOM_SPEED);
            }

            if (!Action.Exists() && hitKey != Keys.None)
            {
                if (hitKey == Keys.Escape && Action.LockActions == eAction.NONE && !Gui.WorldModalPaused)
                {
                    new Action(eAction.EscapeMenu);
                }
                else if ((hitKey == Keys.Oem8 || hitKey == Keys.OemTilde) && Action.LockActions == eAction.NONE && !Gui.WorldModalPaused)
                {
                    new Action(eAction.RunConsoleWindow);
                    return;
                }
                else if (hitKey == KeyHandler.KeyMap[16]) new Action(eAction.Up);
                else if (hitKey == KeyHandler.KeyMap[15]) new Action(eAction.UpLeft);
                else if (hitKey == KeyHandler.KeyMap[17]) new Action(eAction.UpRight);
                else if (hitKey == KeyHandler.KeyMap[18]) new Action(eAction.Left);
                else if (hitKey == KeyHandler.KeyMap[19]) new Action(eAction.Right);
                else if (hitKey == KeyHandler.KeyMap[20]) new Action(eAction.DownLeft);
                else if (hitKey == KeyHandler.KeyMap[21]) new Action(eAction.Down);
                else if (hitKey == KeyHandler.KeyMap[22]) new Action(eAction.DownRight);
                else if (hitKey == KeyHandler.KeyMap[23]) new Action(eAction.QuickSave);
                else if (hitKey == KeyHandler.KeyMap[24]) new Action(eAction.QuickLoad);
                else
                {
                    if (!Game.PlayerTargeting)
                    {
                        if (hitKey == KeyHandler.KeyMap[12]) new Action(eAction.StandReady);
                        else if (hitKey >= Keys.D1 && hitKey <= Keys.D6)
                        {
                            new Action(eAction.ChangeCurrentPC)
                            {
                                PC = Game.CurrentParty.PCList[(int)(hitKey - Keys.D1)]
                            };
                        }
                    }
                    else
                    {
                        switch (hitKey)
                        {
                            case Keys.M: new Action(eAction.Cancel); break;
                            case Keys.Space: new Action(eAction.Space); break;
                            case Keys.A: new Action(eAction.TargetLetterSelectA); break;
                            case Keys.B: new Action(eAction.TargetLetterSelectB); break;
                            case Keys.C: new Action(eAction.TargetLetterSelectC); break;
                            case Keys.D: new Action(eAction.TargetLetterSelectD); break;
                            case Keys.E: new Action(eAction.TargetLetterSelectE); break;
                            case Keys.F: new Action(eAction.TargetLetterSelectF); break;
                            case Keys.G: new Action(eAction.TargetLetterSelectG); break;
                            case Keys.H: new Action(eAction.TargetLetterSelectH); break;
                            case Keys.I: new Action(eAction.TargetLetterSelectI); break;
                            case Keys.J: new Action(eAction.TargetLetterSelectJ); break;
                            case Keys.K: new Action(eAction.TargetLetterSelectK); break;
                            case Keys.L: new Action(eAction.TargetLetterSelectL); break;
                        }
                    }
                }
            }

            if (Action.Exists()) Gui.ActiveToolTip = null;
        }

        ///// <summary>
        ///// Returns the key that has been hit.
        ///// </summary>
        ///// <returns></returns>
        public static Keys GetAllKeysHit() //Relies on GetKeysHit being called at the start of each update
        {
            Keys k = hitKey;
            return k;
        }

        public static void FlushHitKey()
        {
            hitKey = Keys.None;
        }


        [System.Runtime.InteropServices.DllImport("user32.dll")]
        static extern int ToUnicode(uint virtualKeyCode, uint scanCode,
            byte[] keyboardState,
            [System.Runtime.InteropServices.Out, System.Runtime.InteropServices.MarshalAs(System.Runtime.InteropServices.UnmanagedType.LPWStr, SizeConst = 64)]
            StringBuilder receivingBuffer,
            int bufferSize, uint flags);

        public static char GetCharsFromKeys(Keys keys, bool shift, bool altGr)
        {
            var buf = new StringBuilder(256);
            var keyboardState = new byte[256];

            if (shift) keyboardState[16] = 0xff;
            if (altGr) keyboardState[18] = 0xff;

            ToUnicode((uint)keys, 0, keyboardState, buf, 256, 0);
            if (buf.Length > 0)
                return buf.ToString()[0];
            else
                return ' ';
        }

        public static string GetStringFromKeys(Keys keys)
        {
            var buf = new StringBuilder(256);
            var keyboardState = new byte[256];

            switch (keys)
            {
                case Keys.F1: return "F1";
                case Keys.F2: return "F2";
                case Keys.F3: return "F3";
                case Keys.F4: return "F4";
                case Keys.F5: return "F5";
                case Keys.F6: return "F6";
                case Keys.F7: return "F7";
                case Keys.F8: return "F8";
                case Keys.F9: return "F9";
                case Keys.F10: return "F10";
                case Keys.F11: return "F11";
                case Keys.F12: return "F12";
                case Keys.Space: return "(Space)";
                case Keys.D7: return "7";
                case Keys.D8: return "8";
                case Keys.D9: return "9";
                case Keys.D0: return "0";
                case Keys.OemMinus: return "-";
                case Keys.OemPlus: return "+";
                case Keys.OemQuestion: return "?";
                case Keys.OemSemicolon: return ";";
                case Keys.OemTilde: case Keys.Oem8: return "`";
                case Keys.PageDown: return "Page Down";
                case Keys.PageUp: return "Page Up";
                case Keys.Home: return "Home";
                case Keys.End: return "End";
                case Keys.Insert: return "Insert";
                case Keys.Delete: return "Delete";
                case Keys.NumPad0: return "NumPad 0";
                case Keys.NumPad1: return "NumPad 1";
                case Keys.NumPad2: return "NumPad 2";
                case Keys.NumPad3: return "NumPad 3";
                case Keys.NumPad4: return "NumPad 4";
                case Keys.NumPad5: return "NumPad 5";
                case Keys.NumPad6: return "NumPad 6";
                case Keys.NumPad7: return "NumPad 7";
                case Keys.NumPad8: return "NumPad 8";
                case Keys.NumPad9: return "NumPad 9";
                case Keys.OemComma: return ",";
                case Keys.OemPeriod: return ".";
                case Keys.OemOpenBrackets: return "[";
                case Keys.OemCloseBrackets: return "]";
                case Keys.Add: return "NumPad +";
                case Keys.Subtract: return "NumPad -";
                case Keys.Multiply: return "NumPad *";
                case Keys.Divide: return "NumPad /";
            }

            ToUnicode((uint)keys, 0, keyboardState, buf, 256, 0);
            if (buf.Length > 0)
                return buf.ToString().ToUpper();
            else
                return "...";
        }

        public static readonly string[] KeyMapNames = {
                "Look/Search",//0
                "Talk",//1
                "Gather/Loot",//2
                "Use",//3
                "Cast Mage Spell",//4
                "Cast Priest Spell",//5
                "Fire Ranged",//6
                "Alchemy",//7
                "Set Up Camp",//8
                "Start Combat",//9
                "End Combat",//10
                "Wait",//11
                "Stand Ready",//12
                "Defend",//13
                "Toggle Single\nCharacter",//14
                "Move North-West",//15
                "Move North",//16
                "Move North-East",//17
                "Move West",//18
                "Move East",//19
                "Move South-West",//20
                "Move South",//21
                "Move South-East",//22
                "Quick Save",//23
                "Quick Load",//24
                "Toggle Map View",//25
                "Zoom In Map",//26
                "Zoom Out Map", //27
                "Show/Hide\nInventory",//28
                "Show/Hide\nCharacter Stats"};//29

        public static Keys[] KeyMap = new Keys[30];

        public static readonly Keys[] Default1KeyMap = {
                                                Keys.L,//    Look
                                                Keys.T,//    Talk
                                                Keys.G,//    Loot
                                                Keys.U,//    Use
                                                Keys.M,//    Cast Mage Spell
                                                Keys.P,//    Cast Priest Spell
                                                Keys.S,//    Fire Ranged
                                                Keys.Y,//    Alchemy
                                                Keys.H,//    Camp
                                                Keys.F,//    Start Combat
                                                Keys.F,//    End Combat
                                                Keys.W,//    Wait
                                                Keys.NumPad5,// Stand Ready
                                                Keys.D,//    Defend
                                                Keys.K,//    Toggle Single Character
                                                Keys.NumPad7,// Move NW
                                                Keys.NumPad8,// Move N
                                                Keys.NumPad9,// Move NE
                                                Keys.NumPad4,// Move W
                                                Keys.NumPad6,// Move E
                                                Keys.NumPad1,// Move SW
                                                Keys.NumPad2,// Move S
                                                Keys.NumPad3,// Move SE
                                                Keys.F5,//   Quicksave
                                                Keys.F9,//   Quickload
                                                Keys.A,//    Map View
                                                Keys.Add,//    Zoom in map
                                                Keys.Subtract,//    Zoom out map
                                                Keys.I,     //Inventory
                                                Keys.C      //Char stats
                                            };

        public static readonly Keys[] Default2KeyMap = {
                                                Keys.L,//    Look
                                                Keys.T,//    Talk
                                                Keys.G,//    Loot
                                                Keys.U,//    Use
                                                Keys.M,//    Cast Mage Spell
                                                Keys.P,//    Cast Priest Spell
                                                Keys.R,//    Fire Ranged
                                                Keys.Y,//    Alchemy
                                                Keys.H,//    Camp
                                                Keys.F,//    Start Combat
                                                Keys.F,//    End Combat
                                                Keys.O,//    Wait
                                                Keys.S,// Stand Ready
                                                Keys.B,//    Defend
                                                Keys.K,//    Toggle Single Character
                                                Keys.Q,// Move NW
                                                Keys.W,// Move N
                                                Keys.E,// Move NE
                                                Keys.A,// Move W
                                                Keys.D,// Move E
                                                Keys.Z,// Move SW
                                                Keys.X,// Move S
                                                Keys.C,// Move SE
                                                Keys.F5,//   Quicksave
                                                Keys.F9,//   Quickload
                                                Keys.N,//    Map View
                                                Keys.OemPlus,//    Zoom in map
                                                Keys.OemMinus,//    Zoom out map
                                                Keys.I,  //Inventory
                                                Keys.V,  //Stats
                                            };
    }
}