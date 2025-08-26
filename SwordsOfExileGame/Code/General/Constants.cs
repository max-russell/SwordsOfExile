namespace SwordsOfExileGame;

internal static class Constants
{
    public const bool COMPATIBILITY_SPECIALS_INTERRUPT_REST = true;
    public const bool COMPATIBILITY_CHECK_TIMERS_WHILE_RESTING = true;
        
    public const int MAX_SPELL_LEVEL = 7;

    public const int TOWN_VISIT_MEMORY = 4;

    public const int DAY_LENGTH = 3700;

    //INTERFACE
    public const int KEY_REPEAT_DURATION_1ST = 200;
    public const int KEY_REPEAT_DURATION_SUBSEQUENT = 20;
    public const int ZOOM_SPEED = 250;

    public const int SAVE_FILE_VERSION = 5;
    public const string SAVE_FILE_KEY = "SWORDSOFEXILESAVEGAME";
    public const ushort SCENARIO_FILE_VERSION = 3;
    public const string SCENARIO_FILE_KEY = "SWORDSOFEXILESCENARIO";

    public const int AUTOSAVE_LIMIT = 3;

    public const int OBSCURITY_LIMIT = 5; //Used when determining if a square can be seen. The Obscurity level of all
    //terrains between A and B is added one by one. When it gets above this value
    //the vision is completely opaque.
    public const int SIGHT_RANGE = 20;

    public const int FLEE_PROBABILITY = 40; //Percentage chance the PC will leave the combat map

    public const int ITEM_VALUE_IDENTIFY_LIMIT = 16; //Items below this value are always identified
    public const int ITEM_STACK_LIMIT = 999;

    //TOWN
    public const int AREA_NPC_LIMIT = 60; //Total number of creatures allowed in town.
    public const int CREATURE_WANDERINGSPAWN_LIMIT = 50; //Number of creatures in town above which wandering monsters will not spawn.
    public const int PATHFINDLIMIT = 20;
    public const int PATH_NASTY_FIELD_AVERSION = 15;//9;

    public const int PATH_NASTY_FIELD_AVERSION_MIN = 5,
        PATH_NASTY_FIELD_AVERSION_MAX = 50,
        PATH_NASTY_FIELD_AVERSION_HEALTH_LOW = 25,
        PATH_NASTY_FIELD_AVERSION_HEALTH_HIGH = 100;

    public const int TOWN_WANDERING_SPAWN_CHANCE = 70; //1 in x chance of spawning per turn.

    public const int POPUP_ITEMLIST_LIMIT = 10;

    //OUTSIDE
    public const int SECTOR_WIDTH = 48, SECTOR_HEIGHT = 48;
    public const int NPC_GROUP_LIMIT = 10, //How many wandering NPC group can exist at a time.
        NPC_GROUP_CULL_DISTANCE = 24, //At what distance from the party we're permitted to cull NPC groups if need be.
        SPAWN_MAX_DISTANCE = 48,
        SPAWN_MIN_DISTANCE = 5,
        NPC_GROUP_VISIBLE_DISTANCE = 20, //How close to the party the NPC Group has to be to be drawn
        OUTSIDE_WANDERING_SPAWN_CHANCE = 100; //1 in x chance of spawning per turn.

    //SHOP CONSTANTS
    public static int RESURRECTION_PRICE = 1000,
        DESTONE_PRICE = 500,
        HEAL_PRICE = 200;
    public static int[] SHOP_PRICE_MULTIPLIER = { 5, 7, 10, 13, 16, 20, 25 };

    public const int ITEM_CUSTOM_PIC_START = 150;

    //PARTY
    public const int PC_LIMIT = 6, GOLD_LIMIT = 30000, FOOD_LIMIT = 25000,
        STARTING_GOLD = 200, STARTING_FOOD = 100;

    //AI CONSTANTS
    public const int AI_RETURN_FAVOUR_BONUS = 5; //The higher value makes it more likely an npc will switch its attention to the enemy which attacked it.
    public const int AI_I_HATE_PCS_BONUS = 0; //Gives an extra incentive for npcs to target the player.
    public const int AI_ADJACENCY_BONUS = 5; //Gives an extra incentive to target enemies standing right next to the npc.
    public const float AI_DISTRACTION_CHANCE = 0.2f; //How likely the npc will forget who it was attacking and reconsider its target. (Of course it may choose the same target again)
    public const int AI_ATTACK_PROVOCATION_SCORE = 10;

    public const string NPC_Mage_Spell_Demon_ID = "Demon_85";
    public const string NPC_Mage_Spell_Deva_ID = "Deva_126";
    public const string NPC_Mage_Spell_Shade_ID = "Shade_125";
    public const string NPC_Mage_Spell_Serpent_ID = "Serpent_99";
    public const string NPC_Mage_Spell_Asp_ID = "Asp_100";
    public const string NPC_Mage_Spell_Guardian_ID = "Guardian_122";

    //PC
    public const int PC_FIRING_RANGE = 12,
        PC_THROWING_RANGE = 8,
        EXPERIENCE_CAP = 15000;

}