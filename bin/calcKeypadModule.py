# -*- coding: utf8 -*-
"""
This class allows for keyboard input, from the keypad
"""

import tkinter as tk

class KeypadModule(object):

	def __init__(this, tkApp):
		print("KeypadModule")
		this.root = tkApp
		this.root.bind("<Key>", this.keyPressed)

	def keyPressed(this, event):
		key = (event.char, event.keysym, event.keycode)
		this.root.keyPressed(key)
