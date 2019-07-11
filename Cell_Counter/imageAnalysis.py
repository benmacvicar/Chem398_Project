import numpy as np
import cv2


class Image:
		
	def __init__(self, filename, rate_time_pairs = None)
		self.filename = filename
		raw_image = cv2.imread(filename)
		grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
		blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
		self.raw_image = raw_image
		#65 worked really well
		canny_image = cv2.Canny(blurred_image, 75, 100)
		dilated_image = cv2.dilate(canny_image, None, iterations=1)
		eroded_image = cv2.erode(dilated_image, None, iterations=1)

		contours = cv2.findContours(eroded_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		self.contours = contours[0] 
		self.final_image = cv2.cvtColor(raw_image, cv2.COLOR_GRAY2BGR)
		self.numCells = 0
		self.total_area = 0

	def showContours(self, min_area,max_area):
		
		temp_image = self.final_image
		for c in cnts:

			if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
				hull = cv2.convexHull(c)
				cv2.drawContours(temp_image,[hull],-1,(255,14,0),1)
			
		display = np.hstack((self.raw_image, temp_image))
		cv2.imshow(f"{num} cells found",display)
		cv2.waitKey(0)
		cv2.destroyAllWindows() 
		
	def count(self,min_area=15,max_area=100):
		num = 0
		total_area = 0
		temp_image = self.final_image
		for c in cnts:

			if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
				
				num = num + 1
				total_area = total_area + cv2.contourArea(c)
		self.numCells = num
		self.total_area = total_area