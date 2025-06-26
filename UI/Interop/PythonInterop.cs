/* ----- ----- ----- ----- */
// PythonInterop.cs
// Do not distribute or modify
// Author: DragonTaki (https://github.com/DragonTaki)
// Create Date: 2025/06/12
// Update Date: 2025/06/12
// Version: v1.0
/* ----- ----- ----- ----- */

using System;
using System.Diagnostics;

namespace SudokuSniper.UI.Interop
{
    /// <summary>
    /// Handles Python interop logic, including calling scripts and parsing responses.
    /// </summary>
    public static class PythonInterop
    {
        /// <summary>
        /// Executes the specified Python script and obtains the standard output results.
        /// </summary>
        /// <param name="pythonExe">The name of the Python executable, such as "python"</param>
        /// <param name="args">Command line arguments to pass to Python</param>
        /// <param name="workingDir">The folder where the Python script is located (can be null)</param>
        /// <returns>Standard output results</returns>
#nullable enable
        public static string RunScript(string pythonExe, string args, string? workingDir = null)
#nullable disable
        {
            var psi = new ProcessStartInfo
            {
                FileName = pythonExe,
                Arguments = args,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };

            if (workingDir != null)
                psi.WorkingDirectory = workingDir;

            using var process = Process.Start(psi)!;
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();
            process.WaitForExit();

            Console.WriteLine(output);
            Console.WriteLine(error);
            
            if (process.ExitCode != 0)
                throw new Exception($"Python error: {error}");

            return output;
        }
    }
}
