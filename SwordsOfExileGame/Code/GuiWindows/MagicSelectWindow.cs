﻿using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class MagicWindow : GuiWindow
{
    public static MagicWindow Instance = null;

    private static PCType LastPCCaster = null;
    private static MagicSpell LastSpell = null;

    private List<MagicSpell> PCSelectedSpell;
    public PCType Caster = null;
    private PCType TargetedPC = null;

    private ListBox spellListBox;
    //List<OptionPictureButton> casterButtons = new List<OptionPictureButton>();
    private List<OptionPictureButton> targetPCButtons = new();
    private List<OptionButton> spellLevelButtons = new();

    private OptionPictureButton mageButton, priestButton;
    private PictureBox casterPic;
    private RichTextBox casterInfo;

    //List<Label> casterInfo = new List<Label>();
    private Button /*toggleFavourites, addToFavourites,*/ cancelButton, castButton;
    private Label selectPCLabel;

    private MagicSpell selectedSpell;
    private int currentSpellLevel = 1;
    private bool currentIsMage;
    private Label selSpellTitle;
    private RichTextBox selSpellDesc;

    //public static void Update(PCType pc)
    //{
    //    if (instance != null) instance.UpdateCaster(pc);
    //}

    public MagicWindow(bool do_mage)
        : base(0, 0, 500, 400, true, true, false, true, true)
    {
        Action.LockActions = eAction.MAGIC_LOCK_ACTIONS;

        Instance = this; //Not modal, but stop all actions except clicking portrait to change PC
        Position(-2, -2);
        spellListBox = AddListBox(changedSelected, 0, 130, 200, InnerHeight - 70, -1);
        spellListBox.Position(10, 60, -1, -1);
        cancelButton = AddButton(pressCancel, "Cancel", 358, InnerHeight - 30, 110, 30);
        castButton = AddButton(pressCast, "Cast", 238, InnerHeight - 30, 110, 30);
        CancelKeyControl = cancelButton;
        OKKeyControl = castButton;

        mageButton = AddOptionPictureButton(pressButton, new XnaRect(0, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(10, 10, 37, 37), 28);
        priestButton = AddOptionPictureButton(pressButton, new XnaRect(37, 0, 37, 37), Gfx.ButtonsGfx, new XnaRect(47, 10, 37, 37), 28);

        if (do_mage) mageButton.Pressed = true; else priestButton.Pressed = true;
        currentIsMage = do_mage;

        for (var n = 1; n <= Constants.MAX_SPELL_LEVEL; n++)
        {
            spellLevelButtons.Add(AddOptionButton(pressButton, String.Format("{0}", n), 0, 0, 27));
            spellLevelButtons[n - 1].Resize(spellLevelButtons[n - 1].Width, 22);
        }
        spellLevelButtons[0].Pressed = true;

        AddLabel("Spell Level:", priestButton.X + priestButton.Width + 10, 7, -1, -1, false);
        LineUpControls(priestButton.X + priestButton.Width + 10, 24, 0, spellLevelButtons.ToArray());

        PCSelectedSpell = new List<MagicSpell>();
        foreach (var pc in Party.PCList) PCSelectedSpell.Add(null);

        foreach (var pc in Party.PCList)
            targetPCButtons.Add(AddOptionPictureButton(pressSelectPC, new XnaRect(0,0,Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT), pc.PortraitTexture, new XnaRect(0, 0, 32, 32), 1));

        LineUpControls(236, InnerHeight - 70, 5, targetPCButtons.ToArray());
        targetPCButtons[Party.LeaderPC.Slot].Pressed = true;
        TargetedPC = Party.LeaderPC;
        selectPCLabel = AddLabel("Choose party member to cast spell on:", 236, targetPCButtons[0].Y - 20, -1, -1, false);
        selSpellTitle = AddLabel("Yo!", 250, 68, 206, 35, true);
        selSpellTitle.BackColour = Color.Black;
        selSpellTitle.Font = Gfx.TalkFontNormal;
        selSpellTitle.Padding = 4;
        selSpellTitle.SetHandler(pressButton);

        selSpellDesc = AddBlankRichTextBox(handleKeyShortcut, 250, 95, 206, 180);
        selSpellDesc.BackColour = Color.Black;
        selSpellDesc.Padding = 4;
        selSpellDesc.FontNormal = Gfx.TinyFont;
        selSpellDesc.FontBold = Gfx.SmallBoldFont;
        selSpellDesc.FontItalic = Gfx.ItalicFont;

        casterPic = AddPictureBox(Gfx.Dot, XnaRect.Empty, new XnaRect(258, 5, 48, 48));
        casterInfo = AddRichTextBox("", null, 310, 5, 160);

        var cpc = Game.Mode == eMode.COMBAT ? Party.ActivePC : Party.CurrentPC;

        if (LastSpell != null && cpc.KnownSpells.ContainsKey(LastSpell.ID) && currentIsMage == LastSpell.Mage)
        {
            currentSpellLevel = LastSpell.Level;
            PCSelectedSpell[cpc.Slot] = LastSpell;
        }
        else
        {
            currentSpellLevel = Maths.Max(1, cpc.GetSkill(currentIsMage ? eSkill.MAGE_SPELLS : eSkill.PRIEST_SPELLS));
            for (var l = currentSpellLevel; l > 1; l--)
            {
                var found = false;
                foreach (var m in cpc.KnownSpells.Values)
                {
                    if (m.Level == l && m.Mage == currentIsMage) 
                    { 
                        found = true; break; }
                }
                if (!found) currentSpellLevel--;
                else break;
            }
        }
        spellLevelButtons[currentSpellLevel - 1].OptionPress(false);
        UpdateCaster(cpc);
    }

    public override void Draw(SpriteBatch sb, int partial = 0)
    {
        base.Draw(sb, partial);

        Gfx.DrawFrame(X + 250, Y + 72, 230, 220, new Color(0, 0, 0, 0));
    }

    private void changedSelected(bool user_caused, ListBoxItem item)
    {
        if (item == null)
        {
            selSpellTitle.Text = "Select Spell";
            selSpellTitle.SetStandardToolTip(null);
            selSpellTitle.Height = 35;
            selSpellDesc.FormatText("Choose the party member to cast the spell, and the @bspell@e to cast from the list to the left.");
            //addToFavourites.Visible = false;
            foreach (var o in targetPCButtons) o.Enabled = false;
            selectPCLabel.TextColour = Color.DimGray;
            castButton.Enabled = false;
            return;
        }

        //addToFavourites.Visible = true;
        selectedSpell = item.Tag as MagicSpell;
        PCSelectedSpell[Caster.Slot] = selectedSpell;
        selSpellTitle.Text = selectedSpell.Name;
        selSpellTitle.Height = 50;

        var where = selectedSpell.GetWhereString();
            

        var cannotcast = "";
        var cancast = Caster.CanCast(selectedSpell);
        switch (cancast)
        {
            case -1: cannotcast = "Can't cast: Not learnt"; break;
            case -2: cannotcast = "Can't cast: Dumbfounded!"; break;
            case -3: cannotcast = "Can't cast: Paralyzed!"; break;
            case -4: cannotcast = "Can't cast: Asleep!"; break;
            case -5: cannotcast = "Can't cast: Mage Level too low"; break;
            case -6: cannotcast = "Can't cast: Priest Level too low"; break;
            case -7: cannotcast = "Can't cast: Not enough SP"; break;
            case -8: cannotcast = "Can't cast: Not in combat"; break;
            case -9: cannotcast = "Can't cast: Not outdoors"; break;
            case -10: cannotcast = "Can't cast: Not in town"; break;
            case -11: cannotcast = "Can't cast: Too encumbered"; break;
        }

        if (cancast < 0)
            castButton.Enabled = false;
        else
            castButton.Enabled = true;

        if (cancast > 0 && selectedSpell.Target is eSpellTarget.LIVING_PC or eSpellTarget.DEAD_PC)
        {
            foreach (var o in targetPCButtons) o.Enabled = true;
            selectPCLabel.TextColour = Color.White;
        }
        else
        {
            foreach (var o in targetPCButtons) o.Enabled = false;
            selectPCLabel.TextColour = Color.DimGray;
        }

        Keys k;
        if (!Party.SpellKeyShortcuts.TryGetValue(selectedSpell.ID, out k)) {k = Keys.None;}

        selSpellDesc.FormatText(String.Format("@bLEVEL {0} {1} SPELL@e@n@bCOST: {2} SP@n@bKEY SHORTCUT: @e@[Click to change shortcut key@]{7}@n@b{5}WHERE: {6}@e@n@n{3}@n@n@i{4}",
            selectedSpell.Level,
            selectedSpell.Mage ? "MAGE" : "PRIEST",
            selectedSpell.Cost,
            selectedSpell.Description,
            cannotcast,
            selectedSpell.Range == 0 ? "" : "RANGE: " + selectedSpell.Range + "@n", where,
            k == Keys.None ? "@lNone@e" : "@lCtrl+" + char.ToUpper(KeyHandler.GetCharsFromKeys(k, false, false)) + "@e"
        ));
    }

    private void handleKeyShortcut(int n)
    {
        new InputKeyWindow(setNewKeyShortcut, "Press a key to change the shortcut.\nValid keys are 'A' to 'Z' and '0' to '9'.\nPress 'Escape' to remove the shortcut.", false);
    }

    private void setNewKeyShortcut(Keys k)
    {
        if (k == Keys.Escape) //If press Escape, clear the spell's shortcut if it exists in the dictionary
        {
            if (Party.SpellKeyShortcuts.ContainsKey(selectedSpell.ID))
            {
                Party.SpellKeyShortcuts.Remove(selectedSpell.ID);
            }
        }
        else 
        {
            //Remove all existing entries that use this shortcut
            Party.SpellKeyShortcuts = Party.SpellKeyShortcuts.Where(n => n.Value != k).ToDictionary(n => n.Key, n => n.Value);

            //If user has pressed a new key, add it to the dictionary if that spell ID isn't in there, or change the entry for that ID if it is.

            if (!Party.SpellKeyShortcuts.ContainsKey(selectedSpell.ID))
                Party.SpellKeyShortcuts.Add(selectedSpell.ID, k);
            else
                Party.SpellKeyShortcuts[selectedSpell.ID] = k;
        }

        changedSelected(true, spellListBox.SelectedItem);
    }

    private void pressCancel(Control b)
    {
        KillMe = true;
    }

    private void pressCast(Control b)
    {
        PCType pc2 = null;
        var action = eAction.NONE;

        switch (selectedSpell.Target)
        {
            case eSpellTarget.CASTER:
                action = eAction.CastSpell;

                break;
            case eSpellTarget.LIVING_PC:
            case eSpellTarget.DEAD_PC:
                if (selectedSpell.Target == eSpellTarget.LIVING_PC && !TargetedPC.IsAlive()) return;
                if (selectedSpell.Target == eSpellTarget.DEAD_PC && (TargetedPC.IsAlive() || TargetedPC.IsGone())) return;
                action = eAction.CastSpell;
                /*Action.PC2*/ pc2 = selectedSpell.Target == 0 ? null : TargetedPC;
                break;
            case eSpellTarget.CHARACTER:
            case eSpellTarget.LOCATION:
                action = eAction.SpellTargeting;
                break;
        }
        new Action(action) { PC = Caster, Spell = selectedSpell, PC2 = pc2 };

        LastPCCaster = Caster;
        LastSpell = selectedSpell;

        KillMe = true;
    }

    private void pressButton(Control b)
    {
        if (b == selSpellTitle && selectedSpell != null)
        {
            return;
        }

        if (b == mageButton || b == priestButton)
        {
            currentIsMage = b == mageButton;
            UpdateCaster(Caster);
            return;
        }

        for (var n = 1; n <= Constants.MAX_SPELL_LEVEL; n++)
            if (b == spellLevelButtons[n - 1])
            {
                currentSpellLevel = n;
                updateSpellList();
                return;
            }
    }

    private void pressSelectPC(Control b)
    {
        var n = 0;
        for (n = 0; n < targetPCButtons.Count; n++)
            if (targetPCButtons[n] == b)
            {
                TargetedPC = Party.PCList[n];
                return;
            }
    }

    public void UpdateCaster(PCType caster)
    {
        Caster = caster;
        casterPic.SetPicture(caster.PortraitTexture, new XnaRect(0,0,Gfx.PCPORTRAITWIDTH, Gfx.PCPORTRAITHEIGHT));

        string q;
        int m = caster.GetSkill(eSkill.MAGE_SPELLS), p = caster.GetSkill(eSkill.PRIEST_SPELLS);
        if (m == 0 && p == 0)
            q = "@iNo spellcasting ability.@e";
        else if (p == 0)
            q = "@iLevel " + m + " mage@e";
        else if (m == 0)
            q = "@iLevel " + p + " priest.@e";
        else
            q = "@iLevel " + m + " mage / Level " + p + " priest.@e";

        casterInfo.FormatText("@b" + Caster.Name + "@e@n" + q + (m > 0 || p > 0 ? "@nSpell Points: @b" + Caster.SP + "@e \\ @b" + Caster.MaxSP + "@e" : ""));

        updateSpellList();
    }

    private void updateSpellList()
    {
        spellListBox.Clear();

        foreach (var ms in Caster.KnownSpells.Values)
        {
            if (ms == null) continue; //Spell does not exist in the current scenario

            if (ms.Level == currentSpellLevel && ms.Mage == currentIsMage)
            {
                if (Caster.CanCast(ms) > 0)
                    spellListBox.AddItem(String.Format("{0} ({1})", ms.Name, ms.Cost), ms.Mage ? Color.Fuchsia : Color.LightSkyBlue, ms, false);
                else
                    spellListBox.AddItem(String.Format("{0} ({1})", ms.Name, ms.Cost), Color.DarkGray, ms, true);
            }
        }

        if (PCSelectedSpell[Caster.Slot] == null)
        {
            spellListBox.SelectedItem = null;
            spellListBox.RevealItem(null);
        }
        else
        {
            foreach (var l in spellListBox.Items)
                if (l.Tag == PCSelectedSpell[Caster.Slot])
                {
                    spellListBox.SelectedItem = l;
                    spellListBox.RevealItem(l);
                    return;
                }
            spellListBox.SelectedItem = null;
        }

    }

    private PCType firstMagicUser()
    {
        foreach (var pc in Party.EachAlivePC())
        {
            if (pc.GetSkill(eSkill.MAGE_SPELLS) > 0 || pc.GetSkill(eSkill.PRIEST_SPELLS) > 0) return pc;
        }
        return null;
    }

    public override void Close()
    {
        base.Close();
        Action.LockActions = eAction.NONE;
        //Instance = null;
    }

    public override bool Handle()
    {
        var interacted = base.Handle();

        var keys = KeyHandler.GetAllKeysHit();

        if (keys != Keys.None && (KeyHandler.KeyDown(Keys.LeftControl) || KeyHandler.KeyDown(Keys.RightControl)))
        {
            KeyHandler.FlushHitKey();
            foreach (var entry in Party.SpellKeyShortcuts)
            {
                if (keys == entry.Value)
                {
                    MagicSpell m;
                    if (Caster.KnownSpells.TryGetValue(entry.Key, out m))
                    {
                        currentIsMage = m.Mage;
                        spellLevelButtons[m.Level - 1].OptionPress(true);

                        foreach (var i in spellListBox.Items)
                        {
                            if (i.Tag == m)
                            {
                                spellListBox.SelectedItem = i;
                                break;
                            }
                        }
                        return true;
                    }
                    else
                        break;
                }
            }
        }

        return interacted;
    }
}