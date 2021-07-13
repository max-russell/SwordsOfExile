//#define USE_MOVE_SCRIPTS   //Whether NPCs movement is hard-coded, or calls scripts

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
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    //Stores information for an instance of a creature
    public partial class NPC : ICharacter, IExpRecipient, IAnimatable
    {
        //Shortcuts
        TownMap curTown { get { return (TownMap)Game.CurrentMap; } }
        PartyType Party { get { return Game.CurrentParty; } }
        public string TooltipInfo(bool brief) 
        {
            StringBuilder sb = new StringBuilder();
            sb.Append(Record.Name);
            sb.Append(AlliedWith(Party.LeaderPC) ? " (Friendly)" : " (Hostile)");
            sb.Append("\n  Health: ");
            sb.Append(Maths.Max(0,Health));
            sb.Append(" \\ ");
            sb.Append(MaxHealth);

            for (int a = 0; a < 14; a++)
            {
                int s = Status((eAffliction)a);

                if (s != 0)
                    sb.Append("@n@i" + PCType.StatusMsg(this, (eAffliction)a) + "@e");
            }

            return sb.ToString();
        }
        public int Width { get { return Record.Width; } }
        public int Height { get { return Record.Height; } }
        public string Name { get { return Record.Name; } }
        public int Level { get { return Record.Level; } set { } }
        public bool IsAlive() { return !Dying && curTown.NPCList.Contains(this); }
        public Personality Personality { get { if (Start != null) return Start.personality; return null; } }
        //string funcNonCombatMove { get { if (Start.FuncNonCombatMove != null) return Start.FuncNonCombatMove; else return Record.FuncNonCombatMove; } }
       // string funcCombatMove { get { if (Start.FuncCombatMove != null) return Start.FuncCombatMove; else return Record.FuncCombatMove; } }
        public int MaxHealth { get { return Record.Health; } }

        //Temporary properties - no need to save in savefile
        public bool Dying = false;

        IAnimCharacter animAction;
          public IAnimCharacter AnimAction { get { return animAction; } set { animAction = value; } }
        IAnimCharacter animFlash;
          public IAnimCharacter AnimFlash { get { return animFlash; } set { animFlash = value; } }

          public bool NotDrawn { get { return notDrawn; } set { notDrawn = value; } } //Temporarily don't draw (used in teleporting animations)
        bool notDrawn = false;

        public bool IsVisible()
        {
            return Game.CurrentMap.Visible(pos);
        }

        bool hasJustAttacked; //Tracks if the monster attacked this turn
        public int MessingAround; //Stupid thing
        int targetingNum;
          public int TargetingNum { get { return targetingNum; } set { targetingNum = value; } } //Used when the player is targeting for firing an arrow / spell etc, so that the player can press a key to select this NPC

        //Semi-temporary (errr....) Should be saved in save file
        public ICharacter Target; //Who it's currently trying to fight.
        Location WanderTarget; //Was monster_targs - this stores the square a creature wanders to when it is not hostile (used in rand_move)
        int Provocation; //This is calculated at the end of every npcs turn based on what it did that turn. Attacking or casting a spell is a big provocation.
        //But if the npc does nothing attention grabbing it decays back to 0 slowly.
        ICharacter LastAttacked; //Did the npc attack another character last turn? Used when an enemy npc is deciding who to target.

        //Stack<eDir> PathToTarget;// = new Stack<eDir>();
        //Location PathPosition, PathDestination;
        MapPath PathToTarget;
        
        //Intrinsic properties    Should be saved in save file
        public eAttitude Attitude; //Whether the NPC is an ally or enemy of the PCs
          public eAttitude MyAttitude() { return Attitude; } //ICharacter method
          public bool IsABaddie { get { return Attitude == eAttitude.HOSTILE_A || Attitude == eAttitude.HOSTILE_B; } }
        public eActive Active; //Whether the NPC will attempt to attack its enemy
        Location pos;
          public Location Pos { get { return pos; } set { pos = value; }}
        public NPCRecord Record;
        public Boolean Mobile;
        public int Summoned;
        public NPCPreset Start;
        public Direction direction;
          public Direction Dir { get { return direction; } set { direction = value; } }
        public int health, Morale;
        int sp, ap;

          public int SP { get { return sp; } set { sp = Maths.MinMax(0, Record.SP, value); } }
          public int Health { get { return health; } set { health = Math.Min(Record.Health, value); } }
          public int AP { get { return ap; } set { ap = Maths.MinMax(0, Record.Speed, value); } }
          //void take_m_ap(int num) { AP = Math.Max(0, AP - num); }
        int[] status = new int[15];
          public int Status(eAffliction type) { return status[(int)type]; } //ICharacter
          public void SetStatus(eAffliction type, int val, int min = Int32.MinValue, int max = Int32.MaxValue) { status[(int)type] = Maths.MinMax(min, max, val); }
          public void IncStatus(eAffliction type, int val, int max = Int32.MaxValue)
          {
              status[(int)type] += val;
              if (status[(int)type] > max) status[(int)type] = max;
          }
          public void DecStatus(eAffliction type, int val, int min = Int32.MinValue)
          {
              status[(int)type] -= val;
              if (status[(int)type] < min) status[(int)type] = min;
          }
          public void CounteractStatus(eAffliction type, int amount = 1)
          {
              if (status[(int)type] > amount) status[(int)type] -= amount;
              else if (status[(int)type] < -amount) status[(int)type] += amount;
              else status[(int)type] = 0;
          }
          public void ClearStatus()
          {
              for (int n = 0; n < status.Length; n++)
                  status[n] = 0;
          }

          public string DeathSound { get { return Record.DeathSound; } }

        static short[] hit_chance = {20,30,40,45,50,55,60,65,69,73,
							77,81,84,87,90,92,94,96,97,98,99
							,99,99,99,99,99,99,99,99,99,99
							,99,99,99,99,99,99,99,99,99,99,
							99,99,99,99,99,99,99,99,99,99};


/* *********************************************************************************************************************************************************************
 *                                                                              METHODS    
 * *********************************************************************************************************************************************************************/
        public NPC() { }

        public static NPC Instantiate(NPCPreset cs) {

            //If a life variable has been set and its non-zero, never spawn the creature.
            if (cs.LifeVariable != null && cs.LifeVariable != "" && GlobalVariables.Get(cs.LifeVariable) != 0)
                return null;

            NPC ci = new NPC();

            ci.Active = eActive.INACTIVE;//eActive.DOCILE; //Friendly
            ci.Attitude = cs.Attitude;
            ci.Pos = cs.Pos;
            ci.Record = cs.Record;
            ci.Summoned = 0;
            ci.Start = cs;
            ci.Dir = new Direction();
            ci.Mobile = cs.Mobile;

            ci.health = ci.Record.Health;
            ci.Morale = ci.Record.Morale;
            ci.sp = ci.Record.SP;
            ci.ap = ci.Record.Speed;//.AP;

            return ci;
        }

        public static NPC Instantiate(NPCRecord nr, Location loc, eAttitude tude = eAttitude.NOT_SPECIFIED )
        {  //This one is for making the creature instances for an outside combat map
            NPC ci = new NPC();
            ci.Active = eActive.COMBATIVE;
            ci.Pos = loc;
            if (tude == eAttitude.NOT_SPECIFIED) ci.Attitude = nr.Attitude; else ci.Attitude = tude;
            ci.Record = nr;
            ci.Mobile = true;
            ci.health = ci.Record.Health;
            ci.Morale = ci.Record.Morale;
            ci.sp = ci.Record.SP;
            ci.AP = ci.Record.Speed;//.AP;
            return ci;
        }

        public static NPC Summon(NPCRecord cr, Location pos, eAttitude attitude, int duration) {
            NPC ci = new NPC();
            ci.Active = eActive.COMBATIVE;
            ci.Pos = pos;
            ci.Record = cr;
            ci.Summoned = duration;
            ci.Attitude = attitude;
            ci.Dir = new Direction(eDir.N);
            ci.health = cr.Health;
            ci.Morale = cr.Morale;
            ci.sp = cr.SP;
            ci.AP = cr.Speed;// AP;
            ci.Mobile = true;
            return ci;
        }

        public static NPC SplitOffCopy(NPC cr, Location pos)
        {
            NPC ci = new NPC();
            ci.Active = eActive.COMBATIVE;
            ci.Pos = pos;
            ci.Record = cr.Record;
            ci.Summoned = 0;
            ci.Attitude = cr.Attitude;
            ci.Dir = cr.Dir;
            ci.health = cr.health;
            ci.Morale = cr.Morale;
            ci.sp = cr.sp;
            ci.AP = cr.AP;
            ci.Mobile = true;
            return ci;
        }

        public void Draw(SpriteBatch sb, XnaRect dr, Color col)
        {
            if (Record.SpecialSkill == eCSS.INVISIBLE) return;

            float rot = 0;

            if (animAction != null) 
                animAction.AdjustCharRect(ref dr, ref rot, ref col);
            if (animFlash != null)
                animFlash.AdjustCharRect(ref dr, ref rot, ref col);

            dr.Offset(dr.Width / 2, dr.Height / 2);

            Texture2D stex;
            XnaRect sr = Record.GetGraphic(direction.IsFacingRight, animAction is Animation_Attack, out stex);
            sb.Draw(stex, dr, sr, col, rot, new Vector2(Gfx.CHARGFXWIDTH * Record.Width / 2, Gfx.CHARGFXHEIGHT * Record.Height / 2)/*Vector2.Zero*/, SpriteEffects.None, 0);

            if (Gfx.ZoomSizeW > Gfx.ZOOMSIMPLETHRESHOLD && Gfx.ZoomSizeH > Gfx.ZOOMSIMPLETHRESHOLD)
            {
                if (Game.PlayerTargeting && Action.TargetNumbersOn && targetingNum != -1)
                {
                    string s = ((char)(targetingNum + 97)).ToString();
                    Vector2 z = new Vector2(dr.X + (dr.Width / 2f) - Gfx.TinyFont.MeasureString(s).Width, dr.Y + (dr.Height / 2f) - Gfx.TinyFont.MeasureString(s).Height);
                    sb.DrawString(Gfx.TinyFont, s, z, Color.White);
                }

                if (Game.Mode == eMode.COMBAT && Gfx.DrawHealthBars && !Dying)
                {
                    XnaRect br = new XnaRect(134, 181, 20, 6);

                    //Health
                    float h = (float)Health / (float)MaxHealth;
                    br.Y = ((int)(6 - h / (1f / 6f))) * 8 + 181;

                    sb.Draw(Gfx.NewGui, new Vector2(dr.X - (dr.Width / 2f), dr.Y + (dr.Height / 2f) - 6), br, Color.White);
                }
            }
        }

        /// <summary>
        /// Called at the start of the NPCs turn to give it its action points for that turn
        /// </summary>
        public void AssignAP() {

            Provocation = Math.Max(Provocation - 1, 0); //Decay provocation score  before turn starts
            AP = 0;
            if (Active == eActive.COMBATIVE) { // Begin action loop for angry, active monsters
                // First note that hostile monsters are around.
                //if (IsABaddie) Party.vogelsExtraShit[5, 9] = 30;

                // Give monster its action points
                AP = Record.Speed;

                //In non-combat mode, npcs only get a third of their AP (They will have already moved separately so this is only for other
                //actions like attacking/casting spells etc.
                if (Game.Mode == eMode.TOWN)
                    AP = Math.Max(1, AP / 3);

                if (Party.Age % 2 == 0 && Status(eAffliction.HASTE_SLOW) < 0) AP = 0;
                if (AP > 0) { // adjust for webs (currently aslept/paralyzed monsters are cleaning webs as efficiently (i.e badly) as if awoken/free)
                    AP = Math.Max(0, AP - Status(eAffliction.WEBS) / 2);
                    if (AP == 0) SetStatus(eAffliction.WEBS, Math.Max(0, Status(eAffliction.WEBS) - 2));
                }
                if (Status(eAffliction.HASTE_SLOW) > 0)
                    AP *= 2;

                if ((Status(eAffliction.ASLEEP) > 0) || (Status(eAffliction.PARALYZED) > 0))
                    AP = 0;
                if (Game.PassiveNPCs)
                    AP = 0;

                MessingAround = 0;
            }
        }

        public Boolean CanSee(Location l) {
            int i, j;
            Location destination;

            for (i = 0; i < Record.Width; i++)
                for (j = 0; j < Record.Height; j++) {
                    destination.X = Pos.X + i;
                    destination.Y = Pos.Y + j;
                    if (curTown.CanSee(destination, l) < Constants.OBSCURITY_LIMIT)
                        return true;
                }
            return false;
        }

        //Takes into account NPCs that are bigger than 1 tile
        public bool AdjacentTo(Location loc) {

            for(int y = 0; y < Record.Height; y++)
                for (int x = 0; x < Record.Width; x++) {
                    if (loc.adjacent(Pos + new Location(x,y))) return true;
                }
            return false;
        }

        public bool OnSpace(Location loc)
        {
            for (int y = 0; y < Record.Height; y++)
                for (int x = 0; x < Record.Width; x++)
                {
                    if (loc == Pos + new Location(x, y)) return true;
                }
            return false;
        }

        public bool AlliedWith(ICharacter ch)
        {
            if (!IsABaddie)
                if (ch.MyAttitude() == eAttitude.NEUTRAL || ch.MyAttitude() == eAttitude.FRIENDLY) return true;
                else return false;
            return Attitude == ch.MyAttitude();
        }

        /// <summary>
        /// Perform the NPCs main move.
        /// </summary>
        /// <returns>Return true if this NPC has now run out of action points (or has died)</returns>
        public bool DoCombatMove()
        {
            if (AP <= 0 || !IsAlive()) return true;
            if (Status(eAffliction.ASLEEP) > 0 || Status(eAffliction.PARALYZED) > 0) return true;
            hasJustAttacked = false;

            List<PCType> pc_adj = new List<PCType>();

            if (MessingAround == 0)
            {
                foreach (PCType pc in Party.EachIndependentPC())// (j = 0; j < 6; j++)
                    if (AdjacentTo(pc.Pos) == true)
                        pc_adj.Add(pc);
            }

#if USE_MOVE_SCRIPTS
            Script.RunNPCMove(funcCombatMove, this);
#else
////////////////////////////////////////////////////////////////////START SCRIPT - COMBAT MOVE////////////////////////////////////////////////////////////////////
            #region NPC combat move script
            
            if (Game.Mode == eMode.COMBAT) PickTarget();

            bool acted_yet = false;

            // Now the monster, if evil, looks at the situation and maybe picks a tactic.
            // This only happens when there is >1 a.p. left, and tends to involve
            // running to a nice position.
            int current_monst_tactic = 0;
            if (Target != null && AP > 1 && MessingAround == 0)
            {
                Location l = Party.ClosestPC(Pos).Pos;
                if ((Record.MageLevel > 0 || Record.PriestLevel > 0) && l.DistanceTo(Pos) < 5 && !AdjacentTo(l))
                    current_monst_tactic = 1; // this means flee

                if (((Record.SpecialSkill > eCSS.NO_SPECIAL_ABILITY && Record.SpecialSkill < eCSS.THROWS_ROCKS1)
                        || Record.SpecialSkill == eCSS.GOOD_ARCHER) && // Archer?
                Pos.DistanceTo(Target.Pos) < 6 && !AdjacentTo(Target.Pos))
                    current_monst_tactic = 1; // this means flee
            }

            // flee
            if (Target is PCType &&
                ((Morale <= 0 && Record.SpecialSkill != eCSS.MINDLESS && Record.Genus != eGenus.UNDEAD)
                || current_monst_tactic == 1))
            {
                if (Morale < 0) Morale++;
                if (Health > 50) Morale++;
                int r1 = Maths.Rand(1, 1, 6);
                if (r1 == 3) Morale++;
                if (Target.IsAlive() && Mobile)
                {
                    acted_yet = WalkAwayFrom(Target.Pos);
                    if (acted_yet) AP--;
                }
            }
            if (Target != null && Target.IsAlive() && Attitude > eAttitude.NEUTRAL
                && CanSee(Target.Pos)) //&& can_see_monst(Target.Pos))
            { // Begin spec. attacks

                // Breathe (fire)
                if ((Record.Breath > 0)
                    && (Maths.Rand(1, 1, 8) < 4) && !acted_yet)
                {
                    if ((Target != null)
                        && (Pos.DistanceTo(Target.Pos) <= 8))
                    {
                        acted_yet = breathAttack(Target.Pos);
                        acted_yet = true;
                        AP-=4;
                    }
                }
                // Mage spell
                if (Record.MageLevel > 0 && (Maths.Rand(1, 1, 10) < (Record.PriestLevel > 0 ? 6 : 9))
                    && !acted_yet)
                {
                    if ((!AdjacentTo(Target.Pos) || Maths.Rand(1, 0, 2) < 2 || Level > 9) && Pos.DistanceTo(Target.Pos) <= 10)
                    {
                        Location target_pos;
                        ICharacter target_char;

                        NPCMageSpell spell = selectMageSpell(out target_pos, out target_char);

                        if (spell == null)
                            SP++;
                        else
                            castMageSpell(spell, target_pos, target_char);

                        acted_yet = true;
                        AP-=5;
                    }
                }
                // Priest spell
                if (Record.PriestLevel > 0 && Maths.Rand(1, 1, 8) < 7 && !acted_yet)
                {
                    if ((!AdjacentTo(Target.Pos) || Maths.Rand(1, 0, 2) < 2 || Level > 9) && Pos.DistanceTo(Target.Pos) <= 10)
                    {
                        Location target_pos;
                        ICharacter target_char;

                        NPCPriestSpell spell = selectPriestSpell(out target_pos, out target_char);
                        if (spell == null)
                            SP++;
                        else
                            castPriestSpell(spell, target_pos, target_char);

                        acted_yet = true;
                        AP-=4;
                    }
                }

                int[] abil_range = {0,6,8,8,10, 10,10,8,6,8, 6,0,0,0,6, 0,0,0,0,4, 10,0,0,6,0,
							        0,0,0,0,0, 0,0,8,6,9, 0,0,0,0,0};
                int[] abil_odds = {0,5,7,6,6, 5,5,6,6,6, 6,0,0,0,4, 0,0,0,0,4, 8,0,0,7,0,
							        0,0,0,0,0, 0,0,7,5,6, 0,0,0,0,0};

                // Missile
                if (abil_range[(int)Record.SpecialSkill] > 0 // breathing gas short range
                    && Maths.Rand(1, 1, 8) < abil_odds[(int)Record.SpecialSkill] && !acted_yet)
                {
                    // Don't fire when adjacent, unless non-gaze magical attack
                    if ((!AdjacentTo(Target.Pos) ||
                        (Record.SpecialSkill > eCSS.THROWS_RAZORDISKS && Record.SpecialSkill != eCSS.GOOD_ARCHER
                        && Record.SpecialSkill != eCSS.ACID_SPIT))
                        && Pos.DistanceTo(Target.Pos) <= abil_range[(int)Record.SpecialSkill]) // missile range
                    {
                        Game.AddMessage(Record.Name + ":");
                        FireMissile();//Status(eAffliction.BLESS_CURSE), Record.SpecialSkill, Pos, Target);

                        // Vapors don't count as action
                        if (Record.SpecialSkill == eCSS.THROWS_DARTS || Record.SpecialSkill == eCSS.THROWS_RAZORDISKS ||
                            Record.SpecialSkill == eCSS.GOOD_ARCHER)
                            AP-=2;
                        else if (Record.SpecialSkill == eCSS.HEAT_RAY)
                            AP--;
                        else 
                            AP-=3;
                        acted_yet = true;
                    }
                }
            } // Special attacks

            if (Target != null && !AlliedWith(Target) && AdjacentTo(Target.Pos) && !acted_yet)
            {
                Attack(Target);
                AP-=4;
                acted_yet = true;
            }

            if (Game.Mode == eMode.COMBAT)
            {
                if (!acted_yet && Mobile)
                {  
                    Location move_targ = Pos; 

                    if (Target != null && Target.IsAlive())
                        WalkToTarget();
                    else if (Attitude == eAttitude.NEUTRAL)
                    {
                        acted_yet = WalkRandomly();
                        MessingAround++;
                    }

                    AP-=1;
                }
                if (!acted_yet && (Mobile == false))
                { // drain action points
                    AP-=1;
                    MessingAround++;
                }
            }
            else if (!acted_yet)
            {
                AP-=1;
                MessingAround++;
            }

            // Place fields for monsters that create them. Only done when monst sees foe
            if (Target != null && Record.Radiate != eRadiate.NONE && curTown.CanSee(Pos, Target.Pos) < Constants.OBSCURITY_LIMIT)
            {
                if (Maths.Rand(1, 1, 100) <= Record.RadiateProbability)
                {
                    switch (Record.Radiate)
                    {
                        case eRadiate.FIRE: curTown.PlaceFieldPattern(Pattern.Square, Pos, Field.FIRE_WALL, null); break;
                        case eRadiate.ICE: curTown.PlaceFieldPattern(Pattern.Square, Pos, Field.ICE_WALL, null); break;
                        case eRadiate.SHOCK: curTown.PlaceFieldPattern(Pattern.Square, Pos, Field.FORCE_WALL, null); break;
                        case eRadiate.ANTIMAGIC: curTown.PlaceFieldPattern(Pattern.Square, Pos, Field.ANTIMAGIC, null); break;
                        case eRadiate.SLEEP: curTown.PlaceFieldPattern(Pattern.Square, Pos, Field.SLEEP_CLOUD, null); break;
                        case eRadiate.STINK: curTown.PlaceFieldPattern(Pattern.Square, Pos, Field.STINK_CLOUD, null); break;
                        case eRadiate.SUMMON:
                            if (curTown.SummonMonster(this, Record.NPCtoSummon, Pos, 130) == true)
                            {
                                Game.AddMessage(String.Format("  {0} summons allies.", Name));
                                Sound.Play("061_summoning");
                            }
                            break;
                    }
                }
            }
          
#endregion
#endif
/////////////////////////////////////////////////////////////////////END SCRIPT////////////////////////////////////////////////////////////////////////

            // PCs that are parrying attack approaching monsters
            foreach (PCType pc in Party.EachAlivePC())
                if (IsABaddie && !Dying && pc.Parry > 99 && AdjacentTo(pc.Pos) && !pc_adj.Contains(pc))
                {
                    pc.Parry = 0;
                    pc.Attack(this);
                }

            // pcs attack any fleeing monsters
            if (Game.Mode == eMode.COMBAT)
                for (int n = pc_adj.Count - 1; n >= 0; n--)
                    if (!Dying && AdjacentTo(pc_adj[n].Pos) == false && IsABaddie && pc_adj[n].Status(eAffliction.INVISIBLE) == 0)
                    {
                        pc_adj[n].Attack(this);
                        pc_adj.Remove(pc_adj[n]);
                        new Animation_Hold();
                    }

            // If monster dead, take away actions
            if (!IsAlive())
                AP = 0;

            if (MessingAround == 1 && (Maths.Rand(1, 0, 1) == 0)) // If monster's just pissing around, give up
                AP = 0;

            if (AP <= 0) 
            {
                //The NPCs turn is now over
                if (hasJustAttacked == false) LastAttacked = null; //We didn't attack this turn, reset LastAttacked for next time.
                return true;
            }
            return false; //The NPC still has action points to spend - don't end its turn yet.
        }

        public void DoNonCombatMove()
        {
            //Sleeping or paralyzed npcs can't move.
            if (Status(eAffliction.ASLEEP) > 0 || Status(eAffliction.PARALYZED) > 0) return;

#if USE_MOVE_SCRIPTS

            Script.RunNPCMove("DoNonCombatMove", this);
#else
            ////////////////////////////////////////////////////////////START SCRIPT - NON-COMBAT MOVE////////////////////////////////////////////////////////////////////////////
            #region NPc non-combat move script
            
            // have to pick targets
            if (Active != eActive.COMBATIVE)
                Target = null; //Not active : no target
            else
            {
                //NPC wants to fight. Look for a target.
                PickTarget();
            }

            if (Mobile && Active != eActive.INACTIVE)
            {
                if (Active == eActive.DOCILE)
                {
                    if (Maths.Rand(1, 0, 1) == 0) WalkRandomly(); 
                }
                else
                {
                    if (Target != null)
                    {
                        if (Morale < 0 && Record.SpecialSkill != eCSS.MINDLESS && Record.Genus != eGenus.UNDEAD)
                        {
                            WalkAwayFrom(Target.Pos);
                            if (Maths.Rand(1, 0, 10) < 6) Morale++;
                        }
                        else if (curTown.NPCHateSpot(this,Pos))
                        {
                            Location l2 = curTown.FindClearSpot(Pos, true, false);
                            if (l2 != Pos) WalkTowards(l2);
                            else WalkToTarget();
                        }
                        else if (Record.MageLevel == 0 || curTown.CanSee(Pos, Target.Pos) > 3)
                            WalkToTarget();
                    }
                    else
                        if (Maths.Rand(1, 0, 1) == 0) WalkRandomly();
                }
            }

            if (curTown.CanSee(Pos, Party.Pos) < 5)
            {
                if (Active == eActive.INACTIVE)   
                    Active = eActive.DOCILE;
            }

            // Make hostile monsters active
            if (Active == eActive.DOCILE && IsABaddie && Pos.DistanceTo(Party.Pos) <= 8)
            {
                int r1 = Maths.Rand(1, 1, 100);
                r1 += (Party.Stealth > 0) ? 46 : 0;
                r1 += curTown.CanSee(Pos, Party.Pos) * 10; //Guarantees monsters will not see if walls in the way - as CanSee returns 5 if blocked
                if (r1 < 50)
                {
                    Active = eActive.COMBATIVE;
                    new Animation_CharFlash(this, Color.Red, Record.Humanish ? "018_drawingsword" : "046_growl");
                    Game.AddMessage("Monster saw you!");
                }
                else
                    foreach (NPC ci in curTown.NPCList)
                        if (ci.Active == eActive.COMBATIVE && pos.DistanceTo(ci.Pos) <= 5)
                        {
                            Active = eActive.COMBATIVE;
                            new Animation_CharFlash(this, Color.Red, Record.Humanish ? "018_drawingsword" : "046_growl");
                            return;
                        }
            }

            #endregion
            /////////////////////////////////////////////////////////////////////END SCRIPT/////////////////////////////////////////////////////////////////////////
#endif
        }

        /// <summary>
        /// NPC will try changing the target if it feels like it.
        /// </summary>
        /// <returns>True if a valid target has been found.</returns>
        public bool PickTarget()
        {
            //If existing target is now on the NPCs side, or has vanished, reset target.
            if (Target != null && (AlliedWith(Target) || !Target.IsAlive())) Target = null;

            //If this is not-combat mode, change to any of the PCs at random as they are all on the same space
            if (Game.Mode != eMode.COMBAT && Target is PCType)
                Target = Party.RandomPC();

            //An NPC at random may become distracted
            if (Target != null && Maths.Rnd.NextDouble() > Constants.AI_DISTRACTION_CHANCE)
            {
                //Keep existing target but try to recalculate path.

                //If no path to target, or if target is now closer than the existing path's endpoint, re-calculate it.
                if (PathToTarget == null || !PathToTarget.StillValid(Pos, Target.Pos) ||//PathToTarget.Count == 0 || Pos != PathPosition || 
                    Pos.VDistanceTo(Target.Pos) < Pos.VDistanceTo(PathToTarget.GetDestination()) ||
                    curTown.NPCHateSpot(this, Pos))
                {
                    PathToTarget = MapPath.CalculateNew(curTown, this, Target.Pos);
                    //if (PathToTarget != null)
                    //{
                    //    PathPosition = Pos;
                    //    PathDestination = Target.Pos;
                    //}
                }
                return true;
            }

            Target = null;

            //Npc now considers which visible enemy is the most attractive to attack.

            //A list is compiled with all the possibilites and a score for each one.

            var possibles = new List<Tuple<ICharacter, int>>();

            foreach (NPC npc in curTown.NPCList) {

                //If npc is on our side, don't consider
                if (AlliedWith(npc)) continue;

                //If npc is not visible, don't consider
                if (curTown.CanSee(pos, npc.pos) >= 5) continue;

                //Score is based on weighing together the distance to the target (closer is preferable) to its provocation
                //value. Provocation is calculated at the end of each character's turn based on what it did that turn (eg, 
                //casting a spell or attacking is a big provocation)
                int score = pos.DistanceTo(npc.pos);

                //The npc gets a bonus if it is right next to the target candidate
                if (score <= 1) score -= Constants.AI_ADJACENCY_BONUS;


                score -= npc.Provocation;

                //NPCs with a 'Drain spell points' missile attack greatly favour enemies with spell points to drain
                if (Record.SpecialSkill == eCSS.SP_DRAIN_RAY && npc.SP <= 4) score += 100;

                //If we were specifically attacked by this enemy last turn, more likely to target it back.
                if (npc.LastAttacked == this) score -= Constants.AI_RETURN_FAVOUR_BONUS;

                //Add it to the list.
                var candidate = new Tuple<ICharacter, int>(npc, score);
                possibles.Add(candidate);
            }

            //Unless the npc is on the PCs side, also try adding the PCs to the list
            if (IsABaddie) {

                foreach (PCType pc in Party.EachIndependentPC()) {

                    //Mostly the same as for npcs
                    if (curTown.CanSee(pos, pc.Pos) >= Constants.OBSCURITY_LIMIT) continue;
                    int score = pos.DistanceTo(pc.Pos);
                    score -= pc.Provocation;
                    if (pc.LastAttacked == this) score -= Constants.AI_RETURN_FAVOUR_BONUS;

                    //Special bonus possibly applied to make npcs pay extra special attention to pcs
                    score -= Constants.AI_I_HATE_PCS_BONUS;

                    //NPCs with a 'Drain spell points' missile attack greatly favour enemies with spell points to drain
                    if (Record.SpecialSkill == eCSS.SP_DRAIN_RAY && pc.SP <= 4) score += 100;

                    //Add it to the list.
                    var candidate = new Tuple<ICharacter, int>(pc, score);
                    possibles.Add(candidate);
                }

            }

            //No targets found - return with failure.
            if (possibles.Count == 0) return false;

            //Order the list by score.
            possibles = possibles.OrderBy(n => n.Item2).ToList();

            //Set the new target to the one with the lowest score and return success.
            Target = possibles[0].Item1;

            PathToTarget = MapPath.CalculateNew(curTown, this, Target.Pos);
            //if (PathToTarget != null)
            //{
            //    PathPosition = Pos;
            //    PathDestination = Target.Pos;
            //}

            return true;
        }

        public Boolean WalkRandomly()
        {
            Boolean acted_yet = false;
            int j;
            Location store_loc = new Location(0, 0);

            if (Pos == WanderTarget)
                WanderTarget.X = 0;

            // FIrst, try to move to monst_targs. If it don't work, then we'll shift.
            if (WanderTarget.X > 0)
                acted_yet = WalkTowards(WanderTarget);

            if (acted_yet == false) {
                WanderTarget.X = 0;
                for (j = 0; j < 3; j++) {
                    store_loc = Pos;
                    store_loc.X += Maths.Rand(1, 0, 24) - 12;
                    store_loc.Y += Maths.Rand(1, 0, 24) - 12;
                    if (curTown.InBounds(store_loc) && curTown.CanSee(Pos, store_loc) < Constants.OBSCURITY_LIMIT)
                    {
                        WanderTarget = store_loc; j = 3;
                    }
                }

                if (WanderTarget.X == 0) {
                    // maybe pick a wand loc, else just pick a loc

                    //if (curTown.SpawnPoints.Count > 0) {
                    //    j = Maths.Rand(1, 0, curTown.SpawnPoints.Count - 1);
                    //    store_loc = curTown.SpawnPoints[j];
                    //}

                    if (curTown.InBounds(store_loc) && (Maths.Rand(1, 0, 1) == 1))
                        WanderTarget = store_loc;
                    else {
                        store_loc = Pos;
                        store_loc.X += Maths.Rand(1, 0, 20) - 10;
                        store_loc.Y += Maths.Rand(1, 0, 20) - 10;
                        if (curTown.InBounds(store_loc))
                            WanderTarget = store_loc;
                    }
                }
                if (WanderTarget.X > 0)
                    acted_yet = WalkTowards(WanderTarget);
            }

            return acted_yet;
        }


        public void WalkToTarget()
        {

            if (PathToTarget != null && PathToTarget.StillValid(Pos, Target.Pos))//.Count > 0 && Pos == PathPosition)
            {
                if (Walk(PathToTarget.GetNext()))
                {
                //    PathPosition = Pos;
                    return;
                }
            }

            //Path hasn't worked. Get rid of it.
            PathToTarget = null;

            //Just try to walk instead.
            WalkTowards(Target.Pos);

            return;
        }

        //Doesn't necessarily seek 'party', Jeff, just the square l2
        public Boolean WalkTowards(Location l2) {
            Boolean acted_yet = false;

            if (Pos.X > l2.X && Pos.Y > l2.Y)
                acted_yet = Walk(eDir.NW);
            if (Pos.X < l2.X && Pos.Y < l2.Y && !acted_yet)
                acted_yet = Walk(eDir.SE);
            if (Pos.X > l2.X && Pos.Y < l2.Y && !acted_yet)
                acted_yet = Walk(eDir.SW);
            if (Pos.X < l2.X && Pos.Y > l2.Y && !acted_yet)
                acted_yet = Walk(eDir.NE);
            if (Pos.X > l2.X && !acted_yet)
                acted_yet = Walk(eDir.W);
            if (Pos.X < l2.X && !acted_yet)
                acted_yet = Walk(eDir.E);
            if (Pos.Y < l2.Y && !acted_yet)
                acted_yet = Walk(eDir.S);
            if (Pos.Y > l2.Y && !acted_yet)
                acted_yet = Walk(eDir.N);
            if (!acted_yet) {
                MessingAround++;
                acted_yet = Walk(Direction.Random().Dir);
            }
            return acted_yet;
        }

        public Boolean WalkAwayFrom(Location l2) {
            Boolean acted_yet = false;

            if ((Pos.X > l2.X) & (Pos.Y > l2.Y))
                acted_yet = Walk(eDir.SE);
            if ((Pos.X < l2.X) & (Pos.Y < l2.Y) & (!acted_yet))
                acted_yet = Walk(eDir.NW);
            if ((Pos.X > l2.X) & (Pos.Y < l2.Y) & (!acted_yet))
                acted_yet = Walk(eDir.NE);
            if ((Pos.X < l2.X) & (Pos.Y > l2.Y) & (!acted_yet))
                acted_yet = Walk(eDir.SW);
            if ((Pos.X > l2.X) & (!acted_yet))
                acted_yet = Walk(eDir.E);
            if ((Pos.X < l2.X) & (!acted_yet))
                acted_yet = Walk(eDir.W);
            if ((Pos.Y < l2.Y) & (!acted_yet))
                acted_yet = Walk(eDir.N);
            if ((Pos.Y > l2.Y) & (!acted_yet))
                acted_yet = Walk(eDir.S);
            if (!acted_yet) {
                MessingAround++;
                //acted_yet = rand_move();
                acted_yet = Walk(Direction.Random().Dir);
            }
            return acted_yet;
        }

        public Boolean Walk(eDir dir) {

            Direction d = new Direction(dir);
            Location destination = pos + d;
            if (!curTown.CheckNPCDoors(destination, this)) return false;
            else if (curTown.CharacterCanBeThere(destination, this) == false)
                return false;
            else if (Active != eActive.COMBATIVE && (curTown.FieldThere(destination, Field.BARREL) || curTown.FieldThere(destination, Field.CRATE)))
                return false;
            else
            {
                direction.Dir = d.Dir;//new Direction(Pos, destination);//Pos.DirectionTo(destination);
                /*charAnim =*/
                new Animation_Move(this, Pos, destination, Game.Mode == eMode.COMBAT);
                curTown.PushLocation(this, destination);
                Pos = destination;
                curTown.InflictFields(this);
                return true;
            }
            //return false;
        }

        int calculateHit(int how_much, eDamageType dam_type)
        {
            eImmunity resist;

            //victim = &c_town.monst.dudes[which_m];
            resist = Record.Immunities;

            eDamageType[] dams = { eDamageType.MAGIC, eDamageType.FIRE, eDamageType.COLD, eDamageType.POISON };
            eImmunity[] res = { eImmunity.MAGIC_RESISTANCE, eImmunity.FIRE_RESISTANCE, eImmunity.COLD_RESISTANCE, eImmunity.POISON_RESISTANCE };
            for (int a = 0; a < 4; a++)
            {
                if (dam_type == dams[a])
                {
                    if ((resist & (res[a] + 1)) != eImmunity.NONE)
                        how_much = 0;
                    else if ((resist & res[a]) != eImmunity.NONE)
                        how_much = how_much / 2;
                }
            }

            // Saving throw
            if ((dam_type == eDamageType.FIRE || dam_type == eDamageType.COLD) && (Maths.Rand(1, 0, 20) <= Record.Level))
                how_much = how_much / 2;
            if (dam_type == eDamageType.MAGIC && Maths.Rand(1, 0, 24) <= Record.Level)
                how_much = how_much / 2;

            // Rentar-Ihrno?
            if (Record.SpecialSkill == eCSS.INVULNERABILITY)
                how_much = how_much / 10;

            int r1 = Maths.Rand(1, 0, (Record.Armour * 5) / 4);
            r1 += Record.Level / 4;
            if (dam_type == 0)
                how_much -= r1;

            how_much = Maths.Max(how_much, 0);

            return how_much;
        }

        //// Damaging and killing monsters needs to be here because several have specials attached to them.
        public bool Damage(IExpRecipient attacker, int how_much, int how_much_spec, eDamageType dam_type, eDamageType spec_dam_type = eDamageType.WEAPON, string sound_type = null)
        {
        //public Boolean damage_monst(object who_hit, int how_much, int how_much_spec, eDamageType dam_type, bool processing_fields = false, int sound_type = 0)//, bool no_award_xp=false)
        //    //short which_m, who_hit, how_much, how_much_spec;  // 6 for who_hit means dist. xp evenly  7 for no xp
        //    //short dam_type;  // 0 - weapon   1 - fire   2 - poison   3 - general magic   4 - unblockable  5 - cold 
        //    // 6 - demon 7 - undead  
        //    // 9 - marked damage, from during anim mode
        //    //+10 = no_print
        //    // 100s digit - damage sound for boom space

            if (!(Game.PCsAlwaysHit && attacker is PCType))
            {
                how_much = calculateHit(how_much, dam_type);
                how_much_spec = calculateHit(how_much_spec, spec_dam_type);
            }
            else if (how_much <= 0) how_much = 1;

            // Absorb damage?
            if ((dam_type == eDamageType.FIRE || dam_type == eDamageType.MAGIC || dam_type == eDamageType.COLD)
             && Record.SpecialSkill == eCSS.ABSORB_SPELLS)
            {
                Health += how_much;
                Game.AddMessage("  Magic absorbed.");
                return false;
            }

            if (how_much <= 0)
            {
                if (Game.Mode == eMode.COMBAT)
                    Game.AddMessage(String.Format("  {0} undamaged.", Name));
                //if ((how_much <= 0) && ((dam_type == eDamageType.WEAPON) || (dam_type == eDamageType.UNDEAD) || (dam_type == eDamageType.DEMON)))
                //{
                //    //GameScreen.draw_terrain(2);
                //    //new Animation_Hold("002_swordswish");
                //    //Sound.Play(2);
                //}
                return false;
            }

            eDamageType displaydamtype = (spec_dam_type > 0 && spec_dam_type != eDamageType.WEAPON) ? spec_dam_type : dam_type;

            if (sound_type == null)
            {
                switch (dam_type)
                {
                    case eDamageType.FIRE:
                    case eDamageType.UNBLOCKABLE: sound_type = "073_fireimpact"; break;
                    case eDamageType.MAGIC: sound_type = "089_zap"; break;
                    case eDamageType.COLD: sound_type = "075_cold"; break;
                    case eDamageType.POISON: sound_type = "088_slime"; break;
                    default: sound_type = "032_gethit1"; break;
                }
            }

            ///*if (!no_print)*/ InfoListWindow.monst_damaged_mes(how_much, how_much_spec, this);

            if (how_much_spec > 0)
                Game.AddMessage(
                    String.Format("  {0} takes {1}+{2}", Record.Name, how_much, how_much_spec));
            else
                Game.AddMessage(
                    String.Format("  {0} takes {1}", Record.Name, how_much));


            Health = Health - how_much - how_much_spec;

            if (Game.OneHitKill)
                Health = -1;
            // splitting monsters
            if ((Record.SpecialSkill == eCSS.SPLITS) && (Health > 0)) curTown.SplitOffMonster(this);

            if (attacker is PCType || attacker is PartyType)
                Party.total_dam_done += how_much + how_much_spec;

            // Monster is damaged. Make it hostile.
            Active = eActive.COMBATIVE;

            Vector2 animpos = new Vector2(Pos.X + (Width == 2 ? 0.5f : 0), Pos.Y + (Height == 2 ? 0.5f : 0));

            new Animation_Damage(animpos, how_much, how_much_spec, displaydamtype, sound_type);

            //if (how_much_spec > 0)
            //{
            //    new Animation_Hold();
            //    new Animation_Damage(animpos, how_much_spec, eDamageType.MAGIC, sound_type);
            //}

            if (Health <= 0)
            {
                Game.AddMessage(String.Format("  {0} dies.", Record.Name));
                Kill(attacker, eLifeStatus.DEAD);//,no_award_xp);
            }
            else
            {
                if (how_much > 0) Morale--;
                if (how_much > 5) Morale--;
                if (how_much > 10) Morale--;
                if (how_much > 20) Morale -= 2;
            }

            if (!IsABaddie && (attacker is PCType || attacker is PartyType)
             && !curTown.Hostile)///*BoE.monsters_going == false ||*/ Party.vogelsExtraShit[5, 9] == 0))
            {
                Game.AddMessage("Damaged an innocent.           ");
                Attitude = eAttitude.HOSTILE_A;
                curTown.MakeTownHostile();
            }
            return true;
        }

        public bool Kill(IExpRecipient who_killed, eLifeStatus type, bool no_save = false)
        {
            int xp, i;

            // Special killing effects
            if (Start != null && Start.LifeVariable != null && Start.LifeVariable != "") Script.StuffDone[Start.LifeVariable] = 1;//Start.LifeVariable.Value = 1;//Party.SetStuffDone(Start.spec1, Start.spec2, 1);

            //SpecialNode.run_special(12, 2, Start.OnKill, Pos, ref s1, ref s2, ref s3);
            //if (Record.DeathSpecial != null)//if (Record.Radiate1 == 15)
            //    SpecialNode.run_special(12, 0, Record.DeathSpecial/*which_m->m_d.radiate_2*/, Pos, ref s1, ref s2, ref s3);
            if (Start != null) Script.New_KillNPC(Start.FuncOnDeath, this, who_killed as PCType);//new Script(Start.FuncOnDeath, eCallOrigin.KILLED_NPC);
            //new Script(Record.FuncOnDeath, eCallOrigin.KILLED_NPC);
            Script.New_KillNPC(Record.FuncOnDeath, this, who_killed as PCType);

            if (Summoned >= 100 || Summoned == 0)
            { // no xp for party-summoned monsters

                xp = Record.Level * 2;
                if (who_killed is PCType)
                    who_killed.AwardXP(xp);
                else if (who_killed is PartyType)
                    who_killed.AwardXP(xp / 6 + 1);

                if (who_killed is PCType || who_killed is PartyType)
                {
                    i = Math.Max((xp / 6), 1);
                    Party.AwardXP(i);
                }

                if ((Record.DropItem != null) && (Maths.Rand(1, 0, 100) < Record.DropItemChance))
                {
                    curTown.PlaceItem(Record.DropItem.Copy(), Pos);
                }
            }
            if (Summoned == 0)
                curTown.place_treasure(Pos, Record.Level / 2, Record.Treasure, 0);

            //i = which_m->m_loc.x;
            //j = which_m->m_loc.y;
            switch (Record.Genus)
            {
            case eGenus.DEMON: curTown.PlaceField(Pos, Field.CRATER); break;
            case eGenus.UNDEAD: /*if (which_m->number <= 59)*/ curTown.PlaceField(Pos, Field.BONES); break;
            case eGenus.SLIME:
            case eGenus.BUG: curTown.PlaceField(Pos, Field.SMALL_SLIME); break;
            case eGenus.STONE: curTown.PlaceField(Pos, Field.ROCKS); break;
            default: curTown.PlaceField(Pos, Field.SMALL_BLOOD); break;
            }

            if (/*((BoE.is_town()) || (BoE.which_combat_type == 1)) && (*/Summoned == 0)
            {
                curTown.KillCount++;// party.m_killed[c_town.town_num]++;
            }

            if (Start != null) Start.InstanceWasKilled = true;

            Party.total_m_killed++;// party.total_m_killed++;
            //if (Start != null && Start.LifeVariable != null) Start.LifeVariable.Value = 0;//.spec1 = 0; // make sure, if this is a spec. activated monster, it won't come back TODO: Figure this shite out
            //curTown.CreatureInstanceList.Remove(this);
            Dying = true;
            new Animation_Hold();
            new Animation_Death(this);
            return true;
        }

        static bool printedAcid = false;
        static bool printedPoison = false;
        static bool printedDisease = false;

        public static void StartofNPCAfflictions()
        {
            printedAcid = false;
            printedPoison = false;
            printedDisease = false;
        }

        public void HandleAfflictions()
        {
            if (Active == eActive.INACTIVE) return;

            if (Status(eAffliction.ACID) > 0)
            {  // Acid
                if (!printedAcid)
                {
                    Game.AddMessage("Acid:              ");
                    printedAcid = true;
                }
                int r1 = Maths.Rand(Status(eAffliction.ACID), 1, 6);
                Damage(this.IsABaddie ? Party : null, r1, 0, eDamageType.MAGIC);
                if (Dying) return;
                CounteractStatus(eAffliction.ACID);
            }

            if (Status(eAffliction.ASLEEP) == 1)
                Game.AddMessage("  " + Name + " wakes up.");
            CounteractStatus(eAffliction.ASLEEP);
            CounteractStatus(eAffliction.PARALYZED);

            if (Party.Age % 2 == 0)
            {

                CounteractStatus(eAffliction.BLESS_CURSE);
                CounteractStatus(eAffliction.HASTE_SLOW);
                CounteractStatus(eAffliction.WEBS);

                if (Status(eAffliction.POISON) > 0)
                {  // Poison
                    if (!printedPoison)
                    {
                        Game.AddMessage("Poisoned monsters:");
                        printedPoison = true;
                    }
                    int r1 = Maths.Rand(Status(eAffliction.POISON), 1, 6);
                    Damage(this.IsABaddie ? Party : null, r1, 0, eDamageType.POISON);
                    if (Dying) return;
                    CounteractStatus(eAffliction.POISON);
                }
                if (Status(eAffliction.DISEASE) > 0)
                {  // Disease
                    if (!printedDisease)
                    {
                        Game.AddMessage("Diseased monsters:");
                        printedDisease = true;
                    }
                    int k = Maths.Rand(1, 1, 5);
                    switch (k)
                    {
                        case 1:
                        case 2: Poison(2); break;
                        case 3: Slow(2); break;
                        case 4: Curse(2); break;
                        case 5: Scare(10); break;
                    }
                    if (Maths.Rand(1, 1, 6) < 4) CounteractStatus(eAffliction.DISEASE);
                }

            }

            if (Party.Age % 4 == 0)
            {
                SP += 2;
                CounteractStatus(eAffliction.DUMB);
            }
            
            
        }

        /// <summary>
        /// Called when a Death animation has finished, to finally remove the character from the game.
        /// </summary>
        public void FinishDying()
        {
            curTown.NPCList.Remove(this);
            //new Action(eAction.NONE);
        }

        void adjustMagic(ref int how_much)
        {
            if (Record.SpecialSkill == eCSS.ABSORB_SPELLS)
            {
                how_much = 0;
                Health += 3;
            }

            if (Record.ImmuneTo(eImmunity.MAGIC_RESISTANCE)) how_much = how_much / 2;
            if (Record.ImmuneTo(eImmunity.MAGIC_IMMUNITY)) how_much = 0;   /* crash!! */
        }

        public void Heal(int amt, bool silent = false)
        {
            int realamt = Health;
            Health += amt;
            realamt = Health - realamt;
            if (!silent) Game.AddMessage(String.Format("  {0} healed {1}", Name, realamt));
            new Animation_CharFlash(this, Color.FloralWhite, "052_magic2");
        }

        public void Poison(int how_much, bool silent = false)
        {
            if (Record.ImmuneTo(eImmunity.POISON_RESISTANCE)) how_much = how_much / 2;
            if (Record.ImmuneTo(eImmunity.POISON_IMMUNITY))
            {
                if (!silent) Game.AddMessage(String.Format("  {0} resists.", Name));
                return;
            }
            status[(int)eAffliction.POISON] = Math.Min(8, status[(int)eAffliction.POISON] + how_much);
            if (how_much > 0) new Animation_CharFlash(this, Color.LimeGreen, "017_shortcough");
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "resists poison." : " is poisoned."));//String.Format("  {0} resists.", Name)) : Game.AddMessage(String.Format("  {0} is poisoned.", Name));, this);
        }

        public void Acid(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            status[(int)eAffliction.ACID] = Maths.MinMax(-8, 8, status[(int)eAffliction.ACID] + how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} is covered with acid.", Name));
            new Animation_CharFlash(this, Color.GreenYellow, "042_dang");
        }

        public void Slow(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            status[(int)eAffliction.HASTE_SLOW] = Maths.MinMax(-8, 8, status[(int)eAffliction.HASTE_SLOW] - how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "resists." : " is slowed."));
            new Animation_CharFlash(this, Color.PaleTurquoise, "075_cold");

        }
        public void Haste(int how_much, bool silent = false)
        {
            //adjustMagic(ref how_much);
            status[(int)eAffliction.HASTE_SLOW] = Maths.MinMax(-8, 8, status[(int)eAffliction.HASTE_SLOW] + how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} is hastened.", Name));
            new Animation_CharFlash(this, Color.Orange, "075_cold");
        }
        public void Curse(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            status[(int)eAffliction.BLESS_CURSE] = Maths.MinMax(-8, 8, status[(int)eAffliction.BLESS_CURSE] - how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "resists curse." : " is cursed."));
            new Animation_CharFlash(this, Color.Black, "043_stoning");
        }
        public void Bless(int how_much, bool silent = false)
        {
            //adjustMagic(ref how_much);
            status[(int)eAffliction.BLESS_CURSE] = Maths.MinMax(-8, 8, status[(int)eAffliction.BLESS_CURSE] + how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} is blessed.", Name));
            new Animation_CharFlash(this, Color.Gold, "004_bless");
        }
        public void Web(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            status[(int)eAffliction.WEBS] = Maths.MinMax(-8, 8, status[(int)eAffliction.WEBS] + how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "avoids webbing." : " is caught in webs."));
            new Animation_CharFlash(this, Color.Gray, "017_shortcough");
        }
        public void Scare(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            Morale -= how_much;
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "resists fear." : " is scared."));
            //if (!silent) Sound.Play(54);
            new Animation_CharFlash(this, Color.DarkKhaki, "054_scream");
        }
        public void Disease(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            status[(int)eAffliction.DISEASE] = Maths.MinMax(-8, 8, status[(int)eAffliction.DISEASE] + how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "resists disease." : " is diseased."));
           new Animation_CharFlash(this, Color.DarkOrange, "066_disease");
        }

        public void Dumbfound(int how_much, bool silent = false)
        {
            adjustMagic(ref how_much);
            status[(int)eAffliction.DUMB] = Maths.MinMax(-8, 8, status[(int)eAffliction.DUMB] + how_much);
            if (!silent) Game.AddMessage(String.Format("  {0} {1}", Name, how_much == 0 ? "resists dumbfounding." : " is dumbfounded."));
            //if (!silent) Sound.Play(53);
            new Animation_CharFlash(this, Color.DarkSlateBlue, "067_huh");
        }

        public void Sleep(int amount, int penalty)
        {
            short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };
            int r1;

            if (Record.Genus == eGenus.UNDEAD || Record.Genus == eGenus.SLIME || Record.Genus == eGenus.STONE || Record.SpecialSkill == eCSS.BREATHES_SLEEP_CLOUDS
                 || Record.Radiate == eRadiate.SLEEP)
            {
                Game.AddMessage(String.Format("  {0} immune to sleep.", Name));
                return;
            }

            r1 = Maths.Rand(1, 0, 100);
            if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
            if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
            r1 += penalty;
            r1 -= 25;

            if (r1 > charm_odds[Record.Level / 2])
            {
                Game.AddMessage(String.Format("  {0} resists sleep.", Name));
                return;
            }
 
            IncStatus(eAffliction.ASLEEP, amount, 0);
                
            Game.AddMessage(String.Format("  {0} falls asleep.", Name));
            new Animation_CharFlash(this, Color.MidnightBlue, "096_sleep");    
        }

        public void Paralyze(int amount, int penalty)
        {
            short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };

            int r1 = Maths.Rand(1, 0, 100);
            if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
            if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
            r1 += penalty;
            r1 -= 15;

            if (r1 > charm_odds[Record.Level / 2])
            {
                Game.AddMessage(String.Format("  {0} resists.", Name));
                return;
            }
            IncStatus(eAffliction.PARALYZED, amount, 5000);
            Game.AddMessage(String.Format("  {0} is paralyzed.", Name));
            new Animation_CharFlash(this, Color.Olive, "090_paralyze");
        }

        public void Charm(int penalty)//int amount, eAffliction which_status, int penalty)
        // Also used for sleep and paralyze, which_statys is 0 means charm
        {
            short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };

            int r1 = Maths.Rand(1, 0, 100);
            if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
            if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
            r1 += penalty;

            if (r1 > charm_odds[Record.Level / 2])
            {
                Game.AddMessage(String.Format("  {0} resists.", Name));
                return;
            }
  
            Attitude = eAttitude.FRIENDLY;
            Game.AddMessage(String.Format("  {0} is charmed.", Name));
            new Animation_CharFlash(this, Color.PeachPuff, "007_cool");

            //short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };

            //int r1;

            //if (which_status == eAffliction.ASLEEP && (Record.Genus == eGenus.UNDEAD || Record.Genus == eGenus.SLIME || Record.Genus == eGenus.STONE))
            //{
            //    Game.AddMessage(String.Format("  {0} resists.", Name));
            //    return;
            //}
            //r1 = Maths.Rand(1, 0, 100);
            //if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
            //if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
            //r1 += penalty;
            //if (which_status == eAffliction.ASLEEP) r1 -= 25;
            //if (which_status == eAffliction.PARALYZED) r1 -= 15;
            //if (which_status == eAffliction.ASLEEP && Record.SpecialSkill == eCSS.BREATHES_SLEEP_CLOUDS)
            //    return;

            //if (r1 > charm_odds[Record.Level / 2])
            //{
            //    Game.AddMessage(String.Format("  {0} resists.", Name));
            //}
            //else
            //{
            //    if (which_status == eAffliction.NONE)
            //    {
            //        Attitude = eAttitude.FRIENDLY;
            //        Game.AddMessage(String.Format("  {0} is charmed.", Name));
            //        new Animation_CharFlash(this, Color.PeachPuff, "007_cool");
            //    }
            //    else
            //    {
            //        SetStatus(which_status, amount);
            //        if (which_status == eAffliction.ASLEEP)
            //        {
            //            Game.AddMessage(String.Format("  {0} falls asleep.", Name));
            //            new Animation_CharFlash(this, Color.MidnightBlue, "096_sleep");
            //        }
            //        else if (which_status == eAffliction.PARALYZED)
            //        {
            //            Game.AddMessage(String.Format("  {0} is paralyzed.", Name));
            //            new Animation_CharFlash(this, Color.Olive, "090_paralyze");
            //        }
            //    }
            //}
        }

        ////Amalgamation of monster_attack_pc and monster_attack_monster
        public void Attack(ICharacter target) {

            KeyHandler.FlushHitKey();
            new Action(eAction.NONE);
            eDamageType dam_type = eDamageType.WEAPON;
            PCType pc = target as PCType;
            NPC npc = target as NPC;

            // A peaceful monster won't attack
            if (AlliedWith(target))
                return;

            // Check sanctuary
            if (target.Status(eAffliction.INVISIBLE) > 0)
            {
                int r1 = Maths.Rand(1, 0, 100);
                if (r1 > hit_chance[Record.Level / 2])
                {
                    Game.AddMessage("  Can't find target!                 ");
                }
                return;
            }

            direction.FaceTowards(pos, target.Pos);

            for (int i = 0; i < 3; i++) //Repeat for number of attacks.
            {
                if (!target.IsAlive()) break;
                if (Record.AttackAmount[i] <= 0 || Record.AttackMultiplier[i] <= 0) continue;

                hasJustAttacked = true;
                Provocation += Constants.AI_ATTACK_PROVOCATION_SCORE + 1;

                // Attack roll
                int r1 = Maths.Rand(1, 0, 100)
                    - 5 * Math.Min(target is PCType ? 8 : 10, Status(eAffliction.BLESS_CURSE))
                        + 5 * target.Status(eAffliction.BLESS_CURSE)
                        + (target is PCType ? 5 * pc.GetSkillBonus(eSkill.DEXTERITY) : 0)
                        - 15;
                r1 += 5 * (Status(eAffliction.WEBS) / 3);
                if (target is PCType && pc.Parry < 100) r1 += 5 * pc.Parry;

                // Damage roll
                int r2 = Maths.Rand(Record.AttackMultiplier[i], 1, Record.AttackAmount[i])
                    + Math.Min(target is PCType ? 8 : 10, Status(eAffliction.BLESS_CURSE))
                    - target.Status(eAffliction.BLESS_CURSE)
                    + (target is PCType ? 1 : 2);

                if (target is PCType)
                {
                    if (Scenario.difficulty_adjust() > 2)
                        r2 = r2 * 2;
                    else if (Scenario.difficulty_adjust() == 2)
                        r2 = (r2 * 3) / 2;
                }

                if (target.Status(eAffliction.ASLEEP) > 0 || target.Status(eAffliction.PARALYZED) > 0)
                {
                    r1 -= 80;
                    r2 = r2 * 2;
                }

                // Check if hit, and do effects
                if (r1 <= hit_chance[(Record.Skill + 4) / 2])
                {
                    var aa = new Animation_Attack(this);

                    if (Record.Genus == eGenus.DEMON)
                        dam_type = eDamageType.DEMON;
                    if (Record.Genus == eGenus.UNDEAD)
                        dam_type = eDamageType.UNDEAD;

                    int store_hp = target.Health;

                    int type = (int)((i > 0) ? Record.Attack23Type : Record.Attack1Type);
                    string[] m = { "Hits", "Claws", "Bites", "Slimes", "Punches", "Stings", "Clubs", "Burns", "Harms", "Stabs" };
                    string x = "Whacks";
                    if ((int)type < m.Length) x = m[(int)type];
                    Game.AddMessage(String.Format("{0} {1} {2}:", Record.Name, x, target.Name));

                    if (target.Damage(this, r2, 0, dam_type) && store_hp - target.Health > 0 && target.IsAlive())
                    {


                        if (target.Status(eAffliction.MARTYRS_SHIELD) > 0)
                        {
                            Game.AddMessage("  Shares damage!                 ");
                            Damage(target as IExpRecipient, store_hp - target.Health, 0, eDamageType.MAGIC);
                        }

                        if (IsAlive())
                        {

                            //Poison
                            if (Record.Poison > 0 && i == 0) target.Poison(Record.Poison);

                            // Gremlin steals food (Only PCs have food to steal)
                            if (Record.SpecialSkill == eCSS.STEALS_FOOD && target is PCType && Party.Food > 0 && Maths.Rand(1, 0, 2) < 2)
                            {
                                Game.AddMessage("  Steals food!                 ");
                                Sound.Play(26);
                                Party.Food -= Maths.Rand(1, 0, 10) - 10;
                            }

                            // Disease
                            else if (Record.SpecialSkill == eCSS.DISEASE_TOUCH && Maths.Rand(1, 0, 2) < 2)
                            {
                                Game.AddMessage("  Causes disease!                 ");
                                target.Disease(6);
                            }

                            // Undead xp drain
                            else if ((Record.SpecialSkill == eCSS.XP_DRAINING_TOUCH || Record.SpecialSkill == eCSS.ICY_AND_DRAINING_TOUCH)
                                && (target is PCType && pc.HasItemEquippedWithAbility(eItemAbil.LIFE_SAVING) == null))
                            {
                                Game.AddMessage("  Drains life!                 ");
                                pc.AwardXP(-((Record.Level * 3) / 2));
                            }

                            // Undead slow
                            else if (Record.SpecialSkill == eCSS.SLOWING_TOUCH && Maths.Rand(1, 0, 8) < 6
                                && (target is NPC || pc.HasItemEquippedWithAbility(eItemAbil.LIFE_SAVING) == null))
                            {
                                Game.AddMessage("  Stuns! ");
                                target.Slow(2);
                            }

                            // Dumbfound target (This should affect npcs too, eh eh?)
                            else if (Record.SpecialSkill == eCSS.DUMBFOUNDING_TOUCH)
                            {
                                Game.AddMessage("  Dumbfounds! ");
                                target.Dumbfound(2);
                            }

                            // Web target
                            else if (Record.SpecialSkill == eCSS.WEB_TOUCH)
                            {
                                Game.AddMessage("  Webs!                    ");
                                target.Web(target is PCType ? 5 : 4);
                                //Monsters web 4
                            }

                            // Sleep target
                            else if (Record.SpecialSkill == eCSS.SLEEP_TOUCH)
                            {
                                Game.AddMessage("  Sleeps!                    ");
                                target.Sleep(6, -15);// Charm(6, eAffliction.ASLEEP, -15);
                            }

                            // Paralyze target
                            else if (Record.SpecialSkill == eCSS.PARALYSIS_TOUCH)
                            {
                                Game.AddMessage("  Paralysis touch!                    ");
                                target.Paralyze(500, -5);//.Charm(500, eAffliction.PARALYZED, -5);
                            }

                            // Acid touch
                            else if (Record.SpecialSkill == eCSS.ACID_TOUCH)
                            {
                                Game.AddMessage("  Acid touch!      ");
                                if (target is PCType) target.Acid((Record.Level > 20) ? 4 : 2);
                                else target.Acid(3);
                            }

                            // Freezing touch
                            else if ((Record.SpecialSkill == eCSS.ICY_TOUCH || Record.SpecialSkill == eCSS.ICY_AND_DRAINING_TOUCH)
                                && Maths.Rand(1, 0, 8) < 6 && (target is NPC || pc.HasItemEquippedWithAbility(eItemAbil.LIFE_SAVING) == null))
                            {
                                new Animation_Hold();
                                Game.AddMessage("  Freezing touch!");
                                r1 = Maths.Rand(3, 1, 10);
                                target.Damage(this, r1, 0, eDamageType.COLD);
                            }

                            // Killing touch
                            else if (Record.SpecialSkill == eCSS.DEATH_TOUCH) //&& (Maths.get_ran(1, 0, 8) < 6)) 
                            {
                                new Animation_Hold();
                                Game.AddMessage("  Killing touch!");
                                r1 = Maths.Rand(20, 1, 10);
                                target.Damage(this, r1, 0, eDamageType.UNBLOCKABLE);
                            }

                            // Petrification touch
                            else if (Record.SpecialSkill == eCSS.PETRIFYING_TOUCH && target is PCType && Maths.Rand(1, 0, 8) < 3)
                            {
                                Game.AddMessage("  Petrifying touch!");
                                pc.Kill(this, eLifeStatus.STONE);
                            }
                        }
                    }
                    else
                    {
                        Game.AddMessage("  No damage.");
                        aa.SetSound("002_swordswish");
                    }
                }
                else
                {
                    Game.AddMessage(String.Format("{0} misses {1}:", Record.Name, target.Name));
                    new Animation_Attack(this, "002_swordswish");
                }
                LastAttacked = target; //Save who we just attacked for last time - used for working out who we might target in future

                new Animation_Hold();
            }

        }

        public void ForceWallMe(IExpRecipient perp) { if (Record.Radiate != eRadiate.SHOCK) Damage(perp, Maths.Rand(3, 1, 6), 0, eDamageType.MAGIC); }
        public void FireWallMe(IExpRecipient perp) { if (Record.Radiate != eRadiate.FIRE) Damage(perp, Maths.Rand(2, 1, 6), 0, eDamageType.FIRE); }
        public void IceWallMe(IExpRecipient perp) { if (Record.Radiate != eRadiate.ICE) Damage(perp, Maths.Rand(3, 1, 6), 0, eDamageType.COLD); }
        public void BladeWallMe(IExpRecipient perp) { Damage(perp, Maths.Rand(6, 1, 8), 0, eDamageType.WEAPON); }
        public void StinkCloudMe() { if (Record.Radiate != eRadiate.STINK) Curse(Maths.Rand(1, 1, 2)); }
        public void SleepCloudMe() { if (Record.Radiate != eRadiate.SLEEP) Sleep(3, 0); }
        public void QuickfireMe() { if (Record.Radiate != eRadiate.FIRE) Damage(null, Maths.Rand(2, 1, 8), 0, eDamageType.FIRE); }
        public void FireBarrierMe() { if (Record.Radiate != eRadiate.FIRE) Damage(null, Maths.Rand(2, 1, 10), 0, eDamageType.FIRE); }
        public void WebSpaceMe() { if (Record.SpecialSkill != eCSS.SHOOTS_WEB) Web(3);}

        public void AwardXP(int amount)
        {
            //Do nothing - NPCs don't gain experience.
        }

        ////level = spec_skill
        public void FireMissile()//int bless, eCSS level, Location source, object target)
        //    //short target; // 100 +  - monster is target
        {
            hasJustAttacked = true; //Set this if monster targets a specific PC!
            KeyHandler.FlushHitKey();
            new Action(eAction.NONE);

            //CreatureInstance m_target = null;
            //PCType pc_target = null;
            int r1;//, r2, i;
            int[] dam = {0,1,2,3,4, 6,8,7,0,0, 0,0,0,0,0, 0,0,0,0,0,
            8,0,0,0,0, 0,0,0,0,0, 0,0,0,0,6, 0,0,0,0,0};
            //Location targ_space;

            switch (Record.SpecialSkill)
            {

            case eCSS.BREATHES_SLEEP_CLOUDS:
             // sleep cloud
                Game.AddMessage("Creature breathes.");               
                //Gfx.run_a_missile(source, Target.Pos, 0, 0, 44, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 0, false, "044_breathe");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Radius2, Target.Pos, Field.SLEEP_CLOUD, this);
                break;
            case eCSS.BREATHES_STINKING_CLOUDS:
             // vapors

                Game.AddMessage(String.Format("  Breathes on {0}.", Target.Name));
                //Gfx.run_a_missile(source, Target.Pos, 12, 0, 44,
                //    0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 12, false, "044_breathe");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Single, Target.Pos, Field.STINK_CLOUD, this);
                break;
            case eCSS.SHOOTS_WEB:
             // webs
                Game.AddMessage(String.Format("  Throws web at {0}.", Target.Name));
                //Gfx.run_a_missile(source, Target.Pos, 8, 0, 14,
                //    0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 8, false, "014_missile");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Single, Target.Pos, Field.WEB, this);
                break;
            case eCSS.PARALYSIS_RAY:
             // paral
                Sound.Play(51);
                Game.AddMessage(String.Format("  Fires ray at {0}.", Target.Name));
                Target.Paralyze(100, 0);//.Charm(100, eAffliction.PARALYZED, 0);
                break;
            case eCSS.PETRIFICATION_RAY:
             // petrify
                //Gfx.run_a_missile(source, Target.Pos, 14, 0, 43, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 14, false, "043_stoning");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Gazes at {0}.", Target.Name));
                r1 = Maths.Rand(1, 0, 20) + Target.Level / 4 + Target.Status(eAffliction.BLESS_CURSE);
                if (r1 > 14)
                    Game.AddMessage(String.Format("  {0} resists.", Target.Name));
                else
                    Target.Kill(this, eLifeStatus.STONE);
                break;
            case eCSS.SP_DRAIN_RAY:
             // Drain sp
                //Gfx.run_a_missile(source, Target.Pos, 8, 0, 43, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 8, false, "043_stoning");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Drains {0}.", Target.Name));
                Target.SP /= 2;
                break;
            case eCSS.HEAT_RAY:
             // heat ray
                //Gfx.run_a_missile(source, Target.Pos, 13, 0, 51, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 13, false, "051_magic1");
                new Animation_Hold();
                r1 = Maths.Rand(7, 1, 6);
                //store_missile_type.start_missile_anim();
                Game.AddMessage(String.Format("  Hits {0} with heat ray.", Target.Name));
                if (Target.Damage(this, r1, 0, eDamageType.FIRE)) new Animation_Hold();
          
                //Gfx.do_explosion_anim(5, 0);
                //store_missile_type.end_missile_anim();
                //BoE.CurTown.handle_marked_damage();
                break;
            case eCSS.ACID_SPIT:
             // acid spit
                //Gfx.run_a_missile(source, Target.Pos, 0, 1, 64, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 0, true, "064_spit");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Spits acid on {0}.", Target.Name));
                Target.Acid(6);
                break;
            case eCSS.THROWS_DARTS:
            case eCSS.SHOOTS_ARROWS:
            case eCSS.GOOD_ARCHER:
                //Gfx.run_a_missile(source, Target.Pos, 3, 1, 12, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 3, true, "012_longbow");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Shoots at {0}.", Target.Name));
                break;
            case eCSS.THROWS_SPEARS:
                //Gfx.run_a_missile(source, Target.Pos, 5, 1, 14, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 5, true, "014_missile");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Throws spear at {0}.", Target.Name));
                break;
            case eCSS.THROWS_RAZORDISKS:
                //Gfx.run_a_missile(source, Target.Pos, 7, 1, 14, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 7, true, "014_missile");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Throws razordisk at {0}.", Target.Name));
                break;
            case eCSS.SHOOTS_SPINES:
                //Gfx.run_a_missile(source, Target.Pos, 5, 1, 14, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 5, true, "014_missile");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Fires spines at {0}.", Target.Name));
                break;
            default://rock throwing
                //Gfx.run_a_missile(source, Target.Pos, 12, 1, 14, 0, 0, 100);
                new Animation_Missile(Pos, Target.Pos, 12, true, "014_missile");
                new Animation_Hold();
                Game.AddMessage(String.Format("  Throws rock at {0}.", Target.Name));
                break;
            }

            // Check sanctuary
            if (Target.Status(eAffliction.INVISIBLE) > 0)
            {
                if (Maths.Rand(1, 0, 100) > hit_chance[(int)Record.SpecialSkill])
                    Game.AddMessage("  Can't find target!");
                return;
            }

            r1 = Maths.Rand(1, 0, 100) - 5 * Maths.Min(10, Status(eAffliction.BLESS_CURSE)) + 5 * Target.Status(eAffliction.BLESS_CURSE)
                - 5 * (curTown.CanSee(Pos, Target.Pos));
            
            if (Target is PCType && ((PCType)Target).Parry < 100)
                r1 += 5 * ((PCType)Target).Parry;
            int r2 = Maths.Rand(dam[(int)Record.SpecialSkill], 1, 7) + Math.Min(10, Status(eAffliction.BLESS_CURSE));

            if (r1 <= hit_chance[dam[(int)Record.SpecialSkill] * 2])
            {
                if (Target.Damage(this, r2, 0, eDamageType.WEAPON, eDamageType.WEAPON, "098_missilehit")) new Animation_Hold();
            }
            else
            {
                Game.AddMessage(String.Format("  Misses {0}.", Target.Name));
            }
        }

        class NPCMageSpell
        {
            public int Cost, AreaEffect;
            public string Name;

            public static NPCMageSpell Spark = new NPCMageSpell { Cost = 1, AreaEffect = 0, Name = "Spark" };
            public static NPCMageSpell MinorHaste = new NPCMageSpell { Cost = 1, AreaEffect = 0, Name = "Minor Haste" };
            public static NPCMageSpell Strength = new NPCMageSpell { Cost = 1, AreaEffect = 0, Name = "Strength" };
            public static NPCMageSpell FlameCloud = new NPCMageSpell { Cost = 1, AreaEffect = 0, Name = "Flame Cloud" };
            public static NPCMageSpell Flame = new NPCMageSpell { Cost = 2, AreaEffect = 0, Name = "Flame" };
            public static NPCMageSpell MinorPoison = new NPCMageSpell { Cost = 2, AreaEffect = 0, Name = "Minor Poison" };
            public static NPCMageSpell Slow = new NPCMageSpell { Cost = 2, AreaEffect = 0, Name = "Slow" };
            public static NPCMageSpell Dumbfound = new NPCMageSpell { Cost = 2, AreaEffect = 0, Name = "Dumbfound" };
            public static NPCMageSpell StinkingCloud = new NPCMageSpell { Cost = 2, AreaEffect = 1, Name = "Stinking Cloud" };
            public static NPCMageSpell SummonBeast = new NPCMageSpell { Cost = 4, AreaEffect = 0, Name = "Summon Beast" };
            public static NPCMageSpell Conflagration = new NPCMageSpell { Cost = 2, AreaEffect = 1, Name = "Conflagration" };
            public static NPCMageSpell Fireball = new NPCMageSpell { Cost = 4, AreaEffect = 1, Name = "Fireball" };
            public static NPCMageSpell WeakSummoning = new NPCMageSpell { Cost = 4, AreaEffect = 0, Name = "Weak Summoning" };
            public static NPCMageSpell Web = new NPCMageSpell { Cost = 3, AreaEffect = 1, Name = "Web" };
            public static NPCMageSpell Poison = new NPCMageSpell { Cost = 4, AreaEffect = 0, Name = "Poison" };
            public static NPCMageSpell IceBolt = new NPCMageSpell { Cost = 4, AreaEffect = 0, Name = "Ice Bolt" };
            public static NPCMageSpell SlowGroup = new NPCMageSpell { Cost = 4, AreaEffect = 0, Name = "Slow Group" };
            public static NPCMageSpell MajorHaste = new NPCMageSpell { Cost = 5, AreaEffect = 0, Name = "Major Haste" };
            public static NPCMageSpell Firestorm = new NPCMageSpell { Cost = 5, AreaEffect = 1, Name = "Firestorm" };
            public static NPCMageSpell Summoning = new NPCMageSpell { Cost = 5, AreaEffect = 0, Name = "Summoning" };
            public static NPCMageSpell Shockstorm = new NPCMageSpell { Cost = 5, AreaEffect = 1, Name = "Shockstorm" };
            public static NPCMageSpell MajorPoison = new NPCMageSpell { Cost = 6, AreaEffect = 0, Name = "Major Poison" };
            public static NPCMageSpell Kill = new NPCMageSpell { Cost = 6, AreaEffect = 0, Name = "Kill" };
            public static NPCMageSpell Daemon = new NPCMageSpell { Cost = 6, AreaEffect = 0, Name = "Daemon" };
            public static NPCMageSpell MajorBlessing = new NPCMageSpell { Cost = 7, AreaEffect = 0, Name = "Major Blessing" };
            public static NPCMageSpell MajorSummoning = new NPCMageSpell { Cost = 7, AreaEffect = 0, Name = "Major Summoning" };
            public static NPCMageSpell Shockwave = new NPCMageSpell { Cost = 7, AreaEffect = 0, Name = "Shockwave" };
        }

        class NPCPriestSpell
        {
            public int Cost, AreaEffect;
            public string Name;

            public static NPCPriestSpell MinorBless = new NPCPriestSpell { Cost = 1, AreaEffect = 0, Name = "Minor Bless"};
            public static NPCPriestSpell LightHeal = new NPCPriestSpell { Cost = 1, AreaEffect = 0, Name = " Light Heal"};
            public static NPCPriestSpell Wrack = new NPCPriestSpell { Cost = 1, AreaEffect = 0, Name = "Wrack"};
            public static NPCPriestSpell Stumble = new NPCPriestSpell { Cost = 1, AreaEffect = 0, Name = "Stumble"};
            public static NPCPriestSpell Bless = new NPCPriestSpell { Cost = 2, AreaEffect = 0, Name = "Bless"};
            public static NPCPriestSpell Curse = new NPCPriestSpell { Cost = 2, AreaEffect = 0, Name = "Curse"};
            public static NPCPriestSpell Wound = new NPCPriestSpell { Cost = 2, AreaEffect = 0, Name = "Wound"};
            public static NPCPriestSpell SummonSpirit = new NPCPriestSpell { Cost = 4, AreaEffect = 0, Name = "Summon Spirit"};
            public static NPCPriestSpell Disease = new NPCPriestSpell { Cost = 2, AreaEffect = 0, Name = "Disease"};
            public static NPCPriestSpell Heal = new NPCPriestSpell { Cost = 3, AreaEffect = 0, Name = "Heal"};
            public static NPCPriestSpell HolyScourge = new NPCPriestSpell { Cost = 3, AreaEffect = 0, Name = "Holy Scourge"};
            public static NPCPriestSpell Smite = new NPCPriestSpell { Cost = 3, AreaEffect = 0, Name = "Smite"};
            public static NPCPriestSpell CurseAll = new NPCPriestSpell { Cost = 4, AreaEffect = 0, Name = "Curse All"};
            public static NPCPriestSpell SticksToSnakes = new NPCPriestSpell { Cost = 4, AreaEffect = 0, Name = "Sticks to Snakes"};
            public static NPCPriestSpell MartyrsShield = new NPCPriestSpell { Cost = 4, AreaEffect = 0, Name = "Martyr's Shield"};
            public static NPCPriestSpell BlessAll = new NPCPriestSpell { Cost = 5, AreaEffect = 0, Name = "Bless All"};
            public static NPCPriestSpell MajorHeal = new NPCPriestSpell { Cost = 5, AreaEffect = 0, Name = "Major Heal"};
            public static NPCPriestSpell Flamestrike = new NPCPriestSpell { Cost = 5, AreaEffect = 1, Name = "Flamestrike"};
            public static NPCPriestSpell SummonHost = new NPCPriestSpell { Cost = 10, AreaEffect = 0, Name = "Summon Host"};
            public static NPCPriestSpell ReviveSelf = new NPCPriestSpell { Cost = 6, AreaEffect = 0, Name = "Revive Self"};
            public static NPCPriestSpell UnholyRavaging = new NPCPriestSpell { Cost = 6, AreaEffect = 0, Name = "Unholy Ravaging"};
            public static NPCPriestSpell SummonGuardian = new NPCPriestSpell { Cost = 10, AreaEffect = 0, Name = "Summon Guardian"};
            public static NPCPriestSpell Pestilence = new NPCPriestSpell { Cost = 8, AreaEffect = 0, Name = "Pestilence"};
            public static NPCPriestSpell ReviveAll = new NPCPriestSpell { Cost = 8, AreaEffect = 0, Name = "Revive All"};
            public static NPCPriestSpell Avatar = new NPCPriestSpell { Cost = 8, AreaEffect = 0, Name = "Avatar"};
            public static NPCPriestSpell DivineThud = new NPCPriestSpell { Cost = 8, AreaEffect = 1, Name = "Divine Thud"};
        }

        NPCMageSpell selectMageSpell(out Location target_pos, out ICharacter target_char)
        {
            int target_levels = 0, friend_levels_near;
            NPCMageSpell spell;// = eMMageSpells.NO_SPELL;

            target_pos = new Location(-1,-1);
            target_char = null;

            //int[] monst_mage_cost = { 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 2, 4, 4, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7 };
            //int[] monst_mage_area_effect = { 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 };
            //string[] m_mage_sp = {"Spark","Minor Haste","Strength","Flame Cloud","Flame",
            //                            "Minor Poison","Slow","Dumbfound","Stinking Cloud","Summon Beast",
            //                            "Conflagration","Fireball","Weak Summoning","Web","Poison",
            //                            "Ice Bolt","Slow Group","Major Haste","Firestorm","Summoning",
            //                            "Shockstorm","Major Poison","Kill","Daemon","Major Blessing",
            //                            "Major Summoning","Shockwave"};

            NPCMageSpell[,] caster_array = {//mage level 1 (spark, minor haste, strength, flame cloud)
                                        {NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.MinorHaste,
                                        NPCMageSpell.MinorHaste, NPCMageSpell.MinorHaste,NPCMageSpell.Spark ,
                                        NPCMageSpell.Strength,NPCMageSpell.FlameCloud,NPCMageSpell.FlameCloud,
                                        NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.MinorHaste,
                                        NPCMageSpell.MinorHaste, NPCMageSpell.MinorHaste,NPCMageSpell.Strength,NPCMageSpell.FlameCloud},
                                        //mage level 2 (flame, minor poison, slow, dumbfound, stinking cloud, summon beast, conflagration, minor haste)
                                        {NPCMageSpell.Flame,NPCMageSpell.Flame,NPCMageSpell.Flame,NPCMageSpell.MinorPoison,NPCMageSpell.Slow,
                                         NPCMageSpell.Dumbfound,NPCMageSpell.StinkingCloud,NPCMageSpell.SummonBeast,NPCMageSpell.Conflagration,
                                         NPCMageSpell.Conflagration, NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,
                                         NPCMageSpell.Flame,NPCMageSpell.Slow, NPCMageSpell.SummonBeast,NPCMageSpell.SummonBeast,NPCMageSpell.Flame},
                                        //mage level 3 (flame, minor haste, stinking cloud, conflagration, fireball, web, weak summoning)
                                        {NPCMageSpell.Flame,NPCMageSpell.Flame,NPCMageSpell.MinorHaste,NPCMageSpell.StinkingCloud,
                                        NPCMageSpell.Conflagration, NPCMageSpell.Fireball,NPCMageSpell.Fireball,NPCMageSpell.Fireball,
                                        NPCMageSpell.Web,NPCMageSpell.WeakSummoning, NPCMageSpell.WeakSummoning,NPCMageSpell.Fireball,
                                        NPCMageSpell.Fireball,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,
                                        NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste},
                                        //mage level 4 (poison, ice bolt, slow group, flame, fireball, weak summoning, minor haste)
                                        {NPCMageSpell.Poison,NPCMageSpell.Poison,NPCMageSpell.IceBolt,NPCMageSpell.SlowGroup,NPCMageSpell.SlowGroup,
                                        NPCMageSpell.Flame,NPCMageSpell.Fireball,NPCMageSpell.Fireball,NPCMageSpell.WeakSummoning,
                                        NPCMageSpell.WeakSummoning, NPCMageSpell.SlowGroup,NPCMageSpell.SlowGroup,NPCMageSpell.IceBolt,
                                        NPCMageSpell.SlowGroup,NPCMageSpell.IceBolt, NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste},
                                        //mage level 5 (poison, major haste, firestorm, summoning, shockstorm, ice bolt, slow group)
                                        {NPCMageSpell.Poison,NPCMageSpell.MajorHaste,NPCMageSpell.Firestorm,NPCMageSpell.Firestorm,
                                        NPCMageSpell.Summoning, NPCMageSpell.Summoning,NPCMageSpell.Shockstorm,NPCMageSpell.Shockstorm,NPCMageSpell.IceBolt,
                                        NPCMageSpell.SlowGroup, NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,
                                        NPCMageSpell.Firestorm, NPCMageSpell.Firestorm,NPCMageSpell.Firestorm,NPCMageSpell.Summoning},
                                        //mage level 6 (kill, major poison, shockstorm, summoning, daemon, firestorm, major haste)
                                        {NPCMageSpell.Kill,NPCMageSpell.Kill,NPCMageSpell.MajorPoison,NPCMageSpell.MajorPoison,NPCMageSpell.Shockstorm,
                                         NPCMageSpell.Shockstorm,NPCMageSpell.Summoning,NPCMageSpell.Daemon,NPCMageSpell.Firestorm,NPCMageSpell.MajorHaste,
                                         NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,
                                         NPCMageSpell.Kill,NPCMageSpell.Kill,NPCMageSpell.Firestorm},
                                         //mage level 7 (kill, daemon, major blessing, major haste, , major summoning, shockwave, major poison, firestorm )
                                        {NPCMageSpell.Kill,NPCMageSpell.Kill,NPCMageSpell.Daemon,NPCMageSpell.MajorBlessing,
                                        NPCMageSpell.MajorSummoning, NPCMageSpell.Shockwave,NPCMageSpell.Firestorm,NPCMageSpell.MajorPoison,
                                        NPCMageSpell.Firestorm,NPCMageSpell.MajorHaste, NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,
                                        NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorSummoning,
                                        NPCMageSpell.Daemon,NPCMageSpell.Daemon,NPCMageSpell.Kill}
                                        };

            NPCMageSpell[,] emer_spells = { //emergency spells level 1 (minor haste, flame)
                                        {NPCMageSpell.MinorHaste,null,null,NPCMageSpell.Flame},
                                        //emergency spells level 2 (minor haste, summon beast, conflagration slow)
                                        {NPCMageSpell.MinorHaste,NPCMageSpell.SummonBeast,NPCMageSpell.Conflagration,NPCMageSpell.Slow},
                                        //emergency spells level 3 (minor haste, weak summoning, fireball)
                                        {NPCMageSpell.MinorHaste,NPCMageSpell.WeakSummoning,NPCMageSpell.Fireball,NPCMageSpell.WeakSummoning},
                                        //emergency spells level 4 (minor haste, weak summoning, fireball) (same as level 3)
                                        {NPCMageSpell.MinorHaste,NPCMageSpell.WeakSummoning,NPCMageSpell.Fireball,NPCMageSpell.WeakSummoning},
                                        //emergency spells level 5 (major haste, summoning, firestorm)
                                        {NPCMageSpell.MajorHaste,NPCMageSpell.Summoning,NPCMageSpell.Firestorm,NPCMageSpell.MajorHaste},
                                        //emergency spells level 6 (major haste, daemon, firestorm)
                                        {NPCMageSpell.MajorHaste,NPCMageSpell.Daemon,NPCMageSpell.Firestorm,NPCMageSpell.Daemon},
                                        //emergency spells level 7 (major haste, major summoning, firestorm, shockwave)
                                        {NPCMageSpell.MajorHaste,NPCMageSpell.MajorSummoning,NPCMageSpell.Firestorm,NPCMageSpell.Shockwave}};

            if (curTown.FieldThere(Pos, Field.ANTIMAGIC)) return null;

            //Find the Caster's spell level for this spell
            int level = Maths.Max(1, Record.MageLevel - Status(eAffliction.DUMB)) - 1;

            target_pos = curTown.FindSpellTargetPosition(Pos, 1, ref target_levels, this);//ter.find_fireball_loc(Pos, 1, (Attitude % 2 == 1) ? 0 : 1, ref target_levels);
            target_char = Target;

            friend_levels_near = -1 * curTown.CountLevels(Pos, 3, this);//(Attitude % 2 != 1) ? town.count_levels(Pos, 3) : -1 * town.count_levels(Pos, 3);

            //Less than a quarter health remaining -  maybe cast emergency defensive spell
            if (Health * 4 < Record.Health && Maths.Rand(1, 0, 10) < 9)
                spell = emer_spells[level, 3];

            //Or caster has been slowed, maybe cast emergency haste spell
            else if (((Status(eAffliction.HASTE_SLOW) < 0 && Maths.Rand(1, 0, 10) < 7)
                  || (Status(eAffliction.HASTE_SLOW) == 0 && Maths.Rand(1, 0, 10) < 5))
                  && emer_spells[level, 0] != null)
                spell = emer_spells[level, 0];

            //OR no allies nearby, maybe cast emergency summoning spell
            else if (friend_levels_near <= -10 && Maths.Rand(1, 0, 10) < 7 && emer_spells[level, 1] != null)
                spell = emer_spells[level, 1];

            //If a high score on the target spot we've selected, maybe cast emergency area damage spell
            else if (target_levels > 50 && Maths.Rand(1, 0, 10) < 7 && emer_spells[level, 2] != null)
                spell = emer_spells[level, 2];

            //Otherwise choose a spell at random from the spell pool for this level
            else
            {
                int r1 = Maths.Rand(1, 0, 17);
                spell = caster_array[level, r1];
            }

            // Hastes happen often now, but don't cast them redundantly
            if (Status(eAffliction.HASTE_SLOW) > 0 && (spell == NPCMageSpell.MinorHaste || spell == NPCMageSpell.MajorHaste))
                spell = emer_spells[level, 3];

            // Anything preventing spell?
            if (target_pos.X == -1 && spell.AreaEffect > 0)
            {
                int r1 = Maths.Rand(1, 0, 9);
                spell = caster_array[level, r1];
                if (target_pos.X == -1 && spell.AreaEffect > 0)
                    return null;
            }
            if (spell.AreaEffect > 0) target_char = null;

            if (target_char == null)
            {
                if (curTown.FieldThere(target_pos, Field.ANTIMAGIC)) return null;// false;
            }
            else
                if (curTown.FieldThere(target_char.Pos, Field.ANTIMAGIC)) return null;// false;

            // How about shockwave? Good idea?
            if (spell == NPCMageSpell.Shockwave && !IsABaddie)
                spell = NPCMageSpell.MajorSummoning;
            if (spell == NPCMageSpell.Shockwave && IsABaddie && curTown.CountLevels(Pos, 10, this) < 45)
                spell = NPCMageSpell.MajorSummoning;

            if (SP < spell.Cost) return null;

            return spell;
        }

        NPCPriestSpell selectPriestSpell(out Location target_pos, out ICharacter target_char)
        {
            NPCPriestSpell spell = null;
            target_pos = Location.Zero;
            target_char = null;

            NPCPriestSpell[,] caster_array = {   //priest level 1 (minor bless, wrack, stumble)
                                        {NPCPriestSpell.MinorBless,NPCPriestSpell.MinorBless,NPCPriestSpell.MinorBless,
                                        NPCPriestSpell.MinorBless,NPCPriestSpell.Wrack,NPCPriestSpell.Wrack,NPCPriestSpell.Wrack,
                                        NPCPriestSpell.Stumble,NPCPriestSpell.Stumble,NPCPriestSpell.Stumble},
                                        //priest level 2 (bless, curse, wound, summon spirit, disease)
                                        {NPCPriestSpell.Bless,NPCPriestSpell.Bless,NPCPriestSpell.Curse,NPCPriestSpell.Curse,
                                        NPCPriestSpell.Wound,NPCPriestSpell.Wound,NPCPriestSpell.SummonSpirit,
                                        NPCPriestSpell.SummonSpirit,NPCPriestSpell.SummonSpirit,NPCPriestSpell.Disease},
                                        //priest level 3 (disease, curse, holy scourge, smite, )
                                        {NPCPriestSpell.Disease,NPCPriestSpell.Curse,NPCPriestSpell.Curse,
                                        NPCPriestSpell.SummonSpirit,NPCPriestSpell.HolyScourge,NPCPriestSpell.Smite,NPCPriestSpell.Smite,
                                        NPCPriestSpell.Bless,NPCPriestSpell.Bless,NPCPriestSpell.Smite},
                                        //priest level 4 (smite, curse all, sticks to snake, disease, martyr's shield)
                                        {NPCPriestSpell.Smite,NPCPriestSpell.Smite,NPCPriestSpell.CurseAll,NPCPriestSpell.CurseAll,
                                        NPCPriestSpell.SticksToSnakes,NPCPriestSpell.Disease,NPCPriestSpell.Disease,
                                        NPCPriestSpell.SticksToSnakes,NPCPriestSpell.SticksToSnakes,NPCPriestSpell.MartyrsShield},
                                        //priest level 5 (summon host, flamestrike, curse all, martyr's shield, bless all)
                                        {NPCPriestSpell.SummonHost,NPCPriestSpell.Flamestrike,NPCPriestSpell.CurseAll,NPCPriestSpell.SummonHost,
                                        NPCPriestSpell.MartyrsShield,NPCPriestSpell.Flamestrike,NPCPriestSpell.Flamestrike,
                                        NPCPriestSpell.SummonHost,NPCPriestSpell.BlessAll,NPCPriestSpell.Flamestrike},
                                        //priest level 6 (summon guardian, flamestrike, bless all, summon host, unholy ravaging, pestilence)
                                        {NPCPriestSpell.SummonGuardian,NPCPriestSpell.Flamestrike,NPCPriestSpell.BlessAll,
                                        NPCPriestSpell.SummonHost,NPCPriestSpell.Flamestrike,NPCPriestSpell.Flamestrike,NPCPriestSpell.UnholyRavaging,
                                        NPCPriestSpell.SummonGuardian,NPCPriestSpell.Pestilence,NPCPriestSpell.Pestilence},
                                        //priest level 7 (divine thud, avatar, revive all, summon guardian)
                                        {NPCPriestSpell.DivineThud,NPCPriestSpell.DivineThud,NPCPriestSpell.Avatar,NPCPriestSpell.ReviveAll,
                                        NPCPriestSpell.DivineThud,	NPCPriestSpell.SummonGuardian,NPCPriestSpell.ReviveAll,NPCPriestSpell.SummonGuardian,
                                        NPCPriestSpell.DivineThud,NPCPriestSpell.Avatar}};
            NPCPriestSpell[,] emer_spells = { //emergency spells level 1 (minor bless, light heal)
                                        {null,NPCPriestSpell.MinorBless,null,NPCPriestSpell.LightHeal},
                                        //emergency spells level 2 (summon spirit, light heal)
                                        {null,NPCPriestSpell.SummonSpirit,null,NPCPriestSpell.LightHeal},
                                        //emergency spells level 3 (summon spirit, heal)
                                        {null,NPCPriestSpell.SummonSpirit,null,NPCPriestSpell.Heal},
                                        //emergency spells level 4 (sticks to snakes, heal)
                                        {null,NPCPriestSpell.SticksToSnakes,null,NPCPriestSpell.Heal},
                                        //emergency spells level 5 (summon host, flamestrike, major heal)
                                        {null,NPCPriestSpell.SummonHost,NPCPriestSpell.Flamestrike,NPCPriestSpell.MajorHeal},
                                        //emergency spells level 6 (summon host, flamestrike, full heal)
                                        {null,NPCPriestSpell.SummonHost,NPCPriestSpell.Flamestrike,NPCPriestSpell.ReviveSelf},
                                        //emergency spells level 7 (avatar, divine thud, revive all)
                                        {NPCPriestSpell.Avatar,NPCPriestSpell.Avatar,NPCPriestSpell.DivineThud,NPCPriestSpell.ReviveAll}};

            if (curTown.FieldThere(Pos, Field.ANTIMAGIC)) return null;

            int level = Maths.Max(1, Record.PriestLevel - Status(eAffliction.DUMB)) - 1;

            int target_levels = 0;
            target_pos = curTown.FindSpellTargetPosition(Pos, 1, ref target_levels, this);
            int friend_levels_near = -1 * curTown.CountLevels(Pos, 3, this);

            if ((Health * 4 < Record.Health) && (Maths.Rand(1, 0, 10) < 9))
                spell = emer_spells[level, 3];
            else if ((Status(eAffliction.HASTE_SLOW) < 0) && (Maths.Rand(1, 0, 10) < 7) && (emer_spells[level, 0] != null))
                spell = emer_spells[level, 0];
            else if ((friend_levels_near <= -10) && (Maths.Rand(1, 0, 10) < 7) && (emer_spells[level, 1] != null))
                spell = emer_spells[level, 1];
            else if ((target_levels > 50) && (Maths.Rand(1, 0, 10) < 7) && (emer_spells[level, 2] != null))
                spell = emer_spells[level, 2];
            else
                spell = caster_array[level, Maths.Rand(1, 0, 9)];

            // Anything preventing spell?
            if (target_pos.X == -1 && spell.AreaEffect > 0)
            {
                int r1 = Maths.Rand(1, 0, 9);
                spell = caster_array[level, r1];
                if (target_pos.X == -1 && spell.AreaEffect > 0)
                    return null;
            }

            target_char = Target;

            if (spell.AreaEffect > 0) target_char = null;

            if (target_char == null && curTown.FieldThere(target_pos, Field.ANTIMAGIC)) return null;
            if (target_char != null && curTown.FieldThere(target_char.Pos, Field.ANTIMAGIC)) return null;

            // snuff heals if unwounded
            if (Health == Record.Health && (spell == NPCPriestSpell.MajorHeal || spell == NPCPriestSpell.ReviveSelf || spell == NPCPriestSpell.LightHeal || spell == NPCPriestSpell.Heal))
                return null;

            if (SP < spell.Cost) return null;
            else return spell;
        }
         
        void castMageSpell(NPCMageSpell spell, Location target, ICharacter targc)//object targ) {
        {
            KeyHandler.FlushHitKey();
            new Action(eAction.NONE);
            hasJustAttacked = true; //Set this if monster targets a specific PC!

            int i, j=0;
            Location l = Pos;
            if (Dir.IsFacingRight && Record.Width > 1) l.X++;

            Game.AddMessage(String.Format("{0} casts: {1}", Record.Name, spell.Name));//m_mage_sp[(int)spell - 1]));

            SP -= spell.Cost;//monst_mage_cost[(int)spell - 1];

            if (spell == NPCMageSpell.Spark)
            {
                new Animation_Missile(l, targc.Pos, 6, true, "011_3booms");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(2, 1, 4), 0, eDamageType.FIRE)) new Animation_Hold();
            }
            else if (spell == NPCMageSpell.MinorHaste){ // minor haste
                Haste(2);
            }
            else if (spell == NPCMageSpell.Strength)
            { // strength
                Bless(3);
            }
            else if (spell == NPCMageSpell.FlameCloud)
            { // flame cloud
                new Animation_Missile(l, targc.Pos, 2, true, "011_3booms");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Single, targc.Pos, Field.FIRE_WALL, this);
            }
            else if (spell == NPCMageSpell.Flame)
            { // flame
                new Animation_Missile(l, targc.Pos, 2, true, "011_3booms");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(Record.Level, 1, 4), 0, eDamageType.FIRE)) new Animation_Hold();
            }
            else if (spell == NPCMageSpell.MinorPoison)
            { // minor poison
                new Animation_Missile(l, targc.Pos, 11, false, "025_magespell");
                new Animation_Hold();
                targc.Poison(2 + Maths.Rand(1, 0, 1));
            }
            else if (spell == NPCMageSpell.Slow)
            { // slow
                new Animation_Missile(l, targc.Pos, 15, false, "025_magespell");
                new Animation_Hold();
                targc.Slow(2 + Record.Level / 2);
            }
            else if (spell == NPCMageSpell.Dumbfound)
            { // dumbfound
                new Animation_Missile(l, targc.Pos, 14, false, "025_magespell");
                new Animation_Hold();
                targc.Dumbfound(2);
            }
            else if (spell == NPCMageSpell.StinkingCloud)
            { // scloud
                new Animation_Missile(l, target, 0, false, "025_magespell");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Square, target, Field.STINK_CLOUD, this);
            }
            else if (spell == NPCMageSpell.SummonBeast)
            { // summon beast
                NPCRecord sum = NPCRecord.GetSummonMonster(1);
                if (sum != null)
                    //Delay(12,&dummy); // gives sound time to end
                    //Sound.Play(25);
                    //Sound.Play(-61);
                    curTown.SummonMonster(this, sum, Pos, (!IsABaddie ? 0 : 100) + Maths.Rand(3, 1, 4));
            }
            else if (spell == NPCMageSpell.Conflagration)
            { // conflagration
                new Animation_Missile(l, target, 13, true, "025_magespell");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Radius2, target, Field.FIRE_WALL, this);
            }
            else if (spell == NPCMageSpell.Fireball)
            { // fireball
                new Animation_Missile(l, target, 2, true, "011_3booms");
                new Animation_Hold();
                //store_missile_type.start_missile_anim();
                curTown.HitArea(target, Maths.Min(1 + (Record.Level * 3) / 4, 29),1,6, eDamageType.FIRE, Pattern.Square, true, this);
                new Animation_Hold();
            }
            else if (spell == NPCMageSpell.WeakSummoning || spell == NPCMageSpell.Summoning || spell == NPCMageSpell.MajorSummoning)
            {// summon
                //Sound.Play(25);
                NPCRecord sum = null;
                if (spell == NPCMageSpell.WeakSummoning)
                {
                    sum = NPCRecord.GetSummonMonster(1);
                    j = Maths.Rand(2, 1, 3) + 1;
                }
                if (spell == NPCMageSpell.Summoning)
                {
                    sum = NPCRecord.GetSummonMonster(2);
                    j = Maths.Rand(2, 1, 2) + 1;
                }
                if (spell == NPCMageSpell.MajorSummoning)
                {
                    sum = NPCRecord.GetSummonMonster(3);
                    j = Maths.Rand(1, 2, 3);
                }

                if (sum != null)
                {
                    for (i = 0; i < j; i++)
                    {
                        if (!curTown.SummonMonster(this, sum, Pos, (!IsABaddie ? 0 : 100) + Maths.Rand(4, 1, 4)))
                        {
                            Game.AddMessage("  Summon failed.");
                            break;
                        }
                    }
                }
            }
            else if (spell == NPCMageSpell.Web)
            { // web
                Sound.Play(25);
                curTown.PlaceFieldPattern(Pattern.Radius2, target, Field.WEB, this);
            }
            else if (spell == NPCMageSpell.Poison)
            { // poison
                new Animation_Missile(l, targc.Pos, 11, false, "025_magespell");
                new Animation_Hold();
                targc.Poison(4 + Maths.Rand(1, 0, 3));
            }
            else if (spell == NPCMageSpell.IceBolt)
            { // ice bolt
                new Animation_Missile(l, targc.Pos, 6, true, "011_3booms");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(5 + (Record.Level / 5), 1, 8), 0, eDamageType.COLD)) new Animation_Hold();
            }
            else if (spell == NPCMageSpell.SlowGroup)
            { // slow gp
                foreach (ICharacter ch in curTown.EachCharacterInRange(Pos, 7))
                {
                    if (!AlliedWith(ch))
                        ch.Slow(2 + Record.Level / 4, true);
                }
            }
            else if (spell == NPCMageSpell.MajorHaste)
            { // major haste
                foreach (ICharacter ch in curTown.EachCharacterInRange(Pos, 7))
                {
                    if (AlliedWith(ch))
                        ch.Haste(3);
                }
            }
            else if (spell == NPCMageSpell.Firestorm)
            { // firestorm
                new Animation_Missile(l, target, 1, true, "011_3booms");
                new Animation_Hold();
                curTown.HitArea(target, Maths.Min(1 + (Record.Level * 3) / 4 + 3, 29), 1,6, eDamageType.FIRE, Pattern.Radius2, true, this); new Animation_Hold();
            }
            else if (spell == NPCMageSpell.Shockstorm)
            { // shockstorm
                new Animation_Missile(l, target, 6, true, "011_3booms");
                new Animation_Hold();
                curTown.PlaceFieldPattern(Pattern.Radius2, target, Field.FORCE_WALL, this);
            }
            else if (spell == NPCMageSpell.MajorPoison)
            { // m. poison
                new Animation_Missile(l, targc.Pos, 11, true, "011_3booms");
                new Animation_Hold();
                targc.Poison(6 + Maths.Rand(1, 1, 2));
            }
            else if (spell == NPCMageSpell.Kill)
            { // kill!!!
                new Animation_Missile(l, targc.Pos, 9, true, "011_3booms");
                new Animation_Hold();
                if (targc.Damage(this, 35 + Maths.Rand(3, 1, 10), 0, eDamageType.MAGIC)) new Animation_Hold();
            }
            else if (spell == NPCMageSpell.Daemon)
            { // daemon
                //Sound.Play(25);
                //Sound.Play(-61);
                //BoE.pause(12); // gives sound time to end
                curTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Demon_ID], Pos, (!IsABaddie ? 0 : 100) + Maths.Rand(3, 1, 4));
            }
            else if (spell == NPCMageSpell.MajorBlessing)
            { // major bless
                //Sound.Play(25);
                foreach (ICharacter ch in curTown.EachCharacterInRange(Pos, 7))
                {
                    if (!AlliedWith(ch))
                    {
                        ch.Health += Maths.Rand(2, 1, 10);
                        ch.Bless(Maths.Rand(3, 1, 4));
                        ch.SetStatus(eAffliction.WEBS, 0);
                        if (ch.Status(eAffliction.HASTE_SLOW) < 0)
                            ch.SetStatus(eAffliction.HASTE_SLOW, 0);
                        if (ch is NPC) ((NPC)ch).Morale += Maths.Rand(3, 1, 10);
                    }
                }
            }
            else if (spell == NPCMageSpell.Shockwave)
            { // shockwave
                Game.AddMessage("  The ground shakes.");
                foreach (ICharacter ch in curTown.EachCharacterInRange(Pos, 10))
                    if (ch != this && curTown.Visible(ch.Pos))
                        ch.Damage(this, Maths.Rand(2 + Pos.DistanceTo(ch.Pos) / 2, 1, 6), 0, eDamageType.MAGIC);
                new Animation_Hold();
            }
        }



        void castPriestSpell(NPCPriestSpell spell, Location target, ICharacter targc)
        {
            KeyHandler.FlushHitKey();
            new Action(eAction.NONE);
            hasJustAttacked = true; //Set this if monster targets a specific PC!

            Location l = Pos;
            if (Dir.IsFacingRight && Record.Width > 1) l.X++;

            Game.AddMessage(String.Format("{0} casts: {1}", Record.Name, spell.Name));

            SP -= spell.Cost;

            if (spell == NPCPriestSpell.Wrack){
                new Animation_Missile(l, targc.Pos, 8, false, "024_priestspell");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(2, 1, 4),0, eDamageType.UNBLOCKABLE)) new Animation_Hold();
            }
            else if (spell == NPCPriestSpell.Stumble){
                Sound.Play(24);
                curTown.PlaceFieldPattern(Pattern.Single, targc.Pos, Field.WEB, this);
            }
            else if (spell == NPCPriestSpell.MinorBless) Bless(3);
            else if (spell == NPCPriestSpell.Bless) Bless(5);
            else if (spell == NPCPriestSpell.Curse){
                new Animation_Missile(l, targc.Pos, 8, false, "024_priestspell");
                new Animation_Hold();
                int x = Maths.Rand(1, 0, 1);
                targc.Curse(2 + x);
            }
            else if (spell == NPCPriestSpell.Wound){
                new Animation_Missile(l, targc.Pos, 8, false, "024_priestspell");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(2, 1, 6) + 2, 0, eDamageType.MAGIC)) new Animation_Hold();
            }
            else if (spell == NPCPriestSpell.SummonSpirit){
                curTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Shade_ID], Pos, (IsABaddie ? 100 : 0) + Maths.Rand(3, 1, 4));
            }
            else if (spell == NPCPriestSpell.SummonGuardian){
                curTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Guardian_ID], Pos, (IsABaddie ? 100 : 0) + Maths.Rand(3, 1, 4));
            }
            else if (spell == NPCPriestSpell.Disease){
                new Animation_Missile(l, targc.Pos, 11, false, "024_priestspell");
                new Animation_Hold();
                targc.Disease(2 + Maths.Rand(1, 0, 2));
            }
            else if (spell == NPCPriestSpell.HolyScourge){
                new Animation_Missile(l, targc.Pos, 15, false, "024_priestspell");
                new Animation_Hold();
                targc.Slow(2 + Maths.Rand(1,0,2), true);
                targc.Curse(3 + Maths.Rand(1,0,2));
            }
            else if (spell == NPCPriestSpell.Smite){
                new Animation_Missile(l, targc.Pos, 6, false, "024_priestspell");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(4, 1, 6) + 2, 0, eDamageType.COLD)) new Animation_Hold();
            }
            else if (spell == NPCPriestSpell.SticksToSnakes){
                int r1 = Maths.Rand(1, 1, 4) + 2;
                for (int i = 0; i < r1; i++)
                {
                    int r2 = Maths.Rand(1, 0, 7);
                    curTown.SummonMonster(this, r2 == 1 ? NPCRecord.List[Constants.NPC_Mage_Spell_Asp_ID] : NPCRecord.List[Constants.NPC_Mage_Spell_Serpent_ID], Pos, (IsABaddie ? 100 : 0) + Maths.Rand(3, 1, 4));
                }
            }
            else if (spell == NPCPriestSpell.MartyrsShield){
                Sound.Play(24);
                IncStatus(eAffliction.MARTYRS_SHIELD, 5, 10);
            }
            else if (spell == NPCPriestSpell.SummonHost){
                int duration = Maths.Rand(3, 1, 4) + 1;
                curTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Deva_ID], Pos, (!IsABaddie ? 0 : 100) + duration);
                for (int i = 0; i < 4; i++)
                {
                    if (curTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Shade_ID], Pos,
                            (IsABaddie ? 100 : 0) + duration) == false)
                        break;
                }
            }
            else if (spell == NPCPriestSpell.CurseAll || spell == NPCPriestSpell.Pestilence){
                Sound.Play(24);

                foreach(ICharacter ci in curTown.EachCharacterInRange(Pos, 7))
                    if (!AlliedWith(ci))
                    {
                        ci.Curse(2 + Maths.Rand(2, 0, 2), true);
                        ci.Disease(2 + Maths.Rand(1, 0, 2), true);
                    }
            }
            else if (spell == NPCPriestSpell.LightHeal) Heal(Maths.Rand(2, 1, 4) + 2); 
            else if (spell == NPCPriestSpell.Heal) Heal(Maths.Rand(3, 1, 6)); 
            else if (spell == NPCPriestSpell.MajorHeal) Heal(Maths.Rand(5, 1, 6) + 3); 
            else if (spell == NPCPriestSpell.ReviveSelf) Heal(50); 
            else if (spell == NPCPriestSpell.BlessAll || spell == NPCPriestSpell.ReviveAll){
                Sound.Play(24);
                foreach(ICharacter ci in curTown.EachCharacterInRange(Pos, 7))
                    if (AlliedWith(ci))
                    {
                        if (spell == NPCPriestSpell.BlessAll)
                            ci.IncStatus(eAffliction.BLESS_CURSE, Maths.Rand(2, 1, 4));
                        else if (spell == NPCPriestSpell.ReviveAll)
                            ci.Health += Maths.Rand(3, 1, 6); 
                    }
            }
            else if (spell == NPCPriestSpell.Flamestrike){
                new Animation_Missile(l, target, 2, false, "011_3booms");
                new Animation_Hold();
                curTown.HitArea(target, 2 + Record.Level / 2 + 2, 1,6,eDamageType.FIRE, Pattern.Square, true, this); new Animation_Hold();
            }
            else if (spell == NPCPriestSpell.UnholyRavaging){
                new Animation_Missile(l, targc.Pos, 14, false, "053_magic3");
                new Animation_Hold();
                if (targc.Damage(this, Maths.Rand(4, 1, 8), 0, eDamageType.MAGIC)) new Animation_Hold();
                targc.Slow(6);
                targc.Poison(5 + Maths.Rand(1, 0, 2));
            }
            else if (spell == NPCPriestSpell.Avatar){
                Sound.Play(24);
                Game.AddMessage(String.Format("  {0} is an avatar!", Name));
                Health = Record.Health;
                SetStatus(eAffliction.BLESS_CURSE, 8);
                SetStatus(eAffliction.POISON, 0);
                SetStatus(eAffliction.HASTE_SLOW, 8);
                SetStatus(eAffliction.WEBS, 0);
                SetStatus(eAffliction.DISEASE, 0);
                SetStatus(eAffliction.DUMB, 0);
                SetStatus(eAffliction.MARTYRS_SHIELD, 8);
            }
            else if (spell == NPCPriestSpell.DivineThud){
                new Animation_Missile(l, target, 9, false, "011_3booms");
                new Animation_Hold();
                curTown.HitArea(target, Maths.Min((Record.Level * 3) / 4 + 5,29),1,6, eDamageType.COLD, Pattern.Radius2, true, this); new Animation_Hold();
            }
        }

        bool breathAttack(Location target)
        //dam_type; // 0 - fire,  1 - cold,  2 - magic, 3 - darkness (= unblockable type)
        {
            KeyHandler.FlushHitKey();
            new Action(eAction.NONE);
            int level;
            eDamageType[] type = { eDamageType.FIRE, eDamageType.COLD, eDamageType.MAGIC, eDamageType.UNBLOCKABLE };
            int[] missile_t = { 13, 6, 8, 8 };
            Location l;

            l = Pos;
            if (Dir.IsFacingRight && Record.Width > 1) l.X++;

            new Animation_Attack(this);
            new Animation_Missile(l, target, missile_t[(byte)Record.BreathType], false, "044_breathe");
            new Animation_Hold();
            Game.AddMessage(String.Format("  {0} breathes.", Record.Name));
            level = Maths.Rand(Record.Breath, 1, 8);
            if (Game.Mode != eMode.COMBAT) level = level / 3;
            curTown.HitArea(target, 1, level,0, type[(byte)Record.BreathType], Pattern.Single, false, this); new Animation_Hold();
            return true;
        }
    }
}