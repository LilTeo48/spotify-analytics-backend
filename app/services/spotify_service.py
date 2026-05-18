from app.database.db import fake_artists, fake_tracks, fake_genres, fake_summary

def get_top_artists_data():
    return {"top_artists": fake_artists}

def get_top_tracks_data():
    return {"top_tracks": fake_tracks}

def get_top_genres_data():
    return {"top_genres": fake_genres}

def get_listening_summary_data(): 
    return fake_summary   