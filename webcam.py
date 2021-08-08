# Author: @leosncz
from cv2 import *
import sys
class webcam:
	def capture(self):
		cam = VideoCapture(0) #+cv2.CAP_DSHOW)   # 0 -> index of camera
		s, img = cam.read()
		if s:    # frame captured without any errors
    			imwrite("camCapture.jpg",img) #save image
		else:
			print("Error! No webcam")
			sys.exit()
	def isCameraAlive(self):
		cam = VideoCapture(0) #+cv2.CAP_DSHOW)   # 0 -> index of camera
		s, img = cam.read()
		if s:    # frame captured without any errors
    			return 'OK'
		else:
			return 'NO'