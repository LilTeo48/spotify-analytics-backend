from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_dashboard_endpoint():
    response = client.get("/analytics/dashboard")

    assert response.status_code == 200

    data = response.json()

    assert "artist_count" in data
    assert "track_count" in data
    assert "genre_count" in data


def test_artist_search_endpoint():
    response = client.get("/search/artists?q=dr")

    assert response.status_code == 200

    data = response.json()

    assert "artists" in data
    assert isinstance(data["artists"], list)


def test_track_search_endpoint():
    response = client.get("/search/tracks?q=plan")

    assert response.status_code == 200

    data = response.json()

    assert "tracks" in data
    assert isinstance(data["tracks"], list)


def test_genre_search_endpoint():
    response = client.get("/search/genres?q=hip")

    assert response.status_code == 200

    data = response.json()

    assert "genres" in data
    assert isinstance(data["genres"], list)

def test_top_artists_endpoint():
    response = client.get("/top-artists")

    assert response.status_code == 200

    data = response.json()

    assert "top_artists" in data
    assert isinstance(data["top_artists"], list)


def test_top_tracks_endpoint():
    response = client.get("/top-tracks")

    assert response.status_code == 200

    data = response.json()

    assert "top_tracks" in data
    assert isinstance(data["top_tracks"], list)


def test_top_genres_endpoint():
    response = client.get("/top-genres")

    assert response.status_code == 200

    data = response.json()

    assert "top_genres" in data
    assert isinstance(data["top_genres"], list)


def test_top_artists_filter_sort_limit():
    response = client.get("/top-artists?min_streams=1000&limit=2&sort_order=desc")

    assert response.status_code == 200

    data = response.json()

    assert "top_artists" in data
    assert len(data["top_artists"]) <= 2


def test_top_tracks_filter_sort_limit():
    response = client.get("/top-tracks?artist=Future&limit=2&sort_order=desc")

    assert response.status_code == 200

    data = response.json()

    assert "top_tracks" in data
    assert isinstance(data["top_tracks"], list)


def test_top_genres_filter_sort_limit():
    response = client.get("/top-genres?min_hours=50&limit=2&sort_order=desc")

    assert response.status_code == 200

    data = response.json()

    assert "top_genres" in data
    assert len(data["top_genres"]) <= 2  

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"


def test_database_health_endpoint():
    response = client.get("/health/database")

    assert response.status_code == 200

    data = response.json()

    assert "status" in data

def test_get_podcasts_endpoint():
    response = client.get("/podcasts")

    assert response.status_code == 200


def test_search_podcasts_endpoint():
    response = client.get("/search/podcasts?q=pard")

    assert response.status_code == 200

    data = response.json()

    assert "podcasts" in data
    assert isinstance(data["podcasts"], list)

def test_update_missing_artist_returns_404():
    response = client.put(
        "/top-artists/definitely-not-real",
        json={
            "artist": "Updated Artist",
            "streams": 1000
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Artist not found"


def test_delete_missing_artist_returns_404():
    response = client.delete(
        "/top-artists/definitely-not-real"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Artist not found"


def test_update_missing_track_returns_404():
    response = client.put(
        "/top-tracks/definitely-not-real",
        json={
            "track": "Updated Track",
            "artist": "Updated Artist",
            "streams": 1000
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Track not found"


def test_delete_missing_track_returns_404():
    response = client.delete(
        "/top-tracks/definitely-not-real"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Track not found"


def test_update_missing_genre_returns_404():
    response = client.put(
        "/top-genres/definitely-not-real",
        json={
            "genre": "Updated Genre",
            "hours_listened": 100
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Genre not found"


def test_delete_missing_genre_returns_404():
    response = client.delete(
        "/top-genres/definitely-not-real"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Genre not found"


def test_update_missing_podcast_returns_404():
    response = client.put(
        "/podcasts/definitely-not-real",
        json={
            "podcast_name": "Updated Podcast",
            "host": "Updated Host",
            "category": "Technology",
            "episodes": 10,
            "hours_listened": 20
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Podcast not found"


def test_delete_missing_podcast_returns_404():
    response = client.delete(
        "/podcasts/definitely-not-real"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Podcast not found"

def test_top_podcasts_endpoint():
    response = client.get("/podcasts/top")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for podcast in data:
        assert "podcast_name" in podcast
        assert "host" in podcast
        assert "category" in podcast
        assert "episodes" in podcast
        assert "hours_listened" in podcast

def test_top_artists_rejects_negative_min_streams():
    response = client.get("/top-artists?min_streams=-1")

    assert response.status_code == 422


def test_top_artists_rejects_zero_limit():
    response = client.get("/top-artists?limit=0")

    assert response.status_code == 422


def test_top_tracks_rejects_invalid_sort_order():
    response = client.get("/top-tracks?sort_order=sideways")

    assert response.status_code == 422


def test_top_genres_rejects_negative_min_hours():
    response = client.get("/top-genres?min_hours=-1")

    assert response.status_code == 422


def test_top_genres_rejects_limit_over_100():
    response = client.get("/top-genres?limit=101")

    assert response.status_code == 422

def test_artist_crud_lifecycle():
    artist_name = f"pytest-artist-{uuid4()}"

    create_response = client.post(
        "/top-artists",
        json={
            "artist": artist_name,
            "streams": 500
        }
    )

    assert create_response.status_code == 200
    assert create_response.json()["message"] == "Artist added successfully"

    updated_name = f"{artist_name}-updated"

    update_response = client.put(
        f"/top-artists/{artist_name}",
        json={
            "artist": updated_name,
            "streams": 1000
        }
    )

    assert update_response.status_code == 200

    updated_data = update_response.json()

    assert updated_data["artist"]["artist"] == updated_name
    assert updated_data["artist"]["streams"] == 1000

    delete_response = client.delete(
        f"/top-artists/{updated_name}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Artist deleted successfully"


def test_track_crud_lifecycle():
    track_name = f"pytest-track-{uuid4()}"

    create_response = client.post(
        "/top-tracks",
        json={
            "track": track_name,
            "artist": "Pytest Artist",
            "streams": 500
        }
    )

    assert create_response.status_code == 200
    assert create_response.json()["message"] == "Track added successfully"

    updated_name = f"{track_name}-updated"

    update_response = client.put(
        f"/top-tracks/{track_name}",
        json={
            "track": updated_name,
            "artist": "Updated Pytest Artist",
            "streams": 1000
        }
    )

    assert update_response.status_code == 200

    updated_data = update_response.json()

    assert updated_data["track"]["track"] == updated_name
    assert updated_data["track"]["streams"] == 1000

    delete_response = client.delete(
        f"/top-tracks/{updated_name}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Track deleted successfully"


def test_genre_crud_lifecycle():
    genre_name = f"pytest-genre-{uuid4()}"

    create_response = client.post(
        "/top-genres",
        json={
            "genre": genre_name,
            "hours_listened": 25
        }
    )

    assert create_response.status_code == 200
    assert create_response.json()["message"] == "Genre added successfully"

    updated_name = f"{genre_name}-updated"

    update_response = client.put(
        f"/top-genres/{genre_name}",
        json={
            "genre": updated_name,
            "hours_listened": 50
        }
    )

    assert update_response.status_code == 200

    updated_data = update_response.json()

    assert updated_data["genre"]["genre"] == updated_name
    assert updated_data["genre"]["hours_listened"] == 50

    delete_response = client.delete(
        f"/top-genres/{updated_name}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Genre deleted successfully"


def test_podcast_crud_lifecycle():
    podcast_name = f"pytest-podcast-{uuid4()}"

    create_response = client.post(
        "/podcasts",
        json={
            "podcast_name": podcast_name,
            "host": "Pytest Host",
            "category": "Technology",
            "episodes": 10,
            "hours_listened": 20
        }
    )

    assert create_response.status_code == 200
    assert create_response.json()["message"] == "Podcast added successfully"

    update_response = client.put(
        f"/podcasts/{podcast_name}",
        json={
            "podcast_name": podcast_name,
            "host": "Updated Pytest Host",
            "category": "Technology",
            "episodes": 20,
            "hours_listened": 40
        }
    )

    assert update_response.status_code == 200

    delete_response = client.delete(
        f"/podcasts/{podcast_name}"
    )

    assert delete_response.status_code == 200

def test_counts_analytics_endpoint():
    response = client.get("/analytics/counts")

    assert response.status_code == 200

    data = response.json()

    assert "artist_count" in data
    assert "track_count" in data
    assert "genre_count" in data


def test_total_streams_analytics_endpoint():
    response = client.get("/analytics/total-streams")

    assert response.status_code == 200

    data = response.json()

    assert "total_artist_streams" in data
    assert "total_track_streams" in data
    assert "combined_streams" in data


def test_total_hours_analytics_endpoint():
    response = client.get("/analytics/total-hours")

    assert response.status_code == 200

    data = response.json()

    assert "total_hours_listened" in data


def test_database_summary_endpoint():
    response = client.get("/analytics/database-summary")

    assert response.status_code == 200

    data = response.json()

    assert "artist_count" in data
    assert "track_count" in data
    assert "genre_count" in data
    assert "podcast_count" in data


def test_artist_ranking_endpoint():
    response = client.get("/analytics/artist-stream-ranking")

    assert response.status_code == 200

    data = response.json()

    assert "artist_stream_ranking" in data
    assert isinstance(data["artist_stream_ranking"], list)


def test_track_ranking_endpoint():
    response = client.get("/analytics/track-stream-ranking")

    assert response.status_code == 200

    data = response.json()

    assert "track_stream_ranking" in data
    assert isinstance(data["track_stream_ranking"], list)                               