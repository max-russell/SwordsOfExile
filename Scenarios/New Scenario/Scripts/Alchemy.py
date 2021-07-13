def DoAlchemy(pc, recipe):

    fail_chance = [50,40,30,20,10,8,6,4,2,0,0,0,0,0,0,0,0,0,0,0]
    myskill = pc.GetSkill(eSkill.ALCHEMY);
    r1 = Maths.Rand(1,0,100)

    if recipe.Creates == None:
       Message("Alchemy: The item this recipe creates doesn't exist in this scenario.")
       return

    if recipe.Creates == None or r1 < fail_chance[Maths.Min(myskill,19)]:
        Message("Alchemy: Failed.")
        Sound.Play("041_darn")
    else:
        Sound.Play("008_bubbles")

        quantity = recipe.Amount
        if myskill - recipe.Skill >= 5:
            quantity += 1
        if myskill - recipe.Skill >= 11:
            quantity += 1

        i = recipe.Creates.Copy(True, quantity)
        pc.AddItem(i, True)

        Message("Alchemy: Successful.")
