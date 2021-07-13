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
    public class Timer : IListEntity
    {
        static public ExileList<Timer> List = new ExileList<Timer>();

        public string ID { get { return id; } set { id = value; } }
        string id;

        bool Enabled = true;
        int StartCount; //The starting count of the timer
        int Count;      //The current count of the timer. It goes down by 1 every turn.
        string Func; //SpecialNode Node;
        bool Recurring; //The scenario/town timers that are created when the scenario is loaded are all recurring - Once they count down to zero and the event is triggered, they reset back to StartCount and repeat.

        //Timers that are created during play by the special node types 13 & 195 (Start General Timer) are deactivated once the timer hits 0
        IMap Domain; //Null if the timer is global

        //Stores how the timer behaves when not in its domain. This does not apply to Global timers.
        //Timers from converted BoE scenarios are all CONTINUE, except party town timers (created by node type 195) which is DELETE
        eTimerType Behaviour; //A byte

        static public void LoadGame(BinaryReader file)
        {
            List.Clear();
            int count = file.ReadInt32();
            for (int n = 0; n < count; n++)
            {
                Timer t = new Timer();
                t.id = file.ReadString();
                t.Enabled = file.ReadBoolean();
                t.StartCount = file.ReadInt32();
                t.Count = file.ReadInt32();
                t.Func = file.ReadString();
                t.Recurring = file.ReadBoolean();

                int d = file.ReadInt32();
                if (d == -1)
                    t.Domain = null;
                else if (d == -2)
                {
                    t.Domain = Game.WorldMap;
                    t.Behaviour = (eTimerType)file.ReadByte();
                }
                else
                {
                    t.Domain = TownMap.List[d];
                    t.Behaviour = (eTimerType)file.ReadByte();
                }                   
                List.Add(t);
            }
        }

        static public void SaveGame(BinaryWriter file)
        {
            file.Write(List.Count);
            foreach (Timer t in List)
            {
                file.WriteStuff(t.id, t.Enabled, t.StartCount, t.Count, t.Func.DeNull(), t.Recurring);
                if (t.Domain == null)
                    file.Write(-1);
                else
                {
                    if (t.Domain is TownMap)
                        file.Write(((TownMap)t.Domain).Num);
                    else if (t.Domain is WorldMapType)
                        file.Write(-2);

                    file.Write((byte)t.Behaviour);
                }
            }
        }

        static public void ResetLocalTimers(IMap domain)
        {
            List<Timer> to_delete = new List<Timer>();

            foreach (Timer t in List)
            {
                if (t.Domain == domain)
                    if (t.Behaviour == eTimerType.RESET)
                        t.Count = t.StartCount;
                    else if (t.Behaviour == eTimerType.DELETE)
                        to_delete.Add(t);
            }

            foreach (Timer t in to_delete)
                List.Remove(t);
        }

        public Timer() { }

        public void Load(BinaryReader In)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            Enabled = In.ReadBoolean();
            StartCount = In.ReadInt16();
            Count = StartCount;
            Func = In.ReadString();
            string s = In.ReadString();
            if (s == "")
                Domain = null;
            else if (s == "\n")
                Domain = Game.WorldMap;
            else if (TownMap.List.Contains(s))
                Domain = TownMap.List[s];
            else
                Domain = TownMap.List[0];

            if (Domain != null)
                Behaviour = (eTimerType)In.ReadByte();

            Recurring = In.ReadBoolean();
            List.Add(this);

        }

        //Constructor for a non-recurring timer (called by script)
        public Timer(string _id, IMap domain, int moves, bool recurring, string func, eTimerType behaviour = eTimerType.CONTINUE)
        {
            id = _id;
            StartCount = moves;
            Count = StartCount;
            Func = func;//if (nodeno > -1) Node = list[nodeno];
            Behaviour = behaviour;
            Domain = domain;
            Recurring = recurring;
            List.Add(this);
        }

        static public bool Update(int age_increase)
        {
            List<Timer> to_delete = new List<Timer>();
            bool triggered = false;

            foreach (Timer t in List)
            {
                if (t.Enabled)
                {
                    bool in_domain = t.Domain == null || t.Domain == Game.CurrentMap;

                    if (in_domain || t.Behaviour == eTimerType.CONTINUE)
                        t.Count -= age_increase;

                    if (t.Count <= 0)
                    {
                        if (in_domain)
                        {
                            //The Timer is triggered!
                            Script.New_General(t.Func, eCallOrigin.TIMER);
                            triggered = true;
                        }

                        if (t.Recurring)
                        {
                            t.Count = t.StartCount + t.Count;
                            if (t.Count <= 0) t.Count = t.StartCount;
                        }
                        else
                            to_delete.Add(t);
                    }
                }
            }


            foreach (Timer t in to_delete)
                List.Remove(t);

            return triggered;
        }
    }

}