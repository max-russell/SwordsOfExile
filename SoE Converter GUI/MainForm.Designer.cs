

namespace SoE_Converter_GUI
{
    partial class MainForm 
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.folderBrowserDialog = new System.Windows.Forms.FolderBrowserDialog();
            this.tabControl = new System.Windows.Forms.TabControl();
            this.tabOptions = new System.Windows.Forms.TabPage();
            this.lstScenarios = new System.Windows.Forms.ListView();
            this.colFilename = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colTitle = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colSize = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.btnHelp = new System.Windows.Forms.Button();
            this.btnConvert = new System.Windows.Forms.Button();
            this.chkLegacy = new System.Windows.Forms.CheckBox();
            this.btnBrowse = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.txtScenarioDir = new System.Windows.Forms.TextBox();
            this.tabOutput = new System.Windows.Forms.TabPage();
            this.txtOutput = new System.Windows.Forms.RichTextBox();
            this.txtOutputHeader = new System.Windows.Forms.TextBox();
            this.tabControl.SuspendLayout();
            this.tabOptions.SuspendLayout();
            this.tabOutput.SuspendLayout();
            this.SuspendLayout();
            // 
            // folderBrowserDialog
            // 
            this.folderBrowserDialog.RootFolder = System.Environment.SpecialFolder.MyComputer;
            this.folderBrowserDialog.ShowNewFolderButton = false;
            // 
            // tabControl
            // 
            this.tabControl.Controls.Add(this.tabOptions);
            this.tabControl.Controls.Add(this.tabOutput);
            this.tabControl.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabControl.Location = new System.Drawing.Point(0, 0);
            this.tabControl.Name = "tabControl";
            this.tabControl.SelectedIndex = 0;
            this.tabControl.Size = new System.Drawing.Size(632, 431);
            this.tabControl.TabIndex = 6;
            // 
            // tabOptions
            // 
            this.tabOptions.BackColor = System.Drawing.SystemColors.Control;
            this.tabOptions.Controls.Add(this.lstScenarios);
            this.tabOptions.Controls.Add(this.btnHelp);
            this.tabOptions.Controls.Add(this.btnConvert);
            this.tabOptions.Controls.Add(this.chkLegacy);
            this.tabOptions.Controls.Add(this.btnBrowse);
            this.tabOptions.Controls.Add(this.label1);
            this.tabOptions.Controls.Add(this.txtScenarioDir);
            this.tabOptions.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tabOptions.Location = new System.Drawing.Point(4, 22);
            this.tabOptions.Name = "tabOptions";
            this.tabOptions.Padding = new System.Windows.Forms.Padding(3);
            this.tabOptions.Size = new System.Drawing.Size(624, 405);
            this.tabOptions.TabIndex = 0;
            this.tabOptions.Text = "Options";
            // 
            // lstScenarios
            // 
            this.lstScenarios.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
            | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lstScenarios.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colFilename,
            this.colTitle,
            this.colSize});
            this.lstScenarios.FullRowSelect = true;
            this.lstScenarios.GridLines = true;
            this.lstScenarios.Location = new System.Drawing.Point(6, 32);
            this.lstScenarios.MultiSelect = false;
            this.lstScenarios.Name = "lstScenarios";
            this.lstScenarios.Size = new System.Drawing.Size(503, 361);
            this.lstScenarios.TabIndex = 13;
            this.lstScenarios.UseCompatibleStateImageBehavior = false;
            this.lstScenarios.View = System.Windows.Forms.View.Details;
            this.lstScenarios.ColumnClick += new System.Windows.Forms.ColumnClickEventHandler(this.lstScenarios_ColumnClick);
            this.lstScenarios.SelectedIndexChanged += new System.EventHandler(this.lstScenarios_SelectedIndexChanged_1);
            // 
            // colFilename
            // 
            this.colFilename.Text = "Filename";
            this.colFilename.Width = 103;
            // 
            // colTitle
            // 
            this.colTitle.Text = "Title";
            this.colTitle.Width = 320;
            // 
            // colSize
            // 
            this.colSize.Text = "Size";
            this.colSize.Width = 73;
            // 
            // btnHelp
            // 
            this.btnHelp.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnHelp.Location = new System.Drawing.Point(515, 32);
            this.btnHelp.Name = "btnHelp";
            this.btnHelp.Size = new System.Drawing.Size(102, 33);
            this.btnHelp.TabIndex = 12;
            this.btnHelp.Text = "Help";
            this.btnHelp.UseVisualStyleBackColor = true;
            this.btnHelp.Click += new System.EventHandler(this.btnHelp_Click);
            // 
            // btnConvert
            // 
            this.btnConvert.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnConvert.Enabled = false;
            this.btnConvert.Location = new System.Drawing.Point(515, 357);
            this.btnConvert.Name = "btnConvert";
            this.btnConvert.Size = new System.Drawing.Size(102, 36);
            this.btnConvert.TabIndex = 11;
            this.btnConvert.Text = "Convert";
            this.btnConvert.UseVisualStyleBackColor = true;
            this.btnConvert.Click += new System.EventHandler(this.btnConvert_Click);
            // 
            // chkLegacy
            // 
            this.chkLegacy.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.chkLegacy.AutoSize = true;
            this.chkLegacy.Checked = true;
            this.chkLegacy.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkLegacy.Location = new System.Drawing.Point(515, 295);
            this.chkLegacy.Name = "chkLegacy";
            this.chkLegacy.Size = new System.Drawing.Size(106, 56);
            this.chkLegacy.TabIndex = 9;
            this.chkLegacy.Text = "Legacy Scenario\r\n(Created in the\r\noriginal Scenario\r\nEditor)";
            this.chkLegacy.UseVisualStyleBackColor = true;
            this.chkLegacy.Visible = false;
            // 
            // btnBrowse
            // 
            this.btnBrowse.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.btnBrowse.Location = new System.Drawing.Point(563, 6);
            this.btnBrowse.Name = "btnBrowse";
            this.btnBrowse.Size = new System.Drawing.Size(54, 19);
            this.btnBrowse.TabIndex = 8;
            this.btnBrowse.Text = "Browse";
            this.btnBrowse.UseVisualStyleBackColor = true;
            this.btnBrowse.Click += new System.EventHandler(this.btnBrowse_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(3, 3);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(97, 26);
            this.label1.TabIndex = 7;
            this.label1.Text = "Blades of Exile\r\nScenario Directory:";
            // 
            // txtScenarioDir
            // 
            this.txtScenarioDir.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtScenarioDir.Location = new System.Drawing.Point(103, 6);
            this.txtScenarioDir.Name = "txtScenarioDir";
            this.txtScenarioDir.ReadOnly = true;
            this.txtScenarioDir.Size = new System.Drawing.Size(454, 20);
            this.txtScenarioDir.TabIndex = 6;
            // 
            // tabOutput
            // 
            this.tabOutput.BackColor = System.Drawing.SystemColors.Control;
            this.tabOutput.Controls.Add(this.txtOutput);
            this.tabOutput.Controls.Add(this.txtOutputHeader);
            this.tabOutput.Location = new System.Drawing.Point(4, 22);
            this.tabOutput.Name = "tabOutput";
            this.tabOutput.Padding = new System.Windows.Forms.Padding(3);
            this.tabOutput.Size = new System.Drawing.Size(624, 405);
            this.tabOutput.TabIndex = 1;
            this.tabOutput.Text = "Output";
            // 
            // txtOutput
            // 
            this.txtOutput.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
            | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtOutput.BackColor = System.Drawing.Color.Black;
            this.txtOutput.ForeColor = System.Drawing.Color.PaleGreen;
            this.txtOutput.Location = new System.Drawing.Point(10, 35);
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.Size = new System.Drawing.Size(606, 362);
            this.txtOutput.TabIndex = 2;
            this.txtOutput.Text = "";
            // 
            // txtOutputHeader
            // 
            this.txtOutputHeader.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
            | System.Windows.Forms.AnchorStyles.Right)));
            this.txtOutputHeader.Location = new System.Drawing.Point(10, 9);
            this.txtOutputHeader.Name = "txtOutputHeader";
            this.txtOutputHeader.ReadOnly = true;
            this.txtOutputHeader.Size = new System.Drawing.Size(608, 20);
            this.txtOutputHeader.TabIndex = 1;
            // 
            // mainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(632, 431);
            this.Controls.Add(this.tabControl);
            //this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "mainForm";
            this.Text = "Swords of Exile Scenario Converter";
            this.Shown += new System.EventHandler(this.mainForm_Shown);
            this.tabControl.ResumeLayout(false);
            this.tabOptions.ResumeLayout(false);
            this.tabOptions.PerformLayout();
            this.tabOutput.ResumeLayout(false);
            this.tabOutput.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog;
        private System.Windows.Forms.TabControl tabControl;
        private System.Windows.Forms.TabPage tabOptions;
        private System.Windows.Forms.TabPage tabOutput;
        private System.Windows.Forms.Button btnConvert;
        private System.Windows.Forms.CheckBox chkLegacy;
        private System.Windows.Forms.Button btnBrowse;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtScenarioDir;
        private System.Windows.Forms.TextBox txtOutputHeader;
        private System.Windows.Forms.RichTextBox txtOutput;
        private System.Windows.Forms.Button btnHelp;
        private System.Windows.Forms.ListView lstScenarios;
        private System.Windows.Forms.ColumnHeader colFilename;
        private System.Windows.Forms.ColumnHeader colTitle;
        private System.Windows.Forms.ColumnHeader colSize;
    }
}