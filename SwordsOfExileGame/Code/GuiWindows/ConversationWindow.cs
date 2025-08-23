using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class ConversationWindow : GuiWindow
{
    private NPC NPC;
    private Personality P;
    private RichTextBox talkBox;
    private List<TalkingNode> nodeList;
    private Button[] buttons = new Button[8];
    private bool forceEnd; //When true, all options that continue the conversation vanish.

    private List<Tuple<string, bool>> goBackList = new();

    public ConversationWindow(NPC npc) :
        base(0, 0, 400, 445, true, true, true, true, true)
    {
        NPC = npc;
        P = NPC.Personality;

        AddLabel(P.Name, 60, 20, -1, -1, false);

        if (NPC.Start.FacialPic >= 0)
        {
            XnaRect sr;
            var sheet = (NPC.Start.FacialPic & 0x7C00) >> 10;
            var no = (NPC.Start.FacialPic & 0x03FF);

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


        var b = AddButton(pressDone, "Done", 340, 389);
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
                var text = Script.TalkingText;
                setUpText(text);
            }
            return false;
        }
        return base.Handle();
    }

    private void pressText(int index)
    {
        runNode(nodeList[index]);
    }

    private void pressLook(Control button) { setUpText(P.Look, false); }
    private void pressName(Control button) { setUpText(P.NameResponse); }
    private void pressJob(Control button) { setUpText(P.JobResponse); }

    private void pressGoBack(Control button)
    {
        if (goBackList.Count > 1)
        {
            goBackList.RemoveAt(goBackList.Count - 1);
            var store = goBackList[goBackList.Count - 1];
            goBackList.RemoveAt(goBackList.Count - 1);
            setUpText(store.Item1, store.Item2);
        }
    }

    private void pressBuy(Control button)
    {
        var ss = new string[] { "purc", "sale", "heal", "iden", "trai" };

        foreach (var s in ss)
        {
            var node = P.FindTalkingNode(s);
            if (node != null && runNode(node))
            {
                return;
            }
        }
        setUpText(P.BlankResponse);
    }

    private void pressSell(Control button)
    {
        var node = P.FindTalkingNode("sell");
        if (node == null || !runNode(node))
            setUpText(P.BlankResponse);
    }

    private void pressRecord(Control button) 
    {
        Game.AddMessage("Dialogue saved to Notes.");
        Scenario.MakeNote(P.Name + " - Day " + Party.Day, talkBox.GetRawText());
        buttons[7].Enabled = false;
    }

    private void pressAsk(Control button) { new InputTextWindow(returnedAskAbout, "Type what to ask about:", "", false); }

    private void pressDone(Control button) {
        KillMe = true; 
    }

    private void returnedAskAbout(string text)
    {
        if (text != null)
        {
            var node = P.FindTalkingNode(text);
            if (node == null || !runNode(node))
                setUpText(P.BlankResponse);
        }
    }


    private bool runNode(TalkingNode node)
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
                    
                var shop = Shop.List[node.LinkedID];
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
                var n = 0;
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
        }
        return true;
    }

    private string joinTexts(string[] texts)
    {
        var sb = new StringBuilder();
        var first = true;

        foreach (var s in texts)
        {
            if (!first)
                sb.Append("@n");
            sb.Append(s);
            first = false;
        }
        return sb.ToString();
    }

    private void setUpText(string Text, bool do_word_links = true)
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
            foreach (var b in buttons) b.Visible = false;
        }

        if (forceEnd || !do_word_links)
        {
            talkBox.FormatText(Text);
            return;
        }

        nodeList = new List<TalkingNode>();
        var sb = new StringBuilder();
        var foundword = false;
        var startpos = 0;
        //Go through each word in the text, checking it with dialogue nodes for this personality.
        for (var n = 0; n < Text.Length; n++)
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
                var word = sb.ToString();

                var node = P.FindTalkingNode(word);

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