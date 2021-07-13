//#define USE_MAGIC_SCRIPTS //Set this to have all the spells implemented in Python scripts rather than hardcoded

using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;
using System.Text;
using System.IO;
using Microsoft.Xna.Framework.Input;

//#if USE_MAGIC_SCRIPTS
//using IronPython.Hosting;
//using Microsoft.Scripting;
//using Microsoft.Scripting.Hosting;
//using System.Reflection;
//#endif

namespace SwordsOfExileGame
{
    public class MagicSpell : IListEntity
    {
        PartyType Party { get { return Game.CurrentParty; } }

        public static ExileList<MagicSpell> List = new ExileList<MagicSpell>();
        //public static Dictionary<string, MagicSpell> List = new Dictionary<string, MagicSpell>();

//#if USE_MAGIC_SCRIPTS
//        static ScriptEngine m_engine;
//        static ScriptScope m_scope;       
//#endif

        //public static void LoadSpellData(BinaryReader In)
        //{
        //    List.Clear();
        //    int num1 = In.ReadInt16();
        //    for (int x = 0; x < num1; x++) new MagicSpell(In);
        //}

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

            //XElement xml=null;

            //if (File.Exists(Path.Combine(Game.ScenarioDirectory, "Data", "SpellData.xml")))
            //    xml = XElement.Load(Path.Combine(Game.ScenarioDirectory, "Data", "SpellData.xml"));
            //else if (File.Exists(Path.Combine(Game.BaseDirectory, "Data", "SpellData.xml")))
            //    xml = XElement.Load(Path.Combine(Game.BaseDirectory, "Data", "SpellData.xml"));
            //else
            //{
            //    Game.FlagError("Loading Error",  "SpellData.xml not found");
            //    return false;
            //}

            //foreach (XElement spell in xml.Elements())
            //{
            //    if (spell.Name.LocalName != "Spell") continue;

            //    MagicSpell s = new MagicSpell();
                
            //    foreach (XAttribute attr in spell.Attributes())
            //    {
            //        switch (attr.Name.LocalName)
            //        {
            //            case "ID": s.id =/*s.ID =*/ attr.Value; break;
            //            case "Name": s.Name = attr.Value; break;
            //            case "Description": s.Description = attr.Value; break;
            //            case "Mage": s.Mage = Convert.ToBoolean(attr.Value); break;
            //            case "Level": s.Level = Convert.ToInt32(attr.Value); break;
            //            case "Cost": s.Cost = Convert.ToInt32(attr.Value); break;
            //            case "Price": s.Price = Convert.ToInt32(attr.Value); break;
            //            case "Where": s.Where = Convert.ToInt32(attr.Value); break;
            //            case "Target": s.Target = (eSpellTarget)Convert.ToInt32(attr.Value); break;
            //            case "TargetPattern": s.TargetPattern = Pattern.FromIndex(Convert.ToInt32(attr.Value)); break;
            //            case "Missile": s.Missile = Convert.ToInt32(attr.Value); break;
            //            case "Range": s.Range = Convert.ToInt32(attr.Value); break;
            //            case "CastScript": 
            //                s.FuncCast = attr.Value;
            //                break;
            //            case "TargetCountScript": 
            //                s.FuncTargetCount = attr.Value; 
            //                s.MultiTarget = true;
            //                break;
            //        }
            //    }
            //    List.Add(s);
            //}
            //return true;
        //}

        //public eSpell No;
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
        //public Keys KeyShortcut = Keys.None;
        //public Func<IEnumerable<object>> CastScript = null;
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

            //switch (No)
            //{
            ////case eSpell.SPARK: //TEMPORARY FOR TESTING
            ////    return 5;

            //case eSpell.WEAK_SUMMONING:
            //    return Maths.MinMax(1,7, caster.Level / 4 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2);// + Maths.get_ran(1,0,2));
            //case eSpell.FLAME_ARROWS:
            //    return caster.Level / 4 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2;
            //case eSpell.VENOM_ARROWS:
            //    return caster.Level / 5 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2;
            //case eSpell.SUMMONING:
            //    return Maths.MinMax(1, 6, caster.Level / 6 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2);// + Maths.get_ran(1, 0, 1));
            //case eSpell.SPRAY_FIELDS:
            //    return caster.Level / 5 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2;
            //case eSpell.MAJOR_SUMMON:
            //    return Maths.MinMax(1, 5, caster.Level / 8 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2);// + Maths.get_ran(1, 0, 1));
            //case eSpell.DEATH_ARROWS:
            //    return caster.Level / 8 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 3;
            //case eSpell.PARALYSIS:
            //    return caster.Level / 8 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 3;
            //case eSpell.SMITE:
            //    return Maths.MinMax(1, 8, caster.Level / 4 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2);
            //case eSpell.STICKS_TO_SNAKES:
            //    return caster.Level / 5 + caster.GetSkillBonus(eSkill.INTELLIGENCE) / 2;
            //case eSpell.SUMMON_HOST:
            //    return 5;
            //default:
            //    return 1;
            //}
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
                            foundtrig = se;//foundnode = se.NodeToRun;
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
                //Script.New_CastSpell(FuncCast, caster, target, targetlist, npctarget, npctargetlist, pctarget, targetpattern, this);
                //new Script(FuncCast, eCallOrigin.CAST_SPELL, caster, target, targetlist, npctarget, npctargetlist, pctarget, targetpattern, this);
                Game.AddMessage(caster.Name + " casts '" + Name + "'.");
            }
            else
            {
                //Script.New_CastItemSpell(FuncCast, caster, target, targetlist, npctarget, npctargetlist, pctarget, targetpattern, this, item_used);
                //new Script(FuncCast, eCallOrigin.CAST_ITEM_SPELL, caster, target, targetlist, npctarget, npctargetlist, targetpattern, this, item_used);
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
            

//#else
//            ////NOW do each spell.

            //switch (ID)
            //{
//            case eSpell.LIGHT_M:
//                break;//0
//            case eSpell.SPARK:
//                new Animation_Missile(caster.Pos, target, 6, true, 11);
//                new Animation_Hold();
//                town.HitArea(target, Maths.Rand(2, 1, 4), eDamageType.MAGIC, targetpattern, false, caster);
//                break;
//            case eSpell.MINOR_HASTE:
//                break;
//            case eSpell.STRENGTH:
//                break;
//            case eSpell.SCARE:

//                break;
//            case eSpell.FLAME_CLOUD:
//                town.place_spell_pattern(targetpattern, target, eField.FIRE_WALL, caster);
//                break;

//            case eSpell.IDENTIFY:
//                Game.AddMessage("All of your items are identified");
//                foreach (PCType pc in Party.EachAlivePC())
//                {
//                    foreach (Item item in pc.EquippedItems)
//                        if (item != null) item.Identified = true;
//                    foreach (Item item in pc.items)
//                        item.Identified = true;
//                }
//                break;

//            case eSpell.SCRY_MONSTER:
//                Snd.play_sound(52);
//                Party.AddToLibrary(npctarget);
//                break;
//            case eSpell.GOO:
//                town.place_spell_pattern(targetpattern, target, eField.WEB, caster);
//                break;

//            case eSpell.TRUE_SIGHT:
//                for (int x = 0; x < town.Width; x++)
//                    for (int y = 0; y < town.Height; y++)
//                        if ((new Location(x, y)).DistanceTo(caster.Pos) <= 2)
//                            town.MakeExplored(new Location(x, y));
//                break;

//            case eSpell.MINOR_POISON:
//                new Animation_Missile(caster.Pos, target, 4, true, 55);
//                new Animation_Hold();
//                npctarget.Poison(2 + bonus / 2);
//                break;
//            case eSpell.FLAME:
//                new Animation_Missile(caster.Pos, target, 2, true, 11);
//                new Animation_Hold();
//                int damage = Maths.Rand(Maths.Min(10, 1 + level / 3 + bonus), 1, 6);
//                town.HitArea(target, damage, eDamageType.FIRE, targetpattern, false, caster);
//                break;
//            case eSpell.SLOW:
//                break;
//            case eSpell.DUMBFOUND:
//                break;
//            case eSpell.ENVENOM:
//                break;
//            case eSpell.STINKING_CLOUD:
//                town.place_spell_pattern(targetpattern, target, eField.STINK_CLOUD, caster);
//                break;
//            case eSpell.SUMMON_BEAST:
//                new Animation_Missile(caster.Pos, target, 8, true, 61);
//                new Animation_Hold();
//                int duration = Maths.Rand(3, 1, 4) + bonus;
//                if (!town.SummonMonster(caster, NPCRecord.GetSummonMonster(1), target, duration))
//                    Game.AddMessage("  Summon failed.");
//                break;
//            case eSpell.CONFLAGRATION:
//                town.place_spell_pattern(targetpattern, target, eField.FIRE_WALL, caster);
//                break;
//            case eSpell.DISPEL_FIELDS_M:
//                town.place_spell_pattern(targetpattern, target, eField.DISPEL, caster);
//                break;
//            case eSpell.SLEEP_CLOUD:
//                town.place_spell_pattern(targetpattern, target, eField.SLEEP_CLOUD, caster);
//                break;
//            case eSpell.UNLOCK:
//                break;
//            case eSpell.HASTE:
//                break;
//            case eSpell.FIREBALL:
//                new Animation_Missile(caster.Pos, target, 2, true, 11);
//                new Animation_Hold();
//                damage = Math.Min(9, 1 + (level * 2) / 3 + bonus) + 1;
//                if (damage > 10) damage = (damage * 8) / 10;
//                if (damage <= 0) damage = 1;
//                town.HitArea(target, damage, eDamageType.FIRE, targetpattern, true, caster);
//                break;
//            case eSpell.LONG_LIGHT:
//                break;
//            case eSpell.FEAR:
//                break;
//            case eSpell.WALL_OF_FORCE:
//                town.place_spell_pattern(targetpattern, target, eField.FORCE_WALL, caster);
//                break;
//            case eSpell.WEAK_SUMMONING:
//                foreach (Location loc in targetlist)
//                {
//                    new Animation_Missile(caster.Pos, loc, 8, true, 61);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (Location loc in targetlist)
//                {
//                    duration = Maths.Rand(4, 1, 4) + bonus;
//                    if (!town.SummonMonster(caster, NPCRecord.GetSummonMonster(1), loc, duration))
//                        Game.AddMessage("  Summon failed.");
//                }
//                break;
//            case eSpell.FLAME_ARROWS:
//                foreach (NPCType npc in npctargetlist)
//                {
//                    new Animation_Missile(caster.Pos, npc.Pos, 4, true, 0);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (NPCType npc in npctargetlist)
//                    npc.Damage(caster, Maths.Rand(2, 1, 4), 0, eDamageType.FIRE, false);
//                break;
//            case eSpell.WEB:
//                town.place_spell_pattern(targetpattern, target, eField.WEB, caster);
//                break;
//            case eSpell.RESIST_MAGIC:
//                break;
//            case eSpell.POISON:
//                break;
//            case eSpell.ICE_BOLT:
//                new Animation_Missile(caster.Pos, target, 6, true, 11);
//                new Animation_Hold();
//                town.HitArea(target, Maths.Rand(Math.Min(20, level + bonus), 1, 4), eDamageType.COLD, targetpattern, false, caster);
//                break;
            //case eSpell.SLOW_GROUP:
            //    foreach (NPCType npc in town.EachCharacterInRange(caster.Pos, 5, false, true))
            //        if (npc.IsABaddie && town.CanSee(caster.Pos, npc.Pos) < 5)
            //        {
            //            new Animation_Missile(caster.Pos, npc.Pos, 8, true, 0);
            //            npc.Slow(5 + Bonus());
            //        }
            //    break;
            //case eSpell.MAGIC_MAP:
            //    Item item = caster.HasItemWithAbility(eItemAbil.SAPPHIRE);
            //    if (item == null)
            //    {
            //        Game.AddMessage("  You need a sapphire.");
            //        //cancel action
            //    }
            //    else if (town.PreventMapping || town.PreventScrying)
            //    {
            //        Game.AddMessage("  The spell fails.");
            //        //cancel action
            //    }
            //    else
            //    {
            //        caster.UseItemCharge(item);
            //        Game.AddMessage("  As the sapphire dissolves,       ");
            //        Game.AddMessage("  you have a vision.               ");
            //        for (int y = 0; y < town.Height; y++)
            //            for (int x = 0; x < town.Width; x++)
            //                town.MakeExplored(new Location(x, y));
            //    }
            //    break;
//            case eSpell.CAPTURE_SOUL:
//                break;
//            case eSpell.SIMULACRUM:
//                //TODO: Has to display a window letting the player pick a trapped monster. Somewhat tricky. Need 'yield' support.
//                break;
//            case eSpell.VENOM_ARROWS:
//                foreach (NPCType npc in npctargetlist)
//                {
//                    new Animation_Missile(caster.Pos, npc.Pos, 11, true, 55);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (NPCType npc in npctargetlist)
//                    npc.Poison(4 + bonus / 2);
//                break;
//            case eSpell.WALL_OF_ICE:
//                town.place_spell_pattern(targetpattern, target, eField.ICE_WALL, caster);
//                break;
//            case eSpell.STEALTH:
//                break;
            //case eSpell.MAJOR_HASTE:
            //    foreach (PCType pc in Party.EachAlivePC())
            //        pc.Haste(Maths.Min(8, 1 + caster.Level / 8 + Bonus());
            //    Game.AddMessage("  Party hasted.");
            //    break;
//            case eSpell.FIRE_STORM:
//                new Animation_Missile(caster.Pos, target, 2, true, 11);
//                new Animation_Hold();
//                damage = Math.Min(12, 1 + (level * 2) / 3 + bonus) + 2;
//                if (damage > 20) damage = (damage * 8) / 10;
//                town.HitArea(target, damage, eDamageType.FIRE, targetpattern, true, caster);
//                break;
            //case eSpell.DISPEL_BARRIER:
            //    int[] combat_percent = {150,120,100,90,80,80,80,70,70,70, 70,70,67,62,57,52,47,42,40,40};
            //    if (town.FieldThere(target, eField.FIRE_BARRIER) || town.FieldThere(target, eField.FORCE_BARRIER))
            //    {
            //        int r1 = Maths.Rand(1, 0, 100) - 5 * caster.GetSkillBonus(eSkill.INTELLIGENCE) + 5 * (town.Difficulty / 10);
            //        if (town.FieldThere(target, eField.FIRE_BARRIER)) r1 -= 8;
            //        if (r1 < 120 - combat_percent[Maths.Min(19, caster.Level)])
            //        {
            //            Game.AddMessage("  Barrier broken.");
            //            town.RemoveField(target, eField.FIRE_BARRIER);
            //            town.RemoveField(target, eField.FORCE_BARRIER);
            //            town.UpdateVisible();
            //        }
            //        else
            //        {
            //            Sound.Play(41);
            //            Game.AddMessage("  Didn't work.");
            //        }
            //    }
            //    else
            //        Game.AddMessage("  No barrier there.");
            //    break;
//            case eSpell.FIRE_BARRIER:
//                Snd.play_sound(68);
//                town.HitArea(target, Maths.Rand(3, 2, 7), eDamageType.FIRE, Pattern.Single, false, caster);
//                town.MakeFireBarrier(target);
//                if (town.FieldThere(target, eField.FIRE_BARRIER))
//                    Game.AddMessage("  You create the barrier.");
//                else
//                    Game.AddMessage("  Failed.");
//                break;
//            case eSpell.SUMMONING:
//                foreach (Location loc in targetlist)
//                {
//                    new Animation_Missile(caster.Pos, loc, 8, true, 61);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                duration = Maths.Rand(5, 1, 4) + bonus;
//                foreach (Location loc in targetlist)
//                {
//                    duration = Maths.Rand(7, 1, 4) + bonus;
//                    if (!town.SummonMonster(caster, NPCRecord.GetSummonMonster(2), loc, duration))
//                        Game.AddMessage("  Summon failed.");
//                }
//                break;
//            case eSpell.SHOCKSTORM:
//                town.place_spell_pattern(targetpattern, target, eField.FORCE_WALL, caster);
//                break;
//            case eSpell.SPRAY_FIELDS:
//                foreach (Location loc in targetlist)
//                    town.place_spell_pattern(targetpattern, loc, (eField)Maths.Rand(1, 0, 14), caster);
//                break;
//            case eSpell.MAJOR_POISON:
//                break;
//            case eSpell.GROUP_FEAR:
//                break;
//            case eSpell.KILL:
//                new Animation_Missile(caster.Pos, target, 9, true, 11);
//                new Animation_Hold();
//                damage = 40 + Maths.Rand(3, 0, 10) + caster.level * 2;
//                town.HitArea(target, damage, eDamageType.MAGIC, targetpattern, false, caster);
//                break;
//            case eSpell.PARALYSIS:
//                break;
//            case eSpell.DAEMON:
//                new Animation_Missile(caster.Pos, target, 8, true, 61);
//                new Animation_Hold();
//                duration = Maths.Rand(5, 1, 4) + bonus;
//                if (!town.SummonMonster(caster, NPCRecord.List[85], target, duration))
//                    Game.AddMessage("  Summon failed.");
//                break;
//            case eSpell.ANTIMAGIC_CLOUD:
//                town.place_spell_pattern(targetpattern, target, eField.ANTIMAGIC, caster);
//                break;
//            case eSpell.MINDDUEL:
//                if (npctarget.Record.MageLevel == 0 && npctarget.Record.PriestLevel == 0)
//                    Game.AddMessage("  Can't duel: no magic.");
//                else
//                {
//                    Item item = caster.pc_has_abil(eItemAbil.SMOKY_CRYSTAL);
//                    if (item == null)
//                        Game.AddMessage("  You need a smoky crystal.");
//                    else
//                    {
//                        caster.UseItemCharge(item);
//                        //TODO: The actual mind duel - pauses and animations to make it more fancy (use yield)
//                    }
//                }
//                break;
//            case eSpell.FLIGHT:
//                break;
//            case eSpell.SHOCKWAVE:
//                Game.AddMessage("  The ground shakes.");
//                foreach (ICharacter ch in town.EachCharacterInRange(caster.Pos, 10))
//                    if (ch != caster && town.Visible(ch.Pos))
//                        ch.Damage(caster, Maths.Rand(2 + caster.Pos.DistanceTo(ch.Pos) / 2, 1, 6), 0, eDamageType.MAGIC, false);
//                break;
//            case eSpell.MAJOR_BLESSING:
//                break;
//            case eSpell.MASS_PARALYSIS:
//                break;
//            case eSpell.PROTECTION:
//                break;
//            case eSpell.MAJOR_SUMMON:
//                foreach (Location loc in targetlist)
//                {
//                    new Animation_Missile(caster.Pos, loc, 8, true, 61);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (Location loc in targetlist)
//                {
//                    duration = Maths.Rand(7, 1, 4) + bonus;
//                    if (!town.SummonMonster(caster, NPCRecord.GetSummonMonster(3), loc, duration))
//                        Game.AddMessage("  Summon failed.");
//                }
//                break;
//            case eSpell.FORCE_BARRIER:
//                Snd.play_sound(68);
//                town.HitArea(target, Maths.Rand(7, 2, 7), eDamageType.FIRE, Pattern.Single, false, caster);
//                town.MakeForceBarrier(target);
//                if (town.FieldThere(target, eField.FORCE_BARRIER))
//                    Game.AddMessage("  You create the barrier.");
//                else
//                    Game.AddMessage("  Failed.");
//                break;
//            case eSpell.QUICKFIRE:
//                town.make_quickfire(target);
//                break;
//            case eSpell.DEATH_ARROWS:
//                foreach (NPCType npc in npctargetlist)
//                {
//                    new Animation_Missile(caster.Pos, npc.Pos, 9, true, 11);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (NPCType npc in npctargetlist)
//                {
//                    damage = Maths.Rand(3, 0, 10) + caster.level + 3 * bonus;
//                    npc.Damage(caster, damage, 0, eDamageType.MAGIC, false);
//                }
//                break;
//            case eSpell.MINOR_BLESS:
//                break; //62
//            case eSpell.MINOR_HEAL:
//                break;
//            case eSpell.WEAKEN_POISON:
//                break;
//            case eSpell.TURN_UNDEAD:
//                break;
//            case eSpell.LOCATION:
//                break;
//            case eSpell.SANCTUARY:
//                break;
//            case eSpell.SYMBIOSIS:
//                break;
//            case eSpell.MINOR_MANNA:
//                break;
//            case eSpell.RITUAL_SANCTIFY:
//                break;
//            case eSpell.STUMBLE:
//                break;
//            case eSpell.BLESS:
//                break;
//            case eSpell.CURE_POISON:
//                break;
//            case eSpell.CURSE:
//                break;
//            case eSpell.LIGHT_P:
//                break;
//            case eSpell.WOUND:
//                new Animation_Missile(caster.Pos, target, 14, true, 24);
//                new Animation_Hold();
//                town.HitArea(target, Maths.Rand(Maths.Min(7,2 + bonus + level / 2),1,4), eDamageType.MAGIC, targetpattern, false, caster);
//                break;
//            case eSpell.SUMMON_SPIRIT:
//                new Animation_Missile(caster.Pos, target, 8, true, 61);
//                new Animation_Hold();
//                duration = Maths.Rand(2, 1, 5) + bonus;
//                if (!town.SummonMonster(caster, NPCRecord.List[125], target, duration))
//                    Game.AddMessage("  Summon failed.");
//                break;
//            case eSpell.MOVE_MOUNTAINS:
//                break;
//            case eSpell.CHARM_FOE:
//                break;
//            case eSpell.DISEASE:
//                break;
//            case eSpell.AWAKEN:
//                break;
//            case eSpell.HEAL:
//                break;
//            case eSpell.LIGHT_HEAL_ALL:
//                break;
//            case eSpell.HOLY_SCOURGE:
//                break;
//            case eSpell.DETECT_LIFE:
//                break;
//            case eSpell.CURE_PARALYSIS:
//                break;
//            case eSpell.MANNA:
//                break;
//            case eSpell.FORCEFIELD:
//                town.place_spell_pattern(targetpattern, target, eField.FORCE_WALL, caster);
//                break;
//            case eSpell.CURE_DISEASE:
//                break;
//            case eSpell.RESTORE_MIND:
//                break;
//            case eSpell.SMITE:
//                foreach (NPCType npc in npctargetlist)
//                {
//                    new Animation_Missile(caster.Pos, npc.Pos, 6, true, 0);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (Location loc in targetlist)
//                    town.HitArea(loc, Maths.Rand(2, 1, 5), eDamageType.COLD, targetpattern, false, caster); 
//                break;
//            case eSpell.CURE_PARTY:
//                break;
//            case eSpell.CURSE_ALL:
//                break;
//            case eSpell.DISPEL_UNDEAD:
//                break;
//            case eSpell.REMOVE_CURSE:
//                break;
//            case eSpell.STICKS_TO_SNAKES:
//                foreach (Location loc in targetlist)
//                {
//                    new Animation_Missile(caster.Pos, loc, 8, true, 61);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (Location loc in targetlist)
//                {
//                    duration = Maths.Rand(2, 1, 5) + bonus;
//                    NPCRecord npcr = Maths.Rand(1, 0, 7) == 1 ? NPCRecord.List[100] : NPCRecord.List[99];
//                    if (!town.SummonMonster(caster, npcr, loc, duration))
//                        Game.AddMessage("  Summon failed.");
//                }
//                break;
//            case eSpell.MARTYRS_SHIELD:
//                break;
//            case eSpell.CLEANSE:
//                break;
//            case eSpell.FIREWALK:
//                break;
//            case eSpell.BLESS_PARTY:
//                break;
//            case eSpell.MAJOR_HEAL:
//                break;
//            case eSpell.RAISE_DEAD:
//                break;
//            case eSpell.FLAMESTRIKE:
//                new Animation_Missile(caster.Pos, target, 2, true, 11);
//                new Animation_Hold();
//                damage = Math.Min(9, 1 + (level * 2) / 3 + bonus) + 1;
//                damage = damage * 14 / 10;
//                if (damage <= 0) damage = 1;
//                town.HitArea(target, damage, eDamageType.FIRE, targetpattern, true, caster);
//                break;
//            case eSpell.MASS_SANCTUARY:
//                break;
//            case eSpell.SUMMON_HOST:
//                foreach (Location loc in targetlist)
//                {
//                    new Animation_Missile(caster.Pos, loc, 8, true, 61);
//                    new Animation_Pause();
//                }
//                new Animation_Hold();
//                foreach (Location loc in targetlist)
//                {
//                    duration = Maths.Rand(2, 1, 4) + bonus;
//                    NPCRecord npcr = loc == targetlist[0] ? NPCRecord.List[126] : NPCRecord.List[125];
//                    if (!town.SummonMonster(caster, npcr, loc, duration))
//                        Game.AddMessage("  Summon failed.");
//                }
//                break;
//            case eSpell.SHATTER:
//                break;
//            case eSpell.DISPEL_FIELDS_P:
//                town.place_spell_pattern(targetpattern, target, eField.DISPEL, caster);
//                break;
//            case eSpell.HEAL_ALL:
//                break;
//            case eSpell.REVIVE:
//                break;
//            case eSpell.HYPERACTIVITY:
//                break;
//            case eSpell.DESTONE:
//                break;
//            case eSpell.GUARDIAN:
//                new Animation_Missile(caster.Pos, target, 8, true, 61);
//                new Animation_Hold();
//                duration = Maths.Rand(6, 1, 4) + bonus;
//                if (!town.SummonMonster(caster, NPCRecord.List[122], target, duration))
//                    Game.AddMessage("  Summon failed.");
//                break;
//            case eSpell.MASS_CHARM:
//                break;
//            case eSpell.PROTECTIVE_CIRCLE:
//                break;
//            case eSpell.PESTILENCE:
//                break;
//            case eSpell.REVIVE_ALL:
//                break;
//            case eSpell.RAVAGE_SPIRIT:
//                break;
//            case eSpell.RESURRECT:
//                break;
//            case eSpell.DIVINE_THUD:
//                new Animation_Missile(caster.Pos, target, 9, true, 11);
//                new Animation_Hold();
//                damage = Maths.Min(18, (level * 7) / 10 + 2 * bonus);
//                town.HitArea(target, damage, eDamageType.MAGIC, targetpattern, true, caster);
//                break;
//            case eSpell.AVATAR:
//                break;
//            case eSpell.WALL_OF_BLADES:
//                town.place_spell_pattern(targetpattern, target, eField.BLADE_WALL, caster);
//                break;
//            case eSpell.WORD_OF_RECALL:
//                break;
//            case eSpell.MAJOR_CLEANSING:
//                break;
            //}
//#endif
            //Take away the spell points for the spell.
            //caster.take_sp(Cost);
        }

    }
}
