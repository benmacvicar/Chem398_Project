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


class GUI:


	def __init__(self,pump = None):

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
		if answer is not None:
			num = answer
		
			Label(self.master, text = "Total Experiment Volume (ml):").grid(row=0,column=0)
			volumeInput = Entry(self.master)
			self.volumeInput = volumeInput
			volumeInput.grid(row=0,column=1)
			for i in range(num):
				n=i+1
				Label(self.master, text="Flow Rate %d (ml/min):" % n).grid(row = 2*i+1,column=0)
				Label(self.master, text="Length (s):").grid(row = 2*i+1,column=2)

				e1 = Entry(self.master)	 
				e2 = Entry(self.master)

				e1.grid(row=2*i+1, column=1)
				e2.grid(row=2*i+1, column=3)
				self.inputs.append((e1,e2))
			


			q=Button(self.master, text='Quit Program', command=sys.exit)
			s=Button(self.master, text='Graph', command=self.Show)

			q.grid(row=2*num+2, column=0, sticky=W, pady=4)
			s.grid(row=2*num+2, column=1, sticky=W, pady=4)
			
			self.master.deiconify()
			mainloop()
			
	def Show(self):
		volume = float(self.volumeInput.get())
		rate_time_pairs=list()
		volume_time_pairs=list()
		volumes = list()
		run_time = 0
		self.times.append(0)
		for item in self.inputs:
			print(volume)
			print(item[0].get())	
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
		Graph(self)

	def Start(self):
		Run(self.pump,self.rate_vol_pairs,self.times,self.master)
		master.destroy()


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


def Graph(gui):
	
	num,rt,vt = gui.result,gui.rate_time_pairs, gui.volume_time_pairs
	diff = num[1]
	t = 0
	if num[0] == 0:
		msg = "Info: The total volume will be used."
	elif num[0] ==1:
		msg = "Info: There will be %dml left over after the run."%diff
	elif num[0] ==2:
		msg = "Error: The required volume exceeds the available volume by %dml"%diff
	
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
			print(pair)
			
		f = Figure(figsize=(5,5))
		sub = f.add_subplot(111)
		sub.plot(x, y, linestyle='-', drawstyle='steps')
		sub.set_xlabel("Time (s)")
		sub.set_ylabel("Flow Rate (ml/min)")
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


		

