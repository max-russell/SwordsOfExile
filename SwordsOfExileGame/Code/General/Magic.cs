using System.Collections.Generic;
using System.IO;

namespace SwordsOfExileGame
{
    public class MagicSpell : IListEntity
    {
        PartyType Party { get { return Game.CurrentParty; } }

        public static ExileList<MagicSpell> List = new ExileList<MagicSpell>();

        public MagicSpell() { }
        public void Load(BinaryReader In)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            Name = In.ReadString();
            Description = In.ReadString();
            Mage = In.ReadBoolean();
            Level = In.ReadInt32();
            Cost = In.ReadInt32();
            Price = In.ReadInt32();
            Where = (eSpellWhere)In.ReadInt32();
            Range = In.ReadInt32();
            Target = (eSpellTarget)In.ReadByte();
            TargetPattern = Pattern.FromIndex(In.ReadByte());
            MultiTarget = In.ReadBoolean();
            Missile = In.ReadInt32();
            FuncCast = In.ReadString();
            FuncTargetCount = In.ReadString();
            List.Add(this);
        }
        public string GetWhereString()
        {
            switch (Where)
            {
                case eSpellWhere.COMBAT: return "In combat only"; 
                case eSpellWhere.TOWN: return "Town only"; 
                case eSpellWhere.TOWN_AND_OUTDOOR: return "Town & Outdoors"; 
                case eSpellWhere.TOWN_AND_COMBAT: return "Town & Combat"; 
                case eSpellWhere.OUTDOOR: return "Outdoors only"; 
            }
            return "Everywhere";
        }

        public string ID { get { return id; } set { id = value; } }
        string id = "";

        public string Name = "Spell", Description = "";
        public bool Mage = true;
        public int Level = 1;
        public int Cost = 1;
        public int Price = 0;
        public eSpellWhere Where = 0;
        public int Range = 0;
        public eSpellTarget Target = eSpellTarget.CASTER;
        public Pattern TargetPattern = Pattern.Single;
        public bool MultiTarget = false;
        public int Missile = -1;
        string FuncCast, FuncTargetCount;

        /// <summary>
        /// Returns how many targets on the map you select for this spell. In most cases it's just one.
        /// </summary>
        /// <param name="caster"></param>
        /// <returns></returns>
        public int GetTargetCount(PCType caster, Item item)
        {
            if (!MultiTarget || FuncTargetCount == null) return 1;

            return Script.RunTargetCount(FuncTargetCount, caster, this, item);
        }

        public void MakeNewsLine(int targets)
        {
            NewsLine.Clear();

            if (MultiTarget)
            {
                if (targets == 1)
                    if (Target == eSpellTarget.CHARACTER)
                        new NewsLine("Select 1 more enemy to target", true);
                    else
                        new NewsLine("Select 1 more location to target", true);
                else
                    if (Target == eSpellTarget.CHARACTER)
                        new NewsLine("Select " + targets + " more enemies to target", true);
                    else
                        new NewsLine("Select " + targets + " more locations to target", true);
                new NewsLine("('m' to Cancel, space to finish)", false);
            }
            else
            {
                if (Target == eSpellTarget.CHARACTER)
                    new NewsLine("Select an enemy to target", true);
                if (Target == eSpellTarget.LOCATION)
                    new NewsLine("Select a location to target", true);

                if (TargetPattern == Pattern.Field[0])
                {
                    new NewsLine("('m' to Cancel, space to rotate wall)", false);
                }
                else
                    new NewsLine("('m' to Cancel", false);
            }

        }

        public void Cast(PCType caster, object targ, Item item_used)
        {

            TownMap town = Game.CurrentTown;

            if (item_used == null && town != null && town.FieldThere(caster.Pos, Field.ANTIMAGIC))
            {
                Game.AddMessage("Can't cast spells in an antimagic field.");
                return;
            }

            bool castbyitemuse = item_used != null;


            List<NPC> npctargetlist = null;
            List<Location> targetlist = null;
            NPC npctarget = null;
            PCType pctarget = null;
            Location target = Location.Zero;
            Pattern targetpattern = Action.TargetPattern; //Don't use the current spell's TargetPattern property - Wall of Force etc lets the player change the pattern when targeting!
            if (targetpattern == null) targetpattern = Pattern.Single;

            //Get the right target(s) from the object passed in targ
            if (targ is List<Location>)
            {
                targetlist = (List<Location>)targ;
                target = targetlist[0];
            }
            else if (targ is Location)
                target = (Location)targ;

            if (Target == eSpellTarget.CHARACTER && targ is List<Location>)
            {
                npctargetlist = new List<NPC>();
                foreach (Location loc in targetlist)
                    npctargetlist.Add((NPC)Game.CurrentTown.CharacterThere(loc, false, true));
                npctarget = npctargetlist[0];
            }
            else if (Target == eSpellTarget.CHARACTER)
            {
                npctarget = (NPC)Game.CurrentTown.CharacterThere(target, false, true);
                target = npctarget.Pos;
            }
            else if (targ is PCType)
            {
                pctarget = (PCType)targ;
                target = pctarget.Pos;
            }

            //Queue the script!
            Script.New_CastSpell(FuncCast, caster, target, targetlist, npctarget, npctargetlist, pctarget, targetpattern, this, item_used);

            //Check map triggers
            if (targ is Location || targ is List<Location>)
            {
                List<Location> locs;
                if (targ is Location)
                {
                    locs = new List<Location>();
                    locs.Add((Location)targ);
                }
                else
                    locs = (List<Location>)targ;

                foreach (Location l in locs)
                {
                    TriggerSpot foundtrig = null;
                    //Look for special encounter triggers here
                    foreach (TriggerSpot se in Game.CurrentTown.TriggerSpotList)
                    {
                        if (se.Pos == l && se.TriggeredBy(eTriggerSpot.CAST_SPELL) && se.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                        {
                            foundtrig = se;
                            break;
                        }
                    }

                    if (foundtrig == null) //Terrain triggers ignored if map trigger is on the same space.
                    {
                        TerrainRecord ter = Game.CurrentTown.TerrainAt(l);
                        if (ter.Trigger != null && ter.Trigger.TriggeredBy(eTriggerSpot.CAST_SPELL) && ter.Trigger.TriggeredBy(eTriggerSpot.PCS_TRIGGER))
                        {
                            foundtrig = ter.Trigger;
                        }
                    }

                    if (foundtrig != null)
                    {
                        Script.New_MapSpellTrigger(caster, foundtrig, l, this, item_used);
                    }
                }
            }

            if (!castbyitemuse)
            {
                Game.AddMessage(caster.Name + " casts '" + Name + "'.");
            }
            else
            {
                Game.AddMessage(caster.Name + " uses " + item_used.KnownName + ".");
            }

            new Animation_Attack(caster, Missile == -1 ? (Mage ? "025_magespell" : "024_priestspell") : null);
            if (Missile != -1)
            {
                if (targetlist != null)
                    foreach (Location l in targetlist)
                    {
                        new Animation_Missile(caster.Pos, l, Missile, true, "011_3booms");
                        new Animation_Pause();
                    }
                else if (npctargetlist != null)
                    foreach (NPC npc in npctargetlist)
                    {
                        new Animation_Missile(caster.Pos, npc.Pos, Missile, true, "011_3booms");
                        new Animation_Pause();
                    }
                else
                    new Animation_Missile(caster.Pos, target, Missile, true, "011_3booms");
                
            }
            new Animation_Hold();
        }
    }
}
