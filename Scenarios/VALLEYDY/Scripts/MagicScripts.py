def Cast_light_m(p):
    Party.LightLevel += 50
    Town.UpdateVisible()

def Cast_spark(p):
    Town.HitArea(p.Target, 1, Maths.Rand(2, 1, 4), 0, eDamageType.MAGIC, p.TargetPattern, False, p.PC)

def Cast_minor_haste(p):
    p.PCTarget.Haste(2)

def Cast_strength(p):
    p.PCTarget.Bless(3)

def Cast_scare(p):
    p.NPCTarget.Scare(Maths.Rand(2 + Bonus(p.PC, p.UsedItem),1,6))

def Cast_flame_cloud(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.FIRE_WALL, p.PC)

def Cast_identify(p):
    Message("All of your items are identified")
    for pc in Party.EachAlivePC():
        for i in pc.EquippedItemSlots:
            if i is not None: i.Identified = True
        for i in pc.ItemList:
            i.Identified = True

def Cast_scry_monster(p):
    Sound.Play("052_magic2")
    npc = p.NPCTarget
    pt = eDialogPic.CREATURE
    if npc.Width == 2 and npc.Height == 1: pt = eDialogPic.CREATURE2x1
    elif npc.Width == 1 and npc.Height == 2: pt = eDialogPic.CREATURE1x2
    elif npc.Width == 2 and npc.Height == 2: pt = eDialogPic.CREATURE2x2

    msg = "@b%s@e@nLevel: %i  Health: %i@nSpell Points: %i  Armour: %i@nSkill: %i  Morale: %i@nSpeed: %i  Mage Level: %i  Priest Level: %i@nPoison: %i" % (
          npc.Name, npc.Record.Level, npc.MaxHealth, npc.Record.SP, npc.Record.Armour, npc.Record.Skill, npc.Record.Morale, npc.Record.Speed, npc.Record.MageLevel, npc.Record.PriestLevel, npc.Record.Poison)

    ChoiceBox(msg, pt, npc.Record.Picture, ["OK"])

def Cast_goo(p):
    Town.PlaceFieldPattern(Pattern.Single, p.Target, Field.WEB, p.PC)

def Cast_true_sight(p):
    for x in range(Town.Width):
        for y in range(Town.Height):
            if Location(x, y).DistanceTo(p.PC.Pos) <= 2:
                Town.MakeExplored(Location(x, y))
    Town.UpdateVisible()


def Cast_minor_poison(p):
    p.NPCTarget.Poison(2 + Bonus(p.PC, p.UsedItem) / 2)

def Cast_flame(p):
    damage = Maths.Rand(min(10, 1 + Level(p.PC, p.UsedItem) / 3 + Bonus(p.PC, p.UsedItem)), 1, 6)
    Town.HitArea(p.NPCTarget.Pos, 1, damage, 0, eDamageType.FIRE, Pattern.Single, False, p.PC)

def Cast_slow(p):
    p.NPCTarget.Slow(2 + Maths.Rand(1,0,1) + Bonus(p.PC, p.UsedItem))

def Cast_dumbfound(p):
    p.NPCTarget.Dumbfound(1 + Bonus(p.PC, p.UsedItem) / 3)

def Cast_envenom(p):
    Message("  " + p.PCTarget.Name + " receives venom.")
    p.PCTarget.PoisonWeapon(3 + Bonus(p.PC, p.UsedItem))

def Cast_stinking_cloud(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.STINK_CLOUD, p.PC)

def Cast_summon_beast(p):
    duration = Maths.Rand(3, 1, 4) + Bonus(p.PC, p.UsedItem)
    if not Town.SummonMonster(p.PC, NPCRecord.GetSummonMonster(1), p.Target, duration):
        Message("  Summon failed.")

def Cast_conflagration(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.FIRE_WALL, p.PC)

def Cast_dispel_fields_m(p):
    Town.DispelFieldPattern(p.TargetPattern, p.Target, 0)
    #Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.DISPEL, p.PC)

def Cast_sleep_cloud(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.SLEEP_CLOUD, p.PC)

def Cast_unlock(p):

    combat_percent = [150,120,100,90,80,80,80,70,70,70,70,70,67,62,57,52,47,42,40,40]
    ter = Town.TerrainAt(p.Target)

    if ter.Special == eTerSpec.UNLOCKABLE_TERRAIN or ter.Special == eTerSpec.UNLOCKABLE_BASHABLE:

        r1 = Maths.Rand(1, 0, 100) - 5 * p.PC.GetSkillBonus(eSkill.INTELLIGENCE) + 5 * Town.Difficulty
        r1 += ter.Flag2 * 7 #unlock_adjust (door resistance)
        if ter.Flag2 == 10:
            r1 = 10000

        r1 = 0
        if r1 < (135 - combat_percent[Maths.Min(19, p.PC.Level)]):
            Message("  Door unlocked.")
            Sound.Play("009_lockpick")
            Town.AlterTerrain(p.Target, ter.Layer, ter.GetUnlocked())
        else:
            Sound.Play("041_darn")
            Message("  Didn't work.")
    else:
        Message("  Wrong terrain type.")

    #p.PC.CastUnlock(p.Target)

def Cast_haste(p):
    p.PCTarget.Haste(max(2, p.PC.Level / 2 + Bonus(p.PC, p.UsedItem)))

def Cast_fireball(p):
  damage = min(9, 1 + (Level(p.PC, p.UsedItem) * 2) / 3 + Bonus(p.PC, p.UsedItem)) + 1
  if damage > 10:
    damage = (damage * 8) / 10
  if damage <= 0:
    damage = 1
  Town.HitArea(p.Target, damage, 1,6, eDamageType.FIRE, p.TargetPattern, True, p.PC)

def Cast_long_light(p):
    Party.LightLevel += 200
    Town.UpdateVisible()

def Cast_fear(p):
    Animation_Missile(p.PC.Pos, p.Target, 11, True, "011_3booms")
    p.NPCTarget.Scare(Maths.Rand(min(20, p.PC.Level / 2 + Bonus(p.PC, p.UsedItem)), 1,8))

def Cast_wall_of_force(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.FORCE_WALL, p.PC)

def Count_weak_summoning(caster, spell, item):
    return Maths.MinMax(1,7, caster.Level / 4 + Bonus(caster, item) / 2)

def Cast_weak_summoning(p):
    for p.Target in p.TargetList:
        duration = Maths.Rand(4, 1, 4) + Bonus(p.PC, p.UsedItem)
        if not Town.SummonMonster(p.PC, NPCRecord.GetSummonMonster(1), p.Target, duration):
            Message("  Summon failed.")

def Count_flame_arrows(caster, spell, item):
    return caster.Level / 4 + Bonus(caster, item) / 2

def Cast_flame_arrows(p):
    for npc in p.NPCTargetList:
        npc.Damage(p.PC, Maths.Rand(2, 1, 4), 0, eDamageType.FIRE)

def Cast_web(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.WEB, p.PC)

def Cast_resist_magic(p):
    Message("  " + p.PCTarget.Name + " resistant.")
    p.PCTarget.IncStatus(eAffliction.MAGIC_RESISTANCE, 5 + Bonus(p.PC, p.UsedItem))

def Cast_poison(p):
    p.NPCTarget.Poison(4 + Bonus(p.PC, p.UsedItem) / 2)

def Cast_ice_bolt(p):
    Town.HitArea(p.Target, 1, Maths.Rand(min(20, Level(p.PC, p.UsedItem) + Bonus(p.PC, p.UsedItem)), 1, 4),0, eDamageType.COLD, Pattern.Single, False, p.PC)

def Cast_slow_group(p):
    Message("  Enemy slowed:")
    for npc in Town.EachCharacterInRange(p.PC.Pos, p.Spell.Range, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           Animation_Missile(p.PC.Pos, npc.Pos, 8, True)
           Animation_Pause()
           npc.Slow(5 + Bonus(p.PC, p.UsedItem))

def Cast_magic_map(p):
    i = p.PC.HasItemWithAbility(eItemAbil.SAPPHIRE)
    if i is None:
        Message("  You need a sapphire.")
        p.CancelAction = True
    elif Town.PreventMapping or Town.PreventScrying:
        Message("  The spell fails.")
        p.CancelAction = True
    else:
        p.PC.UseItemCharge(i)
        Message("  As the sapphire dissolves,")
        Message("  you have a vision.")
        for  y in range(Town.Height):
             for x in range(Town.Width):
                 Town.MakeExplored(Location(x, y))

def Cast_capture_soul(p):
    r1 = (Maths.Rand(1,0,100) * 7) / 10
    charm_odds = [90,90,85,80,78, 75,73,60,40,30, 20,10,5,2,1, 0,0,0,0,0]
    npc = p.NPCTarget

    if npc.Width > 1 or npc.Height > 1:
	    Message("Capture Soul: Monster is too big.")
	    p.CancelAction = True
    elif r1 > charm_odds[npc.Record.Level / 2] or npc.Record.SpecialSkill == eCSS.SPLITS or npc.Record.Genus == eGenus.IMPORTANT:
	    Sound.Play("068_identify")
	    Message("  %s resists." % npc.Name)
    else:
        slot = Maths.Rand(1,0,3)
        if StuffDone["CapturedSouls", slot] == 0:
            StuffDone["CapturedSouls", slot] = npc.Record.Num
        else:
            slot = Maths.Rand(1,0,3)
            StuffDone["CapturedSouls", slot] = npc.Record.Num
        Message("Capture Soul: Success!")
        Message("  Caught in slot %i." % (slot + 1))
        Sound.Play("053_magic3")

def Count_simulacrum(caster, spell, item):
    for n in range(4):
        if StuffDone["CapturedSouls", n] != 0:
            return 1
    Message("  No souls have been captured.")
    return 0

def Cast_simulacrum(p):
    msg = "Choose a stored creature to summon:@n@n"
    for n in range(4):
        msg += "Slot %i: " % (n+1)
        if StuffDone["CapturedSouls", n] != 0:
            msg += "@b%s@e (Cost: %i)@n" % (NPCRecord.List[StuffDone["CapturedSouls", n]].Name, NPCRecord.List[StuffDone["CapturedSouls", n]].Level)
        else:
            msg += "Empty@n"
    result = ChoiceBox(msg, eDialogPic.STANDARD, 12, ["Cancel", "1", "2", "3", "4"])
    if result == 0:
        p.CancelAction = True
        return
    npcno = StuffDone["CapturedSouls", result-1]
    if npcno == 0:
        Message("Slot empty")
        p.CancelAction = True
        return
    npr = NPCRecord.List[npcno]
    if p.PC.SP < npr.Level:
        Message("Not enough spell points.")
        p.CancelAction = True
        return
    duration = Maths.Rand(3,1,4) + p.PC.GetSkillBonus(eSkill.INTELLIGENCE)
    if not Town.SummonMonster(p.PC, npr, p.TargetList[0], duration):
        Message("  Summon failed.")
        p.CancelAction = True
    else:
        p.PC.SP -= npr.Level

def Count_venom_arrows(caster, spell, item):
    return caster.Level / 5 + Bonus(caster, item) / 2

def Cast_venom_arrows(p):
    for npc in p.NPCTargetList:
        npc.Poison(4 + Bonus(p.PC, p.UsedItem) / 2)

def Cast_wall_of_ice(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.ICE_WALL, p.PC)

def Cast_stealth(p):
    Party.Stealth += max(6, p.PC.Level * 2)

def Cast_major_haste(p):
    for pc in Party.EachAlivePC():
        pc.Haste(min(8, 1 + p.PC.Level / 8 + Bonus(p.PC, p.UsedItem)))
        Animation_Missile(p.PC.Pos, pc.Pos, 8, True)
        Animation_Pause()
    Message("  Party hasted.")

def Cast_fire_storm(p):
    damage = min(12, 1 + (Level(p.PC, p.UsedItem) * 2) / 3 + Bonus(p.PC, p.UsedItem)) + 2
    if damage > 20: damage = (damage * 8) / 10
    Town.HitArea(p.Target, damage,1,6, eDamageType.FIRE, p.TargetPattern, True, p.PC)

def Cast_dispel_barrier(p):
    combat_percent = [150,120,100,90,80,80,80,70,70,70, 70,70,67,62,57,52,47,42,40,40]
    if Town.FieldThere(p.Target, Field.FIRE_BARRIER) or Town.FieldThere(p.Target, Field.FORCE_BARRIER):
       r1 = Maths.Rand(1, 0, 100) - 5 * Bonus(p.PC, p.UsedItem) + 5 * (Town.Difficulty / 10)
       if Town.FieldThere(p.Target, Field.FIRE_BARRIER): r1 -= 8

       #I've decided to make used items that dispel barriers always succeed
       if r1 < 120 - combat_percent[min(19, p.PC.Level)] or p.UsedItem is not None:
          Message("  Barrier broken.")
          Town.RemoveField(p.Target, Field.FIRE_BARRIER)
          Town.RemoveField(p.Target, Field.FORCE_BARRIER)
          Town.UpdateVisible()
       else:
          Sound.Play("041_darn")
          Message("  Didn't work.")
    else:
       Message("  No barrier there.")

def Cast_fire_barrier(p):
    Sound.Play("068_identify")
    Town.HitArea(p.Target, 1, Maths.Rand(3, 2, 7),0, eDamageType.FIRE, Pattern.Single, False, p.PC)
    Town.MakeFireBarrier(p.Target)
    if Town.FieldThere(p.Target, Field.FIRE_BARRIER):
        Message("  You create the barrier.")
    else:
        Message("  Failed.")

def Count_summoning(caster, spell, item):
    return Maths.MinMax(1, 6, caster.Level / 6 + Bonus(caster, item) / 2)

def Cast_summoning(p):
    duration = Maths.Rand(5, 1, 4) + Bonus(p.PC, p.UsedItem)
    for targ in p.TargetList:
        duration = Maths.Rand(7, 1, 4) + Bonus(p.PC, p.UsedItem)
        if not Town.SummonMonster(p.PC, NPCRecord.GetSummonMonster(2), targ, duration):
            Message("  Summon failed.")

def Cast_shockstorm(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.FORCE_WALL, p.PC)

def Count_spray_fields(caster, spell, item):
    return caster.Level / 5 + Bonus(caster, p.UsedItem) / 2

def Cast_spray_fields(p):
    for p.Target in p.TargetList:
        Town.PlaceFieldPattern(p.TargetPattern, p.Target, Maths.Rand(1, 0, 14), p.PC)

def Cast_major_poison(p):
    p.NPCTarget.Poison(8 + Bonus(p.PC, p.UsedItem) / 2)

def Cast_group_fear(p):
    Message("  Enemy scared:")
    for npc in Town.EachCharacterInRange(p.PC.Pos, p.Spell.Range, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           Animation_Missile(p.PC.Pos, npc.Pos, 8, True)
           Animation_Pause()
           npc.Scare(Maths.Rand(p.PC.Level / 3, 1, 8))

def Cast_kill(p):
    damage = 40 + Maths.Rand(3, 0, 10) + p.PC.Level * 2
    Town.HitArea(p.Target, 1, damage, 0, eDamageType.MAGIC, Pattern.Single, False, p.PC)

def Count_paralyze(caster, spell, item):
    return caster.Level / 8 + Bonus(caster, item) / 3

def Cast_paralyze(p):
    for npc in p.NPCTargetList:
        npc.Paralyze(1000,-10)

def Cast_daemon(p):
    duration = Maths.Rand(5, 1, 4) + Bonus(p.PC, p.UsedItem)
    if not Town.SummonMonster(p.PC, NPCRecord.List[85], p.Target, duration):
        Message("  Summon failed.")

def Cast_antimagic_cloud(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.ANTIMAGIC, p.PC)

def Cast_mindduel(p):
    if p.NPCTarget.Record.MageLevel == 0 and p.NPCTarget.Record.PriestLevel == 0:
        Message("  Can't duel: no magic.")
    else:
        sc = p.PC.HasItemWithAbility(eItemAbil.SMOKY_CRYSTAL)
        if sc is None:
            Message("  You need a smoky crystal.")
        else:
            p.PC.UseItemCharge(sc)
            adjust = (p.PC.Level + p.PC.GetSkill(eSkill.INTELLIGENCE)) / 2 - p.NPCTarget.Level * 2

            if p.PC.HasItemEquippedWithAbility(eItemAbil.WILL) is not None: adjust += 20
            if not p.NPCTarget.IsABaddie:
                Town.MakeTownHostile()
            balance = 0
            Message("Mindduel!")
            i = 0
            while p.PC.IsAlive() and p.NPCTarget.IsAlive() and i < 10:
                r1 = Maths.Rand(1,0,100) + adjust
                r1 += 5 * (p.NPCTarget.Status(eAffliction.DUMB) - p.PC.Status(eAffliction.DUMB))
                r1 += 5 * balance
                r2 = Maths.Rand(1,1,6)
                if r1 < 30:
                    Message("  " + p.PC.Name + " is drained " + str(r2) + ".")
                    Animation_CharFlash(p.PC, Colour.FromRGB(134,43,236), "043_stoning")
                    Wait()
                    p.NPCTarget.SP += r2
                    balance+=1
                if p.PC.SP == 0:
                    p.PC.IncStatus(eStatus.DUMB,2)
                    Message("  " + p.PC.Name + " is dumbfounded.")
                    if p.PC.Status(eStatus.DUMB) > 7:
                        Message("  " + p.PC.Name + " is killed!")
                        p.PC.Kill(2)
                    else:
                        p.PC.SP -= r2
                if r1 > 70:
                    Message("  " + p.PC.Name + " drains " + str(r2) + ".")
                    Animation_CharFlash(p.NPCTarget, Colour.FromRGB(134,43,236), "043_stoning")
                    Wait()
                    p.PC.SP += r2
                    balance -= 1
                    if p.NPCTarget.SP == 0:
                        p.NPCTarget.IncStatus(eStatus.DUMB,2)
                        Message("  " + p.NPCTarget.Name + " is dumbfounded.")
                        if p.NPCTarget.Status(eStatus.DUMB) > 7:
                            p.NPCTarget.Kill(p.PC)
                        else:
                            p.NPCTarget.SP -= r2
                i+=1

def Cast_flight(p):
    if Party.Flying > 0:
       Message("  Not while already flying.")
       p.CancelAction = True
       return
    if Party.Vehicle is not None:
       Message("  Leave " + Party.Vehicle.Name + " first.")
       p.CancelAction = True
       return
    Message("  You start flying!")
    Party.Flying = 4


def Cast_shockwave(p):
    Message("  The ground shakes.")
    for ch in Town.EachCharacterInRange(p.PC.Pos, 10):
        if ch != p.PC and Town.Visible(ch.Pos):
            ch.Damage(p.PC, Maths.Rand(2 + p.PC.Pos.DistanceTo(ch.Pos) / 2, 1, 6), 0, eDamageType.MAGIC)

def Cast_major_blessing(p):
    for pc in Party.EachAlivePC():
        pc.Haste(min(8, 3 + Bonus(p.PC, p.UsedItem)))
        pc.PoisonWeapon(2)
        pc.Bless(4)
        Animation_Missile(p.PC.Pos, pc.Pos, 14, True)
        Animation_Pause()
    Message("  Party blessed!")

def Cast_mass_paralysis(p):
    Message("  Enemy paralyzed:")
    for npc in Town.EachCharacterInRange(p.PC.Pos, p.Spell.Range, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           Animation_Missile(p.PC.Pos, npc.Pos, 15, True)
           Animation_Pause()
           npc.Paralyze(1000, 5)

def Cast_protection(p):
    p.PCTarget.IncStatus(eAffliction.INVULNERABLE, 2 + Bonus(p.PC, p.UsedItem) + Maths.Rand(2,1,2))
    for pc in Party.EachAlivePC():
        pc.IncStatus(eAffliction.MAGIC_RESISTANCE, 4 + p.PC.Level / 3 + Bonus(p.PC, p.UsedItem))
    Message("  Party protected.")

def Count_major_summon(caster, spell, item):
    return Maths.MinMax(1, 5, caster.Level / 8 + Bonus(caster, item) / 2)

def Cast_major_summon(p):
    for loc in p.TargetList:
        duration = Maths.Rand(7, 1, 4) + Bonus(p.PC, p.UsedItem)
        if not Town.SummonMonster(p.PC, NPCRecord.GetSummonMonster(3), loc, duration):
            Message("  Summon failed.")

def Cast_force_barrier(p):
    Sound.Play("068_identify")
    Town.HitArea(p.Target, 1, Maths.Rand(7, 2, 7),0, eDamageType.FIRE, Pattern.Single, False, p.PC)
    Town.MakeForceBarrier(p.Target)
    if Town.FieldThere(p.Target, Field.FORCE_BARRIER):
        Message("  You create the barrier.")
    else:
        Message("  Failed.")

def Cast_quickfire(p):
    Town.MakeQuickfire(p.Target)

def Count_death_arrows(caster, spell, item):
    return caster.Level / 8 + Bonus(caster, item) / 3

def Cast_death_arrows(p):
    for npc in p.NPCTargetList:
        damage = Maths.Rand(3, 0, 10) + p.PC.Level + 3 * Bonus(p.PC, p.UsedItem)
        npc.Damage(p.PC, damage, 0, eDamageType.MAGIC)

def Cast_minor_bless(p):
    p.PCTarget.Bless(2)

def Cast_minor_heal(p):
    p.PCTarget.Heal(Maths.Rand(2, 1, 4))

def Cast_weaken_poison(p):
    p.PCTarget.Cure(1 + Maths.Rand(1, 0 , 2) + Bonus(p.PC, p.UsedItem)/2)

def Cast_turn_undead(p):
    if p.NPCTarget.Record.Genus != eGenus.UNDEAD:
       Message("  Not undead.")
       p.CancelAction = True
       return
    Animation_Missile(p.PC.Pos, p.Target, 8, True, "024_priestspell")
    Wait()
    hit_chance = [20,30,40,45,50,55,60,65,69,73,77,81,84,87,90,92,94,96,97,98]
    if Maths.Rand(1,0,90) > hit_chance[Maths.MinMax(0,19,Bonus(p.PC, p.UsedItem) * 2 + Level(p.PC, p.UsedItem) * 4 - (p.NPCTarget.Level / 2) + 3)]:
       Message("  Monster resisted.")
    else:
       Town.HitArea(p.Target, 1,Maths.Rand(2,1,14),0, eDamageType.UNBLOCKABLE, Pattern.Single, False, p.PC)

def Cast_location(p):
    if Game.Mode == eMode.OUTSIDE:
       Message("  You're outside at: x " + str(Party.Pos.X) + "  y " + str(Party.Pos.X) + ".")
    else:
       Message("  You're at: x " + str(Party.Pos.X) + "  y " + str(Party.Pos.X) + ".")

def Cast_sanctuary(p):
    Message("  " + p.PCTarget.Name + " hidden.")
    p.PCTarget.IncStatus(eAffliction.INVISIBLE, max(0, Maths.Rand(0,1,3) + p.PC.Level / 4 + Bonus(p.PC, p.UsedItem)))

def Cast_symbiosis(p):
    if p.PC is p.PCTarget:
       Message("  Can't cast on self.")
       p.CancelAction = True
       return
    store_victim_health = p.PCTarget.Health
    store_caster_health = p.PC.Health
    targ_damaged = p.PCTarget.MaxHealth - p.PCTarget.Health
    while targ_damaged > 0 and p.PC.Health > 0:
       p.PCTarget.Health+=1
       r1 = Maths.Rand(1,0,100) + p.PC.Level / 2 + 3 * Bonus(p.PC, p.UsedItem)
       if r1 < 100:
          p.PC.Health -= 1
       if r1 < 50:
          p.PC.Health -= 1
       targ_damaged = p.PCTarget.MaxHealth - p.PCTarget.Health
    Message("  You absorb damage.")
    Message("  " + p.PCTarget.Name + " healed " + str(p.PCTarget.Health - store_victim_health) + ".")
    Message("  " + p.PC.Name + " takes " + str(store_caster_health - p.PC.Health) + ".")

def Cast_minor_manna(p):
    store = p.PC.Level / 3 + 2 * Bonus(p.PC, p.UsedItem) + Maths.Rand(2,1,4)
    r1 = max(0,store) / 3 + 1
    Message("  You gain " + str(r1) + " food.")
    Party.Food += r1

def Cast_sanctify(p):
    for trig in Town.TriggerSpotList:
        if trig.Pos == p.Target and trig.TriggeredBy(eTriggerSpot.CAST_SPELL):
           #The game will automatically run the TriggerSpot's Sanctify function
           return
    Message("  Nothing happens.")

def Cast_stumble(p):
    p.NPCTarget.Curse(2 + Bonus(p.PC, p.UsedItem)) # Switched with Curse from original Blades of Exile!

def Cast_bless(p):
    p.PCTarget.Bless(max(2,(p.PC.Level * 3) / 4 + 1 + Bonus(p.PC, p.UsedItem)))

def Cast_cure_poison(p):
    p.PCTarget.Cure(3 + Maths.Rand(1, 0 , 2) + Bonus(p.PC, p.UsedItem)/2)

def Cast_curse(p):
    p.NPCTarget.Curse(4 + Bonus(p.PC, p.UsedItem))  # Switched with Stumble from original Blades of Exile!

def Cast_light_p(p):
    Party.LightLevel += 210
    Town.UpdateVisible()

def Cast_wound(p):
    Town.HitArea(p.Target, 1,Maths.Rand(min(7,2 + Bonus(p.PC, p.UsedItem) + Level(p.PC, p.UsedItem) / 2),1,4),0, eDamageType.MAGIC, Pattern.Single, False, p.PC)

def Cast_summon_spirit(p):
    duration = Maths.Rand(2, 1, 5) + Bonus(p.PC, p.UsedItem)
    if not Town.SummonMonster(p.PC, NPCRecord.List[125], p.Target, duration):
        Message("  Summon failed.")

def Cast_move_mountains(p):
    Message("  You blast the area.")
    terfrom = Town.TerrainAt(p.Target)
    terto = terfrom.GetCrumbleTo()
    if terfrom != terto:
        Town.AlterTerrain(p.Target, 0, terto)
        Sound.Play("060_smallboom")
        Message("  The %s crumbles!" % (terfrom.Name))
    else:
        Message("  No effect on the %s" % (terfrom.Name))

def Cast_charm_foe(p):
    p.NPCTarget.Charm(-1 * (Bonus(p.PC, p.UsedItem) + p.PC.Level / 8))

def Cast_disease(p):
    p.NPCTarget.Disease(2 + Maths.Rand(1,0,1) + Bonus(p.PC, p.UsedItem))

def Cast_awaken(p):
    if p.PCTarget.Status(eAffliction.ASLEEP) <= 0:
       Message("  " + p.PCTarget.Name + " is already awake!")
       p.CancelAction = True
    else:
       Message("  " + p.PCTarget.Name + " wakes up.")
       p.PCTarget.SetStatus(eAffliction.ASLEEP, 0)

def Cast_heal(p):
    p.PCTarget.Heal(Maths.Rand(8, 1, 4))

def Cast_light_heal_all(p):
    r1 = Maths.Rand(3 + Bonus(p.PC, p.UsedItem), 1, 4)
    Message("  Party healed " + str(r1) + ".")
    Party.HealAll(r1)
    Sound.Play("052_magic2")

def Cast_holy_scourge(p):
    p.NPCTarget.Curse(2 + p.PC.Level / 2)

def Cast_detect_life(p):
    Message("  Monsters now on map.")
    Party.DetectMonster += 6 + Maths.Rand(1,0,6)

def Cast_cure_paralysis(p):
    if p.PCTarget.Status(eAffliction.PARALYZED) <= 0:
       Message("  " + p.PCTarget.Name + " isn't paralyzed!")
       p.CancelAction = True
    else:
       Message("  " + p.PCTarget.Name + " can move now.")
       p.PCTarget.SetStatus(eAffliction.PARALYZED, 0)

def Cast_manna(p):
    store = p.PC.Level / 3 + 2 * Bonus(p.PC, p.UsedItem) + Maths.Rand(2,1,4)
    r1 = max(0,store)
    Message("  You gain " + str(r1) + " food.")
    Party.Food += r1

def Cast_forcefield(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.FORCE_WALL, p.PC)

def Cast_cure_disease(p):
    Message("  " + p.PCTarget.Name + " recovers.")
    r1 = 2 + Maths.Rand(1,0,2) + Bonus(p.PC, p.UsedItem) / 2
    p.PCTarget.DecStatus(eAffliction.DISEASE, r1, 0)

def Cast_restore_mind(p):
    Message("  " + p.PCTarget.Name + " restored.")
    r1 = 2 + Maths.Rand(1,0,2) + Bonus(p.PC, p.UsedItem) / 2
    p.PCTarget.DecStatus(eAffliction.DUMB, r1, 0)

def Count_smite(caster, spell, item):
    return Maths.MinMax(1, 8, caster.Level / 4 + Bonus(caster, item) / 2)

def Cast_smite(p):
    for loc in p.TargetList:
        Town.HitArea(loc, 1, Maths.Rand(2, 1, 5),0, eDamageType.COLD, p.TargetPattern, False, p.PC)

def Cast_cure_party(p):
    Message("  Party cured.")
    for pc in Party.EachAlivePC():
        pc.Cure(3 + Bonus(p.PC, p.UsedItem))

def Cast_curse_all(p):
    Message("  Enemy cursed:")
    for npc in Town.EachCharacterInRange(p.PC.Pos, p.Spell.Range, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           Animation_Missile(p.PC.Pos, npc.Pos, 8, True)
           Animation_Pause()
           npc.Curse(3 + Bonus(p.PC, p.UsedItem))

def Cast_dispel_undead(p):
    if p.NPCTarget.Record.Genus != eGenus.UNDEAD:
       Message("  Not undead.")
       p.CancelAction = True
       return
    Animation_Missile(p.PC.Pos, p.Target, 8, True)
    Wait()
    hit_chance = [20,30,40,45,50,55,60,65,69,73,77,81,84,87,90,92,94,96,97,98]
    if Maths.Rand(1,0,90) > hit_chance[Maths.MinMax(0,19,Bonus(p.PC, p.UsedItem) * 2 + Level(p.PC, p.UsedItem) * 4 - (p.NPCTarget.Level / 2) + 3)]:
       Message("  Monster resisted.")
    else:
       Town.HitArea(p.Target, 1, Maths.Rand(6,1,14), 0, eDamageType.UNBLOCKABLE, Pattern.Single, False, p.PC)

def Cast_remove_curse(p):
    for i in p.PCTarget.EachItemHeld():
        if i.Cursed and Maths.Rand(1,0,200) - 10 * Bonus(p.PC, p.UsedItem) < 60:
           i.Cursed = False
    Sound.Play("052_magic2")
    Message("  Your items glow.")

def Count_sticks_to_snakes(caster, spell, item):
    return caster.Level / 5 + Bonus(caster, item) / 2

def Cast_sticks_to_snakes(p):
    for loc in p.TargetList:
        duration = Maths.Rand(2, 1, 5) + Bonus(p.PC, p.UsedItem)
        if Maths.Rand(1, 0, 7) == 1:
           npcr = NPCRecord.List[100]
        else:
           npcr = NPCRecord.List[99]
        if not Town.SummonMonster(p.PC, npcr, loc, duration):
            Message("  Summon failed.")

def Cast_martyrs_shield(p):
    Message("  " + p.PCTarget.Name + " shielded.")
    r1 = max(0, Maths.Rand(1,1,3) + p.PC.Level / 4 + Bonus(p.PC, p.UsedItem)) #Original BoE used ran(0,1,3) which would always return 0!
    p.PCTarget.IncStatus(eAffliction.MARTYRS_SHIELD, r1)

def Cast_cleanse(p):
    Message("  " + p.PCTarget.Name + " cleansed.")
    p.PCTarget.SetStatus(eAffliction.DISEASE, 0)
    p.PCTarget.SetStatus(eAffliction.WEBS, 0)

def Cast_firewalk(p):
    Message("  You are now firewalking.")
    Party.Firewalk += p.PC.Level / 12 + 2

def Cast_bless_party(p):
    for pc in Party.EachAlivePC():
        Animation_Missile(p.PC.Pos, pc.Pos, 8, True)
        Animation_Pause()
    Wait()
    for pc in Party.EachAlivePC():
        pc.Bless(p.PC.Level / 3, True)
    Sound.Play("004_bless")
    Message("  Party blessed.")

def Cast_major_heal(p):
    p.PCTarget.Heal(Maths.Rand(14, 1, 4))

def Cast_raise_dead(p):
    item = p.PC.HasItemWithAbility(eItemAbil.RESURRECTION_BALM)
    if item is None:
       Message("  Need resurrection balm.")
       p.CancelAction = True
       return
    p.PC.UseItemCharge(item)

    if p.PCTarget.LifeStatus == eLifeStatus.DEAD:
       if Maths.Rand(1,1,p.PCTarget.Level / 2) == 1:
          Message("  " + p.PCTarget.Name + " now dust.")
          Sound.Play("005_explosion")
          p.PCTarget.LifeStatus = eLifeStatus.DUST
       else:
          for n in range(3):
              if Maths.Rand(1,0,2) < 2:
                 p.PCTarget.SetSkill(n, max(1,p.PCTarget.GetSkill(n)-1))
          p.PCTarget.Health = 1
          p.PCTarget.LifeStatus = eLifeStatus.ALIVE
          Message("  " + p.PCTarget.Name + "  raised.")
          Sound.Play("052_magic2")
    else:
         Message("  Didn't work.")

def Cast_flamestrike(p):
    damage = min(9, 1 + (Level(p.PC, p.UsedItem) * 2) / 3 + Bonus(p.PC, p.UsedItem)) + 1
    damage = damage * 14 / 10
    if damage <= 0: damage = 1
    Town.HitArea(p.Target, damage,1,6, eDamageType.FIRE, p.TargetPattern, True, p.PC)

def Cast_mass_sanctuary(p):
    Message("  Party hidden.")
    for pc in Party.EachAlivePC():
        pc.IncStatus(eAffliction.INVISIBLE, max(0, Maths.Rand(0,1,3) + p.PC.Level / 6 + Bonus(p.PC, p.UsedItem)))

def Count_summon_host(caster, spell, item):
    return 5

def Cast_summon_host(p):
    for loc in p.TargetList:
        duration = Maths.Rand(2, 1, 4) + Bonus(p.PC, p.UsedItem)
        if loc == p.TargetList[0]:
           npcr = NPCRecord.List[126]
        else:
           npcr = NPCRecord.List[125]
        if not Town.SummonMonster(p.PC, npcr, loc, duration):
            Message("  Summon failed.")

def Cast_shatter(p):
    Message("  You send out a burst of energy.")
    for x in range(p.PC.Pos.X - 1, p.PC.Pos.X + 2):
        for y in range(p.PC.Pos.Y - 1, p.PC.Pos.Y + 2):
            Town.AlterTerrain(Location(x,y), Town.TerrainAt(Location(x,y)).GetCrumbleTo())

def Cast_dispel_fields_p(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.DISPEL, p.PC)

def Cast_heal_all(p):
    r1 = Maths.Rand(6 + Bonus(p.PC, p.UsedItem), 1, 4)
    Message("  Party healed " + str(r1) + ".")
    Party.HealAll(r1)
    Sound.Play("052_magic2")

def Cast_revive(p):
    Message("  " + p.PCTarget.Name + " healed.")
    p.PCTarget.Heal(250)
    p.PCTarget.SetStatus(eAffliction.POISON, 0)

def Cast_hyperactivity(p):
    Message("  Party is now really, REALLY awake.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.WEBS, 0)
        pc.SetStatus(eAffliction.DISEASE, 0)

def Cast_destone(p):
    if p.PCTarget.LifeStatus == eLifeStatus.STONE:
       p.PCTarget.LifeStatus = eLiftStatus.ALIVE
       Message("  " + p.PCTarget.Name + " destoned.")
       Sound.Play("053_magic3")
    else:
       Message("  Wasn't stoned.")
       p.CancelAction = True

def Cast_guardian(p):
    duration = Maths.Rand(6, 1, 4) + Bonus(p.PC, p.UsedItem)
    if not Town.SummonMonster(p.PC, NPCRecord.List[122], p.Target, duration):
        Message("  Summon failed.")

def Cast_mass_charm(p):
    Message("  Enemy charmed:")
    for npc in Town.EachCharacterInRange(p.PC.Pos, p.Spell.Range, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           Animation_Missile(p.PC.Pos, npc.Pos, 14, True)
           Animation_Pause()
           npc.Charm(28 - Bonus(p.PC, p.UsedItem))

def Cast_protective_circle(p):
    protect_pat = Pattern(0,6,6,6,6,6,6,6,0, \
                          6,10,10,10,10,10,10,10,6, \
                          6,10,11,11,11,11,11,10,6, \
                          6,10,11,8,8,8,11,10,6, \
                          6,10,11,8,8,8,11,10,6, \
                          6,10,11,8,8,8,11,10,6, \
                          6,10,11,11,11,11,11,10,6, \
                          6,10,10,10,10,10,10,10,6, \
                          0,6,6,6,6,6,6,6,0)
    Town.PlaceFieldPattern(protect_pat, p.PC.Pos, None, p.PC)
    Sound.Play("024_priestspell")
    Message("  Protective field created.")

def Cast_pestilence(p):
    Message("  Enemy diseased:")
    for npc in Town.EachCharacterInRange(p.PC.Pos, p.Spell.Range, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           Animation_Missile(p.PC.Pos, npc.Pos, 14, True)
           Animation_Pause()
           npc.Disease(3 + Bonus(p.PC, p.UsedItem))

def Cast_revive_all(p):
    r1 = Maths.Rand(7 + Bonus(p.PC, p.UsedItem), 1, 4) * 2
    Message("  Party revived.")
    Party.HealAll(r1)
    for pc in Party.EachAlivePC():
        pc.Cure(3 + Bonus(p.PC, p.UsedItem))
    Sound.Play("052_magic2")
    Sound.Play("053_magic3")

def Cast_ravage_spirit(p):
    if p.NPCTarget.Record.Genus != eGenus.DEMON:
       Message("  Not a demon.")
       p.CancelAction = True
       return
    Animation_Missile(p.PC.Pos, p.Target, 2, True)
    Wait()
    hit_chance = [20,30,40,45,50,55,60,65,69,73,77,81,84,87,90,92,94,96,97,98]
    if Maths.Rand(1,0,100) > hit_chance[Maths.MinMax(0,19,Level(p.PC, p.UsedItem) * 4 - p.NPCTarget.Level + 10)]:
       Message("  Demon resisted.")
    else:
       Town.HitArea(p.Target, 1,Maths.Rand(8 + Bonus(p.PC, p.UsedItem) * 2,1,11),0, eDamageType.UNBLOCKABLE, Pattern.Single, False, p.PC)

def Cast_resurrect(p):
    item = p.PC.HasItemWithAbility(eItemAbil.RESURRECTION_BALM)
    if item is None:
       Message("  Need resurrection balm.")
       p.CancelAction = True
       return
    p.PC.UseItemCharge(item)

    if p.PCTarget.LifeStatus == eLifeStatus.DEAD or p.PCTarget.LifeStatus == eLifeStatus.DUST:
          for n in range(3):
              if Maths.Rand(1,0,2) < 1:
                 p.PCTarget.SetSkill(n, max(1,p.PCTarget.GetSkill(n)-1))
          p.PCTarget.Health = 1
          p.PCTarget.LifeStatus = eLifeStatus.ALIVE
          Message("  " + p.PCTarget.Name + "  raised.")
          Sound.Play("052_magic2")
    else:
         Message("  Was OK.")
         p.CancelAction = True

def Cast_divine_thud(p):
    damage = min(18, (Level(p.PC, p.UsedItem) * 7) / 10 + 2 * Bonus(p.PC, p.UsedItem))
    Town.HitArea(p.Target, damage, 1, 6, eDamageType.MAGIC, p.TargetPattern, True, p.PC)

def Cast_avatar(p):
    Message("  " + p.PC.Name + " is an avatar!")
    p.PC.Heal(200)
    p.PC.Cure(8)
    p.PC.SetStatus(eAffliction.BLESS_CURSE, 8)
    p.PC.SetStatus(eAffliction.HASTE_SLOW, 8)
    p.PC.SetStatus(eAffliction.INVULNERABLE, 3)
    p.PC.SetStatus(eAffliction.MAGIC_RESISTANCE, 8)
    p.PC.SetStatus(eAffliction.WEBS, 0)
    p.PC.SetStatus(eAffliction.DISEASE, 0)
    p.PC.SetStatus(eAffliction.DUMB, 0)
    p.PC.SetStatus(eAffliction.MARTYRS_SHIELD, 8)

def Cast_wall_of_blades(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.BLADE_WALL, p.PC)

def Cast_word_of_recall(p):
    Animation_FadeDown()
    Wait()
    Party.Pos = Scenario.TownStartPos
    Party.MoveToMap(Scenario.StartTown)

def Cast_major_cleansing(p):
    Message("  Party cleansed.")
    for pc in Party.EachAlivePC():
        pc.SetStatus(eAffliction.WEBS, 0)
        pc.SetStatus(eAffliction.DISEASE, 0)

#####################################################################################################
def Use_Summoning(p):
    if Town.SummonMonster(p.PC, NPCRecord.List[UsedItem.AbilityStrength], p.PC.Pos, 50) == False:
       Message("  Summon failed.")

def Use_Mass_Summoning(p):
    r1 = Maths.Rand(6,1,4)
    j = Maths.Rand(1,3,5)
    for i in range(j):
        if Town.SummonMonster(p.PC, NPCRecord.List[UsedItem.AbilityStrength], p.PC.Pos, r1) == False:
           Message("  Summon failed.");

def Use_Acid_Spray(p):
    p.NPCTarget.Acid(Level(p.PC, p.UsedItem))

def Use_Stinking_Cloud(p):
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.STINK_CLOUD, p.PC)

def Use_Paralysis(p):
    Message("  It shoots a silvery beam.")
    p.NPCTarget.Paralyze(500,0)

def Use_Web(p):
    Message("  It explodes!")
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.WEB, p.PC)

def Use_Strengthen(p):
    Game.AdDMessage("  It shoots a fiery red ray.")
    p.NPCTarget.Bless(2)

def Use_Quickfire(p):
    Message("  Fire pours out!")
    Town.MakeQuickfire(p.PC.Pos)

def Use_Mass_Charm(p):
    Message("  It throbs, and emits odd rays.")
    for npc in Town.EachCharacterInRange(p.PC.Pos, 8, False, True):
        if npc.IsABaddie and Town.CanSee(p.PC.Pos, npc.Pos) < 5:
           npc.Charm(8)

def Use_Magic_Map(p):
    if Town.PreventMapping or Town.PreventScrying:
        Message("  It doesn't work.")
        p.CancelAction = True
    else:
        p.PC.UseItemCharge(p.UsedItem)
        Message("  You have a vision.")
        for  y in range(Town.Height):
             for x in range(town.Width):
                 Town.MakeExplored(Location(x, y))

def Use_Ice_Wall(p):
    Message("  It shoots a blue sphere!")
    Town.PlaceFieldPattern(p.TargetPattern, p.Target, Field.ICE_WALL, p.PC)




#####################################################################################################

def Level(caster, item):
  if item is None:
    return 1 + caster.Level / 2
  else:
    return Maths.MinMax(2,20, item.AbilityStrength * 2 + 1)


def Bonus(caster, item):
  if item is None:
    return caster.GetSkillBonus(eSkill.INTELLIGENCE)
  else:
    return 1
