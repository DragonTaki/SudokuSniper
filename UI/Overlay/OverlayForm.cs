/* ----- ----- ----- ----- */
// OverlayForm.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/05
// Update Date: 2025/06/05
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Drawing;
using System.Windows.Forms;

namespace SudokuSniper.UI.Overlay
{
    /// <summary>
    /// Transparent fullscreen overlay for selecting screen region.
    /// </summary>
    public class OverlayForm : Form
    {
        private Point _startPoint;
        private Rectangle _selection;
        private bool _selecting = false;

        public event Action<Rectangle>? SelectionMade;

        public OverlayForm()
        {
            DoubleBuffered = true;
            FormBorderStyle = FormBorderStyle.None;
            WindowState = FormWindowState.Maximized;
            BackColor = Color.Black;
            Opacity = 0.3;
            TopMost = true;
            Cursor = Cursors.Cross;
            ShowInTaskbar = false;

            MouseDown += OnMouseDown;
            MouseMove += OnMouseMove;
            MouseUp += OnMouseUp;
            Paint += OnPaint;
        }

        private void OnMouseDown(object? sender, MouseEventArgs e)
        {
            if (e.Button != MouseButtons.Left) return;
            _startPoint = e.Location;
            _selecting = true;
        }

        private void OnMouseMove(object? sender, MouseEventArgs e)
        {
            if (!_selecting) return;
            _selection = GetRectangle(_startPoint, e.Location);
            Invalidate();
        }

        private void OnMouseUp(object? sender, MouseEventArgs e)
        {
            if (!_selecting) return;
            _selecting = false;
            _selection = GetRectangle(_startPoint, e.Location);
            Invalidate();
            Hide();
            SelectionMade?.Invoke(_selection);
        }

        private void OnPaint(object? sender, PaintEventArgs e)
        {
            if (_selecting)
            {
                using var pen = new Pen(Color.Red, 2);
                e.Graphics.DrawRectangle(pen, _selection);
            }
        }

        private Rectangle GetRectangle(Point p1, Point p2)
        {
            return new Rectangle(
                Math.Min(p1.X, p2.X),
                Math.Min(p1.Y, p2.Y),
                Math.Abs(p2.X - p1.X),
                Math.Abs(p2.Y - p1.Y));
        }
    }
}
