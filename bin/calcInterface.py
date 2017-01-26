"""
The calculator's interface
"""
from tkinter import *

class Interface(Tk):
	
	ACTIONS = ["escape", "return", "backspace"]
	
	def __init__(this, core=None):
		super().__init__()
		print("Interface")

		this.core = core
		this.bind("<Key>", this.keyPressed)
		this.create_widgets()

	def create_widgets(this):

		p = PanedWindow(this, orient=VERTICAL)

		#Cree la zone de calcul
		screen = Frame(p, background='white')
		this.Historique =Label(screen,text="",background='white')
		this.Historique.pack(side=TOP, expand=Y, fill=BOTH)
		this.Input = Label(screen,text="",background='white')
		this.Input.pack(side=BOTTOM, expand=Y, fill=BOTH)
		#
		#Create the button clear and clear all
		#
		GroupButtonClear = Frame(this, borderwidth=2, relief=GROOVE)
		Button(GroupButtonClear, text="Effacer",command=lambda: this.refreshDisplay(this.core.clear)).pack(side=LEFT, expand=Y, fill=BOTH)
		Button(GroupButtonClear, text="Tout effacer",command=lambda: this.refreshDisplay(this.core.clearAll)).pack(side=RIGHT, expand=Y, fill=BOTH)
		#
		#Create the button 1234567890.
		#
		GroupButtonCalcul = Frame(this, borderwidth=2, relief=GROOVE)
		#GroupButtonCalcul.pack(expand=Y, fill=BOTH)
		keys = "789 ()456 +-123 */ 0.  ="
		for ligne in range(4):
			for colonne in range(6):
				text = keys[colonne + 6 * ligne]
				if text == " ": continue
				
				# LOL
				command = (lambda x: (lambda: this.sendInput(x)))(text)
				
				Button(GroupButtonCalcul, text='%s' % (text), borderwidth=1, command=command).grid(row=ligne, column=colonne)

		#affichage
		p.pack(side=TOP, expand=Y, fill=BOTH, pady=5, padx=5)
		p.add(screen)
		p.add(GroupButtonClear)
		p.add(GroupButtonCalcul)
		p.pack()

	# Triggered when a key is pressed
	def keyPressed(this, event):
		sym = event.keysym.lower()
		if not this.action(sym):
			this.sendInput(event.char)
	
	def action(this, action):
		if action in this.ACTIONS:
			return False
		elif sym == "return":
			this.evaluate()
		elif sym == "escape":
			this.destroy()
		
		return True
	
	# Send the input to the Core
	def sendInput(this, char):
		this.core.press(char)
		print(this.core.input)
		this.Input.config(text=this.core.input) 
	
	# Evaluate the current expression
	def evaluate(this):
		result = this.core.evalInput()
		print(result)
	
	def refreshDisplay(this, func, *args):
		func(*args)
		this.Input.config(text=this.core.input) 