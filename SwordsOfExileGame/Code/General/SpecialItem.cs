using System.IO;
using System.Collections.Generic;

namespace SwordsOfExileGame;

public class SpecialItem : IListEntity
{

    public static ExileList<SpecialItem> List = new();//All special items in the scenario
    public static ExileList<SpecialItem> Collected = new(); //All special items the party has collected 

    public static void Clear() { List.Clear(); Collected.Clear(); }

    public static void LoadGame(BinaryReader file)
    {
        Collected.Clear();
        var count = file.ReadInt32();
        for (var n = 0; n < count; n++)
        {
            var key = file.ReadString();
            Collected.Add(List[key]);
        }
    }

    public static void SaveGame(BinaryWriter file)
    {
        file.Write(Collected.Count);
        foreach (var s in Collected)
            file.Write(s.ID);
    }

    public string ID { get; set; }

    public string Name, Description;
    public bool Useable, StartWith;
    public string UseFunc; 

    public SpecialItem() { }

    public void Load(BinaryReader In)
    {
        ID = In.ReadString();
        In.ReadString(); //Folder: disregard
        Name = In.ReadString();
        Description = In.ReadString();
        if (StartWith = In.ReadBoolean()) Collected.Add(this);
        Useable = In.ReadBoolean();
        UseFunc = In.ReadString();
        List.Add(this);
    }

    static public bool PartyHas(string key)
    {
        return Collected.Contains(key);
    }

    public static IEnumerable<SpecialItem> EachHas()
    {
        foreach (var i in Collected)
            yield return i;
    }
    public static int NumberHas()
    {
        return Collected.Count;
    }


    static public bool Give(string key)
    {
        if (List.Contains(key))
        {
            if (Collected.Contains(key))
            {
                Game.AddMessage("You already have the " + List[key].Name);
                return false;
            }
            Collected.Add(List[key]);
            Game.AddMessage("You get the " + List[key].Name);
            return true;
        }
        return false;
    }

    static public bool Take(string key)
    {
        if (Collected.Contains(key))
        {
            Collected.Remove(key);
            return true;
        }
        return false;
    }
}