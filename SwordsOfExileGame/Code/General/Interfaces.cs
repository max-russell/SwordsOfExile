using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    public class ExileList<T> : KeyedCollection<string, T> where T : IListEntity, new()
    {
        protected override string GetKeyForItem(T entity)
        {
            // The key is the ID. 
            return ((IListEntity)entity).ID;
        }

        public bool TryGetValue(string key, out T to_find)
        {
            to_find = Items.FirstOrDefault(n => ((IListEntity)n).ID == key);
            return Contains(key);
        }

        public string GetUniqueID(string prefix)
        {
            int n = 0;
            string s;
            do
            {
                s = prefix + "_" + n++;
            } while (Contains(s));
            return s;
        }

        public void Load(BinaryReader In)
        {
            Clear();

            while (true)
            {
                byte b = In.ReadByte();

                if (b == 0) break;

                if (b == 1)
                {
                    T t = new T();
                    t.Load(In);
                }
                else if (b == 2)
                    Scenario.LoadAndDisregardEditorFolder(In);
            }
        }

    }

    public interface IListEntity
    {
        string ID { get; set; }
        void Load(BinaryReader In);
    }

    public interface IInventory //Something that can contain or carry items
    {
        Location Pos { get; set; }
        IEnumerable<Tuple<Item, int>> EachItem();
        Item PlaceItem(Item item, int slotno);
        bool AddItem(Item item, bool stack);
        bool RemoveItem(Item item);//, bool regardless_of_curse);
        Item GetSlot(int slotno);
        //int LastSlot{get;}//(eItemFilter filter);
        bool InventorysClose(IInventory other);
        void MakeInventoryPopUpWindow(Item c);
        void MakeItemToolTip(Item i, XnaRect r);//int slotno);
        void ArrangeItems();
        
        eItemFilter Filter { get; set; }
    }

    public interface IMap
    {

        //int this[int x, int y] { get; }
        bool Visible(Location loc);
        string Name { get; }

        //void Load(BinaryReader In);
        void Draw(SpriteBatch sb);
        bool PlaceItem(Item item, Location loc);
        //void Launch();
        void Enter(bool firsttime);
        //void UpdateVisible(bool only_active = false);//params Location[] locs);

        void UpdateVisible();//params Location[] locs);
        //void UpdateVisiblePC(PCType pc, bool clear_existing);//params Location[] locs);

        void AlterTerrain(Location pos, int layer, TerrainRecord newter);
        string GetInfoRectString(Location pos);
        //bool TerrainBlocked(Location pos);
        TerrainRecord TerrainAt(Location poc);
        bool CheckSpecialTerrainPC(Location pos, PCType ch);
        void DoNastyTerrain(Location pos);
        //ICharacter CharacterThere(Location pos, bool include_pcs = true, bool include_npcs = true);
        bool CharacterCanBeThere(Location loc, ICharacter m_num, bool allow_leave_map = false);
        //Location GetTileAtMouse(MouseState ms);
        string GetToolTipMessage(Location loc);
        //Sign SignAtLoc(Location loc);
        bool DoNPCTurn();
        void StartNPCTurn();
        //int CanSee(Location l1, Location l2, int mode);
        void Search(Location l, PCType pc);
        bool DoStoodOnTriggers();
        //List<SpecialNode> SpecialNodeList { get; }
        bool PCCanTryToWalkThere(Location pos, PCType pc);
        bool TriggerStepOnSpecials(Location pos, Direction dir, PCType pc, bool boat_landing);
        List<PopUpMenuData> GetPopUpMenuOptions(Location loc, Location frompos);
        void HandleMapPopUp(object o, object o2, int data);
    }

    public interface IAnimatable
    {
        IAnimCharacter AnimAction { get; set; }
        IAnimCharacter AnimFlash { get; set; }
        Location Pos { get; set; }
        void FinishDying();
        bool NotDrawn { get; set; }
        bool IsVisible();
    }

    public interface ICharacter
    {
        void Draw(SpriteBatch sb, XnaRect d_rect, Color col);
        Location Pos { get; set; }
        int Width { get; }
        int Height { get; }
        Direction Dir { get; set; }
        bool IsAlive();
        bool OnSpace(Location loc);
        int Health { get; set; }
        int MaxHealth { get; }
        int SP { get; set; }
        int Level { get; set; }
        string DeathSound { get; }
        //void Attack(ICharacter target);
        bool Damage(IExpRecipient attacker, int how_much, int how_much_spec, eDamageType dam_type, eDamageType spec_dam_type = eDamageType.WEAPON, string sound_type = null);
        bool Kill(IExpRecipient who_killed, eLifeStatus type, bool no_save = false);
        void ForceWallMe(IExpRecipient perp);
        void FireWallMe(IExpRecipient perp);
        void IceWallMe(IExpRecipient perp);
        void BladeWallMe(IExpRecipient perp);
        void FireBarrierMe();
        void QuickfireMe();
        void StinkCloudMe();
        void SleepCloudMe();
        void WebSpaceMe();
        void Heal(int how_much, bool silent = false);
        void Acid(int how_much, bool silent = false);
        void Poison(int how_much, bool silent = false);
        void Disease(int how_much, bool silent = false);
        void Slow(int how_much, bool silent = false);
        void Haste(int how_much, bool silent = false);
        void Curse(int how_much, bool silent = false);
        void Bless(int how_much, bool silent = false);
        void Web(int how_much, bool silent = false);
        void Scare(int how_much, bool silent = false);
        void Dumbfound(int how_much, bool silent = false);
        void Sleep(int how_much, int adjust);
        void Paralyze(int how_much, int adjust);
        //void Charm(int how_much, eAffliction what_type, int adjust); //Also handles sleep/paralyse
        string Name { get; }
        string TooltipInfo(bool brief);
        eAttitude MyAttitude();
        bool AlliedWith(ICharacter ch);
        //bool IsNotHere();
        int Status(eAffliction type);
        void SetStatus(eAffliction type, int val, int min = Int32.MinValue, int max = Int32.MaxValue);
        void IncStatus(eAffliction type, int val, int max = Int32.MaxValue);
        int TargetingNum { get; set; }
    }

    /// <summary>
    /// This is either the PC or the Party, either of which can gain experience. NPCs are also included but don't gain experience in BoE.
    /// </summary>
    public interface IExpRecipient
    {
        void AwardXP(int amount);
    }

    public interface IAnimOverlay
    {
        void DrawOverlay(SpriteBatch sb, Vector2 pos);
        Vector2 Pos { get; }
    }
    public interface IAnimUnderlay
    {
        void DrawUnderlay(SpriteBatch sb, Vector2 pos);
        Vector2 Pos { get; }
    }
    public interface IAnimCharacter
    {
        void AdjustCharRect(ref XnaRect r, ref float rot, ref Color colour);
    }
    interface IAnimHold { }


}