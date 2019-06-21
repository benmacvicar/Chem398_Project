import cv2
import sys

def takePic(path,rate):
	cam = cv2.VideoCapture(0)
	print(cam.isOpened())
	a,im = cam.read()

	cv2.imwrite(path +"\\"+f"rate_number_{rate}"+".png",im)

