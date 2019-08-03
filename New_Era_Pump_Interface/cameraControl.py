import sys
import cv2
import numpy as np
 


#This method is for taking images not video, i've kept it for redundancy
#def takePic(path,rate):
#	cam = cv2.VideoCapture(0)
#	print(cam.isOpened())
#	a,im = cam.read()
#	cv2.imwrite(path +"\\"+f"rate_number_{rate}"+".png",im)

#This method handles the creation of the video object and the recording and saving of the video
class Video:
	
	#creates a video file in the specified pth
	def __init__(self,path):

		self.cam = cv2.VideoCapture(0)
		self.frame_width = int(cam.get(3))
		self.frame_height = int(cam.get(4))
		self.out = cv2.VideoWriter(path +"\\"+f"rate_number_{rate}"+".avi",cv2.VideoWriter_fourcc('M','J','P','G'), 10, (self.frame_width,self.frame_height))
		self.playing = False
		self.ret = None
		self.frame = None
	
	#Begins recording from camera
	def play(self):
		self.playing = True
		
		while(self.playing):
			self.ret, self.frame = cap.read()
			if ret == True: 
				out.write(frame)
	
	#Pauses recording
	def pause(self):
		self.playing = False

	#stops recording completely
	def stop(self):
		self.playing = False
		self.cap.release()
		self.out.release()
 
		