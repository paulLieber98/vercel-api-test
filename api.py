from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello from Vercel!",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api")
async def api():
    return {
        "message": "Hello from API endpoint!",
        "timestamp": datetime.now().isoformat()
    } 