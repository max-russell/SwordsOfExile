using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
////using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace SwordsOfExileGame
{
    public class Personality : IListEntity
    {
        public static ExileList<Personality> List = new ExileList<Personality>();

        public string ID { get { return id; } set { id = value; } }
        string id;
        //public int Num;
        //public TownMap Town;
        public string Name, Look, NameResponse, JobResponse, BlankResponse;
        public Personality Parent; //A personality inherits all its talk nodes from its parent
        List<TalkingNode> TalkingNodeList = new List<TalkingNode>();

        public Personality() { }
        public void Load(BinaryReader In)
        {
            id = In.ReadString();
            In.ReadString(); //Folder: disregard
            List.TryGetValue(In.ReadString(), out Parent);
            Name = In.ReadString();
            Look = In.ReadString();
            NameResponse = In.ReadString();
            JobResponse = In.ReadString();
            BlankResponse = In.ReadString();

            int n = In.ReadInt16();
            for (int x = 0; x < n; x++) TalkingNodeList.Add(new TalkingNode(In));

            List.Add(this);


        }

        public TalkingNode FindTalkingNode(string word)
        {
            if (word.Length < 4) return null;

            foreach (TalkingNode node in TalkingNodeList)
            {
                if (/*(node.personality == p || node.personality == Personality.Everyone) &&*/
                    ((node.link1 != "xxxx" && word.Substring(0, 4).ToUpper() == node.link1.ToUpper())
                         || (node.link2 != "xxxx" && word.Substring(0, 4).ToUpper() == node.link2.ToUpper())))
                {
                    if (node.CheckCondition()) return node;
                }
            }

            //Failed to find node for this personality, let's check its parent. This bit is recursive
            if (Parent != null)
                return Parent.FindTalkingNode(word);

            return null;
        }

    }

    public class TalkingNode
    {

        ////public Personality personality;
        //public eTalkNodeTypeOLD Type;
        //public string link1, link2;
        //public string Event = null;
        //short[] extras = new short[4];//[4];
        //public string Text1, Text2;
        //public Shop Shop;
        public eTalkNodeType Type;
        public string link1, link2;
        public string Text;
        public string LinkedID; //Normally either ID of a script function or Shop to run
        public eTalkNodeCondition Condition;
        public string ConditionVar; //StuffDone variable condition tests
        public int ConditionValue;
        public bool SetsVar, ForceEnd;

        //public List<string> ShopList = null;

        //public String Var;
        //public string Func;

        public TalkingNode(BinaryReader In)
        {
            Type = (eTalkNodeType)In.ReadByte();
            link1 = Encoding.UTF8.GetString(In.ReadBytes(4));
            link2 = Encoding.UTF8.GetString(In.ReadBytes(4));
            Text = In.ReadString();

            if (Type == eTalkNodeType.RUN_HEALER || Type == eTalkNodeType.RUN_ENCHANTING)
                LinkedID = Convert.ToString(In.ReadByte());
            else if (Type == eTalkNodeType.RUN_IDENTIFY)
                LinkedID = Convert.ToString(In.ReadInt32());
            else
                LinkedID = In.ReadString();
            Condition = (eTalkNodeCondition)In.ReadByte();
            ConditionVar = In.ReadString();
            ConditionValue = In.ReadInt32();
            SetsVar = In.ReadBoolean();
            ForceEnd = In.ReadBoolean();
        }

        public bool CheckCondition()
        {
            switch(Condition)
            {
                case eTalkNodeCondition.NONE:
                    return true;
                case eTalkNodeCondition.NEVER:
                    return false;
                default:
                    int a = 0;
                    if (GlobalVariables.Contains(ConditionVar, typeof(int))) a = GlobalVariables.Get(ConditionVar);

                    switch (Condition)
                    {
                        case eTalkNodeCondition.EQUAL_TO:
                            return a == ConditionValue;
                        case eTalkNodeCondition.GREATER_THAN:
                            return a > ConditionValue;
                        case eTalkNodeCondition.GREATER_THAN_OR_EQUAL_TO:
                            return a >= ConditionValue;
                        case eTalkNodeCondition.LESS_THAN:
                            return a < ConditionValue;
                        case eTalkNodeCondition.LESS_THAN_OR_EQUAL_TO:
                            return a <= ConditionValue;
                        case eTalkNodeCondition.NOT_EQUAL_TO:
                            return a != ConditionValue;
                    }
                    return false;
            }
        }
            ////int p = In.ReadInt16();
            ////if (p == -1) personality = null;
            ////else if (p == -2) personality = Personality.Everyone;
            ////else
            ////    personality = Personality.List.ElementAt(p).Value; //In.ReadInt16();// BoE.ReadShort(In);

            //Type = (eTalkNodeTypeOLD)In.ReadInt16();

            //link1 = Encoding.UTF8.GetString(In.ReadBytes(4));
            //link2 = Encoding.UTF8.GetString(In.ReadBytes(4));

            //if (Type == eTalkNodeTypeOLD.SHOP)
            //{
            //    var dsfsdf = In.ReadString();
            //    if (!Shop.List.TryGetValue(dsfsdf/*In.ReadString()*/, out Shop)) throw new Exception("Item Shop ID not found.");
            //}
            //else
            //{
            //    //link1 = Encoding.UTF8.GetString(In.ReadBytes(4));
            //    //link2 = Encoding.UTF8.GetString(In.ReadBytes(4));
            //    extras[0] = In.ReadInt16();
            //    extras[1] = In.ReadInt16();

            //    if (Type == eTalkNodeTypeOLD.DEP_ON_TIME_AND_EVENT)
            //        Event = In.ReadString();
            //    //else
                    

            //    extras[2] = In.ReadInt16();
            //    extras[3] = In.ReadInt16();
            //    Text1 = In.ReadString();
            //    Text2 = In.ReadString();

            //    if (Type == eTalkNodeTypeOLD.DEP_ON_SDF || Type == eTalkNodeTypeOLD.SET_SDF || Type == eTalkNodeTypeOLD.BUY_SDF)
            //    {
            //        Var = In.ReadString();
            //        //p = In.ReadInt16();
            //        //if (p != -1) Var = GlobVar.List[p];
            //    }
            //    else if (Type == eTalkNodeTypeOLD.CALL_SCEN_SPEC || Type == eTalkNodeTypeOLD.CALL_TOWN_SPEC)
            //        Func = In.ReadString();
            //    else if (Type == eTalkNodeTypeOLD.DEP_ON_TOWN)
            //    {
            //        TownMap t;
            //        if (TownMap.List.TryGetValue(In.ReadString(), out t))
            //            extras[0] = (short)t.Num;
            //        else
            //            extras[0] = 0;
            //    }
            //    else if (Type == eTalkNodeTypeOLD.BUY_TOWN_LOC)
            //    {
            //        TownMap t;
            //        if (TownMap.List.TryGetValue(In.ReadString(), out t))
            //            extras[1] = (short)t.Num;
            //        else
            //            extras[1] = 0;
            //    }
            //    //else if (Type == eTalkNodeType.BUY_MAGE || Type == eTalkNodeType.BUY_PRIEST || Type == eTalkNodeType.BUY_ALCHEMY)
            //    //{
            //    //    ShopList = new List<string>();
            //    //    for (int n = 0; n < extras[2]; n++)
            //    //    {
            //    //        ShopList.Add(In.ReadString());
            //    //    }
            //    //}
            //}
        //}

        //public int DataA { get { return extras[0]; } }
        //public int DataB { get { return extras[1]; } }
        //public int DataC { get { return extras[2]; } }
        //public int DataD { get { return extras[3]; } }
    }
}