from fastapi import APIRouter
from app.models.schemas import Artist
from app.services.spotify_service import (
    get_top_artists_data,
    get_top_tracks_data,
    get_top_genres_data,
    get_listening_summary_data,
    add_top_artist_data,
    delete_top_artist_data
)

router = APIRouter()


@router.get("/top-artists")
def get_top_artists():
    return get_top_artists_data()


@router.post("/top-artists")
def add_top_artist(artist: Artist):
    return add_top_artist_data(artist)


@router.delete("/top-artists/{artist_name}")
def delete_top_artist(artist_name: str):
    return delete_top_artist_data(artist_name)


@router.get("/top-tracks")
def get_top_tracks():
    return get_top_tracks_data()


@router.get("/top-genres")
def get_top_genres():
    return get_top_genres_data()


@router.get("/listening-summary")
def get_listening_summary():
    return get_listening_summary_data()