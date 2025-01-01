from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/api")
async def read_root():
    return {
        "message": "Hello from Vercel!",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/{path:path}")
async def read_path(path: str):
    return {
        "message": "Hello from Vercel!",
        "path": path,
        "timestamp": datetime.now().isoformat()
    } 