def DoNonCombatMove(npc):
	# Have to pick targets
	if npc.Active != eActive.COMBATIVE:
		npc.Target = None # Not active : no target
	else:
		# NPC wants to fight. Look for a target.
		npc.PickTarget()

	if npc.Mobile and npc.Active != eActive.INACTIVE:
		if npc.Active == eActive.DOCILE:
			if Maths.Rand(1, 0, 1) == 0: npc.WalkRandomly()
		else:
			if npc.Target is not None:
				if npc.Morale < 0 and npc.Record.SpecialSkill != eCSS.MINDLESS and Record.Genus != eGenus.UNDEAD:
					npc.WalkAwayFrom(npc.Target.Pos);
					if Maths.Rand(1, 0, 10) < 6: npc.Morale += 1
				elif Town.NPCHateSpot(npc, npc.Pos):
					l2 = Town.FindClearSpot(npc.Pos, True, False)
					if l2 != npc.Pos: 
						npc.WalkTowards(l2)
					else: 
						npc.WalkToTarget()
				elif npc.Record.MageLevel == 0 or Town.CanSee(npc.Pos, npc.Target.Pos) > 3:
					npc.WalkToTarget()
			else:
				if Maths.Rand(1, 0, 1) == 0:
					WalkRandomly()

	if Town.CanSee(npc.Pos, Party.Pos) < 5:
		if npc.Active == eActive.INACTIVE:   
			npc.Active = eActive.DOCILE

	#Make hostile monsters active
	if npc.Active == eActive.DOCILE and npc.IsABaddie and npc.Pos.DistanceTo(Party.Pos) <= 8:
		r1 = Maths.Rand(1, 1, 100)
		r1 += 46 if Party.Stealth > 0 else 0
		r1 += Town.CanSee(npc.Pos, Party.Pos) * 10 #Guarantees monsters will not see if walls in the way - as CanSee returns 5 if blocked
		if r1 < 50:
			npc.Active = eActive.COMBATIVE;
			Animation_CharFlash(npc, Color.Red, "018_drawingsword" if Record.Humanish else "046_growl")
			Message("Monster saw you!")
		else:
			for ci in Town.NPCList:
				if ci.Active == eActive.COMBATIVE and npc.Pos.DistanceTo(ci.Pos) <= 5:
					npc.Active = eActive.COMBATIVE
					Animation_CharFlash(npc, Color.Red, "018_drawingsword" if Record.Humanish else "046_growl");
					return

def DoCombatMove(npc):
	if Game.Mode == eMode.COMBAT: PickTarget()

	acted_yet = False

	# Now the monster, if evil, looks at the situation and maybe picks a tactic.
	# This only happens when there is >1 a.p. left, and tends to involve
	# running to a nice position.
	current_monst_tactic = 0
	if npc.Target is not None and npc.AP > 1 and npc.MessingAround == 0:
		l = Party.ClosestPC(npc.Pos).Pos
		if (npc.Record.MageLevel > 0 or npc.Record.PriestLevel > 0) and l.DistanceTo(npc.Pos) < 5 and not AdjacentTo(l):
			current_monst_tactic = 1 # this means flee

		if ((npc.Record.SpecialSkill > eCSS.NO_SPECIAL_ABILITY and npc.Record.SpecialSkill < eCSS.THROWS_ROCKS1) or npc.Record.SpecialSkill == eCSS.GOOD_ARCHER) and npc.Pos.DistanceTo(npc.Target.Pos) < 6 and not AdjacentTo(npc.Target.Pos):
			current_monst_tactic = 1 # this means flee

	# flee
	if npc.Target is PCType and ((Morale <= 0 and npc.Record.SpecialSkill != eCSS.MINDLESS and npc.Record.Genus != eGenus.UNDEAD) or current_monst_tactic == 1):
		if Morale < 0: Morale += 1
		if Health > 50: Morale += 1
		r1 = Maths.Rand(1, 1, 6)
		if r1 == 3: Morale += 1
		if npc.Target.IsAlive() and npc.Mobile:
			acted_yet = npc.WalkAwayFrom(npc.Target.Pos)
			if acted_yet: AP -=1

	if npc.Target != null and npc.Target.IsAlive() and Attitude > eAttitude.NEUTRAL and npc.CanSee(npc.Target.Pos):
	    # Begin spec. attacks

		# Breathe (fire)
		if npc.Record.Breath > 0 and Maths.Rand(1, 1, 8) < 4 and not acted_yet:
			if npc.Target is not None and npc.Pos.DistanceTo(npc.Target.Pos) <= 8:
				acted_yet = BreathAttack(npc.Target.Pos)
				acted_yet = True
				npc.AP -= 4

		# Mage spell
		if npc.Record.MageLevel > 0 and (Maths.Rand(1, 1, 10) < (6 if npc.Record.PriestLevel > 0 else 9)) and not acted_yet:
			if (not npc.AdjacentTo(npc.Target.Pos) or Maths.Rand(1, 0, 2) < 2 or npc.Level > 9) and npc.Pos.DistanceTo(npc.Target.Pos) <= 10:

				spell, target_pos, target_char = SelectMageSpell(npc)

				if spell is None:
					npc.SP += 1
				else:
					CastMageSpell(npc, spell, target_pos, target_char)

				acted_yet = True
				npc.AP -= 5

		# Priest spell
		if npc.Record.PriestLevel > 0 and Maths.Rand(1, 1, 8) < 7 and not acted_yet:
			if (not AdjacentTo(npc.Target.Pos) or Maths.Rand(1, 0, 2) < 2 or npc.Level > 9) and Pos.DistanceTo(npc.Target.Pos) <= 10:
				acted_yet = CastPriestSpell(npc)
				acted_yet = True
				AP-=4;

		abil_range = (0,6,8,8,10, 10,10,8,6,8, 6,0,0,0,6, 0,0,0,0,4, 10,0,0,6,0,0,0,0,0,0, 0,0,8,6,9, 0,0,0,0,0)
		abil_odds =  (0,5,7,6,6,  5,5,6,6,6,   6,0,0,0,4, 0,0,0,0,4, 8,0,0,7,0,0,0,0,0,0,  0,0,7,5,6, 0,0,0,0,0)

		# Missile
		if abil_range[int(npc.Record.SpecialSkill)] > 0 and Maths.Rand(1, 1, 8) < abil_odds[int(npc.Record.SpecialSkill)] and not acted_yet:
			# Don't fire when adjacent, unless non-gaze magical attack
			if (not npc.AdjacentTo(npc.Target.Pos) or (npc.Record.SpecialSkill > eCSS.THROWS_RAZORDISKS and npc.Record.SpecialSkill != eCSS.GOOD_ARCHER and npc.Record.SpecialSkill != eCSS.ACID_SPIT)) and npc.Pos.DistanceTo(npc.Target.Pos) <= abil_range[int(npc.Record.SpecialSkill)]: # missile range
				Message(npc.Record.Name + ":")
				FireMissile(npc)

				# Vapors don't count as an action
				if npc.Record.SpecialSkill == eCSS.THROWS_DARTS or npc.Record.SpecialSkill == eCSS.THROWS_RAZORDISKS or npc.Record.SpecialSkill == eCSS.GOOD_ARCHER:
					npc.AP -= 2
				elif npc.Record.SpecialSkill == eCSS.HEAT_RAY:
					npc.AP -= 1
				else:
					npc.AP -= 3
				acted_yet = True

	if npc.Target is not None and not npc.AlliedWith(npc.Target) and npc.AdjacentTo(npc.Target.Pos) and not acted_yet:
		Attack(npc, npc.Target)
		AP -= 4
		acted_yet = True

	if Game.Mode == eMode.COMBAT:
		if not acted_yet and npc.Mobile:
			move_targ = npc.Pos 

			if npc.Target is not None and npc.Target.IsAlive():
				WalkToTarget(npc);
			elif npc.Attitude == eAttitude.NEUTRAL:
				acted_yet = WalkRandomly(npc)
				npc.MessingAround += 1

			npc.AP -= 1
		if not acted_yet and not npc.Mobile:
		    # drain action points
			npc.AP -= 1
			npc.MessingAround += 1
	elif not acted_yet:
		npc.AP -= 1
		npc.MessingAround += 1

	# Place fields for monsters that create them. Only done when monst sees foe
	if npc.Target is not None and npc.Record.Radiate != eRadiate.NONE and Town.CanSee(npc.Pos, npc.Target.Pos) < Constants.OBSCURITY_LIMIT:
		if Maths.Rand(1, 1, 100) <= npc.Record.RadiateProbability:
			if npc.Record.Radiate == eRadiate.FIRE: Town.PlaceFieldPattern(Pattern.Square, Pos, Field.FIRE_WALL, null) 
			elif npc.Record.Radiate == eRadiate.ICE: Town.PlaceFieldPattern(Pattern.Square, Pos, Field.ICE_WALL, null) 
			elif npc.Record.Radiate == eRadiate.SHOCK: Town.PlaceFieldPattern(Pattern.Square, Pos, Field.FORCE_WALL, null)
			elif npc.Record.Radiate == eRadiate.ANTIMAGIC: Town.PlaceFieldPattern(Pattern.Square, Pos, Field.ANTIMAGIC, null)
			elif npc.Record.Radiate == eRadiate.SLEEP: Town.PlaceFieldPattern(Pattern.Square, Pos, Field.SLEEP_CLOUD, null)
			elif npc.Record.Radiate == eRadiate.STINK: Town.PlaceFieldPattern(Pattern.Square, Pos, Field.STINK_CLOUD, null)
			elif npc.Record.Radiate == eRadiate.SUMMON:
				if Town.SummonMonster(npc, npc.Record.NPCtoSummon, npc.Pos, 130):
					Message(String.Format("  {0} summons allies.", npc.Name))
					Sound.Play("061_summoning")
	
def PickTarget(npc):
	#If existing target is now on the NPCs side, or has vanished, reset target.
	if npc.Target is not None and (npc.AlliedWith(npc.Target) or not npc.Target.IsAlive()): npc.Target = None

	#If this is not-combat mode, change to any of the PCs at random as they are all on the same space
	if Game.Mode != eMode.COMBAT and npc.Target is PCType:
		npc.Target = Party.RandomPC()

	#An NPC at random may become distracted
	if npc.Target is not None and Maths.Rnd.NextDouble() > Constants.AI_DISTRACTION_CHANCE:
		#Keep existing target but try to recalculate path.
		#If no path to target, or if target is now closer than the existing path's endpoint, re-calculate it.
		if npc.PathToTarget is None or not PathToTarget.StillValid(npc.Pos, npc.Target.Pos) or npc.Pos.VDistanceTo(npc.Target.Pos) < npc.Pos.VDistanceTo(npc.PathToTarget.GetDestination()) or Town.NPCHateSpot(npc, npc.Pos):
			npc.PathToTarget = MapPath.CalculateNew(Town, npc, npc.Target.Pos);
		return True

	Target = None

	#Npc now considers which visible enemy is the most attractive to attack.

	#A list is compiled with all the possibilites and a score for each one.

	possibles = []

	for n in Town.NPCList:

		#If npc is on our side, don't consider
		if npc.AlliedWith(n): continue

		#If npc is not visible, don't consider
		if Town.CanSee(npc.Pos, n.Pos) >= 5: continue

		#Score is based on weighing together the distance to the target (closer is preferable) to its provocation
		#value. Provocation is calculated at the end of each character's turn based on what it did that turn (eg, 
		#casting a spell or attacking is a big provocation)
		score = npc.Pos.DistanceTo(n.Pos);

		#The npc gets a bonus if it is right next to the target candidate
		if score <= 1: score -= Constants.AI_ADJACENCY_BONUS
		score -= n.Provocation

		#NPCs with a 'Drain spell points' missile attack greatly favour enemies with spell points to drain
		if npc.Record.SpecialSkill == eCSS.SP_DRAIN_RAY and n.SP <= 4: score += 100

		#If we were specifically attacked by this enemy last turn, more likely to target it back.
		if n.LastAttacked == npc: score -= Constants.AI_RETURN_FAVOUR_BONUS

		#Add it to the list.
		candidate = (npc, score)
		possibles.append(candidate)

	#Unless the npc is on the PCs side, also try adding the PCs to the list
	if (npc.IsABaddie)

		for pc in Party.EachIndependentPC():

			#Mostly the same as for npcs
			if Town.CanSee(npc.Pos, pc.Pos) >= Constants.OBSCURITY_LIMIT: continue
			score = npc.Pos.DistanceTo(pc.Pos)
			score -= pc.Provocation
			if pc.LastAttacked == npc: score -= Constants.AI_RETURN_FAVOUR_BONUS

			#Special bonus possibly applied to make npcs pay extra special attention to pcs
			score -= Constants.AI_I_HATE_PCS_BONUS

			#NPCs with a 'Drain spell points' missile attack greatly favour enemies with spell points to drain
			if npc.Record.SpecialSkill == eCSS.SP_DRAIN_RAY and pc.SP <= 4: score += 100

			#Add it to the list.
			candidate = (pc, score)
			possibles.append(candidate)

	#No targets found - return with failure.
	if possibles.len == 0: return False

	#Order the list by score.
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
	
def BreathAttack(npc, target):
	KeyHandler.FlushHitKey()
	Action(eAction.NONE)
	level = 0
	t = (eDamageType.FIRE, eDamageType.COLD, eDamageType.MAGIC, eDamageType.UNBLOCKABLE)
	missile_t = ( 13, 6, 8, 8 )
	l = npc.Pos;
	if npc.Dir.IsFacingRight and npc.Record.Width > 1: l.X += 1
	Animation_Attack(npc)
	Animation_Missile(l, target, missile_t[int(npc.Record.BreathType)], False, "044_breathe")
	Animation_Hold()
	Message("  %s breathes." % (npc.Record.Name))
	level = Maths.Rand(npc.Record.Breath, 1, 8)
	if Game.Mode != eMode.COMBAT: level /= 3
	Town.HitArea(target, 1, level, 0, t[int(Record.BreathType)], Pattern.Single, False, npc)
	Animation_Hold()
    
class NPCMageSpell:
	Spark = NPCMageSpell(Cost = 1, 0, "Spark")
	MinorHaste = NPCMageSpell(1, 0, "Minor Haste")
	Strength = NPCMageSpell(1, 0, "Strength")
	FlameCloud = NPCMageSpell(1, 0, "Flame Cloud")
	Flame = NPCMageSpell(2, 0, "Flame")
	MinorPoison = NPCMageSpell(2, 0, "Minor Poison")
	Slow = NPCMageSpell(2, 0, "Slow")
	Dumbfound = NPCMageSpell(2, 0, "Dumbfound")
	StinkingCloud = NPCMageSpell(2, 1, "Stinking Cloud")
	SummonBeast = NPCMageSpell(4, 0, "Summon Beast")
	Conflagration = NPCMageSpell(2, 1, "Conflagration")
	Fireball = NPCMageSpell(4, 1, "Fireball")
	WeakSummoning = NPCMageSpell(4, 0, "Weak Summoning")
	Web = NPCMageSpell(3, 1, "Web")
	Poison = NPCMageSpell(4, 0, "Poison")
	IceBolt = NPCMageSpell(4, 0, "Ice Bolt")
	SlowGroup = NPCMageSpell(4, 0, "Slow Group")
	MajorHaste = NPCMageSpell(5, 0, "Major Haste")
	Firestorm = NPCMageSpell(5, 1, "Firestorm")
	Summoning = NPCMageSpell(5, 0, "Summoning")
	Shockstorm = NPCMageSpell(5, 1, "Shockstorm")
	MajorPoison = NPCMageSpell(6, 0, "Major Poison")
	Kill = NPCMageSpell(6, 0, "Kill")
	Daemon = NPCMageSpell(6, 0, "Daemon")
	MajorBlessing = NPCMageSpell(7, 0, "Major Blessing")
	MajorSummoning = NPCMageSpell(7, 0, "Major Summoning")
	Shockwave = NPCMageSpell(7, 0, "Shockwave")

    def __init__(cost, area_affect, name):
		self.Cost = cost
		self.AreaAffect = area_affect
        self.Name = name    # instance variables unique to each instance
            
def SelectMageSpell(npc):
	#int target_levels = 0, friend_levels_near;
	#NPCMageSpell spell;// = eMMageSpells.NO_SPELL;

	target_pos = Location(-1,-1)
	target_char = None

	caster_array = (  
					#mage level 1 (spark, minor haste, strength, flame cloud)
				    (NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.MinorHaste, 
					 NPCMageSpell.MinorHaste, NPCMageSpell.MinorHaste,NPCMageSpell.Spark , 
					 NPCMageSpell.Strength,NPCMageSpell.FlameCloud,NPCMageSpell.FlameCloud, 
					 NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.Spark ,NPCMageSpell.MinorHaste, 
					 NPCMageSpell.MinorHaste, NPCMageSpell.MinorHaste,NPCMageSpell.Strength,NPCMageSpell.FlameCloud), 
					 #mage level 2 (flame, minor poison, slow, dumbfound, stinking cloud, summon beast, conflagration, minor haste)
				    (NPCMageSpell.Flame,NPCMageSpell.Flame,NPCMageSpell.Flame,NPCMageSpell.MinorPoison,NPCMageSpell.Slow,
					 NPCMageSpell.Dumbfound,NPCMageSpell.StinkingCloud,NPCMageSpell.SummonBeast,NPCMageSpell.Conflagration,
					 NPCMageSpell.Conflagration, NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,
					 NPCMageSpell.Flame,NPCMageSpell.Slow, NPCMageSpell.SummonBeast,NPCMageSpell.SummonBeast,NPCMageSpell.Flame),
					 #mage level 3 (flame, minor haste, stinking cloud, conflagration, fireball, web, weak summoning)
				    (NPCMageSpell.Flame,NPCMageSpell.Flame,NPCMageSpell.MinorHaste,NPCMageSpell.StinkingCloud,
					 NPCMageSpell.Conflagration, NPCMageSpell.Fireball,NPCMageSpell.Fireball,NPCMageSpell.Fireball,
				 	 NPCMageSpell.Web,NPCMageSpell.WeakSummoning, NPCMageSpell.WeakSummoning,NPCMageSpell.Fireball,
			 		 NPCMageSpell.Fireball,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,
					 NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste),
					 #mage level 4 (poison, ice bolt, slow group, flame, fireball, weak summoning, minor haste)
				    (NPCMageSpell.Poison,NPCMageSpell.Poison,NPCMageSpell.IceBolt,NPCMageSpell.SlowGroup,NPCMageSpell.SlowGroup,
					 NPCMageSpell.Flame,NPCMageSpell.Fireball,NPCMageSpell.Fireball,NPCMageSpell.WeakSummoning,
					 NPCMageSpell.WeakSummoning, NPCMageSpell.SlowGroup,NPCMageSpell.SlowGroup,NPCMageSpell.IceBolt,
					 NPCMageSpell.SlowGroup,NPCMageSpell.IceBolt, NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste,NPCMageSpell.MinorHaste),
					 #mage level 5 (poison, major haste, firestorm, summoning, shockstorm, ice bolt, slow group)
				    (NPCMageSpell.Poison,NPCMageSpell.MajorHaste,NPCMageSpell.Firestorm,NPCMageSpell.Firestorm,
					 NPCMageSpell.Summoning, NPCMageSpell.Summoning,NPCMageSpell.Shockstorm,NPCMageSpell.Shockstorm,NPCMageSpell.IceBolt,
					 NPCMageSpell.SlowGroup, NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,
					 NPCMageSpell.Firestorm, NPCMageSpell.Firestorm,NPCMageSpell.Firestorm,NPCMageSpell.Summoning),
					 #mage level 6 (kill, major poison, shockstorm, summoning, daemon, firestorm, major haste)
				    (NPCMageSpell.Kill,NPCMageSpell.Kill,NPCMageSpell.MajorPoison,NPCMageSpell.MajorPoison,NPCMageSpell.Shockstorm,
					 NPCMageSpell.Shockstorm,NPCMageSpell.Summoning,NPCMageSpell.Daemon,NPCMageSpell.Firestorm,NPCMageSpell.MajorHaste,
					 NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,
					 NPCMageSpell.Kill,NPCMageSpell.Kill,NPCMageSpell.Firestorm),
					 #mage level 7 (kill, daemon, major blessing, major haste, , major summoning, shockwave, major poison, firestorm )
				    (NPCMageSpell.Kill,NPCMageSpell.Kill,NPCMageSpell.Daemon,NPCMageSpell.MajorBlessing,
					 NPCMageSpell.MajorSummoning, NPCMageSpell.Shockwave,NPCMageSpell.Firestorm,NPCMageSpell.MajorPoison,
					 NPCMageSpell.Firestorm,NPCMageSpell.MajorHaste, NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,
					 NPCMageSpell.MajorHaste,NPCMageSpell.MajorHaste,NPCMageSpell.MajorSummoning,
					 NPCMageSpell.Daemon,NPCMageSpell.Daemon,NPCMageSpell.Kill)
				   )

	emer_spells = ( 
	               #emergency spells level 1 (minor haste, flame)
				   (NPCMageSpell.MinorHaste, None, None, NPCMageSpell.Flame),
		           #emergency spells level 2 (minor haste, summon beast, conflagration slow)
				   (NPCMageSpell.MinorHaste,NPCMageSpell.SummonBeast,NPCMageSpell.Conflagration,NPCMageSpell.Slow),
				   #emergency spells level 3 (minor haste, weak summoning, fireball)
				   (NPCMageSpell.MinorHaste,NPCMageSpell.WeakSummoning,NPCMageSpell.Fireball,NPCMageSpell.WeakSummoning),
				   #emergency spells level 4 (minor haste, weak summoning, fireball) (same as level 3)
				   (NPCMageSpell.MinorHaste,NPCMageSpell.WeakSummoning,NPCMageSpell.Fireball,NPCMageSpell.WeakSummoning),
				   #emergency spells level 5 (major haste, summoning, firestorm)
				   (NPCMageSpell.MajorHaste,NPCMageSpell.Summoning,NPCMageSpell.Firestorm,NPCMageSpell.MajorHaste),
				   #emergency spells level 6 (major haste, daemon, firestorm)
				   (NPCMageSpell.MajorHaste,NPCMageSpell.Daemon,NPCMageSpell.Firestorm,NPCMageSpell.Daemon),
				   #emergency spells level 7 (major haste, major summoning, firestorm, shockwave)
				   (NPCMageSpell.MajorHaste,NPCMageSpell.MajorSummoning,NPCMageSpell.Firestorm,NPCMageSpell.Shockwave)
				  )

	if Town.FieldThere(npc.Pos, Field.ANTIMAGIC): return None, target_pos, target_char

	#Find the Caster's spell level for this spell
	level = Maths.Max(1, npc.Record.MageLevel - npc.Status(eAffliction.DUMB)) - 1

	target_pos, target_levels = Town.FindSpellTargetPosition(npc, 1)
	target_char = npc.Target

	friend_levels_near = -1 * Town.CountLevels(npc.Pos, 3, npc)

	#Less than a quarter health remaining -  maybe cast emergency defensive spell
	if Health * 4 < npc.Record.Health and Maths.Rand(1, 0, 10) < 9:
		spell = emer_spells[level, 3]

	#Or caster has been slowed, maybe cast emergency haste spell
	elif ((npc.Status(eAffliction.HASTE_SLOW) < 0 and Maths.Rand(1, 0, 10) < 7)
		  or (npc.Status(eAffliction.HASTE_SLOW) == 0 and Maths.Rand(1, 0, 10) < 5))
		  and emer_spells[level, 0] is not None:
		spell = emer_spells[level, 0];

	#OR no allies nearby, maybe cast emergency summoning spell
	elif friend_levels_near <= -10 and Maths.Rand(1, 0, 10) < 7 and emer_spells[level, 1] is not None:
		spell = emer_spells[level, 1];

	#If a high score on the target spot we've selected, maybe cast emergency area damage spell
	elif target_levels > 50 and Maths.Rand(1, 0, 10) < 7 and emer_spells[level, 2] is not None:
		spell = emer_spells[level, 2]

	#Otherwise choose a spell at random from the spell pool for this level
	else:
		spell = caster_array[level, Maths.Rand(1, 0, 17)];

	# Hastes happen often now, but don't cast them redundantly
	if npc.Status(eAffliction.HASTE_SLOW) > 0 and (spell == NPCMageSpell.MinorHaste or spell == NPCMageSpell.MajorHaste):
		spell = emer_spells[level, 3]

	# Anything preventing spell?
	if target_pos.X == -1 and spell.AreaAffect > 0:
		spell = caster_array[level, Maths.Rand(1, 0, 9)]
		if target_pos.X == -1 and spell.AreaAffect > 0:
			return None, None, None

	if spell.AreaEffect > 0: target_char = None

	if target_char is None:
		if Town.FieldThere(target_pos, Field.ANTIMAGIC): return None, None, None
	else:
		if Town.FieldThere(target_char.Pos, Field.ANTIMAGIC): return None, None, None

	# How about shockwave? Good idea?
	if spell == NPCMageSpell.Shockwave and not IsABaddie:
		spell = NPCMageSpell.MajorSummoning
	if spell == NPCMageSpell.Shockwave and IsABaddie and CountLevels(Pos, 10, npc) < 45:
		spell = NPCMageSpell.MajorSummoning

	if npc.SP < spell.Cost: return None, None, None

	return spell, target_pos, target_char
	
	
def CastMageSpell(npc, spell, target_pos, target_char):
def CastPriestSpell(npc):
def FireMissile(npc):
def Attack(npc, npc.Target):
def WalkTowards(npc, l):
def WalkAwayFrom(npc, l):
def WalkToTarget(npc):
def WalkRandomly(npc):
	
def FindSpellTargetPosition(where, radius, who):
	cur_lev = 0
	level_max = 10;
	possibles = []
	check_loc = Location.Zero

	for check_loc.X in range(1, Town.Width - 1):
		for check_loc.Y in range(1, Town.Height - 1):
			if where.DistanceTo(check_loc) <= 8 and where.DistanceTo(check_loc) > radius and Town.CanSee(where, check_loc, True) < Constants.OBSCURITY_LIMIT and Town.GetObscurity(check_loc) < Constants.OBSCURITY_LIMIT:
				cur_lev = CountLevels(check_loc, radius, who)
				if cur_lev > level_max:
					level_max = cur_lev
					possibles = []
					possibles.append(check_loc)
				elif cur_lev == level_max:
					possibles.append(check_loc)

	if possibles.len == 0: return Location(-1, -1), level_max
	return possibles[Maths.Rand(1, 0, possibles.len - 1)], level_max

def CountLevels(where, radius, who):
	int store = 0;

	for ch in Town.EachCharacterInRange(where, radius, Game.Mode == eMode.COMBAT):
		if Town.CanSee(where, ch.Pos) < Constants.OBSCURITY_LIMIT:
			if who.AlliedWith(ch):
				store -= 10 if ch is PCType else ch.Level
			else:
				store += 10 if ch is PCType else ch.Level

	if Game.Mode != eMode.COMBAT:
		if Party.Pos.VDistanceTo(where) <= radius and Town.CanSee(where, Party.Pos) < Constants.OBSCURITY_LIMIT:
			if who.AlliedWith(Party.LeaderPC):
				store -= 20
			else:
				store += 20
	return store
