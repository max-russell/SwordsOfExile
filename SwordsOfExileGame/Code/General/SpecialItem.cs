using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace SwordsOfExileGame
{

    public class SpecialItem : IListEntity
    {

        public static ExileList<SpecialItem> List = new ExileList<SpecialItem>();//All special items in the scenario
        public static ExileList<SpecialItem> Collected = new ExileList<SpecialItem>(); //All special items the party has collected 

        public static void Clear() { List.Clear(); Collected.Clear(); }

        public static void LoadGame(BinaryReader file)
        {
            Collected.Clear();
            int count = file.ReadInt32();
            for (int n = 0; n < count; n++)
            {
                string key = file.ReadString();
                Collected.Add(List[key]);
            }
        }

        public static void SaveGame(BinaryWriter file)
        {
            file.Write(Collected.Count);
            foreach (SpecialItem s in Collected)
                file.Write(s.id);
        }

        public string ID { get { return id; } set { id = value; } }
        string id;
        public string Name, Description;
        public bool Useable, StartWith;
        public string UseFunc; //SpecialNode UseNode;

        public SpecialItem() { }

        public void Load(BinaryReader In)
        {
            id = In.ReadString();
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

        //public void use_spec_item() {

        //run_special(8, 0, scenario.special_item_special[item], null_loc, &i, &j, &k); TODO
        //}

        //public void put_spec_item_info() {
        //    //        display_strings(data_store5->scen_strs[60 + 1 + which_i * 2], "",
        //    //-1, -1, -1, -1,
        //    //data_store5->scen_strs[60 + which_i * 2], 57, 1600 + scenario.intro_pic, 0);
        //    DisplayStringsForm.Go(Description, "", -1, -1, -1, -1, Name, 57, 1600 + BoE.Scenario.IntroPic);
        //}

    }

}