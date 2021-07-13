//using System;


//namespace SwordsOfExileGame
//{
//    public static class OldProgram
//    {
//        [STAThread]
//        static void Main()
//        {
//            using (var game = new Game1())
//                game.Run();
//        }
//    }
//}

using System;
using System.IO;
using System.Collections.Generic;
using Microsoft.Xna.Framework;

namespace SwordsOfExileGame
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            using (Game game = new Game())
            {
                game.Run();
            }
        }
    }
}

