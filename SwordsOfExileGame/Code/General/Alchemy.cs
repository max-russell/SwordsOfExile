using System;
using System.Collections.Generic;
using System.IO;

namespace SwordsOfExileGame;

public class Recipe : IListEntity
{
    public static readonly ExileList<Recipe> List = new();

    private static readonly Dictionary<string, string> IngredientKeys = new();

    public static string GetIngredientName(string key)
    {
        return IngredientKeys.TryGetValue(key, out var name) ? name : "Unknown";
    }

    public string ID { get; set; } = string.Empty;

    public string Name, Description;
    public int Skill;
    public int Price;
    public Item Creates;
    public int Amount;
    public readonly List<Tuple<string, int>> Ingredients = new();

    public static void LoadIngredients(BinaryReader @in)
    {
        IngredientKeys.Clear();
        int num = @in.ReadInt16();

        for (var n = 0; n < num; n++)
            IngredientKeys.Add(@in.ReadString(), @in.ReadString());
    }
    
    public void Load(BinaryReader @in)
    {
        ID = @in.ReadString();
        @in.ReadString(); //Folder: disregard
        Name = @in.ReadString();
        Description = @in.ReadString();
        Skill = @in.ReadInt32();
        Price = @in.ReadInt32();
        var s = @in.ReadString();
        if (Item.List.Contains(s)) Creates = Item.List[s];
        Amount = @in.ReadInt32();

        int num = @in.ReadInt16();
        for (var n = 0; n < num; n++)
        {
            s = @in.ReadString();
            Ingredients.Add(new Tuple<string, int>(s, @in.ReadInt32()));
        }
        List.Add(this);
    }
}