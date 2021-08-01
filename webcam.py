# Author: @leosncz
from cv2 import *

class webcam:
	def capture(self):
		cam = VideoCapture(0)   # 0 -> index of camera
		s, img = cam.read()
		if s:    # frame captured without any errors
    			imwrite("camCapture.jpg",img) #save image