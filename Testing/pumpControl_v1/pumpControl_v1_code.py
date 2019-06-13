import numpy as np 	
from tkinter import *
from tkinter import simpledialog
import matplotlib 
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

master = Tk()
master.wm_title("Pump Application")
answer = simpledialog.askinteger("Input", "How many different flow rates in the experiment?",
                                parent=master)
inputs = list()

def show():
	volume = float(volumeInput.get())
	rate_time_pairs=list()
	volumes = list()

	for item in inputs:
		print(volume)
		print(item[0].get())
		flowRate = float(item[0].get())
		time = float(item[1].get()) 
		rate_time_pairs.append((flowRate,time))
		volumes.append(flowRate*time/60)
	
	result = check(volume,volumes)
	graph(result,rate_time_pairs)

def check(vol,vols):

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

def graph(num,rt):
	diff = num[1]
	t = 0
	if num[0] == 0:
		msg = "Info: The total volume will be used."
	elif num[0] ==1:
		msg = "Info: There will be %dml left over after the run."%diff
	elif num[0] ==2:
		msg = "Error: The required volume exceeds the available volume by %dml"%diff
	
	gr = Tk()
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
	B2 = Button(gr, text="Quit", command = gr.destroy)
	B2.pack()
	gr.mainloop()

if answer is not None:
	num = answer
	
	Label(master, text = "Total Experiment Volume (ml):").grid(row=0,column=0)
	volumeInput = Entry(master)
	volumeInput.grid(row=0,column=1)
	for i in range(num):
		n=i+1
		Label(master, text="Flow Rate %d (ml/min):" % n).grid(row = 2*i+1,column=0)
		Label(master, text="Length (s):").grid(row = 2*i+1,column=2)

		e1 = Entry(master)
		e2 = Entry(master)

		e1.grid(row=2*i+1, column=1)
		e2.grid(row=2*i+1, column=3)
		inputs.append((e1,e2))
	q=Button(master, text='Quit', command=master.destroy)
	s=Button(master, text='Graph', command=show)

	q.grid(row=2*num+2, column=0, sticky=W, pady=4)
	s.grid(row=2*num+2, column=1, sticky=W, pady=4)

	mainloop()
	
else:
    print("Error: Required")

