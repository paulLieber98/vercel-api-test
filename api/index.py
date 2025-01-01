from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        response = {
            "message": "Hello from Vercel!",
            "timestamp": datetime.now().isoformat(),
            "path": self.path
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8')) 