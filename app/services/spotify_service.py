from app.database.db import SessionLocal
from app.models.db_models import ArtistDB, TrackDB, GenreDB


def get_top_artists_data(
    min_streams: int = 0,
    limit: int = 10,
    sort_order: str = "desc"
):
    db = SessionLocal()

    try:
        query = (
            db.query(ArtistDB)
            .filter(ArtistDB.streams >= min_streams)
        )
        if sort_order == "asc":
            query = query.order_by(
                ArtistDB.streams.asc()
            )
        else:
            query = query.order_by(
                ArtistDB.streams.desc()
            )
        artists = query.limit(limit).all()

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

def get_top_tracks_data(
    artist: str = "",
    limit: int = 10,
    sort_order: str = "desc"
):
    db = SessionLocal()

    try:
        query = db.query(TrackDB)

        if artist:
            query = query.filter(
                TrackDB.artist.ilike(f"%{artist}%")
            )
        if sort_order == "asc":
            query = query.order_by(TrackDB.streams.asc())
        else:
            query = query.order_by(TrackDB.streams.desc())

        tracks = query.limit(limit).all()

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

def get_top_genres_data(
    min_hours: int = 0,
    limit: int = 10,
    sort_order: str = "desc"
):
    db = SessionLocal()

    try:
        query = (
            db.query(GenreDB)
            .filter(
                GenreDB.hours_listened >= min_hours
            )
        )

        if sort_order == "asc":
            query = query.order_by(
                GenreDB.hours_listened.asc()
            )
        else:
            query = query.order_by(
                GenreDB.hours_listened.desc()
            )

        genres = query.limit(limit).all()

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

def add_top_track_data(track):
    db = SessionLocal()

    try:
        new_track = TrackDB(
            track=track.track,
            artist=track.artist,
            streams=track.streams
        )

        db.add(new_track)
        db.commit()
        db.refresh(new_track)

        return {
            "message": "Track added successfully",
            "track": {
                "id": new_track.id,
                "track": new_track.track,
                "artist": new_track.artist,
                "streams": new_track.streams
            }
        }

    finally:
        db.close()


def update_top_track_data(track_name: str, updated_track):
    db = SessionLocal()

    try:
        track = (
            db.query(TrackDB)
            .filter(TrackDB.track.ilike(track_name))
            .first()
        )

        if not track:
            return {"message": "Track not found"}

        track.track = updated_track.track
        track.artist = updated_track.artist
        track.streams = updated_track.streams

        db.commit()
        db.refresh(track)

        return {
            "message": "Track updated successfully",
            "track": {
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
        }

    finally:
        db.close()


def delete_top_track_data(track_name: str):
    db = SessionLocal()

    try:
        track = (
            db.query(TrackDB)
            .filter(TrackDB.track.ilike(track_name))
            .first()
        )

        if not track:
            return {"message": "Track not found"}

        db.delete(track)
        db.commit()

        return {
            "message": "Track deleted successfully"
        }

    finally:
        db.close()

def add_top_genre_data(genre):
    db = SessionLocal()

    try:
        new_genre = GenreDB(
            genre=genre.genre,
            hours_listened=genre.hours_listened
        )

        db.add(new_genre)
        db.commit()
        db.refresh(new_genre)

        return {
            "message": "Genre added successfully",
            "genre": {
                "id": new_genre.id,
                "genre": new_genre.genre,
                "hours_listened": new_genre.hours_listened
            }
        }

    finally:
        db.close()


def update_top_genre_data(genre_name: str, updated_genre):
    db = SessionLocal()

    try:
        genre = (
            db.query(GenreDB)
            .filter(GenreDB.genre.ilike(genre_name))
            .first()
        )

        if not genre:
            return {"message": "Genre not found"}

        genre.genre = updated_genre.genre
        genre.hours_listened = updated_genre.hours_listened

        db.commit()
        db.refresh(genre)

        return {
            "message": "Genre updated successfully",
            "genre": {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
        }

    finally:
        db.close()


def delete_top_genre_data(genre_name: str):
    db = SessionLocal()

    try:
        genre = (
            db.query(GenreDB)
            .filter(GenreDB.genre.ilike(genre_name))
            .first()
        )

        if not genre:
            return {"message": "Genre not found"}

        db.delete(genre)
        db.commit()

        return {
            "message": "Genre deleted successfully"
        }

    finally:
        db.close() 

def search_artist_data(artist_name: str): 
    db = SessionLocal()

    try:
        artists = (
            db.query(ArtistDB)
            .filter(ArtistDB.artist.ilike(f"%{artist_name}%"))
            .all()
        )

        result = [
            {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
            for artist in artists
        ]

        return {"results": result}

    finally: 
        db.close()


def search_track_data(track_name: str): 
    db = SessionLocal()

    try: 
        tracks = (
            db.query(TrackDB)
            .filter(TrackDB.track.ilike(f"%{track_name}%"))
            .all()
        )

        result = [
            {
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
            for track in tracks
        ]

        return {"results": result}

    finally:
        db.close()

def search_genre_data(genre_name: str): 
    db = SessionLocal()

    try: 
        genres = (
            db.query(GenreDB)
            .filter(GenreDB.genre.ilike(f"%{genre_name}%"))
            .all()
        )

        result = [
            {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
            for genre in genres
        ]

        return {"results": result}
    finally:
        db.close()

def get_top_artist_analytics():
    db = SessionLocal()

    try:
        artist = (
            db.query(ArtistDB)
            .order_by(ArtistDB.streams.desc())
            .first()
        )

        if not artist:
            return {"message": "No artists found"}

        return {
            "top_artist": {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
        }

    finally:
        db.close()


def get_top_track_analytics():
    db = SessionLocal()

    try:
        track = (
            db.query(TrackDB)
            .order_by(TrackDB.streams.desc())
            .first()
        )

        if not track:
            return {"message": "No tracks found"}

        return {
            "top_track": {
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
        }

    finally:
        db.close()


def get_top_genre_analytics():
    db = SessionLocal()

    try:
        genre = (
            db.query(GenreDB)
            .order_by(GenreDB.hours_listened.desc())
            .first()
        )

        if not genre:
            return {"message": "No genres found"}

        return {
            "top_genre": {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
        }

    finally:
        db.close()

def get_dashboard_analytics():
    db = SessionLocal()

    try:
        artists = db.query(ArtistDB).all()
        tracks = db.query(TrackDB).all()
        genres = db.query(GenreDB).all()

        return {
            "artist_count": len(artists),
            "track_count": len(tracks),
            "genre_count": len(genres),

            "total_artist_streams":
                sum(artist.streams for artist in artists),

            "total_track_streams":
                sum(track.streams for track in tracks),

            "total_hours_listened":
                sum(genre.hours_listened for genre in genres),

            "top_artist":
                max(
                    artists,
                    key=lambda artist: artist.streams
                ).artist if artists else None,

            "top_track":
                max(
                    tracks,
                    key=lambda track: track.streams
                ).track if tracks else None,

            "top_genre":
                max(
                    genres,
                    key=lambda genre: genre.hours_listened
                ).genre if genres else None
        }

    finally:
        db.close()

def get_counts_analytics():
    db = SessionLocal()

    try:
        return {
            "artist_count": db.query(ArtistDB).count(),
            "track_count": db.query(TrackDB).count(),
            "genre_count": db.query(GenreDB).count()
        }
    finally:
        db.close()

def get_total_streams_analytics():
    db = SessionLocal()

    try:
        artists = db.query(ArtistDB).all()
        tracks = db.query(TrackDB).all()

        return {
            "total_artist_streams": sum(artist.streams for artist in artists),
            "total_track_streams": sum(track.streams for track in tracks),
            "combined_streams": (
                sum(artist.streams for artist in artists)
                + sum(track.streams for track in tracks)
            )
        }
    finally:
        db.close()
def get_total_hours_analytics():
    db = SessionLocal()

    try:
        genres = db.query(GenreDB).all()

        return {
            "total_hours_listened": sum(genre.hours_listened for genre in genres)
        }

    finally:
        db.close()

def get_top_3_artists_analytics():
    db = SessionLocal()

    try:
        artists = (
            db.query(ArtistDB)
            .order_by(ArtistDB.streams.desc())
            .limit(3)
            .all()
        )

        result = [
            {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
            for artist in artists
        ]

        return {"top_3_artists": result}
    finally:
        db.close()

def get_top_3_tracks_analytics():
    db = SessionLocal()

    try:
        tracks = (
            db.query(TrackDB)
            .order_by(TrackDB.streams.desc())
            .limit(3)
            .all()
        )

        result = [
            {
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
            for track in tracks
        ]

        return {"top_3_tracks": result}

    finally:
        db.close()

def get_top_3_genres_analytics():
    db = SessionLocal()

    try:
        genres = (
            db.query(GenreDB)
            .order_by(GenreDB.hours_listened.desc())
            .limit(3)
            .all()
        )

        result = [
            {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
            for genre in genres
        ]
        return {"top_3_genres": result}
    finally:
        db.close()

def get_average_artist_streams_analytics():
    db = SessionLocal()

    try:
        artists = db.query(ArtistDB).all()

        if not artists:
            return {"message": "No artists found"}

        average = (
            sum(artist.streams for artist in artists)
            / len(artists)
        )

        return {
            "average_artist_streams": round(average, 2)
        }

    finally:
        db.close()


def get_average_track_streams_analytics():
    db = SessionLocal()

    try:
        tracks = db.query(TrackDB).all()

        if not tracks:
            return {"message": "No tracks found"}

        average = (
            sum(track.streams for track in tracks)
            / len(tracks)
        )

        return {
            "average_track_streams": round(average, 2)
        }

    finally:
        db.close()


def get_average_genre_hours_analytics():
    db = SessionLocal()

    try:
        genres = db.query(GenreDB).all()

        if not genres:
            return {"message": "No genres found"}

        average = (
            sum(genre.hours_listened for genre in genres)
            / len(genres)
        )

        return {
            "average_genre_hours": round(average, 2)
        }

    finally:
        db.close()        
        
def get_least_streamed_artist_analytics():
    db = SessionLocal()

    try:
        artist = (
            db.query(ArtistDB)
            .order_by(ArtistDB.streams.asc())
            .first()
        )

        if not artist:
            return {"message": "No artists found"}

        return {
            "least_streamed_artist": {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
        }
    finally:
        db.close()

def get_least_streamed_track_analytics():
    db = SessionLocal()

    try:
        track = (
            db.query(TrackDB)
            .order_by(TrackDB.streams.asc())
            .first()
        )

        if not track:
            return{"message": "No tracks found"}

        return {
            "least_streamed_track": {
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
        }
    finally:
        db.close()

def get_least_listened_genre_analytics():
    db = SessionLocal()

    try:
        genre = (
        db.query(GenreDB)
        .order_by(GenreDB.hours_listened.asc())
        .first()
        )
        if not genre:
            return {"message": "No genres found"}

        return {
            "least_listened_genre": {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
        }

    finally:
        db.close()

def get_artist_stream_ranking_analytics():
    db = SessionLocal()

    try:
        artists = (
            db.query(ArtistDB)
            .order_by(ArtistDB.streams.desc())
            .all()
        )

        result = [
            {
                "rank": index + 1,
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
            for index, artist in enumerate(artists)
        ]

        return {"artist_stream_ranking": result}

    finally:
        db.close()


def get_track_stream_ranking_analytics():
    db = SessionLocal()

    try:
        tracks = (
            db.query(TrackDB)
            .order_by(TrackDB.streams.desc())
            .all()
        )

        result = [
            {
                "rank": index + 1,
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
            for index, track in enumerate(tracks)
        ]

        return {"track_stream_ranking": result}

    finally:
        db.close()


def get_genre_ranking_analytics():
    db = SessionLocal()

    try:
        genres = (
            db.query(GenreDB)
            .order_by(GenreDB.hours_listened.desc())
            .all()
        )

        result = [
            {
                "rank": index + 1,
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
            for index, genre in enumerate(genres)
        ]

        return {"genre_ranking": result}

    finally:
        db.close() 

def search_artists_data(q: str = ""):
    db = SessionLocal()


    try:
        artists = (
            db.query(ArtistDB)
            .filter(
                ArtistDB.artist.ilike(f"%{q}%")
            )
            .all()
        )

        result = [
            {
                "id": artist.id,
                "artist": artist.artist,
                "streams": artist.streams
            }
            for artist in artists
        ]
        return {"artists": result}
    finally:
        db.close()

def search_tracks_data(q: str = ""):
    db = SessionLocal()

    try: 
        tracks = (
            db.query(TrackDB)
            .filter(
                TrackDB.track.ilike(f"%{q}%")
            )
            .all()
        )

        result = [
            {
                "id": track.id,
                "track": track.track,
                "artist": track.artist,
                "streams": track.streams
            }
            for track in tracks
        ]

        return {"tracks": result}

    finally:
        db.close()

def search_genres_data(q: str = ""):
    db = SessionLocal()

    try:
        genres = (
            db.query(GenreDB)
            .filter(
                GenreDB.genre.ilike(f"%{q}%")
            )
            .all()
        )

        result = [
            {
                "id": genre.id,
                "genre": genre.genre,
                "hours_listened": genre.hours_listened
            }
            for genre in genres
        ]
        return {"genres": result}
    finally:
        db.close()    

        

