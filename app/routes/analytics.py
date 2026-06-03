from fastapi import APIRouter
from app.models.schemas import Artist, Track, Genre
from app.services.spotify_service import (
    get_top_artists_data,
    get_top_tracks_data,
    get_top_genres_data,
    get_listening_summary_data,
    add_top_artist_data,
    delete_top_artist_data,
    update_top_artist_data,
    add_top_track_data,
    update_top_track_data,
    delete_top_track_data,
    add_top_genre_data,
    update_top_genre_data,
    delete_top_genre_data,
    search_artist_data,
    search_track_data,
    search_genre_data

)

router = APIRouter()


@router.get("/top-artists")
def get_top_artists():
    return get_top_artists_data()


@router.post("/top-artists")
def add_top_artist(artist: Artist):
    return add_top_artist_data(artist)


@router.put("/top-artists/{artist_name}")
def update_top_artist(artist_name: str, updated_artist: Artist):
    return update_top_artist_data(artist_name, updated_artist)


@router.delete("/top-artists/{artist_name}")
def delete_top_artist(artist_name: str):
    return delete_top_artist_data(artist_name)


@router.get("/top-tracks")
def get_top_tracks():
    return get_top_tracks_data()


@router.post("/top-tracks")
def add_top_track(track: Track):
    return add_top_track_data(track)


@router.put("/top-tracks/{track_name}")
def update_top_track(track_name: str, updated_track: Track):
    return update_top_track_data(track_name, updated_track)


@router.delete("/top-tracks/{track_name}")
def delete_top_track(track_name: str):
    return delete_top_track_data(track_name)


@router.get("/top-genres")
def get_top_genres():
    return get_top_genres_data()

@router.post("/top-genres")
def add_top_genre(genre: Genre):
    return add_top_genre_data(genre)


@router.put("/top-genres/{genre_name}")
def update_top_genre(genre_name: str, updated_genre: Genre):
    return update_top_genre_data(genre_name, updated_genre)


@router.delete("/top-genres/{genre_name}")
def delete_top_genre(genre_name: str):
    return delete_top_genre_data(genre_name)


@router.get("/listening-summary")
def get_listening_summary():
    return get_listening_summary_data()

@router.get("/top-artists/search/{artist_name}")
def search_artist(artist_name: str):
    return search_artist_data(artist_name)

@router.get("/top-tracks/search/{track_name}")
def search_track(track_name: str):
    return search_track_data(track_name)

@router.get("/top-genres/search/{genre_name}")
def search_genre(genre_name: str): 
    return search_genre_data(genre_name)