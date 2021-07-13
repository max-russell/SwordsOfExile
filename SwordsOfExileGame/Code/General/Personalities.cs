using System;
using System.IO;
using System.Collections.Generic;
using System.Text;

namespace SwordsOfExileGame
{
    public class Personality : IListEntity
    {
        public static ExileList<Personality> List = new ExileList<Personality>();

        public string ID { get { return id; } set { id = value; } }
        string id;
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
                if ((node.link1 != "xxxx" && word.Substring(0, 4).ToUpper() == node.link1.ToUpper())
                         || (node.link2 != "xxxx" && word.Substring(0, 4).ToUpper() == node.link2.ToUpper()))
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
        public eTalkNodeType Type;
        public string link1, link2;
        public string Text;
        public string LinkedID; //Normally either ID of a script function or Shop to run
        public eTalkNodeCondition Condition;
        public string ConditionVar;
        public int ConditionValue;
        public bool SetsVar, ForceEnd;

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
    }
}