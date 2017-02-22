"""
The calculator's interface
"""
from tkinter import *
from tkinter import filedialog
import tkinter.font as font

__all__ = ['Interface']

class Interface(Tk):
	"""Calculator's interface
	On its own, it does only manage buttons and displays.
	The actual logic is in a Core that you must provide while instancing the object.
	"""

	DEFAULTS = {
		"height": 450,
		"width": 350,
	}

	def __init__(this, core=None, **kargs):
		"""You must provide a Core to actually process the inputs in a fashioned way. (see: bin.calcCore)
		"""
		super().__init__()

		this.core = core
		
		this.buttons = {}

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

	# Internal function setting up the components/widgets
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

		# Create the button clear and clear all
		clearButtons = Frame(this, borderwidth=2, relief=GROOVE)

		# Actual clear buttons
		clearButton = Button(clearButtons, font=this.ButtonFont, text="Effacer",command=lambda: this.refreshInput(this.core.clear))
		clearButton.pack(side=LEFT, expand=Y, fill=BOTH)
		this.buttons["backspace"] = clearButton

		resetButton = Button(clearButtons, font=this.ButtonFont, text="Reset",command=lambda: this.refreshInput(this.core.reset))
		resetButton.pack(side=RIGHT, expand=Y, fill=BOTH)

		clearAllButton = Button(clearButtons, font=this.ButtonFont, text="Tout effacer",command=lambda: this.refreshInput(this.core.clearAll))
		clearAllButton.pack(side=RIGHT, expand=Y, fill=BOTH)
		this.buttons["delete"] = clearAllButton

		# Create the keyboard
		keyboard = [
			"789 +-",
			"456 */",
			"123   ",
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

				butt = Button(keyboardButtons, font=this.ButtonFont, text=label, borderwidth=1, command=command)
				butt.grid(row=row, column=column, sticky=N+S+E+W)
				this.buttons[label] = butt

		# IMP button
		Button(keyboardButtons, font=this.ButtonFont, text="IMP", borderwidth=1, command=this.printHistory).grid(row=row, column=column-1, sticky=N+S+E+W)

		# '=' button
		butt = Button(keyboardButtons, font=this.ButtonFont, text="=", borderwidth=1, command=this.evaluate)
		butt.grid(row=row, column=column, sticky=N+S+E+W)
		this.buttons["return"] = butt
		
		# Display
		p.add(screen)
		p.add(clearButtons)
		p.add(keyboardButtons)
		p.pack(side=TOP, expand=Y, fill=BOTH, pady=5, padx=5)

	# Triggered when a key is pressed
	def keyPressed(this, event):
		"""Handles key pressed calls
		If it can perform an action (eval, quit, etc...) it will not send it to the core, otherwise it will.
		"""
		sym = event.keysym.lower()
		
		butt = this.buttons.get(event.char) or this.buttons.get(sym)
		if butt is not None:
			butt.config(relief=SUNKEN)
			this.after(100, lambda: butt.config(relief=RAISED))
		
		if not this.action(sym):
			this.sendInput(event.char)

	# Try to trigger an action
	def action(this, action):
		"""Tries to execute an action that the core does not directly manage.
		"""
		if action not in this.Actions.keys():
			return False
		else: this.Actions[action]()

		return True

	# Send the input to the Core
	def sendInput(this, char):
		"""Sends a character to the core to be processed.
		(such as an inputed char)
		"""
		this.core.pressAutoEval(char)
		this.refreshInput()

	# Write some text in the input field
	def setScreenInput(this, txt):
		"""Sets the screen to some text, clearing what was there.
		"""
		this.Input.delete("1.0", END)
		this.Input.insert(END, txt)
		this.Input.see(END)
		this.update()

	# Evaluate the current expression
	def evaluate(this):
		"""Asks the core to evaluate the current input.
		Then grab the core's return value and tries to display it.
		"""
		this.setScreenInput("PROCESSING...")
		result = this.core.evalInput()

		"""
		# Re-use the result for next input (0 is annoying)
		if result != 0 and result is not None:
				this.core.input = str(result)
		"""

		this.refreshInput()

	# Takes a function and optional parameters, then refresh the display
	def refreshInput(this, func=(lambda *args: None), *args):
		"""Process some stuff with "func" before refreshing the screen, from the core's input and history
		"""
		func(*args)

		# Generate history
		history = "\n".join(line for line in this.core.history)
		this.setScreenInput("%s\n:> %s" % (history, this.core.input))

	# Prints the history
	def printHistory(this):
		"""This function starts the process to print out with some printer the stored inputs.
		"""
		options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = '~/'
		options['initialfile'] = 'Impression.txt'
		options['parent'] = this
		options['title'] = 'Impression'
		filename = filedialog.asksaveasfilename(**options)
		if filename:
			text = open(filename, 'w')
			text.write("\n".join(line for line in this.core.history if line != ""))
			text.close()
