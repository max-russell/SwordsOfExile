using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace SwordsOfExileGame
{

    public static class Sound
    {
        public static bool Suppress = false;

        static int _Volume = 10;

        public static int Volume { get { return _Volume; } set { _Volume = value; SoundEffect.MasterVolume = _Volume / 10f; } }

        static Dictionary<string, SoundEffect> sfxLib = new Dictionary<string, SoundEffect>();

        static List<SoundEffect> Played = new List<SoundEffect>();

        public static int IndexOf(string key)
        {
            if (key == null || key == "") return -1;
            
            if (!sfxLib.ContainsKey(key)) throw new Exception("Sound not found"); //TODO: Replace with proper error
            
            return sfxLib.Values.ToList().IndexOf(sfxLib[key]);
            //else
                //return -1;
        }
        public static int Duration(string key)
        {
            return sfxLib[key].Duration.Milliseconds;
        }
        public static int Duration(int index)
        {
            return sfxLib.ElementAt(index).Value.Duration.Milliseconds;
        }

        public static void Refresh()
        {
            Played.Clear();
        }

        public static void Load(bool just_base)
        {
            if (just_base)
                Directory.SetCurrentDirectory(Path.Combine(Game.BaseDirectory, "Sounds"));
            else
            {
                if (!Directory.Exists(Path.Combine(Game.ScenarioDirectory, "Sounds"))) return;
                Directory.SetCurrentDirectory(Path.Combine(Game.ScenarioDirectory, "Sounds"));
            }

            var files = Directory.GetFiles(Directory.GetCurrentDirectory(), "*.wav", SearchOption.TopDirectoryOnly).ToList();
            files.Sort();

            foreach (string f in files)
            {
                string s = Path.GetFileNameWithoutExtension(f);

                if (sfxLib.ContainsKey(s))
                    sfxLib[s] = fromFile(f);
                else
                    sfxLib.Add(s, fromFile(f));
            }

        }

        static SoundEffect fromFile(string path)
        {
            SoundEffect s;

            using (Stream fileStream = File.OpenRead(path))
                //try
                //{
                    s = SoundEffect.FromStream(fileStream);
                //}
                //catch
                //{
                //    s = new SoundEffect(File.ReadAllBytes(path), 22050, AudioChannels.Mono);
                //}

            return s;
        }

        public static void Play(int n)
        {
            if (n < 0 || n >= sfxLib.Count) return;

            var s = sfxLib.ElementAt(n);

            if (!Played.Contains(s.Value))
            {
                s.Value.Play();
                Played.Add(s.Value);
            }
        }

        public static void Play(string s)
        {
            if (s == null || s == "") return;
            if (!sfxLib.ContainsKey(s)) Game.AddMessage("ERROR: Sound not found"); //TODO: Replace with proper error

            if (!Played.Contains(sfxLib[s]))
            {
                sfxLib[s].Play();
                Played.Add(sfxLib[s]);
            }

            //Played.Add(s);
        }

        public static void ItemSound()
        {
            Play("001_lowbeep");

            //sfxLib["001_lowbeep"].Play();
        }

        public static void ButtonSound()
        {
            Play("037_button2");
        }

        public static void WalkSound(TerrainRecord tr, int step)
        {
            if (Game.CurrentParty.IsInABoat())
                Play("048_boatmove");
            else switch (tr.step_sound)
            {
                //case 0:
                //    if (step % 2 == 0)          //footsteps alternate sound
                //        Play(49);
                //    else Play(50);
                //    break;
                case 1:
                    Play(55);         //squish
                    break;
                case 2:
                    Play(47);         //crunch
                    break;
                case 3:
                    break;                //silence : do nothing
                default:
                    if (step % 2 == 0)          //safety footsteps valve
                        Play(49);
                    else Play(50);
                    break;
            }
        }

        //public static void one_sound(int n) { }

        public static void SysBeep(int n) { }

    }
}