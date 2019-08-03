import numpy as np 	
from tkinter import *
from tkinter import simpledialog
import matplotlib 
import matplotlib.pyplot as plt
from experiment import Run
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from serialCommunication import Pump

#The GUI class handles the display of the UI and the input of data by the user
class GUI:


	def __init__(self,pump = None):
		
		self.units = "MM"
		self.units_for_display = 'ml'
		self.master = Tk()
		self.master.withdraw()
		self.master.wm_title("Pump Application")
		answer = simpledialog.askinteger("Input", "How many different flow rates in the experiment?",
	                                parent=self.master)
		self.pump = pump
		self.inputs = list()
		self.numSteps = answer
		self.volume = None
		self.volumes = list()
		self.rate_time_pairs = list()
		self.volume_time_pairs = list()
		self.result = None
		self.run = False
		self.times = list()
		self.rate_vol_pairs = list()
		
		#This loop constructs a number flow rate input boxes as specified by the previous input  
		if answer is not None:
			num = answer
		
			Label(self.master, text = f"Total Experiment Volume (select units->):").grid(row=0,column=0)
			volumeInput = Entry(self.master)
			self.volumeInput = volumeInput
			volumeInput.grid(row=0,column=1)
			mm = Button(self.master, text ="mm",command=self.setMM)
			um = Button(self.master, text = "um", command = self.setUM)
			mm.grid(row=0,column =2)
			um.grid(row = 0, column = 3)

			for i in range(num):
				n=i+1
				Label(self.master, text=f"Flow Rate {n} (units/min):").grid(row = 2*i+1,column=0)
				Label(self.master, text="Length (s):").grid(row = 2*i+1,column=2)

				e1 = Entry(self.master)	 
				e2 = Entry(self.master)

				e1.grid(row=2*i+1, column=1)
				e2.grid(row=2*i+1, column=3)
				self.inputs.append((e1,e2))
			


			q=Button(self.master, text='Quit Program', command=self.destroyer)
			s=Button(self.master, text='Graph', command=self.Show)

			q.grid(row=2*num+2, column=0, sticky=W, pady=4)
			s.grid(row=2*num+2, column=1, sticky=W, pady=4)
			
			self.master.deiconify()
			mainloop()
	
	#Set units to ml
	def setMM(self):
		self.units = 'MM'
		self.units_for_display = 'ml'

	#Set units to ul
	def setUM(self):
		self.units = 'UM'
		self.units_for_display = 'ul'
	
	#quits program and closes pump 
	def destroyer(self):
	
		self.pump.sendCmd('STP\x0D')
		self.pump.sendCmd('STP\x0D')
		self.pump.sendCmd('RESET\x0D')
		self.pump.sendCmd('CLD WDR\x0D')
		self.pump.exit()
		sys.exit()

	#Handles the processing of user input data into arrays of usable formats
	#Then calls the graph method
	def Show(self):
		volume = float(self.volumeInput.get())
		rate_time_pairs=list()
		volume_time_pairs=list()
		volumes = list()
		run_time = 0
		self.times.append(0)
		for item in self.inputs:
			flowRate = float(item[0].get())
			time = float(item[1].get())
			run_time = run_time + time 
			rate_time_pairs.append((flowRate,time))
			volume_time_pairs.append(((flowRate*time/60),time))
			volumes.append(flowRate*time/60)
			self.rate_vol_pairs.append((flowRate,(flowRate*time/60)))
			self.times.append(run_time)

		self.volumes = volumes
		self.volume = volume
		self.rate_time_pairs = rate_time_pairs
		self.volume_time_pairs = volume_time_pairs
		self.result = Check(self.volume,self.volumes)
		print(self.rate_vol_pairs)
		Graph(self)

	#Begins the experiment Run
	def Start(self):
		Run(self.pump,self.rate_vol_pairs,self.times,self.master,self.units)
		

#Compares the volume required by the run profile to the total volume specified
def Check(vol,vols):

	total = 0
	for i in vols:
		total = total + i

	#too big
	if total > vol:
		diff = total - vol
		return (2,diff)

	#spot on
	elif total == vol:
		return (0,0)

	#left over volume
	elif total < vol:
		diff = vol - total
		return (1,diff)

#Creats a graph illustrating the run and provides the UI elements that start the run
def Graph(gui):
	
	num,rt,vt = gui.result,gui.rate_time_pairs, gui.volume_time_pairs
	diff = num[1]
	t = 0
	if num[0] == 0:
		msg = "Info: The total volume will be used."
	elif num[0] ==1:
		msg = f"Info: There will be {diff}{gui.units_for_display} left over after the run."
	elif num[0] ==2:
		msg = f"Error: The required volume exceeds the available volume by {diff}{gui.units_for_display} "
	
	gr = Toplevel(gui.master)
	gr.wm_title("Graph")
	x = list()
	x.append(0)
	y = list()
	y.append(0)
	label = Label(gr,text = msg)
	label.pack(side='top',fill ='x')
	if num[0] == 0 or num[0] == 1:
		for pair in rt:
			t = t+pair[1]
			x.append(t)
			y.append(pair[0])
			
		f = Figure(figsize=(5,5))
		sub = f.add_subplot(111)
		sub.plot(x, y, linestyle='-', drawstyle='steps')
		sub.set_xlabel("Time (s)")
		sub.set_ylabel(f"Flow Rate ({gui.units_for_display}/min)")
		sub.set_xlim([0,t])
		canvas = FigureCanvasTkAgg(f, master=gr)
		canvas.draw()
		canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
		canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
	B2 = Button(gr, text="Close", command = gr.destroy)
	
	#B3 starts timer and runs experiment
	B3 = Button(gr,text = "Run Experiment", command = gui.Start)
	B3.pack()
	B2.pack()
	gr.mainloop()


		

