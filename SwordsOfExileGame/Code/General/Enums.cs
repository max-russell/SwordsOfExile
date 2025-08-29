using System;

namespace SwordsOfExileGame;

public enum eState
{
    GAME_OVER,
    BEGIN_COMBAT_END,
    COMBAT_END,
    BEGIN_LEAVE_MAP,
    LEAVE_MAP,
    BEGIN_ENTER_TOWN,
    ENTER_TOWN,
    BEGIN_PARTY_DEATH,
    BEGIN_PARTY_FLEE,
    PARTY_FLEE,
    TARGET_MODE,
    BEGIN_PC_TURN,
    PICK_NEXT_PC,
    BEGIN_NPC_GROUP_ATTACK,
    NPC_GROUP_ATTACK,
    PC_TURN_PROCESS_ACTION,
    BEGIN_NPC_TURN,
    NPC_TURN,
    END_TURN,
    DO_CAMPING,
    PARTY_DEAD
}

public enum eAction
{
    //Movement actions: triggered by pressing the movement keys
    NONE=0, Up, Down, Left, Right, UpLeft, UpRight, DownLeft, DownRight, StandReady, Wait, Act, 

    //General actions:
    Attack, CastSpell, Search, BoatLanding, StartRest, Parry, QuickSave, QuickLoad, LoadSaveMenu, DoAlchemy, Use, DropItem, FireRanged, EscapeMenu, RunConsoleWindow, ZoomIn, ZoomOut,

    //Menu button actions: triggered by pressing the menu bar buttons, or their key shortcuts
    StartCombat, EndCombat, GatherLoot, ChooseMagicM, ChooseMagicP,

    //Map popupmenu actions - Triggered by selecting an option from a context menu on the map
    Talk, TakeItemMap, TakeAllItemMap, BuyItem, SellItem,

    //For when the player must select a target on the map for an action.
    TargetDropItem, MapClick, TargetSearch, TargetTalk, TargetFireRanged, TargetUse, SpellTargeting, ItemSpellTargeting, Space,
    TargetLetterSelectA,
    TargetLetterSelectB,
    TargetLetterSelectC,
    TargetLetterSelectD,
    TargetLetterSelectE,
    TargetLetterSelectF,
    TargetLetterSelectG,
    TargetLetterSelectH,
    TargetLetterSelectI,
    TargetLetterSelectJ,
    TargetLetterSelectK,
    TargetLetterSelectL,

    INVENTORY_LOCKED_ACTIONS, //Placeholder enum - only actions after this are processed when a loot/shop window is active.

    //Ok presses the default button on windows that appear that aren't modal (like loot windows)
    Cancel, Ok,

    //Inventory popupmenu actions - triggered by selecting an option from a context menu on an item
    TakeItem, TakeAllItems, EquipItem, UnequipItem, GiveItem, DropItemToLootSpot, UseItem,

    DRAG_ITEM_LOCKED_ACTIONS, //Placeholder - only actions after this are process when an item is being dragged

    //Triggered by dragging and dropping items between inventory boxes with the mouse
    PlaceInInventory, PlaceInEquipSlot, ShowInventoryWin, ShowCharacterWin,

    MAGIC_LOCK_ACTIONS,

    ChangeCurrentPC, 

    BLOCKABLE_ACTIONS,

    //Actions that need completing after a script has run - cannot be cancelled.
    CompleteMove, CompleteSearch, CompleteCastSpell, CompleteCastItemSpell,

    ALL_ACTIONS
}

public enum eCursor
{
    SWORD, NW, N, NE, TALK, USE, W, WAIT, E, BOOT, TARGET, SW, S, SE, LOOK
};

public enum eTurn { PLAYER = 0, NPCS };

public enum eMode { OUTSIDE, TOWN, COMBAT }

public enum eDir { N = 0, NE = 1, E = 2, SE = 3, S = 4, SW = 5, W = 6, NW = 7, None = -1 }

public enum eBlock2
{
    CLEAR = 0,    // Anyone can cross
    CLEAR_PC = 1, // Only PCs can cross
    CLEAR_NO_PLACE = 2, //Characters can walk through but won't be placed here (spawn npcs or place pcs for combat)
    BLOCKED = 3  // No-one can cross
}

public enum eCallOrigin
{
    MOVING,
    SEARCHING,
    CAST_SPELL,
    CAST_ITEM_SPELL,
    PRE_TARGET_SPELL,
    ENTERING_TOWN,// 5 - entering town                                                 TownMap.OnEntry / TownMap.OnEntryIfAbandoned (local)
    LEAVING_TOWN,// 6 - leaving town                                                   TownMap.ExitNode[4] (local)
    TALKING, // 7 - talking (a,b - numbers of strings to respond)                      TalkingNode.DataA (when TalkingNode.Type is CALL_TOWN_SPEC or CALL_SCEN_SPEC) (local or global)
    USING_SPECIAL_ITEM, // 8 - using a special item                                    SpecialItem.UseNode (global)
    TIMER,
    KILLED_NPC,// 12 - killed a monst                                                  NPCType.Start.OnKill (local)
    OUTDOOR_ENCOUNTER,// 13 - encountering outdoor enc (a - 1 if no fight)             
    WIN_ENCOUNTER,// 14 - winning outdoor enc
    FLEE_ENCOUNTER,// 15 - fleeing outdoor enc
    SANCTIFY,// 16 - ritual of sanct
    USING,// 17 - using space
    BOATLAND,
    START_SCENARIO,
    TOWN_GETS_ANGRY,
    PC_STOOD_ON,
    NPC_STOOD_ON,
    CUSTOM
}

[Flags]
public enum eTriggerSpot
{
    STEP_ON = 1,       //-------1 //Triggered by step on in non-combat mode (town or outdoors)
    SEARCH  = 2,       //------1- //PC triggers by Searching
    USE     = 4,       //-----1-- //PC triggers by Using
    STOOD_ON = 8,      //----1--- //Triggered at the end of every turn character is stood there. TO DO
    PCS_TRIGGER = 16,  //---1---- //Set if this is triggered by PCs (The PC triggering is set in the PC script parameter passed to the function)
    NPCS_TRIGGER = 32, //--1----- //Set if this is triggered by NPCs (The NPC triggering is set in the NPC script parameter passed to the function) - Not yet implemented triggering for NPCs Step On, only Stood On
    CAST_SPELL = 64,   //-1------ //Triggered by a spell being cast on the spot
    STEP_ON_CMBT = 128,//1------- //Triggered by step on in combat mode
}

public enum eTimerType : byte
{   //What happens when a timer's domain is left
    RESET=0, //Timer is set back to StartCount
    PAUSE=1, //Timer is frozen at current time
    CONTINUE=2, //Timer continues ticking down and resets if recurring, but does not trigger while not in domain
    DELETE=3, //Timer is deleted
}

public enum eDialogPic
{
    NONE=-1,
    STANDARD, //'DLOGPICS.png'
    FACE,     //'TALKPORT.png'
    TERRAIN,  //A terrain
    CREATURE,  //An npc
    CREATURE2x1, CREATURE1x2, CREATURE2x2,
    SCENARIO,  //'SCENPICS.png'
    CUSTOM_TILE, //36x28 tile from custom graphics sheet
    CUSTOM_SQUARE, //36x36 custom graphic split in half over 2 custom slots
    CUSTOM_FACE // 32x32 custom graphic, split in 2.
}

public enum eTalkNodeType
{
    REGULAR = 0,
    RUN_FUNCTION = 1,
    RUN_SHOP = 2,
    RUN_HEALER = 3,  
    RUN_TRAINING = 4,
    RUN_IDENTIFY = 5,
    RUN_ENCHANTING = 6
}
//New Talk Nodes:
// REGULAR = 0 :      Text: Response            Func: Ignored
// RUN_FUNCTION = 1:  Text: Default response    Func: Function
// RUN_SHOP = 2:      Text: Ignored             Func: Shop ID
// RUN_HEALER = 3,    Text: Healer shop name    Func: Price level
// RUN_TRAINING = 4   Text: Ignored             Func: Ignored
// RUN_IDENTIFY = 5   Text: Identify response   Func: Cost to identify
// RUN_ENCHANTING = 6 Text: Enchant response    Func: Type of enchantment

//   All nodes can have a condition attached, checking a stuff_done flag, and optionally setting it if condition passed

public enum eTalkNodeCondition
{
    NONE = 0,
    EQUAL_TO = 1,
    NOT_EQUAL_TO = 2,
    LESS_THAN = 3,
    LESS_THAN_OR_EQUAL_TO = 4,
    GREATER_THAN = 5,
    GREATER_THAN_OR_EQUAL_TO = 6,
    NEVER = 7
}

public enum eTerSpec
{
    NONE = 0,
    CHANGE_WHEN_STEP_ON = 1, //Flag 1 - Terrain to change to  Flag 2 - Sound on opening
    DOES_FIRE_DAMAGE = 2,    //Damage = (1 to Flag1) * Flag2 
    DOES_COLD_DAMAGE = 3,    //  Same
    DOES_MAGIC_DAMAGE = 4,   //  Same
    POISON_LAND = 5,         //Flag 1=Effect intensity   Flag2=Percentage chance    
    DISEASED_LAND = 6,       //  Same
    CRUMBLING_TERRAIN = 7,   //Flag 1=Terrain to crumble to
    LOCKABLE_TERRAIN = 8,    //Flag 1=Terrain to lock to
    UNLOCKABLE_TERRAIN = 9,  //Flag 1=Terrain to unlock to   Flag 2=Unlock difficulty (0-10)
    UNLOCKABLE_BASHABLE = 10,//  Same
    //IS_A_SIGN = 11,
    //CALL_LOCAL_SPECIAL = 12,
    //CALL_SCENARIO_SPECIAL = 13,
    IS_A_CONTAINER = 14,     //No flag
    //WATERFALL = 15,
    //CONVEYOR_NORTH = 16,
    //CONVEYOR_EAST = 17,
    //CONVEYOR_SOUTH = 18,
    //CONVEYOR_WEST = 19,
    BLOCKED_TO_MONSTERS = 20,  //No flag
    //TOWN_ENTRANCE = 21,      //Flag 1=Terrain if hidden
    CHANGE_WHEN_USED = 22,   //Flag 1=Terrain to change to
    //CALL_SPECIAL_WHEN_USED = 23,
    //FORGET THAT    HAS_TRIGGER_DOT = 24 //New one used to erase the white dot on the map automatically when the global variable in FUNC_GLOBAL is set to value in flag1 (250 is standard BoE) flag2 is the terrain no to change it to
}

[Flags]
public enum eMapOutExtraBit : byte
{
    //TRIGGER = 1,
    //UNDERLAY = 2,
    //OVERLAY = 4,
    SECRET = 8,
    ENTRANCE = 16,
    ALL_BITS = 255
}
//Flag1: Terrain - 1, 7, 8, 9, 10, 22, 21
//       Number -  2, 3, 4, 5, 6
//Flag2: Sound ID - 1
//       Number -  2, 3, 4, 5, 6, 9, 10

public enum eTrapType
{
    RANDOM = 0,
    BLADE = 1,
    DART = 2,
    GAS = 3,			// poisons all
    EXPLOSION = 4,	// damages all => uses c_town.difficulty rather than level to calculates damages (and even c_town.difficulty /13).
    SLEEP_RAY = 5,
    FALSE_ALARM = 6,
    DRAIN_XP = 7,
    ALERT = 8,		// makes town hostile
    FLAMES = 9,		// damages all => uses level (*5) to calculates damages.
    DUMBFOUND = 10,   //dumbfound all
    DISEASE = 11,
    DISEASE_ALL = 12,
}

public enum ePCRace
{
    HUMAN, NEPHIL, SLITH
}

public enum eLifeStatus
{
    ABSENT = 0,
    ALIVE = 1,
    DEAD = 2,
    DUST = 3,
    STONE = 4,
    FLED = 5,
    SURFACE = 6,
    WON = 7
}
public enum eAffliction
{
    NONE = -1,
    POISONED_WEAPON = 0, 
    BLESS_CURSE = 1, //Minus is a curse, positive is a blessing  //-8 to 8
    POISON = 2, //0 to 8
    HASTE_SLOW = 3, //Minus is slow, positive is haste    -8 to 8
    INVULNERABLE = 4,    //0 to 8
    MAGIC_RESISTANCE = 5,   //0 to 8
    WEBS = 6,   //0 to 8
    DISEASE = 7,  //0 to 8
    INVISIBLE = 8, //sanctuary   //0 to 8
    DUMB = 9,   //0 to 8
    MARTYRS_SHIELD = 10,   
    ASLEEP = 11,  //0 to 8
    PARALYZED = 12,  //0 to 5000
    ACID = 13 //0 to 8
}

public enum eEnchantShop
{
    PLUS_1, PLUS_2, PLUS_3, SHOOT_FLAMES, FLAMING, PLUS_5, BLESSED
}

public enum eSkill
{
    STRENGTH = 0,
    DEXTERITY = 1,
    INTELLIGENCE = 2,
    EDGED_WEAPONS = 3,
    BASHING_WEAPONS = 4,
    POLE_WEAPONS = 5,
    THROWN_MISSILES = 6,
    ARCHERY = 7,
    DEFENSE = 8,
    MAGE_SPELLS = 9,
    PRIEST_SPELLS = 10,
    MAGE_LORE = 11,
    ALCHEMY = 12,
    ITEM_LORE = 13,
    DISARM_TRAPS = 14,
    LOCKPICKING = 15,
    ASSASSINATION = 16,
    POISON = 17,
    LUCK = 18,

    NOT_REALLY_SKILLS = 99,
    HEALTH = 100,
    SPELLPTS = 101
}

public enum eSpellTarget
{
    CASTER = 0,
    LIVING_PC = 1,
    DEAD_PC = 2,
    CHARACTER = 3,
    LOCATION = 4
}

public enum eSpellWhere
{
    EVERYWHERE = 0,
    COMBAT = 1,
    TOWN = 2,
    TOWN_AND_OUTDOOR = 3,
    TOWN_AND_COMBAT = 4,
    OUTDOOR = 5
}

public class Trait
{
    public string Name, Description;
    public int Handicap;
    public bool Race;
       
    public Trait(int i, string nm, int handicap, bool is_a_race, string desc)
    {
        Name = nm; Handicap = handicap; Race = is_a_race; Description = desc;
        Index[i] = this;
        if (!is_a_race) MaxCanHave++; //Add to number of possible traits a character can have (PC must have 1 and only 1 race trait)
    }
    public static Trait[] Index = new Trait[19];

    public static int MaxCanHave = 1;

    public static Trait Tough = new(0, "Toughness", 10, false,
        "This makes you more resistant to damage. Blows of all sorts have less of an effect on you.");
    public static Trait MagicallyApt = new(1, "Magically Apt", 20, false,
        "The possessor of this advantage will find that his or her spells will function better. This helps both Priest and Mage spells.");
    public static Trait Ambidextrous = new(2, "Ambidextrous", 8, false,
        "An ambidextrous warrior will be able to use one weapon in each hand without any penalties. Normally, using two weapons makes both of them much less likely to hit.");
    public static Trait Nimble = new(3, "Nimble Fingers", 10, false,
        "Having nimble fingers improves one's chances of picking locks and disarming traps.");
    public static Trait CaveLore = new(4, "Cave Lore", 4, false,
        "When underground, knowledge of Cave Lore helps one hunt and forage for food and deal better with special circumstances.");
    public static Trait Woodsman = new(5, "Woodsman", 6, false,
        "When roaming the surface of the world, a Woodsman is able to hunt and bring down food, find useful herbs, and deal with circumstances involving nature's adversity.");
    public static Trait Constitution = new(6, "Good Constitution", 10, false,
        "Someone with a Good Constitution will find that poison and disease have a reduced (although not eliminated) effect.");
    public static Trait Alert = new(7, "Highly Alert", 7, false,
        "Highly Alert people have the edginess that helps them resist magical sleep. In addition, having someone in your group who is Highly Alert may help keep you from being surprised.");
    public static Trait Strong = new(8, "Exceptional Strength", 12, false,
        "An Exceptionally Strong character will be able to carry much more stuff, and, in addition, will do a small amount more damage in combat.");
    public static Trait Recuperation = new(9, "Recuperation", 15, false,
        "A very few adventurers have magical blood running in their veins, causing them to heal damage to their bodies at an amazing rate.");
    public static Trait Sluggish = new(10, "Sluggish", -10, false,
        "Sluggish characters just can't move that quickly, even when circumstances seem to demand it. A sluggish character gets fewer action points in combat.");
    public static Trait MagicallyInept = new(11, "Magically Inept", -8, false,
        "Magically Inept characters, for some reason, resist the effects of magical items, and are unable to use them. Potions and scrolls won't work for them at all, although worn items, such as rings and armor, will have a small effect.");
    public static Trait Frail = new(12, "Frail", -8, false,
        "Frail characters are cursed at birth with a weak constitution. Poison and disease will have a greater effect on such characters.");
    public static Trait ChronicDisease = new(13, "Chronic Disease", -20, false,
        "Chronic Disease is the worst disadvantage a character may possess. Such characters have a slow, lingering, incurable physical ailment, causing them to occasionally suffer the effects of a mild disease.");
    public static Trait BadBack = new(14, "Bad Back", -8, false,
        "A character with a Bad Back cannot bear to haul too much weight. Such a person cannot carry as much as he or she might have been able to otherwise.");
    public static Trait Pacifist = new(15, "Pacifist", -50, false, 
        "You hate hurtin' people!"); 
    public static Trait Human = new(16, "Human", 0, true,
        "Human is the default species in Blades of Exile. Humans have skins of a variety of hues, and are soft, generally fragile, and incredibly resourceful.");
    public static Trait Slitherzakai = new(17, "Slitherzakai", 20, true,
        "The Slithzerikai (sliths for short) are a race of lizard men, both strong and smart. Once unknown on the surface world, they are starting to appear there. Slith characters get bonuses to strength and intelligence, and are better at using pole weapons.");
    public static Trait Nephilim = new(18, "Nephilim", 12, true,
        "The Nephilim are a race of feline humanoids. Once common on the surface world, they have been hunted to near extinction, although some now remain in Exile. Nephilim characters start with better dexterity, and are much better at using missile weapons.");

}

public enum eActive { 
    INACTIVE,  //Not discovered yet. Will stay still
    DOCILE,    //Active, but not doing anything specific. Will Wander around
    COMBATIVE  //Active, and will engage the nearest enemy
};

public enum eAttitude { 
    NOT_SPECIFIED = -1, 
    NEUTRAL = 0, 
    HOSTILE_A = 1, 
    FRIENDLY = 2, 
    HOSTILE_B = 3
}

public enum eNPCAppear
{
    NEVER_HERE = -1,
    ALWAYS_HERE = 0,
    APPEAR_WHEN = 1,
    DISAPPEAR_WHEN = 2,
    SOMETIMES_A = 4,
    SOMETIMES_B = 5,
    SOMETIMES_C = 6,
    APPEAR_EVENT = 7,
    DISAPPEAR_EVENT = 8,
    USE_SCRIPT = 9
}

public enum eCSS
{ //Creature Special Skill

    NO_SPECIAL_ABILITY = 0,
    THROWS_DARTS = 1,
    SHOOTS_ARROWS = 2,
    THROWS_SPEARS = 3,
    THROWS_ROCKS1 = 4,    //4-24 damages
    THROWS_ROCKS2 = 5,    //5-30 damages
    THROWS_ROCKS3 = 6,    //6-36 damages
    THROWS_RAZORDISKS = 7,
    PETRIFICATION_RAY = 8,
    SP_DRAIN_RAY = 9,    //spell points drain ray
    HEAT_RAY = 10,
    INVISIBLE = 11,
    SPLITS = 12,
    MINDLESS = 13,
    BREATHES_STINKING_CLOUDS = 14,
    ICY_TOUCH = 15,
    XP_DRAINING_TOUCH = 16,
    ICY_AND_DRAINING_TOUCH = 17,
    SLOWING_TOUCH = 18,
    SHOOTS_WEB = 19,
    GOOD_ARCHER = 20,
    STEALS_FOOD = 21,
    PERMANENT_MARTYRS_SHIELD = 22,
    PARALYSIS_RAY = 23,
    DUMBFOUNDING_TOUCH = 24,
    DISEASE_TOUCH = 25,
    ABSORB_SPELLS = 26,
    WEB_TOUCH = 27,
    SLEEP_TOUCH = 28,
    PARALYSIS_TOUCH = 29,
    PETRIFYING_TOUCH = 30,
    ACID_TOUCH = 31,
    BREATHES_SLEEP_CLOUDS = 32,
    ACID_SPIT = 33,
    SHOOTS_SPINES = 34,
    DEATH_TOUCH = 35,
    INVULNERABILITY = 36,
    GUARD = 37
}

/* Monster Type a.k.a m_type */
public enum eGenus
{
    UNKNOWN = -1, // for parameters to some functions; not valid in the class
    HUMAN = 0,
    REPTILE = 1,
    BEAST = 2,
    IMPORTANT = 3,
    MAGE = 4,
    PRIEST = 5,
    HUMANOID = 6,
    DEMON = 7,
    UNDEAD = 8,
    GIANT = 9,
    SLIME = 10,
    STONE = 11,
    BUG = 12,
    DRAGON = 13,
    MAGICAL = 14,
}

public enum eRadiate
{
    NONE = 0,
    FIRE = 1,
    ICE = 2,
    SHOCK = 3,
    ANTIMAGIC = 4,
    SLEEP = 5,
    STINK = 6,
    // 7,8 and 9 are unused
    SUMMON = 10,    //5 percent chance
    //SUMMON2 = 11,    //20 percent chance
    //SUMMON3 = 12,    //50 percent chance
    // 13 and 14 are unused
    DEATH_TRIGGERS = 15        //death triggers global special
}

public enum eVehicleType
{
    NONE = -1,
    HORSE = 0,
    BOAT = 1
}

/* damage type*/
/* used as parameter to some functions */
public enum eDamageType
{
    WEAPON = 0,
    FIRE = 1,
    POISON = 2,
    MAGIC = 3,
    UNBLOCKABLE = 4, //from the source files - the display is the same as the magic one (damage_monst in SPECIALS.cpp)
    COLD = 5,
    UNDEAD = 6, //from the source files - the display is the same as the weapon one
    DEMON = 7, //from the source files - the display is the same as the weapon one
    // 8 and 9 aren't defined : doesn't print any damage. According to the source files the 9 is MARKED though. Wrong ?
    MARKED = 10, // usage: MARKED + damage_type
    WEAPON_MARKED = 10,
    FIRE_MARKED = 11,
    POISON_MARKED = 12,
    MAGIC_MARKED = 13,
    UNBLOCKABLE_MARKED = 14,
    COLD_MARKED = 15,
    UNDEAD_MARKED = 16,
    DEMON_MARKED = 17,
    NO_PRINT = 30, // usage: NO_PRINT + damage_type
    WEAPON_NO_PRINT = 30,
    FIRE_NO_PRINT = 31,
    POISON_NO_PRINT = 32,
    MAGIC_NO_PRINT = 33,
    UNBLOCKABLE_NO_PRINT = 34,
    COLD_NO_PRINT = 35,
    UNDEAD_NO_PRINT = 36,
    DEMON_NO_PRINT = 37,
    // What about both NO_PRINT and MARKED?
}

public enum eBreathType
{
    FIRE, COLD, ELECTRICITY, DARKNESS
}

public enum eMonsterAttackTypes
{
    SWINGS = 0,
    CLAWS = 1,
    BITES = 2,
    SLIMES = 3,
    PUNCHES = 4,
    STINGS = 5,
    CLUBS = 6,
    BURNS = 7,
    HARMS = 8,
    STABS = 9,
};

public enum eMMageSpells
{
    NO_SPELL = 0,
    SPARK = 1,
    MINOR_HASTE = 2,
    STRENGH = 3,
    FLAME_CLOUD = 4,
    FLAME = 5,
    MINOR_POISON = 6,
    SLOW = 7,
    DUMBFOUND = 8,
    STINKING_CLOUD = 9,
    SUMMON_BEAST = 10,
    CONFLAGRATION = 11,
    FIREBALL = 12,
    WEAK_SUMMONING = 13,
    WEB = 14,
    POISON = 15,
    ICE_BOLT = 16,
    SLOW_GROUP = 17,
    MAJOR_HASTE = 18,
    FIRESTORM = 19,
    SUMMONING = 20,
    SHOCKSTORM = 21,
    MAJOR_POISON = 22,
    KILL = 23,
    DAEMON = 24,
    MAJOR_BLESSING = 25,
    MAJOR_SUMMONING = 26,
    SHOCKWAVE = 27,
};

public enum eMPriestSpells
{
    NO_SPELL = 0,
    MINOR_BLESS = 1,
    LIGHT_HEAL = 2,
    WRACK = 3,
    STUMBLE = 4,
    BLESS = 5,
    CURSE = 6,
    WOUND = 7,
    SUMMON_SPIRIT = 8,
    DISEASE = 9,
    HEAL = 10,
    HOLY_SCOURGE = 11,
    SMITE = 12,
    CURSE_ALL = 13,
    STICKS_TO_SNAKES = 14,
    MARTYRS_SHIELD = 15,
    BLESS_ALL = 16,
    MAJOR_HEAL = 17,
    FLAMESTRIKE = 18,
    SUMMON_HOST = 19,
    REVIVE_SELF = 20,// renamed from heal all, to avoid confusion (this isn't a mass spell !)
    UNHOLY_RAVAGING = 21,
    SUMMON_GUARDIAN = 22,
    PESTILENCE = 23,
    REVIVE_ALL = 24,
    AVATAR = 25,
    DIVINE_THUD = 26
};

[Flags]
public enum eImmunity
{
    NONE = 0,
    MAGIC_RESISTANCE = 1,
    MAGIC_IMMUNITY = 2,
    FIRE_RESISTANCE = 4,
    FIRE_IMMUNITY = 8,
    COLD_RESISTANCE = 16,
    COLD_IMMUNITY = 32,
    POISON_RESISTANCE = 64,
    POISON_IMMUNITY = 128,
    MAGIC = MAGIC_RESISTANCE | MAGIC_IMMUNITY,
    FIRE = FIRE_RESISTANCE | FIRE_IMMUNITY,
    COLD = COLD_RESISTANCE | COLD_IMMUNITY,
    POISON = POISON_RESISTANCE | POISON_IMMUNITY
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////ITEM ENUMS/////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

public enum eVariety
{
    None = 0, OneHanded = 1, TwoHanded = 2, Gold = 3, Bow = 4, Arrows = 5, Thrown, Potion, Scroll,
    Wand = 9, Tool = 10, Food = 11, Shield = 12, Armour, Helm = 14, Gloves, Shield2, Boots, Ring,
    Necklace = 19, Poison, NonUse, Trousers, Crossbow = 23, Bolts = 24, RangedNoAmmo, Unused1, Unused2
}

public enum eMeleeWeaponType
{
    EDGED=1, BLUNT=2, POLE=3
}

public enum eEquipSlot
{
    None = -1, MainHand, OffHand, Ranged, Ammo, Head, Hands, Feet, Ring1, Ring2, Necklace, Legs, Torso, Tool
}

//1 Main hand     1-handed weapon / 2 handed weapon
//2 Off-hand      Shield / 2 handed-weapon
//3 Ranged Weapon Bow / crossbow / discs
//4 Ammo          Arrows / Bolts
//5 Head          Helmet
//6 Hands         Gloves
//7 Feet          Boots
//8 Ring1
//9 Ring2
//10 Necklace
//11 Legs          Trousers

public enum eItemAbil
{
    // Weapon abilities
    NO_ABILITY = 0,
    FLAMING_WEAPON = 1,
    DEMON_SLAYER = 2,
    UNDEAD_SLAYER = 3,
    LIZARD_SLAYER = 4,
    GIANT_SLAYER = 5,
    MAGE_SLAYER = 6,
    PRIEST_SLAYER = 7,
    BUG_SLAYER = 8,
    ACIDIC_WEAPON = 9,
    SOULSUCKER = 10,
    DRAIN_MISSILES = 11,
    WEAK_WEAPON = 12,
    CAUSES_FEAR = 13,
    POISONED_WEAPON = 14,
    // General abilities
    PROTECTION = 30,
    FULL_PROTECTION = 31,
    FIRE_PROTECTION = 32,
    COLD_PROTECTION = 33,
    POISON_PROTECTION = 34,
    MAGIC_PROTECTION = 35,
    ACID_PROTECTION = 36,
    SKILL = 37,
    STRENGTH = 38,
    DEXTERITY = 39,
    INTELLIGENCE = 40,
    ACCURACY = 41,
    THIEVING = 42,
    GIANT_STRENGTH = 43,
    LIGHTER_OBJECT = 44,
    HEAVIER_OBJECT = 45,
    OCCASIONAL_BLESS = 46,
    OCCASIONAL_HASTE = 47,
    LIFE_SAVING = 48,
    PROTECT_FROM_PETRIFY = 49,
    REGENERATE = 50,
    POISON_AUGMENT = 51,
    DISEASE_PARTY = 52,
    WILL = 53,
    FREE_ACTION = 54,
    SPEED = 55,
    SLOW_WEARER = 56,
    PROTECT_FROM_UNDEAD = 57,
    PROTECT_FROM_DEMONS = 58,
    PROTECT_FROM_HUMANOIDS = 59,
    PROTECT_FROM_REPTILES = 60,
    PROTECT_FROM_GIANTS = 61,
    PROTECT_FROM_DISEASE = 62,
    // Nonspell Usable
    POISON_WEAPON = 70, //put poison on weapon
    BLESS_CURSE = 71,
    AFFECT_POISON = 72,
    HASTE_SLOW = 73,
    AFFECT_INVULN = 74,
    AFFECT_MAGIC_RES = 75,
    AFFECT_WEB = 76,
    AFFECT_DISEASE = 77,
    AFFECT_SANCTUARY = 78,
    AFFECT_DUMBFOUND = 79,
    AFFECT_MARTYRS_SHIELD = 80,
    AFFECT_SLEEP = 81,
    AFFECT_PARALYSIS = 82,
    AFFECT_ACID = 83,
    BLISS = 84,
    AFFECT_EXPERIENCE = 85,
    AFFECT_SKILL_POINTS = 86,
    AFFECT_HEALTH = 87,
    AFFECT_SPELL_POINTS = 88,
    DOOM = 89,
    LIGHT = 90,
    STEALTH = 91,
    FIREWALK = 92,
    FLYING = 93,
    MAJOR_HEALING = 94,
    CALL_SPECIAL = 95, //new (Classic Blades of Exile) item property
    // Reagents
    HOLLY = 150, // Holly/Toadstool
    COMFREY_ROOT = 151,
    GLOWING_NETTLE = 152,
    WORMGRASS = 153, // Crypt Shroom/Wormgr.
    ASPTONGUE_MOLD = 154,
    EMBER_FLOWERS = 155,
    GRAYMOLD = 156,
    MANDRAKE = 157,
    SAPPHIRE = 158,
    SMOKY_CRYSTAL = 159,
    RESURRECTION_BALM = 160,
    LOCKPICKS = 161,
    // Missile Abilities
    MISSILE_RETURNING = 170,
    MISSILE_LIGHTNING = 171,
    MISSILE_EXPLODING = 172,
    MISSILE_ACID = 173,
    MISSILE_SLAY_UNDEAD = 174,
    MISSILE_SLAY_DEMON = 175,
    MISSILE_HEAL_TARGET = 176,

    CAST_SPELL = 177//NEW - replace all the spell abilities with this one and a new string property
    //for each item of the spell to cast.
}

public enum eItemFilter { ALL, WEAPONS, ARMOUR, POTIONS, USEABLES, OTHER };

public enum eShop { ITEM, MAGIC, ALCHEMY };