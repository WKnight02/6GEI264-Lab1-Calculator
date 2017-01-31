"""
The calculator's interface
"""
from tkinter import *
import tkinter.font as font

class Interface(Tk):

	DEFAULTS = {
		"height": 450,
		"width": 350,
	}

	def __init__(this, core=None, **kargs):
		super().__init__()
		print("Interface")

		this.core = core

		this.bind("<Key>", this.keyPressed)

		this.Actions = {
			"escape": this.destroy,
			"return": this.evaluate,
			"backspace": lambda: this.refreshInput(this.core.clear),
			"delete": lambda: this.refreshInput(this.core.clearAll),
		}

		# Sets the size of the interface
		this.height = kargs.get("height", this.DEFAULTS["height"])
		this.width = kargs.get("width", this.DEFAULTS["width"])
		this.resizable(width=False, height=False)
		this.geometry("%dx%d" % (this.width, this.height))

		# The app's fonts
		this.ButtonFont = font.Font(family="Arial", size=12, weight="bold")
		this.CommandFont = font.Font(family="Consolas", size=16)

		this.create_widgets()
		this.refreshInput()

	def create_widgets(this):

		# This is the main vertical layout (screen / buttons)
		p = PanedWindow(this, orient=VERTICAL)

		# Cree la zone de calcul
		screen = Frame(p, background='white')

		# Textarea ?
		this.Input = text = Text(screen, font=this.CommandFont, height=this.core.HISTORY_LEN + 1)

		scroll = Scrollbar(screen, orient="vertical", command=text.yview)
		text.configure(yscrollcommand=scroll.set)

		# Packing
		text.pack(side=RIGHT, fill=Y)
		scroll.pack(side=LEFT, fill=Y)

		"""
		# The differents parts of the screen
		this.History = Label(screen,text="",background="white")
		this.Input = Label(screen,text="",background="white")

		this.History.pack(side=TOP, expand=Y, fill=BOTH)
		this.Input.pack(side=BOTTOM, expand=Y, fill=BOTH)
		"""

		# Create the button clear and clear all
		clearButtons = Frame(this, borderwidth=2, relief=GROOVE)

		# Actual clear buttons
		Button(clearButtons, font=this.ButtonFont, text="Effacer",command=lambda: this.refreshInput(this.core.clear)).pack(side=LEFT, expand=Y, fill=BOTH)

		Button(clearButtons, font=this.ButtonFont, text="Reset",command=lambda: this.refreshInput(this.core.reset)).pack(side=RIGHT, expand=Y, fill=BOTH)

		Button(clearButtons, font=this.ButtonFont, text="Tout effacer",command=lambda: this.refreshInput(this.core.clearAll)).pack(side=RIGHT, expand=Y, fill=BOTH)

		# Create the keyboard
		keyboard = [
			"789 ()",
			"456 +-",
			"123 */",
			" 0.   "
		]

		# Layout
		height, width = len(keyboard), len(keyboard[0])
		keyboardButtons = Frame(this, borderwidth=2, relief=GROOVE)

		# Grid config for responsive design
		for row in range(height):
			Grid.rowconfigure(keyboardButtons, row, weight=1)
		for column in range(width):
			Grid.columnconfigure(keyboardButtons, column, weight=1)

		# Creates the buttons
		for row in range(height):
			for column in range(width):
				label = keyboard[row][column]
				if label == " ": continue

				# LOL
				command = (lambda x: (lambda: this.sendInput(x)))(label)

				Button(keyboardButtons, font=this.ButtonFont, text=label, borderwidth=1, command=command).grid(row=row, column=column, sticky=N+S+E+W)

		# '=' button
		Button(keyboardButtons, font=this.ButtonFont, text="=", borderwidth=1, command=this.evaluate).grid(row=row, column=column, sticky=N+S+E+W)

		# Display
		p.add(screen)
		p.add(clearButtons)
		p.add(keyboardButtons)
		p.pack(side=TOP, expand=Y, fill=BOTH, pady=5, padx=5)

	# Triggered when a key is pressed
	def keyPressed(this, event):
		sym = event.keysym.lower()
		if not this.action(sym):
			this.sendInput(event.char)

	# Try to trigger an action
	def action(this, action):
		if action not in this.Actions.keys():
			return False
		else: this.Actions[action]()

		return True

	# Send the input to the Core
	def sendInput(this, char):
		this.core.press(char)
		this.refreshInput()

	# Write some text in the input field
	def setScreenInput(this, txt):
		this.Input.delete("1.0", END)
		this.Input.insert(END, txt)
		this.Input.see(END)

	# Evaluate the current expression
	def evaluate(this):
		this.setScreenInput("PROCESSING...")
		result = this.core.evalInput()

		# Re-use the result for next input
		if result is not None:
			this.core.input = str(result)

		this.refreshInput()

	# Takes a function and optional parameters, then refresh the display
	def refreshInput(this, func=(lambda *args: None), *args):
		func(*args)

		# Generate history
		history = "\n".join(line for line in this.core.history)

		this.setScreenInput("%s\n:> %s" % (history, this.core.input))
