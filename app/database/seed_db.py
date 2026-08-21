from app.database.db import SessionLocal
from app.models.db_models import ArtistDB, TrackDB, GenreDB, PodcastDB

seed_artists = [
    {"artist": "Drake", "streams": 1250},
    {"artist": "Kendrick Lamar", "streams": 980},
    {"artist": "J. Cole", "streams": 875},
    {"artist": "Future", "streams": 1500},
    {"artist": "The Weeknd", "streams": 1320},
]

seed_tracks = [
    {"track": "HUMBLE.", "artist": "Kendrick Lamar", "streams": 420},
    {"track": "Work Out", "artist": "J. Cole", "streams": 390},
    {"track": "God's Plan", "artist": "Drake", "streams": 510},
    {"track": "Mask Off", "artist": "Future", "streams": 465},
    {"track": "Blinding Lights", "artist": "The Weeknd", "streams": 600},
]

seed_genres = [
    {"genre": "Hip-Hop", "hours_listened": 145},
    {"genre": "R&B", "hours_listened": 72},
    {"genre": "Pop", "hours_listened": 40},
]

seed_podcasts = [
    {
        "podcast_name": "The Joe Rogan Experience",
        "host": "Joe Rogan",
        "category": "Comedy",
        "episodes": 2325,
        "hours_listened": 42
    },
    {
        "podcast_name": "Lex Fridman Podcast",
        "host": "Lex Fridman",
        "category": "Technology",
        "episodes": 485,
        "hours_listened": 36
    },
    {
        "podcast_name": "Huberman Lab",
        "host": "Andrew Huberman",
        "category": "Health",
        "episodes": 230,
        "hours_listened": 28
    },
    {
        "podcast_name": "Darknet Diaries",
        "host": "Jack Rhysider",
        "category": "Cybersecurity",
        "episodes": 165,
        "hours_listened": 19
    },
    {
        "podcast_name": "Waveform",
        "host": "Marques Brownlee",
        "category": "Technology",
        "episodes": 270,
        "hours_listened": 15
    }
]


def seed_db():
    db = SessionLocal()

    try:
        # Clear existing data
        db.query(PodcastDB).delete()
        db.query(GenreDB).delete()
        db.query(TrackDB).delete()
        db.query(ArtistDB).delete()

        for artist in seed_artists:
            db.add(ArtistDB(**artist))

        for track in seed_tracks:
            db.add(TrackDB(**track))

        for genre in seed_genres:
            db.add(GenreDB(**genre))

        for podcast in seed_podcasts:
            db.add(PodcastDB(**podcast))

        db.commit()
        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_db()