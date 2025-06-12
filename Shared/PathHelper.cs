/* ----- ----- ----- ----- */
// PathHelper.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/12
// Update Date: 2025/06/12
// Version: v1.0
/* ----- ----- ----- ----- */
using System;
using System.IO;
using System.Runtime.Versioning;

namespace SudokuSniper.Shared
{
    /// <summary>
    /// Provide unified path management logic.
    /// </summary>
    [SupportedOSPlatform("windows6.1")]
    public static class PathHelper
    {
        /// <summary>
        /// Returns the current directory path.
        /// If for DEBUG, it's the project directory; if for release, it's the executable folder.
        /// </summary>
        public static string GetCurrentPath()
        {
#if DEBUG
            return Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, @"..\..\.."));
#else
            return AppContext.BaseDirectory;
#endif
        }

        /// <summary>
        /// Returns the "Temp" directory path.
        /// </summary>
        public static string GetTempFolderPath()
        {
            return Path.Combine(GetCurrentPath(), "Temp");
        }

        /// <summary>
        /// Returns the full path to `capture.png`.
        /// </summary>
        public static string GetCaptureImagePath()
        {
            return Path.Combine(GetTempFolderPath(), "capture.png");
        }

        /// <summary>
        /// Returns the full path to `Analyzer`.
        /// </summary>
        public static string GetAnalyzerPath()
        {
            return Path.Combine(GetCurrentPath(), "Analyzer");
        }
    }
}
