from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Spotify Analytics Backend is running"
    }


@app.get("/top-artists")
def get_top_artists():
    return {
        "top_artists": [
            {
                "artist": "Drake",
                "streams": 1250
            },
            {
                "artist": "Kendrick Lamar",
                "streams": 980
            },
            {
                "artist": "J. Cole",
                "streams": 875
            }
        ]
    }


@app.get("/top-tracks")
def get_top_tracks():
    return {
        "top_tracks": [
            {
                "track": "HUMBLE.",
                "artist": "Kendrick Lamar",
                "streams": 420
            },
            {
                "track": "Work Out",
                "artist": "J. Cole",
                "streams": 390
            },
            {
                "track": "God's Plan",
                "artist": "Drake",
                "streams": 510
            }
        ]
    }


@app.get("/top-genres")
def get_top_genres():
    return {
        "top_genres": [
            {
                "genre": "Hip-Hop",
                "hours_listened": 145
            },
            {
                "genre": "R&B",
                "hours_listened": 72
            },
            {
                "genre": "Pop",
                "hours_listened": 40
            }
        ]
    }
 
@app.get("/listening-summary")
def get_listening_summary():
    return {
        "total_hours": 257,
        "favorite_artist": "Drake",
        "favorite_genre": "Hip-Hop",
        "total_tracks_streamed": 1240
    }   