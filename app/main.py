from fastapi import FastAPI
from app.routes.analytics import router as analytics_router
from app.database.db import Base, engine
from app.models import db_models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(analytics_router)


@app.get("/")
def home():
    return {
        "message": "Spotify Analytics Backend is running"
    }