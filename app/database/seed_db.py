from app.database.db import SessionLocal
from app.models.db_models import ArtistDB, TrackDB, GenreDB

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


def seed_db():
    db = SessionLocal()

    try:
        db.query(ArtistDB).delete()
        db.query(TrackDB).delete()
        db.query(GenreDB).delete()

        for artist in seed_artists:
            new_artist = ArtistDB(
                artist=artist["artist"],
                streams=artist["streams"]
            )
            db.add(new_artist)

        for track in seed_tracks:
            new_track = TrackDB(
                track=track["track"],
                artist=track["artist"],
                streams=track["streams"]
            )
            db.add(new_track)

        for genre in seed_genres:
            new_genre = GenreDB(
                genre=genre["genre"],
                hours_listened=genre["hours_listened"]
            )
            db.add(new_genre)

        db.commit()
        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_db()