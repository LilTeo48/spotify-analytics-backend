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
    search_genre_data,
    get_top_artist_analytics,
    get_top_track_analytics,
    get_top_genre_analytics,
    get_dashboard_analytics,
    get_counts_analytics,
    get_total_streams_analytics,
    get_total_hours_analytics,
    get_top_3_artists_analytics,
    get_top_3_tracks_analytics,
    get_top_3_genres_analytics,
    get_average_artist_streams_analytics,
    get_average_track_streams_analytics,
    get_average_genre_hours_analytics,
    get_least_streamed_artist_analytics,
    get_least_streamed_track_analytics,
    get_least_listened_genre_analytics,
    get_artist_stream_ranking_analytics,
    get_track_stream_ranking_analytics,
    get_genre_ranking_analytics,
)

router = APIRouter()


@router.get("/top-artists")
def get_top_artists(
    min_streams: int = 0,
    limit: int = 10
):
    return get_top_artists_data(min_streams, limit)

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
def get_top_tracks(
    artist: str = "",
    limit: int = 10
):
    return get_top_tracks_data(artist, limit)

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
def get_top_genres(
    min_hours: int = 0,
    limit: int = 10
):
    return get_top_genres_data(min_hours, limit)

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

@router.get("/analytics/top-artist")
def get_top_artist():
    return get_top_artist_analytics()

@router.get("/analytics/top-track")
def get_top_track():
    return get_top_track_analytics()


@router.get("/analytics/top-genre")
def get_top_genre():
    return get_top_genre_analytics()

@router.get("/analytics/dashboard")
def get_dashboard():
    return get_dashboard_analytics()

@router.get("/analytics/counts")
def get_counts():
    return get_counts_analytics()

@router.get("/analytics/total-streams")
def get_total_streams():
    return get_total_streams_analytics()

@router.get("/analytics/total-hours")
def get_total_hours():
    return get_total_hours_analytics()

@router.get("/analytics/top-3-artists")
def get_top_3_artists():
    return get_top_3_artists_analytics()


@router.get("/analytics/top-3-tracks")
def get_top_3_tracks():
    return get_top_3_tracks_analytics()


@router.get("/analytics/top-3-genres")
def get_top_3_genres():
    return get_top_3_genres_analytics()

@router.get("/analytics/average-artist-streams")
def get_average_artist_streams():
    return get_average_artist_streams_analytics()

@router.get("/analytics/average-track-streams")
def get_average_track_streams():
    return get_average_track_streams_analytics()

@router.get("/analytics/average-genre-hours")
def get_average_genre_hours():
    return get_average_genre_hours_analytics()

@router.get("/analytics/least-streamed-artist")
def get_least_streamed_artist():
    return get_least_streamed_artist_analytics()


@router.get("/analytics/least-streamed-track")
def get_least_streamed_track():
    return get_least_streamed_track_analytics()


@router.get("/analytics/least-listened-genre")
def get_least_listened_genre():
    return get_least_listened_genre_analytics()

@router.get("/analytics/artist-stream-ranking")
def get_artist_stream_ranking():
    return get_artist_stream_ranking_analytics()


@router.get("/analytics/track-stream-ranking")
def get_track_stream_ranking():
    return get_track_stream_ranking_analytics()


@router.get("/analytics/genre-ranking")
def get_genre_ranking():
    return get_genre_ranking_analytics()        