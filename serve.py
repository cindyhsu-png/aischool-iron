import http.server
import os
os.chdir('/Users/ironchen/Desktop/AI_school_phaseII')
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', 8080), handler)
print('Server running on port 8080')
httpd.serve_forever()
