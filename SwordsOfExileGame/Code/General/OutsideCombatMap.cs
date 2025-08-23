namespace SwordsOfExileGame;

public class CombatMap : TownMap
{
    public static int GenerateWidth, GenerateHeight;
    public static string GenerateFunc;

    private PartyType Party => Game.CurrentParty;
    public EncounterRecord NPCGroup;

    /// <summary>
    /// Constructor for making a TownMap for the purposes of an outdoor combat encounter.
    /// </summary>
    /// <param name="encounter">The group of NPCs we've encountered here</param>
    /// <param name="underterrain">3x3 array of terrain types The terrain type on the world map the combat map will be based on (mainly the central one)</param>
    /// <param name="overterrain">As above for overlay terrain</param>
    public CombatMap(EncounterRecord encounter, TerrainRecord[,] underterrain, TerrainRecord[,] overterrain)
    {
        NPCGroup = encounter;

        Width = GenerateWidth;
        Height = GenerateHeight;  
        Boundary = new Rectangle(1, 1, Width - 2, Height - 2);

        _Terrain = new ushort[Width, Height];
        _Explored = new bool[Width, Height];
        Misc = new uint[Width, Height];

        Script.RunGenerateMap(GenerateFunc, this, encounter, underterrain, overterrain);
    }
}