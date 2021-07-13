using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace SwordsOfExileGame
{
    public partial class Game : Microsoft.Xna.Framework.Game
    {
        public static string LastSaveFile = "";

        public static SaveInfo LoadSaveInfo(string filename, bool free_parties)//, out string scenfilename, out string scenname, out int scenpic, out string partymap)
        {
            string fn = Path.ChangeExtension(filename, "sav2");
            fn = Path.Combine(RootDirectory, "Saves", fn);

            if (!File.Exists(fn)) return null;// false;

            using (FileStream fs = new FileStream(fn, FileMode.Open, FileAccess.Read))
            using (BinaryReader file = new BinaryReader(fs))
            {
                try
                {
                    if (file.ReadString() != Constants.SAVE_FILE_KEY) return null;// false;
                    if (file.ReadInt32() != Constants.SAVE_FILE_VERSION) return null;// false;

                    string savename = file.ReadString();

                    //Read whether the party in this save game is currently in a scenario.
                    bool in_scenario = file.ReadBoolean();

                    //if (!in_scenario && !free_parties) return null;// false;
                    if (in_scenario == free_parties) return null;

                    //Load the party
                    CurrentParty = new PartyType(file, filename);

                    SaveInfo i = new SaveInfo();
                    i.Filename = filename;
                    i.SaveName = savename;

                    if (!free_parties)
                        i.ScenFile = file.ReadString();
                    i.PartyName = CurrentParty.Name;
                    i.LastSavedDate = CurrentParty.LastSavedDate;
                    i.Age = CurrentParty.Age;

                    if (!free_parties)
                    {
                        i.ScenName = file.ReadString();
                        i.IntroPic = file.ReadInt32();
                        i.CurrentMapName = file.ReadString();
                    }
                    return i;
                }
                catch (EndOfStreamException)
                {
                    return null;
                }
            }    
        }

        public static PartyType LoadSavedPartyInfo(string filename)
        {
            string fn = Path.ChangeExtension(filename, "sav2");
            fn = Path.Combine(RootDirectory, "Saves", fn);

            if (!File.Exists(fn)) return null;// false;

            List<Texture2D> pcpics = new List<Texture2D>();

            PartyType tempParty;

            using (FileStream fs = new FileStream(fn, FileMode.Open, FileAccess.Read))
            using (BinaryReader file = new BinaryReader(fs))
            {
                try
                {
                    if (file.ReadString() != Constants.SAVE_FILE_KEY) return null;// false;
                    if (file.ReadInt32() != Constants.SAVE_FILE_VERSION) return null;// false;

                    string savename = file.ReadString();

                    //Read whether the party in this save game is currently in a scenario.
                    file.ReadBoolean();

                    //Load the party
                    tempParty = new PartyType(file, filename);
                    

                    //foreach (PCType pc in tempParty.PCList)
                    //{
                    //    pcpics.Add(pc.PortraitTexture);
                    //}

                }
                catch (EndOfStreamException)
                {
                    return null;
                }
            }
            return tempParty;
        }

        public static bool LoadGame()
        {
            string filename = LastSaveFile;//CurrentParty.SaveFileName;
            filename = Path.ChangeExtension(filename, "sav2");
            filename = Path.Combine(RootDirectory, "Saves", filename);

            if (!File.Exists(filename)) return false;

            using (FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read))
            using (BinaryReader file = new BinaryReader(fs))
            {
                if (file.ReadString() != Constants.SAVE_FILE_KEY) { FlagError("Loading Error", "'" + LastSaveFile + "' is not a valid save game file"); return false; }
                if (file.ReadInt32() != Constants.SAVE_FILE_VERSION) { FlagError("Loading Error", "'" + LastSaveFile + "' is incompatible with this version of the game."); return false;}

                file.ReadString(); //Save name - not needed.

                //Read whether the party in this save game is currently in a scenario.
                bool in_scenario = file.ReadBoolean();

                //Load the party
                CurrentParty = new PartyType(file, LastSaveFile);//CurrentParty.SaveFileName);

                if (in_scenario)
                {
                    if (!Scenario.LoadGame(file)) return false;

                    //Load vehicles
                    foreach (Vehicle v in Vehicle.List)
                        v.LoadGame(file);
                    int vi = file.ReadInt32();
                    if (vi != -1) CurrentParty.Vehicle = Vehicle.List[vi];

                    SpecialItem.LoadGame(file);

                    Timer.LoadGame(file);

                    foreach (Shop i in Shop.List)
                        i.LoadGame(file);

                    GlobalVariables.LoadGame(file);

                    //Link party's known spells to the spells in the scenario.
                    //foreach (PCType pc in CurrentParty.PCList)
                    //    pc.SetupKnownSpells();
                }
                //InMainMenu = !in_scenario;
            }

            Game.SaveSettings();

            //Action.Requested = eAction.NONE;
            new Action(eAction.NONE);
            //DoneLeaveScript = false;
            return true;
        }

        public static void AutoSave()
        {   
            File.Delete(Path.Combine(SavesDirectory, String.Format("AutoSave{0:D2}.sav2", Constants.AUTOSAVE_LIMIT)));

            for (int n = Constants.AUTOSAVE_LIMIT-1; n > 0 ; n--)
            {
                string oldsav = Path.Combine(SavesDirectory, String.Format("AutoSave{0:D2}.sav2", n));
                string newsav = Path.Combine(SavesDirectory, String.Format("AutoSave{0:D2}.sav2", n+1));

                if (File.Exists(oldsav))
                    File.Move(oldsav, newsav);
            }

            SaveGame("AutoSave01", false);//, "AutoSave");
        }

        public static void SaveGame(string filename, bool only_party)
        {

            if (Game.Mode == eMode.COMBAT)
            {
                AddMessage("Save: Not during combat");
                return;
            }

            if (!only_party) LastSaveFile = filename;
            string fullfilename = Path.ChangeExtension(filename, "sav2");
            fullfilename = Path.Combine(RootDirectory, "Saves", fullfilename);

            if (!Directory.Exists(Path.Combine(RootDirectory, "Saves")))
            {
                Directory.CreateDirectory(Path.Combine(RootDirectory, "Saves"));
            }

            using (FileStream fs = new FileStream(fullfilename, FileMode.Create, FileAccess.Write))
            using (BinaryWriter file = new BinaryWriter(fs))
            {
                //Write save game identifier
                file.Write(Constants.SAVE_FILE_KEY);
                file.Write(Constants.SAVE_FILE_VERSION);

                if (only_party)
                    file.Write(filename);
                else
                    file.Write(LastSaveFile);

                file.Write(!only_party);//Game.InMainMenu); //Write whether the party is in a scenario.

                //Save Party
                CurrentParty.SaveGame(file);

                if (!only_party)//Game.InMainMenu)
                {
                    //Write scenario
                    Scenario.SaveGame(file);

                    //Save latest vehicle positions and status
                    foreach (Vehicle v in Vehicle.List)
                        v.SaveGame(file);
                    if (CurrentParty.Vehicle == null) file.Write(-1);
                    else file.Write(Vehicle.List.IndexOf(CurrentParty.Vehicle));


                    //Save special items collected so far.
                    SpecialItem.SaveGame(file);

                    Timer.SaveGame(file);

                    //Shops - save all items currently stocked.
                    foreach (Shop i in Shop.List)
                        i.SaveGame(file);

                    GlobalVariables.SaveGame(file);
                }
                //Save Game Preferences

            }

            Game.SaveSettings();

            if (!InMainMenu) AddMessage("Save: Done.");
            new Action(eAction.NONE);

            //Assumes some fancy window has already let the player select a filename etc.

            //Party

            //Spell prefs (last spell cast, last spell caster
            //Game preference
        }
    }

    public class SaveInfo
    {
        public string SaveName;
        public string Filename, PartyName, ScenName, ScenFile, CurrentMapName;
        public int Age, IntroPic;
        public DateTime LastSavedDate;
    }

    partial class Scenario
    {
        public static bool LoadGame(BinaryReader file)
        {
            string filename = file.ReadString();
            string name = file.ReadString();
            int pic = file.ReadInt32();
            file.ReadString(); //Name of current map (only needed in LoadGameInfo)

            Filename = filename;
            if (!Load())
            {
                //Game.FlagError("Loading Error", new Exception("Scenario did not load correctly."), filename);
                return false;
            }
            if (name != Name) return false;
            if (!Script.Initialise())
            {
                return false;
            }
            //if (!MagicSpell.LoadSpellData()) return false; 
            //if (!Recipe.LoadAlchemyData()) return false;

            Party.Pos = file.ReadLocation();
            Party.Direction = file.ReadDirection();

            bool outside = file.ReadBoolean();
            if (outside)
            {
                Game.Mode = eMode.OUTSIDE;
                Game.CurrentMap = Game.WorldMap;
            }
            else
            {
                Game.Mode = eMode.TOWN;
                TownMap t;
                if (TownMap.List.TryGetValue(file.ReadString(), out t))
                    Game.CurrentMap = t;
                else
                    Game.CurrentMap = TownMap.List[0];//TownList[file.ReadInt32()];
            }

            int count = file.ReadInt32();

            //Fill recently visited towns with null placeholders for now. They will be filled in later.
            for (int n = 0; n < count; n++)
                Game.RecentTownList.Add(null);

            foreach (TownMap town in TownMap.List)
                town.LoadGame(file);
            foreach (TownMap town in TownMap.List)
                town.LoadGameItemPresets(file);

            Game.WorldMap.LoadGame(file);

            count = file.ReadInt32();
            for (int n = 0; n < count; n++)
                Notes.Add(new Note { Title = file.ReadString(), Message = file.ReadString() });

            return true;
        }

        public static bool SaveGame(BinaryWriter file)
        {
            //SAVE:
            // Scenario name & filename for identification purposes
            file.Write(Path.GetFileNameWithoutExtension(Filename));
            file.Write(Name);
            file.Write(IntroPic);
            file.Write(Game.CurrentMap.Name); //Save name of party's current location.

            file.WriteStuff(Party.Pos, Party.Direction);
            if (Game.Mode == eMode.OUTSIDE)
            {
                file.Write(true);
            }
            else
            {
                file.Write(false);
                file.Write(Game.CurrentTown.ID);//Num);
            }

            file.Write(Game.RecentTownList.Count);

            foreach (TownMap town in TownMap.List)
                town.SaveGame(file);
            foreach (TownMap town in TownMap.List)
                town.SaveGameItemPresets(file);

            Game.WorldMap.SaveGame(file);

            file.Write(Notes.Count);
            foreach(Note n in Notes)
                file.WriteStuff(n.Title, n.Message);

            return true;
        }
    }

    public partial class TownMap : IMap
    {
        public void LoadGame(BinaryReader file)
        {
            for (int y = 0; y < Height; y++)
                for (int x = 0; x < Width; x++)
                {
                    if (Game.DebugLoad)
                        file.ReadUInt16(); //Don't overwrite original scenario terrain data with data from saved game file.
                    else
                        _Terrain[x, y] = file.ReadUInt16();
                }

            for (int y = 0; y < Height; y++)
                for (int x = 0; x < Width; x += 8)
                {
                    byte bit = file.ReadByte();

                    for (int b = 0; b < 8; b++)
                        if (x+b < Width)
                            _Explored[x + b, y] = (bit & (1 << b)) != 0;
                }

            //Load TriggerSpot's Active property (8 per byte)
            byte byt = 0;
            byte bitcount = 0;
            for (int x = 0; x < TriggerSpotList.Count; x++)
            {
                if (bitcount == 0)
                {
                    byt = file.ReadByte();
                    bitcount = 8;
                }
                TriggerSpotList[x].Active = (byt & 128) != 0;
                byt <<= 1;
                bitcount--;
            }

            Hidden = file.ReadBoolean();
            Hostile = file.ReadBoolean();
            Abandoned = file.ReadBoolean();
            KillCount = file.ReadInt32();
            

            int count;

            if (file.ReadBoolean()) //Is this on the Recently visited town list?
            {
                Game.RecentTownList[file.ReadInt32()] = this; //Replace placeholder null in list with this town.

                //Load fields
                Misc = new uint[Width, Height];
                for (int y = 0; y < Height; y++)
                    for (int x = 0; x < Width; x++)
                        Misc[x, y] = file.ReadUInt32();

                //Load creature instances
                NPCList = new List<NPC>();
                count = file.ReadInt32();
                for (int n = 0; n < count; n++)
                    NPCList.Add(new NPC(file, this));
                for (int n = 0; n < count; n++)
                    NPCList[0].LoadGameCharLinks(file, this);

                foreach (NPCPreset npc in CreatureStartList)
                    npc.InstanceWasKilled = file.ReadBoolean();
            }

            //Load items.
            count = file.ReadInt32();
            for (int n = 0; n < count; n++)
            {
                Item i = new Item();
                i.LoadInstance(file);
                ItemList.Add(i);
            }

            

        }

        public void SaveGame(BinaryWriter file)
        {
            //Save terrain data
            for (int y = 0; y < Height; y++)
                for (int x = 0; x < Width; x++)
                    file.Write(_Terrain[x, y]);

            //Save exploration data, but pack 8 tiles at a time into 1 byte to save space
            for (int y = 0; y < Height; y++)
                for (int x = 0; x < Width; x += 8)
                {
                    byte bit = 1;
                    byte d = 0;
                    for (int b = 0; b < 8; b++)
                    {
                        if (x + b < Width && _Explored[x + b, y]) d |= bit;
                        bit <<= 1;
                    }
                    file.Write(d);
                }

            //Save Trigger spots 'Active' property. Pack 8 into 1 byte
            byte byt = 0;
            byte bitcount = 0;

            for (int x = 0; x < TriggerSpotList.Count; x++)
            {
                if (bitcount == 8)
                {
                    file.Write(byt);
                    byt = 0;
                    bitcount = 0;
                }
                byt <<= 1;
                if (TriggerSpotList[x].Active) byt |= 1;
                bitcount++;
            }
            if (bitcount > 0)
            {
                byt <<= 8 - bitcount;
                file.Write(byt);
            }

            file.Write(Hidden);
            file.Write(Hostile);
            file.Write(Abandoned);
            file.Write(KillCount);

            //Kill Count?
            //Abandoned?

            if (!Game.RecentTownList.Contains(this))
            {
                file.Write(false);
                
                //Save items only in the storage area. So just flush all the items not in the area first.
                for (int n = ItemList.Count-1; n >= 0;n--)
                {
                    Item item = ItemList[n];

                    if (!item.Pos.Inside(StorageArea.Left, StorageArea.Top, StorageArea.Right, StorageArea.Bottom))
                        ItemList.Remove(item);
                }
                file.Write(ItemList.Count);

                foreach(Item item in ItemList)
                {
                    if (item.Pos.Inside(StorageArea.Left, StorageArea.Top, StorageArea.Right, StorageArea.Bottom))
                        item.SaveGame(file);
                }

            }
            else
            {
                file.Write(true); //Indicate in save file this is a recently visited town
                file.Write(Game.RecentTownList.IndexOf(this)); //And where it is in the list.

                //Save fields
                for (int y = 0; y < Height; y++)
                    for (int x = 0; x < Width; x++)
                        file.Write(Misc[x, y]);

                //Save creature instances
                file.Write(NPCList.Count);
                foreach (NPC npc in NPCList)
                    npc.SaveGame(file, this);
                foreach (NPC npc in NPCList)
                    npc.SaveGameCharLinks(file, this);


                //Save 'InstanceWasKilled' property of NPCStartList
                foreach (NPCPreset npc in CreatureStartList)
                    file.Write(npc.InstanceWasKilled);

                //Save items
                file.Write(ItemList.Count);
                foreach (Item item in ItemList)
                    item.SaveGame(file);
            }
        }

        public void LoadGameItemPresets(BinaryReader file)
        {
            foreach (PresetItem i in PresetItemList)
            {
                if (file.ReadBoolean()) //Read whether this item preset is linked to an item instance
                {
                    if (file.ReadBoolean()) //True if the instance is held by a PC
                    {
                        PCType pc = Game.CurrentParty.PCList[file.ReadInt32()];
                        if (file.ReadBoolean()) //Equipped item
                            i.Instance = pc.EquippedItemSlots[file.ReadInt32()];
                        else //Not equipped
                            i.Instance = pc.ItemList[file.ReadInt32()];
                    }
                    else //The instance is on a town map
                        i.Instance = TownMap.List[file.ReadInt32()].ItemList[file.ReadInt32()];
                }
            }
        }

        public void SaveGameItemPresets(BinaryWriter file)
        {
            foreach (PresetItem i in PresetItemList)
            {
                if (i.Instance == null)
                    file.Write(false);
                else
                {
                    //WRITE WHERE THE INSTANCE IS SO WE CAN LINK IT BACK WHEN THE GAME IS LOADED.
                    //Item instances could be held by a pc or in a town somewhere
                    //file.Write(true);
                    WritePresetItemLinkInfo(i.Instance, file);
                }
            }
        }

        void WritePresetItemLinkInfo(Item i, BinaryWriter file)
        {
            foreach (TownMap t in TownMap.List)
            {
                for (int n = 0; n < t.ItemList.Count; n++)
                    if (i == t.ItemList[n])
                    {
                        file.WriteStuff(true, false, t.Num, n);
                        return;
                    }
            }
            foreach (PCType pc in Party.PCList)
            {
                foreach (Item i2 in pc.ItemList)
                {
                    if (i == i2)
                    {
                        file.WriteStuff(true, true, pc.Slot, false, pc.ItemList.IndexOf(i));
                        return;
                    }
                }
                for (int n = 0; n < pc.EquippedItemSlots.Length; n++)
                {
                    if (pc.EquippedItemSlots[n] != null)
                    {
                        if (i == pc.EquippedItemSlots[n])
                        {
                            file.WriteStuff(true, true, pc.Slot, true, n);
                            return;
                        }
                    }
                }
            }

            file.Write(false);
            //throw new Exception("So where the hell is this item then?");
        }
    }

    public partial class NPC : ICharacter, IExpRecipient, IAnimatable
    {
        public NPC(BinaryReader file, TownMap town)
        {
            WanderTarget = file.ReadLocation();
            Provocation = file.ReadInt32();
            Attitude =  (eAttitude)file.ReadByte();
            Active = (eActive)file.ReadByte();
            pos = file.ReadLocation();
            Record = NPCRecord.List[file.ReadInt32()];
            Mobile = file.ReadBoolean();
            Summoned = file.ReadInt32();
            Dir = file.ReadDirection();
            health = file.ReadInt32();
            Morale = file.ReadInt32();
            sp = file.ReadInt32();
            ap = file.ReadInt32();
            for (int a = 0; a < status.Length; a++) status[a] = file.ReadInt32();
            Start = town.GetNPCStartByIndex(file.ReadInt32());
        }

        public void LoadGameCharLinks(BinaryReader file, TownMap town)
        {
            Target = file.ReadCharacter(town);
            LastAttacked = file.ReadCharacter(town);
        }

        public void SaveGame(BinaryWriter file, TownMap town)
        {
            file.WriteStuff(WanderTarget, Provocation, (byte)Attitude, (byte)Active, pos, Record.Num,
                Mobile, Summoned, Dir, health, Morale, sp, ap);
            for (int a = 0; a < status.Length; a++) file.Write(status[a]);
            file.Write(town.NPCStartIndex(Start));

            //Save these.
       /*     public ICharacter Target; //Who it's currently trying to fight.
            Location WanderTarget; //Was monster_targs - this stores the square a creature wanders to when it is not hostile (used in rand_move)
            int Provocation; //This is calculated at the end of every npcs turn based on what it did that turn. Attacking or casting a spell is a big provocation.
            ICharacter LastAttacked; //Did the npc attack another character last turn? Used when an enemy npc is deciding who to target.
            public eAttitude Attitude; //Whether the NPC is an ally or enemy of the PCs
            public eActive Active; //Whether the NPC will attempt to attack its enemy
            Location pos;
            public NPCRecord Record;
            public Boolean Mobile;
            public int Summoned;
            public NPCStart Start;
            public Direction direction;
            public int health, Morale, MP, AP;
            int[] status = new int[15];*/
        }

        public void SaveGameCharLinks(BinaryWriter file, TownMap town)
        {
            //Can't save this in SaveGame because we need to have loaded all the NPCs before these vars to a specific one.
            file.Write(Target, town);
            file.Write(LastAttacked, town);
        }

    }

    public partial class Item
    {
        public void SaveGame(BinaryWriter file)
        {
            file.WriteStuff(
                ID.DeNull(),
                Name.DeNull(),
                ShortName.DeNull(),
                (short)Variety,
                (short)Level,
                (sbyte)Awkward,
                (sbyte)Bonus,
                (sbyte)Protection,
                (short)Charges,
                (sbyte)MeleeType,
                (sbyte)MagicUseType,
                (short)Picture,
                (byte)Ability,
                (byte)AbilityStrength,
                (byte)TypeFlag,
                (byte)IsSpecial,
                (byte)a,
                (short)BaseValue,
                (byte)Weight,
                (byte)SpecialClass,
                Pos,
                (byte)TreasureClass,
                (byte)Properties,
                SpellID.DeNull(),
                AlchemyID.DeNull());
        }
    }

    public partial class WorldMapType : IMap
    {
        public void LoadGame(BinaryReader file)
        {
            foreach (OutsideSector o in OutsideSector.List)
            {
                for (int x2 = 0; x2 < Constants.SECTOR_WIDTH; x2++)
                    for (int y2 = 0; y2 < Constants.SECTOR_HEIGHT; y2++)
                        {
                            if (Game.DebugLoad)
                                file.ReadUInt16(); //Don't overwrite scenario terrain data with data stored in saved game file.
                            else
                                o[x2, y2] = file.ReadUInt16();
                            o.Explored[x2, y2] = file.ReadBoolean();
                        }

                    //Load TriggerSpot's Active property (8 per byte)
                    byte byt = 0;
                    byte bitcount = 0;
                    for (int z = 0; z < o.TriggerSpotList.Count; z++)
                    {
                        if (bitcount == 0)
                        {
                            byt = file.ReadByte();
                            bitcount = 8;
                        }
                        o.TriggerSpotList[z].Active = (byt & 128) != 0;
                        byt <<= 1;
                        bitcount--;
                    }
            }

            int count = file.ReadInt32();
            for (int n = 0; n < count; n++)
                NPCGroupList.Add(new Encounter(EncounterRecord.List[file.ReadString()], file.ReadLocation()));
        }

        public void SaveGame(BinaryWriter file)
        {
            foreach (OutsideSector o in OutsideSector.List)
            {
                for (int x2 = 0; x2 < Constants.SECTOR_WIDTH; x2++)
                    for (int y2 = 0; y2 < Constants.SECTOR_HEIGHT; y2++)
                    {
                        file.Write((ushort)(o[x2, y2]));
                        file.Write(o.Explored[x2, y2]);
                    }

                //Save Trigger spots 'Active' property. Pack 8 into 1 byte
                byte byt = 0;
                byte bitcount = 0;

                for (int z = 0; z < o.TriggerSpotList.Count; z++)
                {
                    if (bitcount == 8)
                    {
                        file.Write(byt);
                        byt = 0;
                        bitcount = 0;
                    }
                    byt <<= 1;
                    if (o.TriggerSpotList[z].Active) byt |= 1;
                    bitcount++;
                }
                if (bitcount > 0)
                {
                    byt <<= 8 - bitcount;
                    file.Write(byt);
                }
            }

            file.Write(NPCGroupList.Count);

            foreach (Encounter npc in NPCGroupList)
            {
                
                //int q = NPCGroupRecord.List.IndexOf(npc.Record);
                file.Write(npc.Record.ID);//NPCGroupRecord.List.ElementAt(q).Key);
                file.Write(npc.Pos);
            }
        }
    }

    public partial class PartyType : IExpRecipient
    {
        public void SaveGame(BinaryWriter file)
        {
            LastSavedDate = DateTime.Now;

            file.Write(Name);
            file.Write(CreationDate.ToBinary());
            file.Write(LastSavedDate.ToBinary());
            file.Write(Age);
            file.Write(gold);
            file.Write(food);
            file.Write(LightLevel);
            file.Write(OutsidePos);
            file.Write(outsideDir);
            file.Write(Stealth);
            file.Write(Firewalk);
            file.Write(Flying);

            file.Write(IsSplit);
            file.Write(SplitPos);

            file.Write(DetectMonster);
            file.Write(total_dam_done);
            file.Write(total_m_killed);
            file.Write(total_xp_gained);
            file.Write(total_dam_taken);

            //Write Spell key shortcuts
            file.Write(SpellKeyShortcuts.Count);
            foreach (var entry in SpellKeyShortcuts)
            {
                file.Write(entry.Key);
                file.Write((byte)entry.Value);
            }

            file.Write(KnownRecipes.Count);
            foreach (var r in KnownRecipes.Keys)
                file.Write(r);

            foreach(PCType pc in PCList)
            {
                pc.SaveGame(file);
            }
            file.Write(currentPC.Slot);
        }

        public PartyType(BinaryReader file, string filename)
        {
            Name = file.ReadString();
            CreationDate = DateTime.FromBinary(file.ReadInt64());
            LastSavedDate = DateTime.FromBinary(file.ReadInt64());
            Age = file.ReadInt32();
            gold = file.ReadInt32();
            food = file.ReadInt32();
            LightLevel = file.ReadInt32();
            OutsidePos = file.ReadLocation();
            outsideDir = file.ReadDirection();
            Stealth = file.ReadInt32();
            Firewalk = file.ReadInt32();
            Flying = file.ReadInt32();

            IsSplit = file.ReadBoolean(); 
            SplitPos = file.ReadLocation();

            DetectMonster = file.ReadInt32();
            total_dam_done = file.ReadInt64();
            total_m_killed = file.ReadInt32();
            total_xp_gained = file.ReadInt64();
            total_dam_taken = file.ReadInt64();

            int i = file.ReadInt32();
            //Read Spell Key shortcuts
            for (int n = 0; n < i; n++)
            {
                SpellKeyShortcuts.Add(file.ReadString(), (Keys)file.ReadByte());
            }

            i = file.ReadInt32();
            for (int n = 0; n < i; n++)
            {
                KnownRecipes.Add(file.ReadString(), null);
            }

            PCList = new List<PCType>();
            for (int n = 0; n < Constants.PC_LIMIT; n++)
            {
                PCList.Add(new PCType(file, n));
            }

            currentPC = PCList[file.ReadInt32()];

            //activePC = null; //This forces the Highlight graphic to redraw for the current PC
            activePC = LeaderPC;
        }
    }

    public partial class PCType : IInventory, ICharacter, IExpRecipient, IAnimatable
    {
        public void SaveGame(BinaryWriter file)
        {
            file.Write((byte)LifeStatus);
            file.Write((byte)BackupLifeStatus);
            file.Write(name);
            for (int a = 0; a < 30; a++) file.Write(skills[a]);
            file.Write(max_health);
            file.Write(max_sp);
            file.Write(experience);
            file.Write(level);
            file.Write(cur_health);
            file.Write(cur_sp);
            file.Write(skill_pts);
            for (int a = 0; a < 15; a++) file.Write(status[a]);
            file.Write(Portrait);
            file.Write(which_graphic);

            Gfx.SavePCGraphics(file, PCTexture, PortraitTexture);


            file.Write(ItemList.Count);
            foreach (Item i in ItemList) i.SaveGame(file);

            int poisoned = -1;
            for (int a = 0; a < EquippedItemSlots.Length; a++)
            {
                if (EquippedItemSlots[a] == null) file.Write(false);
                else
                {
                    file.Write(true);
                    EquippedItemSlots[a].SaveGame(file);
                    if (EquippedItemSlots[a] == PoisonedWeapon) poisoned = a;
                }
            }
            file.Write(poisoned);

            file.Write(KnownSpells.Count);
            foreach (string s in KnownSpells.Keys)
                file.Write(s);

            for (int n = 0; n < Trait.Index.Length; n++)
                file.Write(Traits.Contains(Trait.Index[n]));
        }

        public PCType(BinaryReader file, int slot)
        {
            Slot = slot;
            LifeStatus = (eLifeStatus)file.ReadByte();
            BackupLifeStatus = (eLifeStatus)file.ReadByte(); 

            name = file.ReadString();
            for (int a = 0; a < 30; a++) skills[a] = file.ReadInt32();
            max_health = file.ReadInt32();
            max_sp = file.ReadInt32();
            experience = file.ReadInt32();
            level = file.ReadInt32();
            cur_health = file.ReadInt32();
            cur_sp = file.ReadInt32();
            skill_pts = file.ReadInt32();
            for (int a = 0; a < 15; a++) status[a] = file.ReadInt32();
            Portrait = file.ReadInt32();
            which_graphic = file.ReadInt32();

            Gfx.LoadPCGraphics(file, out PCTexture, out PortraitTexture);


            //lastSlot = file.ReadInt32();
            int count = file.ReadInt32();
            for (int n = 0; n < count; n++)
            {
                Item i = new Item();
                i.LoadInstance(file);
                ItemList.Add(i);
            }
            for (int a = 0; a < EquippedItemSlots.Length; a++)
            {
                if (file.ReadBoolean())
                {
                    Item i = new Item();
                    i.LoadInstance(file);
                    EquippedItemSlots[a] = i;
                }
            }
            int poisoned = file.ReadInt32();
            if (poisoned >= 0) PoisonedWeapon = EquippedItemSlots[poisoned];

            count = file.ReadInt32();
            for (int n = 0; n < count; n++)
                KnownSpells.Add(file.ReadString(), null);

            //count = file.ReadInt32();
            //for (int n = 0; n < count; n++)
            //    file.ReadString();// FavouriteSpells.Add(file.ReadString(), null);

            for (int n = 0; n < Trait.Index.Length; n++)
                if (file.ReadBoolean()) Traits.Add(Trait.Index[n]);



            //if (Slot == 3)
            //{
            //    KnownSpells.Add("m_capture_soul", null);//MagicSpell.List["m_capture_soul"]);
            //    KnownSpells.Add("m_simulacrum", null);//MagicSpell.List["m_simulacrum"]);
            //    SetSkill(eSkill.MAGE_SPELLS, 7);
            //    max_sp = 100;
            //    SP = 100;
            //}





        }

    }


}