using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;
using MonoGame.Extended.BitmapFonts;

namespace SwordsOfExileGame
{
    /*Example of Animation setups:
    
     *  new Animation_Attack(----)
     *  new Animation Damage(----)
     *  new Animation_HoldQueue(500)
     *  new Animation_Death(-----)
     *  
     *    This will run the attack and damage animations simultaneously. When both have finished there will be a 500ms pause, and then
     *    the Death animation will begin.
    */

    public class Animation
    {
        static List<Animation> animationList = new List<Animation>();
        protected static void RemoveAnim(Animation a) { animationList.Remove(a); }
        public static void CancelAll() { animationList.Clear(); }
        public static bool NoAnimationsRunning() { return animationList.Count == 0 && (Gfx.FadeMode == 0 || Gfx.FadeMode == 2); }

        public static bool OnlyMovingAnimationsRunning() {// return animationList.Count == 0 || animationList.Find(n => !(n is Animation_Move)) != null; }
            if (animationList.Count == 0) return true;
            Animation finded = animationList.Find(n => !(n is Animation_Move || n is Animation_VehicleMove || n is Animation_CrateMove));
            return finded == null;
        }

        protected int Time, Duration;
        protected bool started = false;
        protected int animSound;

        public static void AdvanceAll(int ms_passed)
        {
            //Go through all the animations in the list and advance each one (Goes in reverse order)
            //If we come to a HoldQueue object it does nothing except prevent all the animations ahead of it in the
            //queue running until all animations behind it have finished.

            //We keep a list of all the sounds that have been triggered this turn so that each type of sound is only played once per turn.
            //This is to stop things like explosions when multiple targets get hit at the same time and all want to play a sound. With this
            //only one sound plays rather than multiple identical sounds.

            for (int n = animationList.Count - 1; n >= 0; n--)
            {
                Animation a = animationList[n];

                if (!(a is Animation_Move || a is Animation_VehicleMove || a is Animation_CrateMove || a is Animation_Hold || a is Animation_Pause)) 
                    new Action(eAction.NONE);

                if (a is IAnimHold)
                    if (n == animationList.Count - 1)
                        a.AdvanceAnim(ms_passed);//No animations remaining before this one, so it can now be removed
                    else
                        break; //Otherwise, exit the loop so any animations still queued are on hold.
                else
                {
                    if (!a.AdvanceAnim(ms_passed))
                        if (a is Animation_Pause) break; //If the pause time is not over, don't run any animations after this
                }

            }
        }

        /// <summary>
        /// Returns all the queued Overlay animations in the list for drawing, as long as they are running.
        /// </summary>
        /// <returns></returns>
        public static IEnumerable<IAnimOverlay> EachOverlayAnim()
        {
            foreach (Animation a in animationList)
            {
                if (a is IAnimOverlay && a.Time > 0)
                    yield return (IAnimOverlay)a;
            }
        }
        public static IEnumerable<IAnimUnderlay> EachUnderlayAnim()
        {
            foreach (Animation a in animationList)
            {
                if (a is IAnimUnderlay /*&& a.Time > 0*/)
                    yield return (IAnimUnderlay)a;
            }
        }

        public Animation(string sound)
        {
            animSound = Sound.IndexOf(sound);
            Duration = Sound.Duration(sound);
            animationList.Insert(0, this);
        }
        public Animation(int duration, int sound_index)
        {
            animSound = sound_index;
            if (duration > 0) Duration = duration;
            else Duration = Sound.Duration(sound_index);
            animationList.Insert(0, this);
        }
        public Animation(int duration, string sound)
        {
            animSound = Sound.IndexOf(sound);
            Duration = duration;
            animationList.Insert(0, this);
        }

        protected virtual bool AdvanceAnim(int ms_passed)
        {
            if (!started)
            {
                started = true;
                if (animSound != -1)
                {
                    Sound.Play(animSound);
                }
            }

            Time += ms_passed;
            if (Time >= Duration)
            {
                RemoveAnim(this);
                return true;
            }
            return false;
        }

        protected float asFraction(int t)
        {
            return (float)t / (float)Duration;
        }

        //Will only work if animation has not yet started.
        public void SetSound(string s)
        {
            if (Duration > 0)
                animSound = Sound.IndexOf(s);
        }
    }

    /// <summary>
    /// A Hold is a special animation class. It only starts running when all animations before it in the queue are over, and it
    /// suspends all animations after it in the queue from starting until it has finished. It does nothing itself except pause for a
    /// certain amount of time, although the pause can be 0, so it will act only to hold the queue up.
    /// </summary>
    public class Animation_Hold : Animation, IAnimHold
    {
        public Animation_Hold(int duration = 0) : base(duration,null) { }
        public Animation_Hold(int duration, int sound_index) : base(duration, sound_index) { }
        public Animation_Hold(string sound) : base(sound) { }
    }

    /// <summary>
    /// A pause is like a hold except it only stops animations after it in the queue from starting for a certain time, regardless
    /// of whether the animations before it are still running. Eg, Flame arrow spell runs several missile animation with a pause between
    /// each one, so they don't all start at the same time.
    /// </summary>
    public class Animation_Pause : Animation
    {
        const int DEFAULT_DURATION = 10;
        public Animation_Pause(int duration = DEFAULT_DURATION) : base(duration, null) { }
        public Animation_Pause(string sound) : base(sound) { }
    }

    public class Animation_FadeDown : Animation, IAnimHold
    {
        public Animation_FadeDown(int duration = 300) : base(duration, null) 
        {
            if (Gfx.FadeMode == 2) Animation.RemoveAnim(this);
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            if (!base.AdvanceAnim(ms_passed))
            {
                Gfx.FadeMode = 1;
                float t = asFraction(Time);
                Gfx.FadeColor.A = (byte)(t * 255f);
                return false;
            }
            else
            {
                Gfx.FadeMode = 2;
                Gfx.FadeColor = Color.Black;
                Action.LockActions = eAction.BLOCKABLE_ACTIONS;
                return true;
            }
        }
    }
    public class Animation_FadeUp : Animation, IAnimHold
    {
        public Animation_FadeUp(int duration = 300) : base(duration, null) 
        {
            if (Gfx.FadeMode == 0) Animation.RemoveAnim(this);
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            if (!base.AdvanceAnim(ms_passed))
            {
                Gfx.FadeMode = 3;
                float t = asFraction(Time);
                Gfx.FadeColor.A = (byte)(255f - t * 255f);
                return false;
            }
            else
            {
                Gfx.FadeMode = 0;
                Gfx.FadeColor = new Color(0,0,0,0);
                Action.LockActions = eAction.NONE;
                return true;
            }
        }
    }

    public class Animation_FieldAppear : Animation, IAnimUnderlay
    {
        const int DEFAULT_DURATION = 100;

        public Field Type;
        public Vector2 Pos { get { return new Vector2(pos.X, pos.Y); } }
        Location pos;

        public Animation_FieldAppear(Location p, Field type) : base(DEFAULT_DURATION, null)
        {
            Type = type;
            pos = p;
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            if (!base.AdvanceAnim(ms_passed)) return false;
            Game.CurrentTown.RemoveField(pos, Field.FIELD_APPEAR);
            return true;
        }

        public void DrawUnderlay(SpriteBatch sb, Vector2 p)
        {
            float t = asFraction(Time);
            int wd = (int)(t * Gfx.ZoomSizeW);
            int ht = (int)(t * Gfx.ZoomSizeH);
            int x = (int)p.X + (Gfx.ZoomSizeW - wd) / 2;
            int y = (int)p.Y + (Gfx.ZoomSizeH - wd) / 2;
            XnaRect r = new XnaRect(x, y, wd, ht);
            sb.Draw(Gfx.FieldsGfx, r, Type.GetSrcRect(), Color.White);
        }

    }

    public class Animation_CrateMove : Animation, IAnimUnderlay
    {
        const int DEFAULT_DURATION = 200;
        public Vector2 Pos { get { return pos; } }
        Location startPos, endPos;
        bool isCrate;
        bool Fades;
        Color Colour = Color.White;
        Vector2 pos;

        public Animation_CrateMove(Location startpos, Location endpos, bool is_crate, bool fades) : base(DEFAULT_DURATION, null)
        {
            isCrate = is_crate;
            Fades = fades;
            startPos = startpos;
            pos = startpos.ToVector2();
            endPos = endpos;
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            if (!base.AdvanceAnim(ms_passed))
            {
                float t = asFraction(Time);
                pos = Vector2.Lerp(startPos.ToVector2(), endPos.ToVector2(), t);
                if (Fades) Colour = Color.FromNonPremultiplied(255,255,255,(int)((1f - t) * 255f));
                return false;
            }
            
            Game.CurrentTown.RemoveField(endPos, Field.CRATE_MOVE);
            return true;
        }

        public void DrawUnderlay(SpriteBatch sb, Vector2 p)
        {
            if (!started) return;
            XnaRect r = new XnaRect((int)p.X, (int)p.Y, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
            XnaRect srcrect = new XnaRect((isCrate ? 6 : 7) * Gfx.SRCTILEWIDTH, 0, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
            sb.Draw(Gfx.FieldsGfx, r, srcrect, Colour, 0, Vector2.Zero, SpriteEffects.None, 0);
        }

    }

    public class Animation_Move : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 200;

        IAnimatable Character;
        float Stage;
        public Location PosMod;
        bool Fades; //whether character fades away as it moves (used for characters fleeing combat area)
        bool WalkSound;
        TerrainRecord steppedOn;
        int Step;

        public Animation_Move(IAnimatable ch, Location oldpos, Location newpos, bool walksound, bool fades = false, int duration = DEFAULT_DURATION/*float rate = 0.2f*/)
            : base(duration, null)
        {
            Character = ch;
              Character.AnimAction = this;
            PosMod = newpos - oldpos;
            Fades = fades;
            WalkSound = walksound;
            steppedOn = Game.CurrentMap.TerrainAt(newpos);
            Step = (newpos.X + newpos.Y) % 2;

            if (!Game.CurrentMap.Visible(oldpos) && !Game.CurrentMap.Visible(newpos))
            {
                Duration = 0;
                animSound = -1;
            }

        }

        override protected bool AdvanceAnim(int ms_passed)
        {
            if (!started && WalkSound) Sound.WalkSound(steppedOn, Step);
            if (base.AdvanceAnim(ms_passed))
            {
                Character.AnimAction = null;
                return true;
            }
            Stage = (float)((Math.Cos((asFraction(Time) + 1) * Math.PI) + 1) / 2);
            return false;
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color col)
        {
            r.Offset((int)((-PosMod.X * (1 - Stage)) * Gfx.ZoomSizeW),
                     (int)(-PosMod.Y * (1 - Stage) * Gfx.ZoomSizeH));
            if (Fades) col = Color.FromNonPremultiplied(col.R, col.G, col.B, (int)((1f - Stage) * 255f));
        }
    }

    public class Animation_Vanish : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 1000;
        IAnimatable Character;
        bool Vanish;
        float Stage;

        public Animation_Vanish(IAnimatable ch, bool vanish, string sound, int duration = DEFAULT_DURATION)
            : base(duration, sound)
        {
            Character = ch;
            Vanish = vanish;
        }

        override protected bool AdvanceAnim(int ms_passed)
        {
            Character.AnimAction = this;
            if (!Vanish) Character.NotDrawn = false;

            if (base.AdvanceAnim(ms_passed))
            {
                Character.AnimAction = null;
                if (Vanish) Character.NotDrawn = true;

                return true;
            }
            Stage = asFraction(Time);
            if (Vanish) Stage = 1f - Stage;
            return false;
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color col)
        {
            col = Color.FromNonPremultiplied(col.R, col.G, col.B, (int)(Stage * 255f));
        }

    }

    public class Animation_VehicleMove : Animation, IAnimCharacter
    {
        IAnimatable vehicle;
        float Stage;
        public Location PosMod;
        bool WalkSound;

        const int DEFAULT_DURATION = 200;
        public Animation_VehicleMove(IAnimatable v, Location oldpos, Location newpos, bool splashsound, int duration = DEFAULT_DURATION/*float rate = 0.2f*/)
            : base(duration, null)
        {
            vehicle = v;
            PosMod = newpos - oldpos;
            WalkSound = splashsound;
            vehicle.AnimAction = this;
        }
        override protected bool AdvanceAnim(int ms_passed)
        {
            if (!started && WalkSound) Sound.Play("048_boatmove");
            if (base.AdvanceAnim(ms_passed))
            {
                vehicle.AnimAction = null;
                return true;
            }
            Stage = (float)((Math.Cos((asFraction(Time) + 1) * Math.PI) + 1) / 2);
            return false;
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color col)
        {
            r.Offset((int)((-PosMod.X * (1 - Stage)) * Gfx.ZoomSizeW),
                     (int)(-PosMod.Y * (1 - Stage) * Gfx.ZoomSizeH));
        }
    }

    /// <summary>
    /// Character tries to move to a new position, but halfway there goes in reverse back to old position
    /// </summary>
    public class Animation_MoveFail : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 200;

        IAnimatable Character;
        float Stage;
        public Location PosMod;

        public Animation_MoveFail(IAnimatable ch, Location oldpos, Location newpos, int duration = DEFAULT_DURATION/*float rate = 0.2f*/)
            : base(duration, "041_darn")
        {
            Character = ch;
            PosMod = newpos - oldpos;

            if (!Game.CurrentMap.Visible(oldpos) && !Game.CurrentMap.Visible(newpos))
            {
                Duration = 0;
                animSound = -1;
            }
        }

        override protected bool AdvanceAnim(int ms_passed)
        {
            Character.AnimAction = this;
            if (base.AdvanceAnim(ms_passed))
            {
                Character.AnimAction = null;
                return true;
            }

            float tf = asFraction(Time);
            if (tf < 0.5)
                Stage = (float)((Math.Cos((tf + 1f) * Math.PI) + 1f) / 2f);
            else
                Stage = (float)((Math.Cos((tf + 2f) * Math.PI) + 1f) / 2f);
            return false;
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color col)
        {
            r.Offset((int)(PosMod.X * Stage * Gfx.ZoomSizeW),
                     (int)(PosMod.Y * Stage * Gfx.ZoomSizeH));
        }
    }

    //Purely decorative explosion
    public class Animation_Explosion : Animation, IAnimOverlay
    {
        const int DEFAULT_DURATION = 750;
        const int EXPLOSION_FRAMES = 8;
        public Vector2 Pos { get { return pos; } }
        Vector2 pos;
        int Type;

        public Animation_Explosion(Location _pos, int type, string sound, int duration = DEFAULT_DURATION)
            : base(duration, sound)
        {
            pos = _pos.ToVector2();
            Type = Maths.MinMax(0,2,type);
        }
        public Animation_Explosion(float x, float y, int type, string sound, int duration = DEFAULT_DURATION)
            : base(duration, sound)
        {
            pos = new Vector2(x,y);
            Type = Maths.MinMax(0, 2, type);
        }


        public void DrawOverlay(SpriteBatch sb, Vector2 dpos)
        {
            int frame = (int)(asFraction(Time) * EXPLOSION_FRAMES);
            XnaRect srcr = new XnaRect(Gfx.SRCTILEWIDTH * frame, Gfx.SRCTILEHEIGHT * (4 + Type), Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
            XnaRect r = new XnaRect((int)dpos.X, (int)dpos.Y, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
            sb.Draw(Gfx.FieldsGfx, r, srcr, Color.White);
        }
    }

    public class Animation_Damage : Animation, IAnimOverlay
    {
        const int DEFAULT_DURATION = 750;

        const int APPEAR_TIME = DEFAULT_DURATION / 10;//0.1f;
        const int END_BEGIN_TIME = DEFAULT_DURATION - APPEAR_TIME;//1 - APPEAR_TIME;
        const int APPEAR_SCALE = DEFAULT_DURATION / APPEAR_TIME;

        public Vector2 Pos { get { return pos; } }
        Vector2 pos;
        string damAmount, damExtra;
        eDamageType damType;

        public Animation_Damage(Vector2 p, int damamt, int extradam, eDamageType type, string sound, int duration = DEFAULT_DURATION/*float rate = 0.05f*/)
            : base(duration, sound)
        {
            damAmount = damamt.ToString();// +"\n+1";//(extradam > 0 ? " + " + extradam.ToString() : "");
            if (extradam > 0) damExtra = "+" + extradam.ToString();

            pos = p;
            damType = type;

            switch (damType)
            {
                case eDamageType.COLD: break;
                case eDamageType.POISON: break;
                case eDamageType.FIRE: break;
                case eDamageType.MAGIC: break;
                default: break;
            }

            if (!Game.CurrentMap.Visible(new Location((int)pos.X, (int)pos.Y)))
            {
                Duration = 0;
                animSound = -1;
            }

        }

        public void DrawOverlay(SpriteBatch sb, Vector2 dpos)
        {
            XnaRect srcr = new XnaRect(0, 0, Gfx.SRCTILEWIDTH, Gfx.SRCTILEHEIGHT);
            XnaRect r = new XnaRect((int)dpos.X, (int)dpos.Y, Gfx.ZoomSizeW, Gfx.ZoomSizeH);
            Color numcol = Color.White;

            switch (damType)
            {
                case eDamageType.COLD: srcr.X = Gfx.SRCTILEWIDTH * 4; numcol = Color.Black; break;
                case eDamageType.FIRE: srcr.X = Gfx.SRCTILEWIDTH * 0; numcol = Color.Black; break;
                case eDamageType.MAGIC: srcr.X = Gfx.SRCTILEWIDTH * 1; numcol = Color.Black; break;
                case eDamageType.POISON: srcr.X = Gfx.SRCTILEWIDTH * 2; numcol = Color.Red; break;
                default: srcr.X = Gfx.SRCTILEWIDTH * 3; break;
            }

            if (Time < APPEAR_TIME)
                r.Inflate(-(int)(asFraction((APPEAR_TIME - Time) * APPEAR_SCALE) * r.Width / 2),
                          -(int)(asFraction((APPEAR_TIME - Time) * APPEAR_SCALE) * r.Height / 2));
            else if (Time > END_BEGIN_TIME)
                r.Inflate(-(int)(asFraction((Time - END_BEGIN_TIME) * APPEAR_SCALE) * r.Width / 2),
                          -(int)(asFraction((Time - END_BEGIN_TIME) * APPEAR_SCALE) * r.Height / 2));
            else
            {
            }

            sb.Draw(Gfx.FieldsGfx, r, srcr, Color.White);

            //Only draw the number on the Damage shape in the time between APPEAR_TIME & END_BEGIN_TIME in the animation
            if (Time >= APPEAR_TIME && Time <= END_BEGIN_TIME)
            {
                Vector2 strsize = Gfx.BoldFont.MeasureString(damAmount);
                Vector2 str1pos, str2pos, extsize;

                if (damExtra != null)
                {
                    str1pos = new Vector2(r.X + ((Gfx.ZoomSizeW - strsize.X) / 2), r.Y + ((Gfx.ZoomSizeH - strsize.Y) * 0.25f));
                    extsize = Gfx.BoldFont.MeasureString(damExtra);
                    str2pos = new Vector2(r.X + ((Gfx.ZoomSizeW - extsize.X) / 2), r.Y + ((Gfx.ZoomSizeH - extsize.Y) * 0.75f));
                    if (Gfx.ZoomSizeW > strsize.X + 4)
                    {
                        sb.DrawString(Gfx.BoldFont, damAmount, str1pos, numcol);
                        sb.DrawString(Gfx.BoldFont, damExtra, str2pos, numcol);
                    }
                }
                else
                {
                    str1pos = new Vector2(r.X + ((Gfx.ZoomSizeW - strsize.X) / 2), r.Y + ((Gfx.ZoomSizeH - strsize.Y) / 2));
                    if (Gfx.ZoomSizeW > strsize.X + 4)
                        sb.DrawString(Gfx.BoldFont, damAmount, str1pos, numcol);
                }
            }
        }
    }

    public class Animation_Missile : Animation, IAnimOverlay
    {
        const int DEFAULT_DURATION = 50;
        const float ARC_MAGNITUDE = 5;

        public Vector2 Pos { get { return pos; } }
        Vector2 pos, startPos, endPos, origin;
        float angle;
        XnaRect srcRect;
        bool arcingPath;

        public Animation_Missile(Location startpos, Location endpos, int missile_gfx_no, bool arcing_path, string sound=null, int duration = DEFAULT_DURATION)
            : base(0, sound)
        {
            Duration = 50 + duration * startpos.DistanceTo(endpos); //Duration depends on the distance the missile will travel
            pos = startPos = startpos.ToVector2() + new Vector2(0.5f,0.5f);
            endPos = endpos.ToVector2() + new Vector2(0.5f, 0.5f);
            angle = startpos.GetAngle(endpos);
            srcRect = new XnaRect(37, 1 + missile_gfx_no * (Gfx.MISSILE_GFX_HEIGHT + 2), Gfx.MISSILE_GFX_WIDTH, Gfx.MISSILE_GFX_HEIGHT);
            origin = new Vector2(Gfx.MISSILE_GFX_WIDTH / 2, Gfx.MISSILE_GFX_HEIGHT / 2);
            arcingPath = arcing_path;

            if (!Game.CurrentMap.Visible(startpos) && !Game.CurrentMap.Visible(endpos))
            {
                Duration = 0;
                animSound = -1;
            }
            
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            if (!base.AdvanceAnim(ms_passed))
            {
                float t = asFraction(Time);

                pos = Vector2.Lerp(startPos, endPos, t);

                if (arcingPath)
                    pos.Y -= (t * (1f - t)) * ARC_MAGNITUDE;

                return false;
            }
            return true;
        }

        public void DrawOverlay(SpriteBatch sb, Vector2 dpos)
        {
            XnaRect r;

            if (!arcingPath)
                r = new XnaRect((int)dpos.X, (int)dpos.Y,
                (int)(Gfx.MISSILE_GFX_WIDTH * ((float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH)) * 2,
                (int)(Gfx.MISSILE_GFX_WIDTH * ((float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH)) * 2);
            else
            {
                float t = 1f + (float)Math.Sin(asFraction(Time) * (float)Math.PI) * 3f;//t = 1f + Math.Abs(asFraction(Time)-0.5f) * 4;
                r = new XnaRect((int)dpos.X, (int)dpos.Y,
                (int)(Gfx.MISSILE_GFX_WIDTH * ((float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH) * t),
                (int)(Gfx.MISSILE_GFX_WIDTH * ((float)Gfx.ZoomSizeW / (float)Gfx.TILEWIDTH) * t));
            }
            sb.Draw(Gfx.MissilesGfx[0], r, srcRect, Color.White, angle, origin, SpriteEffects.None, 0);
        }
    }

    public class Animation_Death : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 1000;

        IAnimatable deceased;
        public Location Pos { get { return deceased.Pos; } }

        public Animation_Death(IAnimatable who_is_dead, int duration = DEFAULT_DURATION)//float rate = 0.05f)
            : base(duration, null)
        {
            deceased = who_is_dead;

            if (deceased is ICharacter)
                animSound = Sound.IndexOf(((ICharacter)deceased).DeathSound);

            if (!deceased.IsVisible())
            {
                Duration = 0;
                animSound = -1;
            }

            //Set sound based sound on what who_is_dead is.
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color colour)
        {
            float t = asFraction(Time);

            rot = t * 2f * (float)Math.PI;

            byte b = (byte)(256f * t);
            colour = new Color(255, 255, 255, (int)b);//Color.FromNonPremultiplied(255,255,255,b);


            r.Inflate(-(int)(t * r.Width / 2),-(int)(t * r.Height / 2));

        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            deceased.AnimAction = this;

            if (base.AdvanceAnim(ms_passed))
            {
                deceased.AnimAction = null;
                deceased.FinishDying();
                return true;
            }
            return false;
        }

    }

    public class Animation_Summon : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 800;
        IAnimatable summoned;
        public Location Pos { get { return summoned.Pos; } }

        public Animation_Summon(IAnimatable who_is_summoned, int duration = DEFAULT_DURATION)
            : base(duration, "061_summoning")
        {
            summoned = who_is_summoned;
            summoned.AnimAction = this; //This must be set in the constructor so that the animation is in its initial state as soon as the creature appears, rather than when any holds are out of the way in the queue

            if (!summoned.IsVisible())
            {
                Duration = 0;
                animSound = -1;
            }

        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color color)
        {
            float t = asFraction(Time);

            int oldwidth = r.Width, oldheight = r.Height;
            r.Width = (int)(t * r.Width);
            r.Height = (int)(t * r.Height);
            r.X -= (r.Width - oldwidth) / 2;
            r.Y -= (r.Height - oldheight) / 2;

            byte b = (byte)(255f * t);
            color = new Color(255, 255, 255, (int)b);
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            if (base.AdvanceAnim(ms_passed))
            {
                summoned.AnimAction = null;
                return true;
            }
            return false;
        }

    }

    public class Animation_Attack : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 400;
        IAnimatable attacker;
        public Location Pos { get { return attacker.Pos; } }

        public Animation_Attack(IAnimatable who_attacks, string sound = null, int duration = DEFAULT_DURATION)
            : base(duration, sound)
        {
            attacker = who_attacks;

            if (!attacker.IsVisible())
            {
                Duration = 0;
                animSound = -1;
            }
            //Base animSound on what who_attacks is
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color color)
        {
            int oldwidth = r.Width, oldheight = r.Height;

            r.Width += (int)(((Math.Cos(((double)asFraction(Time) * 2d + 1d) * Math.PI) + 1d) / 2d) * r.Width / 4);
            r.Height += (int)(((Math.Cos(((double)asFraction(Time) * 2d + 1d) * Math.PI) + 1d) / 2d) * r.Height / 4);

            r.X -= (r.Width - oldwidth) / 2;
            r.Y -= (r.Height - oldheight) / 2;
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            attacker.AnimAction = this;

            if (base.AdvanceAnim(ms_passed))
            {
                attacker.AnimAction = null;
                return true;
            }
            return false;
        }
    }

    public class Animation_CharFlash : Animation, IAnimCharacter
    {
        const int DEFAULT_DURATION = 400;
        IAnimatable flasher;
        Color FlashColour;
        float FlashAmount;

        public Location Pos { get { return flasher.Pos; } }

        public Animation_CharFlash(IAnimatable who_flashes, Color flashcolour, string sound)//int duration = DEFAULT_DURATION)
            : base(DEFAULT_DURATION,sound)
        {
            flasher = who_flashes;
            FlashColour = flashcolour;
            FlashAmount = 0f;

            if (!flasher.IsVisible())
            {
                Duration = 0;
                animSound = -1;
            }

            //Base animSound on what who_notices is
        }

        public void AdjustCharRect(ref XnaRect r, ref float rot, ref Color color)
        {
            FlashAmount = (float)(Math.Cos((asFraction(Time) * 2f + 1f) * (float)Math.PI) + 1f) / 2f;
            Gfx.ApplyFlashShader(FlashColour, FlashAmount);
        }

        protected override bool AdvanceAnim(int ms_passed)
        {
            flasher.AnimFlash = this;

            if (base.AdvanceAnim(ms_passed))
            {
                flasher.AnimFlash = null;
                return true;
            }
            return false;
        }
    }
}
