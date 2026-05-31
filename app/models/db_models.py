from sqlalchemy import Column, Integer, String
from app.database.db import Base

class ArtistDB(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    artist = Column(String, nullable=False)
    streams = Column(Integer, nullable=False)