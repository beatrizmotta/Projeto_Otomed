from http.server import BaseHTTPRequestHandler, HTTPServer
from extract import extract

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = bytes.decode(self.rfile.read(content_len))

        print(len(post_body))


        
server = HTTPServer(('', 8000), handler)
server.serve_forever()