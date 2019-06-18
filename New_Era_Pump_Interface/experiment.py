from serialCommunication import Pump
from cameraControl import takePic
from tkinter import Toplevel
from tkinter import *
import time
import os

class Timer:
	def __init__(self,pump,rate_vol_pairs,times,master):
        self.root = Toplevel(master)
        #Check file path and make directories
        self.path = "C:\\Users\\dkhlab\\Documents\\Experiments"+"\\"+time.asctime().replace(":","-")
        self.pump = pump
        self.pump.sendRun(rate_vol_pairs)
        self.root.geometry("400x200")
        self.start_time = time.time()
        self.on = True
        self.elapsed_time = 0 
        self.root
        self.pause_time = 0
        self.resume_time = None
        self.m = 0
        self.s = 0       
        self.label = Label(self.root,text="", font=("Helvetica 35 bold"))
        q=Button(self.root , text='Close Window', command=self.root.destroy)
        pb=Button(self.root , text='Pause Experiment', command=self.Pause)
        rb = Button(self.root , text='Resume Experiment', command=self.Resume)
        self.label.place(x=160,y=10)
        pb.place(x=25,y=100)
        rb.place(x=150,y=100)
        q.place(x=300,y=100)
        os.mkdir(self.path)
        self.Update()
        self.root.mainloop()
    def Update(self,timePaused=0):
		
        if self.on:
			self.elapsed_time =  time.time() - self.start_time - timePaused
			t = self.elapsed_time
			self.m = int(t/60)
			self.s = int(t%60)
			if self.s <10:
				txt = f"{self.m}:0{self.s}"
			else:
				txt = f"{self.m}:{self.s}"
			self.label.configure(text=txt)
			self.root.after(1000,self.Update)

	def Pause(self):
		self.on = False
		self.pause_time = time.time()
		self.pump.Pause()
		takePic()
	def Resume(self):
		
		if self.on is False:
			self.on = True
			timePaused = time.time()- self.pause_time
			self.Update(timePaused)
			self.pump.Resume()
def Run(pump,rate_vol_pairs,times,master):

	timer = Timer(pump,rate_vol_pairs,times,master)
