"""
The calculator's interface
"""
import tkinter as tk
from tkinter import *

class Interface(tk.Tk):

	def __init__(this, core=None):
		super().__init__()
		print("Interface")

		this.core = core
		this.root.bind("<Key>", this.keyPressed)
		this.create_widgets()

	def create_widgets(this):

		p = PanedWindow(this, orient=VERTICAL)

		#Cree la zone de calcul
		canvas = Canvas(p, width=300, height=200, background='white')

		#
		#Create the button clear and clear all
		#
		GroupButtonClear = Frame(this, borderwidth=2, relief=GROOVE)
		Button(GroupButtonClear, text="Effacer").pack(side=LEFT, expand=Y, fill=BOTH)
		Button(GroupButtonClear, text="Tous effacer").pack(side=RIGHT, expand=Y, fill=BOTH)

		#
		#Create the button 1234567890.
		#
		GroupButtonCalcul = Frame(this, borderwidth=2, relief=GROOVE)
		keys = "789456123 0."
		for ligne in range(4):
			for colonne in range(3):
				text = keys[colonne + 3 * ligne]
				if text == " ": continue
				Button(GroupButtonCalcul, text='%s' % (text), borderwidth=1).grid(row=ligne, column=colonne)

		#affichage
		p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
		p.add(canvas)
		p.add(GroupButtonClear)
		p.add(GroupButtonCalcul)
		p.pack()

	# Triggered when a key is pressed
	def keyPressed(this, event):
		this.sendInput(event.char)
		print(this.core.input)
	
	# Send the input to the Core
	def sendInput(this, char)
		this.core.press(char)
	
	# Evaluate the current expression
	def evaluate(this):
		result = this.core.evalInput()