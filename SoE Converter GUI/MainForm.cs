using System;
using System.Collections;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using System.Xml;
using System.Xml.Linq;

namespace SoE_Converter_GUI
{
    public partial class MainForm : Form
    {
        private const string SETTINGS_FILE = "Converter Gui Settings.xml";
        private string scenDir = "";
        private string SoEPath = "SoE Converter";
        private int sortedColumn = -1;

        private Process converterProcess;

        public MainForm()
        {
            InitializeComponent();
#if DEBUG
            Directory.SetCurrentDirectory(@"..\..\..");
            var s = Directory.GetCurrentDirectory();
#endif
            Text = "Swords of Exile Scenario Converter " + System.Reflection.Assembly.GetExecutingAssembly().GetName().Version;
        }

        private void ShowHelp()
        {
            MessageBox.Show("You can use the Blades of Exile Converter to convert Blades of Exile scenario\n" +
                "to one that can be played in Swords of Exile. Click 'Browse' and find the 'scenarios'" +
                "directory in your Blades of Exile installation. Then choose a scenario from the list" +
                "box and hit 'Convert'", "Help");
        }

        private void btnBrowse_Click(object sender, EventArgs e)
        {
            var d = folderBrowserDialog.ShowDialog();
            if (d == DialogResult.OK)
            {
                scenDir = folderBrowserDialog.SelectedPath;
                updateScenList();
                SaveSettings();
            }
        }

        private void updateScenList()
        {
            txtScenarioDir.Text = scenDir;
            lstScenarios.SuspendLayout();
            lstScenarios.Items.Clear();
            foreach (var s in Directory.EnumerateFiles(scenDir, "*.exs", SearchOption.TopDirectoryOnly))
            {
                using (var fs = new FileStream(s, FileMode.Open))
                {
                    fs.Seek(0xA2A4, SeekOrigin.Begin);
                    var len = fs.ReadByte();
                    fs.Seek(0x13CF6, SeekOrigin.Begin);
                    var nm = new byte[len];
                    fs.Read(nm, 0, len);

                    string[] items = { Path.GetFileName(s), Encoding.ASCII.GetString(nm), Convert.ToString(new FileInfo(s).Length / 1024) + " KB" };

                    var item = new ListViewItem(items);
                    lstScenarios.Items.Add(item);
                }
            }
            lstScenarios.ResumeLayout();
            btnConvert.Enabled = false;
        }

        private void btnConvert_Click(object sender, EventArgs e)
        {
            if (converterProcess != null && !converterProcess.HasExited) return;

            if (lstScenarios.SelectedIndices.Count > 0)
            {
                var scen = Path.Combine(scenDir, Path.ChangeExtension((string)lstScenarios.SelectedItems[0].Text, "exs"));

                txtOutputHeader.Text = "Converting '" + scen + "'...";
                txtOutput.Clear();
                tabControl.SelectedTab = tabOutput;
                converterProcess = Run(dataOut, null, SoEPath, "\"" + scen + "\"" + (chkLegacy.Checked ? " -l" : ""));
            }
        }

        private delegate void SetTextCallback(string text, bool error);

        private void dataOut(string text, bool error)
        {
            // InvokeRequired required compares the thread ID of the
            // calling thread to the thread ID of the creating thread.
            // If these threads are different, it returns true.
            if (txtOutput.InvokeRequired)
            {
                var d = new SetTextCallback(dataOut);
                this.Invoke(d, new object[] { text, error });
            }
            else
            {
                var l = txtOutput.Text.Length;
                txtOutput.Text += text + Environment.NewLine;

                txtOutput.Select(l, text.Length);
                txtOutput.SelectionColor = error ? Color.Red : Color.Green;

                txtOutput.ScrollToCaret();
            }
        }

        public static Process Run(Action<string, bool> output, TextReader input, string exe, string args)
        {
            if (String.IsNullOrEmpty(exe))
                throw new FileNotFoundException();
            if (output == null)
                throw new ArgumentNullException("output");

            var psi = new ProcessStartInfo();
            psi.UseShellExecute = false;
            psi.RedirectStandardError = true;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardInput = true;
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            psi.CreateNoWindow = true;
            psi.ErrorDialog = false;
            psi.WorkingDirectory = Environment.CurrentDirectory;
            psi.FileName = exe;
            psi.Arguments = args;

            var process = Process.Start(psi);

            process.OutputDataReceived += (o, e) => { if (e.Data != null) /*mreOut.Set(); else*/ output(e.Data, false); };
            process.BeginOutputReadLine();
            process.ErrorDataReceived += (o, e) => { if (e.Data != null) /*mreErr.Set(); else*/ output(e.Data, true); };
            process.BeginErrorReadLine();

            string line;
            while (input != null && null != (line = input.ReadLine()))
                process.StandardInput.WriteLine(line);

            process.StandardInput.Close();
            return process;
        }

        private void LoadSettings()
        {
            //Here's where the game's settings are loaded from the XML file in the game root directory

            XElement xml = null;


            if (File.Exists(SETTINGS_FILE))
            {
                xml = XElement.Load(SETTINGS_FILE);
                if (xml.Name != "Settings") throw new Exception("Corrupt settings file.");

                foreach (var e in xml.Elements())
                {
                    if (e.Name.ToString() == "BoE_Dir")
                        scenDir = e.Value;
                }
            }
            else
            {
                SaveSettings();
                ShowHelp();
            }
        }

        private void SaveSettings()
        {
            var settings = new XmlWriterSettings();
            settings.Indent = true;
            settings.OmitXmlDeclaration = true;
            settings.ConformanceLevel = ConformanceLevel.Fragment;

            using (var writer = XmlWriter.Create(SETTINGS_FILE, settings))
            {
                writer.WriteStartElement("Settings");
                writer.WriteElementString("BoE_Dir", scenDir);
                writer.WriteEndElement();
            }
        }

        private void btnHelp_Click(object sender, EventArgs e)
        {
            ShowHelp();
        }

        private void mainForm_Shown(object sender, EventArgs e)
        {
            LoadSettings();
            if (Directory.Exists(scenDir))
                updateScenList();
        }

        private void lstScenarios_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            if (lstScenarios.SelectedIndices.Count > 0) btnConvert.Enabled = true;
        }

        private void lstScenarios_ColumnClick(object sender, ColumnClickEventArgs e)
        {
            // Determine if clicked column is already the column that is being sorted.
            if (e.Column == sortedColumn)
                lstScenarios.Sorting = lstScenarios.Sorting == SortOrder.Ascending ? SortOrder.Descending : SortOrder.Ascending;
            else
            {
                lstScenarios.Sorting = SortOrder.Ascending;
            }

            lstScenarios.ListViewItemSorter = new ListViewItemComparer(e.Column, lstScenarios.Sorting);
            sortedColumn = e.Column;

            // Perform the sort with these new sort options.
            lstScenarios.Sort();
        }
    }

    // Implements the manual sorting of items by columns.
    internal class ListViewItemComparer : IComparer
    {
        private int col;
        private SortOrder order;

        public ListViewItemComparer()
        {
            col = 0;
        }
        public ListViewItemComparer(int column, SortOrder _order)
        {
            col = column;
            order = _order;
        }
        public int Compare(object x, object y)
        {
            int comp;

            if (col < 2)
            {
                comp = String.Compare(((ListViewItem)x).SubItems[col].Text, ((ListViewItem)y).SubItems[col].Text);
            }
            else
            {
                var s1 = ((ListViewItem)x).SubItems[col].Text;
                s1 = s1.Remove(s1.Length - 3);
                var i1 = Convert.ToInt32(s1);
                var s2 = ((ListViewItem)y).SubItems[col].Text;
                s2 = s2.Remove(s2.Length - 3);
                var i2 = Convert.ToInt32(s2);
                comp = i1.CompareTo(i2);
            }

            return order == SortOrder.Ascending ? comp : -comp;
        }
    }
}
