using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Xna.Framework.Input;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace SwordsOfExileGame;

internal class ConversationWindow : GuiWindow
{
    private readonly NPC _npc;
    private readonly Personality _personality;
    private readonly RichTextBox _talkBox;
    private List<TalkingNode> _nodeList;
    private readonly Button[] _buttons = new Button[8];
    private bool _forceEnd; //When true, all options that continue the conversation vanish.
    private readonly List<Tuple<string, bool>> _goBackList = new();

    public ConversationWindow(NPC npc) :
        base(0, 0, 400, 445, true, true, true, true, true)
    {
        _npc = npc;
        _personality = _npc.Personality;

        AddLabel(_personality.Name, 60, 20, -1, -1, false);

        if (_npc.Start.FacialPic >= 0)
        {
            var sheet = (_npc.Start.FacialPic & 0x7C00) >> 10;
            var no = (_npc.Start.FacialPic & 0x03FF);

            if (Gfx.FacesGfx[sheet] != null)
            {
                var sr = new XnaRect(
                    _npc.Start.FacialPic % Gfx.FacesGfxSlotsAcross[sheet] * Gfx.FACEGFXWIDTH, 
                    _npc.Start.FacialPic / Gfx.FacesGfxSlotsAcross[sheet] * Gfx.FACEGFXHEIGHT, 
                    Gfx.FACEGFXWIDTH, 
                    Gfx.FACEGFXHEIGHT);
                AddPictureBox(Gfx.FacesGfx[sheet], sr, new XnaRect(20, 20, Gfx.FACEGFXWIDTH, Gfx.FACEGFXHEIGHT));
            }
        }

        _talkBox = AddBlankRichTextBox(PressText, 20, 62, 350, 280);
        _talkBox.SetFonts(0);
            
        LineUpControls(20, 318, 5,
            _buttons[0] = AddButton(pressLook, "(L)ook", 0, 352),
            _buttons[1] = AddButton(pressName, "(N)ame", 0, 352),
            _buttons[2] = AddButton(pressJob, "(J)ob", 0, 352),
            _buttons[3] = AddButton(pressGoBack, "(G)o Back", 0, 352));

        LineUpControls(20, _buttons[0].Y + _buttons[0].Height + 10, 5,
            _buttons[4] = AddButton(PressBuy, "(B)uy", 0, 352),
            _buttons[5] = AddButton(PressSell, "(S)ell", 0, 352),
            _buttons[6] = AddButton(PressAsk, "(A)sk About", 0, 352),
            _buttons[7] = AddButton(PressRecord, "(R)ecord", 0, 352));

        _buttons[0].KeyShortcut = Keys.L;
        _buttons[1].KeyShortcut = Keys.N;
        _buttons[2].KeyShortcut = Keys.J;
        _buttons[3].KeyShortcut = Keys.G;
        _buttons[4].KeyShortcut = Keys.B;
        _buttons[5].KeyShortcut = Keys.S;
        _buttons[6].KeyShortcut = Keys.A;
        _buttons[7].KeyShortcut = Keys.R;


        var b = AddButton(PressDone, "Done", 340, 389);
        b.Position(-10, -10, 1, 1);
        OKKeyControl = b;
        CancelKeyControl = b;

        SetUpText(_personality.Look, false);
        Position(-2, -2);
    }

    public override bool Handle()
    {
        if (!Script.IsRunning)
        {
            return base.Handle();
        }

        if (Script.RunNext())
        {
            var text = Script.TalkingText;
            SetUpText(text);
        }
        
        return false;
    }

    private void PressText(int index)
    {
        RunNode(_nodeList[index]);
    }

    private void pressLook(Control button) { SetUpText(_personality.Look, false); }
    private void pressName(Control button) { SetUpText(_personality.NameResponse); }
    private void pressJob(Control button) { SetUpText(_personality.JobResponse); }

    private void pressGoBack(Control button)
    {
        if (_goBackList.Count <= 1) return;
        
        _goBackList.RemoveAt(_goBackList.Count - 1);
        var store = _goBackList[^1];
        _goBackList.RemoveAt(_goBackList.Count - 1);
        SetUpText(store.Item1, store.Item2);
    }

    private void PressBuy(Control button)
    {
        var ss = new[] { "purc", "sale", "heal", "iden", "trai" };

        if (ss.Select(s => _personality.FindTalkingNode(s)).Any(node => node != null && RunNode(node)))
        {
            return;
        }
        SetUpText(_personality.BlankResponse);
    }

    private void PressSell(Control button)
    {
        var node = _personality.FindTalkingNode("sell");
        if (node == null || !RunNode(node))
            SetUpText(_personality.BlankResponse);
    }

    private void PressRecord(Control button) 
    {
        Game.AddMessage("Dialogue saved to Notes.");
        Scenario.MakeNote(_personality.Name + " - Day " + Party.Day, _talkBox.GetRawText());
        _buttons[7].Enabled = false;
    }

    private void PressAsk(Control button) { new InputTextWindow(ReturnedAskAbout, "Type what to ask about:", "", false); }

    private void PressDone(Control button) {
        KillMe = true; 
    }

    private void ReturnedAskAbout(string text)
    {
        if (text == null) return;
        
        var node = _personality.FindTalkingNode(text);
        if (node == null || !RunNode(node))
            SetUpText(_personality.BlankResponse);
    }


    private bool RunNode(TalkingNode node)
    {
        if (!node.CheckCondition()) return false;

        if (node.SetsVar) Script.StuffDone[node.ConditionVar] = node.ConditionValue;

        if (node.ForceEnd) _forceEnd = true;

        switch (node.Type)
        {
            case eTalkNodeType.REGULAR:
                SetUpText(node.Text, !_forceEnd);
                break;
            case eTalkNodeType.RUN_FUNCTION:
                Script.TalkingText = node.Text;
                Script.New_Talking(node.LinkedID, _npc);
                break;
            case eTalkNodeType.RUN_SHOP:
                    
                var shop = Shop.List[node.LinkedID];
                if (shop == null)
                {
                    SetUpText("Shop ID '" + node.LinkedID + "' not found.", false);

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
                if (int.TryParse(node.LinkedID, out var n))
                {
                    n = Maths.MinMax(0, 6, n);
                    new HealerShopWindow(this, n);
                }
                break;
            case eTalkNodeType.RUN_IDENTIFY:
                Visible = false;
                if (int.TryParse(node.LinkedID, out n))
                {
                    new IdentifyWindow(this, node.Text, n);
                }
                break;
            case eTalkNodeType.RUN_TRAINING:
                Visible = false;
                new TrainerWindow(this);
                break;
            case eTalkNodeType.RUN_ENCHANTING:
                Visible = false;
                if (int.TryParse(node.LinkedID, out n))
                {
                    n = Maths.MinMax(0, 6, n);
                    new EnchantingWindow(this, node.Text, (eEnchantShop)n);
                }

                break;
        }
        return true;
    }

    private void SetUpText(string Text, bool doWordLinks = true)
    {
        _buttons[7].Enabled = true;

        _goBackList.Add(new Tuple<string, bool>(Text, doWordLinks));
        if (_goBackList.Count == 10)
            _goBackList.RemoveAt(0);

        //Put new lines in properly.
        Text = Text.Replace("|", "@n");

        if (_forceEnd)
        {
            //It has been decreed this conversation must stop. Remove all buttons except for the 'Done' and 'Record' ones.
            foreach (var b in _buttons) b.Visible = false;
        }

        if (_forceEnd || !doWordLinks)
        {
            _talkBox.FormatText(Text);
            return;
        }

        _nodeList = new List<TalkingNode>();
        var sb = new StringBuilder();
        var foundWord = false;
        var startPos = 0;
        
        //Go through each word in the text, checking it with dialogue nodes for this personality.
        for (var n = 0; n < Text.Length; n++)
        {
            if (char.IsLetterOrDigit(Text[n]))
            {
                sb.Append(Text[n]);
                if (!foundWord) startPos = n;
                foundWord = true;
            }
            else if (foundWord && !char.IsLetterOrDigit(Text[n]) || n == Text.Length - 1)
            {
                if (n == Text.Length - 1)
                    sb.Append(Text[n++]);

                //sb should now be our word
                var word = sb.ToString();

                var node = _personality.FindTalkingNode(word);

                if (node != null)
                {
                    Text = Text.Insert(n, "@e");
                    Text = Text.Insert(startPos, "@l");
                    _nodeList.Add(node);
                    n += 3;
                }
                foundWord = false;
                sb.Clear();
            }
        }
        _talkBox.FormatText(Text);
    }

}