# Author: @leosncz
import http.server
import socketserver

from webcam import webcam
from threading import *


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'welcome.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

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
		i = 0
		while 0 == 0:
			if i == 1000:
				userWebcam.capture()
				i = 0
			else:
				i = i + 1
			
	def serve_http(self, httpd):
		# Serve http
		httpd.serve_forever()
			
