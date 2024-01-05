from http.server import BaseHTTPRequestHandler
from os.path import join
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("hola desde serverless GET".encode('utf-8'))
        return
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("hola desde POST".encode('utf-8'))
        return
    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("hola desde PUT".encode('utf-8'))
        return
    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("hola desde DELETE".encode('utf-8'))
        return