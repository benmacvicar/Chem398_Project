import numpy as np
import cv2

#The Image class takes an image and counts the number of cells in it
class Image:
		
	def __init__(self, im, rate_time_pairs,mina,maxa,minh):
		self.im = im
		self.mina = mina
		self.maxa = maxa
		print(minh)
		raw_image = im[1]
		grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
		blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
		canny_image = cv2.Canny(blurred_image, minh[0], minh[1])
		dilate_image = cv2.dilate(canny_image, kernel, iterations=1)
		eroded_image = cv2.erode(dilate_image, kernel, iterations=1)

		contours = cv2.findContours(eroded_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		self.raw_image = raw_image
		self.contours = contours[0] 
		self.final_image = raw_image
		self.numCells = 0
		self.total_area = 0
		self.centroids = list()
	
	#draws the dectected cells
	def showContours(self,min_area=15,max_area=100):
		
		temp_image = self.final_image
		cents = list()
		for c in self.contours:
			
			

			if cv2.contourArea(c) > self.mina and cv2.contourArea(c)< self.maxa:
				hull = cv2.convexHull(c)
				cv2.drawContours(temp_image,[hull],-1,(0,0,255),1)
				

		

		height, width, depth = temp_image.shape
		imgScale = 1/1000
		#newX,newY = temp_image.shape[1]*imgScale, temp_image.shape[0]*imgScale
		newX,newY = 900, 900

		newimg = cv2.resize(temp_image,(int(newX),int(newY)))
		num =self.numCells 
		cv2.imshow(f"{num} cells found",newimg)
		cv2.waitKey(0)
		cv2.destroyAllWindows() 
	
	#Counts the number of detected cells	
	def count(self,min_area=15,max_area=100):
		num = 0
		total_area = 0
		temp_image = self.final_image
		for c in self.contours:

			if cv2.contourArea(c) > self.mina and cv2.contourArea(c)< self.maxa:
				M = cv2.moments(c)
				num = num + 1
				total_area = total_area + cv2.contourArea(c)
				cx = int(M['m10']/M['m00'])
				cy = int(M['m01']/M['m00'])
				self.centroids.append((cx,cy))

		self.numCells = num
		self.total_area = total_area
		return num



