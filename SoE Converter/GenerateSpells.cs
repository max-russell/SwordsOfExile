using System;
using System.Collections.Generic;
using System.IO;
using System.Xml.Linq;

namespace SoE_Converter
{
    internal partial class Program
    {
        private class Recipe
        {
            public string ID = "";
            public string Name = "", Description = "";
            public int Skill;
            public int Price;
            public string Creates = "";
            public int Amount;
            public List<Tuple<string, int>> Ingredients = new();

            private static List<Recipe> List;
            private static Dictionary<string, string> IngredientKeys = new();

            private void Write(BinaryWriter Out)
            {
                Console.WriteLine("    " + ID);
                Out.Write((byte)1);
                Out.Write(ID);
                Out.Write("");
                Out.Write(Name);
                Out.Write(Description);
                Out.Write(Skill);
                Out.Write(Price);
                Out.Write(Creates);
                Out.Write(Amount);
                Out.Write((short)Ingredients.Count);
                foreach (var i in Ingredients)
                {
                    Out.Write(i.Item1);
                    Out.Write(i.Item2);
                }
            }

            public static void WriteRecipes(BinaryWriter Out)
            {
                List = new List<Recipe>();

                var xml = XElement.Load("../../Base/Data/Alchemy.xml");

                foreach (var recipe in xml.Elements())
                {
                    if (recipe.Name.LocalName == "Recipe")
                    {
                        var r = new Recipe();

                        foreach (var attr in recipe.Attributes())
                        {
                            switch (attr.Name.LocalName)
                            {
                                case "ID": r.ID = attr.Value; break;
                                case "Name": r.Name = attr.Value; break;
                                case "Description": r.Description = attr.Value; break;
                                case "Skill": r.Skill = Convert.ToInt32(attr.Value); break;
                                case "Price": r.Price = Convert.ToInt32(attr.Value); break;
                                case "Amount": r.Amount = Convert.ToInt32(attr.Value); break;
                                case "Creates": r.Creates = attr.Value; break;
                            }
                        }

                        foreach (var ing in recipe.Elements())
                        {
                            var req = "";
                            var amt = 1;

                            if (ing.Name.LocalName != "Ingredient") continue;

                            foreach (var attr2 in ing.Attributes())
                                if (attr2.Name.LocalName == "Required")
                                    req = attr2.Value;
                                else if (attr2.Name.LocalName == "Amount")
                                    amt = Convert.ToInt32(attr2.Value);
                            r.Ingredients.Add(new Tuple<string, int>(req, amt));
                        }

                        List.Add(r);
                    }
                    else if (recipe.Name.LocalName == "IngredientKey")
                    {
                        string id = "", name = "";
                        foreach (var attr in recipe.Attributes())
                        {
                            switch (attr.Name.LocalName)
                            {
                                case "ID": id = attr.Value; break;
                                case "Name": name = attr.Value; break;
                            }
                        }
                        IngredientKeys.Add(id, name);
                    }
                }

                Console.WriteLine("Writing Alchemical Recipes:");

                Out.Write((short)IngredientKeys.Count);

                foreach (var key in IngredientKeys)
                {
                    Out.Write(key.Key);
                    Out.Write(key.Value);
                }

                foreach (var r in List)
                    r.Write(Out);
                Out.Write((byte)0);
            }
        }

        private class MagicSpell
        {
            private string ID="";
            private string Name = "Spell", Description = "";
            private bool Mage = true;
            private int Level = 1;
            private int Cost = 1;
            private int Price = 0;
            private int Where = 0;
            private int Range = 0;
            private eSpellTarget Target = eSpellTarget.CASTER;
            private int TargetPattern;
            private bool MultiTarget = false;
            private int Missile = -1;
            private string FuncCast="", FuncTargetCount="";

            private static List<MagicSpell> List;

            private void Write(BinaryWriter Out)
            {
                Console.WriteLine("    " + ID);
                Out.Write((byte)1);
                Out.Write(ID);
                Out.Write("");
                Out.Write(Name);
                Out.Write(Description);
                Out.Write(Mage);
                Out.Write(Level);
                Out.Write(Cost);
                Out.Write(Price);
                Out.Write(Where);
                Out.Write(Range);
                Out.Write((byte)Target);
                Out.Write((byte)TargetPattern);
                Out.Write(MultiTarget);
                Out.Write(Missile);
                Out.Write(FuncCast);
                Out.Write(FuncTargetCount);
            }

            public static void WriteSpells(BinaryWriter Out)
            {
                List = new List<MagicSpell>();

                var xml = XElement.Load("../../Base/Data/SpellData.xml");

                foreach (var spell in xml.Elements())
                {
                    if (spell.Name.LocalName != "Spell") continue;

                    var s = new MagicSpell();

                    foreach (var attr in spell.Attributes())
                    {
                        switch (attr.Name.LocalName)
                        {
                            case "ID": s.ID = attr.Value; break;
                            case "Name": s.Name = attr.Value; break;
                            case "Description": s.Description = attr.Value; break;
                            case "Mage": s.Mage = Convert.ToBoolean(attr.Value); break;
                            case "Level": s.Level = Convert.ToInt32(attr.Value); break;
                            case "Cost": s.Cost = Convert.ToInt32(attr.Value); break;
                            case "Price": s.Price = Convert.ToInt32(attr.Value); break;
                            case "Where": s.Where = Convert.ToInt32(attr.Value); break;
                            case "Target": s.Target = (eSpellTarget)Convert.ToInt32(attr.Value); break;
                            case "TargetPattern": s.TargetPattern = Convert.ToInt32(attr.Value); break;
                            case "Missile": s.Missile = Convert.ToInt32(attr.Value); break;
                            case "Range": s.Range = Convert.ToInt32(attr.Value); break;
                            case "CastScript":
                                s.FuncCast = attr.Value;
                                break;
                            case "TargetCountScript":
                                s.FuncTargetCount = attr.Value;
                                s.MultiTarget = true;
                                break;
                        }
                    }
                    List.Add(s);
                }

                Console.WriteLine("Writing Spells:");

                foreach (var spell in List)
                    spell.Write(Out);
                Out.Write((byte)0); //End of spells
            }

            private enum eSpellTarget
            {
                CASTER = 0,
                LIVING_PC = 1,
                DEAD_PC = 2,
                CHARACTER = 3,
                LOCATION = 4
            }
        }


    }
}