using System.Collections.Generic;
using System.IO;

namespace SwordsOfExileGame
{

    //Stores information for when first placing an instance of a creature in a town
    public class NPCPreset
    {
        public NPCRecord Record;
        public eAttitude Attitude;
        public Location Pos;
        public bool Mobile = true;
        public eNPCAppear Appear;
        public string LifeVariable; 
        public string AppearVariable; //Global Variable which effects whether an NPC appears or not.
        public int SpecialGroup;
        public short AppearDay;
        public short FacialPic;
        public string FuncOnDeath;

        public bool InstanceWasKilled = false; //For keeping track of when not to reinstantiate an npc on entering town

        public Personality personality;

        public NPCPreset() { }

        public NPCPreset(BinaryReader In)
        {
            int i;
            Record = NPCRecord.List[In.ReadInt16()];
            Attitude = (eAttitude)In.ReadByte();
            Pos = In.ReadLocation();
            Mobile = In.ReadBoolean();
            Appear = (eNPCAppear)In.ReadByte();
            LifeVariable = In.ReadString();

            SpecialGroup = In.ReadSByte();
            AppearVariable = In.ReadString(); 
            AppearDay = In.ReadInt16();
            i = In.ReadInt16(); if (i > -1)
            {
                if (i < Personality.List.Count)
                    personality = Personality.List[i];
            }
            FuncOnDeath = In.ReadString();
            FacialPic = In.ReadInt16();
        }
    }

    public class TownEntrance 
    {
        public Location Pos;
        public TownMap DestTown = null;
        public TerrainRecord TerrainIfHidden;

        public TownEntrance(BinaryReader In, OutsideSector o) {
            var t = In.ReadString();

            TownMap.List.TryGetValue(t, out DestTown);//  t >= 0 && t < TownMap.List.Count)
                Pos = In.ReadLocation();
                if (!TerrainRecord.List.TryGetValue(In.ReadString(), out TerrainIfHidden))
                    TerrainIfHidden = Game.WorldMap.TerrainAt(Game.WorldMap.ToGlobal(Pos, o));
        }
    }

    public class InfoRect
    {
        public Rectangle Rect;
        public string Text;

        public InfoRect(BinaryReader In) {
            Rect = Rectangle.Read(In);
            Text = In.ReadString();
        }
    }

    /// <summary>
    /// Trigger spots are stored in a list with each map. Each terrain record also has a trigger spot associated, but 'Pos' is not used.
    /// </summary>
    public class TriggerSpot
    {
        public Location Pos;
        byte triggeredBy;
        public string Func;
        public Dictionary<string, object> Vars = new Dictionary<string, object>();
        public bool Active = false;

        public TriggerSpot(BinaryReader In, bool no_position = false) {
            if (!no_position)
            {
                Pos = In.ReadLocation();
                Active = In.ReadBoolean();
            }
            else
                Active = true;

            triggeredBy = In.ReadByte(); 
            Func = In.ReadString();

            int count = In.ReadInt16();
            for (int n = 0; n < count; n++)
            {
                string id = In.ReadString();
                switch (In.ReadByte())
                {
                    case 0: Vars.Add(id, In.ReadInt32()); break;
                    case 1: Vars.Add(id, In.ReadString()); break;
                    case 2: Vars.Add(id, In.ReadSingle()); break;
                }
            }
        }

        public bool TriggeredBy(eTriggerSpot what)
        {
            return Active && ((triggeredBy & (byte)what) != 0);
        }

    }

    public class PresetItem
    {
        public Location Pos;
        public Item Record; //References the item type in the Scenario list.
        public Item Instance; //References the actual item in the game created from this preset
        public int Charges;
        public bool AlwaysThere, Property, Contained;

        public PresetItem(BinaryReader In) {
            Item.List.TryGetValue(In.ReadString(), out Record);///*Int16()*/];
            Pos = In.ReadLocation();
            Charges = In.ReadInt16();
            AlwaysThere = In.ReadBoolean();
            Property = In.ReadBoolean();
            Contained = In.ReadBoolean();
        }
    }

    public class PresetField
    {
        public Location Pos;
        public Field Type;
        public PresetField(BinaryReader In) {
            Type = Field.List[In.ReadInt16()];
            Pos = In.ReadLocation();
        }
    }

}
