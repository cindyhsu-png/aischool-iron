import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get('PORT', 8080))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', PORT), handler)
print(f'Server running on port {PORT}')
httpd.serve_forever()
