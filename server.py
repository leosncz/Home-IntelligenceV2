# Author: @leosncz
import http.server
import socketserver

from webcam import webcam
from threading import *
from datetime import datetime
from objectRecognition import objectRecognition
from speechRecognition import speechRecognition
import signal
import sys
import random

import config

def signal_handler(sig, frame):
	print('Home-IntelligenceV2 is exiting...')
	sys.exit(0)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	video_status = 'NO'
	audio_input_status = 'NO'
	audio_output_status = 'NO'
	def do_GET(self):
		if "." in self.path:
			return http.server.SimpleHTTPRequestHandler.do_GET(self)

		date = datetime.now()
		# Actual content
		html = '<!doctype html><html><head><link rel="stylesheet" href="bootstrap-3.4.1-dist/css/bootstrap.min.css"></head><body>'
		html = html + '<nav class="navbar navbar-light bg-light"><span class="navbar-brand mb-0 h1">Home-IntelligenceV2</span></nav>'
		html = html + 'Hey <b>you</b>, the <i>Home-IntelligenceV2</i> is running.</br>'
		html = html + 'It is ' + str(date) + '</br>'
		if (self.audio_output_status == 'OK' and self.audio_input_status == 'OK' and self.video_status == 'OK'):
			html = html + '<div class="card" style="width: 18rem;"><img class="card-img-top" src="camCaptureInterpretation.png?'+str(random.randint(1,5))+'" alt="Card image cap"><div class="card-body"><p class="card-text">This is what HIV2 sees</p></div></div>'
		
		if self.audio_output_status == 'OK':
			html = html + '<p><b>audio output </b> <span style="color: green;">'+self.audio_output_status+'</span></p>'
		else:
			html = html + '<p><b>audio output </b> <span style="color: red;">'+self.audio_output_status+'</span></p>'

		if self.audio_input_status == 'OK':
			html = html + '<p><b>audio input </b> <span style="color: green;">'+self.audio_input_status+'</span></p>'
		else:
			html = html + '<p><b>audio input </b> <span style="color: red;">'+self.audio_input_status+'</span></p>'

		if self.video_status == 'OK':
			html = html + '<p><b>video </b> <span style="color: green;">'+self.video_status+'</span></p>'
		else:
			html = html + '<p><b>video </b> <span style="color: red;">'+self.video_status+'</span></p>'

		if (self.audio_output_status != 'OK' or self.audio_input_status != 'OK' or self.video_status != 'OK'):
			html = html + '<p style="color: orange;">You must fix these issues before using Home-IntelligenceV2 - Check <a href="https://github.com/leosncz/Home-IntelligenceV2">this link.</a></p>'
		
		html = html + '</br><p style="text-decoration: underline;"><b>Configuration (you can edit <i>config.py</i> file):</b> </p>'
		html = html + '<p><b>Separator words:</b> ' + str(config.separator_words) + '</p><p><b>Orders: </b>' + str(config.orders) + '</p>'
		html = html + '<p><b>Cam interval: </b>' + str(config.cam_interval) + ' seconds</p>'
		html = html + '</body></html>'
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes(html, "utf8"))
		return

class server:
	PORT = 8000
	handler = 0

	def __init__(self, port):
		self.handler = MyHttpRequestHandler
		self.PORT = port
		
		# SYS CHECK
			# video check
		webcam_test = webcam()
		self.handler.video_status = webcam_test.isCameraAlive()
			# audio_input check TODO
		self.handler.audio_input_status = 'OK'
			# audio_output check TODO
		self.handler.audio_output_status = 'OK'

	def start(self):
		signal.signal(signal.SIGINT, signal_handler)
		my_server = socketserver.TCPServer(("", self.PORT), self.handler)
		print("Home-IntelligenceV2 is running at localhost:" + str(self.PORT))

		thread = Thread(target = self.serve_http, args = (my_server,))
		thread.setDaemon(True)
		thread.start()
		
		self.mainLoop()

	# Main app loop
	def mainLoop(self):
		userWebcam = webcam()
		objReco = objectRecognition()
		speechReco = speechRecognition()
		speechReco.start_thread()
		i = datetime.now()

		while 0 == 0: # Main loop
			# CV
			if speechReco.hasStarted() == "OK" and (datetime.now() - i).total_seconds() >= config.cam_interval and (self.handler.audio_output_status == 'OK' and self.handler.audio_input_status == 'OK' and self.handler.video_status == 'OK'): # Capture webcam every 5 seconds
				userWebcam.capture()
				recognizedObjects = objReco.recognition()
				i = datetime.now()
			# Speech recognition
			sentence = speechReco.getSpeechToText()
			if sentence != "no stt available":
				print(sentence)
			
	def serve_http(self, httpd):
		# Serve http forever
		httpd.serve_forever()
			
