using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.Xna.Framework.Audio;

namespace SwordsOfExileGame;

public static class Sound
{
    public static bool Suppress = false;

    private static int _Volume = 10;

    public static int Volume { get => _Volume;
        set { _Volume = value; SoundEffect.MasterVolume = _Volume / 10f; } }

    private static Dictionary<string, SoundEffect> sfxLib = new();

    private static List<SoundEffect> Played = new();

    public static int IndexOf(string key)
    {
        if (key is null or "") return -1;
            
        if (!sfxLib.ContainsKey(key)) throw new Exception("Sound not found"); //TODO: Replace with proper error
            
        return sfxLib.Values.ToList().IndexOf(sfxLib[key]);
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

        foreach (var f in files)
        {
            var s = Path.GetFileNameWithoutExtension(f);

            if (sfxLib.ContainsKey(s))
                sfxLib[s] = fromFile(f);
            else
                sfxLib.Add(s, fromFile(f));
        }

    }

    private static SoundEffect fromFile(string path)
    {
        SoundEffect s;

        using (Stream fileStream = File.OpenRead(path))
            s = SoundEffect.FromStream(fileStream);

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
        if (s is null or "") return;
        if (!sfxLib.ContainsKey(s)) Game.AddMessage("ERROR: Sound not found"); //TODO: Replace with proper error

        if (!Played.Contains(sfxLib[s]))
        {
            sfxLib[s].Play();
            Played.Add(sfxLib[s]);
        }
    }

    public static void ItemSound()
    {
        Play("001_lowbeep");
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

    public static void SysBeep(int n) { }
}