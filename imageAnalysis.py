from PIL import Image
from PIL import ImageFilter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog

def getImage():

	filename = askopenfilename()
	im = Image.open(filename).convert('L')
	return im

#threshold 1 = 125
#threshold 2 = 100
#threshold 3 = 75
#ecoli threshold 1 = 225
#ecoli 2 threshold 1 = 175
#ecoli 2 threshold 2 = 170
def getThreshold():
	answer = simpledialog.askinteger("Input", "Threshold:")
	return answer
def monochrome(im,thresh):
	width, height = im.size
	pixels = list()
	points = list()
	pix = im.load()
	for y in range(0,height):
		row = list()
		for x in range(0,width):
			if(pix[x,y]  <1):
				row.append(1)
				points.append((x,height-y))
			if(pix[x,y]>=1 and pix[x,y]<=thresh):
				pix[x,y] = 0
			if(pix[x,y]>=thresh):
				pix[x,y] = 255
			else:
				row.append(0)
		pixels.append(row)
	
	filenameFinal = file_name = asksaveasfilename(confirmoverwrite=False)
	im.save(filenameFinal)

def blur(im):
	im1 = im.filter(ImageFilter.BLUR)
	return im1

def saveIm(im):

	filenameFinal = file_name = asksaveasfilename(confirmoverwrite=False)
	im.save(filenameFinal)

pic = getImage()
#picBlurred = blur(pic)
num = getThreshold()
monochrome(pic,num)
#saveIm(pic)
