using System;
using System.Collections.Generic;
using System.IO;

namespace SwordsOfExileGame
{
    public class Recipe : IListEntity
    {
        public static ExileList<Recipe> List = new ExileList<Recipe>();

        public static Dictionary<string, string> IngredientKeys = new Dictionary<string, string>();

        public static string GetIngredientName(string key)
        {
            string name;
            if (IngredientKeys.TryGetValue(key, out name))
                return name;
            else
                return "Unknown";
        }

        public string ID { get { return id; } set { id = value; } }
        string id = "";
        public string Name, Description;
        public int Skill;
        public int Price;
        public Item Creates;
        public int Amount;
        public List<Tuple<string, int>> Ingredients = new List<Tuple<string, int>>();

        public static void LoadIngredients(BinaryReader In)
        {
            IngredientKeys.Clear();
            int num = In.ReadInt16();

            for (int n = 0; n < num; n++)
                IngredientKeys.Add(In.ReadString(), In.ReadString());
        }

        public Recipe() { }
        public void Load(BinaryReader In)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            Name = In.ReadString();
            Description = In.ReadString();
            Skill = In.ReadInt32();
            Price = In.ReadInt32();
            string s = In.ReadString();
            if (Item.List.Contains(s)) Creates = Item.List[s];
            Amount = In.ReadInt32();

            int num = In.ReadInt16();
            for (int n = 0; n < num; n++)
            {
                s = In.ReadString();
                Ingredients.Add(new Tuple<string, int>(s, In.ReadInt32()));
            }
            List.Add(this);
        }
    }
}