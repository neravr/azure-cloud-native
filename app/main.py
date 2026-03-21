from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Cloud Native API", version="1.0.0")

@app.get("/")
def root():
    return {
        "message": "Cloud Native FastAPI on AKS",
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "app": "cloud-native-api",
        "version": "1.0.0",
        "environment": "dev",
        "infrastructure": {
            "cloud": "Azure",
            "orchestration": "AKS",
            "iac": "Terraform"
        }
    }

