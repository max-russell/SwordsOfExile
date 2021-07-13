using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Runtime.InteropServices;
using System.Reflection;
using System.Xml.Linq;

namespace SoE_Converter
{
    partial class Program
    {
        class Recipe
        {
            public string ID = "";
            public string Name = "", Description = "";
            public int Skill;
            public int Price;
            public string Creates = "";
            public int Amount;
            public List<Tuple<string, int>> Ingredients = new List<Tuple<string, int>>();

            static List<Recipe> List;
            static Dictionary<string, string> IngredientKeys = new Dictionary<string, string>();

            void Write(BinaryWriter Out)
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

                XElement xml = XElement.Load("../../Base/Data/Alchemy.xml");

                foreach (XElement recipe in xml.Elements())
                {
                    if (recipe.Name.LocalName == "Recipe")
                    {
                        Recipe r = new Recipe();

                        foreach (XAttribute attr in recipe.Attributes())
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

                        foreach (XElement ing in recipe.Elements())
                        {
                            string req = "";
                            int amt = 1;

                            if (ing.Name.LocalName != "Ingredient") continue;

                            foreach (XAttribute attr2 in ing.Attributes())
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
                        foreach (XAttribute attr in recipe.Attributes())
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

                foreach (Recipe r in List)
                    r.Write(Out);
                Out.Write((byte)0);
            }
        }

        class MagicSpell
        {
            string ID="";
            string Name = "Spell", Description = "";
            bool Mage = true;
            int Level = 1;
            int Cost = 1;
            int Price = 0;
            int Where = 0;
            int Range = 0;
            eSpellTarget Target = eSpellTarget.CASTER;
            int TargetPattern;
            bool MultiTarget = false;
            int Missile = -1;
            string FuncCast="", FuncTargetCount="";

            static List<MagicSpell> List;

            void Write(BinaryWriter Out)
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

                XElement xml = XElement.Load("../../Base/Data/SpellData.xml");

                foreach (XElement spell in xml.Elements())
                {
                    if (spell.Name.LocalName != "Spell") continue;

                    MagicSpell s = new MagicSpell();

                    foreach (XAttribute attr in spell.Attributes())
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

                foreach (MagicSpell spell in List)
                    spell.Write(Out);
                Out.Write((byte)0); //End of spells
            }

            enum eSpellTarget
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