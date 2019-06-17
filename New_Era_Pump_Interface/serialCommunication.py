import serial
from tkinter import Tk
from tkinter import simpledialog
from tkinter import messagebox

def getPort():
	root = Tk()
	root.withdraw()
	num = simpledialog.askinteger("Input", "What port number is the pump connected to (default is 4)",parent = root)
	return num,root

def destroyPrompt(root):
	root.destroy

class Pump:
	
	def __init__(self, portNumber):
		
		self.port = "COM%d" % portNumber
		try:
			ser = serial.Serial(self.port, 9600, timeout = .5)
		except:
			self.status = False
		else:
			self.ser = ser
			self.status = ser.isOpen()



	def checkConnection(self):
		return self.status

	def errorMessage(self):
		root = Tk()
		root.withdraw()
		messagebox.showerror("Error", "Unable to connect to device, check port number in device mangager and try again.")
		
	def sendRun(self,rate_vol_pairs):
		i = 1
		self.ser.write('RESET\x0D')
		for pair in rate_vol_pairs:
			rate = rate_vol_pairs[0]
			vol = rate_vol_pairs[1]
			fun_rat = 'FUN RAT\x0D'
			phase = 'PHN %d\x0D' % i
			rate_cmd = 'RAT %d MM\x0D' % rate
			vol_cmd = 'VOL %d MM\x0D' % vol
			self.ser.write(phase.encode())
			self.ser.write(fun_rat.encode())
			self.ser.write(rate.encode())
			self.ser.write(vol.encode())
			i = i+1
		self.ser.write('RUN\x0D')

	def Pause(self):
		self.ser.write('STP\x0D')

	def Resume(self):
		self.ser.write('RUN\x0D')
