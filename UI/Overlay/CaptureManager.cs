/* ----- ----- ----- ----- */
// CaptureManager.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/05
// Update Date: 2025/06/05
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Runtime.Versioning;
using System.Windows.Forms;
using SudokuSniper.Shared;
using SudokuSniper.UI.Interop;

namespace SudokuSniper.UI.Overlay
{
    /// <summary>
    /// Controls capture workflow: user selects region, screenshot is saved to file.
    /// </summary>
    [SupportedOSPlatform("windows6.1")]
    public class CaptureManager
    {
        private readonly OverlayForm _overlayForm;

        public CaptureManager()
        {
            _overlayForm = new OverlayForm();
            _overlayForm.SelectionMade += OnSelectionMade;
        }

        public void StartCapture()
        {
            _overlayForm.Show();
        }

        private void OnSelectionMade(Rectangle region)
        {
            if (region.Width == 0 || region.Height == 0) return;

            using Bitmap bmp = new Bitmap(region.Width, region.Height);
            using Graphics g = Graphics.FromImage(bmp);
            g.CopyFromScreen(region.Location, Point.Empty, region.Size);

            string path = PathHelper.GetCaptureImagePath();
            Directory.CreateDirectory(Path.GetDirectoryName(path)!);
            bmp.Save(path, ImageFormat.Png);

            //MessageBox.Show($"Saved to {path}", "Capture Complete", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        public string AnalyzeLastCapture()
        {
            string imagePath = PathHelper.GetCaptureImagePath();
            string workingDir = PathHelper.GetCurrentPath();
            return PythonInterop.RunScript("python", $"-m Analyzer \"{imagePath}\"", workingDir);
        }
    }
}
