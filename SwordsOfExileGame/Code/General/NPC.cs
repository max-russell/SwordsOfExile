using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame;

//Stores information for an instance of a creature
public partial class NPC : ICharacter, IExpRecipient, IAnimatable
{
    //Shortcuts
    private static TownMap CurTown => (TownMap)Game.CurrentMap;
    private static PartyType Party => Game.CurrentParty;

    public string TooltipInfo(bool brief) 
    {
        var sb = new StringBuilder();
        sb.Append(Record.Name);
        sb.Append(AlliedWith(Party.LeaderPC) ? " (Friendly)" : " (Hostile)");
        sb.Append("\n  Health: ");
        sb.Append(Maths.Max(0,Health));
        sb.Append(" \\ ");
        sb.Append(MaxHealth);

        for (var a = 0; a < 14; a++)
        {
            var s = Status((eAffliction)a);

            if (s != 0)
                sb.Append("@n@i" + PCType.StatusMsg(this, (eAffliction)a) + "@e");
        }

        return sb.ToString();
    }
    
    public int Width => Record.Width;
    public int Height => Record.Height;
    public string Name => Record.Name;
    public int Level { get => Record.Level;
        set { } }
    public bool IsAlive() { return !Dying && CurTown.NPCList.Contains(this); }
    public Personality Personality { get { if (Start != null) return Start.personality; return null; } }
    public int MaxHealth => Record.Health;

    //Temporary properties - no need to save in savefile
    public bool Dying = false;

    public IAnimCharacter AnimAction { get; set; }

    public IAnimCharacter AnimFlash { get; set; }

    public bool NotDrawn { get; set; } = false; //Temporarily don't draw (used in teleporting animations)

    public bool IsVisible()
    {
        return Game.CurrentMap.Visible(pos);
    }

    private bool hasJustAttacked; //Tracks if the monster attacked this turn
    public int MessingAround; //Stupid thing
    public int TargetingNum { get; set; } //Used when the player is targeting for firing an arrow / spell etc, so that the player can press a key to select this NPC

    //Semi-temporary (errr....) Should be saved in save file
    public ICharacter Target; //Who it's currently trying to fight.
    private Location WanderTarget; //Was monster_targs - this stores the square a creature wanders to when it is not hostile (used in rand_move)

    private int Provocation; //This is calculated at the end of every npcs turn based on what it did that turn. Attacking or casting a spell is a big provocation.
    //But if the npc does nothing attention grabbing it decays back to 0 slowly.
    private ICharacter LastAttacked; //Did the npc attack another character last turn? Used when an enemy npc is deciding who to target.
    private MapPath PathToTarget;
        
    //Intrinsic properties    Should be saved in save file
    public eAttitude Attitude; //Whether the NPC is an ally or enemy of the PCs
    public eAttitude MyAttitude() { return Attitude; } //ICharacter method
    public bool IsABaddie => Attitude is eAttitude.HOSTILE_A or eAttitude.HOSTILE_B;
    public eActive Active; //Whether the NPC will attempt to attack its enemy
    private Location pos;
    public Location Pos { get => pos;
        set => pos = value;
    }
    public NPCRecord Record;
    public bool Mobile;
    public int Summoned;
    public NPCPreset Start;
    public Direction direction;
    public Direction Dir { get => direction;
        set => direction = value;
    }
    public int health, Morale;
    private int sp, ap;

    public int SP { get => sp;
        set => sp = Maths.MinMax(0, Record.SP, value);
    }
    public int Health { get => health;
        set => health = Math.Min(Record.Health, value);
    }
    public int AP { get => ap;
        set => ap = Maths.MinMax(0, Record.Speed, value);
    }

    private int[] status = new int[15];
    public int Status(eAffliction type) { return status[(int)type]; } //ICharacter
    public void SetStatus(eAffliction type, int val, int min = int.MinValue, int max = int.MaxValue) { status[(int)type] = Maths.MinMax(min, max, val); }
    public void IncStatus(eAffliction type, int val, int max = int.MaxValue)
    {
        status[(int)type] += val;
        if (status[(int)type] > max) status[(int)type] = max;
    }
    
    public void DecStatus(eAffliction type, int val, int min = int.MinValue)
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
        for (var n = 0; n < status.Length; n++)
            status[n] = 0;
    }

    public string DeathSound => Record.DeathSound;

    private static readonly short[] HitChance = {20,30,40,45,50,55,60,65,69,73,
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

        var ci = new NPC();

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
        var ci = new NPC();
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
        var ci = new NPC();
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
        var ci = new NPC
        {
            Active = eActive.COMBATIVE,
            Pos = pos,
            Record = cr.Record,
            Summoned = 0,
            Attitude = cr.Attitude,
            Dir = cr.Dir,
            health = cr.health,
            Morale = cr.Morale,
            sp = cr.sp,
            AP = cr.AP,
            Mobile = true
        };
        return ci;
    }

    public void Draw(SpriteBatch sb, XnaRect dr, Color col)
    {
        if (Record.SpecialSkill == eCSS.INVISIBLE) return;

        float rot = 0;

        if (AnimAction != null) 
            AnimAction.AdjustCharRect(ref dr, ref rot, ref col);
        if (AnimFlash != null)
            AnimFlash.AdjustCharRect(ref dr, ref rot, ref col);

        dr.Offset(dr.Width / 2, dr.Height / 2);

        Texture2D stex;
        var sr = Record.GetGraphic(direction.IsFacingRight, AnimAction is Animation_Attack, out stex);
        sb.Draw(stex, dr, sr, col, rot, new Vector2(Gfx.CHARGFXWIDTH * Record.Width / 2, Gfx.CHARGFXHEIGHT * Record.Height / 2)/*Vector2.Zero*/, SpriteEffects.None, 0);

        if (Gfx.ZoomSizeW > Gfx.ZOOMSIMPLETHRESHOLD && Gfx.ZoomSizeH > Gfx.ZOOMSIMPLETHRESHOLD)
        {
            if (Game.PlayerTargeting && Action.TargetNumbersOn && TargetingNum != -1)
            {
                var s = ((char)(TargetingNum + 97)).ToString();
                var z = new Vector2(dr.X + (dr.Width / 2f) - Gfx.TinyFont.MeasureString(s).Width, dr.Y + (dr.Height / 2f) - Gfx.TinyFont.MeasureString(s).Height);
                sb.DrawString(Gfx.TinyFont, s, z, Color.White);
            }

            if (Game.Mode == eMode.COMBAT && Gfx.DrawHealthBars && !Dying)
            {
                var br = new XnaRect(134, 181, 20, 6);

                //Health
                var h = (float)Health / (float)MaxHealth;
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

    public bool CanSee(Location l) {
        int i, j;
        Location destination;

        for (i = 0; i < Record.Width; i++)
        for (j = 0; j < Record.Height; j++) {
            destination.X = Pos.X + i;
            destination.Y = Pos.Y + j;
            if (CurTown.CanSee(destination, l) < Constants.OBSCURITY_LIMIT)
                return true;
        }
        return false;
    }

    //Takes into account NPCs that are bigger than 1 tile
    public bool AdjacentTo(Location loc) {

        for(var y = 0; y < Record.Height; y++)
        for (var x = 0; x < Record.Width; x++) {
            if (loc.adjacent(Pos + new Location(x,y))) return true;
        }
        return false;
    }

    public bool OnSpace(Location loc)
    {
        for (var y = 0; y < Record.Height; y++)
        for (var x = 0; x < Record.Width; x++)
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

        var pc_adj = new List<PCType>();

        if (MessingAround == 0)
        {
            foreach (var pc in Party.EachIndependentPC())// (j = 0; j < 6; j++)
                if (AdjacentTo(pc.Pos) == true)
                    pc_adj.Add(pc);
        }

////////////////////////////////////////////////////////////////////START SCRIPT - COMBAT MOVE////////////////////////////////////////////////////////////////////
        #region NPC combat move script
            
        if (Game.Mode == eMode.COMBAT) PickTarget();

        var acted_yet = false;

        // Now the monster, if evil, looks at the situation and maybe picks a tactic.
        // This only happens when there is >1 a.p. left, and tends to involve
        // running to a nice position.
        var current_monst_tactic = 0;
        if (Target != null && AP > 1 && MessingAround == 0)
        {
            var closestPc = Party.ClosestPC(Pos);
            if (closestPc is not null)
            {
                var l = Party.ClosestPC(Pos).Pos;
                if ((Record.MageLevel > 0 || Record.PriestLevel > 0) && l.DistanceTo(Pos) < 5 && !AdjacentTo(l))
                    current_monst_tactic = 1; // this means flee
            }

            if (Record.SpecialSkill is > eCSS.NO_SPECIAL_ABILITY and < eCSS.THROWS_ROCKS1 or eCSS.GOOD_ARCHER && // Archer?
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
            var r1 = Maths.Rand(1, 1, 6);
            if (r1 == 3) Morale++;
            if (Target.IsAlive() && Mobile)
            {
                acted_yet = WalkAwayFrom(Target.Pos);
                if (acted_yet) AP--;
            }
        }
        if (Target != null && Target.IsAlive() && Attitude > eAttitude.NEUTRAL
            && CanSee(Target.Pos)) 
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

                    var spell = selectMageSpell(out target_pos, out target_char);

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

                    var spell = selectPriestSpell(out target_pos, out target_char);
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
                    FireMissile();

                    // Vapors don't count as action
                    if (Record.SpecialSkill is eCSS.THROWS_DARTS or eCSS.THROWS_RAZORDISKS or eCSS.GOOD_ARCHER)
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
                var move_targ = Pos; 

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
        if (Target != null && Record.Radiate != eRadiate.NONE && CurTown.CanSee(Pos, Target.Pos) < Constants.OBSCURITY_LIMIT)
        {
            if (Maths.Rand(1, 1, 100) <= Record.RadiateProbability)
            {
                switch (Record.Radiate)
                {
                    case eRadiate.FIRE: CurTown.PlaceFieldPattern(Pattern.Square, Pos, Field.FIRE_WALL, null); break;
                    case eRadiate.ICE: CurTown.PlaceFieldPattern(Pattern.Square, Pos, Field.ICE_WALL, null); break;
                    case eRadiate.SHOCK: CurTown.PlaceFieldPattern(Pattern.Square, Pos, Field.FORCE_WALL, null); break;
                    case eRadiate.ANTIMAGIC: CurTown.PlaceFieldPattern(Pattern.Square, Pos, Field.ANTIMAGIC, null); break;
                    case eRadiate.SLEEP: CurTown.PlaceFieldPattern(Pattern.Square, Pos, Field.SLEEP_CLOUD, null); break;
                    case eRadiate.STINK: CurTown.PlaceFieldPattern(Pattern.Square, Pos, Field.STINK_CLOUD, null); break;
                    case eRadiate.SUMMON:
                        if (CurTown.SummonMonster(this, Record.NPCtoSummon, Pos, 130) == true)
                        {
                            Game.AddMessage(string.Format("  {0} summons allies.", Name));
                            Sound.Play("061_summoning");
                        }
                        break;
                }
            }
        }
          
        #endregion
/////////////////////////////////////////////////////////////////////END SCRIPT////////////////////////////////////////////////////////////////////////

        // PCs that are parrying attack approaching monsters
        foreach (var pc in Party.EachAlivePC())
            if (IsABaddie && !Dying && pc.Parry > 99 && AdjacentTo(pc.Pos) && !pc_adj.Contains(pc))
            {
                pc.Parry = 0;
                pc.Attack(this);
            }

        // pcs attack any fleeing monsters
        if (Game.Mode == eMode.COMBAT)
            for (var n = pc_adj.Count - 1; n >= 0; n--)
                if (!Dying && AdjacentTo(pc_adj[n].Pos) == false && IsABaddie && pc_adj[n].Status(eAffliction.INVISIBLE) == 0)
                {
                    pc_adj[n].Attack(this);
                    pc_adj.Remove(pc_adj[n]);
                    Animation.Create(new Animation_Hold());
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
                    else if (CurTown.NPCHateSpot(this,Pos))
                    {
                        var l2 = CurTown.FindClearSpot(Pos, true, false);
                        if (l2 != Pos) WalkTowards(l2);
                        else WalkToTarget();
                    }
                    else if (Record.MageLevel == 0 || CurTown.CanSee(Pos, Target.Pos) > 3)
                        WalkToTarget();
                }
                else
                if (Maths.Rand(1, 0, 1) == 0) WalkRandomly();
            }
        }

        if (CurTown.CanSee(Pos, Party.Pos) < 5)
        {
            if (Active == eActive.INACTIVE)   
                Active = eActive.DOCILE;
        }

        // Make hostile monsters active
        if (Active == eActive.DOCILE && IsABaddie && Pos.DistanceTo(Party.Pos) <= 8)
        {
            var r1 = Maths.Rand(1, 1, 100);
            r1 += (Party.Stealth > 0) ? 46 : 0;
            r1 += CurTown.CanSee(Pos, Party.Pos) * 10; //Guarantees monsters will not see if walls in the way - as CanSee returns 5 if blocked
            if (r1 < 50)
            {
                Active = eActive.COMBATIVE;
                Animation.Create(new Animation_CharFlash(this, Color.Red, Record.Humanish ? "018_drawingsword" : "046_growl"));
                Game.AddMessage("Monster saw you!");
            }
            else
                foreach (var ci in CurTown.NPCList)
                    if (ci.Active == eActive.COMBATIVE && pos.DistanceTo(ci.Pos) <= 5)
                    {
                        Active = eActive.COMBATIVE;
                        Animation.Create(new Animation_CharFlash(this, Color.Red, Record.Humanish ? "018_drawingsword" : "046_growl"));
                        return;
                    }
        }

        #endregion
        /////////////////////////////////////////////////////////////////////END SCRIPT/////////////////////////////////////////////////////////////////////////
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
                CurTown.NPCHateSpot(this, Pos))
            {
                PathToTarget = MapPath.CalculateNew(CurTown, this, Target.Pos);
            }
            return true;
        }

        Target = null;

        //Npc now considers which visible enemy is the most attractive to attack.

        //A list is compiled with all the possibilites and a score for each one.

        var possibles = new List<Tuple<ICharacter, int>>();

        foreach (var npc in CurTown.NPCList) {

            //If npc is on our side, don't consider
            if (AlliedWith(npc)) continue;

            //If npc is not visible, don't consider
            if (CurTown.CanSee(pos, npc.pos) >= 5) continue;

            //Score is based on weighing together the distance to the target (closer is preferable) to its provocation
            //value. Provocation is calculated at the end of each character's turn based on what it did that turn (eg, 
            //casting a spell or attacking is a big provocation)
            var score = pos.DistanceTo(npc.pos);

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

            foreach (var pc in Party.EachIndependentPC()) {

                //Mostly the same as for npcs
                if (CurTown.CanSee(pos, pc.Pos) >= Constants.OBSCURITY_LIMIT) continue;
                var score = pos.DistanceTo(pc.Pos);
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

        PathToTarget = MapPath.CalculateNew(CurTown, this, Target.Pos);

        return true;
    }

    public bool WalkRandomly()
    {
        var acted_yet = false;
        int j;
        var store_loc = new Location(0, 0);

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
                if (CurTown.InBounds(store_loc) && CurTown.CanSee(Pos, store_loc) < Constants.OBSCURITY_LIMIT)
                {
                    WanderTarget = store_loc; j = 3;
                }
            }

            if (WanderTarget.X == 0) {
                if (CurTown.InBounds(store_loc) && (Maths.Rand(1, 0, 1) == 1))
                    WanderTarget = store_loc;
                else {
                    store_loc = Pos;
                    store_loc.X += Maths.Rand(1, 0, 20) - 10;
                    store_loc.Y += Maths.Rand(1, 0, 20) - 10;
                    if (CurTown.InBounds(store_loc))
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
                return;
            }
        }

        //Path hasn't worked. Get rid of it.
        PathToTarget = null;

        //Just try to walk instead.
        WalkTowards(Target.Pos);

        return;
    }

    public bool WalkTowards(Location l2) {
        var acted_yet = false;

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

    public bool WalkAwayFrom(Location l2) {
        var acted_yet = false;

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

    public bool Walk(eDir dir) {

        var d = new Direction(dir);
        var destination = pos + d;
        if (!CurTown.CheckNPCDoors(destination, this)) return false;
        else if (CurTown.CharacterCanBeThere(destination, this) == false)
            return false;
        else if (Active != eActive.COMBATIVE && (CurTown.FieldThere(destination, Field.BARREL) || CurTown.FieldThere(destination, Field.CRATE)))
            return false;
        else
        {
            direction.Dir = d.Dir;
            Animation.Create(new Animation_Move(this, Pos, destination, Game.Mode == eMode.COMBAT));
            CurTown.PushLocation(this, destination);
            Pos = destination;
            CurTown.InflictFields(this);
            return true;
        }
    }

    private int calculateHit(int how_much, eDamageType dam_type)
    {
        eImmunity resist;
        resist = Record.Immunities;

        eDamageType[] dams = { eDamageType.MAGIC, eDamageType.FIRE, eDamageType.COLD, eDamageType.POISON };
        eImmunity[] res = { eImmunity.MAGIC_RESISTANCE, eImmunity.FIRE_RESISTANCE, eImmunity.COLD_RESISTANCE, eImmunity.POISON_RESISTANCE };
        for (var a = 0; a < 4; a++)
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
        if (dam_type is eDamageType.FIRE or eDamageType.COLD && (Maths.Rand(1, 0, 20) <= Record.Level))
            how_much = how_much / 2;
        if (dam_type == eDamageType.MAGIC && Maths.Rand(1, 0, 24) <= Record.Level)
            how_much = how_much / 2;

        // Rentar-Ihrno?
        if (Record.SpecialSkill == eCSS.INVULNERABILITY)
            how_much = how_much / 10;

        var r1 = Maths.Rand(1, 0, (Record.Armour * 5) / 4);
        r1 += Record.Level / 4;
        if (dam_type == 0)
            how_much -= r1;

        how_much = Maths.Max(how_much, 0);

        return how_much;
    }

    //// Damaging and killing monsters needs to be here because several have specials attached to them.
    public bool Damage(IExpRecipient attacker, int how_much, int how_much_spec, eDamageType dam_type, eDamageType spec_dam_type = eDamageType.WEAPON, string sound_type = null)
    {
        if (!(Game.PCsAlwaysHit && attacker is PCType))
        {
            how_much = calculateHit(how_much, dam_type);
            how_much_spec = calculateHit(how_much_spec, spec_dam_type);
        }
        else if (how_much <= 0) how_much = 1;

        // Absorb damage?
        if (dam_type is eDamageType.FIRE or eDamageType.MAGIC or eDamageType.COLD
            && Record.SpecialSkill == eCSS.ABSORB_SPELLS)
        {
            Health += how_much;
            Game.AddMessage("  Magic absorbed.");
            return false;
        }

        if (how_much <= 0)
        {
            if (Game.Mode == eMode.COMBAT)
                Game.AddMessage(string.Format("  {0} undamaged.", Name));
            return false;
        }

        var displaydamtype = (spec_dam_type > 0 && spec_dam_type != eDamageType.WEAPON) ? spec_dam_type : dam_type;

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

        if (how_much_spec > 0)
            Game.AddMessage(
                string.Format("  {0} takes {1}+{2}", Record.Name, how_much, how_much_spec));
        else
            Game.AddMessage(
                string.Format("  {0} takes {1}", Record.Name, how_much));


        Health = Health - how_much - how_much_spec;

        if (Game.OneHitKill)
            Health = -1;
        // splitting monsters
        if ((Record.SpecialSkill == eCSS.SPLITS) && (Health > 0)) CurTown.SplitOffMonster(this);

        if (attacker is PCType or PartyType)
            Party.total_dam_done += how_much + how_much_spec;

        // Monster is damaged. Make it hostile.
        Active = eActive.COMBATIVE;

        var animpos = new Vector2(Pos.X + (Width == 2 ? 0.5f : 0), Pos.Y + (Height == 2 ? 0.5f : 0));

        Animation.Create(new Animation_Damage(animpos, how_much, how_much_spec, displaydamtype, sound_type));

        if (Health <= 0)
        {
            Game.AddMessage(string.Format("  {0} dies.", Record.Name));
            Kill(attacker, eLifeStatus.DEAD);
        }
        else
        {
            if (how_much > 0) Morale--;
            if (how_much > 5) Morale--;
            if (how_much > 10) Morale--;
            if (how_much > 20) Morale -= 2;
        }

        if (!IsABaddie && attacker is PCType or PartyType && !CurTown.Hostile)
        {
            Game.AddMessage("Damaged an innocent.           ");
            Attitude = eAttitude.HOSTILE_A;
            CurTown.MakeTownHostile();
        }
        return true;
    }

    public bool Kill(IExpRecipient who_killed, eLifeStatus type, bool no_save = false)
    {
        int xp, i;

        // Special killing effects
        if (Start != null && Start.LifeVariable != null && Start.LifeVariable != "") Script.StuffDone[Start.LifeVariable] = 1;
        if (Start != null) Script.New_KillNPC(Start.FuncOnDeath, this, who_killed as PCType);
        Script.New_KillNPC(Record.FuncOnDeath, this, who_killed as PCType);

        if (Summoned is >= 100 or 0)
        { // no xp for party-summoned monsters

            xp = Record.Level * 2;
            if (who_killed is PCType)
                who_killed.AwardXP(xp);
            else if (who_killed is PartyType)
                who_killed.AwardXP(xp / 6 + 1);

            if (who_killed is PCType or PartyType)
            {
                i = Math.Max((xp / 6), 1);
                Party.AwardXP(i);
            }

            if ((Record.DropItem != null) && (Maths.Rand(1, 0, 100) < Record.DropItemChance))
            {
                CurTown.PlaceItem(Record.DropItem.Copy(), Pos);
            }
        }
        if (Summoned == 0)
            CurTown.place_treasure(Pos, Record.Level / 2, Record.Treasure, 0);

        switch (Record.Genus)
        {
            case eGenus.DEMON: CurTown.PlaceField(Pos, Field.CRATER); break;
            case eGenus.UNDEAD: CurTown.PlaceField(Pos, Field.BONES); break;
            case eGenus.SLIME:
            case eGenus.BUG: CurTown.PlaceField(Pos, Field.SMALL_SLIME); break;
            case eGenus.STONE: CurTown.PlaceField(Pos, Field.ROCKS); break;
            default: CurTown.PlaceField(Pos, Field.SMALL_BLOOD); break;
        }

        if (Summoned == 0)
        {
            CurTown.KillCount++;
        }

        if (Start != null) Start.InstanceWasKilled = true;

        Party.total_m_killed++;// party.total_m_killed++;
        Dying = true;
        Animation.Create(new Animation_Hold());
        Animation.Create(new Animation_Death(this));
        return true;
    }

    private static bool printedAcid = false;
    private static bool printedPoison = false;
    private static bool printedDisease = false;

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
            var r1 = Maths.Rand(Status(eAffliction.ACID), 1, 6);
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
                var r1 = Maths.Rand(Status(eAffliction.POISON), 1, 6);
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
                var k = Maths.Rand(1, 1, 5);
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
        CurTown.NPCList.Remove(this);
    }

    private void adjustMagic(ref int how_much)
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
        var realamt = Health;
        Health += amt;
        realamt = Health - realamt;
        if (!silent) Game.AddMessage(string.Format("  {0} healed {1}", Name, realamt));
        Animation.Create(new Animation_CharFlash(this, Color.FloralWhite, "052_magic2"));
    }

    public void Poison(int how_much, bool silent = false)
    {
        if (Record.ImmuneTo(eImmunity.POISON_RESISTANCE)) how_much = how_much / 2;
        if (Record.ImmuneTo(eImmunity.POISON_IMMUNITY))
        {
            if (!silent) Game.AddMessage(string.Format("  {0} resists.", Name));
            return;
        }
        status[(int)eAffliction.POISON] = Math.Min(8, status[(int)eAffliction.POISON] + how_much);
        if (how_much > 0) Animation.Create(new Animation_CharFlash(this, Color.LimeGreen, "017_shortcough"));
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "resists poison." : " is poisoned."));//String.Format("  {0} resists.", Name)) : Game.AddMessage(String.Format("  {0} is poisoned.", Name));, this);
    }

    public void Acid(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        status[(int)eAffliction.ACID] = Maths.MinMax(-8, 8, status[(int)eAffliction.ACID] + how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} is covered with acid.", Name));
        Animation.Create(new Animation_CharFlash(this, Color.GreenYellow, "042_dang"));
    }

    public void Slow(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        status[(int)eAffliction.HASTE_SLOW] = Maths.MinMax(-8, 8, status[(int)eAffliction.HASTE_SLOW] - how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "resists." : " is slowed."));
        Animation.Create(new Animation_CharFlash(this, Color.PaleTurquoise, "075_cold"));

    }
    public void Haste(int how_much, bool silent = false)
    {
        status[(int)eAffliction.HASTE_SLOW] = Maths.MinMax(-8, 8, status[(int)eAffliction.HASTE_SLOW] + how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} is hastened.", Name));
        Animation.Create(new Animation_CharFlash(this, Color.Orange, "075_cold"));
    }
    public void Curse(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        status[(int)eAffliction.BLESS_CURSE] = Maths.MinMax(-8, 8, status[(int)eAffliction.BLESS_CURSE] - how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "resists curse." : " is cursed."));
        Animation.Create(new Animation_CharFlash(this, Color.Black, "043_stoning"));
    }
    public void Bless(int how_much, bool silent = false)
    {
        status[(int)eAffliction.BLESS_CURSE] = Maths.MinMax(-8, 8, status[(int)eAffliction.BLESS_CURSE] + how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} is blessed.", Name));
        Animation.Create(new Animation_CharFlash(this, Color.Gold, "004_bless"));
    }
    public void Web(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        status[(int)eAffliction.WEBS] = Maths.MinMax(-8, 8, status[(int)eAffliction.WEBS] + how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "avoids webbing." : " is caught in webs."));
        Animation.Create(new Animation_CharFlash(this, Color.Gray, "017_shortcough"));
    }
    public void Scare(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        Morale -= how_much;
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "resists fear." : " is scared."));
        Animation.Create(new Animation_CharFlash(this, Color.DarkKhaki, "054_scream"));
    }
    public void Disease(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        status[(int)eAffliction.DISEASE] = Maths.MinMax(-8, 8, status[(int)eAffliction.DISEASE] + how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "resists disease." : " is diseased."));
        Animation.Create(new Animation_CharFlash(this, Color.DarkOrange, "066_disease"));
    }

    public void Dumbfound(int how_much, bool silent = false)
    {
        adjustMagic(ref how_much);
        status[(int)eAffliction.DUMB] = Maths.MinMax(-8, 8, status[(int)eAffliction.DUMB] + how_much);
        if (!silent) Game.AddMessage(string.Format("  {0} {1}", Name, how_much == 0 ? "resists dumbfounding." : " is dumbfounded."));
        Animation.Create(new Animation_CharFlash(this, Color.DarkSlateBlue, "067_huh"));
    }

    public void Sleep(int amount, int penalty)
    {
        short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };
        int r1;

        if (Record.Genus == eGenus.UNDEAD || Record.Genus == eGenus.SLIME || Record.Genus == eGenus.STONE || Record.SpecialSkill == eCSS.BREATHES_SLEEP_CLOUDS
            || Record.Radiate == eRadiate.SLEEP)
        {
            Game.AddMessage(string.Format("  {0} immune to sleep.", Name));
            return;
        }

        r1 = Maths.Rand(1, 0, 100);
        if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
        if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
        r1 += penalty;
        r1 -= 25;

        if (r1 > charm_odds[Record.Level / 2])
        {
            Game.AddMessage(string.Format("  {0} resists sleep.", Name));
            return;
        }
 
        IncStatus(eAffliction.ASLEEP, amount, 0);
                
        Game.AddMessage(string.Format("  {0} falls asleep.", Name));
        Animation.Create(new Animation_CharFlash(this, Color.MidnightBlue, "096_sleep"));    
    }

    public void Paralyze(int amount, int penalty)
    {
        short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };

        var r1 = Maths.Rand(1, 0, 100);
        if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
        if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
        r1 += penalty;
        r1 -= 15;

        if (r1 > charm_odds[Record.Level / 2])
        {
            Game.AddMessage(string.Format("  {0} resists.", Name));
            return;
        }
        IncStatus(eAffliction.PARALYZED, amount, 5000);
        Game.AddMessage(string.Format("  {0} is paralyzed.", Name));
        Animation.Create(new Animation_CharFlash(this, Color.Olive, "090_paralyze"));
    }

    public void Charm(int penalty)
    {
        short[] charm_odds = { 90, 90, 85, 80, 78, 75, 73, 60, 40, 30, 20, 10, 5, 2, 1, 0, 0, 0, 0, 0 };

        var r1 = Maths.Rand(1, 0, 100);
        if ((Record.Immunities & eImmunity.MAGIC_RESISTANCE) != eImmunity.NONE) r1 = r1 * 2;
        if ((Record.Immunities & eImmunity.MAGIC_IMMUNITY) != eImmunity.NONE) r1 = 200;
        r1 += penalty;

        if (r1 > charm_odds[Record.Level / 2])
        {
            Game.AddMessage(string.Format("  {0} resists.", Name));
            return;
        }
  
        Attitude = eAttitude.FRIENDLY;
        Game.AddMessage(string.Format("  {0} is charmed.", Name));
        Animation.Create(new Animation_CharFlash(this, Color.PeachPuff, "007_cool"));
    }

    ////Amalgamation of monster_attack_pc and monster_attack_monster
    public void Attack(ICharacter target) {

        KeyHandler.FlushHitKey();
        new Action(eAction.NONE);
        var dam_type = eDamageType.WEAPON;
        var pc = target as PCType;
        var npc = target as NPC;

        // A peaceful monster won't attack
        if (AlliedWith(target))
            return;

        // Check sanctuary
        if (target.Status(eAffliction.INVISIBLE) > 0)
        {
            var r1 = Maths.Rand(1, 0, 100);
            if (r1 > HitChance[Record.Level / 2])
            {
                Game.AddMessage("  Can't find target!                 ");
            }
            return;
        }

        direction.FaceTowards(pos, target.Pos);

        for (var i = 0; i < 3; i++) //Repeat for number of attacks.
        {
            if (!target.IsAlive()) break;
            if (Record.AttackAmount[i] <= 0 || Record.AttackMultiplier[i] <= 0) continue;

            hasJustAttacked = true;
            Provocation += Constants.AI_ATTACK_PROVOCATION_SCORE + 1;

            // Attack roll
            var r1 = Maths.Rand(1, 0, 100)
                     - 5 * Math.Min(target is PCType ? 8 : 10, Status(eAffliction.BLESS_CURSE))
                     + 5 * target.Status(eAffliction.BLESS_CURSE)
                     + (target is PCType ? 5 * pc.GetSkillBonus(eSkill.DEXTERITY) : 0)
                     - 15;
            r1 += 5 * (Status(eAffliction.WEBS) / 3);
            if (target is PCType && pc.Parry < 100) r1 += 5 * pc.Parry;

            // Damage roll
            var r2 = Maths.Rand(Record.AttackMultiplier[i], 1, Record.AttackAmount[i])
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
            if (r1 <= HitChance[(Record.Skill + 4) / 2])
            {
                var aa = new Animation_Attack(this);
                Animation.Create(aa);

                if (Record.Genus == eGenus.DEMON)
                    dam_type = eDamageType.DEMON;
                if (Record.Genus == eGenus.UNDEAD)
                    dam_type = eDamageType.UNDEAD;

                var store_hp = target.Health;

                var type = (int)((i > 0) ? Record.Attack23Type : Record.Attack1Type);
                string[] m = { "Hits", "Claws", "Bites", "Slimes", "Punches", "Stings", "Clubs", "Burns", "Harms", "Stabs" };
                var x = "Whacks";
                if ((int)type < m.Length) x = m[(int)type];
                Game.AddMessage(string.Format("{0} {1} {2}:", Record.Name, x, target.Name));

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
                        else if (Record.SpecialSkill is eCSS.XP_DRAINING_TOUCH or eCSS.ICY_AND_DRAINING_TOUCH
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
                        else if (Record.SpecialSkill is eCSS.ICY_TOUCH or eCSS.ICY_AND_DRAINING_TOUCH
                                 && Maths.Rand(1, 0, 8) < 6 && (target is NPC || pc.HasItemEquippedWithAbility(eItemAbil.LIFE_SAVING) == null))
                        {
                            Animation.Create(new Animation_Hold());
                            Game.AddMessage("  Freezing touch!");
                            r1 = Maths.Rand(3, 1, 10);
                            target.Damage(this, r1, 0, eDamageType.COLD);
                        }

                        // Killing touch
                        else if (Record.SpecialSkill == eCSS.DEATH_TOUCH) //&& (Maths.get_ran(1, 0, 8) < 6)) 
                        {
                            Animation.Create(new Animation_Hold());
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
                Game.AddMessage(string.Format("{0} misses {1}:", Record.Name, target.Name));
                Animation.Create(new Animation_Attack(this, "002_swordswish"));
            }
            LastAttacked = target; //Save who we just attacked for last time - used for working out who we might target in future

            Animation.Create(new Animation_Hold());
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
    public void FireMissile()
    {
        hasJustAttacked = true; //Set this if monster targets a specific PC!
        KeyHandler.FlushHitKey();
        new Action(eAction.NONE);

        int r1;//, r2, i;
        int[] dam = {0,1,2,3,4, 6,8,7,0,0, 0,0,0,0,0, 0,0,0,0,0,
            8,0,0,0,0, 0,0,0,0,0, 0,0,0,0,6, 0,0,0,0,0};

        switch (Record.SpecialSkill)
        {

            case eCSS.BREATHES_SLEEP_CLOUDS:
                Game.AddMessage("Creature breathes.");               
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 0, false, "044_breathe"));
                Animation.Create(new Animation_Hold());
                CurTown.PlaceFieldPattern(Pattern.Radius2, Target.Pos, Field.SLEEP_CLOUD, this);
                break;
            case eCSS.BREATHES_STINKING_CLOUDS:
                Game.AddMessage(string.Format("  Breathes on {0}.", Target.Name));
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 12, false, "044_breathe"));
                Animation.Create(new Animation_Hold());
                CurTown.PlaceFieldPattern(Pattern.Single, Target.Pos, Field.STINK_CLOUD, this);
                break;
            case eCSS.SHOOTS_WEB:
                Game.AddMessage(string.Format("  Throws web at {0}.", Target.Name));
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 8, false, "014_missile"));
                Animation.Create(new Animation_Hold());
                CurTown.PlaceFieldPattern(Pattern.Single, Target.Pos, Field.WEB, this);
                break;
            case eCSS.PARALYSIS_RAY:
                Sound.Play(51);
                Game.AddMessage(string.Format("  Fires ray at {0}.", Target.Name));
                Target.Paralyze(100, 0);
                break;
            case eCSS.PETRIFICATION_RAY:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 14, false, "043_stoning"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Gazes at {0}.", Target.Name));
                r1 = Maths.Rand(1, 0, 20) + Target.Level / 4 + Target.Status(eAffliction.BLESS_CURSE);
                if (r1 > 14)
                    Game.AddMessage(string.Format("  {0} resists.", Target.Name));
                else
                    Target.Kill(this, eLifeStatus.STONE);
                break;
            case eCSS.SP_DRAIN_RAY:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 8, false, "043_stoning"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Drains {0}.", Target.Name));
                Target.SP /= 2;
                break;
            case eCSS.HEAT_RAY:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 13, false, "051_magic1"));
                Animation.Create(new Animation_Hold());
                r1 = Maths.Rand(7, 1, 6);
                Game.AddMessage(string.Format("  Hits {0} with heat ray.", Target.Name));
                if (Target.Damage(this, r1, 0, eDamageType.FIRE)) Animation.Create(new Animation_Hold());
                break;
            case eCSS.ACID_SPIT:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 0, true, "064_spit"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Spits acid on {0}.", Target.Name));
                Target.Acid(6);
                break;
            case eCSS.THROWS_DARTS:
            case eCSS.SHOOTS_ARROWS:
            case eCSS.GOOD_ARCHER:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 3, true, "012_longbow"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Shoots at {0}.", Target.Name));
                break;
            case eCSS.THROWS_SPEARS:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 5, true, "014_missile"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Throws spear at {0}.", Target.Name));
                break;
            case eCSS.THROWS_RAZORDISKS:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 7, true, "014_missile"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Throws razordisk at {0}.", Target.Name));
                break;
            case eCSS.SHOOTS_SPINES:
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 5, true, "014_missile"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Fires spines at {0}.", Target.Name));
                break;
            default://rock throwing
                Animation.Create(new Animation_Missile(Pos, Target.Pos, 12, true, "014_missile"));
                Animation.Create(new Animation_Hold());
                Game.AddMessage(string.Format("  Throws rock at {0}.", Target.Name));
                break;
        }

        // Check sanctuary
        if (Target.Status(eAffliction.INVISIBLE) > 0)
        {
            if (Maths.Rand(1, 0, 100) > HitChance[(int)Record.SpecialSkill])
                Game.AddMessage("  Can't find target!");
            return;
        }

        r1 = Maths.Rand(1, 0, 100) - 5 * Maths.Min(10, Status(eAffliction.BLESS_CURSE)) + 5 * Target.Status(eAffliction.BLESS_CURSE)
             - 5 * (CurTown.CanSee(Pos, Target.Pos));
            
        if (Target is PCType && ((PCType)Target).Parry < 100)
            r1 += 5 * ((PCType)Target).Parry;
        var r2 = Maths.Rand(dam[(int)Record.SpecialSkill], 1, 7) + Math.Min(10, Status(eAffliction.BLESS_CURSE));

        if (r1 <= HitChance[dam[(int)Record.SpecialSkill] * 2])
        {
            if (Target.Damage(this, r2, 0, eDamageType.WEAPON, eDamageType.WEAPON, "098_missilehit")) Animation.Create(new Animation_Hold());
        }
        else
        {
            Game.AddMessage(string.Format("  Misses {0}.", Target.Name));
        }
    }

    private class NPCMageSpell
    {
        public int Cost, AreaEffect;
        public string Name;

        public static NPCMageSpell Spark = new() { Cost = 1, AreaEffect = 0, Name = "Spark" };
        public static NPCMageSpell MinorHaste = new() { Cost = 1, AreaEffect = 0, Name = "Minor Haste" };
        public static NPCMageSpell Strength = new() { Cost = 1, AreaEffect = 0, Name = "Strength" };
        public static NPCMageSpell FlameCloud = new() { Cost = 1, AreaEffect = 0, Name = "Flame Cloud" };
        public static NPCMageSpell Flame = new() { Cost = 2, AreaEffect = 0, Name = "Flame" };
        public static NPCMageSpell MinorPoison = new() { Cost = 2, AreaEffect = 0, Name = "Minor Poison" };
        public static NPCMageSpell Slow = new() { Cost = 2, AreaEffect = 0, Name = "Slow" };
        public static NPCMageSpell Dumbfound = new() { Cost = 2, AreaEffect = 0, Name = "Dumbfound" };
        public static NPCMageSpell StinkingCloud = new() { Cost = 2, AreaEffect = 1, Name = "Stinking Cloud" };
        public static NPCMageSpell SummonBeast = new() { Cost = 4, AreaEffect = 0, Name = "Summon Beast" };
        public static NPCMageSpell Conflagration = new() { Cost = 2, AreaEffect = 1, Name = "Conflagration" };
        public static NPCMageSpell Fireball = new() { Cost = 4, AreaEffect = 1, Name = "Fireball" };
        public static NPCMageSpell WeakSummoning = new() { Cost = 4, AreaEffect = 0, Name = "Weak Summoning" };
        public static NPCMageSpell Web = new() { Cost = 3, AreaEffect = 1, Name = "Web" };
        public static NPCMageSpell Poison = new() { Cost = 4, AreaEffect = 0, Name = "Poison" };
        public static NPCMageSpell IceBolt = new() { Cost = 4, AreaEffect = 0, Name = "Ice Bolt" };
        public static NPCMageSpell SlowGroup = new() { Cost = 4, AreaEffect = 0, Name = "Slow Group" };
        public static NPCMageSpell MajorHaste = new() { Cost = 5, AreaEffect = 0, Name = "Major Haste" };
        public static NPCMageSpell Firestorm = new() { Cost = 5, AreaEffect = 1, Name = "Firestorm" };
        public static NPCMageSpell Summoning = new() { Cost = 5, AreaEffect = 0, Name = "Summoning" };
        public static NPCMageSpell Shockstorm = new() { Cost = 5, AreaEffect = 1, Name = "Shockstorm" };
        public static NPCMageSpell MajorPoison = new() { Cost = 6, AreaEffect = 0, Name = "Major Poison" };
        public static NPCMageSpell Kill = new() { Cost = 6, AreaEffect = 0, Name = "Kill" };
        public static NPCMageSpell Daemon = new() { Cost = 6, AreaEffect = 0, Name = "Daemon" };
        public static NPCMageSpell MajorBlessing = new() { Cost = 7, AreaEffect = 0, Name = "Major Blessing" };
        public static NPCMageSpell MajorSummoning = new() { Cost = 7, AreaEffect = 0, Name = "Major Summoning" };
        public static NPCMageSpell Shockwave = new() { Cost = 7, AreaEffect = 0, Name = "Shockwave" };
    }

    private class NPCPriestSpell
    {
        public int Cost, AreaEffect;
        public string Name;

        public static NPCPriestSpell MinorBless = new() { Cost = 1, AreaEffect = 0, Name = "Minor Bless"};
        public static NPCPriestSpell LightHeal = new() { Cost = 1, AreaEffect = 0, Name = " Light Heal"};
        public static NPCPriestSpell Wrack = new() { Cost = 1, AreaEffect = 0, Name = "Wrack"};
        public static NPCPriestSpell Stumble = new() { Cost = 1, AreaEffect = 0, Name = "Stumble"};
        public static NPCPriestSpell Bless = new() { Cost = 2, AreaEffect = 0, Name = "Bless"};
        public static NPCPriestSpell Curse = new() { Cost = 2, AreaEffect = 0, Name = "Curse"};
        public static NPCPriestSpell Wound = new() { Cost = 2, AreaEffect = 0, Name = "Wound"};
        public static NPCPriestSpell SummonSpirit = new() { Cost = 4, AreaEffect = 0, Name = "Summon Spirit"};
        public static NPCPriestSpell Disease = new() { Cost = 2, AreaEffect = 0, Name = "Disease"};
        public static NPCPriestSpell Heal = new() { Cost = 3, AreaEffect = 0, Name = "Heal"};
        public static NPCPriestSpell HolyScourge = new() { Cost = 3, AreaEffect = 0, Name = "Holy Scourge"};
        public static NPCPriestSpell Smite = new() { Cost = 3, AreaEffect = 0, Name = "Smite"};
        public static NPCPriestSpell CurseAll = new() { Cost = 4, AreaEffect = 0, Name = "Curse All"};
        public static NPCPriestSpell SticksToSnakes = new() { Cost = 4, AreaEffect = 0, Name = "Sticks to Snakes"};
        public static NPCPriestSpell MartyrsShield = new() { Cost = 4, AreaEffect = 0, Name = "Martyr's Shield"};
        public static NPCPriestSpell BlessAll = new() { Cost = 5, AreaEffect = 0, Name = "Bless All"};
        public static NPCPriestSpell MajorHeal = new() { Cost = 5, AreaEffect = 0, Name = "Major Heal"};
        public static NPCPriestSpell Flamestrike = new() { Cost = 5, AreaEffect = 1, Name = "Flamestrike"};
        public static NPCPriestSpell SummonHost = new() { Cost = 10, AreaEffect = 0, Name = "Summon Host"};
        public static NPCPriestSpell ReviveSelf = new() { Cost = 6, AreaEffect = 0, Name = "Revive Self"};
        public static NPCPriestSpell UnholyRavaging = new() { Cost = 6, AreaEffect = 0, Name = "Unholy Ravaging"};
        public static NPCPriestSpell SummonGuardian = new() { Cost = 10, AreaEffect = 0, Name = "Summon Guardian"};
        public static NPCPriestSpell Pestilence = new() { Cost = 8, AreaEffect = 0, Name = "Pestilence"};
        public static NPCPriestSpell ReviveAll = new() { Cost = 8, AreaEffect = 0, Name = "Revive All"};
        public static NPCPriestSpell Avatar = new() { Cost = 8, AreaEffect = 0, Name = "Avatar"};
        public static NPCPriestSpell DivineThud = new() { Cost = 8, AreaEffect = 1, Name = "Divine Thud"};
    }

    private NPCMageSpell selectMageSpell(out Location target_pos, out ICharacter target_char)
    {
        int target_levels = 0, friend_levels_near;
        NPCMageSpell spell;// = eMMageSpells.NO_SPELL;

        target_pos = new Location(-1,-1);
        target_char = null;

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

        if (CurTown.FieldThere(Pos, Field.ANTIMAGIC)) return null;

        //Find the Caster's spell level for this spell
        var level = Maths.Max(1, Record.MageLevel - Status(eAffliction.DUMB)) - 1;

        target_pos = CurTown.FindSpellTargetPosition(Pos, 1, ref target_levels, this);//ter.find_fireball_loc(Pos, 1, (Attitude % 2 == 1) ? 0 : 1, ref target_levels);
        target_char = Target;

        friend_levels_near = -1 * CurTown.CountLevels(Pos, 3, this);//(Attitude % 2 != 1) ? town.count_levels(Pos, 3) : -1 * town.count_levels(Pos, 3);

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
            var r1 = Maths.Rand(1, 0, 17);
            spell = caster_array[level, r1];
        }

        // Hastes happen often now, but don't cast them redundantly
        if (Status(eAffliction.HASTE_SLOW) > 0 && (spell == NPCMageSpell.MinorHaste || spell == NPCMageSpell.MajorHaste))
            spell = emer_spells[level, 3];

        // Anything preventing spell?
        if (target_pos.X == -1 && spell.AreaEffect > 0)
        {
            var r1 = Maths.Rand(1, 0, 9);
            spell = caster_array[level, r1];
            if (target_pos.X == -1 && spell.AreaEffect > 0)
                return null;
        }
        if (spell.AreaEffect > 0) target_char = null;

        if (target_char == null)
        {
            if (CurTown.FieldThere(target_pos, Field.ANTIMAGIC)) return null;// false;
        }
        else
        if (CurTown.FieldThere(target_char.Pos, Field.ANTIMAGIC)) return null;// false;

        // How about shockwave? Good idea?
        if (spell == NPCMageSpell.Shockwave && !IsABaddie)
            spell = NPCMageSpell.MajorSummoning;
        if (spell == NPCMageSpell.Shockwave && IsABaddie && CurTown.CountLevels(Pos, 10, this) < 45)
            spell = NPCMageSpell.MajorSummoning;

        if (SP < spell.Cost) return null;

        return spell;
    }

    private NPCPriestSpell selectPriestSpell(out Location target_pos, out ICharacter target_char)
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

        if (CurTown.FieldThere(Pos, Field.ANTIMAGIC)) return null;

        var level = Maths.Max(1, Record.PriestLevel - Status(eAffliction.DUMB)) - 1;

        var target_levels = 0;
        target_pos = CurTown.FindSpellTargetPosition(Pos, 1, ref target_levels, this);
        var friend_levels_near = -1 * CurTown.CountLevels(Pos, 3, this);

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
            var r1 = Maths.Rand(1, 0, 9);
            spell = caster_array[level, r1];
            if (target_pos.X == -1 && spell.AreaEffect > 0)
                return null;
        }

        target_char = Target;

        if (spell.AreaEffect > 0) target_char = null;

        if (target_char == null && CurTown.FieldThere(target_pos, Field.ANTIMAGIC)) return null;
        if (target_char != null && CurTown.FieldThere(target_char.Pos, Field.ANTIMAGIC)) return null;

        // snuff heals if unwounded
        if (Health == Record.Health && (spell == NPCPriestSpell.MajorHeal || spell == NPCPriestSpell.ReviveSelf || spell == NPCPriestSpell.LightHeal || spell == NPCPriestSpell.Heal))
            return null;

        if (SP < spell.Cost) return null;
        else return spell;
    }

    private void castMageSpell(NPCMageSpell spell, Location target, ICharacter targc)//object targ) {
    {
        KeyHandler.FlushHitKey();
        new Action(eAction.NONE);
        hasJustAttacked = true; //Set this if monster targets a specific PC!

        int i, j=0;
        var l = Pos;
        if (Dir.IsFacingRight && Record.Width > 1) l.X++;

        Game.AddMessage(string.Format("{0} casts: {1}", Record.Name, spell.Name));

        SP -= spell.Cost;

        if (spell == NPCMageSpell.Spark)
        {
            Animation.Create(new Animation_Missile(l, targc.Pos, 6, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(2, 1, 4), 0, eDamageType.FIRE)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCMageSpell.MinorHaste){ // minor haste
            Haste(2);
        }
        else if (spell == NPCMageSpell.Strength)
        { 
            Bless(3);
        }
        else if (spell == NPCMageSpell.FlameCloud)
        { 
            Animation.Create(new Animation_Missile(l, targc.Pos, 2, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            CurTown.PlaceFieldPattern(Pattern.Single, targc.Pos, Field.FIRE_WALL, this);
        }
        else if (spell == NPCMageSpell.Flame)
        { 
            Animation.Create(new Animation_Missile(l, targc.Pos, 2, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(Record.Level, 1, 4), 0, eDamageType.FIRE)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCMageSpell.MinorPoison)
        {
            Animation.Create(new Animation_Missile(l, targc.Pos, 11, false, "025_magespell"));
            Animation.Create(new Animation_Hold());
            targc.Poison(2 + Maths.Rand(1, 0, 1));
        }
        else if (spell == NPCMageSpell.Slow)
        { 
            Animation.Create(new Animation_Missile(l, targc.Pos, 15, false, "025_magespell"));
            Animation.Create(new Animation_Hold());
            targc.Slow(2 + Record.Level / 2);
        }
        else if (spell == NPCMageSpell.Dumbfound)
        { 
            Animation.Create(new Animation_Missile(l, targc.Pos, 14, false, "025_magespell"));
            Animation.Create(new Animation_Hold());
            targc.Dumbfound(2);
        }
        else if (spell == NPCMageSpell.StinkingCloud)
        { 
            Animation.Create(new Animation_Missile(l, target, 0, false, "025_magespell"));
            Animation.Create(new Animation_Hold());
            CurTown.PlaceFieldPattern(Pattern.Square, target, Field.STINK_CLOUD, this);
        }
        else if (spell == NPCMageSpell.SummonBeast)
        { 
            var sum = NPCRecord.GetSummonMonster(1);
            if (sum != null)
                CurTown.SummonMonster(this, sum, Pos, (!IsABaddie ? 0 : 100) + Maths.Rand(3, 1, 4));
        }
        else if (spell == NPCMageSpell.Conflagration)
        { 
            Animation.Create(new Animation_Missile(l, target, 13, true, "025_magespell"));
            Animation.Create(new Animation_Hold());
            CurTown.PlaceFieldPattern(Pattern.Radius2, target, Field.FIRE_WALL, this);
        }
        else if (spell == NPCMageSpell.Fireball)
        { 
            Animation.Create(new Animation_Missile(l, target, 2, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            CurTown.HitArea(target, Maths.Min(1 + (Record.Level * 3) / 4, 29),1,6, eDamageType.FIRE, Pattern.Square, true, this);
            Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCMageSpell.WeakSummoning || spell == NPCMageSpell.Summoning || spell == NPCMageSpell.MajorSummoning)
        {
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
                    if (!CurTown.SummonMonster(this, sum, Pos, (!IsABaddie ? 0 : 100) + Maths.Rand(4, 1, 4)))
                    {
                        Game.AddMessage("  Summon failed.");
                        break;
                    }
                }
            }
        }
        else if (spell == NPCMageSpell.Web)
        {
            Sound.Play(25);
            CurTown.PlaceFieldPattern(Pattern.Radius2, target, Field.WEB, this);
        }
        else if (spell == NPCMageSpell.Poison)
        {
            Animation.Create(new Animation_Missile(l, targc.Pos, 11, false, "025_magespell"));
            Animation.Create(new Animation_Hold());
            targc.Poison(4 + Maths.Rand(1, 0, 3));
        }
        else if (spell == NPCMageSpell.IceBolt)
        {
            Animation.Create(new Animation_Missile(l, targc.Pos, 6, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(5 + (Record.Level / 5), 1, 8), 0, eDamageType.COLD)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCMageSpell.SlowGroup)
        {
            foreach (var ch in CurTown.EachCharacterInRange(Pos, 7))
            {
                if (!AlliedWith(ch))
                    ch.Slow(2 + Record.Level / 4, true);
            }
        }
        else if (spell == NPCMageSpell.MajorHaste)
        {
            foreach (var ch in CurTown.EachCharacterInRange(Pos, 7))
            {
                if (AlliedWith(ch))
                    ch.Haste(3);
            }
        }
        else if (spell == NPCMageSpell.Firestorm)
        {
            Animation.Create(new Animation_Missile(l, target, 1, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            CurTown.HitArea(target, Maths.Min(1 + (Record.Level * 3) / 4 + 3, 29), 1,6, eDamageType.FIRE, Pattern.Radius2, true, this); Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCMageSpell.Shockstorm)
        {
            Animation.Create(new Animation_Missile(l, target, 6, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            CurTown.PlaceFieldPattern(Pattern.Radius2, target, Field.FORCE_WALL, this);
        }
        else if (spell == NPCMageSpell.MajorPoison)
        {
            Animation.Create(new Animation_Missile(l, targc.Pos, 11, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            targc.Poison(6 + Maths.Rand(1, 1, 2));
        }
        else if (spell == NPCMageSpell.Kill)
        {
            Animation.Create(new Animation_Missile(l, targc.Pos, 9, true, "011_3booms"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, 35 + Maths.Rand(3, 1, 10), 0, eDamageType.MAGIC)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCMageSpell.Daemon)
        {
            CurTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Demon_ID], Pos, (!IsABaddie ? 0 : 100) + Maths.Rand(3, 1, 4));
        }
        else if (spell == NPCMageSpell.MajorBlessing)
        { 
            foreach (var ch in CurTown.EachCharacterInRange(Pos, 7))
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
        { 
            Game.AddMessage("  The ground shakes.");
            foreach (var ch in CurTown.EachCharacterInRange(Pos, 10))
                if (ch != this && CurTown.Visible(ch.Pos))
                    ch.Damage(this, Maths.Rand(2 + Pos.DistanceTo(ch.Pos) / 2, 1, 6), 0, eDamageType.MAGIC);
            Animation.Create(new Animation_Hold());
        }
    }

    private void castPriestSpell(NPCPriestSpell spell, Location target, ICharacter targc)
    {
        KeyHandler.FlushHitKey();
        new Action(eAction.NONE);
        hasJustAttacked = true; //Set this if monster targets a specific PC!

        var l = Pos;
        if (Dir.IsFacingRight && Record.Width > 1) l.X++;

        Game.AddMessage(string.Format("{0} casts: {1}", Record.Name, spell.Name));

        SP -= spell.Cost;

        if (spell == NPCPriestSpell.Wrack){
            Animation.Create(new Animation_Missile(l, targc.Pos, 8, false, "024_priestspell"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(2, 1, 4),0, eDamageType.UNBLOCKABLE)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCPriestSpell.Stumble){
            Sound.Play(24);
            CurTown.PlaceFieldPattern(Pattern.Single, targc.Pos, Field.WEB, this);
        }
        else if (spell == NPCPriestSpell.MinorBless) Bless(3);
        else if (spell == NPCPriestSpell.Bless) Bless(5);
        else if (spell == NPCPriestSpell.Curse){
            Animation.Create(new Animation_Missile(l, targc.Pos, 8, false, "024_priestspell"));
            Animation.Create(new Animation_Hold());
            var x = Maths.Rand(1, 0, 1);
            targc.Curse(2 + x);
        }
        else if (spell == NPCPriestSpell.Wound){
            Animation.Create(new Animation_Missile(l, targc.Pos, 8, false, "024_priestspell"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(2, 1, 6) + 2, 0, eDamageType.MAGIC)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCPriestSpell.SummonSpirit){
            CurTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Shade_ID], Pos, (IsABaddie ? 100 : 0) + Maths.Rand(3, 1, 4));
        }
        else if (spell == NPCPriestSpell.SummonGuardian){
            CurTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Guardian_ID], Pos, (IsABaddie ? 100 : 0) + Maths.Rand(3, 1, 4));
        }
        else if (spell == NPCPriestSpell.Disease){
            Animation.Create(new Animation_Missile(l, targc.Pos, 11, false, "024_priestspell"));
            Animation.Create(new Animation_Hold());
            targc.Disease(2 + Maths.Rand(1, 0, 2));
        }
        else if (spell == NPCPriestSpell.HolyScourge){
            Animation.Create(new Animation_Missile(l, targc.Pos, 15, false, "024_priestspell"));
            Animation.Create(new Animation_Hold());
            targc.Slow(2 + Maths.Rand(1,0,2), true);
            targc.Curse(3 + Maths.Rand(1,0,2));
        }
        else if (spell == NPCPriestSpell.Smite){
            Animation.Create(new Animation_Missile(l, targc.Pos, 6, false, "024_priestspell"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(4, 1, 6) + 2, 0, eDamageType.COLD)) Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCPriestSpell.SticksToSnakes){
            var r1 = Maths.Rand(1, 1, 4) + 2;
            for (var i = 0; i < r1; i++)
            {
                var r2 = Maths.Rand(1, 0, 7);
                CurTown.SummonMonster(this, r2 == 1 ? NPCRecord.List[Constants.NPC_Mage_Spell_Asp_ID] : NPCRecord.List[Constants.NPC_Mage_Spell_Serpent_ID], Pos, (IsABaddie ? 100 : 0) + Maths.Rand(3, 1, 4));
            }
        }
        else if (spell == NPCPriestSpell.MartyrsShield){
            Sound.Play(24);
            IncStatus(eAffliction.MARTYRS_SHIELD, 5, 10);
        }
        else if (spell == NPCPriestSpell.SummonHost){
            var duration = Maths.Rand(3, 1, 4) + 1;
            CurTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Deva_ID], Pos, (!IsABaddie ? 0 : 100) + duration);
            for (var i = 0; i < 4; i++)
            {
                if (CurTown.SummonMonster(this, NPCRecord.List[Constants.NPC_Mage_Spell_Shade_ID], Pos,
                        (IsABaddie ? 100 : 0) + duration) == false)
                    break;
            }
        }
        else if (spell == NPCPriestSpell.CurseAll || spell == NPCPriestSpell.Pestilence){
            Sound.Play(24);

            foreach(var ci in CurTown.EachCharacterInRange(Pos, 7))
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
            foreach(var ci in CurTown.EachCharacterInRange(Pos, 7))
                if (AlliedWith(ci))
                {
                    if (spell == NPCPriestSpell.BlessAll)
                        ci.IncStatus(eAffliction.BLESS_CURSE, Maths.Rand(2, 1, 4));
                    else if (spell == NPCPriestSpell.ReviveAll)
                        ci.Health += Maths.Rand(3, 1, 6); 
                }
        }
        else if (spell == NPCPriestSpell.Flamestrike){
            Animation.Create(new Animation_Missile(l, target, 2, false, "011_3booms"));
            Animation.Create(new Animation_Hold());
            CurTown.HitArea(target, 2 + Record.Level / 2 + 2, 1,6,eDamageType.FIRE, Pattern.Square, true, this); Animation.Create(new Animation_Hold());
        }
        else if (spell == NPCPriestSpell.UnholyRavaging){
            Animation.Create(new Animation_Missile(l, targc.Pos, 14, false, "053_magic3"));
            Animation.Create(new Animation_Hold());
            if (targc.Damage(this, Maths.Rand(4, 1, 8), 0, eDamageType.MAGIC)) Animation.Create(new Animation_Hold());
            targc.Slow(6);
            targc.Poison(5 + Maths.Rand(1, 0, 2));
        }
        else if (spell == NPCPriestSpell.Avatar){
            Sound.Play(24);
            Game.AddMessage(string.Format("  {0} is an avatar!", Name));
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
            Animation.Create(new Animation_Missile(l, target, 9, false, "011_3booms"));
            Animation.Create(new Animation_Hold());
            CurTown.HitArea(target, Maths.Min((Record.Level * 3) / 4 + 5,29),1,6, eDamageType.COLD, Pattern.Radius2, true, this); Animation.Create(new Animation_Hold());
        }
    }

    private bool breathAttack(Location target)
    {
        KeyHandler.FlushHitKey();
        new Action(eAction.NONE);
        int level;
        eDamageType[] type = { eDamageType.FIRE, eDamageType.COLD, eDamageType.MAGIC, eDamageType.UNBLOCKABLE };
        int[] missile_t = { 13, 6, 8, 8 };
        Location l;

        l = Pos;
        if (Dir.IsFacingRight && Record.Width > 1) l.X++;

        Animation.Create(new Animation_Attack(this));
        Animation.Create(new Animation_Missile(l, target, missile_t[(byte)Record.BreathType], false, "044_breathe"));
        Animation.Create(new Animation_Hold());
        Game.AddMessage(string.Format("  {0} breathes.", Record.Name));
        level = Maths.Rand(Record.Breath, 1, 8);
        if (Game.Mode != eMode.COMBAT) level = level / 3;
        CurTown.HitArea(target, 1, level,0, type[(byte)Record.BreathType], Pattern.Single, false, this); Animation.Create(new Animation_Hold());
        return true;
    }
}