﻿"""
Copyright (C) 2016 - 2018
Derpyface Development Co. and Dog Face Development Co.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

## All rights reserved.

"""
CRAFTCLASH
Main project file.
"""

# Import Statements
from tkinter import *
import turtle
from craftclash.optionscreen import *
from craftclash.aboutscreen import *

# Window Elements
window = Tk()
window.title("CraftClash - Windows - 0.0.3 BETA")
window.configure(bg = "sky blue")

# Images
titleimg = PhotoImage(file = "assets/logo/titlelogo.gif")
playimg = PhotoImage(file = "assets/gui/play-circle.gif")
optionimg = PhotoImage(file = "assets/gui/cog.gif")
aboutimg = PhotoImage(file = "assets/gui/about.gif")

# Widgets
title_label = Label(window, image = titleimg)
btn_play = Button(window, text = "Play!", height = 3, width = 60, bd = 4, relief = RAISED, command = exit)
play_img = Label(window, image = playimg)
btn_options = Button(window, text = "Options", height = 3, width = 60, bd = 4, relief = RAISED, command = optionsscreen)
options_img = Label(window, image = optionimg)
btn_about = Button(window, text = "About", height = 3, width = 60, bd = 4, relief = RAISED, command = aboutscreen)
about_img = Label(window, image = aboutimg)
copyright_label = Label(window, text = "Copyright © 2016 - 2017 Derpyface Development Co. and Dog Face Development Co. \t\t\t Version 0.0.3 BETA")

# Pack Statements
title_label.grid(row = 1, column = 2, rowspan = 2, pady = 10)
play_img.grid(row = 3, column = 1)
btn_play.grid(row = 3, column = 2, columnspan = 2)
options_img.grid(row = 4, column = 1)
btn_options.grid(row = 4, column = 2, columnspan = 2)
about_img.grid(row = 5, column = 1)
btn_about.grid(row = 5, column = 2, columnspan = 2)
copyright_label.grid(row = 6, column = 1, columnspan = 5)

# Sustain Window
window.mainloop()
