from serialCommunication import Pump
from cameraControl import Video
from tkinter import Toplevel
from tkinter import *
import time
import os

#This class creates the UI associated with the Time as well as realtime control of the experiment
class Timer:
	def __init__(self,pump,rate_vol_pairs,times,master,units):
		
		self.root = Toplevel(master)
		#Check file path and make directories
		self.path = "C:\\Users\\dkhlab\\Documents\\Experiments"+"\\"+time.asctime().replace(":","-")
		
		self.pump = pump
		self.units = units
		self.times = times
		self.rate_vol_pairs =rate_vol_pairs
		self.pump.sendRun(self.rate_vol_pairs,units)
		self.root.geometry("400x200")
		self.start_time = time.time()
		self.on = True
		self.elapsed_time = 0 
		self.root
		self.pause_time = 0
		self.resume_time = None
		self.m = 0
		self.s = 0
		self.count = 0       
		self.label = Label(self.root,text="", font=("Helvetica 35 bold"))
		q=Button(self.root , text='Close Window', command=self.root.destroy)
		pb=Button(self.root , text='Pause Experiment', command=self.Pause)
		rb = Button(self.root , text='Resume Experiment', command=self.Resume)
		self.label.place(x=160,y=10)
		pb.place(x=25,y=100)
		rb.place(x=150,y=100)
		q.place(x=300,y=100)
		os.mkdir(self.path)
		self.vid = Video(self.path)
		self.Update()
		self.root.mainloop()
	
	#Updates the displayed timer
	def Update(self,timePaused=0):
		
		if self.on:
			self.elapsed_time =  time.time() - self.start_time - timePaused
			t = self.elapsed_time
			self.m = int(t/60)
			self.s = round(t%60)
			if round(t) in self.times:
				#takePic(self.path,self.count)
				self.count += 1
			if self.s <10:
				txt = f"{self.m}:0{self.s}"
			else:
				txt = f"{self.m}:{self.s}"
			self.label.configure(text=txt)
			self.root.after(1000,self.Update)
	
	#Pauses Timer
	def Pause(self):
		self.on = False
		self.pause_time = time.time()
		self.pump.Pause()
		self.vid.pause()
	#Resumes Timer
	def Resume(self):
		
		if self.on is False:
			self.on = True
			timePaused = time.time()- self.pause_time
			self.Update(timePaused)
			self.pump.Resume()
			self.vid.play()

#Starts a run of the experiment and creates an associated timer and video object
def Run(pump,rate_vol_pairs,times,master,units):
	timer = Timer(pump,rate_vol_pairs,times,master,units)
	timer.vid.play()
