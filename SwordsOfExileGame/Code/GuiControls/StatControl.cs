using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    //delegate void ChangeStatHandler(eSkill stat, bool increase);

    class StatControl : Control
    {
        eSkill Stat;
        PCType PC { get { return Game.CurrentParty.CurrentPC; } }
        bool canChange, creationMode;
        int[] fixedMin; //when the control is created save the stat value, so that the player can't lower it past what it started as.

        enum eButton { NONE, DEC, INC };
        eButton pressedButton = eButton.NONE;

        static string[] statnames = {"Strength", "Dexterity", "Intelligence", "Edged Weapons", "Bashing Weapons",
                                        "Pole Weapons", "Thrown Missiles", "Archery", "Defense", "Mage Spells",
                                        "Priest Spells", "Mage Lore", "Alchemy", "Item Lore", "Disarm Traps",
                                        "Lockpicking", "Assassination", "Poison", "Luck"};
        static string[] statdesc = {
            "Measures how much brute strength the character possesses. High strength increases damage done in combat, improves odds of kicking down doors, and has other, more subtle effects.",
            "Measures how nimble the character is. High dexterity gives a better chance of hitting in combat (esp. with missile weapons) and makes the character harder to hit. High dexterity also makes picking locks and disarming traps easier.",
            "Measures mental strength and dexterity. High intelligence also makes your spells more effective, sometimes very much so. Intelligence below 4 makes your spells works poorly.",
            "Makes you better at using daggers, swords, axes, etc.",
            "Makes you better at using clubs, maces, hammers, flails, etc.",
            "Makes you better at using spears of all sorts, halberds, etc.",
            "Makes you better at using darts, javelins, and throwing axes.",
            "Makes you better at using a bow and arrows, crossbows, or slings.",
            "This skill has three effects. It determines how well a character does at parrying, decreases the penalty in combat from bulky armor, and occasionally decreases the damage taken from enemies weapons.",
            "Having a certain level of this skill enables you to cast mage spells of up to that level.",
            "Having a certain level of this skill enables you to cast priest spells of up to that level.",
            "You will occasionally need to decipher strange magical readings. This skill determines how good you are at this. If your skill is high enough, you may gain a spell or a valuable piece of information.",
            "You will eventually gain the ability to make magic potions. To make a given potion, however, your Alchemy skill much be above a certain level. The higher it is above this level, the better the chance of succeeding.",
            "Having Item Lore skill gives you a chance of having the items from slain monsters be identified when you find them. The more of this skill that is present, the higher the chance of this happening.",
            "Many chests and some corridors will have traps on them, which can be devastating. The higher this skill, the better your chance of disarming them.",
            "Many towns and dungeons will have locked doors. A character with some of this skill and lock picks equipped can try to pick them. The higher this skill, the better.",
            "Sometimes, when a character attacks a much weaker monster, the blow will do a good deal of extra damage. The more of this skill you have, the better the chance of this happening, and the stronger the monsters it can happen to.",
            "You will find poisons, which you can put on your weapons for a extra damage. Having a few levels in this skill will make it more likely you will put the poison on at full strength, and the less likely you will nick yourself with the poison accidentally.",
            "This skill is expensive, but can be a bargain at twice the cost. Its effects are pervasive, subtle, powerful, and sometimes irreplaceable."};

        static string healthdesc = "Your health is a measure of how much punishment you can take before dying - the more the better. Whenever you get hit, you lose some health. Taking damage when your health is down to 0 will kill you.";
        static string spelldesc = "Your spell points are what you expend to cast spells. Each spell drains away some of your spell points. Time and rest restore them. When creating a character, you get 3 bonus spell points for every level of Mage and Priest Spells skill you buy.";

        public StatControl(GuiWindow p, int xb, int yb, int tno, eSkill stat, bool can_change, bool creating_party)
            : base(p, xb, yb, 226, 18, tno)
        {
            Stat = stat;
            creationMode = creating_party;
            canChange = can_change;
            fixedMin = new int[Game.CurrentParty.PCList.Count];
            int n = 0;
            if (!creating_party)
                foreach (PCType pc in Game.CurrentParty.PCList) fixedMin[n++] = pc.GetSkill(stat);
            else
                foreach (PCType pc in Game.CurrentParty.PCList)
                    if (stat == eSkill.HEALTH) fixedMin[n++] = 6;
                    else if (stat == eSkill.STRENGTH || stat == eSkill.DEXTERITY || stat == eSkill.INTELLIGENCE) fixedMin[n++] = 1;
        }

        public override void Draw(SpriteBatch sb, int xOffset, int yOffset)
        {
            int dx = X + xOffset, dy = Y + yOffset;
            string sn;

            if (Stat == eSkill.HEALTH)
            { sn = "Health"; }
            else if (Stat == eSkill.SPELLPTS)
            { sn = "Spell Points"; }
            else
            { sn = statnames[(int)Stat]; }

            int v = PC.GetSkill(Stat), cost = PC.GetSkillCost(Stat), price = PC.GetSkillPrice(Stat);


            sb.DrawString(Gfx.TinyFont, sn, new Vector2(dx, dy + 2), Color.White);
            sb.DrawString(Gfx.TinyFont, Convert.ToString(cost), new Vector2(dx + 100, dy + 2), Color.Green);
            if (!creationMode) sb.DrawString(Gfx.TinyFont, Convert.ToString(price), new Vector2(dx + 135, dy + 2), Color.LightBlue);
            sb.DrawString(Gfx.SmallBoldFont, Convert.ToString(v), new Vector2(dx + 170, dy + 2), Color.White);

            if (canChange) //Only draw buttons if the user can change the stat (trainer / character creation)
            {
                Color col = pressedButton == eButton.DEC ? Color.Red : (v <= fixedMin[PC.Slot] ? Color.DarkSlateGray : Color.White);
                //if (value <= Min) col = Color.Gray;
                sb.Draw(Gfx.NewGui, new XnaRect(dx + 190, dy, 18, 18), new XnaRect(117, 0, 18, 18), col);
                //if (value <= Min) col = Color.Gray; else col = Color.White;

                bool can_increase = (creationMode || Game.CurrentParty.Gold >= price) && PC.SkillPoints >= cost;

                col = pressedButton == eButton.INC ? Color.Red : (can_increase ? Color.White : Color.DarkSlateGray);
                sb.Draw(Gfx.NewGui, new XnaRect(dx + 208, dy, 18, 18), new XnaRect(99, 0, 18, 18), col);
            }
        }

        public override bool Handle(int xOffset, int yOffset)
        {
            if (!Enabled || !Visible ) return false;
            
            //return base.Handle(xOffset, yOffset);
            int dx = X + xOffset, dy = Y + yOffset;

            if (Gui.Ms.X >= dx && Gui.Ms.Y > dy && Gui.Ms.X < dx + Width && Gui.Ms.Y < dy + Height)
            {
                if (Gui.Ms.X < dx + 190)
                {
                    //if (ToolTip.WaitForToolTip())
                    //{
                    if (Stat == eSkill.HEALTH)
                        new ToolTipV2(false, new XnaRect(dx, dy, Width, Height), healthdesc, 200);//ToolTip(healthdesc, 200, false);
                    else if (Stat == eSkill.SPELLPTS)
                        new ToolTipV2(false, new XnaRect(dx, dy, Width, Height), spelldesc, 200);//ToolTip(spelldesc, 200, false);
                    else
                        new ToolTipV2(false, new XnaRect(dx, dy, Width, Height), statdesc[(int)Stat], 200); //ToolTip(statdesc[(int)Stat], 200, false);
                    //}
                    return false;
                }
                else
                {
                    if (!canChange) return false;
                    if (Gui.Ms.X < dx + 208) //Press 'Decrase button'?
                    {
                        if (Gui.LMBHit)
                        {
                            if (PC.IsAlive() && PC.GetSkill(Stat) > fixedMin[PC.Slot])
                            {
                                pressedButton = eButton.DEC;
                                return true;
                            }
                        }
                        else if (!Gui.LMBDown && pressedButton == eButton.DEC)
                        {
                            Sound.ButtonSound();
                            pressedButton = eButton.NONE;
                            PC.SkillPoints += PC.GetSkillCost(Stat);
                            if (!creationMode) Game.CurrentParty.Gold += PC.GetSkillPrice(Stat);
                            PC.SetSkill(Stat, PC.GetSkill(Stat) - (Stat == eSkill.HEALTH ? 2 : 1));
                            return true;
                        }
                    }
                    else  //Press 'Increase button'?
                    {
                        if (Gui.LMBHit)
                        {
                            if (PC.IsAlive() && (creationMode || Game.CurrentParty.Gold >= PC.GetSkillPrice(Stat)) && PC.SkillPoints >= PC.GetSkillCost(Stat))
                            {
                                pressedButton = eButton.INC;
                                return true;
                            }
                        }
                        else if (!Gui.LMBDown && pressedButton == eButton.INC)
                        {
                            Sound.ButtonSound();
                            pressedButton = eButton.NONE;
                            PC.SkillPoints -= PC.GetSkillCost(Stat);
                            if (!creationMode) Game.CurrentParty.Gold -= PC.GetSkillPrice(Stat);
                            PC.SetSkill(Stat, PC.GetSkill(Stat) + (Stat == eSkill.HEALTH ? 2 : 1));

                            return true;
                        }
                    }
                }
            }
            else
            {
                if (!Gui.LMBDown) pressedButton = eButton.NONE;
            }

            return false;
        }
    }

}