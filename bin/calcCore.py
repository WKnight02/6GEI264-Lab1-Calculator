# -*- coding: utf8 -*-
"""
The calculator's core functions
"""

class Core:

	HISTORY_LEN = 10
	FLOAT_PRECISION = 2
	CHARACTERS = "0.123456789+-*/()"

	# Object's initialization
	def __init__(this):
		print("Core")

		this.input = ""
		this.history = []

	# Add character to input
	def press(this, char):
		if char in this.CHARACTERS:
			this.input += char

	# Clear the whole input
	def clearAll(this):
		this.input = ""

	# Clear character by character
	def clear(this):
		if len(this.input) > 0:
			this.input = this.input[:-1]

	# Adds an entry to the history
	def addToHistory(this, expr):
		this.history.append(expr)
		this.history = this.history[-this.HISTORY_LEN:]

	# Evaluate the input:
	def evalInput(this):
		result = this.evalExpression(this.input)
		this.clearAll()
		return result

	# Evaluate some expression
	def evalExpression(this, expr):

		# Evaluating the expr
		try: result = round(eval(expr), this.FLOAT_PRECISION)
		except: return None

		# End of story
		this.addToHistory("%s = %s" % (expr, result))
		return result
