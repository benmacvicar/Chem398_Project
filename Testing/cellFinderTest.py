import numpy as np
import cv2  

from tkinter.filedialog import askopenfilename
filename = askopenfilename()
vid = cv2.VideoCapture(filename)
vid.set(1,1)
temp = vid.read()
raw_image = temp[1]

grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
canny_image = cv2.Canny(blurred_image, 75, 100)
dilate_image = cv2.dilate(canny_image, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)




cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

final_image = cv2.cvtColor(erode_image, cv2.COLOR_GRAY2BGR)
num = 0
min_area = 50
max_area = 200
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area: 
		hull = cv2.convexHull(c)
		cv2.drawContours(final_image,[hull],-1,(255,0,0),1)
		num = num + 1

print(num)
numpy_horizontal = np.hstack((raw_image, final_image))
newimg = cv2.resize(numpy_horizontal,(1200,800))
cv2.imwrite("C:\\Users\\Ben\\Desktop\\Test Images\\blurred.png",blurred_image)
cv2.imwrite("C:\\Users\\Ben\\Desktop\\Test Images\\final.png",numpy_horizontal)
cv2.imwrite("C:\\Users\\Ben\\Desktop\\Test Images\\erode.png",erode_image)
cv2.imwrite("C:\\Users\\Ben\\Desktop\\Test Images\\canny.png",canny_image)
cv2.imwrite("C:\\Users\\Ben\\Desktop\\Test Images\\dilate.png",dilate_image)
cv2.imshow(f"{num} cells found",newimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 