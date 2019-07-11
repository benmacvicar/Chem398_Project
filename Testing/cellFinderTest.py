import numpy as np
import cv2  

from tkinter.filedialog import askopenfilename
filename = askopenfilename()

raw_image = cv2.imread(filename)

grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

#65 worked really well
canny_image = cv2.Canny(blurred_image, 75, 100)
dilate_image = cv2.dilate(canny_image, None, iterations=1)
erode_image = cv2.erode(dilate_image, None, iterations=1)

cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] 
	
final_image = cv2.cvtColor(erode_image, cv2.COLOR_GRAY2BGR)
num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
		hull = cv2.convexHull(c)
		cv2.drawContours(final_image,[hull],-1,(255,14,0),1)
		num = num + 1

numpy_horizontal = np.hstack((raw_image, final_image))
cv2.imshow(f"{num} cells found",numpy_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows() 