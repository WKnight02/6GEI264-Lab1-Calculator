"""
The calculator's interface
"""
import tkinter as tk
from tkinter import *

class Interface(tk.Tk):

	def __init__(this):
		super().__init__()
		print("Interface")
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
		#this.button1 = tk.Button(this, text="1", command=this.say_hi, width=10, height=10)
		#this.button2 = tk.Button(this, text="2", command=this.destroy , width=10, height=10)
		#this.button3 = tk.Button(this, text="3",  width=10, height=10)
		#this.button4 = tk.Button(this, text="4",  width=10, height=10)
		#this.button5 = tk.Button(this, text="5",  width=10, height=10)
		#this.button6 = tk.Button(this, text="6",  width=10, height=10)
		#this.button1.pack()
		#this.button2.pack()
		#this.button3.pack()
		#this.button4.pack()
		#this.button5.pack()
		#this.button6.pack()
	
	def say_hi(self):
		print("hi there, everyone!")
	


		

		
	