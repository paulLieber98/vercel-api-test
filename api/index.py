from http.server import BaseHTTPRequestHandler
from json import dumps

def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": dumps({
            "message": "Hello from Vercel!"
        })
    } 