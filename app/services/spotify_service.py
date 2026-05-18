from app.database.db import fake_artists, fake_tracks, fake_genres, fake_summary

def get_top_artists_data():
    return {"top_artists": fake_artists}

def get_top_tracks_data():
    return {"top_tracks": fake_tracks}

def get_top_genres_data():
    return {"top_genres": fake_genres}

def get_listening_summary_data(): 
    return fake_summary   

def add_top_artist_data(artist):
    fake_artists.append({
        "artist": artist.artist,
        "streams": artist.streams
    })

    return {
        "message": "Artist added successfully",
        "artist": artist
    }

def delete_top_artist_data(artist_name: str):
    for artist in fake_artists:
        if artist["artist"].lower() == artist_name.lower():
            fake_artists.remove(artist)

            return {
                "message": "Artist deleted successfully",
                "artist": artist
            }

    return {
        "message": "Artist not found"
    }