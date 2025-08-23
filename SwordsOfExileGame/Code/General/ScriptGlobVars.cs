using System;
using System.Collections.Generic;
using System.IO;


namespace SwordsOfExileGame;

public class GlobalVariables
{
    private static Dictionary<string, object> globalVariables = new();

    public static void Clear()
    {
        globalVariables.Clear();
    }

    public static bool Contains(string s, Type t)
    {
        Object o;
        if (s != null && s != "" && globalVariables.TryGetValue(s, out o))
        {
            if (o.GetType() == t) return true;
        }
        return false;
    }

    public static void LoadGame(BinaryReader file)
    {
        globalVariables.Clear();
        var count = file.ReadInt32();
        for (var n = 0; n < count; n++)
        {
            var key = file.ReadString();
            switch (file.ReadByte())
            {
                case 0:
                    globalVariables.Add(key, file.ReadInt32()); break;
                case 1:
                    globalVariables.Add(key, file.ReadString()); break;
                case 2:
                    globalVariables.Add(key, file.ReadSingle()); break;
            }
        }
    }

    public static void SaveGame(BinaryWriter file)
    {
        file.Write(globalVariables.Count);
        foreach (var g in globalVariables)
        {
            file.Write(g.Key);
            if (g.Value is Int32)
            {
                file.Write((byte)0);
                file.Write((int)g.Value);
            }
            else if (g.Value is String)
            {
                file.Write((byte)1);
                file.Write((string)g.Value);
            }
            else if (g.Value is Single or Double)
            {
                file.Write((byte)2);
                file.Write((Single)g.Value);
            }
        }
    }

    static public void Load(BinaryReader In)
    {
        var name = In.ReadString();
        object value = null;
        int t = In.ReadInt16();

        switch (t)
        {
            case 0: 
                value = In.ReadInt32();
                break;
        }

        globalVariables.Add(name, value);
    }

    public static int Get(string s)
    {
        object o;

        if (globalVariables.TryGetValue(s, out o))
            return (int)o;
        else
        {
            //Report error!
            return 0;
        }
    }

    public object this[string key, params int[] index] //Convenient way to read or set a global variable.
    {
        get
        {
            //Index is a way to fudge arrays with Global variables.
            foreach (var i in index) key += "_" + i;

            object o;
            if (globalVariables.TryGetValue(key, out o))
                return o;
            else
            {
                //Report error!
                return 0;
            }
        }
        set
        {
            foreach (var i in index) key += "_" + i;

            try
            {
                globalVariables[key] = value;
            }
            catch
            {
                globalVariables.Add(key, value);
            }
        }
    }


}