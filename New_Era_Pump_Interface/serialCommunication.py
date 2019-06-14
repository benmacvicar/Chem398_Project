import serial
from tkinter import Tk
from tkinter import simpledialog

def getPort():
	num = simpledialog.askinteger("Input", "What port number is the pump connected to (default is 4)",parent = Tk())
	return num

class Pump:
	
	def __init__(self, portNumber):
		
		self.port = "COM%d" % portNumber

num = simpledialog.askinteger("Input", "What port number is the pump connected to (default is 4)",parent = Tk())
test = "COM%d" % num

print(test)
