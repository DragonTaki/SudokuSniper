/* ----- ----- ----- ----- */
// Program.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/05
// Update Date: 2025/06/05
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Runtime.Versioning;
using System.Windows.Forms;

using SudokuSniper.UI.Overlay;

namespace SudokuSniper.UI
{
    /// <summary>
    /// Program entry point, initialization of UI and system components.
    /// </summary>
    [SupportedOSPlatform("windows6.1")]
    internal static class Program
    {
        [STAThread]
        static void Main()
        {
            ApplicationConfiguration.Initialize();
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            var captureManager = new CaptureManager();

            // Bind global hotkeys
            var hotkey = new GlobalHotkey();
            hotkey.HotkeyPressed += captureManager.StartCapture;

            // Create a system tray controller
            using var tray = new TrayController();
            tray.ScreenshotRequested += () => captureManager.StartCapture();
            tray.ReanalyzeRequested += () => captureManager.AnalyzeLastCapture();

            // Create a floating window (initially hidden)
            var overlay = new OverlayWindow();
            overlay.Show();

            Application.Run();
        }
    }
}
