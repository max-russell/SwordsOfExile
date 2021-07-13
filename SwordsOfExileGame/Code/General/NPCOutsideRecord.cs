using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace SwordsOfExileGame
{
    //Stores a group of wandering monsters the party might chance to meet
    public class EncounterRecord : IListEntity
    {
        public static ExileList<EncounterRecord> List = new ExileList<EncounterRecord>();
        public string ID { get { return id; } set { id = value; } }
        string id;

        //public static void Load(BinaryReader In)
        //{
        //    List.Clear();

        //    while (true)
        //    {
        //        byte b = In.ReadByte();

        //        if (b == 0) break;

        //        if (b == 1)
        //            new NPCGroupRecord(In);
        //        else if (b == 2)
        //            Scenario.LoadAndDisregardEditorFolder(In);
        //    }
        //}

        class Component
        {
            public NPCRecord Type;
            public eAttitude Attitude;
            public int Min, Max;

            public Component(BinaryReader In)
            {
                Type = NPCRecord.List[In.ReadInt16()];
                Attitude = (eAttitude)In.ReadInt16();
                Min = In.ReadInt16();
                Max = In.ReadInt16();
            }

        }
        List<Component> Components = new List<Component>();

        public IEnumerable<Tuple<NPCRecord, eAttitude>> EachNPC()
        {
            foreach (Component c in Components)
            {
                int num = Maths.Rand(1, c.Min, c.Max);
                if (num < 1) continue;
                for (int n = 0; n < num; n++)
                {
                    yield return new Tuple<NPCRecord, eAttitude>(c.Type, c.Attitude);
                }
            }
        }

        //public NPCRecord[] Hostiles = new NPCRecord[7];
        //public NPCRecord[] Friendlies = new NPCRecord[3];
        public string FuncOnMeet;
        public string FuncOnWin;
        public string FuncOnFlee;
        public bool CantFlee, //If selected, the encounter will not flee, no matter how strong the party is. This should always be set for special encounters.
                    Forced; //The party will fight the encounter as soon as it appears, even if it isnt anywhere near the party. This should always be set for special encounters, but almost never for wandering encounters.
        //public Location EndSD;
        public string EndVar;


        public EncounterRecord() { }
        public void Load(BinaryReader In)
        {
            id = In.ReadString();

            In.ReadString(); //Editor folder it's in - disregard in game.

            while (In.ReadBoolean())
                Components.Add(new Component(In));

            CantFlee = In.ReadBoolean();
            Forced = In.ReadBoolean();

            EndVar = In.ReadString();

            FuncOnMeet = In.ReadString();
            FuncOnFlee = In.ReadString();
            FuncOnWin = In.ReadString();

            EncounterRecord.List.Add(this);
        }

        public NPCRecord GetChiefMonster() //Gets the monster that represents the whole group when on the outside map
        {
            return Components[0].Type;
        }

        /// <summary>
        /// Get total level of all NPCs in encounter (Don't know exact numbers until they're spawned, so get average expected)
        /// </summary>
        public int out_enc_lev_tot
        {
            get
            {
                float count = 0;
                if (CantFlee == true) return int.MaxValue;
                foreach (Component c in Components)
                {
                    if (c.Attitude == eAttitude.HOSTILE_A || c.Attitude == eAttitude.HOSTILE_B)
                        count += (float)c.Type.Level * (((float)c.Max - (float)c.Min) / 2f + (float)c.Min);
                }
                return (int)count;
            }
        }
    }
}