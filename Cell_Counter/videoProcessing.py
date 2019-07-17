import numpy as np 
import cv2
from imageAnalysis import Image

def getFrames(filename,rate_time_pairs):

	
	vid = cv2.VideoCapture(filename)
	frames= list()
	fps = vid.get(cv2.CAP_PROP_FPS)
	frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
	for item in rate_time_pairs:
		frames.append(int(item[1]*fps))
	print(frames)
	
	if (vid.isOpened()== False):  
		print("Error opening video  file") 
	pics = list()
	frame_num = 0
	for f in frames:
		vid.set(1,f)
		pic = vid.read()
		pics.append(pic)
		print(f)
	return pics

def analizeFrames(pics,rate_time_pairs):
	cells = list()
	for pic in pics:
		im = Image(pic,rate_time_pairs)
		num = im.count()
		cells.append(num)
	print(cells)

def run(filename,rate_time_pairs):

	pics = getFrames(filename,rate_time_pairs)
	analizeFrames(pics,rate_time_pairs)
	return pics

def showPics(pic):
	im = Image(pic)
	im.showContours()







