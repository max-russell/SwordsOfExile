using System;
using System.IO;
using System.Collections.Generic;

namespace SwordsOfExileGame;

public static class Maths
{
    public static Random Rnd = new();

    public static int Rand(int times, int min, int max)
    {
        int store;
        int i, to_ret = 0;

        if ((max - min + 1) == 0)
            return 0;
        for (i = 1; i < times + 1; i++)
        {
            store = Rnd.Next() % (max - min + 1);
            to_ret = to_ret + min + store;
        }
        return to_ret;
    }
    public static float Rand(float lower, float upper)
    {
        if (upper < lower)
        {
            var t = upper;
            upper = lower;
            lower = t;
        }
        return (float)Rnd.NextDouble() * (upper - lower) + lower;
    }


    public static T Max<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) > 0 ? a : b;
    }

    public static T Min<T>(T a, T b) where T : IComparable<T>
    {
        return a.CompareTo(b) < 0 ? a : b;
    }

    public static T MinMax<T>(T min, T max, T val) where T : IComparable<T>
    {
        if (val.CompareTo(min) < 0) return min;
        if (val.CompareTo(max) > 0) return max;
        return val;
    }

    public static bool InRange<T>(List<T> l, int n)
    {
        return n >= 0 && n < l.Count;
    }

    public static void MoveToZero(ref int v)
    {
        if (v > 0) v--;
        else if (v < 0) v++;
    }

    public static int Floor(float v)
    {
        return (int)Math.Floor(v);
    }
    public static int Ceiling(float v)
    {
        return (int)Math.Ceiling(v);
    }

    public static string DeNull(this string s)
    {
        if (s == null) return "";
        return s;
    }

    //Handy extension method for writing locations.
    public static void Write(this BinaryWriter file, Location loc)
    {
        file.Write((short)loc.X);
        file.Write((short)loc.Y);
    }
    public static Location ReadLocation(this BinaryReader file)
    {
        return new Location(file.ReadInt16(), file.ReadInt16());
    }
    public static Direction ReadDirection(this BinaryReader file)
    {
        return new Direction((eDir)file.ReadSByte(), file.ReadBoolean());
    }

    public static void Write(this BinaryWriter file, Direction dir)
    {
        file.Write((sbyte)dir.Dir);
        file.Write(dir.IsFacingRight);
    }
    public static void Write(this BinaryWriter file, ICharacter ch, TownMap town)
    {
        if (ch == null) file.Write(int.MaxValue);
        else if (ch is PCType) file.Write(-1 - ((PCType)ch).Slot);
        else file.Write(town.NPCList.IndexOf((NPC)ch));
    }
    public static ICharacter ReadCharacter(this BinaryReader file, TownMap town)
    {
        var n = file.ReadInt32();
        if (n == int.MaxValue) return null;
        if (n < 0) return Game.CurrentParty.PCList[-(n + 1)];
        return town.NPCList[n];
    }
    public static void WriteStuff(this BinaryWriter file, params object[] obs)
    {
        foreach (var o in obs)
        {
            if (o is int)
                file.Write((int)o);
            else if (o is short)
                file.Write((short)o);
            else if (o is byte)
                file.Write((byte)o);
            else if (o is uint)
                file.Write((uint)o);
            else if (o is ushort)
                file.Write((ushort)o);
            else if (o is sbyte)
                file.Write((sbyte)o);
            else if (o is long)
                file.Write((long)o);
            else if (o is ulong)
                file.Write((ulong)o);
            else if (o is string)
                file.Write((string)o);
            else if (o is Location)
                file.Write((Location)o);
            else if (o is Direction)
                file.Write((Direction)o);
            else if (o is bool)
                file.Write((bool)o);
            else
                throw new Exception("WriteStuff can't write this type.");
        }
    }
}