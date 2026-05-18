from fastapi import FastAPI
from app.routes.analytics import router as analytics_router

app = FastAPI()

app.include_router(analytics_router)



@app.get("/")
def home():
    return {
        "message": "Spotify Analytics Backend is running"
    }

