import numpy as np
import cv2  
from imageAnalysis import Image 
from tkinter.filedialog import askopenfilename
from gui import GUI
filename = askopenfilename()

ui = GUI(filename)