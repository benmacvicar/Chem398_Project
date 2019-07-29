import numpy as np
import cv2  

from tkinter.filedialog import askopenfilename
filename = askopenfilename()
vid = cv2.VideoCapture(filename)
vid.set(1,1)
temp = vid.read()
raw_image = temp[1]
results = list()

#test 1
grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
canny_image = cv2.Canny(blurred_image, 75, 100)

#65 worked really well
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_image = cv2.dilate(canny_image, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)
cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

final_image = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)
num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
		
		num = num + 1

results.append(num)

#test 2 no Canny
grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
#canny_image = cv2.Canny(blurred_image, 75, 100)

#65 worked really well
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_image = cv2.dilate(blurred_image, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)
cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

final_image = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)
num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:

		num = num + 1

results.append(num)


#test 3
grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
#blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
canny_image = cv2.Canny(grayscale_image, 75, 100)

#65 worked really well
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_image = cv2.dilate(canny_image, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)
cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

final_image = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)
num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
		
		num = num + 1
results.append(num)

#test 4
ggrayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
canny_image = cv2.Canny(blurred_image, 75, 100)

#65 worked really well
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_image = cv2.dilate(canny_image, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)
cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

final_image = cv2.cvtColor(canny_image, cv2.COLOR_GRAY2BGR)
num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
		
		num = num + 1

results.append(num)

#test 5
grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)


#65 worked really well
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_image = cv2.dilate(blurred_image, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)
canny_image = cv2.Canny(erode_image, 75, 100)
cnts = cv2.findContours(erode_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
		
		num = num + 1

results.append(num)


#test 6
grayscale_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)


#65 worked really well
canny_image1 = cv2.Canny(blurred_image, 75, 100)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dilate_image = cv2.dilate(canny_image1, kernel, iterations=1)
erode_image = cv2.erode(dilate_image, kernel, iterations=1)
canny_image = cv2.Canny(erode_image, 75, 100)
cnts = cv2.findContours(canny_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] 

num = 0
min_area = 15
max_area = 100
for c in cnts:

	if cv2.contourArea(c) > min_area and cv2.contourArea(c)< max_area	:
		
		num = num + 1

results.append(num)
print(results)

