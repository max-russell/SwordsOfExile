# Swords Of Exile
**This is a remake of Blades of Exile, an RPG originally released in 1997 by [Spiderweb Software](https://www.spiderwebsoftware.com)**.

Blades of Exile followed Spiderweb's oringal Exile trilogy, which have since been remade (twice) under the name Avernum. It was originally shareware, but the source code later released under a GPLv2 licence, and can be found [here](https://www.spiderwebsoftware.com/blades/opensource.html). Blades of Exile's innovation was that it included a scenario editor, allowing player's to construct their own fully-featured adventures. The editor was powerful - almost all features from the original games could be included in custom scenarios - and led to a large number of [user-created adventures](http://www.spiderwebsoftware.com/blades/scen_list.html).

This version is a full rewrite from the ground up in C#/NET. It was started a few years ago using Microsoft XNA as the game engine. This version now uses MonoGame which is more up-to-date and allows cross-platfrom functionality.

My aim is to provide a slightly updated experience to the original game, while allowing all Blades of Exiles scenarios to be played (once they have been converted with the included utility). BoE included a very rudimentary 'scripting' ability, creating event nodes in the editor and allowing simple conditional checking and branching. Swords of Exile, by contrast, uses Python scripting. The conversion utility attempts to automatically write Python code to replicate the original scenario's behaviour. The resulting code is certainly not pretty, but should hopefully run.

It has been built and tested under Windows 10. It should be possible to build it for Linux/MacOS too without too much trouble, but so far this has not been attempted! This applies to the scenario converter too, which is a command-line program. There's also a simple GUI for the converter, which uses WinForms so is likely to be restricted to Windows.
