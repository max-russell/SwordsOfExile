using System;

namespace SwordsOfExileGame;

internal static class Program
{
    /// <summary>
    /// The main entry point for the application.
    /// </summary>
    [STAThread]
    private static void Main(string[] args)
    {
        using (var game = new Game())
        {
            game.Run();
        }
    }
}