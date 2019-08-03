import numpy as np 
import cv2
from imageAnalysis import Image

#Gets the frames in the video associated to the end of each flowrate
#Input: File name of video
#Input: List of tuples of flow rates and end times
#Returns a list of each frame

def getFrames(filename,rate_time_pairs):

	
	vid = cv2.VideoCapture(filename)
	frames= list()
	fps = vid.get(cv2.CAP_PROP_FPS)
	frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
	for item in rate_time_pairs:
		frames.append(int(item[1]*fps))
	
	
	if (vid.isOpened()== False):  
		print("Error opening video  file") 
	pics = list()
	frame_num = 0
	for f in frames:
		vid.set(1,f)
		pic = vid.read()
		pics.append(pic)
	return pics

#Analyzes a list of frames returned by getFrames
#prints the number of cells counted in each frames
#prints the number of cells that are the same between each frame
#Input: list of images
#Input: List of tuples of flow rates and end times
def analizeFrames(pics,rate_time_pairs):
	cells = list()
	intersections = list()
	cents = list()
	for pic in pics:
		im = Image(pic,rate_time_pairs)
		num = im.count()
		cells.append(num)
		cents.append(im.centroids)
	initial = cents[0]
	print("cells found per time step:")
	print(cells)
	for cent in cents:
		num = 0
		for p1 in cent:
			for p2 in initial:
				if dist(p1,p2) < 2.5:
					num = num +1
		intersections.append(num)
	print("cells tracked between frames:")
	print(intersections)

#returns euclidean distance between two points p1 and p2
def dist(p1,p2):
	 return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#excecutes getFrames then analyzeFrames
def run(filename,rate_time_pairs):

	pics = getFrames(filename,rate_time_pairs)
	analizeFrames(pics,rate_time_pairs)
	return pics

#Shows the image with detected cells outlined
def showPics(pic):
	im = Image(pic)
	im.showContours()







