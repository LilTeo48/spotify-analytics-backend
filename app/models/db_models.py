from sqlalchemy import Column, Integer, String
from app.database.db import Base

class ArtistDB(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    artist = Column(String, nullable=False)
    streams = Column(Integer, nullable=False)

class TrackDB(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    track = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    streams = Column(Integer, nullable=False)

class GenreDB(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    genre = Column(String, nullable=False)
    hours_listened = Column(Integer, nullable=False)

class PodcastDB(Base):
    __tablename__ = "podcasts"

    id = Column(Integer, primary_key=True, index=True)
    podcast_name = Column(String, unique=True, index=True)
    host = Column(String)
    category = Column(String)
    episodes = Column(Integer)
    hours_listened = Column(Integer)