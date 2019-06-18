import pygame
import pygame.camera
from pygame.locals import *

def takePic(path,time):
	pygame.camera.init()
	camlist = pygame.camera.list_cameras()
	if camlist:
		cam = pygame.camera.Camera(camlist[0])
		cam.start()
		im = cam.get_image()
		pygame.image.save(img,time+".jpg")
