# -*- coding: utf8 -*-
"""
The calculator's core functions
"""

#from .calcZeroDivision import *
import re

class Core(object):
	"""Core object
	Where all the magic happens.
	"""

	HISTORY_LEN = 6
	FLOAT_PRECISION = 2
	OPERATORS = "+-*/"
	CHARACTERS = "0.123456789()" + OPERATORS

	FORBIDDEN = "|".join([
		r"\+\+",
		r"\-\-",
		r"\*\*",
		r"//",
		r"[+*\/\-]{3,}",
	])

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
			new = this.input + char

			# If there is an invalid format, do not accept it
			regInvalid = re.compile(this.FORBIDDEN)
			if re.search(regInvalid, new) is None:

				# If the expression is ready for evaluation, do it
				if this.readyForEval(new) is not None:
					this.evalInput()
					if this.input != "": this.input += char

				# If the expression is not ready, keep writing
				else:
					this.input = new


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

	# WIP
	def readyForEval(this, expr):
		"""Checks if the input has to be evaluated
		"""
		nb = r"[+-]?[\d.]+"
		regLow = re.compile(r"(%s)[+*\/\-](%s)[+\-]$" % (nb, nb))
		#regHigh = re.compile(r"(%s)[*\/](%s)[+*\/\-]$" % (nb, nb))

		return regLow.search(expr) #or regHigh.search(expr)

	# Evaluate the input:
	def evalInput(this):
		"""Tries to evaluate the current input, and then clears it.
		"""
		result = this.evalExpression(this.input)
		this.clearAll()

		if result is not None and result != 0:
			this.input = str(result)
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
			#ZeroDivision.Exception(10)
		except: # Lets say the syntax is alwways at fault
			error = "SYNTAX ERROR"


		# If we got a result
		if result is not None:

			# Removes decimal when not necessary
			intres = int(result)
			if intres == result:
				result = intres

			this.addToHistory("%s = %s" % (expr, result))

		# An error has occured
		else:
			this.addToHistory("%s > %s" % (expr, error))

		return result
