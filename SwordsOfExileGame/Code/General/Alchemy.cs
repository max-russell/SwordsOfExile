using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using System.Text;
using System.IO;

namespace SwordsOfExileGame
{
    public class Recipe : IListEntity
    {
        //public static Dictionary<string, Recipe> List = new Dictionary<string,Recipe>();
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

        //public static void LoadAlchemyData(BinaryReader In)
        //{
        //    List.Clear();
        //    IngredientKeys.Clear();

        //    int num = In.ReadInt16();

        //    for (int n = 0; n < num; n++)
        //        IngredientKeys.Add(In.ReadString(), In.ReadString());

        //    num = In.ReadInt16();
        //    for (int x = 0; x < num; x++) new Recipe(In);
        //}

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



        //    XElement xml = null;

        //    if (File.Exists(Path.Combine(Game.ScenarioDirectory, "Data", "Alchemy.xml")))
        //        xml = XElement.Load(Path.Combine(Game.ScenarioDirectory, "Data", "Alchemy.xml"));
        //    else if (File.Exists(Path.Combine(Game.BaseDirectory, "Data", "Alchemy.xml")))
        //        xml = XElement.Load(Path.Combine(Game.BaseDirectory, "Data", "Alchemy.xml"));
        //    else
        //    {
        //        Game.FlagError("Loading Error", "Alchemy.xml not found");
        //        return false;
        //    }

        //    foreach (XElement recipe in xml.Elements())
        //    {

        //        if (recipe.Name.LocalName == "Recipe")
        //        {
        //            Recipe r = new Recipe();

        //            foreach (XAttribute attr in recipe.Attributes())
        //            {
        //                switch (attr.Name.LocalName)
        //                {
        //                    case "ID": r.id =/*s.ID =*/ attr.Value; break;
        //                    case "Name": r.Name = attr.Value; break;
        //                    case "Description": r.Description = attr.Value; break;
        //                    case "Skill": r.Skill = Convert.ToInt32(attr.Value); break;
        //                    case "Price": r.Price = Convert.ToInt32(attr.Value); break;
        //                    case "Amount": r.Amount = Convert.ToInt32(attr.Value); break;
        //                    case "Creates":
        //                        Item i;
        //                        if (Item.List.TryGetValue(attr.Value, out i))
        //                            r.Creates = i;
        //                        break;
        //                }
        //            }

        //            foreach (XElement ing in recipe.Elements())
        //            {
        //                string req = "";
        //                int amt = 1;

        //                if (ing.Name.LocalName != "Ingredient") continue;

        //                foreach (XAttribute attr2 in ing.Attributes())
        //                    if (attr2.Name.LocalName == "Required")
        //                        req = attr2.Value;
        //                    else if (attr2.Name.LocalName == "Amount")
        //                        amt = Convert.ToInt32(attr2.Value);
        //                r.Ingredients.Add(new Tuple<string, int>(req, amt));
        //            }

        //            List.Add(r);
        //        }
        //        else if (recipe.Name.LocalName == "IngredientKey")
        //        {
        //            string id="", name="";
        //            foreach (XAttribute attr in recipe.Attributes())
        //            {
        //                switch (attr.Name.LocalName)
        //                {
        //                    case "ID": id = attr.Value; break;
        //                    case "Name": name = attr.Value; break;
        //                }
        //            }
        //            IngredientKeys.Add(id, name);
        //        }
        //    }
        //    return true;
        //}
    }
}