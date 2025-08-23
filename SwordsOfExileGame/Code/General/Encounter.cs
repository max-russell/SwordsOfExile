using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

//Used by the party type to store what outdoors monsters are active
public class Encounter : IAnimatable
{
    private PartyType Party => Game.CurrentParty;

    public Direction direction;
    public EncounterRecord Record;
    //public OutsideSector which_sector;
    public Location Pos
    { 
        get => pos;
        set => pos = value;
    }

    private Location pos;
    private bool doneMeetFunc = false; //Whether the special function on meeting the encounter has been run, so it doesn't run again.

    public bool NotDrawn { get; set; } = false; //Temporarily don't draw (used in teleporting animations)

    /// <summary>
    /// Runs the outside meeting special encounter script.
    /// </summary>
    /// <param name="cancelled">This means the encounter is called off entirely</param>
    /// <returns>True if the encounter shouldn't trigger right now.</returns>
    public bool DoMeetingScript(out bool cancelled)
    {
        cancelled = false;

        if (Record.FuncOnMeet is null or "") return false;

        if (!doneMeetFunc)
        {
            Script.CancelOutdoorEncounter = false;
            Script.New_NPCGroup(Record.FuncOnMeet, eCallOrigin.OUTDOOR_ENCOUNTER, Record);
            doneMeetFunc = true;
            return true;
        }
        else
        {
            cancelled = Script.CancelOutdoorEncounter;
            return Script.CancelOutdoorEncounter;
        }
    }

    public void FinishDying()
    {
        Game.WorldMap.NPCGroupList.Remove(this);
    }

    public bool IsVisible()
    {
        return Game.CurrentMap.Visible(pos);
    }

    public IAnimCharacter AnimAction { get; set; }

    public IAnimCharacter AnimFlash { get; set; }

    public Encounter(EncounterRecord wg, Location loc)
    {
        Record = wg;
        pos = loc;
        direction = new Direction(pos, Party.Pos);
    }

    public void Draw(SpriteBatch sb, XnaRect dr, Color col)
    {

        float rot = 0;
        var record = Record.GetChiefMonster();

        if (AnimAction != null)
            AnimAction.AdjustCharRect(ref dr, ref rot, ref col);
        if (AnimFlash != null)
            AnimFlash.AdjustCharRect(ref dr, ref rot, ref col);

        dr.Offset(dr.Width / 2, dr.Height / 2);

        if (record.Width == 2 && record.Height == 1)
        {
            dr.Height = dr.Width / 2;
            dr.Inflate((int)(dr.Width * 0.25), (int)(dr.Height * 0.25));
        }
        if (record.Height == 2 && record.Width == 1)
        {
            dr.Width = dr.Height / 2;
            dr.Inflate((int)(dr.Width * 0.25), (int)(dr.Height * 0.25));
        }

            

        Texture2D stex;
        var sr = record.GetGraphic(direction.IsFacingRight, AnimAction is Animation_Attack, out stex);
        sb.Draw(stex, dr, sr, col, rot, new Vector2(Gfx.CHARGFXWIDTH * record.Width / 2, Gfx.CHARGFXHEIGHT * record.Height / 2)/*Vector2.Zero*/, SpriteEffects.None, 0);
    }

    /// <summary>
    /// Moves the group.
    /// </summary>
    /// <returns>Returns true if the group is next to a PC and wants to attack them.</returns>
    public bool Move(bool suppress_animation = false)
    {

        if (pos.adjacent(Party.Pos)) return true; //Already next to party, so don't bother moving

        Location newpos;
        if (Maths.Rand(1, 1, 6) == 3)
            newpos = pos.randomShift();
        else
            newpos = pos + new Direction(pos, Party.Pos);

        var newdir = new Direction(pos, newpos);
        var ter = Game.WorldMap.TerrainAt(newpos);

        if (!ter.BlocksNPC && !Game.WorldMap.SomeoneThere(newpos) && Game.WorldMap.TownEntranceHere(newpos) == null)
        {
            if (!suppress_animation) new Animation_Move(this, pos, newpos, Animation.NoAnimationsRunning());
            pos = newpos;
            direction = newdir;
        }

        if (pos.adjacent(Party.Pos)) return true;
        return false;

    }
}