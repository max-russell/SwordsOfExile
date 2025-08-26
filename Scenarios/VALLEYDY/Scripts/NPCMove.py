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
			if npc.Target != None:
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
