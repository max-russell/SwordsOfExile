using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
//using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame
{
    class ConversationWindow : GuiWindow
    {
        NPC NPC;
        Personality P;
        RichTextBox talkBox;
        List<TalkingNode> nodeList;
        Button[] buttons = new Button[8];
        bool forceEnd; //When true, all options that continue the conversation vanish.

        //Texture2D customFace;

        List<Tuple<string, bool>> goBackList = new List<Tuple<string, bool>>();

        public ConversationWindow(NPC npc) :
            base(0, 0, 400, 445, true, true, true, true, true)
        {
            NPC = npc;
            P = NPC.Personality;

            AddLabel(P.Name, 60, 20, -1, -1, false);

            if (NPC.Start.FacialPic >= 0)
            {
                XnaRect sr;
                int sheet = (NPC.Start.FacialPic & 0x7C00) >> 10;
                int no = (NPC.Start.FacialPic & 0x03FF);

                if (Gfx.FacesGfx[sheet] != null)
                {
                    sr = new XnaRect((NPC.Start.FacialPic % Gfx.FacesGfxSlotsAcross[sheet]) * Gfx.FACEGFXWIDTH, (NPC.Start.FacialPic / Gfx.FacesGfxSlotsAcross[sheet]) * Gfx.FACEGFXHEIGHT, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT);
                    AddPictureBox(Gfx.FacesGfx[sheet], sr, new XnaRect(20, 20, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT));
                }
            }

            talkBox = AddBlankRichTextBox(pressText, 20, 62, 350, 280);
            
            LineUpControls(20, 318, 5,
                buttons[0] = AddButton(pressLook, "(L)ook", 0, 352),
                buttons[1] = AddButton(pressName, "(N)ame", 0, 352),
                buttons[2] = AddButton(pressJob, "(J)ob", 0, 352),
                buttons[3] = AddButton(pressGoBack, "(G)o Back", 0, 352));

            LineUpControls(20, buttons[0].Y + buttons[0].Height + 10, 5,
                buttons[4] = AddButton(pressBuy, "(B)uy", 0, 352),
                buttons[5] = AddButton(pressSell, "(S)ell", 0, 352),
                buttons[6] = AddButton(pressAsk, "(A)sk About", 0, 352),
                buttons[7] = AddButton(pressRecord, "(R)ecord", 0, 352));

            buttons[0].KeyShortcut = Keys.L;
            buttons[1].KeyShortcut = Keys.N;
            buttons[2].KeyShortcut = Keys.J;
            buttons[3].KeyShortcut = Keys.G;
            buttons[4].KeyShortcut = Keys.B;
            buttons[5].KeyShortcut = Keys.S;
            buttons[6].KeyShortcut = Keys.A;
            buttons[7].KeyShortcut = Keys.R;


            Button b = AddButton(pressDone, "Done", 340, 389);
            b.Position(-10, -10, 1, 1);
            OKKeyControl = b;
            CancelKeyControl = b;

            setUpText(P.Look, false);
            Position(-2, -2);
        }

        public override bool Handle()
        {
            if (Script.IsRunning)
            {
                if (Script.RunNext())
                {
                    string text = Script.TalkingText;
                    setUpText(text);
                }
                return false;
            }
            return base.Handle();
        }

        void pressText(int index)
        {
            runNode(nodeList[index]);
        }

        void pressLook(Control button) { setUpText(P.Look, false); }
        void pressName(Control button) { setUpText(P.NameResponse); }
        void pressJob(Control button) { setUpText(P.JobResponse); }
        void pressGoBack(Control button)
        {
            if (goBackList.Count > 1)
            {
                goBackList.RemoveAt(goBackList.Count - 1);
                var store = goBackList[goBackList.Count - 1];
                goBackList.RemoveAt(goBackList.Count - 1);
                setUpText(store.Item1, store.Item2);
            }
        }
        void pressBuy(Control button)
        {
            string[] ss = new string[] { "purc", "sale", "heal", "iden", "trai" };

            foreach (string s in ss)
            {
                TalkingNode node = P.FindTalkingNode(s);
                if (node != null && runNode(node))
                {
                    return;
                }
            }
            setUpText(P.BlankResponse);
        }
        void pressSell(Control button)
        {
            TalkingNode node = P.FindTalkingNode("sell");
            if (node == null || !runNode(node))
                setUpText(P.BlankResponse);
        }

        void pressRecord(Control button) 
        {
            Game.AddMessage("Dialogue saved to Notes.");
            Scenario.MakeNote(P.Name + " - Day " + Party.Day, talkBox.GetRawText());
            buttons[7].Enabled = false;
        }
        void pressAsk(Control button) { new InputTextWindow(returnedAskAbout, "Type what to ask about:", "", false); }

        void pressDone(Control button) {
            KillMe = true; 
        }

        void returnedAskAbout(string text)
        {
            if (text != null)
            {
                TalkingNode node = P.FindTalkingNode(text);
                if (node == null || !runNode(node))
                    setUpText(P.BlankResponse);
            }
        }


        bool runNode(TalkingNode node)
        {
            if (!node.CheckCondition()) return false;

            if (node.SetsVar) Script.StuffDone[node.ConditionVar] = node.ConditionValue;

            if (node.ForceEnd) forceEnd = true;

            switch (node.Type)
            {
                case eTalkNodeType.REGULAR:
                    setUpText(node.Text, !forceEnd);
                    break;
                case eTalkNodeType.RUN_FUNCTION:
                    Script.TalkingText = node.Text;
                    Script.New_Talking(node.LinkedID, NPC);
                    break;
                case eTalkNodeType.RUN_SHOP:
                    
                    Shop shop = Shop.List[node.LinkedID];
                    if (shop == null)
                    {
                        setUpText("Shop ID '" + node.LinkedID + "' not found.", false);

                    }
                    else
                    {
                        Visible = false;
                        switch (shop.ShopType)
                        {
                            case eShop.ITEM: new ItemShopWindow(shop, this); break;
                            case eShop.MAGIC: new MagicShopWindow(shop, this); break;
                            case eShop.ALCHEMY: new AlchemyShopWindow(shop, this); break;
                        }
                    }
                    break;
                case eTalkNodeType.RUN_HEALER:
                    Visible = false;
                    int n = 0;
                    int.TryParse(node.LinkedID, out n);
                    n = Maths.MinMax(0, 6, n);
                    new HealerShopWindow(this, n);
                    break;
                case eTalkNodeType.RUN_IDENTIFY:
                    Visible = false;
                    n = 0;
                    int.TryParse(node.LinkedID, out n);
                    new IdentifyWindow(this, node.Text, n);
                    break;
                case eTalkNodeType.RUN_TRAINING:
                    Visible = false;
                    new TrainerWindow(this);
                    break;
                case eTalkNodeType.RUN_ENCHANTING:
                    Visible = false;
                    n = 0;
                    int.TryParse(node.LinkedID, out n);
                    n = Maths.MinMax(0, 6, n);
                    new EnchantingWindow(this, node.Text, (eEnchantShop)n);
                    break;

                //case eTalkNodeTypeOLD.REGULAR:
                //    string[] texts = new string[] { node.Text1, node.Text2 };
                //    setUpText(joinTexts(new string[] { node.Text1, node.Text2 })); break;
                //case eTalkNodeTypeOLD.DEP_ON_SDF:
                //    if ((int)Script.StuffDone[node.Var] <= node.DataC)
                //        setUpText(node.Text1);
                //    else
                //        setUpText(node.Text2);
                //    break;
                //case eTalkNodeTypeOLD.SET_SDF:
                //    setUpText(joinTexts(new string[] { node.Text1, node.Text2 }));
                //    Script.StuffDone[node.Var] = 1;
                //    break;
                //case eTalkNodeTypeOLD.INN:
                //    if (Party.Gold < node.DataA)
                //        setUpText(node.Text2);
                //    else
                //    {
                //        //TODO: Buying a room at the inn.
                //        Party.Gold -= node.DataA;
                //        if (Town.InBounds(new Location(node.DataC, node.DataD))) Party.Pos = new Location(node.DataC, node.DataD);
                //        Town.UpdateVisible();
                //        Party.HealAll(30 * node.DataB,true);
                //        Party.RestoreSP(25 * node.DataB);
                //        forceEnd = true;
                //        setUpText(node.Text1);
                //        Gfx.CentreView(Party.Pos, false);
                //    }
                //    break;
                //case eTalkNodeTypeOLD.DEP_ON_TIME:
                //    if (Party.Day > node.DataA)
                //        setUpText(node.Text2);
                //    else
                //        setUpText(node.Text1);
                //    break;
                //case eTalkNodeTypeOLD.DEP_ON_TIME_AND_EVENT:
                //    break; //TODO: Dialogue node involving events
                //case eTalkNodeTypeOLD.DEP_ON_TOWN:
                //    if (node.DataA >= 0 && node.DataA < TownMap.List.Count && Town == TownMap.List[node.DataA])
                //        setUpText(node.Text1);
                //    else
                //        setUpText(node.Text2);
                //    break;

                //case eTalkNodeTypeOLD.SHOP:
                //    Visible = false;
                //    switch (node.Shop.ShopType)
                //    {
                //        case eShop.ITEM: new ItemShopWindow(node.Shop, this); break;
                //        case eShop.MAGIC: new MagicShopWindow(node.Shop, this); break;
                //        case eShop.ALCHEMY: new AlchemyShopWindow(node.Shop, this); break;
                //    }
                //    break;

                //case eTalkNodeTypeOLD.TRAINING:

                //    Visible = false;
                //    new TrainerWindow(this);
                //    break;

                //case eTalkNodeTypeOLD.BUY_HEALING:
                //    Visible = false;
                //    new HealerShopWindow(this, node.DataA);
                //    break;
                //case eTalkNodeTypeOLD.IDENTIFY:
                //    Visible = false;
                //    new IdentifyWindow(this, node.Text1, node.DataA);
                //    break;

                //case eTalkNodeTypeOLD.ENCHANT:
                //    Visible = false;
                //    new EnchantingWindow(this, node.Text1, (eEnchantShop)node.DataA);
                //    break;

                //case eTalkNodeTypeOLD.BUY_INFO:
                //    if (Party.Gold < node.DataA)
                //        setUpText(node.Text2);
                //    else
                //    {
                //        setUpText(node.Text1);
                //        Party.Gold -= node.DataA;
                //    }
                //    break;
                //case eTalkNodeTypeOLD.BUY_SDF:
                //    if (Party.Gold < node.DataA)
                //        setUpText(node.Text2);
                //    else
                //    {
                //        //Party.SetStuffDone(node.DataB, node.DataC, (byte)node.DataD);
                //        Script.StuffDone[node.Var] = node.DataD;
                //        setUpText(node.Text1);
                //        Party.Gold -= node.DataA;
                //    }
                //    break;
                //case eTalkNodeTypeOLD.BUY_SHIP:
                //case eTalkNodeTypeOLD.BUY_HORSE:
                //    if (Party.Gold < node.DataA)
                //        setUpText(node.Text2);
                //    else
                //    {
                //        //Find the next boat to sell.
                //        Vehicle foundv = null;
                //        for (int a = node.DataB; a < node.DataA + node.DataC; a++)
                //        {
                //            if (a >= 0 && a < Vehicle.List.Count && !Vehicle.List[a].PartyOwns)
                //            {
                //                foundv = Vehicle.List[a];
                //                break;
                //            }

                //        }
                //        if (foundv == null)
                //            setUpText("There are none available to buy.");
                //        else
                //        {
                //            foundv.PartyOwns = true;
                //            setUpText(node.Text1);
                //            Party.Gold -= node.DataA;
                //        }

                //    }

                //    break;
                //case eTalkNodeTypeOLD.BUY_SPEC_ITEM:
                //    //TODO: Buy special item
                //    if (Party.Gold < node.DataB)
                //        setUpText(node.Text2);
                //    else
                //    {
                //        setUpText(node.Text1);

                //    }
                //    break;
                //case eTalkNodeTypeOLD.BUY_TOWN_LOC:
                //    if (Party.Gold < node.DataA)
                //        setUpText(node.Text2);
                //    else
                //    {
                //        if (node.DataB >= 0 && node.DataB < TownMap.List.Count) TownMap.List[node.DataB].Hidden = false;
                //        setUpText(node.Text1);
                //    }
                //    break;
                //case eTalkNodeTypeOLD.END_FORCE:
                //    forceEnd = true;
                //    setUpText(joinTexts(new string[] { node.Text1, node.Text2 }));
                //    break;
                //case eTalkNodeTypeOLD.END_FIGHT:
                //    forceEnd = true;
                //    setUpText(joinTexts(new string[] { node.Text1, node.Text2 }));
                //    NPC.Attitude = eAttitude.HOSTILE_A;
                //    NPC.Mobile = true;
                //    break;
                //case eTalkNodeTypeOLD.END_ALARM:
                //    forceEnd = true;
                //    setUpText(joinTexts(new string[] { node.Text1, node.Text2 }));
                //    Town.MakeTownHostile();
                //    break;
                //case eTalkNodeTypeOLD.END_DIE:
                //    Town.NPCList.Remove(NPC);
                //    if (NPC.Start.LifeVariable != "")
                //        Script.StuffDone[NPC.Start.LifeVariable] = 1;
                //    forceEnd = true;
                //    setUpText(joinTexts(new string[] { node.Text1, node.Text2 }));
                //    break;
                //case eTalkNodeTypeOLD.CALL_TOWN_SPEC:
                //case eTalkNodeTypeOLD.CALL_SCEN_SPEC:
                //    //Set up the default text for if the script that's about to be run doesn't change the response.
                //    texts = new string[] { node.Text1, node.Text2 };
                //    Script.TalkingText = joinTexts(new string[] { node.Text1, node.Text2 });
                //    Script.New_General(node.Func, eCallOrigin.TALKING);
                //    break;
            }
            return true;
        }

        string joinTexts(string[] texts)
        {
            StringBuilder sb = new StringBuilder();
            bool first = true;

            foreach (string s in texts)
            {
                if (!first)
                    sb.Append("@n");
                sb.Append(s);
                first = false;
            }
            return sb.ToString();
        }

        void setUpText(string Text, bool do_word_links = true)
        {
            buttons[7].Enabled = true;

            goBackList.Add(new Tuple<string, bool>(Text, do_word_links));
            if (goBackList.Count == 10)
                goBackList.RemoveAt(0);

            //Put new lines in properly.
            Text = Text.Replace("|", "@n");

            if (forceEnd)
            {
                //It has been decreed this conversation must stop. Remove all buttons except for the 'Done' and 'Record' ones.
                foreach (Button b in buttons) b.Visible = false;
            }

            if (forceEnd || !do_word_links)
            {
                talkBox.FormatText(Text);
                return;
            }

            nodeList = new List<TalkingNode>();
            StringBuilder sb = new StringBuilder();
            bool foundword = false;
            int startpos = 0;
            //Go through each word in the text, checking it with dialogue nodes for this personality.
            for (int n = 0; n < Text.Length; n++)
            {
                if (char.IsLetterOrDigit(Text[n]))
                {
                    sb.Append(Text[n]);
                    if (!foundword) startpos = n;
                    foundword = true;
                }
                else if (foundword && !char.IsLetterOrDigit(Text[n]) || n == Text.Length - 1)
                {
                    if (n == Text.Length - 1)
                        sb.Append(Text[n++]);

                    //sb should now be our word
                    String word = sb.ToString();

                    TalkingNode node = P.FindTalkingNode(word);

                    if (node != null)
                    {
                        Text = Text.Insert(n, "@e");
                        Text = Text.Insert(startpos, "@l");
                        nodeList.Add(node);
                        n += 3;
                    }
                    foundword = false;
                    sb.Clear();
                }
            }
            talkBox.FormatText(Text);
        }

    }

}