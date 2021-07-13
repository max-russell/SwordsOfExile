using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;


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
        //public byte extra1, extra2;
        //public short spec1 = -1, spec2 = -1;
        public string LifeVariable; 
        public string AppearVariable; //Global Variable which effects whether an NPC appears or not.
        public int SpecialGroup;//, time_code;
        public short AppearDay;
        public short FacialPic;
        public string FuncOnDeath;//, FuncNonCombatMove, FuncCombatMove;

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

            //i = In.ReadInt16();
            //if (i != -1) LifeVariable = GlobVar.List[i];
            LifeVariable = In.ReadString();

            SpecialGroup = In.ReadSByte();
            AppearVariable = In.ReadString(); //time_code = In.ReadSByte();
            AppearDay = In.ReadInt16();
            i = In.ReadInt16(); if (i > -1)
            {
                if (i < Personality.List.Count)//Personality.List.Exists(n => n.Num == i))
                    personality = Personality.List[i];//.First(n => n.Num == i); //Make sure this is saved right - NOT TOWN RELATIVE NUMBER
            }
            //FuncNonCombatMove = In.ReadString();
            //FuncCombatMove = In.ReadString();
            FuncOnDeath = In.ReadString();
            //i = In.ReadInt16(); if (i > -1 && i < Scenario.SpecialNodeList.Count) OnKill = Scenario.SpecialNodeList[i];
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
            //{
                Pos = In.ReadLocation();
                //Ter = Game.WorldMap.TerrainAt(Game.WorldMap.ToGlobal(Pos, o));
                //TerrainRecord t2;

                if (!TerrainRecord.List.TryGetValue(In.ReadString(), out TerrainIfHidden))
                    TerrainIfHidden = Game.WorldMap.TerrainAt(Game.WorldMap.ToGlobal(Pos, o));

                //if (TerrainRecord.List.TryGetValue(Ter.Flag1, out t2))
                //    TerrainIfHidden = t2;
                //else
                //    TerrainIfHidden = Ter;
            //}
            //else
           // {
             //   Pos = In.ReadLocation();
            //    In.ReadString();
            //}

            //Ter = o[Pos.x, Pos.y];
            //TerIfHidden = TerrainRecord.List[o[Pos.x, Pos.y]].flag1;
        }
    }

    //public class Sign
    //{
    //    public Location Pos;
    //    public string Text;

    //    public Sign(BinaryReader In) 
    //    {
    //        Pos = Location.Read(In);
    //        Text = In.ReadString();
    //    }
    //}

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

            triggeredBy = In.ReadByte(); //else triggeredBy = 1;
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

            //switch (what)
            //{
            //case eTriggerSpot.SANCTIFY:
            //    if ((triggeredBy & 128) != 0) return true; else return false;
            //case eTriggerSpot.STEP_ON:
            //    if ((triggeredBy & 1) != 0) return true; else return false;
            //case eTriggerSpot.SEARCH:
            //    if ((triggeredBy & 2) != 0) return true; else return false;
            //case eTriggerSpot.USE:
            //    if ((triggeredBy & 4) != 0) return true; else return false;
            //default:
            //    return false;
            //}
        }

    }

    public class PresetItem
    {
        public Location Pos;
        public Item Record; //References the item type in the Scenario list.
        public Item Instance; //References the actual item in the game created from this preset
        //public ItemRecord Instance; //Reference the item instance once it has been put in the town.
        //public int Ability;
        public int Charges;
        public bool AlwaysThere, Property, Contained;
        //public bool HasBeenTaken; //Whether the party has picked up the item in the scenario.

        public PresetItem(BinaryReader In) {
            Item.List.TryGetValue(In.ReadString(), out Record);///*Int16()*/];
            Pos = In.ReadLocation();
            //Ability = In.ReadInt16();
            Charges = In.ReadInt16();
            AlwaysThere = In.ReadBoolean();
            Property = In.ReadBoolean();
            Contained = In.ReadBoolean();
            //HasBeenTaken = false;
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
