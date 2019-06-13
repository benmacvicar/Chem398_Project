from PIL import Image
from PIL import ImageFilter
from tkinter.filedialog import askopenfilename, asksaveasfilename

def getImage():

	filename = askopenfilename()
	im = Image.open(filename).convert('L')
	return im

def compare(im1):
	w1, h1 = im1.size
	total = w1*h1	
	count1 = 0
	pix = im1.load()
	for y in range(0,h1):
		for x in range(0,w1):
			if(pix[x,y]  > 1):
				count1 +=1

	#result = count1/total
	#return 100*result
	return (count1,total)

im1 = getImage()
im2 = getImage()

start = compare(im1)
end = compare(im2)
#diff = start-end
#result = (start,end, diff/start*100)
p1 =start[0]/start[1]*100
p2 = end[0]/end[1]*100
diff = p1 - p2
print(p1,p2,diff)
print(start,end)
print(start[0],start[1])