/* ----- ----- ----- ----- */
// GlobalHotkey.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/05
// Update Date: 2025/06/05
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace SudokuSniper.UI.Overlay
{
    /// <summary>
    /// Handles registration and monitoring of a global hotkey (Ctrl + Shift + Z).
    /// </summary>
    public class GlobalHotkey : IDisposable
    {
        private const int WM_HOTKEY = 0x0312;
        private const int HOTKEY_ID = 9000;

        [DllImport("user32.dll")]
        private static extern bool RegisterHotKey(IntPtr hWnd, int id, uint fsModifiers, Keys vk);

        [DllImport("user32.dll")]
        private static extern bool UnregisterHotKey(IntPtr hWnd, int id);

        private readonly Form _listeningForm;

        public event Action? HotkeyPressed;

        public GlobalHotkey()
        {
            _listeningForm = new HiddenForm();
            RegisterHotKey(_listeningForm.Handle, HOTKEY_ID, MOD_CONTROL | MOD_SHIFT, Keys.Z);
            Application.AddMessageFilter(new HotkeyMessageFilter(HOTKEY_ID, () => HotkeyPressed?.Invoke()));
        }

        public void Dispose()
        {
            UnregisterHotKey(_listeningForm.Handle, HOTKEY_ID);
            _listeningForm.Close();
        }

        private class HiddenForm : Form
        {
            public HiddenForm()
            {
                ShowInTaskbar = false;
                FormBorderStyle = FormBorderStyle.None;
                Opacity = 0;
                Width = 0;
                Height = 0;
                Load += (_, _) => Hide();
            }
        }

        private class HotkeyMessageFilter : IMessageFilter
        {
            private readonly int _hotkeyId;
            private readonly Action _onHotkey;

            public HotkeyMessageFilter(int hotkeyId, Action onHotkey)
            {
                _hotkeyId = hotkeyId;
                _onHotkey = onHotkey;
            }

            public bool PreFilterMessage(ref Message m)
            {
                if (m.Msg == WM_HOTKEY && m.WParam.ToInt32() == _hotkeyId)
                {
                    _onHotkey();
                    return true;
                }
                return false;
            }
        }

        private const uint MOD_CONTROL = 0x0002;
        private const uint MOD_SHIFT = 0x0004;
    }
}
