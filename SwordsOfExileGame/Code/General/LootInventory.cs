using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

public class LootSpot : IInventory
{
    private class lootEntry
    {
        public Item Item;
        public int Slot;
        public Keys Shortcut;
    }

    private List<lootEntry> List = new();
    private TownMap Town;
    private Location basePos;
    public Location Pos { get => basePos;
        set => basePos = value;
    }

    private bool Empty;
    public bool Gathering;

    private eItemFilter _Filter = eItemFilter.ALL;
    public eItemFilter Filter
    {
        get => _Filter;
        set
        { 
            _Filter = value;
            var n = 0;
            //Remake slot list according to the new filter.
            foreach (var l in List)
            {
                if (l.Item.Filter(_Filter))
                    l.Slot = n++;
                else
                    l.Slot = -1;
            }
            setShortcuts();
        }
    }

    public static LootSpot Generate(Location loc, TownMap town, bool gathered)
    {
        var l = new LootSpot(loc, town, gathered);
        l.Gathering = gathered;
        if (l.Empty && gathered) return null;
        return l;
    }

    /// <summary>
    /// Don't call this unless there definitely is a Loot window open.
    /// </summary>
    /// <returns></returns>
    public static LootSpot GetActiveLootSpot()
    {
        return ((LootWindow)Gui.GetWindowOfType(typeof(LootWindow))).Inventory;
    }

    private LootSpot(Location loc, TownMap town, bool gathered)
    {
        Town = town;
        basePos = loc;

        var range = Game.Mode == eMode.COMBAT ? 1 : 4;

        //If this is an outside combat map, we can pick up anything on the map provided all the enemies are dead.
        if (town is CombatMap && town.NoHostileNPCsLeft()) range = int.MaxValue;

        foreach (var i in gathered ? town.EachItemInRange(loc, range) : town.EachItemThere(loc, true))
        {
            if (gathered && i.Contained) continue; //We can't gather items in containers
            AddItem(i, false);
        }

        if (List.Count == 0) Empty = true;
    }

    /// <summary>
    /// Put all the items in the lootspot back where they should be on the map
    /// </summary>
    public void Finish()
    {
        var n = 0;

        foreach (var l in List)
        {

            if (!Town.ItemList.Contains(l.Item))
            {
                Town.PlaceItem(l.Item, basePos);
            }
            else
            {
                if (!Gathering) l.Item.Contained = true;
            }
            n++;
        }
    }

    private void setShortcuts()
    {
        foreach (var l in List)
            l.Shortcut = Keys.None;

        //Get all items in the current filter onto their own list
        var sortlist = List.FindAll(n => n.Item.Filter(_Filter));

        //Sort by slot number
        sortlist = sortlist.OrderBy(o => o.Slot).ToList();

        var k = Keys.A;
        foreach (var l in sortlist)
        {
            if (k > Keys.Z) 
                l.Shortcut = Keys.None;
            else 
                l.Shortcut = k++;
        }
    }

    /// <summary>
    /// Return item from inventory at slot specified, null if slot is empty.
    /// </summary>
    /// <param name="slotno"></param>
    /// <returns></returns>
    public Item GetSlot(int slotno)
    {
        var n = 0;
        foreach (var l in List)
        {
            if (l.Slot == slotno /*&& i != Gui.MoveItem*/) return List[n].Item;
            n++;
        }
        return null;
    }

    public Item GetItemFromShortcut(Keys k)
    {
        var l = List.Find(n => n.Shortcut == k);
        if (l == null) return null; else return l.Item;
    }

    public char GetShortcutFromItem(Item i)
    {
        var l = List.Find(n => n.Item == i);
        if (l == null) return (char)0; else return (char)((l.Shortcut - Keys.A) + (int)'a');
    }

    /// <summary>
    /// IInventory function. Places an item in a specific slot in the inventory, returning the item that was already there. The item returned is not removed from the inventory itself, but that must
    /// be done externally to ensure two items aren't in the same slot.
    /// </summary>
    /// <param name="item">Item to place</param>
    /// <param name="slotno">Slot to place in. </param>
    /// <returns>The item that was in the slot already, or null if it was empty.</returns>
    public Item PlaceItem(Item item, int slotno)
    {
        if (_Filter != eItemFilter.ALL && item.GetFilterGroup() != _Filter)
        {
            //Trying to place an item when the Filter isn't see to this item's type: just bung it into the first free slot for this type.
            AddItem(item, true);
            return null;
        }


        var index = List.FindIndex(n => n.Slot == slotno);

        Item replaces = null;
        if (index != -1) //There is no item in this slot.
        {
            replaces = List[index].Item;
        }

        if (item != null)
        {
            if (item.CombinableWith(replaces))
            {
                item.Charges += replaces.Charges;
                if (item.Charges > Constants.ITEM_STACK_LIMIT)
                {
                    replaces.Charges = item.Charges - Constants.ITEM_STACK_LIMIT;
                    item.Charges = Constants.ITEM_STACK_LIMIT;
                }
                else replaces = null;
            }

            item.Contained = !Gathering;

            var e = List.Find(n => n.Item == item);

            if (e == null)
            {
                List.Add(new lootEntry { Item = item, Slot = slotno });
            }
            else
            {
                e.Slot = slotno;
            }

        }
        setShortcuts();
        return replaces;
    }

    /// <summary>
    /// Add item in the first empty slot in the inventory
    /// </summary>
    /// <param name="item">Item to add</param>
    /// <returns>Successfully added?</returns>
    public bool AddItem(Item item, bool stack)
    {
        if (item == null) return true;

        if (stack)
            //Stack an item if it's combinable with one already held.
            foreach (var l in List)
                if (item != l.Item && item.CombinableWith(l.Item))
                {
                    l.Item.Charges += item.Charges;
                    if (l.Item.Charges > Constants.ITEM_STACK_LIMIT) { item.Charges = l.Item.Charges - Constants.ITEM_STACK_LIMIT; l.Item.Charges = Constants.ITEM_STACK_LIMIT; continue; } //Can only stack to 999
                    return true;
                }

        var n = 0;
        var slotfree = false;
        while (!slotfree)
        {
            var m = 0;
            slotfree = true;
            foreach (var l in List)
            {
                if (l.Slot == n) { n++; slotfree = false; break; }
            }
        };

        List.Add(new lootEntry { Item = item, Slot = n });
        setShortcuts();
        return true;
    }

    public bool RemoveItem(Item item)
    {
        var e = List.Find(n => n.Item == item);
        if (e != null)
        {
            if (Town.ItemList.Contains(item)) Town.ItemList.Remove(item);
            List.Remove(e);
            setShortcuts();
            return true;
        }
        return false;
    }

    public IEnumerable<Item> RemoveEach() //Used with the 'Take All' button in the loot window
    {
        for (var n = List.Count - 1; n >= 0; n--)
        {
            var l = List[n];
            if (!l.Item.Filter(_Filter)) continue;

            if (Town.ItemList.Contains(l.Item)) Town.ItemList.Remove(l.Item);

            List.Remove(l);
            yield return l.Item;
        }
    }

    /// <summary>
    /// Returns all items in the inventory, and the slot number too
    /// </summary>
    /// <returns></returns>
    public IEnumerable<Tuple<Item, int>> EachItem()
    {
        foreach (var l in List)
        {
            if (l.Item.Filter(_Filter))
                yield return new Tuple<Item, int>(l.Item, l.Slot);
        }
    }

    public void ArrangeItems()
    {
        var toremove = new List<Item>();

        //First combine any items that can be combined.
        //Items that should then be removed are put into the toremove list
        foreach (var i1 in EachItem())
        {
            if (toremove.Contains(i1.Item1)) continue;

            var reachedi1 = false;
            foreach (var i2 in EachItem())
            {
                if (reachedi1)
                {
                    if (!toremove.Contains(i2.Item1) && i1.Item1.CombinableWith(i2.Item1))
                    {
                        i1.Item1.Charges += i2.Item1.Charges;
                        if (i1.Item1.Charges > Constants.ITEM_STACK_LIMIT)
                        { i2.Item1.Charges = i1.Item1.Charges - Constants.ITEM_STACK_LIMIT; i1.Item1.Charges = Constants.ITEM_STACK_LIMIT; }
                        else
                            toremove.Add(i2.Item1);
                    }
                }
                else if (i1 == i2)
                    reachedi1 = true;
            }
        }

        //Items in the toremove list are removed from the main list.
        for (var n = List.Count-1; n >= 0; n--)
        {
            if (toremove.Find(i => i == List[n].Item) != null)
                List.RemoveAt(n);
        }

        //Gaps are removed
        var s = 0;
        //Remake slot list according to the filter.
        foreach (var l in List)
        {
            if (l.Item.Filter(_Filter))
                l.Slot = s++;
            else
                l.Slot = -1;
        }
        setShortcuts();
    }

    public bool InventorysClose(IInventory other)
    {
        if (!Gathering)
        {
            if (basePos.adjacent(other.Pos)) return true;
        }
        else
        if (basePos.VDistanceTo(other.Pos) <= 4) return true;
        return false;
    }

    public void MakeItemToolTip(Item e, XnaRect r)
    {
        if (e != null)
            new ToolTipV2(false, r, e.TooltipInfo(), -1);
    }

    public void MakeInventoryPopUpWindow(Item c)
    {
        var popupoptions = new List<PopUpMenuData>();

        if (c != null)
        {
            Gui.DragItem = null;
            if (c.IsEquippable) popupoptions.Add(new PopUpMenuData("Equip", c, null, PopUpMenuData.EQUIP));
            popupoptions.Add(new PopUpMenuData("Take", c, null, PopUpMenuData.TAKE));
            new PopUpMenu(handlePopUp, popupoptions);
        }
    }

    private void handlePopUp(object o, object o2, int data)
    {
        var c = (Item)o;
        var pc = Game.CurrentParty.CurrentPC;//owner as PCType;
        if (data is PopUpMenuData.EQUIP or PopUpMenuData.TAKE)
        {
            new Action(data == PopUpMenuData.EQUIP ? eAction.EquipItem : eAction.TakeItem)
            {
                PC = Game.Mode == eMode.COMBAT ? Game.CurrentParty.ActivePC : Game.CurrentParty.CurrentPC,
                Item = c,
                InventoryFrom = this
            };
        }
    }
}