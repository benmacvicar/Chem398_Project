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
			ser = serial.Serial(self.port, 9600)
		except:
			self.status = False
		else:
			self.ser = ser
			self.ser.write()
			self.status = ser.isOpen()
			#maybe change baud rate here??

	def sendCmd(self,cmd):

		self.ser.write(cmd.encode)
		output = self.ser.readline()

	def checkConnection(self):
		return self.status

	def errorMessage(self):
		root = Tk()
		root.withdraw()
		messagebox.showerror("Error", "Unable to connect to device, check port number in device mangager and try again.")
		
	def sendRun(self,rate_vol_pairs):
		i = 1
		self.ser.write('RESET\x0D'.encode())
		for pair in rate_vol_pairs:
			rate = rate_vol_pairs[0]
			vol = rate_vol_pairs[1]
			fun_rat = 'FUN RAT\x0D'
			phase = f'PHN {i}\x0D'
			rate_cmd = f'RAT {rate} MM\x0D'
			vol_cmd = f'VOL{vol}\x0D'
			self.sendCmd(phase)
			self.sendCmd(fun_rat)
			self.sendCmd(rate_cmd)
			self.sendCmd('VOLMM\x0D')
			self.sendCmd(vol_cmd)
			self.sendCmd('DIR WDR\x0D')
			i = i+1
		self.sendCmd('RUN\x0D')

	def Pause(self):
		self.sendCmd('STP\x0D')

	def Resume(self):
		self.sendCmd('RUN\x0D')
