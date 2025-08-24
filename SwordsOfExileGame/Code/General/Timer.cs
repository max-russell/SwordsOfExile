using System.IO;
using System.Collections.Generic;

namespace SwordsOfExileGame;

public class Timer : IListEntity
{
    public static ExileList<Timer> List = new();

    public string ID { get; set; }

    private bool Enabled = true;
    private int StartCount; //The starting count of the timer
    private int Count;      //The current count of the timer. It goes down by 1 every turn.
    private string Func;
    private bool Recurring; //The scenario/town timers that are created when the scenario is loaded are all recurring - Once they count down to zero and the event is triggered, they reset back to StartCount and repeat.

    //Timers that are created during play by the special node types 13 & 195 (Start General Timer) are deactivated once the timer hits 0
    private IMap Domain; //Null if the timer is global

    //Stores how the timer behaves when not in its domain. This does not apply to Global timers.
    //Timers from converted BoE scenarios are all CONTINUE, except party town timers (created by node type 195) which is DELETE
    private eTimerType Behaviour; //A byte

    public static void LoadGame(BinaryReader file)
    {
        List.Clear();
        var count = file.ReadInt32();
        for (var n = 0; n < count; n++)
        {
            var t = new Timer();
            t.ID = file.ReadString();
            t.Enabled = file.ReadBoolean();
            t.StartCount = file.ReadInt32();
            t.Count = file.ReadInt32();
            t.Func = file.ReadString();
            t.Recurring = file.ReadBoolean();

            var d = file.ReadInt32();
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

    public static void SaveGame(BinaryWriter file)
    {
        file.Write(List.Count);
        foreach (var t in List)
        {
            file.WriteStuff(t.ID, t.Enabled, t.StartCount, t.Count, t.Func.DeNull(), t.Recurring);
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

    public static void ResetLocalTimers(IMap domain)
    {
        var to_delete = new List<Timer>();

        foreach (var t in List)
        {
            if (t.Domain == domain)
                if (t.Behaviour == eTimerType.RESET)
                    t.Count = t.StartCount;
                else if (t.Behaviour == eTimerType.DELETE)
                    to_delete.Add(t);
        }

        foreach (var t in to_delete)
            List.Remove(t);
    }

    public Timer() { }

    public void Load(BinaryReader In)
    {
        ID = In.ReadString();
        In.ReadString();
        Enabled = In.ReadBoolean();
        StartCount = In.ReadInt16();
        Count = StartCount;
        Func = In.ReadString();
        var s = In.ReadString();
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
        ID = _id;
        StartCount = moves;
        Count = StartCount;
        Func = func;
        Behaviour = behaviour;
        Domain = domain;
        Recurring = recurring;
        List.Add(this);
    }

    public static bool Update(int age_increase)
    {
        var to_delete = new List<Timer>();
        var triggered = false;

        foreach (var t in List)
        {
            if (t.Enabled)
            {
                var in_domain = t.Domain == null || t.Domain == Game.CurrentMap;

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


        foreach (var t in to_delete)
            List.Remove(t);

        return triggered;
    }
}