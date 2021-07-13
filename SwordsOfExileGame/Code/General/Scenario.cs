using System;
using System.Collections.Generic;
using System.IO;

namespace SwordsOfExileGame
{
    public partial class Scenario
    {
        static PartyType Party { get { return Game.CurrentParty; } }

        public static string Filename, Name, Description, Credits1, Credits2, ContactInfo;
        static byte[] Version;
        static int Rating, Difficulty;
        static public int IntroPic, IntroMessPic;
        static public string InitialiseFunc,   //Non-latent function that is triggered as soon as the Scenario begins
                             IntroFunc,        //Latent Function that is triggered at the start of the scenario after the fade-up
                             TownPreEntryFunc; //Non-latent Function that is triggered just before any town is entered
                                               //and can be used to alter what town that is.
        static public string DeathMessage;

        static public int OutWidth, OutHeight;
        static public OutsideSector StartOutside;
        static public TownMap StartTown;
        static public Location TownStartPos, OutsideStartPos;

        public static bool Load() {

            Game.ScenarioDirectory = Path.Combine(Game.RootDirectory, "Scenarios", Scenario.Filename);

            Directory.SetCurrentDirectory(Game.ScenarioDirectory);

            string filename = Path.ChangeExtension(Filename, "exs2");

            if (!File.Exists(filename)) return false;

            using (FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read)) {

                using (BinaryReader In = new BinaryReader(fs)) {

                    Filename = filename;
                    if (In.ReadString() != Constants.SCENARIO_FILE_KEY) { Game.FlagError("Loading Error", "'" + filename + "' is not a valid Scenario file"); return false; }
                    if (In.ReadUInt16() != Constants.SCENARIO_FILE_VERSION) { Game.FlagError("Loading Error", "'" + filename + "' is incompatible with this version"); return false; }

                    Name = In.ReadString();
                    Version = In.ReadBytes(3);
                    Description = In.ReadString();
                    Credits1 = In.ReadString();
                    Credits2 = In.ReadString();
                    ContactInfo = In.ReadString();
                    Rating = In.ReadInt16();
                    Difficulty = In.ReadByte();
                    IntroPic = In.ReadByte();
                    In.ReadByte();
                    IntroMessPic = In.ReadInt16();
                    DeathMessage = In.ReadString();
                    InitialiseFunc = In.ReadString();
                    IntroFunc = In.ReadString();
                    TownPreEntryFunc = In.ReadString();
                    CombatMap.GenerateWidth = In.ReadUInt16();
                    CombatMap.GenerateHeight = In.ReadUInt16();
                    CombatMap.GenerateFunc = In.ReadString();
                    Game.WorldMap = new WorldMapType();
                    OutsideSector.List.Load(In);
                    Game.RecentTownList = new List<TownMap>();
                    TownMap.List.Load(In);
                    if (!TownMap.List.TryGetValue(In.ReadString(), out StartTown)) StartTown = TownMap.List[0]; //Start Town
                    TownStartPos = In.ReadLocation();
                    Location loc = In.ReadLocation();
                    StartOutside = Game.WorldMap.SectorAt(loc * 48);// OutsideSectors[loc.x, loc.y];
                    OutsideStartPos = In.ReadLocation();
                    Vehicle.List.Load(In);
                    SpecialItem.List.Load(In);
                    Timer.List.Load(In);
                    TerrainRecord.LoadAll(In);
                    MagicSpell.List.Load(In);
                    Item.List.Load(In);
                    Personality.List.Load(In);
                    Shop.List.Load(In);
                    NPCRecord.LoadAll(In);
                    EncounterRecord.List.Load(In);
                    Game.WorldMap.LoadFull(In);
                    foreach (TownMap t in TownMap.List)
                        t.LoadFull(In);
                    Recipe.LoadIngredients(In);
                    Recipe.List.Load(In);
                }
            }

            Sound.Load(false);
            Notes.Clear();
            GlobalVariables.Clear();
            return true;
        }

        static public void LoadAndDisregardEditorFolder(BinaryReader In)
        {
            //We don't need Editor folders in the Game, but we still need to read past them.
            In.ReadString();//ID
            In.ReadString();//Name
            In.ReadBoolean(); //Open
            In.ReadString(); //Nested Folder
        }

        static public int difficulty_adjust()
        {
            int j = 0;
            int to_return = 1;

            foreach (PCType pc in Party.EachAlivePC())// (i = 0; i < 6; i++)
                j += pc.Level;

            if ((Difficulty <= 0) && (j >= 60)) to_return++;
            if ((Difficulty <= 1) && (j >= 130)) to_return++;
            if ((Difficulty <= 2) && (j >= 210)) to_return++;
            return to_return;
        }

        struct Note
        {
            public string Title, Message;
        }
        static List<Note> Notes = new List<Note>();
        static public void MakeNote(string title, string msg)
        {
            Notes.Add(new Note { Title = title, Message = msg});
        }
        static public IEnumerable<String> ListNotes()
        {
            foreach (Note n in Notes)
                yield return n.Title;
        }
        static public string GetNoteMessage(int n) { if (n >= 0 && n < Notes.Count) return Notes[n].Message; else return ""; }
        static public void DeleteNote(int n) { if (n >= 0 && n < Notes.Count) Notes.RemoveAt(n); }

        static public void End() //Only called from scripts.
        {
            Game.GameOver = true;
            new MessageWindow(null, "Congratulations - you have just completed this scenario! If you want you can save your adventurers now before returning to the main menu.", eDialogPic.NONE, 0, "OK");
        }
    }

    class ScenarioInfo
    {
        public string Filename, Name, Description, Credits1, Credits2, ContactInfo;
        public byte[] Version;
        public int Rating, Difficulty;
        public int IntroPic;

        public static ScenarioInfo LoadScenarioInfo(string fn)
        {
            fn = Path.GetFileNameWithoutExtension(fn);

            string filename = Path.Combine(Game.RootDirectory, "Scenarios", fn, Path.ChangeExtension(fn, "exs2"));
            if (!File.Exists(filename)) return null;

            ScenarioInfo si = new ScenarioInfo();

            using (FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read))
            {

                using (BinaryReader In = new BinaryReader(fs))
                {
                    
                    if (In.ReadString() != Constants.SCENARIO_FILE_KEY) return null;
                    if (In.ReadUInt16() != Constants.SCENARIO_FILE_VERSION) return null;
                    si.Filename = Path.GetFileNameWithoutExtension(filename);
                    si.Name = In.ReadString();
                    si.Version = In.ReadBytes(3);
                    si.Description = In.ReadString();
                    si.Credits1 = In.ReadString();
                    si.Credits2 = In.ReadString();
                    si.ContactInfo = In.ReadString();
                    si.Rating = In.ReadInt16();
                    si.Difficulty = In.ReadByte();
                    si.IntroPic = In.ReadByte();
                }
            }
            return si;
        }

    }

}
