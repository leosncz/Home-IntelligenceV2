# Author: @leosncz
import http.server
import socketserver

from webcam import webcam
from threading import *
from datetime import datetime
from objectRecognition import objectRecognition

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if "." in self.path:
			return http.server.SimpleHTTPRequestHandler.do_GET(self)

		date = datetime.now()
		# Actual content
		html = '<!doctype html><html><head><link rel="stylesheet" href="bootstrap-3.4.1-dist/css/bootstrap.min.css"></head><body>'
		html = html + '<nav class="navbar navbar-light bg-light"><span class="navbar-brand mb-0 h1">Home-IntelligenceV2</span></nav>'
		html = html + 'Hey <b>you</b>, the <i>Home-IntelligenceV2</i> is running.</br>'
		html = html + 'It is ' + str(date) + '</br>'

		html = html + '<div class="card" style="width: 18rem;"><img class="card-img-top" src="camCaptureInterpretation.png" alt="Card image cap"><div class="card-body"><p class="card-text">This is what HIV2 sees</p></div></div>'

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

	# Main app loop
	def start(self):
		my_server = socketserver.TCPServer(("", self.PORT), self.handler)
		print("Home-IntelligenceV2 is running at localhost:" + str(self.PORT))

		thread = Thread(target = self.serve_http, args = (my_server,))
		thread.start()
		
		userWebcam = webcam()
		objReco = objectRecognition()
		i = datetime.now()

		while 0 == 0: # Main loop
			if (datetime.now() - i).total_seconds() >= 5: # Capture webcam every 5 seconds
				self.handler.content = ''
				userWebcam.capture()
				recognizedObjects = objReco.recognition()
				i = datetime.now()
			
	def serve_http(self, httpd):
		# Serve http forever
		httpd.serve_forever()
			
