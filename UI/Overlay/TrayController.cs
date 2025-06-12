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
using System.Runtime.Versioning;

namespace SudokuSniper.UI.Overlay
{
    /// <summary>
    /// 控制系統匣功能，包括圖示與右鍵選單
    /// </summary>
    [SupportedOSPlatform("windows6.1")]
    public class TrayController : IDisposable
    {
        private readonly NotifyIcon _trayIcon;

        public TrayController()
        {
            _trayIcon = new NotifyIcon
            {
                Icon = SystemIcons.Application,
                Text = "SudokuSniper",
                Visible = true,
                ContextMenuStrip = BuildContextMenu()
            };
        }

        /// <summary>
        /// 當使用者選擇「擷取畫面」時觸發
        /// </summary>
#nullable enable
        public event Action? ScreenshotRequested;
#nullable disable

        /// <summary>
        /// 當使用者選擇「重新解析擷圖」時觸發
        /// </summary>
#nullable enable
        public event Action? ReanalyzeRequested;
#nullable disable

        private ContextMenuStrip BuildContextMenu()
        {
            var menu = new ContextMenuStrip();
            menu.Items.Add("擷取畫面", null, (s, e) => ScreenshotRequested?.Invoke());
            menu.Items.Add("重新解析擷圖", null, (s, e) => ReanalyzeRequested?.Invoke());
            menu.Items.Add(new ToolStripSeparator());
            menu.Items.Add("退出", null, (s, e) => Application.Exit());
            return menu;
        }

        public void Dispose()
        {
            _trayIcon.Visible = false;
            _trayIcon.Dispose();
        }
    }
}
