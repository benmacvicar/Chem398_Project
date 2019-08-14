import numpy as np 	
from tkinter import *
from tkinter import simpledialog
from videoProcessing import run
from videoProcessing import showPics
from tkinter.filedialog import askopenfilename
from imageAnalysis import Image

#This class creates the UI that allows the video file to be analyzed
class GUI:

	def __init__(self,filename):

		self.master = Tk()
		self.master.withdraw()
		self.master.wm_title("Video Analysis")
		self.filename = filename
		answer = simpledialog.askinteger("Input", "How many different flow rates in the experiment?",
	                                parent=self.master)
		self.pics = None
		self.inputs = list()
		self.numSteps = answer
		self.volume = None
		self.volumes = list()
		self.rate_time_pairs = list()
		self.volume_time_pairs = list()
		self.result = None
		self.area_inputs = list()
		self.areas = list ()
		self.times = list()
		self.rate_vol_pairs = list()
		self.hyst_inputs = list()
		self.hyst_vals = list()
		if answer is not None:
			num = answer
		
			Label(self.master, text = "Total Experiment Volume (Optional):").grid(row=0,column=0)
			volumeInput = Entry(self.master)
			self.volumeInput = volumeInput
			volumeInput.grid(row=0,column=1)
			volumeInput.insert(0, "0 ")
			Label(self.master, text="Min Area").grid(row = 0,column=2)
			Label(self.master, text="Max Area").grid(row = 0,column=4)
			e3 = Entry(self.master)
			e3.insert(15, "15 ")
			e4 = Entry(self.master)
			e4.insert(100, "100 ")
			e3.grid(row=0, column=3)
			e4.grid(row=0, column=5)

			Label(self.master, text="Min Hysteresis").grid(row = 0,column=6)
			Label(self.master, text="Max Hysteresis").grid(row = 0,column=8)
			e5 = Entry(self.master)
			e5.insert(15, "75 ")
			e6 = Entry(self.master)
			e6.insert(100, "100 ")
			e5.grid(row=0, column=7)
			e6.grid(row=0, column=9)
			self.hyst_inputs.append(e5)
			self.hyst_inputs.append(e6)
			for i in range(num):
				n=i+1
				Label(self.master, text="Flow Rate %d (Optional):" % n).grid(row = 2*i+1,column=0)
				Label(self.master, text="Time (s)").grid(row = 2*i+1,column=2)

				e1 = Entry(self.master)
				e1.insert(0, "0 ")	 
				e2 = Entry(self.master)
				
				
				show = Button(self.master, text ='Show',command = lambda n=n: self.graph(n)) 
				
				e1.grid(row=2*i+1, column=1)
				e2.grid(row=2*i+1, column=3)
		
				show.grid(row=2*i+1, column=4)
				
				self.inputs.append((e1,e2))
				self.areas.append((e3,e4))
			


			q=Button(self.master, text='Quit Program', command=self.destroyer)
			s=Button(self.master, text='Analyze', command=self.Analyze)
			c = Button(self.master, text='Change File', command=self.changeFilename)
			q.grid(row=2*num+2, column=0, sticky=W, pady=4)
			s.grid(row=2*num+2, column=1, sticky=W, pady=4)
			c.grid(row=2*num+2, column=2, sticky=W, pady=4)
			self.master.deiconify()
			mainloop()
	
	#Stops the program
	def destroyer(self):
		sys.exit()

	#Lets you analyze a different file
	def changeFilename(self):
		self.filename = askopenfilename()

	#Displays the image with found contours
	def graph(self,num):
		
		pic = self.pics[num]
		showPics(pic,self.rate_time_pairs,self.area_inputs[0][0],self.area_inputs[0][1],self.hyst_vals)

	#Implements the image analyis base on the user input
	def Analyze(self):
		volume = float(self.volumeInput.get())
		rate_time_pairs=list()
		rate_time_pairs.append((0.0,0.0))
		run_time = 0
		self.times.append(0)
		self.area_inputs = list()
		for item in self.areas:
			self.area_inputs.append((float(item[0].get()),float(item[1].get())))
		self.hyst_vals = list()
		for item in self.hyst_inputs:
			self.hyst_vals.append(float(item.get()))
		#print(self.hyst_vals)
		for item in self.inputs:
			flowRate = float(item[0].get())
			time = float(item[1].get())
			run_time = run_time + time 
			rate_time_pairs.append((flowRate,time))
			print(rate_time_pairs)

		self.rate_time_pairs = rate_time_pairs
		
		self.pics = run(self.filename,self.rate_time_pairs,self.area_inputs[0][0],self.area_inputs[0][1],self.hyst_vals)


