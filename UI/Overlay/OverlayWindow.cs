/* ----- ----- ----- ----- */
// OverlayWindow.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/05
// Update Date: 2025/06/05
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Drawing;
using System.Runtime.Versioning;
using System.Windows.Forms;

namespace SudokuSniper.UI.Overlay
{
    /// <summary>
    /// 懸浮視窗（可縮小、移動、半透明）
    /// </summary>
    [SupportedOSPlatform("windows6.1")]
    public class OverlayWindow : Form
    {
        public OverlayWindow()
        {
            FormBorderStyle = FormBorderStyle.None;
            TopMost = true;
            ShowInTaskbar = false;
            BackColor = Color.LightYellow;
            Opacity = 0.85;
            Size = new Size(300, 300);
            StartPosition = FormStartPosition.Manual;
            Location = new Point(Screen.PrimaryScreen.WorkingArea.Width - 320, 200);

            MouseDown += (s, e) => dragStart = e.Location;
            MouseMove += OnDragMove;
        }

        private Point dragStart;

        private void OnDragMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                Left += e.X - dragStart.X;
                Top += e.Y - dragStart.Y;
            }
        }
    }
}
