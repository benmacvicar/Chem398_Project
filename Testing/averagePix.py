from PIL import Image
from PIL import ImageFilter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog

avgs = list()
for i in range(0,10):
	filename = askopenfilename()
	im = Image.open(filename).convert('L')

	width, height = im.size
	dim = width*height
	total = 0
	pix = im.load()
	for y in range(0,height):
		for x in range(0,width):
			total = total + pix[x,y]

	avg = total/dim
	avgs.append(avg)
print(avgs)