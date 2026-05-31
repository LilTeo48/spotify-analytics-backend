from app.database.db import SessionLocal
from app.models.db_models import ArtistDB, TrackDB, GenreDB
from app.database.db import fake_summary


def get_top_artists_data():
    db = SessionLocal()

    try:
        artists = db.query(ArtistDB).all()

        result = [
            {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
            for artist in artists
        ]

        return {"top_artists": result}

    finally:
        db.close()


def get_top_tracks_data():
    db = SessionLocal()

    try:
        tracks = db.query(TrackDB).all()

        result = [
            {
            "id": track.id,
            "track": track.track,
            "artist": track.artist,
            "streams": track.streams
            }
            for track in tracks
        ]

        return {"top_tracks": result}
    finally:
        db.close()    


def get_top_genres_data():
    db = SessionLocal()

    try:
        genres = db.query(GenreDB).all()

        result = [
            {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
            for genre in genres
        ]

        return {"top_genres": result}

    finally:
        db.close()


def get_listening_summary_data():
    db = SessionLocal()

    try:
        artists = db.query(ArtistDB).all()
        tracks = db.query(TrackDB).all()
        genres = db.query(GenreDB).all()

        total_streams = sum(artist.streams for artist in artists)
        total_tracks_streamed = sum(track.streams for track in tracks)

        favorite_artist = max(
            artists,
            key=lambda artist: artist.streams
        ).artist if artists else None

        favorite_genre = max(
            genres,
            key=lambda genre: genre.hours_listened
        ).genre if genres else None

        total_hours = sum(genre.hours_listened for genre in genres)

        return {
            "total_hours": total_hours,
            "favorite_artist": favorite_artist,
            "favorite_genre": favorite_genre,
            "total_tracks_streamed": total_tracks_streamed,
            "total_artist_streams": total_streams
        }

    finally:
        db.close()


def add_top_artist_data(artist):
    db = SessionLocal()

    try:
        new_artist = ArtistDB(
            artist=artist.artist,
            streams=artist.streams
        )

        db.add(new_artist)
        db.commit()
        db.refresh(new_artist)

        return {
            "message": "Artist added successfully",
            "artist": {
                "id": new_artist.id,
                "artist": new_artist.artist,
                "streams": new_artist.streams
            }
        }

    finally:
        db.close()


def delete_top_artist_data(artist_name: str):
    db = SessionLocal()

    try:
        artist = (
            db.query(ArtistDB)
            .filter(ArtistDB.artist.ilike(artist_name))
            .first()
        )

        if not artist:
            return {"message": "Artist not found"}

        db.delete(artist)
        db.commit()

        return {
            "message": "Artist deleted successfully"
        }

    finally:
        db.close()


def update_top_artist_data(artist_name: str, updated_artist):
    db = SessionLocal()

    try:
        artist = (
            db.query(ArtistDB)
            .filter(ArtistDB.artist.ilike(artist_name))
            .first()
        )

        if not artist:
            return {"message": "Artist not found"}

        artist.artist = updated_artist.artist
        artist.streams = updated_artist.streams

        db.commit()
        db.refresh(artist)

        return {
            "message": "Artist updated successfully",
            "artist": {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
        }

    finally:
        db.close()