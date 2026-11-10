from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Azure FastAPI Demo",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "FastAPI Demo - ItsmePJ - new version 543"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello {name}, welcome to Azure!"
    }