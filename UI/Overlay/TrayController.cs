/* ----- ----- ----- ----- */
// TrayController.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/05
// Update Date: 2025/06/05
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Windows.Forms;
using System.Drawing;

namespace SudokuSniper.UI.Overlay
{
    /// <summary>
    /// 控制系統匣功能，包括圖示與右鍵選單
    /// </summary>
    public class TrayController : IDisposable
    {
        private readonly NotifyIcon trayIcon;

        public TrayController()
        {
            trayIcon = new NotifyIcon
            {
                Icon = SystemIcons.Application,
                Text = "SudokuSniper",
                Visible = true,
                ContextMenuStrip = BuildContextMenu()
            };
        }

        private ContextMenuStrip BuildContextMenu()
        {
            var menu = new ContextMenuStrip();
            menu.Items.Add("擷取畫面", null, (s, e) => ScreenshotRequested?.Invoke());
            menu.Items.Add(new ToolStripSeparator());
            menu.Items.Add("退出", null, (s, e) => Application.Exit());
            return menu;
        }

        public event Action ScreenshotRequested;

        public void Dispose()
        {
            trayIcon.Visible = false;
            trayIcon.Dispose();
        }
    }
}
