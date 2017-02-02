# -*- coding: utf8 -*-
"""
The calculator's core functions
"""

from .calcZeroDivision import *

class Core(object):
	"""Core object
	Where all the magic happens.
	"""

	HISTORY_LEN = 6
	FLOAT_PRECISION = 2
	CHARACTERS = "0.123456789+-*/()"

	# Object's initialization
	def __init__(this):
		this.reset()

	# Reset the calculator
	def reset(this):
		"""Clears both the input and the history.
		"""
		this.input = ""
		this.history = ["" for i in range(this.HISTORY_LEN)]

	# Add character to input
	def press(this, char):
		"""Acts as if you pressed a certain character.
		If it is not a valid char, it will simply do nothing.
		"""
		if char in this.CHARACTERS:
			this.input += char

	# Clears character by character
	def clear(this):
		"""Clears the last character available.
		Does nothing if no input.
		"""
		if len(this.input) > 0:
			this.input = this.input[:-1]

	# Clears the whole input
	def clearAll(this):
		"""Clears the input.
		"""
		this.input = ""

	# Adds an entry to the history
	def addToHistory(this, expr):
		"""Adds an entry to the history, and makes sure it does not grow over the limited value. (Core.HISTORY_LEN)
		"""
		this.history.append(expr)
		this.history = this.history[-this.HISTORY_LEN:]

	# Evaluate the input:
	def evalInput(this):
		"""Tries to evaluate the current input, and then clears it.
		"""
		result = this.evalExpression(this.input)
		this.clearAll()
		return result

	# Evaluate some expression
	def evalExpression(this, expr):
		"""Evals some expression, and adds the result's entry to the history.
		"""

		# If nothing is entered, do nothing
		if expr.strip() == "": return ""

		# Evaluating the expr
		result = None
		try:
			result = round(eval(expr), this.FLOAT_PRECISION)
		except ZeroDivisionError:
			error = "ZERO DIVISION"
			ZeroDivision.Exception(10)
		except: # Lets say the syntax is alwways at fault
			error = "SYNTAX ERROR"


		# End of story
		if result is not None:
			this.addToHistory("%s = %s" % (expr, result))
		else:
			this.addToHistory("%s > %s" % (expr, error))
		return result
