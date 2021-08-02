# Author: @leosncz
import http.server
import socketserver

from webcam import webcam
from threading import *
from datetime import datetime
from peopleDetection import peopleDetection
from objectRecognition import objectRecognition

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	content = ''
	def do_GET(self):
		if ".jpg" in self.path or ".png" in self.path or ".js" in self.path or ".css" in self.path:
			return http.server.SimpleHTTPRequestHandler.do_GET(self)
		#Auto reload every 5 sec
		#html = '<meta http-equiv="refresh" content="5">'
		# Actual content
		html = 'Hey <b>you</b>, the <i>Home-IntelligenceV2</i> is running.</br>'
		date = datetime.now()
		html = html + 'It is ' + str(date) + '</br>'
		html = html + 'Webcam sample:</br><img src="camCapture.jpg"></img>'
		html = html + self.content
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

	# Main app loop
	def start(self):
		my_server = socketserver.TCPServer(("", self.PORT), self.handler)
		print("Home-IntelligenceV2 is running at localhost:" + str(self.PORT))

		thread = Thread(target = self.serve_http, args = (my_server,))
		thread.start()
		
		userWebcam = webcam()
		peopleDetec = peopleDetection()
		objReco = objectRecognition()
		i = datetime.now()
		while 0 == 0: # Main loop
			if (datetime.now() - i).total_seconds() >= 5: # Capture webcam every 5 seconds
				userWebcam.capture()
				self.handler.content = '</br><b>' + str(peopleDetec.computeHowManyPerson()) + ' </b>people detected in capture.'
				recognizedObjects = objReco.recognition()
				for object in recognizedObjects:
					if object is not None:
						self.handler.content = self.handler.content + '</br>' + object
				i = datetime.now()
			
	def serve_http(self, httpd):
		# Serve http
		httpd.serve_forever()
			
