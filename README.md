# CraftClash
![logo](https://raw.githubusercontent.com/Necti-Company/Craft-Clash/master/assets/logo/titlelogo.png)


A dynamic cross of [Clash of Clans](http://supercell.com/en/games/clashofclans/) and [Minecraft](https://minecraft.net/en/). Spend the day upgrading your buildings and walls, craft new items and tend to your world. Have fun spending the night fighting off monsters and hoping you and your world can endure the damage that they do! Written in Python 3 with ❤. Fully open source!! 

**THIS APP IS STILL IN BETA**

![Welcome Screen](https://github.com/Necti-Company/Craft-Clash/blob/master/doc/mainscreen.PNG)

You can craft items to fight monsters such as swords and bows, pickaxes and shovels to mine minerals and other items such as fences to protect your buildings. Use your pickax or shovel to find minerals underground such as coal and iron ore. Then use your coal to turn the iron ore into iron nuggets. Now using your iron you can build some Iron Armour and a Iron Sword to fight the monsters at night, gaining elixir to upgrade your walls that way you are safe from other monster attacks. 

Enough said here, see more in the [game play section](https://github.com/Necti-Company/Craft-Clash#game-play-instructions) or the [wiki](https://github.com/Necti-Company/Craft-Clash/wiki). 

## Installation Instructions
### Through the Python Module (IDLE)
- Download the Python module if you haven’t already: [Download Link](https://www.python.org/downloads), and install it,
- Extract the files from your GitHub Download,
- Double click the `main.py` file in File Explorer,
- And the app will open for you to use!

**THE FOLLOWING TWO OPTIONS CURRENTLY DO NOT WORK:** 

### Creating and Executable File with cx_Freeze (Windows Only)
- Download cx_Freeze if you haven’t already: [Download Link](https://pypi.python.org/packages/38/ae/2cf4f13f42d54b01e26b0b713298722b351ca5a2408b2a77953be67ffb25/cx_Freeze-5.0.win32-py3.5.exe#md5=05e531d442cb9e27d093ca1ee37a03f4), and install it,
- Extract the files from your GitHub download to this location on your computer: `C:\Users\YOUR_USERNAME`,
- Open Command Prompt and type the following command: `python setup.py bdist_msi`
- Run the .msi file that the process creates in a dist sub-directory to create an executable,
- Run the executable and the app will open for you to use!

### Run the Executable File (PyInstaller Required) 
- Extract the files from the GitHub download.
- Navigate to the `exe` file folder
- Extract the `dist.zip` file folder.
- Go to the `main` file folder.
- Run the Executable file named: `main.exe`

## Game Play Instructions
**NOT ALL OF THE BUTTONS WORK RIGHT NOW, WE ARE STILL IN BETA**

After you have opened the app using one of the above options. You will see the apps main interface (GUI). There are three buttons, two of which work right now. The *Play!* button currently does not work but will launch you into your world when it works. Yes there is only one world! We did this that way we could ship our first version of our software faster. The *Options* button will bring you to the options screen which currently only lets you change the volume of the game sounds and the volume of the music. The *Exit* button does exactly what it says it does. It exits the game. Due to a minor bug sometimes the game will reopen after you press this button, to fix this just click the red *X* in the top right hand corner on Windows and the red circle in the left hand corner on Mac. 

To find more information about how to play the game, such as crafting recipes for the world and keyboard controls, see the [wiki](https://github.com/Necti-Company/Craft-Clash/wiki). 

## Releases
**WE ARE STILL IN BETA. SOME FEATURES DO NOT WORK!**

The current release is *BETA v0.0.1*. The next release, version *BETA v0.0.2* is coming out soon with the following features:
- Finished Options screen.
- Game closes when you click the *Exit* button, doesn't re-open.
- Finished documentation, website and wiki!

Your [Pull Requests](https://github.com/Necti-Company/Craft-Clash/pulls) for new features are always welcome! Look to see some of your suggestions in upcoming updates.

## Bugs and Issues
Because this app is still in beta there are lots of things that don't work yet and we are still fixing them, but we need your help too.

Who likes bugs? If you’ve found any feel free to let us know on the [issues page](https://github.com/Necti-Company/Craft-Clash/issues) and we will make sure to fix them in short order, and release those fixes in new releases.

**Note:** Please check the known issues list below before posting an issue to see if your issue is already on the list!
- Program re-opening after the *Exit* button is clicked. (Sometimes)
- The *Play!* button doesn't work. (Not a bug, we haven't got there yet!)

## Contributing
If you are going to contribute please check out the `PLANNING.txt` document for things that we need help with! One thing that we do need right now is help with Travis CI or Circle CI continuous integration.

## Maintainers
- @willtheorangeguy
- @dog-face-developement
- @necti
- @necti-co

## License & Legal Stuff
### License
This software has been released as open source under the *GNU General Public License V3.0* license. 

You can view the license in the [`LICENSE`](https://github.com/Necti-Company/Craft-Clash/blob/master/LICENSE) file in this projects repository.

By using this software you agree to this license. Please adhere to this license when using, distributing, and making changes to the software.

### Assets
Our assets are copyright and license under the *Creative Commons Attribution 4.0 International* license. 

You can view the license in the [`Creative Commons Attribution 4.0 - Assets License.txt`](https://github.com/Necti-Company/Craft-Clash/blob/master/assets/Creative%20Commons%20Attribution%204.0%20-%20Assets%20License.txt) file in the assets folder.

The GUI is Copyright (C) 2016:
Mojang Development (some GUI copied from Minecraft: Windows 10 Edition Beta and then modified) and Necti Co. You can view the license file in [`assets\gui\gui License.txt`](https://github.com/Necti-Company/Craft-Clash/blob/master/assets/gui/gui%20License.txt). 

The Logos are Copyright (C) 2016 Necti Development Co. You can view the license file in [`logo\Logo_Copyrights`](https://github.com/Necti-Company/Craft-Clash/blob/master/assets/logo/Logo_Copyrights.txt).

The Music is Copyright (C) 2016: Mojang Developemt (some music copied from Minecraft: Windows 10 Edition Beta and then modified) and Necti Co. You can vies the license file in [`assets\music\music License.txt`](https://github.com/Necti-Company/Craft-Clash/blob/master/assets/music/music%20License.txt).   
The following songs are copyright by the following individual people:   
*fun.m4a Copyright (C) 2015 William V. (aka: @willtheorangeguy on GitHub)*   
*fun2.mp3 Copyright (C) Mr. Scruff (Album: Ninja Tuna, #1)*    
*calm4.mp3 Copyright (C) Richard Stoltzman, and Slovak Radio Symphony Orchestra (Album: Fine Music, Vol. 1, #2)*

The Textures are Copyright (C) Necti Development Co. and Mojang Development. Some textures copied from Minecraft and Terraria texture packs. The textures have been made with: BDCraft Cubix, and also made with Microsoft Paint. We also made some with Piskel (www.piskelapp.com). You can vies the license file in [`assets\textures\Textures_Info`](https://github.com/Necti-Company/Craft-Clash/blob/master/assets/textures/Textures_Info.txt).

You can learn more about the licensing and legal stuff in the [wiki](https://github.com/Necti-Company/Craft-Clash/wiki). 

## Other Links
Visit these other links to learn more about *CraftClash*:

[The Website](), [Latest Version Download](https://github.com/Necti-Company/Craft-Clash/archive/beta-v0.0.1.zip), [Issues Page](https://github.com/Necti-Company/Craft-Clash/issues), [Pull Request Page](https://github.com/Necti-Company/Craft-Clash/pulls), [Wiki](https://github.com/Necti-Company/Craft-Clash/wiki), and [Documentation](https://github.com/Necti-Company/Craft-Clash/blob/master/README.md).
