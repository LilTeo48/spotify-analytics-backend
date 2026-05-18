from pydantic import BaseModel 

class Artist(BaseModel):
    artist: str 
    streams: int 

class Track(BaseModel):
    track: str 
    artist: str 
    streams: int 

class Genre(BaseModel):
    genre: str
    hours_listened: int 

class ListeningSummary(BaseModel):
    total_hours: int 
    favorite_artist: str 
    favorite_genre: str 
    total_tracks_streamed: int 