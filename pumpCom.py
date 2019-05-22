from new_era import PumpInterface
from tkinter import *
from tkinter import simpledialog

def portCheck(master):
	
	prompt = Tk()
	response = simpledialog.askinteger("Input","What COM port is the pump connected to? (Check Device Manager):", parent = master)
	return response

def convertToVolumePairs(rate_time_pairs):
	rate_volume_pairs = list()
	for pair in rate_time_pairs:
		vol = pair[0]*pair[1]/60
		rate_volume_pairs.append(pair[0],vol)
	return rate_volume_pairs