using System.Runtime.InteropServices;

namespace SoE_Converter
{

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct RECT16
    {
        public short left;
        public short top;
        public short right;
        public short bottom;
    }



    //// char Boolean;
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct location
    {
        public sbyte x, y;
    };
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct shortloc {
        private short x, y; };

    internal struct sd { public int X, Y; };

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct special_node_type //22
    {
        public short type, sd1, sd2, pic, m1, m2, ex1a, ex1b, ex2a, ex2b, jumpto;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct talking_node_type
    {
        public short personality, type;                               //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] link1;                                         //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] link2;                                         //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public short[] extras;                                        //8
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct talking_record_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200)]
        public byte[] strlens;// = new byte[200];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 60)]
        public talking_node_type[] talk_nodes;// = new talking_node_type[60];

        public const int SIZE = 200 + 60 * 20;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct terrain_type_type //SIZE: 16
    {
        public short picture;
        public byte blockage, flag1, flag2, special, trans_to_what, fly_over, boat_over;
        public byte block_horse, light_radius, step_sound, shortcut_key, res1, res2, res3;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct wandering_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] monst;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct out_wandering_type //SIZE: 22
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 7)]
        public byte[] monst;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public byte[] friendly;// = new byte[3];
        public short spec_on_meet, spec_on_win, spec_on_flee, cant_flee;
        public short end_spec1, end_spec2;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct outdoor_record_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 48*48)]
        public byte[] terrain;// = new byte[48, 48]; 
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 18)]
        public location[] special_locs;// = new location[18];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 18)]
        public byte[] special_id;// = new byte[18];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public location[] exit_locs;// = new location[8];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public sbyte[] exit_dests;// = new sbyte[8];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public location[] sign_locs;// = new location[8];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public out_wandering_type[] wandering;// = new out_wandering_type[4];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public out_wandering_type[] special_enc;// = new out_wandering_type[4];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public location[] wandering_locs;// = new location[4];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public RECT16[] info_rect;// = new RECT16[8];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 180)]
        public byte[] strlens;// = new byte[180];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 60)]
        public special_node_type[] specials;// = new special_node_type[60];

        public const int SIZE = 48 * 48 + 18 * 2 + 18 + 8 * 2 + 8 + 8 * 2 + 4 * 22 + 4 * 22 + 8 + 8 * 8 + 180 + 60 * 22;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct creature_start_type
    {
        public byte number;
        public byte start_attitude;
        public location start_loc;
        public byte mobile;
        public byte time_flag;
        public byte extra1, extra2;
        public short spec1, spec2;
        public sbyte spec_enc_code, time_code;
        public short monster_time, personality;
        public short special_on_kill, facial_pic;

        public const int SIZE = 22;
    }


    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct item_record_type //SIZE 66
    {
        public short variety, item_level;                                                  //4
        public sbyte awkward, bonus, protection, charges, type, magic_use_type;            //6
        public byte graphic_num, ability, ability_strength, type_flag, is_special, a;      //6
        public short value;                                                                //2
        public byte weight, special_class;                                                 //2
        public location item_loc;                                                          //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 25)]
        public byte[] full_name;// = new char[25];                                         //25
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 15)]
        public byte[] name;// = new char[15];                                              //15
        public byte treas_class, item_properties, reserved1, reserved2;                    //4

        /* functions */
        //bool isIdent();		/* is identified ? */
        //bool isMagic();		/* is magic ? */
        //bool isContained();	/* is contained in sth ? */
        //bool isCursed();		/* is cursed ? */
        //bool isProperty();	/* is someones property? */
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct preset_item_type
    {
        public location item_loc;    //2
        public short item_code, ability;   //4
        public byte charges, always_there, property, contained;  //4
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct preset_field_type
    {
        public location field_loc;
        public short field_type;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct town_record_type
    {
        public short town_chop_time, town_chop_key;                                //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public wandering_type[] wandering;// = new wandering_type[4];              //4*4=16
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public location[] wandering_locs;// = new location[4];                     //8
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        public location[] special_locs;// = new location[50];                      //100
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        public byte[] spec_id;// = new byte[50];                                   //50
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 15)]
        public location[] sign_locs;// = new location[15];                         //30
        public short lighting;                                                     //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public location[] start_locs;// = new location[4];                         //8
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public location[] exit_locs;// = new location[4];                          //8
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public short[] exit_specs;// = new short[4];                               //8
        public RECT16 in_town_rect;                                                //8
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 64)]
        public preset_item_type[] preset_items;// = new preset_item_type[64];      //64*10 = 640
        public short max_num_monst;                                                //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        public preset_field_type[] preset_fields;// = new preset_field_type[50];   //50*4 = 200
        public short spec_on_entry, spec_on_entry_if_dead;                         //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public short[] timer_spec_times;// = new short[8];                         //16
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public short[] timer_specs;// = new short[8];                              //16
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 180)]
        public byte[] strlens;//= new byte[180];                                   //180
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 100)]
        public special_node_type[] specials;// = new special_node_type[100];       //100*22 = 2200
        public byte specials1, specials2, res1, res2;                              //4
        public short difficulty;                                                   //2

        public const int SIZE = 4 + 16 + 8 + 100 + 50 + 30 + 2 + 8 + 8 + 8 + 8 + 640 + 2 + 200 + 4 + 16 + 16 + 180 + 2200 + 4 + 2;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct big_tr_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 64*64)]
        public byte[] terrain;// = new byte[64, 64];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)]
        public RECT16[] room_rect;// = new RECT16[16];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 60)]
        public creature_start_type[] creatures;// = new creature_start_type[60];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8*64)]
        public byte[] lighting;// = new byte[8, 64]; 

        public const int SIZE = 64 * 64 + 16 * 8 + 60 * creature_start_type.SIZE + 8 * 64;
    } 

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct ave_tr_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 48*48)]
        public byte[] terrain;// = new byte[48, 48];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)]
        public RECT16[] room_rect;// = new RECT16[16];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 40)]
        public creature_start_type[] creatures;// = new creature_start_type[40];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6*48)]
        public byte[] lighting;// = new byte[6, 48];

        public const int SIZE = 48 * 48 + 16 * 8 + 40 * creature_start_type.SIZE + 6 * 48;

    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct tiny_tr_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 32*32)]
        public byte[] terrain;// = new byte[32, 32];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 16)]
        public RECT16[] room_rect;// = new RECT16[16];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        public creature_start_type[] creatures;// = new creature_start_type[30];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4*32)]
        public byte[] lighting;// = new byte[4, 32];

        public const int SIZE = 32 * 32 + 16 * 8 + 30 * creature_start_type.SIZE + 4 * 32;
    } 

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct scen_item_data_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 400)]
        public item_record_type[] scen_items;// = new item_record_type[400];        //400 * 66 = 26400
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256*20)]
        public byte[] monst_names;// = new char[256, 20];                           //5120
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256*30)]
        public byte[] ter_names;// = new char[256, 30];                             //7680

        public const int SIZE = 26400 + 5120 + 7680;
    } 

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct item_storage_shortcut_type //SIZE 44
    {
        private short ter_type;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        private short[] item_num;// = new short[10];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        private short[] item_odds;// = new short[10];

        private short property;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct monster_record_type //SIZE: 108
    {
        public byte m_num, level;                                              //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 26)]
        public byte[] m_name;// = new byte[26];                                //26   THIS IS NOT ACTUALLY USED
        public short health, m_health, mp, max_mp;                             //8
        public byte armor, skill;                                              //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public short[] a;// = new short[3];                                    //6
        public byte a1_type, a23_type, m_type, speed, ap, mu, cl, breath, breath_type, treasure, spec_skill, poison; //12
        public short morale, m_morale;                                         //4
        public short corpse_item, corpse_item_chance;                          //4                    
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 15)]
        public short[] status;// = new short[15];                              //30
        public byte direction, immunities, x_width, y_width, radiate_1, radiate_2; //6
        public byte default_attitude, summon_type, default_facial_pic, res1, res2, res3; //6
        public short picture_num;                                              //2
    } 

    /* CREATURE_DATA_TYPE */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct creature_data_type
    {
        /* variables */
        //public:
        private short active, attitude;
        private byte number;
        private location m_loc;
        private monster_record_type m_d;
        private byte mobile; //boolean
        private short summoned;
        private creature_start_type monst_start;

        /* functions */
        //private:
        //void adjustMagic(short* how_much);
        ////public:
        //void poison(short how_much);
        //void acid(short how_much);
        //void slow(short how_much);
        //void curse(short how_much);
        //void web(short how_much);
        //void scare(short how_much);
        //void disease(short how_much);
        //void dumbfound(short how_much);
        //void charm(short penalty, short which_status, short amount);
        //void record();
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct boat_record_type //SIZE: 10
    {
        public location boat_loc, boat_loc_in_sec, boat_sector; //6
        public short which_town;//2
        public byte exists, property;                        //2
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct scen_header_type //SIZE:17
    {
        public byte flag1, flag2, flag3, flag4;   //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        private byte[] ver;// = new byte[3];   //3

        private byte min_run_ver;              //1     
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        private byte[] prog_make_ver;// = new byte[3];   //3

        private byte num_towns;                          //1
        private byte out_width, out_height, difficulty, intro_pic, default_ground;   //5
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct scenario_data_type //SIZE: 41940
    {
        public byte flag1, flag2, flag3, flag4;                                 //4
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public byte[] ver;// = new byte[3];                                            //3
        public byte min_run_ver;                                                       //1
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public byte[] prog_make_ver;// = new byte[3];                                  //3
        public byte num_towns;                                                  //1
        public byte out_width, out_height, difficulty, intro_pic, default_ground;      //5
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200)]
        public byte[] town_size;// = new byte[200];                                    //200
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200)]
        public byte[] town_hidden;// = new byte[200];                                  //200
        public byte a;                                                                 //1
        public short flag_a;                                                           //2
        public short intro_mess_pic, intro_mess_len;                                   //2
        public location where_start, out_sec_start, out_start;                         //6
        public short which_town_start;                                                 //2
        public short flag_b;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200 * 5)]
        public short[] town_data_size;// = new short[200, 5];                         //2000
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        public short[] town_to_add_to;// = new short[10];                              //20
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10 * 2)]
        public short[] flag_to_add_to_town;// = new short[10, 2];                     //40
        public short flag_c;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 100 * 2)]
        public short[] out_data_size;// = new short[100, 2];                          //400
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public RECT16[] store_item_rects;// = new RECT16[3];                           //24
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public short[] store_item_towns;// = new short[3];                             //6
        public short flag_e;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        public short[] special_items;// = new short[50];                               //100
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        public short[] special_item_special;// = new short[50];                        //100
        public short rating, uses_custom_graphics;                                     //4
        public short flag_f;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]  
        public monster_record_type[] scen_monsters;// = new monster_record_type[256];  //256 * 108 = 27648
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        public boat_record_type[] scen_boats;// = new boat_record_type[30];            //30 * 10 = 300
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        public boat_record_type[] scen_horses;// = new horse_record_type[30];         //30 * 10 = 300
        public short flag_g;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        public terrain_type_type[] ter_types;// = new terrain_type_type[256];          //256 * 16 = 4096
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        public short[] scenario_timer_times;// = new short[20];                        //40
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        public short[] scenario_timer_specs;// = new short[20];                        //40
        public short flag_h;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        public special_node_type[] scen_specials;// = new special_node_type[256];      //256 * 22 = 5632

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        public item_storage_shortcut_type[] storage_shortcuts;// = new item_storage_shortcut_type[10]; //10 * 44 = 440
        public short flag_d;                                                           //2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 300)]
        public byte[] scen_str_len;// = new byte[300];                                 //300
        public short flag_i;                                                           //2
        public location last_out_edited;                                               //2
        public short last_town_edited;                                                 //2

        public const int SIZE = 41942;
        public int CheckFlags()
        {
            if (flag1 == 10 && flag2 == 20 && flag3 == 30 && flag4 == 40)
                return 1;
            if (flag1 == 20 && flag2 == 40 && flag3 == 60 && flag4 == 80)
                return 0;
            return -1;
        }

    } 

    // for game
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct talk_save_type
    {
        private short personality;
        private short town_num;
        private short str1, str2;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct creature_list_type
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 60)]
        private creature_data_type[] dudes;// = new creature_data_type[60];

        private short which_town;
        private short friendly;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct current_town_type
    {
        private short town_num, difficulty;
        private town_record_type town;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 64*64)]
        private sbyte[,] explored;// = new sbyte[64, 64];

        private byte hostile; //Boolean
        private creature_list_type monst;
        private byte in_boat; //Boolean
        private location p_loc;

        /* functions */
        //short placeMonster(byte which, location where);
        //short countMonsters();
        //void activateMonsters(short code);
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct outdoor_creature_type
    {
        private byte exists; //Boolean
        private short direction;
        private out_wandering_type what_monst;
        private location which_sector, m_loc;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct party_record_type
    {
        private int age;
        private short gold, food;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 310*10)]
        private byte[,] stuff_done;// = new byte[310, 10];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200*8)]
        private byte[,] item_taken;// = new byte[200, 8];

        private short light_level;
        private location outdoor_corner, i_w_c, p_loc, loc_in_sec;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        private boat_record_type[] boats;// = new boat_record_type[30];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        private boat_record_type[] horses;// = new horse_record_type[30];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        private creature_list_type[] creature_save;// = new creature_list_type[4];

        private short in_boat, in_horse;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
        private outdoor_creature_type[] out_c;// = new outdoor_creature_type[10];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 5*10)]
        private item_record_type[,] magic_store_items;// = new item_record_type[5, 10];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        private short[] imprisoned_monst;// = new short[4];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        private sbyte[] m_seen;// = new sbyte[256];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        private byte[] journal_str;// = new char[50];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        private short[] journal_day;// = new short[50];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 140*2)]
        private short[,] special_notes_str;// = new short[140, 2];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 120)]
        private talk_save_type[] talk_save;// = new talk_save_type[120];

        private short direction, at_which_save_slot;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        private sbyte[] alchemy;// = new char[20];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200)]
        private byte[] can_find_town;// = new Boolean[200];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 100)]
        private short[] key_times;// = new short[100];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        private short[] party_event_timers;// = new short[30];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        private short[] global_or_town;// = new short[30];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        private short[] node_to_call;// = new short[30];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 50)]
        private sbyte[] spec_items;// = new char[50];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 120)]
        private sbyte[] help_received;// = new char[120];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 200)]
        private short[] m_killed;// = new short[200];

        private int total_m_killed, total_dam_done, total_xp_gained, total_dam_taken;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        private byte[] scen_name;// = new char[256];

        /* functions */
        //bool isFlying() { return stuff_done[305, 1] != 0; }
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct stored_town_maps_type { [MarshalAs(UnmanagedType.ByValArray, SizeConst = 100*8*64)]
        private byte[, ,] town_maps;}// = new char[100, 8, 64]; }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct piles_of_stuff_dumping_type { public string[] town_strs;}//[MarshalAs(UnmanagedType.ByValArray, SizeConst = 180 * 256)] byte[,] town_strs;}// = new char[180, 256]; }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct piles_of_stuff_dumping_type2
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 25*3*80)]
        private byte[, ,] scen_header_strs;// = new char[25, 3, 80];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 25*256)]
        private byte[,] scen_names;// = new char[25, 256];

        private scen_item_data_type scen_item_list;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct piles_of_stuff_dumping_type3 { public string[] talk_strs;}// [MarshalAs(UnmanagedType.ByValArray, SizeConst = 170 * 256)] byte[,] talk_strs;}// = new char[170, 256]; }
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct outdoor_strs_type { [MarshalAs(UnmanagedType.ByValArray, SizeConst = 9*256)]
        private byte[,] out_strs;}// = new char[9, 256]; }
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct piles_of_stuff_dumping_type4 { public string[] outdoor_text;}//[MarshalAs(UnmanagedType.ByValArray, SizeConst = 2*2)]outdoor_strs_type[,] outdoor_text;}// = new outdoor_strs_type[2, 2]; }
    //[StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct piles_of_stuff_dumping_type5 { public string[] scen_strs;}//[MarshalAs(UnmanagedType.ByValArray, SizeConst = 160*256)]byte[,] scen_strs;}// = new char[160, 256]; }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct pc_record_type
    {
        private short main_status;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 20)]
        private byte[] name;// = new char[20];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 30)]
        private short[] skills;// = new short[30];

        private short max_health, cur_health, max_sp, cur_sp, experience, skill_pts, level;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 15)]
        private short[] status;// = new short[15];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 24)]
        private item_record_type[] items;// = new item_record_type[24];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 24)]
        private byte[] equip;// = new Boolean[24];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 62)]
        private byte[] priest_spells;// = new Boolean[62];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 62)]
        private byte[] mage_spells;// = new Boolean[62];

        private short which_graphic, weap_poisoned;
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 15)]
        private byte[] advan;// = new Boolean[15];
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 15)]
        private byte[] traits;// = new Boolean[15];

        private short race, exp_adj, direction;

        /* functions */
        //bool isAlive() { return (main_status == CN.MAIN_STATUS_ALIVE); }
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal class pc_array
    {
        //private:
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        private pc_record_type[] pc;// = new pc_record_type[6];

        //public:
        //    pc_record_type & operator[](int num) { return pc[num]; }
        //pc_record_type this[int v] { get { return pc[v]; } set { pc[v] = value; } }


        /* remember - all this functions refer to all PCs */
        //void affect(short type, short how_much);
        //void cure(short how_much);							/* cure all */
        //void damage(short how_much, short damage_type);		/* damage all */
        //void heal(short how_much);							/* heal all */
        //void kill(short mode);								/* kill all */
        //void giveSpell(short which);
        //void poison(short how_much);						/* poison all */

        //short getMageLore();								/* count total mage lore */
    };

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct setup_save_type { [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4*64*64)]
        private byte[, ,] setup;}// = new byte[4, 64, 64]; }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct town_item_list { [MarshalAs(UnmanagedType.ByValArray, SizeConst = 115)]
        private item_record_type[] items;}// = new item_record_type[CN.NUM_TOWN_ITEMS]; }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct flag_type {
        private short i; }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct effect_pat_type { [MarshalAs(UnmanagedType.ByValArray, SizeConst = 115)]
        private item_record_type[] items;}// = new item_record_type[CN.NUM_TOWN_ITEMS]; } //stored_items_list_type;

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct stored_outdoor_maps_type { [MarshalAs(UnmanagedType.ByValArray, SizeConst = 100*6*48)]
        private byte[, ,] outdoor_maps;}// = new char[100, 6, 48]; }  

}