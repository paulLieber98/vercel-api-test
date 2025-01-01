from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from Vercel!",
            "timestamp": datetime.now().isoformat()
        })
    } 