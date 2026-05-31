from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./spotify_analytics.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

fake_artists = [
    {"artist": "Drake", "streams": 1250},
    {"artist": "Kendrick Lamar", "streams": 980},
    {"artist": "J.Cole", "streams": 875},
]

fake_tracks = [
    {"track": "HUMBLE.", "artist": "Kendrick Lamar", "streams": 420},
    {"track": "Work Out", "artist": "J. Cole", "streams": 390},
    {"track": "God's Plan", "artist": "Drake", "streams": 510},
]

fake_genres = [
    {"genre": "Hip-Hop", "hours_listened": 145},
    {"genre": "R&B", "hours_listened": 72},
    {"genre": "Pop", "hours_listened": 40},
]

fake_summary = {
    "total_hours": 257,
    "favorite_artist": "Drake",
    "favorite_genre": "Hip-Hop",
    "total_tracks_streamed": 1240,
}